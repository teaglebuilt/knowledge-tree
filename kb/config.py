"""Central config for the knowledge pipeline. Everything is env-overridable."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIRS = os.environ.get("KB_DIRS", "tree").split(",")

_vol = os.environ.get("KNOWLEDGE_VOLUME_PATH", "").strip()
SOURCE_VOLUME = Path(_vol).expanduser() if _vol else None

# Local staging dir when the volume is TCC-blocked for Python (macOS /Volumes).
# Finder can still copy; extract stages there then reads.
_cache = os.environ.get("KB_SOURCE_CACHE", "").strip()
SOURCE_CACHE = Path(_cache).expanduser() if _cache else ROOT / ".cache" / "sources"

TREE_DIR = os.environ.get("KB_TREE_DIR", "tree")
BRANCHES_PATH = Path(os.environ.get("KB_BRANCHES", ROOT / TREE_DIR / "branches.yaml"))
SOPS_CONFIG_PATH = Path(os.environ.get("KB_SOPS_CONFIG", ROOT / ".sops.yaml"))

LANCEDB_PATH = Path(os.environ.get("KB_LANCEDB", ROOT / ".lancedb"))
DUCKDB_PATH = Path(os.environ.get("KB_DUCKDB", ROOT / "kb.duckdb"))

LANCE_TABLE = os.environ.get("KB_LANCE_TABLE", "chunks")

# Story / chart aliases: EMBEDDING_MODEL, COLLECTION_NAME
EMBED_MODEL = (
    os.environ.get("EMBEDDING_MODEL")
    or os.environ.get("KB_EMBED_MODEL")
    or "BAAI/bge-small-en-v1.5"
)
EMBED_DIM = int(os.environ.get("KB_EMBED_DIM", "384"))

CHILD_TOKENS = int(os.environ.get("KB_CHILD_TOKENS", "450"))
CHILD_OVERLAP = int(os.environ.get("KB_CHILD_OVERLAP", "60"))

GOLDEN_PATH = Path(os.environ.get("KB_GOLDEN", ROOT / "eval" / "golden.yaml"))

# Qdrant network mode selects cluster DNS vs gateway when QDRANT_URL is unset.
#   internal — in-cluster Service DNS (application/data next to Qdrant)
#   external — cross-cluster / laptop via ingress gateway
_qdrant_network = os.environ.get("QDRANT_NETWORK", "external").strip().lower()
if _qdrant_network in {"internal", "incluster", "cluster", "in-cluster"}:
    QDRANT_NETWORK = "internal"
elif _qdrant_network in {"external", "gateway", "outcluster", "out-of-cluster"}:
    QDRANT_NETWORK = "external"
else:
    raise ValueError(
        f"QDRANT_NETWORK={_qdrant_network!r}; expected 'internal' or 'external'"
    )

QDRANT_INTERNAL_URL = os.environ.get(
    "QDRANT_INTERNAL_URL", "http://qdrant.data.svc.cluster.local:6333"
)
QDRANT_EXTERNAL_URL = os.environ.get(
    "QDRANT_EXTERNAL_URL", "https://qdrant.homelab.internal"
)

if os.environ.get("QDRANT_URL"):
    QDRANT_URL = os.environ["QDRANT_URL"]
elif QDRANT_NETWORK == "internal":
    QDRANT_URL = QDRANT_INTERNAL_URL
else:
    QDRANT_URL = QDRANT_EXTERNAL_URL

QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")  # optional
QDRANT_COLLECTION = (
    os.environ.get("COLLECTION_NAME")
    or os.environ.get("QDRANT_COLLECTION")
    or "knowledge"
)

# TLS verify: default off for external gateway (homelab CA); on for in-cluster HTTP.
_default_verify = "true" if QDRANT_NETWORK == "internal" else "false"
_qdrant_verify = os.environ.get("QDRANT_VERIFY", _default_verify).strip()
if _qdrant_verify.lower() in {"0", "false", "no", "off"}:
    QDRANT_VERIFY: bool | str = False
elif _qdrant_verify.lower() in {"1", "true", "yes", "on"}:
    QDRANT_VERIFY = True
else:
    QDRANT_VERIFY = _qdrant_verify  # path to CA bundle

KB_SEARCH_DEFAULT_K = int(os.environ.get("KB_SEARCH_DEFAULT_K", "8"))
KB_SEARCH_MAX_K = int(os.environ.get("KB_SEARCH_MAX_K", "20"))
