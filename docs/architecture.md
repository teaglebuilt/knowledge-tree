# Architecture

```
                              ┌─────────────────────────────┐
                              │     Humans / AI Agents      │
                              │  Obsidian · Claude · Cursor │
                              └──────────────┬──────────────┘
                                             │
                    ┌────────────────────────┼────────────────────────┐
                    │                        │                        │
                    ▼                        ▼                        ▼
           ┌────────────────┐     ┌──────────────────┐     ┌─────────────────┐
           │  Obsidian Vault│     │   Makefile / CLI │     │  Skills / Tools │
           │   (tree/)      │     │   make extract   │     │  query_knowledge │
           │                │     │   make ingest    │     │  store_knowledge │
           └───────┬────────┘     │   make query     │     └────────┬────────┘
                   │              └────────┬─────────┘              │
                   │                       │                        │
                   └───────────────────────┼────────────────────────┘
                                           │
                                           ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                         Knowledge Bank Library (kb/)                         │
│                                                                              │
│   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐ │
│   │ extract  │──▶│  chunk   │──▶│  embed   │──▶│  store   │──▶│  query   │ │
│   │          │   │          │   │          │   │          │   │          │ │
│   │ books    │   │ parent/  │   │ fastembed│   │ LanceDB  │   │ hybrid   │ │
│   │ pdfs     │   │ child    │   │ bge-small│   │ DuckDB   │   │ BM25+vec │ │
│   │ remote   │   │ sections │   │          │   │ FTS      │   │          │ │
│   └──────────┘   └──────────┘   └──────────┘   └────┬─────┘   └──────────┘ │
│                                                     │                       │
│   ┌──────────┐                                      │          ┌──────────┐ │
│   │ secrets  │◀── sops policy from branches.yaml    │          │   sync   │ │
│   └──────────┘                                      │          └────┬─────┘ │
└─────────────────────────────────────────────────────┼───────────────┼───────┘
                                                      │               │
                              ┌───────────────────────┘               │
                              ▼                                       ▼
                   ┌────────────────────┐                ┌────────────────────┐                ┌────────────────────┐
                   │   Local Indexes    │                │  Cluster Qdrant    │                │  S3 Vector Backup  │
                   │                    │   make sync    │  (homelab k8s)     │   backup       │                    │
                   │  .lancedb/         │ ─────────────▶ │  collection:       │ ─────────────▶ │  snapshots /       │
                   │  kb.duckdb         │                │  knowledge         │ ◀───────────── │  object storage    │
                   └────────────────────┘                └─────────┬──────────┘   restore      └────────────────────┘
                                                                   │
                                          ┌────────────────────────┴───────────────┐
                                          │ kb_search / kb_get_document            │ kb_store_document
                                          ▼                                        │ POST /v1/documents
                                ┌────────────────────┐                             │
                                │   kb-mcp-read      │                    ┌────────┴───────────┐
                                │   (mlops)          │                    │      kb-api        │
                                │   QDRANT_NETWORK=  │                    │   (application)    │
                                │   internal|external│                    │ /v1 · /openapi.json│
                                └────────────────────┘                    │ /mcp = kb-mcp-write│
                                                                          └────────────────────┘


┌──────────────────────────────────────────────────────────────────────────────┐
│                        Knowledge Tree (tree/)                                │
│                                                                              │
│   branches.yaml ─── routing + build policy                                   │
│        │                                                                     │
│        ├── encryption: true/false (sops)                                     │
│        ├── books:  epub/pdf paths ──▶ extract ──▶ markdown                   │
│        ├── pdf:    research docs   ──▶ extract ──▶ markdown                  │
│        └── branches: nested topic tree                                       │
└──────────────────────────────────────────────────────────────────────────────┘


Build pipeline (make index):

  sources (NAS / books / pdf)
           │
           ▼  make extract
  tree/**/*.md  ◀── branches.yaml (what to pull, encrypt, nest)
           │
           ▼  make ingest
  chunks → embeddings → LanceDB + DuckDB (BM25)
           │
           ▼  make reindex
  full-text index ready
           │
           ├──▶ make query Q="..."     (local hybrid search)
           └──▶ make sync              (push vectors → Qdrant → S3 backup)
```

## Knowledge Bank Library

Agents in homelab correctly treat the bank (Qdrant via `kb-mcp-read` / `kb-mcp-write`) as the live knowledge plane. The vault is the human-curated, git-durable subset that feeds that plane. Markdown is the shared representation, not proof that every indexed doc lives in Obsidian. Differentiating them is not optional — it’s already how the write policies work; naming and eval should make that explicit so “updated Qdrant” never implies “updated repo.”

A Python library (`kb/`) that reads from the tree on a compilation loop to compile and reconcile as the tree is edited.

`branches.yaml` defines the tree structure and how to build it — from file encryption to pulling from remote sources such as books or PDF documents.

```yaml
# tree/branches.yaml (sketch)
networking:
  branches:
    censorship:
      encrypted: true
      books:
        some-title: "books/epub/..."
      pdf:
        paper: research/censorship/paper.pdf
    kubernetes:
      branches:
        networking:
          ebpf:
            books:
              learning_ebpf: "books/pdf/learning_ebpf.pdf"
```

## Knowledge Bank Indexing

| Stage | Command | Role |
|-------|---------|------|
| Extract | `make extract` | Convert sources declared in `branches.yaml` → `tree/` markdown |
| Ingest | `make ingest` | Chunk → embed → write LanceDB (incremental) |
| Reindex | `make reindex` | Rebuild BM25 full-text index in DuckDB |
| Query | `make query Q="..."` | Hybrid local search (vector + FTS) |
| Sync | `make sync` | Push local vectors → Qdrant on the cluster |
| Backup | Qdrant → S3 | Snapshot / export vectors to S3 for durable backup |

Local artifacts: `.lancedb/`, `kb.duckdb`. Remote: Qdrant collection `knowledge`. Durable: S3 vector backup (restore into Qdrant).

## Services: API and MCP

One image, `ghcr.io/teaglebuilt/kb`, serves three runtimes, selected by command:

| Runtime | Command | Cluster | Role |
|---|---|---|---|
| `kb-mcp-read` | `python -m kb.mcp` | mlops (next to kagent) | Read MCP: `kb_search`, `kb_get_document` |
| `kb-api` | `python -m kb.api` | application (next to Qdrant) | HTTP `/v1`, `/openapi.json`, and `kb-mcp-write` at `/mcp` |
| sync | `python -m kb sync` | either | LanceDB → Qdrant |

The HTTP contract is [`api.md`](api.md); the MCP surfaces are [`mcp.md`](mcp.md).
Both are generated from one operation registry (`kb/api/operations.py`) and one
set of Pydantic models (`kb/api/schemas.py`), so REST and MCP cannot drift in
parameters or policy.

```
 mlops cluster                                  application cluster
 ┌───────────────────────────┐                  ┌──────────────────────────────────┐
 │ kagent agents             │                  │ kb-api                           │
 │  knowledge-scout ──────────── kb_search ───▶ │   /v1/*        (REST, n8n)       │
 │  (read only)              │   (kb-mcp-read   │   /mcp         (kb-mcp-write)    │
 │                           │    on mlops)     │        │                         │
 │  documentation agent ─────────────────────────────────┘ kb_store_document      │
 │   (RemoteMCPServer        │   Cilium global  │        ▼                         │
 │    kb-mcp-write)          │   Service        │      Qdrant  collection: knowledge
 │                           │                  │        ▲                         │
 │ kb-mcp-read ──────────────────── reads ───────────────┘                         │
 └───────────────────────────┘                  └──────────────────────────────────┘
```

Writes and reads are separate by construction:

- `kb-mcp-read` only accepts operations tagged `mcp-read`; it has no writer and
  never opens one.
- `kb-mcp-write` is a different MCP server inside `kb-api`, behind a write-scope
  token gate. An agent can write only if its AgentTemplate binds the
  `kb-mcp-write` RemoteMCPServer. kagent's harness may ignore per-tool
  allowlists, so the boundary is the server, not a tool list.
- Delete is admin-scoped, REST-only, and never an MCP tool.
- The knowledge-scout agent's egress does not include `kb-api`.

Ownership is unchanged. `kb sync` owns `tree/` and prunes by `source_type=tree`;
`kb-api` writers own disjoint prefixes (n8n `tree/youtube/`, agents `tree/docs/`);
`tree`, `memory` and `chatgpt*` source types are reserved and cannot be claimed
through the API. The private ChatGPT collection is separate from `knowledge`.
See [`write-plane.md`](write-plane.md) and [`read-plane.md`](read-plane.md).
