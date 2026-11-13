"""The kb operations, defined once.

Each Operation is a validated input model plus a sync handler returning a
domain result. kb.api.app serves them as REST routes (operation_id = name);
kb.mcp.factory turns an explicit allowlist of them into MCP tools. Neither
surface carries its own parameter list or policy.
"""
from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import Any

from pydantic import BaseModel

from ..services.ingest import KnowledgeIngest
from ..services.qdrant_store import QdrantChunkStore
from ..services import write_policy
from ..services.search import DocumentPage, KnowledgeSearch
from ..services.write_policy import WritePolicy
from . import schemas


class Services:
    """Lazily built services, shared by every surface in one process.

    The read MCP only ever touches `.search`, so it never opens a writer.
    """

    def __init__(
        self, ingest: KnowledgeIngest | None = None, search: KnowledgeSearch | None = None
    ) -> None:
        self._ingest = ingest
        self._search = search

    @property
    def ingest(self) -> KnowledgeIngest:
        if self._ingest is None:
            self._ingest = KnowledgeIngest()
        return self._ingest

    @property
    def search(self) -> KnowledgeSearch:
        if self._search is None:
            if self._ingest is not None:
                # Same client as the writer; the collection must exist first.
                self._ingest._prepare()
                self._search = KnowledgeSearch(QdrantChunkStore(self._ingest.client))
            else:
                self._search = KnowledgeSearch()
        return self._search


Handler = Callable[[Services, Any, "WritePolicy | None"], Any]


@dataclass(frozen=True)
class Operation:
    operation_id: str
    summary: str
    description: str
    input_model: type[BaseModel]
    handler: Handler
    scope: str
    tag: str


def _search(svc: Services, req: schemas.SearchRequest, _policy: WritePolicy | None):
    return svc.search.search(req.query, req.k, path=req.path, source_type=req.source_type)


def _get_document(
    svc: Services, req: schemas.DocumentPageRequest, _policy: WritePolicy | None
) -> DocumentPage | None:
    return svc.search.document_page(req.path, req.offset, req.limit)


def _store_document(
    svc: Services, req: schemas.StoreDocumentRequest, policy: WritePolicy | None
):
    return write_policy.store(
        svc.ingest,
        policy or write_policy.api_policy(),
        path=req.path,
        markdown=req.markdown,
        source_url=req.source_url,
        source_type=req.source_type,
        title=req.title,
        tags=req.tags,
        force=req.force,
    )


def _document_status(
    svc: Services, req: schemas.DocumentStatusRequest, policy: WritePolicy | None
) -> dict:
    return write_policy.status(svc.ingest, policy or write_policy.api_policy(), req.path)


def _delete_document(
    svc: Services, req: schemas.DocumentStatusRequest, _policy: WritePolicy | None
) -> int:
    return svc.ingest.delete(req.path)


OPERATIONS: dict[str, Operation] = {
    op.operation_id: op
    for op in (
        Operation(
            "kb_search",
            "Semantic search",
            "Semantic search over the knowledge collection. Returns the k most "
            "similar chunks (not whole documents) with path, heading, chunk_index, "
            "score, source_type, source_url, tags and text for citations. Set "
            "`path` to search inside one document, or `source_type` (e.g. "
            '"youtube", "tree") to restrict by origin.',
            schemas.SearchRequest,
            _search,
            scope="read",
            tag="mcp-read",
        ),
        Operation(
            "kb_get_document",
            "Read a stored document",
            "Read a whole stored document, in order, by its `path` from kb_search. "
            "Returns chunks `offset`..`offset+limit-1` stitched into continuous "
            "text. When the response carries `next_offset`, call again with that "
            "offset to read the rest.",
            schemas.DocumentPageRequest,
            _get_document,
            scope="read",
            tag="mcp-read",
        ),
        Operation(
            "kb_store_document",
            "Store (upsert) one markdown document",
            "Store one markdown document in the knowledge tree and index it. `path` "
            "is the document's stable identity, e.g. "
            '"tree/docs/kagent/agent-delegation.md"; writing the same path again '
            "replaces the previous revision. Frontmatter (title, source_url, "
            "source_type, tags) is added if absent for agent writes. Returns a "
            'receipt: status "ingested"|"unchanged"|"empty" plus path, doc_hash '
            "and chunks. Re-sending identical content is a no-op, so retries are safe.",
            schemas.StoreDocumentRequest,
            _store_document,
            scope="write",
            tag="mcp-write",
        ),
        Operation(
            "kb_document_status",
            "Indexed revision of a path",
            "Report whether a path is indexed and which revision (doc_hash) it "
            "holds. Use before writing to avoid duplicate work, and after writing "
            "to confirm completion.",
            schemas.DocumentStatusRequest,
            _document_status,
            # Existence + hash only; same exposure as the read plane.
            scope="read",
            tag="mcp-write",
        ),
        Operation(
            "kb_delete_document",
            "Delete every revision of a path",
            "Admin only. Removes all points stored for `path`. Never exposed as an "
            "agent tool.",
            schemas.DocumentStatusRequest,
            _delete_document,
            scope="admin",
            tag="admin",
        ),
    )
}


def run(op_id: str, svc: Services, req: BaseModel, policy: WritePolicy | None = None) -> Any:
    return OPERATIONS[op_id].handler(svc, req, policy)
