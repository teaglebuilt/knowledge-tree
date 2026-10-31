"""MCP API layer: read-only kb_search + kb_get_document."""
from __future__ import annotations

import asyncio

from mcp.server.mcpserver import MCPServer

from .. import config
from .service import KnowledgeSearch

mcp = MCPServer(
    name="kb-retrieval",
    instructions=(
        "Read-only knowledge-tree retrieval over Qdrant collection "
        f"{config.QDRANT_COLLECTION}. Use kb_search to find citeable chunks; "
        "each hit is one slice of a larger document. Use kb_get_document with "
        "a hit's path to read that whole document (e.g. a full video transcript)."
    ),
)

_search: KnowledgeSearch | None = None


def _service() -> KnowledgeSearch:
    global _search
    if _search is None:
        _search = KnowledgeSearch()
    return _search


@mcp.tool()
async def kb_search(
    query: str,
    k: int = config.KB_SEARCH_DEFAULT_K,
    path: str | None = None,
    source_type: str | None = None,
) -> str:
    """Semantic search over the knowledge collection.

    Returns the k most similar chunks (not whole documents) with path, heading,
    chunk_index, score, source_type, source_url, tags and text for citations.
    Set `path` to search inside one document, or `source_type` (e.g. "youtube",
    "tree") to restrict by origin.
    """
    service = _service()
    return await asyncio.to_thread(
        service.search_formatted, query, k, path=path, source_type=source_type
    )


@mcp.tool()
async def kb_get_document(
    path: str,
    offset: int = 0,
    limit: int = config.KB_DOCUMENT_PAGE_CHUNKS,
) -> str:
    """Read a whole stored document, in order, by its `path` from kb_search.

    Returns chunks `offset`..`offset+limit-1` stitched into continuous text.
    When the response carries `next_offset`, call again with that offset to
    read the rest.
    """
    service = _service()
    return await asyncio.to_thread(service.document_formatted, path, offset, limit)


def create_server(search: KnowledgeSearch | None = None) -> MCPServer:
    """Build the MCP server; optionally inject a search service (tests)."""
    global _search
    if search is not None:
        _search = search
    return mcp
