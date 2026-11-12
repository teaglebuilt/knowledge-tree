# Read plane (`kb_search` + OpenWebUI External Knowledge)

> The HTTP contract is [`api.md`](api.md) and the MCP surfaces are [`mcp.md`](mcp.md); those are canonical. This page keeps the read-plane origin and invariants.

The Qdrant `knowledge` collection now has **two readers**. Both query the same
points, so neither can drift from the other — but they are not equally capable,
and one of them pins an invariant this repo must hold.

| Reader | Transport | Can filter | Used by |
|---|---|---|---|
| `kb_search` / `kb_get_document` | MCP (`kb-mcp-read`), or HTTP `POST /v1/search` / `GET /v1/documents` on `kb-api` | yes — `path`, `source_type` | kagent agents, Claude Code |
| OpenWebUI External Knowledge | native `qdrant-client` from OpenWebUI | **no** | OpenWebUI chat, `#`-attach |

## Why there are two

OpenWebUI (homelab `application` cluster) is the human front door. Its native
Knowledge feature only queries its own `open-webui_*` collections, keyed by
`tenant_id` and joined to its `file` table — so it cannot read this collection
that way, and mirroring `tree/` into an OpenWebUI knowledge base would mean a
second chunker, a second embedder and a second index of the same 639 documents.

Open WebUI has shipped **External Knowledge** since v0.10.0, which replaces the
vector query with a call to an external store. It is *not* an HTTP contract —
there is nothing here to implement. `EXTERNAL_KNOWLEDGE_PROVIDERS = {qdrant,
milvus, pgvector}`; the Qdrant path constructs a `QdrantClient` and calls
`query_points` against a collection you name. So OpenWebUI reads `knowledge`
directly, read-only, and this repo stays the sole owner of indexing.

See homelab `.ai/decisions/openwebui/0005-knowledge-tree-single-read-plane.md`.

## The invariant: OpenWebUI embeds its own queries

Only the ANN search is delegated. OpenWebUI computes the query vector itself:

```python
vector = await embedding_function(query, prefix=await Config.get('rag.embedding_query_prefix'))
```

So its embedding space must match this collection's, or results are meaningless
rather than merely worse. That is satisfied by configuring OpenWebUI with the
local engine and the same model:

```
RAG_EMBEDDING_ENGINE=""                       # in-process sentence-transformers
RAG_EMBEDDING_MODEL=BAAI/bge-small-en-v1.5    # 384-d, matches this collection
RAG_EMBEDDING_QUERY_PREFIX                    # MUST stay unset
```

`RAG_EMBEDDING_QUERY_PREFIX` must stay unset because FastEmbed's `query_embed`
for bge-small applies **no** prefix — it delegates straight to `embed`
(`TextEmbeddingBase.query_embed`). Only `colpali` carries a `QUERY_PREFIX`. If
either side starts prefixing and the other does not, the two readers silently
diverge.

Equivalence was verified empirically, not assumed. Embedding the same query with
sentence-transformers and querying `knowledge` returned the same five chunks in
the same order as `kb_search`, with scores agreeing to four decimals:

| Rank | sentence-transformers → Qdrant | `kb_search` (FastEmbed) |
|---|---|---|
| 1 | 0.8936 | 0.8937 |
| 2 | 0.8816 | 0.8816 |
| 3 | 0.8578 | 0.8578 |

The ~1e-4 delta is ONNX vs torch rounding. **Re-run this check after any change
to `EMBED_MODEL`, `EMBED_DIM`, or the FastEmbed version** — a dimension change
is caught at startup by `assert_collection_compatible`, but a model change at
the same dimension is not caught anywhere.

## What the OpenWebUI reader cannot do

Known limits, verified against the deployed 0.11.4 and v0.13.0 source. These are
upstream behaviours, not configuration mistakes:

- **No payload filtering.** `query_points` is called without `query_filter`, so
  one external knowledge base is the *whole* collection. A knowledge base scoped
  to `source_type=youtube` is not expressible. `kb_search` remains the only
  filtered reader — this is the main reason to keep the MCP tool exposed.
- **Weak citations.** `_retrieve_qdrant` builds its mapping with only
  `content_field` / `metadata_field` / `document_id_field` / `score_field`.
  `title`, `source`, `url` and `page` are read from the *point root*, where they
  do not exist, and `metadata['url']` is then overwritten with `None` — so
  clickable citation links are impossible. Without mitigation every citation
  shows just the knowledge-base name.
- **Bypasses hybrid search, reranking and the relevance threshold.** The external
  branch assigns `query_result` directly and skips `query_collection`, where BM25
  fusion and reranking live. Costs nothing today (this collection is dense-only)
  but a future reranker will not apply to this path.
- **Multi-query truncation.** With query expansion, per-query results are
  concatenated and truncated without re-sorting, so the first sub-query can
  consume the whole budget.

The default field mapping already fits this collection: `content_field` defaults
to `payload.text`, and `text` is a top-level payload field. `vector_field` is
left unset — Qdrant is the one provider where `using=None` selects an unnamed
vector, which is what both writers produce.

## Follow-ups this imposes on this repo

None of these are done yet.

1. **Write `source` (and `title`) onto tree points.** `kb sync` emits
   `chunk_id/path/heading/text/tags` only. With the consumer set to
   `metadata_field: payload`, a `source` key makes
   `metadata.get('source')` resolve and gives OpenWebUI a real citation label
   instead of the knowledge-base name. Cheapest available citation fix.
2. **Keep `KB_API_WRITE_PATH_PREFIXES` narrow (chart: `api.writePolicy.pathPrefixes`, `tree/youtube/,tree/docs/`).** `kb sync` never
   writes `doc_hash`, while `kb-api` dedups on it — so a path already owned by
   the tree sync looks new to the write plane, which re-embeds it and then
   `delete_path`s the tree's own points. The code default `tree/` does not
   prevent this (the chart overrides it); the two writers are only safe while their prefixes are disjoint.
3. **Named sparse BM25 vector + RRF.** The collection is dense-only
   (`sparse_vectors: null`). Both readers are therefore dense-only, and the
   OpenWebUI path cannot be rescued later by its own hybrid search.
4. **Put `parent_text` in the Qdrant payload.** It is computed and stored in
   LanceDB but neither Qdrant writer emits it, so parent expansion exists only on
   the laptop path. `kb_get_document` re-stitches children instead.
5. **Fix the golden set before tuning any of the above.** `eval/golden.yaml` has
   6 cases, 3 of whose paths no longer exist in `tree/` (so recall@k is capped at
   0.50), and `kb/eval.py` imports `search` from `kb.query` — the local LanceDB
   hybrid path. The production read plane that both readers use is unmeasured.

## Related

- [`api.md`](api.md), [`mcp.md`](mcp.md) — canonical HTTP and MCP contracts
- [`write-plane.md`](write-plane.md) — how documents get in
- [`architecture.md`](architecture.md) — pipeline overview
