"""Repository: read-only ANN search against Qdrant."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .. import config
from ..adapters import qdrant

SCROLL_PAGE = 256


@dataclass(frozen=True)
class SearchHit:
    score: float
    path: str
    heading: str
    tags: list[str]
    text: str
    chunk_id: str
    chunk_index: int = 0
    title: str = ""
    source_type: str = ""
    source_url: str = ""


class QdrantChunkStore:
    """Thin wrapper around Qdrant query_points (unnamed default vector)."""

    def __init__(self, client: Any | None = None) -> None:
        self._client = client or qdrant.client()
        qdrant.assert_collection_compatible(
            self._client, config.QDRANT_COLLECTION, config.EMBED_DIM
        )

    def search(
        self,
        vector: list[float],
        limit: int,
        *,
        path: str | None = None,
        source_type: str | None = None,
    ) -> list[SearchHit]:
        response = self._client.query_points(
            collection_name=config.QDRANT_COLLECTION,
            query=vector,
            limit=limit,
            query_filter=_filter(path=path, source_type=source_type),
            with_payload=True,
        )
        return [_to_hit(point) for point in response.points]

    def document(self, path: str) -> list[SearchHit]:
        """Every chunk stored for a path, in document order."""
        hits: list[SearchHit] = []
        offset = None
        while True:
            points, offset = self._client.scroll(
                collection_name=config.QDRANT_COLLECTION,
                scroll_filter=_filter(path=path),
                limit=SCROLL_PAGE,
                with_payload=True,
                with_vectors=False,
                offset=offset,
            )
            hits.extend(_to_hit(p) for p in points)
            if offset is None:
                break
        hits.sort(key=lambda h: h.chunk_index)
        return hits


def _filter(*, path: str | None = None, source_type: str | None = None):
    from qdrant_client import models

    must = [
        models.FieldCondition(key=key, match=models.MatchValue(value=value))
        for key, value in (("path", path), ("source_type", source_type))
        if value
    ]
    return models.Filter(must=must) if must else None


def _to_hit(point: Any) -> SearchHit:
    payload = point.payload or {}
    tags = payload.get("tags") or []
    if not isinstance(tags, list):
        tags = [str(tags)]
    return SearchHit(
        score=float(getattr(point, "score", None) or 0.0),
        path=str(payload.get("path") or ""),
        heading=str(payload.get("heading") or ""),
        tags=[str(t) for t in tags],
        text=str(payload.get("text") or ""),
        chunk_id=str(payload.get("chunk_id") or ""),
        chunk_index=_chunk_index(payload),
        title=str(payload.get("title") or ""),
        source_type=str(payload.get("source_type") or ""),
        source_url=str(payload.get("source_url") or ""),
    )


def _chunk_index(payload: dict) -> int:
    """`kb sync` points predate the chunk_index field; fall back to the id suffix."""
    value = payload.get("chunk_index")
    if value is None:
        value = str(payload.get("chunk_id") or "").rsplit("::", 1)[-1]
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0
