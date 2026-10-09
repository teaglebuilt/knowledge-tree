---
title: GPU Scheduling and Management
description: Deeply analyze K8s GPU Scheduling: NVIDIA Device Plugin, MIG Scheduling, GPU Resource Quotas, Time Slicing, Multi-instance GPU (MIG), AMD
  GPU Scheduling and GPU Health Monitoring
summary: Deeply analyze K8s GPU Scheduling: NVIDIA Device Plugin, MIG Scheduling, GPU Resource Quotas, Time Slicing, Multi-instance GPU (MIG), AMD
  GPU Scheduling and GPU Health Monitoring
category: domain-11-ai-infra
tags:
- k8s
- gpu
- nvidia
- amd
- device-plugin
- mig
- gpu-scheduling
- time-slicing
- scheduler
- prometheus
tier: core
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- MLOps Engineers
- SRE
estimated_read_time: 5min
intent_queries:
- What is GPU Scheduling and Management
- How is GPU Scheduling and Management
- Kubernetes 11 ai infra Best Practices
trigger_keywords:
- GPU
- Scheduling and Management
- ai
- infra
prerequisites:
- kubectl-basics
- helm-basics
- prometheus-basics
- gpu-scheduling-basics
k8s_versions:
- '1.25'
- '1.26'
- '1.27'
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
  path: ../domain-02-workloads-applications/
  label: 'Related Knowledge Domain: domain-02-workloads-applications'
- type: domain
  path: ../domain-03-networking-traffic/
  label: 'Related Knowledge Domain: domain-03-networking-traffic'
- type: fta
  path: ../domain-10-troubleshooting-diagnostics/topic-fta/list/gpu-fta.md
  label: 'Fault Tree: gpu'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
related_docs:
- path: 01-ai-infrastructure-overview.md
  type: depth
  desc: AI Infrastructure Architecture
- path: 05-distributed-training-frameworks.md
  type: depth
  desc: Distributed Training Framework
- path: ../domain-10-troubleshooting-diagnostics/topic-fta/list/gpu-fta.md
  type: fta
  desc: GPU Fault Tree
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/03-gpu-scheduling-management.md
---

> **Production Environment Security Tips**
>
> Commands included in this document can be directly executed. Before executing, please confirm: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information collection with no side effects).




# 133 - GPU Scheduling & Management

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25-v1.32 | **Last Updated**: 2026-01 | **Reference**: [NVIDIA Device Plugin](https://github.com/NVIDIA/k8s-device-plugin)

---


## 1. GPU Resource Management Architecture

### 1.1 Kubernetes GPU Scheduling Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    Kubernetes GPU Scheduler Architecture                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                      Control Plane                                   │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │   │
│  │  │ kube-scheduler│  │ Device Plugin│  │ GPU Operator │              │   │
│  │  │   (scheduler decision)  │  │  Manager     │  │  (lifecycle)   │              │   │
│  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘              │   │
│  │         │                 │                 │                       │   │
│  │         │    Extended Resources API         │                       │   │
│  │         └─────────────────┼─────────────────┘                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                              │
│  ════════════════════════════╪══════════════════════════════════════════   │
│                              │                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        GPU Node                                      │   │
│  │  ┌──────────────────────────────────────────────────────────────┐   │   │
│  │  │  NVIDIA Device Plugin (DaemonSet)                             │   │   │
│  │  │  ├── GPU discovery and registration                                            │   │   │
│  │  │  ├── health checks                                                 │   │   │
│  │  │  ├── device allocation (nvidia.com/gpu)                                │   │   │
│  │  │  └── MIG/Time-Slicing management                                     │   │   │
│  │  └──────────────────────────────────────────────────────────────┘   │   │
│  │                              │                                       │   │
│  │  ┌──────────────┐  ┌────────┴────────┐  ┌──────────────┐           │   │
│  │  │ DCGM Exporter│  │ Container Runtime│  │ GPU Driver   │           │   │
│  │  │ (monitoring metrics)    │  │ (nvidia-container)│  │ (CUDA/cuDNN) │           │   │
│  │  └──────────────┘  └─────────────────┘  └──────────────┘           │   │
│  │                              │                                       │   │
│  │  ┌──────────────────────────────────────────────────────────────┐   │   │
│  │  │                    Physical GPUs                              │   │   │
│  │  │  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐              │   │   │
│  │  │  │ GPU 0  │  │ GPU 1  │  │ GPU 2  │  │ GPU 3  │              │   │   │
│  │  │  │ A100   │  │ A100   │  │ A100   │  │ A100   │              │   │   │
│  │  │  └────────┘  └────────┘  └────────┘  └────────┘              │   │   │
│  │  └──────────────────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Comparison of GPU Virtualization Technologies

| Technology | Isolation Level | Granularity | Memory Isolation | Compute Isolation | Applicable GPU | Applicable Scenario |
|-----|---------|------|---------|---------|--------|---------|
| **Passthrough** | Strong (Hardware) | Whole Card | Complete | Complete | All | Training/Large Model Inference |
| **MIG** | Strong (Hardware) | 1/7 Card | Complete | Complete | A100/H100 | Multi-tenant/Mixed Inference |
| **Time-Slicing** | Weak (Time Slicing) | Simulated Multi-Cards | Soft Limitations | None | All | Development/Small Model Inference |
| **vGPU** | Medium (Software) | Percentage | Soft Isolation | Soft Isolation | Enterprise Edition | Virtualization/VDI |
| **MPS** | Weak (Process) | Shared | None | None | All | Small Tasks Mixed-Mode |
| **DRA** (v1.31+) | Flexible | Dynamic | Depends on Driver | Depends on Driver | All | Next Generation Resource Management |

---


## 2. GPU Operator Deployment

### 2.1 GPU Operator Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      NVIDIA GPU Operator component                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐                                                        │
│  │  GPU Operator   │ ← controller, manages all component lifecycles                           │
│  │  (Deployment)   │                                                        │
│  └────────┬────────┘                                                        │
│           │                                                                  │
│  ┌────────┴────────────────────────────────────────────────────────────┐   │
│  │                    Managed Components (DaemonSet)                    │   │
│  │                                                                      │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │   │
│  │  │ Driver      │  │ Container   │  │ Device      │                 │   │
│  │  │ (driver installation)   │  │ Toolkit     │  │ Plugin      │                 │   │
│  │  │             │  │ (runtime)     │  │ (device discovery)   │                 │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘                 │   │
│  │                                                                      │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                 │   │
│  │  │ DCGM        │  │ MIG Manager │  │ Node Feature│                 │   │
│  │  │ Exporter    │  │ (MIG configuration)    │  │ Discovery   │                 │   │
│  │  │ (monitoring)      │  │             │  │ (node labels)   │                 │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘                 │   │
│  │                                                                      │   │
│  │  ┌─────────────┐  ┌─────────────┐                                  │   │
│  │  │ GPU Feature │  │ Validator   │                                  │   │
│  │  │ Discovery   │  │ (validation)      │                                  │   │
│  │  └─────────────┘  └─────────────┘                                  │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Deployment Configuration

```yaml
# GPU Operator Helm Values (Production-Level Configuration)
apiVersion: v1
kind: ConfigMap
metadata:
  name: gpu-operator-values
data:
  values.yaml: |
    operator:
      defaultRuntime: containerd
      
    driver:
      enabled: true
      version: "535.104.12"
      repository: nvcr.io/nvidia
      
      # Driver Upgrade Strategy
      upgradePolicy:
        autoUpgrade: false
        maxParallelUpgrades: 1
        maxUnavailable: "25%"
        waitForCompletion:
          timeoutSeconds: 0
          
      # RDMA Support
      rdma:
        enabled: true
        useHostMofed: true
        
    toolkit:
      enabled: true
      version: "v1.14.3-ubuntu20.04"
      
    devicePlugin:
      enabled: true
      version: "v0.14.3"
      
      # Time-Slicing Configuration
      config:
        name: "time-slicing-config"
        default: "any"
        
    dcgm:
      enabled: true
      
    dcgmExporter:
      enabled: true
      version: "3.3.0-3.2.0-ubuntu22.04"
      serviceMonitor:
        enabled: true
        
    gfd:
      enabled: true
      version: "v0.8.2"
      
    migManager:
      enabled: true
      
    nodeStatusExporter:
      enabled: true
      
    validator:
      enabled: true
```

> ⚠️ **🟡 Medium Risk Change** — Modify cluster resource status, recommend to first use --dry-run or diff to confirm
> - `helm upgrade/install` : Deploy/Upgrade release

``` bash
# 🟡 Medium Risk: Will modify cluster/resource status, please confirm target, impact scope, and authorization before execution
# Deploy GPU Operator
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
helm repo update

helm install gpu-operator nvidia/gpu-operator \
  --namespace gpu-operator \
  --create-namespace \
  --version v23.9.1 \
  -f gpu-operator-values.yaml
```
---


## 3. Time-Slicing Configuration

### 3.1 Principle of Time-Slicing

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Time-Slicing principle                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Physical GPU (1 A100)                                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                                                                     │   │
│  │    Time Slice 1    Time Slice 2    Time Slice 3    Time Slice 4    │   │
│  │  ┌──────────────┐┌──────────────┐┌──────────────┐┌──────────────┐  │   │
│  │  │   Pod A      ││   Pod B      ││   Pod C      ││   Pod D      │  │   │
│  │  │   (25%)      ││   (25%)      ││   (25%)      ││   (25%)      │  │   │
│  │  └──────────────┘└──────────────┘└──────────────┘└──────────────┘  │   │
│  │        ↓               ↓               ↓               ↓          │   │
│  │  ══════════════════════════════════════════════════════════════   │   │
│  │                    Context Switch (Time Slice)                     │   │
│  │  ══════════════════════════════════════════════════════════════   │   │
│  │                                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Kubernetes perspective: 4 nvidia.com/gpu resources                                     │
│  Actual hardware: 1 physical GPU, shared memory                                               │
│                                                                             │
│  Notes:                                                                   │
│  - Unisolated memory, all Pods share 80GB                                                │
│  - Compute rotates on time slices, not true isolation                                               │
│  - Suitable for development debugging, not production training                                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Time-Slicing Configuration

```yaml
# Time-Slicing ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: time-slicing-config
  namespace: gpu-operator
data:
  any: |
    version: v1
    flags:
      migStrategy: none
    sharing:
      timeSlicing:
        renameByDefault: true
        failRequestsGreaterThanOne: false
        resources:
        - name: nvidia.com/gpu
          replicas: 4           # 每张GPU模拟4张
          
  inference: |
    version: v1
    sharing:
      timeSlicing:
        renameByDefault: true
        resources:
        - name: nvidia.com/gpu
          replicas: 8           # 推理场景更多切片
          
  development: |
    version: v1
    sharing:
      timeSlicing:
        renameByDefault: true
        resources:
        - name: nvidia.com/gpu
          replicas: 10          # 开发环境最大切片

---
# Apply Different Configurations to Node Labels
# Production Training Nodes: Disable Time-Slicing
kubectl label node gpu-train-01 nvidia.com/device-plugin.config=none

# Inference Nodes: 8x Slicing
kubectl label node gpu-infer-01 nvidia.com/device-plugin.config=inference

# Development Nodes: 10x Slicing
kubectl label node gpu-dev-01 nvidia.com/device-plugin.config=development
```

### 3.3 Using Time-Slicing Resources

```yaml
# Pods Using Time-Slicing GPUs
apiVersion: v1
kind: Pod
metadata:
  name: inference-pod
spec:
  containers:
  - name: inference
    image: nvcr.io/nvidia/pytorch:24.01-py3
    resources:
      limits:
        nvidia.com/gpu: 1       # 使用1个虚拟GPU切片
    env:
    - name: CUDA_VISIBLE_DEVICES
      value: "0"
    - name: NVIDIA_VISIBLE_DEVICES
      value: "all"
      
---
# Validate Time-Slicing Effect
apiVersion: v1
kind: Pod
metadata:
  name: gpu-test
spec:
  containers:
  - name: test
    image: nvcr.io/nvidia/cuda:12.2.0-base-ubuntu22.04
    command: ["nvidia-smi", "-L"]
    resources:
      limits:
        nvidia.com/gpu: 1
```

---


## 4. MIG Configuration & Management

### 4.1 MIG Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     A100 80GB MIG configuration example                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Configuration mode 1: 7x 1g.10gb (maximum number of instances)                                          │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐          │   │
│  │ │10GB │ │10GB │ │10GB │ │10GB │ │10GB │ │10GB │ │10GB │          │   │
│  │ │1/7SM│ │1/7SM│ │1/7SM│ │1/7SM│ │1/7SM│ │1/7SM│ │1/7SM│          │   │
│  │ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘ └─────┘          │   │
│  │ Instance 0-6: nvidia.com/mig-1g.10gb                              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Configuration mode 2: 3x 2g.20gb + 1x 1g.10gb (mixed configuration)                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌─────┐                  │   │
│  │ │   20GB    │ │   20GB    │ │   20GB    │ │10GB │                  │   │
│  │ │   2/7SM   │ │   2/7SM   │ │   2/7SM   │ │1/7SM│                  │   │
│  │ └───────────┘ └───────────┘ └───────────┘ └─────┘                  │   │
│  │ nvidia.com/mig-2g.20gb x3   nvidia.com/mig-1g.10gb x1             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Configuration mode 3: 1x 4g.40gb + 3x 1g.10gb (mixed size)                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ ┌───────────────────────┐ ┌─────┐ ┌─────┐ ┌─────┐                  │   │
│  │ │        40GB           │ │10GB │ │10GB │ │10GB │                  │   │
│  │ │        4/7SM          │ │1/7SM│ │1/7SM│ │1/7SM│                  │   │
│  │ └───────────────────────┘ └─────┘ └─────┘ └─────┘                  │   │
│  │ nvidia.com/mig-4g.40gb x1   nvidia.com/mig-1g.10gb x3             │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Configuration mode 4: 1x 7g.80gb (single instance)                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ ┌─────────────────────────────────────────────────────────────────┐ │   │
│  │ │                          80GB                                   │ │   │
│  │ │                          7/7SM (Full GPU)                       │ │   │
│  │ └─────────────────────────────────────────────────────────────────┘ │   │
│  │ nvidia.com/mig-7g.80gb x1 (equivalent to whole card)                              │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 4.2 MIG Configuration Management

```yaml
# MIG Manager ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: mig-parted-config
  namespace: gpu-operator
data:
  config.yaml: |
    version: v1
    mig-configs:
      # Inference Optimization Configuration: 7 small instances
      all-1g.10gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            "1g.10gb": 7
            
      # Mixed Inference Configuration: 3 medium + 1 small
      all-2g.20gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            "2g.20gb": 3
            "1g.10gb": 1
            
      # Large Model Inference: 2 large + 1 small
      all-3g.40gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            "3g.40gb": 2
            "1g.10gb": 1
            
      # Training Configuration: Single large instance
      all-7g.80gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            "7g.80gb": 1
            
      # Disable MIG
      all-disabled:
        - devices: all
          mig-enabled: false

---
# Apply MIG Configuration to Nodes
apiVersion: v1
kind: Node
metadata:
  name: gpu-node-01
  labels:
    nvidia.com/mig.config: "all-1g.10gb"    # 7个小实例
    
---
# Use MIG Resources with Node Selectors
apiVersion: v1
kind: Pod
metadata:
  name: mig-inference-pod
spec:
  nodeSelector:
    nvidia.com/mig.config: "all-1g.10gb"
  containers:
  - name: inference
    image: nvcr.io/nvidia/pytorch:24.01-py3
    resources:
      limits:
        nvidia.com/mig-1g.10gb: 1           # 请求1个MIG实例
```

### 4.3 Specifications of MIG Instance Types

| MIG Profile | Memory | SM Count | Memory Bandwidth | Applicable Scenario |
|------------|------|------|---------|---------|
| **1g.10gb** | 10GB | 14 | ~285GB/s | Small Model Inference/Development |
| **2g.20gb** | 20GB | 28 | ~570GB/s | Medium Model Inference |
| **3g.40gb** | 40GB | 42 | ~855GB/s | Large Model Inference |
| **4g.40gb** | 40GB | 56 | ~1140GB/s | Large Model Inference/Tuning |
| **7g.80gb** | 80GB | 98 | ~2000GB/s | Training/Large Model |

---


## 5. Advanced Scheduling Strategies

### 5.1 GPU Topology-Aware Scheduling

```yaml
# GPU Topology-Aware Scheduling (Multi-GPU Tasks)
apiVersion: scheduling.volcano.sh/v1beta1
kind: PodGroup
metadata:
  name: distributed-training
spec:
  minMember: 4
  queue: training
  
---
apiVersion: batch.volcano.sh/v1alpha1
kind: Job
metadata:
  name: pytorch-distributed
spec:
  minAvailable: 4
  schedulerName: volcano
  plugins:
    env: []
    svc: []
  policies:
  - event: PodEvicted
    action: RestartJob
  tasks:
  - replicas: 4
    name: worker
    template:
      spec:
        schedulerName: volcano
        containers:
        - name: pytorch
          image: nvcr.io/nvidia/pytorch:24.01-py3
          resources:
            limits:
              nvidia.com/gpu: 8
          env:
          - name: NCCL_TOPO_FILE
            value: "/etc/nccl/topo.xml"
        # GPU Topology Affinity
        affinity:
          podAntiAffinity:
            preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              podAffinityTerm:
                labelSelector:
                  matchLabels:
                    job-name: pytorch-distributed
                topologyKey: kubernetes.io/hostname
```

### 5.2 Kueue GPU Queue Management

```yaml
# Kueue ResourceFlavor Definition for GPU Types
apiVersion: kueue.x-k8s.io/v1beta1
kind: ResourceFlavor
metadata:
  name: a100-80gb
spec:
  nodeLabels:
    nvidia.com/gpu.product: "NVIDIA-A100-SXM4-80GB"
  nodeTaints:
  - key: nvidia.com/gpu
    value: "true"
    effect: NoSchedule
    
---
# ClusterQueue Definition for GPU Quota
apiVersion: kueue.x-k8s.io/v1beta1
kind: ClusterQueue
metadata:
  name: gpu-cluster-queue
spec:
  namespaceSelector: {}
  resourceGroups:
  - coveredResources: ["cpu", "memory", "nvidia.com/gpu"]
    flavors:
    - name: a100-80gb
      resources:
      - name: "cpu"
        nominalQuota: 1000
      - name: "memory"
        nominalQuota: 4Ti
      - name: "nvidia.com/gpu"
        nominalQuota: 64
        borrowingLimit: 32            # 可借用上限
        
  # Preemption Strategy
  preemption:
    reclaimWithinCohort: Any
    withinClusterQueue: LowerPriority

---
# LocalQueue Bound to Namespace
apiVersion: kueue.x-k8s.io/v1beta1
kind: LocalQueue
metadata:
  name: ml-team-queue
  namespace: ml-training
spec:
  clusterQueue: gpu-cluster-queue
  
---
# Workload Submission
apiVersion: kueue.x-k8s.io/v1beta1
kind: Workload
metadata:
  name: training-job
  namespace: ml-training
spec:
  queueName: ml-team-queue
  priority: 100
  podSets:
  - name: main
    count: 4
    template:
      spec:
        containers:
        - name: trainer
          resources:
            requests:
              cpu: "32"
              memory: "128Gi"
              nvidia.com/gpu: "8"
```

### 5.3 Volcano Batch Scheduling

```yaml
# Volcano Queue Configuration
apiVersion: scheduling.volcano.sh/v1beta1
kind: Queue
metadata:
  name: training-queue
spec:
  weight: 10
  reclaimable: true
  capability:
    cpu: "1000"
    memory: "4Ti"
    nvidia.com/gpu: "64"
    
---
# Gang Scheduling Training Tasks
apiVersion: batch.volcano.sh/v1alpha1
kind: Job
metadata:
  name: llm-training
spec:
  minAvailable: 8                     # 最少需要8个Pod同时运行
  schedulerName: volcano
  queue: training-queue
  
  # Scheduling Strategy
  policies:
  - event: PodEvicted
    action: RestartJob
  - event: TaskCompleted
    action: CompleteJob
    
  # Plugin Configuration
  plugins:
    env: []
    svc: []
    ssh: []                           # SSH互联
    
  tasks:
  - replicas: 8
    name: worker
    template:
      spec:
        restartPolicy: OnFailure
        containers:
        - name: pytorch
          image: nvcr.io/nvidia/pytorch:24.01-py3
          command: ["torchrun"]
          args:
          - "--nproc_per_node=8"
          - "--nnodes=8"
          - "--node_rank=$(VC_TASK_INDEX)"
          - "--master_addr=$(VC_MASTER_HOST)"
          - "--master_port=29500"
          - "train.py"
          resources:
            requests:
              cpu: "64"
              memory: "512Gi"
              nvidia.com/gpu: "8"
            limits:
              cpu: "64"
              memory: "512Gi"
              nvidia.com/gpu: "8"
          env:
          - name: NCCL_DEBUG
            value: "INFO"
          - name: NCCL_IB_DISABLE
            value: "0"
```

---


## 6. GPU Monitoring & Diagnostics

### 6.1 DCGM Monitoring Metrics

| Metric Name | Field ID | Description | Alert Threshold |
|---------|----------|------|---------|
| `DCGM_FI_DEV_GPU_UTIL` | 203 | GPU Utilization% | < 50% Low Efficiency |
| `DCGM_FI_DEV_MEM_COPY_UTIL` | 204 | Memory Copy Utilization\% | - |
| `DCGM_FI_DEV_FB_USED` | 252 | Used Memory (MB) | > 95\% |
| `DCGM_FI_DEV_FB_FREE` | 251 | Free Memory (MB) | < 5\% |
| `DCGM_FI_DEV_GPU_TEMP` | 150 | GPU Temperature (\xB0C) | > 83\xb0C |
| `DCGM_FI_DEV_POWER_USAGE` | 155 | Power Usage (W) | > TDP |
| `DCGM_FI_DEV_SM_CLOCK` | 100 | SM Clock (MHz) | Frequency Warning |
| `DCGM_FI_DEV_MEM_CLOCK` | 101 | Memory Clock (MHz) | Frequency Warning |
| `DCGM_FI_DEV_PCIE_TX_THROUGHPUT` | 409 | PCIe Transmitted (MB/s) | - |
| `DCGM_FI_DEV_PCIE_RX_THROUGHPUT` | 410 | PCIe Received (MB/s) | - |
| `DCGM_FI_DEV_NVLINK_BANDWIDTH_TOTAL` | 450 | Total NVLink Bandwidth (GB/s) | - |
| `DCGM_FI_DEV_XID_ERRORS` | 230 | XID Errors Count | > 0 |
| `DCGM_FI_DEV_ECC_SBE_VOL_TOTAL` | 310 | Single Bit ECC Errors | Trend Increase |
| `DCGM_FI_DEV_ECC_DBE_VOL_TOTAL` | 313 | Double Bit ECC Errors | > 0 |

### 6.2 Prometheus Alert Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: gpu-alerts
  namespace: monitoring
spec:
  groups:
  - name: gpu-alerts
    rules:
    # Low GPU Utilization
    - alert: GPULowUtilization
      expr: |
        avg_over_time(DCGM_FI_DEV_GPU_UTIL[10m]) < 30
      for: 30m
      labels:
        severity: warning
      annotations:
        summary: "GPU utilization is too low"
        description: "GPU {{ $labels.gpu }} utilization {{ $value }}%"
        
    # GPU Memory Nearly Full
    - alert: GPUMemoryNearFull
      expr: |
        DCGM_FI_DEV_FB_USED / (DCGM_FI_DEV_FB_USED + DCGM_FI_DEV_FB_FREE) > 0.95
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "GPU memory usage exceeds 95%"
        
    # GPU Temperature Too High
    - alert: GPUHighTemperature
      expr: |
        DCGM_FI_DEV_GPU_TEMP > 83
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "GPU temperature exceeds 83°C"
        description: "GPU {{ $labels.gpu }} temperature {{ $value }}°C"
        
    # XID Error
    - alert: GPUXIDError
      expr: |
        increase(DCGM_FI_DEV_XID_ERRORS[5m]) > 0
      for: 0m
      labels:
        severity: critical
      annotations:
        summary: "GPU XID error"
        description: "GPU {{ $labels.gpu }} experienced an unrecoverable XID error"
        
    # ECC Error
    - alert: GPUECCError
      expr: |
        increase(DCGM_FI_DEV_ECC_DBE_VOL_TOTAL[1h]) > 0
      for: 0m
      labels:
        severity: critical
      annotations:
        summary: "GPU double-bit ECC error"
        description: "GPU {{ $labels.gpu }} experienced an uncorrectable ECC error, replacement required"
        
    # GPU Detached
    - alert: GPUNotAvailable
      expr: |
        absent(DCGM_FI_DEV_GPU_UTIL{gpu=~".+"})
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "GPU is unavailable"
        description: "Unable to obtain GPU metrics, GPU may have dropped card"
```

### 6.3 Fault Diagnosis Commands

``` bash
# 🟢 Low Risk: ReadOnly/Information Collection, Typically No Side Effects
# ========== Basic Diagnosis ==========

# GPU Status Overview
nvidia-smi

# Detailed GPU Information
nvidia-smi -q

# GPU Topology
nvidia-smi topo -m

# NVLink Status
nvidia-smi nvlink -s

# ========== Performance Diagnosis ==========

# Real-time Monitoring
nvidia-smi dmon -s pucvmet -d 1

# GPU Process
nvidia-smi pmon -s um -d 1

# Clock Frequency
nvidia-smi -q -d CLOCK

# Power Limiting
nvidia-smi -q -d POWER

# ========== Fault Diagnosis ==========

# XID Error
dmesg | grep -i "nvrm|xid"

# ECC Error
nvidia-smi -q -d ECC

# GPU Reset History
nvidia-smi -q -d PAGE_RETIREMENT

# Driver Version
cat /proc/driver/nvidia/version

# ========== MIG Diagnosis ==========

# MIG Status
nvidia-smi mig -lgi
nvidia-smi mig -lci

# MIG Instance Details
nvidia-smi mig -lgip
nvidia-smi mig -lcip

# ========== Kubernetes Diagnosis ==========

# GPU Node Resources
kubectl describe node <gpu-node> | grep -A 10 "Allocated resources"

# Device Plugin Logs
kubectl logs -n gpu-operator -l app=nvidia-device-plugin-daemonset

# GPU Operator Status
kubectl get pods -n gpu-operator

# Node GPU Tags
kubectl get nodes -L nvidia.com/gpu.product,nvidia.com/gpu.count,nvidia.com/mig.config
```
### 6.4 Common XID Error Codes

| XID | Error Type | Reason | Solution |
|-----|---------|------|---------|
| **13** | Graphics Engine Exception | CUDA kernel error | Check CUDA code |
| **31** | GPU Memory Page Fault | Out-of-bounds Memory Access | Check GPU Memory Allocation |
| **43** | GPU Stopped Processing | GPU Suspended | Reset GPU |
| **45** | Preemptive Cleanup | Memory Cleanup Timeout | Check Driver Version |
| **48** | Double Bit ECC Error | Un-correctable ECC | Replace GPU |
| **61** | Internal Micro-controller Breakpoint | Firmware Issue | Restart Node |
| **62** | Internal micro-controller halt | Firmware severe error | Replace GPU |
| **63** | ECC page retirement | ECC page retirement | Monitor trend |
| **64** | ECC page retirement | Page retirement at limit | Replace GPU |
| **74** | NVLink Error | NVLink issue | Check hardware connection |
| **79** | GPU access to memory denied | Memory access denied | Check driver/BIOS |
| **94** | Contained ECC error | Isolated ECC error | Monitor |
| **95** | Uncontained ECC error | Unisolated ECC error | Replace GPU |

---


## 7. GPU Resource Best Practices (Best Practices)

### 7.1 Resource Request Configuration

```yaml
# Training Task Configuration (Complete Resource Declaration)
apiVersion: v1
kind: Pod
metadata:
  name: training-pod
spec:
  # Scheduling Constraints
  nodeSelector:
    nvidia.com/gpu.product: "NVIDIA-A100-SXM4-80GB"
  tolerations:
  - key: "nvidia.com/gpu"
    operator: "Exists"
    effect: "NoSchedule"
    
  containers:
  - name: trainer
    image: nvcr.io/nvidia/pytorch:24.01-py3
    
    # Resource Request = Limit (Ensure QoS)
    resources:
      requests:
        cpu: "64"
        memory: "512Gi"
        nvidia.com/gpu: "8"
      limits:
        cpu: "64"
        memory: "512Gi"
        nvidia.com/gpu: "8"
        
    # GPU Environment Variables
    env:
    - name: CUDA_VISIBLE_DEVICES
      value: "0,1,2,3,4,5,6,7"
    - name: NVIDIA_VISIBLE_DEVICES
      value: "all"
    - name: NVIDIA_DRIVER_CAPABILITIES
      value: "compute,utility"
      
    # NCCL Optimization
    - name: NCCL_DEBUG
      value: "WARN"
    - name: NCCL_IB_DISABLE
      value: "0"
    - name: NCCL_NET_GDR_LEVEL
      value: "5"
    - name: NCCL_P2P_LEVEL
      value: "NVL"
      
    # Memory Optimization
    - name: PYTORCH_CUDA_ALLOC_CONF
      value: "max_split_size_mb:512"
      
    # Volume Mounting
    volumeMounts:
    - name: shm
      mountPath: /dev/shm
    - name: data
      mountPath: /data
      
  volumes:
  - name: shm
    emptyDir:
      medium: Memory
      sizeLimit: "64Gi"           # 共享内存
  - name: data
    persistentVolumeClaim:
      claimName: training-data
```

### 7.2 Multi-GPU Training Optimization

```yaml
# Distributed Training Configuration
apiVersion: "kubeflow.org/v1"
kind: PyTorchJob
metadata:
  name: distributed-training
spec:
  elasticPolicy:
    rdzvBackend: c10d
    minReplicas: 4
    maxReplicas: 8
    maxRestarts: 3
    
  pytorchReplicaSpecs:
    Worker:
      replicas: 4
      restartPolicy: OnFailure
      template:
        spec:
          containers:
          - name: pytorch
            image: nvcr.io/nvidia/pytorch:24.01-py3
            imagePullPolicy: Always
            
            resources:
              limits:
                nvidia.com/gpu: 8
                rdma/rdma_shared_device_a: 1   # RDMA设备
                
            env:
            # torchrun Configuration
            - name: MASTER_ADDR
              valueFrom:
                fieldRef:
                  fieldPath: status.podIP
            - name: NPROC_PER_NODE
              value: "8"
              
            # Performance Optimization
            - name: OMP_NUM_THREADS
              value: "8"
            - name: MKL_NUM_THREADS
              value: "8"
            - name: NCCL_SOCKET_IFNAME
              value: "eth0"
              
            volumeMounts:
            - name: shm
              mountPath: /dev/shm
              
          volumes:
          - name: shm
            emptyDir:
              medium: Memory
              sizeLimit: "128Gi"
              
          # Topology Affinity
          affinity:
            podAntiAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
              - labelSelector:
                  matchLabels:
                    training.kubeflow.org/job-name: distributed-training
                topologyKey: kubernetes.io/hostname
```

---


## 8. Quick Reference (Quick Reference)

### 8.1 GPU Resource Types

```bash
# Whole Card Resources
nvidia.com/gpu: 1

# MIG Resources (A100/H100)
nvidia.com/mig-1g.10gb: 1
nvidia.com/mig-2g.20gb: 1
nvidia.com/mig-3g.40gb: 1
nvidia.com/mig-4g.40gb: 1
nvidia.com/mig-7g.80gb: 1

# Time-Slicing (Virtual Slicing)
nvidia.com/gpu: 1  # 实际为1/N物理卡
```

### 8.2 Common kubectl Commands

``` bash
# 🟢 Low Risk: Read-Only/Information Collection, Typically No Side Effects
# View GPU Nodes
kubectl get nodes -l nvidia.com/gpu.present=true

# View GPU Allocation
kubectl describe node <node> | grep -A 5 "nvidia.com/gpu"

# View GPU Pod
kubectl get pods -A -o wide --field-selector spec.nodeName=<gpu-node>

# GPU Operator Status
kubectl get clusterpolicy

# MIG Configuration Status
kubectl get nodes -L nvidia.com/mig.config

# Device Plugin Log
kubectl logs -n gpu-operator -l app=nvidia-device-plugin-daemonset --tail=100
```
---

**GPU Management Principles**: Reasonably partition resources → Monitor utilization →in time handle XID errors → Regular health checks

---

**Table bottom marks**: Kusheet Project, author Allen Galler (allengaller@gmail.com)

---


## Obsidian Related Documentation

- domain-11-ai-infra MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Open Source Project Index
- AI Infrastructure Architecture
- 132 - AI/ML Workload Operations (AI/ML Workloads Operations)
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management
- AI Model Deployment and Lifecycle Management

## Related

- [[README]]
- [[MOC]]

- AI Infrastructure Architecture
- Distributed Training Framework
- Related Knowledge Domain: domain-02-workloads-applications
- Related Knowledge Domain: domain-03-networking-traffic
- [[domain-17-system-foundation/topic-cheat-sheet/go.md|Cheat Sheet: go]]
- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Knowledge Graph Index]]

## See Also

- 01-ai-infrastructure-overview
- 02-ai-ml-workloads
- 04-gpu-monitoring-dcgm
- 05-distributed-training-frameworks


<!-- risk-assessed -->
