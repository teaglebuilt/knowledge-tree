---
title: AI Agent Sandbox Security Architecture
description: AI Agent Code Execution Sandbox, Tool Invocation Security, Data Isolation, Kubernetes-based Agent Security Deployment Solution
summary: AI Agent Code Execution Sandbox, Tool Invocation Security, Data Isolation, Kubernetes-based Agent Security Deployment Solution
category: ai-infra
tags:
- k8s
- ai
- agent
- sandbox
- security
- isolation
- gvisor
- wasm
- rbac
- prometheus
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Security Engineers
- Architects
estimated_read_time: 40min
intent_queries:
- How to Implement AI Agent Sandbox
- Code Execution Security Isolation for Agent
- Permission Control for Agent Tool Invocation
- Secure Deployment of AI Agent on Kubernetes
- Protection Against Agent Prompt Injection
trigger_keywords:
- Agent Sandbox
- Security for AI Agent
- Code Execution Sandbox
- Tool Invocation Security
- Agent Isolation
prerequisites:
- kubectl-basics
- prometheus-basics
- gpu-scheduling-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: Dillan Teagle
  role: contributor
cross_refs:
- type: domain
  path: ../domain-05-security-compliance/
  label: Cloud-Native Security Knowledge Domain
- type: domain
  path: ../domain-14-ai-ml-infra/
  label: AI Infrastructure
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/37-agent-sandbox-security.md
---

> **Production Environment Security Tips**
>
> This document contains executable operational commands. Please confirm before execution: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether these commands have been validated in a non-production environment. Risk level annotations: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# AI Agent Sandbox Security Architecture

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.28 - v1.33 | **Last Updated**: 2026-05

---


## 1. Overview

AI Agent possesses the capability to **execute autonomous code, invoke tools, access external systems**, which brings traditional applications no traditional security risks:

| Risk Type | Description | Severity |
|----------|------|----------|
| Code Execution | Agent generates and executes arbitrary code (Python/Bash) | Extreme |
| Tool Abuse | Agent calls dangerous operations such as deletion/modification | High |
| Data Leakage | Agent reads sensitive data and leaks it externally | High |
| Prompt Injection | Malicious inputs hijack Agent behavior | High |
| Resource Exhaustion | Agent enters an infinite loop or allocates excessive resources | Medium |

**Sandbox's Objective**: Minimize the risk boundary of each operation without affecting Agent functionality.

---


## 2. Sandbox Architecture Models

### 2.1 Comparison of Four Modes

| Mode | Isolation Strength | Startup Speed | Resource Consumption | Applicable Scenarios |
|------|---------|---------|---------|---------|
| Container-Level (gVisor) | ★★★★ | ~100ms | ~15MB | General code execution |
| Virtual Machine-Level (Firecracker) | ★★★★★ | ~125ms | ~5MB | Untrusted code |
| Process-Level (nsjail) | ★★★ | ~10ms | ~1MB | Lightweight rapid execution |
| WebAssembly-Level | ★★★ | ~5ms | ~2MB | Edge/lightweight tasks |

### 2.2 Recommended Selection

```
Agent task type  recommended sandbox  reason
──────────────────────────────────────────────────
Python script execution gVisor container compatibility good, isolation strong
Bash commands execution           nsjail + gVisor   quick start, dual isolation
file read/write gVisor + read-only mount deterrent against filesystem damage
Network request   NetworkPolicy  limitation exit domain/IP
Database operations RBAC + Audit logs Minimum permissions + Traceable
Untrusted Code             Firecracker VM    Strongest Isolation
```

---


## 3. Agent Sandbox Implementation on K8s

### 3.1 Safe Template for Agent Pods

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: agent-sandbox
  namespace: agent-workspace
  labels:
    app: ai-agent
    security-level: sandbox
spec:
  runtimeClassName: gvisor          # gVisor 沙箱
  serviceAccountName: agent-limited # 最小权限 SA
  securityContext:
    runAsNonRoot: true
    runAsUser: 65534
    fsGroup: 65534
    seccompProfile:
      type: RuntimeDefault
  containers:
    - name: agent-runtime
      image: agent-runtime:latest
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: ["ALL"]
      resources:
        limits:
          cpu: "2"
          memory: "2Gi"
        requests:
          cpu: "500m"
          memory: "512Mi"
      volumeMounts:
        - name: tmp
          mountPath: /tmp
        - name: workspace
          mountPath: /workspace
          readOnly: false
      env:
        - name: AGENT_TIMEOUT
          value: "300"              # 5 分钟超时
        - name: AGENT_MAX_MEMORY
          value: "1Gi"
  volumes:
    - name: tmp
      emptyDir:
        sizeLimit: "500Mi"
    - name: workspace
      emptyDir:
        sizeLimit: "1Gi"
```

### 3.2 NetworkPolicy Restrictions

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: agent-sandbox-netpol
  namespace: agent-workspace
spec:
  podSelector:
    matchLabels:
      app: ai-agent
  policyTypes:
    - Egress
  egress:
    # Allow DNS
    - to: []
      ports:
        - port: 53
          protocol: UDP
    # Allow access to LLM API
    - to:
        - ipBlock:
            cidr: 0.0.0.0/0
      ports:
        - port: 443
          protocol: TCP
    # Prohibit access to internal services (default deny)
    # All other outbound traffic is blocked
```

### 3.3 RBAC Least Privilege

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: agent-limited
  namespace: agent-workspace
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: agent-readonly
  namespace: agent-workspace
rules:
  - apiGroups: [""]
    resources: ["pods", "services", "configmaps"]
    verbs: ["get", "list"]
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list"]
  # Allow create/update/delete
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: agent-readonly-binding
  namespace: agent-workspace
subjects:
  - kind: ServiceAccount
    name: agent-limited
roleRef:
  kind: Role
  name: agent-readonly
  apiGroup: rbac.authorization.k8s.io
```

---


## 4. Tool Call Security

### 4.1 Graded Approval Model

```
Tool Risk Level    Example                    Agent behavior
─────────────────────────────────────────────────
L0 Low risk      Query status/Read metrics        Autonomous execution
L1 Low risk      Read logs/View configuration    Autonomous execution + Record
L2 Medium risk    Restart Pod/Edit ConfigMap      Confirm before execution
L3 High risk      Delete resources/Edit RBAC      Mandatory manual approval
```

### 4.2 Configuration of Tool Whitelists

```yaml
# Agent tool permission configuration
agent_tools:
  allowed:
    - name: "kubectl_get"
      risk_level: "L0"
      params:
        resources: ["pods", "services", "nodes", "events"]
        verbs: ["get", "list"]
    
    - name: "kubectl_describe"
      risk_level: "L1"
      params:
        resources: ["pods", "services", "deployments"]
    
    - name: "kubectl_logs"
      risk_level: "L1"
      params:
        max_lines: 1000
  
  blocked:
    - "kubectl_delete"
    - "kubectl_exec"
    - "kubectl_cp"
  
  require_approval:
    - name: "kubectl_restart"
      risk_level: "L2"
      approvers: ["sre-team"]
    
    - name: "kubectl_scale"
      risk_level: "L2"
      approvers: ["sre-team"]
```

---


## 5. Code Execution Sandbox

### 5.1 Temporary Container Execution Mode

```yaml
# Agent execution Pod (temp, destroy on completion)
apiVersion: v1
kind: Pod
metadata:
  name: agent-code-exec-{{execution_id}}
  namespace: agent-workspace
  annotations:
    agent.io/execution-id: "{{execution_id}}"
    agent.io/timeout: "300"
spec:
  runtimeClassName: gvisor
  restartPolicy: Never
  activeDeadlineSeconds: 300          # 强制 5 分钟超时
  securityContext:
    runAsNonRoot: true
    runAsUser: 65534
  containers:
    - name: executor
      image: python-sandbox:3.12      # 预装常用库的沙箱镜像
      command: ["python3", "-c", "{{agent_code}}"]
      securityContext:
        readOnlyRootFilesystem: true
        allowPrivilegeEscalation: false
      resources:
        limits:
          cpu: "1"
          memory: "512Mi"
      volumeMounts:
        - name: tmp
          mountPath: /tmp
  volumes:
    - name: tmp
      emptyDir:
        sizeLimit: "100Mi"
```

### 5.2 Timeout and Resource Control

```python
# Agent Execution Controller
import kubernetes
import time

def execute_in_sandbox(code: str, timeout: int = 300):
    """Execute the code generated by the Agent in a sandbox"""
    pod_manifest = build_sandbox_pod(code, timeout)
    
    # Create Pod
    v1 = kubernetes.client.CoreV1Api()
    pod = v1.create_namespaced_pod("agent-workspace", pod_manifest)
    
    # Wait for completion or timeout
    start = time.time()
    while time.time() - start < timeout:
        status = v1.read_namespaced_pod_status(pod.metadata.name, "agent-workspace")
        if status.status.phase in ("Succeeded", "Failed"):
            break
        time.sleep(1)
    
    # Get output
    logs = v1.read_namespaced_pod_log(pod.metadata.name, "agent-workspace")
    
    # Clean up Pod
    v1.delete_namespaced_pod(pod.metadata.name, "agent-workspace")
    
    return logs
```

---


## 6. Monitoring and Auditing

### 6.1 Tracking of Agent Behavior

```yaml
# Prometheus metrics
agent_tool_calls_total{tool="kubectl_get", risk_level="L0"} 1523
agent_tool_calls_total{tool="kubectl_restart", risk_level="L2"} 12
agent_tool_calls_blocked{tool="kubectl_delete", reason="not_allowed"} 5
agent_code_executions_total{status="success"} 342
agent_code_executions_total{status="timeout"} 8
agent_code_executions_total{status="oom"} 3
agent_approval_pending{risk_level="L2"} 2
agent_approval_pending{risk_level="L3"} 0
```

### 6.2 Audit Log Format

```json
{
  "timestamp": "2026-05-19T10:30:00Z",
  "agent_id": "agent-001",
  "execution_id": "exec-abc123",
  "action": "tool_call",
  "tool": "kubectl_restart",
  "risk_level": "L2",
  "params": {"namespace": "production", "deployment": "api-server"},
  "status": "approved",
  "approver": "sre-oncall",
  "latency_ms": 1234
}
```

---


## 7. Production Checklist

- [ ] Use gVisor RuntimeClass for Agent Pod
- [ ] Enable readOnlyRootFilesystem
- [ ] Force runAsNonRoot
- [ ] Limit outbound traffic with NetworkPolicy
- [ ] RBAC Least Privilege (Read-Only)
- [ ] Code Execution Timeout ≤ 5 Minutes
- [ ] Memory Limit ≤ 2Gi
- [ ] Tool Whitelist Configuration
- [ ] Level 2/Level 3 Operations Manual Approval
- [ ] Audit Logs Full Recording
- [ ] Alert for Abnormal Behaviors (Call Frequency/Timeout/OOM)
- [ ] Sandbox Pod Automatic Cleanup (TTL)

---


## Obsidian Related Documentation

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- index.md|Domain-11 AI Infrastructure — Open Source Project Index]]
- AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management

## See Also

- 35-model-drift-monitoring
- 36-ai-platform-observability-enhanced
- 99-kubeflow-ai-platform-guide
- 01-ai-infrastructure-overview


<!-- risk-assessed -->
