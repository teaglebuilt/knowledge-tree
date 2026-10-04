from __future__ import annotations

import json

from . import config, store


def _client():
    from urllib.parse import urlparse

    from qdrant_client import QdrantClient
    # qdrant-client defaults port=6333 even for https://host (no port in URL),
    # which breaks ingress on 443. Use the URL's port, else scheme default.
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


def _point_id(chunk_id: str) -> str:
    import hashlib
    import uuid

    # Deterministic UUID from the stable chunk_id so re-syncs upsert, not dupe.
    h = hashlib.sha256(chunk_id.encode()).hexdigest()
    return str(uuid.UUID(h[:32]))


def push(batch: int = 256) -> dict:
    from qdrant_client import models

    client = _client()
    tbl = store.lance_table()

    existing = {c.name for c in client.get_collections().collections}
    if config.QDRANT_COLLECTION not in existing:
        client.create_collection(
            collection_name=config.QDRANT_COLLECTION,
            vectors_config=models.VectorParams(
                size=config.EMBED_DIM, distance=models.Distance.COSINE
            ),
        )

    # Arrow → list of dicts (avoid pandas; not a project dependency).
    rows = tbl.to_arrow().to_pylist()
    points, pushed = [], 0
    for r in rows:
        points.append(
            models.PointStruct(
                id=_point_id(r["chunk_id"]),
                vector=list(r["vector"]),
                payload={
                    "chunk_id": r["chunk_id"],
                    "path": r["path"],
                    "heading": r["heading"],
                    "text": r["text"],
                    "tags": json.loads(r["tags"] or "[]"),
                },
            )
        )
        if len(points) >= batch:
            client.upsert(config.QDRANT_COLLECTION, points=points)
            pushed += len(points)
            points = []
    if points:
        client.upsert(config.QDRANT_COLLECTION, points=points)
        pushed += len(points)

    print(f"sync: pushed {pushed} points -> {config.QDRANT_URL}/{config.QDRANT_COLLECTION}")
    return {"pushed": pushed}
