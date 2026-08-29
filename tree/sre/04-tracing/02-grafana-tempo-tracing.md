---
title: Grafana Tempo Distributed Tracing
description: 'Grafana Tempo: Deployment architecture (Single/Microservices), TraceQL query language, integration with Loki/Mimir, search performance optimization, Object Storage backend configuration'
summary: 'Tempo deployment architecture, TraceQL, Grafana stack integration and storage optimization'
category: observability
tags:
- grafana-tempo
- distributed-tracing
- traceql
- object-storage
- grafana-stack
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
- What is Grafana Tempo
- How to deploy Grafana Tempo
trigger_keywords:
- Grafana Tempo
- TraceQL
- Distributed Tracing
- Object Storage
- Grafana Stack
prerequisites:
- kubectl-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: KUDIG Team
  role: contributor
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/04-tracing/02-grafana-tempo-tracing.md
---

> **Production Environment Security Notice**
>
> This document contains executable operations commands. Before executing, please confirm: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have verified in a non-production environment first. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state, but usually reversible), 🟢 Low risk/read-only (information gathering, no side effects).


# Grafana Tempo Distributed Tracing

## Overview

Grafana Tempo is an open-source highly scalable distributed tracing backend by Grafana Labs, designed for low cost and high throughput. Compared to Jaeger, Tempo does not require a separate index storage and directly uses Object Storage to store Trace data, significantly reducing operational costs.

## 1. Deployment Architecture

### 1.1 Single Binary Mode (Development/Small Scale)

```
┌─────────────────────────────┐
│      Tempo (Single)         │
│  ┌───────┐ ┌─────┐ ┌────┐  │
│  │Distributor│ │Ingester│ │Query│  │
│  └───────┘ └─────┘ └────┘  │
│           │                  │
│           ▼                  │
│     ┌─────────┐              │
│     │ Object  │              │
│     │ Storage │              │
│     └─────────┘              │
└─────────────────────────────┘
```

### 1.2 Microservices Mode (Production Recommended)

```
┌──────────────────────────────────────────────────────────────┐
│                  Tempo Microservices                         │
│                                                              │
│  ┌─────────────────────────────────────────────────┐        │
│  │              Distributor (Deployment)            │        │
│  │  Receive Trace → Validate → Distribute to Ingester by hash   │
│  └───────────────────────┬─────────────────────────┘        │
│                          ▼                                   │
│  ┌─────────────────────────────────────────────────┐        │
│  │              Ingester (StatefulSet)              │        │
│  │  Receive Trace → Write to WAL → Periodically Flush to Storage  │
│  │  Replication factor: 3 (recommended)                      │
│  └───────────────────────┬─────────────────────────┘        │
│                          ▼                                   │
│  ┌─────────────────────────────────────────────────┐        │
│  │              Compactor (Deployment)              │        │
│  │  Merge Block → Compress → Clean up expired data               │
│  └───────────────────────┬─────────────────────────┘        │
│                          ▼                                   │
│  ┌─────────────────────────────────────────────────┐        │
│  │              Querier (Deployment)                │        │
│  │  Receive query → Read from Storage/Ingester → Return result  │
│  └───────────────────────┬─────────────────────────┘        │
│                          ▼                                   │
│  ┌─────────────────────────────────────────────────┐        │
│  │              Query Frontend (Deployment)          │        │
│  │  Query cache → Query splitting → Parallel queries                 │
│  └─────────────────────────────────────────────────┘        │
│                          ▼                                   │
│  ┌─────────────────────────────────────────────────┐        │
│  │              Object Storage                      │        │
│  │  S3 / GCS / Azure Blob / MinIO                   │        │
│  └─────────────────────────────────────────────────┘        │
└──────────────────────────────────────────────────────────────┘
```

## 2. Production Deployment Configuration

### 2.1 Helm Deployment

``` bash
# 🟡 Medium risk: modifies cluster/resource state, please confirm target, scope and authorization before executing
# Add Grafana Helm repository
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update

# Production mode deployment
helm install tempo grafana/tempo-distributed \
  --namespace observability \
  --create-namespace \
  -f tempo-values.yaml
```
### 2.2 Helm Values (Production Configuration)

```yaml
# tempo-values.yaml
global:
  clusterDomain: cluster.local

distributor:
  replicas: 3
  resources:
    requests:
      cpu: 500m
      memory: 512Mi
    limits:
      cpu: "2"
      memory: 2Gi
  config:
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: "0.0.0.0:4317"
          http:
            endpoint: "0.0.0.0:4318"
      jaeger:
        protocols:
          thrift_compact:
            endpoint: "0.0.0.0:6831"
          thrift_binary:
            endpoint: "0.0.0.0:6832"
          grpc:
            endpoint: "0.0.0.0:14250"
      zipkin:
        endpoint: "0.0.0.0:9411"

ingester:
  replicas: 3
  resources:
    requests:
      cpu: "1"
      memory: 2Gi
    limits:
      cpu: "2"
      memory: 4Gi
  persistence:
    enabled: true
    storageClass: fast-ssd
    size: 50Gi
  config:
    trace_idle_period: 10s
    max_block_bytes: 1048576  # 1MB
    max_block_duration: 30m
    complete_block_timeout: 3m
    flush_check_period: 5s

compactor:
  replicas: 1
  resources:
    requests:
      cpu: 500m
      memory: 512Mi
    limits:
      cpu: "1"
      memory: 1Gi
  config:
    compaction:
      block_retention: 720h  # 30 days
      compacted_block_retention: 10m
      compaction_window: 1h
      max_compaction_objects: 6000000
      max_block_bytes: 107374182400  # 100GB

querier:
  replicas: 3
  resources:
    requests:
      cpu: 500m
      memory: 512Mi
    limits:
      cpu: "2"
      memory: 2Gi
  config:
    frontend_worker:
      frontend_address: tempo-query-frontend:9095

query_frontend:
  replicas: 2
  resources:
    requests:
      cpu: 500m
      memory: 512Mi
    limits:
      cpu: "1"
      memory: 1Gi
  config:
    max_retries: 2
    search:
      max_duration: 0  # No search time range limit
      default_result_limit: 20
      max_result_limit: 0

storage:
  trace:
    backend: s3
    s3:
      bucket: tempo-traces
      endpoint: minio.observability.svc:9000
      access_key: ${MINIO_ACCESS_KEY}
      secret_key: ${MINIO_SECRET_KEY}
      insecure: true
    wal:
      path: /var/tempo/wal
    local:
      path: /var/tempo/blocks
    pool:
      max_workers: 100
      queue_depth: 10000
```

## 3. TraceQL Query Language

### 3.1 Basic Queries

```traceql
# Query by service name
{ resource.service.name = "payment-service" }

# Query by span name
{ name = "processPayment" }

# Query by status
{ status = error }

# Combined conditions
{ resource.service.name = "payment-service" && status = error }

# Query by duration
{ duration > 1s }

# Query by attributes
{ span.http.method = "POST" && span.http.status_code = 500 }
```

### 3.2 Structured Queries

```traceql
# Find traces containing errors
{ resource.service.name = "payment-service" } >> { status = error }

# Find parent span slow, child span normal case
{ duration > 5s } >> { duration < 100ms }

# Find traces with specific path
{ resource.service.name = "api-gateway" }
  >> { resource.service.name = "order-service" }
  >> { resource.service.name = "payment-service" }

# Aggregate queries
{ resource.service.name = "payment-service" }
  | avg(duration) > 500ms
```

### 3.3 Advanced Queries

```traceql
# Filter by environment
{ resource.deployment.environment = "production" && resource.service.name = "api-gateway" }

# Find cross-service call chains
{ resource.service.name = "api-gateway" && span.http.target = "/api/orders" }
  >> { resource.service.name = "order-service" }
  >> { resource.service.name = "inventory-service" }

# Filter by labels
{ resource.k8s.namespace.name = "production" && resource.k8s.pod.name =~ "payment-.*" }

# Query by time range
{ resource.service.name = "payment-service" && duration > 2s }
  | by(resource.service.name)
```

## 4. Grafana Stack Integration

### 4.1 Tempo + Loki Integration

```yaml
# Grafana datasource configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: grafana-datasources
  namespace: observability
data:
  datasources.yaml: |
    apiVersion: 1
    datasources:
    - name: Tempo
      type: tempo
      access: proxy
      url: http://tempo-query-frontend.observability.svc:3100
      uid: tempo
      jsonData:
        tracesToLogsV2:
          datasourceUid: loki
          filterByTraceID: true
          filterBySpanID: true
        tracesToMetrics:
          datasourceUid: prometheus
        serviceMap:
          datasourceUid: prometheus
        nodeGraph:
          enabled: true
        lokiSearch:
          datasourceUid: loki

    - name: Loki
      type: loki
      access: proxy
      url: http://loki-gateway.observability.svc:3100
      uid: loki
      jsonData:
        derivedFields:
        - datasourceUid: tempo
          matcherRegex: "trace_id=(\\w+)"
          name: TraceID
          url: "$${__value.raw}"
```

### 4.2 Tempo + Mimir Integration (Traces to Metrics)

```yaml
# Use Span Metrics to generate metrics
# Configure spanmetrics connector in OTel Collector
connectors:
  spanmetrics:
    histogram:
      explicit:
        buckets: [5ms, 10ms, 25ms, 50ms, 100ms, 250ms, 500ms, 1s, 5s, 10s]
    dimensions:
    - name: http.method
    - name: http.status_code
    - name: service.name
    temporality: cumulative

exporters:
  prometheus/remotewrite:
    endpoint: http://mimir-distributor.observability.svc:8080/api/v1/push

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [otlp/tempo, spanmetrics]
    metrics/spanmetrics:
      receivers: [spanmetrics]
      exporters: [prometheus/remotewrite]
```

## 5. Search Performance Optimization

### 5.1 Search Configuration Optimization

```yaml
# tempo-config.yaml search optimization
query_frontend:
  search:
    max_duration: 0
    default_result_limit: 20
    max_result_limit: 0
    concurrent_jobs: 1000
    target_bytes_per_job: 10485760  # 10MB
    search_recent_trace: true
    ingester:
      search_target_bytes_per_job: 1048576  # 1MB
    default_search_filter: "{resource.service.name=~\".*\"}"

querier:
  search:
    prefer_self: 10
    external_endpoints: []
    external_hedge_requests_at: 5s
    external_hedge_requests_up_to: 2
```

### 5.2 Cache Configuration

```yaml
# Configure Redis cache
query_frontend:
  cache:
    type: redis
    redis:
      endpoint: redis.observability.svc:6379
      expiration: 1h
      db: 0

ingester:
  cache:
    type: redis
    redis:
      endpoint: redis.observability.svc:6379
      expiration: 30m
      db: 1
```

## 6. Object Storage Configuration

### 6.1 S3 Configuration

```yaml
storage:
  trace:
    backend: s3
    s3:
      bucket: tempo-traces
      endpoint: s3.ap-northeast-1.amazonaws.com
      region: ap-northeast-1
      access_key: ${AWS_ACCESS_KEY_ID}
      secret_key: ${AWS_SECRET_ACCESS_KEY}
      insecure: false
      part_size: 5242880  # 5MB
      hedge_requests_at: 500ms
      hedge_requests_up_to: 2
```

### 6.2 GCS Configuration

```yaml
storage:
  trace:
    backend: gcs
    gcs:
      bucket_name: tempo-traces
      credentials_file: /etc/gcp/credentials.json
      prefix: traces/
```

### 6.3 MinIO Configuration

```yaml
storage:
  trace:
    backend: s3
    s3:
      bucket: tempo-traces
      endpoint: minio.observability.svc:9000
      access_key: ${MINIO_ACCESS_KEY}
      secret_key: ${MINIO_SECRET_KEY}
      insecure: true
      forcepathstyle: true
```

## 7. Best Practices

```
Tempo production deployment checklist:

□ Deploy using Microservices mode
□ Configure Object Storage as backend (S3/GCS/MinIO)
□ Set appropriate Block retention time
□ Configure Ingester replication factor (recommended 3)
□ Enable query cache (Redis)
□ Configure TraceQL search optimization
□ Integrate Loki to implement Traces to Logs
□ Integrate Mimir to implement Traces to Metrics
□ Configure Span Metrics to generate RED metrics
□ Monitor Tempo component health status
```

## Related

- [[domain-06-observability/04-tracing/01-jaeger-production-deployment|Jaeger Production Deployment]]
- [[domain-06-observability/04-tracing/03-opentelemetry-collector-patterns|OTel Collector Configuration Patterns]]

## See Also

- [Grafana Tempo Documentation](https://grafana.com/docs/tempo/latest/)
- [TraceQL Documentation](https://grafana.com/docs/tempo/latest/traceql/)


<!-- risk-assessed -->
