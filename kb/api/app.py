"""kb-api: FastAPI over the shared kb operations, plus the write MCP at /mcp.

/v1 routes are the documented contract (/openapi.json). The pre-rename
routes (/ingest, /exists, /delete) stay as hidden aliases with the same auth
until callers migrate; they never appear in OpenAPI and so can never be
generated into a tool. The write MCP (kb-mcp-write) is mounted last behind a
write-scope gate; delete is not one of its tools.
"""
from __future__ import annotations

import contextlib
import json
import logging
from typing import Annotated, Any

from fastapi import Depends, FastAPI, HTTPException, Query, Request
from fastapi.responses import JSONResponse
from pydantic import ValidationError
from starlette.concurrency import run_in_threadpool

from .. import config
from ..mcp import write as mcp_write
from ..services.ingest import KnowledgeIngest
from ..services.qdrant_store import SearchHit
from ..services.write_policy import PayloadTooLarge, PolicyError, WritePolicy
from . import schemas
from .operations import OPERATIONS, Services, run
from .security import ApiError, ScopeGate, error_response, require

log = logging.getLogger("kb.api")

API_VERSION = "1.0.0"

_ERRORS: dict[int | str, dict[str, Any]] = {
    status: {"model": schemas.ErrorResponse, "description": desc}
    for status, desc in {
        400: "Invalid request or write-policy violation",
        401: "Missing or invalid credentials",
        403: "Token lacks the required scope",
        503: "Qdrant or the embedder is unavailable",
    }.items()
}


def _route(op_id: str, **extra: Any) -> dict[str, Any]:
    op = OPERATIONS[op_id]
    responses = dict(_ERRORS) | extra.pop("responses", {})
    return {
        "operation_id": op.operation_id,
        "summary": op.summary,
        "description": op.description,
        "tags": [op.tag],
        "responses": responses,
        "dependencies": [Depends(require(op.scope))],  # type: ignore[arg-type]
        **extra,
    }


async def _call(op_id: str, svc: Services, req: Any, policy: WritePolicy | None = None) -> Any:
    try:
        return await run_in_threadpool(run, op_id, svc, req, policy)
    except PayloadTooLarge as exc:
        raise ApiError(413, "payload_too_large", str(exc)) from exc
    except PolicyError as exc:
        raise ApiError(400, "policy_violation", str(exc)) from exc
    except ValueError as exc:  # IngestError and the search argument checks
        raise ApiError(400, "invalid_request", str(exc)) from exc
    except Exception as exc:
        # Never echo backend errors: they can carry URLs and request details.
        log.exception("%s failed", op_id)
        raise ApiError(503, "backend_unavailable", "storage or embedding backend unavailable") from exc


def _hit(hit: SearchHit) -> schemas.SearchHitModel:
    return schemas.SearchHitModel(
        path=hit.path, heading=hit.heading, chunk_index=hit.chunk_index, score=hit.score,
        source_type=hit.source_type, source_url=hit.source_url, tags=hit.tags, text=hit.text,
    )


def _receipt(result_and_url) -> schemas.StoreDocumentReceipt:
    result, url = result_and_url
    return schemas.StoreDocumentReceipt(
        status=result.status, path=result.path, doc_hash=result.doc_hash,
        chunks=result.chunks, collection=config.QDRANT_COLLECTION, source_url=url,
    )


class _TooLarge(HTTPException):
    """HTTPException so FastAPI's body parser re-raises it instead of a 400."""

    def __init__(self) -> None:
        super().__init__(413, "body too large")


class BodyLimit:
    """Cap every request body (REST and /mcp), declared or chunked."""

    def __init__(self, app, limit: int) -> None:
        self.app = app
        self.limit = limit

    async def __call__(self, scope, receive, send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        too_large = error_response(
            413, "payload_too_large", f"body exceeds {self.limit} bytes"
        )
        length = dict(scope.get("headers") or []).get(b"content-length", b"")
        if length.isdigit() and int(length) > self.limit:
            await too_large(scope, receive, send)
            return
        received = 0
        started = False

        async def limited_receive():
            nonlocal received
            message = await receive()
            if message["type"] == "http.request":
                received += len(message.get("body", b""))
                if received > self.limit:
                    raise _TooLarge()
            return message

        async def tracking_send(message):
            nonlocal started
            if message["type"] == "http.response.start":
                started = True
            await send(message)

        try:
            await self.app(scope, limited_receive, tracking_send)
        except _TooLarge:
            if started:
                raise
            await too_large(scope, receive, send)


def _legacy(route: str, replacement: str) -> None:
    log.warning("deprecated route %s called; use %s", route, replacement)


async def _legacy_body(request: Request) -> dict:
    try:
        body = json.loads(await request.body())
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise ApiError(400, "invalid_request", f"body must be JSON: {exc}") from exc
    if not isinstance(body, dict):
        raise ApiError(400, "invalid_request", "body must be a JSON object")
    return body


def _legacy_model(model: type, **fields: Any) -> Any:
    try:
        return model(**fields)
    except ValidationError as exc:
        raise ApiError(400, "invalid_request", str(exc)) from exc


def create_app(
    ingest_service: KnowledgeIngest | None = None, *, services: Services | None = None
) -> FastAPI:
    svc = services or Services(ingest=ingest_service)
    mcp_server = mcp_write.create_server(svc)
    # Stateless + JSON: each tools/call stands alone, so replicas need no
    # sticky sessions. host=0.0.0.0 keeps the SDK from enabling localhost-only
    # DNS-rebinding checks, which would 421 every in-cluster Host header.
    mcp_app = mcp_server.streamable_http_app(
        stateless_http=True,
        json_response=True,
        host="0.0.0.0",
        max_request_body_size=config.KB_API_MAX_BODY_BYTES,
    )

    @contextlib.asynccontextmanager
    async def lifespan(app: FastAPI):
        # A mounted app's lifespan never runs; the MCP session manager must
        # be started by the outer app.
        async with mcp_server.session_manager.run():
            yield

    app = FastAPI(
        title="Knowledge Tree API",
        version=API_VERSION,
        description=(
            "Search, read and store knowledge-tree documents in Qdrant. Operation IDs "
            "match the MCP tool names; only mcp-read / mcp-write tagged operations are "
            "ever exposed as agent tools, and admin operations never are."
        ),
        lifespan=lifespan,
        redoc_url=None,
    )
    app.add_middleware(BodyLimit, limit=config.KB_API_MAX_BODY_BYTES)

    @app.exception_handler(ApiError)
    async def _api_error(_request: Request, exc: ApiError) -> JSONResponse:
        return error_response(exc.status, exc.code, exc.message)

    # --- probes (no auth, not in OpenAPI) ------------------------------------

    @app.get("/healthz", include_in_schema=False)
    async def healthz() -> dict:
        return {"status": "ok", "collection": config.QDRANT_COLLECTION}

    @app.get("/readyz", include_in_schema=False)
    async def readyz() -> JSONResponse:
        try:
            await run_in_threadpool(svc.ingest._prepare)
        except Exception:
            log.exception("readiness check failed")
            return JSONResponse({"status": "unready"}, status_code=503)
        return JSONResponse({"status": "ready"})

    # --- /v1 ------------------------------------------------------------------

    @app.post("/v1/search", **_route("kb_search"))
    async def search(req: schemas.SearchRequest) -> schemas.SearchResponse:
        hits = await _call("kb_search", svc, req)
        return schemas.SearchResponse(hits=[_hit(h) for h in hits])

    @app.get(
        "/v1/documents",
        **_route("kb_get_document", responses={404: {"model": schemas.ErrorResponse}}),
    )
    async def get_document(
        req: Annotated[schemas.DocumentPageRequest, Query()],
    ) -> schemas.DocumentPageResponse:
        page = await _call("kb_get_document", svc, req)
        if page is None:
            raise ApiError(404, "not_found", f'no document stored at path "{req.path}"')
        return schemas.DocumentPageResponse(
            path=page.path, title=page.title, source_type=page.source_type,
            source_url=page.source_url, total_chunks=page.total_chunks, offset=page.offset,
            returned_chunks=len(page.chunks), next_offset=page.next_offset, text=page.text,
        )

    @app.get("/v1/documents/status", **_route("kb_document_status"))
    async def document_status(
        req: Annotated[schemas.DocumentStatusRequest, Query()],
    ) -> schemas.DocumentStatus:
        return schemas.DocumentStatus(**await _call("kb_document_status", svc, req))

    @app.post(
        "/v1/documents",
        **_route("kb_store_document", responses={413: {"model": schemas.ErrorResponse}}),
    )
    async def store_document(req: schemas.StoreDocumentRequest) -> schemas.StoreDocumentReceipt:
        return _receipt(await _call("kb_store_document", svc, req))

    @app.delete("/v1/documents", **_route("kb_delete_document"))
    async def delete_document(
        req: Annotated[schemas.DocumentStatusRequest, Query()],
    ) -> schemas.DeleteDocumentResponse:
        removed = await _call("kb_delete_document", svc, req)
        return schemas.DeleteDocumentResponse(path=req.path, deleted_revisions=removed)

    # --- deprecated aliases (hidden; same scopes and policy) -----------------

    @app.post("/ingest", include_in_schema=False, dependencies=[Depends(require("write"))])
    async def legacy_ingest(request: Request) -> dict:
        _legacy("/ingest", "POST /v1/documents")
        body = await _legacy_body(request)
        req = _legacy_model(
            schemas.StoreDocumentRequest,
            path=body.get("path", ""),
            markdown=body.get("markdown", ""),
            source_type=body.get("source_type"),
            source_url=body.get("source_url"),
            force=bool(body.get("force", False)),
        )
        return _receipt(await _call("kb_store_document", svc, req)).model_dump(
            include={"path", "doc_hash", "chunks", "status", "collection"}
        )

    @app.get("/exists", include_in_schema=False, dependencies=[Depends(require("read"))])
    async def legacy_exists(path: str = "") -> dict:
        _legacy("/exists", "GET /v1/documents/status")
        req = _legacy_model(schemas.DocumentStatusRequest, path=path)
        return await _call("kb_document_status", svc, req)

    @app.post("/delete", include_in_schema=False, dependencies=[Depends(require("admin"))])
    async def legacy_delete(request: Request) -> dict:
        _legacy("/delete", "DELETE /v1/documents")
        body = await _legacy_body(request)
        req = _legacy_model(schemas.DocumentStatusRequest, path=body.get("path", ""))
        removed = await _call("kb_delete_document", svc, req)
        return {"path": req.path, "deleted_revisions": removed}

    # mcp_app serves /mcp; mounted last so every route above wins.
    app.mount("/", ScopeGate(mcp_app, "write"))
    return app


app = create_app()
