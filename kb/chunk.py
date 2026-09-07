from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field

import yaml

from . import config

_FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_HEADING = re.compile(r"^(#{1,6})\s+(.*)$")


@dataclass
class Doc:
    path: str
    title: str
    tags: list[str]
    body: str          # markdown minus frontmatter
    doc_hash: str      # content hash of the normalized body


@dataclass
class Chunk:
    chunk_id: str
    path: str
    chunk_index: int
    heading: str       # heading trail, e.g. "Censorship > Resources"
    text: str          # child text
    parent_text: str   # full section text for context expansion
    token_count: int
    doc_hash: str
    tags: list[str] = field(default_factory=list)


def _est_tokens(text: str) -> int:
    return int(len(text.split()) * 1.3) + 1


def normalize(text: str) -> str:
    """Normalize before hashing so cosmetic edits don't force re-embeds."""
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def parse_doc(path: str, raw: str) -> Doc:
    fm: dict = {}
    m = _FRONTMATTER.match(raw)
    body = raw
    if m:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            fm = {}
        body = raw[m.end():]
    body = normalize(body)
    tags = fm.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]
    title = fm.get("title") or _first_heading(body) or path
    doc_hash = hashlib.sha256(body.encode("utf-8")).hexdigest()
    return Doc(path=path, title=str(title), tags=[str(t) for t in tags],
               body=body, doc_hash=doc_hash)


def _first_heading(body: str) -> str | None:
    for line in body.splitlines():
        m = _HEADING.match(line)
        if m:
            return m.group(2).strip()
    return None


def _sections(body: str) -> list[tuple[str, str]]:
    """Split body into (heading_trail, section_text), tracking heading hierarchy."""
    sections: list[tuple[str, str]] = []
    trail: list[str] = []
    cur_lines: list[str] = []
    cur_trail = ""

    def flush():
        text = "\n".join(cur_lines).strip()
        if text:
            sections.append((cur_trail, text))

    for line in body.splitlines():
        m = _HEADING.match(line)
        if m:
            flush()
            cur_lines.clear()
            level = len(m.group(1))
            title = m.group(2).strip()
            trail = trail[: level - 1]
            trail.append(title)
            cur_trail = " > ".join(trail)
            cur_lines.append(line)
        else:
            cur_lines.append(line)
    flush()
    if not sections:  # no headings at all
        sections.append(("", body.strip()))
    return sections


def _split_children(text: str) -> list[str]:
    """Split a section into token-bounded children with word overlap."""
    words = text.split()
    if not words:
        return []
    budget = max(1, int(config.CHILD_TOKENS / 1.3))
    overlap = int(config.CHILD_OVERLAP / 1.3)
    step = max(1, budget - overlap)
    out = []
    for start in range(0, len(words), step):
        piece = " ".join(words[start : start + budget])
        if piece.strip():
            out.append(piece)
        if start + budget >= len(words):
            break
    return out


def chunk_doc(doc: Doc) -> list[Chunk]:
    chunks: list[Chunk] = []
    idx = 0
    for heading, section_text in _sections(doc.body):
        for child in _split_children(section_text):
            chunk_id = f"{doc.path}::{doc.doc_hash[:8]}::{idx}"
            chunks.append(
                Chunk(
                    chunk_id=chunk_id,
                    path=doc.path,
                    chunk_index=idx,
                    heading=heading or doc.title,
                    text=child,
                    parent_text=section_text,
                    token_count=_est_tokens(child),
                    doc_hash=doc.doc_hash,
                    tags=doc.tags,
                )
            )
            idx += 1
    return chunks
