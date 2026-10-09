---
title: Agent Harness Tool Engineering: A Complete Practice from Design to Simplification (domain-14-ai-ml-infra)
description: 'title: Agent Harness Tool Engineering: A Complete Practice from Design to Simplification'
summary: 'title: Agent Harness Tool Engineering: A Complete Practice from Design to Simplification'
category: general
tags:
- ai
- ai-agent
- prometheus
- helm
- ingress
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
estimated_read_time: 35min
intent_queries:
- What is Agent Harness Tool Engineering: A Complete Practice from Design to Simplification
- How does Agent Harness Tool Engineering: A Complete Practice from Design to Simplification
- Kubernetes 14 ai ml infra Best Practices
trigger_keywords:
- Agent
- Harness
- What is a Complete Practice from Design to Simplification
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- helm-basics
- prometheus-basics
authors:
- name: Dillan Teagle
  role: contributor
source_path: tree/infrastructure/kubernetes/ai/ai-agents/32-agent-harness-tool-engineering.md
---

# Agent Harness Tooling: A Comprehensive Practice from Design to Simplification

> **Document Type**: Harness Engineering Deep Dive Topics | **Last Updated**: 2026-04 | **Keywords**: Tool Engineering, Tool Design, Function Calling, Tool Simplification, Tool Orchestration, MCP, Tool Security, Schema Design, Tool Registration, Tool Discovery

---

## Overview

Tools (tool layer) is the second layer of the six-layer architecture of Agent Harness, enabling Agents to transition from "just saying" to "doing things." However, tool design is not about "having more tools" — as evidenced by Vercel's experience, reducing 15 tools to just 2 improved accuracy from 80% to 100%.

This article systematically discusses the principles of tool layer design, Schema standards, registration discovery mechanisms, orchestration patterns, security sandboxes, error recovery strategies, and best practices for tool engineering in Kubernetes operational scenarios.

---

## 1. Tool Design Principles

## 1.1 Less is More: The Power of Simplicity

```
Tool simplicity business value:

Relationship between tool quantity and decision quality (empirical data):
  2  tools → Decision accuracy ~100% (Vercel empirical)
  5  tools → Decision accuracy ~95%
  10 tools → Decision accuracy ~85% (Vercel empirical)
  15 tools → Decision accuracy ~80% (Vercel empirical)
  25 tools → Decision accuracy ~65%
  50 tools → Decision accuracy ~45%

Reason analysis:
  1. More tools mean longer Schemas for LLM to read → Context window consumption
  2. Similar functionality tools lead to LLM's decision difficulty → "read_file vs search_file vs grep_file"
  3. Minor differences in tool descriptions are overlooked → Incorrectly calling a tool
  4. More tools = More parameter combinations = More error possibilities
```

## 1.2 Six Major Principles of Tool Design

| Principle | Explanation | Practice Guide |
|------|------|---------|
| **Minimal Sufficiency** | Provide only the necessary tools for the current task | Dynamic toolkit: load different tools based on task type |
| **Unambiguous** | Each tool must have a uniquely clear purpose | Tool names and descriptions should not confuse LLMs |
| **Self-Explanatory** | The Schema itself serves as comprehensive usage documentation | Parameter descriptions include examples and constraints |
| **Security First** | Tool execution should not produce irreversible consequences | Dangerous operations require confirmation mechanisms |
| **Idempotent** | Same inputs yield same outputs | Avoid tools with hidden side effects |
| **Error-Friendly** | Return meaningful error messages on failure | Help the Agent understand why it failed and how to fix it |

---

## 2. Tool Schema Design Standards

## 2.1 Standard Tool Interfaces

```python
from abc import ABC, abstractmethod
from typing import Any, Optional
from dataclasses import dataclass, field
import json

@dataclass
class ToolParameter:
    """tool parameter definition"""
    name: str
    type: str                           # string, integer, boolean, array, object
    description: str
    required: bool = True
    default: Any = None
    enum: list = None                   # 可选值枚举
    example: Any = None                 # 示例值
    pattern: str = None                 # 正则验证
    min_value: Any = None
    max_value: Any = None

@dataclass
class ToolSchema:
    """complete tool schema definition"""
    name: str
    description: str                    # 一句话描述（LLM 选择工具的依据）
    long_description: str = ""          # 详细说明
    parameters: list[ToolParameter] = field(default_factory=list)
    returns: str = ""                   # 返回值说明
    examples: list[dict] = field(default_factory=list)
    category: str = ""                  # 工具类别
    risk_level: str = "low"             # low / medium / high / critical
    idempotent: bool = True
    timeout_seconds: int = 30

    def to_openai_format(self) -> dict:
        """convert to OpenAI Function Calling format"""
        properties = {}
        required = []
        for param in self.parameters:
            prop = {"type": param.type, "description": param.description}
            if param.enum:
                prop["enum"] = param.enum
            if param.example:
                prop["description"] += f" (example: {param.example})"
            properties[param.name] = prop
            if param.required:
                required.append(param.name)

        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": required,
                },
            },
        }

class BaseTool(ABC):
    """tool base class"""

    @abstractmethod
    def get_schema(self) -> ToolSchema:
        """return the schema definition of the tool"""
        ...

    @abstractmethod
    def execute(self, **kwargs) -> dict:
        """execute the tool"""
        ...

    def validate(self, **kwargs) -> tuple[bool, str]:
        """parameter validation"""
        schema = self.get_schema()
        for param in schema.parameters:
            if param.required and param.name not in kwargs:
                return False, f"missing required parameter: {param.name}"
            if param.name in kwargs and param.enum:
                if kwargs[param.name] not in param.enum:
                    return False, f"parameter {param.name} must be: {param.enum}"
        return True, "OK"
```

## 2.2 Design of Kubernetes Maintenance Toolset

```python
class KubectlGetTool(BaseTool):
    """kubectl get tool: obtain K8S resource information"""

    def get_schema(self) -> ToolSchema:
        return ToolSchema(
            name="kubectl_get",
            description="Get a list or detailed information about Kubernetes resources. Used to view the status of resources such as Pods, Nodes, and Services."
            parameters=[
                ToolParameter(
                    name="resource",
                    type="string",
                    description="resource type",
                    enum=["pods", "nodes", "services", "deployments",
                          "events", "pvc", "configmaps", "ingress"],
                    example="pods",
                ),
                ToolParameter(
                    name="namespace",
                    type="string",
                    description="Namespace. Use '--all-namespaces' to view all",
                    required=False,
                    default="default",
                    example="kube-system",
                ),
                ToolParameter(
                    name="name",
                    type="string",
                    description="Resource name. Specify to list all."
                    required=False,
                    example="nginx-deployment-7fb96c846b-xxxxx",
                ),
                ToolParameter(
                    name="output",
                    type="string",
                    description="Output format"
                    required=False,
                    enum=["wide", "yaml", "json", "name"],
                    default="wide",
                ),
                ToolParameter(
                    name="selector",
                    type="string",
                    description="tag selector",
                    required=False,
                    example="app=nginx",
                ),
            ],
            returns="Text output of resource information"
            risk_level="low",
            category="kubernetes",
            idempotent=True,
            timeout_seconds=15,
            examples=[
                {"args": {"resource": "pods", "namespace": "default"},
                 "description": "get all Pods in the default namespace"}
                {"args": {"resource": "nodes", "output": "wide"},
                 "description": "Get all node detailed information"}
            ],
        )

    def execute(self, **kwargs) -> dict:
        resource = kwargs["resource"]
        namespace = kwargs.get("namespace", "default")
        name = kwargs.get("name", "")
        output = kwargs.get("output", "wide")
        selector = kwargs.get("selector", "")

        cmd = f"kubectl get {resource}"
        if name:
            cmd += f" {name}"
        if namespace == "--all-namespaces":
            cmd += " --all-namespaces"
        else:
            cmd += f" -n {namespace}"
        if output:
            cmd += f" -o {output}"
        if selector:
            cmd += f" -l {selector}"

        result = self._run_command(cmd)
        return {"command": cmd, "output": result["stdout"],
                "error": result.get("stderr"), "exit_code": result["exit_code"]}


class KubectlDescribeTool(BaseTool):
    """kubectl describe tool: obtain resource detailed description"""

    def get_schema(self) -> ToolSchema:
        return ToolSchema(
            name="kubectl_describe",
            description: "Retrieve detailed information about Kubernetes resources, including Events and Conditions. Used for diagnosing resource issues."
            parameters=[
                ToolParameter(
                    name="resource",
                    type="string",
                    description="resource type",
                    enum=["pod", "node", "service", "deployment",
                          "pvc", "ingress", "configmap"],
                    example="pod",
                ),
                ToolParameter(
                    name="name",
                    type="string",
                    description="Resource name",
                    example="nginx-pod-xxxxx",
                ),
                ToolParameter(
                    name="namespace",
                    type="string",
                    description="namespace"
                    required=False,
                    default="default",
                ),
            ],
            returns="a detailed description of the resource, including Events and Conditions"
            risk_level="low",
            category="kubernetes",
            idempotent=True,
        )

    def execute(self, **kwargs) -> dict:
        resource = kwargs["resource"]
        name = kwargs["name"]
        namespace = kwargs.get("namespace", "default")
        cmd = f"kubectl describe {resource} {name} -n {namespace}"
        result = self._run_command(cmd)
        return {"command": cmd, "output": result["stdout"],
                "error": result.get("stderr"), "exit_code": result["exit_code"]}


class PrometheusQueryTool(BaseTool):
    """Prometheus query tool: execute PromQL to obtain monitoring metrics"""

    def get_schema(self) -> ToolSchema:
        return ToolSchema(
            name="prometheus_query",
            description: "Execute PromQL queries to obtain monitoring metric data. Used to view system metrics such as CPU, memory, and network."
            parameters=[
                ToolParameter(
                    name="query",
                    type="string",
                    description="PromQL query expression"
                    example='sum(rate(container_cpu_usage_seconds_total{namespace="default"}[5m]))',
                ),
                ToolParameter(
                    name="time_range",
                    type="string",
                    description="Query time range"
                    required=False,
                    enum=["5m", "15m", "1h", "6h", "24h"],
                    default="15m",
                ),
                ToolParameter(
                    name="step",
                    type="string",
                    description="Data point interval",
                    required=False,
                    default="30s",
                ),
            ],
            returns="Metric data (JSON format)",
            risk_level="low",
            category="monitoring",
            timeout_seconds=30,
        )

    def execute(self, **kwargs) -> dict:
        query = kwargs["query"]
        time_range = kwargs.get("time_range", "15m")
        # call Prometheus API
        result = self._query_prometheus(query, time_range)
        return {"query": query, "data": result, "time_range": time_range}
```

---

## 3. Tool Registration and Discovery

## 3.1 Tool Registration Center

```python
from typing import Optional
import logging

logger = logging.getLogger("agent.tools")

class ToolRegistry:
    """tool registration center: manage tool registration, discovery, and lifecycle"""

    def __init__(self):
        self._tools: dict[str, BaseTool] = {}
        self._categories: dict[str, list[str]] = {}
        self._risk_levels: dict[str, list[str]] = {}
        self._usage_stats: dict[str, dict] = {}

    def register(self, tool: BaseTool, override: bool = False):
        """register the tool"""
        schema = tool.get_schema()
        name = schema.name

        if name in self._tools and not override:
            raise ValueError(f"tool '{name}' has been registered, use override=True to override")

        self._tools[name] = tool

        # category index
        category = schema.category or "uncategorized"
        self._categories.setdefault(category, []).append(name)

        # risk level index
        self._risk_levels.setdefault(schema.risk_level, []).append(name)

        # initialization usage statistics
        self._usage_stats[name] = {
            "total_calls": 0, "success": 0, "failures": 0,
            "total_latency_ms": 0, "last_used": None,
        }

        logger.info(f"Registered tool: {name} (category={category}, risk={schema.risk_level})")

    def get_tools_for_task(
        self,
        task_type: str = None,
        categories: list[str] = None,
        max_risk: str = "medium",
        max_tools: int = 8,
    ) -> list[BaseTool]:
        """obtain a set of available tools according to task type and constraints

        Implement the principle of "minimum necessary set of tools": only return the tools required to complete the current task.
        """
        risk_order = {"low": 0, "medium": 1, "high": 2, "critical": 3}
        max_risk_level = risk_order.get(max_risk, 1)

        candidates = []
        for name, tool in self._tools.items():
            schema = tool.get_schema()

            # risk filtering
            if risk_order.get(schema.risk_level, 0) > max_risk_level:
                continue

            # category filtering
            if categories and schema.category not in categories:
                continue

            candidates.append(tool)

        # sort by usage frequency (popular tools first)
        candidates.sort(
            key=lambda t: self._usage_stats.get(t.get_schema().name, {}).get("total_calls", 0),
            reverse=True,
        )

        # Truncate to maximum number of tools
        return candidates[:max_tools]

    def execute(self, tool_name: str, args: dict) -> dict:
        """Securely execute tool calls"""
        import time

        tool = self._tools.get(tool_name)
        if not tool:
            return {"success": False, "error": f"Unknown tool: {tool_name}",
                    "available_tools": list(self._tools.keys())}

        # Parameter validation
        valid, msg = tool.validate(**args)
        if not valid:
            return {"success": False, "error": f"Validation failed: {msg}"}

        # Execution
        start = time.time()
        try:
            schema = tool.get_schema()
            result = tool.execute(**args)
            latency = (time.time() - start) * 1000

            # Update statistics
            stats = self._usage_stats[tool_name]
            stats["total_calls"] += 1
            stats["success"] += 1
            stats["total_latency_ms"] += latency
            stats["last_used"] = time.time()

            return {"success": True, "result": result, "latency_ms": latency,
                    "tool": tool_name}

        except Exception as e:
            latency = (time.time() - start) * 1000
            self._usage_stats[tool_name]["total_calls"] += 1
            self._usage_stats[tool_name]["failures"] += 1

            logger.error(f"Tool execution failed: {tool_name}, error={e}")
            return {"success": False, "error": str(e), "tool": tool_name,
                    "latency_ms": latency}

    def get_usage_report(self) -> dict:
        """Retrieve tool usage report"""
        report = {}
        for name, stats in self._usage_stats.items():
            total = stats["total_calls"]
            report[name] = {
                "total_calls": total,
                "success_rate": stats["success"] / total if total > 0 else 0,
                "avg_latency_ms": stats["total_latency_ms"] / total if total > 0 else 0,
            }
        return report
```

## 3.2 Dynamic Tool Loading

```python
class DynamicToolLoader:
    """Dynamic Tool Loader: Load tools on-demand based on task context"""

    # Mapping of task types to tool sets
    TASK_TOOL_MAPPING = {
        "pod_diagnosis": [
            "kubectl_get", "kubectl_describe", "kubectl_logs",
            "kubectl_events", "kubectl_top",
        ],
        "node_diagnosis": [
            "kubectl_get", "kubectl_describe", "kubectl_top",
            "prometheus_query",
        ],
        "network_diagnosis": [
            "kubectl_get", "kubectl_describe", "kubectl_exec",
            "prometheus_query",
        ],
        "storage_diagnosis": [
            "kubectl_get", "kubectl_describe", "kubectl_logs",
        ],
        "performance_analysis": [
            "prometheus_query", "kubectl_top", "kubectl_get",
        ],
    }

    def __init__(self, registry: ToolRegistry):
        self.registry = registry

    def load_for_task(self, task: str) -> list[dict]:
        """Dynamically load tool set based on task description"""
        task_type = self._classify_task(task)
        tool_names = self.TASK_TOOL_MAPPING.get(task_type, [])

        tools = []
        for name in tool_names:
            tool = self.registry._tools.get(name)
            if tool:
                tools.append(tool.get_schema().to_openai_format())
        return tools

    def _classify_task(self, task: str) -> str:
        """Quick task classification by keywords"""
        task_lower = task.lower()
        if any(kw in task_lower for kw in ["pod", "container", "pending", "crashloop"]):
            return "pod_diagnosis"
        elif any(kw in task_lower for kw in ["node", "node", "notready"]):
            return "node_diagnosis"
        elif any(kw in task_lower for kw in ["network", "network", "dns", "service"]):
            return "network_diagnosis"
        elif any(kw in task_lower for kw in ["storage", "storage", "pvc", "volume"]):
            return "storage_diagnosis"
        elif any(kw in task_lower for kw in ["performance", "cpu", "memory", "latency"]):
            return "performance_analysis"
        return "pod_diagnosis"  # 默认
```

---

## 4. Tool Orchestration Patterns

## 4.1 Five Orchestration Patterns

```
# 🟢 Low-risk: Read-only/information gathering, typically with no side effects
Tool orchestration patterns:

1. Sequential Orchestration
   Tool A → Tool B → Tool C
   Output of previous tool is input for next
   Example: describe pod → Parse events → Query prometheus

2. Parallel Orchestration
   Tool A ─┐
   Tool B ─┼→ Aggregate Results
   Tool C ─┘
   Multiple independent tools run simultaneously
   Example: Fetch pod, node, event information simultaneously

3. Conditional Orchestration (Conditional)
   Tool A → Conditional Judgment → Tool B or Tool C
   Choose next tool based on intermediate results
   Example: If CPU > 90% → Check top pods, otherwise → Check network

4. Waterfall Orchestration (Waterfall)
   Tool A → Tool B → Failure? → Tool C (Alternative)
   Switch automatically to alternative tool on failure
   Example: Prometheus query fails → Switch to kubectl top

5. Pipeline Orchestration (Pipeline)
   Tool A's output is transformed and used as Tool B's input
   Includes data cleaning/transformation steps
   Example: kubectl get -o json → jq Extract → Prometheus query
```
## 4.2 Toolchain Builder

```python
class ToolChainBuilder:
    """Toolchain Builder: Declarative orchestration of tool builds"""

    def __init__(self, registry: ToolRegistry):
        self.registry = registry
        self._chain: list[dict] = []

    def then(self, tool_name: str, args_builder=None) -> 'ToolChainBuilder':
        """Sequential addition of tools"""
        self._chain.append({
            "type": "sequential",
            "tool": tool_name,
            "args_builder": args_builder,
        })
        return self

    def parallel(self, *tool_specs) -> 'ToolChainBuilder':
        """Parallel addition of multiple tools"""
        self._chain.append({
            "type": "parallel",
            "tools": [{"tool": name, "args": args} for name, args in tool_specs],
        })
        return self

    def conditional(self, condition, if_true, if_false) -> 'ToolChainBuilder':
        """Conditional branching"""
        self._chain.append({
            "type": "conditional",
            "condition": condition,
            "if_true": if_true,
            "if_false": if_false,
        })
        return self

    def build(self) -> list:
        return self._chain

    def execute(self, initial_context: dict = None) -> dict:
        """Execute toolchain"""
        context = initial_context or {}
        results = []

        for step in self._chain:
            if step["type"] == "sequential":
                args = step.get("args_builder", lambda c: {})(context) if step.get("args_builder") else {}
                result = self.registry.execute(step["tool"], args)
                results.append(result)
                context["last_result"] = result

            elif step["type"] == "parallel":
                import asyncio
                parallel_results = asyncio.run(self._execute_parallel(step["tools"]))
                results.extend(parallel_results)
                context["parallel_results"] = parallel_results

            elif step["type"] == "conditional":
                condition_met = step["condition"](context)
                branch = step["if_true"] if condition_met else step["if_false"]
                result = self.registry.execute(branch["tool"], branch.get("args", {}))
                results.append(result)
                context["last_result"] = result

        return {"chain_results": results, "final_context": context}


# Usage Example
def build_pod_diagnosis_chain(registry: ToolRegistry, pod_name: str, namespace: str):
    """Build a Pod diagnostic toolchain"""
    chain = ToolChainBuilder(registry)

    # Step 1: Parallel collection of foundational information
    chain.parallel(
        ("kubectl_get", {"resource": "pods", "name": pod_name, "namespace": namespace}),
        ("kubectl_describe", {"resource": "pod", "name": pod_name, "namespace": namespace}),
        ("kubectl_events", {"namespace": namespace, "field_selector": f"involvedObject.name={pod_name}"}),
    )

    # Step 2: Conditionally branch based on Pod status
    chain.conditional(
        condition=lambda ctx: "Pending" in str(ctx.get("parallel_results", [{}])[0].get("result", "")),
        if_true={"tool": "kubectl_get", "args": {"resource": "nodes", "output": "wide"}},
        if_false={"tool": "kubectl_logs", "args": {"pod": pod_name, "namespace": namespace, "tail": 100}},
    )

    return chain
```

---

## 5. Tool Security Sandbox

## 5.1 Secure Execution Environment

```python
import subprocess
import shlex
import re

class ToolSandbox:
    """Tool Safety Sandbox: Control the execution boundary of tools"""

    def __init__(self, config: dict = None):
        self.config = config or {}
        self.allowed_commands = self.config.get("allowed_commands", [])
        self.blocked_patterns = self.config.get("blocked_patterns", [])
        self.max_output_size = self.config.get("max_output_size", 100_000)  # 100KB
        self.command_timeout = self.config.get("command_timeout", 30)
        self.audit_log: list[dict] = []

    def execute_command(self, command: str, dry_run: bool = False) -> dict:
        """Execute commands within the sandbox"""
        # 1. Security Checks
        safety_check = self._check_command_safety(command)
        if not safety_check["safe"]:
            self.audit_log.append({
                "command": command, "action": "blocked",
                "reason": safety_check["reason"],
            })
            return {"success": False, "error": safety_check["reason"],
                    "blocked": True}

        # 2. Dry-run Mode
        if dry_run:
            self.audit_log.append({"command": command, "action": "dry_run"})
            return {"success": True, "dry_run": True,
                    "would_execute": command}

        # 3. Actual Execution
        try:
            result = subprocess.run(
                shlex.split(command),
                capture_output=True,
                text=True,
                timeout=self.command_timeout,
            )

            output = result.stdout[:self.max_output_size]
            if len(result.stdout) > self.max_output_size:
                output += f"\n... (Output truncated, total length {len(result.stdout)} bytes)"

            self.audit_log.append({
                "command": command, "action": "executed",
                "exit_code": result.returncode,
            })

            return {
                "success": result.returncode == 0,
                "stdout": output,
                "stderr": result.stderr[:10000],
                "exit_code": result.returncode,
            }

        except subprocess.TimeoutExpired:
            self.audit_log.append({
                "command": command, "action": "timeout",
            })
            return {"success": False, "error": f"Command timed out ({self.command_timeout}s)"}

    def _check_command_safety(self, command: str) -> dict:
        """Command Security Check"""
        # Check Block Mode
        for pattern in self.blocked_patterns:
            if re.search(pattern, command, re.IGNORECASE):
                return {"safe": False, "reason": f"Match prohibited mode: {pattern}"}

        # Check Command Whitelist
        if self.allowed_commands:
            cmd_base = command.split()[0] if command else ""
            allowed = any(command.startswith(ac) for ac in self.allowed_commands)
            if not allowed:
                return {"safe": False,
                        "reason": f"Command '{cmd_base}' not in allowed list"}

        return {"safe": True}


# Kubernetes Operations Sandbox Configuration
K8S_SANDBOX_CONFIG = {
    "allowed_commands": [
        "kubectl get", "kubectl describe", "kubectl logs",
        "kubectl top", "kubectl events", "kubectl explain",
    ],
    "blocked_patterns": [
        r"kubectl\s+delete",
        r"kubectl\s+drain",
        r"kubectl\s+cordon",
        r"kubectl\s+edit",
        r"kubectl\s+apply",
        r"kubectl\s+patch",
        r"kubectl\s+exec.*--\s*(rm|dd|mkfs|shutdown|reboot)",
        r"helm\s+(uninstall|delete|rollback)",
        r";\s*rm\s+",                    # 命令注入
        r"|\s*rm\s+",                   # 管道注入
        r"\$\(",                         # 命令替换注入
        r"`",                            # 反引号注入
    ],
    "max_output_size": 100_000,
    "command_timeout": 30,
}
```

## 5.2 Tool Permission Model

```python
from enum import IntEnum

class ToolPermission(IntEnum):
    """Tool Permission Level"""
    READ = 1         # 只读操作
    SUGGEST = 2      # 可建议修改但不执行
    WRITE_SAFE = 3   # 可执行安全写操作（如 scale up）
    WRITE_RISKY = 4  # 可执行风险写操作（如 drain node）
    ADMIN = 5        # 管理员操作

class ToolPermissionManager:
    """Tool Permission Manager"""

    def __init__(self, default_permission: ToolPermission = ToolPermission.READ):
        self.default_permission = default_permission
        self._tool_permissions: dict[str, ToolPermission] = {}
        self._namespace_permissions: dict[str, ToolPermission] = {}

    def set_tool_permission(self, tool_name: str, permission: ToolPermission):
        self._tool_permissions[tool_name] = permission

    def set_namespace_permission(self, namespace: str, permission: ToolPermission):
        self._namespace_permissions[namespace] = permission

    def check_permission(self, tool_name: str, args: dict) -> tuple[bool, str]:
        """Check Tool Invocation Permissions"""
        required = self._tool_permissions.get(tool_name, self.default_permission)
        namespace = args.get("namespace", "default")
        ns_permission = self._namespace_permissions.get(namespace, self.default_permission)

        effective = max(required, ns_permission)

        if effective > self.default_permission:
            if effective >= ToolPermission.WRITE_RISKY:
                return False, f"Approval needed: {tool_name} has permission level {effective.name} in {namespace}"
            if effective >= ToolPermission.WRITE_SAFE:
                return True, f"Allow safe write operation: {tool_name}"

        return True, "OK"
```

---

## 6. Error Handling and Recovery

## 6.1 Classification and Recovery Strategies for Tools

```python
class ToolErrorClassifier:
    """Tool Error Classifier"""

    ERROR_PATTERNS = {
        "auth_error": {
            "patterns": ["Unauthorized", "Forbidden", "403", "401",
                         "certificate has expired"],
            "recovery": "refresh_credentials",
            "retryable": True,
        },
        "not_found": {
            "patterns": ["NotFound", "not found", "404",
                         "No resources found"],
            "recovery": "suggest_alternative",
            "retryable": False,
        },
        "timeout": {
            "patterns": ["timed out", "deadline exceeded",
                         "context deadline"],
            "recovery": "retry_with_backoff",
            "retryable": True,
        },
        "resource_conflict": {
            "patterns": ["Conflict", "409", "already exists",
                         "the object has been modified"],
            "recovery": "retry_with_latest",
            "retryable": True,
        },
        "quota_exceeded": {
            "patterns": ["quota", "exceeded", "LimitRange",
                         "insufficient"],
            "recovery": "report_and_suggest",
            "retryable": False,
        },
        "connection_error": {
            "patterns": ["connection refused", "no such host",
                         "network unreachable"],
            "recovery": "check_connectivity",
            "retryable": True,
        },
    }

    def classify(self, error_message: str) -> dict:
        """Classify errors and suggest recovery strategies"""
        for error_type, config in self.ERROR_PATTERNS.items():
            for pattern in config["patterns"]:
                if pattern.lower() in error_message.lower():
                    return {
                        "type": error_type,
                        "recovery": config["recovery"],
                        "retryable": config["retryable"],
                        "original_error": error_message,
                    }
        return {
            "type": "unknown",
            "recovery": "escalate",
            "retryable": False,
            "original_error": error_message,
        }


class ToolRetryHandler:
    """Tool Retry Handler"""

    def __init__(self, max_retries: int = 3, base_delay: float = 1.0):
        self.max_retries = max_retries
        self.base_delay = base_delay
        self.error_classifier = ToolErrorClassifier()

    def execute_with_retry(self, tool, args: dict) -> dict:
        """Smart Retry for Tool Execution"""
        import time

        last_error = None
        for attempt in range(self.max_retries + 1):
            try:
                result = tool.execute(**args)
                if result.get("success"):
                    return result

                # Classify Errors
                error = result.get("error", "Unknown error")
                classified = self.error_classifier.classify(error)

                if not classified["retryable"]:
                    return {
                        "success": False,
                        "error": error,
                        "error_classification": classified,
                        "attempts": attempt + 1,
                    }

                last_error = classified

                # Exponential Backoff
                delay = self.base_delay * (2 ** attempt)
                time.sleep(delay)

            except Exception as e:
                last_error = {"type": "exception", "error": str(e)}
                delay = self.base_delay * (2 ** attempt)
                time.sleep(delay)

        return {
            "success": False,
            "error": f"Failed after retrying {self.max_retries} times"
            "last_error": last_error,
            "attempts": self.max_retries + 1,
        }
```

---

## 7. MCP (Model Context Protocol) Integration

## 7.1 MCP Tool Adapter

```python
class MCPToolAdapter:
    """MCP Protocol Tool Adapter

    将 MCP Server 的工具转换为 Agent Harness 标准工具接口。
    支持动态发现和注册 MCP Server 提供的工具。
    """

    def __init__(self, mcp_server_url: str, auth_token: str = None):
        self.server_url = mcp_server_url
        self.auth_token = auth_token
        self._discovered_tools: dict = {}

    async def discover_tools(self) -> list[ToolSchema]:
        """Discover Available Tools from MCP Server"""
        response = await self._call_mcp("tools/list")
        tools = []
        for tool_def in response.get("tools", []):
            schema = self._convert_mcp_to_schema(tool_def)
            self._discovered_tools[schema.name] = tool_def
            tools.append(schema)
        return tools

    async def execute_tool(self, tool_name: str, args: dict) -> dict:
        """Call the MCP protocol using a tool"""
        if tool_name not in self._discovered_tools:
            return {"success": False, "error": f"MCP tool did not find: {tool_name}"}

        response = await self._call_mcp("tools/call", {
            "name": tool_name,
            "arguments": args,
        })
        return {
            "success": not response.get("isError", False),
            "result": response.get("content", []),
            "error": response.get("error"),
        }

    def _convert_mcp_to_schema(self, mcp_tool: dict) -> ToolSchema:
        """Convert the MCP tool definition to a standard Schema"""
        params = []
        input_schema = mcp_tool.get("inputSchema", {})
        properties = input_schema.get("properties", {})
        required = input_schema.get("required", [])

        for name, prop in properties.items():
            params.append(ToolParameter(
                name=name,
                type=prop.get("type", "string"),
                description=prop.get("description", ""),
                required=name in required,
                enum=prop.get("enum"),
            ))

        return ToolSchema(
            name=mcp_tool["name"],
            description=mcp_tool.get("description", ""),
            parameters=params,
            category="mcp",
        )
```

---

## 8. Best Practices Summary

## 8.1 Tool Design Core Principles

| Principle | Explanation | Practice Suggestions |
|------|------|---------|
| **Minimum Toolset** | Each task type loads only necessary tools | Uses DynamicToolLoader to load on demand |
| **Clear Schema** | Tool descriptions must be accurate, avoiding ambiguity | Includes examples and use cases |
| **Parameter Validation** | Validates parameter validity before calls | Implements complete validation in validate() |
| **Secure Sandbox** | Executes all tools in a sandbox | Uses ToolSandbox to control execution boundaries |
| **Smart Retry** | Decides whether to retry based on error type | Uses ToolErrorClassifier to classify errors |
| **Usage Statistics** | Records call metrics for each tool | Uses ToolRegistry for built-in statistics |
| **Permission Control** | Controls permissions by namespace and operation type | Uses ToolPermissionManager |
| **MCP Standardization** | Implements tool interoperability following MCP protocol | Uses MCPToolAdapter for integration |

## 8.2 Anti-patterns

| Anti-pattern | Problem | Correct approach |
|--------|------|----------|
| **Overloaded Tools** | Provides Agent with all possible tools | Dynamically loads, minimal essential set |
| **Vague Descriptions** | Tool descriptions are unclear | Each tool has a precise one-liner description |
| **No Parameter Validation** | Accepts arbitrary inputs | Type checking + enum restrictions + regex validation |
| **No Error Handling** | Returns "Error" on tool failure | Returns specific error types and recovery suggestions |
| **Hardcoded Tools** | Same set of tools for all scenarios | Dynamically combines by task type |
| **No Audit Logs** | Does not record tool invocation history | Logs each invocation for audit |

---

## Related Documentation

| Documentation | Related content |
|------|--------|
| [30 - Agent Harness Engineering](./30-agent-harness-engineering.md) | Overview of Harness six-layer architecture, principle of tool simplification |
| [31 - Loops and Execution Engine](./31-agent-harness-loop-execution.md) | Flow of tool calls within Loops |
| [35 - Security and Constraints](./35-agent-harness-security-constraints.md) | Tool security sandbox and permission control |
| [05 - Tool Usage and Function Calls](./05-tool-use-function-calling.md) | Foundation theory and guidelines for tool usage |
| [25 - MCP Integration](./25-agent-cli-mcp-integration.md) | MCP Protocol Tools Integration Detailed Explanation |

---

## References

| Source | Content | Date |
|------|------|------|
| Vercel Team | Experiment 15→2: Accuracy Rises from 80% to 100% | 2025 |
| Anthropic | Tool Use Best Practices | 2025-12 |
| OpenAI | Best Practices for Function Calling | 2025 |
| MCP Specification | Model Context Protocol 1.0 | 2025-2026 |

---

*This document is original content by kudig-database project 02-ai-agents series, delving into the engineering design of the Agent Harness tool.*

---

## Obsidian Related Documentation

- 02-ai-agents MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|AI Agent Engineering Special Topic]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|Foundation and Core Architecture of AI Agents]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|Selection and Evaluation of LLM Foundation Models]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Deep Comparison of Mainstream Agent Frameworks]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|Deep Guide on Retrieval-Augmented Generation (RAG)]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Design Guidelines for Tool Usage and Function Calling]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Architecture for Multi-Agent Orchestration and Collaboration]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Engineering Memory Management and Context Window]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Evaluation System and Observability of Agents]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]

## See Also

- 30-agent-harness-engineering
- 31-agent-harness-loop-execution
- 33-agent-harness-context-memory
- 34-agent-harness-verification-quality


<!-- risk-assessed -->
