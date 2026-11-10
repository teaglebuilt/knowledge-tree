from __future__ import annotations

import json

import pytest

from kb import config
from kb.api import app as app_module
from kb.mcp import write as mcp_write
from kb.services.ingest import KnowledgeIngest

DOC = "# Agent delegation\n\nA subAgent binding hands over the conversation.\n"
URL = "https://kagent.dev/docs/kagent/latest/examples/agent-delegation/"
PATH = "tree/docs/kagent/agent-delegation.md"


@pytest.fixture
def service(qdrant, embedded):
    svc = KnowledgeIngest(client=qdrant)
    mcp_write.bind_service(svc)
    return svc


def test_ingest_then_unchanged_receipt(service):
    first = mcp_write.ingest_receipt(PATH, DOC, URL, title="Agent delegation")
    assert first["status"] == "ingested" and first["chunks"] >= 1
    assert first["path"] == PATH and first["doc_hash"]
    again = mcp_write.ingest_receipt(PATH, DOC, URL, title="Agent delegation")
    assert again == {**first, "status": "unchanged", "chunks": 0}
    assert service.exists(PATH)["doc_hash"] == first["doc_hash"]


@pytest.mark.parametrize("kwargs,needle", [
    ({"path": "tree/infrastructure/x.md"}, "only write under"),
    ({"path": "tree/docs/../infrastructure/x.md"}, "normalized"),
    ({"path": "tree/docs/Bad Name.md"}, "lowercase"),
    ({"source_url": ""}, "source_url"),
    ({"source_type": "tree"}, "source_type"),
    ({"source_type": "chatgpt"}, "source_type"),
])
def test_policy_rejections(service, kwargs, needle):
    args = {"path": PATH, "markdown": DOC, "source_url": URL} | kwargs
    path, markdown, url = args.pop("path"), args.pop("markdown"), args.pop("source_url")
    receipt = mcp_write.ingest_receipt(path, markdown, url, **args)
    assert receipt["status"] == "rejected"
    assert needle in receipt["error"]


def test_size_cap(service, monkeypatch):
    monkeypatch.setattr(config, "KB_MCP_INGEST_MAX_BYTES", 10)
    assert mcp_write.ingest_receipt(PATH, DOC, URL)["status"] == "rejected"


def test_frontmatter_added_and_preserved():
    out = mcp_write.with_frontmatter(DOC, title="T", source_url=URL,
                                     source_type="documentation", tags=["kagent"])
    assert out.startswith("---\n") and f"source_url: {URL}" in out
    kept = mcp_write.with_frontmatter("---\ntitle: Mine\n---\n\n" + DOC, title="T",
                                      source_url=URL, source_type="documentation", tags=None)
    assert "title: Mine" in kept and "source_url" in kept and kept.count("---\n") == 2


def test_reserved_source_type_rejected_on_http_writer_too(service):
    from kb.services.ingest import IngestError

    with pytest.raises(IngestError):
        service.ingest("tree/youtube/x.md", DOC, source_type="tree")


# --- HTTP / MCP transport auth ------------------------------------------------

@pytest.fixture
def client(service, monkeypatch):
    from starlette.testclient import TestClient

    monkeypatch.setattr(app_module, "AUTH_TOKEN", "s3cret")
    app = app_module.create_app(service)
    with TestClient(app) as c:
        yield c


MCP_HEADERS = {"accept": "application/json, text/event-stream",
               "content-type": "application/json"}


def _rpc(method, params=None, id_=1):
    return {"jsonrpc": "2.0", "id": id_, "method": method, "params": params or {}}


def test_writes_fail_closed_without_token(service, monkeypatch):
    from starlette.testclient import TestClient

    monkeypatch.setattr(app_module, "AUTH_TOKEN", "")
    monkeypatch.setattr(config, "KB_INGEST_ALLOW_ANONYMOUS", False)
    with TestClient(app_module.create_app(service)) as c:
        r = c.post("/ingest", json={"path": "tree/youtube/x.md", "markdown": DOC})
        assert r.status_code == 401
        assert c.post("/mcp", json=_rpc("tools/list"), headers=MCP_HEADERS).status_code == 401


def test_mcp_requires_bearer(client):
    assert client.post("/mcp", json=_rpc("tools/list"), headers=MCP_HEADERS).status_code == 401
    bad = {**MCP_HEADERS, "authorization": "Bearer nope"}
    assert client.post("/mcp", json=_rpc("tools/list"), headers=bad).status_code == 401


def test_mcp_lists_and_calls_kb_ingest(client):
    auth = {**MCP_HEADERS, "authorization": "Bearer s3cret"}
    init = client.post("/mcp", headers=auth, json=_rpc("initialize", {
        "protocolVersion": "2025-06-18", "capabilities": {},
        "clientInfo": {"name": "pytest", "version": "0"}}))
    assert init.status_code == 200, init.text

    listed = client.post("/mcp", headers=auth, json=_rpc("tools/list", id_=2))
    assert listed.status_code == 200, listed.text
    names = {t["name"] for t in listed.json()["result"]["tools"]}
    assert names == {"kb_ingest", "kb_ingest_status"}

    called = client.post("/mcp", headers=auth, json=_rpc("tools/call", {
        "name": "kb_ingest",
        "arguments": {"path": PATH, "markdown": DOC, "source_url": URL}}, id_=3))
    assert called.status_code == 200, called.text
    receipt = json.loads(called.json()["result"]["content"][0]["text"])
    assert receipt["status"] == "ingested"

    # The REST plane still sees the same document (one service, one collection).
    r = client.get("/exists", params={"path": PATH})
    assert r.json()["exists"] is True


def test_raw_token_header_accepted(client):
    hdr = {**MCP_HEADERS, "x-kb-ingest-token": "s3cret"}
    r = client.post("/mcp", headers=hdr, json=_rpc("initialize", {
        "protocolVersion": "2025-06-18", "capabilities": {},
        "clientInfo": {"name": "pytest", "version": "0"}}))
    assert r.status_code == 200, r.text


def test_rest_routes_still_win_over_mount(client):
    assert client.get("/healthz").json()["status"] == "ok"
