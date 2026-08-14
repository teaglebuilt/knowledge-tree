---
name: store_knowledge
description: Add or update knowledge in this repo and (re)build the search index. Use after writing or editing markdown notes, ingesting new material, or when the knowledge index is stale or empty. Handles chunking, local embedding into LanceDB, and syncing to the shared Qdrant cluster.
---

# Store Knowledge

Turn markdown into searchable knowledge: chunk → embed → index locally in
**LanceDB**, with **DuckDB** tracking content hashes so unchanged files are
skipped. Optionally mirror to **Qdrant** on the k8s cluster for shared access.

## Authoring conventions
New knowledge lives as markdown in the Obsidian vault under `tree/` (e.g.
`tree/networking/`, `tree/infrastructure/`). Give each file YAML frontmatter so
it indexes with good metadata:

```yaml
---
title: Human-readable title
description: One-line summary
tags: [kubernetes, ebpf]
created: '2026-08-09'
last_updated: 2026-08-09
---
```

Use real `#`/`##`/`###` headings — chunking is header-aware and builds
parent-child context from them.

## Build / update the index
```bash
make ingest    # incremental: only changed files are re-embedded (content-hash gate)
make reindex   # rebuild the BM25 full-text index (run after a bulk ingest)
make index     # ingest + reindex in one step
make sync      # push local vectors -> Qdrant on the k8s cluster (shared mirror)
```

- Ingest is **safe to re-run** — chunk IDs are `(path, doc_hash, chunk_index)`, so
  re-embeds upsert rather than duplicate, and deleted files are pruned.
- Use `uv run python -m kb ingest --force` to re-embed everything (e.g. after
  changing the embedding model or chunk sizes in `kb/config.py`).

## Syncing to Qdrant (k8s)
`make sync` reads local LanceDB and upserts into the `knowledge` collection.
Point it at the cluster first — either port-forward or an ingress URL:

```bash
make qdrant-forward                    # kubectl port-forward svc/qdrant 6333:6333
export QDRANT_URL=http://localhost:6333 # (or your ingress); QDRANT_API_KEY if set
make sync
```

Local LanceDB is authoritative; Qdrant is the replayed mirror.

## Related
- Search what you stored: [[query_knowledge]]
- Config (dirs, model, chunk sizes, Qdrant): `kb/config.py`
