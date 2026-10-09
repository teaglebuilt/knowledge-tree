---
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/06-multi-agent-orchestration.md
---
title: Multi-Agent Orchestration and Collaboration Architecture (domain-14-ai-ml-infra)
description: 'title: Multi-Agent Orchestration and Collaboration Architecture'
summary: 'title: Multi-Agent Orchestration and Collaboration Architecture'
category: general
tags:
- ai
- ai-agent
- scheduler
- prometheus
- grafana
- redis
- postgresql
- kafka
- hpa
- gateway
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 25min
intent_queries:
- What is Multi-Agent Orchestration and Collaboration Architecture
- How to use Multi-Agent Orchestration and Collaboration Architecture
- Kubernetes 14 AI ML Infrastructure Best Practices
trigger_keywords:
- Agent
- Orchestration and Collaboration Architecture
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- prometheus-basics
- monitoring-basics
- kafka-basics
- redis-basics
authors:
- name: Dillan Teagle
  role: contributor

---

> **Production Environment Security Tips**
>
> This document contains executable operational commands. Execute at your own risk: confirm that the target cluster and Namespace are correct; ensure you have sufficient RBAC permissions; verify these commands in a non-production environment first. Risk level annotations: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (modifies cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering, no side effects).




title: Multi-Agent Orchestration and Collaboration Architecture
description: '# Multi-Agent Orchestration and Collaboration Architecture'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- scheduler
- [[Prometheus|prometheus]]
- grafana
- redis
- postgresql
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Architects
- SRE
estimated_read_time: 5min
intent_queries:
- What is Multi-Agent Orchestration and Collaboration Architecture
- How to use Multi-Agent Orchestration and Collaboration Architecture
trigger_keywords:
- Agent
- Orchestration and Collaboration Architecture
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

# Multi-Agent Orchestration and Collaboration Architecture

> **Document Type**: Architecture Design Special Topic | **Last Updated**: 2026-03 | **Keywords**: Multi-Agent, Supervisor-Worker, Event-driven, Agent Orchestration, LangGraph, AutoGen, Distributed Agent, Conflict Resolution, Agent Communication Protocol

---

## Overview

Single-Agent systems are limited in handling complex tasks that require expertise from multiple domains. Multi-Agent systems leverage professional specialization and collaboration to handle more complex tasks, improve parallel efficiency, and reduce risks associated with single points of failure. This article covers core design patterns for multi-agent systems, the implementation of LangGraph/AutoGen, [[domain-14-ai-ml-infra/03-agent-runtime/11-agent-communication-protocols.md|communication protocols]], conflict resolution strategies, and the architecture design of a production-grade multi-agent platform.

---

## 1. Multi-Agent Architectural Patterns

## 1.1 Six Core Patterns

```
多 Agent 架构模式
│
├── 1. Supervisor-Worker（主管-工作者）
│      Orchestrator 分解任务 → 分发给专业 Worker Agent
│      适合: 任务可分解为子任务的场景
│
├── 2. Pipeline（流水线）
│      Agent A → Agent B → Agent C → 结果
│      适合: 有明确处理顺序的串行任务
│
├── 3. Peer-to-Peer（对等协作）
│      多个 Agent 平等协商，共同决策
│      适合: 需要多视角验证的决策场景
│
├── 4. Blackboard（黑板系统）
│      共享状态黑板，多 Agent 读写协作
│      适合: 异步、松耦合的并行任务
│
├── 5. Debate（辩论模式）
│      多个 Agent 提出不同方案，通过辩论收敛到最优解
│      适合: 高风险决策需要多方验证
│
└── 6. Hierarchical（层级模式）
       多层 Orchestrator + 专业 Agent 的树状结构
       适合: 大规模复杂系统
```

---

## 2. Supervisor-Worker Pattern (Most Commonly Used in Production)

## 2.1 Architecture Design

```
┌─────────────────────────────────────────────────────────────┐
│                     Orchestrator Agent                       │
│                    （任务分解 + 调度）                          │
│              使用强模型: GPT-4o / Claude 3.5 Sonnet           │
└──────┬──────────────┬──────────────┬──────────────┬──────────┘
       │              │              │              │
       ▼              ▼              ▼              ▼
┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐
│  网络     │  │  存储     │  │  应用     │  │  安全     │
│  诊断    │  │  诊断    │  │  诊断    │  │  审计    │
│  Worker  │  │  Worker  │  │  Worker  │  │  Worker  │
│(专用工具) │  │(专用工具) │  │(专用工具) │  │(专用工具) │
└──────────┘  └──────────┘  └──────────┘  └──────────┘
       │              │              │              │
       └──────────────┴──────────────┴──────────────┘
                              │
                     ┌──────────────┐
                     │ 结果聚合 Agent │
                     │ (综合报告生成) │
                     └──────────────┘
```

## 2.2 LangGraph Implementation

```python
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated, Literal
import operator

# Define Shared State
class OrchestratorState(TypedDict):
    original_task: str
    subtasks: list[dict]
    worker_results: Annotated[dict, lambda a, b: {**a, **b}]  # 合并字典
    final_report: str
    current_stage: str
    error_count: int

# Initialize Model
orchestrator_llm = ChatOpenAI(model="gpt-4o", temperature=0)
worker_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)  # Worker 用便宜模型

# Orchestrator: Task Decomposition
def orchestrator_node(state: OrchestratorState) -> OrchestratorState:
    """Decompose complex tasks into specialized sub-tasks"""
    response = orchestrator_llm.invoke(f"""
    你是运维任务调度专家。将以下复杂任务分解为专业子任务：
    
    任务：{state['original_task']}
    
    可用的专业 Worker：
    - network_worker: 网络连通性、DNS、Service、NetworkPolicy 诊断
    - storage_worker: PVC、StorageClass、CSI 相关问题
    - app_worker: Pod 状态、容器日志、应用配置问题
    - security_worker: RBAC、证书、权限相关问题
    
    输出 JSON 格式的子任务列表，每个子任务指定：worker、任务描述、优先级
    """)
    
    subtasks = parse_subtasks(response.content)
    return {"subtasks": subtasks, "current_stage": "dispatched"}

# Network Diagnostics Worker
def network_worker_node(state: OrchestratorState) -> OrchestratorState:
    """Specialized Network Diagnosis"""
    network_tasks = [t for t in state["subtasks"] if t["worker"] == "network_worker"]
    if not network_tasks:
        return {"worker_results": {}}
    
    # Network Workers have specific toolsets
    network_tools = [test_connectivity_tool, get_dns_tool, get_networkpolicy_tool]
    network_agent = create_react_agent(worker_llm, network_tools)
    
    results = {}
    for task in network_tasks:
        result = network_agent.invoke({"input": task["description"]})
        results[f"network_{task['id']}"] = result["output"]
    
    return {"worker_results": results}

# Result Aggregation
def aggregator_node(state: OrchestratorState) -> OrchestratorState:
    """Aggregate results from all workers to generate a comprehensive report"""
    report = orchestrator_llm.invoke(f"""
    原始任务：{state['original_task']}
    
    各 Worker 诊断结果：
    {format_worker_results(state['worker_results'])}
    
    请生成：
    1. 根因分析摘要
    2. 问题优先级排序
    3. 综合修复方案
    4. 实施步骤（带风险提示）
    """)
    
    return {"final_report": report.content, "current_stage": "complete"}

# Routing: Decide which Workers to Execute (Parallel Execution)
def route_to_workers(state: OrchestratorState) -> list[str]:
    """Parallelly dispatch all necessary workers"""
    workers_needed = set(t["worker"] for t in state["subtasks"])
    return list(workers_needed)  # LangGraph 支持返回列表实现并行

# Build Graph
workflow = StateGraph(OrchestratorState)

workflow.add_node("orchestrator", orchestrator_node)
workflow.add_node("network_worker", network_worker_node)
workflow.add_node("storage_worker", storage_worker_node)
workflow.add_node("app_worker", app_worker_node)
workflow.add_node("security_worker", security_worker_node)
workflow.add_node("aggregator", aggregator_node)

workflow.set_entry_point("orchestrator")

# Parallel Dispatch to Multiple Workers
workflow.add_conditional_edges(
    "orchestrator",
    route_to_workers,
    {
        "network_worker": "network_worker",
        "storage_worker": "storage_worker",
        "app_worker": "app_worker",
        "security_worker": "security_worker",
    }
)

# Aggregate Results After All Workers Complete
for worker in ["network_worker", "storage_worker", "app_worker", "security_worker"]:
    workflow.add_edge(worker, "aggregator")

workflow.add_edge("aggregator", END)

# Compilation
multi_agent_app = workflow.compile()
```

---

## 3. Debate (Debate) Mode: High-Risk Decisions

Applies to high-risk scenarios such as production changes, where multiple Agents review proposals from different perspectives:

```python
class DebateOrchestrator:
    """Debate Mode: Multi-Agent Multi-Round Debates"""
    
    def __init__(self, llm, rounds: int = 2):
        self.llm = llm
        self.rounds = rounds
        
        # Different Roles' Agents (Same LLM, Different System Prompts)
        self.agents = {
            "proposer": "你是变更方案提出者，负责提出并捍卫你的技术方案",
            "critic": "你是技术审查员，专门发现方案中的风险和缺陷，持批评态度",
            "safety_reviewer": "你是 SRE 安全审查员，关注方案对生产稳定性的影响",
            "moderator": "你是讨论主持人，总结各方观点并推动收敛到最终决策",
        }
    
    def debate(self, proposal: str) -> dict:
        """Execute Multi-Round Debates"""
        debate_history = []
        
        # Initial Proposal
        proposer_response = self._agent_respond(
            "proposer", f"请详细阐述以下方案的技术实现和优势：\n{proposal}", []
        )
        debate_history.append({"role": "proposer", "content": proposer_response})
        
        # Multiple Rounds of Debate
        for round_num in range(self.rounds):
            # Reviewer Raises Questions
            critic_response = self._agent_respond(
                "critic", 
                f"针对以下提案，指出3-5个技术风险和潜在缺陷：",
                debate_history
            )
            debate_history.append({"role": "critic", "content": critic_response})
            
            # Security Review
            safety_response = self._agent_respond(
                "safety_reviewer",
                "从生产稳定性角度评估该方案的风险：",
                debate_history
            )
            debate_history.append({"role": "safety_reviewer", "content": safety_response})
            
            # Proposer Responds
            defense = self._agent_respond(
                "proposer",
                "回应以上质疑，必要时修改和完善你的方案：",
                debate_history
            )
            debate_history.append({"role": "proposer", "content": defense})
        
        # Chair Summarizes
        conclusion = self._agent_respond(
            "moderator",
            "综合所有讨论，给出最终决策建议（通过/拒绝/修改后通过），说明理由：",
            debate_history
        )
        
        return {
            "original_proposal": proposal,
            "debate_history": debate_history,
            "conclusion": conclusion,
            "approved": "通过" in conclusion or "修改后通过" in conclusion,
        }
    
    def _agent_respond(self, role: str, task: str, history: list) -> str:
        system_msg = self.agents[role]
        messages = [{"role": "system", "content": system_msg}]
        
        if history:
            messages.append({
                "role": "user",
                "content": f"辩论历史：\n{self._format_history(history)}"
            })
        
        messages.append({"role": "user", "content": task})
        return self.llm.invoke(messages).content
```

---

## 4. Blackboard (Blackboard) Pattern: Asynchronous Collaboration

```python
import asyncio
from dataclasses import dataclass, field
from typing import Optional
import threading

@dataclass
class BlackboardEntry:
    key: str
    value: any
    written_by: str
    timestamp: float
    confidence: float = 1.0  # 置信度，冲突时用于决策

class Blackboard:
    """Shared Knowledge Blackboard: Multi-Agent Asynchronous Read-Write"""
    
    def __init__(self):
        self._data: dict[str, list[BlackboardEntry]] = {}
        self._lock = threading.RLock()
        self._observers: dict[str, list] = {}  # 订阅特定 key 变更的回调
    
    def write(self, key: str, value: any, agent_id: str, confidence: float = 1.0):
        """Agents Write Discovery Results"""
        with self._lock:
            entry = BlackboardEntry(
                key=key, value=value, written_by=agent_id,
                timestamp=time.time(), confidence=confidence
            )
            if key not in self._data:
                self._data[key] = []
            self._data[key].append(entry)
            
            # Notify Subscribers
            for callback in self._observers.get(key, []):
                asyncio.create_task(callback(key, entry))
    
    def read(self, key: str, resolve_conflicts: bool = True) -> Optional[any]:
        """Read Information from the Blackboard, Automatically Resolve Conflicts"""
        with self._lock:
            entries = self._data.get(key, [])
            if not entries:
                return None
            
            if not resolve_conflicts or len(entries) == 1:
                return entries[-1].value
            
            # Conflict Resolution: Choose the Highest Confidence
            return max(entries, key=lambda e: e.confidence).value
    
    def subscribe(self, key: str, callback):
        """Subscribe to Specific Key's Change Events"""
        if key not in self._observers:
            self._observers[key] = []
        self._observers[key].append(callback)

class BlackboardAgent:
    """Asynchronous Agents Based on the Blackboard"""
    
    def __init__(self, agent_id: str, specialization: str, blackboard: Blackboard):
        self.agent_id = agent_id
        self.specialization = specialization
        self.blackboard = blackboard
    
    async def observe_and_act(self):
        """Continuous monitoring of the blackboard, taking action based on new information"""
        while True:
            # Check for new professional-related information on the blackboard
            task = self.blackboard.read(f"task_{self.specialization}")
            
            if task and not self.blackboard.read(f"result_{self.agent_id}"):
                # Execute professional analysis
                result = await self._analyze(task)
                
                # Write back the result
                self.blackboard.write(
                    key=f"result_{self.agent_id}",
                    value=result,
                    agent_id=self.agent_id,
                    confidence=result.get("confidence", 0.8)
                )
            
            await asyncio.sleep(1)  # 避免忙等待
```

---

## 5. Multi-Agent Communication Protocol

## 5.1 Standardized Message Format

```python
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class MessageType(Enum):
    TASK_ASSIGN = "task_assign"       # 分配任务
    TASK_RESULT = "task_result"       # 返回结果
    CLARIFICATION = "clarification"   # 请求澄清
    STATUS_UPDATE = "status_update"   # 状态更新
    ERROR_REPORT = "error_report"     # 错误报告
    ESCALATION = "escalation"         # 升级处理
    APPROVAL_REQUEST = "approval_request"  # 请求审批

@dataclass
class AgentMessage:
    """Standard message format for communication between agents"""
    message_id: str
    sender_id: str
    receiver_id: str            # 或 "broadcast"
    message_type: MessageType
    content: dict
    correlation_id: Optional[str] = None  # 关联的父消息 ID
    priority: int = 5           # 1-10，10 最高
    ttl_seconds: int = 300      # 消息有效期
    timestamp: str = ""

# Example of task allocation messages
task_message = AgentMessage(
    message_id="msg-001",
    sender_id="orchestrator",
    receiver_id="network_worker",
    message_type=MessageType.TASK_ASSIGN,
    content={
        "task_id": "task-001",
        "description": "检查 production 命名空间的网络连通性",
        "context": {
            "affected_pods": ["api-server-xxx", "backend-yyy"],
            "symptoms": "前端无法访问后端 Service",
        },
        "constraints": {
            "readonly_only": True,
            "timeout_seconds": 60,
        },
        "expected_output": "网络连通性诊断报告（含根因和修复建议）"
    },
    priority=8,
)

# Example of result return messages
result_message = AgentMessage(
    message_id="msg-002",
    sender_id="network_worker",
    receiver_id="orchestrator",
    message_type=MessageType.TASK_RESULT,
    correlation_id="msg-001",
    content={
        "task_id": "task-001",
        "status": "completed",
        "findings": {
            "root_cause": "NetworkPolicy 阻断了 frontend → backend 的 8080 端口",
            "evidence": ["kubectl get networkpolicy 输出...", "连通性测试结果..."],
            "confidence": 0.95,
        },
        "recommendations": [
            "修改 NetworkPolicy 允许 frontend → backend:8080",
            "或添加 backend Pod 的 spec.selector 标签",
        ],
        "fix_yaml": "apiVersion: networking.k8s.io/v1\n...",
    },
)
```

## 5.2 Queue Integration

```python
import asyncio
from typing import Callable

class AgentMessageBus:
    """Agent messaging bus based on Redis Stream (production-level implementation)"""
    
    def __init__(self, redis_client):
        self.redis = redis_client
        self.stream_name = "agent_messages"
    
    async def publish(self, message: AgentMessage):
        """Publish a message to the messaging bus"""
        await self.redis.xadd(
            self.stream_name,
            {
                "message_id": message.message_id,
                "sender_id": message.sender_id,
                "receiver_id": message.receiver_id,
                "message_type": message.message_type.value,
                "content": json.dumps(message.content),
                "priority": str(message.priority),
            }
        )
    
    async def subscribe(
        self, 
        agent_id: str, 
        handler: Callable[[AgentMessage], None]
    ):
        """Subscribe to messages sent to a specific agent"""
        last_id = "0"  # 从头读取，生产环境应从断点恢复
        
        while True:
            messages = await self.redis.xread(
                {self.stream_name: last_id},
                count=10,
                block=1000  # 阻塞等待 1 秒
            )
            
            for stream, stream_messages in messages:
                for msg_id, fields in stream_messages:
                    last_id = msg_id
                    
                    # Filter messages belonging to this agent
                    if fields["receiver_id"] in [agent_id, "broadcast"]:
                        agent_msg = self._deserialize(fields)
                        await handler(agent_msg)
```

---

## 6. Conflict Resolution Strategies

When multiple agents arrive at different conclusions about the same issue:

```python
class ConflictResolver:
    """Conflict resolver for multiple agent conclusions"""
    
    def resolve(
        self,
        question: str,
        agent_responses: list[dict],
        resolution_strategy: str = "weighted_confidence"
    ) -> dict:
        """Resolver for multiple agents' conclusions"""
        
        if resolution_strategy == "voting":
            return self._majority_vote(agent_responses)
        
        elif resolution_strategy == "weighted_confidence":
            return self._weighted_confidence(agent_responses)
        
        elif resolution_strategy == "llm_arbitration":
            return self._llm_arbitrate(question, agent_responses)
        
        elif resolution_strategy == "human_escalation":
            return self._escalate_to_human(question, agent_responses)
    
    def _majority_vote(self, responses: list[dict]) -> dict:
        """Majority voting (suitable for categorical conclusions)"""
        from collections import Counter
        
        conclusions = [r["conclusion"] for r in responses]
        vote_counts = Counter(conclusions)
        winner = vote_counts.most_common(1)[0][0]
        
        return {
            "conclusion": winner,
            "method": "majority_vote",
            "vote_distribution": dict(vote_counts),
            "confidence": vote_counts[winner] / len(responses),
        }
    
    def _weighted_confidence(self, responses: list[dict]) -> dict:
        """Weighted confidence (suitable for confident conclusions)"""
        if not responses:
            return {"conclusion": "无法确定", "confidence": 0}
        
        # Sort by Confidence
        sorted_responses = sorted(
            responses, 
            key=lambda r: r.get("confidence", 0.5),
            reverse=True
        )
        
        best = sorted_responses[0]
        
        # If highest confidence < 0.7, and there's significant disagreement, escalate for handling
        if best.get("confidence", 0) < 0.7:
            return {
                "conclusion": best["conclusion"],
                "method": "weighted_confidence",
                "confidence": best.get("confidence", 0),
                "needs_review": True,
                "all_responses": responses,
            }
        
        return {
            "conclusion": best["conclusion"],
            "method": "weighted_confidence",
            "confidence": best.get("confidence", 0),
            "supporting_agents": [r["agent_id"] for r in sorted_responses 
                                  if r["conclusion"] == best["conclusion"]],
        }
    
    def _llm_arbitrate(self, question: str, responses: list[dict]) -> dict:
        """Serve as an arbitrator using LLM (suitable for complex technical judgments)"""
        arbitration_prompt = f"""
        多个专业 Agent 对以下问题产生了不同结论，请作为仲裁者给出最终判断：
        
        问题：{question}
        
        各 Agent 结论：
        {json.dumps(responses, ensure_ascii=False, indent=2)}
        
        请：
        1. 分析各方结论的优缺点
        2. 给出最终判断及理由
        3. 如果确实无法确定，说明需要补充什么信息
        """
        
        final_judgment = self.arbitrator_llm.invoke(arbitration_prompt).content
        
        return {
            "conclusion": final_judgment,
            "method": "llm_arbitration",
            "original_responses": responses,
        }
```

---

## 7. Production-grade Multi-Agent Platform Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                         API Gateway                               │
│                    (认证、限流、路由)                               │
└────────────────────────────┬─────────────────────────────────────┘
                              │
┌────────────────────────────▼─────────────────────────────────────┐
│                    Orchestration Layer                             │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────────────┐   │
│   │  Task Queue  │  │  Scheduler   │  │  State Manager        │   │
│   │  (Redis/Kafka│  │  (LangGraph) │  │  (Redis/PostgreSQL)  │   │
│   └──────────────┘  └──────────────┘  └──────────────────────┘   │
└────────────────────────────┬─────────────────────────────────────┘
                              │
┌────────────────────────────▼─────────────────────────────────────┐
│                       Agent Worker Pool                            │
│   ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌──────────┐   │
│   │ Network    │  │ Storage    │  │ Security   │  │  App     │   │
│   │ Agents     │  │ Agents     │  │ Agents     │  │  Agents  │   │
│   │ (K8s Pod)  │  │ (K8s Pod)  │  │ (K8s Pod)  │  │(K8s Pod) │   │
│   └────────────┘  └────────────┘  └────────────┘  └──────────┘   │
│         │               │               │               │         │
│   ┌─────▼───────────────▼───────────────▼───────────────▼──────┐ │
│   │              Shared Tool Registry (工具注册中心)              │ │
│   └───────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────────┘
                              │
┌─────────────────────────────▼────────────────────────────────────┐
│                      Observability Stack                           │
│      LangSmith / Langfuse + Prometheus + Grafana + 告警            │
└──────────────────────────────────────────────────────────────────┘
```

## 7.1 Kubernetes-based Multi-Agent Deployment

```yaml
# Agent Worker Deployment Template
apiVersion: apps/v1
kind: Deployment
metadata:
  name: k8s-network-agent
  namespace: ai-agents
  labels:
    agent-type: network-specialist
spec:
  replicas: 2  # 高可用
  selector:
    matchLabels:
      app: k8s-network-agent
  template:
    metadata:
      labels:
        app: k8s-network-agent
    spec:
      serviceAccountName: agent-readonly-sa  # 最小权限 SA
      containers:
      - name: agent
        image: kudig/network-agent:v1.2.0
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: llm-api-keys
              key: openai-key
        - name: AGENT_ID
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: MESSAGE_BUS_URL
          value: "redis://redis-master.ai-infra.svc:6379"
        - name: ORCHESTRATOR_URL
          value: "http://orchestrator-svc.ai-agents.svc:8080"
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
      
      # Optional: Use Sidecar for logging collection
      - name: log-shipper
        image: fluent/fluent-bit:latest
        # ...

---
# HPA: Auto-scale based on task queue length
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: network-agent-hpa
  namespace: ai-agents
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: k8s-network-agent
  minReplicas: 1
  maxReplicas: 10
  metrics:
  - type: External
    external:
      metric:
        name: redis_queue_length
        selector:
          matchLabels:
            queue: network_agent_tasks
      target:
        type: AverageValue
        averageValue: "5"  # 每个 Pod 处理 5 个任务时扩容
```

---

## 8. Best Practices and Anti-patterns

## Best Practices

- **Clearly Define Boundaries**: Each Agent's responsibilities should be clear-cut, avoiding cross-calling other Agents' tools
- **Asynchronous Communication**: Agents communicate via message queues rather than direct calls to improve decoupling and elasticity
- **Gradual Introduction**: Start with a single Agent and only refactor when multi-Agent value is confirmed
- **Use Expensive Models for Orchestrator**: Break down tasks and ensure quality control with GPT-4o/Claude, while execution uses cheaper models
- **Timeout Protection**: Set a maximum execution time for each Worker to prevent one from blocking the entire process

## Anti-patterns

- **Over-Division**: Splitting a 3-step task into 5 Agents results in higher communication costs than parallel benefits
- **Direct Calls Between Agents**: Point-to-point dependencies lead to strong coupling; use a message bus instead
- **Shared Mutable State**: Multiple Agents directly read and write the same data structure, introducing race conditions
- **No Centralized State Management**: Task states are scattered across different Agents, making it difficult to track overall progress and recover from issues
- **No Permission Boundaries**: All Agents share the same K8s ServiceAccount, and an attack on one Agent affects the entire system

---

## Related Documentation

| Document | Relevant Content |
|------|---------|
| [01 - Agent Basics](./01-ai-agent-fundamentals.md) | Relationship between Plan-and-Execute mode and Supervisor-Worker |
| [03 - Agent Framework Comparison](./03-agent-frameworks-comparison.md) | Implementation of LangGraph/AutoGen/CrewAI frameworks |
| [05 - Tool Usage](./05-tool-use-function-calling.md) | Sharing and Access Control among multiple Agents |
| [09 - Production Deployment](./09-production-deployment-guide.md) | Deployment architecture for multi-Agent platforms using K8s |
| [14 - Agent Enablement Design and Deployment Path](./14-agent-kudig-design-strategy.md) | Four directions for Kubernetes-based Agent operations |

---

*This document is original content from the kudig-database project's 02-ai-agents topic.*

---

## Obsidian-related Documentation

- 02-ai-agents KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|[[AI Agent Engineering Topic|AI Agent Engineering Topic]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|[[AI Agent Basics and Core Architecture|AI Agent Basics and Core Architecture]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|[[LLM Foundation Model Selection and Evaluation|LLM Foundation Model Selection and Evaluation]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Mainstream Agent Framework Deep Comparison]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|RAG Retrieval-Enhanced Generation Deep Guide]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Tool Use & Function Calling Design Guidelines]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation System and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]
- [[domain-14-ai-ml-infra/02-ai-agents/11-cost-latency-optimization.md|Cost and Latency Optimization Strategies]]

## See Also

- 04-rag-knowledge-retrieval
- 05-tool-use-function-calling
- 07-memory-context-management
- 08-agent-evaluation-observability


<!-- risk-assessed -->
