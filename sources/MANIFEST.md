---
title: Source Manifest
description: Provenance record for binary source artifacts (books, papers) kept outside git.
summary: The binaries live locally / in object storage and are gitignored; this manifest is the versioned record.
category: manifest
tags:
- sources
- provenance
last_updated: 2026-08-14
---

# Source Manifest

Binary source artifacts (epubs, PDFs) are **not** committed — they are gitignored
(`*.epub`, `*.pdf`). Only their **extracted markdown** (under `tree/…`) enters the
retrieval index (`kb/ingest.py` globs `tree/**/*.md`). This manifest is the tracked
provenance record so the sources are known even without the blobs.

Layout mirrors `tree/` by domain:

```
sources/<domain>/{books,pdf}/<file>
tree/<domain>/…                     ← extracted markdown lives here, links back to source
```

Local files are kept for re-extraction; back them up to homelab object storage.

## ai → `tree/ai/`

| Type | Title | Author | File | sha256(16) |
|---|---|---|---|---|
| book | OpenClaw AI in Production | Ken Huang | `sources/ai/books/OpenClaw AI in Production ….epub` | `fb1d825182a00f72` |
| book | The Context Engineering Handbook | Drew Breunig | `sources/ai/books/The Context Engineering Handbook ….epub` | `31252a2d889098a6` |
| pdf | Build Your Own Agentic AI Framework | Gigi Sayfan | `sources/ai/pdf/Build Your Own Agentic AI Framework ….pdf` | `5347e44091e9f0df` |
| pdf | Agents | — | `sources/ai/pdf/agents.pdf` | `6beddc2fab0e2a72` |
| pdf | LLM Training | — | `sources/ai/pdf/llm-training.pdf` | `716484a814cf981c` |

## networking/censorship → `tree/networking/censorship/`

| Type | Title | Author | File | sha256(16) |
|---|---|---|---|---|
| book | Controlled Experimentation of Digital Forensics | Oliveira, Silva et al. | `sources/networking/censorship/books/Controlled Experimentation ….epub` | `306c4ce1f28f713d` |
| pdf | Just Add Water (WATER/WATM runtime) | — | `sources/networking/censorship/pdf/foci-2024-0003.pdf` | `d8cf0ccd9bb46035` |
| pdf | Internet Censorship | — | `sources/networking/censorship/pdf/internet-censorship.pdf` | `85a4f9199323cbb0` |
| pdf | Routing Around Decoys | — | `sources/networking/censorship/pdf/decoy-ccs12.pdf` | `1f0eb34940571b1e` |
| pdf | Deploying Xray-core in a Home Lab | — | `sources/networking/censorship/pdf/Deploying Xray-core in a Home Lab ….pdf` | `33c6fe5c221b355e` |

## specialized_tooling/webassembly → `tree/specialized_tooling/webassembly/`

| Type | Title | Author | File | sha256(16) |
|---|---|---|---|---|
| pdf | Server-Side WebAssembly | Danilo Chiarlone | `sources/specialized_tooling/webassembly/pdf/Server-Side WebAssembly ….pdf` | `3ec57bb279cabda1` |
