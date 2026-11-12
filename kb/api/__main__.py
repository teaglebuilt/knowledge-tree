"""Entry: python -m kb.api [--host H] [--port P]."""
from __future__ import annotations

import argparse
import sys

from .. import config


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="kb.api",
        description="Knowledge Tree API (/v1 REST + write MCP at /mcp -> Qdrant)",
    )
    parser.add_argument("--host", default=config.KB_API_HOST)
    parser.add_argument("--port", type=int, default=config.KB_API_PORT)
    args = parser.parse_args(argv)

    print(
        f"kb-api: network={config.QDRANT_NETWORK} url={config.QDRANT_URL} "
        f"collection={config.QDRANT_COLLECTION} dim={config.EMBED_DIM} "
        f"model={config.EMBED_MODEL} write_token={'set' if config.KB_API_WRITE_TOKEN else 'unset'} "
        f"anonymous_writes={config.KB_API_ALLOW_ANONYMOUS_WRITES}",
        file=sys.stderr,
    )

    import uvicorn

    uvicorn.run("kb.api.app:app", host=args.host, port=args.port, log_level="info")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
