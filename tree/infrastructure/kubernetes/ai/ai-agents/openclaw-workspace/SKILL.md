---
title: K8S Maintenance Diagnostic Skill Library (02-ai-agents)
description: 'title: K8S Maintenance Diagnostic Skill Library'
summary: 'title: K8S Maintenance Diagnostic Skill Library'
category: general
tags:
- ai
- ai-agent
- daily-ops
- etcd
- apiserver
- kubelet
- prometheus
- coredns
- containerd
- docker
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 15min
intent_queries:
- K8S Maintenance Diagnostic Skill Library is what
- How is K8S Maintenance Diagnostic Skill Library
- Kubernetes 14 AI ML Infra Best Practices
trigger_keywords:
- K8S
- Maintenance Diagnostic Skill Library
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- prometheus-basics
- etcd-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/openclaw-workspace/SKILL.md
---

> **Production Environment Security Tips**
>
> This document contains executable maintenance commands. Execute them only after confirming: the target cluster and Namespace are correct; you have sufficient RBAC permissions; and they have been validated in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information collection, no side effects).




title: K8S Maintenance Diagnostic Skill Library
description: [[Kubernetes|Kubernetes]] Maintenance Diagnostic Full Stack Skill Library covering the structured faults of Pod/Node/Network/Storage/Performance five fault domains.
  SOP
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
- coredns
last_updated: 2026-04
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Architects
- SRE
estimated_read_time: 5min
intent_queries:
- K8S Maintenance Diagnostic Skill Library is what
- How is K8S Maintenance Diagnostic Skill Library
trigger_keywords:
- K8S
- Maintenance Diagnostic Skill Library
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
# K8S Maintenance Diagnostic Skill Library

## 1. Skill Coverage Scope

```
技能域全景:

├── Pod 故障域
│   ├── Pending（调度失败）
│   ├── CrashLoopBackOff（崩溃循环）
│   ├── OOMKilled（内存溢出）
│   ├── ImagePullBackOff（镜像拉取失败）
│   ├── Error / Unknown（其他异常）
│   └── Evicted（被驱逐）
│
├── Node 故障域
│   ├── NotReady（节点不就绪）
│   ├── MemoryPressure / DiskPressure / PIDPressure
│   ├── NetworkUnavailable
│   └── SchedulingDisabled
│
├── Network 故障域
│   ├── Service 不通
│   ├── DNS 解析失败
│   ├── Pod 间通信异常
│   ├── Ingress 不可达
│   └── NetworkPolicy 拦截
│
├── Storage 故障域
│   ├── PVC Pending
│   ├── 挂载失败
│   └── CSI 驱动异常
│
└── Performance 故障域
    ├── API Server 延迟高
    ├── etcd 延迟高
    ├── 调度延迟
    └── 网络延迟
```

## 2. Pod Fault Diagnosis SOP

### 2.1 Pod Pending

**Trigger Conditions**: Pod status is Pending for more than 30 seconds

``` bash
# 🟢 Low Risk: Read-only/Information Gathering, Usually No Side Effects
# Step 1: Confirm Status
kubectl get pod <pod> -n <ns> -o wide

# Step 2: Check Events (Critical! Events contain scheduling failure reasons)
kubectl describe pod <pod> -n <ns> | tail -20
kubectl get events -n <ns> --field-selector involvedObject.name=<pod> --sort-by=.lastTimestamp

# Step 3: Diagnose based on events
```
| Event Keyword | Root Cause | Repair Direction |
|-----------|------|---------|
| `Insufficient cpu/memory` | Insufficient node resources | Scale up nodes / Adjust requests |
| `node(s) didn't match selector` | NodeSelector does not match | Check labels / Modify selector |
| `node(s) had taint` | Taint/Toleration does not match | Add Toleration / Remove Taint |
| `persistentvolumeclaim not found` | PVC not bound | Check PVC status and StorageClass |
| `Unschedulable` | Node unschedulable | Check SchedulingDisabled on node |
| `pod has unbound immediate PVC` | Immediate PVC binding not ready | Wait for PVC Ready or check PV |

### 2.2 CrashLoopBackOff

**Trigger Conditions**: Pod status is CrashLoopBackOff

``` bash
# 🟢 Low Risk: Read-only/Information Gathering, Usually No Side Effects
# Step 1: Check last log (Critical! )
kubectl logs <pod> -n <ns> --previous --tail=100

# Step 2: Check container exit code
kubectl get pod <pod> -n <ns> -o jsonpath='{.status.containerStatuses[*].lastState.terminated.exitCode}'

# Step 3: Check probe configuration
kubectl get pod <pod> -n <ns> -o jsonpath='{.spec.containers[*].livenessProbe}'
```
| Exit Code | Meaning | Common Causes |
|--------|------|---------|
| 0 | Normal exit | Application actively exits, check restartPolicy |
| 1 | Application error | Code anomaly, configuration error, unreachable dependencies |
| 137 | SIGKILL (OOM) | Memory limit exceeded, terminated by cgroup OOM Killer |
| 139 | SIGSEGV | Segmentation fault, application bug |
| 143 | SIGTERM | Terminated by K8S (e.g., preStop hook timeout) |

### 2.3 OOMKilled

**Trigger Conditions**: Pod terminated due to OOM

``` bash
# 🟢 Low Risk: Read-only/Information gathering, usually with no side effects
# Step 1: Confirm OOM
kubectl describe pod <pod> -n <ns> | grep -A 5 "Last State:"
kubectl get events -n <ns> --field-selector reason=OOMKilling

# Step 2: Compare limits vs actual usage
kubectl get pod <pod> -n <ns> -o jsonpath='{.spec.containers[*].resources}'
kubectl top pod <pod> -n <ns> --containers

# Step 3: Analyze memory trend (Prometheus)
# sum(container_memory_working_set_bytes{namespace="<ns>",pod="<pod>"}) by (container)
```
**Decision Tree for Fixes**:
```
实际使用 > limits?
  ├── 是 → limits 设置过低
  │   ├── 调整 limits（推荐为实际峰值的 1.5 倍）
  │   └── 同步调整 requests（推荐为实际均值的 1.2 倍）
  └── 否 → 应用内存泄漏
      ├── 分析内存增长趋势
      ├── 检查 JVM heap / Go GC / Python 内存管理
      └── 建议应用团队排查内存泄漏
```

### 2.4 ImagePullBackOff

``` bash
# 🟢 Low Risk: Read-only/Information gathering, usually with no side effects
# Step 1: Check image name and tag
kubectl get pod <pod> -n <ns> -o jsonpath='{.spec.containers[*].image}'

# Step 2: Check imagePullSecrets
kubectl get pod <pod> -n <ns> -o jsonpath='{.spec.imagePullSecrets}'
kubectl get secret <secret> -n <ns> -o jsonpath='{.type}'

# Step 3: Check detailed errors in events
kubectl describe pod <pod> -n <ns> | grep -A 5 "Failed"
```
| Error Message | Root Cause | Fix |
|---------|------|------|
| `repository does not exist` | Incorrect image name | Verify image address |
| `unauthorized` | Authentication failure | Check if imagePullSecret is correct |
| `manifest unknown` | Tag does not exist | Verify if the tag has been pushed |
| `timeout` | Network issues | Check network connectivity between node and Registry |

## 3. Node Fault Diagnosis SOP

### 3.1 Node NotReady

``` bash
# 🟢 Low Risk: Read-only/Information gathering, usually with no side effects
# Step 1: confirm status and Conditions
kubectl get nodes -o wide
kubectl get node <node> -o jsonpath='{.status.conditions}' | python3 -m json.tool

# Step 2: check kubelet
kubectl get --raw /api/v1/nodes/<node>/proxy/healthz 2>/dev/null || echo "kubelet 不可达"

# Step 3: check node events
kubectl get events --field-selector involvedObject.name=<node> --sort-by=.lastTimestamp

# Step 4: resource pressure check
kubectl top node <node>
kubectl describe node <node> | grep -A 5 "Allocated resources:"
```
**NotReady Root Cause Decision Tree**:
```
# 🟢 Low Risk: read-only/information gathering, usually no side effects
Node NotReady
├── kubelet 不响应
│   ├── kubelet 进程挂了 → 重启 kubelet
│   ├── 节点 SSH 不通 → 物理/VM 层面问题
│   └── 证书过期 → 更新 kubelet 证书
├── MemoryPressure = True
│   ├── 系统内存不足 → 清理内存 / 扩容
│   └── 单个 Pod 内存泄漏 → 定位并重启 Pod
├── DiskPressure = True
│   ├── 容器日志占满 → 清理日志
│   ├── 镜像缓存过多 → docker/containerd image prune
│   └── 数据卷满 → 扩容磁盘
└── NetworkUnavailable = True
    ├── CNI 插件异常 → 检查 CNI Pod 状态
    └── 网络配置错误 → 检查路由和 iptables
```
## 4. Network Fault Diagnosis SOP

### 4.1 Service Unavailable

``` bash
# 🟡 Medium Risk: modifies cluster/resource state, confirm target, impact scope, and authorization before execution
# Step 1: confirm Service and Endpoints
kubectl get svc <svc> -n <ns>
kubectl get endpoints <svc> -n <ns>

# Step 2: are Endpoints empty?
kubectl get pods -n <ns> -l <selector> --show-labels

# Step 3: DNS test
kubectl run dns-test --image=busybox:1.36 --rm -it --restart=Never -- nslookup <svc>.<ns>.svc.cluster.local

# Step 4: connectivity test
kubectl run net-test --image=busybox:1.36 --rm -it --restart=Never -- wget -qO- --timeout=5 http://<svc>.<ns>:<port>

# Step 5: check NetworkPolicy
kubectl get networkpolicy -n <ns>
```
### 4.2 DNS fails to resolve

``` bash
# 🟡 Medium Risk: modifies cluster/resource state, confirm target, impact scope, and authorization before execution
# Step 1: CoreDNS status
kubectl get pods -n kube-system -l k8s-app=kube-dns
kubectl logs -n kube-system -l k8s-app=kube-dns --tail=50

# Step 2: CoreDNS configuration
kubectl get configmap coredns -n kube-system -o yaml

# Step 3: DNS test
kubectl run dns-debug --image=busybox:1.36 --rm -it --restart=Never -- nslookup kubernetes.default
```
## 5. Storage Fault Diagnosis SOP

### 5.1 PVC Pending

``` bash
# 🟢 Low Risk: Read-Only/Information Collection, Usually No Side Effects
# Step 1: Check PVC Status
kubectl get pvc -n <ns>
kubectl describe pvc <pvc> -n <ns>

# Step 2: Check StorageClass
kubectl get sc
kubectl describe sc <sc-name>

# Step 3: Check PV
kubectl get pv | grep <pvc>

# Step 4: Check CSI Driver Status
kubectl get pods -n kube-system -l app=csi-*
```
## 6. Performance Diagnosis SOP

### 6.1 High API Server Latency

``` bash
# 🟢 Low Risk: Read-Only/Information Collection, Usually No Side Effects
# Step 1: Confirm Latency
# histogram_quantile(0.99, sum(rate(apiserver_request_duration_seconds_bucket[5m])) by (le, verb))

# Step 2: Check Request Volume
# sum(rate(apiserver_request_total[5m])) by (verb, resource)

# Step 3: Check etcd Latency
# histogram_quantile(0.99, sum(rate(etcd_disk_wal_fsync_duration_seconds_bucket[5m])) by (le))

# Step 4: Check Audit Log Volume
kubectl logs -n kube-system -l component=kube-apiserver --tail=20
```
## 7. Output Format Template

All diagnostic results must be output in the following format:

```markdown
## Diagnostic Results

### 1. Phenomenon
[一句话描述异常状态]

### 2. Root Cause
[基于数据的根本原因分析，标注置信度]
- 置信度: 高/中/低
- 数据来源: [具体的命令或查询]

### 3. Repair Plan
[可直接执行的命令和步骤]
- 风险等级: 低/中/高
- 影响范围: [受影响的资源]
- 回滚方案: [回滚命令]

### 4. Verification Method
[修复后确认问题已解决的命令]

### 5. Prevention Suggestions
[避免再次发生的措施]
```

## 8. Knowledge Base Associations

| Fault Domain | kudig-database reference document |
|--------|------------------------|
| Pod Issues | `domain-10-troubleshooting-diagnostics/05-pod-pending-diagnosis.md` ~ `08-pod-comprehensive-troubleshooting.md` |
| Node Issues | `domain-10-troubleshooting-diagnostics/06-node-notready-diagnosis.md`, `09-node-comprehensive-troubleshooting.md` |
| Network Issues | `domain-10-troubleshooting-diagnostics/25-network-connectivity-troubleshooting.md`, `26-dns-troubleshooting.md` |
| Storage Issues | `domain-10-troubleshooting-diagnostics/14-pvc-storage-troubleshooting.md`, `04-storage-csi-troubleshooting.md` |
| Performance Issues | `domain-10-troubleshooting-diagnostics/33-performance-bottleneck-troubleshooting.md` |
| Fault Tree | `domain-10-troubleshooting-diagnostics/topic-fta/` complete fault tree analysis model |

---

*This section defines the knowledge and operational procedures for the Agent within its domain. Update the SOP to synchronize updates to the corresponding document in kudig-database when necessary.*

## Related

- 29-agentscope-studio-skill-demo
- [[domain-17-system-foundation/topic-cheat-sheet/go.md|go]]
- [[domain-17-system-foundation/topic-cheat-sheet/k8s.md|k8s]]
- [[entities/kubernetes.md|kubernetes]]
- [[entities/coredns.md|coredns]]

- 48-openclaw-skill-mechanism
- [[domain-19-landscape-references/topic-index/etcd-index.md|etcd Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/node-index.md|Node Knowledge Graph Index]]

## See Also

- IDENTITY
- MEMORY
- SOUL
- TOOLS


<!-- risk-assessed -->
