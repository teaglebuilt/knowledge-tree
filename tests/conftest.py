"""Shared fixtures: in-memory Qdrant + a deterministic fake embedder.

No network, no model download: qdrant-client's local mode stands in for the
cluster, and embeddings are a stable hash so tests can assert on exactly what
text would have been sent to the embedder.
"""
from __future__ import annotations

import hashlib
import shutil
import zipfile
from pathlib import Path

import pytest

from kb import config, embed

FIXTURES = Path(__file__).parent / "fixtures"


def _vector(text: str) -> list[float]:
    digest = hashlib.sha256(text.encode()).digest()
    raw = (digest * (config.EMBED_DIM // len(digest) + 1))[: config.EMBED_DIM]
    return [b / 255.0 + 1e-3 for b in raw]


@pytest.fixture
def embedded(monkeypatch) -> list[str]:
    """Patch the embedder; the returned list records every embedded text."""
    seen: list[str] = []

    def fake_embed(texts):
        seen.extend(texts)
        return [_vector(t) for t in texts]

    monkeypatch.setattr(embed, "embed", fake_embed)
    monkeypatch.setattr(embed, "embed_query", _vector)
    return seen


@pytest.fixture
def qdrant():
    from qdrant_client import QdrantClient

    return QdrantClient(":memory:")


@pytest.fixture
def export_zip(tmp_path) -> Path:
    """Synthetic export with numbered conversations-*.json files."""
    zpath = tmp_path / "chatgpt-export.zip"
    with zipfile.ZipFile(zpath, "w") as zf:
        for f in sorted((FIXTURES / "chatgpt").glob("conversations-*.json")):
            zf.write(f, arcname=f.name)
    return zpath


@pytest.fixture
def archive_dir(tmp_path) -> Path:
    path = tmp_path / "archive"
    yield path
    shutil.rmtree(path, ignore_errors=True)
