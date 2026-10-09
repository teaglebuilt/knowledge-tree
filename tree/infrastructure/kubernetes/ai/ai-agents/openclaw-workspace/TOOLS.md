---
title: Tool Authorization Registry (02-ai-agents)
description: 'title: Tool Authorization Registry'
summary: 'title: Tool Authorization Registry'
category: general
tags:
- ai
- ai-agent
- etcd
- apiserver
- kubelet
- prometheus
- grafana
- istio
- helm
- job
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 15min
intent_queries:
- What is Tool Authorization Registry
- How to use Tool Authorization Registry
- Kubernetes 14 ai ml infra Best Practices
trigger_keywords:
- What is Tool Authorization Registry
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- helm-basics
- service-mesh-basics
- prometheus-basics
- monitoring-basics
- etcd-basics
- tls-basics
- logging-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/openclaw-workspace/TOOLS.md
---

> **Production Environment Security Reminders**
>
> This document contains executable operational commands. Execute them only after confirming: the correct target cluster and namespace; sufficient RBAC permissions; and successful validation in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




title: Tool Authorization Registry
description: Specification and security constraints for tool authorization registry of Kubernetes Operational Diagnostic Agent
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- [[etcd|etcd]]
- apiserver
- [[kubelet|kubelet]]
- [[Prometheus|prometheus]]
- grafana
last_updated: 2026-04
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- Architect
- SRE
estimated_read_time: 5min
intent_queries:
- What is the Tool Authorization Registry
- How does the Tool Authorization Registry work
trigger_keywords:
- Tool Authorization Registry
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
# Tool Authorization Registry

## 1. List of Authorized Tools

### 1.1 Information Collection Tools (Read-Only, Default Authorized)

| Tool | Purpose | Permission Level | Output Format |
|------|------|---------|---------|
| `kubectl get` | View resource lists and statuses | Read-Only | table/json/yaml |
| `kubectl describe` | View detailed resource information and events | Read-Only | text |
| `kubectl logs` | View pod logs | Read-Only | text |
| `kubectl top` | View resource usage rates | Read-Only | table |
| `kubectl events` | View cluster events | Read-Only | table |
| `kubectl api-resources` | View available API resources | Read-Only | table |
| `kubectl cluster-info` | View cluster basic information | Read-Only | text |
| `kubectl version` | View version information | Read-Only | json |

### 1.2 Monitoring Query Tools (Read-Only, Default Authorized)

| Tool | Purpose | Permission Level | Parameter Specification |
|------|------|---------|---------|
| `prometheus_query` | Execute Prometheus Query Language (PromQL) instant queries | Read-Only | `query`: PromQL expression |
| `prometheus_query_range` | Execute Prometheus Query Range | Read-Only | `query`, `start`, `end`, `step` |
| `loki_search` | Search Logs | Read-Only | `query`: LogQL expression, `limit` |
| `grafana_dashboard` | View Dashboard Panel | Read-Only | `dashboard_uid`, `panel_id` |

### 1.3 Auxiliary Tools (Read-Only, Default Authorized)

| Tools | Purpose | Permission Level | Description |
|------|------|---------|------|
| `view_text_file` | Read Text File | Read-Only | Used to read REFERENCE files like SKILL.md |
| `execute_shell_command` | Execute Shell Command | Limited Read-Only | Only allows collection-type commands |
| `helm_info` | View Helm Release Information | Read-Only | `helm list`, `helm get values` |
| `etcdctl_status` | View etcd Cluster Status | Read-Only | Limited to `endpoint status/health` |

### 1.4 Limited Write Operation Tools (User Confirmation Required)

| Tools | Purpose | Permission Level | Confirmation Required |
|------|------|---------|---------|
| `kubectl apply` | Apply Configuration Changes | Limited Write | Must first show diff, wait for user confirmation |
| `kubectl scale` | Adjust Pod Count | Limited Write | Show current value and target value, wait for confirmation |
| `kubectl rollout` | Manage Rolling Updates | Limited Write | Only allows `restart` and `undo` |
| `kubectl label` | Manage Labels | Limited Write | Show change content, wait for confirmation |
| `kubectl annotate` | Manage Annotations | Limited Write | Show change content, wait for confirmation |

## 2. Priority of Tool Usage

> ⚠️ **🟡 Medium Risk Changes** — Change cluster resource states, suggest confirming with --dry-run or diff first
> - `kubectl apply/create/replace`: Apply/Change cluster resources

```
# 🟡 Medium Risk: Modifies cluster/resource status; confirm target, impact scope, and authorization before proceeding
Diagnostic tool call order for scenarios:

Level 1: Macro state (mandatory)
  kubectl get pods -n <ns> -o wide
  kubectl get nodes -o wide
  kubectl get events -n <ns> --sort-by=.lastTimestamp

Level 2: Micro details (as needed)
  kubectl describe <resource> -n <ns>
  kubectl logs <pod> -n <ns> [--previous] [--tail=100]
  kubectl top pods/nodes

Level 3: Monitoring data (deep analysis)
  prometheus_query (resource usage trend, error rate)
  loki_search (log keyword search)

Level 4: Write operations (only after user confirmation)
  kubectl apply/scale/rollout
```
## 3. Parameter Specifications

### 3.1 General Parameters for kubectl

```
Parameters that must be included:
  -n <namespace>          # all commands must explicitly specify namespace
  --context <context>      # Multi-cluster environments must specify context

Recommended output format:
  -o wide                  # List queries use wide format
  -o json                  # needs parsing when using json
  -o jsonpath='{...}'      # extract a single field precisely
  -o custom-columns=...    # Custom column output

Log query parameters:
  --tail=100               # Default limit to 100 lines
  --since=30m              # Default last 30 minutes
  --previous               # View logs from the previous crash loop
  --timestamps             # Include timestamps
```

### 3.2 Common Templates for PromQL

```yaml
# Pod CPU Usage
sum(rate(container_cpu_usage_seconds_total{namespace="<ns>", pod=~"<pod>.*"}[5m])) by (pod)

# Pod Memory Usage
sum(container_memory_working_set_bytes{namespace="<ns>", pod=~"<pod>.*"}) by (pod)

# Node CPU Usage
100 - (avg by(instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# API Server Request Latency P99
histogram_quantile(0.99, sum(rate(apiserver_request_duration_seconds_bucket[5m])) by (le, verb))

# etcd Latency
histogram_quantile(0.99, sum(rate(etcd_disk_wal_fsync_duration_seconds_bucket[5m])) by (le))

# Pod Restart Count
sum(increase(kube_pod_container_status_restarts_total{namespace="<ns>"}[1h])) by (pod)
```

### 3.3 Common Templates for LogQL

```yaml
# Pod Error Logs
{namespace="<ns>", pod=~"<pod>.*"} |= "error" | logfmt

# kubelet Logs
{unit="kubelet"} |= "failed" | logfmt

# API Server Audit Logs
{job="apiserver-audit"} | json | verb="delete"
```

## 4. Security Constraints

### 4.1 Command Blacklist

> **🔴 High Risk Operations Warning**
>
> Below commands are irreversible or highly impactful operations, execute only after confirming:
> - Backed up critical data and configurations
> - During approved change window
> - Has obtained authorization from relevant responsible parties
> - Has prepared rollback or recovery plans
> - Target cluster, Namespace, node/resource names are correct without error

```
# 🔴 High Risk: May cause data loss or service disruption; ensure backup, approval for changes, and rollback plan before executing
Absolute prohibition of command modes (regex matching):

kubectl\s+delete\s+(namespace|ns|node|pv)\b
kubectl\s+delete\s+.*--all\b
kubectl\s+drain\s+.*--force
kubectl\s+cordon\b
kubectl\s+taint\b
kubectl\s+edit\b
kubectl\s+exec\s+.*--\s+(rm|mv|dd|mkfs|fdisk)
kubectl\s+create\s+clusterrolebinding
helm\s+uninstall\b
etcdctl\s+del\b
```
### 4.2 Whitelist Mode for Namespaces

```
Default policy: Allow all read-only operations in non-system namespaces

Protected namespaces (write operations require additional approval):
  - kube-system
  - kube-public
  - kube-node-lease
  - monitoring
  - istio-system
  - cert-manager

Prohibited operations in any namespace:
  - default (production cluster should not use default)
```

### 4.3 Output De-sensitization Rules

```
# 🟢 Low Risk: Read-only/information gathering, typically with no side effects
Automatically anonymized content:

Secret type:
  kubectl get secret -o yaml → data field replaced with "***REDACTED***"
  kubectl get secret -o json → same

Environment variables:
  Values containing KEY/TOKEN/PASSWORD/SECRET/CREDENTIAL keywords → "***"

ConfigMap:
  Values containing connection strings, passwords, API Key → partial redaction (keep first 4 characters)
```
## 5. Tool Combinations Templates

### 5.1 Diagnostic Toolchain for Pod Pending

``` bash
# 🟢 Low Risk: Read-only/information gathering, typically with no side effects
# Step 1: Confirm status
kubectl get pod <pod> -n <ns> -o wide

# Step 2: Review events
kubectl describe pod <pod> -n <ns> | grep -A 20 "Events:"

# Step 3: Check node resources
kubectl top nodes
kubectl get nodes -o custom-columns=NAME:.metadata.name,CPU:.status.allocatable.cpu,MEM:.status.allocatable.memory

# Step 4: Check scheduling constraints
kubectl get pod <pod> -n <ns> -o jsonpath='{.spec.nodeSelector}'
kubectl get pod <pod> -n <ns> -o jsonpath='{.spec.affinity}'
```
### 5.2 Diagnostic Toolchain for Node NotReady

``` bash
# 🟢 Low-risk: Read-only/information gathering, usually no side effects
# Step 1: Confirm node status
kubectl get nodes -o wide
kubectl describe node <node> | grep -A 10 "Conditions:"

# Step 2: Check kubelet
kubectl get --raw /api/v1/nodes/<node>/proxy/healthz

# Step 3: Check resource pressure
kubectl top node <node>
kubectl describe node <node> | grep -A 5 "Allocated resources:"

# Step 4: View node events
kubectl get events --field-selector involvedObject.name=<node> --sort-by=.lastTimestamp
```
### 5.3 Diagnostic Toolchain for OOM

``` bash
# 🟢 Low-risk: Read-only/information gathering, usually no side effects
# Step 1: Confirm OOM
kubectl describe pod <pod> -n <ns> | grep -A 5 "Last State:"
kubectl get events -n <ns> --field-selector reason=OOMKilling

# Step 2: View resource configuration
kubectl get pod <pod> -n <ns> -o jsonpath='{.spec.containers[*].resources}'

# Step 3: View actual usage
kubectl top pod <pod> -n <ns> --containers

# Step 4: View historical trends (Prometheus)
# sum(container_memory_working_set_bytes{namespace="<ns>", pod="<pod>"}) by (container)
```
## 6. MCP Tool Integration

### 6.1 MCP Server Configuration

```yaml
# Remote tools that can be integrated via MCP protocol
mcp_servers:
  - name: kubectl-mcp
    transport: stdio
    command: kubectl-mcp-server
    capabilities:
      - kubectl_get
      - kubectl_describe
      - kubectl_logs

  - name: prometheus-mcp
    transport: streamable_http
    url: http://prometheus-mcp:8080/mcp
    capabilities:
      - prometheus_query
      - prometheus_query_range

  - name: loki-mcp
    transport: streamable_http
    url: http://loki-mcp:8080/mcp
    capabilities:
      - loki_search
```

### 6.2 AGENTScope Toolkit Registration Example

```python
from agentscope.tool import Toolkit, execute_shell_command, view_text_file

toolkit = Toolkit()

# Base tools
toolkit.register_tool_function(execute_shell_command)
toolkit.register_tool_function(view_text_file)

# MCP remote tools
# await toolkit.register_mcp_client(kubectl_mcp_client)
# await toolkit.register_mcp_client(prometheus_mcp_client)

# Agent Skill(Domain knowledge)
toolkit.register_agent_skill("openclaw-workspace")
```

---

*This document defines the scope of tool authorization for Agents. Adding new tools requires security review, and deleting tools requires assessing the impact range.*

## Related

- 29-agentscope-studio-skill-demo
- [[log|log]]
- [[domain-17-system-foundation/topic-cheat-sheet/go.md|go]]
- [[domain-17-system-foundation/topic-cheat-sheet/helm.md|helm]]

## See Also

- SKILL
- SOUL
- USER
- AGENTS

```

<!-- risk-assessed -->
