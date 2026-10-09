---
title: AI Infrastructure Architecture
description: 'Comprehensive introduction to the architecture design of AI Infrastructure on K8s: GPU scheduling, distributed training (PyTorch DDP/FSDP/TensorRT), LLM inference (vLLM/TGI/KServe), vector databases, and RAG'
  summary: 'Comprehensive introduction to the architecture design of AI Infrastructure on K8s: GPU scheduling, distributed training (PyTorch DDP/FSDP/TensorRT), LLM inference (vLLM/TGI/KServe), vector databases, and RAG'
summary: Comprehensive introduction to the architecture design of AI Infrastructure on K8s: GPU scheduling, distributed training (PyTorch DDP/FSDP/TensorRT), LLM
  Reasoning (vLLM/TGI/KServe), Vector Databases, and RAG
category: domain-11-ai-infra
tags:
- k8s
- ai
- gpu
- inference
- training
- llm
- rag
- vector-database
- kubeflow
- etcd
tier: peripheral
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
- What is AI Infrastructure Architecture
- How to design AI Infrastructure Architecture
- Kubernetes 11 ai infra best practices
trigger_keywords:
- AI
- Infrastructure Architecture
- ai
- infra
prerequisites:
- kubectl-basics
- helm-basics
- etcd-basics
- redis-basics
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
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
related_docs:
- path: 03-gpu-scheduling-management.md
  type: depth
  desc: GPU Scheduling and Management
- path: 05-distributed-training-frameworks.md
  type: depth
  desc: Distributed Training Framework
- path: ../domain-14-ai-ml-infra/02-ai-agents/
  type: ai-agent
  desc: AI Agent Engineering
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/01-ai-infrastructure-overview.md
---

> **Production Environment Security Reminders**
>
> Commands included in this document are executable directly. Before executing, please confirm: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk levels for commands are marked: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# AI Infrastructure Architecture

> **Applicable Version**: v1.25 - v1.32 \|\| **Last Updated**: 2026-01 \|\| **Reference**: [NVIDIA AI Enterprise](https://www.nvidia.com/en-us/data-center/products/ai-enterprise/) \|\| [[entities/kubeflow.md|Kubeflow]]](https://www.kubeflow.org/)


## AI Infra Overview Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     AI platform control plane                               │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  Kubernetes Control Plane (API Server/Scheduler/etcd)   │  │
│  └──────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  AI scheduler layer: Volcano / Kueue / YuniKorn                    │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              v
┌─────────────────────────────────────────────────────────────────┐
│                     Compute resource layer                                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  GPU cluster     │  │  NPU cluster     │  │  RDMA network    │         │
│  │  A100/H100   │  │  Ascend 910B    │  │  InfiniBand  │         │
│  │  (node pool)    │  │  (node pool)    │  │  RoCE        │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              v
┌─────────────────────────────────────────────────────────────────┐
│                     AI workload orchestration layer                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐               │
│  │ Training framework   │  │ Inference engine   │  │ Data processing   │               │
│  │ PyTorch    │  │ vLLM       │  │ Ray        │               │
│  │ DeepSpeed  │  │ TensorRT   │  │ Spark      │               │
│  │ Megatron   │  │ Triton     │  │ Flink      │               │
│  └────────────┘  └────────────┘  └────────────┘               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              v
┌─────────────────────────────────────────────────────────────────┐
│                     Storage and data layer                                  │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐               │
│  │ Object storage   │  │ Vector database │  │ Feature storage   │               │
│  │ S3/OSS     │  │ Milvus     │  │ Feast      │               │
│  │ (model/data)│  │ Weaviate   │  │ Tecton     │               │
│  └────────────┘  └────────────┘  └────────────┘               │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐               │
│  │ Distributed storage │  │ Cache layer     │  │ Data lake     │               │
│  │ JuiceFS    │  │ Alluxio    │  │ Iceberg    │               │
│  │ CephFS     │  │ Fluid      │  │ Hudi       │               │
│  └────────────┘  └────────────┘  └────────────┘               │
└─────────────────────────────────────────────────────────────────┘
                              │
                              v
┌─────────────────────────────────────────────────────────────────┐
│                     Observability and governance layer                              │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐               │
│  │ Experiment tracking   │  │ Model management   │  │ Data lineage   │               │
│  │ MLflow     │  │ ModelMesh  │  │ DataHub    │               │
│  │ W&B        │  │ Seldon     │  │ Amundsen   │               │
│  └────────────┘  └────────────┘  └────────────┘               │
└─────────────────────────────────────────────────────────────────┘
```

---


## 1. Comparison of Dedicated Schedulers for AI

### Scheduler Selection Matrix

| Scheduler | Gang Scheduling | Queue Management | Priority Preemption | GPU Topology Awareness | Maturity | Production Recommendation |
|-------|---------|---------|-----------|------------|--------|---------|
| **Volcano** | ✅ | ✅ | ✅ | ✅ | ⭐⭐⭐⭐⭐ | Strongly Recommended |
| **Kueue** | ✅ | ✅ | ✅ | ⚠️ Partial | ⭐⭐⭐⭐ | Recommended |
| **YuniKorn** | ✅ | ✅ | ✅ | ❌ | ⭐⭐⭐ | Scenario-Specific |
| **Native K8s Scheduler** | ❌ | ❌ | ✅ | ❌ | ⭐⭐⭐⭐⭐ | Not Recommended for AI |

---

### 1. Volcano - Dedicated AI Scheduler

#### Core Features

**Gang Scheduling**
- Ensure that distributed training tasks are scheduled simultaneously across multiple nodes
- Avoid resource deadlocks and partial failures
- Support configuration of minimum member number

**Queue Management**
- Multi-tenant resource quotas
- Priority queues
- Fair scheduling strategies

**GPU Topology Awareness**
- Optimize NVLink topology
- PCIe affinity scheduling
- NUMA awareness

#### Helm Installation

> ⚠️ **🟡 Medium Risk Changes** — Change cluster resource states, recommend to first use --dry-run or diff to confirm
> - `helm upgrade/install`: deploy/upgrade release

``` bash
# 🔴 Medium Risk: modifies cluster/resource status; confirm target, impact scope, and authorization before proceeding
helm repo add volcano-sh https://volcano-sh.github.io/helm-charts
helm install volcano volcano-sh/volcano \
  --namespace volcano-system \
  --create-namespace \
  --set basic.image_tag_version=v1.8.2
```
#### Queue Configuration

```yaml
apiVersion: scheduling.volcano.sh/v1beta1
kind: Queue
metadata:
  name: ai-training
spec:
  # resource quota
  capability:
    cpu: "1000"
    memory: 2Ti
    nvidia.com/gpu: "64"
  
  # weight (relative priority)
  weight: 100
  
  # guaranteed resources (resource assurance)
  guarantee:
    cpu: "500"
    memory: 1Ti
    nvidia.com/gpu: "32"
  
  # queue state
  state: Open
  
  # recycling strategy
  reclaimable: true
---
apiVersion: scheduling.volcano.sh/v1beta1
kind: Queue
metadata:
  name: ai-inference
spec:
  capability:
    cpu: "500"
    memory: 1Ti
    nvidia.com/gpu: "32"
  weight: 80
  guarantee:
    cpu: "200"
    memory: 512Gi
    nvidia.com/gpu: "16"
  state: Open
```

#### PyTorchJob Gang Scheduling

```yaml
apiVersion: kubeflow.org/v1
kind: PyTorchJob
metadata:
  name: distributed-training
  namespace: ai-training
spec:
  # Volcano scheduler
  schedulerName: volcano
  
  pytorchReplicaSpecs:
    Master:
      replicas: 1
      template:
        metadata:
          annotations:
            # Gang scheduling configuration
            scheduling.volcano.sh/group-name: distributed-training
            scheduling.volcano.sh/queue-name: ai-training
        spec:
          containers:
            - name: pytorch
              image: pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime
              command:
                - python
                - -m
                - torch.distributed.launch
                - --nproc_per_node=8
                - train.py
              resources:
                limits:
                  nvidia.com/gpu: 8
                requests:
                  nvidia.com/gpu: 8
          # GPU topology affinity
          affinity:
            nodeAffinity:
              requiredDuringSchedulingIgnoredDuringExecution:
                nodeSelectorTerms:
                  - matchExpressions:
                      - key: nvidia.com/gpu.product
                        operator: In
                        values: ["NVIDIA-A100-SXM4-80GB"]
    
    Worker:
      replicas: 7
      template:
        metadata:
          annotations:
            scheduling.volcano.sh/group-name: distributed-training
            scheduling.volcano.sh/queue-name: ai-training
        spec:
          containers:
            - name: pytorch
              image: pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime
              command:
                - python
                - -m
                - torch.distributed.launch
                - --nproc_per_node=8
                - train.py
              resources:
                limits:
                  nvidia.com/gpu: 8
                requests:
                  nvidia.com/gpu: 8
```

---

### 2. Kueue - Batch Scheduling Native to Kubernetes

#### Architectural Advantages

- K8s native CRD, no additional components required
- Deeply integrated with K8s scheduler
- Supports multiple workloads (Job/PyTorchJob/RayJob)

#### ClusterQueue Configuration

```yaml
apiVersion: kueue.x-k8s.io/v1beta1
kind: ResourceFlavor
metadata:
  name: gpu-a100
spec:
  nodeLabels:
    nvidia.com/gpu.product: NVIDIA-A100-SXM4-80GB
---
apiVersion: kueue.x-k8s.io/v1beta1
kind: ClusterQueue
metadata:
  name: cluster-queue-training
spec:
  namespaceSelector: {}
  
  # resource quota
  resourceGroups:
    - coveredResources: ["cpu", "memory", "nvidia.com/gpu"]
      flavors:
        - name: gpu-a100
          resources:
            - name: cpu
              nominalQuota: 1000
            - name: memory
              nominalQuota: 2Ti
            - name: nvidia.com/gpu
              nominalQuota: 64
              borrowingLimit: 16  # 可借用16个GPU
  
  # Preemption Strategy
  preemption:
    reclaimWithinCohort: Any
    withinClusterQueue: LowerPriority
---
apiVersion: kueue.x-k8s.io/v1beta1
kind: LocalQueue
metadata:
  name: training-queue
  namespace: ai-training
spec:
  clusterQueue: cluster-queue-training
```

#### Workload Adaptation

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: training-job
  namespace: ai-training
  labels:
    kueue.x-k8s.io/queue-name: training-queue  # 关联队列
spec:
  parallelism: 8
  completions: 8
  template:
    spec:
      containers:
        - name: trainer
          image: pytorch/pytorch:2.1.0
          resources:
            requests:
              nvidia.com/gpu: 1
            limits:
              nvidia.com/gpu: 1
      restartPolicy: OnFailure
```

---


## 2. Advanced GPU Resource Management

### Comparison of GPU Sharing Solutions

| Solution | Isolation Level | Memory Isolation | Performance Overhead | Complexity | Applicable Scenarios |
|------|---------|---------|---------|--------|---------|
| **NVIDIA MIG** | Hardware Level | Complete Isolation | 0% | Low | Multi-tenant for A100/H100 |
| **vGPU** | Hardware Level | Complete Isolation | <5% | Medium | Virtualized environments |
| **Time-Slicing** | Process Level | Soft Isolation | 5-10% | Low | Inference services |
| **cGPU(Alibaba Cloud)** | Process Level | Complete Isolation | <3% | Low | Recommended by ACK |
| **vCUDA** | Process Level | Soft Isolation | 10-15% | High | Test environments |

---

### 1. NVIDIA MIG Configuration

#### MIG Instance Partitioning

```bash
# Check MIG support
nvidia-smi mig -lgip

# Create MIG instance (7 x 1g.10gb instances)
nvidia-smi mig -cgi 19,19,19,19,19,19,19 -C

# Check MIG instance
nvidia-smi mig -lgi

# Example output:
# +----+--------+------+
# | ID | Memory | SMs |
# +====+========+======+
# |  0 | 10240  |  14  |
# |  1 | 10240  |  14  |
# ...
```

#### Kubernetes Device Plugin Configuration

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nvidia-device-plugin-config
  namespace: kube-system
data:
  config.yaml: |
    version: v1
    sharing:
      timeSlicing:
        renameByDefault: false
        failRequestsGreaterThanOne: false
        resources:
          - name: nvidia.com/gpu
            replicas: 10  # 单GPU虚拟10个
    
    # MIG policy
    flags:
      migStrategy: mixed  # single/mixed
      failOnInitError: true
    
    # MIG device naming
    resources:
      gpus:
        - pattern: "*"
          name: nvidia.com/gpu
      mig:
        - pattern: "1g.10gb"
          name: nvidia.com/mig-1g.10gb
        - pattern: "2g.20gb"
          name: nvidia.com/mig-2g.20gb
        - pattern: "3g.40gb"
          name: nvidia.com/mig-3g.40gb
```

#### MIG Instance Usage

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mig-workload
spec:
  containers:
    - name: cuda-app
      image: nvidia/cuda:12.2.0-base-ubuntu22.04
      command: ["nvidia-smi"]
      resources:
        limits:
          nvidia.com/mig-1g.10gb: 1  # 请求1个MIG实例
```

---

### 2. GPU Time-Slicing (Time Slicing)

#### Configuration Example

```yaml
# nvidia-device-plugin-config ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: nvidia-device-plugin-config
  namespace: kube-system
data:
  config.yaml: |
    version: v1
    sharing:
      timeSlicing:
        renameByDefault: false
        resources:
          - name: nvidia.com/gpu
            replicas: 8  # 单GPU虚拟为8个逻辑GPU
```

#### Pod Usage

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: shared-gpu-pod-1
spec:
  containers:
    - name: inference
      image: pytorch/pytorch:2.1.0
      resources:
        limits:
          nvidia.com/gpu: 1  # 实际使用1/8物理GPU
```

**Applicable Scenarios**:
- Inference services (low concurrency)
- Development/test environments
- Jupyter Notebook

**Limitations**:
- No memory isolation (OOM can affect other containers)
- Performance fluctuations (competition for time slices)

---

### 3. cGPU(Aliyun Container GPU)

#### Core Advantages

- **Memory Isolation**: Kernel-level memory isolation, OOM does not affect each other
- **Compute Isolation**: cgroup limits GPU compute power
- **Zero Modification**: Application code does not need to be modified
- **cost reduction**: single GPU supports 10+ inference containers

#### ACK Configuration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cgpu-inference
spec:
  replicas: 20
  template:
    spec:
      containers:
        - name: model-server
          image: registry.cn-hangzhou.aliyuncs.com/acs/vllm:latest
          resources:
            limits:
              aliyun.com/gpu-mem: 8  # 申请8GB显存
              aliyun.com/gpu-core: 30  # 申请30%算力
          env:
            - name: CUDA_VISIBLE_DEVICES
              value: "0"
```

#### Monitoring Metrics

``` bash
# 🔲 Low Risk: read-only/information gathering, typically with no side effects
# Check cGPU usage
kubectl get nodes -o custom-columns=NAME:.metadata.name,GPU-MEM:.status.allocatable.'aliyun\.com/gpu-mem',GPU-CORE:.status.allocatable.'aliyun\.com/gpu-core'
```
---


## 3. High-Speed Network Solution

### RDMA Network Comparison

| Solution | Bandwidth | Latency | Cost | Deployment Complexity | AI Training Recommendation |
|------|------|------|------|-----------|-----------|
| **InfiniBand** | 400Gb/s | <1μs | High | High | ⭐⭐⭐⭐⭐ |
| **RoCE v2** | 100-400Gb/s | <5μs | Medium | Medium | ⭐⭐⭐⭐ |
| **TCP/IP** | 10-100Gb/s | 50-100μs | Low | Low | ⚠️ Not recommended for large-scale training |

---

### 1. RoCE Configuration(Aliyun ACK)

#### Node Configuration

```yaml
# RDMA device plugin DaemonSet
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: rdma-device-plugin
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: rdma-device-plugin
  template:
    metadata:
      labels:
        app: rdma-device-plugin
    spec:
      hostNetwork: true
      containers:
        - name: rdma-device-plugin
          image: mellanox/k8s-rdma-shared-dev-plugin:latest
          securityContext:
            privileged: true
          volumeMounts:
            - name: device-plugin
              mountPath: /var/lib/kubelet/device-plugins
            - name: sys
              mountPath: /sys
      volumes:
        - name: device-plugin
          hostPath:
            path: /var/lib/kubelet/device-plugins
        - name: sys
          hostPath:
            path: /sys
```

#### Pod Usage RDMA

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: rdma-training
  annotations:
    k8s.v1.cni.cncf.io/networks: rdma-network
spec:
  containers:
    - name: pytorch
      image: pytorch/pytorch:2.1.0
      command:
        - python
        - -m
        - torch.distributed.launch
        - --use_env
        - train.py
      resources:
        limits:
          rdma/rdma_shared_device: 1  # 请求RDMA设备
          nvidia.com/gpu: 8
      env:
        - name: NCCL_IB_DISABLE
          value: "0"  # 启用InfiniBand/RoCE
        - name: NCCL_DEBUG
          value: "INFO"
```

---

### 2. NCCL Optimization Configuration

```bash
# Optimize NCCL Environment Variables
export NCCL_SOCKET_IFNAME=eth0
export NCCL_IB_DISABLE=0
export NCCL_IB_HCA=mlx5_0,mlx5_1
export NCCL_IB_GID_INDEX=3
export NCCL_NET_GDR_LEVEL=5
export NCCL_P2P_LEVEL=SYS

# Perform NCCL Performance Testing
/usr/local/bin/nccl-tests/build/all_reduce_perf -b 8 -e 128M -f 2 -g 8
```

**Performance Benchmarks**:
- TCP/IP: ~10GB/s
- RoCE: ~40-50GB/s
- InfiniBand: ~90-100GB/s

---


## 4. Distributed Storage Solutions

### 1. JuiceFS - Distributed File System

| Solution | Throughput | IOPS | Latency | Cost | AI Training Recommendation |
|------|--------|------|------|------|-----------|
| **Local NVMe** | 7GB/s | 1M | <100μs | High | ⭐⭐⭐⭐⭐ Checkpoint |
| **JuiceFS** | 2-5GB/s | 100K | 1-5ms | Medium | ⭐⭐⭐⭐⭐ Dataset |
| **CephFS** | 1-3GB/s | 50K | 5-10ms | Medium | ⭐⭐⭐⭐ Shared Storage |
| **Object Storage (S3/OSS)** | 500MB/s | 10K | 10-50ms | Low | ⭐⭐⭐ Model Archival |
| **NFS** | 500MB/s | 5K | 10-20ms | Low | ⚠️ Not recommended for training |

---

### 1. JuiceFS - Distributed File System

#### Helm Deployment

- **POSIX compatible**: standard file system interface
- **object storage backend**: S3/OSS/MinIO
- **Metadata separation**: Redis/TiKV/etcd
- **Cache acceleration**: local SSD cache

#### Helm Deployment

> ⚠️ **yellow warning** — change cluster resource state, recommend to first use --dry-run or diff to confirm
> - `helm upgrade/install`: deploy/upgrade release

``` bash
# 🟡 Medium Risk: Modifies cluster/resource states; confirm target, impact scope, and authorization before execution
helm repo add juicefs https://juicedata.github.io/charts/
helm install juicefs-csi-driver juicefs/juicefs-csi-driver \
  --namespace kube-system \
  --set storageClasses[0].enabled=true \
  --set storageClasses[0].name=juicefs \
  --set storageClasses[0].backend.name=minio \
  --set storageClasses[0].backend.metaurl="redis://redis:6379/1" \
  --set storageClasses[0].backend.storage=s3 \
  --set storageClasses[0].backend.bucket=http://minio:9000/juicefs
```
#### StorageClass Configuration

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: juicefs-sc
provisioner: csi.juicefs.com
parameters:
  csi.storage.k8s.io/provisioner-secret-name: juicefs-secret
  csi.storage.k8s.io/provisioner-secret-namespace: kube-system
  csi.storage.k8s.io/node-publish-secret-name: juicefs-secret
  csi.storage.k8s.io/node-publish-secret-namespace: kube-system
  
  # Cache Configuration (Critical)
  juicefs/mount-cache-size: "102400"  # 100GB本地缓存
  juicefs/mount-cache-dir: "/var/jfsCache"
  juicefs/mount-prefetch: "1"  # 预读优化
  
  # Performance Tuning
  juicefs/mount-buffer-size: "300"  # 300MB写缓冲
  juicefs/mount-max-uploads: "50"  # 并发上传数
```

#### PVC Usage

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: training-data
  namespace: ai-training
spec:
  accessModes:
    - ReadWriteMany  # 多Pod共享
  storageClassName: juicefs-sc
  resources:
    requests:
      storage: 10Ti
---
apiVersion: v1
kind: Pod
metadata:
  name: data-loader
spec:
  containers:
    - name: loader
      image: pytorch/pytorch:2.1.0
      volumeMounts:
        - name: data
          mountPath: /data
      command:
        - python
        - data_loader.py
  volumes:
    - name: data
      persistentVolumeClaim:
        claimName: training-data
```

---

### 2. Fluid - Data Orchestration Acceleration

#### Architecture Value

- **Data preheating**: cache data on nodes before training
- **Affinity scheduling**: schedule pods to nodes with caches
- **multi-layer caching**: memory+SSD+remote storage

#### Alluxio Runtime Configuration

```yaml
apiVersion: data.fluid.io/v1alpha1
kind: Dataset
metadata:
  name: imagenet
  namespace: ai-training
spec:
  mounts:
    - mountPoint: s3://my-bucket/imagenet/
      name: imagenet
      options:
        s3a.endpoint: oss-cn-hangzhou.aliyuncs.com
        s3a.access.key: <ACCESS_KEY>
        s3a.secret.key: <SECRET_KEY>
  
  # Data Placement Strategy
  placement: Exclusive  # 独占节点缓存
---
apiVersion: data.fluid.io/v1alpha1
kind: AlluxioRuntime
metadata:
  name: imagenet
  namespace: ai-training
spec:
  replicas: 4  # 4个缓存节点
  
  # Master Configuration
  master:
    jvmOptions:
      - "-Xmx16G"
      - "-Xms16G"
    resources:
      requests:
        cpu: 4
        memory: 20Gi
  
  # Worker Configuration
  worker:
    jvmOptions:
      - "-Xmx32G"
      - "-Xms32G"
    resources:
      requests:
        cpu: 8
        memory: 40Gi
  
  # Cache Hierarchy
  tieredstore:
    levels:
      - mediumtype: MEM
        path: /dev/shm
        quota: 30Gi  # 内存缓存30GB
        high: 0.95
        low: 0.7
      - mediumtype: SSD
        path: /var/lib/alluxio
        quota: 500Gi  # SSD缓存500GB
        high: 0.95
        low: 0.7
  
  # Data Warmup
  data:
    replicas: 2  # 2副本
    pin: true  # 常驻内存
```

#### Data Warm-Up Job

```yaml
apiVersion: data.fluid.io/v1alpha1
kind: DataLoad
metadata:
  name: imagenet-preload
  namespace: ai-training
spec:
  dataset:
    name: imagenet
    namespace: ai-training
  
  loadMetadata: true
  
  # Warmup Strategy
  target:
    - path: /train
      replicas: 2  # 训练集2副本
    - path: /val
      replicas: 1  # 验证集1副本
```

---


## 5. AI Platform Component Ecosystem

### MLOps Toolchain

| **stage** | **tool** | **function** | **integration difficulty** | **recommendation** |
|------|------|------|---------|--------|
| **experiment tracking** | MLflow | parameters/metrics/model versions | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **experiment tracking** | Weights & Biases | visualization/collaboration | ⭐ | ⭐⭐⭐⭐ |
| **feature storage** | Feast | feature management | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| **model serving** | [[KServe|KServe]] | inference service | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **workflow** | Kubeflow Pipelines | DAG orchestration | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **workflow** | [[Argo|Argo]] Workflows]] | Argo Workflows]] | general workflow | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **automl** | Katib | hyperparameter tuning | ⭐⭐⭐ | ⭐⭐⭐ |

---

### 1. MLflow on K8s

#### Deployment Architecture

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mlflow-server
  namespace: mlops
spec:
  replicas: 2
  selector:
    matchLabels:
      app: mlflow
  template:
    metadata:
      labels:
        app: mlflow
    spec:
      containers:
        - name: mlflow
          image: ghcr.io/mlflow/mlflow:v2.9.2
          args:
            - server
            - --host=0.0.0.0
            - --port=5000
            - --backend-store-uri=postgresql://mlflow:password@postgres:5432/mlflow
            - --default-artifact-root=s3://mlflow-artifacts/
          env:
            - name: AWS_ACCESS_KEY_ID
              valueFrom:
                secretKeyRef:
                  name: s3-credentials
                  key: access-key
            - name: AWS_SECRET_ACCESS_KEY
              valueFrom:
                secretKeyRef:
                  name: s3-credentials
                  key: secret-key
          ports:
            - containerPort: 5000
          resources:
            requests:
              cpu: 1000m
              memory: 2Gi
            limits:
              cpu: 2000m
              memory: 4Gi
---
apiVersion: v1
kind: Service
metadata:
  name: mlflow-service
  namespace: mlops
spec:
  selector:
    app: mlflow
  ports:
    - port: 5000
      targetPort: 5000
  type: LoadBalancer
```

#### Training Code Integration

```python
import mlflow
import mlflow.pytorch

# MLflow Tracking Configuration
mlflow.set_tracking_uri("http://mlflow-service.mlops:5000")
mlflow.set_experiment("llama2-finetuning")

with mlflow.start_run():
    # Record Parameters
    mlflow.log_params({
        "learning_rate": 2e-5,
        "batch_size": 32,
        "epochs": 3,
        "model": "meta-llama/Llama-2-7b"
    })
    
    # Training Loop
    for epoch in range(3):
        loss = train_one_epoch()
        
        # Record Metrics
        mlflow.log_metrics({
            "train_loss": loss,
            "epoch": epoch
        }, step=epoch)
    
    # Record Model
    mlflow.pytorch.log_model(model, "model")
    
    # Record artifacts
    mlflow.log_artifact("training_curve.png")
```

---

### 2. KServe - Model Serving Service

#### InferenceService Configuration

```yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: llama2-7b
  namespace: ai-inference
spec:
  predictor:
    # Minimum Replicas
    minReplicas: 2
    maxReplicas: 10
    
    # Auto-scaling
    scaleTarget: 80  # 80%并发利用率触发扩容
    scaleMetric: concurrency
    
    # GPU Resources
    resources:
      requests:
        cpu: 4
        memory: 16Gi
        nvidia.com/gpu: 1
      limits:
        cpu: 8
        memory: 32Gi
        nvidia.com/gpu: 1
    
    # Container configuration
    containers:
      - name: kserve-container
        image: vllm/vllm-openai:latest
        args:
          - --model=/mnt/models/llama2-7b
          - --tensor-parallel-size=1
          - --max-num-seqs=256
        volumeMounts:
          - name: model-storage
            mountPath: /mnt/models
    
    volumes:
      - name: model-storage
        persistentVolumeClaim:
          claimName: model-pvc
  
  # Traffic splitting (canary)
  canaryTrafficPercent: 10
```

---


## 6. AI Infrastructure Cost Optimization

### Cost Optimization Strategy Matrix

| **strategy** | saving ratio | implementation difficulty | risk | recommended scenarios |
|------|---------|---------|------|---------|
| **spot instances** | 70-90% | ⭐⭐ | interruption risk | fault-tolerant training |
| **gpu sharing** | 60-80% | ⭐⭐⭐ | performance fluctuations | inference service |
| **model compression** | 50-75% | ⭐⭐⭐⭐ | accuracy loss | edge deployment |
| **data caching** | 30-50% | ⭐⭐ | cache hit rate | repeated training |
| **resource sizing** | 20-40% | ⭐⭐⭐ | need monitoring adjustment | all scenarios |
| **batch inference** | 40-60% | ⭐⭐ | increased latency | offline scenarios |

---

### Spot Instance Configuration

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: spot-training
spec:
  # Tolerate Spot interruptions
  tolerations:
    - key: "kubernetes.azure.com/scalesetpriority"
      operator: "Equal"
      value: "spot"
      effect: "NoSchedule"
  
  # Node affinity
  affinity:
    nodeAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
        nodeSelectorTerms:
          - matchExpressions:
              - key: "kubernetes.azure.com/scalesetpriority"
                operator: In
                values: ["spot"]
  
  containers:
    - name: pytorch
      image: pytorch/pytorch:2.1.0
      command:
        - python
        - train.py
        - --checkpoint-interval=100  # 频繁检查点
      resources:
        limits:
          nvidia.com/gpu: 8
```

---


## 7. Production Best Practices

### AI Infrastructure Checklist

#### Compute Resources

- ✅ GPU node pool isolation(training/inference)
- ✅ configure GPU topology affinity
- ✅ enable Gang scheduling(Volcano/Kueue)
- ✅ configure resource quotas and priorities
- ✅ Deploy GPU monitoring (DCGM Exporter)

#### Network

- ✅ Enable RDMA (RoCE/InfiniBand)
- ✅ Configure NCCL optimization parameters
- ✅ Network bandwidth monitoring
- ✅ Configure QoS to ensure training traffic

#### Storage

- ✅ Use high-performance storage (JuiceFS/Alluxio)
- ✅ Configure data pre-warming
- ✅ Local NVMe cache checkpointing
- ✅ Archive models in object storage

#### Observability

- ✅ Experiment tracking (MLflow)
- ✅ Monitor GPU utilization
- ✅ Train task alerts
- ✅ Cost analysis dashboard

#### Security

- ✅ Model encryption storage
- ✅ Train data access control
- ✅ NetworkPolicy isolation
- ✅ Image security scanning

---

**Table Maintenance**: Kusheet Project | **Author**: Allen Galler (allengaller@gmail.com)

---


## Obsidian Related Documentation

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Open Source Project Index
- 132 - AI/ML Workloads (AI/ML Workloads Operations)
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipelines and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management
- AI Model Deployment and Lifecycle Management

## Related

- [[README]]
- [[README]]
- [[README]]
- [[MOC]]

- GPU Scheduling and Management
- Distributed Training Frameworks
- Related Knowledge Domain: domain-02-workloads-applications
- Related Knowledge Domain: domain-03-networking-traffic
- [[domain-17-system-foundation/topic-cheat-sheet/go.md|Cheat Sheet: go]]
- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Knowledge Graph Index]]

## See Also

- 37-agent-sandbox-security
- 99-kubeflow-ai-platform-guide
- 02-ai-ml-workloads
- 03-gpu-scheduling-management

```

<!-- risk-assessed -->
