---
title: Microsoft AutoGen Multi-Agent Framework In-Depth Guide
description: 'Comprehensive analysis of AutoGen ConversableAgent architecture, covering GroupChat multi-agent conversations, code execution sandboxes, nested conversations, AutoGen Studio, and Semantic Kernel integration'
summary: 'Comprehensive analysis of AutoGen ConversableAgent architecture'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- autogen
- microsoft
- multi-agent
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
- What is Microsoft AutoGen
- How to use Microsoft AutoGen
- AutoGen GroupChat multi-agent conversations
trigger_keywords:
- autogen
- conversable-agent
- group-chat
- code-executor
- semantic-kernel
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/04-autogen-microsoft-agent.md
---
> **Production Environment Security Notice**
>
> This document contains operational commands that can be executed directly. Before executing, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether validation has been performed in a non-production environment. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (will modify cluster state, but is generally reversible), 🟢 Low Risk/Read-Only (information gathering, no side effects).


# Microsoft AutoGen Multi-Agent Framework In-Depth Guide

## 1. AutoGen Architecture Overview

### 1.1 Design Philosophy

AutoGen is an open-source multi-agent conversation framework from Microsoft. Its core concept is **collaboration through conversation**. Unlike LangGraph's state machine, AutoGen models inter-agent interactions as **Conversations**, where agents accomplish tasks through message passing.

```
┌─────────────────────────────────────────────────┐
│                AutoGen Architecture              │
│                                                  │
│  ┌──────────────────────────────────────────┐    │
│  │         ConversableAgent (Base Class)    │    │
│  │  ┌────────┐ ┌────────┐ ┌──────────────┐  │    │
│  │  │ System │ │ LLM    │ │ Code         │  │    │
│  │  │ Prompt │ │ Config │ │ Executor     │  │    │
│  │  └────────┘ └────────┘ └──────────────┘  │    │
│  └───────────────┬──────────────────────────┘    │
│                  │                               │
│    ┌─────────────┼─────────────┐                 │
│    ↓             ↓             ↓                 │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐         │
│  │Assistant │ │UserProxy │ │ GroupChat│         │
│  │Agent     │ │Agent     │ │ Manager  │         │
│  └──────────┘ └──────────┘ └──────────┘         │
└─────────────────────────────────────────────────┘
```

### 1.2 Core Components

| Component | Responsibility | Typical Use |
|------|------|---------|
| ConversableAgent | Base class for all Agents | Custom Agents |
| AssistantAgent | LLM-driven conversational Agent | Code generation, reasoning |
| UserProxyAgent | Proxies user input and code execution | Human-computer interaction, tool invocation |
| GroupChat | Multi-agent group chat | Complex collaborative scenarios |
| GroupChatManager | Manages group chat flow | Automatic message routing |

---

## 2. ConversableAgent Architecture

### 2.1 Basic Agent Definition

```python
from autogen import ConversableAgent, AssistantAgent, UserProxyAgent

# LLM configuration
llm_config = {
    "model": "gpt-4o",
    "api_key": os.environ["OPENAI_API_KEY"],
    "temperature": 0,
    "cache_seed": None,  # Disable cache for production
}

# Assistant Agent (LLM-driven)
assistant = AssistantAgent(
    name="k8s_expert",
    system_message=(
        "You are a Kubernetes cluster diagnostics expert.\n"
        "You have the following capabilities:\n"
        "1. Analyze abnormal Pod states\n"
        "2. Interpret cluster events\n"
        "3. Generate remediation commands\n\n"
        "When delivering the final diagnostic conclusion, end the conversation with TERMINATE."
    ),
    llm_config=llm_config,
)

# User Proxy Agent (proxies the user and executes code)
user_proxy = UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",  # No human input required
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "./workspace",
        "use_docker": "python:3.11-slim",  # Docker sandbox execution
        "timeout": 120,
    },
)
```

### 2.2 Two-Agent Conversation

```python
# Simplest conversation pattern: Assistant ↔ UserProxy
result = user_proxy.initiate_chat(
    assistant,
    message=(
        "The Pod under the nginx-deployment in the default namespace keeps CrashLoopBackOff. "
        "Please help me diagnose the problem and provide a remediation plan."
    ),
    max_turns=8,
)

# View conversation history
for msg in result.chat_history:
    print(f"[{msg['role']}] {msg['content'][:200]}")

# Get summary
print(f"Summary: {result.summary}")
print(f"Total Tokens: {result.cost}")
```

### 2.3 Custom ConversableAgent

```python
from autogen import ConversableAgent

class K8sDiagnosticAgent(ConversableAgent):
    """Custom K8s Diagnostic Agent."""

    DEFAULT_SYSTEM_MESSAGE = (
        "You are KuDig's K8s diagnostics expert. "
        "Use kubectl tools to query cluster state and analyze root causes."
    )

    def __init__(self, name="k8s_diagnostician", **kwargs):
        super().__init__(
            name=name,
            system_message=kwargs.pop(
                "system_message", self.DEFAULT_SYSTEM_MESSAGE
            ),
            **kwargs,
        )
        self._register_tools()

    def _register_tools(self):
        """Register K8s tools."""

        def get_pod_status(namespace: str, pod_name: str = "") -> str:
            """Query Pod status."""
            import subprocess
            cmd = ["kubectl", "get", "pods", "-n", namespace, "-o", "wide"]
            if pod_name:
                cmd = ["kubectl", "get", "pod", pod_name, "-n", namespace, "-o", "yaml"]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return result.stdout

        def get_events(namespace: str) -> str:
            """Get namespace events."""
            import subprocess
            result = subprocess.run(
                ["kubectl", "get", "events", "-n", namespace,
                 "--sort-by=.lastTimestamp"],
                capture_output=True, text=True, timeout=30
            )
            return result.stdout

        # Register as function calls
        self.register_for_llm(
            name="get_pod_status",
            description="Query Pod status in the specified namespace",
        )(get_pod_status)

        self.register_for_llm(
            name="get_events",
            description="Get the list of events in a namespace",
        )(get_events)
```

---

## 3. GroupChat Multi-Agent Conversation

### 3.1 Basic Group Chat

```python
from autogen import GroupChat, GroupChatManager

# Define multiple specialized Agents
diagnostician = AssistantAgent(
    name="diagnostician",
    system_message="You are a diagnostics expert responsible for analyzing root causes.",
    llm_config=llm_config,
)

fixer = AssistantAgent(
    name="fixer",
    system_message="You are a remediation engineer responsible for formulating and executing remediation plans.",
    llm_config=llm_config,
)

validator = AssistantAgent(
    name="validator",
    system_message="You are a validation engineer responsible for verifying whether the fix was successful.",
    llm_config=llm_config,
)

# GroupChat configuration
group_chat = GroupChat(
    agents=[user_proxy, diagnostician, fixer, validator],
    messages=[],
    max_round=20,
    speaker_selection_method="auto",  # Automatically select the next speaker
    # speaker_selection_method="round_robin",  # Round-robin
    # speaker_selection_method="random",        # Random
    # speaker_selection_method="manual",        # Manual
    allow_repeat_speaker=False,  # Do not allow consecutive speaking
)

# GroupChatManager manages the conversation
manager = GroupChatManager(
    groupchat=group_chat,
    llm_config=llm_config,
)

# Start the group chat
user_proxy.initiate_chat(
    manager,
    message="Pod nginx-abc123 has OOMKilled. Please have the team collaborate to investigate.",
)
```

### 3.2 Custom Speaker Selection

```python
def custom_speaker_selection(last_speaker, group_chat):
    """Custom speaker selection logic."""
    messages = group_chat.messages

    if len(messages) == 0:
        return user_proxy  # First speaker

    last_msg = messages[-1]["content"]

    # After diagnosis is complete → remediation engineer
    if "root cause" in last_msg and last_speaker == diagnostician:
        return fixer

    # After fix is complete → validation engineer
    if "fix complete" in last_msg and last_speaker == fixer:
        return validator

    # Validation failed → back to diagnostics
    if "validation failed" in last_msg:
        return diagnostician

    # Default: diagnostics expert speaks
    return diagnostician

group_chat = GroupChat(
    agents=[user_proxy, diagnostician, fixer, validator],
    messages=[],
    max_round=20,
    speaker_selection_method=custom_speaker_selection,
)
```

### 3.3 Nested Chat

Agents can initiate sub-conversations internally to handle complex sub-tasks:

```python
# Nested conversation for the diagnostics Agent: querying the knowledge base
from autogen import AssistantAgent

knowledge_agent = AssistantAgent(
    name="knowledge_base",
    system_message="You are a K8s knowledge base assistant that provides documentation queries.",
    llm_config=llm_config,
)

# Register nested chat for the diagnostics Agent
diagnostician.register_nested_chats(
    [
        {
            "recipient": knowledge_agent,
            "message": lambda recipient, messages, sender, config: (
                f"Query related documentation for the following issue: {messages[-1]['content']}"
            ),
            "summary_method": "last_msg",
            "max_turns": 2,
        }
    ],
    trigger=lambda sender: sender != knowledge_agent,  # Avoid recursion
)
```

---
## 4. Code Execution Sandbox

### 4.1 Docker Sandbox (Recommended)

```python
user_proxy = UserProxyAgent(
    name="executor",
    code_execution_config={
        "use_docker": "python:3.11-slim",  # Use Docker image
        "work_dir": "/workspace",
        "timeout": 120,
        "last_n_messages": 3,  # Check code in the last N messages
    },
)

# Custom Docker image (includes kubectl)
docker_config = {
    "use_docker": "custom-k8s-agent:latest",
    "work_dir": "/workspace",
    "timeout": 180,
    "docker_volume": "/tmp/autogen-workspace",
    "docker_network": "autogen-network",
}
```

```dockerfile
# Dockerfile for code execution sandbox
FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl jq
RUN curl -LO "https://dl.k8s.io/release/$(curl -Ls \
    https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    chmod +x kubectl && mv kubectl /usr/local/bin/

WORKDIR /workspace
```

### 4.2 Local Execution (Not Recommended for Production)

```python
user_proxy = UserProxyAgent(
    name="executor",
    code_execution_config={
        "use_docker": False,  # Local execution
        "work_dir": "/tmp/autogen-workspace",
        "timeout": 60,
    },
)
```

### 4.3 Disable Code Execution

```python
# Conversation-only mode, no code execution
user_proxy = UserProxyAgent(
    name="user",
    code_execution_config=False,  # Disable code execution
    human_input_mode="ALWAYS",    # Wait for human input each round
)
```

---

## 5. AutoGen Studio

### 5.1 Installation and Startup

``` bash
# 🟢 Low risk: read-only/information gathering, usually no side effects
# Install
pip install autogenstudio

# Start Web UI
autogenstudio ui --port 8080 --host 0.0.0.0

# Docker startup
docker run -p 8080:8080 \
    -e OPENAI_API_KEY=$OPENAI_API_KEY \
    ghcr.io/microsoft/autogen/autogenstudio:latest
```
### 5.2 Studio Features

AutoGen Studio provides:
- **Visual Agent Editor**: Drag-and-drop creation and configuration of Agents
- **Skill Management**: Define and test Agent skills (function calls)
- **Session Management**: Create, monitor, and debug Agent conversations
- **Evaluation Dashboard**: Run benchmark tests to evaluate Agent performance
- **API Exposure**: Integrate into external systems via REST API

### 5.3 K8s Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: autogen-studio
spec:
  replicas: 1
  selector:
    matchLabels:
      app: autogen-studio
  template:
    metadata:
      labels:
        app: autogen-studio
    spec:
      containers:
        - name: studio
          image: ghcr.io/microsoft/autogen/autogenstudio:latest
          ports:
            - containerPort: 8080
          env:
            - name: OPENAI_API_KEY
              valueFrom:
                secretKeyRef:
                  name: llm-secrets
                  key: openai-api-key
          resources:
            requests:
              cpu: "500m"
              memory: "512Mi"
            limits:
              cpu: "1000m"
              memory: "2Gi"
---
apiVersion: v1
kind: Service
metadata:
  name: autogen-studio
spec:
  selector:
    app: autogen-studio
  ports:
    - port: 80
      targetPort: 8080
```

---

## 6. Integration with Semantic Kernel

### 6.1 Integration Pattern

AutoGen and Semantic Kernel can be used in a complementary manner:

```python
import semantic_kernel as sk
from autogen import AssistantAgent

# Semantic Kernel provides plugins and functions
kernel = sk.Kernel()
kernel.add_plugin(K8sPlugin(), "k8s")

# AutoGen provides multi-agent conversation
class SKPoweredAgent(AssistantAgent):
    """Agent powered by Semantic Kernel."""

    def __init__(self, kernel: sk.Kernel, **kwargs):
        super().__init__(**kwargs)
        self.kernel = kernel

    def generate_reply(self, messages, sender, **kwargs):
        # Use Semantic Kernel to execute functions
        last_msg = messages[-1]["content"]

        if "query Pod" in last_msg:
            # Call SK plugin
            result = asyncio.run(
                self.kernel.invoke(
                    plugin_name="k8s",
                    function_name="get_pod_status",
                    namespace="default",
                )
            )
            return str(result)

        # Fall back to LLM conversation
        return super().generate_reply(messages, sender, **kwargs)
```

### 6.2 SK Agent and AutoGen Conversation

```python
from semantic_kernel.agents import ChatCompletionAgent
from autogen import GroupChat, GroupChatManager

# Semantic Kernel Agent
sk_agent = ChatCompletionAgent(
    service_id="default",
    kernel=kernel,
    name="sk_k8s_expert",
    instructions="You are a K8s expert who uses SK plugins to query the cluster.",
)

# AutoGen Agent
autogen_agent = AssistantAgent(
    name="autogen_analyst",
    system_message="You are an analysis expert responsible for synthesizing information.",
    llm_config=llm_config,
)

# Bridge via an intermediate layer
class AgentBridge:
    """Bridge between SK Agent and AutoGen."""

    def __init__(self, sk_agent, autogen_agent):
        self.sk_agent = sk_agent
        self.autogen_agent = autogen_agent

    async def process(self, query: str):
        # SK Agent retrieves data
        sk_result = await self.sk_agent.invoke(query)

        # AutoGen Agent analyzes
        autogen_result = self.autogen_agent.generate_reply(
            [{"role": "user", "content": f"Analyze the following data:\n{sk_result}"}],
            sender=None,
        )

        return autogen_result
```

---
## 7. Production Best Practices

### 7.1 Conversation Control

```python
# Limit the number of conversation turns
result = user_proxy.initiate_chat(
    assistant,
    message=query,
    max_turns=8,
    summary_method="last_msg",  # Summary method: last_msg/llm/all
)

# Set termination conditions
def is_termination(msg):
    content = msg.get("content", "")
    return (
        "TERMINATE" in content or
        "Task complete" in content or
        len(content) == 0
    )
```

### 7.2 Error Handling

```python
from autogen import ConversableAgent

# Configure retries
llm_config_with_retry = {
    "model": "gpt-4o",
    "api_key": os.environ["OPENAI_API_KEY"],
    "temperature": 0,
    "max_retries": 3,
    "retry_wait_time": 1,
    "retry_exponential_base": 2,
    "timeout": 60,
}
```

### 7.3 Cost Control

```python
# Use a smaller model for simple tasks
simple_config = {"model": "gpt-4o-mini", "api_key": "..."}

# Use a larger model for complex tasks
complex_config = {"model": "gpt-4o", "api_key": "..."}

# Assign models per Agent
simple_agent = AssistantAgent(
    name="formatter",
    system_message="You are a formatting assistant.",
    llm_config=simple_config,  # Small model
)

complex_agent = AssistantAgent(
    name="reasoner",
    system_message="You are a reasoning expert.",
    llm_config=complex_config,  # Large model
)
```

---

## Related

- [[domain-14-ai-ml-infra/03-agent-runtime/01-langchain-langgraph-deep-dive|LangChain/LangGraph Deep Dive Guide]]
- [[domain-14-ai-ml-infra/03-agent-runtime/06-semantic-kernel-enterprise|Semantic Kernel Enterprise Agent]]

## See Also

- [[domain-14-ai-ml-infra/03-agent-runtime/07-agent-framework-selection-guide|Agent Framework Selection Decision Tree]]


<!-- risk-assessed -->
