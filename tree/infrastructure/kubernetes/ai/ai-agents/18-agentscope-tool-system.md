---
title: AgentScope Tool System Integration with MCP (domain-14-ai-ml-infra)
description: 'description: ''**Document Type**: Tool Development Topic | **Last Updated**: 2026-03 | **Keywords**: AgentScope,
  Toolkit,'
summary: 'description: ''**Document Type**: Tool Development Topic | **Last Updated**: 2026-03 | **Keywords**: AgentScope,
  Toolkit,'
category: general
tags:
- ai
- ai-agent
- prometheus
- postgresql
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
- What is AgentScope Tool System Integration with MCP
- How to integrate AgentScope Tool System with MCP
- Best Practices for Kubernetes 14 AI ML Infra
trigger_keywords:
- AgentScope
- What is integration
- MCP
- Integration with
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- prometheus-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/18-agentscope-tool-system.md
---

> **Production Environment Security Reminders**
>
> Commands included in this document are executable directly. Please confirm before execution: that the target cluster and namespace are correct; that you have sufficient RBAC permissions; and that the commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/ReadOnly (information gathering with no side effects).




title: AgentScope Tool System and MCP Integration
description: '**Document Type**: Tool Development Topic | **Last Updated**: 2026-03 | **Keywords**: AgentScope, Toolkit,
  Tool Registration, MCP, Model Context Protocol, Function Calling, Parallel Tool Invocation, Agent [[SKILL|Skill]], Meta Tool,
  Custom Tool'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- [[Prometheus|prometheus]]
- postgresql
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- Architect
- SRE
estimated_read_time: 5min
intent_queries:
- What is AgentScope Tool System and MCP Integration
- How to integrate AgentScope Tool System and MCP
trigger_keywords:
- AgentScope
- System integration
- MCP
- Integration
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

# AgentScope Tool System and MCP Integration

> **Document Type**: Tool Development Topic | **Last Updated**: 2026-03 | **Keywords**: AgentScope, Toolkit, Tool Registration, MCP, Model Context Protocol, Function Calling, Parallel Tool Invocation, Agent Skill, Meta Tool, Custom Tool

---

## Overview

The AgentScope tool system is crucial for transitioning an agent from a "conversation assistant" to an "autonomous executor." The design of the AgentScope tool system is extremely flexible—**any callable Python object can be used as a tool**, without requiring specific decorators or Schema definitions. It also natively supports the MCP (Model Context Protocol) protocol, allowing seamless integration with external tool services.

This document delves into the registration mechanism of the AgentScope tool system, its built-in tools, MCP integration, parallel invocation, Meta Tool, and practices for custom tool development tailored for Kubernetes operations.

---

## 1. Tool System Design Philosophy

## 1.1 "All Callable Objects Are Tools"

In AgentScope, a "tool" is defined very broadly:

```
AgentScope supported tool types
│
├── Function (function)
├── Partial function (functools.partial)
├── Instance method (instance method)
├── Class method (classmethod)
├── Static method (staticmethod)
└── Callable instance with __call__ method
```

And each tool can be:

```
Call mode
├── Synchronous (sync)   or Asynchronous (async)
├── Stream or Non-stream
└── Stateful or Stateless
```

## 1.2 Comparison with Other Frameworks' Tool Definitions

| Framework | Definition Method | Complexity |
|------|------------|--------|
| LangChain | Requires `@tool` decorator or `StructuredTool` + Pydantic Schema | Moderate |
| AutoGen | Registered through functions or `register_for_execution` | Moderate |
| CrewAI | inherit from `BaseTool` or `@tool` decorator | Medium |
| **AgentScope** | **register any callable object directly without a decorator** | **most concise** |

---

## 2. Toolkit — Tool Registration Center

## 2.1 Basic Usage

```python
from agentscope.tool import Toolkit, ToolResponse
import os


# Define utility functions - prefer ToolResponse as return value
def get_weather(city: str) -> ToolResponse:
    """Get weather information for a specified city.

    Args:
        city: city name, such as "Beijing", "Shanghai"

    Returns:
        天气信息
    """
    # Actual implementation: call weather API
    return ToolResponse(text=f"{city} Today's weather: sunny, temperature 25°C")


def calculate(expression: str) -> str:
    """Calculate mathematical expressions.

    Args:
        expression: 数学表达式，如 "2 + 3 * 4"

    Returns:
        计算结果
    """
    try:
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Calculation error: {e}"


# Register tool
toolkit = Toolkit()
toolkit.register_tool_function(get_weather)
toolkit.register_tool_function(calculate)

# Use preset_kwargs to hide sensitive parameters (e.g., API Key), LLM unaware of these parameters
toolkit.register_tool_function(
    get_weather,
    preset_kwargs={"api_key": os.environ["WEATHER_API_KEY"]},
)

# Pass to Agent
agent = ReActAgent(
    name="Assistant",
    toolkit=toolkit,
    ...
)
```

> **Key Points**:
> - AgentScope generates tool descriptions (JSON Schema) by inspecting the **docstring** and **type hints** of the tool function, which should be clear to the LLM.
> - Tool functions are recommended to return `ToolResponse` instead of `str`. `ToolResponse` supports multiple content types like `text`, `image_url`, etc.
> - Using `preset_kwargs` can pre-set sensitive parameters like API keys into the tool, avoiding them from being exposed in the JSON Schema.

## 2.2 Asynchronous Tools

```python
import aiohttp


async def async_fetch_url(url: str) -> str:
    """Asynchronously get URL content.

    Args:
        url: 要获取的 URL 地址

    Returns:
        URL 页面内容
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


toolkit = Toolkit()
toolkit.register_tool_function(async_fetch_url)
```

## 2.3 Stream Tools

```python
from typing import AsyncGenerator


async def stream_log_tail(
    pod_name: str,
    namespace: str = "default",
    lines: int = 100,
) -> AsyncGenerator[str, None]:
    """Streamline getting Pod logs.

    Args:
        pod_name: Pod 名称
        namespace: 命名空间
        lines: 获取的日志行数

    Yields:
        日志行内容
    """
    import asyncio
    process = await asyncio.create_subprocess_exec(
        "kubectl", "logs", pod_name, "-n", namespace,
        f"--tail={lines}", "-f",
        stdout=asyncio.subprocess.PIPE,
    )
    async for line in process.stdout:
        yield line.decode().strip()


toolkit = Toolkit()
toolkit.register_tool_function(stream_log_tail)
```

## 2.4 Partial Functions and Callable Objects

```python
from functools import partial


def kubectl_command(verb: str, resource: str, name: str, namespace: str = "default") -> str:
    """Execute kubectl command"""
    import subprocess
    cmd = ["kubectl", verb, resource, name, "-n", namespace]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"


# Use partial function to create specific tools
kubectl_get = partial(kubectl_command, verb="get")
kubectl_describe = partial(kubectl_command, verb="describe")

toolkit = Toolkit()
toolkit.register_tool_function(kubectl_get)
toolkit.register_tool_function(kubectl_describe)
```

```python
# Callable objects as tools
class DatabaseQuery:
    """Database query tool"""

    def __init__(self, connection_string: str):
        self.conn_str = connection_string

    async def __call__(self, sql: str) -> str:
        """Execute SQL queries.

        Args:
            sql: SQL 查询语句（只读）

        Returns:
            查询结果
        """
        # Actual implementation: execute SQL queries
        return f"Query result for: {sql}"


db_query = DatabaseQuery("postgresql://localhost:5432/k8s_metrics")
toolkit = Toolkit()
toolkit.register_tool_function(db_query)
```

---

## 3. Built-in Tools

AgentScope provides various built-in tool functions out of the box:

| Tool Function | Purpose | Notes |
|---------|------|--------|
| `execute_python_code` | Execute Python code | Must run in a sandbox in production environments |
| `execute_shell_command` | Execute shell commands | Must run in a sandbox in production environments |
| `view_text_file` | View contents of a text file | Read-only operation |
| `write_text_file` | Write to a text file | Requires file system permissions |
| `insert_text_file` | Insert content at a specific position in a file | Precise editing scenarios |
| `dashscope_text_to_image` | Text-to-image generation using DAWNSOUL | Requires a DashScope API key |
| `openai_text_to_image` | Text-to-image generation using DALL-E | Requires an OpenAI API key |

## 3.1 Code Execution

```python
from agentscope.tool import (
    execute_python_code,
    execute_shell_command,
    view_text_file,
    write_text_file,
    Toolkit,
)

toolkit = Toolkit()
toolkit.register_tool_function(execute_python_code)
toolkit.register_tool_function(execute_shell_command)
toolkit.register_tool_function(view_text_file)
toolkit.register_tool_function(write_text_file)
```

**execute_python_code**:

```python
# Example of Agent invocation
# Input: {"code": "import math; print(math.pi)", "timeout": 300}
# Output: "<returncode>0</returncode><stdout>3.141592653589793\n</stdout>"
```

**execute_shell_command**:

```python
# Example of Agent invocation
# Input: {"command": "kubectl get pods -n production"}
# Output: Result of command execution
```

> **Security Warning**: In production environments, code execution tools should run in a **sandbox**. AgentScope Runtime provides a secure sandbox environment, see [22 - Production Deployment](./deployment.md|22-agentscope-production-deployment)].

---

## 4. Dynamic JSON Schema Extension

AgentScope supports dynamically extending the JSON Schema of tools using Pydantic models, such as adding a **Chain-of-Thought** field during tool invocation:

```python
from pydantic import BaseModel, Field
from agentscope.tool import Toolkit


class CoTThinking(BaseModel):
    """Chain-of-thought extension - have LLM output reasoning steps before calling tools"""
    thinking: str = Field(description="Thinking process before tool invocation")


toolkit = Toolkit()
toolkit.register_tool_function(kubectl_get_pods)

# Dynamically inject CoT thinking field into JSON Schema of all tools
toolkit.set_extended_model(CoTThinking)
```

After this, the generated tool call by the LLM will include an additional `thinking` field:

```json
{
  "type": "tool_use",
  "name": "kubectl_get_pods",
  "input": {
    "thinking": "Pod Pending issue needs to first check the Pod list for status...",
    "namespace": "production",
    "label_selector": "app=nginx"
  }
}
```

> **Applicable Scenarios**: Debugging the inference process of the agent, production scenarios requiring explainability, collecting training data for Agentic RL.

---

## 5. Tool Interruption Support

When a user sends a real-time interruption, the tool currently executing receives an `asyncio.CancelledError`. The tool can gracefully handle the interruption:

```python
import asyncio
from agentscope.tool import ToolResponse


async def long_running_analysis(
    namespace: str,
    depth: str = "full",
) -> ToolResponse:
    """Execute deep cluster analysis (may take a long time).

    Args:
        namespace: 目标命名空间
        depth: 分析深度，"quick" 或 "full"
    """
    results = []
    try:
        # Step 1: Collect Pod information
        pod_info = await collect_pod_info(namespace)
        results.append(pod_info)

        # Step 2: Collect node information
        node_info = await collect_node_info()
        results.append(node_info)

        # Step 3: Resource analysis...
        analysis = await run_analysis(results)
        return ToolResponse(text=analysis)

    except asyncio.CancelledError:
        # Gracefully handle interruptions — return partially completed results
        partial = "\n".join(results) if results else "Analysis not started"
        return ToolResponse(
            text=f"Analysis interrupted. Completed results:\n{partial}",
            is_interrupted=True,  # 标记为中断状态
        )
```

> **Note**: Tools functions must explicitly capture `asyncio.CancelledError`. Failure to do so will force the tool to be canceled, returning an empty result. Setting `is_interrupted=True` informs the Agent that the tool has been interrupted, allowing it to continue processing new user instructions.

---

## 6. Parallel Tool Invocation

## 4.1 Enabling Parallel Invocation

```python
agent = ReActAgent(
    name="K8s-Expert",
    parallel_tool_calls=True,   # 启用并行工具调用
    toolkit=toolkit,
    ...
)
```

When the LLM generates multiple tool calls during a single inference, AgentScope executes them concurrently:

```
Sequential execution (parallel_tool_calls=False):
  get_pods() ──► describe_pod() ──► get_events()
  Total duration: t1 + t2 + t3

Parallel execution (parallel_tool_calls=True):
  get_pods()     ──►
  describe_pod() ──►  (parallel execution, take longest duration)
  get_events()   ──►
  Total time: max(t1, t2, t3)
```

## 4.2 Applicable Scenarios

| Scenario | Parallel Suitable | Reason |
|------|------------|------|
| Simultaneous resource status queries | Suitable | Each query is independent and has no dependencies |
| Get Pod list first then describe | Unsuitable | The latter depends on the result of the former |
| Simultaneous CPU + Memory + Disk checks | Suitable | Monitoring metrics collection is independent |
| Execute repair operations | Unsuitable | Sequential validation of each step's results is required |

---

## 7. MCP Integration

## 7.1 What is MCP

MCP (Model Context Protocol) is a standardized tool protocol proposed by Anthropic, enabling the Agent to call external tool services via a unified interface. AgentScope natively supports MCP.

```
MCP Architecture
│
├── MCP Server (tool provider)
│   Provide standardized tool description and call interface
│   Example: Gaode Map MCP, GitHub MCP, Slack MCP
│
└── MCP Client (AgentScope builtin)
    ├── HttpStatelessClient  → Stateless HTTP connection (most common)
    ├── HttpStatefulClient   → Stateful HTTP connection (persistent session)
    └── StdIOStatefulClient  → Local process communication (stdio)
```

## 7.2 Types of MCP Clients

| Client Type | Transmission Method | Applicable Scenario |
|-----------|---------|--------|
| `HttpStatelessClient` | `streamable_http` | Remote MCP Server (stateless, most common) |
| `HttpStatefulClient` | `streamable_http` | Remote MCP Server (stateful, persistent session) |
| `StdIOStatefulClient` | `stdio` | Local MCP Server (via stdin/stdout) |

## 7.3 Using MCP Tool

**Method One: Obtain a single MCP tool as a local function**

```python
from agentscope.mcp import HttpStatelessClient
from agentscope.tool import Toolkit
import os


async def use_mcp_tool():
    # Initialize MCP client
    client = HttpStatelessClient(
        name="gaode_mcp",
        transport="streamable_http",
        url=f"https://mcp.amap.com/mcp?key={os.environ['GAODE_API_KEY']}",
    )

    # Get MCP tool as a local callable function
    # wrap_tool_result=True makes the returned value automatically wrapped as ToolResponse
    geo_func = await client.get_callable_function(
        func_name="maps_geo",
        wrap_tool_result=True,
    )

    # Directly call
    result = await geo_func(address="Tian'anmen Square", city="Beijing")
    print(result)

    # Register to Toolkit for use by Agent
    toolkit = Toolkit()
    toolkit.register_tool_function(geo_func)
```

**Method Two: Register the entire MCP Server with `register_mcp_client` in one go**

```python
async def register_all_mcp_tools():
    client = HttpStatelessClient(
        name="github_mcp",
        transport="streamable_http",
        url="https://mcp.github.com/mcp",
    )

    toolkit = Toolkit()

    # One-click registration — automatically discover and register all tools on the MCP Server
    await toolkit.register_mcp_client(client)

    # Dynamically remove MCP client (and unregister its tools)
    # toolkit.remove_mcp_clients("github_mcp")

    return toolkit
```

**Method Three: Local stdio MCP Server**

```python
from agentscope.mcp import StdIOStatefulClient

async def use_local_mcp():
    # Start local MCP Server process (via stdio communication)
    client = StdIOStatefulClient(
        name="local_tools",
        command="python",
        args=["-m", "my_mcp_server"],
    )

    toolkit = Toolkit()
    await toolkit.register_mcp_client(client)
    return toolkit
```

**Method Four: Combine MCP tools with local tools**

```python
async def composite_toolkit():
    # MCP tool
    mcp_client = HttpStatelessClient(
        name="maps",
        transport="streamable_http",
        url=f"https://mcp.amap.com/mcp?key={os.environ['GAODE_API_KEY']}",
    )

    # Local tool
    def get_current_time() -> str:
        """Get current time"""
        from datetime import datetime
        return datetime.now().isoformat()

    # Composite registration
    toolkit = Toolkit()
    await toolkit.register_mcp_client(mcp_client)       # MCP 工具（一键注册）
    toolkit.register_tool_function(get_current_time)     # 本地工具
    toolkit.register_tool_function(execute_python_code)  # 内置工具

    return toolkit
```

---

## 8. Meta Tool — Autonomous Management Tool for Agents

## 6.1 Concepts

Enabling the Meta Tool allows the agent to dynamically manage its toolkit during runtime — adding, removing, and querying available tools.

```python
agent = ReActAgent(
    name="Dynamic-Agent",
    enable_meta_tool=True,   # 启用 Meta Tool
    toolkit=toolkit,
    ...
)
```

## 6.2 Use Cases

```
Meta Tool Use Cases
│
├── When the toolkit set is too large (>20 tools), agents load on demand
├── Discover new tools at runtime and register them
├── Dynamically switch toolsets based on task stages
└── Share/tools transfer in multi-Agent scenarios
```

---

## 9. Toolkit Middleware (Middleware)

The middleware mechanism of AgentScope is registered on the **Toolkit** (not the Agent), using an onion model (Onion Model), allowing custom logic to be inserted before and after tool execution.

## 9.1 Onion Model

```
Toolkit Middleware Execution Order (Olive Model)
│
│  → AuthorizationMiddleware.pre  (outermost layer)
│    → LoggingMiddleware.pre
│      → Actual tool execution         (core)
│    ← LoggingMiddleware.post
│  ← AuthorizationMiddleware.post  (outermost layer)
```

## 9.2 Middleware Signature

```python
from typing import AsyncGenerator
from agentscope.tool import ToolResponse


async def my_middleware(
    kwargs: dict,           # 工具调用参数
    next_handler,           # 下一个中间件或实际工具
) -> AsyncGenerator[ToolResponse, None]:
    # === Pre-execution logic (before tool execution) ===
    print(f"Tool parameters: {kwargs}")

    # Call the next layer
    async for response in next_handler(kwargs):
        # === Post-execution logic (after tool execution, can modify the return value) ===
        yield response
```

## 9.3 Practice Examples

**Permission Control Middleware**:

```python
async def authorization_middleware(kwargs, next_handler):
    """Tool permission control — prohibit dangerous operations"""
    tool_name = kwargs.get("_tool_name", "")
    dangerous_tools = {"execute_shell_command", "write_text_file"}

    if tool_name in dangerous_tools:
        yield ToolResponse(
            text=f"Permission denied: {tool_name} does not allow execution in the current environment"
        )
        return  # 不调用实际工具

    async for response in next_handler(kwargs):
        yield response


# Register middleware to Toolkit
toolkit = Toolkit()
toolkit.register_tool_function(execute_shell_command)
toolkit.register_middleware(authorization_middleware)
```

**Output Conversion Middleware**:

```python
async def output_transform_middleware(kwargs, next_handler):
    """Unified truncation of long tool outputs to prevent context explosion"""
    MAX_OUTPUT_LENGTH = 5000

    async for response in next_handler(kwargs):
        if response.text and len(response.text) > MAX_OUTPUT_LENGTH:
            truncated = response.text[:MAX_OUTPUT_LENGTH]
            yield ToolResponse(
                text=f"{truncated}\n\n[Output truncated, original length: {len(response.text)} characters]"
            )
        else:
            yield response


toolkit.register_middleware(output_transform_middleware)
```

> **Hooks vs Middleware**:
> - **Hooks** acts on 2 rank 3 before and after **Agent** level(reply/observe/print doing do down)
> - **Middleware** acts at the **Toolkit** level (before and after tool execution)

---

## 10. Integration Practices for Kubernetes Maintenance Tools

## 7.1 kubectl Toolset

```python
import subprocess
from agentscope.tool import Toolkit


def kubectl_get_pods(namespace: str = "default", label_selector: str = "") -> str:
    """Get the list of Pods in a specified namespace."""

    Args:
        namespace: Kubernetes 命名空间
        label_selector: 标签选择器，如 "app=nginx"

    Returns:
        Pod 列表信息
    """
    cmd = ["kubectl", "get", "pods", "-n", namespace, "-o", "wide"]
    if label_selector:
        cmd.extend(["-l", label_selector])
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"


def kubectl_describe_resource(
    resource_type: str,
    name: str,
    namespace: str = "default",
) -> str:
    """Get detailed information and events of Kubernetes resources."""

    Args:
        resource_type: 资源类型，如 "pod", "node", "service", "deployment"
        name: 资源名称
        namespace: 命名空间

    Returns:
        资源详细信息
    """
    cmd = ["kubectl", "describe", resource_type, name, "-n", namespace]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"


def kubectl_get_events(
    namespace: str = "default",
    field_selector: str = "",
) -> str:
    """Get Kubernetes events."""

    Args:
        namespace: 命名空间
        field_selector: 字段选择器，如 "involvedObject.name=nginx-pod"

    Returns:
        事件列表
    """
    cmd = ["kubectl", "get", "events", "-n", namespace, "--sort-by=.lastTimestamp"]
    if field_selector:
        cmd.extend(["--field-selector", field_selector])
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"


def kubectl_get_logs(
    pod_name: str,
    namespace: str = "default",
    container: str = "",
    tail_lines: int = 100,
    previous: bool = False,
) -> str:
    """Get Pod container logs."""

    Args:
        pod_name: Pod 名称
        namespace: 命名空间
        container: 容器名称（多容器 Pod 时必填）
        tail_lines: 获取最后 N 行日志
        previous: 是否获取上一次容器的日志（CrashLoopBackOff 排查用）

    Returns:
        容器日志内容
    """
    cmd = ["kubectl", "logs", pod_name, "-n", namespace, f"--tail={tail_lines}"]
    if container:
        cmd.extend(["-c", container])
    if previous:
        cmd.append("--previous")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"


def kubectl_top_nodes() -> str:
    """Get cluster node resource usage."""

    Returns:
        节点 CPU/内存使用量
    """
    result = subprocess.run(
        ["kubectl", "top", "nodes"],
        capture_output=True, text=True, timeout=30,
    )
    return result.stdout if result.returncode == 0 else f"Error: {result.stderr}"


# Register K8s toolkit set
def create_k8s_toolkit() -> Toolkit:
    """Create a K8s maintenance operations toolkit set"""
    toolkit = Toolkit()
    toolkit.register_tool_function(kubectl_get_pods)
    toolkit.register_tool_function(kubectl_describe_resource)
    toolkit.register_tool_function(kubectl_get_events)
    toolkit.register_tool_function(kubectl_get_logs)
    toolkit.register_tool_function(kubectl_top_nodes)
    return toolkit
```

## 7.2 Complete K8s Diagnostic Agent

```python
import asyncio
import os
from agentscope.agent import ReActAgent
from agentscope.model import DashScopeChatModel
from agentscope.formatter import DashScopeChatFormatter
from agentscope.memory import InMemoryMemory
from agentscope.message import Msg


async def k8s_diagnosis_agent():
    toolkit = create_k8s_toolkit()

    agent = ReActAgent(
        name="K8s-Doctor",
        sys_prompt="""你是一个 Kubernetes 生产运维诊断专家。

诊断原则:
1. 先通过 kubectl 命令收集足够信息，再下结论
2. 对每个工具返回的结果进行分析
3. 给出: 根因分析 + 修复步骤 + 验证方法
4. 对破坏性操作明确标注风险等级
5. 所有结论必须基于工具获取的实际数据，禁止猜测

诊断顺序建议:
- Pod 问题: get_pods → describe → logs → events
- Node 问题: top_nodes → describe → events
- Service 问题: get_pods (label) → describe → events""",
        model=DashScopeChatModel(
            model_name="qwen-max",
            api_key=os.environ["DASHSCOPE_API_KEY"],
            stream=True,
        ),
        memory=InMemoryMemory(),
        formatter=DashScopeChatFormatter(),
        toolkit=toolkit,
        parallel_tool_calls=True,
        max_iters=15,
    )

    msg = Msg(
        name="user",
        content="production" namespace's nginx-deploy Pod is still in Pending state, please diagnose,
        role="user",
    )

    response = await agent(msg)
    print(f"\nDiagnosis result:\n{response.get_text_content()}")


asyncio.run(k8s_diagnosis_agent())
```

---

## 11. Best Practices for Tool Development

## 8.1 Writing High-Quality Tool Functions

```python
# Best practice: clear docstrings + type hints + error handling

def query_prometheus_metric(
    metric_name: str,
    label_selector: str = "",
    duration: str = "5m",
    step: str = "15s",
) -> str:
    """Query Prometheus monitoring metrics."""

    适用场景: 查询集群或 Pod 级别的 CPU、内存、网络等监控数据。

    Args:
        metric_name: PromQL 指标名称，如 "container_cpu_usage_seconds_total"
        label_selector: 标签过滤器，如 'namespace="production",pod=~"nginx.*"'
        duration: 查询时间范围，如 "5m", "1h", "24h"
        step: 采样步长，如 "15s", "1m"

    Returns:
        JSON 格式的查询结果。失败时返回错误信息。

    Example:
        query_prometheus_metric(
            metric_name="container_memory_usage_bytes",
            label_selector='namespace="production"',
            duration="1h",
        )
    """
    import requests

    try:
        query = metric_name
        if label_selector:
            query = f"{metric_name}{{{label_selector}}}"

        response = requests.get(
            "http://prometheus:9090/api/v1/query_range",
            params={
                "query": query,
                "start": f"now()-{duration}",
                "end": "now()",
                "step": step,
            },
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
    except requests.Timeout:
        return "Error: Prometheus query timeout (10s)"
    except requests.ConnectionError:
        return "Error: Unable to connect to Prometheus (check service address and network)"
    except Exception as e:
        return f"Error: {type(e).__name__}: {e}"

```

## 8.2 Principles of Tool Design

| Principle | Explanation | Anti-pattern |
|------|------|--------|
| **Single Responsibility** | Each tool does one thing | A tool simultaneously queries, modifies, and validates |
| **Clear Description** | Docstring explains purpose, parameters, return values | No documentation or unclear description |
| **Type Annotations** | All parameters and returns use type hints | `def tool(x, y)` without types |
| **Error Handling** | Capture exceptions to return error messages | Exceptions are directly thrown causing Agent loops to interrupt |
| **Timeout Control** | Network calls set timeouts | No timeouts leading to Agent suspensions |
| **Read-Only Priority** | Diagnostic tools are read-only, while modification tools are separated | Querying tools have side effects |
| **Tool Quantity** | ≤20 tools per Agent | Registering over 50 tools leads to a decrease in selection accuracy |

---

## 12. Best Practices and Anti-patterns

## Best Practices

- **Return `ToolResponse`**: Use `ToolResponse(text=...)` instead of pure strings for unified multi-modal responses
- **`preset_kwargs` hides sensitive parameters**: API Keys, database passwords are passed through `preset_kwargs` and not exposed to LLM
- **Docstring Determines Tool Quality**: LLM understands tools better with more precise descriptions
- **Type Hints Are Essential**: AgentScope relies on type annotations to generate tool schemas
- **Use Partial Functions to Simplify Tools**: `partial(kubectl, verb="get")` is clearer than registering a generic kubectl
- **`register_mcp_client` is Better Than Manual Traversal**: One-click registration is more concise than manual traversal of `list_tools`
- **Middleware Implements Cross-cutting Concerns**: Permissions control, output truncation, logging use middleware rather than being written within tools
- **Parallel Call Acceleration Diagnosis**: Independent information collection tasks enable `parallel_tool_calls=True`

## Anti-patterns

- **Tools Without Docstrings**: LLM cannot understand tool purposes, randomly calling them
- **Tool Returns Large Data**: Returning full YAML (over 10000 lines) occupies the context window — use Middleware to truncate
- **No Error Handling**: Tool exceptions cause Agent Loop to be interrupted
- **Direct Execution of Code in Production Environment**:`execute_python_code` must run in a sandbox
- **Mixed Read-Write Tools**: Agent diagnosis should not have `kubectl delete` permissions — use Middleware to intercept
- **Ignoring Tool Interruption Handling**: Not catching `CancelledError` causes lost partial results when users interrupt

---

## Related Documentation

| Document | Associated Content |
|------|---------|
| [17 - Core Concepts](./17-agentscope-core-concepts.md) | Position of tools in core abstractions |
| [19 - Memory Management](./19-agentscope-memory-context.md) | Storage and context management of tool outputs |
| [22 - Production Deployment](./22-agentscope-production-deployment.md) | Safe execution environment for Sandboxes |
| [05 - Tool Use & Function Calling](./05-tool-use-function-calling.md) | Design guidelines for general tool calling |

---

*This document is original content from the kudig-database project's 02-ai-agents topic series.*

---

## Related Documentation for Obsidian

- 02-ai-agents MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|AI Agent Engineering Topic Series]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|Foundation and Core Architecture of AI Agents]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|Selection and Evaluation of LLM Foundation Models]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Deep Comparison of Mainstream Agent Frameworks]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|Deep Guide on Retrieval-Augmented Generation (RAG)]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Design Guidelines for Tool Use & Function Calling]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Multi-Agent Orchestration and Collaboration Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation Framework and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]

## See Also

- 16-agentscope-overview-installation
- 17-agentscope-core-concepts
- 19-agentscope-memory-context
- 20-agentscope-multi-agent-orchestration

```

<!-- risk-assessed -->
