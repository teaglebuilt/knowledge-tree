"""Starlette app exposing the knowledge write plane over HTTP."""
from __future__ import annotations

import json
import os

from starlette.applications import Starlette
from starlette.concurrency import run_in_threadpool
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route

from .. import config
from .service import IngestError, KnowledgeIngest

#: Optional shared secret. Unset (the default) leaves the endpoint open to
#: anything that can reach the Service, which is the in-cluster posture today.
AUTH_TOKEN = os.environ.get("KB_INGEST_TOKEN", "your-doing-it-peter").strip()

_ingest: KnowledgeIngest | None = None


def service() -> KnowledgeIngest:
    global _ingest
    if _ingest is None:
        _ingest = KnowledgeIngest()
    return _ingest


def _authorized(request: Request) -> bool:
    if not AUTH_TOKEN:
        return True
    header = request.headers.get("authorization", "")
    scheme, _, token = header.partition(" ")
    return scheme.lower() == "bearer" and token == AUTH_TOKEN


async def healthz(request: Request) -> JSONResponse:
    return JSONResponse({"status": "ok", "collection": config.QDRANT_COLLECTION})


async def readyz(request: Request) -> JSONResponse:
    try:
        await run_in_threadpool(service()._prepare)
    except Exception as exc:
        return JSONResponse({"status": "unready", "error": str(exc)}, status_code=503)
    return JSONResponse({"status": "ready"})


async def _payload(request: Request) -> dict:
    try:
        body = await request.json()
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
    return Starlette(
        routes=[
            Route("/healthz", healthz, methods=["GET"]),
            Route("/readyz", readyz, methods=["GET"]),
            Route("/exists", exists, methods=["GET"]),
            Route("/ingest", ingest, methods=["POST"]),
            Route("/delete", delete, methods=["POST"]),
        ]
    )


app = create_app()
