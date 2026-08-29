#!/usr/bin/env python3
"""
verify_translation.py -- the gate. Nothing merges into the tree until this passes.

A translation step that is merely *described* gets skipped under load: asked to
translate, analyse, deduplicate and file a 2000-line document, a model will do
the cheap parts and quietly skip the expensive one. The only reliable fix is to
make the expensive part checkable, and to check it.

Three classes of failure this catches:

  1. Residual source language -- the file was not translated, or was translated
     only down to the point where attention drifted. Includes frontmatter,
     which is easy to forget and, because title/description/summary usually
     feed an embedding index, is the most damaging place to leave untranslated.

  2. Structure drift -- headings, code fences, tables or list items were added
     or dropped. This is the signature of a model that started summarising
     instead of translating. Word counts legitimately change; a table losing
     four rows does not.

  3. Broken anchors -- headings became English but the table of contents still
     points at source-language slugs, so every TOC link dead-ends.

Usage
-----
  # One pair
  verify_translation.py --original src/doc.md --translated out/doc.md

  # A whole batch, paired by relative path
  verify_translation.py --original-dir ~/corpus --translated-dir ./staging

  # Residual + anchor checks only, when no original is available
  # (e.g. auditing a tree that was imported before this gate existed)
  verify_translation.py --translated-dir ./tree

Exit codes: 0 = every file passed, 1 = at least one failed, 2 = bad invocation.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path

# Resolve sibling imports so this script runs from any working directory.
sys.path.insert(0, str(Path(__file__).resolve().parent))

from mdlang import (
    SCRIPT_TO_LANGUAGE_HINT,
    anchor_report,
    discover,
    load_config,
    read_text,
    scan_text,
    severity,
    structure_of,
)


@dataclass
class Result:
    path: str
    original: str | None = None
    failures: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    stats: dict = field(default_factory=dict)

    @property
    def passed(self) -> bool:
        return not self.failures


# --------------------------------------------------------------------------
# Individual checks
# --------------------------------------------------------------------------

def check_residual(text: str, config: dict, res: Result) -> None:
    """Any blocking-category non-Latin text means the translation is incomplete."""
    findings, per_cat = scan_text(text, config)
    blocking = [f for f in findings if severity(f.category, config) == "BLOCK"]
    warned = [f for f in findings if severity(f.category, config) == "WARN"]

    res.stats["residual_by_category"] = per_cat
    res.stats["n_blocking_lines"] = len({f.line for f in blocking})

    if blocking:
        by_cat: dict[str, list] = {}
        for f in blocking:
            by_cat.setdefault(f.category, []).append(f)
        for cat, items in sorted(by_cat.items()):
            lines = ", ".join(f"L{f.line}" for f in items[:6])
            more = f" (+{len(items) - 6} more)" if len(items) > 6 else ""
            hint = SCRIPT_TO_LANGUAGE_HINT.get(items[0].script, items[0].script)
            res.failures.append(
                f"untranslated {cat}: {len(items)} line(s) still contain {hint} -- {lines}{more}"
            )
            # Show the worst offender verbatim so the fix is obvious.
            worst = max(items, key=lambda f: f.count)
            res.failures.append(f"    L{worst.line}: {worst.text}")

    if warned:
        cats = sorted({f.category for f in warned})
        res.warnings.append(
            f"non-Latin text inside {'/'.join(cats)} on "
            f"{len({f.line for f in warned})} line(s) -- review whether these are "
            f"literal identifiers (fine) or comments/terms that should be translated"
        )


def check_anchors(text: str, res: Result) -> None:
    """Every in-document anchor link must resolve to a heading that exists."""
    targets, _available, broken = anchor_report(text)
    res.stats["n_anchors"] = len(targets)
    res.stats["n_broken_anchors"] = len(broken)
    if broken:
        shown = ", ".join(f"#{b}" for b in broken[:6])
        more = f" (+{len(broken) - 6} more)" if len(broken) > 6 else ""
        res.failures.append(
            f"broken anchors: {len(broken)} link(s) point at headings that do not "
            f"exist -- {shown}{more}"
        )
        res.failures.append(
            "    regenerate anchor targets from the translated headings; "
            "do not translate the anchor text itself"
        )


def check_structure(orig: str, trans: str, config: dict, res: Result) -> None:
    """Compare the parts of the document translation must leave alone."""
    a = structure_of(orig)
    b = structure_of(trans)
    res.stats["structure_original"] = a.to_dict()
    res.stats["structure_translated"] = b.to_dict()

    def cmp_count(name: str, x: int, y: int) -> None:
        if x != y:
            verb = "dropped" if y < x else "added"
            res.failures.append(f"{name}: original has {x}, translation has {y} ({verb} {abs(x - y)})")

    cmp_count("headings", len(a.heading_levels), len(b.heading_levels))
    if a.heading_levels != b.heading_levels and len(a.heading_levels) == len(b.heading_levels):
        res.failures.append(
            "heading levels changed: the outline nesting differs between original and translation"
        )
    cmp_count("code fences", len(a.fence_infos), len(b.fence_infos))
    if a.fence_infos != b.fence_infos and len(a.fence_infos) == len(b.fence_infos):
        diffs = [f"#{i} {x!r}->{y!r}" for i, (x, y) in enumerate(zip(a.fence_infos, b.fence_infos)) if x != y]
        res.failures.append(
            "code fence languages changed: " + ", ".join(diffs[:5])
            + " -- the info string is code, not prose; it must not be translated"
        )
    cmp_count("links", a.n_links, b.n_links)
    cmp_count("wikilinks", a.n_wikilinks, b.n_wikilinks)
    cmp_count("images", a.n_images, b.n_images)
    cmp_count("table rows", a.n_table_rows, b.n_table_rows)
    cmp_count("list items", a.n_list_items, b.n_list_items)
    cmp_count("blockquote lines", a.n_blockquote_lines, b.n_blockquote_lines)

    # Frontmatter keys are schema. Values change; the key set should not.
    lost = [k for k in a.fm_keys if k not in b.fm_keys]
    if lost:
        res.failures.append(f"frontmatter keys dropped: {', '.join(lost)}")
    gained = [k for k in b.fm_keys if k not in a.fm_keys]
    # Additions are expected -- the skill adds provenance fields.
    if gained:
        res.stats["frontmatter_keys_added"] = gained

    # Line count is a soft signal: translated prose reflows, but a 40% drop
    # means content is gone.
    tol = config["line_delta_tolerance"]
    if a.total_lines:
        delta = (b.total_lines - a.total_lines) / a.total_lines
        res.stats["line_delta_pct"] = round(delta * 100, 1)
        if abs(delta) > tol:
            res.warnings.append(
                f"line count moved {delta * 100:+.0f}% "
                f"({a.total_lines} -> {b.total_lines}); tolerance is +/-{tol * 100:.0f}%. "
                f"A large drop usually means a section was summarised rather than translated"
            )


def check_provenance(text: str, res: Result) -> None:
    """A translated file should record what it was translated from."""
    from mdlang import frontmatter_keys, split_frontmatter

    fm, _, _ = split_frontmatter(text)
    if fm is None:
        res.warnings.append("no YAML frontmatter found")
        return
    keys = frontmatter_keys(fm)
    for required in ("original_language", "source_path"):
        if required not in keys:
            res.warnings.append(
                f"frontmatter is missing `{required}` -- without it a bad "
                f"translation cannot be traced back and re-done"
            )


# --------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------

def verify_one(translated: Path, original: Path | None, config: dict) -> Result:
    res = Result(path=str(translated), original=str(original) if original else None)
    ttext = read_text(translated)

    check_residual(ttext, config, res)
    check_anchors(ttext, res)
    check_provenance(ttext, res)
    if original is not None:
        if not original.exists():
            res.warnings.append(f"original not found at {original}; skipped structure checks")
        else:
            check_structure(read_text(original), ttext, config, res)
    return res


def pair_dirs(orig_dir: Path, trans_dir: Path, exts: list[str] | None) -> list[tuple[Path, Path | None]]:
    """Pair translated files to originals by path relative to each root."""
    pairs: list[tuple[Path, Path | None]] = []
    for t in discover(trans_dir, exts):
        rel = t.relative_to(trans_dir)
        cand = orig_dir / rel
        pairs.append((t, cand if cand.exists() else None))
    return pairs


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="verify_translation.py",
        description="Gate a translated markdown file or batch before it is merged.",
    )
    ap.add_argument("--original", help="the source-language file")
    ap.add_argument("--translated", help="the English file to check")
    ap.add_argument("--original-dir", help="root of the source-language corpus")
    ap.add_argument("--translated-dir", help="root of the translated output")
    ap.add_argument("--config", help="JSON config overriding the defaults")
    ap.add_argument("--ext", action="append", help="file extension to include (repeatable)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--quiet", action="store_true", help="print failures only")
    args = ap.parse_args(argv)

    config = load_config(args.config)

    pairs: list[tuple[Path, Path | None]] = []
    if args.translated_dir:
        tdir = Path(args.translated_dir).expanduser()
        if not tdir.exists():
            print(f"error: no such directory: {tdir}", file=sys.stderr)
            return 2
        if args.original_dir:
            odir = Path(args.original_dir).expanduser()
            if not odir.exists():
                print(f"error: no such directory: {odir}", file=sys.stderr)
                return 2
            pairs = pair_dirs(odir, tdir, args.ext)
        else:
            pairs = [(t, None) for t in discover(tdir, args.ext)]
    elif args.translated:
        t = Path(args.translated).expanduser()
        if not t.exists():
            print(f"error: no such file: {t}", file=sys.stderr)
            return 2
        o = Path(args.original).expanduser() if args.original else None
        pairs = [(t, o)]
    else:
        ap.error("supply --translated or --translated-dir")

    if not pairs:
        print("error: no files to verify", file=sys.stderr)
        return 2

    results = [verify_one(t, o, config) for t, o in pairs]

    if args.json:
        json.dump(
            {
                "n_files": len(results),
                "n_failed": sum(1 for r in results if not r.passed),
                "results": [
                    {
                        "path": r.path,
                        "original": r.original,
                        "passed": r.passed,
                        "failures": r.failures,
                        "warnings": r.warnings,
                        "stats": r.stats,
                    }
                    for r in results
                ],
            },
            sys.stdout, indent=2, ensure_ascii=False,
        )
        print()
    else:
        for r in results:
            if r.passed and args.quiet:
                continue
            tag = "\033[32mPASS\033[0m" if r.passed else "\033[31mFAIL\033[0m"
            print(f"\n{tag}  {r.path}")
            for f in r.failures:
                print(f"  \033[31mx\033[0m {f}" if not f.startswith("    ") else f"  {f}")
            for w in r.warnings:
                print(f"  \033[33m!\033[0m {w}")
        n_fail = sum(1 for r in results if not r.passed)
        print(f"\n\033[1m{len(results)} file(s) verified, {n_fail} failed\033[0m")

    return 1 if any(not r.passed for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
