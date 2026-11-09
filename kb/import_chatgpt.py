"""`python -m kb import-chatgpt FILE` — ChatGPT export -> private archive + chatgpt_history.

Pipeline per conversation: parse -> policy filter -> redact -> write normalized
JSONL to the private archive -> idempotent upsert into Qdrant -> checkpoint.

Resumable: the checkpoint maps conversation_id -> content digest and is
written after each conversation, so an interrupted run resumes where it
stopped and a newer export only re-embeds conversations whose content changed
(timestamps alone are not trusted to detect edits).
"""
from __future__ import annotations

import json
import os
import sys
import tempfile
from pathlib import Path

from . import config
from .sources import chatgpt


def _inside_repo(path: Path) -> bool:
    try:
        path.resolve().relative_to(config.ROOT.resolve())
        return True
    except ValueError:
        return False


def _atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=path.parent, prefix=f".{path.name}.")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(text)
    os.chmod(tmp, 0o600)
    os.replace(tmp, path)


def run(
    file: Path,
    *,
    dry_run: bool = False,
    policy_path: Path | None = None,
    archive_dir: Path | None = None,
    prune: bool = False,
    limit: int | None = None,
    store=None,
) -> dict:
    file = Path(file).expanduser()
    archive = Path(archive_dir or config.ARCHIVE_DIR).expanduser()
    if _inside_repo(archive):
        raise SystemExit(
            f"archive dir {archive} is inside the (public) repo; set KB_ARCHIVE_DIR elsewhere"
        )
    policy = chatgpt.Policy.load(policy_path)
    report = chatgpt.Report()
    export = chatgpt.export_id(file)

    checkpoint_path = archive / "checkpoint.json"
    checkpoint: dict[str, str] = (
        json.loads(checkpoint_path.read_text()) if checkpoint_path.exists() else {}
    )
    totals = {"indexed_conversations": 0, "skipped_unchanged": 0, "points": 0,
              "messages_upserted": 0, "messages_replaced": 0, "messages_removed": 0,
              "estimated_chunks": 0, "pruned_conversations": 0}
    seen: set[str] = set()

    if not dry_run:
        archive.mkdir(parents=True, exist_ok=True)
        os.chmod(archive, 0o700)
        if store is None:
            from .archive.chatgpt_store import ChatHistoryStore

            store = ChatHistoryStore()
        store.prepare()

    from .archive.chatgpt_store import chunk_text

    convs = chatgpt.read_conversations(file, report)
    for n, (meta, records) in enumerate(
        chatgpt.normalize(convs, export=export, policy=policy, report=report)
    ):
        if limit is not None and n >= limit:
            break
        conv_id = meta["conversation_id"]
        seen.add(conv_id)
        indexable = [r for r in records if r.role in config.CHATGPT_INDEX_ROLES]
        totals["estimated_chunks"] += sum(len(chunk_text(r.content)) for r in indexable)
        if dry_run:
            continue
        # Policy/redaction changes must also invalidate the checkpoint.
        digest = ":".join([
            config.CHATGPT_REDACTION_VERSION,
            ",".join(config.CHATGPT_INDEX_ROLES),
            str(meta.get("project")),
            policy.default_privacy,
            chatgpt.conversation_digest(records),
        ])
        if checkpoint.get(conv_id) == digest:
            totals["skipped_unchanged"] += 1
            continue
        _atomic_write(
            archive / "normalized" / f"{conv_id}.jsonl",
            "".join(r.to_json() + "\n" for r in records),
        )
        result = store.upsert_conversation(records)
        totals["indexed_conversations"] += 1
        totals["points"] += result.points
        totals["messages_upserted"] += result.upserted_messages
        totals["messages_replaced"] += result.replaced_messages
        totals["messages_removed"] += result.removed_messages
        checkpoint[conv_id] = digest
        _atomic_write(checkpoint_path, json.dumps(checkpoint, sort_keys=True))

    if prune and not dry_run and limit is None:
        # Only meaningful against a FULL export: anything indexed but absent
        # (deleted in ChatGPT, or newly excluded by policy) is removed.
        for conv_id in store.stored_conversations() - seen:
            store.delete_conversation(conv_id)
            checkpoint.pop(conv_id, None)
            totals["pruned_conversations"] += 1
        _atomic_write(checkpoint_path, json.dumps(checkpoint, sort_keys=True))

    out = {"export_id": export, "dry_run": dry_run,
           "collection": config.CHATGPT_HISTORY_COLLECTION,
           "archive_dir": str(archive), **report.as_dict(), **totals}
    if not dry_run:
        _atomic_write(archive / "reports" / f"{export.split(':')[-1][:16]}.json",
                      json.dumps(out, indent=2, sort_keys=True))
    return out


def main(argv: list[str] | None = None) -> int:
    import argparse

    p = argparse.ArgumentParser(prog="kb import-chatgpt")
    p.add_argument("file", type=Path, help="ChatGPT export ZIP (or conversations*.json)")
    p.add_argument("--dry-run", action="store_true", help="parse, classify, count; write nothing")
    p.add_argument("--policy", type=Path, help="YAML: exclude_titles, exclude_ids, projects")
    p.add_argument("--archive-dir", type=Path, help=f"default {config.ARCHIVE_DIR}")
    p.add_argument("--prune", action="store_true",
                   help="delete indexed conversations absent from this (full) export")
    p.add_argument("--limit", type=int, help="process only the first N conversations")
    a = p.parse_args(argv)
    out = run(a.file, dry_run=a.dry_run, policy_path=a.policy,
              archive_dir=a.archive_dir, prune=a.prune, limit=a.limit)
    json.dump(out, sys.stdout, indent=2, sort_keys=True)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
