---
title: 07 - Custom Metrics Adapter and HPA Extension
description: This document provides an in-depth analysis of Kubernetes custom metrics adapter system from a production operations expert perspective, covering Prometheus Adapter, external metrics integration, HPA advanced configuration, metrics pipeline optimization, and other core topics. Combined with large-scale cluster practical experience, it provides comprehensive guidance for enterprises to build flexible and efficient auto-scaling systems.
summary: This document provides an in-depth analysis of Kubernetes custom metrics adapter system from a production operations expert perspective, covering Prometheus Adapter, external metrics integration, HPA advanced configuration, metrics pipeline optimization, and other core topics. Combined with large-scale cluster practical experience, it provides comprehensive guidance for enterprises to build flexible and efficient auto-scaling systems.
category: observability
tags:
- k8s
- observability
- monitoring
- logging
- tracing
- kubelet
- prometheus
- helm
- hpa
- job
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- DevOps Engineers
- Monitoring Engineers
estimated_read_time: 5min
intent_queries:
- What is Custom Metrics Adapter and HPA Extension
- How to configure Custom Metrics Adapter and HPA Extension
- Kubernetes observability best practices
trigger_keywords:
- custom metrics adapter
- HPA extension
- Custom
- Metrics
- Adapter
- HPA
- Extension
- observability
prerequisites:
- kubectl-basics
- observability-basics
- helm-basics
- prometheus-basics
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
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/02-metrics/11-custom-metrics-adapter.md
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
  label: 'Cheat sheet: promql'
---

> **Production Environment Safety Notice**
>
> This document contains operations commands that can be executed directly. Before executing, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have verified it in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state, but usually can be rolled back), 🟢 Low risk/read-only (information collection, no side effects).




# 07 - Custom Metrics Adapter and HPA Extension

> **Supported versions**: v1.25 - v1.32 | **Last updated**: 2026-01 | **Reference**: [[entities/kubernetes.md|kubernetes]].io/docs/tasks/run-application/horizontal-pod-autoscale](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

This document provides an in-depth analysis of Kubernetes custom metrics adapter system from a production operations expert perspective, covering [[Prometheus|Prometheus]] Adapter, external metrics integration, HPA advanced configuration, metrics pipeline optimization, and other core topics. Combined with large-scale cluster practical experience, it provides comprehensive guidance for enterprises to build flexible and efficient auto-scaling systems.

| API | Path | Provider | Purpose | Version Support |
|-----|------|---------|---------|---------|
| **Resource Metrics** | metrics.k8s.io/v1beta1 | Metrics Server | CPU/Memory | Stable |
| **Custom Metrics** | custom.metrics.k8s.io/v1beta1 | Prometheus Adapter, etc. | Custom Pod metrics | Stable |
| **External Metrics** | external.metrics.k8s.io/v1beta1 | External adapters | External system metrics | Stable |

<!-- chunk: Metrics Server -->
## Metrics Server

```yaml
# Metrics Server deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: metrics-server
  namespace: kube-system
spec:
  selector:
    matchLabels:
      k8s-app: metrics-server
  template:
    metadata:
      labels:
        k8s-app: metrics-server
    spec:
      containers:
      - name: metrics-server
        image: registry.k8s.io/metrics-server/metrics-server:v0.7.0
        args:
        - --cert-dir=/tmp
        - --secure-port=10250
        - --kubelet-preferred-address-types=InternalIP,ExternalIP,Hostname
        - --kubelet-use-node-status-port
        - --metric-resolution=15s
        # May be required in test environments
        # - --kubelet-insecure-tls
        resources:
          requests:
            cpu: 100m
            memory: 200Mi
```

<!-- chunk: Prometheus Adapter -->
## Prometheus Adapter

```yaml
# Prometheus Adapter Helm installation
# helm install prometheus-adapter prometheus-community/prometheus-adapter -f values.yaml

# values.yaml example
prometheus:
  url: http://prometheus.monitoring.svc
  port: 9090

rules:
  default: true
  custom:
  # Custom metrics rules
  - seriesQuery: 'http_requests_total{namespace!="",pod!=""}'
    resources:
      overrides:
        namespace: {resource: "namespace"}
        pod: {resource: "pod"}
    name:
      matches: "^(.*)_total$"
      as: "${1}_per_second"
    metricsQuery: 'sum(rate(<<.Series>>{<<.LabelMatchers>>}[2m])) by (<<.GroupBy>>)'
  
  # External metrics rules
  external:
  - seriesQuery: 'queue_messages_total{queue_name!=""}'
    resources:
      template: <<.Resource>>
    name:
      matches: "^(.*)_total$"
      as: "${1}"
    metricsQuery: 'sum(<<.Series>>{<<.LabelMatchers>>}) by (<<.GroupBy>>)'
```

<!-- chunk: Custom Metrics HPA -->
## Custom Metrics HPA

```yaml
# HPA based on custom metrics
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-hpa-custom
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app
  minReplicas: 2
  maxReplicas: 20
  metrics:
  # Resource metrics
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  # Custom Pod metrics
  - type: Pods
    pods:
      metric:
        name: http_requests_per_second
      target:
        type: AverageValue
        averageValue: "1000"
  # Custom object metrics
  - type: Object
    object:
      metric:
        name: requests_per_second
      describedObject:
        apiVersion: networking.k8s.io/v1
        kind: Ingress
        name: main-ingress
      target:
        type: Value
        value: "10000"
  # External metrics
  - type: External
    external:
      metric:
        name: queue_messages
        selector:
          matchLabels:
            queue: main-queue
      target:
        type: AverageValue
        averageValue: "30"
```

<!-- chunk: [[KEDA|KEDA]](Kubernetes Event-driven Autoscaling) -->
## KEDA (Kubernetes Event-driven Autoscaling)

```yaml
# KEDA installation
# kubectl apply -f https://github.com/kedacore/keda/releases/download/v2.12.0/keda-2.12.0.yaml

# ScaledObject example
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: rabbitmq-scaledobject
spec:
  scaleTargetRef:
    name: consumer-deployment
  pollingInterval: 30
  cooldownPeriod: 300
  minReplicaCount: 1
  maxReplicaCount: 100
  triggers:
  - type: rabbitmq
    metadata:
      host: amqp://user:pass@rabbitmq:5672/
      queueName: tasks
      queueLength: "50"
---
# Prometheus trigger
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: prometheus-scaledobject
spec:
  scaleTargetRef:
    name: app-deployment
  triggers:
  - type: prometheus
    metadata:
      serverAddress: http://prometheus:9090
      metricName: http_requests_total
      threshold: "100"
      query: sum(rate(http_requests_total{deployment="app"}[2m]))
---
# Cron trigger (scheduled scaling)
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: cron-scaledobject
spec:
  scaleTargetRef:
    name: app-deployment
  triggers:
  - type: cron
    metadata:
      timezone: Asia/Shanghai
      start: 0 8 * * 1-5   # Weekday 8:00 AM
      end: 0 20 * * 1-5    # Weekday 8:00 PM
      desiredReplicas: "10"
```

<!-- chunk: Application exposes custom metrics -->
## Application Exposes Custom Metrics

```go
// Go application exposing Prometheus metrics example
package main

import (
    "net/http"
    "github.com/prometheus/client_golang/prometheus"
    "github.com/prometheus/client_golang/prometheus/promhttp"
)

var (
    httpRequestsTotal = prometheus.NewCounterVec(
        prometheus.CounterOpts{
            Name: "http_requests_total",
            Help: "Total number of HTTP requests",
        },
        []string{"method", "path", "status"},
    )
    httpRequestDuration = prometheus.NewHistogramVec(
        prometheus.HistogramOpts{
            Name:    "http_request_duration_seconds",
            Help:    "HTTP request duration in seconds",
            Buckets: prometheus.DefBuckets,
        },
        []string{"method", "path"},
    )
)

func init() {
    prometheus.MustRegister(httpRequestsTotal)
    prometheus.MustRegister(httpRequestDuration)
}

func main() {
    http.Handle("/metrics", promhttp.Handler())
    http.ListenAndServe(":8080", nil)
}
```

```yaml
# Pod configuration for Prometheus scraping
apiVersion: v1
kind: Pod
metadata:
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "8080"
    prometheus.io/path: "/metrics"
spec:
  containers:
  - name: app
    image: app:latest
    ports:
    - containerPort: 8080
      name: metrics
```

<!-- chunk: ServiceMonitor(Prometheus Operator) -->
## ServiceMonitor (Prometheus Operator)

```yaml
# ServiceMonitor definition
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: app-monitor
  labels:
    release: prometheus
spec:
  selector:
    matchLabels:
      app: myapp
  endpoints:
  - port: metrics
    interval: 30s
    path: /metrics
  namespaceSelector:
    matchNames:
    - production
---
# PodMonitor definition
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
  name: app-pod-monitor
spec:
  selector:
    matchLabels:
      app: myapp
  podMetricsEndpoints:
  - port: metrics
    interval: 30s
```

<!-- chunk: Metrics aggregation rules -->
## Metrics Aggregation Rules

```yaml
# PrometheusRule definition
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: app-rules
spec:
  groups:
  - name: app.rules
    interval: 30s
    rules:
    # Recording rules (pre-calculation)
    - record: job:http_requests:rate5m
      expr: sum(rate(http_requests_total[5m])) by (job)
    # Alert rules
    - alert: HighErrorRate
      expr: |
        sum(rate(http_requests_total{status=~"5.."}[5m])) by (job)
        /
        sum(rate(http_requests_total[5m])) by (job) > 0.05
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "High error rate detected"
        description: "Error rate is {{ $value | humanizePercentage }}"
```

<!-- chunk: Validate custom metrics -->
## Validate Custom Metrics

``` bash
# 🟢 Low risk: read-only/information collection, usually no side effects
# Validate Custom Metrics API
kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1" | jq
kubectl get --raw "/apis/custom.metrics.k8s.io/v1beta1/namespaces/default/pods/*/http_requests_per_second" | jq

# Validate External Metrics API
kubectl get --raw "/apis/external.metrics.k8s.io/v1beta1" | jq
kubectl get --raw "/apis/external.metrics.k8s.io/v1beta1/namespaces/default/queue_messages" | jq

# Check HPA status
kubectl describe hpa <name>
kubectl get hpa -w
```
<!-- chunk: ACK Monitoring Extension -->
## ACK Monitoring Extension

| Feature | Product | Integration Method |
|---------|---------|---------|
| **Prometheus Hosting** | ARMS | Component installation |
| **Custom Metrics HPA** | ARMS Adapter | Auto configuration |
| **Business Monitoring** | ARMS Application Monitoring | Agent injection |
| **Log Metrics** | SLS | Log aggregation |

---

**Monitoring Extension Principle**: Expose business metrics, configure reasonable thresholds, and implement automatic scaling

---

**Table Footer Mark**: Kusheet Project, author Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian Related Documents -->
## Obsidian Related Documents

- [[domain-06-observability/MOC.md|domain-06-observability MOC]]
- [[domain-06-observability/README.md|Observability Domain]]
- [[domain-06-observability/00-open-source-projects-index.md|Domain-6 Observability — Open Source Projects Index]]
- Kubernetes Observability Architecture System
- Metrics Monitoring System Explained in Detail
- 03 - Logging Collection Architecture Explained (Logging Architecture)
- Distributed Tracing System
- 05 - Alert Management Strategy (Alerting Management)
- 06 - Monitoring and Alerting Practice and Best Practices (Monitoring Alerting Practice)
- 04 - Monitoring Dashboard Design and Best Practices (Monitoring Dashboards)
- 08 - Logging Audit and Compliance Management (Logging Auditing & Compliance)
- 05 - Events and Audit Logs Management (Events & Audit Logs)

## See Also

- 09-events-audit-logs
- 10-monitoring-metrics-prometheus
- 12-logging-auditing
- 13-cluster-health-check

- [[domain-06-observability/README.md|Back to index]]

## Related

- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Graph Index]]


<!-- risk-assessed -->
