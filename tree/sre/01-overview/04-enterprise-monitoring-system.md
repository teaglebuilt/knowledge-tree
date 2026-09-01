---
title: 04-Enterprise-Grade Monitoring System
description: '# 04-Enterprise-Grade Monitoring System'
summary: 'An enterprise-grade monitoring system is the core infrastructure that ensures stable operation of Kubernetes production environments. This document provides detailed guidance on complete monitoring architecture design, component selection, and best practices.'
category: production-operations
tags:
- k8s
- production
- operations
- best-practices
- prometheus
- grafana
- docker
- statefulset
- daemonset
- job
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- SRE
- Operations Engineer
- Platform Engineer
estimated_read_time: 5min
intent_queries:
- What is an enterprise-grade monitoring system
- How to implement an enterprise-grade monitoring system
- Kubernetes production operations best practices
trigger_keywords:
- enterprise monitoring
- production
- operations
prerequisites:
- kubectl-basics
- observability-basics
- prometheus-basics
- monitoring-basics
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
- type: fta
  path: ../domain-10-troubleshooting-diagnostics/topic-fta/list/monitoring-fta.md
  label: 'Fault Tree: monitoring'
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/01-overview/04-enterprise-monitoring-system.md
---

> **Production Environment Security Notice**
>
> This document contains directly executable operations commands. Before executing, please confirm: whether the current target cluster and namespace are correct; whether sufficient RBAC permissions are available; whether verification has been completed in a non-production environment. Command risk levels: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state but usually reversible), 🟢 Low Risk/Read-only (information collection with no side effects).




# 04-Enterprise-Grade Monitoring System

> **Scope**: [[Kubernetes|Kubernetes]] v1.25-v1.32 | **Maintenance Status**: 🔧 Continuously Updated | **Expert Level**: ⭐⭐⭐⭐⭐

<!-- chunk: 📋 Overview -->## 📋 Overview

An enterprise-grade monitoring system is the core infrastructure that ensures stable operation of Kubernetes production environments. This document provides detailed guidance on complete monitoring architecture design, component selection, and best practices.

<!-- chunk: 🏗️ Monitoring Architecture Design -->## 🏗️ Monitoring Architecture Design

## Three-Layer Monitoring Architecture

## 1. Infrastructure Layer Monitoring
```yaml
# Node Exporter DaemonSet Configuration
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: node-exporter
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: node-exporter
  template:
    metadata:
      labels:
        app: node-exporter
    spec:
      hostNetwork: true
      hostPID: true
      containers:
      - name: node-exporter
        image: quay.io/prometheus/node-exporter:v1.5.0
        args:
        - --web.listen-address=:9100
        - --path.procfs=/host/proc
        - --path.sysfs=/host/sys
        - --collector.filesystem.mount-points-exclude=^/(dev|proc|sys|var/lib/docker/.+)($|/)
        - --collector.filesystem.fs-types-exclude=^(autofs|binfmt_misc|cgroup|configfs|debugfs|devpts|devtmpfs|fusectl|hugetlbfs|mqueue|overlay|proc|procfs|pstore|rpc_pipefs|securityfs|sysfs|tracefs)$
        ports:
        - containerPort: 9100
        volumeMounts:
        - name: proc
          mountPath: /host/proc
          readOnly: true
        - name: sys
          mountPath: /host/sys
          readOnly: true
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 200m
            memory: 256Mi
      volumes:
      - name: proc
        hostPath:
          path: /proc
      - name: sys
        hostPath:
          path: /sys
```

## 2. Kubernetes Component Monitoring
```yaml
# kube-state-metrics Configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: kube-state-metrics
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: kube-state-metrics
  replicas: 2
  template:
    metadata:
      labels:
        app: kube-state-metrics
    spec:
      containers:
      - name: kube-state-metrics
        image: registry.k8s.io/kube-state-metrics/kube-state-metrics:v2.7.0
        ports:
        - containerPort: 8080
          name: http-metrics
        - containerPort: 8081
          name: telemetry
        livenessProbe:
          httpGet:
            path: /healthz
            port: 8080
          initialDelaySeconds: 5
          timeoutSeconds: 5
        readinessProbe:
          httpGet:
            path: /
            port: 8081
          initialDelaySeconds: 5
          timeoutSeconds: 5
---
apiVersion: v1
kind: Service
metadata:
  name: kube-state-metrics
  namespace: monitoring
  labels:
    app: kube-state-metrics
spec:
  ports:
  - name: http-metrics
    port: 8080
    targetPort: http-metrics
  - name: telemetry
    port: 8081
    targetPort: telemetry
  selector:
    app: kube-state-metrics
```

## 3. Application Layer Monitoring
```yaml
# Application Monitoring Sidecar Pattern
apiVersion: apps/v1
kind: Deployment
metadata:
  name: monitored-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
        prometheus.io/path: "/metrics"
    spec:
      containers:
      - name: app
        image: myapp:latest
        ports:
        - containerPort: 8080
        env:
        - name: METRICS_ENABLED
          value: "true"
```

<!-- chunk: 📊 Prometheus Monitoring Stack -->## 📊 Prometheus Monitoring Stack

## Core Component Configuration

## 1. Prometheus Server Configuration
```yaml
# Prometheus Configuration File
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    cluster: production
    region: us-west-2

rule_files:
  - "rules/alerts.yml"
  - "rules/recording.yml"

alerting:
  alertmanagers:
  - static_configs:
    - targets:
      - alertmanager.monitoring.svc:9093

scrape_configs:
  # Kubernetes Node Monitoring
  - job_name: 'kubernetes-nodes'
    kubernetes_sd_configs:
    - role: node
    relabel_configs:
    - source_labels: [__address__]
      regex: '(.*):10250'
      target_label: __address__
      replacement: '${1}:9100'
    - target_label: __scheme__
      replacement: http

  # Kubernetes Pods Monitoring
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
    - role: pod
    relabel_configs:
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
      action: keep
      regex: true
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
      action: replace
      target_label: __metrics_path__
      regex: (.+)
    - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
      action: replace
      regex: ([^:]+)(?::\d+)?;(\d+)
      replacement: $1:$2
      target_label: __address__

  # kube-state-metrics
  - job_name: 'kube-state-metrics'
    static_configs:
    - targets: ['kube-state-metrics:8080']
```

## 2. Long-Term Storage Configuration
```yaml
# Thanos Sidecar Configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prometheus-thanos
  namespace: monitoring
spec:
  replicas: 1
  selector:
    matchLabels:
      app: prometheus-thanos
  template:
    metadata:
      labels:
        app: prometheus-thanos
    spec:
      containers:
      - name: thanos-sidecar
        image: quay.io/thanos/thanos:v0.37.0
        args:
        - sidecar
        - --http-address=0.0.0.0:10902
        - --grpc-address=0.0.0.0:10901
        - --prometheus.url=http://localhost:9090
        - --objstore.config-file=/etc/thanos/objstore.yml
        - --tsdb.path=/prometheus
        ports:
        - name: http
          containerPort: 10902
        - name: grpc
          containerPort: 10901
        volumeMounts:
        - name: prometheus-storage
          mountPath: /prometheus
        - name: thanos-config
          mountPath: /etc/thanos
      volumes:
      - name: prometheus-storage
        persistentVolumeClaim:
          claimName: prometheus-pvc
      - name: thanos-config
        configMap:
          name: thanos-objstore-config
```

## Alert Rules Configuration

## 1. Core Alert Rules
```yaml
# Core Alert Rules
groups:
- name: kubernetes.rules
  rules:
  # Node-related alerts
  - alert: NodeDown
    expr: up{job="kubernetes-nodes"} == 0
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "Node {{ $labels.instance }} is down"
      description: "Node has been down for more than 5 minutes"

  - alert: NodeCPUHigh
    expr: 100 - (avg by(instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 85
    for: 10m
    labels:
      severity: warning
    annotations:
      summary: "High CPU usage on node {{ $labels.instance }}"
      description: "CPU usage is above 85% for more than 10 minutes"

  # Pod-related alerts
  - alert: PodCrashLooping
    expr: rate(kube_pod_container_status_restarts_total[15m]) * 60 * 5 > 0
    for: 15m
    labels:
      severity: critical
    annotations:
      summary: "Pod {{ $labels.pod }} is crash looping"
      description: "Pod is restarting more than 5 times per hour"

  - alert: PodPending
    expr: kube_pod_status_phase{phase="Pending"} == 1
    for: 10m
    labels:
      severity: warning
    annotations:
      summary: "Pod {{ $labels.pod }} is pending"
      description: "Pod has been in Pending state for more than 10 minutes"
```

<!-- chunk: 🎨 Grafana Visualization -->## 🎨 Grafana Visualization

## Core Dashboard Configuration

## 1. Cluster Overview Dashboard
```json
{
  "dashboard": {
    "title": "Kubernetes Cluster Overview",
    "panels": [
      {
        "title": "Cluster Health Status",
        "type": "stat",
        "datasource": "Prometheus",
        "targets": [
          {
            "expr": "sum(up{job=\"kubernetes-nodes\"})",
            "legendFormat": "Nodes Up"
          },
          {
            "expr": "count(kube_pod_info)",
            "legendFormat": "Total Pods"
          },
          {
            "expr": "sum(kube_deployment_status_replicas_available)",
            "legendFormat": "Available Deployments"
          }
        ]
      },
      {
        "title": "Resource Utilization",
        "type": "graph",
        "datasource": "Prometheus",
        "targets": [
          {
            "expr": "100 * sum(kube_pod_container_resource_requests{resource=\"cpu\"}) / sum(kube_node_status_allocatable{resource=\"cpu\"})",
            "legendFormat": "CPU Requested %"
          },
          {
            "expr": "100 * sum(kube_pod_container_resource_limits{resource=\"cpu\"}) / sum(kube_node_status_allocatable{resource=\"cpu\"})",
            "legendFormat": "CPU Limits %"
          }
        ]
      }
    ]
  }
}
```

## 2. Application Performance Dashboard
```json
{
  "dashboard": {
    "title": "Application Performance",
    "panels": [
      {
        "title": "HTTP Request Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(http_requests_total[5m])) by (app)",
            "legendFormat": "{{app}}"
          }
        ]
      },
      {
        "title": "Error Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(http_requests_total{status=~\"5..\"}[5m])) by (app) / sum(rate(http_requests_total[5m])) by (app) * 100",
            "legendFormat": "{{app}} Error %"
          }
        ]
      },
      {
        "title": "Latency Distribution",
        "type": "heatmap",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))",
            "legendFormat": "p95 Latency"
          }
        ]
      }
    ]
  }
}
```

<!-- chunk: 🚨 Alertmanager Alert Management -->## 🚨 Alertmanager Alert Management

## Alert Routing Configuration

## 1. Multi-Level Alert Routing
```yaml
# Alertmanager Configuration
global:
  smtp_smarthost: 'smtp.example.com:587'
  smtp_from: 'alerts@example.com'
  smtp_auth_username: 'alerts'
  smtp_auth_password: 'password'

route:
  group_by: ['alertname', 'cluster']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 3h
  receiver: 'default-receiver'
  
  routes:
  - matchers:
    - severity="critical"
    receiver: pagerduty
    group_wait: 10s
    repeat_interval: 1h
  - matchers:
    - severity="warning"
    receiver: slack-warning
    group_wait: 1m
  - matchers:
    - team="sre"
    receiver: sre-team
  - matchers:
    - service="database"
    receiver: db-team
receivers:
- name: 'default-receiver'
  email_configs:
  - to: 'team@example.com'
    send_resolved: true

- name: 'pagerduty'
  pagerduty_configs:
  - routing_key: 'YOUR_PAGERDUTY_KEY'
    send_resolved: true

- name: 'slack-warning'
  slack_configs:
  - api_url: 'https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK'
    channel: '#alerts-warning'
    send_resolved: true
    title: '{{ template "slack.warning.title" . }}'
    text: '{{ template "slack.warning.text" . }}'
```

## 2. Alert Suppression Rules
```yaml
# Alert Suppression Configuration
inhibit_rules:
- source_matchers:
  - alertname="NodeDown"
  - target_match=""
  - alertname="ServiceDown"
  - equal="['instance']"
- source_matchers:
  - alertname="ClusterDown"
  - target_match_re=""
  - alertname=".*"
  - equal="['cluster']"
```

<!-- chunk: 📈 Performance Optimization -->## 📈 Performance Optimization

## Monitoring System Tuning

## 1. Prometheus Performance Optimization
```yaml
# Prometheus Storage Optimization Configuration
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: prometheus
spec:
  template:
    spec:
      containers:
      - name: prometheus
        image: prom/prometheus:v3.2.1
        args:
        - --storage.tsdb.retention.time=30d
        - --storage.tsdb.retention.size=50GB
        - --storage.tsdb.wal-compression
        - --web.enable-lifecycle
        - --web.enable-admin-api
        - --query.max-concurrency=20
        - --query.timeout=2m
        resources:
          requests:
            cpu: 2
            memory: 8Gi
          limits:
            cpu: 4
            memory: 16Gi
```

## 2. Query Optimization Strategies
```yaml
# Recording Rules Optimization
groups:
- name: recording.rules
  rules:
  # Pre-calculate high-frequency queries
  - record: job:node_cpu_utilization:avg5m
    expr: avg by(job) (rate(node_cpu_seconds_total{mode!="idle"}[5m]))
    
  - record: cluster:memory_utilization:ratio
    expr: sum(node_memory_MemTotal_bytes - node_memory_MemAvailable_bytes) / sum(node_memory_MemTotal_bytes)
    
  # Aggregation and downsampling
  - record: instance:network_bytes:rate1m
    expr: rate(node_network_receive_bytes_total[1m]) + rate(node_network_transmit_bytes_total[1m])
```

<!-- chunk: 🔧 Implementation Checklist -->## 🔧 Implementation Checklist

## Monitoring System Construction
- [ ] Design a complete three-layer monitoring architecture
- [ ] Deploy core monitoring components (Prometheus, Grafana, Alertmanager)
- [ ] Configure infrastructure layer monitoring (Node Exporter, kube-state-metrics)
- [ ] Implement application layer monitoring integration
- [ ] Establish a comprehensive alert rule system
- [ ] Configure multi-channel alert notifications

## Performance and Reliability
- [ ] Optimize Prometheus storage and query performance
- [ ] Implement long-term monitoring data storage solution
- [ ] Configure high-availability deployment for monitoring system
- [ ] Establish monitoring data backup and recovery mechanisms
- [ ] Implement monitoring system capacity planning
- [ ] Regularly review and optimize alert rules

## Operations and Maintenance
- [ ] Establish standardized dashboard templates for monitoring
- [ ] Implement monitoring data quality monitoring
- [ ] Establish alert response and handling procedures
- [ ] Perform regular monitoring system health checks
- [ ] Maintain monitoring documentation and operation manuals
- [ ] Continuously improve monitoring coverage

---

*This document provides comprehensive technical guidance and implementation framework for enterprise-grade Kubernetes monitoring systems*

---

<!-- chunk: Obsidian Related Documents -->## Obsidian Related Documents

- domain-11-production-operations KUDIG Database - Global MOC
- [[domain-11-production-operations/README.md|Domain 11: Production Operations Best Practices]]
- Domain-18 Production Operations - Open Source Project Index
- [[domain-01-cluster-fundamentals/01-production-architecture-design-principles.md|01-Production Architecture Design Principles]]
- 02-Multi-Cloud Hybrid Deployment Strategy
- 03-Edge Computing Production Deployment
- 05-Logging Collection Analysis Platform
- 06-APM Application Performance Monitoring
- 07-Zero-Trust Security Architecture
- 08-CIS Benchmark Compliance Checking
- 09-Software Bill of Materials
- 10-GitOps Pipeline Practices

## See Also

- 02-multi-cloud-hybrid-deployment-strategy
- 03-edge-computing-production-deployment
- 05-logging-collection-analysis-platform
- 06-apm-application-performance-monitoring

- [[domain-06-observability/README.md|Back to index]]

## Related

- [[domain-19-landscape-references/topic-index/etcd-index.md|etcd Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/nginx-ingress-index.md|nginx-ingress-controller Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/higress-index.md|Higress Knowledge Graph Index]]


<!-- risk-assessed -->
