"""Incremental ingest: walk markdown -> hash-gate -> chunk -> embed -> LanceDB."""
from __future__ import annotations

from pathlib import Path

from . import config, embed, store
from .chunk import chunk_doc, parse_doc


def _iter_markdown() -> list[Path]:
    files: list[Path] = []
    for d in config.KNOWLEDGE_DIRS:
        base = config.ROOT / d.strip()
        if base.exists():
            files.extend(sorted(base.rglob("*.md")))
    return files


def run(force: bool = False) -> dict:
    con = store.duck()
    db = store.lance()
    tbl = store.lance_table(db)

    seen: set[str] = set()
    ingested = skipped = 0
    total_chunks = 0

    for fp in _iter_markdown():
        rel = str(fp.relative_to(config.ROOT))
        seen.add(rel)
        doc = parse_doc(rel, fp.read_text(encoding="utf-8", errors="replace"))

        if not force and store.unchanged(con, rel, doc.doc_hash):
            skipped += 1
            continue

        chunks = chunk_doc(doc)
        if not chunks:
            skipped += 1
            continue

        # Replace any prior version of this doc in both stores.
        store.delete_paths(tbl, [rel])
        vectors = embed.embed([c.text for c in chunks])
        store.upsert_chunks(tbl, chunks, vectors)
        store.record_doc(con, rel, doc.doc_hash, doc.title, doc.tags, len(chunks))
        store.record_chunks(con, chunks)

        ingested += 1
        total_chunks += len(chunks)
        print(f"  + {rel}  ({len(chunks)} chunks)")

    # Prune docs deleted from the repo.
    stale = store.known_paths(con) - seen
    if stale:
        store.delete_paths(tbl, list(stale))
        for p in stale:
            con.execute("DELETE FROM chunks WHERE path = ?", [p])
            con.execute("DELETE FROM documents WHERE path = ?", [p])
        print(f"  - pruned {len(stale)} deleted docs")

    con.close()
    print(
        f"\ningest: {ingested} changed, {skipped} unchanged, "
        f"{len(stale)} pruned, {total_chunks} chunks embedded"
    )
    return {"ingested": ingested, "skipped": skipped, "pruned": len(stale),
            "chunks": total_chunks}


def reindex():
    """Rebuild the BM25 full-text index (run after a bulk ingest)."""
    tbl = store.lance_table()
    store.ensure_fts(tbl)
    print(f"reindex: FTS index rebuilt on '{config.LANCE_TABLE}.text'")
