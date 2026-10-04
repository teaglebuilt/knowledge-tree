"""Local embeddings via fastembed (no API, offline)."""
from __future__ import annotations

from functools import lru_cache

from . import config


@lru_cache(maxsize=1)
def _model():
    from fastembed import TextEmbedding

    return TextEmbedding(model_name=config.EMBED_MODEL)


def embed(texts: list[str]) -> list[list[float]]:
    if not texts:
        return []
    return [v.tolist() for v in _model().embed(texts)]


def embed_query(text: str) -> list[float]:
    """Query-space embedding (FastEmbed query_embed, not passage embed)."""
    vector = next(_model().query_embed(text))
    return vector.tolist()
