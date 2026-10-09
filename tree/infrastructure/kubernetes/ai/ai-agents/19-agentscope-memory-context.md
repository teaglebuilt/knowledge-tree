---
title: AgentScope Memory Management and Context Engineering (domain-14-ai-ml-infra)
description: 'title: AgentScope Memory Management and Context Engineering'
summary: 'title: AgentScope Memory Management and Context Engineering'
category: general
tags:
- ai
- ai-agent
- etcd
- redis
- mysql
- postgresql
- gateway
- llm
- rag
- agent
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 25min
intent_queries:
- What is AgentScope Memory Management and Context Engineering
- How does AgentScope Memory Management and Context Engineering work
- Best practices for AgentScope Memory Management and Context Engineering in Kubernetes 14 ai ml infra
trigger_keywords:
- AgentScope
- What is Memory Management and Context Engineering
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- etcd-basics
- redis-basics
- mysql-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/19-agentscope-memory-context.md
---

> **Production Environment Security Reminders**
>
> Commands included in this document are executable directly. Before executing, please confirm: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




title: AgentScope Memory Management and Context Engineering
description: '# AgentScope Memory Management and Context Engineering'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- [[etcd|etcd]]
- redis
- mysql
- postgresql
- gateway
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- Architect
- SRE
estimated_read_time: 5min
intent_queries:
- What is AgentScope Memory Management and Context Engineering
- How does AgentScope Memory Management and Context Engineering work
trigger_keywords:
- AgentScope
- Memory Management and Context Engineering
- ai
- agent
authors:
- name: Dillan Teagle
  role: contributor
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
---

# AgentScope Memory Management and Context Engineering

> **Document Type**: Memory Management Topic | **Last Updated**: 2026-03 | **Keywords**: AgentScope, Memory, Memory Management, InMemoryMemory, AsyncSQLAlchemyMemory, RedisMemory, Long-Term Memory, Mem0, ReMe, Session, JSONSession, State Persistence, Token Management, Context Window, Memory Compression, CompressionConfig, marks

---

## Overview

Memories are the foundation for Agent to achieve **consistent multi-turn dialogues** and **cross-session knowledge accumulation**. AgentScope provides a flexible memory management system: three built-in memory backends (InMemoryMemory, AsyncSQLAlchemyMemory, RedisMemory) for dialogue history within a session, long-term memory (Mem0, ReMe) for cross-session knowledge accumulation, and JSONSession for state persistence in production environments.

This document comprehensively explains the complete solution for AgentScope's memory management, starting from the basic InMemoryMemory to production-level persistence and long-term memory.

---

## 1. Memory Architecture Overview

```
AgentScope Memory Architecture
│
├── Short-Term Memory
│   ├── InMemoryMemory       → Memory stored in memory, lost when process exits, used for development and debugging
│   ├── AsyncSQLAlchemyMemory→ Persistent storage using SQL (SQLite/PostgreSQL/MySQL)
│   └── RedisMemory          → Persistent storage using Redis, suitable for distributed scenarios
│
├── Long-Term Memory
│   ├── Mem0LongTermMemory
│   │   └── Vector-based long-term memory based on Mem0
│   └── ReMePersonalLongTermMemory
│       └── Personalized long-term memory based on ReMe
│
│   Pattern:
│   ├── agent_control  → The intelligent body manages itself through tools
│   ├── static_control → The framework automatically reads and writes before and after replies
│   └── both           → Activates both above modes simultaneously
│
├── Message Markers
│   └── String tag system, used for message classification/filtering/deletion
│
├── Memory Compression
│   └── Built into ReActAgent, automatically compresses LLM summaries
│
├── Session Management
│   └── JSONSession → File persistence
│
└── State Management
    ├── state_dict()        → Export state snapshot (synchronous)
    └── load_state_dict()   → recover state (synchronous)
```

---

## 2. Three Memory Backends

AgentScope provides three built-in memory implementations, all implementing the same `Memory` interface:

| Memory Type | Storage Backend | Persistence | Applicable Scenarios |
|---------|---------|--------|--------|
| `InMemoryMemory` | Python Memory | No (lost upon process restart) | Development debugging, short dialogues |
| `AsyncSQLAlchemyMemory` | SQLite/PostgreSQL/MySQL | Yes | Production single-machine/single-database |
| `RedisMemory` | Redis | Yes | Production distributed/high-performance |

## 2.1 InMemoryMemory —— Basic Usage

```python
from agentscope.memory import InMemoryMemory
from agentscope.message import Msg

# Create a memory instance
memory = InMemoryMemory()

# Add a message
await memory.add(Msg("user", "user", "user"))
await memory.add(Msg("assistant", "I will check the logs...", "assistant"))
await memory.add(Msg("user", "What is the reason for container startup failure?", "user"))

# Get all memories
messages = await memory.get_memory()
# Return: [Msg("user", ...), Msg("assistant", ...), Msg("user", ...)]

# Get the number of memories
count = len(messages)
```

## 2.2 AsyncSQLAlchemyMemory —— SQL Persistence

```python
from agentscope.memory import AsyncSQLAlchemyMemory

# SQLite backend (single machine, zero configuration)
memory = AsyncSQLAlchemyMemory(
    url="sqlite+aiosqlite:///./agent_memory.db",
)

# PostgreSQL backend (production recommendation)
memory = AsyncSQLAlchemyMemory(
    url="postgresql+asyncpg://user:pass@db-host:5432/agent_db",
    # Connection pool configuration (required for production environments)
    pool_size=10,
    max_overflow=20,
)

# Usage is identical to InMemoryMemory
await memory.add(Msg("user", "How do I handle Pod Pending?", "user"))
messages = await memory.get_memory()
```

> **Advantages**: Process restarts do not affect memory; support connection pooling; suitable for FastAPI etc. web services.

## 2.3 RedisMemory —— Distributed

```python
from agentscope.memory import RedisMemory

# Suitable for K8s multi-replica scenarios, multiple Agent instances share state
memory = RedisMemory(
    url="redis://redis-host:6379/0",
)

# Usage is identical to InMemoryMemory
await memory.add(Msg("user", "etcd leader frequently switches", "user"))
```

## 2.4 Using in Agent

```python
from agentscope.agent import ReActAgent
from agentscope.memory import InMemoryMemory

agent = ReActAgent(
    name="Expert",
    memory=InMemoryMemory(),  # inject short-term memory
    ...
)

# Agent automatically manages memories:
# 1. Receive a message → memory.add(input_msg)
# 2. Generate a response → memory.add(response_msg)
# 3. For inference next time → memory.get_memory() to get history as context
```

## 2.5 Message Marking System (Marks)

AgentScope's memory supports **marks** (string tags) to categorize, filter, and batch delete messages:

```python
from agentscope.memory import InMemoryMemory
from agentscope.message import Msg

memory = InMemoryMemory()

# Add a message with a tag
await memory.add(Msg("user", "What is the cluster status?", "user"), marks="diagnosis")
await memory.add(Msg("system", "Hint: Check the logs", "system"), marks="hint")
await memory.add(Msg("assistant", "Check completed", "assistant"), marks="diagnosis")

# Search messages by tag
diag_msgs = await memory.get_memory(marks="diagnosis")
# Return: [User question, Assistant reply]

# Delete messages by tag
await memory.delete(marks="hint")
# All messages tagged "hint" are deleted
```

```
Marks common usage
│
├── "hint"         → temporary hint, delete after use
├── "diagnosis"    → diagnostic process message, can be retrieved by task
├── "tool_result"  → tool execution result, can be deleted preferentially when compressed
└── "summary"      → summary message generated during compression
```

## 2.6 State Management

```python
memory = InMemoryMemory()
await memory.add(Msg("user", "hello", "user"))

# Export State (Synchronous API, serializable as JSON)
state = memory.state_dict()
# state contains all stored messages

# Create a new instance and restore state
new_memory = InMemoryMemory()
new_memory.load_state_dict(state)

# new_memory now has the same conversation history
messages = await new_memory.get_memory()
```

---

## 3. Long-Term Memory

## 3.1 Design Philosophy

AgentScope does not strictly differentiate between short-term and long-term memory functions—everything is driven by demand. Long-term memory offers two implementations and three operational modes:

**Implementation**:

| Implementation | Description | Applicable Scenarios |
|------|------|--------|
| `Mem0LongTermMemory` | Vector-based long-term memory leveraging Mem0 | General knowledge accumulation, fact retrieval |
| `ReMePersonalLongTermMemory` | Personalized long-term memory using ReMe | User preferences, personalized services |

**Running Mode**:

| Mode | Manager | Applicable Scenarios |
|------|--------|--------|
| `agent_control` | Autonomous decision-making by the agent for reading and writing | Complex reasoning scenarios, agent-driven retrieval |
| `static_control` | Automatic reading and writing by the framework before and after `reply` | Simple scenarios, automated knowledge enhancement |
| `both` | Both modes activated simultaneously | Maximum flexibility |

## 3.2 Mem0LongTermMemory

```python
from agentscope.memory import Mem0LongTermMemory
from agentscope.agent import ReActAgent

# Create Mem0 Long-Term Memory
long_term = Mem0LongTermMemory(
    user_id="ops-engineer-001",
    # Mem0 configuration (vector storage, LLM extraction, etc.)
    mem0_config={
        "llm": {
            "provider": "openai",
            "config": {"model": "gpt-4o-mini"},
        },
    },
)

agent = ReActAgent(
    name="K8s-Expert",
    long_term_memory=long_term,
    long_term_memory_mode="agent_control",
    ...
)
```

## 3.3 agent_control Mode

Agents manage their long-term memory through utility functions—deciding when to save important information and when to retrieve historical knowledge.

```python
from agentscope.agent import ReActAgent

agent = ReActAgent(
    name="K8s-Expert",
    long_term_memory=long_term_memory_instance,
    long_term_memory_mode="agent_control",
    # Intelligent experience automatically acquires tools for memory management:
    # - Save information to long-term memory
    # - Retrieve information from long-term memory
    ...
)
```

**Workflow**:

```
You: "Previously you helped me diagnose the issue with etcd, what was the reason?"
                    │
Agent inference: Need to retrieve long-term memory about etcd diagnosis history
                    │
Agent call: recall_from_long_term_memory("etcd diagnosis")
                    │
long-term memory return: "2026-03-10 Diagnosis: frequent leader switch of etcd cluster"
              Root cause is insufficient disk IOPS, recommend using SSD
                    │
Agent reply: "Last etcd's problem was insufficient disk IOPS causing frequent leader switching..."
```

## 3.4 static_control Mode

At the beginning/end of each `reply` call, the framework automatically handles long-term memory:

```
static_control workflow:
│
├── reply Begin before
│   └── automatically retrieve relevant historical information from long-term memory for current message
│       → inject into context of Agent
│
├── Agent inference and action
│
└── reply End after
    └── automatically save key information of this conversation into long-term memory
```

```python
agent = ReActAgent(
    name="K8s-Expert",
    long_term_memory=long_term_memory_instance,
    long_term_memory_mode="static_control",
    ...
)
```

---

## 4. Memory Compression

## 4.1 Why Compression is Needed

As conversations grow, the content of the memory expands leading to:

```
Memory inflation problem
│
├── 1. Token limit exceeded    → exceed model context window
├── 2. Cost increases      → each LLM call consumes more tokens
├── 3. Reasoning quality drops → too much irrelevant information interferes with reasoning
└── 4. Delay increases      → longer prompts lead to slower responses
```

## 4.2 AgentScope Built-in CompressionConfig

AgentScope's `ReActAgent` includes built-in memory compression functionality, configured via `CompressionConfig`:

```python
from agentscope.agent import ReActAgent
from agentscope.memory import InMemoryMemory, CompressionConfig

agent = ReActAgent(
    name="K8s-Expert",
    memory=InMemoryMemory(),
    compression_config=CompressionConfig(
        trigger_threshold=50,    # 消息数超过 50 时触发压缩
        keep_recent=10,          # 保留最近 10 条原始消息
        # Customizable summary Schema (optional)
        # summary_schema=MySummarySchema,
    ),
    ...
)
```

**Compression Process**:

```
CompressionConfig workflow
│
├── 1. Trigger conditions detected
│      Current message count > trigger_threshold (50)
│
├── 2. Messages separated
│      Old messages = messages[:-keep_recent]  → to compress
│      New messages = messages[-keep_recent:]   → to keep
│
├── 3. LLM summary
│      Compress old messages into concise summaries through LLM
│
└── 4. Replace memory
       Memory = [summary messages] + new messages
```

**Compression Strategy**:

```
Compression strategy for memory
│
├── Truncation by window (simplest)
│   Keep system messages + recent N messages
│   Pros: Simple and fast, zero cost
│   Cons: Lose early context
│
├── LLM Compression (CompressionConfig)
│   Compress old messages using LLM to create a summary
│   advantages: retain key information
│   Shortcoming: additional LLM call cost
│
└── Hybrid Strategy (Recommended)
    retain system messages + old message summary + last N raw messages
    Advantages: balance information retention and Token consumption
```

> **Note**:`CompressionConfig` is a built-in compression scheme within AgentScope, no custom compression class required. For more granular control, use the `summary_schema` parameter to customize the summary format.

## 4.3 Manual Implementation of Compression Strategies

```python
from agentscope.message import Msg


class CompressedMemory:
    """Memory manager with compression features"""

    def __init__(
        self,
        model,
        max_messages: int = 50,
        keep_recent: int = 10,
    ):
        self.model = model
        self.max_messages = max_messages
        self.keep_recent = keep_recent
        self.messages: list[Msg] = []
        self.summary: str = ""

    async def add(self, msg: Msg) -> None:
        self.messages.append(msg)

        # Trigger compression when threshold is exceeded
        if len(self.messages) > self.max_messages:
            await self._compress()

    async def _compress(self) -> None:
        """Compress old messages into a summary"""
        old_messages = self.messages[:-self.keep_recent]
        recent_messages = self.messages[-self.keep_recent:]

        # Generate a summary using an LLM
        compress_prompt = f"""请将以下对话历史压缩为简洁的摘要，保留关键信息和决策:

{self._format_messages(old_messages)}

当前已有摘要: {self.summary}

请输出更新后的摘要（200字以内）:"""

        response = await self.model(compress_prompt)
        self.summary = response.content

        # Retain recent messages
        self.messages = recent_messages

    async def get_context(self) -> list[Msg]:
        """Retrieve full context (summary + recent messages)"""
        context = []
        if self.summary:
            context.append(Msg(
                "system",
                f"[Conversation Summary]: {self.summary}",
                "system",
            ))
        context.extend(self.messages)
        return context

    def _format_messages(self, messages: list[Msg]) -> str:
        return "\n".join(
            f"{m.name}: {m.content}" for m in messages
        )
```

---

## 5. Session Management

## 5.1 Why Session Management Is Needed

```
No Session (development stage):
  Agent starts → conversation → process exits → all memory lost

With Session (production environment):
  Agent starts → conversation → automatic state saving
       ↓
  Agent restarts → restore state from persistent storage → continue conversation
```

## 5.2 JSONSession(File Persistence)

AgentScope provides `JSONSession` as a built-in session solution, based on file system persistence:

```python
from agentscope.session import JSONSession
from agentscope.agent import ReActAgent

# Create file-persistent Session
session = JSONSession(save_dir="./agent_sessions")

# Save Agent state
session.save_session_state(
    session_id="session-001",
    user_id="user-alice",
    agent=agent,
)

# Restore Agent state
session.load_session_state(
    session_id="session-001",
    user_id="user-alice",
    agent=agent,
)
```

## 5.3 Production Environment Session Selection

For distributed deployment in production environments, it is recommended to combine `AsyncSQLAlchemyMemory` as the memory backend with `JSONSession` for state persistence:

| Component | Development Environment | Production Environment (Single Machine) | Production Environment (Distributed) |
|------|---------|-------------|---------------|
| **Memory** | InMemoryMemory | AsyncSQLAlchemyMemory | RedisMemory |
| **Session** | None | JSONSession | JSONSession + Shared Storage |
| **Long-Term Memory** | None | Mem0LongTermMemory | Mem0LongTermMemory |

---

## 6. Token Management and Context Window

## 6.1 Token Calculation

AgentScope provides a Token calculation tool, used for monitoring and managing context window usage:

```python
from agentscope.token import count_tokens

# Calculate the number of Tokens in a message
token_count = count_tokens(
    messages=[
        {"role": "system", "content": "you are a K8s expert"},
        {"role": "user", "content": "How do I handle Pod Pending?"},
    ],
    model_name="qwen-max",
)
print(f"Current context: {token_count} tokens")
```

## 6.2 Context Window Management Strategy

```
Context Window Management
│
├── Mainstream Model Context Window
│   ├── qwen-max          128K tokens
│   ├── qwen-plus          32K tokens
│   ├── qwen-turbo        128K tokens
│   ├── gpt-4o            128K tokens
│   ├── gpt-4o-mini       128K tokens
│   └── claude-3.5-sonnet  200K tokens
│
├── Window Allocation Suggestions
│   ├── System Prompt:     5-10%
│   ├── Historical Summary: 10-20%
│   ├── Recent Conversation: 30-40%
│   ├── Tool Description:  10-15%
│   └── Output Reserve:     20-30%
│
└── Handle overflow
    ├── Truncate oldest message automatically
    ├── Trigger memory compression
    └── Downgrade to shorter prompt
```

## 6.3 Practice: Context Window Manager

```python
class ContextWindowManager:
    """Context manager for window management"""

    def __init__(
        self,
        model_name: str = "qwen-max",
        max_tokens: int = 128000,
        output_reserve_ratio: float = 0.25,
    ):
        self.model_name = model_name
        self.max_tokens = max_tokens
        self.output_reserve = int(max_tokens * output_reserve_ratio)
        self.available_tokens = max_tokens - self.output_reserve

    def should_compress(self, messages: list[dict]) -> bool:
        """Determine if compression is needed"""
        current = count_tokens(messages, self.model_name)
        return current > self.available_tokens * 0.8  # 80% 阈值

    def trim_messages(self, messages: list[dict]) -> list[dict]:
        """Truncate messages over the limit"""
        # Retain system messages
        system_msgs = [m for m in messages if m.get("role") == "system"]
        other_msgs = [m for m in messages if m.get("role") != "system"]

        system_tokens = count_tokens(system_msgs, self.model_name)
        budget = self.available_tokens - system_tokens

        # Retain from the most recent message
        kept = []
        used = 0
        for msg in reversed(other_msgs):
            msg_tokens = count_tokens([msg], self.model_name)
            if used + msg_tokens <= budget:
                kept.insert(0, msg)
                used += msg_tokens
            else:
                break

        return system_msgs + kept
```

---

## 7. State Persistence Deep Dive

## 7.1 Nested State Management in AgentScope

```
Agent.state_dict()
│
├── agent itself status
│   ├── name
│   └── Other custom fields
│
├── memory.state_dict()
│   └── All stored messages
│
├── toolkit.state_dict()
│   └── Long-term memory content and index
│
└── long_term_memory.state_dict()
    └── Long-term memory content and index
```

## 7.2 Complete State Management Workflow

```python
import json
from agentscope.agent import ReActAgent


async def save_agent_state(agent: ReActAgent, filepath: str) -> None:
    """Save the complete agent state to a file"""
    state = agent.state_dict()  # 同步 API
    with open(filepath, "w") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
    print(f"Agent state saved to {filepath}")


async def load_agent_state(agent: ReActAgent, filepath: str) -> None:
    """Restore the agent state from a file"""
    with open(filepath, "r") as f:
        state = json.load(f)
    agent.load_state_dict(state)  # 同步 API
    print(f"Agent state restored from {filepath}")


# Usage Example
agent = ReActAgent(name="K8s-Expert", ...)

# ... several rounds of conversation ...

# Save state
await save_agent_state(agent, "/tmp/agent_state.json")

# Create a new Agent and restore the state
new_agent = ReActAgent(name="K8s-Expert", ...)
await load_agent_state(new_agent, "/tmp/agent_state.json")

# The new_agent now has the previous conversation memory and tool state
```

> **Note**: `state_dict()` and `load_state_dict()` are **synchronous** APIs that do not require `await`. This differs from the asynchronous methods like `add()` and `get_memory()` provided by Memory.

---

## 8. Production Environment Memory Architecture Design

## 8.1 Recommended Architecture

```
Production environment memory architecture
│
├── Request entry
│   └── API Gateway → AgentApp
│
├── State recovery
│   └── JSONSession.load_session_state(session_id, user_id, agent)
│
├── Agent processing
│   ├── Short-term memory (AsyncSQLAlchemyMemory) — Current session
│   └── Long-term memory (Mem0LongTermMemory) — Cross-session knowledge
│
├── State saving
│   └── JSONSession.save_session_state(session_id, user_id, agent)
│
└── Storage layer
    ├── PostgreSQL/Redis (memory persistence)
    │   ├── AsyncSQLAlchemyMemory connection pool
    │   └── Supports multi-replica sharing
    └── Vector database (long-term memory retrieval)
        ├── Semantic similarity retrieval
        └── Knowledge graph indexing
```

## 8.2 FastAPI + AsyncSQLAlchemyMemory Production Example

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI
from agentscope.agent import ReActAgent
from agentscope.memory import AsyncSQLAlchemyMemory, CompressionConfig
from agentscope.session import JSONSession
import os


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Start: Initialize the connection pool
    app.state.session = JSONSession(save_dir="./sessions")
    print("Agent service started")
    yield
    print("Agent service stopped")


app = FastAPI(lifespan=lifespan)


@app.post("/chat")
async def chat(session_id: str, user_id: str, message: str):
    # Use AsyncSQLAlchemyMemory as persistent memory
    memory = AsyncSQLAlchemyMemory(
        url=os.getenv("DB_URL", "sqlite+aiosqlite:///./memory.db"),
        pool_size=10,
    )

    agent = ReActAgent(
        name="K8s-Expert",
        memory=memory,
        compression_config=CompressionConfig(
            trigger_threshold=50,
            keep_recent=10,
        ),
        ...
    )

    # Restore session state
    app.state.session.load_session_state(
        session_id=session_id,
        user_id=user_id,
        agent=agent,
    )

    # Handle request
    msg = Msg("user", message, "user")
    response = await agent(msg)

    # Save session state
    app.state.session.save_session_state(
        session_id=session_id,
        user_id=user_id,
        agent=agent,
    )

    return {"response": response.get_text_content()}
```

---

## 9. Best Practices and Anti-patterns

## Best Practices

- **Use InMemoryMemory for development and AsyncSQLAlchemyMemory/RedisMemory in production**: Use InMemoryMemory during development for debugging, switch to persistent memory before deployment.
- **Use CompressionConfig**: For long dialogue scenarios (>30 turns), enable built-in compression without custom compression classes.
- **Utilize the Marking System**: Categorize messages for easier task retrieval and compression prioritization.
- **Persist Agent State Periodically**: Save state after each reply to prevent loss in case of anomalies.
- **Use agent_control for Long-Term Memory**: Let agents decide when to save/retrieve, more flexible than static control.

## Anti-patterns

- **Use AsyncSQLAlchemyMemory/RedisMemory in Production**: All conversations lost on process restart — use AsyncSQLAlchemyMemory or RedisMemory in production.
- **Do not manage context windows**: Exceeding token limits due to growing conversation — use CompressionConfig.
- **Store messages in long-term memory**: Too much noise reduces retrieval quality.
- **Ignore serialization of state_dict**: Includes non-serializable objects causing save failures.
- **Use await with state_dict/load_state_dict**: These methods are synchronous and do not require `await`.

---

## Related Documentation

| Document | Related Content |
|------|---------|
| [17 - Core Concepts](./17-agentscope-core-concepts.md) | The position of Memory in core abstractions |
| [20 - Multi-Agent Orchestration](./20-agentscope-multi-agent-orchestration.md) | Shared memory in multi-agent scenarios |
| [22 - Production Deployment](./deployment.md|22-agentscope-production-deployment]].md) | Production deployment of Session + Runtime |
| [07 - Memory Management and Context Windows](./07-memory-context-management.md) | General theories and strategies for memory management |

---

*This document is original content for the kudig-database project's 02-ai-agents topic.*

---

## Related Obsidian Documentation

- 02-ai-agents KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|[[AI Agent Engineering Topic|AI Agent Engineering Topic]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|AI Agent Fundamentals and Core Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|LLM Foundation Model Selection and Evaluation]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Deep Comparison of Main Agent Frameworks]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|Deep Guide to Retrieval-Augmented Generation (RAG)]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Design Guidelines for Tool Usage and Function Calling]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Deep Architecture for Multi-Agent Orchestration and Collaboration]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Engineering Memory Management and Context Window]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Deep Architecture for Agent Evaluation and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]

## Related

- 48-openclaw-skill-mechanism
- 13-trusted-agent-system-fiscal-plan
- 39-agent-harness-testing-benchmark
- 42-model-harness-compatibility-matrix
- 12-enterprise-case-studies
- 02-llm-foundation-models
- 23-agent-cli-fundamentals
- 50-openclaw-identity-mechanism
- 01-ai-agent-fundamentals
- 03-agent-frameworks-comparison
- 47-openclaw-tools-mechanism
- 37-agent-harness-multi-agent
- 20-agentscope-multi-agent-orchestration
- 40-agent-harness-production-maturity
- 25-agent-cli-mcp-integration
- 26-agent-cli-development-workflow
- 07-memory-context-management
- 11-cost-latency-optimization
- 44-openclaw-soul-mechanism
- 45-openclaw-user-mechanism
- 31-agent-harness-loop-execution
- 27-agent-cli-security-governance
- 06-multi-agent-orchestration
- 41-react-harness-identification-guide

## See Also

- 17-agentscope-core-concepts
- 18-agentscope-tool-system
- 20-agentscope-multi-agent-orchestration
- 21-agentscope-advanced-features


<!-- risk-assessed -->
