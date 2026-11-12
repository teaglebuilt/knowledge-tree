"""Renamed env vars: new name wins, old name still works with a warning, and
two different values are an error instead of a silent pick."""
from __future__ import annotations

import logging

import pytest

from kb import config


def test_new_name_used(monkeypatch):
    monkeypatch.setenv("KB_API_WRITE_TOKEN", "new")
    monkeypatch.delenv("KB_INGEST_TOKEN", raising=False)
    assert config.env_compat("KB_API_WRITE_TOKEN", "") == "new"


def test_legacy_name_resolves_with_warning(monkeypatch, caplog):
    monkeypatch.delenv("KB_MCP_WRITE_MAX_BYTES", raising=False)
    monkeypatch.setenv("KB_MCP_INGEST_MAX_BYTES", "1024")
    with caplog.at_level(logging.WARNING, logger="kb.config"):
        assert config.env_compat("KB_MCP_WRITE_MAX_BYTES", "0") == "1024"
    assert "KB_MCP_INGEST_MAX_BYTES is deprecated" in caplog.text


def test_same_value_under_both_names_is_fine(monkeypatch):
    monkeypatch.setenv("KB_API_WRITE_PATH_PREFIXES", "tree/docs/")
    monkeypatch.setenv("KB_INGEST_PATH_PREFIXES", "tree/docs/")
    assert config.env_compat("KB_API_WRITE_PATH_PREFIXES", "tree/") == "tree/docs/"


def test_conflicting_values_fail(monkeypatch):
    monkeypatch.setenv("KB_API_ALLOW_ANONYMOUS_WRITES", "false")
    monkeypatch.setenv("KB_INGEST_ALLOW_ANONYMOUS", "true")
    with pytest.raises(ValueError, match="both set and differ"):
        config.env_compat("KB_API_ALLOW_ANONYMOUS_WRITES", "false")


def test_default_when_neither_set(monkeypatch):
    monkeypatch.delenv("KB_API_PORT", raising=False)
    monkeypatch.delenv("KB_INGEST_PORT", raising=False)
    assert config.env_compat("KB_API_PORT", "3000") == "3000"
