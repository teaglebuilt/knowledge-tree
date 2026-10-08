#!/usr/bin/env python3
"""
translation_scan.py -- scan the knowledge tree for non-English markdown and
optionally translate it to English via the Anthropic API.

Detection and chunking reuse the collect_knowledge skill scripts (mdlang /
lang_scan / verify_translation). This is the batch driver that calls Anthropic
and, with --write, overwrites files in place after the verify gate passes.

Usage
-----
  # Report only (no API calls)
  uv run python scripts/translation_scan.py tree/

  # Translate + overwrite one file
  uv run python scripts/translation_scan.py path/to/doc.md --write

  # Batch with filters
  uv run python scripts/translation_scan.py tree/ --bucket HEAVY --limit 5 --write

Requires ANTHROPIC_API_KEY when --write is used (export via .envrc / direnv).
"""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
from pathlib import Path

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
    load_config,
    paint,
    plan_chunks,
    read_text,
    slugify,
    split_frontmatter,
)
from mdlang import _LINK_RE  # noqa: E402
from verify_translation import verify_one  # noqa: E402

DEFAULT_MODEL = "claude-sonnet-4-6"
DEFAULT_PATHS = ["tree"]
# Smaller than mdlang's 400 — large chunks are where list/heading drops appear.
DEFAULT_TRANSLATE_CHUNK_LINES = 200

SYSTEM_PROMPT = """\
You are a precise technical documentation translator. Translate the markdown \
chunk into English.

Rules (must follow):
- Translate prose, headings, and human-readable frontmatter values \
(title, description, summary, abstract, audience, keywords, aliases, notes, \
intent_queries, trigger_keywords).
- Translate code comments inside fenced blocks. Leave code, commands, YAML/JSON \
keys, identifiers, and fence info strings (e.g. ```yaml) untouched.
- Never translate URLs, paths, wikilink targets, or link destinations. Link \
display text may be translated.
- NEVER summarize, improve, reorganize, merge, or omit content. Every heading, \
numbered/bulleted list item, table row, and code block in the source must \
appear in the output — same count, same order.
- For TOC / in-document links like [text](#anchor): translate ONLY the link \
text; leave the #anchor target as a placeholder (any slug). A post-processor \
will regenerate anchors from the final English headings.
- Preserve markdown structure, whitespace intent, and YAML frontmatter keys.
- Output ONLY the translated markdown chunk — no preamble or commentary.
"""

_NUM_HEADING_RE = re.compile(r"^\s*(\d+)([.\s]|$)")


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


def _heading_slugs(text: str) -> tuple[list[str], dict[str, str], dict[str, str]]:
    """
    Returns (slugs_in_order, slug_set_map, number_to_slug).

    number_to_slug maps leading section numbers ("1", "2", …) to the first
    heading slug that starts with that number — used to repair TOC anchors.
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
        m = _NUM_HEADING_RE.match(htext.strip())
        if m:
            by_number.setdefault(m.group(1), slug)
    return ordered, {s: s for s in ordered}, by_number


def repair_internal_anchors(text: str) -> str:
    """
    Rewrite in-document `#anchor` targets so they resolve to real headings.

    Models routinely invent TOC slugs that don't match slugify(heading). Prefer:
    1) keep if already valid, 2) slugify(link text), 3) leading section number,
    4) suffix / containment match against available heading slugs.
    """
    ordered, avail, by_number = _heading_slugs(text)
    if not ordered:
        return text

    doc = paint(text)
    body_lines = doc.body.split("\n")
    fence_lines: set[int] = set()
    for fr in doc.fences:
        fence_lines.update(range(fr.start_line, min(fr.end_line + 1, len(body_lines))))

    def resolve(label: str, target: str) -> str:
        if target in avail:
            return target
        for candidate in (slugify(label), slugify(label.lstrip("0123456789. "))):
            if candidate and candidate in avail:
                return candidate
        m = re.match(r"^(\d+)\b", target) or _NUM_HEADING_RE.match(label.strip())
        if m and m.group(1) in by_number:
            return by_number[m.group(1)]
        label_slug = slugify(label)
        if label_slug:
            for slug in ordered:
                if slug == label_slug or slug.endswith("-" + label_slug):
                    return slug
        # Last resort: longest available slug contained in the bad target or vice versa.
        for slug in ordered:
            if slug and (slug in target or target in slug):
                return slug
        return target

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
            title = m.group(3) or ""
            return f"[{label}](#{fixed}{title})"

        new_lines.append(_LINK_RE.sub(_sub, line))

    fm = doc.frontmatter
    body = "\n".join(new_lines)
    if fm is None:
        return body
    # Reconstruct with the same --- fences the source used.
    return f"---\n{fm}\n---\n{body}"


def extract_chunk_text(text: str, start_line: int, end_line: int) -> str:
    """Slice 1-indexed inclusive line range from text."""
    lines = text.split("\n")
    return "\n".join(lines[start_line - 1 : end_line])


def translate_chunk(client, model: str, chunk_text: str, heading: str, index: int, n: int) -> str:
    user = (
        f"Translate chunk {index + 1}/{n}"
        + (f" ({heading})" if heading else "")
        + " to English.\n\n"
        + chunk_text
    )
    msg = client.messages.create(
        model=model,
        max_tokens=16384,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user}],
    )
    parts = []
    for block in msg.content:
        if getattr(block, "type", None) == "text":
            parts.append(block.text)
    out = "".join(parts).strip()
    if not out:
        raise RuntimeError(f"empty translation for chunk {index}")
    # Drop accidental markdown fences around the whole response.
    if out.startswith("```") and out.endswith("```"):
        inner = out.split("\n", 1)
        if len(inner) == 2:
            out = inner[1]
            if out.endswith("```"):
                out = out[: -3].rstrip()
    return out


def translate_file(
    client,
    model: str,
    text: str,
    config: dict,
    lang: str,
    source_path: str,
) -> str:
    chunks = plan_chunks(text, config["max_chunk_lines"])
    if not chunks:
        return repair_internal_anchors(ensure_provenance(text, lang, source_path))
    pieces: list[str] = []
    for c in chunks:
        piece = extract_chunk_text(text, c.start_line, c.end_line)
        print(
            f"    chunk {c.index}: lines {c.start_line}-{c.end_line} "
            f"({c.end_line - c.start_line + 1})  {c.heading}",
            flush=True,
        )
        pieces.append(
            translate_chunk(client, model, piece, c.heading, c.index, len(chunks))
        )
    assembled = "\n".join(pieces)
    if not assembled.endswith("\n") and text.endswith("\n"):
        assembled += "\n"
    assembled = ensure_provenance(assembled, lang, source_path)
    return repair_internal_anchors(assembled)


def _is_structure_drop(result) -> bool:
    return any(
        "dropped" in f and any(k in f for k in ("list items", "headings", "table rows"))
        for f in result.failures
    )


def atomic_write(path: Path, content: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(content, encoding="utf-8")
    tmp.replace(path)


def verify_text(original: Path, translated_text: str, config: dict):
    with tempfile.NamedTemporaryFile(
        mode="w",
        suffix=original.suffix or ".md",
        encoding="utf-8",
        delete=False,
    ) as fh:
        fh.write(translated_text)
        tmp_path = Path(fh.name)
    try:
        return verify_one(tmp_path, original, config)
    finally:
        tmp_path.unlink(missing_ok=True)


def require_api_key() -> str:
    key = os.environ.get("ANTHROPIC_API_KEY", "").strip()
    if not key:
        print(
            "error: ANTHROPIC_API_KEY not set\n"
            "  export it (e.g. direnv allow after adding to .envrc)",
            file=sys.stderr,
        )
        sys.exit(2)
    return key


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="translation_scan.py",
        description="Scan tree for non-English markdown; translate via Anthropic with --write.",
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
        help="translate with Anthropic and overwrite in place after verify passes",
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
    ap.add_argument("--model", default=DEFAULT_MODEL, help=f"Anthropic model (default {DEFAULT_MODEL})")
    ap.add_argument(
        "--max-chunk-lines",
        type=int,
        default=DEFAULT_TRANSLATE_CHUNK_LINES,
        help=f"plan_chunks size (default {DEFAULT_TRANSLATE_CHUNK_LINES})",
    )
    ap.add_argument("--show", type=int, default=5, help="sample blocking lines in report")
    args = ap.parse_args(argv)

    config = load_config()
    config["max_chunk_lines"] = args.max_chunk_lines

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
    for f in files:
        if not args.include_books and is_book_path(f):
            skipped_books += 1
            continue
        reports.append(analyse(f, config))

    if args.bucket:
        reports = [r for r in reports if r["bucket"] == args.bucket]

    dirty = [r for r in reports if r["bucket"] != "CLEAN" and r["blocking_chars"] > 0]
    clean_n = sum(1 for r in reports if r["bucket"] == "CLEAN" or r["blocking_chars"] == 0)

    print(f"scanned {len(reports)} file(s)" + (f" (skipped {skipped_books} books)" if skipped_books else ""))
    buckets: dict[str, int] = {}
    for r in reports:
        buckets[r["bucket"]] = buckets.get(r["bucket"], 0) + 1
    for b in ("HEAVY", "PARTIAL", "TRACE", "CLEAN"):
        if buckets.get(b):
            print(f"  {b:<8} {buckets[b]}")
    print(f"  {len(dirty)} file(s) need translation; {clean_n} clean")

    for r in dirty:
        print(f"\n{r['path']}")
        print(
            f"  {r['bucket']}  {r['lines_with_non_latin']}/{r['total_lines']} lines  "
            f"({r['language_hint'] or '-'})"
        )
        blocking = [f for f in r["findings"] if f["severity"] == "BLOCK"]
        for f in blocking[: args.show]:
            print(f"    L{f['line']:<5} {f['category']:<14} {f['text']}")
        if len(blocking) > args.show:
            print(f"    ... {len(blocking) - args.show} more")

    if not args.write:
        print("\n(dry-run — pass --write to translate and overwrite)")
        return 0 if not dirty else 1

    if not dirty:
        print("\nnothing to translate")
        return 0

    sys.stdout.flush()
    require_api_key()
    try:
        import anthropic
    except ImportError:
        print(
            "error: anthropic package missing — run: uv add anthropic && uv sync",
            file=sys.stderr,
        )
        return 2

    client = anthropic.Anthropic()
    targets = dirty
    if args.limit is not None:
        targets = dirty[: args.limit]

    translated_ok = 0
    failed = 0
    for r in targets:
        path = Path(r["path"])
        lang = language_label(r["dominant_script"])
        rel = str(path)
        print(f"\ntranslating {path} ({r['bucket']}, {lang}) with {args.model}")
        try:
            original_text = read_text(path)
            file_config = dict(config)
            new_text = translate_file(
                client, args.model, original_text, file_config, lang, rel
            )
            result = verify_text(path, new_text, file_config)
            # One retry with smaller chunks when the model drops structure.
            if not result.passed and _is_structure_drop(result):
                retry_lines = max(80, file_config["max_chunk_lines"] // 2)
                print(
                    f"  structure drop — retrying with max_chunk_lines={retry_lines}",
                    flush=True,
                )
                file_config["max_chunk_lines"] = retry_lines
                new_text = translate_file(
                    client, args.model, original_text, file_config, lang, rel
                )
                result = verify_text(path, new_text, file_config)
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
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
