"""Agent-facing MCP servers, generated from kb.api.operations.

read  -> kb-mcp-read  (kb_search, kb_get_document); `python -m kb.mcp`
write -> kb-mcp-write (kb_store_document, kb_document_status); mounted at /mcp by kb.api

Two servers on purpose: kagent grants tools per bound server, so merging them
would give every reader write access (enforced by tests/test_plane_separation.py).
"""
