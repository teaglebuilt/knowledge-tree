---
title: AgentScope Overview and Installation Introduction (domain-14-ai-ml-infra)
description: 'title: AgentScope Overview and Installation Introduction'
summary: 'title: AgentScope Overview and Installation Introduction'
category: general
tags:
- ai
- ai-agent
- deep-dive
- configuration
- docker
- redis
- postgresql
- serverless
- llm
- rag
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 25min
intent_queries:
- What is AgentScope Overview and Installation Introduction
- How to do AgentScope Overview and Installation Introduction
- Kubernetes 14 ai ml infra Best Practices
trigger_keywords:
- AgentScope
- Overview and Installation Introduction
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- redis-basics
- observability-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/16-agentscope-overview-installation.md
---

> **Production Environment Security Reminders**
>
> Commands included in this document are executable directly. Before executing, please confirm: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




title: AgentScope Overview and Installation Basics
description: '# AgentScope Overview and Installation Basics'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- docker
- redis
- postgresql
- serverless
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- Architect
- SRE
estimated_read_time: 10min
intent_queries:
- What is AgentScope Overview and Installation Basics
- How to do AgentScope Overview and Installation Basics
trigger_keywords:
- AgentScope
- Overview and Installation Basics
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

# AgentScope Overview and Installation Primer

> **Document Type**: Framework Introduction Series | **Last Updated**: 2026-03 | **Keywords**: AgentScope, Installation, Basics, ReAct Agent, Multi-Agent Framework, Alibaba, ModelScope, DashScope, Asynchronous Architecture

---

## Overview

AgentScope is an **production-level, developer-friendly** multi-agent framework launched by Alibaba, with its core design philosophy being **facing the increasing model capabilities** — leveraging the inference and tool invocation capabilities of models rather than strict prompts and fixed orchestration.

This article is the first in the AgentScope series, systematically introducing the framework positioning, core features, installation configuration, and a first Hello World example, helping readers set up their environment and run their first agent within five minutes.

> **Official Resources**:
> - GitHub: https://github.com/agentscope-ai/agentscope
> - Documentation: <https://doc.agentscope.io/>
> - Runtime: https://github.com/agentscope-ai/agentscope-runtime
> - Studio: https://github.com/agentscope-ai/agentscope-studio

---

## 1. What is AgentScope

## 1.1 Core Positioning

```
AgentScope Positioning
│
├── Developer-Centric Agent Framework (Developer-Centric)
│   Not a low-code platform, emphasizing control and flexibility over code
│
├── Production-Ready
│   Built-in OTel tracing, runtime deployment, state management, sandbox execution
│
├── Designed for increasingly enhanced model capabilities
│   Leveraging model inference and tool invocation capabilities, rather than fixed orchestration constraints
│
└── Built-in Micro-Tuning Support (Agentic RL)
    Supports direct micro-tuning of Agent behavior through reinforcement learning
```

## 1.2 Design Philosophy

AgentScope's design philosophy differs fundamentally from frameworks like LangChain:

| Design Dimension | Traditional Frameworks (like LangChain) | AgentScope |
|---------|------------------------|------------|
| **Orchestration Concept** | Strict Chain/Graph orchestration, developers define each step | Trusting model inference capabilities, ReAct paradigm allows models to make autonomous decisions |
| **Asynchronous Support** | Partial support, requires explicit handling | Complete asynchronous architecture (native async/await) |
| **State Management** | Each component manages independently | Unified state interface (state_dict/load_state_dict) |
| **Tool Definition** | Requires specific decorators/Schemas | Any Python callable object is a tool |
| **Production Deployment** | Additional framework (e.g., FastAPI) | Built-in Runtime (AgentApp + FastAPI inheritance) |
| **Fine-tuning Capability** | No built-in support | Built-in Agentic RL fine-tuning |

## 1.3 Position within the Agent Framework Ecosystem

```
Agent Framework Ecosystem (2026)
│
├── General Orchestration Framework
│   ├── LangChain / LangGraph    - Most rich ecosystem, multi-level abstraction
│   ├── LlamaIndex               - Strongest RAG capabilities
│   └── Semantic Kernel           - Enterprise-grade, Microsoft .NET/Python
│
├── Multi-Agent Collaboration Framework
│   ├── AutoGen (Microsoft)        - Conversational workflow orchestration in Group Chat
│   ├── CrewAI                    - Role-playing, easy to use
│   └── AgentScope (Alibaba)     - Asynchronous native, production-grade, built-in fine-tuning ◄─ This series
│
├── Low-Code Platform
│   ├── Dify                      - Visual workflow
│   └── Coze / Coze - For non-technical users
│
└── Vertical Domain
    └── MetaGPT - Software development simulation
```

---

## 2. Core Features Overview

## 2.1 Feature Matrix

```
AgentScope Core Features
│
├── Foundation Capabilities (5-Minute Setup)
│   ├── ReAct Agent - Out-of-the-box reasoning and action agent
│   ├── Tool System - Any Python callable object as a tool + 7 built-in tools
│   ├── Human-in-the-Loop - Real-time intervention, interruption, recovery
│   ├── Memory Management - Short-term (InMemory/AsyncSQLAlchemy/Redis) + Long-term memory
│   ├── Planning Module - Subtask decomposition and management
│   ├── Real-time Speech - Voice input/output + TTS
│   ├── Evaluation Framework - ACEBench + OpenJudge
│   └── Model Fine-tuning - Agentic RL reinforcement learning
│
├── Scalability
│   ├── Ecosystem Integration - Large number of tools, memory, observability integration
│   ├── MCP Support - Native integration with Model Context Protocol
│   ├── A2A Support - Agent-to-Agent protocol
│   ├── MsgHub - Flexible multi-agent message orchestration
│   └── Pipeline - Sequential/parallel/routing/pass-through workflow
│
└── Production Ready
    ├── Local/Cloud/K8s Deployment     - Multiple deployment modes
    ├── Serverless Scalability   - On-demand scaling
    ├── OTel Observability          - Native tracing with OpenTelemetry
    ├── Sandbox Execution              - Secure isolated tool execution environment
    └── AgentScope Studio     - Visualization development and tracking tool
```

## 2.2 Four-Layer Core Module Architecture

AgentScope 1.0 abstracts the components required by the Agent application into four modules:

```
┌──────────────────────────────────────────────────────────┐
│                    Agent Application Layer                           │
│   ReActAgent / Custom Agent / Voice Agent / A2A Agent    │
├──────────────────────────────────────────────────────────┤
│              Agent Infrastructure Layer                              │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐    │
│  │ Message  │ │  Model   │ │  Memory  │ │   Tool   │    │
│  │ Message System  │ │ Model Interface  │ │ Memory Management  │ │ Toolkit System  │    │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘    │
├──────────────────────────────────────────────────────────┤
│              Workflow and Orchestration Layer                                │
│  MsgHub / Pipeline / Routing / Handoffs / Plan           │
├──────────────────────────────────────────────────────────┤
│              Engineering Support Layer                                    │
│  Runtime / Studio / Tracing / Evaluation / Sandbox       │
└──────────────────────────────────────────────────────────┘
```

---

## 3. Installation and Environment Setup

## 3.1 System Requirements

| Requirement | Description |
|------|------|
| **Python** | Version 3.10 or higher (recommended 3.11+, verified on 3.13) |
| **Operating System** | macOS / Linux / Windows |
| **Package Manager** | pip or uv |
| **Node.js** | Version 20.0.0+ (only needed for the AgentScope Studio visualization tool) |
| **Optional** | Docker / Podman (for sandbox execution and production deployment) |

## 3.2 Installation Methods

**Method One: Install from PyPI (recommended)**

```bash
# Base Installation
pip install agentscope

# Or use uv (faster)
uv pip install agentscope
```

**Method Two: Install Complete Dependencies**

```bash
# Additional dependencies that include all model APIs and utility functions
# macOS / Linux
pip install agentscope\[full\]

# Windows
pip install agentscope[full]
```

**Method Three: Install from Source Code (developer mode)**

```bash
# Clone the repository
git clone -b main https://github.com/agentscope-ai/agentscope.git
cd agentscope

# Install in editable mode
pip install -e .

# Or install development dependencies
pip install -e .[dev]
```

**Method Four: Install AgentScope Runtime (production deployment)**

```bash
# Runtime core
pip install agentscope-runtime

# Runtime + Extension
pip install "agentscope-runtime[ext]"
```

## 3.3 Full `agentscope` Core Dependency List

Following are the actual core dependencies installed for `agentscope[full]` v1.0.17 (based on Python 3.13 / Linux x86_64 verification):

| Category | Dependency Package | Version | Purpose |
|------|--------|------|------|
| **LLM Providers** | `openai` | 2.28.0 | OpenAI API client |
| | `anthropic` | 0.85.0 | Anthropic Claude API client |
| | `dashscope` | 1.25.14 | Alibaba Cloud DashScope (Qwen) API |
| **MCP Protocol** | `mcp` | 1.26.0 | MCP Protocol support |
| **Observability** | `opentelemetry-api` | 1.40.0 | OTel API |
| | `opentelemetry-sdk` | 1.40.0 | OTel SDK |
| | `opentelemetry-exporter-otlp` | 1.40.0 | OTel OTLP Exporter |
| **Data Processing** | `numpy` | 2.4.3 | Numerical Computing |
| | `tiktoken` | 0.12.0 | Token Counting (OpenAI tokenizer) |
| | `sqlalchemy` | 2.0.48 | Object-Relational Mapping (ORM) |
| **Asynchronous/IO** | `aiofiles` | 25.1.0 | Asynchronous File Operations |
| | `aioitertools` | 0.13.0 | Asynchronous Iteration Tools |
| | `python-socketio` | 5.16.1 | WebSocket Communication |
| **Tools** | `json5` / `json_repair` | 0.13.0 / 0.58.6 | Loose JSON Parsing + Auto Repair |
| | `docstring_parser` | 0.17.0 | Automatic Extraction of Tool Function Signatures |
| | `shortuuid` | 1.0.13 | Generation of Short UUIDs |
| **Audio** | `sounddevice` | 0.5.5 | Audio Input and Output for Voice Agents |

> The complete dependency tree includes approximately **242 packages**, listed here are only the core direct dependencies.

## 3.4 Verification of Installation

```python
import agentscope
print(agentscope.__version__)
# Output: 1.0.17 (or higher version)
```

## 3.5 Configuration of API Key

AgentScope supports multiple LLM providers and requires configuration of corresponding API Keys:

**DashScope (Alibaba Cloud Baileys/Tongyi Qianwen)**:

```bash
# Method 1: Environment variables
export DASHSCOPE_API_KEY="sk-your-dashscope-api-key"

# Method 2: Passing directly in code
# DashScopeChatModel(model_name="qwen-max", api_key="sk-xxx")
```

> Obtain DashScope API Key: <https://dashscope.console.aliyun.com/>

**OpenAI**:

```bash
export OPENAI_API_KEY="sk-your-openai-api-key"
```

**Local Models (Ollama)**:

```bash
# No API Key required, ensure Ollama service is running
ollama serve
ollama pull qwen2.5:7b
```

## 3.6 Installation of AgentScope Studio (Visual Tool)

AgentScope Studio is a **standalone visual development tool**, based on Node.js, which needs to be installed separately. It provides features such as Trace visualization, real-time interaction with Agents, and evaluation analysis.

> Official Repository: <https://github.com/agentscope-ai/agentscope-studio>

**Prerequisites:**

```bash
# Confirm Node.js version (must >= 20.0.0)
node --version   # 应显示 v20.x.x 或更高
npm --version    # 应显示 10.x.x 或更高
```

**RHEL / CentOS / Alibaba Cloud Linux Install Node.js**:

```bash
# Method 1: Official NodeSource source (recommended)
curl -fsSL https://rpm.nodesource.com/setup_20.x | bash -
yum install -y nodejs

# Method 2: Binary package (offline/accelerated)
cd /usr/local
curl -O https://nodejs.org/dist/v20.18.3/node-v20.18.3-linux-x64.tar.xz
tar xf node-v20.18.3-linux-x64.tar.xz
ln -sf /usr/local/node-v20.18.3-linux-x64/bin/{node,npm,npx} /usr/local/bin/
```

> **Note**: `yum install node` will return "No match", the correct package name is `nodejs`; but the default repository version is usually outdated, it is recommended to use the NodeSource source.

**Install C++ Compiler Toolchain** (native module `better-sqlite3` requires):

```bash
# Must be installed, otherwise npm install will report "g++: Command not found"
yum install -y gcc-c++ make
```

**Install Studio**:

```bash
# Domestic environment suggests using the Taobao mirror
npm config set registry https://registry.npmmirror.com

# Global installation
npm install -g @agentscope/studio
```

**Start Studio**:

```bash
# Frontend start (default listens on http://localhost:3000)
as_studio

# Backend run
nohup as_studio > /tmp/as_studio.log 2>&1 &
```

**Connect AgentScope App**:

In Python code, configure `studio_url`, Agent runtime data will be reported in real time to Studio:

```python
import agentscope

agentscope.init(
    # ...other configurations...
    studio_url="http://localhost:3000"
)
```

**Deploy Studio via Docker** (alternative solution):

``` bash
# 🟢 Low-risk: read-only/information gathering, typically with no side effects
# Domestic environments require configuration for image acceleration, direct connection to Docker Hub may timeout
# Podman users edit /etc/containers/registries.conf to add mirror
docker run -p 3000:3000 agentscope/studio:latest
```
**Troubleshoot Remote Access to Cloud Server (ECS)**:

If deployed on an Alibaba Cloud ECS, and the browser cannot access, check three levels:

| Troubleshooting Level | Check Command / Operation | Explanation |
|--------|----------------|------|
| **① Service Binding Address** | `ss -tlnp | grep 3000` | If shows `127.0.0.1:3000`, need to change to `as_studio --host 0.0.0.0` or `HOST=0.0.0.0 as_studio` |
| **② Alibaba Cloud Security Group** | ECS Console → Security Group → Add TCP/3000 inbound rule | This is the cloud platform-level firewall, **must be configured in the console** |
| **③ Operating System Firewall** | `firewall-cmd --add-port=3000/tcp --permanent && firewall-cmd --reload` | Operating system-level firewall |

---

## 4. Hello World: First Agent

## 4.1 Simplest Example — ReAct Agent Dialogue

```python
from agentscope.agent import ReActAgent, UserAgent
from agentscope.model import DashScopeChatModel
from agentscope.formatter import DashScopeChatFormatter
from agentscope.memory import InMemoryMemory
from agentscope.tool import Toolkit, execute_python_code, execute_shell_command
import os
import asyncio


async def main():
    # 1. Prepare tools
    toolkit = Toolkit()
    toolkit.register_tool_function(execute_python_code)
    toolkit.register_tool_function(execute_shell_command)

    # 2. Create ReAct Agent
    agent = ReActAgent(
        name="Friday",
        sys_prompt="You're a helpful assistant named Friday.",
        model=DashScopeChatModel(
            model_name="qwen-max",
            api_key=os.environ["DASHSCOPE_API_KEY"],
            stream=True,
        ),
        memory=InMemoryMemory(),
        formatter=DashScopeChatFormatter(),
        toolkit=toolkit,
    )

    # 3. Create User Agent (for terminal input reception)
    user = UserAgent(name="user")

    # 4. Dialogue loop
    msg = None
    while True:
        msg = await agent(msg)
        msg = await user(msg)
        if msg.get_text_content() == "exit":
            break


asyncio.run(main())
```

**Run Effect**:

```
user: Use Python to calculate 1+1
Friday: {
  "type": "tool_use",
  "name": "execute_python_code",
  "input": {"code": "print(1+1)", "timeout": 300}
}
system: {
  "type": "tool_result",
  "name": "execute_python_code",
  "output": [{"type": "text", "text": "<returncode>0</returncode><stdout>2\n</stdout>"}]
}
Friday: The result of 1+1 is 2.
user: exit
```

## 4.2 Using OpenAI Models

```python
from agentscope.model import OpenAIChatModel
from agentscope.formatter import OpenAIChatFormatter

agent = ReActAgent(
    name="Friday",
    sys_prompt="You're a helpful assistant named Friday.",
    model=OpenAIChatModel(
        model_name="gpt-4o",
        api_key=os.environ["OPENAI_API_KEY"],
        stream=True,
    ),
    memory=InMemoryMemory(),
    formatter=OpenAIChatFormatter(),
    toolkit=toolkit,
)
```

## 4.3 Using Local Models (Ollama)

```python
from agentscope.model import OllamaChatModel
from agentscope.formatter import OllamaChatFormatter

agent = ReActAgent(
    name="Friday",
    sys_prompt="You're a helpful assistant named Friday.",
    model=OllamaChatModel(
        model_name="qwen2.5:7b",
        # Ollama default address
        base_url="http://localhost:11434",
        stream=True,
    ),
    memory=InMemoryMemory(),
    formatter=OllamaChatFormatter(),
    toolkit=toolkit,
)
```

## 4.4 No-tool Simple Dialogue Agent

```python
from agentscope.agent import ReActAgent
from agentscope.model import DashScopeChatModel
from agentscope.formatter import DashScopeChatFormatter
from agentscope.memory import InMemoryMemory
from agentscope.message import Msg
import asyncio
import os


async def simple_chat():
    agent = ReActAgent(
        name="assistant"
        sys_prompt="you are a friendly chinese helper, skilled at answering various questions.",
        model=DashScopeChatModel(
            model_name="qwen-max",
            api_key=os.environ["DASHSCOPE_API_KEY"],
            stream=True,
        ),
        memory=InMemoryMemory(),
        formatter=DashScopeChatFormatter(),
    )

    # Direct message sending (non-interactively)
    msg = Msg(
        name="user",
        content="Please provide a brief introduction to the core components of Kubernetes",
        role="user",
    )

    response = await agent(msg)
    print(f"Agent reply: {response.get_text_content()}")


asyncio.run(simple_chat())
```

---

## 5. Project Structure and Ecosystem

## 5.1 AgentScope Project Matrix

```
AgentScope Ecosystem
│
├── agentscope (core framework)
│   ├── agentscope.agent      - Intelligent Body module (ReActAgent, UserAgent, AgentBase...)
│   ├── agentscope.model      - Model interface (DashScope, OpenAI, Ollama...)
│   ├── agentscope.memory     - Memory management (InMemoryMemory, AsyncSQLAlchemyMemory, RedisMemory)
│   ├── agentscope.tool       - Toolkit system (Toolkit, ToolResponse, 7 built-in tools)
│   ├── agentscope.message    - Message system (Msg)
│   ├── agentscope.formatter  - prompt formatter
│   ├── agentscope.pipeline   - orchestration pipeline (sequential/fanout_pipeline, stream_printing_messages)
│   ├── agentscope.mcp        - MCP protocol client (Http/StdIO)
│   └── agentscope.session    - session management (JSONSession)
│
├── agentscope-runtime (production runtime)
│   ├── AgentApp              - FastAPI-inherited Agent service
│   ├── Sandbox               - sandbox execution environment
│   ├── DeployManager         - deployment manager
│   └── Adapters              - multi-framework adapters
│
├── agentscope-studio (visualization tool)
│   ├── Tracing Visualization  - OpenTelemetry Trace visualization
│   ├── Project Management    - run management and configuration
│   └── Evaluation Interface  - Agent evaluation visualization
│
└── agentscope-samples (sample projects)
    ├── ReAct Agent Sample
    ├── Multi-Agent Werewolf Game
    ├── Deep Research Agent
    ├── Browser Automation Agent
    └── Agentic RL Fine-tuning Sample
```

## 5.2 Relationship with Existing Topics

| Series Document | Corresponding Topic Existing Content | Relationship Explanation |
|-----------|----------------|---------|
| 16 - Overview and Installation | [03 - Framework Comparison](./03-agent-frameworks-comparison.md) | Deep exploration of AgentScope in framework comparison |
| 17 - Core Concepts | [01 - Agent Basics](./01-ai-agent-fundamentals.md) | Specific implementation of general Agent concepts by AgentScope |
| 18 - Toolkit System | [05 - Tool Usage](./05-tool-use-function-calling.md) | Implementation of tool calling by AgentScope and integration with MCP |
| 19 - Memory Management | [07 - Memory Context Management](./07-memory-context-management.md) | Specific scheme of memory/contexts by AgentScope |
| 20 - Multi-Agent | [06 - Multi-Agent Orchestration](./06-multi-agent-orchestration.md) | AgentScope MsgHub/Pipeline Orchestration Practice |
| 21 - Advanced Features | [04 - RAG](./04-rag-knowledge-retrieval.md) | AgentScope RAG, Evaluation, RL Tuning, etc. Advanced |
| 22 - Production Deployment | [09 - Production Deployment Guide](./09-production-deployment-guide.md) | AgentScope Runtime's K8s Deployment Practice |

---

## 6. List of Built-in Tools

AgentScope includes utility functions, which can be registered via `toolkit.register_tool_function()`:

| Tool Function | Module | Functionality |
|---------|------|------|
| `execute_python_code` | `agentscope.tool` | Execute Python Code |
| `execute_shell_command` | `agentscope.tool` | Execute Shell Command |
| `view_text_file` | `agentscope.tool` | View Text File Content |
| `write_text_file` | `agentscope.tool` | Write to Text File |
| `insert_text_file` | `agentscope.tool` | Insert Content at a Specific Position in a Text File |
| `dashscope_text_to_image` | `agentscope.tool` | DashScope Text-to-Image |
| `openai_text_to_image` | `agentscope.tool` | OpenAI DALL·E Text-to-Image |

> See [18 - Tool System and MCP Integration](./18-agentscope-tool-system.md).

---

## 7. Quick Troubleshooting

## 7.1 Common Installation Issues

**Core Installation Issues for AgentScope**:

| Issue | Reason | Solution |
|------|------|--------|
| `ModuleNotFoundError: No module named 'agentscope'` | Incorrect installation | Run `pip install agentscope` |
| `Python version < 3.10` | Version requirements not met | Upgrade Python to 3.10+; recommended with pyenv management |
| `ImportError: cannot import name 'ReActAgent'` | Outdated version | Run `pip install --upgrade agentscope` |
| Authentication failure for DashScope API | Invalid or missing API key | Check the `DASHSCOPE_API_KEY` environment variable |
| Connection timeout for OpenAI API | Network issues | Configure proxies or use `base_url` for transit addresses |
| `extras` installation fails (macOS) | shell escaping issue | Use `pip install agentscope\[full\]` (backslash escaping) |

**AgentScope Studio Installation Issues**:

| Issue | Reason | Solution |
|------|------|--------|
| `yum install node` → No match | Package name error | Correct package name is `nodejs`, but it's recommended to install v20+ using NodeSource repository |
| `npm install` → `g++: Command not found` | Missing C++ compiler | `yum install -y gcc-c++ make` (better-sqlite3 requires compilation) |
| `docker pull` → `dial tcp ... i/o timeout` | Docker Hub cannot be accessed from China | Configure mirror acceleration or use `npm install -g @agentscope/studio` |
| Studio starts but cannot access the internet from outside | Default binds to `127.0.0.1` | `as_studio --host 0.0.0.0` + Security group rule + Firewall rule |
| ECS public IP cannot access port 3000 | Alibaba Cloud Security Group not configured | ECS console → Security Group → Inbound Rules → Add TCP/3000 rule |

## 7.2 Recommended Development Environment

```bash
# Recommended to use pyenv + virtualenv
pyenv install 3.11.9
pyenv virtualenv 3.11.9 agentscope-env
pyenv activate agentscope-env

# Install AgentScope
pip install agentscope\[full\]

# Verify
python -c "import agentscope; print(agentscope.__version__)"
```

---

## 8. Best Practices and Anti-patterns

## Best Practices

- **Start with ReActAgent**: The core component of AgentScope, ReActAgent, should be mastered before expanding
- **Manage API Keys via Environment Variables**: Avoid hardcoding keys in code; use `os.environ` or `.env` files
- **Prioritize DashScope**: AgentScope integrates most deeply with Alibaba Cloud DashScope, and Qwen series models have the best compatibility
- **Use stream=True**: Always enable streaming output in production environments for better user experience and response speed
- **Install full dependencies**: During development, it's recommended to install `agentscope[full]` to avoid missing dependencies causing functionality gaps

## Anti-patterns

- **Ignore asynchronous design**: AgentScope natively supports async, don't wrap with `sync` wrapper to bypass `async/await`
- **Skip version validation**: Don't skip version validation after installation, which can lead to incompatible APIs
- **Mix Formatter and Model**: DashScopeChatModel must be paired with DashScopeChatFormatter; mixing them will result in format errors
- **Use InMemoryMemory in production**: In-memory memory doesn't persist across restarts; use `AsyncSQLAlchemyMemory` (PostgreSQL/SQLite) or `RedisMemory` in production

---

## Related Documentation

| Document | Related Content |
|------|---------|
| [17 - Core Concepts and Basic Operations](./17-agentscope-core-concepts.md) | Detailed explanations of Agent, Message, Model, and Formatter |
| [18 - Tool System and MCP Integration](./18-agentscope-tool-system.md) | Toolkit, MCP, custom tools |
| [03 - Mainstream Agent Framework Comparison](./03-agent-frameworks-comparison.md) | AgentScope vs LangChain/AutoGen/CrewAI |
| [01 - AI Agent Basics and Core Architecture](./01-ai-agent-fundamentals.md) | General Concepts and Inference Framework for Agents |

---

*This document is original content for the kudig-database project's 02-ai-agents topic. *

---

## Obsidian Documentation

- 02-ai-agents KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|AI Agent Topic Overview]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|AI Agent Basics and Core Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|Selection and Evaluation of LLM Foundation Models]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Deep Dive into Mainstream Agent Framework Comparisons]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|RAG Knowledge Retrieval Deep Guide]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Design Guidelines for Tool Usage and Function Calling]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Multi-Agent Orchestration and Collaboration Architectures]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation System and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]

## See Also

- 14-agent-kudig-design-strategy
- 15-agent-corpus-gap-analysis
- 17-agentscope-core-concepts
- 18-agentscope-tool-system

## Related

- [[deep-dive|#deep-dive Hub]] — tag hub


<!-- risk-assessed -->
