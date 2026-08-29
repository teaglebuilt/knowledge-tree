---
title: KEDA Event-Driven Auto-Scaling Practice Guide
description: 'KEDA Event-Driven Auto-Scaling Practice Guide'
summary: 'kubectl describe scaledobject order-processor -n production'
category: production-operations
tags:
- k8s
- production
- operations
- best-practices
- prometheus
- helm
- redis
- mysql
- postgresql
- kafka
tier: peripheral
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
- What is KEDA Event-Driven Auto-Scaling Practice Guide
- How to use KEDA Event-Driven Auto-Scaling Practice Guide
- Kubernetes 18 production operations best practices
trigger_keywords:
- KEDA
- Event-Driven Auto-Scaling Practice Guide
- production
- operations
prerequisites:
- kubectl-basics
- platform-engineering-basics
- helm-basics
- prometheus-basics
- kafka-basics
- redis-basics
- mysql-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: KUDIG Team
  role: contributor
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./99-keda-event-driven-autoscaling-guide.md
original_language: Chinese
---

> **Production Environment Safety Tips**
>
> This document contains operations commands that can be directly executed. Before executing, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have tested in a non-production environment. Command risk levels are marked as follows: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state but usually can be rolled back), 🟢 Low Risk/Read-only (information gathering with no side effects).




# [[KEDA|KEDA]] Event-Driven Auto-Scaling Practice Guide

> **Applicable Version**: KEDA v2.16  
> **Last Updated**: 2026-04-24  
> **Difficulty**: Intermediate

---

<!-- chunk: 📋 Table of Contents -->## 📋 Table of Contents

- [I. KEDA Architecture](#i-keda-architecture)
- [II. Installation and Deployment](#ii-installation-and-deployment)
- [III. ScaledObject Core Concepts](#iii-scaledobject-core-concepts)
- [IV. Built-in Scaler Detailed Explanation](#iv-built-in-scaler-detailed-explanation)
- [V. Production-level Configuration](#v-production-level-configuration)
- [VI. Multi-dimensional Hybrid Scaling](#vi-multi-dimensional-hybrid-scaling)
- [VII. Cron Scheduled Scaling](#vii-cron-scheduled-scaling)
- [VIII. Comparison with HPA](#viii-comparison-with-hpa)
- [IX. Monitoring and Alerting](#ix-monitoring-and-alerting)

---

<!-- chunk: I. KEDA Architecture -->## I. KEDA Architecture

```
# 🟢 Low Risk: Read-only/information gathering, usually no side effects
KEDA Architecture
├── KEDA Operator (Deployment)
│   ├── ScaledObject Controller    ← Listen to ScaledObject CRD
│   ├── ScaledJob Controller       ← Listen to ScaledJob CRD
│   └── Metrics Adapter            ← Provide external metrics to HPA
│
├── ScaledObject / ScaledJob (CRD)
│   ├── Scale Target (Deployment/StatefulSet)
│   ├── Triggers (event source definition)
│   └── Scaling Behavior (scaling policy)
│
└── Event Sources (60+ Scalers)
    ├── Message Queues: Kafka, RabbitMQ, NATS, SQS, Azure Queue
    ├── Databases: PostgreSQL, MySQL, MongoDB
    ├── Cache: Redis
    ├── Storage: AWS S3, Azure Blob
    ├── Monitoring: Prometheus, Datadog, New Relic
    ├── Cloud Events: AWS CloudWatch, Azure Monitor
    └── Custom: External, Metrics API
```
## KEDA vs Native HPA

| Capability | HPA v2 | KEDA |
|:---|:---|:---|
| CPU/Memory Metrics | ✅ Native Support | ✅ Supported |
| Custom Metrics | ⚠️ Requires Metrics Server | ✅ Built-in 60+ Scalers |
| Event-Driven | ❌ Not Supported | ✅ Core Capability |
| Scale Down to 0 | ❌ Minimum 1 Replica | ✅ minReplicas: 0 |
| Scheduled Scaling | ❌ Not Supported | ✅ Cron Scaler |
| Job Scaling | ❌ Not Supported | ✅ ScaledJob |
| Multiple Triggers | ❌ Not Supported | ✅ Multi-dimensional Hybrid |

---

<!-- chunk: II. Installation and Deployment -->## II. Installation and Deployment

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend using --dry-run or diff to confirm first
> - `helm upgrade/install`: Deploy/upgrade release

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, please confirm target, impact scope and authorization before executing
helm repo add kedacore https://kedacore.github.io/charts
helm repo update

helm install keda kedacore/keda \
  --namespace keda \
  --create-namespace \
  --version 2.16.0
```
## Verify Installation

``` bash
# 🟢 Low Risk: Read-only/information gathering, usually no side effects
kubectl get pods -n keda
kubectl get crd | grep keda
# You should see: scaledobjects.keda.sh, scaledjobs.keda.sh, triggerauthentications.keda.sh
```
---

<!-- chunk: III. ScaledObject Core Concepts -->## III. ScaledObject Core Concepts

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: myapp-scaler
  namespace: production
spec:
  # Scale target
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: myapp
  
  # Replica range
  minReplicaCount: 0      # Can scale down to 0 (Serverless)
  maxReplicaCount: 100
  
  # Cooldown period
  cooldownPeriod: 300     # Scale down cooldown 5 minutes
  
  # Polling interval
  pollingInterval: 30     # Check event source every 30s
  
  # Advanced behavior
  advanced:
    restoreToOriginalReplicaCount: false
    horizontalPodAutoscalerConfig:
      behavior:
        scaleDown:
          stabilizationWindowSeconds: 300
          policies:
          - type: Percent
            value: 10
            periodSeconds: 60
        scaleUp:
          stabilizationWindowSeconds: 0
          policies:
          - type: Percent
            value: 100
            periodSeconds: 15
  
  # Trigger list
  triggers:
  - type: kafka
    metadata:
      bootstrapServers: kafka:9092
      consumerGroup: myapp-group
      topic: orders
      lagThreshold: "100"
      activationLagThreshold: "10"
```

---

<!-- chunk: IV. Built-in Scaler Detailed Explanation -->## IV. Built-in Scaler Detailed Explanation

## 4.1 Kafka Scaler (Most Common)

```yaml
triggers:
- type: kafka
  metadata:
    bootstrapServers: kafka-kafka-bootstrap.kafka:9092
    consumerGroup: order-processor
    topic: orders
    # Trigger threshold: 100 unprocessed messages per pod
    lagThreshold: "100"
    # Activation threshold: start from 0 when lag > 10
    activationLagThreshold: "10"
    # Optional: allocate by partition (ensure each partition has a consumer)
    allowIdleConsumers: "false"
    # Optional: consumer offset strategy
    offsetResetPolicy: latest
  authenticationRef:
    name: kafka-trigger-auth
---
apiVersion: keda.sh/v1alpha1
kind: TriggerAuthentication
metadata:
  name: kafka-trigger-auth
  namespace: production
spec:
  secretTargetRef:
  - parameter: sasl
    name: kafka-secret
    key: sasl
  - parameter: username
    name: kafka-secret
    key: username
  - parameter: password
    name: kafka-secret
    key: password
```

## 4.2 RabbitMQ Scaler

```yaml
triggers:
- type: rabbitmq
  metadata:
    protocol: amqp
    queueName: task-queue
    mode: QueueLength      # QueueLength | MessageRate
    value: "100"           # Scale up when queue length > 100
  authenticationRef:
    name: rabbitmq-auth
```

## 4.3 PostgreSQL Scaler

```yaml
triggers:
- type: postgresql
  metadata:
    host: postgres.database.svc.cluster.local
    port: "5432"
    userName: appuser
    dbName: appdb
    sslmode: disable
    query: "SELECT COUNT(*) FROM jobs WHERE status='pending'"
    targetQueryValue: "10"   # Scale up when pending jobs > 10
  authenticationRef:
    name: postgres-auth
```

## 4.4 Prometheus Scaler

```yaml
triggers:
- type: prometheus
  metadata:
    serverAddress: http://prometheus.monitoring.svc.cluster.local:9090
    metricName: http_requests_per_second
    query: |
      sum(rate(http_requests_total{service="myapp"}[2m]))
    threshold: "100"         # Scale up when RPS > 100
  authenticationRef:
    name: prometheus-auth
```

## 4.5 Redis Streams Scaler

```yaml
triggers:
- type: redis-streams
  metadata:
    address: redis.cache.svc.cluster.local:6379
    stream: events
    consumerGroup: processors
    pendingEntriesCount: "10"
```

## 4.6 AWS SQS Scaler

```yaml
triggers:
- type: aws-sqs-queue
  authenticationRef:
    name: aws-auth
  metadata:
    queueURL: https://sqs.us-east-1.amazonaws.com/123456789012/my-queue
    queueLength: "5"         # 5 messages per pod
    awsRegion: us-east-1
```

---

<!-- chunk: V. Production-level Configuration -->## V. Production-level Configuration

## 5.1 Serverless Mode with Zero Scaling

```yaml
spec:
  minReplicaCount: 0
  cooldownPeriod: 60        # Quick scale down to 0 to save costs
  triggers:
  - type: kafka
    metadata:
      lagThreshold: "50"
      activationLagThreshold: "1"  # Start immediately when messages arrive
```

## 5.2 Reserved Capacity Mode

```yaml
spec:
  minReplicaCount: 2        # Always keep 2 replicas to handle spikes
  maxReplicaCount: 50
  triggers:
  - type: prometheus
    metadata:
      threshold: "80"
```

## 5.3 Stability Optimization

```yaml
spec:
  advanced:
    horizontalPodAutoscalerConfig:
      behavior:
        scaleDown:
          # Stabilization period before scaling down: metrics must stay below threshold for 5 minutes before scaling down
          stabilizationWindowSeconds: 300
          policies:
          # Scale down at most 10% of replicas per minute
          - type: Percent
            value: 10
            periodSeconds: 60
        scaleUp:
          # Stabilization period before scaling up: 0 (immediate scale up)
          stabilizationWindowSeconds: 0
          policies:
          # Scale up at most 100% every 15 seconds
          - type: Percent
            value: 100
            periodSeconds: 15
          # Or scale up at most 4 pods per 15 seconds
          - type: Pods
            value: 4
            periodSeconds: 15
          # Select the maximum change
          selectPolicy: Max
```

---

<!-- chunk: VI. Multi-dimensional Hybrid Scaling -->## VI. Multi-dimensional Hybrid Scaling

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: order-processor
  namespace: production
spec:
  scaleTargetRef:
    name: order-processor
  minReplicaCount: 2
  maxReplicaCount: 100
  triggers:
  # Dimension 1: Kafka queue depth
  - type: kafka
    name: kafka-trigger
    metadata:
      bootstrapServers: kafka:9092
      consumerGroup: order-processor
      topic: orders
      lagThreshold: "100"
  
  # Dimension 2: CPU utilization
  - type: cpu
    metricType: Utilization
    metadata:
      value: "70"
  
  # Dimension 3: Memory utilization
  - type: memory
    metricType: Utilization
    metadata:
      value: "80"
  
  # Dimension 4: Prometheus custom metrics
  - type: prometheus
    name: latency-trigger
    metadata:
      serverAddress: http://prometheus:9090
      metricName: p95_latency
      query: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[2m]))
      threshold: "0.5"       # Scale up when P95 latency > 500ms
```

---

<!-- chunk: VII. Cron Scheduled Scaling -->## VII. Cron Scheduled Scaling

```yaml
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: cron-scaler
  namespace: production
spec:
  scaleTargetRef:
    name: batch-processor
  minReplicaCount: 0
  maxReplicaCount: 10
  triggers:
  # Keep 5 replicas during business hours
  - type: cron
    metadata:
      timezone: Asia/Shanghai
      start: 0 9 * * 1-5       # Monday to Friday at 9:00
      end: 0 18 * * 1-5        # Monday to Friday at 18:00
      desiredReplicas: "5"
  
  # Scale up to 10 replicas during night batch processing
  - type: cron
    metadata:
      timezone: Asia/Shanghai
      start: 0 2 * * *         # Every day at 2:00
      end: 0 5 * * *           # Every day at 5:00
      desiredReplicas: "10"
```

---

<!-- chunk: VIII. Comparison with HPA -->## VIII. Comparison with HPA

| Scenario | HPA | KEDA |
|:---|:---|:---|
| Web Service (CPU-driven) | ✅ Applicable | ✅ Applicable |
| Message Queue Consumer | ❌ Cannot sense queue depth | ✅ Core Use Case |
| Scheduled Batch Processing | ❌ Not Supported | ✅ Cron Scaler |
| Event-driven Serverless | ❌ Minimum 1 Replica | ✅ Can Scale to 0 |
| Database Queue Processing | ❌ Not Supported | ✅ PostgreSQL/MySQL Scaler |
| Hybrid Metrics-driven | ❌ Single Trigger | ✅ Multi-trigger OR Logic |

## Joint Usage Recommendations

```
Web Layer (HPA)
  ├── CPU/Memory-driven
  └── Quickly respond to traffic changes

Worker Layer (KEDA)
  ├── Kafka/RabbitMQ queue depth-driven
  ├── Can scale down to 0 to save costs
  └── Precise scaling based on message volume

Batch Processing (KEDA ScaledJob)
  ├── Trigger one Job per message
  └── Automatically clean up after completion
```

---

<!-- chunk: IX. Monitoring and Alerting -->## IX. Monitoring and Alerting

## 9.1 KEDA Metrics

``` bash
# 🟢 Low Risk: Read-only/information gathering, usually no side effects
# View ScaledObject status
kubectl get scaledobject -n production
kubectl describe scaledobject order-processor -n production

# View HPA status (KEDA creates this via Metrics Adapter)
kubectl get hpa -n production
```
## 9.2 Prometheus Alerts

```yaml
- alert: KEDAScalerErrors
  expr: rate(keda_scaler_errors[5m]) > 0
  for: 5m
  labels:
    severity: warning
  annotations:
    summary: "KEDA Scaler Error"

- alert: KEDAScaledObjectNotReady
  expr: keda_scaled_object_errors > 0
  for: 5m
  labels:
    severity: critical
  annotations:
    summary: "ScaledObject Not Ready"

- alert: KEDAMaxReplicasReached
  expr: |
    kube_deployment_status_replicas{deployment="order-processor"}
    ==
    keda_scaled_object_spec_max_replicas{scaledObject="order-processor"}
  for: 10m
  labels:
    severity: warning
  annotations:
    summary: "Maximum replicas reached, may need to increase limit"
```

---

<!-- chunk: Reference Links -->## Reference Links

- [KEDA Official Documentation](https://keda.sh/docs/)
- [KEDA GitHub](https://github.com/kedacore/keda)
- [Complete Scaler List](https://keda.sh/docs/scalers/)
- [KEDA Samples](https://github.com/kedacore/samples)
- [HPA Official Documentation](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

---

<!-- chunk: Obsidian Related Documentation -->## Obsidian Related Documentation

- domain-11-production-operations KUDIG Database — Global MOC
- [[domain-11-production-operations/README.md|Domain 11: Production Operations Best Practices ([[Production Operations|Production Operations]] Best Practices Best Practices Dictionary|Operations Best Practices]])]]
- Domain-18 Production Operations — Open Source Project Index
- [[domain-01-cluster-fundamentals/01-production-architecture-design-principles.md|01-Production Architecture Design Principles]]
- 02-Multi-cloud Hybrid Deployment Strategy
- 03-Edge Computing Production Deployment
- 04-Enterprise Monitoring System
- 05-Log Collection and Analysis Platform
- 06-APM Application Performance Monitoring
- 07-Zero Trust Security Architecture
- 08-CIS Benchmark Compliance Checking
- 09-Software Bill of Materials

## See Also

- 99-greenops-sustainable-computing-guide
- 99-karpenter-node-autoscaling-guide
- 99-kubernetes-deployment-patterns-architecture
- 99-kubernetes-multi-tenant-architecture

## Related

- [[domain-19-landscape-references/topic-index/etcd-index.md|etcd Knowledge Graph Index]]

```

<!-- risk-assessed -->