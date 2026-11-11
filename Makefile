PY := uv run python

# kb-retrieval MCP image (must match chart/values.yaml image.* unless overridden)
IMAGE_REPO ?= ghcr.io/teaglebuilt/kb-retrieval
IMAGE_TAG  ?= 0.4.0
IMAGE      ?= $(IMAGE_REPO):$(IMAGE_TAG)
GHCR_HOST  ?= ghcr.io
GHCR_SCOPES ?= write:packages,read:packages

# Write plane lands in the cluster that hosts Qdrant and its callers.
INGEST_CONTEXT ?= application
INGEST_SECRET  ?= qdrant-apikey
RETRIEVAL_CONTEXT ?= mlops
CHART_DIR ?= chart
GHCR_USER ?= teaglebuilt
OCI_REGISTRY ?= oci://ghcr.io/teaglebuilt/charts
DOCKER_BUILDKIT ?= 1
BUILDKIT_PROGRESS ?= plain

.DEFAULT_GOAL := help
.PHONY: help install extract ingest reindex index query sync mcp-retrieval golden clean \
        docker-build docker-login docker-push helm-deploy push-chart mcp-image translate-scan \
        ingest-api helm-deploy-ingest import-chatgpt test \
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
	$(PY) -m kb.mcp --transport stdio

ingest-api: ## Run the HTTP write plane (POST /ingest, /mcp kb_ingest -> Qdrant) on :3000
	KB_INGEST_ALLOW_ANONYMOUS=$${KB_INGEST_ALLOW_ANONYMOUS:-true} $(PY) -m kb.api

import-chatgpt: ## ChatGPT export -> chatgpt_history: make import-chatgpt FILE=~/Downloads/x.zip [DRY_RUN=1] [POLICY=p.yaml] [PRUNE=1]
	@test -n "$(FILE)" || (echo "FILE=<export.zip> is required"; exit 1)
	$(PY) -m kb import-chatgpt "$(FILE)" $(if $(DRY_RUN),--dry-run) \
		$(if $(POLICY),--policy "$(POLICY)") $(if $(PRUNE),--prune) $(if $(LIMIT),--limit $(LIMIT))

test: ## Unit tests (no Qdrant / no model downloads)
	uv run --with pytest --with httpx pytest -q tests

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

push-chart: ## Package chart/ and push it to $(OCI_REGISTRY)
	@command -v helm >/dev/null || { echo "helm not found on PATH"; exit 1; }
	@test -f $(CHART_DIR)/Chart.yaml || { echo "no Chart.yaml at $(CHART_DIR)"; exit 1; }
	@set -e; \
	meta="$$(helm show chart $(CHART_DIR))"; \
	name="$$(printf '%s\n' "$$meta" | awk '/^name:/{print $$2; exit}')"; \
	ver="$$(printf '%s\n' "$$meta" | awk '/^version:/{print $$2; exit}')"; \
	out="$$(mktemp -d)"; \
	trap 'rm -rf "$$out"' EXIT; \
	token="$${GITHUB_TOKEN:-$${GH_TOKEN:-$$(gh auth token 2>/dev/null || true)}}"; \
	if [ -z "$$token" ]; then \
		echo "gh auth token (or GITHUB_TOKEN) required to push to G+HCR"; \
		exit 1; \
	fi; \
	echo "$$token" | helm registry login $(GHCR_HOST) -u $(GHCR_USER) --password-stdin; \
	helm package $(CHART_DIR) -d "$$out"; \
	helm push "$$out/$${name}-$${ver}.tgz" '$(OCI_REGISTRY)'; \
	echo "published $(OCI_REGISTRY)/$${name}:$${ver}"

helm-deploy: ## Install/upgrade chart; key comes from the qdrant-apikey Secret in ai
	@command -v kubectx >/dev/null || { echo "kubectx required (brew install kubectx)"; exit 1; }
	@PREV=$$(kubectl config current-context 2>/dev/null); \
	kubectx $(RETRIEVAL_CONTEXT) || exit 1; \
	helm upgrade --install knowledge-tree chart -n ai; \
	rc=$$?; \
	[ -n "$$PREV" ] && kubectx "$$PREV" >/dev/null; \
	exit $$rc

helm-deploy-ingest: ## Install/upgrade the write plane (kb-ingest) on the cluster holding Qdrant
	@command -v kubectx >/dev/null || { echo "kubectx required (brew install kubectx)"; exit 1; }
	@set -a; . ./.envrc; set +a; \
	if [ -z "$$QDRANT_API_KEY" ]; then \
		echo "QDRANT_API_KEY is empty — export it in .envrc"; \
		exit 1; \
	fi; \
	PREV=$$(kubectl config current-context 2>/dev/null); \
	kubectx $(INGEST_CONTEXT) || exit 1; \
	helm upgrade --install knowledge-ingest chart -n ai \
		--set ingest.enabled=true \
		--set mcpServer.enabled=false \
		--set agent.enabled=false \
		--set qdrant.existingSecretEnabled=false \
		--set-string qdrant.apikey="$$QDRANT_API_KEY"; \
	rc=$$?; \
	[ -n "$$PREV" ] && kubectx "$$PREV" >/dev/null; \
	exit $$rc

translate-scan: ## Scan tree for non-English; dry-run (add WRITE=1 to overwrite)
	$(PY) scripts/translation_scan.py tree/ $(if $(WRITE),--write,)

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
