"""Agent-facing write MCP: `kb_ingest` + `kb_ingest_status`.

Served by the kb-ingest process at /mcp, NOT by kb-retrieval. kb-retrieval is
bound by every agent that reads the tree, and kagent's Claude harness ignores
per-tool allowlists, so a write tool there would be a write tool everywhere.
Keeping writes on their own server means "can write" is decided by which
RemoteMCPServer an AgentTemplate binds, not by a list the harness may ignore.

Every call returns a JSON receipt. The receipt is the completion signal a
delegating agent relays upward: `status` plus `doc_hash` is proof the
document is indexed, and `kb_ingest_status` (or kb-retrieval's
`kb_get_document`) can re-verify it independently.
"""
from __future__ import annotations

import asyncio
import json
import re

import yaml
from mcp.server.mcpserver import MCPServer

from .. import config
from ..chunk import _FRONTMATTER
from .service import IngestError, KnowledgeIngest, frontmatter, normalize_path

mcp = MCPServer(
    name="kb-ingest",
    instructions=(
        "Write plane for the knowledge tree. kb_ingest stores ONE markdown "
        "document at a stable path under "
        f"{', '.join(config.KB_MCP_INGEST_PATH_PREFIXES)} and returns a JSON "
        "receipt; status 'ingested' or 'unchanged' means it is searchable via "
        "kb_search now. Re-sending identical content is a no-op, so retries "
        "are safe. Use kb_ingest_status to check a path before or after."
    ),
)

_ingest: KnowledgeIngest | None = None
_SLUG = re.compile(r"^[a-z0-9][a-z0-9._/-]*\.md$")


def _service() -> KnowledgeIngest:
    global _ingest
    if _ingest is None:
        _ingest = KnowledgeIngest()
    return _ingest


def bind_service(service: KnowledgeIngest) -> None:
    """Share the HTTP app's service (one Qdrant client per process)."""
    global _ingest
    _ingest = service


def agent_path(path: str) -> str:
    rel = normalize_path(path)
    if not rel.startswith(config.KB_MCP_INGEST_PATH_PREFIXES):
        raise IngestError(
            "agents may only write under "
            + ", ".join(config.KB_MCP_INGEST_PATH_PREFIXES)
        )
    if not _SLUG.match(rel):
        raise IngestError("path must be lowercase [a-z0-9._/-] and end with .md")
    return rel


def with_frontmatter(
    markdown: str, *, title: str | None, source_url: str, source_type: str,
    tags: list[str] | None,
) -> str:
    """Ensure provenance frontmatter exists.

    doc_hash covers the body only (kb.chunk.parse_doc), so frontmatter never
    changes idempotency; fields are still kept deterministic so a stored
    document is reproducible from the same inputs.
    """
    body = markdown.strip() + "\n"
    existing = frontmatter(body)
    if existing:
        missing = {
            k: v
            for k, v in {
                "source_url": source_url,
                "source_type": source_type,
                "title": title,
                "tags": tags,
            }.items()
            if v and k not in existing
        }
        if not missing:
            return body
        merged = {**existing, **missing}
        rest = body[_FRONTMATTER.match(body).end() :].lstrip("\n")
        return "---\n" + yaml.safe_dump(merged, sort_keys=True).strip() + "\n---\n\n" + rest
    meta = {"source_url": source_url, "source_type": source_type}
    if title:
        meta["title"] = title
    if tags:
        meta["tags"] = list(tags)
    return "---\n" + yaml.safe_dump(meta, sort_keys=True).strip() + "\n---\n\n" + body


def ingest_receipt(
    path: str,
    markdown: str,
    source_url: str,
    *,
    title: str | None = None,
    tags: list[str] | None = None,
    source_type: str = "documentation",
    force: bool = False,
) -> dict:
    """Validate agent policy, ingest, and return a receipt (never raises)."""
    try:
        rel = agent_path(path)
        if source_type not in config.KB_MCP_INGEST_SOURCE_TYPES:
            raise IngestError(
                "source_type must be one of "
                + ", ".join(config.KB_MCP_INGEST_SOURCE_TYPES)
            )
        url = (source_url or "").strip()
        if not url.startswith(("https://", "http://")):
            raise IngestError("source_url (http/https) is required for provenance")
        if len((markdown or "").encode()) > config.KB_MCP_INGEST_MAX_BYTES:
            raise IngestError(
                f"markdown exceeds {config.KB_MCP_INGEST_MAX_BYTES} bytes; "
                "split it into several documents"
            )
        doc = with_frontmatter(
            markdown or "", title=title, source_url=url,
            source_type=source_type, tags=tags,
        )
        result = _service().ingest(
            rel, doc, source_type=source_type, source_url=url, force=force
        )
    except IngestError as exc:
        return {"status": "rejected", "path": path, "error": str(exc)}
    except Exception as exc:  # Qdrant/embedding outage: retryable, not caller's fault
        return {"status": "failed", "path": path, "error": f"{type(exc).__name__}: {exc}",
                "retryable": True}
    return {
        "status": result.status,
        "path": result.path,
        "doc_hash": result.doc_hash,
        "chunks": result.chunks,
        "collection": config.QDRANT_COLLECTION,
        "source_url": url,
    }


@mcp.tool()
async def kb_ingest(
    path: str,
    markdown: str,
    source_url: str,
    title: str | None = None,
    tags: list[str] | None = None,
    source_type: str = "documentation",
    force: bool = False,
) -> str:
    """Store one markdown document in the knowledge tree and index it.

    `path` is the document's stable identity, e.g.
    "tree/docs/kagent/agent-delegation.md"; writing the same path again
    replaces the previous revision. `source_url` is required. Frontmatter
    (title, source_url, source_type, tags) is added if absent.

    Returns JSON: {"status": "ingested"|"unchanged"|"empty"|"rejected"|"failed",
    "path", "doc_hash", "chunks", ...}. "rejected" means fix the input;
    "failed" with retryable=true means try again later.
    """
    receipt = await asyncio.to_thread(
        ingest_receipt, path, markdown, source_url,
        title=title, tags=tags, source_type=source_type, force=force,
    )
    return json.dumps(receipt, sort_keys=True)


@mcp.tool()
async def kb_ingest_status(path: str) -> str:
    """Report whether a path is indexed and which revision (doc_hash) it holds.

    Returns JSON {"path", "exists", "doc_hash"}. Use before writing to avoid
    duplicate work, and after writing to confirm completion.
    """

    def _status() -> dict:
        try:
            return _service().exists(agent_path(path))
        except IngestError as exc:
            return {"path": path, "exists": False, "error": str(exc)}

    return json.dumps(await asyncio.to_thread(_status), sort_keys=True)
