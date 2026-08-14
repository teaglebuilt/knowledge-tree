"""Retrieval eval: recall@k and MRR against a labeled golden set.

Turns tuning from guessing into measuring. Change one knob (chunk size, embed
model, hybrid weighting), re-run, and see whether the numbers move.
"""
from __future__ import annotations

import yaml

from . import config
from .query import search


def _load_golden() -> list[dict]:
    if not config.GOLDEN_PATH.exists():
        raise SystemExit(
            f"No golden set at {config.GOLDEN_PATH}. Add questions there first."
        )
    data = yaml.safe_load(config.GOLDEN_PATH.read_text()) or []
    if not data:
        raise SystemExit(f"Golden set {config.GOLDEN_PATH} is empty.")
    return data


def _hit_rank(results: list[dict], relevant: list[str]) -> int | None:
    """1-based rank of the first result whose path matches any relevant suffix."""
    for i, r in enumerate(results, 1):
        path = r.get("path") or ""
        if any(path.endswith(rel) or rel in path for rel in relevant):
            return i
    return None


def run(ks: tuple[int, ...] = (1, 3, 6, 10)) -> dict:
    golden = _load_golden()
    kmax = max(ks)
    recall = {k: 0 for k in ks}
    rr_sum = 0.0
    misses: list[str] = []

    for item in golden:
        q = item["question"]
        relevant = item.get("relevant", [])
        results = search(q, k=kmax)
        rank = _hit_rank(results, relevant)
        if rank is None:
            misses.append(q)
        else:
            rr_sum += 1.0 / rank
            for k in ks:
                if rank <= k:
                    recall[k] += 1

    n = len(golden)
    print(f"\nGolden set: {n} questions\n" + "-" * 32)
    for k in ks:
        print(f"  recall@{k:<2} = {recall[k] / n:.2f}  ({recall[k]}/{n})")
    print(f"  MRR      = {rr_sum / n:.3f}")
    if misses:
        print(f"\nMissed entirely (not in top {kmax}):")
        for q in misses:
            print(f"  - {q}")
    return {"n": n, "recall": {k: recall[k] / n for k in ks}, "mrr": rr_sum / n}
