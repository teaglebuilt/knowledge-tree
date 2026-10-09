---
title: AI Platform Observability System
description: '## One,AI Platform Observability Panoramic Architecture'
summary: 'pos_file /var/log/fluentd-containers.log.pos'
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
- istio
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
- What is AI Platform Observability System
- How is AI Platform Observability System
- Kubernetes 11 ai infra best practices
trigger_keywords:
- AI Platform Observability System
- ai
- infra
prerequisites:
- kubectl-basics
- helm-basics
- service-mesh-basics
- prometheus-basics
- monitoring-basics
- gpu-scheduling-basics
- logging-basics
- observability-basics
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
source_path: tree/infrastructure/kubernetes/ai/infrastructure/13-ai-platform-observability.md
---

> **Production Environment Security Reminders**
>
> This document contains executable operational commands. Execute them only after confirming: the correct target cluster and namespace; sufficient RBAC permissions; and successful validation in a non-production environment. Risk levels for commands: 🔴 High Risk (can lead to data loss or service disruption), 🟡 Medium Risk (modifies cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# AI Platform Observability System

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **Last Updated**: 2026-02 | **References**: [[entities/prometheus.md|Prometheus]](https://prometheus.io/) | [[entities/opentelemetry.md|OpenTelemetry]](https://opentelemetry.io/) | [Grafana](https://grafana.com/)


## 1. Overall Architecture of AI Platform Observability

### 1.1 Unified Monitoring Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                          AI Platform Observability Architecture                     │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                              Data Collection Layer (Collection)                           │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │  Prometheus │  │   DCGM      │  │ OpenTelemetry│  │   Fluentd   │          │  │
│  │  │   Server    │  │  Exporter   │  │   Collector  │  │   Agent     │          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  │ • Kubernetes metrics   │  │ • GPU utilization │  │ • Inference latency  │  │ • Application logs  │          │  │
│  │  │ • Pod status   │  │ • Memory usage  │  │ • Token count   │  │ • Training logs  │          │  │
│  │  │ • Node resources  │  │ • Temperature power consumption  │  │ • Error rate    │  │ • System logs  │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └─────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                              Storage Layer (Storage)                                 │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │  Prometheus │  │    Loki     │  │   Tempo     │  │   Mimir     │          │  │
│  │  │   TSDB      │  │   Log Store │  │ Trace Store │  │   Backend   │          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  │ • Retain for 15 days  │  │ • Retain for 30 days  │  │ • Retain for 3 days   │  │ • Long-term storage  │          │  │
│  │  │ • 100GB     │  │ • 500GB     │  │ • 50GB      │  │ • S3/GCS    │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └─────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                             Processing Layer (Processing)                           │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │ Alertmanager│  │   Grafana   │  │  Pyroscope  │  │  Custom     │          │  │
│  │  │             │  │             │  │             │  │  Analytics  │          │  │
│  │  │ • Alert routing  │  │ • Visualization    │  │ • Performance analysis  │  │ • Cost analysis  │          │  │
│  │  │ • Suppression silence  │  │ • Dashboard    │  │ • Flame graph    │  │ • Trend forecasting  │          │  │
│  │  │ • Notification grouping  │  │ • Exploration query  │  │ • Continuous analysis  │  │ • Anomaly detection  │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └─────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                             Presentation Layer (Presentation)                         │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │   Grafana   │  │   Slack     │  │    Email    │  │  Webhook    │          │  │
│  │  │  Dashboards │  │  Channels   │  │  Templates  │  │ Integrations│          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  │ • GPU monitoring   │  │ • Real-time alert  │  │ • Detailed report  │  │ • Automatic repair  │          │  │
│  │  │ • Cost analysis  │  │ • Upgrade notification  │  │ • Weekly/monthly reports  │  │ • Service tickets  │          │  │
│  │  │ • Model performance  │  │ • Team channel  │  │ • Management report  │  │ • CMDB synchronization  │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Configuration of Monitoring Indicators for GPUs

#### Core Monitoring Dimensions

| Dimension | Metric Category | Key Metrics | Alert Thresholds | Collection Frequency |
|------|----------|----------|----------|----------|
| **Infrastructure** | Nodes/GPUs/Network | CPU/Memory/GPU Utilization | 80%/85%/90% | 15s |
| **Training Jobs** | Training Progress/Resources | Loss/Accuracy/GPU Mem | Loss increases/Accuracy drops | 30s |
| **Inference Services** | Performance/Quality | Latency/Throughput/Error Rate | P99>500ms/Error rate>1% | 10s |
| **Storage Systems** | Capacity/Performance | Disk IO/Latency/Usage | Usage>85%/Latency>100ms | 30s |
| **Cost Management** | Resource Consumption | GPU Hours/Cost/Utilization | Exceeding budget/Utilization<30% | 5min |

---


## 2. AI Platform Observability System Deployment

### 2.1 Complete Monitoring Stack Deployment

```yaml
# ai-monitoring-stack.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: ai-monitoring
  labels:
    istio-injection: enabled
---
# Prometheus Server Configuration
apiVersion: monitoring.coreos.com/v1
kind: Prometheus
metadata:
  name: ai-prometheus
  namespace: ai-monitoring
spec:
  serviceAccountName: prometheus
  serviceMonitorSelector:
    matchLabels:
      team: ai-platform
  ruleSelector:
    matchLabels:
      team: ai-platform
  resources:
    requests:
      memory: 4Gi
      cpu: 2
    limits:
      memory: 8Gi
      cpu: 4
  storage:
    volumeClaimTemplate:
      spec:
        storageClassName: fast-ssd
        resources:
          requests:
            storage: 200Gi
  # Remote write configuration - Long-term storage
  remoteWrite:
  - url: http://mimir-remote-write:9009/api/v1/push
    writeRelabelConfigs:
    - sourceLabels: [__name__]
      regex: '(kubecost|dcgm|llm)_.*'
      action: keep
---
# GPU Monitoring ServiceMonitor
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: dcgm-exporter
  namespace: ai-monitoring
  labels:
    team: ai-platform
spec:
  selector:
    matchLabels:
      app: dcgm-exporter
  endpoints:
  - port: metrics
    interval: 15s
    path: /metrics
    relabelings:
    - sourceLabels: [__meta_kubernetes_pod_node_name]
      targetLabel: node
    - sourceLabels: [__meta_kubernetes_pod_label_nvidia_com_gpu_product]
      targetLabel: gpu_type
---
# Inference Service Monitoring
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: llm-inference
  namespace: ai-monitoring
  labels:
    team: ai-platform
spec:
  selector:
    matchLabels:
      app: vllm
  endpoints:
  - port: http
    interval: 10s
    path: /metrics
    metricRelabelings:
    - sourceLabels: [__name__]
      regex: 'vllm:(.*)'
      targetLabel: __name__
      replacement: 'llm_$1'
```

### 2.2 Configuration of Monitoring Indicators for GPUs

```yaml
# dcgm-exporter-values.yaml
# DCGM Exporter Helm values
dcgmExporter:
  # Enabled metrics
  metrics:
    - DCGM_FI_DEV_GPU_TEMP
    - DCGM_FI_DEV_POWER_USAGE
    - DCGM_FI_DEV_GPU_UTIL
    - DCGM_FI_DEV_MEM_COPY_UTIL
    - DCGM_FI_DEV_FB_USED
    - DCGM_FI_DEV_FB_FREE
    - DCGM_FI_DEV_SM_CLOCK
    - DCGM_FI_DEV_MEM_CLOCK
    - DCGM_FI_DEV_PCIE_TX_THROUGHPUT
    - DCGM_FI_DEV_PCIE_RX_THROUGHPUT
  
  # Custom metric tags
  serviceMonitor:
    enabled: true
    additionalLabels:
      team: ai-platform
    
  # Resource limits
  resources:
    limits:
      cpu: 100m
      memory: 128Mi
    requests:
      cpu: 50m
      memory: 64Mi
```

---


## 3. Grafana Dashboard Configuration

### 3.1 GPU Resource Monitoring Panel

```json
{
  "dashboard": {
    "title": "AI Platform - GPU Monitoring",
    "tags": ["ai", "gpu", "infrastructure"],
    "timezone": "browser",
    "panels": [
      {
        "type": "timeseries",
        "title": "GPU Utilization by Node",
        "datasource": "Prometheus",
        "targets": [
          {
            "expr": "avg by(node, gpu_type)(DCGM_FI_DEV_GPU_UTIL)",
            "legendFormat": "{{node}} - {{gpu_type}}"
          }
        ],
        "thresholds": [
          { "value": 80, "color": "orange" },
          { "value": 90, "color": "red" }
        ]
      },
      {
        "type": "stat",
        "title": "Total GPU Hours Today",
        "datasource": "Prometheus",
        "targets": [
          {
            "expr": "sum(increase(DCGM_FI_DEV_GPU_UTIL[24h])) / 100",
            "instant": true
          }
        ]
      }
    ]
  }
}
```

### 3.2 Performance Panel of Inference Services

```json
{
  "dashboard": {
    "title": "LLM Inference Performance",
    "panels": [
      {
        "type": "timeseries",
        "title": "Request Latency (P50/P95/P99)",
        "targets": [
          {
            "expr": "histogram_quantile(0.50, sum(rate(llm_request_duration_seconds_bucket[5m])) by (le))",
            "legendFormat": "P50"
          },
          {
            "expr": "histogram_quantile(0.95, sum(rate(llm_request_duration_seconds_bucket[5m])) by (le))",
            "legendFormat": "P95"
          },
          {
            "expr": "histogram_quantile(0.99, sum(rate(llm_request_duration_seconds_bucket[5m])) by (le))",
            "legendFormat": "P99"
          }
        ]
      },
      {
        "type": "gauge",
        "title": "Current Throughput (req/sec)",
        "targets": [
          {
            "expr": "sum(rate(llm_requests_total[1m]))",
            "instant": true
          }
        ],
        "thresholds": [
          { "value": 100, "color": "green" },
          { "value": 50, "color": "orange" },
          { "value": 10, "color": "red" }
        ]
      }
    ]
  }
}
```

---


## 4. Alert Rule Configuration

### 4.1 Core Alert Rules

```yaml
# ai-alert-rules.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: ai-platform-alerts
  namespace: ai-monitoring
  labels:
    team: ai-platform
spec:
  groups:
  - name: ai.gpu.rules
    rules:
    # High GPU utilization alert
    - alert: HighGPUUtilization
      expr: avg by(node)(DCGM_FI_DEV_GPU_UTIL) > 95
      for: 5m
      labels:
        severity: warning
        team: ai-platform
      annotations:
        summary: "GPU utilization is too high ({{ $labels.node }})"
        description: "Average GPU utilization on node {{ $labels.node }} reaches {{ $value }}%"
        
    # Abnormal GPU temperature alert
    - alert: HighGPUTemperature
      expr: DCGM_FI_DEV_GPU_TEMP > 85
      for: 2m
      labels:
        severity: critical
        team: ai-platform
      annotations:
        summary: "GPU temperature is too high ({{ $labels.node }})"
        description: "GPU temperature on node {{ $labels.node }} reaches {{ $value }}°C"
        
  - name: ai.inference.rules
    rules:
    # High inference latency alert
    - alert: HighInferenceLatency
      expr: histogram_quantile(0.99, sum(rate(llm_request_duration_seconds_bucket[5m])) by (le)) > 0.5
      for: 3m
      labels:
        severity: warning
        service: llm-inference
      annotations:
        summary: "Inference latency is too high"
        description: "P99 latency exceeds 500ms, current value: {{ $value }}s"
        
    # Rising inference error rate alert
    - alert: HighInferenceErrorRate
      expr: sum(rate(llm_requests_failed_total[5m])) / sum(rate(llm_requests_total[5m])) > 0.01
      for: 2m
      labels:
        severity: critical
        service: llm-inference
      annotations:
        summary: "Inference error rate is abnormal"
        description: "Error rate exceeds 1%, current value: {{ $value | humanizePercentage }}"
```

### 4.2 Configuration of Alert Notification

```yaml
# alertmanager-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: alertmanager-config
  namespace: ai-monitoring
data:
  alertmanager.yml: |
    global:
      resolve_timeout: 5m
      smtp_smarthost: 'smtp.company.com:587'
      smtp_from: 'alerts@company.com'
      
    route:
      group_by: ['alertname', 'team']
      group_wait: 30s
      group_interval: 5m
      repeat_interval: 3h
      
      # AI Platform Alert Routing
      routes:
      - matchers:
        - team="ai-platform"
        receiver: ai-slack
        continue: true
      - matchers:
        - severity="critical"
        receiver: ai-critical
    receivers:
    - name: ai-slack
      slack_configs:
      - api_url: 'https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK'
        channel: '#ai-platform-alerts'
        send_resolved: true
        title: '{{ template "slack.title" . }}'
        text: '{{ template "slack.text" . }}'
        
    - name: ai-critical
      email_configs:
      - to: 'ai-team@company.com'
        send_resolved: true
        html: '{{ template "email.html" . }}'
```

---


## 5. Log Collection and Analysis

### 5.1 Configuration of Fluentd

```yaml
# fluentd-config.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluentd-config
  namespace: ai-monitoring
data:
  fluent.conf: |
    <source>
      @type tail
      path /var/log/containers/*_ai-*_*.log
      pos_file /var/log/fluentd-containers.log.pos
      tag kubernetes.*
      read_from_head true
      <parse>
        @type json
        time_key time
        time_format %Y-%m-%dT%H:%M:%S.%NZ
      </parse>
    </source>
    
    <filter kubernetes.**>
      @type kubernetes_metadata
      @id filter_kube_metadata
    </filter>
    
    # Specific Log Processing for AI
    <filter kubernetes.var.log.containers.*_ai-*_*.log>
      @type record_transformer
      <record>
        log_type ${if record["log"].include?("TRAINING"); "training";
                 elsif record["log"].include?("INFERENCE"); "inference";
                 else "general"; end}
        model_name ${record["kubernetes"]["labels"]["model"] || "unknown"}
        job_name ${record["kubernetes"]["labels"]["job-name"] || "unknown"}
      </record>
    </filter>
    
    <match kubernetes.**>
      @type loki
      url "http://loki:3100"
      tenant_id "ai-platform"
      <label>
        job kubernetes
        node ${record.dig("kubernetes", "host")}
        namespace ${record.dig("kubernetes", "namespace_name")}
        pod ${record.dig("kubernetes", "pod_name")}
        container ${record.dig("kubernetes", "container_name")}
        log_type ${record["log_type"]}
        model_name ${record["model_name"]}
      </label>
    </match>
```

### 5.2 Example of Loki Query

```logql
# Querying Change in Loss Value in Training Logs
{namespace="ai-training", log_type="training"} 
|~ "loss=" 
| regexp "loss=(?P<loss>[0-9.]+)" 
| unwrap loss 
| __error__="" 

# Querying Inference Error Logs
{namespace="ai-inference", log_type="inference"} 
|= "ERROR" 
| json 
| level="ERROR"

# Counting Errors for Each Model
sum by(model_name) (
  count_over_time(
    {namespace="ai-inference"} |= "ERROR" [1h]
  )
)
```

---


## 6. Cost Monitoring Integration

### 6.1 Configuration of Kubecost Integration

```yaml
# kubecost-ai-integration.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: kubecost-ai-config
  namespace: ai-monitoring
data:
  # AI Workload Cost Allocation Rules
  cost-analyzer-config.yaml: |
    # Allocate costs by tag
    allocation:
      labels:
        - team
        - project
        - model
        - environment
        - cost-center
      
      # Specific Cost Allocation Rules for AI
      sharedNamespaces:
        - ai-monitoring
        - ai-ops
      sharedLabels:
        team: ai-platform
        
    # Custom Pricing for GPUs
    pricing:
      customPrices:
        GPU:
          nvidia.com/gpu:
            price: "32.77"  # A100按需价格
            spotPrice: "10.00"
            
    # Cost Alarm Configuration
    alerts:
      budgets:
        - name: "ai-monthly-budget"
          amount: 50000
          aggregation: "namespace"
          filter: "namespace: ai-*"
          window: "month"
          
      efficiency:
        - name: "gpu-utilization"
          threshold: 30
          filter: "label_app: vllm or label_app: training-job"
          window: "7d"
```

### 6.2 Cost Visualization Panel

```json
{
  "dashboard": {
    "title": "AI Platform Cost Analysis",
    "panels": [
      {
        "type": "timeseries",
        "title": "Daily GPU Cost Trend",
        "targets": [
          {
            "expr": "sum by(namespace)(kubecost_node_gpu_hourly_cost * 24)",
            "legendFormat": "{{namespace}}"
          }
        ]
      },
      {
        "type": "piechart",
        "title": "Cost by Model Type",
        "targets": [
          {
            "expr": "topk(5, sum by(label_model)(kubecost_namespace_gpu_cost_total))",
            "legendFormat": "{{label_model}}"
          }
        ]
      }
    ]
  }
}
```

---


## 7. Best Practices

### 7.1 Monitoring Configuration Checklist

✅ **Infrastructure Monitoring**
- [ ] All GPU nodes have DCGM Exporter
- [ ] Node resource usage monitoring is in place
- [ ] Network bandwidth and latency monitoring configured
- [ ] Storage I/O and capacity monitoring enabled

✅ **Application Performance Monitoring**
- [ ] Collect Loss/Accuracy metrics for training tasks
- [ ] Monitor inference service latency/throughput
- [ ] Track model version and deployment status
- [ ] Monitor error rate and success rate

✅ **Alert Configuration**
- [ ] Key metrics have corresponding alert rules
- [ ] Correct alert grading and routing configuration
- [ ] Notification channels are tested successfully
- [ ] Alert suppression and silent rules are set up

✅ **Log Management**
- [ ] Unified structured log format
- [ ] Appropriate labels for key fields
- [ ] Clear log retention policy
- [ ] Abnormal logs can be quickly searched

### 7.2 Common Issue Troubleshooting

**GPU monitoring has no data**
``` bash
# 🟡 Medium Risk: Will modify cluster/resource status, please confirm target, impact scope, and authorization before execution
# Check DCGM Exporter status
kubectl get pods -n ai-monitoring -l app=dcgm-exporter
kubectl logs -n ai-monitoring -l app=dcgm-exporter

# Verify metric collection
kubectl port-forward svc/dcgm-exporter 9400:9400
curl http://localhost:9400/metrics | grep DCGM_FI
```
**Inference latency alerts occur frequently**
``` bash
# 🟢 Low Risk: Read-only/information gathering, usually has no side effects
# Check inference service resource usage
kubectl top pods -n ai-inference -l app=vllm
kubectl describe nodes | grep -A 10 "Allocated resources"

# Analyze slow query logs
kubectl logs -n ai-inference -l app=vllm --since=1h | grep "slow"
```
**Cost exceeds budget**
``` bash
# 🟢 Low Risk: Read-only/information gathering, usually has no side effects
# View real-time cost
kubectl get --raw /apis/metrics.k8s.io/v1beta1/namespaces/ai-training/pods

# Analyze resource waste
kubectl get pods -n ai-training -o wide | grep -E "(Pending|Evicted)"
```
---

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
- AI Model Registry Center and Version Management

## See Also

- 11-ai-security-model-protection
- 12-ai-cost-analysis-finops
- 14-troubleshooting-performance
- 15-llm-data-pipeline

## Related

- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Index]]
- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Index]]


<!-- risk-assessed -->
