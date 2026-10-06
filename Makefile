PY := uv run python

# kb-retrieval MCP image (must match chart/values.yaml image.* unless overridden)
IMAGE_REPO ?= ghcr.io/teaglebuilt/kb-retrieval
IMAGE_TAG  ?= 0.1.0
IMAGE      ?= $(IMAGE_REPO):$(IMAGE_TAG)
GHCR_HOST  ?= ghcr.io
GHCR_SCOPES ?= write:packages,read:packages
DOCKER_BUILDKIT ?= 1
BUILDKIT_PROGRESS ?= plain

.DEFAULT_GOAL := help
.PHONY: help install extract ingest reindex index query sync mcp-retrieval golden clean \
        docker-build docker-login docker-push helm-deploy mcp-image \
        secrets-status secrets-encrypt secrets-decrypt secrets-check secrets-config secrets-hooks

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

install:
	uv sync

extract:
	$(PY) -m kb extract

ingest: ## changed markdown -> chunk -> embed -> LanceDB
	$(PY) -m kb ingest

reindex: ## Rebuild the BM25 full-text index (run after a bulk ingest)
	$(PY) -m kb reindex

index: extract ingest reindex ## Full local build: extract sources, ingest, rebuild FTS index

query: ## Query the local index: make query Q="ebpf network policy"
	@$(PY) -m kb query $(Q)

sync: ## Push local LanceDB vectors -> Qdrant on the k8s cluster
	$(PY) -m kb sync

mcp-retrieval: ## Run kb_search MCP (stdio). QDRANT_NETWORK=internal|external
	$(PY) -m kb.mcp_retrieval --transport stdio

docker-build: ## Build kb-retrieval MCP image (bakes bge-small FastEmbed weights)
	DOCKER_BUILDKIT=$(DOCKER_BUILDKIT) BUILDKIT_PROGRESS=$(BUILDKIT_PROGRESS) \
		docker build -t $(IMAGE) -f Dockerfile .

docker-login: ## Login to GHCR using gh auth token (write:packages)
	@command -v gh >/dev/null || { echo "gh CLI required (https://cli.github.com)"; exit 1; }
	@gh auth status -h github.com >/dev/null 2>&1 || { echo "run: gh auth login"; exit 1; }
	@gh auth status -h github.com 2>&1 | grep -q 'write:packages' || \
		gh auth refresh -h github.com -s $(GHCR_SCOPES)
	@TOKEN=$$(gh auth token); \
	echo "$$TOKEN" | docker login $(GHCR_HOST) -u "$$(gh api user --jq .login)" --password-stdin

docker-push: docker-build docker-login ## Push kb-retrieval image to IMAGE_REPO
	docker push $(IMAGE)

helm-deploy: ## Install/upgrade chart; qdrant.apikey from QDRANT_API_KEY (.envrc)
	@test -n "$${QDRANT_API_KEY}" || { \
		echo "QDRANT_API_KEY not set — run: direnv allow  (or export from .envrc)"; \
		exit 1; \
	}
	helm upgrade --install knowledge-tree chart -n ai \
		--set-string qdrant.apikey="$${QDRANT_API_KEY}"

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
