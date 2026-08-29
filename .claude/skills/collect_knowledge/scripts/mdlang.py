#!/usr/bin/env python3
"""
mdlang.py -- markdown + language primitives shared by the collect_knowledge skill.

Why this exists
---------------
A plain `grep -P '[\\x{4e00}-\\x{9fff}]'` cannot tell the difference between:

    这是一段还没翻译的正文              <- a paragraph nobody translated
    [文档](https://example.com/文档)     <- a URL that must NEVER be translated
    [[notes/index.md|返回目录]]          <- target must stay, alias must translate
    ](#1-供应链安全简介)                  <- an anchor that must be REGENERATED

Treating those four the same produces either false alarms (blocking on URLs) or
false confidence (passing a file whose whole body is untranslated). So this
module paints a document into categories and reports non-Latin text per
category, which is what lets the scanner and the verifier make useful calls.

Nothing here is specific to any repository or language pair. Callers supply
paths and, optionally, a config dict; the defaults are meant to be reasonable
for any markdown corpus.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

# --------------------------------------------------------------------------
# Script detection
# --------------------------------------------------------------------------
# Ranges chosen to cover the scripts that realistically show up in technical
# documentation corpora. Greek is deliberately absent: alpha/beta/sigma appear
# constantly in legitimately-English math and would generate endless noise.

SCRIPT_RANGES: list[tuple[int, int, str]] = [
    (0x0400, 0x04FF, "Cyrillic"),
    (0x0500, 0x052F, "Cyrillic"),
    (0x0590, 0x05FF, "Hebrew"),
    (0x0600, 0x06FF, "Arabic"),
    (0x0750, 0x077F, "Arabic"),
    (0x0900, 0x097F, "Devanagari"),
    (0x0980, 0x09FF, "Bengali"),
    (0x0E00, 0x0E7F, "Thai"),
    (0x1100, 0x11FF, "Hangul"),
    (0x3000, 0x303F, "CJK-Punctuation"),
    (0x3040, 0x309F, "Hiragana"),
    (0x30A0, 0x30FF, "Katakana"),
    (0x3400, 0x4DBF, "CJK"),
    (0x4E00, 0x9FFF, "CJK"),
    (0xA960, 0xA97F, "Hangul"),
    (0xAC00, 0xD7AF, "Hangul"),
    (0xD7B0, 0xD7FF, "Hangul"),
    (0xF900, 0xFAFF, "CJK"),
    (0xFE30, 0xFE4F, "CJK-Punctuation"),
    (0xFF00, 0xFFEF, "Fullwidth"),
    (0x20000, 0x2A6DF, "CJK"),
]

# Fullwidth digits/latin live in the Fullwidth block and signal CJK authoring,
# but the block also holds halfwidth katakana and a few neutral forms. Keep it.

_SCRIPT_CACHE: dict[str, str | None] = {}


def script_of(ch: str) -> str | None:
    """Return the script name for a non-Latin character, or None if Latin/neutral."""
    cached = _SCRIPT_CACHE.get(ch)
    if cached is not None or ch in _SCRIPT_CACHE:
        return cached
    cp = ord(ch)
    result = None
    for lo, hi, name in SCRIPT_RANGES:
        if lo <= cp <= hi:
            result = name
            break
    _SCRIPT_CACHE[ch] = result
    return result


def dominant_script(text: str) -> str | None:
    """The most frequent non-Latin script in `text`, or None if there is none."""
    counts: dict[str, int] = {}
    for ch in text:
        s = script_of(ch)
        if s and s not in ("CJK-Punctuation", "Fullwidth"):
            counts[s] = counts.get(s, 0) + 1
    if not counts:
        # Fall back to punctuation-only evidence (a doc of pure 。、「」 is odd
        # but still not English).
        for ch in text:
            s = script_of(ch)
            if s:
                counts[s] = counts.get(s, 0) + 1
    if not counts:
        return None
    return max(counts.items(), key=lambda kv: kv[1])[0]


# Human-friendly names for report output.
SCRIPT_TO_LANGUAGE_HINT = {
    "CJK": "Chinese (or Japanese kanji)",
    "Hiragana": "Japanese",
    "Katakana": "Japanese",
    "Hangul": "Korean",
    "Cyrillic": "Russian (or another Cyrillic language)",
    "Arabic": "Arabic",
    "Hebrew": "Hebrew",
    "Devanagari": "Hindi (or another Devanagari language)",
    "Bengali": "Bengali",
    "Thai": "Thai",
}


# --------------------------------------------------------------------------
# Categories
# --------------------------------------------------------------------------

CAT_PROSE = "prose"
CAT_FRONTMATTER = "frontmatter"
CAT_HEADING = "heading"
CAT_CODE = "code"
CAT_CODE_COMMENT = "code_comment"
CAT_INLINE_CODE = "inline_code"
CAT_ANCHOR = "anchor"
CAT_LINK_TARGET = "link_target"
CAT_WIKILINK_TARGET = "wikilink_target"

ALL_CATEGORIES = [
    CAT_PROSE,
    CAT_FRONTMATTER,
    CAT_HEADING,
    CAT_CODE_COMMENT,
    CAT_ANCHOR,
    CAT_INLINE_CODE,
    CAT_CODE,
    CAT_LINK_TARGET,
    CAT_WIKILINK_TARGET,
]

# What each category means for a translation gate:
#
#   blocking -- untranslated content that will reach a reader or an embedding
#               index. Never merge a file with these.
#   warn     -- probably should be translated, but a literal identifier or a
#               deliberate quotation is plausible. Surface, do not block.
#   info     -- expected to stay in the source language (paths, URLs).
DEFAULT_BLOCKING = [CAT_PROSE, CAT_FRONTMATTER, CAT_HEADING, CAT_CODE_COMMENT, CAT_ANCHOR]
DEFAULT_WARN = [CAT_INLINE_CODE, CAT_CODE]
DEFAULT_INFO = [CAT_LINK_TARGET, CAT_WIKILINK_TARGET]


DEFAULT_CONFIG = {
    # Frontmatter keys whose *values* carry human-readable text and therefore
    # must end up in English. These feed titles, summaries and embeddings.
    "translatable_frontmatter": [
        "title", "description", "summary", "abstract", "excerpt",
        "audience", "intent_queries", "trigger_keywords", "keywords",
        "aliases", "note", "notes",
    ],
    # Frontmatter keys exempt from the scan: slugs, dates, enums, provenance.
    # A value here may legitimately hold non-Latin text (e.g. an author name).
    "preserve_frontmatter": [
        "tags", "category", "tier", "created", "last_updated", "date",
        "difficulty", "reading_level", "estimated_read_time",
        "source_path", "original_language", "authors", "author",
        "prerequisites", "k8s_versions", "versions", "slug", "id", "type",
    ],
    "blocking_categories": DEFAULT_BLOCKING,
    "warn_categories": DEFAULT_WARN,
    "max_chunk_lines": 400,
    "line_delta_tolerance": 0.15,
    # Line prefixes treated as comments inside a fenced code block. Comments
    # carry explanation and should be translated; surrounding code should not.
    # Override for corpora dominated by a language this list misses.
    "comment_prefixes": ["#", "//", "--", "/*", "*", ";", "%", "<!--", "'''", '"""'],
}


def load_config(path: str | Path | None = None) -> dict:
    """Load config, overlaying a JSON file on the defaults."""
    cfg = json.loads(json.dumps(DEFAULT_CONFIG))  # deep copy
    if path:
        with open(path, encoding="utf-8") as fh:
            cfg.update(json.load(fh))
    return cfg


# --------------------------------------------------------------------------
# Frontmatter
# --------------------------------------------------------------------------

_FM_RE = re.compile(r"\A---[ \t]*\r?\n(.*?)\r?\n---[ \t]*\r?\n?", re.S)


def split_frontmatter(text: str) -> tuple[str | None, str, int]:
    """
    Split a YAML frontmatter block off the front of `text`.

    Returns (frontmatter_text_or_None, body, body_start_line_zero_indexed).
    Deliberately does not parse YAML: we only need key boundaries and raw
    values, and a hard YAML dependency would make the skill less portable.
    """
    m = _FM_RE.match(text)
    if not m:
        return None, text, 0
    fm = m.group(1)
    body = text[m.end():]
    body_start_line = text[: m.end()].count("\n")
    return fm, body, body_start_line


_FM_KEY_RE = re.compile(r"^([A-Za-z_][\w-]*):(.*)$")


def frontmatter_entries(fm_text: str) -> list[tuple[str, int, str]]:
    """
    Yield (key, line_index_within_fm, line_text) for every line of frontmatter,
    attributing continuation lines (list items, folded scalars) to the key
    that owns them. Line index is relative to the frontmatter body.
    """
    out: list[tuple[str, int, str]] = []
    current = ""
    for i, line in enumerate(fm_text.split("\n")):
        m = _FM_KEY_RE.match(line)
        if m and not line.startswith((" ", "\t", "-")):
            current = m.group(1)
        out.append((current, i, line))
    return out


def frontmatter_keys(fm_text: str) -> list[str]:
    """Top-level keys, in order of appearance."""
    keys: list[str] = []
    for line in fm_text.split("\n"):
        m = _FM_KEY_RE.match(line)
        if m and not line.startswith((" ", "\t", "-")):
            if m.group(1) not in keys:
                keys.append(m.group(1))
    return keys


# --------------------------------------------------------------------------
# Body painting
# --------------------------------------------------------------------------

_FENCE_RE = re.compile(r"^(\s{0,3})(`{3,}|~{3,})\s*(\S*)")
_INLINE_CODE_RE = re.compile(r"(`+)([^\n]*?)\1")
_LINK_RE = re.compile(r"!?\[([^\]]*)\]\(([^)\s]*)(\s+\"[^\"]*\")?\)")
_WIKILINK_RE = re.compile(r"\[\[([^\]|]*)(\|([^\]]*))?\]\]")
_AUTOLINK_RE = re.compile(r"<((?:https?|ftp|mailto):[^>\s]+)>")
_BARE_URL_RE = re.compile(r"(?<![\(<\"])\b(?:https?://|www\.)[^\s\)\]<>\"]+")
_ATX_HEADING_RE = re.compile(r"^(\s{0,3})(#{1,6})\s+(.*?)\s*#*\s*$")

_COMMENT_PREFIXES = ("#", "//", "--", "/*", "*", ";", "%", "<!--", "'''", '"""')


@dataclass
class FenceRegion:
    start_line: int          # zero-indexed, the fence-open line
    end_line: int            # zero-indexed, the fence-close line (or EOF)
    info: str                # the language info string, e.g. "yaml"


@dataclass
class PaintedDoc:
    """A document with every body character assigned a category."""
    text: str
    frontmatter: str | None
    body: str
    body_start_line: int
    categories: list[str]              # one entry per character of `body`
    fences: list[FenceRegion] = field(default_factory=list)
    headings: list[tuple[int, str, int]] = field(default_factory=list)  # (level, text, line)


def find_fences(body: str) -> list[FenceRegion]:
    """Locate fenced code blocks, honouring the CommonMark close-fence rules."""
    regions: list[FenceRegion] = []
    lines = body.split("\n")
    i = 0
    while i < len(lines):
        m = _FENCE_RE.match(lines[i])
        if m:
            marker = m.group(2)
            char = marker[0]
            length = len(marker)
            info = m.group(3) or ""
            start = i
            i += 1
            end = len(lines) - 1
            while i < len(lines):
                cm = _FENCE_RE.match(lines[i])
                # A closing fence uses the same char, is at least as long, and
                # carries no info string.
                if cm and cm.group(2)[0] == char and len(cm.group(2)) >= length and not cm.group(3):
                    end = i
                    break
                i += 1
            regions.append(FenceRegion(start, end, info))
        i += 1
    return regions


def _line_offsets(text: str) -> list[int]:
    offsets = [0]
    for i, ch in enumerate(text):
        if ch == "\n":
            offsets.append(i + 1)
    return offsets


def paint(text: str, config: dict | None = None) -> PaintedDoc:
    """
    Assign every character of the body a category.

    Precedence matters. Fenced code wins over everything inside it; link
    targets win over the prose that surrounds them; whatever is left is prose.
    Painting is done onto a mutable array so later passes can only claim
    characters that are still prose.
    """
    cfg = config or DEFAULT_CONFIG
    comment_prefixes = tuple(cfg.get("comment_prefixes", _COMMENT_PREFIXES))
    fm, body, body_start_line = split_frontmatter(text)
    cats = [CAT_PROSE] * len(body)
    offsets = _line_offsets(body)
    lines = body.split("\n")

    def paint_span(start: int, end: int, cat: str, only_over: str = CAT_PROSE) -> None:
        for k in range(max(0, start), min(len(cats), end)):
            if cats[k] == only_over:
                cats[k] = cat

    # --- pass 1: fenced code -------------------------------------------------
    fences = find_fences(body)
    for fr in fences:
        for ln in range(fr.start_line, min(fr.end_line + 1, len(lines))):
            start = offsets[ln]
            end = start + len(lines[ln])
            stripped = lines[ln].strip()
            # The fence delimiter lines themselves are structure, not content.
            is_delim = ln in (fr.start_line, fr.end_line) and _FENCE_RE.match(lines[ln])
            if is_delim:
                cat = CAT_CODE
            elif stripped.startswith(comment_prefixes):
                cat = CAT_CODE_COMMENT
            else:
                cat = CAT_CODE
            paint_span(start, end, cat)

    fence_lines = set()
    for fr in fences:
        fence_lines.update(range(fr.start_line, min(fr.end_line + 1, len(lines))))

    # --- pass 2: headings ----------------------------------------------------
    headings: list[tuple[int, str, int]] = []
    for ln, line in enumerate(lines):
        if ln in fence_lines:
            continue
        hm = _ATX_HEADING_RE.match(line)
        if hm:
            level = len(hm.group(2))
            htext = hm.group(3)
            headings.append((level, htext, ln))
            start = offsets[ln] + hm.start(3)
            paint_span(start, start + len(htext), CAT_HEADING)

    # Everything below operates only on non-fence regions. Build a predicate
    # rather than slicing, so offsets stay aligned with the original body.
    def outside_fence(pos: int) -> bool:
        ln = _line_of(offsets, pos)
        return ln not in fence_lines

    # --- pass 3: inline code -------------------------------------------------
    for m in _INLINE_CODE_RE.finditer(body):
        if outside_fence(m.start()):
            paint_span(m.start(), m.end(), CAT_INLINE_CODE)
            paint_span(m.start(), m.end(), CAT_INLINE_CODE, only_over=CAT_HEADING)

    # --- pass 4: wikilinks (target protected, alias left as prose) -----------
    for m in _WIKILINK_RE.finditer(body):
        if not outside_fence(m.start()):
            continue
        paint_span(m.start(1), m.end(1), CAT_WIKILINK_TARGET)
        paint_span(m.start(1), m.end(1), CAT_WIKILINK_TARGET, only_over=CAT_HEADING)

    # --- pass 5: inline links (target protected, text left as prose) ---------
    for m in _LINK_RE.finditer(body):
        if not outside_fence(m.start()):
            continue
        target = m.group(2)
        cat = CAT_ANCHOR if target.startswith("#") else CAT_LINK_TARGET
        paint_span(m.start(2), m.end(2), cat)
        paint_span(m.start(2), m.end(2), cat, only_over=CAT_HEADING)

    # --- pass 6: autolinks and bare URLs -------------------------------------
    for rx in (_AUTOLINK_RE, _BARE_URL_RE):
        for m in rx.finditer(body):
            if outside_fence(m.start()):
                paint_span(m.start(), m.end(), CAT_LINK_TARGET)

    return PaintedDoc(
        text=text,
        frontmatter=fm,
        body=body,
        body_start_line=body_start_line,
        categories=cats,
        fences=fences,
        headings=headings,
    )


def _line_of(offsets: list[int], pos: int) -> int:
    """Binary search a character offset back to its zero-indexed line."""
    lo, hi = 0, len(offsets) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if offsets[mid] <= pos:
            lo = mid
        else:
            hi = mid - 1
    return lo


# --------------------------------------------------------------------------
# Findings
# --------------------------------------------------------------------------

@dataclass
class Finding:
    line: int          # 1-indexed, relative to the whole file
    category: str
    script: str
    text: str          # the trimmed source line, for eyeballing
    count: int         # non-Latin characters on this line in this category


def scan_text(text: str, config: dict | None = None) -> tuple[list[Finding], dict[str, int]]:
    """
    Find every non-Latin character and attribute it to a category.

    Returns (findings, per-category character totals). Findings are aggregated
    per (line, category) so a 40-character Chinese paragraph is one finding,
    not forty.
    """
    cfg = config or DEFAULT_CONFIG
    doc = paint(text, cfg)
    per_cat: dict[str, int] = {}
    agg: dict[tuple[int, str], Finding] = {}

    translatable = {k.lower() for k in cfg["translatable_frontmatter"]}
    preserve = {k.lower() for k in cfg["preserve_frontmatter"]}

    # --- frontmatter ---------------------------------------------------------
    if doc.frontmatter is not None:
        for key, idx, line in frontmatter_entries(doc.frontmatter):
            k = key.lower()
            # Unknown keys default to translatable: a corpus we have never seen
            # is more likely to hide real untranslated prose behind an unknown
            # key than to hold deliberate source-language text there.
            if k in preserve and k not in translatable:
                continue
            counts: dict[str, int] = {}
            for ch in line:
                s = script_of(ch)
                if s:
                    counts[s] = counts.get(s, 0) + 1
            if counts:
                total = sum(counts.values())
                script = max(counts.items(), key=lambda kv: kv[1])[0]
                fileline = idx + 2  # +1 for the opening ---, +1 for 1-indexing
                per_cat[CAT_FRONTMATTER] = per_cat.get(CAT_FRONTMATTER, 0) + total
                agg[(fileline, CAT_FRONTMATTER)] = Finding(
                    line=fileline, category=CAT_FRONTMATTER, script=script,
                    text=line.strip()[:160], count=total,
                )

    # --- body ----------------------------------------------------------------
    offsets = _line_offsets(doc.body)
    body_lines = doc.body.split("\n")
    for pos, ch in enumerate(doc.body):
        s = script_of(ch)
        if not s:
            continue
        cat = doc.categories[pos]
        per_cat[cat] = per_cat.get(cat, 0) + 1
        ln = _line_of(offsets, pos)
        fileline = doc.body_start_line + ln + 1
        key = (fileline, cat)
        if key in agg:
            agg[key].count += 1
        else:
            agg[key] = Finding(
                line=fileline, category=cat, script=s,
                text=body_lines[ln].strip()[:160], count=1,
            )

    findings = sorted(agg.values(), key=lambda f: (f.line, f.category))
    return findings, per_cat


def severity(category: str, config: dict | None = None) -> str:
    cfg = config or DEFAULT_CONFIG
    if category in cfg["blocking_categories"]:
        return "BLOCK"
    if category in cfg["warn_categories"]:
        return "WARN"
    return "INFO"


def density_bucket(non_latin_lines: int, total_lines: int) -> str:
    """Coarse label used to triage a corpus and to size translation batches."""
    if total_lines <= 0 or non_latin_lines == 0:
        return "CLEAN"
    pct = non_latin_lines * 100 // total_lines
    if pct >= 25:
        return "HEAVY"
    if pct >= 5:
        return "PARTIAL"
    return "TRACE"


# --------------------------------------------------------------------------
# Structure fingerprint (used by the verifier)
# --------------------------------------------------------------------------

@dataclass
class Structure:
    total_lines: int
    fm_keys: list[str]
    heading_levels: list[int]
    fence_infos: list[str]
    n_links: int
    n_wikilinks: int
    n_images: int
    n_table_rows: int
    n_list_items: int
    n_blockquote_lines: int

    def to_dict(self) -> dict:
        return {
            "total_lines": self.total_lines,
            "fm_keys": self.fm_keys,
            "heading_levels": self.heading_levels,
            "fence_infos": self.fence_infos,
            "n_links": self.n_links,
            "n_wikilinks": self.n_wikilinks,
            "n_images": self.n_images,
            "n_table_rows": self.n_table_rows,
            "n_list_items": self.n_list_items,
            "n_blockquote_lines": self.n_blockquote_lines,
        }


_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)\s]*)")
_LIST_RE = re.compile(r"^\s{0,8}([-*+]|\d+\.)\s+\S")
_TABLE_RE = re.compile(r"^\s*\|.*\|\s*$")


def structure_of(text: str) -> Structure:
    """
    Fingerprint the parts of a document that translation must not change.

    Translation rewrites words. It must not add or drop a heading, reorder
    code fences, or lose a table row. Comparing these counts before and after
    is how a dropped section gets caught -- the failure mode where a model
    quietly summarises instead of translating.
    """
    doc = paint(text)
    lines = doc.body.split("\n")
    fence_lines: set[int] = set()
    for fr in doc.fences:
        fence_lines.update(range(fr.start_line, min(fr.end_line + 1, len(lines))))

    n_links = n_wikilinks = n_images = n_table = n_list = n_quote = 0
    for ln, line in enumerate(lines):
        if ln in fence_lines:
            continue
        n_links += len(_LINK_RE.findall(line))
        n_wikilinks += len(_WIKILINK_RE.findall(line))
        n_images += len(_IMAGE_RE.findall(line))
        if _TABLE_RE.match(line):
            n_table += 1
        if _LIST_RE.match(line):
            n_list += 1
        if line.lstrip().startswith(">"):
            n_quote += 1

    return Structure(
        total_lines=text.count("\n") + 1,
        fm_keys=frontmatter_keys(doc.frontmatter) if doc.frontmatter else [],
        heading_levels=[lvl for lvl, _, _ in doc.headings],
        fence_infos=[fr.info for fr in doc.fences],
        n_links=n_links,
        n_wikilinks=n_wikilinks,
        n_images=n_images,
        n_table_rows=n_table,
        n_list_items=n_list,
        n_blockquote_lines=n_quote,
    )


# --------------------------------------------------------------------------
# Anchors
# --------------------------------------------------------------------------

_ANCHOR_STRIP_RE = re.compile(r"[^\w\s-]", re.UNICODE)


def slugify(heading: str) -> str:
    """
    GitHub-flavoured heading slug: lowercase, punctuation dropped, spaces to
    hyphens. Markdown formatting is stripped first so `**Bold**` and `Bold`
    produce the same anchor.
    """
    text = re.sub(r"`([^`]*)`", r"\1", heading)
    text = re.sub(r"\*\*([^*]*)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]*)\*", r"\1", text)
    text = re.sub(r"\[\[([^\]|]*)\|([^\]]*)\]\]", r"\2", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = text.strip().lower()
    text = _ANCHOR_STRIP_RE.sub("", text)
    text = re.sub(r"\s+", "-", text)
    return text


def anchor_report(text: str) -> tuple[list[str], list[str], list[str]]:
    """
    Returns (all_anchor_targets, available_slugs, broken_targets).

    A TOC whose anchors were translated as if they were prose -- or left in the
    source language while the headings became English -- produces broken
    targets here. That is the single most common silent breakage when
    translating a document that opens with a table of contents.
    """
    doc = paint(text)
    lines = doc.body.split("\n")
    fence_lines: set[int] = set()
    for fr in doc.fences:
        fence_lines.update(range(fr.start_line, min(fr.end_line + 1, len(lines))))

    slugs: dict[str, int] = {}
    available: list[str] = []
    for _, htext, _ in doc.headings:
        base = slugify(htext)
        n = slugs.get(base, 0)
        slugs[base] = n + 1
        available.append(base if n == 0 else f"{base}-{n}")

    targets: list[str] = []
    for ln, line in enumerate(lines):
        if ln in fence_lines:
            continue
        for m in _LINK_RE.finditer(line):
            t = m.group(2)
            if t.startswith("#"):
                targets.append(t[1:])

    avail = set(available)
    broken = [t for t in targets if t and t not in avail]
    return targets, available, broken


# --------------------------------------------------------------------------
# Chunk planning
# --------------------------------------------------------------------------

@dataclass
class Chunk:
    index: int
    start_line: int   # 1-indexed, inclusive, relative to the whole file
    end_line: int     # 1-indexed, inclusive
    heading: str      # the section heading this chunk opens with, for context


def plan_chunks(text: str, max_lines: int = 400) -> list[Chunk]:
    """
    Split a document into translation-sized pieces on heading boundaries.

    Whole-file rewriting is where summarisation drift creeps in: asked to
    "translate this 2700-line document", a model starts condensing around the
    middle. Handing it a bounded section at a time and reassembling keeps every
    line accounted for. Splits never land inside a fenced code block, because
    half a code block has no context to translate against.
    """
    doc = paint(text)
    lines = doc.body.split("\n")
    fence_lines: set[int] = set()
    for fr in doc.fences:
        fence_lines.update(range(fr.start_line, min(fr.end_line + 1, len(lines))))

    # Candidate split points: every H2 or H1 that is not inside a fence.
    boundaries = [ln for lvl, _, ln in doc.headings if lvl <= 2 and ln not in fence_lines]
    heading_at = {ln: htext for lvl, htext, ln in doc.headings if lvl <= 2}
    if not boundaries or boundaries[0] != 0:
        boundaries = [0] + boundaries

    # Merge adjacent sections until adding one more would exceed max_lines.
    chunks: list[Chunk] = []
    i = 0
    idx = 0

    # Frontmatter is its own chunk. It sits above the first heading, so a plan
    # built only from heading boundaries would silently omit it -- and
    # title/description/summary are the highest-cost thing to leave
    # untranslated, because they are what gets embedded. Emitting it
    # explicitly makes the plan cover the file from line 1 and makes skipping
    # it a visible choice rather than an accident.
    if doc.body_start_line > 0:
        chunks.append(Chunk(
            index=0,
            start_line=1,
            end_line=doc.body_start_line,
            heading="(frontmatter -- translate title/description/summary, keep slugs and dates)",
        ))
        idx = 1
    while i < len(boundaries):
        start = boundaries[i]
        j = i + 1
        while j < len(boundaries) and (boundaries[j] - start) < max_lines:
            j += 1
        end = boundaries[j] - 1 if j < len(boundaries) else len(lines) - 1

        # If a single section is itself oversized, fall back to splitting on
        # blank lines outside fences so we never hand over a half-open fence.
        if (end - start) > max_lines * 2:
            sub = start
            while sub <= end:
                stop = min(sub + max_lines, end)
                while stop < end and (stop in fence_lines or lines[stop].strip() != ""):
                    stop += 1
                chunks.append(Chunk(
                    index=idx,
                    start_line=doc.body_start_line + sub + 1,
                    end_line=doc.body_start_line + stop + 1,
                    heading=heading_at.get(start, "")[:80],
                ))
                idx += 1
                sub = stop + 1
        else:
            chunks.append(Chunk(
                index=idx,
                start_line=doc.body_start_line + start + 1,
                end_line=doc.body_start_line + end + 1,
                heading=heading_at.get(start, "")[:80],
            ))
            idx += 1
        i = j
    return chunks


# --------------------------------------------------------------------------
# File discovery
# --------------------------------------------------------------------------

DEFAULT_EXTENSIONS = [".md", ".markdown", ".txt", ".rst", ".mdx"]
DEFAULT_IGNORES = {".git", "node_modules", ".venv", "venv", "__pycache__", ".obsidian"}


def discover(root: str | Path, extensions: list[str] | None = None) -> list[Path]:
    """Recursively collect candidate files under `root`, or [root] if it is a file."""
    exts = {e.lower() for e in (extensions or DEFAULT_EXTENSIONS)}
    p = Path(root).expanduser()
    if p.is_file():
        return [p]
    out: list[Path] = []
    for f in sorted(p.rglob("*")):
        if not f.is_file():
            continue
        if any(part in DEFAULT_IGNORES for part in f.parts):
            continue
        if f.suffix.lower() in exts:
            out.append(f)
    return out


def read_text(path: str | Path) -> str:
    """Read as UTF-8, tolerating the odd stray byte rather than crashing a batch."""
    return Path(path).read_text(encoding="utf-8", errors="replace")
