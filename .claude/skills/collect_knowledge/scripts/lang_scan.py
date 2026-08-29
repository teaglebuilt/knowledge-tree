#!/usr/bin/env python3
"""
lang_scan.py -- find content that still needs translating, and plan the work.

This is the detector half of the translate-then-verify loop. It answers three
questions cheaply, with no model tokens involved:

  1. Which files in this corpus are not in English, and how badly?
  2. Within a file, *which lines* -- and is that line prose that must be
     translated, or a URL that must not be?
  3. How should a large file be cut into translation-sized pieces?

Usage
-----
  # Triage a corpus before starting
  lang_scan.py ~/corpus --summary

  # Per-file detail with sample lines
  lang_scan.py ~/corpus/doc.md --show 20

  # Machine-readable, for driving a batch
  lang_scan.py ~/corpus --json > scan.json

  # Plan the chunks for one large file
  lang_scan.py ~/corpus/big.md --plan

  # Use as a CI / pre-merge gate (exit 1 if anything blocking remains)
  lang_scan.py ./tree --gate

Exit codes: 0 = no blocking findings (or --gate not passed), 1 = blocking
findings present, 2 = bad invocation.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Resolve sibling imports so this script runs from any working directory.
sys.path.insert(0, str(Path(__file__).resolve().parent))

import mdlang
from mdlang import (
    SCRIPT_TO_LANGUAGE_HINT,
    Finding,
    density_bucket,
    discover,
    dominant_script,
    load_config,
    plan_chunks,
    read_text,
    scan_text,
    severity,
)


def analyse(path: Path, config: dict) -> dict:
    text = read_text(path)
    findings, per_cat = scan_text(text, config)
    total_lines = text.count("\n") + 1
    lines_with = len({f.line for f in findings})
    blocking = [f for f in findings if severity(f.category, config) == "BLOCK"]
    warning = [f for f in findings if severity(f.category, config) == "WARN"]
    script = dominant_script(text)
    return {
        "path": str(path),
        "total_lines": total_lines,
        "lines_with_non_latin": lines_with,
        "bucket": density_bucket(lines_with, total_lines),
        "dominant_script": script,
        "language_hint": SCRIPT_TO_LANGUAGE_HINT.get(script or "", "unknown") if script else None,
        "by_category": per_cat,
        "blocking_chars": sum(f.count for f in blocking),
        "warning_chars": sum(f.count for f in warning),
        "n_blocking_lines": len({f.line for f in blocking}),
        "findings": [
            {
                "line": f.line,
                "category": f.category,
                "severity": severity(f.category, config),
                "script": f.script,
                "count": f.count,
                "text": f.text,
            }
            for f in findings
        ],
    }


def print_file_report(rep: dict, show: int, config: dict) -> None:
    rel = rep["path"]
    hint = rep["language_hint"] or "-"
    print(f"\n\033[1m{rel}\033[0m")
    print(
        f"  {rep['bucket']}  "
        f"{rep['lines_with_non_latin']}/{rep['total_lines']} lines contain non-Latin text  "
        f"(likely {hint})"
    )
    if rep["by_category"]:
        parts = []
        for cat in mdlang.ALL_CATEGORIES:
            n = rep["by_category"].get(cat)
            if n:
                sev = severity(cat, config)
                mark = {"BLOCK": "!", "WARN": "~", "INFO": " "}[sev]
                parts.append(f"{mark}{cat}={n}")
        print("  " + "  ".join(parts))
    if show:
        blocking = [f for f in rep["findings"] if f["severity"] == "BLOCK"]
        for f in blocking[:show]:
            print(f"    L{f['line']:<5} {f['category']:<14} {f['text']}")
        if len(blocking) > show:
            print(f"    ... {len(blocking) - show} more blocking lines "
                  f"(raise --show to see them)")


def cmd_plan(paths: list[Path], config: dict, as_json: bool) -> int:
    out = []
    for p in paths:
        text = read_text(p)
        chunks = plan_chunks(text, config["max_chunk_lines"])
        entry = {
            "path": str(p),
            "total_lines": text.count("\n") + 1,
            "n_chunks": len(chunks),
            "chunks": [
                {
                    "index": c.index,
                    "start_line": c.start_line,
                    "end_line": c.end_line,
                    "lines": c.end_line - c.start_line + 1,
                    "heading": c.heading,
                }
                for c in chunks
            ],
        }
        out.append(entry)
        if not as_json:
            print(f"\n\033[1m{p}\033[0m  ({entry['total_lines']} lines -> {len(chunks)} chunks)")
            for c in chunks:
                print(f"  chunk {c.index:<3} lines {c.start_line}-{c.end_line} "
                      f"({c.end_line - c.start_line + 1:>4})  {c.heading}")
    if as_json:
        json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
        print()
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        prog="lang_scan.py",
        description="Detect untranslated content in a markdown corpus.",
    )
    ap.add_argument("paths", nargs="+", help="files or directories to scan")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--summary", action="store_true",
                    help="corpus-level counts only, no per-file detail")
    ap.add_argument("--plan", action="store_true",
                    help="emit a chunk plan for each file instead of scanning")
    ap.add_argument("--gate", action="store_true",
                    help="exit 1 if any blocking findings remain")
    ap.add_argument("--show", type=int, default=8,
                    help="sample blocking lines to print per file (default 8)")
    ap.add_argument("--clean-only", action="store_true",
                    help="list only files with no findings")
    ap.add_argument("--bucket", choices=["HEAVY", "PARTIAL", "TRACE", "CLEAN"],
                    help="list only files in this density bucket")
    ap.add_argument("--config", help="JSON config overriding the defaults")
    ap.add_argument("--ext", action="append",
                    help="file extension to include (repeatable; default .md .markdown .txt .rst .mdx)")
    args = ap.parse_args(argv)

    config = load_config(args.config)

    files: list[Path] = []
    for raw in args.paths:
        p = Path(raw).expanduser()
        if not p.exists():
            print(f"error: no such path: {p}", file=sys.stderr)
            return 2
        files.extend(discover(p, args.ext))
    if not files:
        print("error: no matching files found", file=sys.stderr)
        return 2

    if args.plan:
        return cmd_plan(files, config, args.json)

    reports = [analyse(f, config) for f in files]

    if args.bucket:
        reports = [r for r in reports if r["bucket"] == args.bucket]
    if args.clean_only:
        reports = [r for r in reports if r["blocking_chars"] == 0]

    if args.json:
        json.dump(
            {
                "n_files": len(reports),
                "n_blocking_files": sum(1 for r in reports if r["blocking_chars"]),
                "files": reports,
            },
            sys.stdout, indent=2, ensure_ascii=False,
        )
        print()
    else:
        buckets: dict[str, int] = {}
        scripts: dict[str, int] = {}
        for r in reports:
            buckets[r["bucket"]] = buckets.get(r["bucket"], 0) + 1
            if r["dominant_script"]:
                scripts[r["dominant_script"]] = scripts.get(r["dominant_script"], 0) + 1

        if not args.summary:
            for r in reports:
                if r["blocking_chars"] or r["warning_chars"] or args.clean_only:
                    print_file_report(r, args.show, config)

        print(f"\n\033[1m{len(reports)} file(s) scanned\033[0m")
        for b in ("HEAVY", "PARTIAL", "TRACE", "CLEAN"):
            if buckets.get(b):
                print(f"  {b:<8} {buckets[b]}")
        if scripts:
            print("  scripts: " + ", ".join(f"{k}={v}" for k, v in sorted(scripts.items())))
        n_block = sum(1 for r in reports if r["blocking_chars"])
        print(f"  {n_block} file(s) have blocking findings "
              f"({sum(r['blocking_chars'] for r in reports)} characters)")

    if args.gate and any(r["blocking_chars"] for r in reports):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
