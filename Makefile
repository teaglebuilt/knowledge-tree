PY := uv run python

.DEFAULT_GOAL := help
.PHONY: help install ingest reindex index query sync qdrant-forward golden clean

help: ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

install: ## Sync Python deps (lancedb, duckdb, fastembed, qdrant-client, ...)
	uv sync

ingest: ## Incremental ingest: changed markdown -> chunk -> embed -> LanceDB
	$(PY) -m kb ingest

reindex: ## Rebuild the BM25 full-text index (run after a bulk ingest)
	$(PY) -m kb reindex

index: ingest reindex ## Full local build: ingest then rebuild FTS index

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
