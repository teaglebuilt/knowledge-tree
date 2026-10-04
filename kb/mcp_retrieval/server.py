"""MCP API layer: expose kb_search only (read-only)."""
from __future__ import annotations

import asyncio

from mcp.server.mcpserver import MCPServer

from .. import config
from .service import KnowledgeSearch

mcp = MCPServer(
    name="kb-retrieval",
    instructions=(
        "Read-only knowledge-tree retrieval over Qdrant collection "
        f"{config.QDRANT_COLLECTION}. Use kb_search to find citeable chunks."
    ),
)

_search: KnowledgeSearch | None = None


def _service() -> KnowledgeSearch:
    global _search
    if _search is None:
        _search = KnowledgeSearch()
    return _search


@mcp.tool()
async def kb_search(query: str, k: int = config.KB_SEARCH_DEFAULT_K) -> str:
    """Semantic search over the knowledge collection.

    Returns ranked chunks with path, heading, tags, score, and text for citations.
    """
    service = _service()
    return await asyncio.to_thread(service.search_formatted, query, k)


def create_server(search: KnowledgeSearch | None = None) -> MCPServer:
    """Build the MCP server; optionally inject a search service (tests)."""
    global _search
    if search is not None:
        _search = search
    return mcp
