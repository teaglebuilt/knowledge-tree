---
title: K8s Distributed Tracing Practice Guide (Jaeger / Tempo / OpenTelemetry)
description: 'K8s Distributed Tracing Practice Guide (Jaeger / Tempo / OpenTelemetry)'
summary: 'helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts'
category: enterprise-monitoring-alerting
tags:
- k8s
- monitoring
- alerting
- prometheus
- grafana
- jaeger
- helm
- docker
- mysql
- elasticsearch
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Monitoring Engineer
- DevOps Engineer
estimated_read_time: 5min
intent_queries:
- What is K8s Distributed Tracing Practice Guide (Jaeger / Tempo / OpenTelemetry)
- How to implement K8s Distributed Tracing Practice Guide (Jaeger / Tempo / OpenTelemetry)
- Kubernetes Enterprise Monitoring Alerting Best Practices
trigger_keywords:
- K8s
- Distributed Tracing
- Jaeger
- Tempo
- OpenTelemetry
- enterprise
- monitoring
- alerting
prerequisites:
- kubectl-basics
- observability-basics
- helm-basics
- prometheus-basics
- monitoring-basics
- mysql-basics
- logging-basics
- tracing-basics
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
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/04-tracing/99-distributed-tracing-guide.md
cross_refs:
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/promql.md
  label: 'Cheatsheet: promql'
---

> **Production Environment Security Notice**
>
> This document contains operational commands that can be executed directly. Before execution, please confirm: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether it has been validated in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state, but usually reversible), 🟢 Low risk/read-only (information collection, no side effects).




# K8s Distributed Tracing Practice Guide ([[Jaeger|Jaeger]] / Tempo / [[OpenTelemetry|OpenTelemetry]])

> **Applicable Versions**: Jaeger v1.65 / Grafana Tempo v2.7 / OpenTelemetry Collector v0.120  
> **Last Updated**: 2026-04-24  
> **Difficulty**: Intermediate

---

<!-- chunk: 📋 Table of Contents -->## 📋 Table of Contents

- [One. Three Pillars of Observability](#one-three-pillars-of-observability)
- [Two. OpenTelemetry Architecture](#two-opentelemetry-architecture)
- [Three. OpenTelemetry Collector Deployment](#three-opentelemetry-collector-deployment)
- [Four. Jaeger End-to-End Tracing](#four-jaeger-end-to-end-tracing)
- [Five. Grafana Tempo Lightweight Tracing](#five-grafana-tempo-lightweight-tracing)
- [Six. Application Auto-Instrumentation](#six-application-auto-instrumentation)
- [Seven. Trace and Log Correlation](#seven-trace-and-log-correlation)
- [Eight. Sampling Strategies and Cost Control](#eight-sampling-strategies-and-cost-control)
- [Nine. Feature Comparison](#nine-feature-comparison)

---

<!-- chunk: One. Three Pillars of Observability -->## One. Three Pillars of Observability

```
Observability Stack
├── Metrics (Indicators)
│   ├── Prometheus (pull-based)
│   ├── Grafana (visualization)
│   └── Question: What happened? (WHAT)
│
├── Logs (Logs)
│   ├── Loki / ELK / Fluentd
│   └── Question: Why did it happen? (WHY)
│
└── Traces (Traces)  ◄── Focus of this guide
    ├── Jaeger / Tempo / Zipkin
    └── Question: Where did it happen? (WHERE)
        └── Complete call chain across services
```

## Trace Core Concepts

| Concept | Explanation | Analogy |
|:---|:---|:---|
| Trace | A complete request call chain | The complete mail delivery path of a letter |
| Span | An operation unit in the call chain | Each processing node at the post office |
| SpanContext | Context propagation (TraceID, SpanID) | Tracking barcode on the envelope |
| Baggage | Key-value pairs propagated across Spans | Notes attached with the letter |

---

<!-- chunk: Two. OpenTelemetry Architecture -->## Two. OpenTelemetry Architecture

```
OpenTelemetry (CNCF Graduated)
├── API / SDK (Application Integration)
│   ├── Auto-Instrumentation (Zero Code)
│   └── Manual Instrumentation (Custom Spans)
│
├── Collector (Unified Collection)
│   ├── Receivers (Receive: OTLP / Jaeger / Zipkin)
│   ├── Processors (Process: Batch / Memory Limit)
│   └── Exporters (Export: Jaeger / Tempo / Prometheus)
│
└── Protocol (OTLP)
    ├── gRPC (default)
    └── HTTP/Protobuf
```

---

<!-- chunk: Three. OpenTelemetry Collector Deployment -->## Three. OpenTelemetry Collector Deployment

## 3.1 Helm Installation

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend --dry-run or diff first
> - `helm upgrade/install`: Deploy/upgrade release

``` bash
# 🟡 Medium risk: modifies cluster/resource state, confirm target, scope, and authorization before executing
helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts
helm install otel-collector open-telemetry/opentelemetry-collector \
  --namespace observability \
  --create-namespace \
  --set mode=deployment
```
## 3.2 Production-Grade Configuration

```yaml
# values-otel-collector.yaml
mode: deployment
replicaCount: 2

resources:
  requests:
    cpu: 200m
    memory: 512Mi
  limits:
    cpu: 1000m
    memory: 2Gi

config:
  receivers:
    otlp:
      protocols:
        grpc:
          endpoint: 0.0.0.0:4317
        http:
          endpoint: 0.0.0.0:4318
    
    prometheus:
      config:
        scrape_configs:
        - job_name: 'otel-collector'
          scrape_interval: 10s
          static_configs:
          - targets: ['0.0.0.0:8888']
  
  processors:
    batch:
      timeout: 1s
      send_batch_size: 1024
    
    memory_limiter:
      limit_mib: 1500
      spike_limit_mib: 512
      check_interval: 5s
    
    resource:
      attributes:
      - key: k8s.cluster.name
        value: production
        action: upsert
      - key: environment
        value: production
        action: upsert
  
  exporters:
    # Export to Jaeger
    otlp/jaeger:
      endpoint: jaeger-collector.observability.svc.cluster.local:4317
      tls:
        insecure: true
    
    # Export to Tempo
    otlp/tempo:
      endpoint: tempo.observability.svc.cluster.local:4317
      tls:
        insecure: true
    
    # Export to Prometheus (Metrics)
    prometheusremotewrite:
      endpoint: http://prometheus.monitoring.svc.cluster.local:9090/api/v1/write
    
    # Debug output
    logging:
      loglevel: warn
  
  service:
    pipelines:
      traces:
        receivers: [otlp]
        processors: [memory_limiter, resource, batch]
        exporters: [otlp/jaeger, otlp/tempo]
      
      metrics:
        receivers: [otlp, prometheus]
        processors: [memory_limiter, resource, batch]
        exporters: [prometheusremotewrite]
```

---

<!-- chunk: Four. Jaeger End-to-End Tracing -->## Four. Jaeger End-to-End Tracing

## 4.1 Deployment

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend --dry-run or diff first
> - `helm upgrade/install`: Deploy/upgrade release

``` bash
# 🟡 Medium risk: modifies cluster/resource state, confirm target, scope, and authorization before executing
helm repo add jaegertracing https://jaegertracing.github.io/helm-charts
helm install jaeger jaegertracing/jaeger \
  --namespace observability \
  --create-namespace \
  --set provisionDataStore.cassandra=false \
  --set provisionDataStore.elasticsearch=true \
  --set storage.type=elasticsearch \
  --set elasticsearch.replicas=1
```
## 4.2 Production-Grade Configuration (Using External Storage)

```yaml
# values-jaeger.yaml
provisionDataStore:
  cassandra: false
  elasticsearch: false  # Use external ES

storage:
  type: elasticsearch
  elasticsearch:
    serverUrls: http://elasticsearch.monitoring.svc.cluster.local:9200

agent:
  enabled: false  # Use OpenTelemetry Collector

collector:
  service:
    otlp:
      grpc:
        enabled: true
      http:
        enabled: true
  
  resources:
    requests:
      cpu: 500m
      memory: 1Gi
    limits:
      cpu: 2000m
      memory: 4Gi

query:
  enabled: true
  service:
    type: ClusterIP
  ingress:
    enabled: true
    hosts:
      - jaeger.example.com
```

## 4.3 Accessing Jaeger UI

``` bash
# 🟡 Medium risk: modifies cluster/resource state, confirm target, scope, and authorization before executing
kubectl port-forward -n observability svc/jaeger-query 16686:16686
# Open http://localhost:16686
```
---

<!-- chunk: Five. Grafana Tempo Lightweight Tracing -->## Five. Grafana Tempo Lightweight Tracing

## 5.1 Deployment

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend --dry-run or diff first
> - `helm upgrade/install`: Deploy/upgrade release

``` bash
# 🟡 Medium risk: modifies cluster/resource state, confirm target, scope, and authorization before executing
helm repo add grafana https://grafana.github.io/helm-charts
helm install tempo grafana/tempo \
  --namespace observability \
  --create-namespace \
  --set tempo.storage.trace.backend=local
```
## 5.2 Production-Grade Configuration (Object Storage)

```yaml
# values-tempo.yaml
tempo:
  storage:
    trace:
      backend: s3
      s3:
        bucket: tempo-traces
        endpoint: s3.us-east-1.amazonaws.com
        region: us-east-1
        access_key: ${AWS_ACCESS_KEY_ID}
        secret_key: ${AWS_SECRET_ACCESS_KEY}
  
  # Retention policy
  compactor:
    compaction:
      block_retention: 168h  # 7 days
  
  # Resource limits
  resources:
    requests:
      cpu: 500m
      memory: 2Gi
    limits:
      cpu: 2000m
      memory: 8Gi

# Grafana data source configuration
datasources:
  - name: Tempo
    type: tempo
    url: http://tempo.observability.svc.cluster.local:3100
    isDefault: false
```

## 5.3 Tempo Advantages

| Feature | Jaeger | Tempo |
|:---|:---|:---|
| Storage | Elasticsearch / Cassandra | S3 / GCS / Azure Blob |
| Cost | High (indexed storage) | Low (object storage) |
| Dependency queries | Built-in | Via Grafana + TraceQL |
| Alerting | Not supported | Via Grafana |
| Learning curve | Low | Medium (requires TraceQL) |

---

<!-- chunk: Six. Application Auto-Instrumentation -->## Six. Application Auto-Instrumentation

## 6.1 Java (OpenTelemetry Agent)

```dockerfile
# Dockerfile
FROM openjdk:17-jdk
COPY --from=ghcr.io/open-telemetry/opentelemetry-java-instrumentation:latest \
  /opentelemetry-javaagent.jar /opt/opentelemetry-javaagent.jar
ENV JAVA_TOOL_OPTIONS="-javaagent:/opt/opentelemetry-javaagent.jar"
ENV OTEL_SERVICE_NAME=myapp
ENV OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector.observability.svc.cluster.local:4317
COPY target/*.jar app.jar
ENTRYPOINT ["java", "-jar", "/app.jar"]
```

## 6.2 Node.js

```bash
npm install @opentelemetry/auto-instrumentations-node
```

```javascript
// tracing.js
const { NodeSDK } = require('@opentelemetry/sdk-node');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-grpc');
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');

const sdk = new NodeSDK({
  traceExporter: new OTLPTraceExporter({
    url: 'http://otel-collector.observability.svc.cluster.local:4317'
  }),
  instrumentations: [getNodeAutoInstrumentations()]
});

sdk.start();
```

## 6.3 Python

```bash
pip install opentelemetry-distro opentelemetry-exporter-otlp
opentelemetry-bootstrap -a install
```

```bash
# Start application
OTEL_SERVICE_NAME=myapp \
OTEL_EXPORTER_OTLP_ENDPOINT=http://otel-collector.observability.svc.cluster.local:4317 \
opentelemetry-instrument python app.py
```

## 6.4 Go (Manual Instrumentation)

```go
import (
    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
    "go.opentelemetry.io/otel/sdk/trace"
)

func initTracer() (*trace.TracerProvider, error) {
    exporter, err := otlptracegrpc.New(context.Background(),
        otlptracegrpc.WithEndpoint("otel-collector.observability.svc.cluster.local:4317"),
        otlptracegrpc.WithInsecure(),
    )
    if err != nil {
        return nil, err
    }
    
    tp := trace.NewTracerProvider(
        trace.WithBatcher(exporter),
    )
    otel.SetTracerProvider(tp)
    return tp, nil
}
```

---

<!-- chunk: Seven. Trace and Log Correlation -->## Seven. Trace and Log Correlation

## 7.1 Injecting TraceID into Logs

```python
# Python example
import logging
from opentelemetry import trace

tracer = trace.get_tracer(__name__)

class TraceIdFilter(logging.Filter):
    def filter(self, record):
        current_span = trace.get_current_span()
        record.trace_id = format(current_span.get_span_context().trace_id, '032x') if current_span else 'N/A'
        record.span_id = format(current_span.get_span_context().span_id, '016x') if current_span else 'N/A'
        return True

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - trace_id=%(trace_id)s - %(message)s'
)
logger = logging.getLogger(__name__)
logger.addFilter(TraceIdFilter())
```

## 7.2 Loki Log Label Correlation

```yaml
# Promtail configuration
scrape_configs:
- job_name: kubernetes-pods
  pipeline_stages:
  - json:
      expressions:
        trace_id: trace_id
  - labels:
      trace_id:
```

---

<!-- chunk: Eight. Sampling Strategies and Cost Control -->## Eight. Sampling Strategies and Cost Control

## 8.1 Head-based Sampling (Collector Side)

```yaml
processors:
  probabilistic_sampler:
    sampling_percentage: 10.0  # 10% sampling
  
  tail_sampling:
    decision_wait: 10s
    num_traces: 100000
    expected_new_traces_per_sec: 1000
    policies:
      - name: errors
        type: status_code
        status_code: {status_codes: [ERROR]}
      - name: slow_requests
        type: latency
        latency: {threshold_ms: 1000}
```

## 8.2 Sampling Strategy Comparison

| Strategy | Implementation Location | Advantages | Disadvantages |
|:---|:---|:---|:---|
| Head-based | SDK/Agent | Simple, low overhead | Cannot sample based on results |
| Tail-based | Collector | Can sample based on errors/latency | Large memory overhead |
| Adaptive | Collector | Dynamically adjusts sampling rate | Complex configuration |

## 8.3 Cost Control

```
Trace Cost ≈ Storage Cost + Network Cost + Compute Cost

Optimization Methods:
1. Reasonable sampling rate (production 1-10%, development 100%)
2. Short retention period (7 days vs 30 days)
3. Object storage (Tempo vs Jaeger+ES)
4. Drop healthy Spans (retain only exceptions)
5. Compression (gzip OTLP)
```

---

<!-- chunk: Nine. Feature Comparison -->## Nine. Feature Comparison

| Dimension | Jaeger | Tempo | Zipkin |
|:---|:---|:---|:---|
| **CNCF Status** | Graduated | Non-CNCF | Incubating |
| **Storage Backend** | ES/Cassandra/Badger | S3/GCS/Azure | ES/MySQL/Cassandra |
| **Query Language** | Native UI | TraceQL (Grafana) | Native UI |
| **Dependency Analysis** | Built-in | Grafana Tempo + plugin | Built-in |
| **Alerting** | Not supported | Grafana alerts | Not supported |
| **Multi-tenancy** | Limited | Supported | Limited |
| **Storage Cost** | High | Low | Medium |
| **Recommended Scenario** | Full-featured tracing | Cost-sensitive / Grafana ecosystem | Simple scenarios / Spring |

## Recommended Architecture

```
Application (Auto-Instrumentation)
    |
    ├── OTLP/gRPC ──► OpenTelemetry Collector
    |                       |
    |                       ├── traces ──► Tempo (low-cost long-term storage)
    |                       ├── traces ──► Jaeger (real-time queries)
    |                       └── metrics ──► Prometheus
    |
    └── Logs (trace_id) ──► Loki
                                |
                                └── Grafana (unified queries: Metrics + Logs + Traces)
```

---

<!-- chunk: Reference Links -->## Reference Links

- [OpenTelemetry Official](https://opentelemetry.io/)
- [Jaeger Documentation](https://www.jaegertracing.io/docs/)
- [Grafana Tempo Documentation](https://grafana.com/docs/tempo/)
- [OpenTelemetry Collector](https://opentelemetry.io/docs/collector/)
- [TraceQL Query Language](https://grafana.com/docs/tempo/latest/traceql/)

---

<!-- chunk: Obsidian Related Documentation -->## Obsidian Related Documentation

- domain-20-enterprise-monitoring-alerting MOC
- [[domain-06-observability/README.md|Domain 06: Enterprise Monitoring and Alerting (Enterprise Monitoring & Alerting)]]
- [[domain-06-observability/00-open-source-projects-index.md|Domain-20 Enterprise Monitoring and Alerting — Open Source Project Index]]
- Prometheus Enterprise Monitoring System In-Depth Practice
- Grafana Enterprise Observability Platform In-Depth Practice
- OpenTelemetry Distributed Tracing and Observability In-Depth Practice
- Thanos Enterprise Metrics Federation and Long-term Storage
- Datadog Enterprise APM In-Depth Practice
- Datadog Enterprise Monitoring Platform In-Depth Practice
- Elastic Stack Enterprise Log Analysis In-Depth Practice
- Elastic Stack Enterprise Observability Platform In-Depth Practice
- Zabbix Enterprise Monitoring Platform In-Depth Practice

## See Also

- 07-zabbix-enterprise-monitoring
- 08-new-relic-enterprise-apm
- 99-prometheus-enterprise-guide
- 01-prometheus-enterprise-monitoring

- [[domain-06-observability/README.md|Back to index]]

## Related

- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Graph Index]]

```

<!-- risk-assessed -->
