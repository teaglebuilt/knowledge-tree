#!/usr/bin/env python3
"""
translation_scan.py -- scan the knowledge tree for non-English markdown and
optionally translate it to English with the self-hosted model on the cluster.

Detection and chunking reuse the collect_knowledge skill scripts (mdlang /
lang_scan / verify_translation). This is the batch driver that calls the model
and, with --write, overwrites files in place after the verify gate passes.

Inference goes to the `vllm-selfhosted` backend through svc/ai-gateway in the
`ai` namespace, over its OpenAI-compatible /v1/chat/completions API. There is
no API key. On the 192.168.2.0/24 VLAN the gateway LoadBalancer answers
directly; from anywhere else, port-forward it and point AI_GATEWAY_URL there:

  kubectl port-forward -n ai svc/ai-gateway 8080:80
  AI_GATEWAY_URL=http://127.0.0.1:8080 uv run python scripts/translation_scan.py ...

Usage
-----
  # Report only (no inference)
  uv run python scripts/translation_scan.py tree/

  # Translate + overwrite one file
  uv run python scripts/translation_scan.py path/to/doc.md --write

  # Batch with filters
  uv run python scripts/translation_scan.py tree/ --bucket HEAVY --limit 5 --write
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

SKILL_SCRIPTS = (
    Path(__file__).resolve().parent.parent
    / ".claude"
    / "skills"
    / "collect_knowledge"
    / "scripts"
)
sys.path.insert(0, str(SKILL_SCRIPTS))

from lang_scan import analyse  # noqa: E402
from mdlang import (  # noqa: E402
    SCRIPT_TO_LANGUAGE_HINT,
    discover,
    line_roles,
    load_config,
    paint,
    read_text,
    scan_text,
    severity,
    slugify,
    split_frontmatter,
)
from mdlang import _LINK_RE  # noqa: E402
from verify_translation import verify_one  # noqa: E402

# Must match --served-model-name on the vllm-selfhosted Deployment.
DEFAULT_MODEL = "vllm-selfhosted"
# svc/ai-gateway's LoadBalancer; AI_GATEWAY_URL / --url override it.
DEFAULT_BASE_URL = os.environ["AI_GATEWAY_URL"]
# HTTPRoute prefix that rewrites to the vLLM backend's own root.
ROUTE_PREFIX = "/vllm"
# Qwen2.5-3B-Instruct serves 32k; chunks run ~2.5k in / ~2.1k out, so this is
# ample headroom while staying far from the context limit.
DEFAULT_MAX_TOKENS = 8192
# Translation wants the most likely token, not a creative one.
DEFAULT_TEMPERATURE = 0.0
DEFAULT_TIMEOUT = 600
DEFAULT_PATHS = ["tree"]
# Lines per request. Small batches keep context tight and make one bad line
# cheap to retry on its own.
DEFAULT_BATCH_LINES = 20
# Attempts per line: once inside its batch, then alone.
DEFAULT_LINE_RETRIES = 2

SCRIPTS_DIR = Path(__file__).resolve().parent
PROMPTS_DIR = SCRIPTS_DIR / "translation_prompts"
PROFILES_PATH = SCRIPTS_DIR / "translation_profiles.yaml"

DEFAULT_ROLE_TEMPLATES = {
    "prose": "line_prose.j2",
    "heading": "line_heading.j2",
    "frontmatter": "line_frontmatter.j2",
    "fence_diagram": "line_fence_diagram.j2",
    "mermaid_label": "line_mermaid_label.j2",
    "code_comment": "line_code_comment.j2",
    "code_string": "line_code_string.j2",
    "anchor": "line_anchor.j2",
}
DEFAULT_PHRASE_TEMPLATE = "phrase_repair.j2"
DEFAULT_POSTPROCESS_STEPS = [
    "strip_chunk_comments",
    "ensure_provenance",
    "repair_internal_anchors",
    "fold_english_fullwidth",
]


@dataclass(frozen=True)
class LineJob:
    """One 1-indexed line queued for translation, with its mdlang role."""

    n: int
    role: str


def load_profile(path: Path | None = None) -> dict:
    """Load optional YAML profile overrides (prompts, fence infos, postprocess)."""
    p = path or PROFILES_PATH
    if not p.is_file():
        return {}
    data = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"profile must be a mapping: {p}")
    return data


def merge_config(base: dict, profile: dict) -> dict:
    """Overlay profile keys onto mdlang config (shallow + known nested maps)."""
    cfg = dict(base)
    for key in (
        "diagram_fence_infos",
        "string_fence_langs",
        "comment_prefixes",
        "blocking_categories",
        "warn_categories",
        "translatable_frontmatter",
        "preserve_frontmatter",
    ):
        if key in profile:
            cfg[key] = profile[key]
    cfg["role_templates"] = {
        **DEFAULT_ROLE_TEMPLATES,
        **(profile.get("role_templates") or {}),
    }
    cfg["phrase_template"] = profile.get("phrase_template", DEFAULT_PHRASE_TEMPLATE)
    cfg["postprocess_steps"] = list(
        profile.get("postprocess_steps") or DEFAULT_POSTPROCESS_STEPS
    )
    return cfg


class PromptBank:
    """Jinja-rendered system prompts keyed by line role."""

    def __init__(self, prompts_dir: Path, role_templates: dict[str, str], phrase_template: str) -> None:
        self.env = Environment(
            loader=FileSystemLoader(str(prompts_dir)),
            autoescape=select_autoescape(enabled_extensions=()),
            trim_blocks=True,
            lstrip_blocks=True,
        )
        self.role_templates = role_templates
        self.phrase_template = phrase_template
        self._cache: dict[str, str] = {}

    def for_role(self, role: str) -> str:
        if role not in self._cache:
            name = self.role_templates.get(role) or self.role_templates.get("prose")
            if not name:
                raise KeyError(f"no prompt template for role {role!r}")
            self._cache[role] = self.env.get_template(name).render()
        return self._cache[role]

    def phrase(self) -> str:
        if "_phrase" not in self._cache:
            self._cache["_phrase"] = self.env.get_template(self.phrase_template).render()
        return self._cache["_phrase"]

_NUM_HEADING_RE = re.compile(r"^\s*(\d+)([.\s]|$)")
_CHUNK_COMMENT_RE = re.compile(r"<!--\s*chunk:\s*.*?-->", re.IGNORECASE | re.DOTALL)
_HTML_COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
# Ideographs + kana/hangul/cyrillic/… plus the Fullwidth / CJK-punctuation
# blocks. Qwen routinely leaves `：` / `（` in otherwise-English lines; those
# must fail `_line_problem` (and get folded to ASCII by `_clean_translated`).
_NON_LATIN_RE = re.compile(
    r"[\u0400-\u04FF\u0590-\u05FF\u0600-\u06FF\u0900-\u097F"
    r"\u3000-\u303F\u3040-\u30FF\u3400-\u9FFF\uAC00-\uD7AF"
    r"\uF900-\uFAFF\uFE30-\uFE4F\uFF00-\uFFEF]"
)
# Ideographs only — used to decide whether a line is still Chinese prose
# (keep its punctuation) vs English (fold fullwidth punct to ASCII).
_CJK_IDEOGRAPH_RE = re.compile(r"[\u3400-\u9FFF\uF900-\uFAFF]")
_CJK_PUNCT_TO_ASCII = str.maketrans(
    {
        "\u3000": " ",  # ideographic space
        "\u3001": ",",  # 、
        "\u3002": ".",  # 。
        "\u3008": "<",  # 〈
        "\u3009": ">",  # 〉
        "\u300a": '"',  # 《
        "\u300b": '"',  # 》
        "\u300c": '"',  # 「
        "\u300d": '"',  # 」
        "\u300e": '"',  # 『
        "\u300f": '"',  # 』
        "\u3010": "[",  # 【
        "\u3011": "]",  # 】
        "\u3014": "(",  # 〔
        "\u3015": ")",  # 〕
        "\u30fb": "·",  # ・
        "\uff5e": "~",  # ～ (fullwidth tilde; outside FF01-FF5E map)
    }
)

# TOC corpora often number sections with Arabic, Roman, or Chinese numerals.
_CN_NUM = {
    "一": "1",
    "二": "2",
    "三": "3",
    "四": "4",
    "五": "5",
    "六": "6",
    "七": "7",
    "八": "8",
    "九": "9",
    "十": "10",
    "十一": "11",
    "十二": "12",
    "十三": "13",
    "十四": "14",
    "十五": "15",
}
_ROMAN_NUM = {
    "I": "1",
    "II": "2",
    "III": "3",
    "IV": "4",
    "V": "5",
    "VI": "6",
    "VII": "7",
    "VIII": "8",
    "IX": "9",
    "X": "10",
    "XI": "11",
    "XII": "12",
}
_SECTION_NUM_RE = re.compile(
    r"^(?:(\d+)|([IVX]{1,5})|([一二三四五六七八九十]{1,3}))"
    r"(?:[.\s、．]|$)",
    re.IGNORECASE,
)


def is_book_path(path: Path) -> bool:
    return "books" in path.parts


def language_label(script: str | None) -> str:
    if not script:
        return "unknown"
    hint = SCRIPT_TO_LANGUAGE_HINT.get(script, script)
    # Prefer a short token for frontmatter.
    if "Chinese" in hint:
        return "Chinese"
    if "Japanese" in hint:
        return "Japanese"
    if "Korean" in hint:
        return "Korean"
    if "Russian" in hint:
        return "Russian"
    return hint.split()[0]


def _set_fm_keys(text: str, updates: dict[str, str]) -> str:
    """Set or refresh YAML frontmatter keys; keep all existing keys/order."""
    fm, body, _ = split_frontmatter(text)
    if fm is None:
        block = "\n".join(f"{k}: {v}" for k, v in updates.items())
        return f"---\n{block}\n---\n{text}"
    lines = fm.split("\n")
    out: list[str] = []
    seen: set[str] = set()
    for line in lines:
        replaced = False
        for key, val in updates.items():
            if line.startswith(f"{key}:"):
                out.append(f"{key}: {val}")
                seen.add(key)
                replaced = True
                break
        if not replaced:
            out.append(line)
    for key, val in updates.items():
        if key not in seen:
            out.append(f"{key}: {val}")
    return "---\n" + "\n".join(out) + "\n---\n" + body


def ensure_provenance(text: str, lang: str, source_path: str) -> str:
    return _set_fm_keys(
        text,
        {
            "original_language": lang,
            "source_path": source_path,
        },
    )


def _section_number(text: str) -> str | None:
    """Extract a normalized section number (Arabic digits) from label/heading/slug."""
    s = text.strip()
    m = _SECTION_NUM_RE.match(s)
    if not m:
        # Slugs like "6-最佳实践" or "三内容生产"
        m = re.match(
            r"^(?:(\d+)|([IVX]{1,5})|([一二三四五六七八九十]{1,3}))(?:-|$)",
            s,
            re.IGNORECASE,
        )
    if not m:
        return None
    if m.group(1):
        return str(int(m.group(1)))
    if m.lastindex >= 2 and m.group(2):
        return _ROMAN_NUM.get(m.group(2).upper())
    if m.lastindex >= 3 and m.group(3):
        return _CN_NUM.get(m.group(3))
    return None


def _heading_slugs(text: str) -> tuple[list[str], set[str], dict[str, str]]:
    """
    Returns (slugs_in_order, avail, number_to_slug).

    number_to_slug maps leading section numbers ("1", "2", …) to the first
    *major* heading (e.g. "1. Foo", not "1.1 Foo").
    """
    doc = paint(text)
    counts: dict[str, int] = {}
    ordered: list[str] = []
    by_number: dict[str, str] = {}
    for _, htext, _ in doc.headings:
        base = slugify(htext)
        n = counts.get(base, 0)
        counts[base] = n + 1
        slug = base if n == 0 else f"{base}-{n}"
        ordered.append(slug)
        stripped = htext.strip()
        # Major sections: "1. Title" / "1 Title" — not "1.1 Title".
        major = re.match(r"^(\d+)\.\s+\S", stripped) or re.match(r"^(\d+)\s+[A-Za-z\u4e00-\u9fff]", stripped)
        if major:
            by_number.setdefault(major.group(1).lstrip("0") or "0", slug)
            continue
        num = _section_number(stripped)
        if num:
            by_number.setdefault(num, slug)
    return ordered, set(ordered), by_number


def strip_chunk_comments(text: str) -> str:
    """Drop collection markers and any HTML comments that still hold non-Latin text."""
    text = _CHUNK_COMMENT_RE.sub("", text)

    def _scrub(m: re.Match[str]) -> str:
        return "" if _NON_LATIN_RE.search(m.group(0)) else m.group(0)

    return _HTML_COMMENT_RE.sub(_scrub, text)


def normalize_source(text: str) -> str:
    """
    Normalize before translate + structure verify.

    Collection markers are glued onto headings (`<!-- chunk: X -->## X`).
    mdlang does not count those lines as headings, but the model emits real
    `##` headings — verify then reports "headings added". Strip markers first
    so original and translation share the same outline.

    Also repair a missing newline after the opening `---` fence (`---title:`),
    which otherwise makes `split_frontmatter` miss the block and causes
    provenance to prepend a second frontmatter.
    """
    if text.startswith("---") and len(text) > 3 and text[3] not in "\r\n":
        text = "---\n" + text[3:]
    return strip_chunk_comments(text)


def repair_internal_anchors(text: str) -> str:
    """
    Rewrite in-document `#anchor` targets so they resolve to real headings.

    Prefer: valid slug, slugify(label), section number (Arabic/Roman/Chinese),
    suffix match. Unresolvable hash links become plain label text so verify
    does not fail on ghost TOC entries.
    """
    ordered, avail, by_number = _heading_slugs(text)
    if not ordered:
        return text

    doc = paint(text)
    body_lines = doc.body.split("\n")
    fence_lines: set[int] = set()
    for fr in doc.fences:
        fence_lines.update(range(fr.start_line, min(fr.end_line + 1, len(body_lines))))

    def resolve(label: str, target: str) -> str | None:
        if target in avail:
            return target
        for candidate in (
            slugify(label),
            slugify(re.sub(r"^(?:\d+|[IVX]+|[一二三四五六七八九十]+)[.\s、．]+", "", label, flags=re.I)),
        ):
            if candidate and candidate in avail:
                return candidate
        for raw in (target, label):
            num = _section_number(raw)
            if num and num in by_number:
                return by_number[num]
        label_slug = slugify(label)
        if label_slug:
            for slug in ordered:
                if slug == label_slug or slug.endswith("-" + label_slug):
                    return slug
            # Fuzzy: all latin tokens from label appear in slug
            tokens = [t for t in re.split(r"[^a-z0-9]+", label_slug) if len(t) > 2]
            if tokens:
                for slug in ordered:
                    if all(t in slug for t in tokens):
                        return slug
        return None

    new_lines: list[str] = []
    for ln, line in enumerate(body_lines):
        if ln in fence_lines or "](#" not in line:
            new_lines.append(line)
            continue

        def _sub(m: re.Match[str]) -> str:
            full = m.group(0)
            if full.startswith("!"):
                return full
            label, dest = m.group(1), m.group(2)
            if not dest.startswith("#"):
                return full
            fixed = resolve(label, dest[1:])
            if fixed is None:
                # Ghost TOC / unmapped section — keep readable text, drop dead href.
                return label
            title = m.group(3) or ""
            return f"[{label}](#{fixed}{title})"

        new_lines.append(_LINK_RE.sub(_sub, line))

    fm = doc.frontmatter
    body = "\n".join(new_lines)
    if fm is None:
        return body
    return f"---\n{fm}\n---\n{body}"


def fold_fullwidth_punctuation(text: str) -> str:
    """
    Map fullwidth / CJK punctuation to ASCII.

    Small CJK-trained models keep `：` `（` `）` etc. after translating the
    words around them. mdlang flags those as blocking Fullwidth/CJK-Punctuation
    findings, so the verify gate rejects an otherwise-good file.
    """
    chars: list[str] = []
    for i, ch in enumerate(text):
        cp = ord(ch)
        # Fullwidth ASCII graphic variants (！＂＃ … ／：； … ～).
        if 0xFF01 <= cp <= 0xFF5E:
            ascii_ch = chr(cp - 0xFEE0)
            chars.append(ascii_ch)
            # CJK `：word` has no space; English wants `: word`. Skip URLs (`://`).
            if (
                ascii_ch in ":,;"
                and i + 1 < len(text)
                and text[i + 1] not in " \t\n/"
                and (text[i + 1].isalnum() or ord(text[i + 1]) > 127)
            ):
                chars.append(" ")
        else:
            chars.append(ch)
    return "".join(chars).translate(_CJK_PUNCT_TO_ASCII)


def fold_english_fullwidth(text: str, **_kwargs: object) -> str:
    """Fold fullwidth punct on English-only lines (CJK ideograph lines kept)."""
    out: list[str] = []
    for line in text.split("\n"):
        if _CJK_IDEOGRAPH_RE.search(line):
            out.append(line)
        else:
            out.append(fold_fullwidth_punctuation(line))
    return "\n".join(out)


def _step_strip_chunk_comments(text: str, **_kwargs: object) -> str:
    return strip_chunk_comments(text)


def _step_ensure_provenance(text: str, *, lang: str, source_path: str, **_kwargs: object) -> str:
    return ensure_provenance(text, lang, source_path)


def _step_repair_internal_anchors(text: str, **_kwargs: object) -> str:
    return repair_internal_anchors(text)


POSTPROCESS_REGISTRY = {
    "strip_chunk_comments": _step_strip_chunk_comments,
    "ensure_provenance": _step_ensure_provenance,
    "repair_internal_anchors": _step_repair_internal_anchors,
    "fold_english_fullwidth": fold_english_fullwidth,
}


def run_postprocess(
    text: str,
    steps: list[str],
    *,
    lang: str,
    source_path: str,
) -> str:
    """Apply named postprocess steps in order (config/profile driven)."""
    ctx = {"lang": lang, "source_path": source_path}
    for name in steps:
        fn = POSTPROCESS_REGISTRY.get(name)
        if fn is None:
            raise KeyError(f"unknown postprocess step: {name!r}")
        text = fn(text, **ctx)
    return text


def postprocess_translation(
    text: str,
    lang: str,
    source_path: str,
    steps: list[str] | None = None,
) -> str:
    """Strip markers, repair TOC anchors, stamp provenance, fold leftover FW punct."""
    return run_postprocess(
        text,
        steps or DEFAULT_POSTPROCESS_STEPS,
        lang=lang,
        source_path=source_path,
    )


class GatewayError(RuntimeError):
    """The ai-gateway or the vLLM backend could not be reached, or refused."""


class VllmClient:
    """Minimal OpenAI-compatible chat client for the self-hosted vLLM backend."""

    def __init__(
        self,
        base_url: str,
        model: str,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
        timeout: int = DEFAULT_TIMEOUT,
    ) -> None:
        self.base = base_url.rstrip("/")
        self.model = model
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.timeout = timeout

    @property
    def endpoint(self) -> str:
        return f"{self.base}{ROUTE_PREFIX}"

    def _get_json(self, path: str, timeout: int) -> dict:
        try:
            with urllib.request.urlopen(f"{self.endpoint}{path}", timeout=timeout) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            raise GatewayError(f"HTTP {exc.code} from {path}: {exc.read().decode()[:400]}") from exc
        except urllib.error.URLError as exc:
            raise GatewayError(f"cannot reach {self.endpoint}: {exc.reason}") from exc

    def _post_json(self, path: str, payload: dict) -> dict:
        req = urllib.request.Request(
            f"{self.endpoint}{path}",
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as exc:
            raise GatewayError(f"HTTP {exc.code} from {path}: {exc.read().decode()[:400]}") from exc
        except urllib.error.URLError as exc:
            raise GatewayError(f"cannot reach {self.endpoint}: {exc.reason}") from exc

    def served_models(self) -> list[str]:
        body = self._get_json("/v1/models", timeout=20)
        return [m.get("id", "") for m in body.get("data") or []]

    def complete(self, system: str, user: str) -> str:
        body = self._post_json(
            "/v1/chat/completions",
            {
                "model": self.model,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                "max_tokens": self.max_tokens,
                "temperature": self.temperature,
            },
        )
        choices = body.get("choices") or []
        if not choices:
            raise GatewayError(f"no choices in response: {str(body)[:300]}")
        choice = choices[0]
        # A truncated chunk would reassemble into a silently incomplete file.
        if choice.get("finish_reason") == "length":
            raise GatewayError(
                f"output hit max_tokens={self.max_tokens} and was truncated - "
                f"lower --max-chunk-lines or raise --max-tokens"
            )
        return (choice.get("message") or {}).get("content") or ""


_BLOCK_SCRIPT_RE = _NON_LATIN_RE
_HAS_TEXT_RE = re.compile(r"[0-9A-Za-z]|" + _NON_LATIN_RE.pattern)
# Small models sometimes omit the tab before CJK (`3专线_access`), or echo the
# two-char sequence `\t` instead of a real tab. Allow a bare number only when
# the next char is non-ASCII — not before `.` / `[` / Latin, which would
# false-match ordinary markdown like `8. [Foo](#bar)`.
_REPLY_LINE_RE = re.compile(
    r"^\s*(\d+)(?:\t|\\t| {1,8}|(?=[^\x00-\x7F]))(.*)$"
)
# Loose link matcher for cleanup (mdlang's `_LINK_RE` rejects whitespace in URLs).
_MD_LINK_LOOSE_RE = re.compile(r"(!?)\[([^\]]*)\]\(([^)]+)\)")


def plan_lines(
    text: str,
    config: dict,
    roles_filter: set[str] | None = None,
) -> list[LineJob]:
    """
    Build translation jobs from mdlang roles.

    Only BLOCK-severity categories are queued. Optional `roles_filter` keeps
    only those roles (for debugging a single fence type).
    """
    roles = line_roles(text, config)
    jobs: list[LineJob] = []
    for n in sorted(roles):
        role = roles[n]
        if severity(role, config) != "BLOCK":
            continue
        if roles_filter is not None and role not in roles_filter:
            continue
        jobs.append(LineJob(n, role))
    return jobs


def blocking_lines(text: str, config: dict) -> list[int]:
    """1-indexed line numbers the scanner flags as must-translate."""
    return [j.n for j in plan_lines(text, config)]


_BOX_STRUCT_RE = re.compile(r"[\u2500-\u257F│├└─┌┐┘┤┬┴┼┃┏┓┗┛━]")
_TREE_PREFIX_RE = re.compile(
    r"^(\s*(?:(?:[│|]\s*)?(?:├──|└──|├─|└─|\|--|`──|\+--)\s*)?)"
)
_MERMAID_NODE_RE = re.compile(r"\b([A-Za-z_][\w]*)\s*[\[\(\{]")


def _scaffold(line: str) -> tuple[tuple, str]:
    """Split a line into its markdown scaffolding signature and its prose."""
    rest = line.strip()
    quote = 0
    while rest.startswith(">"):
        quote += 1
        rest = rest[1:].lstrip()
    heading = 0
    m = re.match(r"(#{1,6})\s+", rest)
    if m:
        heading = len(m.group(1))
        rest = rest[m.end() :]
    bullet = bool(re.match(r"[-*+]\s+", rest))
    ordered = bool(re.match(r"\d+[.)]\s+", rest))
    if bullet or ordered:
        rest = re.sub(r"^(?:[-*+]|\d+[.)])\s+", "", rest)
    checkbox = bool(re.match(r"\[[ xX]\]", rest))
    if checkbox:
        rest = rest[3:].lstrip()
    # Cell count matters only for table rows; a stray pipe in prose does not.
    pipes = rest.count("|") if rest.startswith("|") else 0
    return (quote, heading, bullet, ordered, checkbox, pipes), rest


def _diagram_sig(line: str) -> tuple:
    """Structural signature for ASCII/decision-tree diagram lines."""
    indent = len(line) - len(line.lstrip(" "))
    prefix = _TREE_PREFIX_RE.match(line)
    pref = prefix.group(1) if prefix else line[:indent]
    boxes = len(_BOX_STRUCT_RE.findall(line))
    return (indent, pref.replace(" ", "·"), boxes)


def _mermaid_sig(line: str) -> tuple:
    """Node IDs + keyword skeleton for a Mermaid line."""
    ids = tuple(_MERMAID_NODE_RE.findall(line))
    keywords = tuple(
        m.group(0)
        for m in re.finditer(
            r"\b(?:flowchart|graph|subgraph|end|classDef|click|style|TB|LR|BT|RL)\b",
            line,
        )
    )
    edges = len(re.findall(r"-->|---|\-\.->|==>", line))
    return (ids, keywords, edges)


def _clean_translated(text: str) -> str:
    """
    Strip protocol artifacts small models echo into translations.

    The request format is `<n>\\t<text>`; Qwen sometimes re-emits that tab
    inside markdown (especially `#anchors`), which makes `_LINK_RE` miss the
    link because its URL class is `[^)\\s]*`. Collapse whitespace inside link
    destinations so the link still parses; `repair_internal_anchors` rewrites
    the target from the heading label afterwards.

    Also fold fullwidth / CJK punctuation to ASCII — the model translates the
    words but keeps `：` / `（`, which verify flags as residual Fullwidth.
    """
    text = text.replace("\\t", " ").replace("\t", " ")
    text = fold_fullwidth_punctuation(text)

    def _fix_dest(m: re.Match[str]) -> str:
        bang, label, dest = m.group(1), m.group(2), m.group(3).strip()
        title = ""
        tm = re.match(r'^(.*?)(\s+"[^"]*")$', dest)
        if tm:
            dest, title = tm.group(1).strip(), tm.group(2)
        if dest.startswith("#"):
            slug = re.sub(r"[\s]+", "-", dest[1:])
            slug = re.sub(r"-{2,}", "-", slug).strip("-")
            dest = f"#{slug}"
        return f"{bang}[{label}]({dest}{title})"

    return _MD_LINK_LOOSE_RE.sub(_fix_dest, text)


def _line_problem(
    original: str,
    translated: str | None,
    role: str = "prose",
) -> str | None:
    """Why this translated line is unusable, or None when it is fine."""
    if translated is None:
        return "missing from reply"
    if _BLOCK_SCRIPT_RE.search(translated):
        return "still contains source-language text"
    if role == "fence_diagram":
        if _diagram_sig(original) != _diagram_sig(translated):
            return "diagram scaffolding changed"
        if _SEGMENT_SCRIPT_RE.search(original) and not re.search(r"[A-Za-z]", translated):
            return "content dropped"
    elif role == "mermaid_label":
        if _mermaid_sig(original) != _mermaid_sig(translated):
            return "mermaid node/edge skeleton changed"
        if _SEGMENT_SCRIPT_RE.search(original) and not re.search(r"[A-Za-z]", translated):
            return "content dropped"
    else:
        o_sig, o_rest = _scaffold(original)
        t_sig, t_rest = _scaffold(translated)
        if o_sig != t_sig:
            return f"markdown scaffolding changed {o_sig} -> {t_sig}"
        if _HAS_TEXT_RE.search(o_rest) and not _HAS_TEXT_RE.search(t_rest):
            return "content dropped"
        if len(_LINK_RE.findall(original)) != len(_LINK_RE.findall(translated)):
            return "link count changed"
    return None


def _parse_reply(reply: str, wanted: set[int]) -> dict[int, str]:
    """Pull `<number><TAB><text>` pairs out of a reply, ignoring anything else."""
    body = reply.strip()
    if body.startswith("```"):
        parts = body.split("\n", 1)
        body = parts[1] if len(parts) == 2 else ""
        if body.rstrip().endswith("```"):
            body = body.rstrip()[:-3].rstrip()
    out: dict[int, str] = {}
    for raw in body.split("\n"):
        m = _REPLY_LINE_RE.match(raw)
        if not m:
            continue
        n = int(m.group(1))
        # Membership is the guard that makes the loose separator safe.
        if n in wanted and n not in out:
            out[n] = _clean_translated(m.group(2))
    return out


# Script runs worth handing to the phrase model. Punctuation/fullwidth alone is
# folded to ASCII by `_clean_translated` — do not open a segment for `：`.
_SEGMENT_SCRIPT_RE = re.compile(
    r"[\u0400-\u04FF\u0590-\u05FF\u0600-\u06FF\u0900-\u097F"
    r"\u3040-\u30FF\u3400-\u9FFF\uAC00-\uD7AF\uF900-\uFAFF]"
)


def _segments(line: str) -> list[tuple[int, int]]:
    """Maximal spans of source-language text, merging the punctuation between them."""
    hits = [m.start() for m in _SEGMENT_SCRIPT_RE.finditer(line)]
    if not hits:
        return []
    spans: list[list[int]] = [[hits[0], hits[0] + 1]]
    for i in hits[1:]:
        gap = line[spans[-1][1] : i]
        # Keep a phrase whole across CJK punctuation, spaces and digits.
        if len(gap) <= 6 and all(
            c.isspace() or c.isdigit() or c in "\u3001\u3002\uff0c\uff1a\uff1b\uff08\uff09()\u00b7-\u2014/." for c in gap
        ):
            spans[-1][1] = i + 1
        else:
            spans.append([i, i + 1])
    return [(a, b) for a, b in spans]


def _non_latin_count(text: str) -> int:
    return len(_BLOCK_SCRIPT_RE.findall(text))


def _translate_phrases(
    client: VllmClient,
    phrases: list[str],
    prompts: PromptBank,
) -> dict[int, str]:
    """Translate phrases; drop dirty replies and retry misses one at a time."""
    if not phrases:
        return {}
    wanted = list(range(1, len(phrases) + 1))
    got: dict[int, str] = {}
    system = prompts.phrase()

    def ask(indices: list[int]) -> None:
        if not indices:
            return
        payload = "\n".join(f"{i}\t{phrases[i - 1]}" for i in indices)
        try:
            reply = client.complete(system, payload)
        except GatewayError:
            return
        for i, text in _parse_reply(reply, set(indices)).items():
            # Small models occasionally glue escapes (`\dedicated`) or wrap quotes.
            cleaned = text.strip().strip("\\\"'`")
            if not cleaned or _BLOCK_SCRIPT_RE.search(cleaned):
                continue
            got[i] = cleaned

    ask(wanted)
    for i in wanted:
        if i not in got:
            ask([i])
    return got


def _repair_by_segment(
    client: VllmClient,
    line: str,
    prompts: PromptBank,
) -> str | None:
    """
    Translate only the source-language runs inside `line` and substitute them back.

    Last resort for lines the model will not translate as a whole - typically
    residual CJK next to Latin acronyms, or text trapped inside link syntax.
    Prefer calling this on a best-effort partial translation when one exists.
    """
    spans = _segments(line)
    if not spans:
        return None
    phrases = [line[a:b] for a, b in spans]
    got = _translate_phrases(client, phrases, prompts)
    if len(got) != len(phrases):
        return None
    out: list[str] = []
    prev = 0
    for i, (a, b) in enumerate(spans):
        gap = line[prev:a]
        piece = got[i + 1]
        # `VPN` + `专线` → `VPNdedicated` without a spacer; keep tokens readable.
        if gap and piece and gap[-1].isalnum() and piece[0].isalnum():
            piece = " " + piece
        out.append(gap)
        out.append(piece)
        prev = b
    out.append(line[prev:])
    # Phrase text may contain spaces; if it landed inside a `#anchor`, compress
    # those to hyphens so `_LINK_RE` still sees a link.
    return _clean_translated("".join(out))


def _remember_partial(
    best: dict[int, str],
    n: int,
    original: str,
    candidate: str | None,
    role: str,
) -> None:
    """Keep the cleanest scaffold-faithful partial for later segment repair."""
    if candidate is None:
        return
    # Role-specific skeleton must hold; otherwise the partial is unusable.
    if role == "fence_diagram":
        if _diagram_sig(original) != _diagram_sig(candidate):
            return
    elif role == "mermaid_label":
        if _mermaid_sig(original) != _mermaid_sig(candidate):
            return
    else:
        o_sig, _ = _scaffold(original)
        t_sig, _ = _scaffold(candidate)
        if o_sig != t_sig:
            return
    cand_n = _non_latin_count(candidate)
    if cand_n == 0 or cand_n >= _non_latin_count(original):
        return
    prev = best.get(n)
    if prev is None or cand_n < _non_latin_count(prev):
        best[n] = candidate


def translate_lines(
    client: VllmClient,
    lines: list[str],
    jobs: list[LineJob],
    prompts: PromptBank,
    batch_size: int = DEFAULT_BATCH_LINES,
    retries: int = DEFAULT_LINE_RETRIES,
) -> tuple[dict[int, str], dict[int, str], Counter]:
    """
    Translate planned `jobs` (1-indexed line + role).

    Batches are grouped by role so each request uses the matching Jinja system
    prompt. Wire format stays `<number>\\t<text>`.

    Returns (clean_by_line, unresolved_with_reason, role_ok_counts).
    """
    done: dict[int, str] = {}
    problems: dict[int, str] = {}
    best: dict[int, str] = {}
    role_of = {j.n: j.role for j in jobs}
    pending = [j.n for j in jobs]
    role_ok: Counter = Counter()

    for attempt in range(1, retries + 1):
        if not pending:
            break
        # First pass batches for throughput; later passes go one line at a
        # time, which is where the model is most reliable.
        size = batch_size if attempt == 1 else 1
        # Group by role so one system prompt applies to the whole batch.
        by_role: dict[str, list[int]] = defaultdict(list)
        for n in pending:
            by_role[role_of[n]].append(n)
        retry_queue: list[int] = []
        for role, nums in by_role.items():
            groups = [nums[i : i + size] for i in range(0, len(nums), size)]
            system = prompts.for_role(role)
            for group in groups:
                payload = "\n".join(f"{n}\t{lines[n - 1]}" for n in group)
                try:
                    reply = client.complete(system, payload)
                except GatewayError as exc:
                    for n in group:
                        problems[n] = str(exc)
                        retry_queue.append(n)
                    continue
                got = _parse_reply(reply, set(group))
                for n in group:
                    cand = got.get(n)
                    r = role_of[n]
                    _remember_partial(best, n, lines[n - 1], cand, r)
                    why = _line_problem(lines[n - 1], cand, r)
                    if why is None and cand is not None:
                        done[n] = cand
                        problems.pop(n, None)
                        role_ok[r] += 1
                    else:
                        problems[n] = why or "missing from reply"
                        retry_queue.append(n)
        pending = [n for n in retry_queue if n not in done]
        if pending and attempt < retries:
            print(f"    retrying {len(pending)} line(s) individually", flush=True)

    if pending:
        print(f"    segment-repairing {len(pending)} line(s)", flush=True)
        for n in pending:
            # Prefer a near-miss English line (e.g. only `专线` left) over the
            # full Chinese original — fewer, shorter phrases for the model.
            r = role_of[n]
            base = best.get(n, lines[n - 1])
            fixed = _repair_by_segment(client, base, prompts)
            if fixed is not None and _BLOCK_SCRIPT_RE.search(fixed):
                again = _repair_by_segment(client, fixed, prompts)
                if again is not None:
                    fixed = again
            why = _line_problem(lines[n - 1], fixed, r)
            if why is None and fixed is not None:
                done[n] = fixed
                problems.pop(n, None)
                role_ok[r] += 1
            else:
                problems[n] = f"segment repair failed: {why or 'missing from reply'}"

    return done, {n: why for n, why in problems.items() if n not in done}, role_ok


def translate_file(
    client: VllmClient,
    text: str,
    config: dict,
    lang: str,
    source_path: str,
    prompts: PromptBank | None = None,
    roles_filter: set[str] | None = None,
) -> tuple[str, dict[int, str], Counter]:
    """
    Translate the flagged lines and splice them back in place.

    Lines the scanner did not flag are copied byte-for-byte, so heading, list,
    fence and table counts cannot drift - the structural checks in the verify
    gate are satisfied by construction rather than by the model's goodwill.
    """
    lines = text.split("\n")
    jobs = plan_lines(text, config, roles_filter=roles_filter)
    bank = prompts or PromptBank(
        PROMPTS_DIR,
        config.get("role_templates", DEFAULT_ROLE_TEMPLATES),
        config.get("phrase_template", DEFAULT_PHRASE_TEMPLATE),
    )
    steps = config.get("postprocess_steps", DEFAULT_POSTPROCESS_STEPS)
    if not jobs:
        return postprocess_translation(text, lang, source_path, steps), {}, Counter()

    by_role = Counter(j.role for j in jobs)
    role_bits = ", ".join(f"{r}={c}" for r, c in sorted(by_role.items()))
    print(
        f"    {len(jobs)} of {len(lines)} line(s) need translation "
        f"({len(jobs) / len(lines):.0%}) [{role_bits}]",
        flush=True,
    )
    done, problems, role_ok = translate_lines(
        client,
        lines,
        jobs,
        bank,
        config.get("batch_lines", DEFAULT_BATCH_LINES),
        config.get("line_retries", DEFAULT_LINE_RETRIES),
    )
    for n, translated in done.items():
        original = lines[n - 1]
        # Leading spaces carry list/diagram nesting; take from source, not model.
        pad = len(original) - len(original.lstrip(" "))
        lines[n - 1] = original[:pad] + translated.lstrip(" ")
    return (
        postprocess_translation("\n".join(lines), lang, source_path, steps),
        problems,
        role_ok,
    )


def atomic_write(path: Path, content: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(path)


def verify_text(original_text: str, translated_text: str, config: dict, suffix: str = ".md"):
    """Compare translation to an in-memory original (already normalized)."""
    orig_tmp = trans_tmp = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=suffix, encoding="utf-8", delete=False
        ) as fh:
            fh.write(original_text)
            orig_tmp = Path(fh.name)
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=suffix, encoding="utf-8", delete=False
        ) as fh:
            fh.write(translated_text)
            trans_tmp = Path(fh.name)
        return verify_one(trans_tmp, orig_tmp, config)
    finally:
        if orig_tmp is not None:
            orig_tmp.unlink(missing_ok=True)
        if trans_tmp is not None:
            trans_tmp.unlink(missing_ok=True)


def preflight(client: VllmClient) -> None:
    """Fail the batch up front rather than once per file."""
    try:
        models = client.served_models()
    except GatewayError as exc:
        print(
            f"error: {exc}\n"
            f"  on the 192.168.2.0/24 VLAN the gateway answers at {DEFAULT_BASE_URL}\n"
            f"  elsewhere: kubectl port-forward -n ai svc/ai-gateway 8080:80\n"
            f"             then AI_GATEWAY_URL=http://127.0.0.1:8080",
            file=sys.stderr,
        )
        sys.exit(2)
    if client.model not in models:
        print(
            f"error: {client.model!r} is not served at {client.endpoint}\n"
            f"  available: {', '.join(m for m in models if m) or '(none)'}",
            file=sys.stderr,
        )
        sys.exit(2)


def _has_provenance(text: str) -> bool:
    fm, _, _ = split_frontmatter(text)
    if fm is None:
        return False
    keys = {ln.split(":", 1)[0].strip() for ln in fm.split("\n") if ":" in ln}
    return "original_language" in keys


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="translation_scan.py",
        description="Scan tree for non-English markdown; translate on the cluster with --write.",
    )
    ap.add_argument(
        "paths",
        nargs="*",
        default=DEFAULT_PATHS,
        help="files or directories to scan (default: tree)",
    )
    ap.add_argument(
        "--write",
        action="store_true",
        help="translate on the cluster and overwrite in place after verify passes",
    )
    ap.add_argument(
        "--include-books",
        action="store_true",
        help="also process paths under **/books/** (skipped by default)",
    )
    ap.add_argument(
        "--bucket",
        choices=["HEAVY", "PARTIAL", "TRACE"],
        help="only process files in this density bucket",
    )
    ap.add_argument("--limit", type=int, help="max files to translate (with --write)")
    ap.add_argument(
        "--roles",
        help="comma-separated roles to translate (e.g. fence_diagram,mermaid_label)",
    )
    ap.add_argument(
        "--resume",
        action="store_true",
        help="skip files that already have original_language and no blocking findings",
    )
    ap.add_argument(
        "--profile",
        type=Path,
        default=PROFILES_PATH,
        help=f"YAML profile path (default {PROFILES_PATH})",
    )
    ap.add_argument(
        "--model",
        default=os.environ.get("AI_MODEL", DEFAULT_MODEL),
        help=f"served model name (default {DEFAULT_MODEL})",
    )
    ap.add_argument(
        "--url",
        default=os.environ.get("AI_GATEWAY_URL", DEFAULT_BASE_URL),
        help=f"ai-gateway base URL, without {ROUTE_PREFIX} (default {DEFAULT_BASE_URL})",
    )
    ap.add_argument(
        "--max-tokens",
        type=int,
        default=DEFAULT_MAX_TOKENS,
        help=f"completion cap per chunk (default {DEFAULT_MAX_TOKENS})",
    )
    ap.add_argument(
        "--temperature", type=float, default=DEFAULT_TEMPERATURE,
        help=f"sampling temperature (default {DEFAULT_TEMPERATURE})",
    )
    ap.add_argument(
        "--timeout", type=int, default=DEFAULT_TIMEOUT,
        help=f"per-chunk request timeout in seconds (default {DEFAULT_TIMEOUT})",
    )
    ap.add_argument(
        "--batch-lines",
        type=int,
        default=DEFAULT_BATCH_LINES,
        help=f"flagged lines per request (default {DEFAULT_BATCH_LINES})",
    )
    ap.add_argument(
        "--line-retries",
        type=int,
        default=DEFAULT_LINE_RETRIES,
        help=f"attempts per line (default {DEFAULT_LINE_RETRIES})",
    )
    ap.add_argument("--show", type=int, default=5, help="sample blocking lines in report")
    args = ap.parse_args(argv)

    profile = load_profile(args.profile)
    config = merge_config(load_config(), profile)
    config["batch_lines"] = args.batch_lines
    config["line_retries"] = args.line_retries
    roles_filter = (
        {r.strip() for r in args.roles.split(",") if r.strip()} if args.roles else None
    )

    files: list[Path] = []
    for raw in args.paths:
        p = Path(raw).expanduser()
        if not p.exists():
            print(f"error: no such path: {p}", file=sys.stderr)
            return 2
        files.extend(discover(p))
    if not files:
        print("error: no matching files found", file=sys.stderr)
        return 2

    reports = []
    skipped_books = 0
    skipped_resume = 0
    for f in files:
        if not args.include_books and is_book_path(f):
            skipped_books += 1
            continue
        rep = analyse(f, config)
        if args.resume and rep["blocking_chars"] == 0 and _has_provenance(read_text(f)):
            skipped_resume += 1
            continue
        reports.append(rep)

    if args.bucket:
        reports = [r for r in reports if r["bucket"] == args.bucket]

    dirty = [r for r in reports if r["bucket"] != "CLEAN" and r["blocking_chars"] > 0]
    clean_n = sum(1 for r in reports if r["bucket"] == "CLEAN" or r["blocking_chars"] == 0)

    skip_bits = []
    if skipped_books:
        skip_bits.append(f"skipped {skipped_books} books")
    if skipped_resume:
        skip_bits.append(f"resume-skipped {skipped_resume}")
    print(
        f"scanned {len(reports)} file(s)"
        + (f" ({', '.join(skip_bits)})" if skip_bits else "")
    )
    buckets: dict[str, int] = {}
    for r in reports:
        buckets[r["bucket"]] = buckets.get(r["bucket"], 0) + 1
    for b in ("HEAVY", "PARTIAL", "TRACE", "CLEAN"):
        if buckets.get(b):
            print(f"  {b:<8} {buckets[b]}")
    print(f"  {len(dirty)} file(s) need translation; {clean_n} clean")

    role_totals: Counter = Counter()
    for r in dirty:
        print(f"\n{r['path']}")
        print(
            f"  {r['bucket']}  {r['lines_with_non_latin']}/{r['total_lines']} lines  "
            f"({r['language_hint'] or '-'})"
        )
        blocking = [f for f in r["findings"] if f["severity"] == "BLOCK"]
        if roles_filter:
            blocking = [f for f in blocking if f["category"] in roles_filter]
        for f in blocking:
            role_totals[f["category"]] += 1
        for f in blocking[: args.show]:
            print(f"    L{f['line']:<5} {f['category']:<14} {f['text']}")
        if len(blocking) > args.show:
            print(f"    ... {len(blocking) - args.show} more")

    if role_totals:
        print("\nblocking lines by role:")
        for role, n in sorted(role_totals.items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"  {role:<16} {n}")

    if not args.write:
        print("\n(dry-run — pass --write to translate and overwrite)")
        return 0 if not dirty else 1

    if not dirty:
        print("\nnothing to translate")
        return 0

    sys.stdout.flush()
    client = VllmClient(
        base_url=args.url,
        model=args.model,
        max_tokens=args.max_tokens,
        temperature=args.temperature,
        timeout=args.timeout,
    )
    preflight(client)
    prompts = PromptBank(
        PROMPTS_DIR,
        config.get("role_templates", DEFAULT_ROLE_TEMPLATES),
        config.get("phrase_template", DEFAULT_PHRASE_TEMPLATE),
    )

    targets = dirty
    if args.limit is not None:
        targets = dirty[: args.limit]

    translated_ok = 0
    failed = 0
    role_translated: Counter = Counter()
    role_failed_lines: Counter = Counter()
    for r in targets:
        path = Path(r["path"])
        lang = language_label(r["dominant_script"])
        rel = str(path)
        print(f"\ntranslating {path} ({r['bucket']}, {lang}) with {args.model} at {client.endpoint}")
        try:
            # Normalize first so <!-- chunk: -->## Heading lines count as
            # headings in both the source outline and the translation.
            original_text = normalize_source(read_text(path))
            file_config = dict(config)
            # --roles is a scoped pass: only gate residual findings in those roles
            # so unrelated Chinese does not block writing the lines we just fixed.
            if roles_filter is not None:
                file_config["blocking_categories"] = sorted(roles_filter)
            new_text, problems, role_ok = translate_file(
                client,
                original_text,
                file_config,
                lang,
                rel,
                prompts=prompts,
                roles_filter=roles_filter,
            )
            role_translated.update(role_ok)
            if problems:
                print(f"  {len(problems)} line(s) never came back clean:")
                for n, why in sorted(problems.items())[:5]:
                    print(f"    L{n}: {why}")
                # Attribute failures by planned role when possible.
                planned = {j.n: j.role for j in plan_lines(original_text, file_config, roles_filter)}
                for n in problems:
                    role_failed_lines[planned.get(n, "?")] += 1
            result = verify_text(original_text, new_text, file_config, path.suffix or ".md")
            for w in result.warnings:
                print(f"  ! {w}")
            if not result.passed:
                failed += 1
                print(f"  FAIL verify — leaving {path} unchanged")
                for fail in result.failures:
                    print(f"    - {fail}")
                continue
            atomic_write(path, new_text)
            translated_ok += 1
            print(f"  OK wrote {path}")
        except Exception as exc:  # noqa: BLE001 — batch driver continues
            failed += 1
            print(f"  ERROR {path}: {exc}", file=sys.stderr)

    print(f"\ndone: {translated_ok} written, {failed} failed, {len(targets)} attempted")
    if role_translated or role_failed_lines:
        print("lines by role:")
        all_roles = sorted(set(role_translated) | set(role_failed_lines))
        for role in all_roles:
            print(
                f"  {role:<16} ok={role_translated.get(role, 0)}  "
                f"failed={role_failed_lines.get(role, 0)}"
            )
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
