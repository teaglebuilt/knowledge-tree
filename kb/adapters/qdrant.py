"""Shared Qdrant client factory (sync + MCP read plane)."""
from __future__ import annotations

from urllib.parse import urlparse

from .. import config


def client():
    """Build a QdrantClient using URL port/scheme defaults correctly.

    qdrant-client defaults port=6333 even for https://host with no port,
    which breaks ingress on 443. Prefer the URL's port, else scheme default.
    """
    from qdrant_client import QdrantClient

    parsed = urlparse(config.QDRANT_URL)
    if parsed.port is not None:
        port = parsed.port
    else:
        port = 443 if parsed.scheme == "https" else 6333

    return QdrantClient(
        url=config.QDRANT_URL,
        port=port,
        api_key=config.QDRANT_API_KEY,
        check_compatibility=False,
        verify=config.QDRANT_VERIFY,
    )


def unnamed_vector_size(collection_info) -> int:
    """Return size of the unnamed/default vector, or raise if named-only."""
    vectors = collection_info.config.params.vectors
    if hasattr(vectors, "size"):
        return int(vectors.size)
    raise RuntimeError(
        "Collection uses named vectors; knowledge expects the unnamed default vector"
    )


def assert_collection_compatible(qdrant, collection: str, expected_dim: int) -> None:
    """Fail fast if the collection is missing or wrong dimensionality."""
    existing = {c.name for c in qdrant.get_collections().collections}
    if collection not in existing:
        raise RuntimeError(
            f"Qdrant collection {collection!r} not found at {config.QDRANT_URL}"
        )
    size = unnamed_vector_size(qdrant.get_collection(collection))
    if size != expected_dim:
        raise RuntimeError(
            f"Collection {collection!r} vector size is {size}, expected {expected_dim}"
        )
