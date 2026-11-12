# Goal

Ship the **knowledge-tree read plane** as an MCP server owned by this repo (`teaglebuilt/knowledge`), so cluster agents (starting with homelab `solutions-architect`) can call `kb_search` against the Qdrant `knowledge` collection with the same embedding space as `make ingest` / `make sync`.

Homelab already has the Agent CR wired for this tool. Do **not** implement the MCP server inside `teaglebuilt/homelab`.

---

# Why this lives here

| Concern | Owner |
|---------|--------|
| Chunking, `bge-small` embeddings, LanceDB authority, `make sync` → Qdrant | this repo (`kb/`) |
| Collection schema (`knowledge`, 384-d cosine, payload `text`/`path`/`heading`/`tags`/`chunk_id`) | this repo |
| `kb_search` MCP (query embed + ANN + cite paths) | **this story** |
| kagent `Agent` `solutions-architect` + `RemoteMCPServer` pointer | `teaglebuilt/homelab` (done / thin follow-up) |

Stock `mcp-server-qdrant` is **not** usable against `knowledge`:

- It expects payload key `document` + nested `metadata`; our points use `text`, `path`, `heading`, `tags`, `chunk_id`.
- It searches **named** FastEmbed vectors; our collection uses the **unnamed** default vector.

---

# Contract (load-bearing)

| Item | Value |
|------|--------|
| Tool name | `kb_search` (required — Agent filters on this) |
| Args | `query: string`, `k: int` (default 8, max ~20) |
| Collection | `knowledge` |
| Embedding | `BAAI/bge-small-en-v1.5` via FastEmbed **query** embed (not passage) |
| Distance | cosine, vector size **384**, unnamed / default vector |
| Return | Ranked chunks including `score`, `path`, `heading`, `tags`, `text` (enough for citations) |
| Writes | **None** — read-only. No `qdrant-store`. |
| Consumer | kagent Agent `solutions-architect` in namespace `ai` on **mlops** |

Reference prototype (remove from homelab after this lands; copy into this repo as the starting point):

- Was drafted at `homelab/platform/ai/kubernetes/mcp/kb-retrieval-server.py`
- Logic: FastMCP stdio → `TextEmbedding.query_embed` → `QdrantClient.query_points` → format `<chunk path=…>`.

---

# Network / deploy facts (verified 2026-10-04)

- Qdrant runs on **application**, namespace `data`, Service `qdrant:6333`.
- Collection `knowledge` is populated (~12k points).
- From **mlops** pods: `https://qdrant.homelab.internal/readyz` works with TLS verify **disabled** (homelab CA). Direct `:6333` to the gateway VIP times out.
- Preferred long-term: run `kb-retrieval` on **application** next to Qdrant (`http://qdrant.data.svc:6333`), expose MCP over HTTP, and let mlops kagent reach it via internal DNS/HTTPRoute (same pattern as `firecrawl-mcp`).
- Acceptable short-term: run on **mlops** `ai` and call Qdrant at `https://qdrant.homelab.internal` with `verify=false`.

kagent consumer wiring in homelab expects a discoverable MCP named **`kb-retrieval`** exposing **`kb_search`**. Prefer:

```yaml
# In homelab (thin RemoteMCPServer) OR emitted by this chart into ns ai
apiVersion: kagent.dev/v1alpha2
kind: RemoteMCPServer
metadata:
  name: kb-retrieval
  namespace: ai
spec:
  description: Knowledge-tree read plane (kb_search → Qdrant knowledge)
  protocol: STREAMABLE_HTTP
  url: http://<kb-retrieval-service>.<ns>.svc.cluster.local:3000/mcp
  timeout: 120s
```

If you deploy via KMCP `MCPServer` (stdio) **into `ai` on mlops**, the Agent can keep `kind: MCPServer` / `name: kb-retrieval` instead — match whatever you ship and update the Agent tool ref once.

---

# Work breakdown

## 1. Package the MCP server in this repo

- [ ] Add a small module under e.g. `kb/mcp_retrieval/` (or `kb/retrieval_mcp/`) with FastMCP tool `kb_search`.
- [ ] Depend on `mcp`, `qdrant-client`, `fastembed` (align versions with existing `pyproject.toml` / uv lock).
- [ ] Env config: `QDRANT_URL`, `QDRANT_API_KEY`, `QDRANT_VERIFY`, `COLLECTION_NAME=knowledge`, `EMBEDDING_MODEL=BAAI/bge-small-en-v1.5`, `KB_SEARCH_DEFAULT_K`, `KB_SEARCH_MAX_K`.
- [ ] Entry point: `python -m kb.mcp_retrieval` (stdio) and/or HTTP/SSE transport for in-cluster Service.
- [ ] Unit/smoke: embed + search against live Qdrant (or recorded fixtures) asserting payload fields render.

## 2. Container image

- [ ] Dockerfile (non-root, read-only root FS friendly, cache dir for FastEmbed model).
- [ ] Pin base + deps; pre-pull or bake `bge-small` weights so first pod start is not a multi-minute download if practical.
- [ ] Publish to the registry you already use for homelab images (document tag).

## 3. Helm chart (`chart/`)

Extend the existing `chart/` (today only has a draft `templates/agent.yaml` for knowledge-scout):

- [ ] Deployment + Service for `kb-retrieval`.
- [ ] Values: image, Qdrant URL/key (from Secret), resources, replicas.
- [ ] Optional: HTTPRoute `kb.homelab.internal` **only if** needed cross-cluster; otherwise ClusterIP + RemoteMCPServer URL.
- [ ] Optional: RemoteMCPServer / MCPServer manifest templated for namespace `ai` (mlops), or document the one-file apply in homelab.
- [ ] Do **not** block on finishing `knowledge-scout` agent in the same PR unless you want them together.

## 4. Secrets

- [ ] Qdrant API key via SOPS (same key the cluster Qdrant chart uses) — no plaintext in git.
- [ ] Document how sync + retrieval share that secret.

## 5. Homelab handoff (minimal)

After MCP is reachable from mlops `ai`:

- [ ] Ensure `RemoteMCPServer` or `MCPServer` named `kb-retrieval` exists in `ai`.
- [ ] Confirm Agent `solutions-architect` status `Accepted` + `Ready` and that `kb_search` appears in discovered tools.
- [ ] Smoke invoke: ask the agent a homelab-specific question and verify it cites `tree/...` paths from search hits.
- [ ] Delete any leftover WIP `MCPServer`/`ConfigMap` named `kb-retrieval` that was applied experimentally from homelab during prototyping.

## 6. Docs

- [ ] Update `docs/architecture.md` read-plane diagram: Agents → `kb_search` MCP → Qdrant `knowledge`.
- [ ] Cross-link from homelab `docs/platform/ai/rag.md` (replace “kb-retrieval not implemented”).

---

# Acceptance

1. `kb_search("kgateway HTTPRoute internal TLS")` returns chunks with real `path` values under `tree/…` and non-empty `text`.
2. Wrong embedding model or named-vector misuse is impossible by construction (tests or startup check on collection vector size 384).
3. Homelab `solutions-architect` can call `kb_search` without code changes beyond the RemoteMCPServer URL (or MCPServer deploy into `ai`).
4. No write tools exposed on this server.

---

# Out of scope

- Rerank / parent-expand / score abstain (called out as TODO in homelab RAG docs — later).
- OpenWebUI native RAG against `knowledge` (wrong embedding space — do not do this).
- Replacing LanceDB as source of truth; Qdrant remains the cluster mirror via `make sync`.

---

# Suggested first PR slice

1. Python package + local `uv run` stdio smoke against Qdrant.
2. Image + chart Deployment on **application** `data` (or `ai`) talking to `http://qdrant.data.svc:6333`.
3. RemoteMCPServer in mlops `ai` + agent smoke.
