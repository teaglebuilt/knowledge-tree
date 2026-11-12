# Write plane (`kb-api`)

> The HTTP contract is [`api.md`](api.md) and the MCP surfaces are [`mcp.md`](mcp.md); those are canonical. This page keeps the write-plane origin and invariants.

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
one embedding space. It runs the same image as `kb-mcp-read` (`ghcr.io/teaglebuilt/kb`), which already
bakes the FastEmbed weights.

## Contract

Full route, schema and error reference: [`api.md`](api.md).

```
POST /v1/documents
{
  "path":        "tree/youtube/<slug>.md",   # required, stable document identity
  "markdown":    "---\ntitle: …\n---\n\n…",  # required, frontmatter + body
  "source_type": "youtube",                   # optional, else frontmatter, else "unknown"
  "source_url":  "https://…",                 # optional, else frontmatter
  "title": "…", "tags": ["…"],                # optional
  "force":       false                        # optional, re-embed even if unchanged
}
→ {"path":…, "doc_hash":…, "chunks":12, "status":"ingested"|"unchanged"|"empty",
   "collection":"knowledge", "source_url":…}

GET    /v1/documents/status?path=tree/youtube/<slug>.md
→ {"path":…, "exists":true|false, "doc_hash":…|null}

DELETE /v1/documents?path=…        (admin scope)
GET    /healthz  GET /readyz
```

The pre-rename routes `/ingest`, `/exists` and `/delete` still work as hidden
deprecated aliases with the same auth and their old response shapes; see
[`api.md#migration`](api.md#migration).

`status: unchanged` means every stored point for that path already carries the
submitted body's `doc_hash`, so nothing was re-embedded.

`GET /v1/documents/status` lets a poller skip work it has already done without
paying for the upstream fetch first. The n8n YouTube workflow gates on it so
that a failed transcript fetch leaves the path absent and is retried on the next
poll — dedupe state held by the caller would instead mark the video seen and
drop it permanently.

### Agent MCP endpoint (`/mcp`)

The same process serves the `kb-mcp-write` MCP server over stateless streamable
HTTP at `/mcp`, with tools `kb_store_document` and `kb_document_status`, for
kagent agents (registered as the `kb-mcp-write` RemoteMCPServer). It is
narrower than `POST /v1/documents`: only `tree/docs/`, `source_type:
documentation`, a required `source_url`, and a 512 KiB cap. It returns a JSON
receipt. The old tool names `kb_ingest` / `kb_ingest_status` are still served
here (and only here) while `KB_MCP_WRITE_LEGACY_TOOLS=true`. Why writes live on
their own server and not on `kb-mcp-read`, and how delegating agents use the
receipt as their completion signal, is covered in [`mcp.md`](mcp.md) and
[`stories/import-memory.md` §15](stories/import-memory.md) (historical).

### Auth

Scopes are `read` ⊂ `write` ⊂ `admin`. Writes (`POST /v1/documents`, `/mcp`)
require `KB_API_WRITE_TOKEN`, sent as `Authorization: Bearer <t>` or
`X-KB-Write-Token: <t>` (legacy `X-KB-Ingest-Token` is still accepted). With no
token configured, writes are **refused**; `KB_API_ALLOW_ANONYMOUS_WRITES=true`
allows them, which `make api ANON=1` sets for local dev only. `source_type`
values `tree`, `chatgpt*` and `memory` are reserved and rejected. Details in
[`api.md`](api.md#auth).

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
`KB_API_WRITE_PATH_PREFIXES` (code default `tree/`; chart default
`tree/youtube/,tree/docs/`) bounds what the write plane may own; keep it narrow so
that is enforced rather than conventional.

## Deploy

Install into the cluster that hosts Qdrant and the callers:

```sh
make helm-deploy-api     # context application, release knowledge-tree-api
```

The Qdrant API key comes from an existing Secret (`API_QDRANT_SECRET`, default
`qdrant-apikey`), not `--set-string`. The write token comes from the Secret named
by `api.auth.writeTokenSecret` (default `kb-api-write-token`). The read plane
(`kb-mcp-read`) and the `knowledge-scout` agent stay on mlops with kagent;
`make helm-deploy` is unchanged apart from the new value names. Moving from the
old `kb-ingest` release is covered in [`api.md#migration`](api.md#migration).

How documents are read back out — and the embedding-space invariant that
OpenWebUI's reader imposes — is in [`read-plane.md`](read-plane.md).
