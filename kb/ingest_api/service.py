"""Write plane: markdown document -> chunk -> embed -> Qdrant.

Reuses kb.chunk and kb.embed unchanged so documents pushed over HTTP land in
the same vector space, with the same chunk ids, as `kb ingest` + `kb sync`.
Touches Qdrant only — callers have no filesystem, LanceDB or DuckDB.
"""
from __future__ import annotations

import os
import posixpath
from dataclasses import dataclass

import yaml

from .. import config, embed
from ..adapters import qdrant as qd
from ..chunk import _FRONTMATTER, chunk_doc, parse_doc

UPSERT_BATCH = int(os.environ.get("KB_INGEST_BATCH", "128"))

#: Paths the write plane may own. Keeps a misconfigured caller from
#: overwriting documents the local tree pipeline is the writer for.
ALLOWED_PREFIXES = tuple(
    p.strip()
    for p in os.environ.get("KB_INGEST_PATH_PREFIXES", "tree/").split(",")
    if p.strip()
)


class IngestError(ValueError):
    """Caller-fixable problem with the submitted document."""


@dataclass
class IngestResult:
    path: str
    doc_hash: str
    chunks: int
    status: str  # ingested | unchanged | empty


def normalize_path(path: str) -> str:
    candidate = (path or "").strip().lstrip("/")
    if not candidate:
        raise IngestError("path is required")
    if candidate != posixpath.normpath(candidate) or candidate.startswith(".."):
        raise IngestError(f"path must be normalized and relative: {path!r}")
    if not candidate.endswith(".md"):
        raise IngestError("path must end with .md")
    if ALLOWED_PREFIXES and not candidate.startswith(ALLOWED_PREFIXES):
        raise IngestError(
            f"path must start with one of {', '.join(ALLOWED_PREFIXES)}"
        )
    return candidate


def frontmatter(raw: str) -> dict:
    m = _FRONTMATTER.match(raw)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


class KnowledgeIngest:
    """Single-writer ingest into the Qdrant knowledge collection."""

    def __init__(self, client=None) -> None:
        self._client = client or qd.client()
        self._prepared = False

    def _prepare(self) -> None:
        if self._prepared:
            return
        qd.ensure_collection(
            self._client, config.QDRANT_COLLECTION, config.EMBED_DIM
        )
        qd.ensure_payload_indexes(self._client, config.QDRANT_COLLECTION)
        self._prepared = True

    def ingest(
        self,
        path: str,
        markdown: str,
        *,
        source_type: str | None = None,
        source_url: str | None = None,
        force: bool = False,
    ) -> IngestResult:
        rel = normalize_path(path)
        if not (markdown or "").strip():
            raise IngestError("markdown is required")

        fm = frontmatter(markdown)
        doc = parse_doc(rel, markdown)
        resolved_type = source_type or fm.get("source_type") or "unknown"
        resolved_url = source_url or fm.get("source_url")

        self._prepare()
        collection = config.QDRANT_COLLECTION
        existing = qd.path_doc_hashes(self._client, collection, rel)

        if not force and existing == {doc.doc_hash}:
            return IngestResult(rel, doc.doc_hash, 0, "unchanged")

        chunks = chunk_doc(doc)
        if not chunks:
            return IngestResult(rel, doc.doc_hash, 0, "empty")

        vectors = embed.embed([c.text for c in chunks])

        # Replace rather than merge: an edited doc gets new chunk ids, so the
        # previous revision's points would otherwise linger forever.
        if existing:
            qd.delete_path(self._client, collection, rel)

        self._upsert(collection, doc, chunks, vectors, resolved_type, resolved_url)
        return IngestResult(rel, doc.doc_hash, len(chunks), "ingested")

    def _upsert(self, collection, doc, chunks, vectors, source_type, source_url):
        from qdrant_client import models

        batch = []
        for chunk, vector in zip(chunks, vectors):
            payload = {
                "chunk_id": chunk.chunk_id,
                "path": chunk.path,
                "heading": chunk.heading,
                "text": chunk.text,
                "tags": list(chunk.tags),
                "doc_hash": chunk.doc_hash,
                "chunk_index": chunk.chunk_index,
                "title": doc.title,
                "source_type": source_type,
            }
            if source_url:
                payload["source_url"] = str(source_url)
            batch.append(
                models.PointStruct(
                    id=qd.point_id(chunk.chunk_id),
                    vector=list(vector),
                    payload=payload,
                )
            )
            if len(batch) >= UPSERT_BATCH:
                self._client.upsert(collection, points=batch, wait=True)
                batch = []
        if batch:
            self._client.upsert(collection, points=batch, wait=True)

    def exists(self, path: str) -> dict:
        """Cheap 'do you already hold this path?' check for pollers."""
        rel = normalize_path(path)
        self._prepare()
        hashes = qd.path_doc_hashes(self._client, config.QDRANT_COLLECTION, rel)
        return {
            "path": rel,
            "exists": bool(hashes),
            "doc_hash": next(iter(hashes)) if len(hashes) == 1 else None,
        }

    def delete(self, path: str) -> int:
        rel = normalize_path(path)
        self._prepare()
        collection = config.QDRANT_COLLECTION
        existing = qd.path_doc_hashes(self._client, collection, rel)
        if existing:
            qd.delete_path(self._client, collection, rel)
        return len(existing)
