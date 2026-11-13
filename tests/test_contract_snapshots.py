"""Schema-drift gates: /openapi.json and both MCP tools/list must match the
committed snapshots. Regenerate deliberately with KB_UPDATE_SNAPSHOTS=1 and
review the diff — a change here is a change to every client's contract.
"""
from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path

import pytest

SNAPSHOTS = Path(__file__).parent / "snapshots"


def _check(name: str, actual: object) -> None:
    path = SNAPSHOTS / name
    rendered = json.dumps(actual, indent=2, sort_keys=True) + "\n"
    if os.environ.get("KB_UPDATE_SNAPSHOTS") == "1":
        path.write_text(rendered)
        return
    if not path.exists():
        pytest.fail(f"missing {path}; run with KB_UPDATE_SNAPSHOTS=1 and commit it")
    assert json.loads(path.read_text()) == actual, f"{name} drifted; see module docstring"


def _tools(server) -> list[dict]:
    return sorted(
        ({"name": t.name, "description": t.description, "input_schema": t.input_schema}
         for t in asyncio.run(server.list_tools())),
        key=lambda t: t["name"],
    )


def test_openapi_snapshot():
    from kb.api.app import create_app

    spec = create_app().openapi()
    ops = {op["operationId"] for path in spec["paths"].values() for op in path.values()}
    assert ops == {"kb_search", "kb_get_document", "kb_store_document",
                   "kb_document_status", "kb_delete_document"}
    _check("openapi.json", spec)


def test_read_mcp_tools_snapshot():
    from kb.mcp.read import mcp

    _check("mcp-read-tools.json", _tools(mcp))


def test_write_mcp_tools_snapshot():
    from kb.mcp.write import create_server

    _check("mcp-write-tools.json", _tools(create_server(legacy=False)))
