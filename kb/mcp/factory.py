"""Generate MCP servers from an explicit allowlist of kb operations.

A tool is an Operation from kb.api.operations served under its operation_id:
the input schema is built from the operation's Pydantic model and the call
runs the operation's handler. A surface only chooses *which* operations, the
policy they run under, and how the result is rendered as text for an LLM.

This is deliberately in-repo rather than fastapi-mcp: fastapi-mcp 0.4 targets
the mcp 1.x lowlevel server API, and this project is on mcp 2.x. Generating
from the operation registry also keeps the allowlist a code-level fact rather
than a route filter.
"""
from __future__ import annotations

import asyncio
import inspect
import logging
from collections.abc import Callable
from dataclasses import dataclass
from typing import Annotated, Any

from mcp.server.mcpserver import MCPServer
from pydantic import BaseModel, Field

from ..api.operations import OPERATIONS, Operation, Services
from ..services.write_policy import WritePolicy

log = logging.getLogger("kb.mcp")

Render = Callable[[Any, BaseModel], str]
OnError = Callable[[dict, Exception], str]


@dataclass(frozen=True)
class ToolBinding:
    operation_id: str
    render: Render
    #: Defaults to operation_id. Set only for deprecated aliases.
    name: str | None = None
    #: A subclass of the operation's model (e.g. the stricter agent variant).
    input_model: type[BaseModel] | None = None
    policy: Callable[[], WritePolicy] | None = None
    #: Turn a failure into a text result (write receipts); None re-raises.
    on_error: OnError | None = None
    description: str | None = None


def build_server(
    name: str,
    instructions: str,
    bindings: tuple[ToolBinding, ...],
    services: Callable[[], Services],
    *,
    tag: str,
) -> MCPServer:
    """Serve exactly `bindings`; every one must carry the operation tag `tag`."""
    server = MCPServer(name=name, instructions=instructions)
    for binding in bindings:
        op = OPERATIONS[binding.operation_id]
        if op.tag != tag:
            raise ValueError(f"{op.operation_id} is tagged {op.tag!r}, not {tag!r}; not on {name}")
        model = binding.input_model or op.input_model
        if not issubclass(model, op.input_model):
            raise TypeError(f"{model.__name__} must subclass {op.input_model.__name__}")
        server.add_tool(
            _tool(binding, op, model, services),
            name=binding.name or op.operation_id,
            description=binding.description or op.description,
            structured_output=False,
        )
    return server


def _tool(
    binding: ToolBinding, op: Operation, model: type[BaseModel],
    services: Callable[[], Services],
):
    tool_name = binding.name or op.operation_id

    async def call(**kwargs: Any) -> str:
        if tool_name != op.operation_id:
            log.warning("deprecated tool %s called; use %s", tool_name, op.operation_id)
        try:
            req = model(**kwargs)
            policy = binding.policy() if binding.policy else None
            result = await asyncio.to_thread(op.handler, services(), req, policy)
        except Exception as exc:
            if binding.on_error is None:
                raise
            return binding.on_error(kwargs, exc)
        return binding.render(result, req)

    sig = _signature(model)
    call.__signature__ = sig  # type: ignore[attr-defined]
    call.__annotations__ = {p.name: p.annotation for p in sig.parameters.values()} | {
        "return": str
    }
    call.__name__ = call.__qualname__ = tool_name
    return call


def _signature(model: type[BaseModel]) -> inspect.Signature:
    """Keyword-only parameters mirroring the model's fields and constraints."""
    params = []
    for field_name, field in model.model_fields.items():
        annotation = Annotated[  # type: ignore[valid-type]
            (field.annotation, *field.metadata, Field(description=field.description))
        ]
        default = inspect.Parameter.empty if field.is_required() else field.default
        params.append(
            inspect.Parameter(
                field_name, inspect.Parameter.KEYWORD_ONLY, default=default,
                annotation=annotation,
            )
        )
    return inspect.Signature(params, return_annotation=str)
