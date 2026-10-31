"""Shared Qdrant client factory (sync + MCP read plane)."""
from __future__ import annotations

from urllib.parse import urlparse

from .. import config


def client():
    """
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


def point_id(chunk_id: str) -> str:
    """Deterministic UUID from a stable chunk_id so re-writes upsert, not dupe.
    Shared by every writer (local `kb sync`, the HTTP ingest plane) so the same
    chunk always lands on the same Qdrant point.
    """
    import hashlib
    import uuid

    h = hashlib.sha256(chunk_id.encode()).hexdigest()
    return str(uuid.UUID(h[:32]))


def ensure_collection(qdrant, collection: str, dim: int) -> bool:
    """Create the collection with the unnamed cosine vector if absent."""
    from qdrant_client import models

    existing = {c.name for c in qdrant.get_collections().collections}
    if collection in existing:
        return False
    qdrant.create_collection(
        collection_name=collection,
        vectors_config=models.VectorParams(size=dim, distance=models.Distance.COSINE),
    )
    return True


#: Payload fields that must be indexed for filtered delete/scroll to work.
INDEXED_PAYLOAD_FIELDS = ("path", "doc_hash", "source_type")


def ensure_payload_indexes(qdrant, collection: str) -> list[str]:
    """Create the keyword indexes delete-by-path and source filtering need."""
    from qdrant_client import models

    info = qdrant.get_collection(collection)
    existing = set(getattr(info, "payload_schema", None) or {})
    created = []
    for field in INDEXED_PAYLOAD_FIELDS:
        if field in existing:
            continue
        qdrant.create_payload_index(
            collection_name=collection,
            field_name=field,
            field_schema=models.PayloadSchemaType.KEYWORD,
            wait=True,
        )
        created.append(field)
    return created


def _path_filter(path: str):
    from qdrant_client import models

    return models.Filter(
        must=[models.FieldCondition(key="path", match=models.MatchValue(value=path))]
    )


def path_doc_hashes(qdrant, collection: str, path: str) -> set[str]:
    """Every doc_hash currently stored for a path (empty when the path is new)."""
    hashes: set[str] = set()
    offset = None
    while True:
        points, offset = qdrant.scroll(
            collection_name=collection,
            scroll_filter=_path_filter(path),
            limit=256,
            with_payload=["doc_hash"],
            with_vectors=False,
            offset=offset,
        )
        for p in points:
            h = (p.payload or {}).get("doc_hash")
            if h:
                hashes.add(str(h))
        if offset is None:
            break
    return hashes


def delete_path(qdrant, collection: str, path: str) -> None:
    """Drop every point for a path. Requires the `path` payload index."""
    from qdrant_client import models

    qdrant.delete(
        collection_name=collection,
        points_selector=models.FilterSelector(filter=_path_filter(path)),
        wait=True,
    )
