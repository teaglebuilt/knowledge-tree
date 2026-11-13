# Knowledge Tree — API/MCP Unification & Naming Migration Plan

**Repository:** [`teaglebuilt/knowledge-tree`](https://github.com/teaglebuilt/knowledge-tree)  
**Source of truth:** `master` at [`d78973e369bf6c95fa0d84b64001709991b01e85`](https://github.com/teaglebuilt/knowledge-tree/tree/d78973e369bf6c95fa0d84b64001709991b01e85)  
**Prepared:** 2026-11-12  
**Status:** Proposed implementation plan only — no application or GitHub repository files changed  
**Primary outcome:** One `kb` product and image, one documented HTTP contract, generated and selectively exposed MCP tools, explicitly isolated read/write authorization, and consistent deployment naming.

> **Important baseline correction:** Current `master` is **not** the older `kb/ingest_api/` + `kb/mcp_retrieval/` layout. It already has `kb/api/`, `kb/mcp/read.py`, `kb/mcp/write.py`, and `kb/services/`. This plan is an incremental migration **from that current code**, not a replacement based on an outdated branch.

## 1. Decisions / intended end state

1. **Keep the product name `Knowledge Tree`, the import package `kb`, and the CLI `python -m kb`.** The project is broader than ingestion/retrieval; internal operations such as `make ingest` remain valid pipeline verbs.
2. **Use a single OCI image `ghcr.io/teaglebuilt/kb`** for the HTTP API, MCP read runtime, document operations, sync jobs, and future functionality; runtime mode is selected by command/configuration. Image tags should be immutable release versions and/or digests.
3. **Use FastAPI + Pydantic as the canonical HTTP schema and generate OpenAPI** at `/openapi.json`. Convert a **curated subset** of those operations to MCP, using `fastapi-mcp` initially; validate its current version/behavior before committing to it. FastMCP's OpenAPI provider is the fallback if separate cross-service conversion is easier.
4. **Preserve separate MCP read and write capabilities as a hard security boundary.** Do **not** expose a combined MCP server merely because the generated tooling makes this easy. The existing tests explicitly document that the kagent Claude harness may ignore per-tool allowlists. Only bind a writer RemoteMCPServer to authorized agents.
5. **Replace capability-narrow infrastructure and agent names** such as `kb-retrieval`, `kb-ingest`, and `kb_ingest` with durable names that describe the surface or document action. Keep backend/domain functions named `ingest` where they accurately mean indexing.
6. **Retain the two source/ownership paths:** local Git/Obsidian `tree/` → LanceDB/DuckDB → Qdrant via `kb sync`, versus API/agent Qdrant documents. Do not silently claim that API writes update Git or LanceDB. Preserve disjoint path prefixes and source-type protections.
7. **Migrate compatibly:** new names/routes first, aliases for existing n8n/agents temporarily, cut over Helm and clients, then remove aliases only after measured usage drops to zero.

### Proposed runtime architecture

```text
                               One repository / one image
                                  ghcr.io/teaglebuilt/kb
                                            |
                  +-------------------------+------------------------+
                  |                         |                        |
                  v                         v                        v
          kb-mcp-read (mlops)       kb-api (application)       kb sync Job / CLI
          isolated read tools       FastAPI + OpenAPI            local + Qdrant
          read-only Qdrant          read/write HTTP             unchanged core
                  |                         |
                  |                         +--> kb-mcp-write endpoint
                  |                              generated ALLOWLIST
                  |                              authenticated writer
                  v                         v
           kagent/Claude/agents       n8n / authorized agents
                  \                         /
                   +------ shared kb.services -------+
                                          |
                               chunk / embed / Qdrant
```

The read-only MCP endpoint can remain a separate process/cluster deployment while it is migrated to generated tooling; **same source code and image does not mean same permission boundary or exposed port**. A read-only read API should eventually share canonical models with the writer API, even if served by another runtime profile.

## 2. Verified `master` inventory and findings

| Current path / resource | Verified current state | Proposed treatment |
|---|---|---|
| `kb/api/app.py` | Starlette HTTP `/ingest`, `/exists`, `/delete`, `/healthz`, `/readyz` and mounted hand-written write MCP `/mcp` | Convert outer app to FastAPI; canonical Pydantic models; typed document/search routes; generated, allowlisted write MCP |
| `kb/api/__main__.py` | `python -m kb.api`, but CLI log label is `kb-ingest` and config vars are ingest-specific | Retain module path, use `kb-api` log/service identity |
| `kb/mcp/read.py` | Manual `MCPServer(name="kb-retrieval")` with `kb_search` and `kb_get_document` | Preserve behavior/format and read-only tool set; move to generated interface after parity tests; rename server `kb-mcp-read` |
| `kb/mcp/write.py` | Manual `MCPServer(name="kb-ingest")` with `kb_ingest`, `kb_ingest_status`; has URL provenance, path and source-type rules, size cap, receipt | Move policy into shared operation/service layer; generate `kb_store_document` and `kb_document_status`; keep receipts and pre/post validation |
| `kb/services/ingest.py`, `kb/services/search.py`, `kb/services/qdrant_store.py` | Already separates business logic and persistence from HTTP/MCP | Reuse, do not rewrite indexing logic unnecessarily |
| `kb/config.py` | `KB_INGEST_*`, `KB_MCP_INGEST_*`, private `CHATGPT_HISTORY_COLLECTION`, reserved source types | Rename only **service configuration**; preserve private collection separation and provenance policy |
| `Dockerfile` | One image already uses separate entrypoint commands (`kb.mcp` default, `kb.api` override); runtime deps include Starlette/Uvicorn | Retain one-image pattern, add FastAPI/generation dependencies, update comments/metadata; keep non-root execution and baked FastEmbed |
| `pyproject.toml` | Project distribution named `knowledge-kb`; `kb` package retained; app-specific dependencies not fully declared | Align distribution name to `knowledge-tree` if no published consumer requires old name; explicitly declare runtime dependencies and lock |
| `Makefile` | `IMAGE_REPO=ghcr.io/teaglebuilt/kb-retrieval`, targets `mcp-retrieval`, `ingest-api`, `helm-deploy-ingest` | `IMAGE_REPO=ghcr.io/teaglebuilt/kb`, targets `mcp`, `api`, `helm-deploy-api`; preserve local `ingest` pipeline target |
| `chart/Chart.yaml` | Chart `knowledge-tree` v`2.0.2`, appVersion `0.4.0`; description assumes read/ingest | Keep chart name, update description and versions as part of deliberate release |
| `chart/values.yaml` | `image.repository=ghcr.io/teaglebuilt/kb-retrieval`; `mcpServer.name=kb-retrieval`; `ingest.name=kb-ingest`; `docsAgent.kbIngest` | Move to consistent image, read MCP, API, write MCP values; stage Helm schema changes |
| `chart/templates/deployment.yaml`, `service.yaml` | Conditionally render write service from `.Values.ingest`; same image runs `kb.api` | Rename templates logically to API when appropriate and update Deployment/Service identity to `kb-api` |
| `chart/templates/mcp/kb-read.yaml` | Creates MCPServer and read RemoteMCPServer named `kb-retrieval` | Change both to `kb-mcp-read` and update URL/labels/annotations |
| `chart/templates/mcp/kb-write.yaml` | Creates write RemoteMCPServer `kb-ingest`, points to `kb-ingest.../mcp`, passes `X-KB-Ingest-Token` from Secret | Change to `kb-mcp-write`, pointing to `kb-api.../mcp` (or `/mcp/write`), with a staged token/header migration |
| `chart/templates/agents/kb-scout/agent-template.yaml` | Research agent intentionally binds only read MCP | Update reference to `kb-mcp-read`; maintain its no-write guarantee |
| `chart/templates/agents/documentation/agent-template.yaml` | Binds both old read/write servers; expects `kb_ingest` receipt and status | Update tool names, prompt, tool bindings and strict receipt schema together; preserve resumable cursor behavior |
| `chart/templates/agents/*/egress-policies.yaml`, `chart/values.yaml` | Origins contain both old Services | Update destination hosts before removing previous Services, including cross-cluster Cilium global-service routing |
| `chart/templates/sync-job.yaml` | Uses same image to run `python -m kb sync` | Change only image/ref labels; preserve prune and origin guarantees |
| `docs/read-plane.md`, `docs/write-plane.md`, `docs/architecture.md`, `README.md` | Documents old server names and the dual-writer architecture | Rewrite to API/MCP terminology, update paths/diagrams; keep semantic explanation of read/write ownership |
| `tests/test_chart_render.py`, `tests/test_plane_separation.py`, `tests/test_mcp_ingest.py` | Existing tests assert exact old server/tool names and auth boundary | Update to new contract; add OpenAPI/schema/tool parity, security and Helm migration tests |
| `.github/workflows/ci.yaml` | Present, but empty at pinned commit | Add real tests, lint, chart rendering and image build checks before cutover |
| `.claude/skills/**`, `docs/stories/import-memory.md`, `.ai/**` | Skills and historical design docs may reference old terminology | Audit **active instructions** for rename; preserve historical narrative unless clearly marked superseded |

**Specific existing safeguards that must survive:** `kb/api/app.py` refuses writes without a token unless explicit anonymous-development override is set; `kb/mcp/write.py` allows agent writes only to configured subpaths (currently `tree/docs/`), requires an HTTP(S) provenance URL, restricts source types (`documentation`) and size (~512 KiB), and returns idempotent `doc_hash` receipts; `kb/services/ingest.py` rejects reserved `tree`, `chatgpt`, `chatgpt_export`, `memory` origins. The chat history is kept in a separate Qdrant collection. Do not regress any of these.

**Known issues worth fixing during migration:** `make ingest-api` currently defaults to anonymous local writes; `/exists` is not protected in the same way as mutating endpoints; embedding model equivalence with OpenWebUI must remain invariant; frontmatter-only metadata edits do not necessarily change the body `doc_hash`; the Makefile `helm-deploy-ingest` sets `agent.enabled=false`, but chart values use `knowledgeScoutAgent.enabled` and `docsAgent.enabled` instead. Verify each fix against pinned tests and deployed constraints rather than assuming current installations are identical to the repository.

## 3. Canonical naming conventions

### Stable product, runtime, cluster and artifacts

| Entity | Old | New | Notes |
|---|---|---|---|
| Product name | Knowledge Tree | **Knowledge Tree** | Keep |
| Python import/CLI | `kb`, `python -m kb` | **same** | Keep stable code namespace |
| Python distribution | `knowledge-kb` | `knowledge-tree` | Requires lock/package metadata update; confirm downstream installs |
| Container image | `ghcr.io/teaglebuilt/kb-retrieval` | **`ghcr.io/teaglebuilt/kb`** | Mandatory |
| Read MCP server/RemoteMCPServer | `kb-retrieval` | `kb-mcp-read` | Explicit capability boundary |
| HTTP application Deployment/Service | `kb-ingest` | `kb-api` | All-purpose API, not only ingestion |
| Write RemoteMCPServer | `kb-ingest` | `kb-mcp-write` | Logical MCP facade hosted on `kb-api` |
| Main Helm chart/release on mlops | `knowledge-tree` | `knowledge-tree` | Keep unless full release migration requested |
| API Helm release on application | `knowledge-ingest` (Makefile) | `knowledge-tree-api` | May create a new release; stage coexistence |
| Read MCP executable | `python -m kb.mcp` | same | Use read-only runtime profile |
| API executable | `python -m kb.api` | same | Long-lived application module |
| Make read MCP | `make mcp-retrieval` | `make mcp` | Temporary deprecated alias |
| Make API | `make ingest-api` | `make api` | Require explicit dev anonymous mode |
| Deploy API | `make helm-deploy-ingest` | `make helm-deploy-api` | Change release and values; old target prints deprecation notice temporarily |
| Chart values: server | `mcpServer.*` | `mcp.read.*` | Breaking Helm config path, staged migration |
| Chart values: API | `ingest.*` | `api.*` | Keep `api.writePolicy.*`, not service name `ingest` |
| Chart values: docs agent | `docsAgent.kbIngest.*` | `docsAgent.kbWriter.*` | Endpoint name `kb-mcp-write` |
| App log/OTel service | `kb-ingest`, `kb-retrieval` | `kb-api`, `kb-mcp-read` | Same app/compose label `app.kubernetes.io/part-of: knowledge-tree` |

Use **`kb-<surface>`** for runtime resources (`kb-api`, `kb-mcp-read`, `kb-mcp-write`), **`kb_<action>_<resource>`** for tools (`kb_store_document`), **`KB_<AREA>_<SETTING>`** for environment variables. Keep legacy `ingest` in genuine pipeline/module functions, not in names that imply an entire service does only one operation. Do not rename existing Qdrant collection `knowledge`, vault `tree/`, or stored Qdrant paths/IDs as part of this refactor.

### Tools, HTTP routes and operation IDs

| Current agent tool / HTTP route | Proposed stable operation / endpoint | Visibility |
|---|---|---|
| `kb_search` (already present) | `kb_search` → `POST /v1/search` | Read MCP + authorized REST |
| `kb_get_document` (already present) | `kb_get_document` → `GET /v1/documents?path=...&offset=...&limit=...` | Read MCP + authorized REST |
| `kb_ingest` / `POST /ingest` | **`kb_store_document`** → `POST /v1/documents` | Write MCP + authorized REST |
| `kb_ingest_status` / `GET /exists` | **`kb_document_status`** → `GET /v1/documents/status?path=...` | Write MCP + authorized REST; optionally read REST |
| `POST /delete` | `kb_delete_document` → `DELETE /v1/documents?path=...` | Admin REST only; **not** in agent MCP by default |
| `/healthz`, `/readyz` | same | Probes only, excluded from MCP and OpenAPI agent catalogs |

`POST /v1/documents` is an upsert keyed by a validated `path`; preserve the current request `markdown`, `source_type`, `source_url`, `force` and receipt fields. Define explicit, stable FastAPI `operation_id` values. Keep HTTP semantics and idempotence behavior well documented. A future bulk import is a *separate* asynchronous job API (`POST /v1/jobs/import`) and tool, not overloaded into `kb_store_document`.

**Compatibility:** Temporarily keep `/ingest`, `/exists`, `/delete` as non-OpenAPI/non-MCP deprecated aliases with identical authorization and logging; maintain `kb_ingest` and `kb_ingest_status` compatibility **only on the authorized write MCP** during agent migration. Do not put legacy write aliases on the read MCP. Set a removal release after the n8n/agent consumers are verified updated.

### Service configuration migrations

| Existing key | New key / chart shape | Migration strategy |
|---|---|---|
| `KB_INGEST_TOKEN` | `KB_API_WRITE_TOKEN` | Support old during cutover; prefer one Secret, no tokens in Helm command args |
| `X-KB-Ingest-Token` | `X-KB-Write-Token` | Accept both briefly, remove old after callers migrate; bearer preferred where supported |
| `KB_INGEST_ALLOW_ANONYMOUS` | `KB_API_ALLOW_ANONYMOUS_WRITES` | Default `false`; forbidden in production chart; explicit opt-in in local dev |
| `KB_INGEST_PATH_PREFIXES` | `KB_API_WRITE_PATH_PREFIXES` | Retain exact disjoint prefixes by default |
| `KB_INGEST_MAX_BODY_BYTES` | `KB_API_MAX_BODY_BYTES` | Keep current 2 MiB default until tests approve change |
| `KB_MCP_INGEST_PATH_PREFIXES` | `KB_MCP_WRITE_PATH_PREFIXES` | Keep current `tree/docs/` restriction |
| `KB_MCP_INGEST_SOURCE_TYPES` | `KB_MCP_WRITE_SOURCE_TYPES` | Preserve closed `documentation` set |
| `KB_MCP_INGEST_MAX_BYTES` | `KB_MCP_WRITE_MAX_BYTES` | Keep 512 KiB agent cap |
| `INGEST_CONTEXT` | `API_CONTEXT` | Keep `application` initial value |
| `RETRIEVAL_CONTEXT` | `MCP_CONTEXT` | Keep `mlops` initial value |
| `IMAGE_REPO`, `IMAGE_TAG` | unchanged keys | Repository now `ghcr.io/teaglebuilt/kb` |

Keep all embedding/Qdrant settings (`EMBEDDING_MODEL`, `QDRANT_*`, `COLLECTION_NAME`), separate ChatGPT archive names, and local indexing config unchanged. Use a single compatibility resolver for old/new env values, emit warnings for old names, and **fail on conflicting values** rather than silently selecting one.

## 4. Implementation phases and acceptance criteria

### Phase 0 — Pin baseline, inventory consumers, create rollback path

- [ ] Create a feature branch **from the pinned `master` SHA** and confirm it has not diverged before implementation.
- [ ] Search the repo **at the pinned SHA** (not the possibly stale GitHub code-search index) for `kb-retrieval`, `kb-ingest`, `kb_ingest`, `KB_INGEST_`, `KB_MCP_INGEST_`, old GHCR, old Helm values, and names in prompts/skills/tests/docs.
- [ ] Inventory *external* consumers: homelab overlays (`platform/ai/kubernetes/overlays/{mlops,application}` per chart test), kagent RemoteMCPServer bindings, egress rules, n8n YouTube workflows, CronJobs, CI, docker pulls and private app deployment scripts. These are **not all in this repository**; verify them separately before deleting old Services.
- [ ] Capture current `helm template`, current MCP `tools/list`, REST requests/responses and Qdrant test data as golden fixtures. Verify actual kagent CRD versions in both clusters.
- [ ] Snapshot Qdrant before touching shared collection. Confirm rollback of image, chart and Secrets is possible.

**Exit:** all known callers and rollback objects documented; no unreviewed write boundary changes.

### Phase 1 — Define one shared API schema (no client cutover)

Files: `kb/api/app.py` (or new `kb/api/routers/*.py`), new `kb/api/schemas.py`, new `kb/api/security.py`, `kb/services/*.py`, `pyproject.toml`, `uv.lock`, `Dockerfile`, `tests/*`.

- [ ] Introduce FastAPI and typed request/response/error models; retain existing `kb.services` and Qdrant adapter logic. Ensure `uv sync` and Docker use a consistent, locked dependency set; do not leave FastAPI/Starlette/Uvicorn declared only in Docker.
- [ ] Define `/v1/search`, `/v1/documents`, `/v1/documents/status`, admin delete, `/openapi.json`, `/healthz`, `/readyz`; tag operations `mcp-read`, `mcp-write`, or `admin` as appropriate, with fixed operation IDs.
- [ ] Extract from `kb/mcp/write.py` the frontmatter, path, provenance, source-type and size validation into reusable **write-policy/domain service functions**. Both REST and generated MCP must traverse those checks; avoid relying solely on tool descriptions or route filters.
- [ ] Preserve `kb_search` formatting/citation metadata and `kb_get_document` pagination behavior, or introduce explicit compact response DTOs and verify context-token sizes.
- [ ] Define auth for read vs write vs admin; keep probes reachable without credentials. Add the required auth policy to `/exists`/status based on collection privacy; do not regress fail-closed writes.
- [ ] Define OpenAPI examples and error codes (400 validation, 401 missing token, 403 insufficient scope, 413 payload limit, 409 conflict where meaningful, 503 backend unavailable). Never expose secrets in spec or error bodies.
- [ ] Keep old HTTP routes during compatibility window but mark them `include_in_schema=False` so they are **never** generated into MCP.

**Exit:** OpenAPI snapshot stable; old and new REST contract tests pass against in-memory Qdrant; storage and embedding results match pinned baseline.

### Phase 2 — Generate MCP tools, *without* broadening permissions

Files: `kb/mcp/read.py`, `kb/mcp/write.py`, `kb/mcp/__main__.py`, `kb/api/app.py`, new `kb/mcp/factory.py` or equivalent, tests.

- [ ] Add `fastapi-mcp` and do a compatibility spike against the pinned FastAPI/MCP versions. Use **include_operations**, not automatic publication of all routes. If running the read MCP separately across clusters is simpler with `FastMCP.from_openapi`, assess its HTTP auth and response shape explicitly before choosing it.
- [ ] Generate exactly `kb_search`, `kb_get_document` for **`kb-mcp-read`**; generate exactly `kb_store_document`, `kb_document_status` for **`kb-mcp-write`**. Never generate delete/admin functions as agent tools by default.
- [ ] Run writer MCP behind `kb-api` with its own authenticated path, e.g. `/mcp`; run reader MCP as a physically separate profile/process/Service in mlops. Generation must use **the same canonical schema definitions**, not a second list of handwritten parameter models.
- [ ] Compare discovered MCP `tools/list` names, descriptions, JSON schemas, response structure and error semantics against the previous tools. Preserve `status`/`doc_hash` receipts and documented `unchanged` behavior.
- [ ] Where auto-conversion is semantically weaker (such as paginated citation-friendly output), use a thin curated adapter generated from a stable API operation or retain a minimal custom read tool **without duplicating business logic**. Tool quality/security outranks 100% generation.
- [ ] Retain read-server unit test asserting **zero write tools** regardless of kagent's per-tool filtering behavior. Independently test an unprivileged read-agent token cannot call writer API/MCP.
- [ ] Update `documentation-agent` prompt/tools to `kb_store_document`/`kb_document_status` and adjust any tool receipt references. `knowledge-scout` remains read-only.

**Exit:** exact tool inventories asserted, agent integration passes, a read-only agent cannot write even when deliberately calling the writer URL.

### Phase 3 — Normalize image/build, Helm and Kubernetes identities

Files: `Makefile`, `Dockerfile`, `chart/Chart.yaml`, `chart/values.yaml`, `chart/templates/{deployment,service,sync-job}.yaml`, `chart/templates/mcp/*.yaml`, `chart/templates/agents/**/*.yaml`, `tests/test_chart_render.py`.

- [ ] Change **both** image references to `ghcr.io/teaglebuilt/kb` (`IMAGE_REPO`, Helm `image.repository`); update image build/push help and chart release notes. Use the **same tag/digest** for read, API and sync across compatible deployment versions.
- [ ] Rename physical Service/Deployment to `kb-api`, read MCPServer + RemoteMCPServer to `kb-mcp-read`, writer RemoteMCPServer to `kb-mcp-write`; keep writer target URL pointing to `kb-api` and preserve the secret-backed header.
- [ ] Adopt chart values `api.*`, `mcp.read.*`, `docsAgent.kbWriter.*`. Add `values.schema.json` to catch removed/unknown overlay keys; consider a compatibility window for `ingest.*` and `mcpServer.*` with explicit warnings rather than silent divergence.
- [ ] Preserve the **two-cluster topology**: `application` hosts Qdrant and the `kb-api` writer; `mlops` hosts kagent and the read MCP. Check Cilium global Service name/annotations, actual DNS, egress policies, cross-cluster TLS and network boundaries.
- [ ] Update Helm releases: `knowledge-tree` on mlops; proposed `knowledge-tree-api` on application. Do not blindly rename an in-place release with `helm upgrade`: a new release may overlap resource ownership. Stage new release/service, cut over clients, then retire old release, or keep existing release temporarily while renaming only resources.
- [ ] Fix Makefile install switches to explicitly disable `knowledgeScoutAgent.enabled` and `docsAgent.enabled` on application. Add chart tests for **both real overlays**, plus cross-namespace Secret references and resource collisions.
- [ ] Keep chart agent objects optional on clusters without the kagent CRDs; do not apply MCPServer/RemoteMCPServer CRs where their CRDs are unavailable.
- [ ] Remove the pattern of passing the Qdrant credential through `helm --set-string`; configure Kubernetes Secret/ExternalSecret rather than values stored in Helm release metadata.
- [ ] Introduce consistent `app.kubernetes.io/name`/`part-of`/`component` and OTEL service names (`kb-api`, `kb-mcp-read`) while preserving selectors safely (selector changes can require resource replacement).

**Exit:** `helm lint` and `helm template` pass for mlops/application, both endpoints are reachable, writer remains authenticated, no unexpected Cilium or Secret regressions.

### Phase 4 — Migrate consumers, docs and observability

- [ ] Update the n8n YouTube workflow to `POST /v1/documents` and `GET /v1/documents/status`; keep its ownership `tree/youtube/`, replay/idempotency semantics and body size policy.
- [ ] Update kagent Agents/AgentTemplates, RemoteMCPServer refs, Firecrawl/Context7 docs-agent prompt, discovered tool names, strict JSON outputs, and EgressPolicy origins.
- [ ] Update homelab GitOps overlays **in the homelab repository** and sequence rollout so no agent or workflow is stranded on the old Service name.
- [ ] Update README and `docs/architecture.md`, add canonical `docs/api.md` and `docs/mcp.md`; optionally redirect `docs/read-plane.md` / `docs/write-plane.md` to new pages while retaining origin/invariant explanations.
- [ ] Audit active `.claude/skills/` and `.ai/` instructions; update present-tense instructions but label historical story artifacts as legacy rather than rewriting past decisions indiscriminately.
- [ ] Add Prometheus/OTel request and MCP call metrics: tool name, operation ID, principal/role, latency, token/response size where safe, storage errors, `status`, retries and Qdrant latency. Never log documents, raw tokens or private memory payloads by default.
- [ ] Capture legacy-route/tool usage to decide removal date; expose a migration matrix for caller, old URL/name, new URL/name, owner and validated date.

**Exit:** each caller uses new name/route, no legacy traffic over an agreed observation window, docs match runtime.

### Phase 5 — Remove compatibility and harden ongoing contract checks

- [ ] Remove old Service identities, MCP tools and HTTP aliases only after dependent agents/n8n have migrated; remove old env aliases after a separate release.
- [ ] Preserve Git/Obsidian vs direct-Qdrant authoring modes in docs. Decide separately whether API-authored documents should eventually commit to Git or create a durable source manifest; **not** a side-effect of this rename.
- [ ] Add schema drift CI: OpenAPI snapshot, exact allowlisted MCP tool schemas, test `tools/list` via Streamable HTTP, verify tools work through in-process and remote transports.
- [ ] Add security CI: missing/wrong/expired tokens, read-only credentials, forbidden source types, path traversal, invalid slug/URL, oversized docs, admin/delete exclusion, prompt-injection content treated only as data.
- [ ] Add ingestion integrity tests: idempotent repeat, edited revision replacement, metadata-only changes, source-owner collisions, failed embed/upsert interruption and retry behavior, Qdrant prune affects `source_type=tree` only.
- [ ] Re-run OpenWebUI embedding compatibility checks (`BAAI/bge-small-en-v1.5`, 384 dims, matching query embedding behavior), retrieval-quality golden tests and 32k-context agent tests with long document pagination.
- [ ] Publish change notes and new example commands. Cut a new app/image tag and an incremented chart version; verify rollback by reverting chart/image and testing an old workflow.

**Exit:** no active references to the old naming conventions (excluding explicitly archived history), passing CI and controlled deployments, zero unauthorized write capability.

## 5. Concrete CI/test matrix

| Test / contract | Command or approach | Must assert |
|---|---|---|
| Python unit and service tests | `make test` / `uv run --with pytest --with httpx pytest -q tests` | Unchanged chunk/embed/Qdrant behavior |
| OpenAPI | FastAPI `app.openapi()` snapshot | Versioned routes, fixed operation IDs, request and response schemas; no old aliases |
| Generated tool registry | MCP `tools/list` for read and write | Read: exactly 2 tools; write: exactly 2 tools; no delete or admin |
| MCP REST parity | HTTP and MCP call same document against in-memory Qdrant | Same stored `doc_hash`, source type, chunks and status |
| Permission boundary | Call protected write endpoint with read-only/missing credentials | Refused; no Qdrant mutation |
| Helm render | `helm lint chart`; `helm template ... -f overlay` | Names, image, split clusters, no duplicated or missing CRs |
| Network/release migration | Against actual mlops/application installations | `kb-api` visible via Cilium global Service and only authorized path |
| Auth/header rotation | Both current and future headers in migration test | Old accepted only during transition; new token required by default |
| Data ownership | Qdrant fake/local tests | `tree`/ChatGPT/memory origins never overwritten by regular agent writer |
| Client integration | n8n, documentation agent, knowledge-scout | New endpoints/tool names; read-only scout remains read-only |
| E2E smoke | Ingest one small documentation page, status, search, get | Verified receipt, pagination, citations; no unexpected large context return |

Add a CI workflow (`.github/workflows/ci.yaml` is empty at this baseline), covering Python tests, `ruff`/type-check as configured, Helm lint/render, OpenAPI schema drift, generated MCP tool-schema snapshot and Docker build. The image should be published **after** quality gates, not merely after Docker compiles.

## 6. Deployment sequence, risk controls and rollback

**Sequence:** (1) ship image under **new GHCR package** while old deployments still work → (2) deploy new `kb-api` Service and verified secured `/v1` API beside old endpoints → (3) deploy `kb-mcp-write` RemoteMCPServer and migrate documentation agent → (4) deploy `kb-mcp-read` and migrate scout/other read agents → (5) migrate n8n → (6) update default chart values and GitOps overlays → (7) observe no old traffic → (8) remove aliases and old Services.

**Do not** rename/delete `kb-ingest` or `kb-retrieval` first. Kubernetes Secret names, AgentTemplate references, cross-cluster egress and Cilium global-service DNS all make those live dependencies. Confirm actual cluster state before deciding between in-place rollout and parallel releases. Avoid accidental duplicate writes when old/new deployments both consume the same upstream job.

**Rollback:** keep previous image digest and chart revision; restore old RemoteMCPServer/Service and agent references if new tool discovery or auth fails; leave the Qdrant payload schema and collection unchanged for this release, so rollback requires no vector migration. Snapshot Qdrant as defense against unexpected document overwrite. Do not run `kb sync` as a blind cleanup/rollback step.

### Top risks / explicit mitigations

| Risk | Mitigation |
|---|---|
| Auto-generated MCP exposes `/delete` or admin controls | Explicit operation allowlists and exact tool-set assertions in tests; separate MCP server identities |
| kagent per-tool filters ignored | Authorization and physical server separation; write endpoint independently guarded |
| Agent/tool names change in prompts and persisted workflows | Keep aliases during cutover; migrate templates and n8n before retiring old names |
| FastAPI-MCP changes error/receipt formatting or loses text citations | Typed DTOs, contract snapshots and a small curated adapter where necessary |
| API schema and MCP generator use different policies | One service policy per operation; test REST/MCP parity and auth independently |
| New Helm release collides with old K8s ownership | Render with both overlays; staged coexistence; explicit resource owner migration |
| Cross-cluster Cilium global Service disappears under rename | Test global service DNS/routes/egress prior to consumer cutover |
| `kb sync` overwrites API-authored data or vice versa | Keep path-prefix and reserved source-type restrictions; regression tests |
| Client embedding drifts from OpenWebUI | Embed-model fingerprint/compatibility regression checks; do not change model as part of rename |
| Private ChatGPT/memory content leaks to knowledge collection | Preserve separate collection and restricted source-type policy; auth/redaction tests |
| GHCR new package lacks visibility/pull authorization | Publish new image first; verify `ghcr-secret` and pull on both clusters |

## 7. Suggested PR breakdown

| PR | Scope | Merge gate |
|---|---|---|
| **PR 1 — API contract** | FastAPI, Pydantic models, `/v1`, auth/policy extraction, OpenAPI snapshot; legacy aliases remain | Existing tests + new REST parity/auth tests |
| **PR 2 — MCP generation** | Allowlisted read/write generation, renamed tools, independent runtime profiles, snapshot tests | Exact discovered tools, agent receipts, no read-to-write escalation |
| **PR 3 — Packaging and naming** | `ghcr.io/teaglebuilt/kb`, Makefile, chart values/templates, new Secrets/header names | Image smoke, Helm render, credential isolation |
| **PR 4 — Consumer migration** | Agent templates, egress, docs, homelab overlay changes, n8n workflows | End-to-end verification in both clusters |
| **PR 5 — Cleanup** | Remove deprecated names/endpoints/env aliases, tighten CI/observability | Legacy usage zero, rollback documented |

For an especially low-risk first change, separate the **container image rename** into its own PR before code/API changes. It is mostly configuration but should still test GHCR pull permissions.

## 8. Completion criteria / definition of done

- [ ] `ghcr.io/teaglebuilt/kb:<version>` exists and is used by API, MCP read and sync modes.
- [ ] `python -m kb`, local indexing commands and Qdrant data remain compatible.
- [ ] API is FastAPI with versioned, typed routes and a stable `/openapi.json`.
- [ ] MCP read (`kb-mcp-read`) exposes only `kb_search` and `kb_get_document`.
- [ ] MCP write (`kb-mcp-write`) exposes only `kb_store_document` and `kb_document_status`, with independent authentication.
- [ ] No agent MCP surface exposes deletion by default.
- [ ] New Helm values and API/RemoteMCPServer/Deployment/Service names are consistent, and both cluster overlays render and deploy.
- [ ] `knowledge-scout` cannot write; documentation agent can store verified docs under its allowed prefix.
- [ ] n8n still collects and deduplicates YouTube documents; source/ownership paths remain disjoint.
- [ ] ChatGPT private archive remains isolated; OpenWebUI retrieval remains semantically compatible.
- [ ] No active `kb-retrieval`, `kb-ingest` or `kb_ingest` names remain in commands, runtime resources, active prompts, charts, docs, workflows or CI; historical prose can be retained as historical.
- [ ] Contract, security, build and Helm tests pass; rollback verified.

## 9. Sources and boundaries

**Pinned repository paths reviewed directly via GitHub connector:** [`kb/api/app.py`](https://github.com/teaglebuilt/knowledge-tree/blob/d78973e369bf6c95fa0d84b64001709991b01e85/kb/api/app.py), [`kb/mcp/read.py`](https://github.com/teaglebuilt/knowledge-tree/blob/d78973e369bf6c95fa0d84b64001709991b01e85/kb/mcp/read.py), [`kb/mcp/write.py`](https://github.com/teaglebuilt/knowledge-tree/blob/d78973e369bf6c95fa0d84b64001709991b01e85/kb/mcp/write.py), [`kb/services/ingest.py`](https://github.com/teaglebuilt/knowledge-tree/blob/d78973e369bf6c95fa0d84b64001709991b01e85/kb/services/ingest.py), [`kb/services/search.py`](https://github.com/teaglebuilt/knowledge-tree/blob/d78973e369bf6c95fa0d84b64001709991b01e85/kb/services/search.py), [`kb/config.py`](https://github.com/teaglebuilt/knowledge-tree/blob/d78973e369bf6c95fa0d84b64001709991b01e85/kb/config.py), [`Makefile`](https://github.com/teaglebuilt/knowledge-tree/blob/d78973e369bf6c95fa0d84b64001709991b01e85/Makefile), [`Dockerfile`](https://github.com/teaglebuilt/knowledge-tree/blob/d78973e369bf6c95fa0d84b64001709991b01e85/Dockerfile), [`chart/values.yaml`](https://github.com/teaglebuilt/knowledge-tree/blob/d78973e369bf6c95fa0d84b64001709991b01e85/chart/values.yaml), chart templates, [`docs/read-plane.md`](https://github.com/teaglebuilt/knowledge-tree/blob/d78973e369bf6c95fa0d84b64001709991b01e85/docs/read-plane.md), [`docs/write-plane.md`](https://github.com/teaglebuilt/knowledge-tree/blob/d78973e369bf6c95fa0d84b64001709991b01e85/docs/write-plane.md), and tests.

**External implementation references (not claims that the repo already uses them):** [`tadata-org/fastapi_mcp`](https://github.com/tadata-org/fastapi_mcp) and [FastMCP OpenAPI integration](https://gofastmcp.com/integrations/openapi). Exact implementation APIs and compatible dependency versions should be checked in the selected locked releases.

**Not reviewed as live runtime state:** actual Kubernetes cluster objects and Helm release history, n8n workflows, homelab overlays in the *other* repository, GHCR package permissions, external clients. Those are implementation prerequisites, not facts inferred from the source repository.
