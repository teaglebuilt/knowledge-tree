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
    live_ids = set()
    for r in rows:
        live_ids.add(_point_id(r["chunk_id"]))
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

    # An empty table almost always means a wrong KB_LANCEDB, not an empty
    # tree — pruning then would wipe every tree point in Qdrant.
    if live_ids:
        pruned = prune(client, live_ids, batch=batch)
    else:
        print("sync: LanceDB table is empty; skipping prune")
        pruned = 0

    print(
        f"sync: pushed {pushed}, pruned {pruned} points -> "
        f"{config.QDRANT_URL}/{config.QDRANT_COLLECTION}"
    )
    return {"pushed": pushed, "pruned": pruned}


def prune(client, live_ids: set[str], batch: int = 256) -> int:
    """Delete `source_type: tree` points LanceDB no longer has.

    chunk_ids embed the doc hash, so this drops both deleted docs and the old
    chunks of edited ones. Points from the HTTP ingest plane carry their own
    source_type and are never touched.
    """
    from qdrant_client import models

    tree_only = models.Filter(
        must=[models.FieldCondition(key="source_type", match=models.MatchValue(value="tree"))]
    )
    stale, offset = [], None
    while True:
        found, offset = client.scroll(
            collection_name=config.QDRANT_COLLECTION,
            scroll_filter=tree_only,
            limit=1024,
            with_payload=False,
            with_vectors=False,
            offset=offset,
        )
        stale.extend(p.id for p in found if str(p.id) not in live_ids)
        if offset is None:
            break

    for i in range(0, len(stale), batch):
        client.delete(
            collection_name=config.QDRANT_COLLECTION,
            points_selector=models.PointIdsList(points=stale[i : i + batch]),
            wait=True,
        )
    return len(stale)
