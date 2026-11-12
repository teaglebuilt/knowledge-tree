"""Entry: python -m kb.mcp [--transport stdio|streamable-http] (read plane only)."""
from __future__ import annotations

import argparse
import os
import sys

from .. import config
from .read import mcp


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="kb.mcp",
        description="Knowledge-tree read MCP, kb-mcp-read (kb_search, kb_get_document -> Qdrant)",
    )
    parser.add_argument(
        "--transport",
        choices=("stdio", "sse", "streamable-http"),
        default=os.environ.get("MCP_TRANSPORT", "stdio"),
    )
    parser.add_argument("--host", default=os.environ.get("MCP_HOST", "0.0.0.0"))
    parser.add_argument(
        "--port",
        type=int,
        default=int(os.environ.get("MCP_PORT", "3000")),
    )
    args = parser.parse_args(argv)

    print(
        f"kb-mcp-read: network={config.QDRANT_NETWORK} "
        f"url={config.QDRANT_URL} collection={config.QDRANT_COLLECTION} "
        f"transport={args.transport}",
        file=sys.stderr,
    )

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    else:
        mcp.run(transport=args.transport, host=args.host, port=args.port)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
