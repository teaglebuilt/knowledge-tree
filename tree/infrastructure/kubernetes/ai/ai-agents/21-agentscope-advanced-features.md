---
title: Advanced Features and Extension Development (domain-14-ai-ml-infra)
description: 'description: ''**Document Type**: Advanced Feature Topic | **Last Updated**: 2026-03 | **Keywords**: AgentScope,
  Hooks, Middleware,'
summary: 'description: ''**Document Type**: Advanced Feature Topic | **Last Updated**: 2026-03 | **Keywords**: AgentScope,
  Hooks, Middleware,'
category: general
tags:
- ai
- ai-agent
- kubelet
- jaeger
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
estimated_read_time: 15min
intent_queries:
- What is AgentScope Advanced Features and Extension Development
- How to do AgentScope Advanced Features and Extension Development
- Kubernetes 14 ai ml infra Best Practices
trigger_keywords:
- AgentScope
- What are Advanced Features and Extension Development
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- tracing-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/21-agentscope-advanced-features.md
---

> **Production Environment Security Reminders**
>
> This document contains executable operational commands. Please confirm before execution: that the target cluster and Namespace are correct; that you have sufficient RBAC permissions; and that these commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




title: AgentScope Advanced Features and Extension Development
description: '**Document Type**: Advanced Features Special Topic | **Last Updated**: 2026-03 | **Keywords**: AgentScope, Hooks, Middleware, RAG, A2A, Agent-to-Agent, Realtime Voice, Realtime Steering, Structured Output, Agentic RL, Reinforcement Learning Fine-tuning, Evaluation,
  RAG, A2A, Agent-to-Agent, Real-time Voice, Realtime Steering, Structured Output, Agentic RL, Reinforcement Learning Fine-tuning, Evaluation,
  ACEBench, Embedding'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- [[kubelet|kubelet]]
- [[Jaeger|jaeger]]
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Architects
- SRE
estimated_read_time: 5min
intent_queries:
- What is AgentScope Advanced Features and Extension Development
- How to use AgentScope Advanced Features and Extension Development
trigger_keywords:
- AgentScope
- Advanced Features and Extension Development
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

# AgentScope Advanced Features and Extension Development

> **Document Type**: Advanced Features Special Topic | **Last Updated**: 2026-03 | **Keywords**: AgentScope, Hooks, Middleware, RAG, A2A, Agent-to-Agent, Realtime Voice, Realtime Steering, Structured Output, Agentic RL, Reinforcement Learning Fine-tuning, Evaluation, ACEBench, Embedding

---

## Overview

AgentScope offers a range of advanced features beyond its core components: Agent Hooks and Middleware for behavior enhancement, RAG for knowledge enhancement, A2A protocol for cross-framework Agent communication, real-time voice support for voice interaction, Agentic RL for reinforcement learning fine-tuning, and a comprehensive evaluation system.

This document systematically explains the design principles, usage methods, and production practices of these advanced features.

---

## 1. Agent Hooks — Hooks Function

## 1.1 Concept

Hooks allow custom logic to be inserted before or after the core functions of an Agent (reply, observe, print, _reasoning, _acting) without modifying the Agent's source code.

```
Agent Hooks Execution Flow
│
├── before_reply_hook(msg)      ← Message preprocessing, logging
├── agent.reply(msg)            ← Core logic of Agent
│   ├── before_reasoning_hook() ← Reasoning pre-hook (ReActAgent)
│   ├── agent._reasoning()      ← Reasoning
│   ├── after_reasoning_hook()  ← Reasoning post-hook
│   ├── before_acting_hook()    ← Acting pre-hook
│   ├── agent._acting()         ← Acting (executing tool)
│   └── after_acting_hook()     ← Acting post-hook
├── after_reply_hook(response)  ← Post-reply processing, metric collection
│
├── before_observe_hook(msg)
├── agent.observe(msg)
├── after_observe_hook()
│
├── before_print_hook(msg)
├── agent.print(msg)
└── after_print_hook()
```

## 1.2 Hook Registration API

AgentScope provides two ways to register Hooks:

| Registration Method | Scope | Purpose |
|---------|---------|------|
| `register_instance_hook(agent, hook_fn)` | Single Agent Instance | Debugging/Monitoring specific Agent |
| `register_class_hook(AgentClass, hook_fn)` | All Instances of a Class | Global-level Logging/Auditing |

**Unified Hook Signature**:

```python
from agentscope.agent import ReActAgent
from agentscope.hook import register_instance_hook, register_class_hook


# Hook function unified signature: async def hook(agent, *args)
async def log_before_reply(agent, msg):
    """pre-reply hook: receives agent and input message"""
    print(f"[{agent.name}] received message: {msg.get_text_content()[:80]}")


async def log_after_reply(agent, response):
    """post-response hook: receives agent and response message"""
    print(f"[{agent.name}] response length: {len(response.get_text_content())}")


# Instance-level registration (only affects a single Agent)
agent = ReActAgent(name="K8s-Expert", ...)
register_instance_hook(agent, "before_reply", log_before_reply)
register_instance_hook(agent, "after_reply", log_after_reply)

# Class-level registration (affects all instances of ReActAgent)
register_class_hook(ReActAgent, "before_reply", log_before_reply)
```

## 1.3 Common Hook Scenarios

| Hook Location | Typical Use Case |
|-----------|---------|
| `before_reply` | Input validation, sensitive information de-identification, request rate limiting |
| `after_reply` | Response auditing, delay monitoring, Token statistics |
| `before_reasoning` | Inject additional context (such as current time, environment information) |
| `after_reasoning` | Check the rationality of the reasoning results |
| `before_acting` | Permission check for tool calls, risk assessment |
| `after_acting` | Validate the execution result of the tool, enhance error handling |
| `before_observe` | Message filtering (filter irrelevant information) |
| `before_print` | Format output, multi-language translation |

---

## 3. Middleware — Middleware

> **Important**: The Middleware of **AgentScope** is registered on the **Toolkit** (rather than the Agent), using an onion model. Detailed usage can be found in [Section 9 of the Toolkit System](./18-agentscope-tool-system.md).

```
Hooks vs Middleware Responsibilities
│
├── Hooks    → Applied at the Agent level
│   ├── register_instance_hook   → Single Agent
│   └── register_class_hook      → All instances of a certain class of Agent
│   purpose: Logging, auditing, monitoring, context injection
│
└── Middleware → Applied at the Toolkit level
    └── toolkit.register_middleware(fn)
    purpose: Permission control, output truncation, result transformation
```

---

## 2. RAG — Retrieval-Augmented Generation

## 2.1 AgentScope RAG Architecture

AgentScope's RAG module adopts a three-layer architecture: **Reader → Knowledge → Store**:

```
AgentScope RAG Architecture
│
├── Reader(Document Reader)
│   ├── TextReader       → Pure text files
│   ├── PDFReader        → PDF Document
│   ├── ImageReader      → Image File (Multimodal)
│   └── Custom Reader    → Inherits ReaderBase for extension
│
├── Knowledge(Knowledge Management)
│   └── SimpleKnowledge  → Includes Reader + Store, unified management
│       ├── load()       → Load document
│       ├── retrieve()   → Retrieve relevant fragments
│       └── delete()     → Delete document
│
└── Store(Vector Storage)
    └── QdrantStore      → Vector storage based on Qdrant
        ├── Cloud: Qdrant Cloud
        └── Local: Qdrant Container
```

## 2.2 Using AgentScope RAG

```python
from agentscope.rag import SimpleKnowledge, QdrantStore, TextReader
from agentscope.agent import ReActAgent


async def rag_agent_example():
    # 1. Create knowledge base
    knowledge = SimpleKnowledge(
        name="k8s-troubleshooting",
        reader=TextReader(),           # 文本读取器
        store=QdrantStore(             # Qdrant 向量存储
            collection_name="k8s_docs",
            url="http://localhost:6333",  # 本地 Qdrant
        ),
        embedding_model=embedding_model,
    )

    # 2. Load documents
    await knowledge.load(
        paths=["./domain-10-troubleshooting-diagnostics/"],
        file_types=[".md"],
    )

    # 3. Retrieve relevant content
    results = await knowledge.retrieve(
        query="Pod Pending Troubleshooting Steps"
        top_k=5,
    )
```

## 2.3 RAG Integration Methods

AgentScope supports two modes of RAG integration:

| Integration Mode | Description | Applicable Scenarios |
|---------|------|--------|
| **Agentic Integration** | RAG registers as a tool to the Toolkit, and the Agent decides autonomously when to retrieve | Complex scenarios where the Agent needs to determine whether to retrieve |
| **Generic Integration** | Automatically injects retrieval results into the Agent's sys_prompt | Simple scenarios where retrieval is required each time |

```python
# Agentic integration (recommended): register search function as a tool
async def search_knowledge(query: str) -> str:
    """search K8s knowledge base."""

    Args:
        query: 搜索关键词或问题描述

    Returns:
        相关知识片段
    """
    results = await knowledge.retrieve(query=query, top_k=5)
    return "\n\n".join(r.content for r in results)

toolkit = Toolkit()
toolkit.register_tool_function(search_knowledge)
```

## 2.4 RAG Best Practices

| Phase | Best Practice | Anti-pattern |
|------|---------|--------|
| Document Reading | Use the corresponding Reader (TextReader/PDFReader) | Treat all formats uniformly as plain text |
| Chunking | Segment by semantic paragraphs to maintain contextual integrity | Fixed-length segmentation leads to semantic breaks |
| Embedding | Use multilingual models (BGE-M3) | English models process Chinese documents |
| Retrieval | Top-K=5 + Re-ranking | Top-K=1 results in insufficient information |
| Integration | Agentic Integration (RAG as a tool) | Always full-scale injection of retrieval results |
| Injection | Clearly mark "from knowledge base" | Direct concatenation leads to LLMS confusing sources |

---

## 4. A2A Protocol — Agent-to-Agent

## 4.1 What is A2A

A2A (Agent-to-Agent) is an open protocol proposed by Google, used for standardized communication between agents from different frameworks. AgentScope includes built-in support for A2A.

```
A2A vs MCP's Difference
│
├── MCP(Model Context Protocol)
│   Agent ↔ Tool/Data
│   "How does an Agent call external tools"
│
└── A2A(Agent-to-Agent Protocol)
    Agent ↔ Agent
    "How different Agents (even different frameworks) collaborate"
```

## 4.2 A2A Agent Example

```python
# AgentScope's A2A Agent can communicate with Agents from other frameworks
from agentscope.agent import ReActAgent

# Create an Agent supporting A2A protocol
a2a_agent = ReActAgent(
    name="K8s-Expert-A2A",
    sys_prompt="You are a Kubernetes operations expert, receiving and responding to requests via A2A protocol",
    ...
)

# After deployment by AgentScope Runtime,
# Agents from other frameworks can communicate with it via A2A protocol
```

## 4.3 Value of A2A in Production

```
A2A Production Use Cases
│
├── Collaborative Agents Across Teams
│   Team A's LangGraph Agent ←A2A→ Team B's AgentScope Agent
│
├── Incremental migration
│   Gradually replace old framework Agents with AgentScope Agents
│   They collaborate seamlessly through A2A
│
└── Microservices Agent
    Deploy independent Agent services for each domain
    Compose Agent grid through A2A protocol
```

---

## 5. Real-time Voice Agent

## 5.1 Voice Agent Architecture

```
Voice Agent Architecture
│
├── Voice Input
│   ├── Microphone Capture
│   ├── ASR (Speech Recognition)
│   └── Text Message
│
├── Agent Processing
│   └── ReActAgent (standard inference and tool invocation)
│
├── Voice Output
│   ├── TTS (Text-to-Speech)
│   └── Audio Playback
│
└── Web Interface
    └── Real-time bi-directional voice interaction
```

## 5.2 Creating a Voice Agent

```python
from agentscope.agent import ReActAgent
from agentscope.tts import TTSModel

# Create an Agent with TTS
voice_agent = ReActAgent(
    name="Voice-Assistant",
    sys_prompt="you are a voice assistant, reply in simple natural language.",
    model=model,
    formatter=formatter,
    memory=memory,
    # TTS configuration
    tts_model=TTSModel(
        model_name="cosyvoice",  # 阿里 CosyVoice
        # or other TTS services
    ),
)
```

---

## 6. Real-time Intervention (Realtime Steering)

## 6.1 Concepts

real-time intervention allows users to **intercept** and adjust directions during Agent execution, which AgentScope implements through the `handle_interrupt` mechanism:

```
Real-time Intervention Workflow
│
├── Agent is executing (inference + tool calls)
│
├── User sends interrupt signal
│
├── Agent receives interrupt
│   ├── Pause current execution
│   ├── Save completed state
│   └── Call handle_interrupt()
│
└── User can:
    ├── Modify instruction, Agent continues
    ├── Cancel current task
    └── Switch to other task
```

## 6.2 Custom Interrupt Handling

```python
from agentscope.agent import AgentBase
from agentscope.message import Msg


class InterruptibleAgent(AgentBase):
    """Agent supporting graceful interruption"""

    async def handle_interrupt(self) -> Msg:
        """handle user interruption"""
        # Save current progress
        progress = await self._save_progress()

        return Msg(
            name=self.name,
            content=f"""执行已中断。

当前进度:
{progress}

您可以:
1. 输入新指令继续
2. 输入 "resume" 从断点恢复
3. 输入 "cancel" 取消任务""",
            role="assistant",
        )

    async def _save_progress(self) -> str:
        """save the progress at the time of interruption"""
        state = await self.state_dict()
        # persist the state...
        return f"completed {len(state.get('tool_calls', []))} tool calls"
```

---

## 7. Structured Output

## 7.1 Make Agent Output Structured Data

```python
from agentscope.agent import ReActAgent

# Guide structured output through system prompts
agent = ReActAgent(
    name="Structured-Expert",
    sys_prompt="""你是 K8s 诊断专家。

输出格式要求（严格 JSON）:
{
    "severity": "critical|high|medium|low",
    "root_cause": "problem root cause description",
    "affected_resources": ["affected resources list"],
    "fix_steps": [
        {"step": 1, "action": "operation description", "command": "specific command", "risk": "risk level"}
    ],
    "verification": "verification steps",
    "rollback": "rollback plan"
}""",
    ...
)
```

---

## 8. Tracing — Full-Link Tracing

## 8.1 Enable Tracing via agentscope.init

AgentScope initializes tracing uniformly using `agentscope.init()`.

```python
import agentscope

# Enable AgentScope Studio Tracing
agentscope.init(
    studio_url="http://studio:3000",
    tracing_url="http://otel-collector:4317",
)
```

## 8.2 Built-in Tracing Decorators

AgentScope provides built-in decorators to automatically trace critical operations:

| Decorator | Tracked Content |
|---------|--------|
| `@trace_llm` | LLM calls (Tokens, delay, model name) |
| `@trace_reply` | Entire process of Agent reply |
| `@trace_format` | Formatting process of the Formatter |
| `@trace` | General tracing decorator |

## 8.3 Third-party Tracing Integrations

AgentScope supports exporting tracing data to multiple backends:

| Backend | Type | Description |
|------|------|------|
| AgentScope Studio | Built-in | Officially visualizable tool, including tracing + evaluation |
| Alibaba Cloud CloudMonitor | Cloud service | Native monitoring provided by Alibaba Cloud |
| Arize-Phoenix | Open-source | Focuses on LLM observability |
| Langfuse | Open-source/Cloud | LLM engineering platform |
| Jaeger / Zipkin | Open-source | General distributed tracing |

---

## 9. Agentic RL — Reinforcement Learning Fine-tuning

## 8.1 Concepts

AgentScope includes built-in support for Agentic RL, allowing direct fine-tuning of Agent behavior via reinforcement learning rather than just optimizing prompts:

```
Agentic RL workflow
│
├── 1. Agent executes task
│      Using current strategy (LLM + prompt)
│
├── 2. Obtain feedback
│      ├── Environment feedback (task success/failure)
│      ├── Judge (LLM-as-Judge) evaluation
│      └── Manual scoring
│
├── 3. Strategy update
│      Through RL algorithm update LLM weights
│
└── 4. Iterative optimization
       Repeat steps 1-3, continuously enhance Agent capabilities
```

## 8.2 AgentScope Agentic RL Example

AgentScope offers multiple ready-to-use Agentic RL training scenarios:

| Example | Description | Base Model | Training Effect |
|------|------|---------|---------|
| Math Agent | Multi-step Mathematical Reasoning | Qwen3-0.6B | Accuracy 75% → 85% |
| Frozen Lake | Environment Navigation | Qwen2.5-3B-Instruct | Success Rate 15% → 86% |
| Learn to Ask | LLM-as-Judge Feedback | Qwen2.5-7B-Instruct | Accuracy 47% → 92% |
| Email Search | Tool Usage Optimization | Qwen3-4B-Instruct | Accuracy 60% |
| Werewolf Game | Multi-Agent Game | Qwen2.5-7B-Instruct | Wolf Win Rate 50% → 80% |
| Data Augment | Synthetic Data Augmentation | Qwen3-0.6B | AIME-24 Accuracy 20% → 60% |

## 8.3 K8s Operational Agent Fine-tuning Approach

```
K8s Diagnostic Agent Fine-tuning Solution
│
├── Training Data
│   ├── Historical Fault Diagnosis Records (Problem → Diagnostic Steps → Root Cause)
│   ├── kudig-database Knowledge Base (Structured SOP)
│   └── Synthetic Data (Problem Simulation + Diagnostic Trajectory)
│
├── Reward Functions
│   ├── Diagnostic Accuracy (Is the root cause correct)
│   ├── Diagnostic Efficiency (Are the steps optimal)
│   ├── Tool Usage Rationality (Did the correct tools get used)
│   └── Security (Did dangerous operations avoid)
│
├── Baseline Model
│   └── Qwen2.5-7B-Instruct (or larger model)
│
└── Expected Outcomes
    ├── Diagnostic Accuracy Improvement 20-30%
    ├── Average Diagnostic Steps Reduced by 40%
    └── False Operation Rate Reduced to <1%
```

---

## 10. Evaluation System

## 9.1 AgentScope Evaluation Framework

AgentScope provides comprehensive Agent evaluation capabilities:

```
Evaluation System
│
├── ACEBench (Built-in Benchmarking)
│   ├── Tool Usage Accuracy Evaluation
│   ├── Evaluation of multi-step reasoning capability
│   └── Standardized scoring metrics
│
├── OpenJudge(LLM-as-Judge)
│   ├── Use LLM to evaluate the quality of Agent's output
│   ├── Supports multi-dimensional scoring
│   └── Customizable scoring standards
│
└── AgentScope Studio (visual evaluation)
    ├── Visualization of evaluation results
    ├── Playback of Agent trajectories
    └── Comparison of different versions of Agents
```

## 9.2 Evaluation Dimensions

| Dimension | Evaluation Metric | Method |
|------|---------|------|
| **Accuracy** | Root Cause Diagnosis Accuracy | Ground Truth Comparison |
| **Efficiency** | Average Inference Steps | Trajectory Analysis |
| **Tool Usage** | Tool Selection Accuracy, Call Success Rate | Tool Call Log Analysis |
| **Safety** | Detection Rate of Dangerous Operations | Hit Rate of Safety Barriers |
| **Consistency** | Consistency of Answers to the Same Question | Multiple Sampling Comparison |
| **Latency** | End-to-End Response Time | P50/P95/P99 Latency |
| **Cost** | Token Consumption per Diagnosis | Token Counting |

## 9.3 Evaluation Practices

```python
# Evaluate the accuracy of the K8s diagnostic Agent
test_cases = [
    {
        "input": "Pod is in Pending state",
        "expected_root_cause": "insufficient resources or scheduling constraints",
        "expected_tools": ["kubectl_get_pods", "kubectl_describe_resource"],
    },
    {
        "input": "Service cannot be accessed",
        "expected_root_cause": "Endpoint is empty or Selector does not match",
        "expected_tools": ["kubectl_get_pods", "kubectl_describe_resource"],
    },
    {
        "input": "Node NotReady",
        "expected_root_cause": "kubelet anomaly or resource pressure",
        "expected_tools": ["kubectl_describe_resource", "kubectl_get_events"],
    },
]


async def evaluate_agent(agent, test_cases):
    """evaluate the Agent"""
    results = []
    for case in test_cases:
        msg = Msg("user", case["input"], "user")
        response = await agent(msg)

        # Score using LLM-as-Judge
        score = await llm_judge(
            question=case["input"],
            expected=case["expected_root_cause"],
            actual=response.get_text_content(),
        )
        results.append({
            "input": case["input"],
            "score": score,
            "response_length": len(response.get_text_content()),
        })

    avg_score = sum(r["score"] for r in results) / len(results)
    print(f"average score: {avg_score:.2f}")
    return results
```

---

## 11. Embedding Module

AgentScope provides an Embedding interface for text vectorization, supporting RAG and semantic search:

```python
from agentscope.embedding import EmbeddingModel

# DashScope Embedding
embedding = EmbeddingModel(
    model_name="text-embedding-v3",
    api_key=os.environ["DASHSCOPE_API_KEY"],
)

# generate vector
vector = await embedding.embed("Kubernetes Pod Pending Debug")
# vector: [0.023, -0.114, 0.089, ...]
```

---

## 12. Best Practices and Anti-patterns

## Best Practices

- **Hooks are used for cross-cutting concerns at the Agent level**: Logging, monitoring, auditing, etc., use Hooks, tool execution uses Toolkit Middleware
- **`register_instance_hook` vs `register_class_hook`**: Debugging for a single Agent uses instance-level, global logs use class-level
- **RAG integrates with Agentic**: RAG is registered as a tool and the Agent decides autonomously when to retrieve data
- **agentscope.init enables tracing**: Production environments enable full-chain tracing through `agentscope.init(studio_url=..., tracing_url=...)`
- **A2A Achieve Loose Coupling**: different teams' Agents communicate via A2A to avoid framework coupling
- **Test-Driven Development**: define evaluation metrics first, then optimize the Agent
- **Agentic RL Start with Smaller Models**: validate methods on 0.6B-3B models before scaling up to larger models

## Anti-patterns

- **Overuse of Hooks**: long hooks chains (>5) increase debugging difficulty
- **Confuse Hooks with Middleware**: Agent-level logic uses Hooks, tool-level logic uses Toolkit Middleware
- **Full Rag Injection**: search results are directly injected into context without filtering
- **Disable Tracing**: performance issues and errors are nearly impossible to locate in production without tracing
- **Ignore Structured Output Validation**: Agent's JSON output may not be valid, requiring validation and retries
- **Agentic RL Without Security Constraints**: fine-tuned models might generate more aggressive operational strategies
- **Insufficient Test Data Sets**: evaluation results with less than 50 test cases lack statistical significance

---

## Associated Documents

| Document | Related Content |
|------|---------|
| [17 - Core Concepts](./17-agentscope-core-concepts.md) | Base class and extension points for Agents |
| [18 - Tool System](./18-agentscope-tool-system.md) | MCP Integration and Tool Registration |
| [20 - Multi-Agent Orchestration](./20-agentscope-multi-agent-orchestration.md) | Application of A2A in multi-Agent scenarios |
| [22 - Production Deployment](./deployment.md|22-agentscope-production-deployment]].md) | Runtime Deployment and Observability |
| [04 - RAG Knowledge Retrieval](./04-rag-knowledge-retrieval.md) | General RAG Architecture and Strategies |
| [08 - Evaluation and Observability](./08-agent-evaluation-observability.md) | General Evaluation Framework |

---

*This document is original content from the kudig-database project's 02-ai-agents topic.*

---

## Obsidian-related Documents

- 02-ai-agents MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|AI Agent Engineering Topic]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|AI Agent Basics and Core Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|LLM Foundation Model Selection and Evaluation]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|LLM Foundation Model Selection and Evaluation]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Mainstream Agent Framework Deep Comparison]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|RAG Retrieval-Augmented Generation Deep Guide]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Tool Usage and Function Calling Design Guidelines]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Mult-Agent Orchestration and Collaboration Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation System and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]

## See Also

- 19-agentscope-memory-context
- 20-agentscope-multi-agent-orchestration
- 22-agentscope-production-deployment
- 23-agent-cli-fundamentals


<!-- risk-assessed -->
