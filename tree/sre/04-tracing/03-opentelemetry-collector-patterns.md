---
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/04-tracing/03-opentelemetry-collector-patterns.md
title: OpenTelemetry Collector Configuration Patterns
description: 'OTel Collector configuration patterns: Pipeline design (receiver→processor→exporter), batch processors, sampling processors, multi-tenant configuration, K8s auto-injection, performance tuning'
summary: 'OTel Collector Pipeline, processor configuration, multi-tenancy and K8s auto-injection'
category: observability
tags:
- opentelemetry
- otel-collector
- pipeline
- sampling
- auto-instrumentation
tier: supporting
created: '2026-07-02'
last_updated: 2026-07
difficulty: advanced
reading_level: advanced
audience:
- SRE
- Security Engineer
- Platform Engineer
estimated_read_time: 15min
intent_queries:
- What are OpenTelemetry Collector configuration patterns
- How to configure OTel Collector Pipeline
trigger_keywords:
- OpenTelemetry Collector
- OTel Collector
- Pipeline
- receiver
- processor
- exporter
prerequisites:
- kubectl-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: Dillan Teagle
  role: contributor
---

> **Production environment security notice**
>
> This document contains directly executable operations commands. Before executing, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have verified in a non-production environment first. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state, but usually reversible), 🟢 Low risk/read-only (information gathering, no side effects).


# OpenTelemetry Collector Configuration Patterns

## Overview

OpenTelemetry Collector is a vendor-neutral telemetry data collection agent that supports three signal types: Traces, Metrics, and Logs. This document covers production-grade configuration patterns including Pipeline design, processor configuration, multi-tenant solutions, and K8s auto-injection.

## 1. Pipeline Architecture

### 1.1 Basic Pipeline Pattern

```
┌──────────────────────────────────────────────────────────┐
│                  OTel Collector                           │
│                                                          │
│  Receivers         Processors         Exporters          │
│  ┌──────┐         ┌──────────┐       ┌──────────┐       │
│  │ OTLP │────────→│  batch   │──────→│ OTLP     │       │
│  └──────┘         │  memory  │       │ (Tempo)  │       │
│  ┌──────┐         │  limiter │       └──────────┘       │
│  │Jaeger│────────→│  filter  │       ┌──────────┐       │
│  └──────┘         │  k8sattr │──────→│Prometheus│       │
│  ┌──────┐         │  span    │       │ (Mimir)  │       │
│  │Prom  │────────→│  metrics │       └──────────┘       │
│  └──────┘         └──────────┘       ┌──────────┐       │
│  ┌──────┐                            │ Loki     │       │
│  │Fluent│───────────────────────────→│          │       │
│  └──────┘                            └──────────┘       │
└──────────────────────────────────────────────────────────┘
```

### 1.2 Multi-Pipeline Pattern

```yaml
# otel-collector-config.yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

  jaeger:
    protocols:
      thrift_compact:
        endpoint: 0.0.0.0:6831
      grpc:
        endpoint: 0.0.0.0:14250

  prometheus:
    config:
      scrape_configs:
      - job_name: 'kubernetes-pods'
        kubernetes_sd_configs:
        - role: pod
        relabel_configs:
        - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
          action: keep
          regex: true

  filelog:
    include: [/var/log/containers/*.log]
    exclude: [/var/log/containers/*_kube-system_*.log]
    operators:
    - type: container
      id: container-parser

processors:
  batch:
    # Timeout for sending batches
    timeout: 5s
    # Minimum batch size
    send_batch_size: 1024
    # Maximum batch size
    send_batch_max_size: 2048

  memory_limiter:
    # Check interval
    check_interval: 1s
    # Memory limit (MB)
    limit_mib: 512
    # Memory burst limit
    spike_limit_mib: 128

  k8sattributes:
    auth_type: "serviceAccount"
    passthrough: false
    extract:
      metadata:
      - k8s.namespace.name
      - k8s.deployment.name
      - k8s.pod.name
      - k8s.pod.uid
      - k8s.node.name
      labels:
      - tag_name: app
        key: app.kubernetes.io/name
        from: pod
    pod_association:
    - sources:
      - from: resource_attribute
        name: k8s.pod.ip

  filter/traces:
    error_mode: ignore
    traces:
      span:
        - 'attributes["http.target"] == "/health"'
        - 'attributes["http.target"] == "/metrics"'

  attributes:
    actions:
    - key: environment
      value: production
      action: upsert
    - key: service.version
      from_attribute: app.kubernetes.io/version
      action: insert

exporters:
  otlp/tempo:
    endpoint: tempo-distributor.observability.svc:4317
    tls:
      insecure: true
    retry_on_failure:
      enabled: true
      initial_interval: 5s
      max_interval: 30s
      max_elapsed_time: 300s

  prometheusremotewrite/mimir:
    endpoint: http://mimir-distributor.observability.svc:8080/api/v1/push

  loki:
    endpoint: http://loki-gateway.observability.svc:3100/loki/api/v1/push

extensions:
  health_check:
    endpoint: 0.0.0.0:13133
  pprof:
    endpoint: 0.0.0.0:1888
  zpages:
    endpoint: 0.0.0.0:55679

service:
  extensions: [health_check, pprof, zpages]
  pipelines:
    traces:
      receivers: [otlp, jaeger]
      processors: [memory_limiter, k8sattributes, filter/traces, attributes, batch]
      exporters: [otlp/tempo]

    metrics:
      receivers: [otlp, prometheus]
      processors: [memory_limiter, k8sattributes, batch]
      exporters: [prometheusremotewrite/mimir]

    logs:
      receivers: [otlp, filelog]
      processors: [memory_limiter, k8sattributes, batch]
      exporters: [loki]
```

## 2. Processor Details

### 2.1 Batch Processor

```yaml
processors:
  batch:
    # Send timeout duration
    timeout: 5s
    # Minimum batch size
    send_batch_size: 1024
    # Maximum batch size
    send_batch_max_size: 2048
    # Number of concurrent sends
    metadata_cardinality_limit: 1000
```

### 2.2 Memory Limiter Processor

```yaml
processors:
  memory_limiter:
    # Check interval
    check_interval: 1s
    # Memory limit (MB)
    limit_mib: 512
    # Memory burst limit
    spike_limit_mib: 128
    # Memory limit percentage (relative to system memory)
    limit_percentage: 80
    spike_limit_percentage: 20
```

### 2.3 Tail Sampling Processor

```yaml
processors:
  tail_sampling:
    decision_wait: 10s
    num_traces: 100000
    expected_new_traces_per_sec: 1000
    policies:
    # Error sampling (100%)
    - name: errors
      type: status_code
      status_code:
        status_codes: [ERROR]

    # Slow request sampling (100%)
    - name: slow-traces
      type: latency
      latency:
        threshold_ms: 5000

    # Sampling by Service
    - name: payment-service
      type: string_attribute
      string_attribute:
        key: service.name
        values: [payment-service]
      type: probabilistic
      probabilistic:
        sampling_percentage: 50

    # Default sampling rate
    - name: default
      type: probabilistic
      probabilistic:
        sampling_percentage: 10
```

### 2.4 Span Metrics Processor

```yaml
processors:
  spanmetrics:
    metrics_exporter: prometheusremotewrite
    latency_histogram_buckets: [1ms, 5ms, 10ms, 25ms, 50ms, 100ms, 250ms, 500ms, 1s, 5s]
    dimensions:
    - name: http.method
    - name: http.status_code
    - name: service.name
    - name: service.namespace
    aggregation_temporality: "AGGREGATION_TEMPORALITY_CUMULATIVE"
    enable_open_census_bridge: true
```

## 3. Multi-Tenant Configuration

### 3.1 Header-based Multi-Tenant

```yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  routing:
    attribute_source: context
    from_attribute: X-Tenant-ID
    default_tenant: default
    table:
    - value: tenant-a
      exporters: [otlp/tempo-tenant-a]
    - value: tenant-b
      exporters: [otlp/tempo-tenant-b]

exporters:
  otlp/tempo-tenant-a:
    endpoint: tempo-tenant-a.observability.svc:4317
    headers:
      X-Scope-OrgID: tenant-a

  otlp/tempo-tenant-b:
    endpoint: tempo-tenant-b.observability.svc:4317
    headers:
      X-Scope-OrgID: tenant-b

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [memory_limiter, routing]
      exporters: [otlp/tempo-tenant-a, otlp/tempo-tenant-b]
```

### 3.2 Namespace Isolation

```yaml
# Independent OTel Collector per namespace
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
  namespace: tenant-a
data:
  config.yaml: |
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317

    processors:
      attributes:
        actions:
        - key: tenant
          value: tenant-a
          action: upsert
      batch:
        timeout: 5s

    exporters:
      otlp:
        endpoint: central-otel-collector.observability.svc:4317

    service:
      pipelines:
        traces:
          receivers: [otlp]
          processors: [attributes, batch]
          exporters: [otlp]
```

## 4. K8s Auto-Injection

### 4.1 OpenTelemetry Operator Deployment

``` bash
# 🟡 Medium risk: will modify cluster/resource state, please confirm target, impact scope and authorization before execution
# Install OTel Operator
kubectl apply -f https://github.com/open-telemetry/opentelemetry-operator/releases/latest/download/opentelemetry-operator.yaml
```
### 4.2 Instrumentation CR

```yaml
apiVersion: opentelemetry.io/v1alpha1
kind: Instrumentation
metadata:
  name: instrumentation
  namespace: production
spec:
  exporter:
    endpoint: http://otel-collector.observability.svc:4317

  propagators:
  - tracecontext
  - baggage

  sampler:
    type: parentbased_traceidratio
    argument: "0.1"

  env:
  - name: OTEL_K8S_NAMESPACE
    valueFrom:
      fieldRef:
        apiVersion: v1
        fieldPath: metadata.namespace
  - name: OTEL_K8S_POD_NAME
    valueFrom:
      fieldRef:
        apiVersion: v1
        fieldPath: metadata.name
  - name: OTEL_K8S_NODE_NAME
    valueFrom:
      fieldRef:
        apiVersion: v1
        fieldPath: spec.nodeName

  java:
    image: ghcr.io/open-telemetry/opentelemetry-operator/autoinstrumentation-java:latest
    env:
    - name: OTEL_JAVAAGENT_ENABLED
      value: "true"

  python:
    image: ghcr.io/open-telemetry/opentelemetry-operator/autoinstrumentation-python:latest

  nodejs:
    image: ghcr.io/open-telemetry/opentelemetry-operator/autoinstrumentation-nodejs:latest
```

### 4.3 Auto-Injection Configuration

```yaml
# Add annotations to Deployment to enable auto-injection
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
  namespace: production
spec:
  template:
    metadata:
      annotations:
        instrumentation.opentelemetry.io/inject-java: "true"
        instrumentation.opentelemetry.io/inject-python: "true"
        sidecar.opentelemetry.io/inject: "true"
    spec:
      containers:
      - name: app
        image: my-app:latest
```

## 5. Performance Tuning

### 5.1 Collector Resource Configuration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: otel-collector
  namespace: observability
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: otel-collector
        resources:
          requests:
            cpu: "1"
            memory: 1Gi
          limits:
            cpu: "2"
            memory: 2Gi
        env:
        - name: GOGC
          value: "100"
        - name: GOMEMLIMIT
          value: "1800MiB"
```

### 5.2 Queue and Retry Configuration

```yaml
exporters:
  otlp/tempo:
    endpoint: tempo-distributor.observability.svc:4317
    sending_queue:
      enabled: true
      num_consumers: 10
      queue_size: 5000
      storage: file_storage
    retry_on_failure:
      enabled: true
      initial_interval: 5s
      max_interval: 30s
      max_elapsed_time: 300s

extensions:
  file_storage:
    directory: /var/lib/otel/storage
    timeout: 1s
```

### 5.3 Prometheus Monitoring

```yaml
# OTel Collector self-metrics exposure
service:
  telemetry:
    metrics:
      address: 0.0.0.0:8888
      level: detailed
    logs:
      level: info

# Prometheus ServiceMonitor
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: otel-collector
  namespace: observability
spec:
  selector:
    matchLabels:
      app: otel-collector
  endpoints:
  - port: metrics
    interval: 15s
```

## 6. Best Practices

```
OTel Collector configuration checklist:

□ Configure memory_limiter to prevent OOM
□ Use batch processor to optimize throughput
□ Configure k8sattributes processor to automatically add K8s metadata
□ Use filter processor to filter noise data such as health checks
□ Configure retry and queue mechanisms to ensure reliability
□ Use OTel Operator for auto-injection
□ Configure multiple Pipelines to separate different signal types
□ Deploy HPA for automatic Collector scaling
□ Monitor Collector self-metrics
□ Use Tail Sampling to optimize sampling costs
```

## Related

- [[domain-06-observability/04-tracing/01-jaeger-production-deployment|Jaeger Production Deployment]]
- [[domain-06-observability/04-tracing/02-grafana-tempo-tracing|Grafana Tempo]]

## See Also

- [OpenTelemetry Collector documentation](https://opentelemetry.io/docs/collector/)
- [OTel Operator documentation](https://opentelemetry.io/docs/kubernetes/operator/)


<!-- risk-assessed -->
