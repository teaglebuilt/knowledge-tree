---title: '03 - Logging Collection Architecture (Logging Architecture)'
description: 'Deep dive into Kubernetes logging collection architecture, covering log architecture patterns, component selection, configuration management, and structured logging best practices'
summary: 'Comprehensive guide to production-grade logging system design for Kubernetes clusters'
category: general
tags:
  - k8s
  - observability
  - prometheus
  - monitoring
  - architecture
  - kubelet
  - grafana
  - containerd
  - docker
  - elasticsearch
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
  - All engineers
estimated_read_time: 25min
intent_queries:
  - 03-logging-architecture design
  - 03-logging-architecture components and interactions
  - 03-logging-architecture system design
trigger_keywords:
  - Logging collection architecture
  - Logging
  - Architecture
  - observability
prerequisites:
  - kubectl-basics
  - observability-basics
  - prometheus-basics
  - monitoring-basics
  - logging-basics
original_language: Chinese
authors:
- name: Dillan Teagle
  role: contributor
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/03-logging/03-logging-architecture.md
---

> **Production Environment Security Notice**
>
> This document contains operations commands that can be executed directly. Before execution, please confirm: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have validated in a non-production environment. Command risk levels are marked: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state but usually reversible), 🟢 Low risk/read-only (information collection, no side effects).

# 03 - Logging Collection Architecture (Logging Architecture)

> **Applicable versions**: v1.25 - v1.32 | **Last updated**: 2026-01 | **Reference**: [kubernetes.io/docs/concepts/cluster-administration/logging](https://kubernetes.io/docs/concepts/cluster-administration/logging/)

<!-- chunk: Overview -->

## Overview

This document provides an in-depth analysis of Kubernetes logging collection architecture, covering log architecture patterns, component selection, configuration management, structured logging best practices, and other content to provide comprehensive guidance for enterprises to build production-grade logging systems.

---

<!-- chunk: Part 1 - Log Architecture Design -->

## Part 1: Log Architecture Design

### 1.1 Log Architecture Patterns

#### Three-Layer Log Architecture

```
# 🟢 Low risk: read-only/information collection, typically no side effects
┌─────────────────────────────────────────────────────────────────────┐
│                        Application Layer Logs                       │
├─────────────────────────────────────────────────────────────────────┤
│  • Business logs (stdout/stderr)                                    │
│  • Access logs (access.log)                                         │
│  • Error logs (error.log)                                           │
│  • Audit logs (audit.log)                                           │
└─────────────────┬───────────────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      Container Runtime Layer                        │
├─────────────────────────────────────────────────────────────────────┤
│  • Docker/Containerd log drivers                                    │
│  • Log files (/var/log/containers/*.log)                            │
│  • Log rotation (logrotate)                                         │
└─────────────────┬───────────────────────────────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     Infrastructure Layer                            │
├─────────────────────────────────────────────────────────────────────┤
│  • Node-level collectors (DaemonSet)                                │
│  • Sidecar collectors                                               │
│  • Direct application push                                          │
└─────────────────────────────────────────────────────────────────────┘
```

### 1.2 Log Collection Patterns Comparison

#### Three Primary Collection Patterns

| Pattern | Architecture Description | Advantages | Disadvantages | Applicable Scenarios |
|---------|--------------------------|------------|---------------|-----------------------|
| **Node-level Agent** | DaemonSet deploys collectors on each node | Low intrusion, unified management, high resource efficiency | Cannot collect container-internal file logs | Standard stdout logs |
| **Sidecar Container** | Deploy dedicated log collection containers within pods | Flexible, handles file logs, strong preprocessing capability | Higher resource overhead, complex configuration | File logs, log preprocessing |
| **Direct Push** | Applications push logs directly to backend storage | Most flexible, strong real-time capability, feature-rich | High application coupling, high maintenance cost | Special format logs |

---

<!-- chunk: Part 2 - Log Component Selection -->

## Part 2: Log Component Selection

### 2.1 Core Component Comparison

#### Log Collector Comparison

| Component | Type | Characteristics | Version Requirements | Resource Consumption | Cloud Alternative |
|-----------|------|-----------------|---------------------|----------------------|-------------------|
| **Fluentd** | Collector | Rich plugins, comprehensive features, active community | v1.16+ | Medium (200-500MB) | Logtail |
| **Fluent Bit** | Collector | Lightweight, high performance, low resource usage | v2.2+ | Low (<100MB) | Logtail |
| **Filebeat** | Collector | Elastic ecosystem, stable and reliable | v8.x | Low (<150MB) | Logtail |
| **Vector** | Collector | Written in Rust, ultra-high performance | v0.30+ | Very low (<50MB) | Limited native support |

#### Log Storage Comparison

| Component | Type | Characteristics | Query Capability | Cost-effectiveness | Applicable Scale |
|-----------|------|-----------------|------------------|-------------------|------------------|
| **Loki** | Storage/Query | Label-based indexing, low cost, easy deployment | LogQL queries | High | Small-to-medium clusters |
| **Elasticsearch** | Storage/Query | Full-text indexing, powerful features, mature ecosystem | Lucene queries | Medium | Large clusters |
| **SLS** | Storage/Query | Alibaba Cloud native, maintenance-free, highly available | SQL queries | High | Cloud environments |
| **OpenSearch** | Storage/Query | Open-source alternative, ES API compatible | Lucene queries | Medium | Medium-to-large clusters |

### 2.2 Production Recommended Combinations

#### Recommended Architecture Stack

```yaml
recommended_logging_stack:
  small_cluster:  # < 50 nodes
    collector: fluent_bit
    storage: loki
    visualization: grafana
    cost: low
    
  medium_cluster:  # 50-200 nodes
    collector: fluent_bit
    storage: elasticsearch/opensearch
    visualization: grafana/kibana
    cost: medium
    
  large_cluster:  # > 200 nodes
    collector: fluentd/vector (hybrid)
    storage: elasticsearch + s3 archival
    visualization: kibana/grafana
    cost: high
    
  cloud_native:  # ACK/AWS/EKS
    collector: logtail/cloudwatch
    storage: sls/cloudwatch
    visualization: native console
    cost: pay-as-you-go
```

---

<!-- chunk: Part 3 - Fluent Bit Production Configuration -->

## Part 3: Fluent Bit Production Configuration

### 3.1 Core Configuration Details

#### Fluent Bit Main Configuration

```ini
# fluent-bit.conf
[SERVICE]
    Flush         5
    Daemon        off
    Log_Level     info
    Parsers_File  parsers.conf
    Plugins_File  plugins.conf
    HTTP_Server   On
    HTTP_Listen   0.0.0.0
    HTTP_Port     2020
    Health_Check  On
    HC_Errors_Count 5
    HC_Retry_Failure_Count 5
    HC_Period 60

[INPUT]
    Name              tail
    Path              /var/log/containers/*.log
    Parser            docker
    Tag               kube.*
    Refresh_Interval  5
    Mem_Buf_Limit     50MB
    Skip_Long_Lines   On
    DB                /var/log/flb_kube.db
    DB.Sync           Normal

[INPUT]
    Name              systemd
    Tag               host.*
    Systemd_Filter    _SYSTEMD_UNIT=kubelet.service
    Systemd_Filter    _SYSTEMD_UNIT=docker.service
    Read_From_Tail    On

[FILTER]
    Name                kubernetes
    Match               kube.*
    Kube_URL            https://kubernetes.default.svc:443
    Kube_CA_File        /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    Kube_Token_File     /var/run/secrets/kubernetes.io/serviceaccount/token
    Kube_Tag_Prefix     kube.var.log.containers.
    Merge_Log           On
    Merge_Log_Key       log_processed
    Keep_Log            Off
    K8S-Logging.Parser  On
    K8S-Logging.Exclude On
    Annotations         Off
    Labels              On

[FILTER]
    Name    modify
    Match   kube.*
    Add     cluster_name prod-cluster
    Add     region cn-hangzhou
    Rename  log message

[OUTPUT]
    Name  loki
    Match kube.*
    Url   http://loki.monitoring.svc:3100/loki/api/v1/push
    BatchWait 1s
    BatchSize 30720
    Labels job=fluentbit, nodename=${NODE_NAME}
    RemoveKeys kubernetes, stream
    AutoKubernetesLabels true

[OUTPUT]
    Name  es
    Match kube.*
    Host  elasticsearch.logging.svc.cluster.local
    Port  9200
    Index k8s-logs-%Y.%m.%d
    Type  _doc
    Logstash_Format On
    Logstash_Prefix k8s
    Time_Key @timestamp
    Replace_Dots On
    Retry_Limit False
```

### 3.2 Parser Configuration

#### parsers.conf Configuration

```ini
[PARSER]
    Name        docker
    Format      json
    Time_Key    time
    Time_Format %Y-%m-%dT%H:%M:%S.%LZ
    Time_Keep   On
    Decode_Field_As escaped_utf8 log do_next
    Decode_Field_As json log

[PARSER]
    Name        nginx
    Format      regex
    Regex       ^(?<remote>[^ ]*) - (?<host>[^ ]*) \[(?<time>[^]]*)\] "(?<method>\S+)(?: +(?<path>[^\"]*?)(?: +\S*)?)?" (?<code>[^ ]*) (?<size>[^ ]*)(?: "(?<referer>[^\"]*)" "(?<agent>[^\"]*)"(?:\s+(?<http_x_forwarded_for>[^ ]+))?)?$
    Time_Key    time
    Time_Format %d/%b/%Y:%H:%M:%S %z
    Time_Keep   On

[PARSER]
    Name        json
    Format      json
    Time_Key    timestamp
    Time_Format %Y-%m-%dT%H:%M:%S.%L
    Time_Keep   On
```

---

<!-- chunk: Part 4 - Structured Logging Best Practices -->

## Part 4: Structured Logging Best Practices

### 4.1 Application Log Format Standard

#### Recommended JSON Log Format

```json
{
  "timestamp": "2026-01-18T10:30:00.123Z",
  "level": "ERROR",
  "service": "user-api",
  "version": "v1.2.3",
  "trace_id": "abc123def456",
  "span_id": "span789",
  "user_id": "12345",
  "session_id": "sess98765",
  "request_id": "req123456789",
  "method": "POST",
  "path": "/api/users",
  "query_params": {
    "page": "1",
    "limit": "20"
  },
  "status": 500,
  "duration_ms": 234,
  "bytes_in": 1024,
  "bytes_out": 512,
  "client_ip": "192.168.1.100",
  "user_agent": "Mozilla/5.0...",
  "referrer": "https://example.com",
  "error": "Database connection timeout",
  "error_code": "DB_TIMEOUT",
  "stack_trace": "at com.example.UserService.createUser(UserService.java:45)...",
  "business_context": {
    "order_id": "ORD-2026-001",
    "customer_tier": "premium",
    "region": "cn-hangzhou"
  },
  "kubernetes": {
    "namespace": "production",
    "pod": "user-api-7d4f5b8c9-xk2p4",
    "container": "app",
    "node": "node-1",
    "pod_ip": "10.244.1.10"
  },
  "resource": {
    "cpu_cores": 0.5,
    "memory_mb": 256,
    "threads": 8
  }
}
```

### 4.2 Logging Configuration for Different Languages

#### Java Application Configuration

```xml
<!-- logback-spring.xml -->
<configuration>
    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <encoder class="net.logstash.logback.encoder.LoggingEventCompositeJsonEncoder">
            <providers>
                <timestamp>
                    <fieldName>timestamp</fieldName>
                    <timeZone>UTC</timeZone>
                </timestamp>
                <logLevel>
                    <fieldName>level</fieldName>
                </logLevel>
                <loggerName>
                    <fieldName>logger</fieldName>
                </loggerName>
                <message>
                    <fieldName>message</fieldName>
                </message>
                <mdc/>
                <arguments/>
                <stackTrace>
                    <fieldName>stack_trace</fieldName>
                </stackTrace>
            </providers>
        </encoder>
    </appender>
    
    <springProfile name="production">
        <root level="INFO">
            <appender-ref ref="STDOUT" />
        </root>
    </springProfile>
</configuration>
```

#### Go Application Configuration

```go
// structured_logger.go
package main

import (
    "context"
    "go.uber.org/zap"
    "go.uber.org/zap/zapcore"
)

func NewStructuredLogger() *zap.Logger {
    config := zap.Config{
        Level:       zap.NewAtomicLevelAt(zap.InfoLevel),
        Development: false,
        Sampling: &zap.SamplingConfig{
            Initial:    100,
            Thereafter: 100,
        },
        Encoding:         "json",
        EncoderConfig:    zapcore.EncoderConfig{
            TimeKey:        "timestamp",
            LevelKey:       "level",
            NameKey:        "logger",
            CallerKey:      "caller",
            MessageKey:     "message",
            StacktraceKey:  "stack_trace",
            LineEnding:     zapcore.DefaultLineEnding,
            EncodeLevel:    zapcore.LowercaseLevelEncoder,
            EncodeTime:     zapcore.ISO8601TimeEncoder,
            EncodeDuration: zapcore.SecondsDurationEncoder,
            EncodeCaller:   zapcore.ShortCallerEncoder,
        },
        OutputPaths:      []string{"stdout"},
        ErrorOutputPaths: []string{"stderr"},
    }
    
    logger, _ := config.Build()
    return logger
}

// Usage example
func HandleRequest(ctx context.Context, logger *zap.Logger) {
    reqID := ctx.Value("request_id").(string)
    userID := ctx.Value("user_id").(string)
    
    logger.Info("Processing request",
        zap.String("request_id", reqID),
        zap.String("user_id", userID),
        zap.String("path", "/api/users"),
        zap.Int("status", 200),
        zap.Duration("duration", time.Since(start)),
    )
}
```

#### Python Application Configuration

```python
# structured_logging.py
import logging
import json
from pythonjsonlogger import jsonlogger

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            log_record['timestamp'] = record.created
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname

def setup_structured_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    
    handler = logging.StreamHandler()
    formatter = CustomJsonFormatter(
        '%(timestamp)s %(level)s %(name)s %(message)s %(pathname)s %(lineno)d'
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    
    return logger

# Usage example
logger = setup_structured_logging()

def process_user_request(user_id, request_data):
    logger.info(
        "Processing user request",
        extra={
            'user_id': user_id,
            'request_type': 'CREATE_USER',
            'ip_address': request.remote_addr,
            'user_agent': request.headers.get('User-Agent')
        }
    )
```

---

<!-- chunk: Part 5 - Advanced Log Collection Configuration -->

## Part 5: Advanced Log Collection Configuration

### 5.1 Multi-Path Log Collection

#### Complex Log Path Configuration

```yaml
# Multi-path log collection
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluent-bit-config
  namespace: logging
data:
  fluent-bit.conf: |
    [INPUT]
        Name              tail
        Path              /var/log/containers/*.log
        Parser            docker
        Tag               kube.*
        Exclude_Path      *_test_*.log
        
    [INPUT]
        Name              tail
        Path              /var/log/application/*.log
        Parser            json
        Tag               app.*
        Path_Key          filepath
        
    [INPUT]
        Name              tail
        Path              /var/log/nginx/access.log
        Parser            nginx
        Tag               nginx.access
        
    [INPUT]
        Name              tail
        Path              /var/log/nginx/error.log
        Parser            nginx-error
        Tag               nginx.error
        
    [FILTER]
        Name    rewrite_tag
        Match   kube.*
        Rule    $kubernetes['namespace_name'] ^(production)$ kube.production.$TAG false
        Rule    $kubernetes['namespace_name'] ^(staging)$ kube.staging.$TAG false
        Rule    $kubernetes['labels']['app'] ^(.+)$ kube.app.$1.$TAG false
```

### 5.2 Log Filtering and Sampling

#### Intelligent Log Processing

```ini
# Log filtering and sampling configuration
[FILTER]
    Name    grep
    Match   kube.*
    # Filter out health check logs
    Exclude log .*GET /health.*

[FILTER]
    Name    throttle
    Match   kube.*
    # Limit log rate
    Rate    1000
    Window  5

[FILTER]
    Name    lua
    Match   kube.*
    Script  sampling.lua
    Call    sample_log

[FILTER]
    Name    nest
    Match   kube.*
    Operation lift
    Nested_under kubernetes
```

#### Sampling Lua Script

```lua
-- sampling.lua
function sample_log(tag, timestamp, record)
    -- Consistent sampling based on trace_id
    if record.trace_id then
        local hash = 0
        for i = 1, #record.trace_id do
            hash = hash + string.byte(record.trace_id, i)
        end
        -- 10% sampling rate
        if hash % 100 < 10 then
            return 1, timestamp, record
        else
            return -1, timestamp, record
        end
    end
    return 1, timestamp, record
end
```

---

<!-- chunk: Part 6 - Log Storage and Query -->

## Part 6: Log Storage and Query

### 6.1 Loki Query Syntax

#### LogQL Query Examples

```logql
# Basic query
{namespace="production", app="user-api"} |= "ERROR"

# Time range query
{job="fluentbit"} |~ "timeout" [5m]

# JSON log parsing
{app="api"} | json | level="error" | line_format "{{.message}}"

# Aggregation statistics
sum(count_over_time({namespace="production"} |~ "ERROR" [1h])) by (app)

# Complex filtering
{namespace="production"} 
  | json 
  | level="ERROR" 
  | status >= 500 
  | duration_ms > 1000
  | line_format "{{.error}} - {{.path}}"

# Correlation query
{trace_id="abc123"} |~ "database"
```

### 6.2 Elasticsearch Query

#### ES Query DSL Examples

```json
{
  "query": {
    "bool": {
      "must": [
        {
          "term": {
            "kubernetes.namespace": "production"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": "now-1h",
              "lt": "now"
            }
          }
        }
      ],
      "filter": [
        {
          "terms": {
            "level": ["ERROR", "FATAL"]
          }
        }
      ]
    }
  },
  "aggs": {
    "errors_by_app": {
      "terms": {
        "field": "kubernetes.labels.app.keyword",
        "size": 10
      }
    }
  },
  "sort": [
    {
      "@timestamp": {
        "order": "desc"
      }
    }
  ]
}
```

---

<!-- chunk: Part 7 - Log Alerting and Analysis -->

## Part 7: Log Alerting and Analysis

### 7.1 Log Alert Rules

#### Log-Based Alerting

```yaml
# Loki alert rules
groups:
- name: log_alerts
  rules:
  # High application error rate
  - alert: HighErrorRate
    expr: |
      sum(rate({namespace="production", app!="health-check"} 
      |= "ERROR" [5m])) > 10
    for: 5m
    labels:
      severity: warning
      category: application
    annotations:
      summary: "High error rate in {{ $labels.app }}"
      description: "{{ $value }} errors per second"

  # Specific error patterns
  - alert: DatabaseConnectionFailures
    expr: |
      sum(count_over_time({app="user-api"} 
      |~ "database.*connection.*failed" [10m])) > 5
    for: 2m
    labels:
      severity: critical
      category: database
    annotations:
      summary: "Database connection failures detected"
      description: "Multiple database connection failures in user-api"

  # Business exceptions
  - alert: PaymentProcessingErrors
    expr: |
      sum(count_over_time({app="payment-service"} 
      | json | error_code="PAYMENT_FAILED" [15m])) > 3
    for: 5m
    labels:
      severity: critical
      category: business
    annotations:
      summary: "Payment processing errors"
      description: "Payment failures detected in payment service"
```

### 7.2 Log Analysis Practice

#### Common Analysis Scenarios

```sql
-- Slow request analysis (Loki)
topk(10, 
  sum by(path) (
    rate({app="api"} 
    | json 
    | duration_ms > 1000 [5m])
  )
)

-- Error trend analysis (Elasticsearch)
GET /k8s-logs-*/_search
{
  "aggs": {
    "errors_over_time": {
      "date_histogram": {
        "field": "@timestamp",
        "calendar_interval": "1h"
      },
      "aggs": {
        "error_types": {
          "terms": {
            "field": "error_code.keyword"
          }
        }
      }
    }
  }
}

-- User behavior analysis
{app="frontend"} 
  | json 
  | user_id != "" 
  | line_format "{{.user_id}} {{.page_visited}}" 
  | pattern "<user> <page>"
```

---

<!-- chunk: Part 8 - Compliance and Security Management -->

## Part 8: Compliance and Security Management

### 8.1 Log Retention Policy

#### Compliance Retention Requirements

| Compliance Standard | Log Type | Retention Period | Encryption Requirement | Audit Requirement |
|-------------------|----------|-----------------|----------------------|------------------|
| **PCI-DSS** | Access logs, security events | 1 year | Transport encryption + at-rest encryption | Regular auditing |
| **SOC2** | System logs, audit logs | 1 year | AES-256 encryption | Third-party audit |
| **Information Security Protection Certification 2.0** | Comprehensive logging | 6 months | National cryptography algorithm | Self-audit |
| **GDPR** | Data access logs | As needed | End-to-end encryption | DPIA assessment |

### 8.2 Sensitive Information Handling

#### Log Desensitization Configuration

```yaml
# Sensitive information filtering
[FILTER]
    Name    modify
    Match   kube.*
    # Remove sensitive fields
    Remove  credit_card_number
    Remove  password
    Remove  ssn
    
[FILTER]
    Name    record_modifier
    Match   kube.*
    Record  email ${EMAIL:anonymous@example.com}
    
[FILTER]
    Name    lua
    Match   kube.*
    Script  mask_sensitive.lua
    Call    mask_fields

[FILTER]
    Name    aws_sigv4
    Match   *
    Enabled On
    Role_arn arn:aws:iam::123456789012:role/log-forwarder
```

#### Desensitization Lua Script

```lua
-- mask_sensitive.lua
function mask_fields(tag, timestamp, record)
    -- Mask phone numbers
    if record.phone then
        record.phone = string.gsub(record.phone, "(%d{3})%d+(%d{4})", "%1****%2")
    end
    
    -- Mask email addresses
    if record.email then
        record.email = string.gsub(record.email, "(%w+)@(.+)", "***@%2")
    end
    
    -- Mask ID cards
    if record.id_card then
        record.id_card = string.gsub(record.id_card, "(%d{6})%d+(%d{4})", "%1********%2")
    end
    
    return 1, timestamp, record
end
```

---

**Logging Principles**: Structured output, centralized storage, establish alerting, regular auditing, compliance retention

---

**Implementation Recommendations**: Start simple, gradually improve, prioritize quality and security over feature richness

---

**Table Maintenance**: Kusheet Project | **Authors**: Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian Related Documentation -->

## Obsidian Related Documentation

- domain-06-observability MOC
- [[domain-06-observability/README.md|Observability Domain]]
- [[domain-06-observability/00-open-source-projects-index.md|Domain-8 Observability — Open Source Projects Index]]
- Kubernetes Observability Architecture System
- Detailed Metrics Monitoring System
- Distributed Tracing System
- 05 - Alerting Management Strategy
- 06 - Monitoring Alerting Practice and Best Practices
- 04 - Monitoring Dashboard Design and Best Practices
- 08 - Logging Auditing & Compliance Management
- 05 - Events & Audit Logs Management
- 07 - Monitoring and Metrics Tables

## Related

- 77-fusion-energy-monitoring
- [[domain-02-workloads-applications/07-java-observability-kubernetes.md|07-java-observability-kubernetes]]

- [[domain-06-observability/README.md|Back to index]] - [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Graph Index]]

## See Also

- 01-observability-architecture-overview
- 02-monitoring-metrics-system
- 04-distributed-tracing
- 05-alerting-management

<!-- risk-assessed -->
