---
title: Agent Harness Multi-Agent Orchestration (domain-14-ai-ml-infra)
description: 'description: ''**Document Type**: Deep Engineering Topic of Harness | **Last Updated**: 2026-04 | **Keywords**:
  Multi-Agent,'
summary: 'description: ''**Document Type**: Deep Engineering Topic of Harness | **Last Updated**: 2026-04 | **Keywords**: Multi-Agent,
category: general
tags:
- ai
- ai-agent
- prometheus
- helm
- llm
- rag
- agent
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- all engineers
estimated_read_time: 25min
intent_queries:
- What is Agent Harness Multi-Agent Orchestration
- How to do Agent Harness Multi-Agent Orchestration
- Kubernetes 14 ai ml infra best practices
trigger_keywords:
- Agent
- Harness
- Agent
- Orchestration
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- helm-basics
- prometheus-basics
- logging-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/37-agent-harness-multi-agent.md
---

> **Production Environment Security Tips**
>
> The commands in this document are executable directly. Please confirm before execution: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether the commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information collection, no side effects).




title: Agent Harness Multi-Agent Orchestration
description: '**Document Type**: Deep Engineering Topic of Harness | **Last Updated**: 2026-04 | **Keywords**: Multi-Agent, Orchestration, Orchestrator, Layered Harness, Agent Communication, Task Decomposition, Conflict Resolution, Isolation Principle, DAG, Workflow'
  Orchestration, Orchestrator, Layered Harness, Agent Communication, Task Decomposition, Conflict Resolution, Principle of Isolation, DAG, Workflow'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- [[Prometheus|prometheus]]
- [[Helm|helm]]
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Architect
- SRE
estimated_read_time: 5min
intent_queries:
- What is Agent Harness Multi-Agent Orchestration
- How to do Agent Harness Multi-Agent Orchestration
trigger_keywords:
- Agent
- Harness
- Agent
- Orchestration
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

# Agent Harness Multi-Agent Orchestration

> **Document Type**: Deep Engineering Topic of Harness | **Last Updated**: 2026-04 | **Keywords**: Multi-Agent, Orchestration, Orchestrator, Layered Harness, Agent Communication, Task Decomposition, Conflict Resolution, Isolation Principle, DAG, Workflow

---

## Overview

After a single Agent's Harness is ready, the next challenge is **orchestration of multiple Agents' Harnesses**. Production-grade systems often require multiple specialized Agents to collaborate—diagnostic Agents to find root causes, repair Agents to execute operations, and validation Agents to confirm recovery. Each Agent has its own Harness (with different permissions, tools, and constraints), and the orchestration layer needs to coordinate their collaboration, communication, and conflict resolution.

This article systematically discusses multi-Agent orchestration patterns, Orchestrator design, Agent communication protocols, task decomposition and allocation, Harness isolation principles, conflict resolution mechanisms, and practical collaboration practices for multiple Agents in Kubernetes (K8S) operational scenarios.

---

## 1. Multi-Agent Orchestration Patterns

## 1.1 Four Core Orchestration Patterns

```
多 Agent 编排模式:

1. 顺序流水线（Sequential Pipeline）
   Agent A → Agent B → Agent C
   每个 Agent 的输出是下一个的输入
   示例: 诊断 → 修复 → 验证

2. 并行扇出（Parallel Fan-out）
   Agent A ─┐
   Agent B ─┼→ 聚合器 → 输出
   Agent C ─┘
   多个 Agent 同时处理不同子任务
   示例: 同时检查 Pod/Node/Network

3. 层级委派（Hierarchical Delegation）
   Orchestrator Agent
      ├── 子 Agent A（诊断）
      ├── 子 Agent B（监控分析）
      └── 子 Agent C（文档生成）
   主 Agent 分解任务并委派
   示例: SRE 指挥官 Agent 调度诊断团队

4. 辩论共识（Debate & Consensus）
   Agent A ←→ Agent B
      ↓         ↓
      共识判断器
   多个 Agent 对同一问题给出独立判断，通过辩论达成共识
   示例: 两个诊断 Agent 交叉验证根因
```

## 1.2 Pattern Selection Matrix

| Pattern | Applicable Scenarios | Latency | Cost | Reliability | Complexity |
|------|---------|------|------|--------|--------|
| **Sequential Pipeline** | Tasks with clear stages | High | Low | Medium | Low |
| **Parallel Fanout** | Independent sub-tasks that can be parallelized | Low | Medium | High | Medium |
| **Hierarchical Delegation** | Complex multi-step tasks | Medium | High | High | High |
| **Consensus Debate** | High-risk decisions requiring cross-validation | High | High | Highest | High |

---

## 2. Orchestrator Design

## 2.1 Orchestrator Architecture

```python
from dataclasses import dataclass, field
from typing import Optional, Any
from enum import Enum
import asyncio

class AgentRole(Enum):
    DIAGNOSTICIAN = "diagnostician"
    REMEDIATOR = "remediator"
    VERIFIER = "verifier"
    ANALYST = "analyst"
    COORDINATOR = "coordinator"

@dataclass
class AgentSpec:
    """Agent Specification Definition"""
    role: AgentRole
    harness_config: dict
    tools: list[str]
    constraints: dict
    model: str = "gpt-4o"
    priority: int = 0

class Orchestrator:
    """Multi-Agent Orchestrator"""

    def __init__(self, agent_specs: dict[str, AgentSpec]):
        self.specs = agent_specs
        self.agents: dict[str, Any] = {}
        self._execution_graph: list = []
        self._results: dict[str, Any] = {}

    def register_agent(self, name: str, agent, harness):
        """Registering Agents and Their Harnesses"""
        self.agents[name] = {
            "agent": agent,
            "harness": harness,
            "spec": self.specs[name],
        }

    async def execute_pipeline(self, task: str, pipeline: list[dict]) -> dict:
        """Executing Sequential Pipelines"""
        context = {"original_task": task}

        for stage in pipeline:
            agent_name = stage["agent"]
            agent_info = self.agents[agent_name]
            stage_task = stage.get("task_template", "{task}").format(
                task=task, **context,
            )

            result = await self._run_agent(
                agent_name, stage_task, context,
            )

            context[f"{agent_name}_result"] = result
            self._results[agent_name] = result

            # Stage-to-stage gating: Continue if current stage fails
            if not result.get("success") and stage.get("gate", True):
                return {
                    "status": "pipeline_halted",
                    "halted_at": agent_name,
                    "reason": result.get("error"),
                    "results": self._results,
                }

        return {
            "status": "pipeline_complete",
            "results": self._results,
        }

    async def execute_parallel(self, task: str,
                                agent_names: list[str]) -> dict:
        """Executing Parallel Fanouts"""
        tasks = []
        for name in agent_names:
            tasks.append(self._run_agent(name, task, {}))

        results = await asyncio.gather(*tasks, return_exceptions=True)

        parallel_results = {}
        for name, result in zip(agent_names, results):
            if isinstance(result, Exception):
                parallel_results[name] = {
                    "success": False, "error": str(result),
                }
            else:
                parallel_results[name] = result

        # Aggregating Results
        aggregated = self._aggregate_results(parallel_results)

        return {
            "status": "parallel_complete",
            "individual_results": parallel_results,
            "aggregated": aggregated,
        }

    async def execute_hierarchical(self, task: str) -> dict:
        """Execute Hierarchical Delegation"""
        # 1. Coordinator Agent Decompose Task
        coordinator = self.agents.get("coordinator")
        decomposition = await self._run_agent(
            "coordinator", f"分解以下任务为子任务: {task}", {},
        )

        subtasks = decomposition.get("subtasks", [])
        if not subtasks:
            return {"status": "decomposition_failed", "error": "无法分解任务"}

        # 2. Assign Subtasks to Professional Agents
        sub_results = {}
        for subtask in subtasks:
            agent_name = subtask.get("assign_to")
            if agent_name in self.agents:
                result = await self._run_agent(
                    agent_name, subtask["description"], {},
                )
                sub_results[agent_name] = result

        # 3. Coordinator Synthesize Results
        synthesis = await self._run_agent(
            "coordinator",
            f"综合以下子任务结果:\n{sub_results}",
            {"sub_results": sub_results},
        )

        return {
            "status": "hierarchical_complete",
            "decomposition": decomposition,
            "sub_results": sub_results,
            "synthesis": synthesis,
        }

    async def _run_agent(self, name: str, task: str,
                          context: dict) -> dict:
        """Run a Single Agent"""
        agent_info = self.agents[name]
        harness = agent_info["harness"]

        result = await harness.async_run(task, context)
        return result

    def _aggregate_results(self, results: dict) -> dict:
        """Aggregate Parallel Results"""
        successful = {k: v for k, v in results.items() if v.get("success")}
        failed = {k: v for k, v in results.items() if not v.get("success")}

        return {
            "total_agents": len(results),
            "successful": len(successful),
            "failed": len(failed),
            "consensus": self._find_consensus(successful),
        }

    def _find_consensus(self, results: dict) -> Optional[str]:
        """Find Consensus Among Multiple Successful Results"""
        if len(results) <= 1:
            return list(results.values())[0].get("answer") if results else None

        # Simple Strategy: If the answers from most Agents are similar, adopt the majority answer
        answers = [v.get("answer", "") for v in results.values()]
        # Production environments should use semantic similarity comparison
        return answers[0]
```

---

## 3. Agent Communication

## 3.1 Message Protocol

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional
from enum import Enum

class MessageType(Enum):
    TASK_ASSIGNMENT = "task_assignment"
    TASK_RESULT = "task_result"
    INFORMATION_REQUEST = "info_request"
    INFORMATION_RESPONSE = "info_response"
    APPROVAL_REQUEST = "approval_request"
    APPROVAL_RESPONSE = "approval_response"
    STATUS_UPDATE = "status_update"
    ESCALATION = "escalation"

@dataclass
class AgentMessage:
    """Messages between Agents"""
    id: str
    type: MessageType
    sender: str
    receiver: str
    content: dict
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat())
    correlation_id: Optional[str] = None  # 关联同一会话的消息
    priority: int = 0
    ttl_seconds: int = 300  # 消息过期时间

class MessageBus:
    """Agent Message Bus"""

    def __init__(self):
        self._queues: dict[str, list[AgentMessage]] = {}
        self._handlers: dict[str, list] = {}
        self._history: list[AgentMessage] = []

    def send(self, message: AgentMessage):
        """Send Messages"""
        receiver = message.receiver
        if receiver not in self._queues:
            self._queues[receiver] = []
        self._queues[receiver].append(message)
        self._history.append(message)

        # Trigger Handler
        for handler in self._handlers.get(receiver, []):
            handler(message)

    def receive(self, agent_name: str,
                message_type: MessageType = None) -> list[AgentMessage]:
        """Receive Messages"""
        queue = self._queues.get(agent_name, [])
        if message_type:
            messages = [m for m in queue if m.type == message_type]
        else:
            messages = queue.copy()

        # Clear Read Messages
        for m in messages:
            if m in queue:
                queue.remove(m)

        return messages

    def subscribe(self, agent_name: str, handler):
        """Subscribe to Messages"""
        if agent_name not in self._handlers:
            self._handlers[agent_name] = []
        self._handlers[agent_name].append(handler)

    def broadcast(self, sender: str, content: dict,
                  message_type: MessageType = MessageType.STATUS_UPDATE):
        """Broadcast Messages to All Agents"""
        for agent_name in self._queues:
            if agent_name != sender:
                self.send(AgentMessage(
                    id=f"broadcast_{datetime.utcnow().timestamp()}",
                    type=message_type,
                    sender=sender,
                    receiver=agent_name,
                    content=content,
                ))
```

## 3.2 Shared Context Management

```python
class SharedContext:
    """Multi-Agent Shared Context"""

    def __init__(self):
        self._shared_state: dict = {}
        self._agent_contributions: dict[str, list] = {}
        self._locks: dict[str, bool] = {}

    def write(self, agent_name: str, key: str, value: Any,
              overwrite: bool = False):
        """Write Shared Context"""
        if key in self._shared_state and not overwrite:
            # Append instead of overwrite
            if isinstance(self._shared_state[key], list):
                self._shared_state[key].append(value)
            else:
                self._shared_state[key] = [self._shared_state[key], value]
        else:
            self._shared_state[key] = value

        # Record contributions
        if agent_name not in self._agent_contributions:
            self._agent_contributions[agent_name] = []
        self._agent_contributions[agent_name].append({
            "key": key, "timestamp": datetime.utcnow().isoformat(),
        })

    def read(self, key: str, default: Any = None) -> Any:
        """Read Shared Context"""
        return self._shared_state.get(key, default)

    def read_all(self) -> dict:
        """Read All Shared Context"""
        return self._shared_state.copy()

    def get_agent_contributions(self, agent_name: str) -> list:
        """Get Contribution Records for a Specific Agent"""
        return self._agent_contributions.get(agent_name, [])
```

---

## 4. Harness Isolation Principle

## 4.1 Agent Isolation Architecture

```
多 Agent Harness 隔离:

┌──────────────────────────────────────────────────────┐
│                  Orchestrator Harness                  │
│  全局约束 │ 任务分配 │ 结果聚合 │ 冲突解决            │
├──────────────────────────────────────────────────────┤
│                                                        │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐ │
│  │ 诊断 Agent    │  │ 修复 Agent    │  │ 验证 Agent   │ │
│  │              │  │              │  │              │ │
│  │ Constraints: │  │ Constraints: │  │ Constraints: │ │
│  │  只读        │  │  写+审批     │  │  只读+对比   │ │
│  │              │  │              │  │              │ │
│  │ Tools:       │  │ Tools:       │  │ Tools:       │ │
│  │  get/describe│  │  apply/patch │  │  get/describe│ │
│  │  logs/events │  │  scale/rollout│ │  logs/events │ │
│  │  prom/loki   │  │              │  │  prom query  │ │
│  │              │  │              │  │              │ │
│  │ Verify:      │  │ Verify:      │  │ Verify:      │ │
│  │  事实一致性  │  │  安全检查    │  │  恢复确认    │ │
│  └──────────────┘  └──────────────┘  └──────────────┘ │
│                                                        │
│  隔离规则:                                              │
│  1. 每个 Agent 有独立的 Harness 实例                    │
│  2. 诊断 Agent 不信任修复 Agent 的自述                  │
│  3. 验证 Agent 独立运行，不依赖修复 Agent 的输出        │
│  4. 共享上下文通过 Orchestrator 中转                    │
└──────────────────────────────────────────────────────┘
```

## 4.2 Implementing Isolation

```python
class IsolatedHarnessFactory:
    """Isolated Harness Factory: Create Independent Harnesses for Different Roles"""

    ROLE_CONFIGS = {
        AgentRole.DIAGNOSTICIAN: {
            "constraints": {
                "read_only": True,
                "can_write": False,
                "can_delete": False,
                "max_iterations": 10,
                "max_tokens": 30_000,
                "blocked_commands": [
                    "kubectl delete", "kubectl drain",
                    "kubectl apply", "kubectl patch",
                    "helm install", "helm uninstall",
                ],
            },
            "tools": [
                "kubectl_get", "kubectl_describe", "kubectl_logs",
                "kubectl_events", "kubectl_top",
                "prometheus_query", "loki_search",
            ],
            "verifiers": [
                "factual_consistency",
                "output_format",
                "completeness",
            ],
        },
        AgentRole.REMEDIATOR: {
            "constraints": {
                "read_only": False,
                "can_write": True,
                "can_delete": False,
                "max_iterations": 5,
                "max_tokens": 20_000,
                "require_approval": True,
                "blocked_commands": [
                    "kubectl delete namespace",
                    "kubectl drain --force",
                    "helm uninstall",
                ],
            },
            "tools": [
                "kubectl_get", "kubectl_describe",
                "kubectl_apply", "kubectl_patch",
                "kubectl_scale", "kubectl_rollout",
            ],
            "verifiers": [
                "command_safety",
                "output_format",
            ],
        },
        AgentRole.VERIFIER: {
            "constraints": {
                "read_only": True,
                "can_write": False,
                "can_delete": False,
                "max_iterations": 5,
                "max_tokens": 15_000,
            },
            "tools": [
                "kubectl_get", "kubectl_describe",
                "kubectl_logs", "kubectl_events",
                "prometheus_query",
            ],
            "verifiers": [
                "factual_consistency",
            ],
        },
    }

    def create_harness(self, role: AgentRole, llm, tools_registry) -> dict:
        """Create Isolated Harness for a Specific Role"""
        config = self.ROLE_CONFIGS.get(role, {})

        # Filter toolkit
        allowed_tools = config.get("tools", [])
        filtered_tools = tools_registry.get_tools_for_task(
            categories=None,
            max_tools=len(allowed_tools),
        )

        return {
            "role": role,
            "constraints": config.get("constraints", {}),
            "tools": filtered_tools,
            "verifiers": config.get("verifiers", []),
        }
```

---

## 5. Conflict Resolution

## 5.1 Types of Conflicts and Resolution Strategies

```python
class ConflictResolver:
    """Multi-Agent Conflict Resolver"""

    def resolve(self, agent_results: dict[str, dict],
                conflict_type: str) -> dict:
        """Resolve Conflicts Between Agents"""
        strategies = {
            "diagnosis_disagreement": self._resolve_diagnosis,
            "action_conflict": self._resolve_action,
            "priority_conflict": self._resolve_priority,
        }

        strategy = strategies.get(conflict_type, self._resolve_default)
        return strategy(agent_results)

    def _resolve_diagnosis(self, results: dict) -> dict:
        """Diagnose Dispute Resolution: Weighted Voting"""
        diagnoses = []
        for agent, result in results.items():
            diagnoses.append({
                "agent": agent,
                "diagnosis": result.get("root_cause", ""),
                "confidence": result.get("confidence", 0),
                "evidence_count": len(result.get("evidence", [])),
            })

        # Sort by confidence × evidence count
        diagnoses.sort(
            key=lambda d: d["confidence"] * (1 + d["evidence_count"] * 0.1),
            reverse=True,
        )

        winner = diagnoses[0]

        # If highest confidence < 0.7 and there's a dispute, escalate to manual
        if winner["confidence"] < 0.7 and len(set(d["diagnosis"] for d in diagnoses)) > 1:
            return {
                "resolution": "escalate_to_human",
                "reason": "诊断分歧且置信度不足",
                "candidates": diagnoses,
            }

        return {
            "resolution": "accepted",
            "selected_agent": winner["agent"],
            "diagnosis": winner["diagnosis"],
            "confidence": winner["confidence"],
            "dissenting": [d for d in diagnoses if d["agent"] != winner["agent"]],
        }

    def _resolve_action(self, results: dict) -> dict:
        """Action Conflict Resolution: Security First"""
        actions = []
        for agent, result in results.items():
            actions.append({
                "agent": agent,
                "action": result.get("recommended_action", {}),
                "risk_level": result.get("risk_level", "unknown"),
            })

        # Choose the Action Plan with Lowest Risk
        risk_order = {"low": 0, "medium": 1, "high": 2, "critical": 3, "unknown": 4}
        actions.sort(key=lambda a: risk_order.get(a["risk_level"], 4))

        return {
            "resolution": "lowest_risk",
            "selected": actions[0],
            "alternatives": actions[1:],
        }

    def _resolve_priority(self, results: dict) -> dict:
        """Priority Conflict: By Role Weight"""
        role_weights = {
            AgentRole.DIAGNOSTICIAN: 3,
            AgentRole.VERIFIER: 2,
            AgentRole.REMEDIATOR: 1,
        }
        # Choose Action Plan by Role Weight
        sorted_results = sorted(
            results.items(),
            key=lambda x: role_weights.get(x[1].get("role"), 0),
            reverse=True,
        )
        return {"resolution": "role_priority", "selected": sorted_results[0]}

    def _resolve_default(self, results: dict) -> dict:
        return {"resolution": "first_successful",
                "selected": next(iter(results.values()))}
```

---

## 6. K8S Problem Handling Multi-Agent Orchestration

## 6.1 Problem Handling Pipeline

```python
class IncidentResponsePipeline:
    """K8S Problem Handling Multi-Agent Pipeline"""

    def __init__(self, orchestrator: Orchestrator):
        self.orchestrator = orchestrator

    async def handle_incident(self, incident: dict) -> dict:
        """Handle the Problem"""

        # Stage 1: Parallel Diagnosis (Collect Information from Multiple Angles)
        parallel_diagnosis = await self.orchestrator.execute_parallel(
            task=f"诊断以下问题: {incident['description']}",
            agent_names=["pod_diagnostician", "node_diagnostician", "network_diagnostician"],
        )

        # Stage 2: Synthesize Diagnostic Results
        diagnosis = self._synthesize_diagnosis(parallel_diagnosis)
        if diagnosis.get("confidence", 0) < 0.6:
            return {
                "status": "escalate",
                "reason": "多 Agent 诊断置信度不足",
                "diagnosis_results": parallel_diagnosis,
            }

        # Stage 3: Generate Repair Solution
        remediation = await self.orchestrator.execute_pipeline(
            task=f"根据诊断结果制定修复方案: {diagnosis['root_cause']}",
            pipeline=[
                {"agent": "remediator", "gate": True},
            ],
        )

        # Stage 4: Independently Validate Repair Effectiveness
        verification = await self.orchestrator.execute_pipeline(
            task=f"验证问题是否已恢复: {incident['description']}",
            pipeline=[
                {"agent": "verifier", "gate": False},
            ],
        )

        return {
            "status": "resolved" if verification.get("success") else "partially_resolved",
            "diagnosis": diagnosis,
            "remediation": remediation,
            "verification": verification,
        }

    def _synthesize_diagnosis(self, parallel_results: dict) -> dict:
        """Synthesize Diagnostics from Multiple Agents"""
        resolver = ConflictResolver()
        individual = parallel_results.get("individual_results", {})

        # If All Agents Point to the Same Root Cause
        root_causes = [
            r.get("answer", {}).get("root_cause", "")
            for r in individual.values()
            if r.get("success")
        ]

        if len(set(root_causes)) == 1 and root_causes[0]:
            return {
                "root_cause": root_causes[0],
                "confidence": 0.95,
                "consensus": "unanimous",
            }

        # Otherwise Resolve Conflicts
        return resolver.resolve(individual, "diagnosis_disagreement")
```

---

## 7. Layered Harness Architecture

## 7.1 Foundation Layer + Scenario Layer + User Layer

```python
class LayeredHarnessArchitecture:
    """Three-Layer Harness Architecture"""

    def __init__(self):
        # Layer 1: Foundation Layer (Shared by All Agents)
        self.base_config = {
            "max_iterations": 20,
            "timeout_seconds": 300,
            "safety_checks": True,
            "otel_tracing": True,
            "pii_filtering": True,
            "audit_logging": True,
        }

        # Layer 2: Scenario Layer (Differentiated by Scenarios)
        self.scenario_configs = {
            "k8s_diagnosis": {
                "read_only": True,
                "tools": ["kubectl_get", "kubectl_describe", "kubectl_logs",
                         "prometheus_query"],
                "max_iterations": 10,
                "verifiers": ["factual_consistency", "output_format"],
            },
            "k8s_remediation": {
                "read_only": False,
                "require_approval": True,
                "tools": ["kubectl_apply", "kubectl_patch", "kubectl_scale"],
                "max_iterations": 5,
                "verifiers": ["command_safety", "output_format"],
            },
            "code_review": {
                "read_only": True,
                "tools": ["read_file", "search_code", "run_tests"],
                "max_iterations": 15,
                "verifiers": ["completeness"],
            },
        }

        # Layer 3: User Layer (User Customizable Override)
        self.user_config = None

    def build_harness(self, scenario: str, user_overrides: dict = None) -> dict:
        """Build the final Harness configuration"""
        # Foundation Layer
        config = self.base_config.copy()

        # Scenario Layer Override
        scenario_config = self.scenario_configs.get(scenario, {})
        config.update(scenario_config)

        # User Layer Override
        if user_overrides:
            config.update(user_overrides)

        return config
```

---

## 8. Best Practices

## 8.1 Core Principles for Multi-Agent Orchestration

| Principle | Explanation | Practice Recommendation |
|------|------|---------|
| **Harness Isolation** | Each Agent has its own Harness | Read-only diagnostics, approval required for fixes, independent validation |
| **Minimal Trust** | Agents do not trust each other's outputs | Validate that each Agent independently checks and verifies the repair results |
| **Consensus Decision Making** | High-risk operations require consensus from multiple Agents | Use a debate consensus mode |
| **Security First** | In case of conflict, choose the lowest-risk solution | ConflictResolver with a security-first strategy |
| **Layered Configuration** | Three layers of Harness: Foundation + Scenario + User | Use LayeredHarnessArchitecture |
| **Asynchronous Communication** | Agents communicate through a message bus | Use MessageBus to decouple them |

## 8.2 Anti-patterns

| Anti-pattern | Problem | Correct Approach |
|--------|------|----------|
| **Shared Harness** | All Agents use the same constraints | Each role should have its own set of constraints |
| **Direct Communication** | Agents directly call each other | Use Orchestrator to act as a mediator |
| **Blindly Trusting Results** | Believe an Agent when it says "fixed" | Independently validate the results reported by the Agent |
| **Serial Everything** | All Agents execute sequentially | Parallelize diagnostic tasks that can be executed concurrently |
| **Conflict Resolution** | Ignore Disputes Between Agents | Deploy Conflict Resolution Mechanisms |

---

## Associated Documents

| Document | Related Content |
|------|--------|
| [30 - Agent Harness Engineering](./30-agent-harness-engineering.md) | Foundation Concepts for Multi-Agent Orchestration |
| [35 - Security and Constraints](./35-agent-harness-security-constraints.md) | Implementation of Isolation Constraints for Agents |
| [06 - Multi-Agent Orchestration](./06-multi-agent-orchestration.md) | Theoretical Foundations for Multi-Agent Orchestration |

---

## References

| Source | Content | Date |
|------|------|------|
| Anthropic | Best Practices for Multi-Agent System Design | 2026-02 |
| Microsoft | AutoGen Multi-Agent Framework | 2025-2026 |
| LangChain | LangGraph Multi-Agent Orchestration | 2025-2026 |
| CrewAI | Roles and Collaboration Patterns for Agents | 2025-2026 |

---

*This document is original content from the kudig-database project series 02-ai-agents, delving into Multi-Agent Orchestration of Agent Harness.*

---

## Related Obsidian Documents

- 02-ai-agents KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|[[AI Agent Engineering Topic|AI Agent Engineering Topic]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|Foundation and Core Architecture of AI Agents]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|Selection and Evaluation of LLM Foundation Models]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Deep Comparison of Mainstream Agent Frameworks]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|Deep Guide to Retrieval-Augmented Generation with RAG]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Design Guidelines for Tool Use and Function Calling]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Multi-Agent Orchestration and Collaboration Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]

## See Also

- 35-agent-harness-security-constraints
- 36-agent-harness-observability
- 38-agent-harness-performance-cost
- 39-agent-harness-testing-benchmark


<!-- risk-assessed -->
