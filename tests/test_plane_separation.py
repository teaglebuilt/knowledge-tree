"""Fitness functions: kb-mcp-read stays read-only, writes stay on kb-mcp-write.

kagent's Claude harness ignores per-tool allowlists, so which *server* an
agent binds is the real permission boundary. If a write tool ever appears on
kb-mcp-read, every agent that reads the tree silently becomes a writer.
"""
from __future__ import annotations

import asyncio
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent


def _names(server) -> set[str]:
    return {t.name for t in asyncio.run(server.list_tools())}


def test_read_server_exposes_exactly_read_tools():
    from kb.mcp.read import SERVER_NAME, mcp

    assert SERVER_NAME == "kb-mcp-read"
    assert _names(mcp) == {"kb_search", "kb_get_document"}


def test_write_server_tools_and_legacy_toggle():
    from kb.mcp.write import SERVER_NAME, create_server

    assert SERVER_NAME == "kb-mcp-write"
    assert _names(create_server(legacy=False)) == {"kb_store_document", "kb_document_status"}
    assert _names(create_server(legacy=True)) == {
        "kb_store_document", "kb_document_status", "kb_ingest", "kb_ingest_status"}


def test_no_agent_surface_exposes_admin_operations():
    from kb.api.operations import OPERATIONS
    from kb.mcp.read import mcp as read
    from kb.mcp.write import create_server

    admin = {op_id for op_id, op in OPERATIONS.items() if op.tag == "admin"}
    assert admin == {"kb_delete_document"}
    exposed = _names(read) | _names(create_server(legacy=True))
    assert not exposed & admin
    assert not any("delete" in name for name in exposed)


def test_factory_refuses_cross_plane_bindings():
    from kb.api.operations import Services
    from kb.mcp.factory import ToolBinding, build_server

    for op_id in ("kb_store_document", "kb_document_status", "kb_delete_document"):
        with pytest.raises(ValueError):
            build_server("x", "", (ToolBinding(op_id, render=str),), Services, tag="mcp-read")


def test_tool_schemas_come_from_the_canonical_models():
    from kb.api import schemas
    from kb.mcp.read import mcp as read
    from kb.mcp.write import create_server

    tools = {t.name: t for t in asyncio.run(read.list_tools())}
    tools |= {t.name: t for t in asyncio.run(create_server(legacy=False).list_tools())}
    for name, model in {
        "kb_search": schemas.SearchRequest,
        "kb_get_document": schemas.DocumentPageRequest,
        "kb_store_document": schemas.AgentStoreDocumentRequest,
        "kb_document_status": schemas.DocumentStatusRequest,
    }.items():
        schema = tools[name].input_schema
        assert set(schema["properties"]) == set(model.model_fields), name
        required = {f for f, info in model.model_fields.items() if info.is_required()}
        assert set(schema.get("required", [])) == required, name


def test_only_documentation_agent_binds_the_write_server():
    """No other AgentTemplate in this chart may bind kb-mcp-write or its tools."""
    templates = [
        p for p in (ROOT / "chart" / "templates").rglob("*.yaml")
        if "kind: AgentTemplate" in p.read_text()
    ]
    assert len(templates) >= 2, "expected kb-scout and documentation AgentTemplates"
    for path in templates:
        text = path.read_text()
        binds_writer = "kbWriter" in text or "kb_store_document" in text or "kb_ingest" in text
        assert binds_writer == (path.parent.name == "documentation"), path


def test_scout_cannot_reach_the_writer_even_by_url():
    values = yaml.safe_load((ROOT / "chart" / "values.yaml").read_text())
    assert not any("kb-api" in o for o in values["knowledgeScoutAgent"]["egressOrigins"])


def test_values_keep_writer_prefixes_disjoint_from_tree_sync():
    values = yaml.safe_load((ROOT / "chart" / "values.yaml").read_text())
    http = values["api"]["writePolicy"]["pathPrefixes"].split(",")
    mcp = values["api"]["mcpWrite"]["pathPrefixes"].split(",")
    assert "tree/" not in http, "tree/ overlaps paths kb sync owns"
    assert all(any(m.startswith(h) for h in http) for m in mcp)
    for prefix in http + mcp:
        assert not (ROOT / prefix).exists(), f"{prefix} is a real tree/ dir owned by kb sync"
