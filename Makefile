PY := uv run python

.DEFAULT_GOAL := help
.PHONY: help install extract ingest reindex index query sync qdrant-forward golden clean \
        secrets-status secrets-encrypt secrets-decrypt secrets-check secrets-config secrets-hooks

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

install: ## Sync Python deps (lancedb, duckdb, fastembed, qdrant-client, ...)
	uv sync

extract: ## Convert sources/ epub+pdf -> tree/ markdown (idempotent, hash-gated)
	$(PY) -m kb extract

ingest: ## Incremental ingest: changed markdown -> chunk -> embed -> LanceDB
	$(PY) -m kb ingest

reindex: ## Rebuild the BM25 full-text index (run after a bulk ingest)
	$(PY) -m kb reindex

index: extract ingest reindex ## Full local build: extract sources, ingest, rebuild FTS index

query: ## Query the local index: make query Q="ebpf network policy"
	@$(PY) -m kb query $(Q)

sync: ## Push local LanceDB vectors -> Qdrant on the k8s cluster
	$(PY) -m kb sync

qdrant-forward: ## Port-forward the cluster Qdrant to localhost:6333
	kubectl -n $(or $(QDRANT_NS),qdrant) port-forward svc/qdrant 6333:6333

golden: ## Measure retrieval quality (recall@k / MRR) against eval/golden.yaml
	$(PY) -m kb eval

clean: ## Remove local vector/db artifacts (LanceDB + DuckDB)
	rm -rf .lancedb kb.duckdb

secrets-status: ## Per-file: tree/branches.yaml policy vs on-disk state
	@$(PY) -m kb secrets status $(P)

secrets-encrypt: ## Encrypt every file branches.yaml marks encrypted (idempotent)
	@$(PY) -m kb secrets encrypt $(P)

secrets-decrypt: ## Decrypt in place so Obsidian + `make ingest` can read them
	@$(PY) -m kb secrets decrypt $(P)

secrets-check: ## Fail if any file violates the branches.yaml policy
	@$(PY) -m kb secrets check $(P)

secrets-config: ## Regenerate .sops.yaml from tree/branches.yaml
	@$(PY) -m kb secrets config

secrets-hooks: ## Install pre-commit + the git textconv driver for encrypted diffs
	@pre-commit install
	@git config diff.sops.textconv ./scripts/sops-textconv.sh
	@git config diff.sops.cachetextconv false
	@echo "registered diff.sops.textconv (see .gitattributes)"
