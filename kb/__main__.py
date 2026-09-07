"""CLI: python -m kb <command>. Wired to the Makefile targets."""
from __future__ import annotations

import argparse
import sys


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="kb", description="Knowledge base RAG pipeline")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_ext = sub.add_parser("extract", help="convert sources declared in branches.yaml -> tree/ markdown")
    p_ext.add_argument("--force", action="store_true", help="re-extract unchanged sources")

    p_ing = sub.add_parser("ingest", help="incremental ingest markdown -> LanceDB")
    p_ing.add_argument("--force", action="store_true", help="re-embed all docs")

    sub.add_parser("reindex", help="rebuild the BM25 full-text index")

    p_q = sub.add_parser("query", help="hybrid search the local index")
    p_q.add_argument("question", nargs="+")
    p_q.add_argument("-k", type=int, default=6)
    p_q.add_argument("--expand", action="store_true", help="show parent sections")

    sub.add_parser("sync", help="push local vectors -> Qdrant (k8s)")

    sub.add_parser("eval", help="recall@k / MRR against eval/golden.yaml")

    p_sec = sub.add_parser("secrets", help="sops encryption policy from tree/branches.yaml")
    sec = p_sec.add_subparsers(dest="action", required=True)
    p_st = sec.add_parser("status", help="per-file: policy vs on-disk state")
    p_st.add_argument("paths", nargs="*", help="limit to these pathspecs")
    p_st.add_argument("--all", action="store_true",
                      help="include files that are plaintext by default")

    for action, helptext in [
        ("encrypt", "encrypt everything branches.yaml marks encrypted"),
        ("decrypt", "decrypt in place for Obsidian / ingest"),
    ]:
        s = sec.add_parser(action, help=helptext)
        s.add_argument("paths", nargs="*", help="limit to these pathspecs")

    p_chk = sec.add_parser("check", help="exit 1 if any file violates the policy")
    p_chk.add_argument("paths", nargs="*")
    p_chk.add_argument("--staged", action="store_true",
                       help="inspect staged blobs rather than the working tree")

    p_cfg = sec.add_parser("config", help="regenerate .sops.yaml from branches.yaml")
    p_cfg.add_argument("--kms", help="KMS ARN (default: reuse the one in .sops.yaml)")
    p_cfg.add_argument("--check", action="store_true",
                       help="exit 1 if .sops.yaml is stale instead of rewriting it")

    args = p.parse_args(argv)

    if args.cmd == "extract":
        from .extract import run as run_extract
        stats = run_extract(force=args.force)
        return 1 if stats["failed"] else 0
    elif args.cmd == "ingest":
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
    elif args.cmd == "secrets":
        from . import secrets
        if args.action == "check":
            return secrets.check(args.paths, staged=args.staged)
        if args.action == "config":
            return secrets.gen_sops_config(args.kms, check_only=args.check)
        if args.action == "status":
            return secrets.status(args.paths, show_all=args.all)
        return getattr(secrets, args.action)(args.paths)
    return 0


if __name__ == "__main__":
    sys.exit(main())
