---
title: Kubernetes v1.29-v1.33 Platform Operations New Features Guide
description: 'title: Kubernetes v1.29-v1.33 Platform Operations New Features Guide'
summary: 'title: Kubernetes v1.29-v1.33 Platform Operations New Features Guide'
category: general
tags:
- k8s
- devops
- daily-ops
- guide
- etcd
- apiserver
- kubelet
- scheduler
- controller-manager
- prometheus
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 15min
intent_queries:
- What is Kubernetes?
- How to use Kubernetes?
- What are the best practices for Kubernetes?
trigger_keywords:
- Kubernetes
- v1.29-v1.33
- Platform Operations New Features Guide
- platform
- engineering
prerequisites:
- kubectl-basics
- platform-engineering-basics
- prometheus-basics
- etcd-basics
- gpu-scheduling-basics
- observability-basics
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./operate/99-kubernetes-v1.33-platform-ops-guide.md
original_language: Chinese
---

> **Production Environment Security Notice**
>
> This document contains directly executable operations commands. Before execution, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have verified it in a non-production environment. Command risk levels are marked: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (modifies cluster state but usually can be rolled back), 🟢 Low Risk/Read-Only (information gathering with no side effects).




title: [[Kubernetes|Kubernetes]] v1.29-v1.33 Platform Operations New Features Guide
description: '# Kubernetes v1.29-v1.33 Platform Operations New Features Guide'
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- [[etcd|etcd]]
- apiserver
- [[kubelet|kubelet]]
- scheduler
- controller-manager
- [[Prometheus|prometheus]]
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Platform Engineers
- Operations Engineers
estimated_read_time: 5min
intent_queries:
- What is Kubernetes v1.29-v1.33 Platform Operations New Features Guide
- How to Kubernetes v1.29-v1.33 Platform Operations New Features Guide
- Kubernetes 9 platform ops best practices
trigger_keywords:
- Kubernetes
- v1.29-v1.33
- Platform Operations New Features Guide
- platform
- ops
cross_refs:
- type: domain
  path: ../domain-06-observability/
  label: 'Related Knowledge Domain: domain-06-observability'
- type: domain
  path: ../domain-15-specialized-tech/
  label: 'Related Knowledge Domain: domain-15-specialized-tech'
- type: domain
  path: ../domain-10-troubleshooting-diagnostics/
  label: 'Related Knowledge Domain: domain-10-troubleshooting-diagnostics'
authors:
- name: KUDIG Team
  role: contributor
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
---

# Kubernetes v1.29-v1.33 Platform Operations New Features Guide

> **Applicable Versions**: Kubernetes v1.29 - v1.33  
> **Last Updated**: 2026-04-24  
> **Purpose**: Detailed explanation of platform operations new features and production practices

---

<!-- chunk: 📋 Table of Contents -->
## 📋 Table of Contents

- [1. Version Upgrade Strategy and Tools](#1-version-upgrade-strategy-and-tools)
- [2. Scheduler Queueing Hints (v1.33 Beta)](#2-scheduler-queueing-hints-v133-beta)
- [3. Coordinated Leader Election (v1.32 Alpha)](#3-coordinated-leader-election-v132-alpha)
- [4. Cluster Autoscaling New Features](#4-cluster-autoscaling-new-features)
- [5. Multi-tenant Management Enhancements](#5-multi-tenant-management-enhancements)
- [6. Node Operations New Tools](#6-node-operations-new-tools)
- [7. Platform Operations Checklist](#7-platform-operations-checklist)

---

<!-- chunk: 1. Version Upgrade Strategy and Tools -->
## 1. Version Upgrade Strategy and Tools

### 1.1 v1.33 Upgrade Path

```
Recommended upgrade path:
v1.29 → v1.30 → v1.31 → v1.32 → v1.33

Key milestones:
├── v1.30: ValidatingAdmissionPolicy GA, BoundServiceAccountToken GA
├── v1.31: AppArmor GA, Gateway API v1.1, OpenTelemetry Tracing GA
├── v1.32: Job Pod Replacement Policy, Pod Failure Policy enhancements
└── v1.33: Sidecar GA, DRA GA, nftables Beta, Queueing Hints Beta
```

### 1.2 Pre-Upgrade Check Script

``` bash
# 🟢 Low Risk: Read-only/information gathering, usually no side effects
#!/bin/bash
# pre-upgrade-check.sh
# Complete pre-upgrade check for v1.33

VERSION="1.33"
NODE_NAME=$(kubectl get nodes -o jsonpath='{.items[0].metadata.name}')

echo "=== K8s v${VERSION} Pre-Upgrade Check ==="

# 1. Current version
echo "[1] Current cluster version"
kubectl version -o json | jq '.serverVersion.gitVersion'

# 2. Deprecated API check
echo "[2] Deprecated API usage check"
kubectl get --raw /apis | jq -r '.groups[].name' | while read api; do
  kubectl get --raw /apis/$api 2>/dev/null | jq -r '.resources[].name' 2>/dev/null
done | sort | uniq

# 3. Feature Gate compatibility
echo "[3] Enabled Feature Gates"
kubectl get --raw /api/v1/nodes/$NODE_NAME/proxy/configz | jq '.kubeletconfig.featureGates'

# 4. etcd backup check
echo "[4] etcd Backup"
etcdctl snapshot status /backup/etcd-$(date +%Y%m%d).db 2>/dev/null || echo "Please perform etcd backup"

# 5. PodDisruptionBudget check
echo "[5] PDB Status"
kubectl get pdb --all-namespaces

# 6. Node health check
echo "[6] Node Status"
kubectl get nodes -o wide

echo "=== Check Complete ==="
```

### 1.3 kubeadm Upgrade Steps

> ⚠️ **🟠 High-Risk Operations** — Affects business traffic or node state, requires change ticket + impact assessment + rollback plan
> - `kubectl drain`: Evicts all Pods from a node, affecting business traffic
> - `systemctl stop/restart`: Stops/restarts system services, affecting all containers on the node

> **🔴 High-Risk Operation Warning**
>
> The following commands are irreversible or high-impact operations. Before execution, please confirm:
> - Critical data and configurations have been backed up
> - Within an approved change window period
> - Authorized by relevant responsible parties
> - Rollback or recovery plan has been prepared
> - Target cluster, namespace, node/resource names are correct and without errors

``` bash
# 🔴 High Risk: May cause data loss or service disruption, requires backup, change approval and rollback plan before execution
# 1. Upgrade kubeadm
apt-mark unhold kubeadm && \
apt-get update && apt-get install -y kubeadm=1.33.0-1.1 && \
apt-mark hold kubeadm

# 2. Verify upgrade plan
kubeadm upgrade plan v1.33.0

# 3. Execute control plane upgrade
kubeadm upgrade apply v1.33.0 --etcd-upgrade=true

# 4. Upgrade kubelet and kubectl
apt-mark unhold kubelet kubectl && \
apt-get update && apt-get install -y kubelet=1.33.0-1.1 kubectl=1.33.0-1.1 && \
apt-mark hold kubelet kubectl

# 5. Restart kubelet
systemctl restart kubelet

# 6. Upgrade worker nodes (execute node by node)
kubectl drain node-2 --ignore-daemonsets --delete-emptydir-data
# Execute steps 1,4,5 above on node-2
kubectl uncordon node-2
```

---

<!-- chunk: 2. Scheduler Queueing Hints (v1.33 Beta) -->
## 2. Scheduler Queueing Hints (v1.33 Beta)

### 2.1 Core Concepts

QueueingHints optimizes the scheduler queue's event-driven mechanism, waking unschedulable Pods only when relevant resources change.

### 2.2 Performance Impact

```
Traditional scheduling queue (without QueueingHints):
├── 1000 unschedulable Pods
├── Any node event triggers all retries
├── Invalid scheduling attempts per second: 50,000+
└── Scheduler CPU utilization: 40%+

After enabling QueueingHints:
├── 1000 unschedulable Pods
├── Only relevant events trigger specific Pod retries
├── Invalid scheduling attempts per second: < 5,000
└── Scheduler CPU utilization: 15%
```

### 2.3 Enable Configuration

```yaml
# kube-scheduler enabled by default (v1.33 Beta)
# No additional configuration needed

# Verify enabled status
kubectl get pods -n kube-system -l component=kube-scheduler -o yaml | \
  grep -A 2 "feature-gates"
```

### 2.4 Monitoring Metrics

```yaml
# PrometheusRule: Scheduler performance alerts
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: scheduler-performance
spec:
  groups:
    - name: scheduler
      rules:
        - alert: SchedulerHighRetryRate
          expr: rate(scheduler_schedule_attempts_total{result="unschedulable"}[5m]) > 1000
          for: 10m
          labels:
            severity: warning
          annotations:
            summary: "Scheduler retry rate is too high, QueueingHints may not be enabled"
```

---

<!-- chunk: 3. Coordinated Leader Election (v1.32 Alpha) -->
## 3. Coordinated Leader Election (v1.32 Alpha)

### 3.1 Core Concepts

Allows multiple control plane components to share leader election strategies, reducing the number of etcd Lease objects.

### 3.2 Enable Configuration

```yaml
# kube-apiserver
# --feature-gates=CoordinatedLeaderElection=true
```

### 3.3 LeaseCandidate Configuration

```yaml
apiVersion: coordination.k8s.io/v1alpha1
kind: LeaseCandidate
metadata:
  name: kube-controller-manager
  namespace: kube-system
spec:
  leaseName: kube-controller-manager
  preferredStrategies:
    - OldestEmulationVersion
  binaryVersion: "1.33.0"
  emulationVersion: "1.33.0"
---
apiVersion: coordination.k8s.io/v1alpha1
kind: LeaseCandidate
metadata:
  name: kube-scheduler
  namespace: kube-system
spec:
  leaseName: kube-scheduler
  preferredStrategies:
    - OldestEmulationVersion
  binaryVersion: "1.33.0"
  emulationVersion: "1.33.0"
```

### 3.4 Verification

``` bash
# 🟢 Low Risk: Read-only/information gathering, usually no side effects
# Check reduction in Lease count
kubectl get leases -n kube-system | wc -l

# View coordinated election status
kubectl get leasecandidates -n kube-system

# View Lease details
kubectl get lease kube-controller-manager -n kube-system -o yaml
```

---

<!-- chunk: 4. Cluster Autoscaling New Features -->
## 4. Cluster Autoscaling New Features

### 4.1 Karpenter vs Cluster Autoscaler Comparison

| Feature | Cluster Autoscaler | Karpenter |
|:---|:---|:---|
| Scheduling Awareness | No | Yes |
| Node Configuration | Node Groups (Fixed) | NodePool (Dynamic) |
| Scale-up Speed | 30-60s | 10-20s |
| Multi-cloud Support | Partial | AWS/GCP/Azure |
| Consolidation | Scale-down Only | Scale-up + Scale-down + Replace |

### 4.2 Karpenter NodePool Configuration (v1.33 Compatible)

```yaml
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: default
spec:
  template:
    spec:
      requirements:
        - key: kubernetes.io/arch
          operator: In
          values: ["amd64", "arm64"]
        - key: kubernetes.io/os
          operator: In
          values: ["linux"]
        - key: karpenter.sh/capacity-type
          operator: In
          values: ["spot", "on-demand"]
      nodeClassRef:
        group: karpenter.k8s.aws
        kind: EC2NodeClass
        name: default
      expireAfter: 720h  # Auto-replace after 30 days
      terminationGracePeriod: 30m
  limits:
    cpu: 1000
    memory: 4000Gi
  disruption:
    consolidationPolicy: WhenEmpty
    consolidateAfter: 1m
```

### 4.3 Autoscaling Integration with DRA

```yaml
# GPU workload autoscaling using DRA
apiVersion: karpenter.sh/v1
kind: NodePool
metadata:
  name: gpu
spec:
  template:
    spec:
      requirements:
        - key: nvidia.com/gpu.present
          operator: In
          values: ["true"]
      taints:
        - key: nvidia.com/gpu
          value: "true"
          effect: NoSchedule
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gpu-training
spec:
  replicas: 2
  template:
    spec:
      tolerations:
        - key: nvidia.com/gpu
          operator: Exists
      containers:
        - name: trainer
          image: pytorch:v2.0
          resources:
            claims:
              - name: gpu
      resourceClaims:
        - name: gpu
          source:
            resourceClaimTemplateName: gpu-claim-template
```

---

<!-- chunk: 5. Multi-tenant Management Enhancements -->
## 5. Multi-tenant Management Enhancements

### 5.1 Pod Security Admission (Already GA)

```yaml
# Cluster-level PSA configuration
apiVersion: apiserver.config.k8s.io/v1
kind: AdmissionConfiguration
plugins:
  - name: PodSecurity
    configuration:
      apiVersion: pod-security.admission.config.k8s.io/v1
      kind: PodSecurityConfiguration
      defaults:
        enforce: "restricted"
        audit: "restricted"
        warn: "restricted"
      exemptions:
        usernames: []
        runtimeClasses: []
        namespaces: [kube-system, monitoring]
```

### 5.2 Resource Quotas and Limit Ranges

```yaml
# Namespace-level resource quotas
apiVersion: v1
kind: ResourceQuota
metadata:
  name: team-a-quota
  namespace: team-a
spec:
  hard:
    requests.cpu: "100"
    requests.memory: 500Gi
    limits.cpu: "200"
    limits.memory: 1000Gi
    pods: "100"
    services: "20"
---
# Limit ranges
apiVersion: v1
kind: LimitRange
metadata:
  name: team-a-limits
  namespace: team-a
spec:
  limits:
    - default:
        cpu: "1"
        memory: 2Gi
      defaultRequest:
        cpu: "200m"
        memory: 512Mi
      type: Container
```

### 5.3 Network Policy Templates

```yaml
# Default deny all ingress traffic
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-ingress
  namespace: team-a
spec:
  podSelector: {}
  policyTypes:
    - Ingress
---
# Allow same-namespace communication
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-same-namespace
  namespace: team-a
spec:
  podSelector: {}
  ingress:
    - from:
        - podSelector: {}
  policyTypes:
    - Ingress
```

---

<!-- chunk: 6. Node Operations New Tools -->
## 6. Node Operations New Tools

### 6.1 kubectl debug Enhancements

``` bash
# 🟢 Low Risk: Read-only/information gathering, usually no side effects
# Create temporary debug container
kubectl debug pod/myapp -it --image=nicolaka/netshoot --target=myapp

# Node-level debugging (no SSH required)
kubectl debug node/node-1 -it --image=nicolaka/netshoot

# Copy Pod for debugging (preserve environment)
kubectl debug pod/myapp -it --copy-to=myapp-debug --image=myapp:debug

# Debug with temporary container (no restart required)
kubectl debug pod/myapp --image=busybox --target=myapp
```

### 6.2 Node Troubleshooting Commands

``` bash
# 🟢 Low Risk: Read-only/information gathering, usually no side effects
# View node resource pressure
kubectl top node

# View node conditions
kubectl get nodes -o json | jq '.items[].status.conditions'

# Node log query (NodeLogQuery Alpha)
kubectl node-logs node-1 --query=kubelet --since=1h

# Node health check
kubectl get --raw /api/v1/nodes/node-1/proxy/healthz

# View Pod resource usage on the node
kubectl get --raw /api/v1/nodes/node-1/proxy/stats/summary
```

### 6.3 Graceful Node Maintenance

> ⚠️ **🟠 High-Risk Operations** — Affects business traffic or node state, requires change ticket + impact assessment + rollback plan
> - `kubectl cordon`: Mark node as unschedulable
> - `kubectl drain`: Evict all Pods from a node, affecting business traffic

> **🔴 High-Risk Operation Warning**
>
> The following commands are irreversible or high-impact operations. Before execution, please confirm:
> - Critical data and configurations have been backed up
> - Within an approved change window period
> - Authorized by relevant responsible parties
> - Rollback or recovery plan has been prepared
> - Target cluster, namespace, node/resource names are correct and without errors

``` bash
# 🔴 High Risk: May cause data loss or service disruption, requires backup, change approval and rollback plan before execution
# 1. Mark node as unschedulable
kubectl cordon node-1

# 2. Evict Pods from node (respects PDB)
kubectl drain node-1 --ignore-daemonsets --delete-emptydir-data --force

# 3. Perform maintenance operations
# ...

# 4. Resume node scheduling
kubectl uncordon node-1

# 5. Verify Pod rescheduling
kubectl get pods --all-namespaces -o wide | grep node-1
```

---

<!-- chunk: 7. Platform Operations Checklist -->
## 7. Platform Operations Checklist

### 7.1 Daily Check

``` bash
# 🟢 Low Risk: Read-only/information gathering, usually no side effects
#!/bin/bash
# daily-check.sh

echo "=== $(date) Daily Operations Check ==="

# 1. Node status
kubectl get nodes -o json | jq -r '
  .items[] | 
  select(.status.conditions[] | select(.type=="Ready" and .status!="True")) |
  .metadata.name'

# 2. Abnormal Pods
kubectl get pods --all-namespaces --field-selector=status.phase!=Running,status.phase!=Succeeded

# 3. Resource usage Top 10
kubectl top nodes --sort-by=cpu | head -11
kubectl top pods --all-namespaces --sort-by=cpu | head -11

# 4. Event alerts
kubectl get events --all-namespaces --field-selector=type=Warning --sort-by=.lastTimestamp | tail -20

# 5. PVC usage
kubectl get pvc --all-namespaces -o json | jq -r '
  .items[] |
  select(.status.capacity.storage) |
  "\(.metadata.namespace)/\(.metadata.name): \(.status.phase)"'

echo "=== Check Complete ==="
```

### 7.2 Weekly Check

> ⚠️ **🟡 Medium-Risk Changes** — Modifies cluster resource state, recommend using --dry-run or diff first
> - `kubectl exec`: Enter container to execute commands, may change container state

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, please confirm target, impact scope and authorization before execution
#!/bin/bash
# weekly-check.sh

echo "=== $(date) Weekly Operations Check ==="

# 1. Certificate expiration check
kubeadm certs check-expiration

# 2. etcd health check
kubectl exec -it etcd-control-plane -n kube-system -- etcdctl endpoint health

# 3. Image security scan
kubectl get pods --all-namespaces -o jsonpath='{range .items[*].spec.containers[*]}{.image}{"\n"}{end}' | sort | uniq | while read img; do
  trivy image --severity HIGH,CRITICAL "$img" 2>/dev/null | grep -E "Total|HIGH|CRITICAL"
done

# 4. Resource quota usage
kubectl get resourcequota --all-namespaces

# 5. Unused ConfigMaps/Secrets
kubectl get configmaps --all-namespaces -o json | jq '[.items[] | select(.metadata.ownerReferences == null)] | length'
kubectl get secrets --all-namespaces -o json | jq '[.items[] | select(.metadata.ownerReferences == null)] | length'

echo "=== Check Complete ==="
```

### 7.3 Feature Enable Status Overview

``` bash
# 🟢 Low Risk: Read-only/information gathering, usually no side effects
#!/bin/bash
# check-all-features.sh

echo "=== K8s v1.33 Feature Enable Status Overview ==="

NODE=$(kubectl get nodes -o jsonpath='{.items[0].metadata.name}')
CONFIGZ=$(kubectl get --raw /api/v1/nodes/$NODE/proxy/configz)

# GA Features (no need to check, enabled by default)
echo "✅ GA Features (v1.33):"
echo "  - SidecarContainers"
echo "  - DynamicResourceAllocation (requires explicit FG enablement)"
echo "  - UserNamespacesSupport (requires explicit FG enablement)"
echo "  - ValidatingAdmissionPolicy"
echo "  - AppArmor"
echo "  - KubeletTracing"

# Beta Features
echo ""
echo "🔵 Beta Features:"
echo "  - SchedulerQueueingHints: $(echo $CONFIGZ | jq '.kubeletconfig.featureGates.SchedulerQueueingHints // "Enabled by default"')"
echo "  - KubeletResourceMetrics: $(echo $CONFIGZ | jq '.kubeletconfig.featureGates.KubeletResourceMetrics // "Enabled by default"')"
echo "  - NFTablesProxyMode: $(echo $CONFIGZ | jq '.kubeletconfig.featureGates.NFTablesProxyMode // "Not configured"')"

# Alpha Features
echo ""
echo "🟡 Alpha Features (requires explicit enablement):"
echo "  - InPlacePodVerticalScaling: $(echo $CONFIGZ | jq '.kubeletconfig.featureGates.InPlacePodVerticalScaling // "Not enabled"')"
echo "  - NodeSwap: $(echo $CONFIGZ | jq '.kubeletconfig.featureGates.NodeSwap // "Not enabled"')"
echo "  - NodeLogQuery: $(echo $CONFIGZ | jq '.kubeletconfig.featureGates.NodeLogQuery // "Not enabled"')"
echo "  - VolumeAttributesClass: $(echo $CONFIGZ | jq '.kubeletconfig.featureGates.VolumeAttributesClass // "Not enabled"')"
echo "  - SELinuxMount: $(echo $CONFIGZ | jq '.kubeletconfig.featureGates.SELinuxMount // "Not enabled"')"

echo ""
echo "=== Check Complete ==="
```

---

<!-- chunk: References -->
## References

- [Kubernetes Upgrade Guide](https://kubernetes.io/docs/tasks/administer-cluster/kubeadm/kubeadm-upgrade/)
- [Karpenter Documentation](https://karpenter.sh/docs/)
- [Queueing Hints KEP](https://github.com/kubernetes/enhancements/tree/master/keps/sig-scheduling/4247-queueing-hint)
- [Coordinated Leader Election KEP](https://github.com/kubernetes/enhancements/tree/master/keps/sig-api-machinery/4355-coordinated-leader-election)

---

<!-- chunk: Obsidian Related Documents -->
## Obsidian Related Documents

- domain-07-platform-engineering MOC
- [[domain-07-platform-engineering/README.md|Platform Ops Domain (Platform Operations Domain)]]
- Domain-9 Platform Operations — Open Source Projects Index
- Platform Operations Overview
- Cluster Lifecycle Management
- Capacity Planning & Resource Assessment
- Performance Benchmarking & Tuning
- Operations Metrics System
- Monitoring and Alerting System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization & FinOps

## Related

- 12-demo-env-guide
- 21-platform-selection-guide

## See Also

- 26-kubectl-plugin-ecosystem
- 99-java-k8s-client-operator-guide
- 01-platform-ops-overview
- 02-cluster-lifecycle-management

```

<!-- risk-assessed -->