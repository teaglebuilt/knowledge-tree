---
title: 141 - AI Cost Analysis & FinOps Practice (AI Cost Analysis & FinOps)
description: '# 141 - AI Cost Analysis & FinOps Practice (AI Cost Analysis & FinOps)'
summary: '"stage3_param_persistence_threshold": 1e5'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- prometheus
- grafana
- helm
- job
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
- What is AI Cost Analysis & FinOps Practice (AI Cost Analysis & FinOps)
- How to AI Cost Analysis & FinOps Practice (AI Cost Analysis & FinOps)
- Kubernetes 11 AI infra Best Practices
trigger_keywords:
- AI Cost Analysis & FinOps Practice
- AI
- Cost
- Analysis
- FinOps
- ai
- infra
prerequisites:
- kubectl-basics
- helm-basics
- prometheus-basics
- monitoring-basics
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
  path: ../domain-02-workloads-applications/
  label: 'Related Knowledge Domain: domain-02-workloads-applications'
- type: domain
  path: ../domain-03-networking-traffic/
  label: 'Related Knowledge Domain: domain-03-networking-traffic'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/12-ai-cost-analysis-finops.md
---

> **Production Environment Security Tips**
>
> Commands included in this document can be directly executed. Before executing, please confirm: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information collection with no side effects).




# 141 - AI cost analysis and FinOps practice (AI Cost Analysis & FinOps)

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25-v1.32 | **Last Updated**: 2026-01 | **Reference**: [FinOps Foundation](https://www.finops.org/)

---


## 1. Cost Structure Overview

### 1.1 Cost Composition Analysis

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AI/ML Infrastructure Cost Breakdown                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  Compute cost (Compute) 60-75%                                           │  │
│  │  ├── NVIDIA GPU instance (A100/H100/L40S)                    45-55%             │  │
│  │  ├── CPU instance (data processing/scheduling)                      10-15%             │  │
│  │  └── Spot/Preemptible instance                        5-10%              │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  Storage cost (Storage) 15-25%                                           │  │
│  │  ├── Object storage (S3/GCS/OSS)                       8-12%              │  │
│  │  ├── High-performance SSD storage                          5-8%               │  │
│  │  └── NFS/Lustre/GPFS file storage                  2-5%               │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  Network cost (Network) 5-10%                                            │  │
│  │  ├── Cross-region/AZ transmission                             3-5%               │  │
│  │  ├── Public network outbound traffic                      1-3%               │  │
│  │  └── Dedicated line/VPN                                    1-2%               │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  Other costs (Others) 5-10%                                             │  │
│  │  ├── Monitoring/log/APM                               2-3%               │  │
│  │  ├── Backup/disaster recovery                           1-2%               │  │
│  │  └── Software license                                  2-5%               │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Cost Distribution by Stage

| Stage | Compute percentage wo percentage wo percentage | Storage percentage ratio | Network percentage share | Features |
|-----|---------|---------|---------|------|
| **Data Preparation** | 30% | 55% | 15% | I/O-intensive, large data migration |
| **Model Training** | 85% | 10% | 5% | GPU-intensive, frequent checkpoints |
| **Model Fine-tuning** | 75% | 15% | 10% | Moderate GPU demand |
| **Model Inference** | 70% | 10% | 20% | Stable GPU, high network throughput |
| **MLOps Platform** | 40% | 30% | 30% | Metadata/model repository |

---


## 2. GPU Instance Cost Comparison

### 2.1 Pricing of Mainstream Cloud Vendor GPU Instances

| GPU Model | Memory | AWS On-Demand | AWS Spot | GCP On-Demand | Azure On-Demand | Alibaba Cloud |
|--------|------|---------------|----------|---------------|-----------------|-------|
| **H100 80GB** | 80GB | $32.77/h | ~$12/h | $37.20/h | $31.58/h | ¥185/h |
| **A100 80GB** | 80GB | $32.77/h | ~$10/h | $25.20/h | $24.48/h | ¥120/h |
| **A100 40GB** | 40GB | $19.50/h | ~$6/h | $15.12/h | $14.69/h | ¥85/h |
| **A10G 24GB** | 24GB | $1.006/h | ~$0.30/h | $1.02/h | $0.90/h | ¥12/h |
| **L4 24GB** | 24GB | $0.81/h | ~$0.25/h | $0.72/h | $0.85/h | ¥10/h |
| **T4 16GB** | 16GB | $0.526/h | ~$0.16/h | $0.35/h | $0.45/h | ¥5/h |
| **V100 32GB** | 32GB | $3.06/h | ~$0.92/h | $2.48/h | $2.48/h | ¥35/h |

### 2.2 Guide to Selecting GPUs for Training Tasks

| Model Size | Recommended GPU | Quantity | Estimated training cost/day | Applicable scenarios |
|---------|--------|------|----------------|---------|
| **<1B parameters** | A10G/L4 | 1-4 | $25-100 | Small models/fine-tuning |
| **1-7B parameters** | A100 40GB | 4-8 | $400-800 | Medium-sized LLMs |
| **7-13B parameters** | A100 80GB | 8-16 | $1,500-3,000 | Large model fine-tuning |
| **13-70B parameters** | A100 80GB/H100 | 32-64 | $6,000-15,000 | Large-scale pre-training models |
| **>70B parameters** | H100 | 128-512 | $50,000+ | Super-large-scale pre-training |

### 2.3 Guide to Selecting GPUs for Inference Services

| Model Type | Recommended GPU | QPS/GPU | Cost/1M tokens | Applicable scenarios |
|---------|--------|--------|---------------|---------|
| **7B Quantized Model** | T4/L4 | 50-100 | $0.05-0.10 | Low-cost online services |
| **13B Quantized Model** | A10G/L4 | 30-60 | $0.10-0.20 | Medium-quality services |
| **70B Quantized Model** | A100 40GB | 10-20 | $0.50-1.00 | High-quality services |
| **70B FP16** | A100 80GB | 5-10 | $2.00-4.00 | Highest Quality Service |

---


## 3. FinOps Practice Framework

### 3.1 FinOps Maturity Model

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        FinOps Maturity Model                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Level 3: Optimize (Optimize)                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ • Automated cost optimization strategies                                                  │   │
│  │ • Predictive Capacity Planning                                                       │   │
│  │ • Continuous Cost Engineering                                                         │   │
│  │ • Resource Decisions Driven by ROI                                                    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ↑                                              │
│  Level 2: Operate                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ • Cost Allocation and Showback/Chargeback                                        │   │
│  │ • Budget Management and Alerts                                                       │   │
│  │ • Anomaly Detection and Analysis                                                       │   │
│  │ • Regular Cost Audits                                                         │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              ↑                                              │
│  Level 1: Inform                                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │ • Cost Visibility Establishment                                                       │   │
│  │ • Resource Tagging System                                                         │   │
│  │ • Base Cost Report                                                         │   │
│  │ • Team Cost Awareness Cultivation                                                     │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 Kubernetes Resource Label System

```yaml
# Cost Tracking Tag Specification
apiVersion: v1
kind: Pod
metadata:
  labels:
    # Business Dimension
    app.kubernetes.io/name: "llm-inference"
    app.kubernetes.io/component: "serving"
    
    # Cost Center
    cost-center: "ai-platform"
    business-unit: "search"
    project: "chatbot-v2"
    
    # Environment
    environment: "production"
    
    # Responsible Party
    owner: "ml-team"
    contact: "ml-lead@company.com"
    
    # Workload Type
    workload-type: "inference"       # training/inference/data-processing
    gpu-type: "a100"
    
    # Lifecycle
    lifecycle: "persistent"          # persistent/ephemeral/spot
    
    # Cost Priority
    cost-priority: "p1"              # p0(关键)/p1(重要)/p2(普通)/p3(可中断)
```

### 3.3 Cost Allocation Model

```yaml
# Kubecost Cost Allocation Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: kubecost-allocation
  namespace: kubecost
data:
  allocation.yaml: |
    # Shared Cost Sharing Rules
    sharedCosts:
      - name: "control-plane"
        type: "cluster"
        allocation: "proportional"  # 按资源使用比例分摊
        
      - name: "monitoring"
        type: "namespace"
        namespaces: ["monitoring", "logging"]
        allocation: "even"          # 平均分摊
        
      - name: "gpu-operator"
        type: "namespace"
        namespaces: ["gpu-operator-resources"]
        allocation: "gpu-weighted"  # 按GPU使用量分摊
    
    # Idle Resource Cost
    idleCosts:
      cpuIdleCost: 0.5              # 50%分配到用户
      gpuIdleCost: 1.0              # 100%分配到用户
      shareWithNamespaces: true
    
    # Network Cost
    networkCosts:
      enabled: true
      zoneCostMultiplier: 0.01
      regionCostMultiplier: 0.05
      internetCostMultiplier: 0.12
```

---


## 4. Cost Optimization Strategies

### 4.1 Optimization of Computing Resources

#### Spot/Preemptible Instance Strategy

```yaml
# Karpenter Spot Instance Configuration
apiVersion: karpenter.sh/v1alpha5
kind: Provisioner
metadata:
  name: gpu-spot-provisioner
spec:
  requirements:
    - key: "karpenter.sh/capacity-type"
      operator: In
      values: ["spot", "on-demand"]
    - key: "node.kubernetes.io/instance-type"
      operator: In
      values: ["p4d.24xlarge", "p3.16xlarge", "g5.48xlarge"]
  
  # Spot Instance Priority
  weight: 100
  
  # Interruption Handling
  ttlSecondsAfterEmpty: 30
  ttlSecondsUntilExpired: 86400
  
  # Hybrid Strategy: 70% Spot + 30% On-Demand
  limits:
    resources:
      nvidia.com/gpu: 100
  
  providerRef:
    name: default
    
---
# Volcano Scheduler Spot Awareness Configuration
apiVersion: scheduling.volcano.sh/v1beta1
kind: Queue
metadata:
  name: training-spot
spec:
  weight: 10
  capability:
    nvidia.com/gpu: 80
  reclaimable: true        # 可被抢占
  
  # Prioritize Spot Nodes
  nodeSelector:
    karpenter.sh/capacity-type: spot
```

#### Optimization of GPU Utilization

```yaml
# GPU Time-Slicing Configuration (Enhance Utilization)
apiVersion: v1
kind: ConfigMap
metadata:
  name: nvidia-device-plugin-config
  namespace: gpu-operator-resources
data:
  config.yaml: |
    version: v1
    sharing:
      timeSlicing:
        renameByDefault: false
        resources:
        - name: nvidia.com/gpu
          replicas: 4           # 每张GPU模拟4张
          
---
# MIG Configuration (A100/H100)
apiVersion: v1
kind: ConfigMap
metadata:
  name: mig-config
  namespace: gpu-operator-resources
data:
  config.yaml: |
    version: v1
    mig-configs:
      # A100 80GB: 7 instances of 10GB
      a100-80gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            "1g.10gb": 7
      
      # A100 80GB: 3 one20GB + 1 ones40GB
      a100-80gb-mixed:
        - devices: all
          mig-enabled: true
          mig-devices:
            "2g.20gb": 3
            "4g.40gb": 1
```

### 4.2 Optimization of Training Costs

| Optimization Techniques | Memory Savings | Speed Impact | Cost Savings | Complexity Level |
|---------|---------|---------|---------|----------|
| Mixed Precision Training(AMP) | 40-50% | +10-30% | 40-50% | Low |
| Gradient Accumulation | 60-80% | -10-20% | 30-40% | Low |
| Gradient Checkpointing | 50-70% | -20-30% | 25-35% | Medium |
| ZeRO-Offloading | 80%+ | -30-50% | 40-60% | Medium |
| Model Parallelism | N/A | -10-20% | Scalability | High |
| Early Stopping | N/A | +20-40% | 20-40% | Low |
| Learning Rate Scheduling | N/A | +10-20% | 10-20% | Low |

```python
# DeepSpeed ZeRO Configuration Example
deepspeed_config = {
    "zero_optimization": {
        "stage": 3,
        "offload_optimizer": {
            "device": "cpu",
            "pin_memory": True
        },
        "offload_param": {
            "device": "cpu",
            "pin_memory": True
        },
        "overlap_comm": True,
        "contiguous_gradients": True,
        "reduce_bucket_size": 5e7,
        "stage3_prefetch_bucket_size": 5e7,
        "stage3_param_persistence_threshold": 1e5
    },
    "fp16": {
        "enabled": True,
        "loss_scale": 0,
        "initial_scale_power": 16
    },
    "gradient_accumulation_steps": 8,
    "gradient_clipping": 1.0,
    "train_batch_size": "auto",
    "train_micro_batch_size_per_gpu": "auto"
}
```

### 4.3 Optimization of Inference Costs

| Optimization Techniques | Delay Impact | Throughput Improvement | Cost Savings | Accuracy Loss |
|---------|---------|---------|---------|---------|
| INT8 Quantization | -10% | +50-100% | 50-60% | <1% |
| INT4 Quantization | -20% | +100-200% | 70-80% | 1-3% |
| KV Cache Optimization | 0% | +30-50% | 20-30% | 0% |
| **Continuous Batching** | -5% | +200-400% | 60-75% | 0% |
| **Speculative Decoding** | +20% | +50-100% | 30-40% | 0% |
| **Flash Attention** | -10% | +100-200% | 40-50% | 0% |
| **PagedAttention** | 0% | +200-300% | 50-70% | 0% |

```yaml
# vLLM Efficient Inference Configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-inference
spec:
  template:
    spec:
      containers:
      - name: vllm
        image: vllm/vllm-openai:latest
        args:
        - "--model=/models/llama-2-70b"
        - "--tensor-parallel-size=4"
        - "--quantization=awq"            # AWQ量化
        - "--max-model-len=4096"
        - "--gpu-memory-utilization=0.9"  # 显存利用率90%
        - "--enable-prefix-caching"       # 前缀缓存
        - "--max-num-seqs=256"            # 最大并发
        resources:
          limits:
            nvidia.com/gpu: 4
          requests:
            memory: "64Gi"
            cpu: "16"
```

### 4.4 Optimization of Storage Costs

```yaml
# Storage Hierarchical Strategy
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: ai-data-tiered
provisioner: csi.juicefs.com
parameters:
  # Hot data: NVMe SSD
  juicefs-secret-name: "juicefs-secret"
  juicefs-secret-namespace: "default"
  
  # Store layered configuration
  storage-tiers: |
    tier-hot:
      backend: "nvme-ssd"
      capacity: "1Ti"
      ttl: "7d"
    tier-warm:
      backend: "ssd"
      capacity: "10Ti"
      ttl: "30d"
    tier-cold:
      backend: "s3"
      capacity: "unlimited"
      
---
# Data Lifecycle Management
apiVersion: batch/v1
kind: CronJob
metadata:
  name: data-lifecycle-manager
spec:
  schedule: "0 2 * * *"  # 每天凌晨2点
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: lifecycle
            image: data-lifecycle-manager:latest
            env:
            - name: HOT_TO_WARM_DAYS
              value: "7"
            - name: WARM_TO_COLD_DAYS
              value: "30"
            - name: DELETE_AFTER_DAYS
              value: "365"
```

---


## 5. Cost Monitoring and Alerts

### 5.1 Kubecost Deployment Configuration

```yaml
# Kubecost Helm Values
kubecostModel:
  # Cloud Billing Integration
  cloudIntegration:
    enabled: true
    aws:
      athenaProjectID: "aws-cost-project"
      athenaBucketName: "s3://cur-bucket"
      athenaRegion: "us-east-1"
      athenaDatabase: "cur_database"
      athenaTable: "cur_table"
  
  # GPU cost
  gpuCost:
    enabled: true
    # Custom GPU price ($/h)
    prices:
      nvidia.com/gpu:
        a100-80gb: 32.77
        a100-40gb: 19.50
        a10g: 1.006
        t4: 0.526
  
  # Budget Configuration
  budgets:
    enabled: true
    configs:
      - namespace: "ml-training"
        monthly: 50000
        alertThresholds: [50, 75, 90, 100]
      - namespace: "ml-inference"
        monthly: 30000
        alertThresholds: [50, 75, 90, 100]

prometheus:
  server:
    retention: "30d"
    
grafana:
  enabled: true
  dashboards:
    enabled: true
```

### 5.2 Cost Alert Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: ai-cost-alerts
  namespace: monitoring
spec:
  groups:
  - name: ai-cost-alerts
    rules:
    # Daily cost exceeds budget
    - alert: DailyCostOverBudget
      expr: |
        sum(increase(kubecost_cluster_costs_daily[24h])) > 5000
      for: 1h
      labels:
        severity: warning
      annotations:
        summary: "Daily cost exceeds $5000"
        description: "Current daily cost: ${{ $value | humanize }}"
    
    # GPU Idle Alarm
    - alert: GPUIdleHigh
      expr: |
        (1 - avg(DCGM_FI_DEV_GPU_UTIL) / 100) > 0.5
      for: 30m
      labels:
        severity: warning
      annotations:
        summary: "GPU idle rate exceeds 50%"
        description: "Average GPU utilization: {{ $value | humanizePercentage }}"
    
    # Risk of Spot Instance Interruption
    - alert: SpotInstanceInterruptionRisk
      expr: |
        sum(karpenter_interruption_actions_performed) > 5
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Spot instance frequently interrupted"
        description: "Number of interruptions within 5 minutes: {{ $value }}"
    
    # Storage cost growth exceeds expectation
    - alert: StorageCostSpike
      expr: |
        (sum(kubecost_pv_hourly_cost) - sum(kubecost_pv_hourly_cost offset 1d)) 
        / sum(kubecost_pv_hourly_cost offset 1d) > 0.2
      for: 1h
      labels:
        severity: warning
      annotations:
        summary: "Storage cost growth exceeds 20%"
    
    # Network cost anomaly
    - alert: NetworkCostAnomaly
      expr: |
        sum(rate(kubecost_network_zone_egress_cost[1h])) > 100
      for: 30m
      labels:
        severity: warning
      annotations:
        summary: "Cross-area network cost anomaly"
        description: "Hourly network cost: ${{ $value | humanize }}"
```

### 5.3 Cost Dashboard (Grafana)

```json
{
  "title": "AI Infrastructure Cost Overview",
  "panels": [
    {
      "title": "Total Cost Trend (Daily)"
      "type": "timeseries",
      "targets": [{
        "expr": "sum(increase(kubecost_cluster_costs_daily[24h]))",
        "legendFormat": "Daily Cost"
      }]
    },
    {
      "title": "Cost Distribution (By Namespace)"
      "type": "piechart",
      "targets": [{
        "expr": "sum by (namespace) (kubecost_namespace_hourly_cost * 24 * 30)",
        "legendFormat": "{{namespace}}"
      }]
    },
    {
      "title": "GPU cost efficiency"
      "type": "gauge",
      "targets": [{
        "expr": "avg(DCGM_FI_DEV_GPU_UTIL) / 100 * 100"
      }],
      "thresholds": {
        "steps": [
          {"color": "red", "value": 0},
          {"color": "yellow", "value": 50},
          {"color": "green", "value": 75}
        ]
      }
    },
    {
      "title": "Amount saved by Spot"
      "type": "stat",
      "targets": [{
        "expr": "sum(kubecost_savings_spot_monthly)"
      }]
    }
  ]
}
```

---


## 6. Optimization Case Studies

### 6.1 Training Task Optimization Case

| Optimization Items | Before Optimization | After Optimization | Savings | Annual Savings |
|-------|-------|-------|------|---------|
| Spot Instances | 100% On-Demand | 70% Spot | 49% | $180,000 |
| Mixed Precision Training | FP32 | AMP | 45% | $120,000 |
| GPU Utilization | 35% | 75% | 53% | $150,000 |
| Storage Tiering | All SSD | Hot/Cold/Temperature Tiering | 60% | $48,000 |
| Reserved Instances | On-Demand | 1 Year Reserved | 35% | $80,000 |
| Scheduling Optimization | Manual | Kueue Auto | 20% | $40,000 |
| **total** | - | - | **51%** | **$618,000** |

### 6.2 Inference Service Optimization Case

| Service | Original Config | Optimized | Delay Impact | Cost Savings |
|-----|-------|-------|---------|---------|
| **ChatBot** | 8x A100 FP16 | 4x A100 INT4 | +5ms | 65% |
| **Search Ranking** | 16x V100 | 8x A10G | -2ms | 70% |
| **Image Generation** | 4x A100 | 2x A100 MIG | +10ms | 50% |
| **Speech Recognition** | 8x T4 | 4x T4 Batch | +50ms | 50% |

---


## 7. FinOps Tool Ecosystem (FinOps Tools)

### 7.1 Cost Management Tool Comparison

| Tools | Type | Cloud Support | Kubernetes Native | GPU Cost | Open Source | Price |
|-----|------|-------|--------|--------|------|------|
| **Kubecost** | Cost Analysis | AWS/GCP/Azure | Yes | Yes | Yes | Free/Business Edition |
| **[[OpenCost|OpenCost]]** | Cost Analysis | Multi-cloud | Yes | Yes | Yes | Free |
| **Vantage** | FinOps platform | Multi-cloud | Yes | Yes | No | Paid |
| **CloudHealth** | FinOps Platform | Multi-cloud | Partial | No | No | Paid |
| **Spot.io** | Optimization | AWS/GCP/Azure | Yes | Yes | No | Paid |
| **CAST AI** | Optimization | Multi-cloud | Yes | Yes | No | Paid |

### 7.2 OpenCost Quick Deployment

> ⚠️ **🟡 Medium Risk Changes** — Change cluster resource status, recommend to first --dry-run or diff confirm
> - `helm upgrade/install`: Deploy/upgrade release
> - `kubectl apply/create/replace`: Create/modify cluster resources

``` bash
# 🔴 Medium Risk: Modifies cluster/resource state, confirm target, impact scope, and authorization before deployment
# Deploy OpenCost
helm install opencost opencost/opencost \
  --namespace opencost \
  --create-namespace \
  --set opencost.prometheus.internal.enabled=true \
  --set opencost.ui.enabled=true \
  --set opencost.exporter.defaultClusterId="production" \
  --set opencost.customPricing.enabled=true \
  --set opencost.customPricing.configmapName="opencost-custom-pricing"

# Custom GPU Price
kubectl create configmap opencost-custom-pricing -n opencost --from-file=pricing.json
```
---


## 8. Cost Governance Best Practices (Governance Best Practices)

### 8.1 Cost Governance Process

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        cost governance cycle                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐  │
│  │   Plan      │───→│   Execute      │───→│   Check      │───→│   Improve      │  │
│  │   Plan      │    │   Do        │    │   Check     │    │   Act       │  │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘  │
│        │                  │                  │                  │          │
│        ▼                  ▼                  ▼                  ▼          │
│  • set budget          • resource tags         • cost report         • optimization strategy      │
│  • Cost Forecasting          • Cost Allocation         • Anomaly Analysis         • Strategy Adjustments       │
│  • Goal Setting          • Automated Execution       • KPI Evaluation          • Process Improvements       │
│                                                                             │
│  ════════════════════════════════════════════════════════════════════════  │
│                              monthly cycle                                        │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 8.2 Cost Optimization Checklist

```markdown

## Monthly Cost Audit Checklist

### Compute Resources
- [ ] GPU利用率 > 70%
- [ ] CPU利用率 > 50%
- [ ] Spot实例占比 > 60% (可中断任务)
- [ ] 无长期空闲GPU实例
- [ ] 预留实例覆盖率达标

### Storage Resources
- [ ] 存储分层策略生效
- [ ] 无孤儿PV/PVC
- [ ] 快照保留策略合理
- [ ] 跨区域复制必要性验证

### Network Resources
- [ ] 跨区流量最小化
- [ ] CDN覆盖率优化
- [ ] 专线利用率合理

### Governance Compliance
- [ ] 所有资源100%标签覆盖
- [ ] 成本分配准确性验证
- [ ] 预算告警有效性测试
- [ ] 成本异常根因分析完成
```

---


## 9. Quick Reference (Quick Reference)

### 9.1 Cost Calculation Formula

```
# GPU Hour Cost
GPU hours cost = GPU unit price × usage duration × (1 - Spot discount)

# Total Training Cost
Training total cost = GPU hours cost × number of GPUs × training duration + storage cost + network cost

# Inference Service Monthly Cost
Monthly cost = (GPU unit price × 24 × 30) × number of instances × (1 + redundancy factor)

# Cost Efficiency
Cost efficiency = model performance improvement / cost increase
ROI = (business value - total cost) / total cost × 100%
```

### 9.2 Common Commands

> ⚠️ **🟡 Medium Risk Changes** — Change cluster resource status, recommend to first --dry-run or diff confirm
> - `kubectl exec`: Enter container to execute commands, may change container state

``` bash
# 🟡 Medium Risk: Will modify cluster/resource status, please confirm target, impact scope, and authorization before execution
# Kubecost Cost Query
kubectl cost namespace --window 7d --show-all-resources

# OpenCost API Query
curl http://opencost.opencost:9003/allocation/compute?window=7d

# GPU Utilization Query
kubectl exec -it dcgm-exporter-xxx -- dcgmi dmon -e 203,204

# Spot Instance Status
kubectl get nodes -l karpenter.sh/capacity-type=spot

# Cost Label Coverage Check
kubectl get pods -A -o json | jq '[.items[] | select(.metadata.labels["cost-center"] == null)] | length'
```
---

**cost optimization principles**: Spot priority → Improve utilization → Storage tiering → Continuous monitoring

---

**table bottom mark**: Kusheet Project, author Allen Galler (allengaller@gmail.com)

---


## Obsidian Related Documentation

- domain-11-ai-infra MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Open Source Project Index
- AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations (AI/ML Workloads Operations)
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management

## See Also

- 10-model-deployment-management
- 11-ai-security-model-protection
- 13-ai-platform-observability
- 14-troubleshooting-performance

## Related

- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Knowledge Graph Index]]


<!-- risk-assessed -->
