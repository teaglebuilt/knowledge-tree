# Vault vs Bank Ownership & RAG Evaluation

**Repository:** `teaglebuilt/knowledge` (Knowledge Tree)  
**Related:** [`refactor.md`](refactor.md) (API/MCP naming), [`../read-plane.md`](../read-plane.md), [`../write-plane.md`](../write-plane.md), [`../architecture.md`](../architecture.md)  
**Homelab consumers:** kagent agents via `kb-retrieval` / `kb-ingest` RemoteMCPServers; OpenWebUI External Knowledge; n8n YouTube ingest  
**Prepared:** 2026-11-12  
**Status:** Proposed story — documents the ownership invariant and an evaluation plan; does not change runtime code by itself

## Goal

Make **Obsidian vault (`tree/`)** and **knowledge bank (indexes + Qdrant)** first-class, explicitly different layers so that:

1. “Updated Qdrant” never implies “updated git / Obsidian.”
2. Agents in homelab treat the **bank** as the live retrieval plane, with provenance that tells them whether a hit is vault-backed or bank-only.
3. Retrieval quality is measured with a real golden set **before** further chunk/embed/rerank tuning — separately from homelab agent trajectory evals.

---

## Decision

**Differentiate the vault from the bank.** They already behave differently in write policy and sync prune; naming, docs, agent prompts, and evals must say so out loud.

| Layer | What it is | Durable where | Updated by |
|---|---|---|---|
| **Vault** | Curated markdown under `tree/` (Obsidian) | Git | Humans, extract pipeline, PRs |
| **Bank** | Chunks + embeddings + search surfaces | LanceDB/DuckDB locally; Qdrant collection `knowledge` in homelab | `make ingest` / `make sync`, **and** API/MCP writers |
| **Agent surface** | MCP read/write + OpenWebUI External Knowledge | Runtime | kagent, n8n, chat |

Markdown is the **shared representation**, not proof that every indexed document lives in Obsidian.

- For `source_type=tree`: git markdown **is** the source of truth → ingest → sync → Qdrant.
- For API/agent writes (`youtube`, `documentation`, …): markdown is the **payload** that lands in Qdrant under a logical `path` (often `tree/...`) **without** updating LanceDB or git unless a separate promotion step runs.

Paths like `tree/docs/` and `tree/youtube/` are document IDs that *look* vault-like. They must not be assumed to exist as files in the repo.

---

## Current architecture (verified behavior)

```text
Humans (Obsidian) ──edit──▶ tree/*.md ──ingest──▶ LanceDB ──sync──▶ Qdrant[source_type=tree]
                                                                        ▲
n8n / docs agent ──markdown──▶ kb-api / kb-mcp-write ───────────────────┘
                                                                        │
kagent / OpenWebUI ◀── kb_search / External Knowledge ──────────────────┘
```

| Path | Owner | Lands in git? | `source_type` | Touched by `kb sync` prune? |
|---|---|---|---|---|
| Local vault sync | `make ingest` + `make sync` | Yes (already in `tree/`) | `tree` | Yes — stale tree points only |
| n8n YouTube | HTTP write plane | No (unless separately committed) | `youtube` | No |
| Documentation agent | Write MCP (`tree/docs/`, provenance URL required) | No | `documentation` | No |
| ChatGPT / memory | Restricted / separate collection | No | reserved / private | No |

Hard invariants that must survive any rename or eval work (see also `refactor.md`):

- Reserved origins (`tree`, `chatgpt*`, `memory`) are not overwritable by normal writers.
- Sync prune is scoped to `source_type=tree` only.
- Read MCP exposes search + get only; write MCP stays a separate authenticated surface.
- Embedding space stays `BAAI/bge-small-en-v1.5` / 384-d for MCP **and** OpenWebUI.

### Homelab usage pattern

Cluster agents do **not** browse a checkout of this repo. Architect / software-factory / scout bind read MCP (`kb_search`, `kb_get_document`). The documentation agent may write under policy. OpenWebUI reads the same Qdrant collection directly (no payload filters). For those callers, **Qdrant is the working corpus**.

---

## Problem this story fixes

Without an explicit vault≠bank model:

1. Operators expect API/MCP writes to appear in Obsidian or git — they do not.
2. Local skills that only read `tree/` miss bank-only documents agents already use.
3. Eval work conflates **retrieval quality** (did we fetch the right chunks?) with **agent trajectory** (did the agent call `kb_search` with expected args?).
4. A single aggregate Recall@K cannot diagnose regressions across `tree` / `youtube` / `documentation`.

---

## Evaluation maturity (as of this story)

| Plane | What exists today | Gap |
|---|---|---|
| **Retrieval (this repo)** | `eval/golden.yaml` (~6 hand-labeled questions) + `kb/eval.py` Recall@K / MRR via `make golden` | Far below v1 target (50–200); no Precision@K, Context Precision, or `source_type` slices |
| **Agent behavior (homelab)** | `agentevals` + Taskfile cases (e.g. `qdrant-architecture`) scoring tool trajectories | Measures wiring/discipline, not whether retrieved chunks support the answer |
| **Answer quality** | Informal human spot checks | No faithfulness / citation-quality golden set yet |

**Rule:** do not start with uncalibrated LLM-as-judge for retrieval. Grow the hand-labeled golden set first. Keep homelab trajectory evals; do not treat a green trajectory as proof of retrieval health.

### Target retrieval metrics (v1)

| Metric | Use |
|---|---|
| Recall@K / Hit@K | Baseline: relevant doc in top-K? |
| MRR | First relevant rank (Q&A style) |
| Precision@K | Noise in top-K |
| Context Precision (when a reranker exists) | Are relevants ranked near the top? |

Slice golden results by **document origin** (`source_type`), **query style** (keyword vs conceptual), and **corpus segment** (e.g. kubernetes vs networking) before changing global chunk/embed settings.

### Diagnostic triage (bank-specific)

| Bad signal | Likely layer | First look |
|---|---|---|
| Low Recall@K on `tree` | Chunking / sync / filter | Ingest coverage, prune, `source_type=tree` filter |
| Agent invents paths | Answer / prompt | Architect skill; False Answer — not chunk size |
| OpenWebUI worse than MCP | Reader contract | Unfiltered whole-collection search; embedding prefix drift |
| Doc in chat, missing in Obsidian | Ownership | Bank-only write; no vault promotion |
| YouTube/docs vanished after sync | Bug | Prune must remain `tree`-only |
| Receipt OK, search empty | Write/index | Collection, dim, path filter, embed model drift |

---

## Intended end state

1. **Docs and architecture** state vault vs bank as two layers with shared markdown representation and disjoint write paths.
2. **Agent prompts / skills** (homelab + any in-repo skills) cite `path` + `source_type` + `source_url`, and never assume bank hits exist in git.
3. **Promotion policy** is explicit — either bank-only by default, or a separate “promote to vault” job — not an accidental side effect of write MCP.
4. **`eval/golden.yaml` ≥ 50** labeled queries with `source_type` / segment tags; `make golden` is a CI-adjacent gate for retrieval changes.
5. **Homelab agent evals** remain separate gates (tool use, no invented paths); later add claim-level citation checks once labels exist.
6. Naming migration in `refactor.md` preserves these ownership rules; it does not merge vault and bank.

---

## Work breakdown

### Phase A — Document the invariant (this story + docs)

- [ ] Land this story under `docs/stories/`.
- [ ] Update [`../architecture.md`](../architecture.md) so vault vs bank is a first-class section (not only a single paragraph): diagram of dual writers, “Qdrant ≠ repo,” and pointers to read/write planes.
- [ ] Cross-link from `read-plane.md` / `write-plane.md`: readers may see bank-only docs; writers do not update git.
- [ ] Audit active agent skills (homelab `architect`, documentation agent prompts; in-repo query/store skills) for language that equates “in knowledge” with “in Obsidian.”

**Exit:** a new reader can answer “where does this document live?” from docs alone.

### Phase B — Ownership clarity in product behavior

- [ ] Keep path-prefix and reserved `source_type` protections; add regression tests already listed in `refactor.md` Phase 5 (sync must not prune non-`tree`).
- [ ] Decide **promotion policy** (pick one; implement later if needed):
  - **B1 — Bank-only default:** agent/API docs stay in Qdrant; Obsidian only after explicit human/PR promotion.
  - **B2 — Promote job:** periodic or on-receipt export of selected prefixes into `tree/` + PR.
- [ ] Surface `source_type` (and when useful `source_url`) in any human-facing search UI that currently implies “vault path = file on disk.”
- [ ] Optional: inventory Qdrant paths under `tree/docs/` and `tree/youtube/` that have **no** corresponding git file; publish as ops note.

**Exit:** written policy + tests; no silent claim that API writes update git.

### Phase C — Retrieval golden set (v1 eval)

- [ ] Expand `eval/golden.yaml` toward **≥ 50** hand-labeled questions (~60% happy path, ~20% edge, ~20% unanswerable / abstention).
- [ ] Tag each item with `source_type` expectation and optional `segment` (branch under `tree/`).
- [ ] Keep `kb/eval.py` Recall@K + MRR; add Precision@K when labeling supports it.
- [ ] Run `make golden` after any change to chunk size, embed model, hybrid weights, or sync.
- [ ] Wire a CI or pre-merge check that fails on Recall@K regression beyond an agreed delta vs `eval/baselines.json` (create when first stable run exists).
- [ ] Do **not** replace this with LLM-as-judge until human agreement ≥ ~80% on a calibration sample.

**Exit:** retrieval changes are gated on labeled metrics, not vibe.

### Phase D — Separate agent eval from retrieval eval

- [ ] Homelab: keep trajectory cases for MCP wiring; document that they are **not** retrieval quality scores ([`homelab/.ai/stories/agent-evaluations.md`](../../../homelab/.ai/stories/agent-evaluations.md)).
- [ ] Add at least a few cases that assert **cited paths exist** and match `source_type` when filtered.
- [ ] Later (v2): per-claim citation support labels; calibrated judge only after that foundation.

**Exit:** green architect trajectory ≠ automatic green `make golden`.

---

## Non-goals

- Renaming MCP/API services (owned by [`refactor.md`](refactor.md)).
- Changing the embedding model or collection schema as part of this story.
- Automatically committing every agent write into git.
- Building OpenWebUI payload filters (upstream limitation; MCP remains the filtered reader).
- Replacing hand-labeled retrieval eval with synthetic-only or judge-only pipelines.

---

## Acceptance criteria

- [ ] Docs state vault ≠ bank; “updated Qdrant ≠ updated repo” is unambiguous.
- [ ] Agent-facing instructions cite `source_type` / provenance and do not require a local `tree/` checkout.
- [ ] Promotion policy chosen (B1 or B2) and recorded here or in architecture.
- [ ] Golden set ≥ 50 with origin/segment tags; baseline Recall@K / MRR recorded.
- [ ] Sync/write ownership tests still pass (tree reserved; prune tree-only).
- [ ] Homelab agent eval docs note the retrieval vs trajectory split.

---

## References

- Dual writers and prune scope: `kb/sync.py`, `kb/services/write_policy.py`, `docs/write-plane.md`
- Shared read plane / OpenWebUI invariant: `docs/read-plane.md`
- Homelab agent grounding: `homelab/platform/ai/agents/solutions-architect/skills/architect/SKILL.md`
- Retrieval eval scaffold: `eval/golden.yaml`, `kb/eval.py`
- Naming / API-MCP migration (preserves ownership): [`refactor.md`](refactor.md)
)