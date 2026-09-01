---
title: 06-APM Application Performance Monitoring
description: '# 06-APM Application Performance Monitoring'
summary: 'Application Performance Monitoring (APM) is a critical tool for ensuring stable operation of microservices architecture. This document details best practices for distributed tracing, performance metrics collection, and application monitoring.'
category: production-operations
tags:
- k8s
- production
- operations
- best-practices
- prometheus
- grafana
- jaeger
- redis
- elasticsearch
- job
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- SRE
- DevOps Engineer
- Platform Engineer
estimated_read_time: 5min
intent_queries:
- What is APM application performance monitoring
- How to implement APM application performance monitoring
- Kubernetes production operations best practices
trigger_keywords:
- APM Application Performance Monitoring
- production
- operations
prerequisites:
- kubectl-basics
- observability-basics
- prometheus-basics
- monitoring-basics
- redis-basics
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
cross_refs:
- type: fta
  path: ../domain-10-troubleshooting-diagnostics/topic-fta/list/monitoring-fta.md
  label: 'Fault Tree: monitoring'
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/01-overview/06-apm-application-performance-monitoring.md
---

> **Production Environment Security Notice**
>
> This document contains operations commands that can be executed directly. Before executing, please verify: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether the commands have been verified in a non-production environment. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state but usually reversible), 🟢 Low Risk/Read-Only (information gathering, no side effects).




# 06-APM Application Performance Monitoring

> **Applicable Scope**: [[Kubernetes|Kubernetes]] v1.25-v1.32 | **Maintenance Status**: 🔧 Continuously Updated | **Expert Level**: ⭐⭐⭐⭐⭐

<!-- chunk: 📋 Overview -->## 📋 Overview

Application Performance Monitoring (APM) is a critical tool for ensuring stable operation of microservices architecture. This document details best practices for distributed tracing, performance metrics collection, and application monitoring.

<!-- chunk: 🎯 APM Architecture Design -->## 🎯 APM Architecture Design

## Core Component Architecture

## 1. OpenTelemetry Collection Layer
```yaml
# OpenTelemetry Collector Configuration
apiVersion: opentelemetry.io/v1alpha1
kind: OpenTelemetryCollector
metadata:
  name: otel-collector
  namespace: observability
spec:
  config: |
    receivers:
      otlp:
        protocols:
          grpc:
          http:
      jaeger:
        protocols:
          thrift_http:
          grpc:
      zipkin:
      
    processors:
      batch:
      memory_limiter:
        check_interval: 1s
        limit_mib: 4000
        spike_limit_mib: 500
      attributes:
        actions:
          - key: environment
            value: production
            action: insert
      
    exporters:
      otlp/tempo:
        endpoint: tempo:4317
        tls:
          insecure: true
      prometheus:
        endpoint: "0.0.0.0:8889"
        namespace: otel
        const_labels:
          exporter: prometheus
      logging:
      
    service:
      pipelines:
        traces:
          receivers: [otlp, jaeger, zipkin]
          processors: [memory_limiter, batch, attributes]
          exporters: [otlp/tempo, logging]
        metrics:
          receivers: [otlp]
          processors: [memory_limiter, batch]
          exporters: [prometheus, logging]
```

## 2. Application Instrumentation Configuration
```yaml
# Java Application OpenTelemetry Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-otel-config
  namespace: production
data:
  otel-agent-config.yaml: |
    extensions:
      health_check:
      pprof:
      zpages:
    
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
          http:
            endpoint: 0.0.0.0:4318
    
    processors:
      batch:
      memory_limiter:
        check_interval: 1s
        limit_mib: 100
    
    exporters:
      otlp:
        endpoint: otel-collector:4317
        tls:
          insecure: true
    
    service:
      extensions: [health_check, pprof, zpages]
      pipelines:
        traces:
          receivers: [otlp]
          processors: [batch, memory_limiter]
          exporters: [otlp]
```

<!-- chunk: 📊 Distributed Tracing -->## 📊 Distributed Tracing

## Jaeger Tracing Configuration

## 1. Jaeger Operator Deployment
```yaml
# Jaeger Instance Configuration
apiVersion: jaegertracing.io/v1
kind: Jaeger
metadata:
  name: jaeger-all-in-one
spec:
  strategy: allInOne
  allInOne:
    image: jaegertracing/all-in-one:1.40
    options:
      log-level: debug
  storage:
    type: elasticsearch
    options:
      es:
        server-urls: http://elasticsearch:9200
  ingress:
    enabled: true
    annotations:
      kubernetes.io/ingress.class: nginx
      nginx.ingress.kubernetes.io/auth-type: basic
      nginx.ingress.kubernetes.io/auth-secret: jaeger-basic-auth
```

## 2. Application Tracing Instrumentation
```java
// Java Application Tracing Example
@RestController
public class UserController {
    
    @Autowired
    private Tracer tracer;
    
    @GetMapping("/users/{id}")
    public ResponseEntity<User> getUser(@PathVariable String id) {
        Span span = tracer.buildSpan("get-user")
            .withTag("user.id", id)
            .withTag("http.method", "GET")
            .start();
        
        try (Scope scope = tracer.scopeManager().activate(span)) {
            // Business logic
            User user = userService.findById(id);
            
            span.setTag("user.found", user != null);
            if (user != null) {
                span.setTag("user.email.domain", 
                    user.getEmail().split("@")[1]);
            }
            
            return ResponseEntity.ok(user);
        } catch (Exception e) {
            Tags.ERROR.set(span, true);
            span.log(Collections.singletonMap("event", "error"));
            span.log(Collections.singletonMap("error.object", e));
            throw e;
        } finally {
            span.finish();
        }
    }
}
```

## Tracing Data Sampling

## 1. Intelligent Sampling Strategy
```yaml
# Tempo Sampling Configuration
apiVersion: tempo.grafana.com/v1alpha1
kind: TempoMonolithic
metadata:
  name: tempo
  namespace: observability
spec:
  storage:
    traces:
      backend: s3
      s3:
        bucket: tempo-traces
        endpoint: s3.amazonaws.com
  sampling:
    policies:
    - always_sample: {}
    - numeric_attribute:
        key: http.status_code
        min_value: 500
        max_value: 599
    - string_attribute:
        key: service.name
        values:
          - critical-service
          - payment-service
    - rate_limiting:
        spans_per_second: 10
```

## 2. Tracing Data Filtering
```yaml
# Tracing Data Filtering Configuration
processors:
  filter/traces:
    error_mode: ignore
    traces:
      span:
      - name: health_check
      - name: readiness_probe
      - attributes["http.route"] == "/metrics"
      - attributes["http.route"] == "/health"
```

<!-- chunk: 📈 Performance Metrics Monitoring -->## 📈 Performance Metrics Monitoring

## Application Metrics Collection

## 1. Micrometer Integration
```yaml
# Spring Boot Application Metrics Configuration
management:
  endpoints:
    web:
      exposure:
        include: health,info,metrics,prometheus
  metrics:
    export:
      prometheus:
        enabled: true
    distribution:
      percentiles-histogram:
        http.server.requests: true
      slo:
        http.server.requests: 100ms, 200ms, 500ms
    tags:
      application: ${spring.application.name}
      environment: ${spring.profiles.active}
```

## 2. Custom Business Metrics
```java
// Custom Business Metrics
@Component
public class BusinessMetrics {
    
    private final MeterRegistry meterRegistry;
    private final Counter orderCounter;
    private final Timer orderProcessingTimer;
    private final Gauge activeUsersGauge;
    
    public BusinessMetrics(MeterRegistry meterRegistry) {
        this.meterRegistry = meterRegistry;
        
        // Order counter
        orderCounter = Counter.builder("business.orders.total")
            .description("Total number of orders")
            .tags("type", "ecommerce")
            .register(meterRegistry);
            
        // Order processing time
        orderProcessingTimer = Timer.builder("business.order.processing")
            .description("Order processing time")
            .publishPercentileHistogram()
            .sla(Duration.ofMillis(100), Duration.ofMillis(200))
            .register(meterRegistry);
            
        // Active user count
        activeUsersGauge = Gauge.builder("business.users.active")
            .description("Number of active users")
            .register(meterRegistry, this, BusinessMetrics::getActiveUserCount);
    }
    
    public void recordOrder(String orderType) {
        orderCounter.increment();
        meterRegistry.counter("business.orders.by_type", "type", orderType).increment();
    }
    
    public Sample startOrderProcessing() {
        return Timer.start(meterRegistry);
    }
    
    public void recordOrderProcessing(Sample sample) {
        sample.stop(orderProcessingTimer);
    }
}
```

## Database Performance Monitoring

## 1. Database Connection Pool Monitoring
```yaml
# HikariCP Monitoring Configuration
spring:
  datasource:
    hikari:
      pool-name: app-pool
      register-mbeans: true
      metrics-tracker-factory: com.zaxxer.hikari.metrics.prometheus.PrometheusMetricsTrackerFactory
      
management:
  metrics:
    export:
      prometheus:
        descriptions: true
```

## 2. SQL Execution Monitoring
```java
// SQL Execution Monitoring Aspect
@Aspect
@Component
public class SqlMonitoringAspect {
    
    private final Timer sqlTimer;
    private final Counter sqlErrorCounter;
    
    public SqlMonitoringAspect(MeterRegistry meterRegistry) {
        sqlTimer = Timer.builder("database.sql.execution")
            .description("SQL execution time")
            .publishPercentileHistogram()
            .register(meterRegistry);
            
        sqlErrorCounter = Counter.builder("database.sql.errors")
            .description("SQL execution errors")
            .register(meterRegistry);
    }
    
    @Around("@annotation(org.springframework.transaction.annotation.Transactional)")
    public Object monitorSqlExecution(ProceedingJoinPoint joinPoint) throws Throwable {
        Timer.Sample sample = Timer.start(sqlTimer);
        
        try {
            return joinPoint.proceed();
        } catch (Exception e) {
            sqlErrorCounter.increment();
            throw e;
        } finally {
            sample.stop(sqlTimer);
        }
    }
}
```

<!-- chunk: 🔍 Exception Monitoring and Alerting -->## 🔍 Exception Monitoring and Alerting

## Error Tracing Configuration

## 1. Sentry Integration
```yaml
# Sentry Configuration
sentry:
  dsn: ${SENTRY_DSN}
  environment: ${SPRING_PROFILES_ACTIVE}
  release: ${APP_VERSION}
  traces-sample-rate: 1.0
  enable-tracing: true
  logging:
    minimum-breadcrumb-level: INFO
    minimum-event-level: ERROR
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sentry-relay
  namespace: observability
spec:
  replicas: 2
  selector:
    matchLabels:
      app: sentry-relay
  template:
    metadata:
      labels:
        app: sentry-relay
    spec:
      containers:
      - name: relay
        image: getsentry/relay:23.1.1
        ports:
        - containerPort: 3000
        env:
        - name: SENTRY_RELAY_MODE
          value: "managed"
        - name: SENTRY_RELAY_UPSTREAM
          value: "https://sentry.io/"
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 512Mi
```

## 2. Exception Metric Alerts
```yaml
# Exception Monitoring Alert Rules
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: application-error-alerts
  namespace: monitoring
spec:
  groups:
  - name: application.rules
    rules:
    - alert: HighErrorRate
      expr: sum(rate(http_server_requests_seconds_count{status=~"5.."}[5m])) by (job) / sum(rate(http_server_requests_seconds_count[5m])) by (job) > 0.05
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "High error rate detected in {{ $labels.job }}"
        
    - alert: DatabaseConnectionErrors
      expr: rate(database_connection_errors_total[5m]) > 1
      for: 2m
      labels:
        severity: critical
      annotations:
        summary: "Database connection errors in {{ $labels.job }}"
        
    - alert: SlowAPIResponse
      expr: histogram_quantile(0.95, rate(http_server_requests_seconds_bucket{uri!~"/health|/metrics"}[5m])) > 2
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "Slow API response time in {{ $labels.job }}"
```

<!-- chunk: 🎨 Visualization Display -->## 🎨 Visualization Display

## Grafana Dashboards

## 1. Application Performance Overview
```json
{
  "dashboard": {
    "title": "Application Performance Overview",
    "panels": [
      {
        "title": "Request Rate and Error Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(rate(http_server_requests_seconds_count[5m])) by (job)",
            "legendFormat": "{{job}} - Total"
          },
          {
            "expr": "sum(rate(http_server_requests_seconds_count{status=~\"5..\"}[5m])) by (job)",
            "legendFormat": "{{job}} - Errors"
          }
        ]
      },
      {
        "title": "Response Time Distribution",
        "type": "heatmap",
        "targets": [
          {
            "expr": "histogram_quantile(0.5, rate(http_server_requests_seconds_bucket[5m]))",
            "legendFormat": "p50"
          },
          {
            "expr": "histogram_quantile(0.95, rate(http_server_requests_seconds_bucket[5m]))",
            "legendFormat": "p95"
          },
          {
            "expr": "histogram_quantile(0.99, rate(http_server_requests_seconds_bucket[5m]))",
            "legendFormat": "p99"
          }
        ]
      },
      {
        "title": "Database Connection Pool",
        "type": "graph",
        "targets": [
          {
            "expr": "hikaricp_connections_active",
            "legendFormat": "Active Connections"
          },
          {
            "expr": "hikaricp_connections_idle",
            "legendFormat": "Idle Connections"
          },
          {
            "expr": "hikaricp_connections_pending",
            "legendFormat": "Pending Connections"
          }
        ]
      }
    ]
  }
}
```

## 2. Business Metrics Dashboard
```json
{
  "dashboard": {
    "title": "Business Metrics Dashboard",
    "panels": [
      {
        "title": "Order Processing Metrics",
        "type": "graph",
        "targets": [
          {
            "expr": "business_orders_total",
            "legendFormat": "Total Orders"
          },
          {
            "expr": "rate(business_orders_total[5m])",
            "legendFormat": "Orders per Second"
          }
        ]
      },
      {
        "title": "User Activity",
        "type": "stat",
        "targets": [
          {
            "expr": "business_users_active",
            "legendFormat": "Active Users"
          },
          {
            "expr": "increase(business_user_sessions_total[1h])",
            "legendFormat": "Sessions (Last Hour)"
          }
        ]
      }
    ]
  }
}
```

<!-- chunk: 🔧 Performance Tuning -->## 🔧 Performance Tuning

## Application Performance Optimization

## 1. JVM Performance Monitoring
```yaml
# JVM Monitoring Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: jvm-monitoring
  namespace: production
data:
  jvm-exporter.yaml: |
    lowercaseOutputName: true
    lowercaseOutputLabelNames: true
    rules:
    - pattern: 'java.lang<type=OperatingSystem><>(FreePhysicalMemorySize|TotalPhysicalMemorySize|FreeSwapSpaceSize|TotalSwapSpaceSize|SystemCpuLoad|ProcessCpuLoad|OpenFileDescriptorCount|MaxFileDescriptorCount)'
      name: os_$1
      type: GAUGE
      attrNameSnakeCase: true
    - pattern: 'java.lang<type=Threading><>(TotalStartedThreadCount|ThreadCount)'
      name: jvm_threads_$1
      type: GAUGE
      attrNameSnakeCase: true
```

## 2. Cache Performance Monitoring
```java
// Redis Cache Monitoring
@Configuration
public class CacheMonitoringConfig {
    
    @Bean
    public CacheMetricsRegistrar cacheMetricsRegistrar(
            MeterRegistry meterRegistry,
            CacheManager cacheManager) {
        
        return new CacheMetricsRegistrar(meterRegistry, 
            Collections.singletonList(cacheManager));
    }
    
    @EventListener
    public void handleCacheStats(CacheStatisticsEvent event) {
        Cache cache = event.getCache();
        String cacheName = cache.getName();
        
        // Record cache hit ratio
        double hitRatio = (double) event.getHits() / 
            (event.getHits() + event.getMisses());
            
        meterRegistry.gauge("cache.hit.ratio", 
            Tags.of("cache", cacheName), hitRatio);
    }
}
```

<!-- chunk: 🛡️ Security and Compliance -->## 🛡️ Security and Compliance

## Data Privacy Protection

## 1. Sensitive Information Sanitization
```java
// Tracing Data Sanitization
@Component
public class TraceDataSanitizer {
    
    private static final Pattern EMAIL_PATTERN = 
        Pattern.compile("\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Z|a-z]{2,}\\b");
    
    private static final Pattern PHONE_PATTERN = 
        Pattern.compile("\\b\\d{3}-\\d{3}-\\d{4}\\b");
    
    public void sanitizeSpanAttributes(Span span) {
        Map<String, Object> tags = span.tags();
        
        // Sanitize email addresses
        tags.replaceAll((key, value) -> {
            if (value instanceof String) {
                String strValue = (String) value;
                strValue = EMAIL_PATTERN.matcher(strValue).replaceAll("[EMAIL]");
                strValue = PHONE_PATTERN.matcher(strValue).replaceAll("[PHONE]");
                return strValue;
            }
            return value;
        });
    }
}
```

## 2. Access Control Configuration
```yaml
# APM Tool Access Control
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: apm-access-control
  namespace: observability
spec:
  podSelector:
    matchLabels:
      app: jaeger
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: monitoring
    - podSelector:
        matchLabels:
          role: sre
    ports:
    - protocol: TCP
      port: 16686
```

<!-- chunk: 🔧 Implementation Checklist -->## 🔧 Implementation Checklist

## APM Platform Construction
- [ ] Select appropriate APM toolchain (OpenTelemetry/Jaeger/Tempo)
- [ ] Deploy distributed tracing infrastructure
- [ ] Integrate application performance metrics collection
- [ ] Configure exception monitoring and alerting mechanism
- [ ] Establish visualization monitoring dashboard
- [ ] Implement data sampling and storage strategy

## Application Integration
- [ ] Add tracing instrumentation in critical applications
- [ ] Configure business metrics collection
- [ ] Implement database and cache performance monitoring
- [ ] Integrate error tracking and reporting tools
- [ ] Configure security and privacy protection measures
- [ ] Establish performance baseline and thresholds

## Operations and Maintenance
- [ ] Establish APM platform operations standards
- [ ] Build performance issue troubleshooting process
- [ ] Regularly review and optimize monitoring configuration
- [ ] Maintain monitoring documentation and best practices
- [ ] Continuously improve monitoring coverage
- [ ] Establish performance optimization feedback mechanism

---

*This document provides comprehensive technical guidance for building enterprise-grade APM systems and application performance monitoring*

---

<!-- chunk: Obsidian Related Documentation -->## Obsidian Related Documentation

- domain-11-production-operations KUDIG Database — Global MOC
- [[domain-11-production-operations/README.md|Domain 11: Production Operations Best Practices]]
- Domain-18 Production Operations — Open Source Project Index
- [[domain-01-cluster-fundamentals/01-production-architecture-design-principles.md|01-Production Architecture Design Principles]]
- 02-Multi-Cloud Hybrid Deployment Strategy
- 03-Edge Computing Production Deployment
- 04-Enterprise Monitoring System
- 05-Log Collection and Analysis Platform
- 07-Zero Trust Security Architecture
- 08-CIS Benchmark Compliance Audit
- 09-Software Bill of Materials
- 10-GitOps Pipeline Practice

## See Also

- 04-enterprise-monitoring-system
- 05-logging-collection-analysis-platform
- 07-zero-trust-security-architecture
- 08-cis-benchmark-compliance-audit

- [[domain-06-observability/README.md|Back to index]]

## Related

- [[domain-19-landscape-references/topic-index/etcd-index.md|etcd Knowledge Graph Index]]


<!-- risk-assessed -->
