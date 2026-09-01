---
title: Deep Dive into Monitoring Metrics System
description: Deep dive into Prometheus monitoring system: metric types (Counter/Gauge/Histogram/Summary), PromQL queries, ServiceMonitor, Prometheus Operator, Alertmanager and alert rule configuration
summary: Deep dive into Prometheus monitoring system: metric types (Counter/Gauge/Histogram/Summary), PromQL queries, ServiceMonitor, Prometheus Operator, Alertmanager and alert rule configuration
category: domain-06-observability
tags:
- k8s
- prometheus
- metrics
- monitoring
- alertmanager
- promql
- servicemonitor
- etcd
- apiserver
- scheduler
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- DevOps Engineer
- Monitoring Engineer
estimated_read_time: 5min
intent_queries:
- What is deep dive into monitoring metrics system
- How to implement monitoring metrics system
- Kubernetes observability best practices
trigger_keywords:
- monitoring metrics system
- observability
prerequisites:
- kubectl-basics
- observability-basics
- prometheus-basics
- monitoring-basics
- etcd-basics
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
  label: 'Related domain: domain-01-cluster-fundamentals'
- type: domain
  path: ../domain-02-workloads-applications/
  label: 'Related domain: domain-02-workloads-applications'
- type: domain
  path: ../domain-03-networking-traffic/
  label: 'Related domain: domain-03-networking-traffic'
- type: domain
  path: ../domain-07-platform-engineering/
  label: 'Related domain: domain-07-platform-engineering'
- type: fta
  path: ../domain-10-troubleshooting-diagnostics/topic-fta/list/monitoring-fta.md
  label: 'Fault tree: monitoring'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/promql.md
  label: 'Cheat sheet: promql'
related_docs:
- path: 01-observability-architecture-overview.md
  type: depth
  desc: Observability architecture system
- path: 04-distributed-tracing.md
  type: depth
  desc: Distributed tracing system
- path: ../domain-17-system-foundation/topic-cheat-sheet/promql.md
  type: cheatsheet
  desc: PromQL cheat sheet
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/02-metrics/02-monitoring-metrics-system.md
---

> **Production Environment Security Notice**
>
> This document contains operational commands that can be executed directly. Before execution, ensure: the current target cluster and namespace are correct; sufficient RBAC permissions are available; validation has been completed in non-production environments. Command risk levels: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state but usually can be rolled back), 🟢 Low risk/read-only (information collection, no side effects).




# 02 - Deep Dive into Monitoring Metrics System

> **Applicable Versions**: v1.25 - v1.32 | **Last Updated**: 2026-01 | **Reference**: [[entities/prometheus.md|prometheus]].io/docs](https://prometheus.io/docs/)

<!-- chunk: Overview -->
## Overview

This document provides an in-depth analysis of the Kubernetes metrics monitoring system, covering the Prometheus ecosystem, core component metrics, custom metric extensions, alert rule design, and other key content, providing complete guidance for building production-grade monitoring systems.

---

<!-- chunk: One, Prometheus Monitoring Architecture -->
## One, Prometheus Monitoring Architecture

### 1.1 Core Component Architecture

#### Prometheus Ecosystem Components
```yaml
prometheus_ecosystem:
  core_components:
    prometheus_server:
      function: Data collection, storage, query engine
      features:
        - pull_based_scraping
        - tsdb_storage
        - promql_query_language
        - http_api
        
    alertmanager:
      function: Alert routing, deduplication, suppression
      features:
        - receiver_routing
        - silencing
        - inhibition_rules
        - high_availability
        
    pushgateway:
      function: Metric push for short-lived jobs
      use_cases:
        - cron_jobs
        - batch_processes
        - ci_cd_pipelines
        
  kubernetes_operators:
    prometheus_operator:
      function: Prometheus instance lifecycle management
      crds:
        - prometheus
        - servicemonitor
        - podmonitor
        - prometheusrule
        - alertmanagerconfig
        
    kube_prometheus_stack:
      function: Complete monitoring stack deployment
      components:
        - prometheus_operator
        - prometheus
        - alertmanager
        - grafana
        - node_exporter
        - kube_state_metrics
```

### 1.2 High Availability Deployment Architecture

#### Prometheus HA Approach
```yaml
prometheus_ha_deployment:
  # Approach 1: Thanos Architecture
  thanos_approach:
    components:
      - prometheus_with_thanos_sidecar
      - thanos_querier
      - thanos_store_gateway
      - thanos_compactor
      - thanos_ruler
      
    advantages:
      - Global query view
      - Long-term storage support
      - No single point of failure
      - Horizontal scaling capability
      
  # Approach 2: Federation Architecture
  federation_approach:
    levels:
      - leaf_prometheus: Regional monitoring
      - global_prometheus: Global aggregation
      
    configuration:
      leaf_config: |
        global:
          external_labels:
            region: cn-beijing
            replica: "$(HOSTNAME)"
            
      global_config: |
        scrape_configs:
        - job_name: federate
          scrape_interval: 15s
          honor_labels: true
          metrics_path: /federate
          params:
            'match[]':
              - '{job=~"kubernetes-.*"}'
              - '{__name__=~"job:.*"}'
```

---

<!-- chunk: Two, Core Component Monitoring Metrics -->
## Two, Core Component Monitoring Metrics

### 2.1 API Server Key Metrics

#### API Server Performance Metrics
| Metric Name | Type | Description | Alert Threshold | Operations Scenario |
|---------|------|------|---------|---------|
| `apiserver_request_total` | Counter | Total API requests (grouped by verb/resource/code) | 5xx error rate > 1% | Monitor API health |
| `apiserver_request_duration_seconds` | Histogram | API request latency | P99 > 1s | Performance troubleshooting |
| `apiserver_current_inflight_requests` | Gauge | Current in-flight request count | > 80% limit | Overload detection |
| `apiserver_longrunning_requests` | Gauge | Long-running request count (watch, etc.) | Abnormal growth | Watch leak detection |
| `apiserver_request_terminations_total` | Counter | Request termination count | Rapid increase | Timeout issues |
| `apiserver_audit_event_total` | Counter | Audit event count | - | Audit monitoring |
| `apiserver_storage_objects` | Gauge | etcd object count (by resource) | Approaching quota | Storage capacity |

#### API Server Monitoring Configuration
```yaml
# ServiceMonitor Configuration
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: kube-apiserver
  namespace: monitoring
spec:
  endpoints:
  - bearerTokenFile: /var/run/secrets/kubernetes.io/serviceaccount/token
    interval: 30s
    metricRelabelings:
    - action: keep
      regex: apiserver_request_(latency|count|duration)|etcd_(server|disk|network)
      sourceLabels:
      - __name__
    port: https
    scheme: https
    tlsConfig:
      caFile: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
      serverName: kubernetes
  jobLabel: component
  namespaceSelector:
    matchNames:
    - default
  selector:
    matchLabels:
      component: apiserver
      provider: kubernetes
```

### 2.2 etcd Key Metrics

#### etcd Stability Metrics
| Metric Name | Type | Description | Alert Threshold | Operations Scenario |
|---------|------|------|---------|---------|
| `etcd_server_has_leader` | Gauge | Has leader or not | =0 | Cluster health |
| `etcd_server_leader_changes_seen_total` | Counter | Leader change count | > 3/h | Stability issues |
| `etcd_disk_wal_fsync_duration_seconds` | Histogram | WAL sync latency | P99 > 10ms | Disk performance |
| `etcd_disk_backend_commit_duration_seconds` | Histogram | Backend commit latency | P99 > 25ms | Disk performance |
| `etcd_mvcc_db_total_size_in_bytes` | Gauge | Database size | > 80% quota | Storage capacity |
| `etcd_network_peer_round_trip_time_seconds` | Histogram | Peer node RTT | P99 > 100ms | Network issues |
| `etcd_server_proposals_failed_total` | Counter | Failed proposal count | > 0 continuously | Raft issues |

#### etcd Monitoring Best Practices
```yaml
# etcd Monitoring Configuration
apiVersion: monitoring.coreos.com/v1
kind: PodMonitor
metadata:
  name: etcd
  namespace: monitoring
spec:
  podMetricsEndpoints:
  - bearerTokenFile: /var/run/secrets/kubernetes.io/serviceaccount/token
    interval: 15s
    metricRelabelings:
    - action: keep
      regex: etcd_(server|disk|network|mvcc)
      sourceLabels:
      - __name__
    port: metrics
    scheme: https
    tlsConfig:
      ca:
        secret:
          key: etcd-ca.crt
          name: etcd-client-tls
      cert:
        secret:
          key: etcd-client.crt
          name: etcd-client-tls
      keySecret:
        key: etcd-client.key
        name: etcd-client-tls
  selector:
    matchLabels:
      component: etcd
```

### 2.3 Scheduler Key Metrics

#### Scheduler Performance Metrics
| Metric Name | Type | Description | Alert Threshold | Operations Scenario |
|---------|------|------|---------|---------|
| `scheduler_pending_pods` | Gauge | Pending pod count (by queue) | > 100 continuously | Scheduling bottleneck |
| `scheduler_pod_scheduling_duration_seconds` | Histogram | Scheduling latency | P99 > 5s | Scheduling performance |
| `scheduler_schedule_attempts_total` | Counter | Scheduling attempt count (by result) | unschedulable increase | Resource shortage |
| `scheduler_preemption_attempts_total` | Counter | Preemption attempt count | Continuous increase | Resource contention |
| `scheduler_framework_extension_point_duration_seconds` | Histogram | Plugin execution time | P99 > 50ms | Plugin performance |

---

<!-- chunk: Three, Custom Metric Extension -->
## Three, Custom Metric Extension

### 3.1 Application Metrics

#### Application Metric Exposure Methods
```yaml
# Application Prometheus Configuration
application_metrics_setup:
  # 1. Application exposes metrics endpoint
  metrics_endpoint: /metrics
  port: 8080
  
  # 2. ServiceMonitor Configuration
  service_monitor:
    apiVersion: monitoring.coreos.com/v1
    kind: ServiceMonitor
    metadata:
      name: app-metrics
      namespace: monitoring
    spec:
      endpoints:
      - interval: 30s
        path: /metrics
        port: http-metrics
      selector:
        matchLabels:
          app: my-application
          
  # 3. Sample Application Metrics
  sample_metrics:
    http_requests_total:
      type: Counter
      help: Total number of HTTP requests
      
    http_request_duration_seconds:
      type: Histogram
      help: HTTP request latencies in seconds
      
    current_users:
      type: Gauge
      help: Current number of active users
```

### 3.2 Custom Exporter Development

#### Exporter Development Template
```go
// Go Language Exporter Example
package main

import (
    "net/http"
    "github.com/prometheus/client_golang/prometheus"
    "github.com/prometheus/client_golang/prometheus/promhttp"
)

var (
    httpRequestTotal = prometheus.NewCounterVec(
        prometheus.CounterOpts{
            Name: "http_requests_total",
            Help: "Total number of HTTP requests",
        },
        []string{"method", "endpoint", "status"},
    )
    
    httpRequestDuration = prometheus.NewHistogramVec(
        prometheus.HistogramOpts{
            Name:    "http_request_duration_seconds",
            Help:    "HTTP request latencies in seconds",
            Buckets: prometheus.DefBuckets,
        },
        []string{"method", "endpoint"},
    )
)

func init() {
    prometheus.MustRegister(httpRequestTotal)
    prometheus.MustRegister(httpRequestDuration)
}

func metricsMiddleware(next http.Handler) http.Handler {
    return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
        start := time.Now()
        
        // Execute original handler
        next.ServeHTTP(w, r)
        
        // Record metrics
        duration := time.Since(start).Seconds()
        httpRequestTotal.WithLabelValues(r.Method, r.URL.Path, "200").Inc()
        httpRequestDuration.WithLabelValues(r.Method, r.URL.Path).Observe(duration)
    })
}
```

---

<!-- chunk: Four, Alert Rule System -->
## Four, Alert Rule System

### 4.1 Alert Rule Classification

#### Hierarchical Alert Strategy
```yaml
alert_categories:
  infrastructure_alerts:
    critical:
      - KubeAPIServerDown
      - EtcdNoLeader
      - NodeNotReady
    warning:
      - EtcdHighFsyncDuration
      - KubeSchedulerPendingPods
      - NodeMemoryPressure
      
  application_alerts:
    critical:
      - PodCrashLooping
      - DeploymentReplicasMismatch
      - PersistentVolumeClaimPending
    warning:
      - HighErrorRate
      - HighLatency
      - LowSuccessRate
      
  business_alerts:
    critical:
      - BusinessTransactionFailure
      - RevenueImpactAlert
    warning:
      - SLAViolation
      - PerformanceDegradation
```

### 4.2 Production-Grade Alert Rules

#### Core Alert Rule Set
```yaml
# PrometheusRule Configuration
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: kubernetes-rules
  namespace: monitoring
spec:
  groups:
  - name: kubernetes-system
    rules:
    # === Critical Alerts ===
    - alert: KubeAPIServerDown
      expr: absent(up{job="kubernetes-apiservers"} == 1)
      for: 5m
      labels:
        severity: critical
        category: infrastructure
      annotations:
        summary: "Kubernetes API Server is down"
        description: "API Server has been unreachable for more than 5 minutes"
        
    - alert: EtcdNoLeader
      expr: etcd_server_has_leader == 0
      for: 1m
      labels:
        severity: critical
        category: infrastructure
      annotations:
        summary: "etcd has no leader"
        description: "etcd cluster has lost quorum"
        
    # === Warning Alerts ===
    - alert: KubeSchedulerPendingPods
      expr: scheduler_pending_pods{queue="active"} > 100
      for: 10m
      labels:
        severity: warning
        category: infrastructure
      annotations:
        summary: "Too many pending pods"
        description: "{{ $value }} pods are pending scheduling"
        
    - alert: NodeMemoryPressure
      expr: (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) > 0.9
      for: 5m
      labels:
        severity: warning
        category: infrastructure
      annotations:
        summary: "Node {{ $labels.instance }} memory pressure"
        description: "Memory usage is above 90%"
        
    # === Application Alerts ===
    - alert: PodRestartingTooMuch
      expr: increase(kube_pod_container_status_restarts_total[1h]) > 5
      for: 5m
      labels:
        severity: warning
        category: application
      annotations:
        summary: "Pod {{ $labels.namespace }}/{{ $labels.pod }} restarting frequently"
        description: "Pod has restarted {{ $value }} times in the last hour"
```

### 4.3 Alert Suppression and Deduplication

#### Alert Management Strategy
```yaml
alertmanager_config:
  global:
    resolve_timeout: 5m
    
  route:
    group_by: ['alertname', 'cluster']
    group_wait: 30s
    group_interval: 5m
    repeat_interval: 3h
    receiver: 'default-receiver'
    
  inhibit_rules:
    # When node is down, suppress all alerts on that node
    - source_matchers:
      - alertname="NodeNotReady"
      - target_match=""
      - alertname="PodNotReady"
      - equal="['node']"
    # When API Server is down, suppress all related alerts
    - source_matchers:
      - alertname="KubeAPIServerDown"
      - target_match_re=""
      - alertname="^(Kube|Etcd).*"
  receivers:
    - name: 'default-receiver'
      email_configs:
      - to: 'alerts@example.com'
        send_resolved: true
      webhook_configs:
      - url: 'http://alert-gateway:8080/webhook'
```

---

<!-- chunk: Five, Performance Optimization and Tuning -->
## Five, Performance Optimization and Tuning

### 5.1 Prometheus Performance Tuning

#### Storage and Query Optimization
```yaml
prometheus_optimization:
  storage_tuning:
    # TSDB Configuration Optimization
    tsdb_config:
      retention.time: 15d
      retention.size: "50GB"
      wal-compression: true
      max-block-duration: 2h
      min-block-duration: 2h
      
    # Resource Limits
    resources:
      requests:
        memory: 4Gi
        cpu: 2
      limits:
        memory: 8Gi
        cpu: 4
        
  scrape_optimization:
    # Scrape Configuration Optimization
    scrape_configs:
      - job_name: 'kubernetes-nodes'
        scrape_interval: 30s
        scrape_timeout: 10s
        sample_limit: 5000
        metric_relabel_configs:
        - source_labels: [__name__]
          regex: '(go_|process_).*'
          action: drop
          
  query_optimization:
    # Query Performance Optimization
    query_config:
      lookback-delta: 5m
      max-concurrency: 20
      timeout: 2m
      max-samples: 50000000
```

### 5.2 Long-Term Storage Solution

#### Thanos Long-Term Storage Configuration
```yaml
thanos_components:
  # Sidecar Configuration
  sidecar:
    args:
      - sidecar
      - --prometheus.url=http://localhost:9090
      - --objstore.config-file=/etc/thanos/objstore.yml
      - --tsdb.path=/prometheus
      - --reloader.config-file=/etc/prometheus/prometheus.yml
      
  # Store Gateway Configuration
  store_gateway:
    args:
      - store
      - --data-dir=/data
      - --objstore.config-file=/etc/thanos/objstore.yml
      - --index-cache-size=500MB
      - --chunk-pool-size=2GB
      
  # Compactor Configuration
  compactor:
    args:
      - compact
      - --data-dir=/data
      - --objstore.config-file=/etc/thanos/objstore.yml
      - --retention.resolution-raw=30d
      - --retention.resolution-5m=120d
      - --retention.resolution-1h=1y
```

---

<!-- chunk: Six, Monitoring Maturity Model -->
## Six, Monitoring Maturity Model

### 6.1 Monitoring Maturity Levels

#### Five Maturity Levels
```
Monitoring Maturity Levels:

Level 1 - Basic Monitoring
├── Core component state monitoring
├── Basic alert configuration
├── Simple dashboard display
└── Manual troubleshooting

Level 2 - Standard Monitoring
├── Comprehensive metric collection
├── Automated alerting
├── Rich visualization
├── Standardized monitoring processes
└── Basic performance analysis

Level 3 - Advanced Monitoring
├── Intelligent alert strategy
├── Predictive analysis
├── Automated diagnostics
├── Cost optimization monitoring
└── User experience monitoring

Level 4 - Intelligent Monitoring
├── AI-driven anomaly detection
├── Adaptive threshold setting
├── Automated root cause analysis
├── Intelligent capacity planning
└── Business impact assessment

Level 5 - Autonomous Operations
├── Fully automated operations
├── Preventive problem resolution
├── Dynamic resource optimization
├── Business continuity assurance
└── Continuous improvement mechanisms
```

### 6.2 Maturity Assessment Criteria

#### Assessment Metrics by Level
| Maturity Level | Key Metrics | Implementation Requirements | Value Benefits |
|-----------|---------|---------|---------|
| **Level 1** | 95% core component monitoring coverage | Basic Prometheus deployment | Basic stability assurance |
| **Level 2** | 99% monitoring coverage, < 5 minute MTTD | Complete monitoring stack | Proactive problem discovery |
| **Level 3** | Intelligent alerts, predictive maintenance | ML-assisted analysis | Reduce problem impact |
| **Level 4** | Automated root cause analysis, adaptive thresholds | AI/ML deep integration | Improve operations efficiency |
| **Level 5** | Autonomous operations, business-driven optimization | Full automation | Maximize business value |

---

**Monitoring Philosophy**: From "reactive response" to "proactive prevention", from "local visibility" to "global insights", from "manual control" to "intelligent automation"

---

**Implementation Recommendation**: Progress gradually, first ensure basic monitoring is complete, then gradually improve intelligence level

---

**Table Maintenance**: Kusheet Project | **Author**: Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian Related Documentation -->
## Obsidian Related Documentation

- observability/MOC.md|domain-06-observability MOC]]
- [[domain-06-observability/README.md|Observability Domain]]
- [[domain-06-observability/00-open-source-projects-index.md|Domain-6 Observability — Open Source Projects Index]]
- Kubernetes Observability Architecture System
- 03 - Logging Architecture (Logging Architecture)
- Distributed Tracing System
- 05 - Alert Management Strategy (Alerting Management)
- 06 - Monitoring Alerting Practice and Best Practices (Monitoring Alerting Practice)
- 04 - Monitoring Dashboard Design and Best Practices (Monitoring Dashboards)
- 08 - Logging Audit and Compliance Management (Logging Auditing & Compliance)
- 05 - Events and Audit Log Management (Events & Audit Logs)
- 07 - Monitoring and Metrics Tables

## Related

- [[concepts/Operator Pattern × Observability.md|Operator Pattern × Observability]]

- Observability Architecture System
- Distributed Tracing System
- [[domain-17-system-foundation/topic-cheat-sheet/promql.md|PromQL Cheat Sheet]]
- Related domain: domain-01-cluster-fundamentals
- Related domain: domain-02-workloads-applications
- Related domain: domain-03-networking-traffic
- Related domain: domain-07-platform-engineering
- [[domain-17-system-foundation/topic-cheat-sheet/promql.md|Cheat sheet: promql]]

- [[domain-06-observability/README.md|Back to index]]- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Map Index]]

## See Also

- UPDATED-QUALITY-REPORT
- 01-observability-architecture-overview
- 03-logging-architecture
- 04-distributed-tracing


<!-- risk-assessed -->
