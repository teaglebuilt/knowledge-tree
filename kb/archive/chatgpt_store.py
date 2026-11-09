"""Qdrant `chatgpt_history` operations: idempotent message-level upsert.

Same embedding space as `knowledge` (bge-small, 384-d) so one embedder serves
both, but a separate collection: nothing here is visible to kb_search, and
`kb sync` (which prunes `source_type=tree` in `knowledge` only) never sees it.

Identity: one message may span several chunks. Point id is derived from
(conversation, message, content_sha, chunk) so re-importing the same export
is a no-op and an edited message replaces only its own points.
"""
from __future__ import annotations

from dataclasses import dataclass

from .. import config, embed
from ..adapters import qdrant as qd
from ..sources.chatgpt import MessageRecord

INDEXED_FIELDS = (
    "conversation_id", "message_id", "role", "project", "privacy_class",
    "branch", "source", "content_sha256",
)
UPSERT_BATCH = 128


def chunk_text(text: str, size: int | None = None, overlap: int | None = None) -> list[str]:
    """Word-window split for long messages (transcripts have no headings)."""
    size = size or config.CHILD_TOKENS
    overlap = min(overlap if overlap is not None else config.CHILD_OVERLAP, size - 1)
    words = text.split()
    if len(words) <= size:
        return [text.strip()]
    out, step = [], size - overlap
    for start in range(0, len(words), step):
        out.append(" ".join(words[start : start + size]))
        if start + size >= len(words):
            break
    return out


def fingerprint(r: MessageRecord) -> str:
    """Everything that, if changed, must rewrite the message's points.

    Content alone is not enough: a policy change (project, privacy class) or
    a new redaction version must update payloads even when text is identical.
    """
    import hashlib

    key = "|".join([r.content_sha256, r.branch, str(r.project), r.privacy_class,
                    r.redaction_version, str(r.parent_message_id)])
    return hashlib.sha256(key.encode()).hexdigest()


@dataclass
class ConversationResult:
    conversation_id: str
    upserted_messages: int = 0
    unchanged_messages: int = 0
    replaced_messages: int = 0
    removed_messages: int = 0
    points: int = 0


class ChatHistoryStore:
    def __init__(self, client=None, collection: str | None = None) -> None:
        self._client = client or qd.client()
        self.collection = collection or config.CHATGPT_HISTORY_COLLECTION
        if self.collection == config.QDRANT_COLLECTION:
            raise RuntimeError("refusing to write chat history into the knowledge collection")
        self._prepared = False

    def prepare(self) -> None:
        if self._prepared:
            return
        from qdrant_client import models

        qd.ensure_collection(self._client, self.collection, config.EMBED_DIM)
        qd.assert_collection_compatible(self._client, self.collection, config.EMBED_DIM)
        info = self._client.get_collection(self.collection)
        existing = set(getattr(info, "payload_schema", None) or {})
        for field_name in INDEXED_FIELDS:
            if field_name not in existing:
                self._client.create_payload_index(
                    collection_name=self.collection,
                    field_name=field_name,
                    field_schema=models.PayloadSchemaType.KEYWORD,
                    wait=True,
                )
        self._prepared = True

    def _filter(self, **match):
        from qdrant_client import models

        return models.Filter(must=[
            models.FieldCondition(key=k, match=models.MatchValue(value=v))
            for k, v in match.items()
        ])

    def stored_messages(self, conversation_id: str) -> dict[str, str]:
        """message_id -> fingerprint currently indexed for a conversation."""
        out: dict[str, str] = {}
        offset = None
        while True:
            points, offset = self._client.scroll(
                collection_name=self.collection,
                scroll_filter=self._filter(conversation_id=conversation_id),
                limit=256,
                with_payload=["message_id", "fingerprint"],
                with_vectors=False,
                offset=offset,
            )
            for p in points:
                pl = p.payload or {}
                out[str(pl.get("message_id"))] = str(pl.get("fingerprint"))
            if offset is None:
                return out

    def _delete(self, **match) -> None:
        from qdrant_client import models

        self._client.delete(
            collection_name=self.collection,
            points_selector=models.FilterSelector(filter=self._filter(**match)),
            wait=True,
        )

    def upsert_conversation(
        self, records: list[MessageRecord], *, roles: tuple[str, ...] | None = None
    ) -> ConversationResult:
        from qdrant_client import models

        self.prepare()
        roles = roles or config.CHATGPT_INDEX_ROLES
        indexable = [r for r in records if r.role in roles]
        conv_id = records[0].conversation_id if records else ""
        result = ConversationResult(conv_id)
        if not records:
            return result
        stored = self.stored_messages(conv_id)
        wanted = {r.message_id: fingerprint(r) for r in indexable}

        # Messages gone from this conversation (deleted branch, role filter
        # change) are removed; edited ones are replaced below.
        for message_id in set(stored) - set(wanted):
            self._delete(conversation_id=conv_id, message_id=message_id)
            result.removed_messages += 1

        todo: list[MessageRecord] = []
        for r in indexable:
            prior = stored.get(r.message_id)
            if prior == wanted[r.message_id]:
                result.unchanged_messages += 1
                continue
            if prior is not None:
                self._delete(conversation_id=conv_id, message_id=r.message_id)
                result.replaced_messages += 1
            todo.append(r)

        batch: list = []
        for r in todo:
            pieces = chunk_text(r.content)
            header = f"{r.conversation_title}\n{r.role}: "
            vectors = embed.embed([header + p for p in pieces])
            for idx, (piece, vector) in enumerate(zip(pieces, vectors)):
                key = f"chatgpt::{r.conversation_id}::{r.message_id}::{wanted[r.message_id][:12]}::{idx}"
                payload = {
                    "source": r.source,
                    "source_type": r.source,
                    "export_id": r.export_id,
                    "conversation_id": r.conversation_id,
                    "conversation_title": r.conversation_title,
                    "message_id": r.message_id,
                    "parent_message_id": r.parent_message_id,
                    "role": r.role,
                    "branch": r.branch,
                    "created_at": r.created_at,
                    "updated_at": r.updated_at,
                    "message_created_at": r.message_created_at,
                    "content_type": r.content_type,
                    "project": r.project,
                    "privacy_class": r.privacy_class,
                    "redaction_version": r.redaction_version,
                    "content_sha256": r.content_sha256,
                    "fingerprint": wanted[r.message_id],
                    "chunk_index": idx,
                    "chunk_count": len(pieces),
                    "text": piece,
                }
                batch.append(models.PointStruct(id=qd.point_id(key), vector=list(vector), payload=payload))
                if len(batch) >= UPSERT_BATCH:
                    self._client.upsert(self.collection, points=batch, wait=True)
                    result.points += len(batch)
                    batch = []
            result.upserted_messages += 1
        if batch:
            self._client.upsert(self.collection, points=batch, wait=True)
            result.points += len(batch)
        return result

    def stored_conversations(self) -> set[str]:
        ids: set[str] = set()
        offset = None
        while True:
            points, offset = self._client.scroll(
                collection_name=self.collection, limit=1024,
                with_payload=["conversation_id"], with_vectors=False, offset=offset,
            )
            ids.update(str((p.payload or {}).get("conversation_id")) for p in points)
            if offset is None:
                return ids

    def delete_conversation(self, conversation_id: str) -> None:
        self._delete(conversation_id=conversation_id)
