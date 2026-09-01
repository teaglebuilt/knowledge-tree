---
title: Distributed Tracing System
description: In-depth analysis of distributed tracing: OpenTelemetry architecture, Jaeger/Knative tracing, Span/Trace models, Baggage, sampling strategies and integration practices in Kubernetes
summary: In-depth analysis of distributed tracing: OpenTelemetry architecture, Jaeger/Knative tracing, Span/Trace models, Baggage, sampling strategies and integration practices in Kubernetes
category: domain-06-observability
tags:
- k8s
- tracing
- opentelemetry
- jaeger
- span
- distributed-tracing
- observability
- prometheus
- grafana
- helm
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- SRE
- DevOps Engineers
- Monitoring Engineers
estimated_read_time: 5min
intent_queries:
- What is a distributed tracing system
- How to implement distributed tracing
- Kubernetes observability best practices
trigger_keywords:
- distributed-tracing-system
- observability
prerequisites:
- kubectl-basics
- observability-basics
- helm-basics
- prometheus-basics
- monitoring-basics
- kafka-basics
- redis-basics
- policy-basics
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
- name: Dillan Teagle
  role: contributor
cross_refs:
- type: domain
  path: ../domain-01-cluster-fundamentals/
  label: 'Related Knowledge Domain: domain-01-cluster-fundamentals'
- type: domain
  path: ../domain-02-workloads-applications/
  label: 'Related Knowledge Domain: domain-02-workloads-applications'
- type: domain
  path: ../domain-03-networking-traffic/
  label: 'Related Knowledge Domain: domain-03-networking-traffic'
- type: domain
  path: ../domain-07-platform-engineering/
  label: 'Related Knowledge Domain: domain-07-platform-engineering'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/promql.md
  label: 'Quick Reference: promql'
related_docs:
- path: 01-observability-architecture-overview.md
  type: depth
  desc: Observability Architecture System
- path: 02-monitoring-metrics-system.md
  type: depth
  desc: Metrics Monitoring System
- path: ../domain-26-service-mesh/
  type: depth
  desc: Service Mesh
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/04-tracing/04-distributed-tracing.md
---

> **Production Environment Security Notice**
>
> This document contains directly executable operations commands. Before execution, please verify: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have validated in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state, but usually recoverable), 🟢 Low risk/Read-only (information collection, no side effects).




# 04 - Distributed Tracing System (Distributed Tracing)

> **Applicable Versions**: v1.25 - v1.32 | **Last Updated**: 2026-01 | **Reference**: [[entities/opentelemetry.md|opentelemetry]].io](https://opentelemetry.io/)

<!-- chunk: Overview -->
## Overview

From the perspective of a senior performance engineer, this document provides in-depth analysis of the distributed tracing system in Kubernetes environments, covering OpenTelemetry standard specifications, Jaeger/Tempo enterprise-level deployments, full-link application instrumentation practices, and intelligent root cause analysis. Combined with experience from complex microservices architectures and large-scale production environment optimization, it provides professional guidance for enterprises to build high-precision, low-overhead, and scalable distributed tracing capabilities.

---

<!-- chunk: 1. Basic Concepts of Distributed Tracing -->
## 1. Basic Concepts of Distributed Tracing

### 1.1 Core Terminology Definitions

#### Basic Tracing Concepts
```yaml
tracing_concepts:
  trace:
    definition: The complete execution path of a request in a distributed system
    composition: Composed of multiple spans
    identifier: trace_id (globally unique)
    
  span:
    definition: The execution representation of a single unit of work
    contains:
      - operation_name: Operation name
      - span_id: Unique span identifier
      - parent_span_id: Parent span identifier
      - start_time: Start time
      - end_time: End time
      - attributes: Key-value pair attributes
      - events: Point-in-time events
      - status: Execution status
      
  context_propagation:
    purpose: Pass tracing context between services
    headers:
      - traceparent: W3C standard header
      - tracestate: Trace state information
      - baggage: Cross-service propagated metadata
```

### 1.2 Tracing Data Model

#### Span Data Structure
```json
{
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "span_id": "00f067aa0ba902b7",
  "parent_span_id": "00f067aa0ba902b6",
  "name": "HTTP GET /api/users",
  "kind": "SERVER",
  "start_time_unix_nano": 1502788081928613000,
  "end_time_unix_nano": 1502788081928659000,
  "attributes": {
    "http.method": "GET",
    "http.url": "http://localhost:8080/api/users",
    "http.status_code": 200,
    "user.id": "12345"
  },
  "events": [
    {
      "time_unix_nano": 1502788081928630000,
      "name": "DB query started",
      "attributes": {
        "db.statement": "SELECT * FROM users WHERE ..."
      }
    }
  ],
  "status": {
    "code": "STATUS_CODE_OK"
  }
}
```

---

<!-- chunk: 2. OpenTelemetry Standard System -->
## 2. OpenTelemetry Standard System

### 2.1 OpenTelemetry Architecture

#### Unified Observability Framework
```yaml
opentelemetry_architecture:
  instrumentation:
    auto_instrumentation:
      languages_supported:
        - java: javaagent
        - go: otelhttp, otelgrpc
        - python: opentelemetry-instrumentation
        - nodejs: @opentelemetry/auto-instrumentations-node
      benefits:
        - Zero code invasion
        - Automatically capture common frameworks
        - Quick deployment
        
    manual_instrumentation:
      use_cases:
        - Business logic instrumentation
        - Custom span creation
        - Special scenario handling
      api_components:
        - tracer: Create spans
        - meter: Create metrics
        - logger: Create logs
        
  collector:
    components:
      receivers:
        - otlp: OpenTelemetry protocol
        - jaeger: Jaeger protocol
        - zipkin: Zipkin protocol
        - prometheus: Prometheus metrics
      processors:
        - batch: Batch processing
        - memory_limiter: Memory limiting
        - attributes: Attribute processing
        - spanmetrics: Span metrics generation
      exporters:
        - jaeger: Send to Jaeger
        - otlp: Send to OTLP backend
        - prometheus: Export metrics
        - logging: Log output
        
  backend:
    traces_storage:
      - jaeger: Feature-complete, active community
      - tempo: Lightweight, good Grafana integration
      - signoz: Open source APM platform
    metrics_storage:
      - prometheus: Standard metrics storage
      - victoria_metrics: High-performance alternative
    logs_storage:
      - loki: Good traces integration
      - elasticsearch: Feature-rich
```

### 2.2 Collector Configuration Example

#### Production-Grade Collector Configuration
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
      thrift_http:
        endpoint: 0.0.0.0:14268
      grpc:
        endpoint: 0.0.0.0:14250
        
  zipkin:
    endpoint: 0.0.0.0:9411

processors:
  batch:
    timeout: 5s
    send_batch_size: 8192
    
  memory_limiter:
    limit_mib: 400
    spike_limit_mib: 100
    
  attributes:
    actions:
      - key: environment
        value: production
        action: insert
      - key: k8s.namespace
        from_attribute: k8s.namespace.name
        action: upsert
        
  spanmetrics:
    metrics_exporter: prometheus
    dimensions:
      - name: http.method
      - name: http.status_code
      - name: k8s.namespace.name

exporters:
  jaeger:
    endpoint: jaeger-collector:14250
    tls:
      insecure: true
      
  prometheus:
    endpoint: "0.0.0.0:8889"
    namespace: otel
    
  loki:
    endpoint: http://loki:3100/loki/api/v1/push
    headers:
      "X-Scope-OrgID": "production"

extensions:
  health_check:
  pprof:
  zpages:

service:
  extensions: [health_check, pprof, zpages]
  pipelines:
    traces:
      receivers: [otlp, jaeger, zipkin]
      processors: [memory_limiter, batch, attributes]
      exporters: [jaeger]
      
    metrics:
      receivers: [otlp]
      processors: [memory_limiter, batch, spanmetrics]
      exporters: [prometheus]
      
    logs:
      receivers: [otlp]
      processors: [memory_limiter, batch]
      exporters: [loki]
```

---

<!-- chunk: 3. Application Instrumentation Practices -->
## 3. Application Instrumentation Practices

### 3.1 Instrumentation Examples in Different Languages

#### Java Application Instrumentation
```java
// OpenTelemetry Java example
@Configuration
public class OpenTelemetryConfig {
    
    @Bean
    public OpenTelemetry openTelemetry() {
        return OpenTelemetrySdk.builder()
            .setTracerProvider(SdkTracerProvider.builder()
                .addSpanProcessor(BatchSpanProcessor.builder(
                    OtlpGrpcSpanExporter.builder()
                        .setEndpoint("http://otel-collector:4317")
                        .build())
                    .build())
                .build())
            .build();
    }
}

@RestController
@RequestMapping("/api/users")
public class UserController {
    
    private final Tracer tracer = GlobalOpenTelemetry.getTracer("user-service");
    
    @GetMapping("/{id}")
    public ResponseEntity<User> getUser(@PathVariable String id, HttpServletRequest request) {
        // Extract trace context from HTTP headers
        Context parentContext = OpenTelemetryServletUtil.extract(request, Context.current());
        
        Span span = tracer.spanBuilder("GET /api/users/{id}")
            .setParent(parentContext)
            .setAttribute("user.id", id)
            .setAttribute("http.method", "GET")
            .startSpan();
            
        try (Scope scope = span.makeCurrent()) {
            // Add events
            span.addEvent("Database query started");
            
            User user = userService.findById(id);
            
            span.addEvent("Database query completed");
            span.setAttribute("user.exists", user != null);
            
            return ResponseEntity.ok(user);
        } catch (Exception e) {
            span.recordException(e);
            span.setStatus(StatusCode.ERROR, e.getMessage());
            throw e;
        } finally {
            span.end();
        }
    }
}
```

#### Go Application Instrumentation
```go
// OpenTelemetry Go example
package main

import (
    "context"
    "go.opentelemetry.io/otel"
    "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracegrpc"
    "go.opentelemetry.io/otel/propagation"
    "go.opentelemetry.io/otel/sdk/resource"
    sdktrace "go.opentelemetry.io/otel/sdk/trace"
    semconv "go.opentelemetry.io/otel/semconv/v1.17.0"
    "go.opentelemetry.io/otel/trace"
    "google.golang.org/grpc"
)

func initTracer() (*sdktrace.TracerProvider, error) {
    ctx := context.Background()
    
    res, err := resource.New(ctx,
        resource.WithAttributes(
            semconv.ServiceName("user-service"),
            semconv.ServiceVersion("1.0.0"),
        ),
    )
    if err != nil {
        return nil, err
    }

    conn, err := grpc.DialContext(ctx, "otel-collector:4317", grpc.WithInsecure())
    if err != nil {
        return nil, err
    }

    traceExporter, err := otlptracegrpc.New(ctx, otlptracegrpc.WithGRPCConn(conn))
    if err != nil {
        return nil, err
    }

    tp := sdktrace.NewTracerProvider(
        sdktrace.WithBatcher(traceExporter),
        sdktrace.WithResource(res),
    )
    
    otel.SetTracerProvider(tp)
    otel.SetTextMapPropagator(propagation.NewCompositeTextMapPropagator(
        propagation.TraceContext{}, 
        propagation.Baggage{},
    ))
    
    return tp, nil
}

func getUserHandler(w http.ResponseWriter, r *http.Request) {
    ctx := r.Context()
    
    // Extract trace context from HTTP request
    ctx = otel.GetTextMapPropagator().Extract(ctx, propagation.HeaderCarrier(r.Header))
    
    tracer := otel.Tracer("user-service")
    ctx, span := tracer.Start(ctx, "GET /api/users/{id}",
        trace.WithAttributes(
            attribute.String("http.method", r.Method),
            attribute.String("http.url", r.URL.String()),
        ),
    )
    defer span.End()
    
    // Add events
    span.AddEvent("Database query started")
    
    vars := mux.Vars(r)
    userID := vars["id"]
    
    user, err := userService.GetByID(ctx, userID)
    if err != nil {
        span.RecordError(err)
        span.SetStatus(codes.Error, err.Error())
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
    
    span.AddEvent("Database query completed")
    span.SetAttributes(
        attribute.Bool("user.found", user != nil),
        attribute.String("user.id", userID),
    )
    
    // Return response
    json.NewEncoder(w).Encode(user)
}
```

#### Python Application Instrumentation
```python
# OpenTelemetry Python example
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

def setup_opentelemetry():
    resource = Resource(attributes={
        "service.name": "user-service",
        "service.version": "1.0.0",
    })
    
    provider = TracerProvider(resource=resource)
    
    processor = BatchSpanProcessor(
        OTLPSpanExporter(endpoint="http://otel-collector:4317")
    )
    provider.add_span_processor(processor)
    
    trace.set_tracer_provider(provider)

# Flask application example
from flask import Flask, request
import requests

app = Flask(__name__)
setup_opentelemetry()
FlaskInstrumentor().instrument_app(app)
RequestsInstrumentor().instrument()

@app.route('/api/users/<user_id>')
def get_user(user_id):
    tracer = trace.get_tracer(__name__)
    
    with tracer.start_as_current_span("GET /api/users/{id}") as span:
        span.set_attribute("user.id", user_id)
        span.set_attribute("http.method", request.method)
        
        span.add_event("Database query started")
        
        # Call database
        user = get_user_from_db(user_id)
        
        span.add_event("Database query completed")
        span.set_attribute("user.found", user is not None)
        
        if user:
            # Call external service
            with tracer.start_as_current_span("call-payment-service") as child_span:
                response = requests.get(f"http://payment-service/api/balance/{user_id}")
                child_span.set_attribute("http.status_code", response.status_code)
        
        return {"user": user}

def get_user_from_db(user_id):
    # Database query logic
    pass
```

---

<!-- chunk: 4. Jaeger Deployment and Configuration -->
## 4. Jaeger Deployment and Configuration

### 4.1 Jaeger Production Deployment

#### Helm Deployment Configuration
```yaml
# values.yaml
jaeger:
  provisionDataStore:
    cassandra: false
    elasticsearch: true
    
  storage:
    type: elasticsearch
    elasticsearch:
      host: elasticsearch.logging.svc.cluster.local
      port: 9200
      scheme: http
      user: elastic
      password: changeme
      
  agent:
    enabled: true
    cmdlineParams:
      processor.jaeger-binary.server-host-port: :6832
      processor.jaeger-compact.server-host-port: :6831
      
  collector:
    enabled: true
    cmdlineParams:
      collector.zipkin.http-port: 9411
    service:
      zipkin:
        port: 9411
        
  query:
    enabled: true
    service:
      type: LoadBalancer
      port: 80
      
  ingester:
    enabled: false  # Can be enabled if using Kafka
```

### 4.2 Jaeger Query Interface

#### Key Query Features
```yaml
jaeger_query_features:
  trace_search:
    search_criteria:
      - trace_id: Exact trace lookup
      - service: Filter by service name
      - operation: Filter by operation name
      - tags: Filter by tags
      - duration: Time range filter
      - time_range: Time range
      
  trace_analysis:
    capabilities:
      - dependency_graph: Service dependency graph
      - trace_comparison: Trace comparison analysis
      - statistics: Performance statistics
      - flame_graph: Flame graph display
      
  integration:
    grafana:
      dashboard_url: "/d/jaeger/jaeger-dashboard"
      variables:
        - service
        - operation
    prometheus:
      metrics_correlation: true
      span_metrics: true
```

---

<!-- chunk: 5. Trace Analysis and Optimization -->
## 5. Trace Analysis and Optimization

### 5.1 Performance Bottleneck Identification

#### Common Performance Problem Patterns
```yaml
performance_patterns:
  database_bottlenecks:
    indicators:
      - db.query.duration > 100ms
      - high number of sequential queries
      - connection pool exhaustion
    solutions:
      - query optimization
      - connection pooling
      - caching strategies
      
  network_latency:
    indicators:
      - http.client.duration spikes
      - cross-region calls
      - third-party service delays
    solutions:
      - CDN optimization
      - regional deployment
      - async processing
      
  resource_contention:
    indicators:
      - thread/blocking time high
      - GC pause durations
      - memory allocation spikes
    solutions:
      - resource scaling
      - profiling and optimization
      - load balancing
```

### 5.2 Trace Optimization Practices

#### Optimization Strategy Examples
```yaml
optimization_strategies:
  async_processing:
    pattern: fire_and_forget
    implementation:
      - message_queues: kafka, rabbitmq
      - event_driven_architecture
      - background_jobs
      
  caching_layers:
    types:
      - local_cache: redis, memcached
      - distributed_cache: hazelcast, ignite
      - cdn_cache: cloudfront, akamai
      
  database_optimization:
    techniques:
      - connection_pooling: hikariCP, HikariDataSource
      - query_optimization: indexes, query plans
      - read_replicas: master-slave setup
      - sharding: horizontal partitioning
```

---

<!-- chunk: 6. Production Best Practices -->
## 6. Production Best Practices

### 6.1 Sampling Strategies

#### Intelligent Sampling Configuration
```yaml
sampling_strategies:
  probabilistic_sampling:
    rate: 0.1  # 10% sampling rate
    configuration:
      - default: 10%
      - high_priority: 100%
      - low_priority: 1%
      
  adaptive_sampling:
    algorithm: throughput_based
    parameters:
      target_spans_per_second: 1000
      adjustment_interval: 1m
      min_rate: 0.01
      max_rate: 1.0
      
  rule_based_sampling:
    rules:
      - condition: "error = true"
        sampling_rate: 1.0
      - condition: "http.status_code >= 500"
        sampling_rate: 1.0
      - condition: "user.tier = 'premium'"
        sampling_rate: 0.5
      - condition: "path matches '/api/critical/*'"
        sampling_rate: 1.0
```

### 6.2 Tag Management Standards

#### Standardized Tag System
```yaml
standard_tags:
  required_tags:
    - service.name: Service name
    - span.kind: Span type (CLIENT/SERVER/PRODUCER/CONSUMER/INTERNAL)
    - http.method: HTTP method
    - http.status_code: HTTP status code
    
  recommended_tags:
    - user.id: User ID
    - request.id: Request ID
    - trace_id: Trace ID
    - version: Service version
    - environment: Environment identifier
    
  business_tags:
    - order.id: Order ID
    - payment.id: Payment ID
    - session.id: Session ID
    - tenant.id: Tenant ID
```

---

**Tracing Value**: From black box to transparency, from speculation to precise diagnosis, from passive to proactive optimization

---

**Implementation Recommendations**: Prioritize instrumentation of core workflows, gradually expand coverage, and emphasize data quality and analytical value

---

**Table Maintenance**: Kusheet Project | **Author**: Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian Related Documents -->
## Obsidian Related Documents

- observability/MOC.md|domain-06-observability MOC]]
- [[domain-06-observability/README.md|Observability Domain]]
- [[domain-06-observability/00-open-source-projects-index.md|Domain-8 Observability — Open Source Projects Index]]
- Kubernetes Observability Architecture System
- Metrics Monitoring System Details
- 03 - Logging Collection Architecture Details (Logging Architecture)
- 05 - Alert Management Strategy (Alerting Management)
- 06 - Monitoring Alerting Practice and Best Practices (Monitoring Alerting Practice)
- 04 - Monitoring Dashboard Design and Best Practices (Monitoring Dashboards)
- 08 - Logging Audit and Compliance Management (Logging Auditing & Compliance)
- 05 - Event and Audit Log Management (Events & Audit Logs)
- 07 - Monitoring and Metrics Table

## Related

- [[domain-02-workloads-applications/07-java-observability-kubernetes.md|07-java-observability-kubernetes]]

- Observability Architecture System
- Metrics Monitoring System
- Related Knowledge Domain: domain-01-cluster-fundamentals
- Related Knowledge Domain: domain-02-workloads-applications
- Related Knowledge Domain: domain-03-networking-traffic
- Related Knowledge Domain: domain-07-platform-engineering
- [[domain-17-system-foundation/topic-cheat-sheet/promql.md|Quick Reference: promql]]

- [[domain-06-observability/README.md|Back to Index]]- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Map Index]]

## See Also

- 02-monitoring-metrics-system
- 03-logging-architecture
- 05-alerting-management
- 06-monitoring-alerting-practice


<!-- risk-assessed -->
