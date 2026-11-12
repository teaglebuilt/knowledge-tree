"""kb-api: /v1 REST, legacy aliases, write MCP, and the auth boundary between them."""
from __future__ import annotations

import json

import pytest

from kb import config
from kb.api import app as app_module
from kb.api.operations import Services
from kb.services import write_policy
from kb.services.ingest import IngestError, KnowledgeIngest
from kb.services.write_policy import PayloadTooLarge, agent_policy

DOC = "# Agent delegation\n\nA subAgent binding hands over the conversation.\n"
URL = "https://kagent.dev/docs/kagent/latest/examples/agent-delegation/"
PATH = "tree/docs/kagent/agent-delegation.md"
YT_PATH = "tree/youtube/abc123.md"

WRITE, READ, ADMIN = "w-s3cret", "r-s3cret", "a-s3cret"


@pytest.fixture
def service(qdrant, embedded, monkeypatch):
    monkeypatch.setattr(config, "KB_API_WRITE_PATH_PREFIXES", ("tree/youtube/", "tree/docs/"))
    return KnowledgeIngest(client=qdrant)


@pytest.fixture
def tokens(monkeypatch):
    monkeypatch.setattr(config, "KB_API_WRITE_TOKEN", WRITE)
    monkeypatch.setattr(config, "KB_API_READ_TOKEN", "")
    monkeypatch.setattr(config, "KB_API_ADMIN_TOKEN", "")
    monkeypatch.setattr(config, "KB_API_ALLOW_ANONYMOUS_WRITES", False)


@pytest.fixture
def client(service, tokens):
    from starlette.testclient import TestClient

    with TestClient(app_module.create_app(service)) as c:
        yield c


def bearer(token: str) -> dict:
    return {"authorization": f"Bearer {token}"}


# --- write policy (shared by REST and MCP) ------------------------------------

def _agent_store(service, **overrides):
    args = {"path": PATH, "markdown": DOC, "source_url": URL} | overrides
    return write_policy.store(service, agent_policy(), **args)


def test_agent_store_then_unchanged(service):
    first, url = _agent_store(service, title="Agent delegation")
    assert first.status == "ingested" and first.chunks >= 1 and url == URL
    again, _ = _agent_store(service, title="Agent delegation")
    assert (again.status, again.chunks, again.doc_hash) == ("unchanged", 0, first.doc_hash)
    assert service.exists(PATH)["doc_hash"] == first.doc_hash


@pytest.mark.parametrize("overrides,needle", [
    ({"path": "tree/youtube/x.md"}, "only write under"),
    ({"path": "tree/docs/../infrastructure/x.md"}, "normalized"),
    ({"path": "tree/docs/Bad Name.md"}, "lowercase"),
    ({"source_url": ""}, "source_url"),
    ({"source_url": "file:///etc/passwd"}, "http(s)"),
    ({"source_type": "tree"}, "source_type"),
    ({"source_type": "chatgpt"}, "source_type"),
])
def test_agent_policy_rejections(service, overrides, needle):
    with pytest.raises(IngestError) as info:
        _agent_store(service, **overrides)
    assert needle in str(info.value)


def test_agent_size_cap(service, monkeypatch):
    monkeypatch.setattr(config, "KB_MCP_WRITE_MAX_BYTES", 10)
    with pytest.raises(PayloadTooLarge):
        _agent_store(service)


def test_frontmatter_added_and_preserved():
    out = write_policy.with_frontmatter(DOC, title="T", source_url=URL,
                                        source_type="documentation", tags=["kagent"])
    assert out.startswith("---\n") and f"source_url: {URL}" in out
    kept = write_policy.with_frontmatter("---\ntitle: Mine\n---\n\n" + DOC, title="T",
                                         source_url=URL, source_type="documentation", tags=None)
    assert "title: Mine" in kept and "source_url" in kept and kept.count("---\n") == 2


def test_reserved_source_type_rejected_for_http_writer_too(service):
    with pytest.raises(IngestError, match="reserved"):
        write_policy.store(service, write_policy.api_policy(), path=YT_PATH,
                           markdown=DOC, source_type="tree")


def test_api_writer_cannot_leave_api_prefixes(service):
    with pytest.raises(IngestError, match="must start with"):
        write_policy.store(service, write_policy.api_policy(),
                           path="tree/infrastructure/x.md", markdown=DOC)


# --- /v1 REST -----------------------------------------------------------------

def test_v1_store_status_get_search_roundtrip(client):
    r = client.post("/v1/documents", headers=bearer(WRITE),
                    json={"path": YT_PATH, "markdown": DOC, "source_type": "youtube",
                          "source_url": "https://youtu.be/abc123"})
    assert r.status_code == 200, r.text
    receipt = r.json()
    assert receipt["status"] == "ingested" and receipt["collection"] == config.QDRANT_COLLECTION

    again = client.post("/v1/documents", headers=bearer(WRITE),
                        json={"path": YT_PATH, "markdown": DOC, "source_type": "youtube"})
    assert again.json()["status"] == "unchanged"

    status = client.get("/v1/documents/status", params={"path": YT_PATH}).json()
    assert status == {"path": YT_PATH, "exists": True, "doc_hash": receipt["doc_hash"]}

    page = client.get("/v1/documents", params={"path": YT_PATH}).json()
    assert page["path"] == YT_PATH and page["next_offset"] is None
    assert "subAgent binding" in page["text"]

    hits = client.post("/v1/search", json={"query": "subAgent binding", "k": 3}).json()["hits"]
    assert hits and hits[0]["path"] == YT_PATH and hits[0]["source_type"] == "youtube"


def test_v1_get_missing_document_is_404(client):
    r = client.get("/v1/documents", params={"path": "tree/docs/nope.md"})
    assert r.status_code == 404 and r.json()["code"] == "not_found"


def test_v1_policy_error_is_400_and_reserved_type_refused(client):
    r = client.post("/v1/documents", headers=bearer(WRITE),
                    json={"path": YT_PATH, "markdown": DOC, "source_type": "memory"})
    assert r.status_code == 400 and "reserved" in r.json()["error"]


def test_v1_schema_validation_is_422(client):
    r = client.post("/v1/documents", headers=bearer(WRITE), json={"path": YT_PATH, "bogus": 1})
    assert r.status_code == 422


def test_body_cap_is_413(service, tokens, monkeypatch):
    from starlette.testclient import TestClient

    monkeypatch.setattr(config, "KB_API_MAX_BODY_BYTES", 64)
    with TestClient(app_module.create_app(service)) as c:
        r = c.post("/v1/documents", headers=bearer(WRITE),
                   json={"path": YT_PATH, "markdown": DOC * 10})
        assert r.status_code == 413 and r.json()["code"] == "payload_too_large"


def test_backend_failure_is_503_without_leaking_detail(service, tokens):
    from starlette.testclient import TestClient

    class Broken(Services):
        @property
        def ingest(self):
            raise RuntimeError("qdrant at http://secret-host:6333 refused api-key=xyz")

    with TestClient(app_module.create_app(services=Broken())) as c:
        r = c.post("/v1/documents", headers=bearer(WRITE), json={"path": YT_PATH, "markdown": DOC})
        assert r.status_code == 503
        assert "secret-host" not in r.text and "xyz" not in r.text


# --- auth scopes ----------------------------------------------------------------

def test_writes_fail_closed_without_token(service, monkeypatch):
    from starlette.testclient import TestClient

    monkeypatch.setattr(config, "KB_API_WRITE_TOKEN", "")
    monkeypatch.setattr(config, "KB_API_ALLOW_ANONYMOUS_WRITES", False)
    with TestClient(app_module.create_app(service)) as c:
        assert c.post("/v1/documents", json={"path": YT_PATH, "markdown": DOC}).status_code == 401
        assert c.post("/ingest", json={"path": YT_PATH, "markdown": DOC}).status_code == 401
        assert c.post("/mcp", json=_rpc("tools/list"), headers=MCP_HEADERS).status_code == 401
        assert service.exists(YT_PATH)["exists"] is False


def test_wrong_token_is_401(client):
    r = client.post("/v1/documents", headers=bearer("nope"), json={"path": YT_PATH, "markdown": DOC})
    assert r.status_code == 401 and r.headers["www-authenticate"] == "Bearer"


def test_read_token_cannot_write_rest_or_mcp(service, tokens, monkeypatch):
    from starlette.testclient import TestClient

    monkeypatch.setattr(config, "KB_API_READ_TOKEN", READ)
    with TestClient(app_module.create_app(service)) as c:
        assert c.post("/v1/documents", headers=bearer(READ),
                      json={"path": YT_PATH, "markdown": DOC}).status_code == 403
        assert c.post("/mcp", headers={**MCP_HEADERS, **bearer(READ)},
                      json=_rpc("tools/list")).status_code == 403
        assert c.delete("/v1/documents", headers=bearer(READ),
                        params={"path": YT_PATH}).status_code == 403
        # Reads now need a token, and the read token is enough.
        assert c.get("/v1/documents/status", params={"path": YT_PATH}).status_code == 401
        assert c.get("/exists", params={"path": YT_PATH}).status_code == 401
        assert c.get("/v1/documents/status", headers=bearer(READ),
                     params={"path": YT_PATH}).status_code == 200
        assert service.exists(YT_PATH)["exists"] is False


def test_admin_token_splits_delete_from_write(service, tokens, monkeypatch):
    from starlette.testclient import TestClient

    monkeypatch.setattr(config, "KB_API_ADMIN_TOKEN", ADMIN)
    with TestClient(app_module.create_app(service)) as c:
        c.post("/v1/documents", headers=bearer(WRITE), json={"path": YT_PATH, "markdown": DOC})
        assert c.delete("/v1/documents", headers=bearer(WRITE),
                        params={"path": YT_PATH}).status_code == 403
        r = c.delete("/v1/documents", headers=bearer(ADMIN), params={"path": YT_PATH})
        assert r.status_code == 200 and r.json()["deleted_revisions"] == 1


def test_raw_token_headers_new_and_legacy(client):
    for header in ("x-kb-write-token", "x-kb-ingest-token"):
        r = client.post("/v1/documents", headers={header: WRITE},
                        json={"path": YT_PATH, "markdown": DOC})
        assert r.status_code == 200, (header, r.text)


def test_probes_need_no_credentials(client):
    assert client.get("/healthz").json()["status"] == "ok"
    assert client.get("/readyz").json()["status"] == "ready"


# --- legacy aliases ----------------------------------------------------------------

def test_legacy_routes_keep_their_shapes(client):
    r = client.post("/ingest", headers=bearer(WRITE),
                    json={"path": YT_PATH, "markdown": DOC, "unknown": "ignored"})
    assert r.status_code == 200, r.text
    assert set(r.json()) == {"path", "doc_hash", "chunks", "status", "collection"}

    exists = client.get("/exists", params={"path": YT_PATH}).json()
    assert exists["exists"] is True and exists["doc_hash"] == r.json()["doc_hash"]

    bad = client.post("/ingest", headers=bearer(WRITE), content=b"not json")
    assert bad.status_code == 400 and "error" in bad.json()

    gone = client.post("/delete", headers=bearer(WRITE), json={"path": YT_PATH})
    assert gone.json() == {"path": YT_PATH, "deleted_revisions": 1}


def test_legacy_routes_hidden_from_openapi(client):
    paths = set(client.get("/openapi.json").json()["paths"])
    assert paths == {"/v1/search", "/v1/documents", "/v1/documents/status"}


# --- write MCP over HTTP -------------------------------------------------------------

MCP_HEADERS = {"accept": "application/json, text/event-stream",
               "content-type": "application/json"}


def _rpc(method, params=None, id_=1):
    return {"jsonrpc": "2.0", "id": id_, "method": method, "params": params or {}}


def _mcp(client, method, params=None, id_=1, headers=None):
    return client.post("/mcp", headers={**MCP_HEADERS, **(headers or bearer(WRITE))},
                       json=_rpc(method, params, id_))


def _initialize(client, headers=None):
    return _mcp(client, "initialize", {
        "protocolVersion": "2025-06-18", "capabilities": {},
        "clientInfo": {"name": "pytest", "version": "0"}}, headers=headers)


def _call_tool(client, name, arguments):
    r = _mcp(client, "tools/call", {"name": name, "arguments": arguments}, id_=3)
    assert r.status_code == 200, r.text
    return json.loads(r.json()["result"]["content"][0]["text"])


def test_mcp_requires_write_token(client):
    assert client.post("/mcp", json=_rpc("tools/list"), headers=MCP_HEADERS).status_code == 401
    assert _mcp(client, "tools/list", headers=bearer("nope")).status_code == 401


def test_mcp_lists_store_and_status_never_delete(client):
    assert _initialize(client).status_code == 200
    listed = _mcp(client, "tools/list", id_=2)
    assert listed.status_code == 200, listed.text
    names = {t["name"] for t in listed.json()["result"]["tools"]}
    expected = {"kb_store_document", "kb_document_status"}
    if config.KB_MCP_WRITE_LEGACY_TOOLS:
        expected |= {"kb_ingest", "kb_ingest_status"}
    assert names == expected
    assert not any("delete" in n for n in names)


def test_mcp_store_receipt_matches_rest(client):
    receipt = _call_tool(client, "kb_store_document",
                         {"path": PATH, "markdown": DOC, "source_url": URL})
    assert receipt["status"] == "ingested" and receipt["source_url"] == URL
    rest = client.get("/v1/documents/status", params={"path": PATH}).json()
    assert rest["doc_hash"] == receipt["doc_hash"]

    status = _call_tool(client, "kb_document_status", {"path": PATH})
    assert status == {"path": PATH, "exists": True, "doc_hash": receipt["doc_hash"]}


def test_mcp_policy_violation_is_rejected_receipt(client):
    receipt = _call_tool(client, "kb_store_document",
                         {"path": YT_PATH, "markdown": DOC, "source_url": URL})
    assert receipt["status"] == "rejected" and "only write under" in receipt["error"]
    status = _call_tool(client, "kb_document_status", {"path": YT_PATH})
    assert status["exists"] is False and "error" in status


def test_mcp_legacy_alias_same_receipt(client):
    if not config.KB_MCP_WRITE_LEGACY_TOOLS:
        pytest.skip("legacy tools disabled")
    new = _call_tool(client, "kb_store_document", {"path": PATH, "markdown": DOC, "source_url": URL})
    old = _call_tool(client, "kb_ingest", {"path": PATH, "markdown": DOC, "source_url": URL})
    assert old == {**new, "status": "unchanged", "chunks": 0}


def test_mcp_legacy_header_accepted(client):
    assert _initialize(client, headers={"x-kb-ingest-token": WRITE}).status_code == 200
