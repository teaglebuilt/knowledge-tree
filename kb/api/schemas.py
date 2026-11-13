"""Canonical request/response models for kb-api and both MCP surfaces.

The REST routes, /openapi.json and the generated MCP tool input schemas all
come from these classes; there is no second, hand-written parameter list.
"""
from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

from .. import config

# Emptiness and shape are checked by the write policy, not here, so an agent
# gets a "rejected" receipt it can act on instead of a schema error.
_PATH = Field(
    description="Stable document identity, e.g. tree/docs/kagent/agent-delegation.md",
    max_length=512,
)


class _Model(BaseModel):
    model_config = ConfigDict(extra="forbid")


# --- read ---------------------------------------------------------------------

class SearchRequest(_Model):
    query: str = Field(min_length=1, max_length=2000, description="Natural-language query.")
    k: int = Field(
        default=config.KB_SEARCH_DEFAULT_K,
        ge=1,
        description=f"Number of chunks to return (capped at {config.KB_SEARCH_MAX_K}).",
    )
    path: str | None = Field(default=None, description="Search inside one document only.")
    source_type: str | None = Field(
        default=None, description='Restrict by origin, e.g. "youtube", "tree", "documentation".'
    )


class SearchHitModel(BaseModel):
    path: str
    heading: str
    chunk_index: int
    score: float
    source_type: str
    source_url: str
    tags: list[str]
    text: str


class SearchResponse(BaseModel):
    hits: list[SearchHitModel]


class DocumentPageRequest(_Model):
    path: str = _PATH
    offset: int = Field(default=0, ge=0, description="First chunk to return; use next_offset.")
    limit: int = Field(
        default=config.KB_DOCUMENT_PAGE_CHUNKS,
        ge=1,
        description=f"Chunks per page (capped at {config.KB_DOCUMENT_MAX_PAGE_CHUNKS}).",
    )


class DocumentPageResponse(BaseModel):
    path: str
    title: str
    source_type: str
    source_url: str
    total_chunks: int
    offset: int
    returned_chunks: int
    next_offset: int | None = Field(description="Pass as offset to read on; null at the end.")
    text: str


# --- write --------------------------------------------------------------------

StoreStatus = Literal["ingested", "unchanged", "empty"]


class StoreDocumentRequest(_Model):
    """Upsert one markdown document keyed by `path` (HTTP writers, e.g. n8n)."""

    path: str = _PATH
    markdown: str = Field(description="Full markdown body, frontmatter allowed.")
    source_url: str | None = Field(default=None, description="http(s) provenance URL.")
    source_type: str | None = Field(
        default=None, description="Origin label; reserved types (tree, memory, chatgpt*) refused."
    )
    title: str | None = Field(default=None, description="Title for added frontmatter.")
    tags: list[str] | None = Field(default=None, description="Tags for added frontmatter.")
    force: bool = Field(default=False, description="Re-embed even if the body is unchanged.")


class AgentStoreDocumentRequest(StoreDocumentRequest):
    """Agent variant: provenance is mandatory and the type defaults to documentation."""

    source_url: str = Field(description="http(s) page the content came from.")
    source_type: str | None = Field(
        default="documentation", description="Must be one of the agent-allowed source types."
    )


class StoreDocumentReceipt(BaseModel):
    status: StoreStatus = Field(
        description="ingested/unchanged mean the document is searchable now; retries are safe."
    )
    path: str
    doc_hash: str
    chunks: int
    collection: str
    source_url: str | None = None


class DocumentStatusRequest(_Model):
    path: str = _PATH


class DocumentStatus(BaseModel):
    path: str
    exists: bool
    doc_hash: str | None = Field(description="Indexed revision; null if absent or ambiguous.")


class DeleteDocumentResponse(BaseModel):
    path: str
    deleted_revisions: int


# --- errors -------------------------------------------------------------------

ErrorCode = Literal[
    "invalid_request",
    "policy_violation",
    "unauthorized",
    "forbidden",
    "not_found",
    "payload_too_large",
    "backend_unavailable",
]


class ErrorResponse(BaseModel):
    error: str
    code: ErrorCode
