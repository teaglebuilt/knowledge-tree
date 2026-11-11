"""Fitness functions: the read plane stays read-only, writes stay on kb-ingest.

kagent's Claude harness ignores per-tool allowlists, so which *server* an
agent binds is the real permission boundary. If a write tool ever appears on
kb-retrieval, every agent that reads the tree silently becomes a writer.
"""
from __future__ import annotations

import asyncio
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def _names(server) -> set[str]:
    return {t.name for t in asyncio.run(server.list_tools())}


def test_read_plane_exposes_no_write_tools():
    from kb.mcp.read import mcp

    assert _names(mcp) == {"kb_search", "kb_get_document"}


def test_write_plane_tools():
    from kb.mcp.write import mcp

    assert _names(mcp) == {"kb_ingest", "kb_ingest_status"}


def test_only_documentation_agent_binds_the_write_server():
    """No other AgentTemplate in this chart may bind kb-ingest."""
    templates = [
        p for p in (ROOT / "chart" / "templates").rglob("*.yaml")
        if "kind: AgentTemplate" in p.read_text()
    ]
    assert len(templates) >= 2, "expected kb-scout and documentation AgentTemplates"
    for path in templates:
        binds_writer = "kb_ingest" in path.read_text()
        assert binds_writer == (path.parent.name == "documentation"), path


def test_values_keep_writer_prefixes_disjoint_from_tree_sync():
    values = yaml.safe_load((ROOT / "chart" / "values.yaml").read_text())
    http = values["ingest"]["pathPrefixes"].split(",")
    mcp = values["ingest"]["mcp"]["pathPrefixes"].split(",")
    assert "tree/" not in http, "tree/ overlaps paths kb sync owns"
    assert all(any(m.startswith(h) for h in http) for m in mcp)
    for prefix in http + mcp:
        assert not (ROOT / prefix).exists(), f"{prefix} is a real tree/ dir owned by kb sync"
