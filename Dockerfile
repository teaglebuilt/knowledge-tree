# syntax=docker/dockerfile:1.7
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS builder

WORKDIR /build

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_PYTHON_DOWNLOADS=0 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

RUN uv venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install \
      "mcp[cli]>=1.6" \
      "qdrant-client>=1.12" \
      "fastembed>=0.4" \
      "onnxruntime<1.24"

COPY kb/__init__.py kb/config.py kb/embed.py /build/kb/
COPY kb/adapters/ /build/kb/adapters/
COPY kb/mcp_retrieval/ /build/kb/mcp_retrieval/

ENV FASTEMBED_CACHE_PATH=/opt/fastembed \
    HOME=/tmp \
    PYTHONPATH=/build
RUN mkdir -p /opt/fastembed \
 && python -c "from fastembed import TextEmbedding; TextEmbedding(model_name='BAAI/bge-small-en-v1.5')"

FROM python:3.12-slim-bookworm AS runtime

RUN apt-get update \
 && apt-get install -y --no-install-recommends libgomp1 \
 && rm -rf /var/lib/apt/lists/* \
 && groupadd --gid 1000 mcp \
 && useradd --uid 1000 --gid mcp --create-home --home-dir /home/mcp mcp

# Ownership via COPY --chown avoids a recursive chown/chmod metadata layer that
# stalls Colima's containerd unpack on large onnxruntime/fastembed trees.
# /opt/venv stays root-owned; pip installs are world-readable (a+rX) so uid 1000 works.
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder --chown=1000:1000 /build/kb /app/kb
COPY --from=builder --chown=1000:1000 /opt/fastembed /opt/fastembed

ENV PATH="/opt/venv/bin:$PATH" \
    PYTHONPATH=/app \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    HOME=/home/mcp \
    FASTEMBED_CACHE_PATH=/opt/fastembed \
    QDRANT_NETWORK=internal

WORKDIR /app
USER 1000:1000

# stdio by default, override with --transport streamable-http for HTTP.
ENTRYPOINT ["python", "-m", "kb.mcp_retrieval"]
CMD []
