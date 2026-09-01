---title: Kubernetes v1.29-v1.33 Observability New Features Guide
description: 'title: Kubernetes v1.29-v1.33 Observability New Features Guide'
summary: 'title: Kubernetes v1.29-v1.33 Observability New Features Guide'
category: general
tags:
- k8s
- observability
- prometheus
- monitoring
- guide
- apiserver
- kubelet
- scheduler
- controller-manager
- grafana
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All engineers
estimated_read_time: 15min
intent_queries:
- What is Kubernetes?
- How do I use Kubernetes?
- What are Kubernetes best practices?
trigger_keywords:
- Kubernetes
- v1.29-v1.33
- Observability new features guide
- observability
prerequisites:
- kubectl-basics
- observability-basics
- prometheus-basics
- monitoring-basics
- cilium-basics
- cni-basics
- logging-basics
- tracing-basics
original_language: Chinese
authors:
- name: Dillan Teagle
  role: contributor
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/01-overview/99-kubernetes-v1.33-observability-guide.md
---

> **Production Environment Security Warning**
>
> This document contains directly executable operations commands. Before execution, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have verified in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state but usually can be rolled back), 🟢 Low risk/read-only (information gathering, no side effects).




title: [[Kubernetes|Kubernetes]] v1.29-v1.33 Observability New Features Guide
description: '# Kubernetes v1.29-v1.33 Observability New Features Guide'
category: observability
tags:
- k8s
- observability
- monitoring
- logging
- tracing
- apiserver
- kubelet
- scheduler
- controller-manager
- prometheus
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Operations engineers
- Monitoring engineers
estimated_read_time: 5min
intent_queries:
- What is Kubernetes v1.29-v1.33 Observability New Features Guide
- How do I use Kubernetes v1.29-v1.33 Observability New Features Guide
- What are Kubernetes observability best practices
trigger_keywords:
- Kubernetes
- v1.29-v1.33
- Observability new features guide
- observability
cross_refs:
- type: domain
  path: ../domain-01-cluster-fundamentals/
  label: 'Related knowledge domain: domain-01-cluster-fundamentals'
- type: domain
  path: ../domain-02-workloads-applications/
  label: 'Related knowledge domain: domain-02-workloads-applications'
- type: domain
  path: ../domain-03-networking-traffic/
  label: 'Related knowledge domain: domain-03-networking-traffic'
- type: domain
  path: ../domain-07-platform-engineering/
  label: 'Related knowledge domain: domain-07-platform-engineering'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/promql.md
  label: 'Quick reference: promql'
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

# Kubernetes v1.29-v1.33 Observability New Features Guide

> **Applicable versions**: Kubernetes v1.29 - v1.33  
> **Last updated**: 2026-04-24  
> **Purpose**: Deep dive into new observability features and integration practices

---

<!-- chunk: Table of Contents -->
## Table of Contents

- [1. Kubelet OpenTelemetry Tracing (v1.31 GA)](#1-kubelet-opentelemetry-tracing-v131-ga)
- [2. Kubelet Resource Metrics (v1.33 Beta)](#2-kubelet-resource-metrics-v133-beta)
- [3. Structured Logging Enhancement](#3-structured-logging-enhancement)
- [4. Node Log Query (v1.30 Alpha)](#4-node-log-query-v130-alpha)
- [5. Pod-level Resource Metrics and Monitoring](#5-pod-level-resource-metrics-and-monitoring)
- [6. Event Streaming Optimization](#6-event-streaming-optimization)
- [7. Production Observability Architecture Recommendations](#7-production-observability-architecture-recommendations)

---

<!-- chunk: 1. Kubelet OpenTelemetry Tracing (v1.31 GA) -->
## 1. Kubelet OpenTelemetry Tracing (v1.31 GA)

### 1.1 Core Concepts

KubeletTracing incorporates distributed tracing capabilities into Kubelet and exports tracing data via the OTLP protocol.

### 1.2 Architecture

```
User creates Pod
    │
    ▼
APIServer ──Span──► Kubelet ──Span──► CRI (containerd/CRI-O)
    │                    │
    │                    ├── Span ──► CNI (Cilium/Calico)
    │                    │
    │                    └── Span ──► CSI (storage driver)
    │
    └── All Spans exported via OTLP
                │
                ▼
        OpenTelemetry Collector
                │
        ┌───────┴───────┐
        ▼               ▼
    Jaeger/Tempo    Prometheus/Grafana
```

### 1.3 Kubelet Configuration

```yaml
# /var/lib/kubelet/config.yaml
featureGates:
  KubeletTracing: true  # v1.31 GA, enabled by default

tracing:
  endpoint: "localhost:4317"  # OTLP gRPC endpoint
  samplingRatePerMillion: 100000  # 10% sampling rate
```

### 1.4 Verify Tracing Data

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
# Check if Kubelet is exporting traces
curl -s http://localhost:10248/healthz?verbose | grep tracing

# View tracing endpoint configuration
kubectl get --raw /api/v1/nodes/NODE_NAME/proxy/configz | jq '.kubeletconfig.tracing'
```
### 1.5 Tracing Context Propagation

```yaml
# Pod configuration: enable tracing context injection
apiVersion: v1
kind: Pod
metadata:
  name: traced-app
spec:
  containers:
    - name: app
      image: myapp:v1.0
      env:
        # Inject tracing information via Downward API
        - name: OTEL_SERVICE_NAME
          value: "myapp"
        - name: OTEL_EXPORTER_OTLP_ENDPOINT
          value: "http://otel-collector.monitoring:4317"
```

---

<!-- chunk: 2. Kubelet Resource Metrics (v1.33 Beta) -->
## 2. Kubelet Resource Metrics (v1.33 Beta)

### 2.1 Core Concepts

Provides standardized node resource utilization metrics without requiring metrics-server to obtain core resource usage information.

### 2.2 Metrics Endpoint

```
# Kubelet resource metrics endpoint
GET /metrics/resource

Returned metrics:
├── container_cpu_usage_seconds_total
├── container_memory_working_set_bytes
├── pod_cpu_usage_seconds_total
├── pod_memory_working_set_bytes
├── node_cpu_usage_seconds_total
├── node_memory_working_set_bytes
├── container_start_time_seconds
└── pod_start_time_seconds
```

### 2.3 Enable Configuration

```yaml
# /var/lib/kubelet/config.yaml
featureGates:
  KubeletResourceMetrics: true  # v1.33 Beta, enabled by default
```

### 2.4 Prometheus Scrape Configuration

```yaml
# Prometheus ServiceMonitor
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: kubelet-resource-metrics
  namespace: monitoring
spec:
  endpoints:
    - bearerTokenFile: /var/run/secrets/kubernetes.io/serviceaccount/token
      honorLabels: true
      interval: 15s
      path: /metrics/resource
      port: https-metrics
      scheme: https
      tlsConfig:
        insecureSkipVerify: true
  namespaceSelector:
    matchNames:
      - kube-system
  selector:
    matchLabels:
      k8s-app: kubelet
```

### 2.5 Comparison with metrics-server

| Feature | metrics-server | KubeletResourceMetrics |
|:---|:---|:---|
| Data source | Summary API (/stats/summary) | Dedicated endpoint (/metrics/resource) |
| Data format | JSON | Prometheus format |
| Precision | Cumulative value | Standardized counter/gauge |
| Overhead | Higher (JSON serialization) | Lower |
| Dependency | Must be deployed | Built-in to kubelet |

---

<!-- chunk: 3. Structured Logging Enhancement -->
## 3. Structured Logging Enhancement

### 3.1 Core Concepts

v1.29+ progressively advances structured logging, migrating traditional text logs to key-value pair format.

### 3.2 Log Format Comparison

```
Traditional log (text):
I0424 10:30:15.123456    1234 controller.go:456] "Pod created" pod="default/nginx-123"

Structured log (json):
{
  "ts": 1713957015.123456,
  "level": "info",
  "caller": "controller.go:456",
  "msg": "Pod created",
  "pod": "default/nginx-123",
  "controller": "deployment",
  "reconcileID": "abc-123-def"
}
```

### 3.3 Component Configuration

```bash
# API Server
kube-apiserver --logging-format=json

# Controller Manager
kube-controller-manager --logging-format=json

# Scheduler
kube-scheduler --logging-format=json

# Kubelet
# /var/lib/kubelet/config.yaml
logging:
  format: json
  verbosity: 2
```

### 3.4 Fluent Bit Parse Configuration

```yaml
# fluent-bit-config.yaml
[PARSER]
    Name        k8s-json
    Format      json
    Time_Key    ts
    Time_Format %s.%L
    Time_Keep   On

[FILTER]
    Name                kubernetes
    Match               kube.*
    Kube_URL            https://kubernetes.default.svc:443
    Kube_CA_File        /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    Kube_Token_File     /var/run/secrets/kubernetes.io/serviceaccount/token
```

---

<!-- chunk: 4. Node Log Query (v1.30 Alpha) -->
## 4. Node Log Query (v1.30 Alpha)

### 4.1 Core Concepts

Directly query system service logs on nodes via kubectl without requiring SSH access to the node.

### 4.2 Enable Configuration

```yaml
# /var/lib/kubelet/config.yaml
featureGates:
  NodeLogQuery: true
```

### 4.3 Query Commands

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
# Query kubelet logs from all nodes
kubectl node-logs --all-nodes --query="kubelet"

# Query systemd service logs from a specific node
kubectl node-logs node-1 --service=kubelet --since=1h

# Query kernel logs
kubectl node-logs node-1 --query="kernel"

# Query container runtime logs
kubectl node-logs node-1 --service=containerd
```
### 4.4 RBAC Configuration

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: node-log-reader
rules:
  - apiGroups: [""]
    resources: ["nodes/log"]
    verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: node-log-reader-binding
subjects:
  - kind: Group
    name: oncall-engineers
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: ClusterRole
  name: node-log-reader
  apiGroup: rbac.authorization.k8s.io
```

---

<!-- chunk: 5. Pod-level Resource Metrics and Monitoring -->
## 5. Pod-level Resource Metrics and Monitoring

### 5.1 Resource Utilization Monitoring

```yaml
# PrometheusRule: Pod resource alerts
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: pod-resource-alerts
  namespace: monitoring
spec:
  groups:
    - name: pod-resources
      rules:
        # CPU usage alert
        - alert: PodHighCPUUsage
          expr: |
            (
              rate(container_cpu_usage_seconds_total[5m])
              /
              kube_pod_container_resource_limits{resource="cpu"}
            ) > 0.8
          for: 5m
          labels:
            severity: warning
          annotations:
            summary: "Pod {{ $labels.pod }} CPU usage exceeds 80%"
            
        # Memory usage alert
        - alert: PodHighMemoryUsage
          expr: |
            (
              container_memory_working_set_bytes
              /
              kube_pod_container_resource_limits{resource="memory"}
            ) > 0.9
          for: 5m
          labels:
            severity: critical
          annotations:
            summary: "Pod {{ $labels.pod }} memory usage exceeds 90%"
```

### 5.2 Dashboard based on KubeletResourceMetrics

```json
{
  "dashboard": {
    "title": "Kubernetes Resource Utilization (v1.33+)",
    "panels": [
      {
        "title": "Node CPU Usage",
        "targets": [
          {
            "expr": "rate(node_cpu_usage_seconds_total[5m])",
            "legendFormat": "{{node}}"
          }
        ]
      },
      {
        "title": "Pod Memory Working Set",
        "targets": [
          {
            "expr": "pod_memory_working_set_bytes",
            "legendFormat": "{{pod}}"
          }
        ]
      }
    ]
  }
}
```

---

<!-- chunk: 6. Event Streaming Optimization -->
## 6. Event Streaming Optimization

### 6.1 Core Concepts

v1.29+ optimized Event API performance and supports more efficient streaming.

### 6.2 Event Query Optimization

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
# Use field-selector for efficient filtering
kubectl get events --field-selector reason=FailedScheduling

# Query by time range
kubectl get events --sort-by='.lastTimestamp' | tail -50

# Use watch for stream monitoring
kubectl get events --watch --field-selector type=Warning
```
### 6.3 Event Persistence Recommendations

```yaml
# Event Exporter configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kubernetes-event-exporter
  namespace: monitoring
spec:
  replicas: 1
  selector:
    matchLabels:
      app: event-exporter
  template:
    metadata:
      labels:
        app: event-exporter
    spec:
      containers:
        - name: exporter
          image: ghcr.io/resmoio/kubernetes-event-exporter:v1.7
          args:
            - --config=/config/config.yaml
          volumeMounts:
            - name: config
              mountPath: /config
      volumes:
        - name: config
          configMap:
            name: event-exporter-config
---
# Output to Loki
apiVersion: v1
kind: ConfigMap
metadata:
  name: event-exporter-config
data:
  config.yaml: |
    logLevel: info
    logFormat: json
    route:
      routes:
        - matchers:
          - - receiver="loki"
    receivers:
      - name: loki
        loki:
          url: http://loki.monitoring:3100/loki/api/v1/push
          streamLabels:
            source: kubernetes-event-exporter
```

---

<!-- chunk: 7. Production Observability Architecture Recommendations -->
## 7. Production Observability Architecture Recommendations

### 7.1 v1.33 Recommended Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     Collection Layer (Agent)                │
├─────────────┬─────────────┬─────────────┬───────────────────┤
│  Prometheus │  Fluent Bit │  OTel Agent │  Event Exporter   │
│  (Metrics)  │  (Logs)     │  (Traces)   │  (Events)         │
└──────┬──────┴──────┬──────┴──────┬──────┴─────────┬─────────┘
       │             │             │                │
       ▼             ▼             ▼                ▼
┌─────────────────────────────────────────────────────────────┐
│                    Processing Layer (Pipeline)              │
├─────────────┬─────────────┬─────────────────────────────────┤
│  Prometheus │  Loki       │  Tempo/Jaeger                   │
│  (TSDB)     │  (Log Store)│  (Trace Store)                  │
└──────┬──────┴──────┬──────┴────────────────┬────────────────┘
       │             │                       │
       ▼             ▼                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    Visualization Layer (Visualization)      │
├─────────────────────────────────────────────────────────────┤
│                      Grafana Unified                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────────┐    │
│  │ Metrics │  │ Logs    │  │ Traces  │  │ Alerting    │    │
│  │ Dashboard│  │ Explore │  │ Explore │  │ Rules       │    │
│  └─────────┘  └─────────┘  └─────────┘  └─────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Key Metrics Checklist

| Level | Metric | Source | Alert Threshold |
|:---|:---|:---|:---|
| Cluster | Node ready rate | kube_node_status_condition | < 90% |
| Cluster | API Server request latency | apiserver_request_duration_seconds | P99 > 1s |
| Node | CPU usage | node_cpu_usage_seconds_total | > 80% |
| Node | Memory usage | node_memory_working_set_bytes | > 90% |
| Pod | CPU usage | container_cpu_usage_seconds_total | > 80% of limits |
| Pod | Memory usage | container_memory_working_set_bytes | > 90% of limits |
| Pod | Restart count | kube_pod_container_status_restarts_total | > 3/hour |
| Storage | PVC usage | kubelet_volume_stats_used_bytes | > 85% |

### 7.3 Version Feature Enablement Checklist

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
#!/bin/bash
# check-observability-features.sh

echo "=== K8s v1.33 Observability Features Check ==="

# 1. Kubelet Tracing
echo "[1] Kubelet Tracing (GA v1.31)"
kubectl get --raw /api/v1/nodes/$(kubectl get nodes -o jsonpath='{.items[0].metadata.name}')/proxy/configz | jq -r '.kubeletconfig.tracing.endpoint // "not configured"'

# 2. Kubelet Resource Metrics
echo "[2] Kubelet Resource Metrics (Beta v1.33)"
curl -sk https://$(kubectl get nodes -o jsonpath='{.items[0].status.addresses[0].address}'):10250/metrics/resource --header "Authorization: Bearer $(kubectl get secrets -n kube-system -o jsonpath='{.items[?(@.type=="kubernetes.io/service-account-token")].data.token}' | base64 -d)" 2>/dev/null | head -5 || echo "unable to access"

# 3. Structured logging
echo "[3] Structured logging format"
kubectl get pods -n kube-system -l component=kube-apiserver -o jsonpath='{.items[0].spec.containers[0].command}' | grep -o 'logging-format=[^,}]*' || echo "default text"

# 4. Node Log Query
echo "[4] Node Log Query (Alpha v1.30)"
kubectl get --raw /api/v1/nodes/$(kubectl get nodes -o jsonpath='{.items[0].metadata.name}')/proxy/configz | jq -r '.kubeletconfig.featureGates.NodeLogQuery // "not enabled"'

echo "=== Check complete ==="
```
---

<!-- chunk: References -->
## References

- [KEP-2831: Kubelet Tracing](https://github.com/kubernetes/enhancements/tree/master/keps/sig-instrumentation/2831-kubelet-tracing)
- [KEP-727: Kubelet Resource Metrics](https://github.com/kubernetes/enhancements/tree/master/keps/sig-instrumentation/727-resource-metrics)
- [Structured Logging](https://kubernetes.io/docs/concepts/cluster-administration/system-logs/)
- [Node Log Query](https://kubernetes.io/docs/concepts/cluster-administration/node-log-query/)

---

<!-- chunk: Obsidian Related Documents -->
## Obsidian Related Documents

- domain-06-observability MOC
- [[domain-06-observability/README.md|Observability Domain]]
- [[domain-06-observability/00-open-source-projects-index.md|Domain-8 Observability — Open Source Projects Index]]
- Kubernetes observability architecture system
- Metrics monitoring system explained in detail
- 03 - Logging Collection Architecture (Logging Architecture)
- Distributed tracing system
- 05 - Alerting Management Strategy (Alerting Management)
- 06 - Monitoring Alerting Practice and Best Practices (Monitoring Alerting Practice)
- 04 - Monitoring Dashboard Design and Best Practices (Monitoring Dashboards)
- 08 - Logging Audit and Compliance Management (Logging Auditing & Compliance)
- 05 - Events and Audit Log Management (Events & Audit Logs)

## Related

- 12-demo-env-guide
- 21-platform-selection-guide
- [[domain-02-workloads-applications/07-java-observability-kubernetes.md|07-java-observability-kubernetes]]

- [[domain-06-observability/README.md|Back to index]]- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Graph Index]]

## See Also

- 27-performance-profiling-tools
- 99-java-observability-kubernetes-guide
- FINAL-QUALITY-ASSESSMENT
- QUALITY-REPORT


<!-- risk-assessed -->
