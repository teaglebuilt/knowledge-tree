"""Repository: read-only ANN search against Qdrant."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .. import config
from ..adapters import qdrant


@dataclass(frozen=True)
class SearchHit:
    score: float
    path: str
    heading: str
    tags: list[str]
    text: str
    chunk_id: str


class QdrantChunkStore:
    """Thin wrapper around Qdrant query_points (unnamed default vector)."""

    def __init__(self, client: Any | None = None) -> None:
        self._client = client or qdrant.client()
        qdrant.assert_collection_compatible(
            self._client, config.QDRANT_COLLECTION, config.EMBED_DIM
        )

    def search(self, vector: list[float], limit: int) -> list[SearchHit]:
        response = self._client.query_points(
            collection_name=config.QDRANT_COLLECTION,
            query=vector,
            limit=limit,
            with_payload=True,
        )
        return [_to_hit(point) for point in response.points]


def _to_hit(point: Any) -> SearchHit:
    payload = point.payload or {}
    tags = payload.get("tags") or []
    if not isinstance(tags, list):
        tags = [str(tags)]
    return SearchHit(
        score=float(point.score or 0.0),
        path=str(payload.get("path") or ""),
        heading=str(payload.get("heading") or ""),
        tags=[str(t) for t in tags],
        text=str(payload.get("text") or ""),
        chunk_id=str(payload.get("chunk_id") or ""),
    )
