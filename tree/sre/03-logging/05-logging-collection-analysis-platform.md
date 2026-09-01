---
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/03-logging/05-logging-collection-analysis-platform.md
title: Logging Collection and Analysis Platform
description: 'Comprehensive logging collection and analysis platform as a critical component of observability. Detailed enterprise-level logging solution based on ELK/EFK technology stack.'
summary: A complete logging collection and analysis platform is an essential part of an observability system. This document provides a detailed introduction to an enterprise-level logging solution based on the ELK/EFK technology stack.
category: production-operations
tags:
- k8s
- production
- operations
- best-practices
- prometheus
- docker
- opa
- redis
- kafka
- elasticsearch
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- SRE
- Operations Engineer
- Platform Engineer
estimated_read_time: 5min
intent_queries:
- What is a logging collection and analysis platform
- How to implement a logging collection and analysis platform
- Kubernetes production operations best practices
trigger_keywords:
- logging collection and analysis platform
- production
- operations
prerequisites:
- kubectl-basics
- observability-basics
- prometheus-basics
- kafka-basics
- redis-basics
- policy-basics
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
---

> **Production Environment Safety Notice**
>
> This document contains directly executable operations commands. Before execution, please verify: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have validated the commands in a non-production environment. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state but usually reversible), 🟢 Low Risk / Read-Only (information gathering, no side effects).




# Logging Collection and Analysis Platform

> **Applicable Scope**: [[Kubernetes|Kubernetes]] v1.25-v1.32 | **Maintenance Status**: 🔧 Continuously Updated | **Expert Level**: ⭐⭐⭐⭐⭐

<!-- chunk: 📋 Overview -->## 📋 Overview

A complete logging collection and analysis platform is an essential component of an observability system. This document provides a detailed introduction to an enterprise-level logging solution based on the ELK/EFK technology stack.

<!-- chunk: 🏗️ Log Architecture Design -->## 🏗️ Log Architecture Design

## Tiered Log Architecture

## 1. Log Collection Layer
```yaml
# Fluent Bit DaemonSet Configuration
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluent-bit
  namespace: logging
spec:
  selector:
    matchLabels:
      app: fluent-bit
  template:
    metadata:
      labels:
        app: fluent-bit
    spec:
      serviceAccountName: fluent-bit
      containers:
      - name: fluent-bit
        image: fluent/fluent-bit:2.0
        ports:
        - containerPort: 2020
        env:
        - name: FLUENT_ELASTICSEARCH_HOST
          value: "elasticsearch.logging.svc"
        - name: FLUENT_ELASTICSEARCH_PORT
          value: "9200"
        volumeMounts:
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
        - name: fluent-bit-config
          mountPath: /fluent-bit/etc/
        resources:
          limits:
            memory: 100Mi
          requests:
            cpu: 100m
            memory: 100Mi
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers
      - name: fluent-bit-config
        configMap:
          name: fluent-bit-config
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluent-bit-config
  namespace: logging
data:
  fluent-bit.conf: |
    [SERVICE]
        Flush         1
        Log_Level     info
        Daemon        off
        Parsers_File  parsers.conf
        HTTP_Server   On
        HTTP_Listen   0.0.0.0
        HTTP_Port     2020

    [INPUT]
        Name              tail
        Tag               kube.*
        Path              /var/log/containers/*.log
        Parser            docker
        DB                /var/log/flb_kube.db
        Mem_Buf_Limit     5MB
        Skip_Long_Lines   On
        Refresh_Interval  10

    [FILTER]
        Name                kubernetes
        Match               kube.*
        Kube_URL            https://kubernetes.default.svc:443
        Kube_CA_File        /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        Kube_Token_File     /var/run/secrets/kubernetes.io/serviceaccount/token
        K8S-Logging.Parser  On
        K8S-Logging.Exclude Off

    [OUTPUT]
        Name            es
        Match           kube.*
        Host            ${FLUENT_ELASTICSEARCH_HOST}
        Port            ${FLUENT_ELASTICSEARCH_PORT}
        Logstash_Format On
        Replace_Dots    On
        Retry_Limit     False
```

## 2. Log Buffering Layer
```yaml
# Kafka as Log Buffer
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: kafka
  namespace: logging
spec:
  serviceName: kafka-headless
  replicas: 3
  selector:
    matchLabels:
      app: kafka
  template:
    metadata:
      labels:
        app: kafka
    spec:
      containers:
      - name: kafka
        image: confluentinc/cp-kafka:7.3.0
        env:
        - name: KAFKA_BROKER_ID
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: KAFKA_ZOOKEEPER_CONNECT
          value: "zookeeper:2181"
        - name: KAFKA_ADVERTISED_LISTENERS
          value: "PLAINTEXT://kafka-$(KAFKA_BROKER_ID).kafka-headless:9092"
        - name: KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR
          value: "3"
        - name: KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR
          value: "3"
        ports:
        - containerPort: 9092
        volumeMounts:
        - name: data
          mountPath: /var/lib/kafka
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 100Gi
```

## 3. Log Storage Layer
```yaml
# Elasticsearch Cluster Configuration
apiVersion: elasticsearch.k8s.elastic.co/v1
kind: Elasticsearch
metadata:
  name: elasticsearch
  namespace: logging
spec:
  version: 8.5.3
  nodeSets:
  - name: default
    count: 3
    config:
      node.store.allow_mmap: false
    volumeClaimTemplates:
    - metadata:
        name: elasticsearch-data
      spec:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 100Gi
    podTemplate:
      spec:
        containers:
        - name: elasticsearch
          env:
          - name: ES_JAVA_OPTS
            value: -Xms2g -Xmx2g
          resources:
            requests:
              memory: 2Gi
              cpu: 1
            limits:
              memory: 4Gi
              cpu: 2
```

<!-- chunk: 🔍 Log Analysis Platform -->## 🔍 Log Analysis Platform

## Kibana Configuration

## 1. Kibana Deployment Configuration
```yaml
# Kibana Configuration
apiVersion: kibana.k8s.elastic.co/v1
kind: Kibana
metadata:
  name: kibana
  namespace: logging
spec:
  version: 8.5.3
  count: 1
  elasticsearchRef:
    name: elasticsearch
  config:
    server.publicBaseUrl: "https://kibana.example.com"
    xpack.security.encryptionKey: "something_at_least_32_characters"
    xpack.security.session.idleTimeout: "1h"
    xpack.security.session.lifespan: "30d"
  http:
    tls:
      selfSignedCertificate:
        disabled: true
```

## 2. Log Index Template
```json
{
  "index_patterns": ["kubernetes-*"],
  "template": {
    "settings": {
      "number_of_shards": 3,
      "number_of_replicas": 1,
      "refresh_interval": "30s",
      "blocks": {
        "read_only_allow_delete": "false"
      }
    },
    "mappings": {
      "properties": {
        "@timestamp": { "type": "date" },
        "log.level": { "type": "keyword" },
        "message": { "type": "text" },
        "kubernetes": {
          "properties": {
            "pod": { "type": "keyword" },
            "namespace": { "type": "keyword" },
            "container": { "type": "keyword" },
            "node": { "type": "keyword" }
          }
        },
        "host": {
          "properties": {
            "name": { "type": "keyword" }
          }
        }
      }
    }
  }
}
```

## Log Parsing Optimization

## 1. Structured Log Processing
```yaml
# Log Parsing Configuration
parsers.conf: |
  [PARSER]
      Name   json
      Format json
      Time_Key time
      Time_Format %d/%b/%Y:%H:%M:%S %z

  [PARSER]
      Name   docker
      Format json
      Time_Key time
      Time_Format %Y-%m-%dT%H:%M:%S.%L
      Time_Keep   On

  [PARSER]
      Name   syslog
      Format regex
      Regex ^\<(?<pri>[0-9]+)\>(?<time>[^ ]* {1,2}[^ ]* [^ ]*) (?<host>[^ ]*) (?<ident>[a-zA-Z0-9_\/\.\-]*)(?:\[(?<pid>[0-9]+)\])?(?:[^\:]*\:)? *(?<message>.*)$
      Time_Key time
      Time_Format %b %d %H:%M:%S
```

## 2. Multi-Format Log Adaptation
```yaml
# Multi-Format Log Routing
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluent-bit-multi-format
  namespace: logging
data:
  fluent-bit.conf: |
    [SERVICE]
        Flush         1
        Log_Level     info
        
    [INPUT]
        Name              tail
        Path              /var/log/containers/app-*.log
        Parser            docker
        Tag               app.*

    [INPUT]
        Name              tail
        Path              /var/log/containers/nginx-*.log
        Parser            nginx
        Tag               nginx.*

    [FILTER]
        Name          rewrite_tag
        Match         app.*
        Rule          $kubernetes['container_name'] ^(app-.+)$ app.$1 false

    [OUTPUT]
        Name          es
        Match         app.*
        Index         kubernetes-app-%Y.%m.%d
```

<!-- chunk: 📊 Log Analysis Practices -->## 📊 Log Analysis Practices

## Key Metrics Monitoring

## 1. Error Log Monitoring
```yaml
# Error Log Alert Rules
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: log-error-alerts
  namespace: monitoring
spec:
  groups:
  - name: log.rules
    rules:
    - alert: HighErrorRate
      expr: rate(log_messages_total{level="error"}[5m]) > 10
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "High error log rate detected"
        description: "{{ $labels.app }} is generating {{ printf \"%.2f\" $value }} errors per second"
```

## 2. Application Performance Logs
```json
{
  "dashboard": {
    "title": "Application Logs Analysis",
    "panels": [
      {
        "title": "Error Rate by Service",
        "type": "graph",
        "targets": [
          {
            "query": "SELECT count(*) as error_count FROM \"kubernetes-*\" WHERE log.level = 'error' GROUP BY kubernetes.container"
          }
        ]
      },
      {
        "title": "Response Time Distribution",
        "type": "heatmap",
        "targets": [
          {
            "query": "SELECT percentile(response_time, 50) as p50, percentile(response_time, 95) as p95, percentile(response_time, 99) as p99 FROM \"kubernetes-*\" GROUP BY time(5m)"
          }
        ]
      }
    ]
  }
}
```

## Log Search Optimization

## 1. Elasticsearch Index Lifecycle Management
```yaml
# ILM Policy Configuration
apiVersion: elasticsearch.k8s.elastic.co/v1
kind: Elasticsearch
metadata:
  name: elasticsearch
spec:
  auth:
    fileRealm:
    - username: ilm_admin
      password: changeme
  http:
    tls:
      certificate:
        secretName: elasticsearch-cert
---
PUT _ilm/policy/log_retention_policy
{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": {
            "max_age": "7d",
            "max_size": "50gb"
          }
        }
      },
      "warm": {
        "min_age": "7d",
        "actions": {
          "forcemerge": {
            "max_num_segments": 1
          }
        }
      },
      "cold": {
        "min_age": "30d",
        "actions": {
          "freeze": {}
        }
      },
      "delete": {
        "min_age": "90d",
        "actions": {
          "delete": {}
        }
      }
    }
  }
}
```

## 2. Log Sampling Strategy
```yaml
# Intelligent Log Sampling Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluent-bit-sampling
  namespace: logging
data:
  fluent-bit.conf: |
    [SERVICE]
        Flush         1
        Log_Level     info
        
    [INPUT]
        Name              tail
        Path              /var/log/containers/debug-*.log
        Parser            docker
        Tag               debug.*
        
    [FILTER]
        Name          throttle
        Match         debug.*
        Rate          100
        Window        300
        Interval      1s
        
    [FILTER]
        Name          grep
        Match         *
        Exclude       log.level debug
        Exclude       kubernetes.container debug-container
```

<!-- chunk: 🔧 Platform Operations Management -->## 🔧 Platform Operations Management

## Secure Access Control

## 1. Authentication and Authorization Configuration
```yaml
# Kibana Security Configuration
apiVersion: kibana.k8s.elastic.co/v1
kind: Kibana
metadata:
  name: kibana
spec:
  secureSettings:
  - secretName: kibana-secure-settings
---
apiVersion: v1
kind: Secret
metadata:
  name: kibana-secure-settings
type: Opaque
data:
  xpack.security.authc.providers: |
    basic.basic1:
      order: 0
    saml.saml1:
      order: 1
      realm: saml1
  xpack.security.encryptionKey: |
    base64_encoded_encryption_key
```

## 2. Network Policy Configuration
```yaml
# Logging Component Network Isolation
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: logging-isolation
  namespace: logging
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: monitoring
    ports:
    - protocol: TCP
      port: 9200
  - from:
    - podSelector:
        matchLabels:
          app: kibana
    ports:
    - protocol: TCP
      port: 9200
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          name: kube-system
    ports:
    - protocol: TCP
      port: 53
    - protocol: UDP
      port: 53
```

## Performance Tuning

## 1. Resource Quota Management
```yaml
# Logging Component Resource Limits
apiVersion: v1
kind: ResourceQuota
metadata:
  name: logging-quota
  namespace: logging
spec:
  hard:
    requests.cpu: "4"
    requests.memory: 8Gi
    limits.cpu: "8"
    limits.memory: 16Gi
    persistentvolumeclaims: "10"
    requests.storage: 1Ti
---
apiVersion: v1
kind: LimitRange
metadata:
  name: logging-limits
  namespace: logging
spec:
  limits:
  - default:
      cpu: 1
      memory: 2Gi
    defaultRequest:
      cpu: 500m
      memory: 1Gi
    type: Container
```

## 2. Storage Optimization Configuration
```yaml
# Elasticsearch Storage Optimization
apiVersion: elasticsearch.k8s.elastic.co/v1
kind: Elasticsearch
metadata:
  name: elasticsearch
spec:
  nodeSets:
  - name: hot-nodes
    count: 3
    config:
      node.roles: ["data_hot", "ingest"]
      index.routing.allocation.require.data: "hot"
    podTemplate:
      spec:
        containers:
        - name: elasticsearch
          resources:
            requests:
              memory: 4Gi
              cpu: 2
            limits:
              memory: 8Gi
              cpu: 4
  - name: warm-nodes
    count: 2
    config:
      node.roles: ["data_warm"]
      index.routing.allocation.require.data: "warm"
    podTemplate:
      spec:
        containers:
        - name: elasticsearch
          resources:
            requests:
              memory: 8Gi
              cpu: 2
            limits:
              memory: 16Gi
              cpu: 4
```

<!-- chunk: 📈 Monitoring and Alerting -->## 📈 Monitoring and Alerting

## Logging Platform Health Monitoring

## 1. Component Health Check
```yaml
# Logging Component Health Monitoring
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: logging-health
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: elasticsearch
  endpoints:
  - port: http
    path: /_cluster/health
    interval: 30s
    scrapeTimeout: 10s
---
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: logging-platform-alerts
  namespace: monitoring
spec:
  groups:
  - name: logging.rules
    rules:
    - alert: ElasticsearchClusterRed
      expr: elasticsearch_cluster_health_status{color="red"} == 1
      for: 2m
      labels:
        severity: critical
      annotations:
        summary: "Elasticsearch cluster is in RED state"
        
    - alert: FluentBitBufferFull
      expr: fluentbit_buffer_overrun_total > 0
      for: 1m
      labels:
        severity: warning
      annotations:
        summary: "Fluent Bit buffer is overrun"
```

## 2. Performance Metrics Monitoring
```json
{
  "dashboard": {
    "title": "Logging Platform Performance",
    "panels": [
      {
        "title": "Log Processing Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(fluentbit_input_bytes_total[5m])",
            "legendFormat": "Bytes/sec"
          }
        ]
      },
      {
        "title": "Elasticsearch Indexing Rate",
        "type": "graph",
        "targets": [
          {
            "expr": "rate(elasticsearch_indices_indexing_index_total[5m])",
            "legendFormat": "Documents/sec"
          }
        ]
      }
    ]
  }
}
```

<!-- chunk: 🔧 Implementation Checklist -->## 🔧 Implementation Checklist

## Platform Deployment
- [ ] Design log collection architecture and data flow
- [ ] Deploy log collection agents (Fluent Bit/Fluentd)
- [ ] Configure log buffering layer (Kafka/Redis)
- [ ] Deploy log storage (Elasticsearch cluster)
- [ ] Configure log analysis interface (Kibana)
- [ ] Implement log parsing and structured processing

## Security and Performance
- [ ] Configure access authentication and authorization mechanisms
- [ ] Implement network security isolation policies
- [ ] Optimize storage and query performance
- [ ] Configure index lifecycle management
- [ ] Implement log sampling and filtering strategies
- [ ] Establish monitoring and alerting system

## Operations and Maintenance
- [ ] Establish log retention and cleanup policies
- [ ] Create logging platform operations manual
- [ ] Perform regular performance tuning
- [ ] Maintain log analysis templates and dashboards
- [ ] Establish troubleshooting and recovery procedures
- [ ] Continuously improve log collection coverage

---

*This document provides a complete technical implementation plan and operations guidance for an enterprise-level logging collection and analysis platform*

---

<!-- chunk: Related Obsidian Documents -->## Related Obsidian Documents

- domain-11-production-operations KUDIG Database — Global MOC
- [[domain-11-production-operations/README.md|Domain 11: Production Operations Best Practices]]
- Domain-18 Production Operations — Open Source Project Index
- [[domain-01-cluster-fundamentals/01-production-architecture-design-principles.md|01-Production Architecture Design Principles]]
- 02-Multi-Cloud Hybrid Deployment Strategy
- 03-Edge Computing Production Deployment
- 04-Enterprise Monitoring System
- 06-APM Application Performance Monitoring
- 07-Zero-Trust Security Architecture
- 08-CIS Benchmark Compliance Check
- 09-Software Bill of Materials
- 10-GitOps Pipeline Practices

## See Also

- 03-edge-computing-production-deployment
- 04-enterprise-monitoring-system
- 06-apm-application-performance-monitoring
- 07-zero-trust-security-architecture

- [[domain-06-observability/README.md|Back to index]]

<!-- risk-assessed -->
