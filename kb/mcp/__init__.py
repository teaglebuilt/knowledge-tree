"""Agent-facing MCP servers over the knowledge tree.

read  -> kb-retrieval (kb_search, kb_get_document); `python -m kb.mcp`
write -> kb-ingest (kb_ingest, kb_ingest_status); mounted at /mcp by kb.api

Two servers on purpose: kagent grants tools per bound server, so merging them
would give every reader write access (enforced by tests/test_plane_separation.py).
"""
