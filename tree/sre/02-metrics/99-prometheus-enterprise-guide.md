---
title: Prometheus Enterprise-Grade Monitoring Deployment Guide
description: 'Prometheus Enterprise-Grade Monitoring Deployment Guide'
summary: 'helm repo add prometheus-community https://prometheus-community.github.io/helm-charts'
category: enterprise-monitoring-alerting
tags:
- k8s
- monitoring
- alerting
- prometheus
- grafana
- helm
- hpa
- statefulset
- daemonset
- job
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Monitoring Engineer
- Operations Engineer
estimated_read_time: 5min
intent_queries:
- What is Prometheus Enterprise-Grade Monitoring Deployment Guide
- How to deploy Prometheus Enterprise-Grade Monitoring Guide
- Kubernetes 20 enterprise monitoring alerting best practices
trigger_keywords:
- Prometheus
- Enterprise-Grade Monitoring Deployment Guide
- enterprise
- monitoring
- alerting
prerequisites:
- kubectl-basics
- observability-basics
- helm-basics
- prometheus-basics
- monitoring-basics
- logging-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: Dillan Teagle
  role: contributor
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/02-metrics/99-prometheus-enterprise-guide.md
cross_refs:
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/promql.md
  label: 'Cheat Sheet: PromQL'
---

> **Production Environment Security Warning**
>
> This document contains directly executable operations commands. Before executing, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether the commands have been verified in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state, but usually recoverable), 🟢 Low risk/read-only (information collection, no side effects).




# [[Prometheus|Prometheus]] Enterprise-Grade Monitoring Deployment Guide

> **Applicable Version**: Prometheus v3.3.0 / kube-state-metrics v2.15 / Alertmanager v0.28  
> **Last Updated**: 2026-04-24  
> **Difficulty**: Intermediate → Advanced

---

## 📋 Table of Contents

- [1. Architecture Design](#1-architecture-design)
- [2. [[Helm|Helm]] Deployment](#2-helm-deployment)
- [3. High Availability Configuration](#3-high-availability-configuration)
- [4. Alert Rules Best Practices](#4-alert-rules-best-practices)
- [5. Service Discovery Configuration](#5-service-discovery-configuration)
- [6. Performance Tuning](#6-performance-tuning)
- [7. Common Troubleshooting](#7-common-troubleshooting)

---

## 1. Architecture Design

### 1.1 Single Instance Architecture (< 100 nodes)

```
┌────────────────────────────────────────┐
│           K8s Cluster                  │
│  ┌─────────────┐  ┌─────────────────┐  │
│  │ Prometheus  │  │ Alertmanager    │  │
│  │ (StatefulSet│  │ (StatefulSet x2)│  │
│  │  + PVC)     │  │                 │  │
│  └──────┬──────┘  └─────────────────┘  │
│         │ scrape                        │
│  ┌──────┴──────┐  ┌─────────────────┐  │
│  │kube-state   │  │node_exporter    │  │
│  │metrics      │  │(DaemonSet)      │  │
│  └─────────────┘  └─────────────────┘  │
└────────────────────────────────────────┘
```

### 1.2 Federated Architecture (> 100 nodes / multi-cluster)

```
┌──────────────┐      ┌──────────────┐      ┌──────────────┐
│  Prometheus  │      │  Prometheus  │      │  Prometheus  │
│  Cluster A   │◄────►│  Cluster B   │◄────►│  Cluster C   │
└──────┬───────┘      └──────┬───────┘      └──────┬───────┘
       │ scrape (federation) │ scrape            │ scrape
       └─────────────────────┴───────────────────┘
                           │
                    ┌──────┴───────┐
                    │  Thanos      │
                    │  Query       │
                    │  + Store     │
                    └──────┬───────┘
                           │
                    ┌──────┴───────┐
                    │   Grafana    │
                    └──────────────┘
```

---

## 2. Helm Deployment

### 2.1 kube-prometheus-stack (Recommended)

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, it is recommended to use --dry-run or diff to confirm first
> - `helm upgrade/install`: Deploy/upgrade release

``` bash
# 🟡 Medium Risk: Will modify cluster/resource state, please confirm target, scope, and authorization before execution
# Add repository
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

# Prepare custom values
# values-production.yaml
cat << 'EOF' > values-production.yaml
prometheus:
  prometheusSpec:
    retention: 30d
    retentionSize: "50GB"
    resources:
      requests:
        memory: "4Gi"
        cpu: "1000m"
      limits:
        memory: "8Gi"
        cpu: "2000m"
    storageSpec:
      volumeClaimTemplate:
        spec:
          storageClassName: standard
          accessModes: ["ReadWriteOnce"]
          resources:
            requests:
              storage: 100Gi
    additionalScrapeConfigs:
      # Custom job example
      - job_name: 'custom-app'
        kubernetes_sd_configs:
          - role: pod
            namespaces:
              names:
                - production
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

alertmanager:
  enabled: true
  config:
    global:
      smtp_smarthost: 'smtp.example.com:587'
      smtp_from: 'alert@example.com'
    route:
      receiver: 'default'
      group_by: ['alertname', 'namespace']
      group_wait: 30s
      group_interval: 5m
      repeat_interval: 12h
      routes:
      - match:
          severity: critical
        receiver: 'pagerduty-critical'
        continue: true
      - match:
          severity: warning
        receiver: 'slack-warning'
    receivers:
    - name: 'default'
      slack_configs:
      - api_url: 'https://hooks.slack.com/services/XXX'
        channel: '#alerts'
        title: '{% raw %}{{ .GroupLabels.alertname }}{% endraw %}'
        text: '{% raw %}{{ range .Alerts }}{{ .Annotations.summary }}\n{{ end }}{% endraw %}'
    - name: 'pagerduty-critical'
      pagerduty_configs:
      - routing_key: '<PAGERDUTY_KEY>'
    - name: 'slack-warning'
      slack_configs:
      - api_url: 'https://hooks.slack.com/services/YYY'
        channel: '#warnings'

grafana:
  enabled: true
  adminPassword: "changeme-strong-password"
  persistence:
    enabled: true
    size: 10Gi
  additionalDataSources:
    - name: Loki
      type: loki
      url: http://loki:3100
      access: proxy

kubeStateMetrics:
  enabled: true

nodeExporter:
  enabled: true
EOF

# Deploy
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  --values values-production.yaml \
  --version 69.8.0
```
---

## 3. High Availability Configuration

### 3.1 Prometheus HA (Thanos Sidecar Pattern)

```yaml
# Deploy Thanos Sidecar alongside each Prometheus Pod
prometheus:
  prometheusSpec:
    containers:
      - name: thanos-sidecar
        image: quay.io/thanos/thanos:v0.38.0
        args:
          - sidecar
          - --tsdb.path=/prometheus
          - --prometheus.url=http://localhost:9090
          - --objstore.config-file=/etc/thanos/objstore.yml
        volumeMounts:
          - name: thanos-objstore
            mountPath: /etc/thanos
          - name: prometheus-data
            mountPath: /prometheus
    volumes:
      - name: thanos-objstore
        secret:
          secretName: thanos-objstore
```

### 3.2 Alertmanager HA

```yaml
alertmanager:
  alertmanagerSpec:
    replicas: 3  # Gossip cluster auto-discovery
    podAntiAffinity: hard  # Distributed across different nodes
```

---

## 4. Alert Rules Best Practices

### 4.1 Core Kubernetes Alert Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: kubernetes-rules
  namespace: monitoring
spec:
  groups:
  - name: kubernetes-apps
    rules:
    # Pod crash loop
    - alert: KubePodCrashLooping
      expr: |
        rate(kube_pod_container_status_restarts_total[10m]) > 0
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "Pod {% raw %}{{ $labels.namespace }}/{{ $labels.pod }}{% endraw %} is in crash loop"
        description: "Container {% raw %}{{ $labels.container }}{% endraw %} has restarted more than 0 times in 10 minutes"

    # Pod not ready
    - alert: KubePodNotReady
      expr: |
        sum by (namespace, pod) (
          max by(namespace, pod) (
            kube_pod_status_phase{% raw %}{phase=~"Pending|Unknown"}{% endraw %}
          ) * on(namespace, pod) group_left(owner_kind) topk by(namespace, pod) (
            1, max by(namespace, pod, owner_kind) (kube_pod_owner{owner_kind!="Job"})
          )
        ) > 0
      for: 15m
      labels:
        severity: warning
      annotations:
        summary: "Pod not ready for more than 15 minutes"

    # Node memory pressure
    - alert: NodeMemoryPressure
      expr: |
        (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) < 0.1
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Node {% raw %}{{ $labels.instance }}{% endraw %} low on memory"

    # Node disk pressure
    - alert: NodeDiskPressure
      expr: |
        (node_filesystem_avail_bytes / node_filesystem_size_bytes) < 0.1
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Node {% raw %}{{ $labels.instance }}{% endraw %} running out of disk space"

    # HPA reached max replicas
    - alert: HpaMaxedOut
      expr: |
        kube_horizontalpodautoscaler_status_desired_replicas >= 
        kube_horizontalpodautoscaler_spec_max_replicas
      for: 15m
      labels:
        severity: warning
      annotations:
        summary: "HPA {% raw %}{{ $labels.horizontalpodautoscaler }}{% endraw %} has reached max replicas"
```

### 4.2 Alert Severity Tiering Strategy

| Level | Response Time | Notification Channel | Example |
|:---|:---|:---|:---|
| critical | Within 5 minutes | PagerDuty + Slack + Phone | Core service unavailable, data loss risk |
| warning | Within 30 minutes | Slack | High resource utilization, Pod restarts |
| info | Next business day | Email/Slack | Certificate expiring soon, version upgradeable |

---

## 5. Service Discovery Configuration

### 5.1 Pod Monitoring Annotation Standards

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  template:
    metadata:
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
        prometheus.io/path: "/metrics"
    spec:
      containers:
      - name: app
        ports:
        - containerPort: 8080
          name: metrics
```

### 5.2 ServiceMonitor (Prometheus Operator)

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: myapp-metrics
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: myapp
  namespaceSelector:
    matchNames:
      - production
  endpoints:
  - port: metrics
    interval: 30s
    path: /metrics
    honorLabels: true
```

---

## 6. Performance Tuning

### 6.1 Horizontal Scaling Parameters

```yaml
prometheus:
  prometheusSpec:
    # Scrape concurrency
    query:
      maxConcurrency: 20
    # Storage optimization
    tsdb:
      minBlockDuration: 2h
      maxBlockDuration: 2h
      retentionSize: "45GB"  # Slightly smaller than PVC capacity
    # Memory optimization
    enableAdminAPI: false
    walCompression: true
```

### 6.2 Remote Write

```yaml
prometheus:
  prometheusSpec:
    remoteWrite:
      - url: "http://thanos-receive:19291/api/v1/receive"
        queueConfig:
          maxSamplesPerSend: 1000
          maxShards: 200
        writeRelabelConfigs:
          - sourceLabels: [__name__]
            regex: 'go_.*'
            action: drop  # Filter high-cardinality metrics
```

---

## 7. Common Troubleshooting

| Issue | Cause | Solution |
|:---|:---|:---|
| Prometheus OOMKilled | Too many scrape targets / high-cardinality labels | Increase memory limits, add relabel filters, reduce targets |
| Disk growing rapidly | Retention too long / high cardinality | Shorten retention, enable compression, filter unused metrics |
| Query timeout | Complex queries / large data volume | Increase query.timeout, use recording rules |
| Target showing down | Network unreachable / incorrect metrics path | Check [[Service|Service]]/Pod annotations, network policies |
| Alertmanager not triggering | Route rules not matching / inhibit | Check alertmanager config, routing tree |

---

## References

- [kube-prometheus-stack Helm Chart](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
- [Prometheus Configuration Documentation](https://prometheus.io/docs/prometheus/latest/configuration/configuration/)
- [Alertmanager Configuration](https://prometheus.io/docs/alerting/latest/configuration/)
- [Thanos Deployment Guide](https://thanos.io/tip/thanos/getting-started.md/)

---

## Obsidian Related Documents

- observability/MOC.md|domain-20-enterprise-monitoring-alerting MOC]]
- [[domain-06-observability/README.md|Domain 06: Enterprise Monitoring and Alerting]]
- [[domain-06-observability/00-open-source-projects-index.md|Domain-20 Enterprise Monitoring and Alerting — Open Source Projects Index]]
- Prometheus Enterprise-Grade Monitoring System Deep Practice
- Grafana Enterprise Observability Platform Deep Practice
- OpenTelemetry Distributed Tracing and Observability Deep Practice
- Thanos Enterprise Metrics Federation and Long-term Storage
- Datadog Enterprise APM Deep Practice
- Datadog Enterprise Monitoring Platform Deep Practice
- Elastic Stack Enterprise Log Analysis Deep Practice
- Elastic Stack Enterprise Observability Platform Deep Practice
- Zabbix Enterprise Monitoring Platform Deep Practice

## See Also

- 08-new-relic-enterprise-apm
- 99-distributed-tracing-guide
- 01-prometheus-enterprise-monitoring
- 02-grafana-enterprise-observability

- [[domain-06-observability/README.md|Back to index]]

## Related

- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Graph Index]]

```

<!-- risk-assessed -->
