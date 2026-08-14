"""Hybrid retrieval over the local LanceDB index (vector + BM25 -> RRF)."""
from __future__ import annotations

import json

from . import config, embed, store


def search(question: str, k: int = 6) -> list[dict]:
    tbl = store.lance_table()
    qvec = embed.embed_query(question)

    # Try hybrid (needs an FTS index); fall back to vector-only.
    try:
        rows = (
            tbl.search(query_type="hybrid")
            .vector(qvec)
            .text(question)
            .limit(k)
            .to_list()
        )
    except Exception:
        rows = tbl.search(qvec).limit(k).to_list()

    results = []
    for r in rows:
        results.append(
            {
                "chunk_id": r.get("chunk_id"),
                "path": r.get("path"),
                "heading": r.get("heading"),
                "text": r.get("text"),
                "parent_text": r.get("parent_text"),
                "tags": json.loads(r.get("tags") or "[]"),
                "score": r.get("_relevance_score") or r.get("_distance"),
            }
        )
    return results


def format_results(results: list[dict], expand: bool = False) -> str:
    if not results:
        return "No results. Has the index been built? Run `make ingest`."
    out = []
    for i, r in enumerate(results, 1):
        body = r["parent_text"] if expand else r["text"]
        out.append(
            f"[{i}] {r['path']}  —  {r['heading']}\n"
            f"    score={r['score']}\n"
            f"    {body.strip()[:600]}"
        )
    return "\n\n".join(out)
