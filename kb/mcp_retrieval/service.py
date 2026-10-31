"""Service: embed query → ANN search → citation-friendly text."""
from __future__ import annotations

from html import escape

from .. import config, embed
from .store import QdrantChunkStore, SearchHit


class KnowledgeSearch:
    """Read-only knowledge search (no writes)."""

    def __init__(self, store: QdrantChunkStore | None = None) -> None:
        self._store = store or QdrantChunkStore()

    def search(
        self,
        query: str,
        k: int | None = None,
        *,
        path: str | None = None,
        source_type: str | None = None,
    ) -> list[SearchHit]:
        question = query.strip()
        if not question:
            raise ValueError("query must be a non-empty string")
        limit = _clamp_k(k)
        vector = embed.embed_query(question)
        return self._store.search(
            vector, limit, path=_clean(path), source_type=_clean(source_type)
        )

    def search_formatted(
        self,
        query: str,
        k: int | None = None,
        *,
        path: str | None = None,
        source_type: str | None = None,
    ) -> str:
        hits = self.search(query, k, path=path, source_type=source_type)
        return format_hits(hits)

    def document_formatted(
        self, path: str, offset: int = 0, limit: int | None = None
    ) -> str:
        rel = _clean(path)
        if not rel:
            raise ValueError("path must be a non-empty string")
        if offset < 0:
            raise ValueError("offset must be >= 0")
        page = _clamp_page(limit)
        chunks = self._store.document(rel)
        if not chunks:
            return f'No document stored at path "{rel}".'
        return format_document(chunks, offset, page)


def _clean(value: str | None) -> str | None:
    value = (value or "").strip()
    return value or None


def _clamp_k(k: int | None) -> int:
    if k is None:
        return config.KB_SEARCH_DEFAULT_K
    if k < 1:
        raise ValueError("k must be >= 1")
    return min(k, config.KB_SEARCH_MAX_K)


def _clamp_page(limit: int | None) -> int:
    if limit is None:
        return config.KB_DOCUMENT_PAGE_CHUNKS
    if limit < 1:
        raise ValueError("limit must be >= 1")
    return min(limit, config.KB_DOCUMENT_MAX_PAGE_CHUNKS)


def format_hits(hits: list[SearchHit]) -> str:
    if not hits:
        return "No results."
    blocks = []
    for hit in hits:
        attrs = {
            "path": hit.path,
            "heading": hit.heading,
            "chunk_index": str(hit.chunk_index),
            "score": f"{hit.score:.4f}",
            "source_type": hit.source_type,
            "source_url": hit.source_url,
            "tags": ",".join(hit.tags),
        }
        blocks.append(f"<chunk {_attrs(attrs)}>\n{hit.text.strip()}\n</chunk>")
    return "\n\n".join(blocks)


def format_document(chunks: list[SearchHit], offset: int, limit: int) -> str:
    total = len(chunks)
    window = chunks[offset : offset + limit]
    end = offset + len(window)
    head = chunks[0]
    attrs = {
        "path": head.path,
        "title": head.title,
        "source_type": head.source_type,
        "source_url": head.source_url,
        "chunks": f"{offset}-{max(offset, end - 1)} of {total}",
    }
    if end < total:
        attrs["next_offset"] = str(end)
    if not window:
        body = f"offset {offset} is past the last chunk ({total - 1})."
    else:
        body = stitch(window)
    return f"<document {_attrs(attrs)}>\n{body}\n</document>"


def stitch(chunks: list[SearchHit]) -> str:
    """Rejoin ordered chunks into readable text without the chunker's overlap."""
    sections: list[tuple[str, str]] = []
    for chunk in chunks:
        text = chunk.text.strip()
        if sections and sections[-1][0] == chunk.heading:
            heading, prior = sections[-1]
            sections[-1] = (heading, _join_overlapping(prior, text))
        else:
            sections.append((chunk.heading, text))
    out = []
    for heading, text in sections:
        if heading and not text.lstrip().startswith("#"):
            out.append(f"[{heading}]\n{text}")
        else:
            out.append(text)
    return "\n\n".join(out)


def _join_overlapping(left: str, right: str) -> str:
    """Drop the longest word run that ends `left` and starts `right`."""
    a, b = left.split(), right.split()
    longest = min(len(a), len(b), config.CHILD_OVERLAP * 2)
    for size in range(longest, 0, -1):
        if a[-size:] == b[:size]:
            return " ".join(a + b[size:])
    return f"{left} {right}"


def _attrs(values: dict[str, str]) -> str:
    return " ".join(
        f'{key}="{escape(value, quote=True)}"' for key, value in values.items() if value
    )
