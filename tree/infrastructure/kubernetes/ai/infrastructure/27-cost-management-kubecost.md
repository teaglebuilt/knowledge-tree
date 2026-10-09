---
title: Cost Management and FinOps
description: 'title: Cost Management and FinOps'
summary: 'title: Cost Management and FinOps'
category: general
tags:
- k8s
- ai
- gpu
- deep-dive
- cost-optimization
- prometheus
- helm
- vpa
- daemonset
- job
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 35min
intent_queries:
- What is cost-management-kubecost?
- How to use cost-management-kubecost
- Best practices for cost-management-kubecost
trigger_keywords:
- Cost Management and
- FinOps
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- helm-basics
- prometheus-basics
- iac-basics
- gpu-scheduling-basics
- policy-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/27-cost-management-kubecost.md
---

> **Production Environment Security Reminders**
>
> This document contains executable operational commands. Please confirm before execution: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the command has been validated in a non-production environment. Command risk levels are annotated: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually can be rolled back), 🟢 Low Risk/Read-Only (information gathering with no side effects).




title: cost management and FinOps
description: '# cost management and FinOps'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- [[Prometheus|prometheus]]
- [[Helm|helm]]
- vpa
- [[DaemonSet|daemonset]]
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- MLOps Engineer
- SRE
estimated_read_time: 5min
intent_queries:
- What is cost management and FinOps
- How to do cost management and FinOps
- [[Kubernetes|Kubernetes]] 11 ai infra best practices
trigger_keywords:
- cost management and
- FinOps
- ai
- infra
cross_refs:
- type: domain
  path: ../domain-02-workloads-applications/
  label: 'Related Knowledge Domains: domain-02-workloads-applications'
- type: domain
  path: ../domain-03-networking-traffic/
  label: 'Related Knowledge Domains: domain-03-networking-traffic'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
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

# Cost Management and FinOps


## Overview

Kubernetes cost management is a critical practice for ensuring the economic efficiency of cloud-native infrastructure. This document provides detailed information on cost analysis, deployment of monitoring tools, optimization strategies, and the maturity model of FinOps.


## Cost Architecture

### Kubernetes Cost Composition Model

```
# 🟢 Low Risk: read-only/information gathering, typically with no side effects
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           Kubernetes cost model architecture                                    │
│                                                                                      │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │                          Total Cost of Ownership (TCO)                    │   │
│   │                                                                              │   │
│   │   ┌─────────────────────────────────────────────────────────────────────┐   │   │
│   │   │                      Compute Cost (50-70%)                               │   │   │
│   │   │                                                                      │   │   │
│   │   │   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐               │   │   │
│   │   │   │   CPU cost   │   │   Memory cost  │   │   GPU cost  │               │   │   │
│   │   │   │             │   │             │   │             │               │   │   │
│   │   │   │ • On-Demand instance  │   │ • On-Demand instance  │   │ • Training tasks  │               │   │   │
│   │   │   │ • Reserved instance  │   │ • High-memory type  │   │ • Inference service  │               │   │   │
│   │   │   │ • Spot instance  │   │             │   │ • Spot GPU  │               │   │   │
│   │   │   └─────────────┘   └─────────────┘   └─────────────┘               │   │   │
│   │   │                                                                      │   │   │
│   │   └──────────────────────────────────────────────────────────────────────┘   │   │
│   │                                                                              │   │
│   │   ┌────────────────────────┐   ┌────────────────────────┐                   │   │
│   │   │     Storage Cost (15-25%)   │   │     Network Cost (10-20%)   │                   │   │
│   │   │                        │   │                        │                   │   │
│   │   │  • Block storage (EBS/Disk)   │   │  • Traffic across AZs          │                   │   │
│   │   │  • File storage (EFS/NFS)  │   │  • Traffic across regions          │                   │   │
│   │   │  • Object storage (S3)       │   │  • Internet gateway traffic          │                   │   │
│   │   │  • Snapshots and backups          │   │  • Load balancers            │                   │   │
│   │   └────────────────────────┘   └────────────────────────┘                   │   │
│   │                                                                              │   │
│   │   ┌────────────────────────┐   ┌────────────────────────┐                   │   │
│   │   │     Management Cost (5-10%)    │   │     Other Costs (5-10%)    │                   │   │
│   │   │                        │   │                        │                   │   │
│   │   │  • Control plane (managed)     │   │  • Log storage            │                   │   │
│   │   │  • Monitoring/observability       │   │  • Security tools            │                   │   │
│   │   │  • Service mesh            │   │  • CI/CD pipelines            │                   │   │
│   │   │  • Backup/DR             │   │  • Development environment            │                   │   │
│   │   └────────────────────────┘   └────────────────────────┘                   │   │
│   │                                                                              │   │
│   └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘
```
### Cost Allocation Model

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              Cost Allocation Architecture                                            │
│                                                                                      │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │                          Organization Level (Organization)                             │   │
│   │                                                                              │   │
│   │   ┌──────────────────────────────────────────────────────────────────────┐  │   │
│   │   │                          Company Level (Company)                               │  │   │
│   │   │                                                                       │  │   │
│   │   │   ┌─────────────────────────────────────────────────────────────┐    │  │   │
│   │   │   │                     Department                        │    │  │   │
│   │   │   │                                                              │    │  │   │
│   │   │   │   ┌────────────────────────────────────────────────────┐    │    │  │   │
│   │   │   │   │                  Team                        │    │    │  │   │
│   │   │   │   │                                                     │    │    │  │   │
│   │   │   │   │   ┌───────────────────────────────────────────┐    │    │    │  │   │
│   │   │   │   │   │              Project                │    │    │    │  │   │
│   │   │   │   │   │                                            │    │    │    │  │   │
│   │   │   │   │   │   ┌────────────────────────────────────┐  │    │    │    │  │   │
│   │   │   │   │   │   │         Environment          │  │    │    │    │  │   │
│   │   │   │   │   │   │   prod | staging | dev | test      │  │    │    │    │  │   │
│   │   │   │   │   │   └────────────────────────────────────┘  │    │    │    │  │   │
│   │   │   │   │   │                                            │    │    │    │  │   │
│   │   │   │   │   └───────────────────────────────────────────┘    │    │    │  │   │
│   │   │   │   │                                                     │    │    │  │   │
│   │   │   │   └────────────────────────────────────────────────────┘    │    │  │   │
│   │   │   │                                                              │    │  │   │
│   │   │   └─────────────────────────────────────────────────────────────┘    │  │   │
│   │   │                                                                       │  │   │
│   │   └──────────────────────────────────────────────────────────────────────┘  │   │
│   │                                                                              │   │
│   └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │                          Kubernetes Layer                                     │   │
│   │                                                                              │   │
│   │   Cluster ──► Namespace ──► Deployment ──► Pod ──► Container               │   │
│   │      │            │              │           │          │                   │   │
│   │      │            │              │           │          │                   │   │
│   │   labels:      labels:       labels:     labels:    resources:             │   │
│   │   • env        • team        • app       • version  • requests             │   │
│   │   • region     • project     • component             • limits              │   │
│   │   • cost-center• owner                                                      │   │
│   │                                                                              │   │
│   └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘
```


## Cost Monitoring Tools Comparison

| Tool | Type | Core Function | Cost | Use Cases |
|-----|-----|---------|------|---------|
| **Kubecost** | Open Source/Commercial | Cost allocation, optimization suggestions, budget alerts | Free version available | Suitable for medium to large clusters |
| **OpenCost** | Open Source (CNCF) | Cost monitoring, Prometheus integration | Free | Suitable for any size |
| **CloudHealth** | Commercial | Multi-cloud cost management, governance | Paid | Suitable for enterprise-level multi-cloud |
| **Spot.io** | Commercial | Automated cost optimization, Spot management | Paid | Suitable for automation needs |
| **CAST AI** | Commercial | Automatic optimization, cross-cloud scheduling | Paid | Suitable for multi-cloud/hybrid cloud |
| **AWS Cost Explorer** | Cloud Provider | AWS Original Cost Analysis | Included | AWS Users |
| **AliCloud Cost Analysis** | Cloud Provider | ACK Original Cost Statistics | Included | AliCloud Users |


## Kubecost Deployment

### Helm Installation

> ⚠️ **🟡 Medium Risk Changes** — Change cluster resource status, suggest to first use --dry-run or diff to confirm
> - `helm upgrade/install`: Deploy/Upgrade release
> - `kubectl apply/create/replace`: Create/Modify cluster resources

``` bash
# 🟡 Medium Risk: modifies cluster/resource state, confirm target, impact scope, and authorization before execution
#!/bin/bash
# deploy-kubecost.sh
# Kubecost Complete Deployment Script

set -e

NAMESPACE="kubecost"
RELEASE_NAME="kubecost"

message: "=== Deployment of Kubecost ==="

# Add Helm repository
helm repo add kubecost https://kubecost.github.io/cost-analyzer/
helm repo update

# Create namespace
kubectl create namespace $NAMESPACE --dry-run=client -o yaml | kubectl apply -f -

# Create values file
cat > kubecost-values.yaml << 'EOF'
# Kubecost Helm Values

# Global configuration
global:
  prometheus:
    enabled: true
    nodeExporter:
      enabled: true

# Product configuration
kubecostProductConfigs:
  # Cluster name
  clusterName: "production-cluster"
  
  # Currency settings
  currencyCode: "USD"
  
  # Shared cost allocation
  sharedCostEnabled: true
  sharedNamespaces:
    - kube-system
    - monitoring
    - ingress-nginx
    
# Prometheus configuration
prometheus:
  server:
    retention: 30d
    persistentVolume:
      enabled: true
      size: 32Gi
    resources:
      requests:
        cpu: 500m
        memory: 2Gi
      limits:
        cpu: 2
        memory: 8Gi
        
  nodeExporter:
    enabled: true
    
  alertmanager:
    enabled: false

# Network Cost Monitoring
networkCosts:
  enabled: true
  config:
    # Regional pricing
    zoneCost: 0.01
    regionCost: 0.02
    internetCost: 0.12

# Persistence
persistentVolume:
  enabled: true
  size: 32Gi
  storageClass: "gp3"

# Resource configuration
kubecostModel:
  resources:
    requests:
      cpu: 200m
      memory: 512Mi
    limits:
      cpu: 1
      memory: 2Gi
      
# Frontend configuration
kubecostFrontend:
  resources:
    requests:
      cpu: 50m
      memory: 64Mi
    limits:
      cpu: 200m
      memory: 256Mi

# Service configuration
service:
  type: ClusterIP
  port: 9090

# Ingress configuration (optional)
ingress:
  enabled: false
  # className: nginx
  # hosts:
  #   - host: kubecost.example.com
  #     paths:
  #       - path: /
  #         pathType: Prefix

# RBAC
rbac:
  create: true

# ServiceAccount
serviceAccount:
  create: true
  # annotations:
  #   eks.amazonaws.com/role-arn: arn:aws:iam::ACCOUNT:role/kubecost-role
EOF

# Deploy Kubecost
helm upgrade --install $RELEASE_NAME kubecost/cost-analyzer \
  --namespace $NAMESPACE \
  --values kubecost-values.yaml \
  --wait --timeout 10m

message: "=== Wait for Pods to be Ready ==="
kubectl wait --for=condition=Ready pod \
  -l app=cost-analyzer \
  -n $NAMESPACE \
  --timeout=300s

message: "=== Deployment Complete ==="
message: "Visit command: kubectl port-forward -n $NAMESPACE svc/kubecost-cost-analyzer 9090:9090"
message: "Browser access: http://localhost:9090"
```
### OpenCost Deployment (Open Source Alternative)

```yaml
# opencost-deployment.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: opencost

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: opencost
  namespace: opencost
spec:
  replicas: 1
  selector:
    matchLabels:
      app: opencost
  template:
    metadata:
      labels:
        app: opencost
    spec:
      serviceAccountName: opencost
      containers:
        - name: opencost
          image: ghcr.io/opencost/opencost:latest
          ports:
            - containerPort: 9003
          env:
            - name: PROMETHEUS_SERVER_ENDPOINT
              value: "http://prometheus-server.monitoring:9090"
            - name: CLOUD_PROVIDER_API_KEY
              valueFrom:
                secretKeyRef:
                  name: opencost-secrets
                  key: CLOUD_PROVIDER_API_KEY
                  optional: true
            - name: CLUSTER_ID
              value: "production-cluster"
          resources:
            requests:
              cpu: 100m
              memory: 256Mi
            limits:
              cpu: 500m
              memory: 1Gi
              
        - name: opencost-ui
          image: ghcr.io/opencost/opencost-ui:latest
          ports:
            - containerPort: 9090
          resources:
            requests:
              cpu: 50m
              memory: 64Mi

---
apiVersion: v1
kind: Service
metadata:
  name: opencost
  namespace: opencost
spec:
  selector:
    app: opencost
  ports:
    - name: api
      port: 9003
      targetPort: 9003
    - name: ui
      port: 9090
      targetPort: 9090

---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: opencost
  namespace: opencost

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: opencost
rules:
  - apiGroups: [""]
    resources:
      - configmaps
      - deployments
      - nodes
      - pods
      - services
      - resourcequotas
      - replicationcontrollers
      - limitranges
      - persistentvolumeclaims
      - persistentvolumes
      - namespaces
      - endpoints
    verbs: ["get", "list", "watch"]
  - apiGroups: ["extensions", "apps"]
    resources: ["daemonsets", "deployments", "replicasets"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["batch"]
    resources: ["cronjobs", "jobs"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["autoscaling"]
    resources: ["horizontalpodautoscalers"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["policy"]
    resources: ["poddisruptionbudgets"]
    verbs: ["get", "list", "watch"]
  - apiGroups: ["storage.k8s.io"]
    resources: ["storageclasses"]
    verbs: ["get", "list", "watch"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: opencost
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: opencost
subjects:
  - kind: ServiceAccount
    name: opencost
    namespace: opencost
```


## Resource Optimization Configuration

### VPA Resource Recommendations

```yaml
# vpa-recommendation.yaml
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: myapp-vpa
  namespace: production
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  updatePolicy:
    updateMode: "Off"  # 仅建议模式,不自动更新
  resourcePolicy:
    containerPolicies:
      - containerName: "*"
        minAllowed:
          cpu: 50m
          memory: 64Mi
        maxAllowed:
          cpu: 4
          memory: 8Gi
        controlledResources:
          - cpu
          - memory
        controlledValues: RequestsAndLimits

---
# VPA Recommended Configuration - Automatic Update Mode
apiVersion: autoscaling.k8s.io/v1
kind: VerticalPodAutoscaler
metadata:
  name: backend-vpa-auto
  namespace: production
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: backend
  updatePolicy:
    updateMode: "Auto"
    minReplicas: 2  # 保证最小副本数
  resourcePolicy:
    containerPolicies:
      - containerName: backend
        minAllowed:
          cpu: 100m
          memory: 128Mi
        maxAllowed:
          cpu: 2
          memory: 4Gi
```

### Cluster Autoscaler Cost Optimization

```yaml
# cluster-autoscaler-cost-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-autoscaler-config
  namespace: kube-system
data:
  config.yaml: |
    # Expander Configuration - Prioritize the cheapest node pool
    expanders:
      - priority
      - least-waste
    
    # Node Pool Priority (lower number means higher priority)
    priorities: |
      10:
        - .*spot.*           # 最优先 Spot 实例
      20:
        - .*preemptible.*    # 其次抢占式实例
      50:
        - .*ondemand.*       # 最后按需实例
    
    # Drain Configuration
    scale-down-enabled: true
    scale-down-delay-after-add: 10m          # 扩容后等待缩容
    scale-down-delay-after-delete: 0s        # 删除节点后等待
    scale-down-delay-after-failure: 3m       # 失败后等待
    scale-down-unneeded-time: 10m            # 节点空闲时间
    scale-down-unready-time: 20m             # 不健康节点空闲时间
    scale-down-utilization-threshold: 0.5    # 利用率阈值
    
    # Node Group Configuration
    balance-similar-node-groups: true        # 平衡相似节点组
    
    # Performance Configuration
    scan-interval: 10s
    max-node-provision-time: 15m
    max-graceful-termination-sec: 600
    max-empty-bulk-delete: 10

---
# Karpenter Cost Optimization Configuration
apiVersion: karpenter.sh/v1beta1
kind: NodePool
metadata:
  name: cost-optimized
spec:
  template:
    spec:
      requirements:
        - key: kubernetes.io/arch
          operator: In
          values: ["amd64"]
        - key: karpenter.sh/capacity-type
          operator: In
          values: ["spot", "on-demand"]  # 优先 Spot
        - key: node.kubernetes.io/instance-type
          operator: In
          values:
            - m5.large
            - m5.xlarge
            - m5a.large
            - m5a.xlarge
            - m6i.large
            - m6i.xlarge
      nodeClassRef:
        name: default
  limits:
    cpu: 1000
    memory: 1000Gi
  disruption:
    consolidationPolicy: WhenUnderutilized
    consolidateAfter: 30s
  # Weight Configuration - Prioritize Spot
  weight: 100
```


## Cost Tagging System

### Tag Specification

```yaml
# cost-labeling-standard.yaml

---
# Namespace-Level Labels
apiVersion: v1
kind: Namespace
metadata:
  name: team-backend
  labels:
    # Organization Labels
    team: backend
    department: engineering
    cost-center: "CC-12345"
    
    # Environment Labels
    environment: production
    
    # Management Labels
    owner: backend-team@company.com
    managed-by: terraform

---
# Deployment-Level Labels
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api-server
  namespace: team-backend
  labels:
    # Application Labels
    app: api-server
    app.kubernetes.io/name: api-server
    app.kubernetes.io/component: backend
    app.kubernetes.io/part-of: platform
    
    # Cost Labels
    team: backend
    project: platform-api
    cost-center: "CC-12345"
    
    # Operations Labels
    tier: critical
    sla: gold
spec:
  template:
    metadata:
      labels:
        app: api-server
        team: backend
        project: platform-api
      annotations:
        # Kubecost Annotation
        cost.kubernetes.io/team: "backend"
        cost.kubernetes.io/project: "platform-api"
    spec:
      containers:
        - name: api-server
          resources:
            requests:
              cpu: 500m
              memory: 512Mi
            limits:
              cpu: 2
              memory: 2Gi
```

### Mandatory Tag Policies

```yaml
# cost-label-policy.yaml
# Use Kyverno to enforce cost labels at the namespace level

apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-cost-labels
  annotations:
    policies.kyverno.io/title: 强制成本标签
    policies.kyverno.io/description: 所有 Pod 必须包含成本分配标签
spec:
  validationFailureAction: Enforce
  background: true
  rules:
    - name: require-team-label
      match:
        any:
          - resources:
              kinds:
                - Pod
              namespaces:
                - "!kube-system"
                - "!kube-public"
                - "!monitoring"
      validate:
        message: "All Pods must contain the 'team' label for cost allocation"
        pattern:
          metadata:
            labels:
              team: "?*"
              
    - name: require-project-label
      match:
        any:
          - resources:
              kinds:
                - Pod
              namespaces:
                - production
                - staging
      validate:
        message: "Production/Staging environment Pods must contain the 'project' label"
        pattern:
          metadata:
            labels:
              project: "?*"
              
    - name: require-cost-center
      match:
        any:
          - resources:
              kinds:
                - Namespace
      validate:
        message: "The namespace must contain the 'cost-center' label"
        pattern:
          metadata:
            labels:
              cost-center: "?*"
```


## Cost Query and Analysis

### Prometheus Cost Query

```promql
# cost-prometheus-queries.promql

# =============================================================================
# Statistic CPU Cost by Namespace
# =============================================================================
sum by (namespace) (
  rate(container_cpu_usage_seconds_total{container!="", namespace!="kube-system"}[5m])
) * on (node) group_left() 
(node_hourly_cost / 3600)

# =============================================================================
# Statistic Memory Cost by Namespace
# =============================================================================
sum by (namespace) (
  container_memory_usage_bytes{container!="", namespace!="kube-system"}
) * on (node) group_left() 
(node_hourly_cost / 3600 / 1024 / 1024 / 1024)

# =============================================================================
# Count costs by tag (team)
# =============================================================================
sum by (label_team) (
  rate(container_cpu_usage_seconds_total{container!=""}[1h]) 
  * on (namespace, pod) group_left(label_team) 
  kube_pod_labels
) * on (node) group_left() 
node_hourly_cost

# =============================================================================
# Resource requests vs actual usage (identify waste)
# =============================================================================
# CPU request utilization
sum(rate(container_cpu_usage_seconds_total{container!=""}[5m])) by (namespace)
/
sum(kube_pod_container_resource_requests{resource="cpu"}) by (namespace)

# Memory request utilization
sum(container_memory_usage_bytes{container!=""}) by (namespace)
/
sum(kube_pod_container_resource_requests{resource="memory"}) by (namespace)

# =============================================================================
# Idle resource statistics
# =============================================================================
# CPU idle quantity
(
  sum(kube_pod_container_resource_requests{resource="cpu"}) -
  sum(rate(container_cpu_usage_seconds_total{container!=""}[5m]))
) 
/ 
sum(kube_pod_container_resource_requests{resource="cpu"}) * 100

# Memory idle quantity
(
  sum(kube_pod_container_resource_requests{resource="memory"}) -
  sum(container_memory_usage_bytes{container!=""})
) 
/ 
sum(kube_pod_container_resource_requests{resource="memory"}) * 100

# =============================================================================
# Node utilization (identify nodes to scale down)
# =============================================================================
# Nodes with CPU utilization below 50%
(
  sum(rate(container_cpu_usage_seconds_total{container!=""}[5m])) by (node)
  /
  sum(kube_node_status_allocatable{resource="cpu"}) by (node)
) < 0.5

# =============================================================================
# Estimate cross AZ traffic cost
# =============================================================================
sum(rate(container_network_transmit_bytes_total[5m])) by (namespace) 
* 0.01  # Assume cross AZ traffic $0.01/GB
```

### ResourceQuota Cost Control

```yaml
# resourcequota-cost-control.yaml

---
# Team quota
apiVersion: v1
kind: ResourceQuota
metadata:
  name: team-backend-quota
  namespace: team-backend
spec:
  hard:
    # Compute resources
    requests.cpu: "100"
    requests.memory: 200Gi
    limits.cpu: "200"
    limits.memory: 400Gi
    
    # GPU resources
    requests.nvidia.com/gpu: "4"
    
    # Storage resources
    persistentvolumeclaims: "50"
    requests.storage: 1Ti
    
    # Number of objects
    pods: "200"
    services: "50"
    secrets: "100"
    configmaps: "100"
    
    # Specific storage class quota
    gp3.storageclass.storage.k8s.io/requests.storage: 500Gi
    io2.storageclass.storage.k8s.io/requests.storage: 100Gi

---
# Default resources in LimitRange
apiVersion: v1
kind: LimitRange
metadata:
  name: team-backend-limits
  namespace: team-backend
spec:
  limits:
    # Container defaults
    - type: Container
      default:
        cpu: 500m
        memory: 512Mi
      defaultRequest:
        cpu: 100m
        memory: 128Mi
      min:
        cpu: 50m
        memory: 64Mi
      max:
        cpu: 4
        memory: 8Gi
        
    # Pod limits
    - type: Pod
      max:
        cpu: "16"
        memory: 32Gi
        
    # PVC Limit
    - type: PersistentVolumeClaim
      min:
        storage: 1Gi
      max:
        storage: 100Gi
```


## Cost Alert Rules

```yaml
# cost-alerting-rules.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: cost-alerts
  namespace: monitoring
spec:
  groups:
    # =================================================================
    # Cost Threshold Alert
    # =================================================================
    - name: cost.thresholds
      interval: 5m
      rules:
        - alert: DailyCostHigh
          expr: |
            sum(increase(kubecost_cluster_cost_total[24h])) > 1000
          for: 30m
          labels:
            severity: warning
          annotations:
            summary: "Daily cost exceeds $1000"
            description: "Cluster cost over the past 24 hours: ${{ $value | printf \"%.2f\" }}"
            
        - alert: NamespaceCostSpike
          expr: |
            (
              sum(increase(kubecost_namespace_cost_total[1h])) by (namespace)
              /
              avg_over_time(sum(increase(kubecost_namespace_cost_total[1h])) by (namespace)[24h:1h])
            ) > 2
          for: 15m
          labels:
            severity: warning
          annotations:
            summary: "Cost in namespace {{ $labels.namespace }} has spiked"
            description: "Cost has increased by {{ $value | printf \"%.1f\" }}x compared to the average over the past 24 hours"
            
    # =================================================================
    # Resource Efficiency Alert
    # =================================================================
    - name: cost.efficiency
      interval: 5m
      rules:
        - alert: LowCPUUtilization
          expr: |
            (
              sum(rate(container_cpu_usage_seconds_total{container!=""}[1h])) by (namespace)
              /
              sum(kube_pod_container_resource_requests{resource="cpu"}) by (namespace)
            ) < 0.2
          for: 2h
          labels:
            severity: info
          annotations:
            summary: "CPU utilization in namespace {{ $labels.namespace }} is low"
            description: "CPU utilization is only {{ $value | printf \"%.1f\" }}%, suggest adjusting resource requests"
            
        - alert: LowMemoryUtilization
          expr: |
            (
              sum(container_memory_usage_bytes{container!=""}) by (namespace)
              /
              sum(kube_pod_container_resource_requests{resource="memory"}) by (namespace)
            ) < 0.3
          for: 2h
          labels:
            severity: info
          annotations:
            summary: "Memory utilization in namespace {{ $labels.namespace }} is low"
            description: "Memory utilization is only {{ $value | printf \"%.1f\" }}%"
            
        - alert: OverprovisionedResources
          expr: |
            (
              sum(kube_pod_container_resource_limits{resource="cpu"}) by (namespace)
              /
              sum(kube_pod_container_resource_requests{resource="cpu"}) by (namespace)
            ) > 3
          for: 1h
          labels:
            severity: info
          annotations:
            summary: "Namespace {{ $labels.namespace }} has resource over-allocation"
            description: "The ratio of limits to requests is {{ $value | printf \"%.1f\" }}x"
            
    # =================================================================
    # Budget Alert
    # =================================================================
    - name: cost.budget
      interval: 15m
      rules:
        - alert: MonthlyBudget80Percent
          expr: |
            (
              sum(kubecost_cluster_cost_total)
              /
              kubecost_budget_monthly_total
            ) > 0.8
          labels:
            severity: warning
          annotations:
            summary: "Monthly budget has been used at 80%"
            
        - alert: MonthlyBudgetExceeded
          expr: |
            (
              sum(kubecost_cluster_cost_total)
              /
              kubecost_budget_monthly_total
            ) > 1.0
          labels:
            severity: critical
          annotations:
            summary: "Monthly budget has exceeded"
```


## Cost Optimization Checklist

### Optimization Strategy Matrix

| Strategy | Savings Rate | Implementation Complexity | Applicable Scenarios |
|---------|---------|-----------|---------|
| **Preemptible/Spot Instances** | 50-90% | Low | Non-critical workloads |
| **Reserved Instances** | 30-60% | Low | Stable baseline loads |
| **Node Auto Scaling** | 20-40% | Medium | Load fluctuation scenarios |
| **VPA Resource Adjustment** | 15-30% | Low | Over-provisioned applications |
| **Node Pool Optimization** | 10-30% | Medium | Diverse workload scenarios |
| **Bin Packing** | 15-25% | Medium | Improve bin packing rate |
| **Storage Layering** | 20-40% | Medium | Large storage scenarios |
| **Network Optimization** | 10-20% | High | Large cross-region traffic |

### Check Command Set

``` bash
# 🟢 Low Risk: Read-only/information gathering, typically with no side effects
#!/bin/bash
# cost-optimization-checklist.sh
# Cost Optimization Check Script

echo "=== Kubernetes Cost Optimization Check ==="
echo ""

echo "1. Resource Utilization Check"
echo "--- Pods Without Resource Requests ---"
kubectl get pods --all-namespaces -o json | jq -r '
  .items[] | 
  select(.spec.containers[].resources.requests == null) | 
  "\(.metadata.namespace)/\(.metadata.name)"'
echo ""

echo "2. Idle Pod Check"
echo "--- Pods With CPU Usage Below 10% ---"
kubectl top pods --all-namespaces --sort-by=cpu | head -20
echo ""

echo "3. Expired PVC Check"
echo "--- Unbound PVCs ---"
kubectl get pvc --all-namespaces --field-selector=status.phase!=Bound
echo ""

echo "4. Unused ConfigMap/Secrets"
echo "--- Check Command ---"
echo "kubectl get configmaps --all-namespaces -o json | jq '.items[].metadata.name'"
echo ""

echo "5. Node Utilization"
kubectl top nodes
echo ""

echo "6. Pod Distribution Across AZs"
kubectl get pods --all-namespaces -o wide | awk '{print $8}' | sort | uniq -c
echo ""

echo "=== Check Complete ==="
```

## Financial Operations Maturity Model

### Maturity Phases

| Stage | Name | Core Capabilities | Key Metrics | Goals |
|-----|------|---------|---------|------|
| **Level 1** | Crawl (Beginner) | Cost Visibility | See cost data | Know how much was spent |
| **Level 2** | Walk (Walking) | Cost Allocation | Allocate by team/project | Know who spent what |
| **Level 3** | Run (Running) | Cost Optimization | Active optimization measures | Continuously reduce costs |
| **Level 4** | Fly (Flying) | Predictive Optimization | Predictive cost management | Proactive decision-making |

### Vendor-Specific Features

| Feature | AWS EKS | Azure AKS | GCP GKE | AliCloud ACK |
|-----|---------|-----------|---------|-----------|
| Cost Analysis | Cost Explorer | Cost Management | Cloud Billing | Cost Analysis |
| Resource Recommendations | Compute Optimizer | Advisor | Recommender | Resource Profile |
| Spot Nodes | Spot Instances | Spot VMs | Preemptible VMs | Spot Instance |
| Reserved Instances | Reserved/Savings Plans | Reserved | CUDs | Reserved Instance |
| Elastic Quotas | Service Quotas | Quotas | Quotas | Elastic Quotas |


## Version Change Log

| Version | Change Log | Impact |
|-----|---------|------|
| **Kubecost 2.0** | GPU Cost Tracking Enhancements | More Precise Cost Analysis |
| **OpenCost 1.0** | CNCF Graduated Project | Open Source Standardization |
| **v1.29** | Enhanced VPA | Better Resource Recommendations |
| **v1.28** | GA for Karpenter | Smarter Node Management |


## Best Practice Summary

### Cost Management Checklist

- [ ] Deploy Cost Monitoring Tools (Kubecost/OpenCost)
- [ ] Establish Cost Tagging Standards
- [ ] Configure ResourceQuota and LimitRange
- [ ] Enable VPA Resource Recommendations
- [ ] Configure Auto-scaling for Nodes
- [ ] Use Spot/Spot Instances
- [ ] Set up Cost Alerts
- [ ] Conduct Regular Cost Reviews

---

**References**:
- [Kubecost Documentation](https://docs.kubecost.com/)
- [OpenCost Project](https://www.opencost.io/)
- [FinOps Foundation](https://www.finops.org/)
- [Kubernetes Cost Optimization](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/)

---


## Obsidian Documentation Related

- domain-11-ai-infra MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Open Source Project Index
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

- 25-llm-observability
- 26-cost-optimization-overview
- 28-green-computing-sustainability
- 29-alibaba-cloud-integration

```

## Related

- [[deep-dive|#deep-dive Hub]] — tag hub


<!-- risk-assessed -->
