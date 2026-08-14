"""Storage layer: DuckDB (metadata + hash gate) and LanceDB (vectors + FTS)."""
from __future__ import annotations

import json

import duckdb
import lancedb
import pyarrow as pa

from . import config
from .chunk import Chunk


# ---------------------------------------------------------------------------
# DuckDB: document/chunk metadata and the incremental-ingest hash gate.
# ---------------------------------------------------------------------------
def duck() -> duckdb.DuckDBPyConnection:
    con = duckdb.connect(str(config.DUCKDB_PATH))
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS documents (
            path        TEXT PRIMARY KEY,
            doc_hash    TEXT,
            title       TEXT,
            tags        TEXT,        -- json array
            n_chunks    INTEGER,
            last_ingested TIMESTAMP DEFAULT now()
        );
        CREATE TABLE IF NOT EXISTS chunks (
            chunk_id    TEXT PRIMARY KEY,
            path        TEXT,
            chunk_index INTEGER,
            heading     TEXT,
            token_count INTEGER,
            doc_hash    TEXT
        );
        """
    )
    return con


def unchanged(con, path: str, doc_hash: str) -> bool:
    row = con.execute(
        "SELECT doc_hash FROM documents WHERE path = ?", [path]
    ).fetchone()
    return bool(row) and row[0] == doc_hash


def record_doc(con, path: str, doc_hash: str, title: str, tags, n_chunks: int):
    con.execute("DELETE FROM chunks WHERE path = ?", [path])
    con.execute("DELETE FROM documents WHERE path = ?", [path])
    con.execute(
        "INSERT INTO documents (path, doc_hash, title, tags, n_chunks) "
        "VALUES (?, ?, ?, ?, ?)",
        [path, doc_hash, title, json.dumps(tags), n_chunks],
    )


def record_chunks(con, chunks: list[Chunk]):
    con.executemany(
        "INSERT INTO chunks (chunk_id, path, chunk_index, heading, token_count, doc_hash) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        [
            [c.chunk_id, c.path, c.chunk_index, c.heading, c.token_count, c.doc_hash]
            for c in chunks
        ],
    )


def known_paths(con) -> set[str]:
    return {r[0] for r in con.execute("SELECT path FROM documents").fetchall()}


# ---------------------------------------------------------------------------
# LanceDB: vectors + full-text index (hybrid = vector + BM25 -> RRF).
# ---------------------------------------------------------------------------
def _schema() -> pa.Schema:
    return pa.schema(
        [
            pa.field("chunk_id", pa.string()),
            pa.field("path", pa.string()),
            pa.field("heading", pa.string()),
            pa.field("text", pa.string()),
            pa.field("parent_text", pa.string()),
            pa.field("tags", pa.string()),
            pa.field("vector", pa.list_(pa.float32(), config.EMBED_DIM)),
        ]
    )


def lance():
    return lancedb.connect(str(config.LANCEDB_PATH))


def lance_table(db=None):
    db = db or lance()
    if config.LANCE_TABLE in db.table_names():
        return db.open_table(config.LANCE_TABLE)
    return db.create_table(config.LANCE_TABLE, schema=_schema())


def delete_paths(tbl, paths: list[str]):
    for p in paths:
        tbl.delete(f"path = '{p}'")


def upsert_chunks(tbl, chunks: list[Chunk], vectors: list[list[float]]):
    rows = [
        {
            "chunk_id": c.chunk_id,
            "path": c.path,
            "heading": c.heading,
            "text": c.text,
            "parent_text": c.parent_text,
            "tags": json.dumps(c.tags),
            "vector": v,
        }
        for c, v in zip(chunks, vectors)
    ]
    if rows:
        tbl.add(rows)


def ensure_fts(tbl):
    """(Re)build the BM25 full-text index over chunk text for hybrid search."""
    try:
        tbl.create_fts_index("text", replace=True)
    except Exception:
        # tantivy missing or already current; hybrid falls back to vector-only.
        pass
