---
title: Dify Agent Platform In-Depth Guide
description: 'Comprehensive analysis of the Dify platform architecture, covering the four-layer architecture of API/Worker/Plugin/Proxy, Workflow orchestration, Agent strategies, knowledge base management, and K8s Helm deployment'
summary: 'Comprehensive analysis of the Dify platform architecture'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- dify
- workflow
- low-code
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
- What is the Dify Agent Platform
- How to use the Dify Agent Platform
- Dify Workflow orchestration
trigger_keywords:
- dify
- workflow
- chatflow
- knowledge-base
- plugin
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/05-dify-agent-platform.md
---
> **Production Environment Safety Notice**
>
> This document contains operational commands that can be executed directly. Before executing, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have verified in a non-production environment. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (will modify cluster state, but usually reversible), 🟢 Low Risk/Read-Only (information gathering, no side effects).


# Dify Agent Platform In-Depth Guide

## 1. Platform Architecture

### 1.1 Overall Architecture

Dify is an open-source LLM application development platform that provides visual Agent and Workflow building capabilities:

```
┌─────────────────────────────────────────────────────────────┐
│                      Dify Architecture                       │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐ │
│  │ Web UI   │  │ REST API │  │ Plugin   │  │ Model Proxy  │ │
│  │ (Next.js)│  │ (Flask)  │  │ Service  │  │              │ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └──────┬───────┘ │
│       │              │             │               │         │
│  ┌────┴──────────────┴─────────────┴───────────────┴──────┐  │
│  │                    API Gateway                          │  │
│  └────┬──────────────┬─────────────┬───────────────┬──────┘  │
│       │              │             │               │         │
│  ┌────┴───┐    ┌─────┴────┐  ┌────┴─────┐  ┌─────┴──────┐  │
│  │ App    │    │ Workflow │  │ Knowledge│  │ Model      │  │
│  │ Engine │    │ Engine   │  │ Base     │  │ Service    │  │
│  └────────┘    └──────────┘  └──────────┘  └────────────┘  │
│                                                              │
│  ┌──────────────────────────────────────────────────────┐    │
│  │              Storage Layer                            │    │
│  │  ┌────────┐  ┌──────────┐  ┌─────────┐  ┌─────────┐  │    │
│  │  │Postgres│  │  Redis   │  │ Weaviate│  │  S3     │  │    │
│  │  └────────┘  └──────────┘  └─────────┘  └─────────┘  │    │
│  └──────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Core Services

| Service | Responsibility | Tech Stack |
|------|------|--------|
| API Server | REST API + Business Logic | Python / Flask |
| Web Frontend | Visual Console | Next.js / React |
| Worker | Asynchronous Task Processing | Celery / Redis |
| Plugin Service | Plugin Loading and Management | Python |
| Model Proxy | LLM Call Proxy | Python / Multi-vendor Adaptation |

### 1.3 Data Storage

| Storage | Purpose |
|------|------|
| PostgreSQL | Application configuration, user data, conversation records |
| Redis | Cache, session state, Celery Broker |
| Weaviate / Qdrant | Vector storage (knowledge base) |
| S3 / MinIO | File storage (uploaded documents) |

---

## 2. Workflow Orchestration

### 2.1 Application Types

Dify provides two core application types:

**Chatflow (Conversational Flow):**
- Designed for multi-turn conversation scenarios
- Automatically manages session state
- Supports context memory

**Workflow:**
- Designed for automated tasks
- Stateless, one-time processing
- Suitable for batch processing and data pipelines

### 2.2 Node Types

```yaml
# Dify Workflow node types
nodes:
  # Start node
  - type: start
    config:
      variables:
        - name: namespace
          type: string
          required: true
        - name: pod_name
          type: string
          required: true

  # LLM node
  - type: llm
    config:
      model: gpt-4o
      prompt: |
        You are a K8s diagnostics expert.
        Pod {{pod_name}} in namespace {{namespace}} has encountered an anomaly.
        Please analyze the possible causes.
      temperature: 0

  # Knowledge retrieval node
  - type: knowledge_retrieval
    config:
      knowledge_base: k8s_docs
      query: "{{start.output}}"
      top_k: 5

  # Code execution node
  - type: code
    config:
      language: python
      code: |
        import subprocess
        result = subprocess.run(
            ["kubectl", "get", "pod", pod_name, "-n", namespace, "-o", "json"],
            capture_output=True, text=True
        )
        return {"pod_status": result.stdout}

  # Conditional branch node
  - type: if_else
    config:
      conditions:
        - variable: "{{code.pod_status}}"
          operator: "contains"
          value: "CrashLoopBackOff"
          then: llm_diagnosis
          else: end_success

  # HTTP request node
  - type: http_request
    config:
      method: GET
      url: "http://prometheus:9090/api/v1/query"
      params:
        query: 'container_memory_usage_bytes{pod="{{pod_name}}"}'

  # Variable aggregator node
  - type: variable_aggregator
    config:
      variables:
        - "{{llm.output}}"
        - "{{knowledge.output}}"
        - "{{http.output}}"

  # End node
  - type: end
    config:
      output: "{{variable_aggregator.output}}"
```

### 2.3 Workflow Example: K8s Automatic Diagnosis

```python
# Create and run a Workflow via API
import requests

API_BASE = "http://dify-api/v1"
API_KEY = "app-xxxxx"

# Run Workflow
response = requests.post(
    f"{API_BASE}/workflows/run",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "inputs": {
            "namespace": "default",
            "pod_name": "nginx-abc123",
        },
        "response_mode": "streaming",  # blocking / streaming
        "user": "operator-001",
    },
)

# Process results as stream
for line in response.iter_lines():
    if line:
        event = json.loads(line.decode())
        if event["event"] == "node_started":
            print(f"[Node Started] {event['data']['node_id']}")
        elif event["event"] == "node_finished":
            print(f"[Node Finished] {event['data']['node_id']}")
            print(f"  Output: {event['data'].get('outputs', {})}")
        elif event["event"] == "workflow_finished":
            print(f"[Workflow Finished] Status: {event['data']['status']}")
            print(f"  Final Output: {event['data']['outputs']}")
```

---

## 3. Agent Strategies

### 3.1 ReAct Strategy

```yaml
# Agent configuration (ReAct mode)
agent:
  strategy: react
  model: gpt-4o
  max_iterations: 10
  tools:
    - name: kubectl_query
      description: "Query K8s cluster resource status"
      parameters:
        namespace:
          type: string
          description: "Namespace"
          default: default
        resource:
          type: string
          description: "Resource type"
      api_endpoint: "http://kubectl-proxy/get"

    - name: log_search
      description: "Search Pod logs for errors"
      parameters:
        pod_name:
          type: string
        keyword:
          type: string
      api_endpoint: "http://log-service/search"

  system_prompt: |
    You are a KuDig K8s operations expert.
    Use tools to query cluster status and analyze the root cause of issues.
    Call only one tool at a time, wait for the result before deciding the next step.
```

### 3.2 Function Calling Strategy

```yaml
# Function Calling mode
agent:
  strategy: function_calling
  model: gpt-4o
  tools:
    - name: get_pod_status
      description: "Get Pod status"
      parameters:
        type: object
        properties:
          namespace:
            type: string
          pod_name:
            type: string
        required: [namespace]
      # Directly mapped to OpenAI Function Schema
```

### 3.3 Tool Integration Methods

Dify provides three tool integration methods:

```python
# 1. Built-in tools (officially provided by Dify)
builtin_tools = [
    "web_search",       # Web search
    "calculator",       # Calculator
    "wikipedia",        # Wikipedia query
    "code_interpreter", # Code interpreter
]

# 2. API tools (imported via OpenAPI Schema)
api_tool_schema = {
    "openapi": "3.0.0",
    "info": {"title": "K8s API", "version": "1.0"},
    "paths": {
        "/api/v1/pods": {
            "get": {
                "operationId": "listPods",
                "summary": "List Pods",
                "parameters": [
                    {
                        "name": "namespace",
                        "in": "query",
                        "schema": {"type": "string"},
                    }
                ],
            }
        }
    }
}

# 3. Custom tools (developed via plugins)
# Register in the Dify plugin system
```

---
## 4. Knowledge Base Management

### 4.1 Creating a Knowledge Base

```python
# Create a knowledge base via API
import requests

# Create knowledge base
resp = requests.post(
    f"{API_BASE}/datasets",
    headers={"Authorization": f"Bearer {API_KEY}"},
    json={
        "name": "K8s Operations Manual",
        "indexing_technique": "high_quality",  # high_quality / economy
        "permission": "all_team_members",
    },
)
dataset_id = resp.json()["id"]

# Upload document
with open("k8s-troubleshooting.md", "rb") as f:
    resp = requests.post(
        f"{API_BASE}/datasets/{dataset_id}/documents",
        headers={"Authorization": f"Bearer {API_KEY}"},
        files={"file": f},
        data={
            "process_rule": json.dumps({
                "mode": "automatic",
                "rules": {
                    "pre_processing_rules": [
                        {"id": "remove_extra_spaces", "enabled": True},
                        {"id": "remove_urls_emails", "enabled": True},
                    ],
                    "segmentation": {
                        "separator": "\n\n",
                        "max_tokens": 500,
                    },
                },
            }),
        },
    )
```

### 4.2 Retrieval Modes

```yaml
# Hybrid retrieval configuration
retrieval:
  model: text-embedding-3-small
  search_method: hybrid  # semantic / keyword / hybrid
  reranking:
    enabled: true
    model: rerank-v2
    top_n: 5
  top_k: 10
  score_threshold:
    enabled: true
    value: 0.5
```

### 4.3 Multi-Knowledge Base Retrieval

```yaml
# Agent configured with multiple knowledge bases
agent:
  knowledge_bases:
    - name: k8s_docs
      description: "Official K8s documentation"
      weight: 1.0
    - name: troubleshooting_guides
      description: "Troubleshooting guides"
      weight: 0.8
    - name: best_practices
      description: "Best practices"
      weight: 0.6
```

---

## 5. Plugin Ecosystem

### 5.1 Plugin Structure

```
dify-plugin-k8s/
├── manifest.yaml          # Plugin metadata
├── provider/
│   ├── k8s.yaml          # Provider definition
│   └── k8s.py            # Provider implementation
├── tools/
│   ├── get_pod.yaml      # Tool definition
│   ├── get_pod.py        # Tool implementation
│   ├── get_logs.yaml
│   └── get_logs.py
└── requirements.txt
```

```yaml
# manifest.yaml
name: k8s-tools
version: 1.0.0
description: "Kubernetes cluster management toolset"
author: Dillan Teagle
type: plugin
icon: k8s.png

plugins:
  tools:
    - provider/k8s.yaml
```

```yaml
# tools/get_pod.yaml
name: get_pod_status
description: "Query Pod status details"
parameters:
  namespace:
    type: string
    description: "Namespace"
    required: true
  pod_name:
    type: string
    description: "Pod name"
    required: false
```

### 5.2 Plugin Implementation

```python
# tools/get_pod.py
from dify_plugin import Tool
from dify_plugin.entities.tool import ToolInvokeMessage

class GetPodTool(Tool):
    def _invoke(self, tool_parameters: dict) -> ToolInvokeMessage:
        namespace = tool_parameters.get("namespace", "default")
        pod_name = tool_parameters.get("pod_name", "")

        import subprocess
        cmd = ["kubectl", "get", "pods", "-n", namespace, "-o", "json"]
        if pod_name:
            cmd = ["kubectl", "get", "pod", pod_name, "-n", namespace, "-o", "json"]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

        if result.returncode != 0:
            return self.create_text_message(f"Query failed: {result.stderr}")

        return self.create_json_message(json.loads(result.stdout))
```

---

## 6. K8s Helm Deployment

### 6.1 Helm Chart Configuration

```yaml
# values.yaml
api:
  replicaCount: 2
  image:
    repository: langgenius/dify-api
    tag: "0.6.0"
  resources:
    requests:
      cpu: "500m"
      memory: "1Gi"
    limits:
      cpu: "2000m"
      memory: "4Gi"
  env:
    - name: SECRET_KEY
      valueFrom:
        secretKeyRef:
          name: dify-secrets
          key: secret-key
    - name: DB_USERNAME
      valueFrom:
        secretKeyRef:
          name: dify-db
          key: username

worker:
  replicaCount: 2
  image:
    repository: langgenius/dify-api
    tag: "0.6.0"
  resources:
    requests:
      cpu: "500m"
      memory: "1Gi"

web:
  replicaCount: 2
  image:
    repository: langgenius/dify-web
    tag: "0.6.0"

# External PostgreSQL (recommended: RDS)
externalPostgres:
  enabled: true
  host: "dify-db.xxxx.rds.amazonaws.com"
  port: 5432
  database: "dify"

# External Redis
externalRedis:
  enabled: true
  host: "dify-redis.xxxx.cache.amazonaws.com"
  port: 6379

# Vector database
vectorStore:
  type: qdrant  # qdrant / weaviate / milvus
  qdrant:
    endpoint: "http://qdrant:6333"

# File storage
storage:
  type: s3  # s3 / azure_blob / local
  s3:
    bucket: "dify-files"
    region: "us-east-1"
```

### 6.2 Installation

``` bash
# 🟡 Medium risk: modifies cluster/resource state — confirm target, scope, and authorization before executing
# Add Helm repository
helm repo add dify https://langgenius.github.io/dify-helm
helm repo update

# Install
helm install dify dify/dify \
  -n ai-platform \
  --create-namespace \
  -f values.yaml

# Upgrade
helm upgrade dify dify/dify -n ai-platform -f values.yaml
```
---
## 7. Multi-Tenant Configuration

### 7.1 Workspace Isolation

```yaml
# Dify supports multiple workspaces
workspace:
  # Each team has an independent workspace
  teams:
    - name: "sre-team"
      plan: "professional"
      max_apps: 50
      max_knowledge_docs: 10000
    - name: "dev-team"
      plan: "basic"
      max_apps: 10
      max_knowledge_docs: 1000
```

### 7.2 API Key Management

```python
# Each application has an independent API Key
# Created via the Dify console

# Application-level access control
headers = {"Authorization": "Bearer app-xxxxx"}

# User-level identification
payload = {"user": "user-id-123"}
```

---

## Related

- [[domain-14-ai-ml-infra/03-agent-runtime/01-langchain-langgraph-deep-dive|LangChain/LangGraph Deep Dive Guide]]
- [[domain-14-ai-ml-infra/03-agent-runtime/07-agent-framework-selection-guide|Agent Framework Selection Decision Tree]]

## See Also

- [[domain-14-ai-ml-infra/03-agent-runtime/03-crewai-multi-agent-framework|CrewAI Multi-Agent Framework]]
- [[domain-14-ai-ml-infra/03-agent-runtime/06-semantic-kernel-enterprise|Semantic Kernel Enterprise-Grade Agent]]


<!-- risk-assessed -->
