from __future__ import annotations

import json

from . import config, store
from .adapters.qdrant import (
    client as _client,
    ensure_collection,
    ensure_payload_indexes,
    point_id as _point_id,
)


def push(batch: int = 256) -> dict:
    from qdrant_client import models

    client = _client()
    tbl = store.lance_table()

    ensure_collection(client, config.QDRANT_COLLECTION, config.EMBED_DIM)
    ensure_payload_indexes(client, config.QDRANT_COLLECTION)

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
                    "source_type": "tree",
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
