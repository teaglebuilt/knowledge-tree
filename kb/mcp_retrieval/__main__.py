"""Entry: python -m kb.mcp_retrieval [--transport stdio|streamable-http]."""
from __future__ import annotations

import argparse
import os
import sys

from .. import config
from .server import mcp


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="kb.mcp_retrieval",
        description="Knowledge-tree MCP read plane (kb_search → Qdrant)",
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
        f"kb-retrieval: network={config.QDRANT_NETWORK} "
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
