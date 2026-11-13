"""Write policy: who may store what, where. One check, every write surface.

REST (`POST /v1/documents`, legacy `/ingest`) and the write MCP
(`kb_store_document`) both call `store()`; they differ only in which
WritePolicy they pass. Tool descriptions and route filters are hints for
callers; this module is the enforcement.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

import yaml

from .. import config
from ..chunk import _FRONTMATTER
from .ingest import IngestError, IngestResult, KnowledgeIngest, frontmatter, normalize_path

_SLUG = re.compile(r"^[a-z0-9][a-z0-9._/-]*\.md$")


class PolicyError(IngestError):
    """The write is well-formed but this caller may not make it."""


class PayloadTooLarge(PolicyError):
    """The document exceeds the caller's size cap."""


@dataclass(frozen=True)
class WritePolicy:
    name: str
    #: Narrower than config.KB_API_WRITE_PATH_PREFIXES (always enforced).
    path_prefixes: tuple[str, ...] = ()
    require_slug: bool = False
    #: None allows any source_type that is not reserved.
    source_types: tuple[str, ...] | None = None
    default_source_type: str | None = None
    require_source_url: bool = False
    max_markdown_bytes: int | None = None
    ensure_frontmatter: bool = False


def api_policy() -> WritePolicy:
    """HTTP callers (n8n): API path prefixes, any non-reserved source type."""
    return WritePolicy(name="api")


def agent_policy() -> WritePolicy:
    """kb-mcp-write callers: own prefix, closed types, provenance, size cap."""
    return WritePolicy(
        name="agent",
        path_prefixes=config.KB_MCP_WRITE_PATH_PREFIXES,
        require_slug=True,
        source_types=config.KB_MCP_WRITE_SOURCE_TYPES,
        default_source_type="documentation",
        require_source_url=True,
        max_markdown_bytes=config.KB_MCP_WRITE_MAX_BYTES,
        ensure_frontmatter=True,
    )


def check_path(path: str, policy: WritePolicy) -> str:
    rel = normalize_path(path)
    if policy.path_prefixes and not rel.startswith(policy.path_prefixes):
        raise PolicyError(
            f"{policy.name} callers may only write under " + ", ".join(policy.path_prefixes)
        )
    if policy.require_slug and not _SLUG.match(rel):
        raise PolicyError("path must be lowercase [a-z0-9._/-] and end with .md")
    return rel


def with_frontmatter(
    markdown: str, *, title: str | None, source_url: str | None, source_type: str | None,
    tags: list[str] | None,
) -> str:
    """Ensure provenance frontmatter exists.

    doc_hash covers the body only (kb.chunk.parse_doc), so frontmatter never
    changes idempotency; fields are still kept deterministic so a stored
    document is reproducible from the same inputs.
    """
    body = markdown.strip() + "\n"
    wanted = {"source_url": source_url, "source_type": source_type, "title": title, "tags": tags}
    existing = frontmatter(body)
    if existing:
        missing = {k: v for k, v in wanted.items() if v and k not in existing}
        if not missing:
            return body
        merged = {**existing, **missing}
        rest = body[_FRONTMATTER.match(body).end() :].lstrip("\n")
        return "---\n" + yaml.safe_dump(merged, sort_keys=True).strip() + "\n---\n\n" + rest
    meta = {k: (list(v) if k == "tags" else v) for k, v in wanted.items() if v}
    return "---\n" + yaml.safe_dump(meta, sort_keys=True).strip() + "\n---\n\n" + body


def store(
    service: KnowledgeIngest,
    policy: WritePolicy,
    *,
    path: str,
    markdown: str,
    source_url: str | None = None,
    source_type: str | None = None,
    title: str | None = None,
    tags: list[str] | None = None,
    force: bool = False,
) -> tuple[IngestResult, str | None]:
    """Validate against `policy`, then upsert. Returns (result, source_url)."""
    rel = check_path(path, policy)
    resolved_type = source_type or policy.default_source_type
    if policy.source_types is not None and resolved_type not in policy.source_types:
        raise PolicyError("source_type must be one of " + ", ".join(policy.source_types))
    url = (source_url or "").strip() or None
    if url and not url.startswith(("https://", "http://")):
        raise PolicyError("source_url must be an http(s) URL")
    if policy.require_source_url and not url:
        raise PolicyError("source_url (http/https) is required for provenance")
    if policy.max_markdown_bytes is not None and (
        len((markdown or "").encode()) > policy.max_markdown_bytes
    ):
        raise PayloadTooLarge(
            f"markdown exceeds {policy.max_markdown_bytes} bytes; split it into several documents"
        )
    doc = markdown or ""
    if policy.ensure_frontmatter:
        doc = with_frontmatter(
            doc, title=title, source_url=url, source_type=resolved_type, tags=tags
        )
    result = service.ingest(rel, doc, source_type=resolved_type, source_url=url, force=force)
    return result, url


def status(service: KnowledgeIngest, policy: WritePolicy, path: str) -> dict:
    """Indexed revision for a path the caller could write."""
    return service.exists(check_path(path, policy))
