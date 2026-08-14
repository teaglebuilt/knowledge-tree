"""Central config for the knowledge pipeline. Everything is env-overridable."""
from __future__ import annotations

import os
from pathlib import Path

# Repo root = parent of this package.
ROOT = Path(__file__).resolve().parent.parent

# Root(s) holding ingestable markdown — the Obsidian vault under `tree/`.
# A single root is rglob'd, so new domain dirs are picked up automatically.
KNOWLEDGE_DIRS = os.environ.get("KB_DIRS", "tree").split(",")

# Local stores (gitignored). LanceDB is the primary read path.
LANCEDB_PATH = Path(os.environ.get("KB_LANCEDB", ROOT / ".lancedb"))
DUCKDB_PATH = Path(os.environ.get("KB_DUCKDB", ROOT / "kb.duckdb"))
LANCE_TABLE = os.environ.get("KB_LANCE_TABLE", "chunks")

# Local embedding model (no API, works offline). BGE-small = 384 dims.
EMBED_MODEL = os.environ.get("KB_EMBED_MODEL", "BAAI/bge-small-en-v1.5")
EMBED_DIM = int(os.environ.get("KB_EMBED_DIM", "384"))

# Chunking (header-aware parent-child). Sizes are token estimates.
CHILD_TOKENS = int(os.environ.get("KB_CHILD_TOKENS", "450"))
CHILD_OVERLAP = int(os.environ.get("KB_CHILD_OVERLAP", "60"))

# Golden set for retrieval eval (recall@k). See `eval/golden.yaml`.
GOLDEN_PATH = Path(os.environ.get("KB_GOLDEN", ROOT / "eval" / "golden.yaml"))

# Qdrant on the k8s cluster (the shared/sync target, NOT the hot read path).
# Reach it via port-forward (kubectl -n <ns> port-forward svc/qdrant 6333:6333)
# or an ingress URL. e.g. QDRANT_URL=http://localhost:6333
QDRANT_URL = os.environ.get("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")  # optional
QDRANT_COLLECTION = os.environ.get("QDRANT_COLLECTION", "knowledge")
