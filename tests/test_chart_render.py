"""The chart must render with the values each homelab overlay passes.

Mirrors the valuesInline in homelab platform/ai/kubernetes/overlays/{mlops,application}.
A template that dereferences a removed values key renders fine in review and
only fails in the cluster's GitOps sync, so render it here.
"""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

import pytest

CHART = Path(__file__).resolve().parent.parent / "chart"

OVERLAYS = {
    "mlops": ["--set", "knowledgeScoutAgent.enabled=false"],
    "application": [
        "--set", "api.enabled=true",
        "--set", "mcp.read.enabled=false",
        "--set", "knowledgeScoutAgent.enabled=false",
        "--set", "docsAgent.enabled=false",
    ],
}

#: Chart 2.x overlay keys; values.schema.json must reject each one.
LEGACY_OVERLAYS = [
    ["--set", "ingest.enabled=true"],
    ["--set", "mcpServer.enabled=false"],
    ["--set", "docsAgent.kbIngest.name=kb-ingest"],
]

pytestmark = pytest.mark.skipif(shutil.which("helm") is None, reason="helm not installed")


def _helm_template(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["helm", "template", "knowledge-tree", str(CHART), "-n", "ai", *args],
        capture_output=True, text=True,
    )


def _render(args: list[str]) -> str:
    out = _helm_template(args)
    assert out.returncode == 0, out.stderr
    return out.stdout


def _docs(args: list[str]) -> list[dict]:
    import yaml

    return [d for d in yaml.safe_load_all(_render(args)) if d]


def _kinds(args: list[str]) -> list[str]:
    return [l.split(":", 1)[1].strip() for l in _render(args).splitlines() if l.startswith("kind:")]


def test_chart_defaults_render_with_every_object_named():
    import yaml

    docs = [d for d in yaml.safe_load_all(_render([])) if d]
    assert docs
    for d in docs:
        assert d["metadata"].get("name"), d["kind"]


@pytest.mark.parametrize("overlay", OVERLAYS)
def test_no_duplicate_objects(overlay):
    import yaml

    ids = [(d["kind"], d["metadata"]["name"])
           for d in yaml.safe_load_all(_render(OVERLAYS[overlay])) if d]
    assert len(ids) == len(set(ids)), sorted(i for i in ids if ids.count(i) > 1)


def test_mlops_renders_read_mcp_and_docs_agent():
    docs = _docs(OVERLAYS["mlops"])
    remotes = {d["metadata"]["name"]: d for d in docs if d["kind"] == "RemoteMCPServer"}
    assert set(remotes) == {"kb-mcp-read", "kb-mcp-write"}
    assert remotes["kb-mcp-write"]["spec"]["url"] == "http://kb-api.ai.svc.cluster.local:3000/mcp"
    header = remotes["kb-mcp-write"]["spec"]["headersFrom"][0]
    assert header["name"] == "X-KB-Write-Token"
    assert {d["metadata"]["name"] for d in docs if d["kind"] == "MCPServer"} == {"kb-mcp-read"}
    assert "Deployment" not in {d["kind"] for d in docs}  # kb-api lives on application


def test_application_renders_api_only():
    docs = _docs(OVERLAYS["application"])
    assert sorted((d["kind"], d["metadata"]["name"]) for d in docs) == [
        ("Deployment", "kb-api"), ("Service", "kb-api")]
    env = {e["name"]: e for e in docs[0 if docs[0]["kind"] == "Deployment" else 1]
           ["spec"]["template"]["spec"]["containers"][0]["env"]}
    assert env["KB_API_WRITE_TOKEN"]["valueFrom"]["secretKeyRef"]["name"] == "kb-api-write-token"
    assert not any(name.startswith(("KB_INGEST_", "KB_MCP_INGEST_")) for name in env)


def test_every_workload_uses_the_one_kb_image():
    docs = _docs(OVERLAYS["application"] + ["--set", "sync.enabled=true"]) + _docs([])
    images = set()
    for d in docs:
        if d["kind"] == "MCPServer":
            images.add(d["spec"]["deployment"]["image"])
        elif d["kind"] in {"Deployment", "Job"}:
            images |= {c["image"] for c in d["spec"]["template"]["spec"]["containers"]}
    assert images and {i.rsplit(":", 1)[0] for i in images} == {"ghcr.io/teaglebuilt/kb"}


def test_agents_bind_new_tool_names_only():
    text = _render([])
    assert "kb_store_document" in text and "kb_document_status" in text
    for old in ("kb-retrieval", "kb-ingest", "kb_ingest"):
        assert old not in text, old


@pytest.mark.parametrize("args", LEGACY_OVERLAYS, ids=lambda a: a[1].split("=")[0])
def test_chart_2x_overlay_keys_are_rejected(args):
    out = _helm_template(args)
    assert out.returncode != 0, f"{args} rendered; stale overlays must fail loudly"
