---
title: 17 - Logging and Audit Tables
description: '# 17 - Logging and Audit Tables'
summary: 'kubectl get events -A --sort-by=.lastTimestamp'
category: observability
tags:
- k8s
- observability
- monitoring
- logging
- tracing
- apiserver
- kubelet
- scheduler
- controller-manager
- prometheus
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
- What is Logging and Audit Tables
- How to use Logging and Audit Tables
- Kubernetes observability best practices
trigger_keywords:
- Logging and Audit Tables
- observability
prerequisites:
- kubectl-basics
- observability-basics
- prometheus-basics
- monitoring-basics
- kafka-basics
- logging-basics
k8s_versions:
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
  path: ../domain-01-cluster-fundamentals/
  label: 'Related Domain: domain-01-cluster-fundamentals'
- type: domain
  path: ../domain-02-workloads-applications/
  label: 'Related Domain: domain-02-workloads-applications'
- type: domain
  path: ../domain-03-networking-traffic/
  label: 'Related Domain: domain-03-networking-traffic'
- type: domain
  path: ../domain-07-platform-engineering/
  label: 'Related Domain: domain-07-platform-engineering'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/promql.md
  label: 'Quick Reference: promql'
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/03-logging/12-logging-auditing.md
---

> **Production Environment Security Reminder**
>
> This document contains directly executable operations commands. Before executing, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have verified in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state but usually reversible), 🟢 Low risk/read-only (information gathering, no side effects).




# 17 - Logging and Audit Tables

> **Applicable Versions**: v1.25 - v1.32 | **Last Updated**: 2026-01 | **Reference**: [kubernetes.io/docs/concepts/cluster-administration/logging](https://kubernetes.io/docs/concepts/cluster-administration/logging/)

<!-- chunk: Logging Architecture Patterns -->
## Logging Architecture Patterns

| Pattern | Description | Advantages | Disadvantages | Use Cases |
|-----|------|------|------|---------|
| **Node-level Agent** | DaemonSet collects node logs | Low intrusion, unified management | Cannot collect container internal file logs | Standard stdout logs |
| **Sidecar Container** | Sidecar in Pod collects logs | Flexible, can handle file logs | Resource overhead | File logs, log preprocessing |
| **Direct Push** | Application sends directly to backend | Most flexible | Application coupling | Special format logs |

<!-- chunk: Logging Component Comparison -->
## Logging Component Comparison

| Component | Type | Features | Version Requirements | ACK Alternative |
|-----|------|------|---------|---------|
| **Fluentd** | Collector | Rich plugins, comprehensive functionality | v1.16+ | Logtail |
| **Fluent Bit** | Collector | Lightweight, high performance | v2.2+ | Logtail |
| **Filebeat** | Collector | Elastic ecosystem | v8.x | Logtail |
| **Logtail** | Collector | Alibaba Cloud native | - | Native |
| **Loki** | Storage/Query | Label indexing, low cost | v2.9+ | SLS |
| **Elasticsearch** | Storage/Query | Full-text indexing, powerful features | v8.x | SLS |
| **SLS** | Storage/Query | Alibaba Cloud native, no ops | - | Native |

<!-- chunk: Container Log Configuration -->
## Container Log Configuration

| Log Type | Path | Collection Method | Configuration Method |
|---------|------|---------|---------|
| **stdout/stderr** | /var/log/containers/*.log | Node agent automatic collection | Application output to standard output |
| **Container internal files** | Any path in container | Sidecar or volume mount | Configure volume + Sidecar |
| **emptyDir logs** | emptyDir volume path | Node agent mount and read | Volume mount to node agent |

```yaml
# Sidecar log collection example
apiVersion: v1
kind: Pod
metadata:
  name: app-with-logging
spec:
  containers:
  - name: app
    image: app:latest
    volumeMounts:
    - name: log-volume
      mountPath: /var/log/app
  - name: log-collector
    image: fluent/fluent-bit:latest
    volumeMounts:
    - name: log-volume
      mountPath: /var/log/app
      readOnly: true
    - name: fluent-bit-config
      mountPath: /fluent-bit/etc/
  volumes:
  - name: log-volume
    emptyDir: {}
  - name: fluent-bit-config
    configMap:
      name: fluent-bit-config
```

<!-- chunk: Kubernetes Audit Logs -->
## Kubernetes Audit Logs

| Audit Level | Recorded Content | Storage Impact | Use Cases |
|---------|---------|---------|---------|
| **None** | Do not record | None | Health checks, etc. |
| **Metadata** | Request metadata | Low | Most resources |
| **Request** | Metadata + request body | Medium | Sensitive resources |
| **RequestResponse** | Metadata + request + response | High | Critical audit |

<!-- chunk: Audit Policy Configuration -->
## Audit Policy Configuration

```yaml
# Audit policy example
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
  # Do not record read-only requests to certain resources
  - level: None
    resources:
    - group: ""
      resources: ["events"]
  
  # Do not record kubelet/kube-proxy watch requests
  - level: None
    users: ["system:kube-proxy", "system:kubelet"]
    verbs: ["watch"]
    resources:
    - group: ""
      resources: ["endpoints", "services", "services/status"]
  
  # Secret reads record Metadata
  - level: Metadata
    resources:
    - group: ""
      resources: ["secrets"]
  
  # Secret writes record Request
  - level: Request
    verbs: ["create", "update", "patch", "delete"]
    resources:
    - group: ""
      resources: ["secrets", "configmaps"]
  
  # Other resources record Metadata
  - level: Metadata
    omitStages:
    - "RequestReceived"
```

<!-- chunk: Audit Backend Configuration -->
## Audit Backend Configuration

| Backend Type | Configuration Parameter | Description | Version Support |
|---------|---------|------|---------|
| **Log File** | --audit-log-path | Write to local file | Stable |
| **Webhook** | --audit-webhook-config-file | Send to external service | Stable |
| **Dynamic Backend** | --audit-dynamic-configuration | Dynamic configuration (deprecated) | Deprecated |

```bash
# API Server audit parameters
--audit-log-path=/var/log/kubernetes/audit.log
--audit-log-maxage=30
--audit-log-maxbackup=10
--audit-log-maxsize=100
--audit-policy-file=/etc/kubernetes/audit-policy.yaml
```

<!-- chunk: Event API -->
## Event API

| Resource | Purpose | Retention Time | Version Support |
|-----|------|---------|---------|
| **events.k8s.io/v1** | New Event API | Configurable | v1.19+ GA |
| **core/v1 Event** | Old Event | 1 hour default | Stable |

``` bash
# 🟢 Low risk: read-only/information gathering, usually no side effects
# View events
kubectl get events -A --sort-by='.lastTimestamp'
kubectl events --for pod/<name>  # v1.26+
kubectl get events --field-selector=type=Warning

# Event retention configuration (API Server)
--event-ttl=1h
```
<!-- chunk: Structured Logging (v1.19+) -->
## Structured Logging (v1.19+)

| Feature | Description | Version Support |
|-----|------|---------|
| **JSON Format** | Component logs output JSON | v1.19+ |
| **Log Level** | -v flag controls verbosity | Stable |
| **Log Cleanup** | Automatic rotation | Component configuration |

```bash
# Enable JSON logging (kubelet example)
--logging-format=json
--log-json-info-buffer-size=0
--log-json-split-stream=true

# Log levels
-v=0  # Minimal output
-v=2  # Useful steady state information
-v=4  # Debug level
-v=6  # API request/response
-v=8  # Verbose debug
```

<!-- chunk: Log Aggregation Best Practices -->
## Log Aggregation Best Practices

| Practice | Description | Tool |
|-----|------|------|
| **Structured Logging** | JSON format for easy parsing | Application configuration |
| **Unified Timestamp** | UTC or unified timezone | Application configuration |
| **Correlation ID** | Trace request chains | OpenTelemetry |
| **Log Leveling** | Filter by level | Application framework |
| **Sampling** | Sample high-traffic logs | Fluent Bit |
| **Retention Policy** | Set retention as needed | Storage system |

<!-- chunk: ACK Log Integration -->
## ACK Log Integration

| Feature | Product | Configuration Method |
|-----|------|---------|
| **Container Logs** | SLS | Logtail DaemonSet |
| **K8S Events** | SLS | Console enable |
| **Audit Logs** | SLS | Console enable |
| **Ingress Logs** | SLS | Annotation configuration |
| **Application Tracing** | ARMS | Agent injection |

```yaml
# ACK Logtail configuration
apiVersion: log.alibabacloud.com/v1alpha1
kind: AliyunLogConfig
metadata:
  name: app-logs
spec:
  project: my-project
  logstore: app-logs
  shardCount: 2
  lifeCycle: 30
  logtailConfig:
    inputType: plugin
    configName: app-logs
    inputDetail:
      plugin:
        inputs:
        - type: service_docker_stdout
          detail:
            Stdout: true
            Stderr: true
            IncludeLabel:
              app: myapp
        processors:
        - type: processor_json
          detail:
            SourceKey: content
            KeepSource: false
```

<!-- chunk: Log Alert Rules -->
## Log Alert Rules

| Alert Type | Log Pattern | Alert Condition |
|---------|---------|---------|
| **Application Error** | ERROR/FATAL keywords | >10/min |
| **Pod Restart** | Event: BackOff | >3 times/hour |
| **Node Issue** | Event: NodeNotReady | Any occurrence |
| **OOM** | OOMKilled | Any occurrence |
| **Security Event** | Audit log specific operations | Any occurrence |

<!-- chunk: Compliance Audit Requirements -->
## Compliance Audit Requirements

| Compliance Standard | Log Requirements | Retention Period |
|---------|---------|-------|
| **PCI-DSS** | Access logs, security events | 1 year |
| **SOC2** | System logs, audit logs | 1 year |
| **等保2.0** | Comprehensive logging | 6 months |
| **GDPR** | Data access logs | As required |

# 17 - Logging and Audit Tables

> **Applicable Versions**: v1.25 - v1.32 | **Last Updated**: 2026-01 | **Reference**: [kubernetes.io/docs/concepts/cluster-administration/logging](https://kubernetes.io/docs/concepts/cluster-administration/logging/)

(Supplementing original content)

<!-- chunk: Production-Grade Logging Architecture -->
## Production-Grade Logging Architecture

### Logging Hierarchy Architecture

```
Application-Level Logs
    ├─ Business logs (stdout)
    ├─ Access logs (access.log)
    └─ Error logs (error.log)
          ↓
Container Runtime
    ├─ Docker/Containerd log driver
    └─ Log files (/var/log/containers/*.log)
          ↓
Collection Layer
    ├─ DaemonSet collector (Filebeat/Fluentd/Logtail)
    └─ Sidecar collector
          ↓
Transport Layer
    ├─ Log queue (Kafka)
    └─ Direct transmission
          ↓
Storage Layer
    ├─ Elasticsearch/Loki/SLS
    └─ Object storage archiving
          ↓
Analysis Layer
    ├─ Kibana/Grafana query
    ├─ Alert rules
    └─ Report analysis
```

<!-- chunk: Structured Logging Best Practices -->
## Structured Logging Best Practices

### Recommended Log Format

```json
{
  "timestamp": "2026-01-18T10:30:00.123Z",
  "level": "ERROR",
  "service": "user-api",
  "trace_id": "abc123def456",
  "span_id": "span789",
  "user_id": "12345",
  "method": "POST",
  "path": "/api/users",
  "status": 500,
  "duration_ms": 234,
  "error": "Database connection timeout",
  "stack_trace": "...",
  "kubernetes": {
    "namespace": "production",
    "pod": "user-api-7d4f5b8c9-xk2p4",
    "container": "app",
    "node": "node-1"
  }
}
```

### Application Log Library Configuration

```yaml
# Java Logback configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: logback-config
data:
  logback.xml: |
    <configuration>
      <appender name="JSON" class="ch.qos.logback.core.ConsoleAppender">
        <encoder class="net.logstash.logback.encoder.LogstashEncoder">
          <customFields>{"service":"user-api"}</customFields>
        </encoder>
      </appender>
      <root level="INFO">
        <appender-ref ref="JSON" />
      </root>
    </configuration>
```

<!-- chunk: Advanced Log Collection Configuration -->
## Advanced Log Collection Configuration

### Fluent Bit Production Configuration

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluent-bit-config
  namespace: logging
data:
  fluent-bit.conf: |
    [SERVICE]
        Flush         5
        Daemon        off
        Log_Level     info
        Parsers_File  parsers.conf
    
    [INPUT]
        Name              tail
        Path              /var/log/containers/*.log
        Parser            docker
        Tag               kube.*
        Refresh_Interval  5
        Mem_Buf_Limit     50MB
        Skip_Long_Lines   On
    
    [FILTER]
        Name                kubernetes
        Match               kube.*
        Kube_URL            https://kubernetes.default.svc:443
        Kube_CA_File        /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        Kube_Token_File     /var/run/secrets/kubernetes.io/serviceaccount/token
        Kube_Tag_Prefix     kube.var.log.containers.
        Merge_Log           On
        Keep_Log            Off
        K8S-Logging.Parser  On
        K8S-Logging.Exclude On
    
    [FILTER]
        Name    modify
        Match   kube.*
        Add     cluster_name prod-cluster
        Add     region cn-hangzhou
    
    [OUTPUT]
        Name  es
        Match kube.*
        Host  elasticsearch.logging.svc.cluster.local
        Port  9200
        Index k8s-logs
        Type  _doc
        Logstash_Format On
        Logstash_Prefix k8s
        Retry_Limit 5
        
    [OUTPUT]
        Name  sls
        Match kube.*
        Region cn-hangzhou
        Project k8s-logs
        Logstore app-logs
```

<!-- chunk: Complete Audit Log Configuration -->
## Complete Audit Log Configuration

### Production-Grade Audit Policy

```yaml
apiVersion: audit.k8s.io/v1
kind: Policy
omitStages:
  - "RequestReceived"
rules:
  # === Requests not to record ===
  # 1. Read-only requests to non-sensitive resources
  - level: None
    verbs: ["get", "list", "watch"]
    resources:
    - group: ""
      resources: ["events", "nodes/status", "pods/log", "pods/status"]
  
  # 2. System components health checks
  - level: None
    users: ["system:kube-proxy", "system:kube-controller-manager", "system:kube-scheduler"]
    verbs: ["get"]
    resources:
    - group: ""
      resources: ["endpoints", "services"]
  
  # === RequestResponse level (most detailed) ===
  # 1. All Secret operations
  - level: RequestResponse
    resources:
    - group: ""
      resources: ["secrets"]
  
  # 2. Delete operations
  - level: RequestResponse
    verbs: ["delete", "deletecollection"]
  
  # 3. Privileged operations
  - level: RequestResponse
    verbs: ["create", "update", "patch"]
    resources:
    - group: ""
      resources: ["serviceaccounts", "pods/exec", "pods/attach", "pods/portforward"]
    - group: "rbac.authorization.k8s.io"
      resources: ["clusterroles", "clusterrolebindings", "roles", "rolebindings"]
  
  # === Request level ===
  # ConfigMap write operations
  - level: Request
    verbs: ["create", "update", "patch", "delete"]
    resources:
    - group: ""
      resources: ["configmaps"]
  
  # === Metadata level (default) ===
  # All other resources
  - level: Metadata
```

### API Server Audit Configuration

```bash
# /etc/kubernetes/manifests/kube-apiserver.yaml
spec:
  containers:
  - command:
    - kube-apiserver
    # Audit log configuration
    - --audit-policy-file=/etc/kubernetes/audit-policy.yaml
    - --audit-log-path=/var/log/kubernetes/audit.log
    - --audit-log-maxage=30
    - --audit-log-maxbackup=10
    - --audit-log-maxsize=100
    - --audit-log-format=json
    # Audit Webhook (send to SLS)
    - --audit-webhook-config-file=/etc/kubernetes/audit-webhook.yaml
    - --audit-webhook-batch-max-size=100
    - --audit-webhook-batch-max-wait=5s
```

<!-- chunk: Log Alert Rules -->
## Log Alert Rules

### Prometheus Log Alerts

```yaml
groups:
- name: log_alerts
  rules:
  # High application error rate
  - alert: HighErrorRate
    expr: |
      sum(rate(log_messages_total{level="ERROR"}[5m])) by (namespace, pod) > 10
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "High error rate in {{ $labels.namespace }}/{{ $labels.pod }}"
  
  # Pod restarting frequently
  - alert: PodRestarting
    expr: |
      rate(kube_pod_container_status_restarts_total[15m]) > 0.2
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "Pod {{ $labels.namespace }}/{{ $labels.pod }} restarting frequently"
  
  # OOM Kill
  - alert: PodOOMKilled
    expr: |
      kube_pod_container_status_last_terminated_reason{reason="OOMKilled"} > 0
    labels:
      severity: critical
    annotations:
      summary: "Pod {{ $labels.namespace }}/{{ $labels.pod }} was OOM killed"
```

---

**Logging Principle**: Structured output, centralized storage, establish alerts, regular audit, compliant retention

---

**Table Maintenance**: Kusheet Project | **Author**: Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian Related Documentation -->
## Obsidian Related Documentation

- domain-06-observability MOC
- [[domain-06-observability/README.md|Observability Domain]]
- [[domain-06-observability/00-open-source-projects-index.md|Domain-8 Observability — Open Source Projects Index]]
- Kubernetes Observability Architecture System
- Metrics Monitoring System Detailed Explanation
- 03 - Logging Collection Architecture Detailed Explanation (Logging Architecture)
- Distributed Tracing System
- 05 - Alert Management Strategy (Alerting Management)
- 06 - Monitoring Alert Practice and Best Practices (Monitoring Alerting Practice)
- 04 - Monitoring Dashboard Design and Best Practices (Monitoring Dashboards)
- 08 - Logging Audit and Compliance Management (Logging Auditing & Compliance)
- 05 - Events and Audit Log Management (Events & Audit Logs)

## See Also

- 10-monitoring-metrics-prometheus
- 11-custom-metrics-adapter
- 13-cluster-health-check
- 14-chaos-engineering

- [[domain-06-observability/README.md|Back to index]]

## Related

- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Graph Index]]


<!-- risk-assessed -->
