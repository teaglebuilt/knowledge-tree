# Knowledge Tree: ChatGPT Conversation Import & Agent Memory Plan

**Project:** [`teaglebuilt/knowledge-tree`](https://github.com/teaglebuilt/knowledge-tree)  
**Status:** Implementation plan — proposed changes, not deployed  
**Prepared:** November 7, 2026  
**Primary goal:** Turn exported ChatGPT conversations into verifiable, useful, long-term context for KAgent and other assistants without building a competing knowledge platform.

---

## 1. Executive decision

Extend the existing **knowledge-tree** platform rather than introducing a separate memory stack.

- **Keep** the Git-backed Markdown/Obsidian knowledge tree, local LanceDB + DuckDB pipeline, Qdrant cluster index, `kb-ingest` write API, and `kb-retrieval` MCP server.
- **Add** an importer for ChatGPT conversation exports and a separate, protected archive index for unprocessed historical conversations.
- **Add** a memory extraction, verification, reconciliation, and promotion workflow that turns conversations into durable facts, decisions, procedures, preferences, and incident lessons.
- **Keep** KAgent's own session/agent memory, if configured, as a supplementary working-memory layer; use knowledge-tree MCP for shared cross-agent knowledge.
- **Defer** Mem0, Graphiti, a knowledge graph, and a new PostgreSQL service until evaluations demonstrate a concrete gap.

**Important:** Importing data does **not** train or fine-tune the underlying LLM. This improves responses through retrieval, context engineering, and feedback. Model training is a separate future option.

### Desired outcome

Given a request such as:

> "Create an automated recovery workflow for `mlops-work-00` when GPU connectivity breaks."

A KAgent worker should retrieve relevant **confirmed** architectural details and validated runbooks from `knowledge-tree`, use historical conversations as supporting context when needed, and explicitly distinguish old discussions from current cluster state.

---

## 2. Current repository baseline

The following components are present in the repository as inspected on the `master` branch on November 7, 2026. Paths and behavior are grounded in the repository; proposed additions are distinguished below.

| Existing path | Observed purpose | Plan |
| --- | --- | --- |
| `README.md` | Obsidian/Git knowledge tree entry point | Update usage instructions |
| `docs/architecture.md` | Local-to-cluster indexing architecture | Extend diagram and data flows |
| `tree/branches.yaml` | Knowledge routing/build and encryption policy | Add memory branches as appropriate |
| `kb/chunk.py` | Markdown frontmatter and heading-aware overlapping chunks | Reuse for promoted Markdown, add transcript-aware splitting as needed |
| `kb/config.py` | Embeddings, Qdrant, source/index configuration | Add archive collection and privacy configuration |
| `kb/ingest_api/app.py` | HTTP endpoints `/ingest`, `/exists`, `/delete` | Reuse for *approved* knowledge writes; harden auth |
| `kb/ingest_api/service.py` | Incremental embed/upsert into Qdrant; `path` ownership | Reuse carefully; add metadata and access constraints |
| `kb/mcp_retrieval/server.py` | MCP tools `kb_search`, `kb_get_document` | Extend retrieval with history/memory tools |
| `kb/mcp_retrieval/store.py` | Qdrant read-side search / full document retrieval | Add dedicated history store and filters |
| `kb/sync.py` | LanceDB → Qdrant synchronization; prunes `source_type=tree` | Preserve existing pruning isolation |
| `kb/adapters/qdrant.py` | Qdrant connection, collection, payload indexes, IDs | Extend for archive collection; honor separate auth policies |
| `chart/values.yaml` | Helm configuration for `kb-retrieval`, optional `kb-ingest`, agent | Add controlled config and optional importer Job |
| `chart/templates/agent.yaml` | KAgent `knowledge-scout-agent` template | Update agent's available tools/policy as compatible with deployed version |
| `Makefile` | `make ingest`, `reindex`, `sync`, `golden`, deploy targets | Add `import-chatgpt`, `extract-memories`, validation targets |

### Current behavior and constraints to preserve

1. Existing Qdrant collection defaults to **`knowledge`** and uses **`BAAI/bge-small-en-v1.5`**, **384 dimensions**. Do not change the vector model or dimension of the existing collection without an explicit reindex/migration.
2. The current write plane accepts JSON with `path`, `markdown`, `source_type`, `source_url`, `force` and stores chunked Markdown in Qdrant.
3. Existing `kb_search` supports `query`, `k`, `path`, `source_type`, and returns citeable chunks. `kb_get_document` pages through an indexed document.
4. Current `kb/sync.py` prunes *only* `source_type=tree` records. New imported sources must not be given that type unintentionally.
5. In `kb/ingest_api/app.py`, an unset `KB_INGEST_TOKEN` allows all callers that can reach the service to write. **Fix this before importing private history.**
6. Repository `master` is **public**. Do not commit raw personal conversations, secrets, sensitive memories, or private extracted notes to `tree/` without intentional classification and protection.
7. Helm chart values contain both `mcpServer` and `ingest` sections; validate their rendered manifests and the deployed KAgent CRD version before changing resource schemas.
8. Retrieval currently uses vector similarity against Qdrant, not a proven hybrid BM25+vector search in the deployed MCP path. Hybrid retrieval is a future improvement to measure.

Useful references: [Architecture](https://github.com/teaglebuilt/knowledge-tree/blob/master/docs/architecture.md), [Write-plane API](https://github.com/teaglebuilt/knowledge-tree/blob/master/kb/ingest_api/app.py), [Write service](https://github.com/teaglebuilt/knowledge-tree/blob/master/kb/ingest_api/service.py), [MCP server](https://github.com/teaglebuilt/knowledge-tree/blob/master/kb/mcp_retrieval/server.py), [Helm values](https://github.com/teaglebuilt/knowledge-tree/blob/master/chart/values.yaml).

---

## 3. Target architecture

```mermaid
flowchart TD
    A[ChatGPT official export ZIP] --> B[Private staging / parser]
    B --> C[Normalize messages & thread branches]
    C --> D[PII/secret scan + inclusion policy]
    D --> E[Encrypted raw archive in private S3/NAS]
    D --> F[Chat history indexer]
    F --> Q[(Qdrant: chatgpt_history)]
    D --> G[Memory extraction worker]
    G --> H[Deduplicate, contradict, rank, verify]
    H --> I{Approval / validation policy}
    I -->|Approved| J[Knowledge Tree private memory store]
    I -->|Needs review| R[Review queue]
    J --> K[Existing kb-ingest + knowledge index]
    K --> L[(Qdrant: knowledge)]
    Q --> M[Extended retrieval MCP]
    L --> M
    M --> N[KAgent / knowledge-scout]
    M --> O[Claude Code / Cursor]
    M --> P[OpenWebUI / n8n]
    N --> U[Feedback + evaluations]
    O --> U
    P --> U
    U --> H
```

### Storage separation

| Store | Data | Intended access | Retention |
| --- | --- | --- | --- |
| Private object storage, e.g. S3/NAS | Original ZIP, normalized JSONL, redaction audit, checkpoints | Ingestion/admin only | Explicit retention policy |
| Qdrant `chatgpt_history` | Searchable conversation/message chunks + provenance | Restricted historical retrieval, per-user access | Until deletion/retention rules apply |
| Existing Qdrant `knowledge` | Existing indexed docs; approved memories only | Knowledge MCP with policy filtering | Existing policy / revision management |
| Git-backed public `tree/` | General non-sensitive reference material | Existing Git workflow | Versioned in Git |
| Private memory records (design choice: encrypted private folder/object store) | Personal/project-specific accepted memories, revisions and approval state | User- and project-scoped | Explicit deletion + supersession policy |

**Design choice:** Do not treat a public Git repository as the source of truth for private memory. Store private memory Markdown or JSON outside the public checkout, with optional publishing of sanitized, expressly approved knowledge into `tree/`.

---

## 4. Data model and source provenance

### 4.1 Raw conversation record

Capture at least:

```json
{
  "source": "chatgpt_export",
  "export_id": "sha256:...",
  "conversation_id": "...",
  "conversation_title": "KAgent memory import",
  "created_at": "2026-11-06T00:00:00Z",
  "updated_at": "2026-11-07T00:00:00Z",
  "message_id": "...",
  "parent_message_id": "...",
  "role": "user",
  "message_created_at": "2026-11-06T00:00:00Z",
  "content_type": "text",
  "content": "...",
  "thread_id": "...",
  "project": "homelab",
  "privacy_class": "private",
  "redaction_version": "v1",
  "content_sha256": "..."
}
```

Treat this as a **logical schema**, not a promise that every ChatGPT export exposes every field. Missing values must be nullable. Store unmodified raw records separately for provenance and audit.

### 4.2 Derived durable memory record

```yaml
id: decision-kagent-claude-code-runtime-separation
kind: architectural_decision
owner_scope: personal
project: homelab
summary: >-
  Claude Code subagents are used for development-time engineering;
  KAgent is used for deployed runtime/operational agents.
status: proposed  # proposed | confirmed | rejected | superseded
confidence: 0.92  # extraction confidence, not proof
valid_from: null
valid_to: null
supersedes: null
source:
  system: chatgpt
  conversation_id: "..."
  message_ids: ["..."]
evidence:
  - type: conversation
    ref: "..."
verified_by: null
verified_at: null
privacy_class: private
tags: [kagent, claude-code, architecture]
```

### 4.3 Memory categories

- **Semantic:** persistent facts about projects or enduring preferences.
- **Episodic:** previous incidents, work sessions, and observed outcomes.
- **Decisions:** accepted, rejected, and superseded architecture decisions, with rationale.
- **Procedural:** validated runbooks, workflows, and reusable lessons.
- **Historical:** searchable original source conversations, not automatically trusted as facts.

Required behavior: distinguish **user-confirmed claims** from assistant suggestions, intentions from implementations, and old decisions from current state. Historical chats cannot establish the current condition of the cluster.

---

## 5. Proposed repository changes

```text
knowledge-tree/
├── kb/
│   ├── sources/
│   │   ├── __init__.py
│   │   └── chatgpt.py                 # NEW: export parser and normalizer
│   ├── memory/
│   │   ├── __init__.py
│   │   ├── models.py                  # NEW: memory schemas
│   │   ├── extract.py                 # NEW: conversation -> candidate memories
│   │   ├── reconcile.py               # NEW: dedupe/conflicts/supersession
│   │   ├── approve.py                 # NEW: promotion/review state
│   │   └── retrieval.py               # NEW: ranked memory/context assembly
│   ├── archive/
│   │   ├── __init__.py
│   │   └── chatgpt_store.py           # NEW: dedicated Qdrant archive operations
│   ├── mcp_retrieval/
│   │   ├── server.py                  # EXTEND: new read tools
│   │   ├── service.py                 # EXTEND: routed search
│   │   └── store.py                   # REUSE: knowledge collection
│   ├── ingest_api/
│   │   ├── app.py                     # HARDEN: auth, size limits, audit
│   │   └── service.py                 # EXTEND: metadata policy if needed
│   └── config.py                      # EXTEND: collection/privacy settings
├── scripts/
│   └── import_chatgpt.py              # NEW: CLI entry point
├── tests/
│   ├── fixtures/chatgpt/             # NEW: synthetic ZIP/JSON examples
│   ├── test_chatgpt_import.py         # NEW
│   ├── test_memory_extract.py         # NEW
│   ├── test_memory_reconcile.py       # NEW
│   ├── test_memory_retrieval.py       # NEW
│   └── test_memory_permissions.py     # NEW
├── eval/
│   └── chatgpt_memory.yaml            # NEW: recall and correctness dataset
├── docs/
│   ├── chatgpt-import.md              # NEW: user/admin runbook
│   └── memory-architecture.md         # NEW: design, trust rules, deletion
├── chart/
│   ├── values.yaml                    # EXTEND
│   └── templates/                    # OPTIONAL: import CronJob/Job + secrets
└── Makefile                           # EXTEND
```

**Note:** Directory names above are proposed. First inspect the current test/packaging layout before creating files, and match its conventions.

---

## 6. Implementation phases

### Phase 0 — Baseline, security and controls

**Goal:** Prove that private history can be handled safely without changing existing retrieval behavior.

- [ ] Create a feature branch and document the existing working `make ingest`, `make sync`, `make golden`, and Helm deployment behavior.
- [ ] Record existing Qdrant collection configuration and take a verified backup/snapshot.
- [ ] Confirm whether `kb-ingest` and `kb-retrieval` require auth in actual deployed manifests; require authenticated writes to ingest/delete endpoints.
- [ ] Apply network policies and least-privilege service identities, including authorization for both history and accepted-memory retrieval.
- [ ] Configure private object storage for exports and checkpoints; enable encryption and private bucket policy.
- [ ] Define a data inclusion/exclusion policy: personal, confidential, work-related, third-party data, secrets, credentials, and copyrighted source material.
- [ ] Specify deletion behavior for raw source, derived vector points, promoted memories, snapshots, and backups.
- [ ] Add test fixtures with fabricated conversations; never put real exports in source control or CI logs.

**Done when:** Security controls, backup, data policy, and an empty archive collection exist; existing services still pass baseline tests.

### Phase 1 — Official ChatGPT ZIP importer

**Goal:** Deterministically import history with reliable threading and provenance.

- [ ] Obtain export through ChatGPT **Settings → Data controls → Export data**.
- [ ] Support ZIP archives containing `conversations.json` and numbered `conversations-*.json` files when present; inspect actual file names rather than assuming one layout.
- [ ] Traverse the conversation mapping/tree using parent-child links and the conversation's current-node semantics when available; preserve alternate branches without inventing chronological relationships.
- [ ] Normalize supported text content and roles; record non-text or unsupported elements rather than silently dropping them.
- [ ] Preserve conversation IDs, message IDs, timestamps, titles, parent IDs, and source archive ID.
- [ ] Redact credentials and other prohibited content *before* generating embeddings or sending content to any external LLM.
- [ ] Tag private, project-specific and sensitive topics for scoped indexing; exclude unwanted categories.
- [ ] Generate stable IDs (source + conversation + message/branch + content version); support reimport without duplicates.
- [ ] Implement dry-run mode with counts, classification distribution, skipped elements, and estimates.
- [ ] Store source objects and parsed JSONL in encrypted private storage.
- [ ] Index only approved normalized content into Qdrant `chatgpt_history`, with appropriate indexed filter fields.
- [ ] Add incremental checkpoints and restart/retry logic. Do not rely solely on historical timestamps to identify edits.

**Suggested command contract:**

```bash
make import-chatgpt FILE="$HOME/Downloads/chatgpt-export.zip" DRY_RUN=1
make import-chatgpt FILE="$HOME/Downloads/chatgpt-export.zip"
```

**Done when:** A sample export imports without duplicate entries on repeated runs; branches and metadata are preserved; excluded content is not embedded; interrupted imports resume safely.

### Phase 2 — Extract durable memory

**Goal:** Convert conversations to concise candidate memories with evidence.

- [ ] Build an extractor that operates at conversation/topic level and can use your existing AI Gateway to select a model.
- [ ] Extract facts, architecture decisions, preferences, incidents, verified outcomes, procedures, and rejected options.
- [ ] Require source message references in every generated memory; reject unsupported assertions.
- [ ] Separate user statements from assistant-generated suggestions and unconfirmed technical advice.
- [ ] Classify each candidate as `proposed`, `confirmed`, `rejected`, or `superseded` as evidence permits.
- [ ] Detect contradicting facts and revisions; do not overwrite an old decision without recording the supersession.
- [ ] Merge duplicates while preserving all corroborating source references.
- [ ] Use an approval queue for private, high-impact, low-confidence, or otherwise ambiguous candidates.
- [ ] Save only confirmed/safe candidate memories to a protected, versioned private store; do not immediately commit them to public `tree/`.
- [ ] Promote sanitized, approved general-purpose knowledge through the existing Markdown ingestion route.

**Suggested commands:**

```bash
make extract-memories SOURCE=chatgpt DRY_RUN=1
make review-memories
make promote-memories
```

**Done when:** Candidate memories can be traced to exact source message IDs; a confirmed memory can be retrieved; a rejected item cannot silently reappear as confirmed upon reimport.

### Phase 3 — MCP retrieval and KAgent integration

**Goal:** Give agents context on demand without flooding prompts with history.

Preserve existing tools:

- `kb_search(query, k, path?, source_type?)`
- `kb_get_document(path, offset?, limit?)`

Add proposed tools:

| Tool | Behavior | Access |
| --- | --- | --- |
| `kb_recall(query, project?, kinds?, limit?)` | Return relevant approved memories and citations | Read-scoped |
| `kb_search_conversations(query, project?, date_range?, limit?)` | Search raw historical archive with provenance and warning that history is unverified | Restricted read |
| `kb_get_conversation(conversation_id, message_range?)` | Fetch a bounded conversation segment, not an unbounded transcript | Restricted read |
| `kb_propose_memory(memory)` | Stage memory for deduplication, checks and approval | Authorized write |
| `kb_review_memory(id, action)` | Approve, reject, supersede or delete according to permissions | Privileged control |

Implementation notes:

- [ ] Route retrieval to the correct collection using server-side, authenticated scopes; do **not** take a user-supplied arbitrary collection name.
- [ ] Filter by user/tenant, project, privacy class, validity, and approval state **before** returning data.
- [ ] Index needed payload fields in Qdrant; use strict ownership checks rather than trusting arbitrary metadata supplied by agents.
- [ ] Perform relevance ranking and token budgeting; prefer confirmed memory and current authoritative sources, then older conversation excerpts.
- [ ] Return timestamps, source IDs, confidence/status, and enough citation metadata for the agent to verify claims.
- [ ] Provide a policy to use `kb_recall` at the start of relevant tasks and raw-history lookup only when needed.
- [ ] Verify deployment against the *installed* KAgent CRDs; chart currently uses `api.kagent.dev/v1alpha3` for the agent and `kagent.dev/v1alpha1` for the MCP server configuration.
- [ ] Connect any design-time Claude Code or OpenWebUI integrations to the same MCP read plane rather than replicating state.

**Done when:** A KAgent task retrieves a relevant approved memory, can cite its source, cannot see unauthorized history, and correctly falls back when no memory applies.

### Phase 4 — Reconciliation, evaluation and feedback

**Goal:** Demonstrate better answers rather than just more retrieved text.

- [ ] Build a golden evaluation set from real but sanitized questions: historical recall, prior decisions, incident recovery, current-vs-old architecture, and rejected proposals.
- [ ] Compare **no memory**, **raw history only**, **distilled memory only**, and **distilled + on-demand history** variants.
- [ ] Evaluate retrieval Recall@k, MRR, citation correctness, contradictory-memory rate, answer accuracy, token use, latency and estimated cost.
- [ ] Track whether an agent used an irrelevant memory, missed a relevant one, or treated an unverified historical statement as current truth.
- [ ] Add explicit helpful/not-helpful feedback with a reason and optional correction.
- [ ] Store agent execution lessons as *proposed* memories; promote only after validation.
- [ ] Review aging facts periodically; for operational state, verify against live Kubernetes/GitHub tooling instead of trusting historical memory.

**Done when:** Evaluations show reproducible, positive improvement over the no-memory baseline with acceptable privacy risk and token/latency budgets.

### Phase 5 — Production hardening and lifecycle

- [ ] Add resource requests/limits and appropriate node scheduling for ingestion Jobs; keep bulk import separate from the interactive MCP service.
- [ ] Add Prometheus metrics: processed messages, skipped messages, extraction acceptance ratio, archive retrieval latency, failure/retry rates, duplicate suppression, and redaction events (counts only).
- [ ] Add tracing without logging raw conversation content or secrets.
- [ ] Add retention controls, authenticated deletion and verification that derived records are removed from live indexes and appropriate backups.
- [ ] Version embedding model and extractor prompts; provide schema/index migration tooling.
- [ ] Document disaster recovery: S3 archive → normalization/re-extraction → collection rebuild, with validation.
- [ ] Consider periodic imports only if a permitted, reliable export feed is available. Do not assume ChatGPT has a supported, continuously syncing personal-chat API.

**Done when:** Backups, restore, rollout, rollback, observability, authorization and deletion are tested.

---

## 7. Key API changes

### Proposed history import API (optional)

For an initial local CLI, a new public HTTP endpoint is **not** necessary. The importer can write through a narrowly scoped internal service/client after validation.

If remote imports are eventually needed, prefer asynchronous import jobs with authentication, upload size limits, malware scanning, content-type checks, audit logs, and idempotency keys—not sending an arbitrary ZIP body to the existing `/ingest` Markdown endpoint.

### Proposed context response shape

```json
{
  "query": "How should we handle GPU worker recovery?",
  "memories": [
    {
      "id": "incident-gpu-worker-001",
      "kind": "episodic",
      "status": "confirmed",
      "summary": "Verified recovery procedure ...",
      "source": {
        "conversation_id": "...",
        "message_ids": ["..."]
      },
      "observed_at": "...",
      "verified_at": "..."
    }
  ],
  "conversation_matches": [],
  "warnings": ["Historical information may no longer match live cluster state."]
}
```

---

## 8. Retrieval policy for agents

Recommended retrieval priority when answering an engineering request:

1. **Current state from authoritative tools:** cluster APIs, GitHub code, active manifests, or live telemetry when relevant and permitted.
2. **Approved, in-scope memory:** current project decisions, validated runbooks, and stable preferences.
3. **Existing knowledge tree:** general engineering knowledge and reference docs.
4. **Raw ChatGPT history:** only when searching for prior rationale, unresolved discussions, context not already distilled, or citation evidence.

Never automatically feed an entire conversation into a prompt. Retrieve bounded passages, resolve conflicts, and enforce a context token budget. In case of conflict, prefer current verified evidence and explain the discrepancy.

---

## 9. Security and privacy non-negotiables

- **Never import full personal history into public Git or an unrestricted agent namespace.** The GitHub repository is public.
- Run secret scanning, PII classification, and opt-in exclusion **before embedding and before third-party model calls**.
- Keep embeddings and payloads protected: vectors can still expose sensitive information through retrieval.
- Maintain user/project authorization across Qdrant collections, MCP tools, ingestion workers and promoted documents.
- Use a trust boundary around transcript content: historic chat text is **data**, not system instructions or executable code.
- Block prompt-injection attempts that ask the importer or retriever to ignore policy, reveal secrets, or execute commands.
- Require explicit approval for knowledge-tree publication and privileged memory changes.
- Make deletion comprehensive and testable, including derived chunks and backups under the chosen retention policy.
- Use safe logs and metrics; avoid writing raw prompts, secrets, or entire conversations to tracing backends.
- Preserve a redaction-version audit so changes can trigger reprocessing.

---

## 10. Test and acceptance matrix

| Test | Expected result |
| --- | --- |
| Export ZIP has one `conversations.json` | Successfully parse |
| Export has multiple numbered conversation files | Detect and import them |
| Thread contains edited/alternate branches | Preserve parent IDs and distinct branches |
| Message has missing timestamp or unsupported attachment | Preserve metadata/null or skip with audited reason |
| Same export imported twice | No duplicate indexed records |
| Export revised and imported again | Update changed items and remove or tombstone stale items as policy requires |
| API key or secret occurs in chat | Redacted/excluded before embedding |
| Unauthorized agent requests another user's history | Denied |
| Conversation contradicts an active cluster manifest | Active verified state wins; conflict is visible |
| Assistant suggested an approach but user never confirmed | Memory stays `proposed` |
| Previously accepted decision is reversed | Prior memory remains auditable as `superseded` |
| `make sync` runs after import | Historical records are not pruned |
| MCP search returns history | Source/branch/message provenance available |
| Delete conversation request | All relevant live archive and derived records removed |
| Cluster recovery from backup | Collections and approval states are reproducible |
| Golden evaluation comparison | Accuracy/relevance improvement measured objectively |

---

## 11. Delivery order / suggested pull requests

| PR | Scope | Dependencies |
| --- | --- | --- |
| **PR 1 — Private history foundations** | Auth hardening, archive collection config, privacy policy, synthetic fixtures | None |
| **PR 2 — ChatGPT importer** | ZIP parser, normalization, redaction, idempotent Qdrant import, CLI | PR 1 |
| **PR 3 — Extraction and reconciliation** | Candidate memory schemas, extractor, conflict handling, private storage, review | PR 2 |
| **PR 4 — Memory retrieval MCP** | Scoped archive search, verified recall, KAgent/Claude Code integration | PR 3 |
| **PR 5 — Eval and lifecycle** | Golden tests, telemetry, deletion, backup/restore, runbooks | PRs 1–4 |

**Minimum useful release:** PRs 1–2 plus a restricted historical search MCP tool.  
**Best agent-quality release:** PRs 1–4 plus the first measurable evaluation set.

---

## 12. Immediate action checklist

- [ ] Confirm availability of the official ChatGPT export ZIP locally.
- [ ] Snapshot Qdrant `knowledge` and record embedding model/version.
- [ ] Decide which history categories must be excluded from imports.
- [ ] Verify and enforce authenticated access to `kb-ingest` before private writes.
- [ ] Create a private `chatgpt_history` collection with separate access scope.
- [ ] Implement `scripts/import_chatgpt.py` + `kb/sources/chatgpt.py` with dry-run.
- [ ] Write synthetic fixtures covering branching, duplicate, missing, edited, and non-text messages.
- [ ] Run first small import, validate provenance, then execute a complete local import.
- [ ] Add memory candidates and the approval/reconciliation pipeline.
- [ ] Expose scoped retrieval through MCP and run the first controlled KAgent evaluation.

### First development task

> **Implement PR 1 and PR 2 inside `teaglebuilt/knowledge-tree` without altering existing `knowledge` collection semantics.** Include an idempotent, privacy-aware ChatGPT export importer, a separate `chatgpt_history` collection, dry-run reports, CLI wiring, and tests using synthetic conversation exports. Do not commit real personal history or enable unauthenticated writes.

---

## 13. Risks and decisions to revisit

| Decision | Recommendation now | Revisit when |
| --- | --- | --- |
| Mem0 | Do not add | Extraction/updates become complex enough to justify adopting it |
| Graphiti/graph DB | Do not add | Temporal and relationship queries consistently fail existing retrieval |
| PostgreSQL for memory | Do not add solely for this import | Structured metadata/transactions require stronger multi-user consistency |
| Separate Qdrant collections | Yes: `knowledge`, `chatgpt_history` | Only after authorization and query quality evaluation |
| Raw ZIP in Git | Never | Not applicable |
| Private memory in public `tree/` | No | Only sanitized, expressly approved publication |
| Automatic memory writes by runtime agents | Review first | Evals show reliable extraction and safe authorization |
| Continuous ChatGPT sync | Not assumed | Official supported export/sync capability becomes available |
| Fine-tuning on history | Not in initial scope | Retrieval-based approach plateaus and a justified, consented training dataset exists |

---

## 14. Definition of success

A successful implementation enables a KAgent or Claude Code agent to answer questions such as:

- "What did we previously decide about KAgent runtime agents versus Claude Code subagents?"
- "Find our earlier GPU passthrough troubleshooting discussion and the recovery steps that actually succeeded."
- "Which architectural approaches did we reject and why?"
- "What is the current runbook, and how is it different from our old discussion?"

It must do so with **relevant retrieval, exact provenance, safe access control, validated facts, and measured improvement**—not simply by storing more chat text.

---

*Repository snapshot reviewed: `teaglebuilt/knowledge-tree`, `master`, November 7, 2026. This document is a recommended design and rollout plan; it does not assert that these new features have already been implemented.*
