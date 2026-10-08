---
title: Agent Runtime Architecture Overview
description: 'Agent Runtime layered architecture, component relationships, data flow, deployment topology, and K8s ecosystem integration'
summary: 'Agent Runtime layered architecture, component relationships, data flow, deployment topology, and K8s ecosystem integration'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- architecture
- overview
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
- What is the Agent Runtime Architecture Overview
- Agent Runtime architecture design
- Agent system layered architecture
- Agent deployment topology
trigger_keywords:
- agent runtime
- architecture
- deployment topology
- data flow
- k8s integration
prerequisites:
- llm-basics
- kubernetes-basics
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/21-agent-runtime-architecture-overview.md
---
# Agent Runtime Architecture Overview

## Overview

Agent Runtime is the infrastructure layer that hosts the runtime behavior of AI Agents. It encapsulates capabilities such as LLM inference, tool invocation, session management, security controls, and observability into a unified runtime engine, allowing Agent developers to focus on business logic rather than infrastructure.

This document provides a comprehensive review of the Agent Runtime architecture design from five dimensions: layered architecture, component relationships, data flow, deployment topology, and Kubernetes ecosystem integration.

## 1. Layered Architecture

### 1.1 Four-Layer Architecture Model

```
┌─────────────────────────────────────────────────────────────┐
│                    Layer 4: Application                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌───────────────┐ │
│  │Customer  │ │  Code    │ │  Data    │ │ Custom Agent  │ │
│  │Service   │ │Assistant │ │Analytics │ │               │ │
│  └──────────┘ └──────────┘ └──────────┘ └───────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                    Layer 3: Agent Framework                   │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌───────────────┐ │
│  │ LangGraph│ │ CrewAI   │ │ AutoGen  │ │ In-house      │ │
│  │          │ │          │ │          │ │ Framework     │ │
│  └──────────┘ └──────────┘ └──────────┘ └───────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                    Layer 2: Runtime Engine                    │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌───────────────┐ │
│  │Inference │ │  Tool    │ │ Session  │ │ Security &    │ │
│  │ Engine   │ │ Engine   │ │ Manager  │ │ Rate Limiting │ │
│  └──────────┘ └──────────┘ └──────────┘ └───────────────┘ │
├─────────────────────────────────────────────────────────────┤
│                    Layer 1: Infrastructure                    │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌───────────────┐ │
│  │LLM API   │ │  Vector  │ │ Message  │ │ K8s / Cloud   │ │
│  │(OpenAI/  │ │    DB    │ │  Queue   │ │ (EKS/GKE/AKS) │ │
│  │ Anthropic)│ │(Milvus/ │ │(Kafka/  │ │               │ │
│  │          │ │ Qdrant)  │ │ Redis)   │ │               │ │
│  └──────────┘ └──────────┘ └──────────┘ └───────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Responsibilities of Each Layer

```yaml
Layer 4 - Application:
  Responsibilities: Agent implementations oriented toward business scenarios
  Components:
    - Business Agents (customer service / code / data / custom)
    - Agent configuration (Prompt / tool / knowledge base bindings)
    - Publishing channels (Web / API / IM integration)
  Characteristics:
    - Maintained by business teams
    - Agent behavior defined via configuration or code
    - No direct contact with infrastructure

Layer 3 - Agent Framework:
  Responsibilities: Abstraction and implementation of Agent orchestration logic
  Components:
    - Orchestration engine (ReAct / Plan-Execute / Multi-Agent)
    - Tool registration and discovery
    - Memory management (short-term / long-term / working memory)
    - Prompt template management
  Characteristics:
    - Provides Agent development SDK
    - Shields developers from underlying Runtime complexity
    - Pluggable orchestration strategies

Layer 2 - Runtime Engine:
  Responsibilities: Core engine for Agent execution
  Components:
    - Inference engine (LLM invocation / retry / fallback)
    - Tool engine (tool execution / sandbox / timeout)
    - Session management (state / context / memory)
    - Security controls (rate limiting / budget / content filtering)
    - Observability (Trace / Metrics / Log)
  Characteristics:
    - High performance, high availability
    - Multi-tenant support
    - Elasticity and fault tolerance

Layer 1 - Infrastructure:
  Responsibilities: Underlying resource provisioning
  Components:
    - LLM API (model inference service)
    - Vector database (Embedding retrieval)
    - Object storage (file / knowledge base storage)
    - Message queue (asynchronous processing)
    - K8s (container orchestration)
    - Observability infrastructure (Prometheus / Jaeger / Loki)
  Characteristics:
    - Replaceable (multi-cloud / hybrid cloud)
    - Horizontal scaling
    - Infrastructure as code
```

## 2. Component Relationships

### 2.1 Core Component Interaction Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                        Agent Runtime                             │
│                                                                  │
│  ┌─────────────┐    ┌──────────────┐    ┌──────────────────┐   │
│  │   API       │    │   Agent      │    │   Session        │   │
│  │   Gateway   │───→│   Router     │───→│   Manager        │   │
│  │             │    │              │    │                  │   │
│  │ Auth/Rate   │    │ Intent       │    │ State/Context    │   │
│  │ Limit       │    │ Classify     │    │ Memory           │   │
│  └─────────────┘    └──────┬───────┘    └────────┬─────────┘   │
│                            │                      │              │
│                            ▼                      ▼              │
│                    ┌───────────────────────────────────┐        │
│                    │        Inference Engine            │        │
│                    │                                   │        │
│                    │  ┌──────────┐  ┌──────────────┐  │        │
│                    │  │ Prompt   │  │  LLM Client  │  │        │
│                    │  │ Compiler │──│  (Multi-model)│  │        │
│                    │  │          │  │  Retry/Fallback│ │        │
│                    │  └──────────┘  └──────────────┘  │        │
│                    └───────────────┬───────────────────┘        │
│                                    │                             │
│                                    ▼                             │
│                    ┌───────────────────────────────────┐        │
│                    │        Tool Engine                 │        │
│                    │                                   │        │
│                    │  ┌──────────┐  ┌──────────────┐  │        │
│                    │  │ Tool     │  │  Execution   │  │        │
│                    │  │ Registry │──│  Sandbox     │  │        │
│                    │  │          │  │  (K8s Pod/   │  │        │
│                    │  │          │  │   Container) │  │        │
│                    │  └──────────┘  └──────────────┘  │        │
│                    └───────────────────────────────────┘        │
│                                                                  │
│  ┌─────────────┐    ┌──────────────┐    ┌──────────────────┐   │
│  │ Knowledge   │    │   Cost &     │    │   Observability  │   │
│  │ Base        │    │   Quota      │    │                  │   │
│  │             │    │   Manager    │    │ Trace/Metrics/   │   │
│  │ RAG/Search  │    │              │    │ Log              │   │
│  └─────────────┘    └──────────────┘    └──────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Component Responsibilities and Interfaces

```python
from abc import ABC, abstractmethod

# API Gateway
class APIGateway(ABC):
    """API Gateway: authentication, rate limiting, routing"""

    @abstractmethod
    async def handle_request(self, request) -> dict:
        """Handle inbound requests"""
        pass

    @abstractmethod
    async def authenticate(self, api_key: str) -> dict:
        """Authenticate and return tenant information"""
        pass

    @abstractmethod
    async def rate_limit(self, tenant_id: str) -> bool:
        """Rate limit check"""
        pass

# Agent Router
class AgentRouter(ABC):
    """Agent Router: intent recognition and Agent dispatching"""

    @abstractmethod
    async def route(self, message: str, context: dict) -> str:
        """Route to the target Agent"""
        pass

# Inference Engine
class InferenceEngine(ABC):
    """Inference Engine: LLM invocation management"""

    @abstractmethod
    async def infer(self, messages: list, config: dict) -> dict:
        """Execute inference"""
        pass

    @abstractmethod
    async def infer_stream(self, messages: list, config: dict):
        """Streaming inference"""
        pass

# Tool Engine
class ToolEngine(ABC):
    """Tool Engine: tool registration, invocation, and sandbox execution"""

    @abstractmethod
    async def execute(self, tool_name: str, params: dict, context: dict) -> dict:
        """Execute a tool call"""
        pass

    @abstractmethod
    def register(self, tool_def: dict):
        """Register a tool"""
        pass

# Session Manager
class SessionManager(ABC):
    """Session Manager: state, context, and memory"""

    @abstractmethod
    async def get_context(self, session_id: str) -> dict:
        """Retrieve session context"""
        pass

    @abstractmethod
    async def update_context(self, session_id: str, updates: dict):
        """Update session context"""
        pass

# Knowledge Base
class KnowledgeBase(ABC):
    """Knowledge Base: RAG retrieval"""

    @abstractmethod
    async def search(self, query: str, tenant_id: str, top_k: int) -> list:
        """Semantic retrieval"""
        pass
```
## 3. Data Flow

### 3.1 Complete Request Processing Flow

```
User Input
  │
  ▼
┌──────────────────────────────────────────────────────────────────┐
│  Step 1: API Gateway                                             │
│  - Auth: Validate API Key → Get Tenant ID                        │
│  - Rate Limiting: Check tenant/user/Agent-level rate limits      │
│  - Budget: Check daily/monthly Token budget                      │
│  - Routing: Parse request, determine target Agent                │
└──────────────┬───────────────────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────────────────┐
│  Step 2: Session Manager                                         │
│  - Load Session: Retrieve historical messages, context variables │
│  - Window Trimming: Summarize and compress history beyond window │
│  - Memory Injection: Load user long-term memory                  │
└──────────────┬───────────────────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────────────────┐
│  Step 3: Prompt Compiler                                         │
│  - Assemble Prompt: System + Context + History + User Input      │
│  - Tool Injection: Inject available tool schemas into Prompt     │
│  - Knowledge Injection: Inject RAG retrieval results into context│
└──────────────┬───────────────────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────────────────┐
│  Step 4: Inference Engine                                        │
│  - Model Routing: Select model based on complexity/budget        │
│  - LLM Call: Send inference request                              │
│  - Response Parsing: Parse tool calls or final answer            │
│  - Resilience: Timeout/retry/fallback                            │
└──────────────┬───────────────────────────────────────────────────┘
               │
               ├──→ No tool call → Step 7 (Output)
               │
               ▼
┌──────────────────────────────────────────────────────────────────┐
│  Step 5: Tool Engine (Loop)                                      │
│  - Tool Selection: Parse tool calls returned by LLM              │
│  - Permission Check: Verify tenant has permission for the tool   │
│  - Idempotency Check: Check if already executed (deduplication)  │
│  - Sandbox Execution: Execute tool in isolated environment       │
│  - Result Return: Inject tool results into conversation          │
│  - Loop Decision: Determine whether further inference is needed  │
└──────────────┬───────────────────────────────────────────────────┘
               │
               │ Loop back to Step 4 (until no tool call or max steps reached)
               │
               ▼
┌──────────────────────────────────────────────────────────────────┐
│  Step 6: Safety & Post-processing                                │
│  - Content Filtering: Check output for policy violations         │
│  - Citation Annotation: Annotate knowledge base citation sources │
│  - Formatting: Format output by channel (Markdown/plain text/card)│
└──────────────┬───────────────────────────────────────────────────┘
               │
               ▼
┌──────────────────────────────────────────────────────────────────┐
│  Step 7: Response & Async                                        │
│  - Synchronous Return: Return result to user                     │
│  - Async Recording: Log audit trail, update usage, update session│
│  - Observability: Send Trace/Metrics to monitoring system        │
└──────────────────────────────────────────────────────────────────┘
```

### 3.2 Streaming Data Flow

```
Streaming Data Flow:

Client ←── SSE/WebSocket ──→ API Gateway ←── gRPC Stream ──→ Runtime

Token Stream:
  LLM API ──stream──→ Inference Engine ──chunk──→ API Gateway ──SSE──→ Client

  Each chunk contains:
  {
    "id": "chatcmpl-xxx",
    "object": "chat.completion.chunk",
    "choices": [{
      "index": 0,
      "delta": {
        "content": "Hello",  // or tool_calls delta
      },
      "finish_reason": null  // or "stop"/"tool_calls"
    }]
  }

Tool call intermediate states:
  {"type": "tool_start", "tool": "search", "params": {...}}
  {"type": "tool_result", "tool": "search", "result": "..."}
  {"type": "thinking", "content": "Analyzing search results..."}
```

## 4. Deployment Topology

### 4.1 Single-Node Deployment

Suitable for development/test environments:

```
┌──────────────────────────────────────┐
│         Single Node                   │
│                                      │
│  ┌─────────────────────────────────┐│
│  │        Agent Runtime Pod        ││
│  │  ┌────────┐  ┌──────────────┐  ││
│  │  │ API    │  │  Inference   │  ││
│  │  │ Server │  │  Engine      │  ││
│  │  └────────┘  └──────────────┘  ││
│  │  ┌────────┐  ┌──────────────┐  ││
│  │  │ Tool   │  │  Session     │  ││
│  │  │ Engine │  │  Store       │  ││
│  │  └────────┘  └──────────────┘  ││
│  └─────────────────────────────────┘│
│                                      │
│  ┌────────┐  ┌────────┐  ┌───────┐ │
│  │ SQLite │  │ Redis  │  │ File  │ │
│  │ (Data) │  │(Cache) │  │Storage│ │
│  └────────┘  └────────┘  └───────┘ │
└──────────────────────────────────────┘

Resource Requirements:
  CPU: 2-4 cores
  Memory: 4-8 Gi
  Storage: 50 Gi
  Use case: Development/Testing/PoC
```

### 4.2 Distributed Deployment

Suitable for production environments:

```
┌─────────────────────────────────────────────────────────────────┐
│                      K8s Cluster (Production)                    │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Ingress Controller (Nginx/Istio)                         │   │
│  └──────────────────────────┬───────────────────────────────┘   │
│                              │                                   │
│  ┌───────────────────────────┼───────────────────────────────┐  │
│  │  ns: agent-platform                                       │  │
│  │                           │                                │  │
│  │  ┌─────────────┐  ┌──────┴──────┐  ┌──────────────────┐ │  │
│  │  │ API Gateway │  │ Agent Router│  │ Auth Service     │ │  │
│  │  │ (3 replicas)│  │ (2 replicas)│  │ (2 replicas)     │ │  │
│  │  └─────────────┘  └─────────────┘  └──────────────────┘ │  │
│  │                                                           │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌──────────────────┐ │  │
│  │  │ Inference   │  │ Tool Engine │  │ Session Manager  │ │  │
│  │  │ Engine      │  │ (5 replicas)│  │ (3 replicas)     │ │  │
│  │  │ (10 replicas)│ │             │  │                  │ │  │
│  │  └─────────────┘  └─────────────┘  └──────────────────┘ │  │
│  │                                                           │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌──────────────────┐ │  │
│  │  │ LLM Proxy   │  │ Cost        │  │ Audit Logger     │ │  │
│  │  │ (3 replicas)│  │ Controller  │  │ (2 replicas)     │ │  │
│  │  └─────────────┘  │ (2 replicas)│  └──────────────────┘ │  │
│  │                    └─────────────┘                       │  │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  ns: data-services                                        │   │
│  │                                                           │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌──────────────────┐ │   │
│  │  │ PostgreSQL  │  │ Redis       │  │ Milvus/Qdrant    │ │   │
│  │  │ (HA Cluster)│  │ (Sentinel)  │  │ (Vector DB)      │ │   │
│  │  └─────────────┘  └─────────────┘  └──────────────────┘ │   │
│  │                                                           │   │
│  │  ┌─────────────┐  ┌─────────────┐                        │   │
│  │  │ Kafka       │  │ MinIO/S3    │                        │   │
│  │  │ (3 brokers) │  │ (Object)    │                        │   │
│  │  └─────────────┘  └─────────────┘                        │   │
│  └──────────────────────────────────────────────────────────┘   │
│                                                                  │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  ns: observability                                        │   │
│  │                                                           │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌──────────────────┐ │   │
│  │  │ Prometheus  │  │ Jaeger      │  │ Grafana          │ │   │
│  │  │ (Metrics)   │  │ (Tracing)   │  │ (Dashboard)      │ │   │
│  │  └─────────────┘  └─────────────┘  └──────────────────┘ │   │
│  │                                                           │   │
│  │  ┌─────────────┐  ┌─────────────┐                        │   │
│  │  │ Loki        │  │ Alert       │                        │   │
│  │  │ (Logs)      │  │ Manager     │                        │   │
│  │  └─────────────┘  └─────────────┘                        │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

### 4.3 Edge Deployment

Suitable for low-latency/offline scenarios:

```
┌─────────────────────────────────────────────────┐
│              Edge Node                            │
│                                                  │
│  ┌─────────────────────────────────────────────┐│
│  │         Lightweight Agent Runtime            ││
│  │                                              ││
│  │  ┌──────────┐  ┌──────────┐  ┌───────────┐ ││
│  │  │ API      │  │ Local    │  │ Edge      │ ││
│  │  │ Server   │  │ LLM      │  │ Cache     │ ││
│  │  │          │  │ (Ollama/ │  │           │ ││
│  │  │          │  │  vLLM)   │  │           │ ││
│  │  └──────────┘  └──────────┘  └───────────┘ ││
│  └─────────────────────────────────────────────┘│
│                                                  │
│  ┌─────────────────────────────────────────────┐│
│  │  Cloud Sync (periodic sync to cloud)         ││
│  │  - Session data upload                       ││
│  │  - Model weight updates                      ││
│  │  - Knowledge base incremental sync           ││
│  └─────────────────────────────────────────────┘│
└─────────────────────────────────────────────────┘

Resource Requirements:
  CPU: 4-8 cores (ARM/x86)
  Memory: 8-16 Gi
  GPU: Optional (7B model)
  Use case: IoT/Factory/Retail/Offline scenarios
```
## 5. Integration with the K8s Ecosystem

### 5.1 Integration Points Overview

```yaml
K8s Ecosystem Integration:

Service Mesh (Istio/Linkerd):
  - mTLS encryption for Agent services
  - Traffic management (canary/blue-green)
  - Fault injection (Chaos Testing)
  - Rate limiting (EnvoyFilter)

Observability:
  - Prometheus: Agent metrics collection (request volume/latency/token consumption/cost)
  - Jaeger/OpenTelemetry: Distributed tracing (Agent reasoning chain)
  - Loki: Log aggregation (conversation logs/tool call logs)
  - Grafana: Visualization Dashboard

Storage:
  - PVC: Session persistence/knowledge base storage
  - CSI: Cloud storage integration (S3/GCS/OSS)
  - StatefulSet: Stateful services (vector database/Redis)

Security:
  - RBAC: Agent service account permission control
  - NetworkPolicy: Tenant network isolation
  - Secret: API Key/model credential management
  - OPA/Gatekeeper: Policy enforcement

Auto-scaling:
  - HPA: Horizontal scaling based on CPU/memory/request volume
  - KEDA: Event-driven scaling based on queue depth
  - VPA: Vertical scaling (resource request adjustment)

Scheduling:
  - NodeAffinity: GPU node scheduling
  - PodAntiAffinity: High-availability replica distribution
  - PriorityClass: Agent task priority
  - ResourceQuota: Tenant resource quota
```

### 5.2 Integration Configuration Examples

```yaml
# HPA - Agent auto-scaling
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: agent-runtime-hpa
  namespace: agent-platform
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: agent-runtime
  minReplicas: 3
  maxReplicas: 50
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
  - type: Pods
    pods:
      metric:
        name: agent_requests_per_second
      target:
        type: AverageValue
        averageValue: "100"
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
      - type: Pods
        value: 5
        periodSeconds: 60
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Pods
        value: 2
        periodSeconds: 120
---
# KEDA - scaling based on queue depth
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: agent-worker-scaler
spec:
  scaleTargetRef:
    name: agent-worker
  minReplicaCount: 1
  maxReplicaCount: 20
  triggers:
  - type: kafka
    metadata:
      bootstrapServers: kafka:9092
      consumerGroup: agent-workers
      topic: agent-tasks
      lagThreshold: "100"
---
# PodDisruptionBudget - high availability guarantee
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  name: agent-runtime-pdb
spec:
  minAvailable: 2
  selector:
    matchLabels:
      app: agent-runtime
---
# PriorityClass - Agent task priority
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass
metadata:
  name: agent-high-priority
value: 1000000
globalDefault: false
description: "High-priority Agent tasks"
```

### 5.3 ServiceMonitor Configuration

```yaml
# Prometheus ServiceMonitor
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: agent-runtime-metrics
  namespace: agent-platform
spec:
  selector:
    matchLabels:
      app: agent-runtime
  endpoints:
  - port: metrics
    interval: 15s
    path: /metrics
    metricRelabelings:
    - sourceLabels: [__name__]
      regex: 'agent_.*'
      action: keep
---
# Grafana Dashboard ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: agent-dashboard
  namespace: monitoring
  labels:
    grafana_dashboard: "1"
data:
  agent-runtime.json: |
    {
      "dashboard": {
        "title": "Agent Runtime Dashboard",
        "panels": [
          {
            "title": "Agent Requests/sec",
            "type": "graph",
            "targets": [{"expr": "rate(agent_requests_total[5m])"}]
          },
          {
            "title": "LLM Latency P99",
            "type": "graph",
            "targets": [{"expr": "histogram_quantile(0.99, agent_llm_latency_bucket)"}]
          },
          {
            "title": "Token Usage (Daily)",
            "type": "stat",
            "targets": [{"expr": "sum(agent_tokens_used_today)"}]
          },
          {
            "title": "Cost (Daily USD)",
            "type": "stat",
            "targets": [{"expr": "sum(agent_cost_usd_today)"}]
          },
          {
            "title": "Error Rate",
            "type": "graph",
            "targets": [{"expr": "rate(agent_errors_total[5m]) / rate(agent_requests_total[5m])"}]
          },
          {
            "title": "Active Sessions",
            "type": "stat",
            "targets": [{"expr": "agent_active_sessions"}]
          }
        ]
      }
    }
```
## 6. Document Index for This Series

```
domain-14-ai-ml-infra/03-agent-runtime/
  ├── 15-cloud-agent-platforms.md        # Cloud Agent Platform as a Service
  ├── 16-coze-agent-platform.md          # Coze Agent Platform
  ├── 17-agent-rate-limiting-cost-control.md  # Agent Rate Limiting and Cost Control
  ├── 18-agent-retry-resilience.md       # Agent Resilience Design
  ├── 19-agent-ci-cd-pipeline.md         # Agent CI/CD Pipeline
  ├── 20-agent-multi-tenancy.md          # Agent Multi-Tenancy Architecture
  └── 21-agent-runtime-architecture-overview.md  # This article: Architecture Overview
```

## Related Topics

- [[domain-14-ai-ml-infra/03-agent-runtime/15-cloud-agent-platforms|Cloud Agent Platform as a Service]]
- [[domain-14-ai-ml-infra/03-agent-runtime/17-agent-rate-limiting-cost-control|Agent Rate Limiting and Cost Control]]
- [[domain-14-ai-ml-infra/03-agent-runtime/20-agent-multi-tenancy|Agent Multi-Tenancy Architecture]]

## References

- LangChain/LangGraph Architecture
- Kubernetes Production Best Practices
- Istio Service Mesh
- OpenTelemetry for LLM Observability
