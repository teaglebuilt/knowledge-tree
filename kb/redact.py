from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field

_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("private_key", re.compile(
        r"-----BEGIN [A-Z0-9 ]*PRIVATE KEY-----.*?-----END [A-Z0-9 ]*PRIVATE KEY-----",
        re.DOTALL)),
    ("aws_access_key", re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b")),
    ("github_token", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{40,})\b")),
    ("anthropic_key", re.compile(r"\bsk-ant-[A-Za-z0-9_\-]{20,}")),
    ("openai_key", re.compile(r"\bsk-(?:proj-|svcacct-)?[A-Za-z0-9_\-]{20,}")),
    ("slack_token", re.compile(r"\bxox[abposr]-[A-Za-z0-9-]{10,}")),
    ("google_api_key", re.compile(r"\bAIza[0-9A-Za-z_\-]{35}\b")),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_\-]{8,}\.eyJ[A-Za-z0-9_\-]{8,}\.[A-Za-z0-9_\-]{8,}")),
    ("bearer", re.compile(r"(?i)\bbearer\s+[A-Za-z0-9._~+/\-]{20,}=*")),
    ("url_credentials", re.compile(r"(?i)\b([a-z][a-z0-9+.\-]*://)[^\s:/@]+:[^\s@/]+@")),
    # key = value / key: value for secret-ish keys; keeps the key, drops the value.
    ("assignment", re.compile(
        r"(?i)\b((?:api[_-]?key|secret(?:[_-]?key)?|password|passwd|token|access[_-]?key"
        r"|client[_-]?secret|auth[_-]?token)\b[\"']?\s*[:=]\s*)[\"']?[^\s\"',;]{6,}[\"']?")),
)


@dataclass
class Redaction:
    text: str
    counts: Counter = field(default_factory=Counter)

    @property
    def redacted(self) -> bool:
        return bool(self.counts)


def redact(text: str) -> Redaction:
    counts: Counter = Counter()
    out = text or ""
    for kind, pattern in _PATTERNS:
        def _sub(m: re.Match[str], kind: str = kind) -> str:
            counts[kind] += 1
            if kind == "assignment":
                return f"{m.group(1)}[REDACTED:{kind}]"
            if kind == "url_credentials":
                return f"{m.group(1)}[REDACTED:{kind}]@"
            return f"[REDACTED:{kind}]"

        out = pattern.sub(_sub, out)
    return Redaction(out, counts)
