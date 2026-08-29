---
title: Monitoring & Alerting System
description: In-depth analysis of enterprise-grade monitoring and alerting systems: Prometheus/Grafana deep integration, SLO/SLI/SLA engineering practices, alert aggregation and suppression, On-Call duty rotation and MTTR optimization
summary: In-depth analysis of enterprise-grade monitoring and alerting systems: Prometheus/Grafana deep integration, SLO/SLI/SLA engineering practices, alert aggregation and suppression, On-Call duty rotation and MTTR optimization
category: domain-07-platform-engineering
tags:
- k8s
- monitoring
- alerting
- prometheus
- grafana
- slo
- sli
- sla
- oncall
- mttr
tier: core
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
- What is a monitoring and alerting system
- How to implement a monitoring and alerting system
- Kubernetes platform ops best practices
trigger_keywords:
- Monitoring and alerting system
- platform
- ops
prerequisites:
- kubectl-basics
- platform-engineering-basics
- prometheus-basics
- monitoring-basics
- logging-basics
- tracing-basics
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
- type: fta
  path: ../domain-10-troubleshooting-diagnostics/topic-fta/list/monitoring-fta.md
  label: 'Fault Tree: monitoring'
related_docs:
- path: 01-platform-ops-overview.md
  type: depth
  desc: Platform Ops Overview
- path: 02-cluster-lifecycle-management.md
  type: depth
  desc: Cluster Lifecycle Management
- path: ../domain-06-observability/02-monitoring-metrics-system.md
  type: depth
  desc: Metrics Monitoring System
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/operate/06-monitoring-alerting-system.md
original_language: Chinese
---

> **Production Environment Safety Reminder**
>
> This document contains directly executable operations commands. Before execution, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have verified in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state, but usually reversible), 🟢 Low risk/read-only (information gathering, no side effects).




# Monitoring & Alerting System

<!-- chunk: Overview -->
## Overview

The monitoring and alerting system is the eyes and ears of platform operations, ensuring stable platform operation and rapid problem response through comprehensive data collection, intelligent analysis and alerting, and visual presentation.

<!-- chunk: Core Component Architecture -->
## Core Component Architecture

### 1. Data Collection Layer
```
Metrics Collection → Log Aggregation → Distributed Tracing → Event Monitoring
```

### 2. Data Processing Layer
```
Data Cleaning → Format Conversion → Aggregation Calculation → Storage Persistence
```

### 3. Analysis & Alerting Layer
```
Anomaly Detection → Root Cause Analysis → Alert Generation → Notification Distribution
```

### 4. Display & Management Layer
```
Dashboards → Report Analysis → Historical Queries → Decision Support
```

<!-- chunk: Prometheus Monitoring System -->
## Prometheus Monitoring System

### Core Components
```yaml
# Prometheus Deployment Configuration
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: prometheus
spec:
  serviceName: prometheus
  replicas: 3
  selector:
    matchLabels:
      app: prometheus
  template:
    metadata:
      labels:
        app: prometheus
    spec:
      containers:
      - name: prometheus
        image: prom/prometheus:v3.2.1
        args:
        - '--config.file=/etc/prometheus/prometheus.yml'
        - '--storage.tsdb.path=/prometheus'
        - '--web.console.libraries=/etc/prometheus/console_libraries'
        - '--web.console.templates=/etc/prometheus/consoles'
        - '--storage.tsdb.retention.time=30d'
        ports:
        - containerPort: 9090
        volumeMounts:
        - name: prometheus-config
          mountPath: /etc/prometheus
        - name: prometheus-storage
          mountPath: /prometheus
```

### Service Discovery Configuration
```yaml
# Kubernetes Service Discovery
scrape_configs:
- job_name: 'kubernetes-nodes'
  kubernetes_sd_configs:
  - role: node
  relabel_configs:
  - source_labels: [__address__]
    regex: '(.*):10250'
    target_label: __address__
    replacement: '${1}:9100'

- job_name: 'kubernetes-pods'
  kubernetes_sd_configs:
  - role: pod
  relabel_configs:
  - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
    action: keep
    regex: true
```

### Key Monitoring Metrics

#### Cluster-Level Metrics
```promql
# Cluster Health Status
up{job="kubernetes-apiservers"} == 1
kube_node_status_condition{condition="Ready",status="true"} == 1

# Resource Utilization
sum(kube_pod_container_resource_requests{resource="cpu"}) / sum(kube_node_status_allocatable{resource="cpu"})
sum(kube_pod_container_resource_requests{resource="memory"}) / sum(kube_node_status_allocatable{resource="memory"})

# Pod Status Statistics
count(kube_pod_status_phase{phase="Running"})
count(kube_pod_status_phase{phase="Pending"})
count(kube_pod_status_phase{phase="Failed"})
```

#### Node-Level Metrics
```promql
# CPU Utilization
100 - (avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Memory Utilization
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

# Disk I/O
rate(node_disk_reads_completed_total[5m])
rate(node_disk_writes_completed_total[5m])

# Network Traffic
rate(node_network_receive_bytes_total{device!="lo"}[5m])
rate(node_network_transmit_bytes_total{device!="lo"}[5m])
```

#### Application-Level Metrics
```promql
# HTTP Request Latency
histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))

# Error Rate
rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])

# Throughput
rate(http_requests_total[5m])
```

<!-- chunk: Grafana Visualization -->
## Grafana Visualization

### Dashboard Design Principles
```json
{
  "dashboard": {
    "title": "Kubernetes Cluster Overview",
    "panels": [
      {
        "title": "Cluster Health Status",
        "type": "stat",
        "targets": [
          {
            "expr": "sum(up{job=\"kubernetes-apiservers\"})",
            "legendFormat": "Number of API Servers Online"
          }
        ]
      },
      {
        "title": "Resource Usage Trends",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(kube_pod_container_resource_requests{resource=\"cpu\"})",
            "legendFormat": "Total CPU Requests"
          },
          {
            "expr": "sum(kube_pod_container_resource_limits{resource=\"cpu\"})",
            "legendFormat": "Total CPU Limits"
          }
        ]
      }
    ]
  }
}
```

### Common Dashboard Templates
- **Cluster Overview**: Overall cluster status overview
- **Node Resources**: Node resource utilization
- **Pod Performance**: Pod performance metrics
- **Network Traffic**: Network traffic analysis
- **Storage Usage**: Storage usage statistics
- **Application Metrics**: Application performance monitoring

<!-- chunk: AlertManager Management -->
## AlertManager Management

### Alert Rule Configuration
```yaml
# Alert Rule Examples
groups:
- name: kubernetes.rules
  rules:
  - alert: KubeAPIDown
    expr: absent(up{job="kubernetes-apiservers"} == 1)
    for: 10m
    labels:
      severity: critical
    annotations:
      summary: "Kubernetes API Server is unavailable"
      description: "API Server could not be reached in the past 10 minutes"

  - alert: NodeNotReady
    expr: kube_node_status_condition{condition="Ready",status!="true"} == 1
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "Node {{ $labels.node }} is not ready"
      description: "Node status is abnormal for more than 5 minutes"

  - alert: HighCPUUsage
    expr: (1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m]))) * 100 > 80
    for: 15m
    labels:
      severity: warning
    annotations:
      summary: "Node CPU usage is too high"
      description: "Node {{ $labels.instance }} CPU usage exceeds 80%"
```

### Notification Routing Configuration
```yaml
# Notification Routing
route:
  group_by: ['alertname']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 3h
  receiver: 'default'
  
  routes:
  - matchers:
    - severity="critical"
    receiver: pagerduty
  - matchers:
    - severity="warning"
    receiver: slack
  - matchers:
    - service=~"^(frontend|backend)$"
    receiver: service-team
receivers:
- name: 'default'
  email_configs:
  - to: 'alerts@example.com'
- name: 'pagerduty'
  pagerduty_configs:
  - routing_key: '<pagerduty-service-key>'
- name: 'slack'
  slack_configs:
  - api_url: '<slack-webhook-url>'
    channel: '#alerts'
```

<!-- chunk: Log Collection System -->
## Log Collection System

### Fluentd Configuration
```xml
<source>
  @type tail
  path /var/log/containers/*.log
  pos_file /var/log/fluentd-containers.log.pos
  tag kubernetes.*
  read_from_head true
  <parse>
    @type json
    time_format %Y-%m-%dT%H:%M:%S.%NZ
  </parse>
</source>

<filter kubernetes.**>
  @type kubernetes_metadata
</filter>

<match kubernetes.var.log.containers.**_nginx_**.log>
  @type elasticsearch
  host elasticsearch
  port 9200
  logstash_format true
  logstash_prefix nginx-access
</match>
```

### Loki Log System
```yaml
# Loki Configuration
auth_enabled: false

server:
  http_listen_port: 3100

ingester:
  lifecycler:
    address: 127.0.0.1
    ring:
      kvstore:
        store: inmemory
      replication_factor: 1
  chunk_idle_period: 1h
  max_chunk_age: 1h
  chunk_target_size: 1048576
  chunk_retain_period: 30s

schema_config:
  configs:
  - from: 2020-10-24
    store: boltdb-shipper
    object_store: filesystem
    schema: v11
    index:
      prefix: index_
      period: 24h
```

<!-- chunk: Distributed Tracing System -->
## Distributed Tracing System

### Jaeger Configuration
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jaeger
spec:
  selector:
    matchLabels:
      app: jaeger
  template:
    metadata:
      labels:
        app: jaeger
    spec:
      containers:
      - name: jaeger
        image: jaegertracing/all-in-one:1.47
        ports:
        - containerPort: 16686
          name: query-http
        - containerPort: 14268
          name: collector-http
        env:
        - name: SPAN_STORAGE_TYPE
          value: badger
        - name: BADGER_EPHEMERAL
          value: "false"
        - name: BADGER_DIRECTORY_VALUE
          value: "/badger/data"
        - name: BADGER_DIRECTORY_KEY
          value: "/badger/key"
        volumeMounts:
        - name: data
          mountPath: /badger
      volumes:
      - name: data
        emptyDir: {}
```

<!-- chunk: SLO/SLI Definition -->
## SLO/SLI Definition

### Service Quality Metrics
```yaml
# SLO Configuration Examples
slos:
- name: api-server-availability
  objective: 99.9
  sli:
    good: up{job="kubernetes-apiservers"} == 1
    total: up{job="kubernetes-apiservers"}
  window: 30d

- name: pod-startup-latency
  objective: 95
  sli:
    good: histogram_quantile(0.95, rate(pod_startup_duration_seconds_bucket[5m])) < 30
    total: rate(pod_startup_duration_seconds_count[5m])
  window: 7d
```

### Alert Threshold Configuration
- **API Server Availability**: < 99.9% sends critical alert
- **Node Ready Rate**: < 95% sends warning alert
- **Pod Restart Rate**: > 10 times/hour sends warning alert
- **CPU Utilization**: > 80% sends warning alert, > 90% sends critical alert

<!-- chunk: Best Practices -->
## Best Practices

### 1. Layered Monitoring Strategy
- Infrastructure layer monitoring
- Platform service layer monitoring
- Application business layer monitoring
- User experience layer monitoring

### 2. Intelligent Alert Mechanism
- Alert deduplication and suppression
- Alert severity-based handling
- Root cause correlation analysis
- Automatic recovery verification

### 3. Visualization Design Principles
- Key metrics prominently displayed
- Trends clearly visible
- Anomalies immediately highlighted in red
- Intuitive and user-friendly interactions

### 4. Continuous Optimization and Improvement
- Regular review of alert rules
- Optimize monitoring metric coverage
- Improve alert accuracy
- Enhance user experience

By establishing a comprehensive monitoring and alerting system, you can achieve full control over platform status, quickly discover problems and respond promptly, and provide strong support for stable business operations.

---

<!-- chunk: Obsidian Related Documents -->
## Obsidian Related Documents

- domain-07-platform-engineering KUDIG Database — Global MOC
- [[domain-07-platform-engineering/README.md|[[Platform Ops Domain|Platform Ops Domain]]]]
- Domain-9 Platform Ops — Open Source Project Index
- Platform Ops Overview
- Cluster Lifecycle Management
- [[domain-07-platform-engineering/governance/03-capacity-planning-resource-assessment.md|03 capacity planning resource assessment]]
- Performance Benchmarking & Tuning
- Operations Metrics System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization & FinOps
- Security & Compliance Management

## Related

- [[README]]

- Platform Ops Overview
- Cluster Lifecycle Management
- Metrics Monitoring System
- Related Knowledge Domain: domain-06-observability
- Related Knowledge Domain: domain-15-specialized-tech
- Related Knowledge Domain: domain-10-troubleshooting-diagnostics
- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Graph Index]]

## See Also

- 04-performance-benchmarking-tuning
- 05-operations-metrics-system
- 07-gitops-configuration-management
- 08-automation-toolchain


<!-- risk-assessed -->