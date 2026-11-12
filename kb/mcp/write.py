"""Write MCP server (kb-mcp-write): `kb_store_document` + `kb_document_status`.

A separate MCPServer from read.py, mounted at /mcp by kb.api behind its token
gate, never served by the kb-mcp-read process. kb-mcp-read is bound by every
agent that reads the tree, and kagent's Claude harness ignores per-tool
allowlists, so a write tool there would be a write tool everywhere. Keeping
writes on their own server means "can write" is decided by which
RemoteMCPServer an AgentTemplate binds, not by a list the harness may ignore.

Tools run under the agent write policy (kb.services.write_policy.agent_policy):
own path prefix, closed source types, mandatory provenance, size cap.

Every store call returns a JSON receipt. The receipt is the completion signal
a delegating agent relays upward: `status` plus `doc_hash` is proof the
document is indexed, and `kb_document_status` (or kb-mcp-read's
`kb_get_document`) can re-verify it independently.
"""
from __future__ import annotations

import json

from mcp.server.mcpserver import MCPServer

from .. import config
from ..api import schemas
from ..api.operations import Services
from ..services.ingest import IngestError
from ..services.write_policy import agent_policy
from .factory import ToolBinding, build_server

SERVER_NAME = "kb-mcp-write"

INSTRUCTIONS = (
    "Write plane for the knowledge tree. kb_store_document stores ONE markdown "
    "document at a stable path under "
    f"{', '.join(config.KB_MCP_WRITE_PATH_PREFIXES)} and returns a JSON "
    "receipt; status 'ingested' or 'unchanged' means it is searchable via "
    "kb_search now. Re-sending identical content is a no-op, so retries "
    "are safe. Use kb_document_status to check a path before or after."
)


def _dumps(value: dict) -> str:
    return json.dumps(value, sort_keys=True)


def _receipt(result_and_url, _req) -> str:
    result, url = result_and_url
    return _dumps(
        schemas.StoreDocumentReceipt(
            status=result.status,
            path=result.path,
            doc_hash=result.doc_hash,
            chunks=result.chunks,
            collection=config.QDRANT_COLLECTION,
            source_url=url,
        ).model_dump()
    )


def _store_error(args: dict, exc: Exception) -> str:
    path = args.get("path")
    if isinstance(exc, IngestError):
        return _dumps({"status": "rejected", "path": path, "error": str(exc)})
    # Qdrant/embedding outage: retryable, not the caller's fault.
    return _dumps(
        {"status": "failed", "path": path, "error": f"{type(exc).__name__}: {exc}",
         "retryable": True}
    )


def _status_error(args: dict, exc: Exception) -> str:
    if isinstance(exc, IngestError):
        return _dumps({"path": args.get("path"), "exists": False, "error": str(exc)})
    raise exc


_STORE = dict(
    render=_receipt,
    input_model=schemas.AgentStoreDocumentRequest,
    policy=agent_policy,
    on_error=_store_error,
)
_STATUS = dict(render=lambda status, _req: _dumps(status), policy=agent_policy,
               on_error=_status_error)

WRITE_TOOLS = (
    ToolBinding("kb_store_document", **_STORE),
    ToolBinding("kb_document_status", **_STATUS),
)

#: Pre-rename names, same operations and policy, while agents migrate.
LEGACY_TOOLS = (
    ToolBinding("kb_store_document", name="kb_ingest", **_STORE,
                description="Deprecated alias of kb_store_document; use that instead."),
    ToolBinding("kb_document_status", name="kb_ingest_status", **_STATUS,
                description="Deprecated alias of kb_document_status; use that instead."),
)


def tools(legacy: bool | None = None) -> tuple[ToolBinding, ...]:
    enabled = config.KB_MCP_WRITE_LEGACY_TOOLS if legacy is None else legacy
    return WRITE_TOOLS + (LEGACY_TOOLS if enabled else ())


def create_server(services: Services | None = None, *, legacy: bool | None = None) -> MCPServer:
    """A fresh write server (each needs its own streamable-HTTP session manager)."""
    svc = services or Services()
    return build_server(SERVER_NAME, INSTRUCTIONS, tools(legacy), lambda: svc, tag="mcp-write")


#: Module-level instance for inventory checks; kb.api builds its own.
mcp = create_server()
