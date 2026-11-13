"""Token auth for kb-api: one resolver for REST routes and the /mcp gate.

Scopes are hierarchical: admin ⊃ write ⊃ read. Tokens come from config at
call time so tests (and a future rotation hook) can swap them.
"""
from __future__ import annotations

import hmac
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Annotated, Literal

from fastapi import Depends, Request
from fastapi.security import APIKeyHeader, HTTPAuthorizationCredentials, HTTPBearer
from starlette.responses import JSONResponse

from .. import config

Scope = Literal["read", "write", "admin"]

#: Raw-token header for callers that can only copy a Secret value verbatim
#: (kagent RemoteMCPServer `headersFrom` cannot prepend "Bearer ").
TOKEN_HEADER = "x-kb-write-token"
#: Pre-rename header; accepted until callers migrate (docs/api.md#migration).
LEGACY_TOKEN_HEADER = "x-kb-ingest-token"


@dataclass(frozen=True)
class Principal:
    name: str
    scopes: frozenset[str]

    def can(self, scope: Scope) -> bool:
        return scope in self.scopes


class ApiError(Exception):
    def __init__(self, status: int, code: str, message: str) -> None:
        super().__init__(message)
        self.status = status
        self.code = code
        self.message = message


def _eq(a: str, b: str) -> bool:
    return hmac.compare_digest(a.encode(), b.encode())


def presented_token(authorization: str, headers: Mapping[str, str]) -> str:
    scheme, _, token = (authorization or "").partition(" ")
    if scheme.lower() == "bearer" and token.strip():
        return token.strip()
    return (headers.get(TOKEN_HEADER) or headers.get(LEGACY_TOKEN_HEADER) or "").strip()


def authenticate(token: str) -> Principal:
    read, write, admin = (
        config.KB_API_READ_TOKEN,
        config.KB_API_WRITE_TOKEN,
        config.KB_API_ADMIN_TOKEN,
    )
    # Without a dedicated admin token, the write token keeps the old
    # single-token power to delete.
    write_scopes = {"read", "write"} | (set() if admin else {"admin"})
    if token and (read or write or admin):
        if admin and _eq(token, admin):
            return Principal("admin", frozenset({"read", "write", "admin"}))
        if write and _eq(token, write):
            return Principal("write", frozenset(write_scopes))
        if read and _eq(token, read):
            return Principal("read", frozenset({"read"}))
        raise ApiError(401, "unauthorized", "invalid credentials")
    scopes: set[str] = set() if read else {"read"}
    if not write and config.KB_API_ALLOW_ANONYMOUS_WRITES:
        scopes |= write_scopes
    return Principal("anonymous", frozenset(scopes))


def authorize(principal: Principal, scope: Scope) -> None:
    if principal.can(scope):
        return
    if principal.name == "anonymous":
        raise ApiError(401, "unauthorized", "missing credentials")
    raise ApiError(403, "forbidden", f"token lacks the {scope!r} scope")


# --- FastAPI dependencies -----------------------------------------------------
# Declared as security schemes so /openapi.json documents both header forms.
_bearer = HTTPBearer(auto_error=False, description="Bearer <token>")
_raw = APIKeyHeader(name="X-KB-Write-Token", auto_error=False, description="Raw token")


def require(scope: Scope):
    def dependency(
        request: Request,
        _b: Annotated[HTTPAuthorizationCredentials | None, Depends(_bearer)],
        _r: Annotated[str | None, Depends(_raw)],
    ) -> Principal:
        headers = request.headers
        principal = authenticate(presented_token(headers.get("authorization", ""), headers))
        authorize(principal, scope)
        return principal

    return dependency


# --- ASGI gate for the mounted write MCP --------------------------------------

def error_response(status: int, code: str, message: str) -> JSONResponse:
    headers = {"WWW-Authenticate": "Bearer"} if status == 401 else None
    return JSONResponse({"error": message, "code": code}, status_code=status, headers=headers)


class ScopeGate:
    """Refuse any HTTP request lacking `scope` before it reaches the wrapped app."""

    def __init__(self, app, scope: Scope) -> None:
        self.app = app
        self.scope = scope

    async def __call__(self, scope, receive, send) -> None:
        if scope["type"] == "http":
            headers = {
                k.decode("latin-1"): v.decode("latin-1") for k, v in scope.get("headers") or []
            }
            try:
                principal = authenticate(
                    presented_token(headers.get("authorization", ""), headers)
                )
                authorize(principal, self.scope)
            except ApiError as exc:
                await error_response(exc.status, exc.code, exc.message)(scope, receive, send)
                return
        await self.app(scope, receive, send)
