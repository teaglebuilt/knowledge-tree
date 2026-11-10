"""Per-provider conversation-export ingestion (kb.providers.<name>).

Each provider is a self-contained package for one external export format
(e.g. `openai/` for ChatGPT exports). A provider package parses its own
format into `MessageRecord`s and stores them, but does not import from a
sibling provider package. Cross-cutting concerns that aren't tied to any
one export format (secret redaction, config, the Qdrant adapter) live at
`kb.redact`, `kb.config`, `kb.adapters` instead of inside a provider.

No shared base class is enforced here: with a single provider there isn't
yet a real shape to abstract. Once a second provider (e.g. `claude/`)
exists, pull out a `typing.Protocol` for whatever their `run()`/store
classes turn out to have in common, rather than guessing now.
"""
