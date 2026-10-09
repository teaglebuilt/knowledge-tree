---
title: GPU Monitoring and Observability
description: '# GPU Monitoring and Observability'
summary: 'DCGM_FI_DEV_GPU_UTIL{gpu="0", kubernetes_node="node-1"}'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- kubelet
- prometheus
- grafana
- helm
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
- What is GPU Monitoring and Observability
- How to do GPU Monitoring and Observability
- Kubernetes 11 ai infra Best Practices
trigger_keywords:
- GPU Monitoring and Observability
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
- type: fta
  path: ../domain-10-troubleshooting-diagnostics/topic-fta/list/monitoring-fta.md
  label: 'Fault Tree: monitoring'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/04-gpu-monitoring-dcgm.md
---

> **Production Environment Security Tips**
>
> This document contains executable operational commands. Execute them only after confirming: the correct target cluster and namespace; sufficient RBAC permissions; and successful validation in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (modifies cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# GPU Monitoring and Observability

> **Applicable Version**: v1.25 - v1.32 | **Last Updated**: 2026-01 | **Reference**: [DCGM Exporter](https://github.com/NVIDIA/dcgm-exporter) | [GPU Operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/)


## GPU Monitoring Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     GPU metrics collection layer                                │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │  NVIDIA DCGM (Data Center GPU Manager)                  │  │
│  │  - GPU utilization, temperature, power                                 │  │
│  │  │  - Memory usage, ECC errors                                  │  │
│  │  │  - NVLink topology, PCIe traffic                              │  │
│  └──────────────┬───────────────────────────────────────────┘  │
└─────────────────┼──────────────────────────────────────────────┘
                  │ DCGM Exporter (Prometheus format)
                  v
┌─────────────────────────────────────────────────────────────────┐
│                     Prometheus (time series database)                       │
│  - 15s granularity collection                                                   │
│  - 30-day local retention                                                  │
│  - Thanos long-term storage                                                │
└─────────────────┬───────────────────────────────────────────────┘
                  │
                  v
┌─────────────────────────────────────────────────────────────────┐
│                     Visualization and alerting layer                                │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │  Grafana    │  │ AlertManager│  │  Slack/     │            │
│  │  Dashboard  │  │  (alerting)     │  │  PagerDuty  │            │
│  └─────────────┘  └─────────────┘  └─────────────┘            │
└─────────────────────────────────────────────────────────────────┘
```

---


## 1. Deploying DCGM Exporter

### 1. Installing GPU Operator (Recommended)

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource status, recommend using --dry-run or diff to confirm first
> - `helm upgrade/install` : Deploy/upgrade release

``` bash
# 🟡 Medium Risk: modifies cluster/resource status; confirm target, impact scope, and authorization before proceeding
# Add NVIDIA Helm repository
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia
helm repo update

# Install GPU Operator (including DCGM Exporter)
helm install --wait --generate-name \
  -n gpu-operator --create-namespace \
  nvidia/gpu-operator \
  --set dcgmExporter.enabled=true \
  --set dcgmExporter.serviceMonitor.enabled=true \
  --set toolkit.enabled=true
```
### 2. Independent Deployment of DCGM Exporter

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: dcgm-exporter
  namespace: gpu-monitoring
spec:
  selector:
    matchLabels:
      app: dcgm-exporter
  template:
    metadata:
      labels:
        app: dcgm-exporter
    spec:
      hostNetwork: true
      hostPID: true
      tolerations:
        - key: nvidia.com/gpu
          operator: Exists
          effect: NoSchedule
      
      containers:
        - name: dcgm-exporter
          image: nvcr.io/nvidia/k8s/dcgm-exporter:3.3.0-3.2.0-ubuntu22.04
          
          env:
            # Metrics collection configuration
            - name: DCGM_EXPORTER_LISTEN
              value: ":9400"
            - name: DCGM_EXPORTER_KUBERNETES
              value: "true"
            - name: DCGM_EXPORTER_COLLECTORS
              value: "/etc/dcgm-exporter/dcp-metrics-included.csv"
          
          ports:
            - name: metrics
              containerPort: 9400
          
          securityContext:
            privileged: true
            capabilities:
              add: ["SYS_ADMIN"]
          
          volumeMounts:
            - name: pod-gpu-resources
              mountPath: /var/lib/kubelet/pod-resources
              readOnly: true
            - name: device-metrics
              mountPath: /run/prometheus
          
          livenessProbe:
            httpGet:
              path: /health
              port: 9400
            initialDelaySeconds: 45
            periodSeconds: 5
          
          readinessProbe:
            httpGet:
              path: /health
              port: 9400
            initialDelaySeconds: 45
      
      volumes:
        - name: pod-gpu-resources
          hostPath:
            path: /var/lib/kubelet/pod-resources
        - name: device-metrics
          emptyDir: {}
---
apiVersion: v1
kind: Service
metadata:
  name: dcgm-exporter
  namespace: gpu-monitoring
  labels:
    app: dcgm-exporter
spec:
  selector:
    app: dcgm-exporter
  ports:
    - name: metrics
      port: 9400
      targetPort: 9400
  type: ClusterIP
```

### 3. Configuring ServiceMonitor

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: dcgm-exporter
  namespace: gpu-monitoring
  labels:
    app: dcgm-exporter
spec:
  selector:
    matchLabels:
      app: dcgm-exporter
  endpoints:
    - port: metrics
      interval: 15s
      path: /metrics
      relabelings:
        # Add node labels
        - sourceLabels: [__meta_kubernetes_pod_node_name]
          targetLabel: node
        # Add namespace labels
        - sourceLabels: [__meta_kubernetes_namespace]
          targetLabel: namespace
        # Add Pod labels
        - sourceLabels: [__meta_kubernetes_pod_name]
          targetLabel: pod
```

---


## 2. Core GPU Metrics

### 1. List of Key Indicators

| Metric | Prometheus Metric | Description | Alert Thresholds |
|------|------------------|------|---------|
| **GPU Utilization** | `DCGM_FI_DEV_GPU_UTIL` | GPU computational unit usage | <30%(waste) >95%(saturation) |
| **Memory Usage** | `DCGM_FI_DEV_FB_USED` | Used memory (MB) | >90% |
| **Total Memory** | `DCGM_FI_DEV_FB_TOTAL` | Total memory (MB) | - |
| **GPU Temperature** | `DCGM_FI_DEV_GPU_TEMP` | GPU temperature (°C) | >85°C |
| **Power Consumption** | `DCGM_FI_DEV_POWER_USAGE` | Current power (W) | >350W(A100) |
| **Memory Temperature** | `DCGM_FI_DEV_MEMORY_TEMP` | Memory temperature (°C) | >95°C |
| **SM Activity** | `DCGM_FI_PROF_SM_ACTIVE` | Stream Processor activity | <50% |
| **SM Occupancy** | `DCGM_FI_PROF_SM_OCCUPANCY` | SM occupancy | <60% |
| **Tensor Core Utilization** | `DCGM_FI_PROF_PIPE_TENSOR_ACTIVE` | Tensor Core activity | <30%(AI training) |
| **FP16 Activity** | `DCGM_FI_PROF_PIPE_FP16_ACTIVE` | FP16 computation activity | - |
| **DRAM Utilization** | `DCGM_FI_PROF_DRAM_ACTIVE` | DRAM utilization | <70% |
| **PCIe Transmitted** | `DCGM_FI_PROF_PCIE_TX_BYTES` | PCIe transmitted bytes | >10GB/s |
| **PCIe Received** | `DCGM_FI_PROF_PCIE_RX_BYTES` | PCIe received bytes | >10GB/s |
| **NVLink Traffic** | `DCGM_FI_PROF_NVLINK_TX_BYTES` | NVLink transmitted traffic | >50GB/s |
| **XID Error** | `DCGM_FI_DEV_XID_ERRORS` | hardware error code | >0 |
| **Single-bit ECC Error** | `DCGM_FI_DEV_ECC_SBE_VOL_TOTAL` | correctable memory errors | >100/day |
| **Double-bit ECC Error** | `DCGM_FI_DEV_ECC_DBE_VOL_TOTAL` | uncorrectable errors | >0 |

---

### 2. Example PromQL Queries

#### GPU Utilization

```promql
# Single GPU utilization
DCGM_FI_DEV_GPU_UTIL{gpu="0", kubernetes_node="node-1"}

# Average GPU utilization for the cluster
avg(DCGM_FI_DEV_GPU_UTIL)

# Average GPU utilization per node
avg(DCGM_FI_DEV_GPU_UTIL) by (kubernetes_node)

# GPU utilization per Pod
avg(DCGM_FI_DEV_GPU_UTIL{pod=~"training-.*"}) by (pod)

# GPU utilization below 30% (waste of resources)
DCGM_FI_DEV_GPU_UTIL < 30
```

#### Memory Usage Rate

```promql
# Memory usage (%)
(DCGM_FI_DEV_FB_USED / DCGM_FI_DEV_FB_TOTAL) * 100

# Memory usage > 90%
(DCGM_FI_DEV_FB_USED / DCGM_FI_DEV_FB_TOTAL) * 100 > 90

# Memory usage per namespace
sum(DCGM_FI_DEV_FB_USED) by (namespace)

# Available memory
DCGM_FI_DEV_FB_FREE
```

#### Tensor Core Utilization

```promql
# Tensor Core activity (key AI training metric)
DCGM_FI_PROF_PIPE_TENSOR_ACTIVE

# Average Tensor Core utilization
avg(DCGM_FI_PROF_PIPE_TENSOR_ACTIVE)

# Tensor Core utilization below 30% (low training efficiency)
DCGM_FI_PROF_PIPE_TENSOR_ACTIVE < 30
```

#### GPU Temperature and Power

```promql
# GPU temperature exceeds 85℃
DCGM_FI_DEV_GPU_TEMP > 85

# Power Consumption Trend (5-minute Average)
avg_over_time(DCGM_FI_DEV_POWER_USAGE[5m])

# Power Exceeds Rated Value (A100=400W)
DCGM_FI_DEV_POWER_USAGE > 400
```

#### NVLink Traffic

```promql
# NVLink Transmission Rate (GB/s)
rate(DCGM_FI_PROF_NVLINK_TX_BYTES[1m]) / 1024 / 1024 / 1024

# NVLink Reception Rate
rate(DCGM_FI_PROF_NVLINK_RX_BYTES[1m]) / 1024 / 1024 / 1024

# Total NVLink Bandwidth
(rate(DCGM_FI_PROF_NVLINK_TX_BYTES[1m]) + 
 rate(DCGM_FI_PROF_NVLINK_RX_BYTES[1m])) / 1024 / 1024 / 1024
```

#### Error Detection

```promql
# XID Errors (Hardware Issues)
increase(DCGM_FI_DEV_XID_ERRORS[1h]) > 0

# ECC Single-bit Error Trend
rate(DCGM_FI_DEV_ECC_SBE_VOL_TOTAL[1h])

# ECC Double-bit Errors (Severe)
increase(DCGM_FI_DEV_ECC_DBE_VOL_TOTAL[1h]) > 0
```

---


## 3. Prometheus Alert Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: gpu-alerts
  namespace: gpu-monitoring
spec:
  groups:
    - name: gpu-health
      interval: 30s
      rules:
        # ========== Resource Utilization Alerts ==========
        
        - alert: GPULowUtilization
          expr: |
            avg_over_time(DCGM_FI_DEV_GPU_UTIL[10m]) < 30
          for: 30m
          labels:
            severity: warning
            team: ml-platform
          annotations:
            summary: "GPU utilization is too low"
            description: |
              节点 {{ $labels.kubernetes_node }} 的 GPU {{ $labels.gpu }}
              利用率过低: {{ $value | humanizePercentage }}
              
              可能原因:
              - 训练任务配置不当
              - 数据加载瓶颈
              - 模型计算强度低
              
              排查命令:
              kubectl exec -it {{ $labels.pod }} -n {{ $labels.namespace }} -- nvidia-smi
        
        - alert: GPUHighMemoryUsage
          expr: |
            (DCGM_FI_DEV_FB_USED / DCGM_FI_DEV_FB_TOTAL) * 100 > 95
          for: 5m
          labels:
            severity: critical
            team: ml-platform
          annotations:
            summary: "GPU memory is about to be exhausted"
            description: |
              节点 {{ $labels.kubernetes_node }} 的 GPU {{ $labels.gpu }}
              显存使用率: {{ $value | humanizePercentage }}
              
              已用: {{ query "DCGM_FI_DEV_FB_USED" | first | value }}MB
              总量: {{ query "DCGM_FI_DEV_FB_TOTAL" | first | value }}MB
              
              可能导致OOM崩溃！
        
        - alert: LowTensorCoreUtilization
          expr: |
            avg_over_time(DCGM_FI_PROF_PIPE_TENSOR_ACTIVE[10m]) < 30
          for: 30m
          labels:
            severity: warning
            team: ml-platform
          annotations:
            summary: "Tensor Core utilization is low"
            description: |
              Pod {{ $labels.pod }} 的 Tensor Core 利用率仅 {{ $value | humanizePercentage }}
              
              优化建议:
              - 启用混合精度训练(FP16/BF16)
              - 检查是否使用Tensor Core优化算子
              - 增大batch size
        
        # ========== Hardware Health Alerts ==========
        
        - alert: GPUHighTemperature
          expr: |
            DCGM_FI_DEV_GPU_TEMP > 85
          for: 10m
          labels:
            severity: critical
            team: infra
          annotations:
            summary: "GPU temperature is high"
            description: |
              节点 {{ $labels.kubernetes_node }} 的 GPU {{ $labels.gpu }}
              温度达到 {{ $value }}℃ (阈值: 85℃)
              
              可能原因:
              - 散热问题
              - 环境温度过高
              - 负载过大
              
              立即检查节点物理状态！
        
        - alert: GPUMemoryTemperatureHigh
          expr: |
            DCGM_FI_DEV_MEMORY_TEMP > 95
          for: 5m
          labels:
            severity: critical
            team: infra
          annotations:
            summary: "VRAM temperature is abnormal"
            description: |
              节点 {{ $labels.kubernetes_node }} 的 GPU {{ $labels.gpu }}
              显存温度: {{ $value }}℃ (阈值: 95℃)
              
              可能导致硬件损坏！
        
        - alert: GPUXIDError
          expr: |
            increase(DCGM_FI_DEV_XID_ERRORS[5m]) > 0
          labels:
            severity: critical
            team: infra
          annotations:
            summary: "GPU hardware error detected"
            description: |
              节点 {{ $labels.kubernetes_node }} 的 GPU {{ $labels.gpu }}
              发生 XID 错误 (错误码: {{ $value }})
              
              常见XID错误:
              - 13: 图形引擎异常
              - 31/32: GPU内存页错误
              - 43: GPU驱动错误
              - 48: 双比特ECC错误
              - 79: GPU陷入死循环
              
              建议立即隔离该GPU！
        
        - alert: ECCDoubleBitError
          expr: |
            increase(DCGM_FI_DEV_ECC_DBE_VOL_TOTAL[1h]) > 0
          labels:
            severity: critical
            team: infra
          annotations:
            summary: "ECC double-bit error detected"
            description: |
              节点 {{ $labels.kubernetes_node }} 的 GPU {{ $labels.gpu }}
              发生不可纠正的显存错误
              
              该GPU需要更换！
        
        - alert: ECCSingleBitErrorHigh
          expr: |
            rate(DCGM_FI_DEV_ECC_SBE_VOL_TOTAL[1h]) > 100
          for: 1h
          labels:
            severity: warning
            team: infra
          annotations:
            summary: "ECC single-bit error rate is high"
            description: |
              节点 {{ $labels.kubernetes_node }} 的 GPU {{ $labels.gpu }}
              单比特ECC错误率: {{ $value }}/小时
              
              虽可自动纠正，但错误率过高可能预示硬件老化
        
        # ========== Communication Performance Alerts ==========
        
        - alert: LowNVLinkBandwidth
          expr: |
            (rate(DCGM_FI_PROF_NVLINK_TX_BYTES[5m]) + 
             rate(DCGM_FI_PROF_NVLINK_RX_BYTES[5m])) 
            / 1024 / 1024 / 1024 < 10
          for: 15m
          labels:
            severity: warning
            team: ml-platform
          annotations:
            summary: "NVLink bandwidth is abnormally low"
            description: |
              节点 {{ $labels.kubernetes_node }} 的 NVLink 总带宽: {{ $value }}GB/s
              
              可能原因:
              - 分布式训练通信不频繁
              - NVLink硬件问题
              - 训练框架配置问题
        
        - alert: GPUThrottling
          expr: |
            DCGM_FI_DEV_CLOCK_THROTTLE_REASONS > 0
          for: 10m
          labels:
            severity: warning
            team: infra
          annotations:
            summary: "GPU is underclocked"
            description: |
              节点 {{ $labels.kubernetes_node }} 的 GPU {{ $labels.gpu }}
              被降频 (原因码: {{ $value }})
              
              降频原因:
              - 1: GPU空闲
              - 2: 应用时钟设置
              - 4: 软件功率限制
              - 8: 硬件慢速阈值
              - 16: 硬件热慢速
              - 32: 软件热慢速
              - 64: 同步Boost
              
              影响训练性能！
        
        # ========== Cluster-Level Alerts ==========
        
        - alert: GPUClusterLowUtilization
          expr: |
            avg(DCGM_FI_DEV_GPU_UTIL) < 40
          for: 1h
          labels:
            severity: info
            team: ml-platform
          annotations:
            summary: "Cluster GPU utilization is low"
            description: |
              集群整体GPU利用率: {{ $value | humanizePercentage }}
              
              成本优化建议:
              - 缩减GPU节点数量
              - 启用GPU共享(MIG/cGPU)
              - 调整任务调度策略
        
        - alert: GPUNodeDown
          expr: |
            up{job="dcgm-exporter"} == 0
          for: 5m
          labels:
            severity: critical
            team: infra
          annotations:
            summary: "GPU node is offline"
            description: |
              节点 {{ $labels.kubernetes_node }} 的 DCGM Exporter 无法访问
              
              排查步骤:
              1. kubectl get nodes {{ $labels.kubernetes_node }}
              2. kubectl describe node {{ $labels.kubernetes_node }}
              3. kubectl logs -n gpu-monitoring -l app=dcgm-exporter --tail=100
```

---


## 4. Grafana Dashboards

### 1. GPU Cluster Overview Dashboard

```json
{
  "dashboard": {
    "title": "GPU Cluster Overview",
    "panels": [
      {
        "title": "Total number of GPUs and online rate",
        "type": "stat",
        "targets": [
          {
            "expr": "count(DCGM_FI_DEV_GPU_UTIL)",
            "legendFormat": "Total GPUs"
          },
          {
            "expr": "count(DCGM_FI_DEV_GPU_UTIL > 0)",
            "legendFormat": "Active GPUs"
          }
        ]
      },
      {
        "title": "Cluster GPU utilization",
        "type": "graph",
        "targets": [
          {
            "expr": "avg(DCGM_FI_DEV_GPU_UTIL)",
            "legendFormat": "Average Utilization"
          }
        ]
      },
      {
        "title": "GPU utilization distribution (heatmap)",
        "type": "heatmap",
        "targets": [
          {
            "expr": "DCGM_FI_DEV_GPU_UTIL",
            "format": "time_series"
          }
        ]
      },
      {
        "title": "VRAM usage situation",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(DCGM_FI_DEV_FB_USED) / 1024",
            "legendFormat": "Used (GB)"
          },
          {
            "expr": "sum(DCGM_FI_DEV_FB_TOTAL) / 1024",
            "legendFormat": "Total (GB)"
          }
        ]
      },
      {
        "title": "GPU temperature distribution",
        "type": "graph",
        "targets": [
          {
            "expr": "DCGM_FI_DEV_GPU_TEMP",
            "legendFormat": "{{kubernetes_node}}-gpu{{gpu}}"
          }
        ],
        "alert": {
          "conditions": [
            {
              "evaluator": {
                "params": [85],
                "type": "gt"
              },
              "operator": {
                "type": "and"
              },
              "query": {
                "params": ["A", "5m", "now"]
              },
              "reducer": {
                "type": "avg"
              },
              "type": "query"
            }
          ]
        }
      },
      {
        "title": "Tensor Core utilization (training tasks)",
        "type": "graph",
        "targets": [
          {
            "expr": "avg(DCGM_FI_PROF_PIPE_TENSOR_ACTIVE{namespace=\"ai-training\"})",
            "legendFormat": "Tensor Core Active"
          }
        ]
      },
      {
        "title": "Total NVLink bandwidth",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(DCGM_FI_PROF_NVLINK_TX_BYTES[1m]) + rate(DCGM_FI_PROF_NVLINK_RX_BYTES[1m])) / 1024 / 1024 / 1024",
            "legendFormat": "Total Bandwidth (GB/s)"
          }
        ]
      },
      {
        "title": "GPU error statistics"
        "type": "table",
        "targets": [
          {
            "expr": "DCGM_FI_DEV_XID_ERRORS > 0",
            "format": "table"
          }
        ]
      }
    ]
  }
}
```

---


## 5. Dedicated Monitoring for Training Tasks

### 1. PyTorchJob Monitoring

```yaml
apiVersion: kubeflow.org/v1
kind: PyTorchJob
metadata:
  name: monitored-training
  namespace: ai-training
spec:
  pytorchReplicaSpecs:
    Master:
      replicas: 1
      template:
        metadata:
          annotations:
            # Prometheus Scrape Configuration
            prometheus.io/scrape: "true"
            prometheus.io/port: "8000"
            prometheus.io/path: "/metrics"
        spec:
          containers:
            - name: pytorch
              image: pytorch/pytorch:2.1.0
              command:
                - python
                - train.py
              ports:
                - containerPort: 8000  # Prometheus metrics端口
              env:
                - name: RANK
                  value: "0"
                - name: WORLD_SIZE
                  value: "8"
              resources:
                limits:
                  nvidia.com/gpu: 8
```

### 2. Training Metrics Export

```python
from prometheus_client import start_http_server, Gauge, Counter

# Define Metrics
training_loss = Gauge('training_loss', 'Current training loss')
training_accuracy = Gauge('training_accuracy', 'Current training accuracy')
training_throughput = Gauge('training_throughput_samples_per_sec', 
                            'Training throughput')
gpu_memory_allocated = Gauge('gpu_memory_allocated_bytes', 
                             'GPU memory allocated', ['gpu_id'])
gpu_memory_reserved = Gauge('gpu_memory_reserved_bytes', 
                            'GPU memory reserved', ['gpu_id'])
training_step = Counter('training_steps_total', 'Total training steps')

# Start metrics server
start_http_server(8000)

# Update metrics during training loop
for epoch in range(num_epochs):
    for batch in dataloader:
        loss = train_step(batch)
        
        # Update metrics
        training_loss.set(loss.item())
        training_step.inc()
        
        # GPU Memory Monitoring
        for i in range(torch.cuda.device_count()):
            allocated = torch.cuda.memory_allocated(i)
            reserved = torch.cuda.memory_reserved(i)
            gpu_memory_allocated.labels(gpu_id=str(i)).set(allocated)
            gpu_memory_reserved.labels(gpu_id=str(i)).set(reserved)
```

---


## 6. Cost Monitoring

### 1. GPU Cost Calculation

```promql
# Hourly GPU Cost per GPU ($3/hour assuming A100)
sum(DCGM_FI_DEV_GPU_UTIL > 0) * 3

# Statistic GPU Usage Cost by Namespace
sum(DCGM_FI_DEV_GPU_UTIL > 0) by (namespace) * 3

# Inefficient GPU costs (utilization < 30%)
sum(DCGM_FI_DEV_GPU_UTIL < 30 and DCGM_FI_DEV_GPU_UTIL > 0) * 3

# Daily cost estimation
sum(DCGM_FI_DEV_GPU_UTIL > 0) * 3 * 24
```

---


## 7. Production Best Practices

### GPU Monitoring Checklist

- ✅ Deploy DCGM Exporter to all GPU nodes
- ✅ Configure Prometheus for 15s sampling
- ✅ Enable ServiceMonitor auto-discovery
- ✅ Configure 30-day local data retention
- ✅ Integrate Thanos for long-term storage
- ✅ Create Grafana GPU Overview Dashboard
- ✅ Configure GPU temperature/speed warning
- ✅ Monitor ECC errors and XID errors
- ✅ Track Tensor Core utilization
- ✅ Monitor NVLink bandwidth
- ✅ Integrate custom metrics for training tasks
- ✅ Configure Slack/PagerDuty alert notifications
- ✅ Establish GPU cost analysis Dashboard

---

**Table Maintenance**: Kusheet Project | **Author**: Allen Galler (allengaller@gmail.com)

---


## Obsidian Related Documentation

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- index.md|Domain-11 AI Infrastructure — Open Source Project Index]]
- AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations
- GPU Scheduling and Management
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry Center and Version Management
- AI Model Deployment and Lifecycle Management

## See Also

- 02-ai-ml-workloads
- 03-gpu-scheduling-management
- 05-distributed-training-frameworks
- 06-ai-data-pipeline

## Related

- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Knowledge Graph Index]]

```

<!-- risk-assessed -->
