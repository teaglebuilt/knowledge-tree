"""Central config for the knowledge pipeline. Everything is env-overridable."""
from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

KNOWLEDGE_DIRS = os.environ.get("KB_DIRS", "tree").split(",")
SOURCES_DIR = Path(os.environ.get("KB_SOURCES", ROOT / "sources"))

# Encryption policy: which subtrees sops encrypts, and the config generated
# from it. TREE_DIR is the vault root that branches.yaml describes.
TREE_DIR = os.environ.get("KB_TREE_DIR", "tree")
BRANCHES_PATH = Path(os.environ.get("KB_BRANCHES", ROOT / TREE_DIR / "branches.yaml"))
SOPS_CONFIG_PATH = Path(os.environ.get("KB_SOPS_CONFIG", ROOT / ".sops.yaml"))

LANCEDB_PATH = Path(os.environ.get("KB_LANCEDB", ROOT / ".lancedb"))
DUCKDB_PATH = Path(os.environ.get("KB_DUCKDB", ROOT / "kb.duckdb"))

LANCE_TABLE = os.environ.get("KB_LANCE_TABLE", "chunks")

EMBED_MODEL = os.environ.get("KB_EMBED_MODEL", "BAAI/bge-small-en-v1.5")
EMBED_DIM = int(os.environ.get("KB_EMBED_DIM", "384"))

CHILD_TOKENS = int(os.environ.get("KB_CHILD_TOKENS", "450"))
CHILD_OVERLAP = int(os.environ.get("KB_CHILD_OVERLAP", "60"))

GOLDEN_PATH = Path(os.environ.get("KB_GOLDEN", ROOT / "eval" / "golden.yaml"))

QDRANT_URL = os.environ.get("QDRANT_URL", "http://localhost:6333")
QDRANT_API_KEY = os.environ.get("QDRANT_API_KEY")  # optional
QDRANT_COLLECTION = os.environ.get("QDRANT_COLLECTION", "knowledge")
