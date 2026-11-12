"""Read MCP server (kb-mcp-read): kb_search + kb_get_document, nothing else.

Generated from the read operations in kb.api.operations; build_server refuses
any operation not tagged mcp-read, so a write tool cannot be added here by
editing this allowlist alone (enforced again by tests/test_plane_separation.py).
"""
from __future__ import annotations

from mcp.server.mcpserver import MCPServer

from .. import config
from ..api.operations import Services
from ..services.search import KnowledgeSearch, format_hits, format_page, missing_document
from .factory import ToolBinding, build_server

SERVER_NAME = "kb-mcp-read"

INSTRUCTIONS = (
    "Read-only knowledge-tree retrieval over Qdrant collection "
    f"{config.QDRANT_COLLECTION}. Use kb_search to find citeable chunks; "
    "each hit is one slice of a larger document. Use kb_get_document with "
    "a hit's path to read that whole document (e.g. a full video transcript)."
)

READ_TOOLS = (
    ToolBinding("kb_search", render=lambda hits, _req: format_hits(hits)),
    ToolBinding(
        "kb_get_document",
        render=lambda page, req: format_page(page) if page else missing_document(req.path),
    ),
)

_services = Services()

mcp = build_server(SERVER_NAME, INSTRUCTIONS, READ_TOOLS, lambda: _services, tag="mcp-read")


def create_server(search: KnowledgeSearch | None = None) -> MCPServer:
    """Return the read server; optionally inject a search service (tests)."""
    global _services
    if search is not None:
        _services = Services(search=search)
    return mcp
