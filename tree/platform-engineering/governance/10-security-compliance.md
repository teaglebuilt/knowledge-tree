---
title: 55 - Virtual Clusters and Multi-tenancy
description: '| Mode | Isolation Level | Resource Efficiency | Management Complexity | Applicable Scenarios |'
summary: '| Mode | Isolation Level | Resource Efficiency | Management Complexity | Applicable Scenarios |'
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- etcd
- apiserver
- scheduler
- controller-manager
- helm
- opa
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Platform Engineers
- Operations Engineers
estimated_read_time: 5min
intent_queries:
- What is Virtual Clusters and Multi-tenancy
- How to use Virtual Clusters and Multi-tenancy
- Kubernetes 9 platform ops best practices
trigger_keywords:
- Virtual Clusters and Multi-tenancy
- platform
- ops
prerequisites:
- kubectl-basics
- platform-engineering-basics
- helm-basics
- etcd-basics
- policy-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: KUDIG Team
  role: contributor
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
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./operate/25-virtual-clusters.md
original_language: Chinese
---

> **Production Environment Security Tips**
>
> This document contains operations commands that can be executed directly. Before execution, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have verified in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state, but usually reversible), 🟢 Low risk/read-only (information gathering, no side effects).




# 55 - Virtual Clusters and Multi-tenancy

<!-- chunk: Multi-tenant isolation modes -->
## Multi-tenant Isolation Modes

| Mode | Isolation Level | Resource Efficiency | Management Complexity | Applicable Scenarios |
|-----|---------|---------|-----------|---------|
| Namespace | Soft Isolation | High | Low | Team Isolation |
| Virtual Cluster | Strong Isolation | Medium | Medium | Multi-tenant Platform |
| Physical Cluster | Complete Isolation | Low | High | Security Sensitive |

<!-- chunk: Virtual Cluster Tools Comparison -->
## Virtual Cluster Tools Comparison

| Tool | Architecture | API Compatibility | Maturity | Community |
|-----|------|---------|-------|------|
| vCluster | Embedded Control Plane | Complete | ⭐⭐⭐⭐⭐ | Active |
| Kamaji | External Control Plane | Complete | ⭐⭐⭐⭐ | Active |
| Cluster API | Independent Cluster | Complete | ⭐⭐⭐⭐⭐ | CNCF |
| Hierarchical Namespaces | Namespace Hierarchy | Partial | ⭐⭐⭐ | K8s SIG |

<!-- chunk: vCluster Architecture -->
## vCluster Architecture

| Component | Location | Function |
|-----|------|------|
| syncer | Virtual Cluster Pod | Resource Synchronization |
| kube-apiserver | Virtual Cluster Pod | API Server |
| [[etcd|etcd]]/SQLite | Virtual Cluster Pod | Data Storage |
| kube-controller-manager | Virtual Cluster Pod | Controller Management |
| kube-scheduler | Optional | Scheduler |

<!-- chunk: vCluster Installation -->
## vCluster Installation

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, it is recommended to use --dry-run or diff to confirm first
> - `helm upgrade/install`: Deploy/upgrade release

``` bash
# 🟡 Medium risk: modifies cluster/resource state, please confirm target, impact scope and authorization before execution
# Install vCluster CLI
curl -L -o vcluster "https://github.com/loft-sh/vcluster/releases/latest/download/vcluster-linux-amd64"
chmod +x vcluster
sudo mv vcluster /usr/local/bin

# Create virtual cluster
vcluster create my-vcluster -n host-namespace

# Connect to virtual cluster
vcluster connect my-vcluster -n host-namespace

# Install using Helm
helm upgrade --install my-vcluster vcluster \
  --repo https://charts.loft.sh \
  --namespace host-namespace \
  --create-namespace
```
<!-- chunk: vCluster Configuration -->
## vCluster Configuration

```yaml
# values.yaml
sync:
  # Resource types to synchronize
  pods:
    enabled: true
  services:
    enabled: true
  configmaps:
    enabled: true
  secrets:
    enabled: true
  persistentvolumeclaims:
    enabled: true
  ingresses:
    enabled: true
  
# Control plane configuration
controlPlane:
  distro:
    k8s:
      enabled: true
  statefulSet:
    resources:
      limits:
        cpu: "1"
        memory: 2Gi
      requests:
        cpu: 200m
        memory: 256Mi
    persistence:
      size: 5Gi

# Synchronization options
sync:
  toHost:
    pods:
      enabled: true
    services:
      enabled: true
  fromHost:
    nodes:
      enabled: true
    
# Isolation configuration
isolation:
  enabled: true
  resourceQuota:
    enabled: true
  limitRange:
    enabled: true
  networkPolicy:
    enabled: true
```

<!-- chunk: Hierarchical Namespaces (HNC) -->
## Hierarchical Namespaces (HNC)

```yaml
# Install HNC
kubectl apply -f https://github.com/kubernetes-sigs/hierarchical-namespaces/releases/latest/download/default.yaml

# Create parent namespace
apiVersion: v1
kind: Namespace
metadata:
  name: org-team-a

# Create sub-namespace
apiVersion: hnc.x-k8s.io/v1alpha2
kind: SubnamespaceAnchor
metadata:
  name: dev
  namespace: org-team-a
---
apiVersion: hnc.x-k8s.io/v1alpha2
kind: SubnamespaceAnchor
metadata:
  name: staging
  namespace: org-team-a
```

<!-- chunk: HNC Resource Inheritance -->
## HNC Resource Inheritance

```yaml
# Create resource in parent namespace (automatically propagated to child namespaces)
apiVersion: v1
kind: ConfigMap
metadata:
  name: team-config
  namespace: org-team-a
  labels:
    hnc.x-k8s.io/inherited-from: org-team-a
data:
  team: team-a
  
# Configure propagation rules
apiVersion: hnc.x-k8s.io/v1alpha2
kind: HNCConfiguration
metadata:
  name: config
spec:
  resources:
  - resource: secrets
    mode: Propagate  # Propagate/Remove/Ignore
  - resource: roles
    mode: Propagate
  - resource: rolebindings
    mode: Propagate
  - resource: networkpolicies
    mode: Propagate
```

<!-- chunk: Multi-tenant RBAC Policy -->
## Multi-tenant RBAC Policy

```yaml
# Tenant administrator role
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: tenant-admin
rules:
- apiGroups: [""]
  resources: ["namespaces"]
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources: ["pods", "services", "configmaps", "secrets"]
  verbs: ["*"]
- apiGroups: ["apps"]
  resources: ["deployments", "statefulsets", "daemonsets"]
  verbs: ["*"]
- apiGroups: ["networking.k8s.io"]
  resources: ["networkpolicies", "ingresses"]
  verbs: ["*"]
---
# Tenant RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: tenant-admin-binding
  namespace: tenant-a
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: tenant-admin
subjects:
- kind: Group
  name: tenant-a-admins
  apiGroup: rbac.authorization.k8s.io
```

<!-- chunk: Tenant Isolation NetworkPolicy -->
## Tenant Isolation NetworkPolicy

```yaml
# Deny all traffic by default
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: tenant-a
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
---
# Allow same namespace communication
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-same-namespace
  namespace: tenant-a
spec:
  podSelector: {}
  ingress:
  - from:
    - podSelector: {}
  egress:
  - to:
    - podSelector: {}
```

<!-- chunk: Tenant ResourceQuota -->
## Tenant ResourceQuota

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: tenant-quota
  namespace: tenant-a
spec:
  hard:
    requests.cpu: "20"
    requests.memory: 40Gi
    limits.cpu: "40"
    limits.memory: 80Gi
    pods: "100"
    services: "20"
    secrets: "100"
    configmaps: "100"
    persistentvolumeclaims: "20"
    requests.storage: 100Gi
```

<!-- chunk: ACK Multi-tenant Solution -->
## ACK Multi-tenant Solution

| Function | Description |
|-----|------|
| ACK One | Unified Multi-cluster Management |
| Elastic Quota | Tenant Resource Sharing |
| Namespace Quota | Resource Limits |
| Network Isolation | Terway NetworkPolicy |
| Log Isolation | SLS Log Isolation |

<!-- chunk: Version Change Log -->
## Version Change Log

| Version | Change Content |
|------|---------|
| v1.25 | PSA replaces PSP for tenant security |
| v1.27 | Resource quota improvements |
| v1.28 | CEL admission policy enhancements |
| v1.30 | ValidatingAdmissionPolicy GA |

---

**Table Bottom Mark**: Kusheet Project, Author Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian Related Documentation -->
## Obsidian Related Documentation

- domain-07-platform-engineering KUDIG Database — Global MOC
- [[domain-07-platform-engineering/README.md|[[Platform Ops Domain|Platform Ops Domain]]]]
- Domain-9 Platform Operations — Open Source Project Index
- Platform Operations Overview
- Cluster Lifecycle Management
- Capacity Planning and Resource Assessment
- Performance Benchmarking and Tuning
- Operations Metrics System Building
- Monitoring and Alerting System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization and FinOps Practices

## See Also

- 23-cli-enhancement-tools
- 24-addons-extensions
- 26-kubectl-plugin-ecosystem
- 99-java-k8s-client-operator-guide

## Related

- [[domain-19-landscape-references/topic-index/cluster-index.md|Cluster Knowledge Map Index]]

```

<!-- risk-assessed -->