"""CLI: python -m kb <command>. Wired to the Makefile targets."""
from __future__ import annotations

import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="kb", description="Knowledge base RAG pipeline")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_ing = sub.add_parser("ingest", help="incremental ingest markdown -> LanceDB")
    p_ing.add_argument("--force", action="store_true", help="re-embed all docs")

    sub.add_parser("reindex", help="rebuild the BM25 full-text index")

    p_q = sub.add_parser("query", help="hybrid search the local index")
    p_q.add_argument("question", nargs="+")
    p_q.add_argument("-k", type=int, default=6)
    p_q.add_argument("--expand", action="store_true", help="show parent sections")

    sub.add_parser("sync", help="push local vectors -> Qdrant (k8s)")

    sub.add_parser("eval", help="recall@k / MRR against eval/golden.yaml")

    args = p.parse_args(argv)

    if args.cmd == "ingest":
        from .ingest import run
        run(force=args.force)
    elif args.cmd == "reindex":
        from .ingest import reindex
        reindex()
    elif args.cmd == "query":
        from .query import format_results, search
        results = search(" ".join(args.question), k=args.k)
        print(format_results(results, expand=args.expand))
    elif args.cmd == "sync":
        from .sync import push
        push()
    elif args.cmd == "eval":
        from .eval import run as run_eval
        run_eval()
    return 0


if __name__ == "__main__":
    sys.exit(main())
