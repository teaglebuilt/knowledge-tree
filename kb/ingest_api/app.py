"""Starlette app exposing the knowledge write plane over HTTP."""
from __future__ import annotations

import contextlib
import hmac
import json
import os

from starlette.applications import Starlette
from starlette.concurrency import run_in_threadpool
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route

from .. import config
from . import mcp_tools
from .service import IngestError, KnowledgeIngest

#: Shared bearer secret for every write (POST /ingest, /delete, /mcp).
#: Unset means writes are REFUSED unless KB_INGEST_ALLOW_ANONYMOUS=true —
#: private history must never land through an open door by omission.
AUTH_TOKEN = os.environ.get("KB_INGEST_TOKEN", "").strip()

_ingest: KnowledgeIngest | None = None


def service() -> KnowledgeIngest:
    global _ingest
    if _ingest is None:
        _ingest = KnowledgeIngest()
    return _ingest


#: Raw-token header for callers that can only copy a Secret value verbatim
#: (kagent RemoteMCPServer `headersFrom` cannot prepend "Bearer ").
TOKEN_HEADER = "x-kb-ingest-token"


def _token_ok(authorization: str, raw_token: str = "") -> bool:
    if not AUTH_TOKEN:
        return config.KB_INGEST_ALLOW_ANONYMOUS
    scheme, _, token = (authorization or "").partition(" ")
    if scheme.lower() != "bearer":
        token = raw_token
    token = (token or "").strip()
    return bool(token) and hmac.compare_digest(token.encode(), AUTH_TOKEN.encode())


def _authorized(request: Request) -> bool:
    return _token_ok(
        request.headers.get("authorization", ""), request.headers.get(TOKEN_HEADER, "")
    )


class BearerGate:
    """ASGI guard for the MCP sub-app (kagent sends the token via headersFrom)."""

    def __init__(self, app) -> None:
        self.app = app

    async def __call__(self, scope, receive, send) -> None:
        if scope["type"] == "http":
            headers = dict(scope.get("headers") or [])
            auth = headers.get(b"authorization", b"").decode("latin-1")
            raw = headers.get(TOKEN_HEADER.encode(), b"").decode("latin-1")
            if not _token_ok(auth, raw):
                await JSONResponse({"error": "unauthorized"}, status_code=401)(
                    scope, receive, send
                )
                return
            length = headers.get(b"content-length")
            if length and length.isdigit() and int(length) > config.KB_INGEST_MAX_BODY_BYTES:
                await JSONResponse({"error": "body too large"}, status_code=413)(
                    scope, receive, send
                )
                return
        await self.app(scope, receive, send)


async def healthz(request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok", "collection": config.QDRANT_COLLECTION})


async def readyz(request: Request) -> JSONResponse:
    try:
        await run_in_threadpool(service()._prepare)
    except Exception as exc:
        return JSONResponse({"status": "unready", "error": str(exc)}, status_code=503)
    return JSONResponse({"status": "ready"})


async def _payload(request: Request) -> dict:
    raw = await request.body()
    if len(raw) > config.KB_INGEST_MAX_BODY_BYTES:
        raise IngestError(f"body exceeds {config.KB_INGEST_MAX_BODY_BYTES} bytes")
    try:
        body = json.loads(raw)
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise IngestError(f"body must be JSON: {exc}") from exc
    if not isinstance(body, dict):
        raise IngestError("body must be a JSON object")
    return body


async def ingest(request: Request) -> JSONResponse:
    if not _authorized(request):
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    try:
        body = await _payload(request)
        result = await run_in_threadpool(
            service().ingest,
            body.get("path", ""),
            body.get("markdown", ""),
            source_type=body.get("source_type"),
            source_url=body.get("source_url"),
            force=bool(body.get("force", False)),
        )
    except IngestError as exc:
        return JSONResponse({"error": str(exc)}, status_code=400)
    return JSONResponse(
        {
            "path": result.path,
            "doc_hash": result.doc_hash,
            "chunks": result.chunks,
            "status": result.status,
            "collection": config.QDRANT_COLLECTION,
        }
    )


async def exists(request: Request) -> JSONResponse:
    try:
        result = await run_in_threadpool(
            service().exists, request.query_params.get("path", "")
        )
    except IngestError as exc:
        return JSONResponse({"error": str(exc)}, status_code=400)
    return JSONResponse(result)


async def delete(request: Request) -> JSONResponse:
    if not _authorized(request):
        return JSONResponse({"error": "unauthorized"}, status_code=401)
    try:
        body = await _payload(request)
        removed = await run_in_threadpool(service().delete, body.get("path", ""))
    except IngestError as exc:
        return JSONResponse({"error": str(exc)}, status_code=400)
    return JSONResponse({"path": body.get("path"), "deleted_revisions": removed})


def create_app(ingest_service: KnowledgeIngest | None = None) -> Starlette:
    global _ingest
    if ingest_service is not None:
        _ingest = ingest_service
    # Lazy: the MCP tools resolve the shared service on first call, so a test
    # that injects a service after import still gets it.
    mcp_tools.bind_service(_LazyService())

    # Stateless + JSON: each tools/call stands alone, so replicas need no
    # sticky sessions. host=0.0.0.0 keeps the SDK from enabling localhost-only
    # DNS-rebinding checks, which would 421 every in-cluster Host header.
    mcp_app = mcp_tools.mcp.streamable_http_app(
        stateless_http=True,
        json_response=True,
        host="0.0.0.0",
        max_request_body_size=config.KB_INGEST_MAX_BODY_BYTES,
    )

    @contextlib.asynccontextmanager
    async def lifespan(app):
        # A mounted app's lifespan never runs; the MCP session manager must
        # be started by the outer app.
        async with mcp_tools.mcp.session_manager.run():
            yield

    return Starlette(
        routes=[
            Route("/healthz", healthz, methods=["GET"]),
            Route("/readyz", readyz, methods=["GET"]),
            Route("/exists", exists, methods=["GET"]),
            Route("/ingest", ingest, methods=["POST"]),
            Route("/delete", delete, methods=["POST"]),
            # mcp_app serves /mcp; mounted last so the REST routes win.
            Mount("/", app=BearerGate(mcp_app)),
        ],
        lifespan=lifespan,
    )


class _LazyService:
    """Proxy so mcp_tools and the REST routes share one KnowledgeIngest."""

    def __getattr__(self, name):
        return getattr(service(), name)


app = create_app()
