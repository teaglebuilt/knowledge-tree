
<p align="center">
  <img src="docs/assets/knowledge-tree-icon.svg" width="180" alt="Knowledge Tree"><br>
  <strong>Knowledge Tree</strong><br>
  <em>where knowledge takes root</em>
</p>

## Overview

Knowledge as an obsidian vault stored as markdown in git and ingested and indexed context with skills and tools for human and ai coordination. For details on how this works from a high level, read [architecture](./docs/architecture.md)

## Branches

[branches.yaml](tree/branches.yaml) is the routing file for the knowledge tree and controls building the tree at compilation with controls for encryption, pulling from remote sources such as books, etc...

- [AI](tree/ai)
- [Infrastructure](tree/infrastructure)
- [Networking](tree/networking)
- [Application](tree/application)
- [Specialized Tooling](tree/specialized_tooling)

## Searching Trees

- indexing
- tagging

## Commands

Source code used for knowledge management. Commands to interact with the knowledge bank exist in makefile.
Run `make help` to see the available commands.

## Services

One image, `ghcr.io/teaglebuilt/kb`, runs every mode:

| Mode | Command | Purpose |
|---|---|---|
| `kb-mcp-read` | `python -m kb.mcp` | Read MCP: `kb_search`, `kb_get_document` |
| `kb-api` | `python -m kb.api` | FastAPI `/v1` + `/openapi.json`, and `kb-mcp-write` at `/mcp` |
| sync | `python -m kb sync` | LanceDB → Qdrant |

- [docs/api.md](docs/api.md) - canonical HTTP contract, auth, configuration and the migration from the old names.
- [docs/mcp.md](docs/mcp.md) - the two MCP servers and their exact tool inventories.
- [docs/write-plane.md](docs/write-plane.md) - why `kb-api` exists and how writes land in Qdrant.
- [docs/read-plane.md](docs/read-plane.md) - how documents are read back, including OpenWebUI.

Automated sources (n8n YouTube ingestion) `POST /v1/documents` to `kb-api`
instead of running the local pipeline. Local commands: `make mcp` (read MCP,
stdio), `make api` (kb-api on :3000; `ANON=1` for anonymous local writes),
`make openapi` (print the OpenAPI document), `make helm-deploy-api`.
