---
name: collect_knowledge
description: Collect and import knowledge from local files or directories into the knowledge tree, translating any non-English content to English first and verifying the translation before anything is merged. Analyzes content to determine domain placement, evaluates whether the knowledge already exists in the tree, decides optimal organization (new file, merge, or skip), and generates frontmatter. Use this skill whenever importing local markdown, documentation, notes, or text files from an external directory into the tree — especially when the source may be in another language, when you need deduplication against existing content, or when a corpus needs organizing by domain.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task
---

# Collect Knowledge

Import local files and directories into the knowledge tree under `tree/`, in English, without breaking their structure.

The hard part is not reading files — it is that a corpus in another language must come out the other side fully translated, with its headings, code, tables, links and frontmatter intact. That does not happen by intending it. Translation is expensive and every other step in this skill is cheap, so under load the expensive step is the one that silently gets skipped. This skill therefore treats translation as a **gated** step: staged, machine-checked, and blocked from merging until it passes.

## When to use

- You have a local directory of notes or documentation to integrate into the tree
- A corpus is in Chinese, Japanese, Korean, Russian, or any non-English language and needs to land in the tree in English
- You're consolidating multiple local sources and need to avoid duplicates
- You want to assess whether new knowledge is truly new or supplements existing tree content
- You need to audit an already-imported part of the tree for untranslated content

## The tools

Three scripts under `scripts/`, all path-agnostic — they take arguments, hold no embedded paths, and work on any markdown corpus:

| Script | Role |
|---|---|
| `lang_scan.py` | Detect what still needs translating, and where. Plans chunks for large files. |
| `verify_translation.py` | The gate. Residual-language, structure-parity and anchor checks. |
| `mdlang.py` | Shared library — not run directly. |

They resolve their own imports, so run them from any working directory. Python 3.9+, no third-party dependencies.

## Workflow

### 1. Triage the source

```bash
python scripts/lang_scan.py <source-path> --summary
```

This buckets every file by how much non-English text it holds, and names the dominant script. Use it to size the job before starting, then branch per file:

| Bucket | Meaning | What to do |
|---|---|---|
| `CLEAN` | no non-Latin text found | skip to step 5 — nothing to translate |
| `TRACE` | under 5% of lines | translate whole-file; often just a stray line or a proper noun |
| `PARTIAL` | 5–25% of lines | translate whole-file, or chunk if long |
| `HEAVY` | over 25% of lines | chunk if over ~400 lines, then translate |

Add `--show 20` on any single file to see exactly which lines and which category.

### 2. Stage, don't edit in place

Translate into a staging directory, never over the source. Keeping the original untouched is what makes the structure comparison in step 4 possible, and what makes a bad translation recoverable.

Mirror the path each file has *relative to the corpus root* — step 4 pairs originals to translations by that relative path, and files that don't line up get no structure checking at all:

```bash
SRC=<source-path>                 # e.g. ~/corpus/domain-05
STAGE=/tmp/collect-staging

# For a file at $SRC/01-identity/03-tokens.md, stage it at
# $STAGE/01-identity/03-tokens.md
mkdir -p "$STAGE/01-identity"
```

### 3. Translate — delegate to Haiku

**Translation is execution, not judgment. Dispatch it to Haiku subagents rather than doing it inline.**

The decisions in this skill — which domain a file belongs to, whether something is a duplicate, whether a failing check is a real problem — are judgment and belong to the orchestrating model. Rendering Chinese prose into English while preserving markdown is mechanical, high-volume, and the single largest token cost in the whole workflow. Running it inline is the expensive way to get the same result, and on a corpus of any size it will exhaust context before the batch finishes.

Dispatch one Haiku subagent per file (or per chunk, for large files) with `Task`, setting `model: "haiku"`:

```
Task(
  model: "haiku",
  prompt: """
    Translate this file to English and write the result to <staging-path>.
    Source: <source-path>            # for a chunk: lines N-M only
    Read these rules first and follow them exactly:
      <skill-path>/references/translation-rules.md
    Translate — do not summarize, improve, or reorganize. Every heading, table
    row, list item and code block in the source must appear in your output.
    Do not modify the source file.
  """
)
```

Because subagents run in parallel and can't see each other's terminology choices, two guards matter:

- **Chunks of the same file must go to the same agent, in order**, or terminology drifts mid-document. Parallelize across *files*, serialize within one.
- **Never trust a subagent's "done."** It reports success; step 4 decides. This is the entire reason the gate exists — a reported-complete translation with an untranslated frontmatter block looks identical to a correct one until something checks.

Batch dispatch, then gate the whole batch at once. Re-dispatch only the files that failed, quoting the specific failure so the retry is targeted rather than a blind re-translation.

#### What to dispatch, per file

Every file that isn't `CLEAN` needs a job. Read the translation rules below before writing the first prompt, and skim `references/translation-rules.md` for the cases the summary can't settle — mixed-language files, text that should legitimately stay in the source language, and ambiguous inline code. Point each subagent at that reference too; it's written to be read by whoever does the work.

**Small files (under ~400 lines):** one job — translate the whole file to staging.

**Large files:** get a chunk plan first —

```bash
python scripts/lang_scan.py <file> --plan
```

It prints one line per chunk:

```
chunk 0   lines 1-56      ( 56)  (frontmatter -- translate title/description/summary, keep slugs and dates)
chunk 1   lines 57-498    (442)
chunk 2   lines 499-999   (501)  2.6 Grype in continuous integration
chunk 3   lines 1000-1565 (566)  4.1 CVSS v3.1 base scoring
```

Ranges are contiguous and cover the file from line 1. Translate them **in order**, appending each result to the staged file (`>>`), so the reassembled document has every line accounted for.

Chunk 0 is always the frontmatter when the file has any. It gets its own chunk precisely because it sits above the first heading — a plan built from heading boundaries alone would skip it, and untranslated `title`/`description`/`summary` is the costliest thing to miss. Body boundaries land on `##`/`#` headings and never inside a code fence, so each piece is self-contained. A chunk may run somewhat over the target size when a single section is long; that's expected.

Chunking is not an optimization, it's a correctness measure. Asked to "translate this 2,700-line document," a model starts condensing somewhere in the middle; asked to translate a bounded section, it translates it. Carry forward the terminology you chose in earlier chunks so a term doesn't change spelling halfway through the file.

Whatever you do, **translate — do not summarize, improve, or reorganize.** Every heading, row, bullet and code block in the source must appear in the output. Step 4 checks this, and a file that lost content will be sent back.

### 4. Verify — the gate

```bash
python scripts/verify_translation.py \
  --original-dir <source-path> \
  --translated-dir /tmp/collect-staging
```

Exit code 0 means clean; 1 means at least one file failed. Failures are specific — line numbers for residual text, counts for dropped structure, named targets for broken anchors. **Fix and re-run until it exits 0.** Nothing moves into `tree/` before that.

Warnings (`!`) don't block, but read them. The two that matter most:

- **Line-count delta beyond ±15%** (the default `line_delta_tolerance`). A large *negative* delta usually means a section was summarized away rather than translated — check the chunk seams first.
- **Non-Latin text inside code.** Usually a comment that was missed. Occasionally a legitimate string literal, which is why it warns rather than blocks.

### 5. Analyze and deduplicate

Only once the content is in English:

- Determine the domain (`networking`, `infrastructure`, `security`, `ai`, etc.) and pick a destination under `tree/<domain>/`, using subdirectories where a topic warrants it
- Query the tree for near-duplicates using [[query_knowledge]] — semantic similarity plus metadata overlap
- Decide per file: **new** → promote it; **duplicate** → skip and note it; **supplement** → merge into the existing file or add a cross-reference

This ordering is deliberate. Similarity search against an English tree using a source-language query returns noise, so deduplication before translation produces a bad answer.

### 6. Promote into the tree

Staging exists so the tree only ever receives verified content. Move each **new** file to the destination you chose:

```bash
STAGE=/tmp/collect-staging
DEST=tree/security/incident-response          # the domain path you decided in step 5

mkdir -p "$DEST"
cp "$STAGE/07-incident-response/01-security-incident-response-playbook.md" "$DEST/"
```

Copy rather than move, so staging stays intact if you need to re-check something. The source layout and the tree layout are usually *different* — step 2's mirroring existed to pair files with their originals for verification, not to dictate where they belong. Reorganize freely here.

Three things to settle as you promote:

1. **Rewrite intra-corpus links.** A file that linked to `[[domain-05-security/README.md|Back to index]]` now needs the tree path. Links to files you didn't collect will dangle — list them in the report rather than deleting them; a dangling link is a useful marker of something worth collecting later, but only if someone knows it exists.
2. **Merge candidates aren't copies.** If a file supplements existing tree content, edit the existing file and cross-reference; don't drop a near-duplicate beside it.
3. **Update `source_path`** if you renamed the file, so provenance still resolves.

Then re-run the gate against the tree itself, because promotion can introduce problems staging never had — a bad merge, a broken rewritten link:

```bash
python scripts/lang_scan.py tree/ --gate
```

Finally, index the new content so it becomes searchable:

```bash
make ingest && make reindex
```

### 7. Report

Summarize: files collected and where they landed, files translated and from which language, duplicates skipped, merge candidates, and anything left for manual review.

---

## Translation rules

The single question that governs everything: **will a reader or an embedding index see this text?** If yes it must be English. If it's a machine identifier — a path, a URL, a variable name — it must be left exactly as it is.

### Always translate

| What | Why it matters |
|---|---|
| Body prose, headings, list items, table cells | The obvious content |
| Frontmatter `title`, `description`, `summary`, `audience`, `intent_queries` | **These feed the embedding index.** Leaving them in the source language poisons search across the whole tree — the highest-cost mistake available here |
| Comments inside code blocks | They're explanation, not code |
| Link text and wikilink aliases — the part *after* the `\|` | Reader-visible |
| Blockquotes, callouts, admonitions | Reader-visible |

### Never translate

| What | What breaks if you do |
|---|---|
| URLs, and link targets inside `](...)` | Dead links |
| Wikilink targets — the part *before* the `\|` in `[[target\|alias]]` | The graph loses the edge |
| Code: identifiers, function names, string literals, CLI flags | The code stops working |
| Code fence info strings (` ```yaml `) | Syntax highlighting breaks; the verifier flags it |
| Frontmatter *keys*, and slug-valued fields (`tags`, `category`, `tier`, dates) | Schema drift |

### Regenerate, don't translate

**Heading anchors.** A table of contents entry like `[概述](#1-概述)` has two halves that behave differently: the link text is prose and gets translated, while the `#1-概述` target is *derived* from the heading. Translating it as text produces `#1-overview` only by luck; the reliable move is to rebuild every anchor from the final English heading using GitHub slug rules — lowercase, punctuation dropped, spaces to hyphens. `verify_translation.py` checks that every anchor resolves to a heading that actually exists.

**Relative paths to other documents.** If a source file links to `../other-domain/doc.md` and that file lands somewhere else in `tree/`, the link needs remapping to the new location, not translating. Cross-corpus links that have no counterpart in the tree should be flagged in the report rather than silently left broken.

For edge cases — mixed-language files, quoted source-language material that should stay, ambiguous inline code — see `references/translation-rules.md`.

---

## Frontmatter convention

Keep every key the source already has and keep its slug-valued fields untouched; translate the human-readable values; then add the two provenance fields below **if they aren't already present**:

```yaml
---
title: Human-readable title, in English
description: Brief summary, in English — this is indexed, so it must be English
tags: [domain, topic]            # slugs, left as-is
created: '2026-08-29'
last_updated: 2026-08-29
source_path: /original/path/to/file.md
original_language: Chinese        # or English when no translation was needed
---
```

`source_path` and `original_language` are what make a bad translation recoverable later — without them there's no way to find the original and redo it. The verifier warns when they're missing.

---

## Auditing content that's already in the tree

The scanner works on the tree itself, which is how you find content that was imported before this gate existed:

```bash
python scripts/lang_scan.py tree/ --summary
python scripts/lang_scan.py tree/ --bucket HEAVY --show 5    # worst offenders
python scripts/lang_scan.py tree/ --gate                     # exit 1 if any remain
```

The `--gate` form is suitable for a pre-commit hook or CI step, so untranslated content can't re-enter.

---

## After collecting

The gate proves structure and completeness. It cannot prove the translation is *good*, so two things remain human-shaped:

1. **Spot-check terminology** on a translated file against its original. The verifier confirms nothing was dropped and no source language remains; it has no opinion on whether a domain term was rendered well.
2. **Query what you collected** with [[query_knowledge]] to confirm the new material actually surfaces for the questions it should answer. If it doesn't, the `title`/`description`/`summary` are usually the reason.

## Related

- Index collected knowledge: [[store_knowledge]]
- Search the knowledge tree: [[query_knowledge]]
- Run analysis on collected material: [[run_research_report]]
- Config (embedding model, chunk sizes): `kb/config.py`
