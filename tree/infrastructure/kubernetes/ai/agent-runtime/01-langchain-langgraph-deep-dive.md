---
title: LangChain/LangGraph In-Depth Guide
description: 'A comprehensive deep-dive into LangChain core architecture and the LangGraph state graph engine, covering the four major components Chain/Agent/Tool/Memory, StateGraph state machine, persistent checkpoints, Human-in-the-Loop, Streaming, and K8s production deployment'
summary: 'A comprehensive deep-dive into LangChain core architecture and the LangGraph state graph engine'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- langchain
- langgraph
- state-graph
tier: supporting
created: '2026-07-02'
last_updated: 2026-07
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Platform Engineers
- Architects
estimated_read_time: 20min
intent_queries:
- What is the LangChain/LangGraph In-Depth Guide
- How to use the LangChain/LangGraph In-Depth Guide
- LangChain core architecture
- LangGraph StateGraph state graph
trigger_keywords:
- langchain
- langgraph
- state-graph
- checkpointer
- human-in-the-loop
prerequisites:
- llm-basics
- python-basics
- kubectl-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: Dillan Teagle
  role: contributor
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/01-langchain-langgraph-deep-dive.md
---
> **Production Environment Security Notice**
>
> This document contains directly executable operations commands. Before executing, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have validated in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state, but is generally reversible), 🟢 Low risk / Read-only (information gathering, no side effects).


# LangChain/LangGraph In-Depth Guide

## 1. LangChain Core Architecture

### 1.1 Overall Design Philosophy

LangChain adopts a layered abstraction design, decomposing LLM applications into composable, standardized components. The core concept is **Chain Composition** — each component does one thing, and complex applications are built by connecting them through pipelines.

```
┌─────────────────────────────────────────────────┐
│                  Application Layer               │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐   │
│  │  Chain   │  │  Agent   │  │  Retrieval   │   │
│  └────┬─────┘  └────┬─────┘  └──────┬───────┘   │
│       │              │               │           │
│  ┌────┴──────────────┴───────────────┴───────┐   │
│  │           LCEL (LangChain Expression)     │   │
│  └────┬──────────┬──────────┬────────────────┘   │
│       │          │          │                    │
│  ┌────┴───┐ ┌────┴───┐ ┌───┴────┐               │
│  │ Model  │ │  Tool  │ │ Memory │               │
│  └────────┘ └────────┘ └────────┘               │
└─────────────────────────────────────────────────┘
```

### 1.2 LCEL — LangChain Expression Language

LCEL is the core orchestration language for LangChain 0.2+, implementing declarative pipelines based on the Runnable protocol:

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

# LCEL pipeline: Prompt → Model → Parser
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a Kubernetes expert."),
    ("human", "{question}")
])
model = ChatOpenAI(model="gpt-4o", temperature=0)
parser = StrOutputParser()

# Chain together using the | operator
chain = prompt | model | parser

# Synchronous invocation
result = chain.invoke({"question": "Explain Pod QoS levels"})

# Batch invocation
results = chain.batch([
    {"question": "What is a DaemonSet?"},
    {"question": "What is a StatefulSet?"}
])
```

**Runnable Protocol Core Methods:**

| Method | Purpose | Typical Use Case |
|--------|---------|-----------------|
| `invoke` | Single invocation | Synchronous request-response |
| `batch` | Batch invocation | Parallel processing of multiple inputs |
| `stream` | Streaming output | Real-time UI feedback |
| `ainvoke` | Async invocation | High-concurrency services |
| `astream` | Async streaming | Async real-time output |

### 1.3 Chain Components

Chain is the fundamental orchestration unit in LangChain. LCEL replaces the legacy `LLMChain`, `SequentialChain`, and other deprecated classes:

```python
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

# Retrieval-Augmented Generation (RAG) pipeline
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {
        "context": retriever | RunnableLambda(format_docs),
        "question": RunnablePassthrough()
    }
    | prompt
    | model
    | parser
)

# Chain with fallback
from langchain_core.runnables import RunnableWithFallbacks

chain_with_fallback = model.with_fallbacks([
    ChatOpenAI(model="gpt-4o-mini"),  # Fall back to a smaller model
])
```

### 1.4 Agent Architecture

An Agent is an autonomous decision-making unit with tool-calling capabilities. LangChain 0.3+ recommends using LangGraph to build Agents, but `create_react_agent` provides a convenient wrapper:

```python
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool

@tool
def get_pod_status(namespace: str, pod_name: str) -> str:
    """Query the running status of the specified Pod."""
    # In actual implementation, call kubectl or the K8s API
    import subprocess
    result = subprocess.run(
        ["kubectl", "get", "pod", pod_name, "-n", namespace, "-o", "json"],
        capture_output=True, text=True
    )
    return result.stdout

@tool
def get_pod_logs(namespace: str, pod_name: str, tail_lines: int = 100) -> str:
    """Get recent logs from a Pod."""
    import subprocess
    result = subprocess.run(
        ["kubectl", "logs", pod_name, "-n", namespace,
         f"--tail={tail_lines}"],
        capture_output=True, text=True
    )
    return result.stdout

# Create a ReAct Agent
agent = create_react_agent(
    model=ChatOpenAI(model="gpt-4o"),
    tools=[get_pod_status, get_pod_logs],
    state_modifier="You are a KuDig K8s diagnostics expert. Use tools to query cluster status."
)

# Execute
result = agent.invoke({
    "messages": [("user", "Check the status of nginx-pod in the default namespace")]
})
```

### 1.5 Tool Abstraction

Tools are the standardized interface through which Agents interact with the external world:

```python
from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

# Define input schema using Pydantic
class KubectlInput(BaseModel):
    command: str = Field(description="kubectl subcommand, e.g. get/describe/logs")
    namespace: str = Field(default="default", description="K8s namespace")
    resource: str = Field(description="Resource type, e.g. pod/service/deployment")

def execute_kubectl(command: str, namespace: str, resource: str) -> str:
    """Execute a kubectl command."""
    import subprocess
    cmd = ["kubectl", command, resource, "-n", namespace]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        return f"Command failed: {result.stderr}"
    return result.stdout

kubectl_tool = StructuredTool.from_function(
    func=execute_kubectl,
    name="kubectl",
    description="Execute kubectl commands to query K8s cluster resources",
    args_schema=KubectlInput,
    return_direct=False  # Set to True to return directly to the user
)
```

### 1.6 Memory System

Memory maintains conversational context across turns:

```python
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# In-memory storage (use Redis/Postgres in production)
store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = ChatMessageHistory()
    return store[session_id]

# Conversation chain with history
with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

# Specify session_id on each call
config = {"configurable": {"session_id": "user-123"}}
result = with_history.invoke({"question": "What Pod was I just looking at?"}, config=config)
```

**Production-Grade Memory Backend Comparison:**

| Backend | Persistence | Use Case | LangChain Module |
|---------|------------|---------|-----------------|
| In-Memory | No | Development & testing | `ChatMessageHistory` |
| Redis | Yes | High-concurrency sessions | `RedisChatMessageHistory` |
| PostgreSQL | Yes | Structured queries | `PostgresChatMessageHistory` |
| MongoDB | Yes | Flexible document storage | `MongoDBChatMessageHistory` |

---
## 2. LangGraph State Graph Engine

### 2.1 Why LangGraph Is Needed

LangChain's Chain is a linear pipeline that cannot express complex control flows such as branching, loops, and parallelism. LangGraph models LLM applications as **Finite State Machines (FSM)**, where each node is a processing step and edges define state transitions.

```
┌──────────┐   Conditional Edge   ┌──────────┐
│  Start   │──────────────────→   │  LLM     │
└──────────┘                      └────┬─────┘
                                       │
                           ┌───────────┼───────────┐
                           ↓           ↓           ↓
                     ┌─────────┐ ┌─────────┐ ┌─────────┐
                     │ Tool A  │ │ Tool B  │ │ Tool C  │
                     └────┬────┘ └────┬────┘ └────┬────┘
                          │           │           │
                          └───────────┼───────────┘
                                      ↓
                                ┌──────────┐
                                │   End    │
                                └──────────┘
```

### 2.2 StateGraph Basics

```python
from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
import operator

# Define state schema
class DiagnosisState(TypedDict):
    # messages accumulate using the add operator
    messages: Annotated[list, operator.add]
    # diagnosis phase
    phase: str
    # collected evidence
    evidence: Annotated[list, operator.add]
    # diagnosis conclusion
    conclusion: str

# Create state graph
graph = StateGraph(DiagnosisState)

# Define node functions
def collect_info(state: DiagnosisState) -> dict:
    """Information collection node."""
    last_msg = state["messages"][-1]
    # Call LLM to analyze what information is needed
    response = llm.invoke([
        SystemMessage(content="Analyze the current issue and list the information that needs to be collected."),
        *state["messages"]
    ])
    return {
        "messages": [response],
        "phase": "collecting"
    }

def analyze_root_cause(state: DiagnosisState) -> dict:
    """Root cause analysis node."""
    evidence_summary = "\n".join(state["evidence"])
    response = llm.invoke([
        SystemMessage(content=f"Analyze the root cause based on the following evidence:\n{evidence_summary}"),
        *state["messages"]
    ])
    return {
        "messages": [response],
        "phase": "analyzing",
        "conclusion": response.content
    }

def generate_fix(state: DiagnosisState) -> dict:
    """Generate fix plan node."""
    response = llm.invoke([
        SystemMessage(content=f"Root cause: {state['conclusion']}. Generate a fix plan."),
        *state["messages"]
    ])
    return {"messages": [response], "phase": "fixing"}

# Add nodes
graph.add_node("collect_info", collect_info)
graph.add_node("analyze", analyze_root_cause)
graph.add_node("fix", generate_fix)

# Set entry point
graph.set_entry_point("collect_info")

# Add edges
graph.add_edge("collect_info", "analyze")
graph.add_edge("analyze", "fix")
graph.add_edge("fix", END)

# Compile
diagnosis_app = graph.compile()
```

### 2.3 Conditional Routing

Conditional edges dynamically determine the next step based on state:

```python
from langgraph.graph import END

def should_continue(state: DiagnosisState) -> str:
    """Conditional routing: decide whether more information is needed."""
    last_message = state["messages"][-1]

    # If the LLM indicates insufficient information, continue collecting
    if "need more information" in last_message.content:
        return "collect_info"

    # If a fix plan has been generated, proceed to review
    if state["phase"] == "fixing":
        return "review"

    # Default: continue analyzing
    return "analyze"

# Add conditional edge
graph.add_conditional_edges(
    "collect_info",        # source node
    should_continue,       # routing function
    {
        "collect_info": "collect_info",  # loop back to collect
        "analyze": "analyze",            # proceed to analysis
        "review": "review",              # proceed to review
    }
)
```

### 2.4 Persistent Checkpointer

The Checkpointer implements state snapshots, supporting breakpoint recovery, time travel, and Human-in-the-Loop:

```python
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.checkpoint.memory import MemorySaver

# In-memory (development)
checkpointer = MemorySaver()

# PostgreSQL (production)
checkpointer = PostgresSaver.from_conn_string(
    "postgresql://user:pass@postgres:5432/langgraph"
)

# Bind Checkpointer at compile time
app = graph.compile(checkpointer=checkpointer)

# Specify thread_id (session identifier) at execution time
config = {"configurable": {"thread_id": "diag-session-001"}}
result = app.invoke(
    {"messages": [("user", "Pod nginx-0 keeps CrashLooping")]},
    config=config
)

# Get checkpoint snapshot
snapshot = app.get_state(config)
print(f"Current phase: {snapshot.values['phase']}")
print(f"Message count: {len(snapshot.values['messages'])}")

# Time travel: rewind to a specific checkpoint
history = list(app.get_state_history(config))
for i, state in enumerate(history):
    print(f"  [{i}] step={state.metadata['step']}")

# Restore to a specific checkpoint
old_config = history[2].config
app.update_state(old_config, {"phase": "collecting"})
```

### 2.5 Human-in-the-Loop Pattern

Pause at critical decision points to wait for human confirmation:

```python
from langgraph.graph import StateGraph, END

graph = StateGraph(DiagnosisState)

# Use interrupt_before to pause before a node executes
app = graph.compile(
    checkpointer=checkpointer,
    interrupt_before=["fix"]  # pause before executing the fix
)

# Execution will pause before the fix node
config = {"configurable": {"thread_id": "diag-002"}}
result = app.invoke(
    {"messages": [("user", "Pod OOMKilled")]},
    config=config
)

# View current state and wait for human confirmation
snapshot = app.get_state(config)
print(f"Suggested fix plan: {snapshot.values.get('conclusion')}")

# Continue execution after human approval
user_approved = True
if user_approved:
    app.invoke(None, config=config)  # resume from breakpoint
else:
    # Modify state manually then continue
    app.update_state(config, {
        "conclusion": "Revised plan: first scale memory up to 512Mi",
    })
    app.invoke(None, config=config)
```

### 2.6 Streaming Support

LangGraph provides multiple streaming output modes:

```python
# Mode 1: streaming tokens (LLM output)
for event in app.stream(input_data, config=config, stream_mode="messages"):
    print(event.content, end="", flush=True)

# Mode 2: streaming state updates (node level)
for event in app.stream(input_data, config=config, stream_mode="updates"):
    for node, update in event.items():
        print(f"[{node}] update: {update}")

# Mode 3: mixed streaming
for event in app.stream(input_data, config=config, stream_mode=["updates", "messages"]):
    if isinstance(event, tuple):
        mode, data = event
        if mode == "updates":
            print(f"State update: {data}")
        elif mode == "messages":
            print(f"Token: {data.content}", end="")

# Mode 4: custom event stream
from langchain_core.callbacks import StreamingStdOutCallbackHandler

async for event in app.astream_events(input_data, config=config, version="v2"):
    kind = event["event"]
    if kind == "on_chat_model_stream":
        print(event["data"]["chunk"].content, end="")
    elif kind == "on_tool_start":
        print(f"\n[Calling tool] {event['name']}")
    elif kind == "on_tool_end":
        print(f"[Tool returned] {event['data'].content[:100]}...")
```

---
## 3. K8s Production Deployment

### 3.1 Dockerization

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl jq && \
    rm -rf /var/lib/apt/lists/*

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -Ls https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    chmod +x kubectl && mv kubectl /usr/local/bin/

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

# Non-root user
RUN useradd -m agent && chown -R agent:agent /app
USER agent

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```text
# requirements.txt
langchain==0.3.*
langgraph==0.3.*
langchain-openai==0.3.*
langgraph-checkpoint-postgres==2.0.*
psycopg[binary]==3.2.*
uvicorn[standard]==0.34.*
fastapi==0.115.*
```

### 3.2 Helm Chart

```yaml
# helm/langgraph-agent/values.yaml
replicaCount: 2

image:
  repository: registry.example.com/langgraph-agent
  tag: "1.0.0"
  pullPolicy: IfNotPresent

env:
  - name: OPENAI_API_KEY
    valueFrom:
      secretKeyRef:
        name: llm-secrets
        key: openai-api-key
  - name: POSTGRES_URL
    valueFrom:
      secretKeyRef:
        name: langgraph-db
        key: connection-string

resources:
  requests:
    cpu: "500m"
    memory: "512Mi"
  limits:
    cpu: "2000m"
    memory: "2Gi"

# Dedicated ServiceAccount (least privilege)
serviceAccount:
  create: true
  name: langgraph-agent
  annotations:
    # IRSA / Workload Identity binding
    eks.amazonaws.com/role-arn: arn:aws:iam::123456789:role/langgraph-agent

# RBAC: read-only Pod/Service/Event
rbac:
  create: true
  rules:
    - apiGroups: [""]
      resources: ["pods", "services", "events", "configmaps"]
      verbs: ["get", "list", "watch"]
    - apiGroups: ["apps"]
      resources: ["deployments", "replicasets"]
      verbs: ["get", "list", "watch"]

# HPA autoscaling
autoscaling:
  enabled: true
  minReplicas: 2
  maxReplicas: 10
  targetCPUUtilizationPercentage: 70
  targetMemoryUtilizationPercentage: 80

# Health checks
healthCheck:
  liveness:
    path: /healthz
    initialDelaySeconds: 15
    periodSeconds: 10
  readiness:
    path: /readyz
    initialDelaySeconds: 5
    periodSeconds: 5
```

### 3.3 FastAPI Service Wrapper

```python
# src/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langgraph.checkpoint.postgres import PostgresSaver
import uuid

app = FastAPI(title="LangGraph K8s Agent")

# Initialize Checkpointer
checkpointer = PostgresSaver.from_conn_string(
    os.environ["POSTGRES_URL"]
)

# Compile Agent
agent = build_diagnosis_agent(checkpointer)

class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None

class ChatResponse(BaseModel):
    reply: str
    session_id: str
    phase: str

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest):
    session_id = req.session_id or str(uuid.uuid4())
    config = {"configurable": {"thread_id": session_id}}

    try:
        result = await agent.ainvoke(
            {"messages": [("user", req.message)]},
            config=config
        )
        snapshot = agent.get_state(config)
        return ChatResponse(
            reply=result["messages"][-1].content,
            session_id=session_id,
            phase=snapshot.values.get("phase", "unknown")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/healthz")
async def healthz():
    return {"status": "ok"}

@app.get("/readyz")
async def readyz():
    # Check PostgreSQL connection
    try:
        checkpointer.conn.execute("SELECT 1")
        return {"status": "ready"}
    except Exception:
        raise HTTPException(status_code=503, detail="DB not ready")
```

---

## 4. Production Best Practices

### 4.1 Error Handling and Retries

```python
from langchain_core.runnables import RunnableRetry

# Automatic retry
chain_with_retry = model.with_retry(
    retry_if_exception_type=(TimeoutError, ConnectionError),
    wait_exponential_jitter=True,
    stop_after_attempt=3
)

# Chain with fallback
from langchain_core.runnables import RunnableWithFallbacks

resilient_chain = chain.with_fallbacks(
    [backup_chain],
    exceptions_to_handle=(RateLimitError,)
)
```

### 4.2 Observability

```python
# LangSmith tracing
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-key"
os.environ["LANGCHAIN_PROJECT"] = "kudig-k8s-agent"

# OpenTelemetry integration
from langchain_community.callbacks.tracers import OpenTelemetryTracer

# Custom callback
from langchain_core.callbacks import BaseCallbackHandler

class MetricsCallback(BaseCallbackHandler):
    def on_llm_end(self, response, **kwargs):
        tokens = response.llm_output.get("token_usage", {})
        # Push to Prometheus
        LLM_TOKENS.labels(model="gpt-4o").inc(tokens.get("total_tokens", 0))

    def on_tool_error(self, error, **kwargs):
        TOOL_ERRORS.labels(tool=kwargs.get("name", "unknown")).inc()
```

### 4.3 Security Considerations

| Risk | Mitigation |
|------|-----------|
| Prompt injection | Input validation + `RunnablePassthrough.with_types` type guards |
| Tool permissions | RBAC least privilege + Tool input schema validation |
| Code execution | Sandbox isolation (Docker/Kata) + timeout control |
| API key leakage | K8s Secret + External Secrets Operator |
| Output leakage | Output filtering + PII detection middleware |

### 4.4 Performance Optimization

```python
# 1. Parallel tool calls
from langgraph.prebuilt import ToolNode

tool_node = ToolNode(tools, handle_tool_errors=True)

# 2. Embedding cache
from langchain_community.cache import RedisCache
import langchain
langchain.llm_cache = RedisCache(redis.Redis(host="redis"))

# 3. Batch embedding
from langchain_openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
batch_vectors = embeddings.embed_documents(texts, chunk_size=100)

# 4. Streaming to reduce time-to-first-token
async for chunk in agent.astream(input_data, config=config):
    print(chunk, end="")
```

---
## 5. Summary & Selection Recommendations

| Feature | LangChain | LangGraph |
|------|-----------|-----------|
| Positioning | General-purpose LLM orchestration framework | Stateful graph agent engine |
| Control flow | Linear pipeline (LCEL) | State machine (branching / loops / parallel) |
| State management | Relies on Memory components | Native State + Checkpointer |
| Use cases | RAG, simple agents, tool chains | Complex agents, multi-step reasoning, human-in-the-loop |
| Learning curve | Low | Medium |
| Production maturity | High (v0.3 stable) | Medium-high (rapidly iterating) |

**Recommended selection path:**
- Simple RAG / tool calling → LangChain LCEL
- Complex agents / state persistence required → LangGraph
- Existing LangChain projects → Gradually migrate to LangGraph

---

## Related

- [[domain-14-ai-ml-infra/03-agent-runtime/02-llamaindex-data-agent|LlamaIndex Data Agent]]
- [[domain-14-ai-ml-infra/03-agent-runtime/07-agent-framework-selection-guide|Agent Framework Selection Decision Tree]]

## See Also

- [[domain-14-ai-ml-infra/03-agent-runtime/03-crewai-multi-agent-framework|CrewAI Multi-Agent Framework]]
- [[domain-14-ai-ml-infra/03-agent-runtime/06-semantic-kernel-enterprise|Semantic Kernel Enterprise Agent]]


<!-- risk-assessed -->
