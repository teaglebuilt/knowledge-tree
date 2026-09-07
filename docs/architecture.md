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
                   └────────────────────┘                └────────────────────┘   restore      └────────────────────┘


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
