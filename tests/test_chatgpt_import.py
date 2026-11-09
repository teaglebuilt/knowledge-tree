from __future__ import annotations

import json
import zipfile

import pytest

from kb import config, import_chatgpt
from kb.archive.chatgpt_store import ChatHistoryStore, chunk_text
from kb.sources import chatgpt
from kb.sources.redact import redact


def _policy(tmp_path):
    p = tmp_path / "policy.yaml"
    p.write_text(
        "exclude_titles: ['therapy']\n"
        "projects:\n  - {pattern: 'homelab', project: homelab}\n"
    )
    return p


def _records(export_zip, policy=None):
    report = chatgpt.Report()
    out = dict(
        (meta["conversation_id"], recs)
        for meta, recs in chatgpt.normalize(
            chatgpt.read_conversations(export_zip, report),
            export="sha256:test", policy=policy, report=report,
        )
    )
    return out, report


def test_reads_every_numbered_file(export_zip):
    convs, report = _records(export_zip)
    assert report.files == ["conversations-000.json", "conversations-001.json"]
    assert set(convs) == {"conv-gpu", "conv-media", "conv-private"}


def test_branches_and_parents_preserved(export_zip):
    convs, _ = _records(export_zip)
    by_id = {r.message_id: r for r in convs["conv-gpu"]}
    assert "m-sys" not in by_id  # visually hidden system prompt skipped
    assert {k for k, r in by_id.items() if r.branch == "current"} == {"m-u1", "m-a1", "m-u2b", "m-a2b"}
    assert {k for k, r in by_id.items() if r.branch == "alternate"} == {"m-u2a", "m-a2a"}
    assert by_id["m-u2a"].parent_message_id == "m-a1"
    assert by_id["m-u2b"].parent_message_id == "m-a1"
    # The hidden system node is not emitted, but provenance still points at it.
    assert by_id["m-u1"].parent_message_id == "m-sys"


def test_missing_timestamp_and_non_text_are_recorded(export_zip):
    convs, report = _records(export_zip)
    media = {r.message_id: r for r in convs["conv-media"]}
    assert media["m-u1"].message_created_at is None
    assert media["m-u1"].unsupported_parts == 1
    assert media["m-u1"].content == "Here is the diagram"
    assert media["m-a1"].content == "exit 0"
    assert report.messages_by_content_type["multimodal_text"] == 1


def test_secrets_redacted_in_records(export_zip):
    convs, report = _records(export_zip)
    text = " ".join(r.content for r in convs["conv-gpu"])
    assert "ghp_" not in text and "hunter2" not in text
    assert report.redactions["github_token"] == 1
    assert report.redactions["assignment"] == 1


@pytest.mark.parametrize("secret,kind", [
    ("AKIAABCDEFGHIJKLMNOP", "aws_access_key"),
    ("sk-ant-api03-abcdefghijklmnopqrstuvwxyz", "anthropic_key"),
    ("postgres://admin:s3cretpw@db:5432/x", "url_credentials"),
    ("-----BEGIN OPENSSH PRIVATE KEY-----\nabc\n-----END OPENSSH PRIVATE KEY-----", "private_key"),
])
def test_redaction_patterns(secret, kind):
    out = redact(f"value {secret} end")
    assert out.counts[kind] == 1
    assert secret not in out.text


def test_policy_excludes_and_tags_project(export_zip, tmp_path):
    policy = chatgpt.Policy.load(_policy(tmp_path))
    convs, report = _records(export_zip, policy)
    assert "conv-private" not in convs
    assert report.conversations_excluded["excluded_title"] == 1
    assert all(r.project == "homelab" for r in convs["conv-gpu"])


def test_dry_run_writes_nothing(export_zip, archive_dir, embedded):
    out = import_chatgpt.run(export_zip, dry_run=True, archive_dir=archive_dir)
    assert out["dry_run"] is True and out["estimated_chunks"] > 0
    assert not archive_dir.exists()
    assert embedded == []


def test_archive_inside_repo_refused(export_zip):
    with pytest.raises(SystemExit):
        import_chatgpt.run(export_zip, dry_run=True, archive_dir=config.ROOT / "tmp-archive")


def test_never_writes_knowledge_collection(qdrant):
    with pytest.raises(RuntimeError):
        ChatHistoryStore(client=qdrant, collection=config.QDRANT_COLLECTION)


def _count(qdrant):
    return qdrant.count(config.CHATGPT_HISTORY_COLLECTION, exact=True).count


def test_import_is_idempotent_and_redacts_before_embedding(
    export_zip, archive_dir, embedded, qdrant, tmp_path
):
    store = ChatHistoryStore(client=qdrant)
    first = import_chatgpt.run(export_zip, archive_dir=archive_dir, store=store,
                               policy_path=_policy(tmp_path))
    assert first["indexed_conversations"] == 2
    n = _count(qdrant)
    assert n == first["points"] > 0
    joined = "\n".join(embedded)
    assert "ghp_" not in joined and "hunter2" not in joined
    assert "search results" not in joined  # tool role recorded, not embedded
    assert "private stuff" not in joined    # excluded by policy

    embedded.clear()
    second = import_chatgpt.run(export_zip, archive_dir=archive_dir, store=store,
                                policy_path=_policy(tmp_path))
    assert second["indexed_conversations"] == 0
    assert second["skipped_unchanged"] == 2
    assert embedded == [] and _count(qdrant) == n

    # Normalized archive is written privately, outside the repo.
    assert (archive_dir / "normalized" / "conv-gpu.jsonl").exists()
    assert oct((archive_dir / "checkpoint.json").stat().st_mode & 0o777) == "0o600"


def test_resume_without_checkpoint_does_not_duplicate(export_zip, archive_dir, embedded, qdrant):
    store = ChatHistoryStore(client=qdrant)
    import_chatgpt.run(export_zip, archive_dir=archive_dir, store=store)
    n = _count(qdrant)
    (archive_dir / "checkpoint.json").unlink()  # simulate crash before checkpoint
    again = import_chatgpt.run(export_zip, archive_dir=archive_dir, store=store)
    assert _count(qdrant) == n
    assert again["messages_upserted"] == 0


def test_edited_message_replaces_old_points(export_zip, archive_dir, embedded, qdrant, tmp_path):
    store = ChatHistoryStore(client=qdrant)
    import_chatgpt.run(export_zip, archive_dir=archive_dir, store=store)
    n = _count(qdrant)

    edited = tmp_path / "edited.zip"
    with zipfile.ZipFile(export_zip) as src, zipfile.ZipFile(edited, "w") as dst:
        for name in src.namelist():
            data = json.loads(src.read(name))
            for conv in data:
                node = conv["mapping"].get("a2b")
                if node:
                    node["message"]["content"]["parts"] = ["Re-bind to vfio-pci instead."]
            dst.writestr(name, json.dumps(data))

    out = import_chatgpt.run(edited, archive_dir=archive_dir, store=store)
    assert out["messages_replaced"] == 1
    assert _count(qdrant) == n
    texts = [p.payload["text"] for p in qdrant.scroll(
        config.CHATGPT_HISTORY_COLLECTION, limit=100)[0]]
    assert "Re-bind to vfio-pci instead." in texts
    assert not any("re-binding the PCI device to nvidia" in t for t in texts)


def test_prune_removes_conversations_absent_from_full_export(
    export_zip, archive_dir, embedded, qdrant, tmp_path
):
    store = ChatHistoryStore(client=qdrant)
    import_chatgpt.run(export_zip, archive_dir=archive_dir, store=store)
    assert "conv-private" in store.stored_conversations()
    out = import_chatgpt.run(export_zip, archive_dir=archive_dir, store=store,
                             policy_path=_policy(tmp_path), prune=True)
    assert out["pruned_conversations"] == 1
    assert "conv-private" not in store.stored_conversations()
    # Policy change (project tag) rewrote payloads without new text.
    projects = {p.payload["project"] for p in qdrant.scroll(
        config.CHATGPT_HISTORY_COLLECTION, limit=100)[0]
        if p.payload["conversation_id"] == "conv-gpu"}
    assert projects == {"homelab"}


def test_chunk_text_windows():
    words = " ".join(f"w{i}" for i in range(1000))
    pieces = chunk_text(words, size=400, overlap=50)
    assert len(pieces) == 3
    assert pieces[1].split()[0] == "w350"
