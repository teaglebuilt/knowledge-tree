---
title: Cloud Agent Platform as a Service
description: 'Comparison of mainstream cloud vendor Agent platforms: AWS Bedrock Agents, Azure AI Agent Service, Google Vertex AI Agent Builder, Alibaba Cloud BaiLian'
summary: 'Comparison of mainstream cloud vendor Agent platforms: AWS Bedrock Agents, Azure AI Agent Service, Google Vertex AI Agent Builder, Alibaba Cloud BaiLian'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- cloud
- paas
- bedrock
- vertex
- azure
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
- What is Cloud Agent Platform as a Service
- How to choose a Cloud Agent Platform
- How to use AWS Bedrock Agents
- Architecture of Azure AI Agent Service
- Comparison between Google Vertex AI Agent Builder and Alibaba Cloud BaiLian
trigger_keywords:
- cloud agent
- bedrock agents
- vertex ai agent
- azure ai agent
- How to use BaiLian
- agent paas
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/15-cloud-agent-platforms.md
---

> **Production Environment Security Tips**
>
> Commands included in this document are executable directly. Before executing, please confirm: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk levels for commands are annotated: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).


# Cloud Agent Platform as a Service

## Overview

Cloud Agent Platform (Agent PaaS) encapsulates the infrastructure required to build Agents—LLM calls, knowledge base retrieval, tool orchestration, session management—into managed services. Compared to building an Agent framework from scratch, the platform provides out-of-the-box orchestration capabilities, deep integration with the cloud ecosystem, and an elastic billing model based on usage.

This document covers four major platforms: AWS Bedrock Agents, Azure AI Agent Service, Google Vertex AI Agent Builder, and Alibaba Cloud Baolian Agent, and provides a selection framework.

## 1. AWS Bedrock Agents

### 1.1 Core Architecture

Bedrock Agents use a three-component model:

```
┌─────────────────────────────────────────────────┐
│                  Bedrock Agent                   │
│                                                  │
│  ┌──────────┐  ┌──────────────┐  ┌───────────┐ │
│  │ Foundation│  │  Knowledge   │  │  Action   │ │
│  │  Model    │  │   Bases      │  │  Groups   │ │
│  │ (Claude/  │  │ (OpenSearch/ │  │ (Lambda/  │ │
│  │  Titan/   │  │  S3/RDS)     │  │  Step Fn) │ │
│  │  Llama)   │  │              │  │           │ │
│  └──────────┘  └──────────────┘  └───────────┘ │
│                                                  │
│  ┌──────────────────────────────────────────┐   │
│  │         Agent Alias (version management)            │   │
│  └──────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

**Foundation Model**: The base model bound to the Agent, supporting models like Claude, Titan, and Llama hosted by Bedrock. Model selection is specified during Agent creation, and can be switched using an Alias.

**Knowledge Base**: Retrieval layer RAG, supports the following data sources:
- Amazon S3 (documents/PDFs/HTML/Markdown)
- Amazon OpenSearch Serverless (vector retrieval)
- Aurora PostgreSQL (pgvector)
- Kendra (enterprise search)

The Knowledge Base automatically handles document chunking, embedding generation (using Amazon Titan Embedding or Cohere Embeddings), and vector indexing. During retrieval, it automatically executes Hybrid Search (vector+keyword).

**Action Group**: The boundary of the Agent's capabilities, defining callable tools:
- **Lambda Action**: Calls AWS Lambda functions to execute operations (database writes, API calls, file operations, etc.)
- **Schema Definition**: Describes the inputs/outputs of the Action using OpenAPI 3.0 Schema
- **Return Control**: Returns the Action results back to the Agent for inference

### 1.2 Agent Alias and Version Management

```
Agent (DEV)
  ├── Alias: LIVE → Version 3
  ├── Alias: STAGING → Version 4 (draft)
  └── Version 1 (archived)
  └── Version 2 (archived)
  └── Version 3 (published)
```

Each Agent can create multiple Aliases, each pointing to a specific version. Versions include:
- Instructions
- Action Group definitions
- Knowledge Base configurations
- Basic Model Settings

Support Blue/Green deployment: After creating a new version, switching the Alias to point at it completes the traffic switch.

### 1.3 Session Management and Memory

Bedrock Agents maintain session state (Session State), supporting:
- **Session ID**: A unique identifier for each session
- **Session Attributes**: Key-value pairs passed across rounds (up to 3KB)
- **Prompt Session Attributes**: Temporary data visible only in the current inference step
- **Memory** (added in 2025): Long-term memory across sessions, configurable memory window

### 1.4 Enterprise Features

```yaml
安全:
  - IAM细粒度权限控制（Agent/Action/KB独立授权）
  - VPC端点支持（私有网络访问）
  - KMS加密（数据静态加密）
  - CloudTrail审计日志

可观测性:
  - CloudWatch Metrics（调用次数/Latency/Token消耗）
  - CloudWatch Logs（推理Trace/Action调用日志）
  - X-Ray分布式追踪

合规:
  - SOC 1/2/3
  - HIPAA
  - FedRAMP
  - ISO 27001
```

### 1.5 Pricing Model

```
Bedrock Agents Pricing (Q2 2026):
  - Agent Orchestration Fee: $0.003/call
  - LLM Call: based on model Token price (separate charge)
  - Knowledge Base Search: $0.0005/call
  - Lambda Execution: based on Lambda pricing (separate charge)
  - Storage: S3/OpenSearch at respective pricing

Example: 10,000 calls/day for Agent
  Agent Orchestration: 10000 × $0.003 = $30/day
  LLM (Claude Sonnet): ~$50/day (assuming 5K tokens/call)
  KB Search: 10000 × $0.0005 = $5/day
  Total: ~$85/day ≈ $2,550/month
```

## 2. Azure AI Agent Service

### 2.1 Integration with Azure AI Foundry and Architecture

Azure AI Agent Service integrates deeply with Azure AI Foundry (formerly Azure AI Studio), providing a unified Agent building experience:

```
┌─────────────────────────────────────────────────┐
│              Azure AI Foundry                    │
│                                                  │
│  ┌──────────────────────────────────────────┐   │
│  │           AI Agent Service                │   │
│  │  ┌────────┐ ┌────────┐ ┌──────────────┐ │   │
│  │  │ Model  │ │ Tools  │ │  Knowledge   │ │   │
│  │  │(GPT-4/ │ │(Func/  │ │  (AI Search/ │ │   │
│  │  │ Phi-3/ │ │ Code   │ │  Blob/ShareP)│ │   │
│  │  │ Llama) │ │ Interp)│ │              │ │   │
│  │  └────────┘ └────────┘ └──────────────┘ │   │
│  └──────────────────────────────────────────┘   │
│                                                  │
│  ┌──────────────────────────────────────────┐   │
│  │  Connected Agents (Multi-Agent orchestration)       │   │
│  └──────────────────────────────────────────┘   │
└─────────────────────────────────────────────────┘
```

**Core Components**:
- **Agent**: The runtime entity configured with models, commands, and tools
- **Thread**: Dialog thread maintaining message history and context
- **Run**: A single inference execution, including a loop of tool calls
- **Run Step**: Atomic steps in the inference process

### 2.2 Tool Types

```python
# Azure AI Agent Service Tool Type

# 1. Code Interpreter - Built-in Code Execution
agent = client.agents.create_agent(
    model="gpt-4o",
    name="data-analyst",
    instructions: "You are an analytics assistant",
    tools=[{"type": "code_interpreter"}]
)

# 2. File Search - RAG Retrieval
agent = client.agents.create_agent(
    tools=[{"type": "file_search"}],
    tool_resources={
        "file_search": {
            "vector_store_ids": ["vs_abc123"]
        }
    }
)

# 3. Function Calling - Custom Function
agent = client.agents.create_agent(
    tools=[{
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get weather",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"}
                }
            }
        }
    }]
)

# 4. Azure AI Search - Enterprise Search
# 5. Azure Functions - Serverless Execution
# 6. Bing Search - Internet Search
```

### 2.3 Connected Agents (Multi-Agent Orchestration)

Azure supports hierarchical calls between Agents:

```python
# Create Sub-Agent
billing_agent = client.agents.create_agent(
    model="gpt-4o-mini",
    name="billing-agent",
    instructions: "Handle bill inquiry",
)

# The Main Agent calls the Sub-Agent via Connected Agent
main_agent = client.agents.create_agent(
    model="gpt-4o",
    name="customer-service",
    instructions: "You are the customer service agent",
    tools=[{
        "type": "connected_agent",
        "connected_agent": {
            "name": "billing_agent",
            "id": billing_agent.id
        }
    }]
)
```

### 2.4 Enterprise Features

```
Integration with Azure ecosystem:
  - Entra ID (AAD) authentication
  - Azure RBAC role-based access control
  - Managed Identity zero-signing access to Azure resources
  - Private Endpoint private deployment
  - Azure Monitor full-chain monitoring
  - Microsoft Purview Data Governance
```

## 3. Google Vertex AI Agent Builder

### 3.1 Dual Mode Agent

Vertex AI Agent Builder provides two Agent building modes:

**Conversation Agent (Dialog Agent)**:
```
┌──────────────────────────────────────┐
│       Conversation Agent             │
│                                      │
│  ┌──────────┐  ┌────────────────┐   │
│  │ Gemini   │  │  Tools         │   │
│  │ Models   │  │  - Extensions  │   │
│  │          │  │  - Functions   │   │
│  │          │  │  - Data Stores │   │
│  └──────────┘  └────────────────┘   │
│                                      │
│  ┌──────────────────────────────┐   │
│  │  Playbooks (behavior orchestration)         │   │
│  └──────────────────────────────┘   │
└──────────────────────────────────────┘
```

**Search Agent (Search Agent)**:
- Built based on Vertex AI Search
- Enhanced enterprise knowledge base retrieval for generative tasks
- Supports structured/unstructured data sources
- automatically extract, chunk, and index

### 3.2 Extensions and Function Calling

```python
# Vertex AI Extension Example
from vertexai.preview import extensions

# Create Weather Query Extension
extension = extensions.Extension.create(
    display_name="weather-extension",
    description: "Query weather information",
    manifest={
        "name": "weather",
        "description": "Weather API",
        "api_spec": {
            "open_api_gcs_uri": "gs://bucket/weather_api.yaml"
        },
        "operation_config": {
            "allowed_operations": ["GET /weather"]
        }
    }
)

# Deploy to Agent
agent = agent_builder.create_agent(
    model="gemini-1.5-pro",
    tools=[
        {"extension": extension.resource_name}
    ]
)
```

### 3.3 Playbooks (Behavior Orchestration)

Playbook is an advanced orchestration primitive of Vertex AI Agent Builder, defining the behavior of the Agent in a specific scenario:

```yaml
# Playbook Definition Example
playbook:
  name: "customer-escalation"
  trigger:
    condition: "User expresses dissatisfaction or requests human customer service"
  steps:
    - id: detect_sentiment
      action: sentiment_analysis
    - id: check_urgency
      action: classify_urgency
      condition: "sentiment == negative"
    - id: escalate
      action: route_to_human
      condition: "urgency == high"
    - id: offer_solution
      action: suggest_alternative
      condition: "urgency != high"
```

### 3.4 Grounding (Knowledge Grounding)

```
Grounding options:
  1. Data Store Grounding
     - Vertex AI Search data storage
     - supports website, PDF, BigQuery, etc. data sources
     - automatically cites original sources

  2. Web Grounding
     - real-time internet search
     - based on Google Search
     - returns answers with citations

  3. Custom Grounding
     - custom search interface
     - integrates with enterprise systems
```

## 4. Alibaba Cloud Beacon Agent

### 4.1 Platform Architecture

Bailian is an Agent building platform of Alibaba Cloud, based on the Tongyi Qianwen series of models:

```
┌──────────────────────────────────────────────────┐
│                  Ant Cloud Hundred                    │
│                                                    │
│  ┌─────────────┐  ┌─────────────┐  ┌──────────┐ │
│  │  Model Service    │  │  Agent Orchestration   │  │  Knowledge Base   │ │
│  │  Tongyi Thousand Questions    │  │  Workflow Engine  │  │  Vector Retrieval │ │
│  │  Qwen-Max   │  │  Multi-Agent     │  │  Document Parsing │ │
│  │  Qwen-Plus  │  │  Dialogue Management    │  │  RAG     │ │
│  └─────────────┘  └─────────────┘  └──────────┘ │
│                                                    │
│  ┌──────────────────────────────────────────────┐│
│  │  Application Integration: DingTalk/WeChat/Flysky/Web/API             ││
│  └──────────────────────────────────────────────┘│
└──────────────────────────────────────────────────┘
```

### 4.2 Core Capabilities

```yaml
模型层:
  - 通义千问系列（Qwen-Max/Plus/Turbo）
  - 支持第三方模型接入（OpenAI兼容接口）
  - 模型微调平台

Agent编排:
  - 可视化工作流编辑器
  - 条件分支/循环/并行节点
  - 代码节点（Python/JavaScript）
  - 多Agent协作（主Agent+子Agent）

知识库:
  - 文档解析（PDF/Word/网页/图片OCR）
  - 向量检索（基于DashVector）
  - 多路召回（向量+关键词+重排序）
  - 引用溯源

应用发布:
  - API接入
  - 钉钉机器人
  - 微信公众号/小程序
  - 飞书机器人
  - Web Widget
```

### 4.3 Enterprise Features

```
Private deployment:
  - supports deployment to customer VPC
  - data stays within domain
  - Private model deployment (GPU cluster)

security compliance:
  - RAM access control
  - Data encryption (transmission+storage)
  - Operation audit (ActionTrail)
  - Content security review (Green Network)
```

## 5. Comparison Selection

### 5.1 Feature Comparison

| Dimension | AWS Bedrock Agents | Azure AI Agent Service | Vertex AI Agent Builder | Alibaba Cloud Bailian |
|------|-------------------|----------------------|------------------------|-----------|
| **model selection** | Claude/Titan/Llama/Mistral | GPT-4o/Phi-3/Llama | Gemini/Anthropic/OpenAI | Tongyi Qianwen series + third-party |
| **RAG solution** | Knowledge Base(OpenSearch/S3) | File Search + AI Search | Data Store + Web Grounding | DashVector knowledge base |
| **tool invocation** | Lambda + OpenAPI Schema | Function + Code Interpreter | Extension + Function | Workflow node + API |
| **multi-Agent** | Basic (requires self-built orchestration) | Connected Agents | Agent-to-Agent | Sub-Agent mode |
| **session management** | Session State + Memory | Thread + Run | Session + Context | Dialog variables |
| **visual editing** | Console basic configuration | AI Foundry Studio | Agent Builder Console | Visual workflow |
| **Chinese support** | Good (needs to select Chinese model) | Good | Poor | Native optimization |
| **private deployment** | Not supported | Not supported (only Private Link) | Not supported | Supported |

### 5.2 Pricing Comparison

```
# 🟢 Low Risk: Read-only/information gathering, typically with no side effects
price range (based on public information from Q2 2026):

AWS Bedrock Agents:
  orchestration fee: $0.003/call
  LLM: Claude Sonnet $3/$15 per 1M token (input/output)
  implicit cost: Lambda/S3/OpenSearch separately

Azure AI Agent Service:
  orchestration fee: included in API calls
  LLM: GPT-4o $2.50/$10 per 1M token
  implicit cost: AI Search/Azure Functions separately

Vertex AI Agent Builder:
  orchestration fee: $0.002/call (Conversation Agent)
  LLM: Gemini 1.5 Pro $1.25/$5 per 1M token
  implicit cost: AI Search/Cloud Functions separately

Zhongliangyun:
  orchestration fee: 0.003 yuan/call
  LLM: Qwen-Max 0.12 yuan/k token
  implicit cost: DashVector/OSS separately

Small scale (10K calls/day): each platform monthly fee $500-$3,000
Medium scale (100K calls/day): each platform monthly fee $5,000-$30,000
Large scale (1M calls/day): negotiation for enterprise discount
```
### 5.3 Vendor Lock-in Risk Assessment

```
# 🟢 Low Risk: Read-only/information gathering, typically with no side effects
Lock down dimension analysis:

┌─────────────┬──────────┬──────────┬──────────┬──────────┐
│ Dimension  │ AWS  │ Azure  │ GCP  │ Alibaba Cloud  │
├─────────────┼──────────┼──────────┼──────────┼──────────┤
│ Model migration │ Low  │ Medium  │ Low  │ High  │
│ API compatibility │ Own API │ OpenAI  │ Own API │ Own API │
│ Knowledge base migration │ Medium │ Medium  │ Medium │ High  │
│ Tool migration │ High(Lambda) │ Medium │ Medium │ High  │
│ Session format │ Own  │ Own  │ Own  │ Own  │
│ Comprehensive lock risk │ High  │ Medium  │ Medium │ High  │
└─────────────┴──────────┴──────────┴──────────┴──────────┘

Reduce lock strategy:
  1. Use OpenAI compatible interface layer (LiteLLM/OneAPI)
  2. Standardize tool definitions (OpenAPI 3.0)
  3. Independently store knowledge base data
  4. Decouple agent logic from platform APIs
```
### 5.4 Selection Decision Framework

```
Selection decision tree:

Q1: Has any cloud platform been deeply invested in?
    → AWS deep users → Prioritize Bedrock Agents
    → Azure deep users → Prioritize Azure AI Agent Service
    → GCP deep users → Prioritize Vertex AI Agent Builder
    → Alibaba Cloud deep users → Prioritize Qianlian

Q2: Is private deployment required?
    → Yes → Hundred Forge Enterprise Edition (only supported)
    → No → Continue evaluation

Q3: Chinese scenario proportion?
    > 80% → Forge > Bedrock > Azure > Vertex
    < 20% → Azure ≈ Bedrock > Vertex > Baolin

Q4: Multi-Agent orchestration complexity?
    High → Azure(Connected Agents most mature)
    Middle → Zhonglian (visual workflow)
    Low → All platforms can

Q5: Budget sensitivity?
    High → Vertex (best value)/ Bayon (domestic price advantage)
    Medium → Azure(quality of OpenAI models)
    Low → Bedrock(enterprise stability)
```

## 6. Mixed Architecture Practice

Production environments often cannot meet all needs with a single cloud platform. Hybrid architecture mode:

```yaml
Hybrid Mode 1: Multi-cloud Agent Gateway
  Description: Unified Agent gateway, backend routes to different cloud platforms
  Applicable: Need to leverage advantages of each platform
  Architecture:
    API Gateway → Agent Router
      → Bedrock (Claude for reasoning)
      → Vertex (Gemini for multimodal)
      → Hundred-Forging (Qwen for Chinese)

Hybrid Mode 2: Cloud Platform + Self-built Framework
  Description: Cloud platform handles infrastructure, self-built framework manages orchestration
  aplicable: appears only necessary now only not simple specialized scheduling syntax
  Architecture:
    Built-in Agent Framework (LangGraph/CrewAI)
      → Bedrock API (model invocation)
      → OpenSearch (knowledge base)
      → Lambda (tool execution)

Hybrid Mode 3: Gradual Migration
  Description: Migrating from one platform to another
  Phases:
    1. Dual Write: Running on both old and new platforms concurrently
    2. Shadow Traffic: Receiving replica traffic by the new platform
    3. Canary: Gradually switching traffic
    4. Full Switch: Dismantling the old platform
```

## 7. Integration with K8s

In typical modes of using cloud Agent platforms in K8s environments:

```yaml
# Run Agent Application in K8s and call cloud platform API
apiVersion: apps/v1
kind: Deployment
metadata:
  name: agent-app
spec:
  template:
    spec:
      containers:
      - name: agent
        image: agent-app:latest
        env:
        - name: CLOUD_PROVIDER
          value: "bedrock"  # 或 azure/vertex/bailian
        - name: AGENT_ID
          valueFrom:
            secretKeyRef:
              name: agent-config
              key: agent-id
        - name: API_KEY
          valueFrom:
            secretKeyRef:
              name: agent-config
              key: api-key
        resources:
          requests:
            cpu: "500m"
            memory: "512Mi"
          limits:
            cpu: "2"
            memory: "2Gi"
---
# Multi-platform Route Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: agent-router-config
data:
  routing.yaml: |
    routes:
      - match:
          intent: "reasoning"
        target: bedrock
        model: claude-sonnet
      - match:
          intent: "multimodal"
        target: vertex
        model: gemini-1.5-pro
      - match:
          intent: "chinese"
        target: bailian
        model: qwen-max
```

## Related Topics

- [[domain-14-ai-ml-infra/03-agent-runtime/16-coze-agent-platform|Coze Agent platform]]
- [[domain-14-ai-ml-infra/03-agent-runtime/17-agent-rate-limiting-cost-control|Agent limitation and cost control]]
- [[domain-14-ai-ml-infra/03-agent-runtime/21-agent-runtime-architecture-overview|Agent Runtime architecture overview]]

## References

- AWS Bedrock Agents Documentation
- Azure AI Agent Service Documentation
- Vertex AI Agent Builder Documentation
- Aliyun Bailian product documentation


<!-- risk-assessed -->
