"""Service: embed query → ANN search → citation-friendly text."""
from __future__ import annotations

from .. import config, embed
from .store import QdrantChunkStore, SearchHit


class KnowledgeSearch:
    """Read-only knowledge search (no writes)."""

    def __init__(self, store: QdrantChunkStore | None = None) -> None:
        self._store = store or QdrantChunkStore()

    def search(self, query: str, k: int | None = None) -> list[SearchHit]:
        question = query.strip()
        if not question:
            raise ValueError("query must be a non-empty string")
        limit = _clamp_k(k)
        vector = embed.embed_query(question)
        return self._store.search(vector, limit)

    def search_formatted(self, query: str, k: int | None = None) -> str:
        hits = self.search(query, k)
        return format_hits(hits)


def _clamp_k(k: int | None) -> int:
    if k is None:
        return config.KB_SEARCH_DEFAULT_K
    if k < 1:
        raise ValueError("k must be >= 1")
    return min(k, config.KB_SEARCH_MAX_K)


def format_hits(hits: list[SearchHit]) -> str:
    if not hits:
        return "No results."
    blocks = []
    for hit in hits:
        tags = ",".join(hit.tags)
        blocks.append(
            f'<chunk path="{hit.path}" heading="{hit.heading}" '
            f'score="{hit.score:.4f}" tags="{tags}">\n'
            f"{hit.text.strip()}\n"
            f"</chunk>"
        )
    return "\n\n".join(blocks)
