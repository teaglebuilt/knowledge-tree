"""Entry: python -m kb.ingest_api [--host H] [--port P]."""
from __future__ import annotations

import argparse
import os
import sys

from .. import config


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="kb.ingest_api",
        description="Knowledge write plane (POST /ingest -> Qdrant)",
    )
    parser.add_argument("--host", default=os.environ.get("KB_INGEST_HOST", "0.0.0.0"))
    parser.add_argument(
        "--port", type=int, default=int(os.environ.get("KB_INGEST_PORT", "3000"))
    )
    args = parser.parse_args(argv)

    print(
        f"kb-ingest: network={config.QDRANT_NETWORK} url={config.QDRANT_URL} "
        f"collection={config.QDRANT_COLLECTION} dim={config.EMBED_DIM} "
        f"model={config.EMBED_MODEL}",
        file=sys.stderr,
    )

    import uvicorn

    uvicorn.run("kb.ingest_api.app:app", host=args.host, port=args.port, log_level="info")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
