"""Service: embed query → ANN search → citation-friendly text."""
from __future__ import annotations

from dataclasses import dataclass
from html import escape

from .. import config, embed
from .qdrant_store import QdrantChunkStore, SearchHit


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

    def document_page(
        self, path: str, offset: int = 0, limit: int | None = None
    ) -> DocumentPage | None:
        """One page of a stored document, or None when nothing is at `path`."""
        rel = _clean(path)
        if not rel:
            raise ValueError("path must be a non-empty string")
        if offset < 0:
            raise ValueError("offset must be >= 0")
        chunks = self._store.document(rel)
        if not chunks:
            return None
        return page_document(chunks, offset, _clamp_page(limit))

    def document_formatted(
        self, path: str, offset: int = 0, limit: int | None = None
    ) -> str:
        page = self.document_page(path, offset, limit)
        return format_page(page) if page else missing_document(path)


@dataclass(frozen=True)
class DocumentPage:
    path: str
    title: str
    source_type: str
    source_url: str
    total_chunks: int
    offset: int
    chunks: list[SearchHit]
    next_offset: int | None

    @property
    def text(self) -> str:
        return stitch(self.chunks)


def page_document(chunks: list[SearchHit], offset: int, limit: int) -> DocumentPage:
    window = chunks[offset : offset + limit]
    end = offset + len(window)
    head = chunks[0]
    return DocumentPage(
        path=head.path,
        title=head.title,
        source_type=head.source_type,
        source_url=head.source_url,
        total_chunks=len(chunks),
        offset=offset,
        chunks=window,
        next_offset=end if end < len(chunks) else None,
    )


def missing_document(path: str) -> str:
    return f'No document stored at path "{_clean(path)}".'


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
    return format_page(page_document(chunks, offset, limit))


def format_page(page: DocumentPage) -> str:
    end = page.offset + len(page.chunks)
    attrs = {
        "path": page.path,
        "title": page.title,
        "source_type": page.source_type,
        "source_url": page.source_url,
        "chunks": f"{page.offset}-{max(page.offset, end - 1)} of {page.total_chunks}",
    }
    if page.next_offset is not None:
        attrs["next_offset"] = str(page.next_offset)
    if not page.chunks:
        body = f"offset {page.offset} is past the last chunk ({page.total_chunks - 1})."
    else:
        body = page.text
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
