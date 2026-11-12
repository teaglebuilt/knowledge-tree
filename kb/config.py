"""Central config for the knowledge pipeline. Everything is env-overridable."""
from __future__ import annotations

import logging
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

# Local dir or object-store URI (s3://bucket/prefix). Kept as a string: Path()
# would collapse "s3://" to "s3:/".
_lancedb = os.environ.get("KB_LANCEDB", "").strip()
if not _lancedb:
    LANCEDB_URI = str(ROOT / ".lancedb")
elif "://" in _lancedb:
    LANCEDB_URI = _lancedb
else:
    LANCEDB_URI = str(Path(_lancedb).expanduser())

# Passed straight to lancedb.connect(storage_options=...) for s3:// URIs.
# SeaweedFS/MinIO need endpoint + allow_http; keys fall back to the AWS_* env.
_s3_opts = {
    "endpoint": os.environ.get("KB_S3_ENDPOINT") or os.environ.get("AWS_ENDPOINT_URL"),
    "region": os.environ.get("KB_S3_REGION") or os.environ.get("AWS_REGION") or "us-east-1",
    "access_key_id": os.environ.get("KB_S3_ACCESS_KEY_ID") or os.environ.get("AWS_ACCESS_KEY_ID"),
    "secret_access_key": (
        os.environ.get("KB_S3_SECRET_ACCESS_KEY") or os.environ.get("AWS_SECRET_ACCESS_KEY")
    ),
    "allow_http": os.environ.get("KB_S3_ALLOW_HTTP", "false").strip().lower(),
}
LANCEDB_STORAGE_OPTIONS = (
    {k: v for k, v in _s3_opts.items() if v} if LANCEDB_URI.startswith("s3://") else {}
)

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

# kb_get_document paging, in chunks (~CHILD_TOKENS each) per call.
KB_DOCUMENT_PAGE_CHUNKS = int(os.environ.get("KB_DOCUMENT_PAGE_CHUNKS", "24"))
KB_DOCUMENT_MAX_PAGE_CHUNKS = int(os.environ.get("KB_DOCUMENT_MAX_PAGE_CHUNKS", "60"))


def _csv(name: str, default: str) -> tuple[str, ...]:
    return tuple(p.strip() for p in os.environ.get(name, default).split(",") if p.strip())


def _flag(name: str, default: str = "false") -> bool:
    return os.environ.get(name, default).strip().lower() in {"1", "true", "yes", "on"}


# --- kb-api / kb-mcp-write service configuration ----------------------------
# Renamed from KB_INGEST_* / KB_MCP_INGEST_* (docs/api.md#configuration). The
# old names still resolve during the migration window, with a warning; setting
# both to different values is an error rather than a silent pick.
_LEGACY_ENV = {
    "KB_API_WRITE_TOKEN": "KB_INGEST_TOKEN",
    "KB_API_ALLOW_ANONYMOUS_WRITES": "KB_INGEST_ALLOW_ANONYMOUS",
    "KB_API_WRITE_PATH_PREFIXES": "KB_INGEST_PATH_PREFIXES",
    "KB_API_MAX_BODY_BYTES": "KB_INGEST_MAX_BODY_BYTES",
    "KB_API_HOST": "KB_INGEST_HOST",
    "KB_API_PORT": "KB_INGEST_PORT",
    "KB_MCP_WRITE_PATH_PREFIXES": "KB_MCP_INGEST_PATH_PREFIXES",
    "KB_MCP_WRITE_SOURCE_TYPES": "KB_MCP_INGEST_SOURCE_TYPES",
    "KB_MCP_WRITE_MAX_BYTES": "KB_MCP_INGEST_MAX_BYTES",
}


def env_compat(name: str, default: str) -> str:
    """Resolve `name`, falling back to its deprecated alias in _LEGACY_ENV."""
    legacy = _LEGACY_ENV.get(name)
    value = os.environ.get(name)
    old = os.environ.get(legacy) if legacy else None
    if value is not None and old is not None and value.strip() != old.strip():
        raise ValueError(f"{name} and deprecated {legacy} are both set and differ; unset {legacy}")
    if value is not None:
        return value
    if old is not None:
        logging.getLogger("kb.config").warning("%s is deprecated; set %s instead", legacy, name)
        return old
    return default


def _csv_compat(name: str, default: str) -> tuple[str, ...]:
    return tuple(p.strip() for p in env_compat(name, default).split(",") if p.strip())


def _flag_compat(name: str, default: str = "false") -> bool:
    return env_compat(name, default).strip().lower() in {"1", "true", "yes", "on"}


#: Tokens, by scope. write implies read; admin implies write. With no admin
#: token, the write token also authorizes admin (DELETE), matching the old
#: single-token behaviour. With no read token, reads are open — the same
#: exposure the in-cluster read MCP has. Writes with no write token are
#: REFUSED unless KB_API_ALLOW_ANONYMOUS_WRITES=true: private history must
#: never land through an open door by omission.
KB_API_WRITE_TOKEN = env_compat("KB_API_WRITE_TOKEN", "").strip()
KB_API_READ_TOKEN = os.environ.get("KB_API_READ_TOKEN", "").strip()
KB_API_ADMIN_TOKEN = os.environ.get("KB_API_ADMIN_TOKEN", "").strip()
#: Local dev opts in explicitly; the cluster never should.
KB_API_ALLOW_ANONYMOUS_WRITES = _flag_compat("KB_API_ALLOW_ANONYMOUS_WRITES")

#: Paths the HTTP writer (n8n) may own. Must stay DISJOINT from what `kb sync`
#: owns, or a sync prune deletes API-authored documents.
KB_API_WRITE_PATH_PREFIXES = _csv_compat("KB_API_WRITE_PATH_PREFIXES", "tree/")
#: HTTP body cap for every route, including /mcp.
KB_API_MAX_BODY_BYTES = int(env_compat("KB_API_MAX_BODY_BYTES", str(2 * 1024 * 1024)))
KB_API_HOST = env_compat("KB_API_HOST", "0.0.0.0")
KB_API_PORT = int(env_compat("KB_API_PORT", "3000"))

# Agents (kb-mcp-write) get a narrower slice than the HTTP callers: their own
# path prefix, a closed set of source types, a size cap, and a mandatory
# source_url so every agent-written document carries provenance.
KB_MCP_WRITE_PATH_PREFIXES = _csv_compat("KB_MCP_WRITE_PATH_PREFIXES", "tree/docs/")
KB_MCP_WRITE_SOURCE_TYPES = _csv_compat("KB_MCP_WRITE_SOURCE_TYPES", "documentation")
KB_MCP_WRITE_MAX_BYTES = int(env_compat("KB_MCP_WRITE_MAX_BYTES", str(512 * 1024)))
#: Also serve the pre-rename tool names (kb_ingest, kb_ingest_status) on the
#: write MCP while agents migrate. Never on the read MCP. Removed in a later release.
KB_MCP_WRITE_LEGACY_TOOLS = _flag("KB_MCP_WRITE_LEGACY_TOOLS", "true")

#: source_type values no writer outside its owner may claim. `tree` is pruned
#: by `kb sync`; the memory types belong to the import/approval pipeline.
KB_RESERVED_SOURCE_TYPES = frozenset(
    _csv("KB_RESERVED_SOURCE_TYPES", "tree,chatgpt,chatgpt_export,memory")
)

# --- Private conversation archive (ChatGPT import) ---------------------------
# Separate collection, same embedding space. Never the `knowledge` collection:
# historical chat is unverified and private, and must not leak into kb_search.
CHATGPT_HISTORY_COLLECTION = os.environ.get("KB_CHATGPT_COLLECTION", "chatgpt_history")
if CHATGPT_HISTORY_COLLECTION == QDRANT_COLLECTION:
    raise ValueError("KB_CHATGPT_COLLECTION must differ from the knowledge collection")
# Normalized JSONL + checkpoints. Must live outside the public checkout.
_archive = os.environ.get("KB_ARCHIVE_DIR", "").strip()
ARCHIVE_DIR = (
    Path(_archive).expanduser() if _archive else Path.home() / ".local/share/kb/archive"
)
#: Roles indexed from exports. `tool` / `system` messages are recorded, not embedded.
CHATGPT_INDEX_ROLES = _csv("KB_CHATGPT_INDEX_ROLES", "user,assistant")
CHATGPT_REDACTION_VERSION = "v1"
