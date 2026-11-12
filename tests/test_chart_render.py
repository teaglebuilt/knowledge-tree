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
        "--set", "ingest.enabled=true",
        "--set", "mcpServer.enabled=false",
        "--set", "knowledgeScoutAgent.enabled=false",
        "--set", "docsAgent.enabled=false",
    ],
}

pytestmark = pytest.mark.skipif(shutil.which("helm") is None, reason="helm not installed")


def _render(args: list[str]) -> str:
    out = subprocess.run(
        ["helm", "template", "knowledge-tree", str(CHART), "-n", "ai", *args],
        capture_output=True, text=True,
    )
    assert out.returncode == 0, out.stderr
    return out.stdout


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


def test_mlops_renders_read_plane_and_docs_agent():
    import yaml

    docs = [d for d in yaml.safe_load_all(_render(OVERLAYS["mlops"])) if d]
    remotes = {d["metadata"]["name"] for d in docs if d["kind"] == "RemoteMCPServer"}
    assert remotes == {"kb-retrieval", "kb-ingest"}
    assert "MCPServer" in {d["kind"] for d in docs}
    assert "Deployment" not in {d["kind"] for d in docs}  # kb-ingest lives on application


def test_application_renders_write_plane_only():
    kinds = _kinds(OVERLAYS["application"])
    assert sorted(kinds) == ["Deployment", "Service"]
