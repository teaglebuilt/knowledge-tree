---
title: CrewAI Multi-Agent Framework In-Depth Guide
description: 'Comprehensive breakdown of CrewAI's four-layer abstraction (Crew/Agent/Task/Tool), covering role definition, task delegation, process patterns, memory mechanisms, and K8s production deployment'
summary: 'Comprehensive breakdown of CrewAI's four-layer abstraction, covering role definition, task delegation, process patterns, and K8s deployment'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- crewai
- multi-agent
- orchestration
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
- What is the CrewAI multi-agent framework
- How to use the CrewAI multi-agent framework
- CrewAI role definition and task delegation
trigger_keywords:
- crewai
- multi-agent
- crew
- agent
- task
- delegation
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/03-crewai-multi-agent-framework.md
---
> **Production Environment Safety Notice**
>
> This document contains operational commands that can be executed directly. Before executing, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have validated in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state, but is generally reversible), 🟢 Low risk / Read-only (information gathering, no side effects).


# CrewAI Multi-Agent Framework In-Depth Guide

## 1. Core Architecture

### 1.1 Four-Layer Abstraction Model

CrewAI builds a multi-Agent collaboration system around four core concepts:

```
# 🟢 Low risk: Read-only / information gathering, generally no side effects
┌─────────────────────────────────────────────────┐
│                   Crew (Team)                    │
│  ┌──────────────────────────────────────────┐    │
│  │  Process: Sequential / Hierarchical      │    │
│  └──────────────────────────────────────────┘    │
│                                                  │
│  ┌──────────────┐  ┌──────────────┐              │
│  │ Agent A      │  │ Agent B      │              │
│  │ Role: Diagnostician │ Role: Fixer │            │
│  │ Goal: Locate root cause │ Goal: Execute fix │  │
│  │ Tools: [k8s] │  │ Tools: [kubectl]│            │
│  └──────┬───────┘  └──────┬───────┘              │
│         │                  │                     │
│  ┌──────┴───────┐  ┌──────┴───────┐              │
│  │ Task 1       │  │ Task 2       │              │
│  │ Diagnose Pod anomaly │ Execute fix plan │      │
│  │ Context: []  │  │ Context: [T1] │              │
│  └──────────────┘  └──────────────┘              │
└─────────────────────────────────────────────────┘
```
### 1.2 Agent Definition

```python
from crewai import Agent

# K8s Diagnostics Expert Agent
diagnostician = Agent(
    role="K8s Diagnostics Expert",
    goal="Quickly and accurately locate the root cause of Pod anomalies in Kubernetes clusters",
    backstory=(
        "You are a senior Kubernetes SRE engineer with 10 years of cluster operations experience."
        "You excel at extracting key information from logs, events, and metrics, using elimination to narrow down the fault scope."
        "You always collect sufficient data before drawing conclusions and never guess."
    ),
    tools=[kubectl_tool, log_analyzer_tool, metrics_query_tool],
    llm="gpt-4o",
    verbose=True,
    allow_delegation=False,  # Whether to allow delegating tasks to other Agents
    max_iter=15,             # Maximum reasoning iteration count
    max_retry_limit=3,       # Maximum retry count
    memory=True,             # Enable short-term memory
)

# Fix Execution Agent
fixer = Agent(
    role="K8s Repair Engineer",
    goal="Safely and efficiently execute Kubernetes cluster repair operations",
    backstory=(
        "You are a K8s cluster repair expert, skilled at restoring services with minimal impact."
        "You always confirm the rollback plan before executing any write operations."
    ),
    tools=[kubectl_apply_tool, rollout_tool],
    llm="gpt-4o",
    allow_delegation=False,
)

# Validation Agent
validator = Agent(
    role="Repair Validation Engineer",
    goal="Verify whether the repair operation was successful and confirm service has returned to normal",
    backstory=(
        "You are responsible for comprehensive validation after a repair to ensure the issue is resolved with no side effects."
    ),
    tools=[kubectl_tool, health_check_tool, metrics_query_tool],
    llm="gpt-4o",
    allow_delegation=True,  # Can delegate tasks
)
```

### 1.3 Task Definition

```python
from crewai import Task

# Diagnosis task
diagnosis_task = Task(
    description=(
        "Analyze Pod anomalies for nginx-deployment in the default namespace."
        "Specific steps:\n"
        "1. Check Pod status and recent events\n"
        "2. Check container logs (last 500 lines)\n"
        "3. Check Pod resource usage\n"
        "4. Check whether related ConfigMaps and Secrets exist\n"
        "5. Output a root cause analysis report"
    ),
    expected_output=(
        "A structured diagnostic report containing:\n"
        "- Problem description\n"
        "- Evidence list (log excerpts, events, metrics)\n"
        "- Root cause analysis\n"
        "- Fix recommendations (including specific commands)\n"
        "- Risk assessment"
    ),
    agent=diagnostician,
    # Output file (optional)
    output_file="diagnosis_report.md",
)

# Fix task (depends on the output of the diagnosis task)
fix_task = Task(
    description=(
        "Execute repair operations based on the diagnostic report. Requirements:\n"
        "1. First list the repair steps and rollback plan\n"
        "2. Execute step by step, verifying each step\n"
        "3. Record the execution process and results"
    ),
    expected_output="Repair execution report, including each operation and its result",
    agent=fixer,
    context=[diagnosis_task],  # Depends on the output of the diagnosis task
)

# Validation task
validation_task = Task(
    description=(
        "Verify whether the repair was successful:\n"
        "1. Check whether the Pod status is Running\n"
        "2. Verify that health checks pass\n"
        "3. Confirm there are no new error events\n"
        "4. Compare metrics before and after the repair"
    ),
    expected_output="Validation report confirming the service has returned to normal",
    agent=validator,
    context=[fix_task],
)
```

---

## 2. Process Modes

### 2.1 Sequential Process

Tasks are executed one by one in sequence; the output of the previous task is automatically passed to the next:

```python
from crewai import Crew, Process

# Sequential process: Diagnose → Fix → Validate
crew = Crew(
    agents=[diagnostician, fixer, validator],
    tasks=[diagnosis_task, fix_task, validation_task],
    process=Process.sequential,
    verbose=True,
    memory=True,           # Enable team memory
    max_rpm=10,            # API call rate limit
    share_crew=False,      # Whether to share Crew context
)

# Execute
result = crew.kickoff(inputs={
    "namespace": "default",
    "pod_name": "nginx-abc123",
})
print(result.raw)          # Final output
print(result.tasks_output) # List of outputs from each task
```

### 2.2 Hierarchical Process

A Manager Agent automatically coordinates task assignment:

```python
from crewai import Crew, Process

crew = Crew(
    agents=[diagnostician, fixer, validator],
    tasks=[diagnosis_task, fix_task, validation_task],
    process=Process.hierarchical,
    manager_llm="gpt-4o",  # LLM used by the Manager Agent
    manager_agent=None,     # Can customize the Manager Agent
    verbose=True,
)

# The Manager Agent will automatically:
# 1. Analyze task dependencies
# 2. Decide execution order
# 3. Assign tasks to appropriate Agents
# 4. Handle context passing between tasks
result = crew.kickoff()
```

### 2.3 Parallel Execution

Independent tasks can be executed in parallel:

```python
# Collect information from different dimensions in parallel
collect_logs_task = Task(
    description="Collect Pod logs",
    agent=log_analyzer,
    async_execution=True,  # Mark as asynchronous execution
)

collect_metrics_task = Task(
    description="Collect resource metrics",
    agent=metrics_analyzer,
    async_execution=True,
)

collect_events_task = Task(
    description="Collect cluster events",
    agent=event_analyzer,
    async_execution=True,
)

# Synthesis task (waits for all parallel tasks to complete)
synthesize_task = Task(
    description="Synthesize all information and analyze the root cause",
    agent=diagnostician,
    context=[
        collect_logs_task,
        collect_metrics_task,
        collect_events_task,
    ],
)

crew = Crew(
    agents=[log_analyzer, metrics_analyzer, event_analyzer, diagnostician],
    tasks=[
        collect_logs_task,
        collect_metrics_task,
        collect_events_task,
        synthesize_task,
    ],
    process=Process.sequential,
)
```

---
## 3. Custom Tool Development

### 3.1 Tool Base Class

```python
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

# Tool input schema
class KubectlQueryInput(BaseModel):
    namespace: str = Field(
        default="default",
        description="Kubernetes namespace"
    )
    resource: str = Field(
        description="Resource type: pod/service/deployment/configmap"
    )
    name: str = Field(
        default="",
        description="Resource name, leave empty to list all"
    )

# Tool implementation
class KubectlQueryTool(BaseTool):
    name: str = "kubectl_query"
    description: str = (
        "Query Kubernetes cluster resource status. "
        "Can view detailed information for Pod, Service, Deployment, and other resources."
    )
    args_schema: Type[BaseModel] = KubectlQueryInput

    def _run(
        self,
        namespace: str = "default",
        resource: str = "pod",
        name: str = "",
    ) -> str:
        import subprocess
        cmd = ["kubectl", "get", resource]
        if name:
            cmd.append(name)
        cmd.extend(["-n", namespace, "-o", "wide"])

        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            return f"Command execution failed: {result.stderr}"
        return result.stdout
```

### 3.2 Advanced Tool Example

```python
from crewai.tools import BaseTool
from typing import Type

class LogAnalysisInput(BaseModel):
    namespace: str = Field(description="Namespace")
    pod_name: str = Field(description="Pod name")
    keyword: str = Field(default="", description="Filter keyword")
    tail_lines: int = Field(default=200, description="Retrieve the last N lines of logs")

class LogAnalysisTool(BaseTool):
    name: str = "log_analysis"
    description: str = (
        "Analyze Pod logs with support for keyword filtering and error pattern recognition. "
        "Returns recent log entries and error statistics."
    )
    args_schema: Type[BaseModel] = LogAnalysisInput

    def _run(
        self,
        namespace: str,
        pod_name: str,
        keyword: str = "",
        tail_lines: int = 200,
    ) -> str:
        import subprocess
        import re
        from collections import Counter

        # Fetch logs
        cmd = [
            "kubectl", "logs", pod_name,
            "-n", namespace,
            f"--tail={tail_lines}",
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            return f"Failed to retrieve logs: {result.stderr}"

        lines = result.stdout.strip().split("\n")

        # Keyword filtering
        if keyword:
            lines = [l for l in lines if keyword.lower() in l.lower()]

        # Error pattern statistics
        error_patterns = Counter()
        for line in lines:
            if re.search(r"\b(error|exception|fatal|panic)\b", line, re.I):
                # Extract error type
                match = re.search(r"(\w+Error|\w+Exception)", line)
                if match:
                    error_patterns[match.group()] += 1

        # Format output
        output = f"=== Log Analysis ({namespace}/{pod_name}) ===\n"
        output += f"Total lines: {len(lines)}\n"
        output += f"Error patterns:\n"
        for pattern, count in error_patterns.most_common(10):
            output += f"  {pattern}: {count} occurrences\n"
        output += f"\nLast 20 log lines:\n"
        for line in lines[-20:]:
            output += f"  {line}\n"

        return output
```

### 3.3 Async Tools

```python
import aiohttp
from crewai.tools import BaseTool

class PrometheusQueryTool(BaseTool):
    name: str = "prometheus_query"
    description: str = "Execute PromQL queries to retrieve cluster metrics"

    def _run(self, query: str, duration: str = "1h") -> str:
        import requests
        url = "http://prometheus:9090/api/v1/query_range"
        params = {
            "query": query,
            "start": f"now-{duration}",
            "end": "now",
            "step": "60s",
        }
        resp = requests.get(url, params=params, timeout=30)
        data = resp.json()
        if data["status"] != "success":
            return f"Query failed: {data.get('error', 'unknown')}"
        return json.dumps(data["data"]["result"][:5], indent=2)
```

---

## 4. Memory and Delegation Mechanisms

### 4.1 Short-Term Memory

CrewAI has a built-in memory system that maintains context across tasks:

```python
crew = Crew(
    agents=[diagnostician, fixer, validator],
    tasks=[diagnosis_task, fix_task, validation_task],
    memory=True,          # Enable short-term memory
    embedder={            # Custom embedding model
        "provider": "openai",
        "config": {
            "model": "text-embedding-3-small",
        }
    },
)
```

### 4.2 Long-Term Memory

Persistent memory storage that retains knowledge across sessions:

```python
from crewai.memory import LongTermMemory, EntityMemory
from crewai.memory.storage import SQLiteStorage

# Configure persistent storage
crew = Crew(
    agents=[diagnostician, fixer],
    tasks=[diagnosis_task],
    memory=True,
    long_term_memory=LongTermMemory(
        storage=SQLiteStorage(db_path="./crew_memory.db"),
    ),
    entity_memory=EntityMemory(
        storage=SQLiteStorage(db_path="./crew_entities.db"),
    ),
)
```

### 4.3 Task Delegation

Agents can delegate subtasks to other agents:

```python
# Agent with delegation enabled
supervisor = Agent(
    role="Operations Supervisor",
    goal="Coordinate the team to complete cluster troubleshooting",
    allow_delegation=True,  # Enable delegation
    tools=[],
)

# Agents can:
# 1. Delegate tool calls to more specialized agents
# 2. Request input from other agents
# 3. Delegate validation and confirmation tasks
```

---
## 5. K8s Deployment and Scaling

### 5.1 Dockerization

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/

# Install kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -Ls \
    https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    chmod +x kubectl && mv kubectl /usr/local/bin/

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 5.2 Helm Chart

```yaml
# helm/crewai-agent/values.yaml
replicaCount: 2

image:
  repository: registry.example.com/crewai-agent
  tag: "1.0.0"

env:
  - name: OPENAI_API_KEY
    valueFrom:
      secretKeyRef:
        name: llm-secrets
        key: openai-api-key
  - name: CREW_MEMORY_DB
    value: "/data/crew_memory.db"

# Persistent storage (memory database)
persistence:
  enabled: true
  storageClass: gp3
  size: 10Gi
  mountPath: /data

resources:
  requests:
    cpu: "500m"
    memory: "1Gi"
  limits:
    cpu: "2000m"
    memory: "4Gi"

serviceAccount:
  create: true
  name: crewai-agent

rbac:
  create: true
  rules:
    - apiGroups: [""]
      resources: ["pods", "services", "events", "configmaps", "secrets"]
      verbs: ["get", "list", "watch"]
    - apiGroups: ["apps"]
      resources: ["deployments", "replicasets", "statefulsets"]
      verbs: ["get", "list", "watch", "patch", "update"]
```

### 5.3 FastAPI Service Wrapper

```python
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from crewai import Crew, Process
import uuid

app = FastAPI(title="CrewAI K8s Agent")

class DiagnosisRequest(BaseModel):
    namespace: str = "default"
    pod_name: str = ""
    description: str = ""
    priority: str = "P2"

class TaskStatus(BaseModel):
    task_id: str
    status: str  # pending/running/completed/failed
    result: str | None = None

# Task storage
tasks_db: dict[str, TaskStatus] = {}

@app.post("/diagnose")
async def start_diagnosis(
    req: DiagnosisRequest,
    background_tasks: BackgroundTasks,
):
    task_id = str(uuid.uuid4())
    tasks_db[task_id] = TaskStatus(task_id=task_id, status="pending")

    background_tasks.add_task(run_diagnosis, task_id, req)
    return {"task_id": task_id, "status": "pending"}

@app.get("/tasks/{task_id}")
async def get_task_status(task_id: str) -> TaskStatus:
    if task_id not in tasks_db:
        raise HTTPException(404, "Task not found")
    return tasks_db[task_id]

async def run_diagnosis(task_id: str, req: DiagnosisRequest):
    tasks_db[task_id].status = "running"
    try:
        crew = Crew(
            agents=[diagnostician, fixer, validator],
            tasks=[diagnosis_task, fix_task, validation_task],
            process=Process.sequential,
            memory=True,
        )
        result = crew.kickoff(inputs={
            "namespace": req.namespace,
            "pod_name": req.pod_name,
            "description": req.description,
        })
        tasks_db[task_id].status = "completed"
        tasks_db[task_id].result = result.raw
    except Exception as e:
        tasks_db[task_id].status = "failed"
        tasks_db[task_id].result = str(e)
```

---

## 6. Production Best Practices

### 6.1 Rate Limiting and Cost Control

```python
crew = Crew(
    agents=agents,
    tasks=tasks,
    max_rpm=20,           # Maximum requests per minute
    language="zh-CN",     # Output language
    full_output=True,     # Full output (including intermediate steps)
)
```

### 6.2 Error Handling

```python
try:
    result = crew.kickoff()
except Exception as e:
    # CrewAI will automatically retry up to max_retry_limit times
    # An exception is raised after the limit is exceeded
    logger.error(f"Crew execution failed: {e}")
    # Fall back to single-agent mode
    fallback_result = diagnostician.kickoff()
```

### 6.3 Observability

```python
# CrewAI integrates with LangSmith
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "your-key"

# Custom callbacks
from crewai.utilities.events import CrewAgentExecutionEvent

def on_agent_step(event: CrewAgentExecutionEvent):
    print(f"[{event.agent.role}] {event.type}: {event.output}")

crew = Crew(agents=agents, tasks=tasks, verbose=True)
```

---

## Related

- [[domain-14-ai-ml-infra/03-agent-runtime/01-langchain-langgraph-deep-dive|LangChain/LangGraph Deep Dive Guide]]
- [[domain-14-ai-ml-infra/03-agent-runtime/04-autogen-microsoft-agent|Microsoft AutoGen]]

## See Also

- [[domain-14-ai-ml-infra/03-agent-runtime/07-agent-framework-selection-guide|Agent Framework Selection Decision Tree]]


<!-- risk-assessed -->
