from __future__ import annotations

import hashlib
import json
import re
import zipfile
from collections import Counter
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Iterator

from ... import config
from ...redact import redact

SOURCE = "chatgpt_export"
_CONV_FILE = re.compile(r"(?:^|/)conversations(?:-\d+)?\.json$")
_TEXT_TYPES = {"text", "multimodal_text"}
_CODE_TYPES = {"code", "execution_output"}


@dataclass
class MessageRecord:
    source: str
    export_id: str
    conversation_id: str
    conversation_title: str
    created_at: str | None
    updated_at: str | None
    message_id: str
    parent_message_id: str | None
    role: str
    message_created_at: str | None
    content_type: str
    content: str
    branch: str  # current | alternate
    project: str | None
    privacy_class: str
    redaction_version: str
    redactions: dict[str, int]
    content_sha256: str
    unsupported_parts: int = 0

    def to_json(self) -> str:
        return json.dumps(asdict(self), sort_keys=True, ensure_ascii=False)


@dataclass
class Policy:
    """Inclusion policy. Exclusion wins over every project rule."""

    exclude_titles: list[str] = field(default_factory=list)  # regex, case-insensitive
    exclude_ids: set[str] = field(default_factory=set)
    project_rules: list[tuple[str, str]] = field(default_factory=list)  # (regex, project)
    default_privacy: str = "private"

    @classmethod
    def load(cls, path: Path | None) -> "Policy":
        if not path:
            return cls()
        import yaml

        raw = yaml.safe_load(Path(path).read_text()) or {}
        return cls(
            exclude_titles=list(raw.get("exclude_titles") or []),
            exclude_ids=set(raw.get("exclude_ids") or []),
            project_rules=[(r["pattern"], r["project"]) for r in raw.get("projects") or []],
            default_privacy=str(raw.get("default_privacy") or "private"),
        )

    def excluded(self, conv_id: str, title: str) -> str | None:
        if conv_id in self.exclude_ids:
            return "excluded_id"
        for pat in self.exclude_titles:
            if re.search(pat, title or "", re.IGNORECASE):
                return "excluded_title"
        return None

    def project(self, title: str) -> str | None:
        for pat, project in self.project_rules:
            if re.search(pat, title or "", re.IGNORECASE):
                return project
        return None


@dataclass
class Report:
    conversations: int = 0
    conversations_excluded: Counter = field(default_factory=Counter)
    messages: int = 0
    messages_by_role: Counter = field(default_factory=Counter)
    messages_by_content_type: Counter = field(default_factory=Counter)
    skipped: Counter = field(default_factory=Counter)
    redactions: Counter = field(default_factory=Counter)
    branches: Counter = field(default_factory=Counter)
    files: list[str] = field(default_factory=list)

    def as_dict(self) -> dict:
        return {
            k: (dict(v) if isinstance(v, Counter) else v) for k, v in vars(self).items()
        }


def export_id(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return "sha256:" + h.hexdigest()


def _iso(ts) -> str | None:
    if ts in (None, ""):
        return None
    try:
        return datetime.fromtimestamp(float(ts), tz=timezone.utc).isoformat().replace("+00:00", "Z")
    except (TypeError, ValueError, OverflowError, OSError):
        return None


def read_conversations(path: Path, report: Report | None = None) -> Iterator[dict]:
    """Yield raw conversation dicts from a ZIP or a bare conversations*.json."""
    path = Path(path)
    if path.suffix == ".json":
        if report is not None:
            report.files.append(path.name)
        yield from _as_list(json.loads(path.read_text(encoding="utf-8")))
        return
    with zipfile.ZipFile(path) as zf:
        names = sorted(n for n in zf.namelist() if _CONV_FILE.search(n))
        if not names:
            raise ValueError(f"{path}: no conversations*.json inside the archive")
        for name in names:
            if report is not None:
                report.files.append(name)
            with zf.open(name) as fh:
                yield from _as_list(json.load(fh))


def _as_list(data) -> list[dict]:
    if isinstance(data, list):
        return [c for c in data if isinstance(c, dict)]
    if isinstance(data, dict) and isinstance(data.get("conversations"), list):
        return [c for c in data["conversations"] if isinstance(c, dict)]
    raise ValueError("unrecognized conversations file shape")


def _current_branch(mapping: dict, current: str | None) -> set[str]:
    seen: set[str] = set()
    node = current
    while node and node in mapping and node not in seen:
        seen.add(node)
        node = mapping[node].get("parent")
    return seen


def _render(content: dict) -> tuple[str, int]:
    """Return (text, unsupported_part_count) for a message content object."""
    ctype = content.get("content_type") or "unknown"
    if ctype in _TEXT_TYPES:
        texts, unsupported = [], 0
        for part in content.get("parts") or []:
            if isinstance(part, str):
                texts.append(part)
            elif isinstance(part, dict) and isinstance(part.get("text"), str):
                texts.append(part["text"])
            else:
                unsupported += 1  # image/file asset pointers, audio, ...
        return "\n".join(t for t in texts if t.strip()), unsupported
    if ctype in _CODE_TYPES and isinstance(content.get("text"), str):
        return content["text"], 0
    return "", 1


def normalize(
    conversations: Iterable[dict],
    *,
    export: str,
    policy: Policy | None = None,
    report: Report | None = None,
) -> Iterator[tuple[dict, list[MessageRecord]]]:
    """Yield (conversation_meta, records) per included conversation."""
    policy = policy or Policy()
    report = report if report is not None else Report()
    for conv in conversations:
        conv_id = str(conv.get("conversation_id") or conv.get("id") or "")
        title = str(conv.get("title") or "")
        if not conv_id:
            report.skipped["conversation_without_id"] += 1
            continue
        report.conversations += 1
        reason = policy.excluded(conv_id, title)
        if reason:
            report.conversations_excluded[reason] += 1
            continue
        mapping = conv.get("mapping") or {}
        current = _current_branch(mapping, conv.get("current_node"))
        meta = {
            "conversation_id": conv_id,
            "conversation_title": title,
            "created_at": _iso(conv.get("create_time")),
            "updated_at": _iso(conv.get("update_time")),
            "project": policy.project(title),
        }
        records: list[MessageRecord] = []
        for node_id, node in mapping.items():
            msg = (node or {}).get("message")
            if not msg:
                continue  # synthetic root
            role = str(((msg.get("author") or {}).get("role")) or "unknown")
            content = msg.get("content") or {}
            ctype = str(content.get("content_type") or "unknown")
            report.messages_by_content_type[ctype] += 1
            if (msg.get("metadata") or {}).get("is_visually_hidden_from_conversation"):
                report.skipped["hidden"] += 1
                continue
            text, unsupported = _render(content)
            if not text.strip():
                report.skipped["no_text" if not unsupported else f"unsupported:{ctype}"] += 1
                continue
            red = redact(text)
            report.redactions.update(red.counts)
            message_id = str(msg.get("id") or node_id)
            parent = node.get("parent")
            parent_msg = (mapping.get(parent) or {}).get("message") if parent else None
            branch = "current" if (not current or node_id in current) else "alternate"
            report.branches[branch] += 1
            report.messages += 1
            report.messages_by_role[role] += 1
            records.append(
                MessageRecord(
                    source=SOURCE,
                    export_id=export,
                    message_id=message_id,
                    parent_message_id=(str(parent_msg.get("id")) if parent_msg else None),
                    role=role,
                    message_created_at=_iso(msg.get("create_time")),
                    content_type=ctype,
                    content=red.text,
                    branch=branch,
                    privacy_class=policy.default_privacy,
                    redaction_version=config.CHATGPT_REDACTION_VERSION,
                    redactions=dict(red.counts),
                    content_sha256=hashlib.sha256(red.text.encode("utf-8")).hexdigest(),
                    unsupported_parts=unsupported,
                    **meta,
                )
            )
        records.sort(key=lambda r: (r.message_created_at or "", r.message_id))
        yield meta, records


def conversation_digest(records: list[MessageRecord]) -> str:
    """Content-addressed checkpoint value (edits change it; timestamps do not)."""
    h = hashlib.sha256()
    for r in sorted(records, key=lambda r: r.message_id):
        h.update(f"{r.message_id}:{r.content_sha256}:{r.branch}\n".encode())
    return h.hexdigest()
