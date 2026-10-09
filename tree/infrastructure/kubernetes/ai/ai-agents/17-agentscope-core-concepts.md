---
title: AgentScope Core Concepts and Fundamental Operations (domain-14-ai-ml-infra)
description: 'description: ''**Document Type**: Core Concepts Topic | **Last Updated**: 2026-03 | **Keywords**: AgentScope,
  Core Concepts, State,'
summary: 'description: ''**Document Type**: Core Concepts Topic | **Last Updated**: 2026-03 | **Keywords**: AgentScope,
  Core Concepts, State,'
category: general
tags:
- ai
- ai-agent
- redis
- mysql
- postgresql
- hpa
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
- What is AgentScope Core Concepts and Fundamental Operations
- How to do AgentScope Core Concepts and Fundamental Operations
- Best Practices for AgentScope 14 ai ml infra
trigger_keywords:
- AgentScope
- Core Concepts and Fundamental Operations
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- redis-basics
- mysql-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/17-agentscope-core-concepts.md
---

> **Production Environment Security Reminders**
>
> Commands included in this document are executable directly. Before executing, please confirm: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify the cluster state but can usually be rolled back), 🟢 Low Risk/Read-Only (information gathering with no side effects).




title: AgentScope Core Concepts and Basic Operations
description: '**Document Type**: Core Concepts Topic | **Last Updated**: 2026-03 | **Keywords**: AgentScope, Core Concepts, State, Message, Agent, Model, Formatter, Memory, ReActAgent, AgentBase, Custom Agent'
  Message, Agent, Model, Formatter, Memory, ReActAgent, AgentBase, Custom Agent'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- redis
- mysql
- postgresql
- hpa
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- Architect
- SRE
estimated_read_time: 5min
intent_queries:
- What is AgentScope Core Concepts and Basic Operations
- How to do AgentScope Core Concepts and Basic Operations
trigger_keywords:
- AgentScope
- Core Concepts and Basic Operations
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

# AgentScope Core Concepts and Basic Operations

> **Document Type**: Core Concepts Topic | **Last Updated**: 2026-03 | **Keywords**: AgentScope, Core Concepts, State, Message, Agent, Model, Formatter, Memory, ReActAgent, AgentBase, Custom Agent

---

## Overview

AgentScope abstracts the components required to build an Agent application into **four core modules**: message (Message), model (Model), memory (Memory), and tool (Tool). It unifies their management through a common state mechanism to facilitate subsequent tool systems, memory management, and multi-Agent orchestration.

---

## 1. Six Major Core Abstractions

```
AgentScope core abstraction
│
├── State(status)      → The runtime snapshot of all objects, supporting export/import
├── Message(message)    → Communication structure for intelligent bodies
├── Model(model)      → Model (LLM API unified interface encapsulation)
├── Formatter (formatting) → Message to LLM API format conversion layer
├── Memory (memory)     → Dialogue history and knowledge management
└── Tool(ool)       → Agent can call Python callable object
```

The relationships between these six concepts:

```
                    ┌─────────────┐
                    │    Agent    │
                    │  (Agent)   │
                    └──────┬──────┘
                           │ Combine usage
          ┌────────┬───────┼───────┬────────┐
          ▼        ▼       ▼       ▼        ▼
     ┌────────┐┌───────┐┌──────┐┌───────┐┌──────┐
     │ Model  ││Memory ││ Tool ││Format ││ State│
     │ model ││ memory ││ tool ││ formatting ││ status │
     └────────┘└───────┘└──────┘└───────┘└──────┘
          │        │       │       │        │
          └────────┴───────┴───────┴────────┘
                    Through Message interaction
```

---

## 2. State — State Management

## 2.1 Design Philosophy

AgentScope separates the initialization of objects from their state management. All stateful modules inherit from the `StateModule` base class, allowing:

- Exporting a snapshot of the current state
- Restoring to any saved state
- Implementing cross-session state persistence

## 2.2 StateModule Base Class

`StateModule` forms the foundation of AgentScope's state management, offering three key methods:

| Method | Parameters | Description |
|------|------|------|
| `register_state` | attr_name, custom_to_json, custom_from_json | Register attributes as states with support for custom serialization |
| `state_dict` | — | Get the current object's state dictionary (synchronous method) |
| `load_state_dict` | state_dict, strict | Load the state dictionary into the current object |

In the `StateModule` object, the following properties are automatically part of the state:
- **Inherited properties from `StateModule`** (automatically registered)
- **Properties manually registered with `register_state`**

```python
from agentscope.module import StateModule
import json


class K8sConfig(StateModule):
    """K8s cluster configuration (stateful objects)"""

    def __init__(self, cluster_name: str) -> None:
        super().__init__()
        self.cluster_name = cluster_name
        self.register_state("cluster_name")  # 手动注册为状态


class DiagnosisContext(StateModule):
    """Diagnostic context (nested state management)"""

    def __init__(self) -> None:
        super().__init__()
        # config inherits from StateModule → automatically becomes part of state
        self.config = K8sConfig("production-cluster")
        self.findings = "No findings"
        self.register_state("findings")  # 手动注册


# Nested state export
ctx = DiagnosisContext()
state = ctx.state_dict()
print(json.dumps(state, indent=2, ensure_ascii=False))
# {
#   "config": { "cluster_name": "production-cluster" },
#   "findings": "No findings"
# }
```

> **Key**: `AgentBase`, `MemoryBase`, `LongTermMemoryBase`, and `Toolkit` all inherit from `StateModule`, thus supporting nested state management.

## 2.3 Agent State Management Practices

```python
agent = ReActAgent(name="Friday", ...)

# Export state (state_dict is a synchronous method)
state = agent.state_dict()
# State includes: name, _sys_prompt, memory content, toolkit status

# State changes after conversation
await agent(Msg("user", "aken from source text done", "user"))
new_state = agent.state_dict()
# memory.content now contains conversation messages

# Restore to initial state
agent.load_state_dict(state)
# Agent's memory is cleared, restored to initial state
```

## 2.4 Overview of Stateful Objects

In the `AgentScope` scope, the following objects are stateful (inherit `StateModule`):

| Object | State Content | Use Cases |
|------|---------|----------|
| Agent (Agent) | name, sys_prompt, memory, toolkit | Session recovery, Agent migration |
| Memory (Memory) | conversation history messages, compressed summaries | Persistent dialogue |
| Long-term Memory | retrieval index, cross-session knowledge | Accumulation of cross-session knowledge |
| Toolkit (Tool Module) | active_groups, tool state | Dynamic tool management |
| PlanNotebook | plan and subtask states | Persistent task planning |

---

## 3. Message — Messaging System

## 3.1 Msg Class

The `Msg` is the most core data structure in `AgentScope`, bearing four responsibilities:

```
Message's four roles
│
├── 1. Information exchange between intelligent bodies    → agent_a(msg) → agent_b(response)
├── 2. User Interface Information Display    → agent.print(msg) → Terminal/Web UI
├── 3. Memory Storage        → memory.add(msg)
└── 4. LLM API Unified Medium    → formatter.format([msg1, msg2, ...])    → API Request
```

## 3.2 Creating Messages

```python
from agentscope.message import Msg

# Base text message
user_msg = Msg(
    name="user",
    content="Please analyze the reason for Pod CrashLoopBackOff",
    role="user",
)

# System message
system_msg = Msg(
    name="system",
    content="You are a Kubernetes operations expert",
    role="system",
)

# Assistant message
assistant_msg = Msg(
    name="Friday",
    content="I will help you analyze the problem...",
    role="assistant",
)
```

## 3.3 Core Fields of Messages

| Field | Type | Description |
|------|------|------|
| `name` | str | Sender's name of the message |
| `content` | str / list | Message content (supports multimodal) |
| `role` | str | Role identifier: `"user"`, `"assistant"`, `"system"` |
| `metadata` | dict | Metadata (optional) |

## 3.4 Multimodal Messages

```python
# Messages containing images
multimodal_msg = Msg(
    name="user",
    content=[
        {"type": "text", "text": "What problems does this architecture diagram have?"},
        {"type": "image_url", "image_url": {"url": "https://example.com/arch.png"}},
    ],
    role="user",
)

# Get pure text content
text = multimodal_msg.get_text_content()
```

---

## 4. Model — Model Interface

## 4.1 Supported Model Providers

`AgentScope` provides a unified LLM interface through the model wrapper (Model Wrapper).

| Model Class | Provider | Typical Model |
|--------|--------|---------|
| `DashScopeChatModel` | Alibaba Cloud Baileys | qwen-max, qwen-plus, qwen-turbo |
| `OpenAIChatModel` | OpenAI | gpt-4o, gpt-4o-mini |
| `OllamaChatModel` | Ollama (Local) | qwen2.5, llama3, mistral |
| `AnthropicChatModel` | Anthropic | claude-3.5-sonnet |
| `GeminiChatModel` | Google | gemini-1.5-pro |

## 4.2 Detailed Model Configuration

**DashScope (Recommended, Integrated Deepest with AgentScope)**:

```python
from agentscope.model import DashScopeChatModel

model = DashScopeChatModel(
    model_name="qwen-max",           # 模型名称
    api_key=os.environ["DASHSCOPE_API_KEY"],  # API Key
    stream=True,                      # 流式输出（生产推荐）
    enable_thinking=False,            # 是否启用思考模式（Qwen3 支持）
    temperature=0.7,                  # 温度参数
    max_tokens=4096,                  # 最大输出 Token 数
)
```

**OpenAI**:

```python
from agentscope.model import OpenAIChatModel

model = OpenAIChatModel(
    model_name="gpt-4o",
    api_key=os.environ["OPENAI_API_KEY"],
    stream=True,
    temperature=0,
    # Optional: Custom API endpoint (for Azure OpenAI or proxy)
    # base_url="https://your-proxy.com/v1",
)
```

**Local Models (Ollama)**:

```python
from agentscope.model import OllamaChatModel

model = OllamaChatModel(
    model_name="qwen2.5:7b",
    base_url="http://localhost:11434",
    stream=True,
)
```

## 4.3 Model Call Flow

```
Agent code                AgentScope Internal
  │                         │
  │  agent(msg)             │
  │──────────────────►      │
  │                    formatter.format(messages)
  │                         │ → Convert to API format
  │                    model(prompt)
  │                         │ → Call LLM API
  │                    Parse response → Msg
  │  ◄──────────────────    │
  │  response               │
```

---

## 5. Formatter — Prompt Formatting

## 5.1 Why Need Formatter

Different LLM APIs have different requirements for message formats. The Formatter is responsible for converting AgentScope's `Msg` object to the format required by specific APIs, while also handling prompt engineering, truncation, and message validation.

## 5.2 Built-in Formatter

| Formatter | Applicable Model | Features |
|-----------|---------|------|
| `DashScopeChatFormatter` | DashScope series | Supports the tool calling format unique to Qwen |
| `OpenAIChatFormatter` | OpenAI / Azure | Standard OpenAI Chat Completions format |
| `OllamaChatFormatter` | Local Ollama models | Adapts to Ollama API format |
| `AnthropicChatFormatter` | Claude series | Anthropic Messages API format |
| `MultiAgentFormatter` | Multi-Agent Scenarios | Handles scenarios where messages contain multiple identity entities |

## 5.3 Using Rules

**Key Principle: The Formatter must match the Model**.

```python
# Correct ✅ - DashScope model + DashScope formatter
agent = ReActAgent(
    model=DashScopeChatModel(model_name="qwen-max", ...),
    formatter=DashScopeChatFormatter(),
    ...
)

# Correct ✅ - OpenAI model + OpenAI formatter
agent = ReActAgent(
    model=OpenAIChatModel(model_name="gpt-4o", ...),
    formatter=OpenAIChatFormatter(),
    ...
)

# Incorrect ❌ - Mixing will result in formatting errors
agent = ReActAgent(
    model=DashScopeChatModel(model_name="qwen-max", ...),
    formatter=OpenAIChatFormatter(),  # 格式不兼容!
    ...
)
```

## 5.4 Multi-Agent Formatting

When messages contain multiple identity entities (e.g., multi-party chat, games), the standard `role` field (user/assistant/system) cannot distinguish between different speakers. In such cases, the `MultiAgentFormatter` (such as `DashScopeMultiAgentFormatter`) is needed:

```python
from agentscope.formatter import DashScopeMultiAgentFormatter

# Suitable for scenarios such as group chat, games, and social simulations
formatter = DashScopeMultiAgentFormatter()
```

> **Key Distinction**: Multi-Agent Workflow ≠ Multi-Agent within Formatters.
>
> For example, even if the following code involves multiple agents (tool_agent and caller), the input is wrapped as a role="user" message, and the standard Formatter can distinguish:
>
> ```python
> async def tool_function(query: str) -> str:
>     """Call a tool function of another agent"""
>     msg = Msg("user", query, role="user")
>     tool_agent = ReActAgent(name="Programmer", ...)
>     return await tool_agent(msg)
> ```
>
> Only when a single LLM call's input message contains multiple different speakers (such as Alice, Bob, Charlie having a conversation) does `MultiAgentFormatter` need to be used.

---

## 6. Agent — Agent System

## 6.1 Core Base Class

```
AgentScope intelligent agent inheritance system
│
├── AgentBase (all agent base classes)
│   ├── reply(msg)           \→ process message and generate response
│   ├── observe(msg)         \→ receive message without returning response
│   ├── print(msg)           \→ output message to terminal/Web
│   └── handle_interrupt()   \→ handle user interruption
│
├── ReActAgentBase (ReAct intelligent agent base class)
│   ├── inherit all methods from AgentBase
│   ├── _reasoning()         \→ reasoning phase (LLM tool call)
│   └── _acting()            \→ action phase (execute utility function)
│
├── ReActAgent (out-of-the-box ReAct intelligent agent)
│   └── inherit ReActAgentBase, provide complete implementation
│
└── UserAgent (user agent intelligent agent)
    └── receive user input from terminal
```

## 6.2 Three Core Functions of ReActAgent

```python
from agentscope.agent import AgentBase
from agentscope.message import Msg


class MyAgent(AgentBase):
    """Example of custom agent"""

    async def reply(self, msg: Msg | list[Msg] | None) -> Msg:
        """
        核心函数：处理传入消息并生成响应。
        - 接收用户/其他智能体的消息
        - 执行推理和工具调用
        - 返回响应消息
        """
        pass

    async def observe(self, msg: Msg | list[Msg] | None) -> None:
        """
        观察函数：接收消息但不返回响应。
        - 用于旁听其他智能体的对话
        - 将消息存储在记忆中
        - 适合监控/日志类智能体
        """
        pass

    async def handle_interrupt(self) -> Msg:
        """
        中断处理：当用户中断智能体回复时调用。
        - 实时介入（Realtime Steering）的关键机制
        - 允许优雅地处理中断
        """
        pass
```

## 6.3 Complete Parameters of ReActAgent

```python
from agentscope.agent import ReActAgent

agent = ReActAgent(
    # === Required Parameters ===
    name="K8s-Expert",                  # 智能体名称
    sys_prompt="You are a Kubernetes operations expert...",  # system prompt
    model=model,                         # LLM 模型实例
    formatter=formatter,                 # 提示词格式化器

    # === Optional Parameters ===
    toolkit=toolkit,                     # 工具模块
    memory=InMemoryMemory(),             # 短期记忆
    long_term_memory=None,               # 长期记忆
    long_term_memory_mode="agent_control",  # 长期记忆管理模式
    # "agent_control": Autonomous management of the agent
    # "static_control": Developer management
    # "both": Both activated simultaneously

    enable_meta_tool=False,              # 是否允许智能体自主管理工具
    parallel_tool_calls=True,            # 是否允许并行工具调用
    max_iters=10,                        # 最大迭代次数
    plan_notebook=None,                  # 计划模块
    print_hint_msg=True,                 # 是否打印提示消息
)
```

## 6.4 Customizing Agent from Scratch

```python
from agentscope.agent import AgentBase
from agentscope.model import DashScopeChatModel
from agentscope.formatter import DashScopeChatFormatter
from agentscope.memory import InMemoryMemory
from agentscope.message import Msg
import os


class K8sDiagnosisAgent(AgentBase):
    """K8s Diagnostic Agent — Customized from AgentBase"""

    def __init__(self) -> None:
        super().__init__()
        self.name = "K8s-Doctor"
        self.sys_prompt = """你是一个 Kubernetes 生产运维诊断专家。
诊断原则:
1. 先收集信息再下结论
2. 给出根因分析 + 修复步骤 + 验证方法
3. 对破坏性操作给出风险提示
4. 所有结论必须基于工具获取的实际数据"""

        self.model = DashScopeChatModel(
            model_name="qwen-max",
            api_key=os.environ["DASHSCOPE_API_KEY"],
            stream=False,
        )
        self.formatter = DashScopeChatFormatter()
        self.memory = InMemoryMemory()

    async def reply(self, msg: Msg | list[Msg] | None) -> Msg:
        """Handle diagnostic requests"""
        # Store input message to memory
        await self.memory.add(msg)

        # Build prompt
        prompt = await self.formatter.format(
            [
                Msg("system", self.sys_prompt, "system"),
                *await self.memory.get_memory(),
            ],
        )

        # Call model
        response = await self.model(prompt)

        # Create response message
        reply_msg = Msg(
            name=self.name,
            content=response.content,
            role="assistant",
        )

        # Store response to memory
        await self.memory.add(reply_msg)

        # Print message
        await self.print(reply_msg)

        return reply_msg

    async def observe(self, msg: Msg | list[Msg] | None) -> None:
        """Observe messages (eavesdropping mode)"""
        await self.memory.add(msg)

    async def handle_interrupt(self) -> Msg:
        """Handle interruptions"""
        return Msg(
            name=self.name,
            content="Diagnosis has been interrupted. Please re-describe the problem to continue.",
            role="assistant",
        )
```

---

## 7. Memory — Memory Foundation

## 7.1 Built-in Memory Types

AgentScope provides three implementations for memory storage:

| class | storage mode | applicable scenarios |
|----|---------|----------|
| `InMemoryMemory` | memory | development debugging, short sessions |
| `AsyncSQLAlchemyMemory` | relational database (SQLite/PostgreSQL/MySQL) | production environment, supports connection pooling |
| `RedisMemory` | Redis | high-performance distributed scenarios |

## 7.2 Basic Usage of InMemoryMemory

```python
from agentscope.memory import InMemoryMemory
from agentscope.message import Msg

memory = InMemoryMemory()

# Add message
await memory.add(Msg("user", "Pod is in Pending state", "user"))
await memory.add(Msg("assistant", "I will help you diagnose...", "assistant"))

# Add a message marked (mark)
await memory.add(
    Msg("system", "<system-hint>Check resource quotas first</system-hint>", "system"),
    marks="hint",  # 标记为 hint 类型
)

# Retrieve messages by mark
hint_msgs = await memory.get_memory(mark="hint")

# Delete messages by tag
deleted = await memory.delete_by_mark("hint")

# Get all memories
messages = await memory.get_memory()
```

## 7.3 Mark (Marking) System

**Mark** is an important feature of AgentScope memory management, used for categorizing, filtering, and retrieving messages:

```
Mark marking system
│
├── message classification    \→ distinguish prompt messages, tool results, user dialogue
├── selective retrieval  \→ get_memory(mark="hint") only retrieve specific types
├── batch management    \→ delete_by_mark("hint") clean up one-time prompts
└── internal use    \→ ReActAgent use "hint" mark management for one-time prompts
```

## 7.4 State Management

```python
memory = InMemoryMemory()
await memory.add(Msg("user", "hello", "user"))

# Export state (state_dict is a synchronous method)
state = memory.state_dict()
# State contains _compressed_summary and all messages (with tags)

# Restore state
new_memory = InMemoryMemory()
new_memory.load_state_dict(state)
```

> **Note**: `InMemoryMemory` loses data upon process exit. Production environments should use `AsyncSQLAlchemyMemory` (relational database) or `RedisMemory` (Redis), see [19 - Memory Management and Context Engineering](./19-agentscope-memory-context.md).

---

## 8. Full Example: K8s Questioning Agent

Combine these concepts to build a complete Kubernetes knowledge Q&A Agent:

```python
import asyncio
import os

from agentscope.agent import ReActAgent
from agentscope.model import DashScopeChatModel
from agentscope.formatter import DashScopeChatFormatter
from agentscope.memory import InMemoryMemory
from agentscope.message import Msg


async def k8s_qa_agent():
    """K8s Knowledge Q&A Agent"""

    agent = ReActAgent(
        name="K8s-Expert",
        sys_prompt="""你是一个资深 Kubernetes 运维专家，拥有以下专长:
- 集群架构设计与优化
- 故障诊断与排查
- 性能调优
- 安全最佳实践

回答问题时:
1. 给出清晰的结构化回答
2. 包含具体的命令和配置示例
3. 说明潜在风险和注意事项""",
        model=DashScopeChatModel(
            model_name="qwen-max",
            api_key=os.environ["DASHSCOPE_API_KEY"],
            stream=True,
        ),
        memory=InMemoryMemory(),
        formatter=DashScopeChatFormatter(),
        max_iters=5,
    )

    # Simulate multi-round dialogue
    questions = [
        "Pod remains in Pending state, what could be the reasons?",
        "If it's due to insufficient resources, how can we solve it quickly?",
        "How do we configure HPA to automatically handle such issues?",
    ]

    for q in questions:
        print(f"\n{'='*60}")
        print(f"User: {q}")
        print(f"{'='*60}")

        msg = Msg(name="user", content=q, role="user")
        response = await agent(msg)

        print(f"\nAgent: {response.get_text_content()}")


asyncio.run(k8s_qa_agent())
```

---

## 9. Best Practices

## Design Principles

- **Make the system prompt specific**: specify the agent's expertise, behavior boundaries, and output format requirements in `sys_prompt`
- **Ensure Formatter and Model match strictly**: this is the most common configuration error in AgentScope
- **Use observe for eavesdropping**: monitor-type agents use `observe` instead of `reply`, to avoid unnecessary responses
- **Maintain state management throughout**: implement session recovery and agent migration using `state_dict/load_state_dict`
- **Set a reasonable max_iters limit**: prevent infinite inference loops, suggest 5-15 iterations

## Naming Conventions

```python
# Recommendation: Clear role naming
agent = ReActAgent(name="K8s-Diagnosis-Expert", ...)
agent = ReActAgent(name="Network-Analyzer", ...)
agent = ReActAgent(name="Cost-Advisor", ...)

# Avoid: Ambiguous naming
agent = ReActAgent(name="agent1", ...)
agent = ReActAgent(name="bot", ...)
```

---

## Related Documentation

| document | associated content |
|------|---------|
| [16 - Overview and Installation](./16-agentscope-overview-installation.md) | installation configuration and Hello World |
| [18 - Tool System and MCP](./18-agentscope-tool-system.md) | Tool details and MCP integration |
| [19 - Memory Management](./19-agentscope-memory-context.md) | Deep use of Memory and Production Solutions |
| [01 - Agent Basics](./01-ai-agent-fundamentals.md) | General Agent Concepts and Inference Framework |

---

*This document is original content from the kudig-database project 02-ai-agents topic series.*

---

## Related Obsidian Documentation

- 02-ai-agents KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|[[AI Agent Engineering Topic Series|AI Agent Engineering Topic Series]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|[[AI Agent Basics and Core Architecture|AI Agent Basics and Core Architecture]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|[[LLM Foundation Models|LLM Foundation Models]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Mainstream Agent Framework Deep Comparison]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|RAG Retrieval Enhanced Generation Deep Guide]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Tool Use & Function Calling Design Guidelines]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Multy-Agent Orchestration and Collaboration Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation System and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]

## See Also

- 15-agent-corpus-gap-analysis
- 16-agentscope-overview-installation
- 18-agentscope-tool-system
- 19-agentscope-memory-context


<!-- risk-assessed -->
