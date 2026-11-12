# Write plane (`kb-ingest`)

An HTTP front door that takes one markdown document and lands it in the Qdrant
`knowledge` collection, for callers that have no filesystem — in practice the
n8n YouTube ingestion workflow.

## Why it exists

The local pipeline (`make ingest && make sync`) is filesystem-driven: it walks
`tree/**/*.md`, hash-gates against DuckDB, embeds into LanceDB, then pushes
LanceDB to Qdrant. Automated sources have no laptop in the loop.

The alternative was letting the caller embed and upsert itself. That was
rejected: it would need its own embedding model (drifting from
`BAAI/bge-small-en-v1.5` / 384-d and silently corrupting the one collection),
its own chunking, and its own point-id scheme. Instead the write plane reuses
`kb.chunk` and `kb.embed` unchanged, so there is still exactly one chunker and
one embedding space. It runs the same image as `kb-retrieval`, which already
bakes the FastEmbed weights.

## Contract

```
POST /ingest
{
  "path":        "tree/youtube/<slug>.md",   # required, stable document identity
  "markdown":    "---\ntitle: …\n---\n\n…",  # required, frontmatter + body
  "source_type": "youtube",                   # optional, else frontmatter, else "unknown"
  "source_url":  "https://…",                 # optional, else frontmatter
  "force":       false                        # optional, re-embed even if unchanged
}
→ {"path":…, "doc_hash":…, "chunks":12, "status":"ingested"|"unchanged"|"empty"}

GET  /exists?path=tree/youtube/<slug>.md
→ {"path":…, "exists":true|false, "doc_hash":…|null}

POST /delete   {"path": "tree/youtube/<slug>.md"}
GET  /healthz  GET /readyz
```

`status: unchanged` means every stored point for that path already carries the
submitted body's `doc_hash`, so nothing was re-embedded.

`/exists` lets a poller skip work it has already done without paying for the
upstream fetch first. The n8n YouTube workflow gates on it so that a failed
transcript fetch leaves the path absent and is retried on the next poll —
dedupe state held by the caller would instead mark the video seen and drop it
permanently.

### Agent MCP endpoint (`/mcp`)

The same process serves MCP tools `kb_ingest` and `kb_ingest_status` over
stateless streamable HTTP at `/mcp`, for kagent agents (registered as the
`kb-ingest` RemoteMCPServer). It is narrower than `POST /ingest`: only
`tree/docs/`, `source_type: documentation`, a required `source_url`, and a
512 KiB cap. It returns a JSON receipt. Why this lives here and not on kb-retrieval,
and how delegating agents use the receipt as their completion signal, is covered in
[`stories/import-memory.md` §15](stories/import-memory.md).

### Auth

Every write (`/ingest`, `/delete`, `/mcp`) requires `KB_INGEST_TOKEN`, sent as
`Authorization: Bearer <t>` or `X-KB-Ingest-Token: <t>`. With the token unset,
writes are **refused**. Set `KB_INGEST_ALLOW_ANONYMOUS=true` to allow them, which
`make ingest-api` does for local dev only. `source_type` values `tree`,
`chatgpt*` and `memory` are reserved and rejected.

## Idempotency and replacement

`chunk_id` is `"{path}::{doc_hash[:8]}::{index}"` and the Qdrant point id is a
deterministic UUID over it, so re-posting identical content upserts in place.

Re-posting *edited* content produces a new `doc_hash`, hence new chunk ids, so
the previous revision's points would linger. The write plane deletes by
`path` filter before upserting — which is why `path`, `doc_hash` and
`source_type` are now keyword payload indexes (`adapters.qdrant.ensure_payload_indexes`).

## Payload

Adds `doc_hash`, `chunk_index`, `title`, `source_type` and `source_url` on top
of the `chunk_id` / `path` / `heading` / `text` / `tags` that `kb sync` already
wrote. Additive, so `kb_search` is unaffected. `kb sync` now stamps
`source_type: tree` so the two writers' documents are distinguishable.

## Known divergence

Documents ingested this way exist in Qdrant but **not** in LanceDB/DuckDB, so
local BM25 hybrid search does not see them. `kb_search` is dense-only against
Qdrant, so retrieval through the MCP read plane is unaffected. `kb ingest`'s
prune step only compares the local tree against LanceDB, so it will not delete
them either — the two writers coexist as long as they own disjoint paths.
`KB_INGEST_PATH_PREFIXES` (default `tree/`) bounds what the write plane may own;
narrow it to `tree/youtube/` if you want that enforced rather than conventional.

## Deploy

Install into the cluster that hosts Qdrant and the callers:

```sh
make helm-deploy-ingest                      # context application, QDRANT_API_KEY from .envrc
```

The read plane (`kb-retrieval`) and the `knowledge-scout` agent stay on mlops
with kagent; `make helm-deploy` is unchanged.

How documents are read back out — and the embedding-space invariant that
OpenWebUI's reader imposes — is in [`read-plane.md`](read-plane.md).
