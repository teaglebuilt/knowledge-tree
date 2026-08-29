---
title: Operations Metrics System
description: Operations Metrics System
summary: The operations metrics system is a core tool for measuring platform health and guiding operational decisions. This document starts from business value and constructs a complete four-tier metrics system (USE, RED, Four Golden Signals, Error Budget), providing implementable solutions for metrics collection, analysis, and application.
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- apiserver
- prometheus
- grafana
- job
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Platform Engineers
- Operations Engineers
estimated_read_time: 5min
intent_queries:
- What is Operations Metrics System
- How to implement Operations Metrics System
- Kubernetes 9 platform ops best practices
trigger_keywords:
- Operations Metrics System
- Operations
- Metrics
- System
- platform
- ops
prerequisites:
- kubectl-basics
- platform-engineering-basics
- prometheus-basics
- monitoring-basics
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
  path: ../domain-06-observability/
  label: 'Related knowledge domain: domain-06-observability'
- type: domain
  path: ../domain-15-specialized-tech/
  label: 'Related knowledge domain: domain-15-specialized-tech'
- type: domain
  path: ../domain-10-troubleshooting-diagnostics/
  label: 'Related knowledge domain: domain-10-troubleshooting-diagnostics'
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./operate/05-operations-metrics-system.md
original_language: Chinese
---

> **Production Environment Security Notice**
>
> This document contains directly executable operations commands. Before execution, please confirm: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether it has been tested in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state, but usually can be rolled back), 🟢 Low risk/read-only (information collection, no side effects).




# Operations Metrics System

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **Document Version**: v1.0 | **Last Updated**: 2026-02
> **Target Readers**: Operations Managers, SRE Teams, Platform Engineers

<!-- chunk: Overview -->
## Overview

The operations metrics system is a core tool for measuring platform health and guiding operational decisions. This document starts from business value and constructs a complete four-tier metrics system (USE, RED, Four Golden Signals, Error Budget), providing implementable solutions for metrics collection, analysis, and application.

<!-- chunk: Metrics System Architecture -->
## Metrics System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      Metrics System Overview                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│  │  Business       │  │  System         │  │  Operations     │            │
│  │  Metrics        │  │  Metrics        │  │  Metrics        │            │
│  │  (Business)     │  │  (System)       │  │  (Operations)   │            │
│  │                 │  │                 │  │                 │            │
│  │ • Success Rate  │  │ • Resource      │  │ • Deployment    │            │
│  │ • User Exp.     │  │   Utilization   │  │   Frequency     │            │
│  │ • Revenue       │  │ • Availability  │  │ • MTTR          │            │
│  │                 │  │ • Performance   │  │ • Change Fail   │            │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘            │
│          │                     │                     │                     │
│          ▼                     ▼                     ▼                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│  │  Four-Tier      │  │  Metrics        │  │  Intelligent    │            │
│  │  Metrics        │  │  Collection     │  │  Analysis &     │            │
│  │  System         │  │  System         │  │  Application    │            │
│  │                 │  │                 │  │                 │            │
│  │ • USE Method    │  │ • Prometheus    │  │ • Anomaly       │            │
│  │ • RED Method    │  │ • Grafana       │  │   Detection     │            │
│  │ • Four Golden   │  │ • ELK Stack     │  │ • Trend         │            │
│  │ • Error Budget  │  │ • Custom        │  │   Forecasting   │            │
│  │                 │  │   Exporter      │  │ • Root Cause    │            │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- chunk: Four-Tier Metrics System Details -->
## Four-Tier Metrics System Details

### Tier 1: USE Method (Utilization, Saturation, Errors)

#### Resource Utilization Metrics
```yaml
use_method_metrics:
  cpu_metrics:
    utilization:
      - node_cpu_usage_seconds_total
      - container_cpu_usage_seconds_total
      - rate(node_cpu_seconds_total[5m])
    saturation:
      - node_load1
      - node_load5
      - node_load15
    errors:
      - node_cpu_guest_seconds_total  # Abnormal CPU time
      - node_cpu_steal_seconds_total  # Stolen CPU time
      
  memory_metrics:
    utilization:
      - node_memory_MemTotal_bytes
      - node_memory_MemFree_bytes
      - container_memory_working_set_bytes
    saturation:
      - node_memory_MemAvailable_bytes
      - container_memory_cache
    errors:
      - node_memory_Unevictable_bytes  # Non-evictable memory
      - increase(container_memory_failures_total[5m])
      
  disk_metrics:
    utilization:
      - node_filesystem_size_bytes
      - node_filesystem_free_bytes
      - node_disk_io_time_seconds_total
    saturation:
      - node_disk_io_time_weighted_seconds_total
      - node_disk_reads_completed_total
    errors:
      - node_filesystem_readonly
      - increase(node_disk_read_errors_total[5m])
      
  network_metrics:
    utilization:
      - node_network_receive_bytes_total
      - node_network_transmit_bytes_total
      - container_network_receive_bytes_total
    saturation:
      - node_network_receive_packets_total
      - node_network_transmit_packets_total
    errors:
      - increase(node_network_receive_errs_total[5m])
      - increase(node_network_transmit_errs_total[5m])
```

### Tier 2: RED Method (Rate, Errors, Duration)

#### Service-Level Metrics
```yaml
red_method_metrics:
  http_services:
    rate:
      - rate(http_requests_total[5m])  # Request rate
      - rate(nginx_http_requests_total[5m])
      
    errors:
      - rate(http_requests_total{status=~"5.."}[5m])  # 5xx error rate
      - rate(http_requests_total{status=~"4.."}[5m])  # 4xx error rate
      
    duration:
      - histogram_quantile(0.5, rate(http_request_duration_seconds_bucket[5m]))  # P50 latency
      - histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) # P95 latency
      - histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m])) # P99 latency
      
  grpc_services:
    rate:
      - rate(grpc_server_handled_total[5m])
      
    errors:
      - rate(grpc_server_handled_total{grpc_code!="OK"}[5m])
      
    duration:
      - histogram_quantile(0.95, rate(grpc_server_handling_seconds_bucket[5m]))
```

### Tier 3: Four Golden Signals

#### Google SRE Classic Metrics
```yaml
four_golden_signals:
  latency:
    definition: "Service response time distribution"
    key_metrics:
      - histogram_quantile(0.50, rate(http_request_duration_seconds_bucket[5m]))
      - histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))
      - histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))
    targets:
      p50: "< 100ms"
      p95: "< 500ms" 
      p99: "< 1000ms"
      
  traffic:
    definition: "Service request volume"
    key_metrics:
      - rate(http_requests_total[5m])
      - rate(grpc_server_started_total[5m])
    measurement: "requests per second (RPS)"
    
  errors:
    definition: "Ratio of failed requests"
    key_metrics:
      - rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])
      - sum(rate(grpc_server_handled_total{grpc_code!="OK"}[5m])) / sum(rate(grpc_server_started_total[5m]))
    targets: "< 0.1% (one per thousand)"
    
  saturation:
    definition: "Degree to which resource usage approaches the limit"
    key_metrics:
      - node_cpu_usage_seconds_total / node_cpu_seconds_total
      - container_memory_working_set_bytes / container_spec_memory_limit_bytes
      - node_filesystem_avail_bytes / node_filesystem_size_bytes
    targets: "< 70% (alert threshold)"
```

### Tier 4: Error Budget

#### SLO-Driven Error Budget Management
```yaml
error_budget_management:
  service_level_objectives:
    availability_slo:
      target: 99.9%
      calculation_window: "30 days"
      error_budget: 0.1%  # 0.1% error budget
      
    latency_slo:
      target: "95% of requests latency < 200ms"
      calculation_window: "30 days"
      error_budget: 5%   # 5% latency overage budget
      
  budget_consumption_tracking:
    metrics:
      - error_budget_burn_rate  # Error budget consumption rate
      - remaining_error_budget  # Remaining error budget
      - slo_compliance_ratio    # SLO achievement rate
      
    alerting_rules:
      slow_burn_alert:
        condition: "burn_rate > 1.0 for 1h"
        action: "Send warning notification"
        
      fast_burn_alert:
        condition: "burn_rate > 10.0 for 5m"
        action: "Immediate response, may require degradation"
```

<!-- chunk: Metrics Collection System -->
## Metrics Collection System

### Prometheus Metrics Collection Configuration
```yaml
# Prometheus configuration file
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  
scrape_configs:
  # Kubernetes component metrics
  - job_name: 'kubernetes-apiservers'
    kubernetes_sd_configs:
    - role: endpoints
    scheme: https
    tls_config:
      ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    relabel_configs:
    - source_labels: [__meta_kubernetes_namespace, __meta_kubernetes_service_name, __meta_kubernetes_endpoint_port_name]
      action: keep
      regex: default;kubernetes;https
      
  # Node metrics
  - job_name: 'kubernetes-nodes'
    kubernetes_sd_configs:
    - role: node
    scheme: https
    tls_config:
      ca_file: /var/run/secrets/kubernetes.io/serviceaccount/ca.crt
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    relabel_configs:
    - action: labelmap
      regex: __meta_kubernetes_node_label_(.+)
    - target_label: __address__
      replacement: kubernetes.default.svc:443
    - source_labels: [__meta_kubernetes_node_name]
      regex: (.+)
      target_label: __metrics_path__
      replacement: /api/v1/nodes/${1}/proxy/metrics
      
  # Pod metrics
  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
    - role: pod
    relabel_configs:
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
      action: keep
      regex: true
    - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_path]
      action: replace
      target_label: __metrics_path__
      regex: (.+)
    - source_labels: [__address__, __meta_kubernetes_pod_annotation_prometheus_io_port]
      action: replace
      regex: ([^:]+)(?::\d+)?;(\d+)
      replacement: $1:$2
      target_label: __address__
```

### Custom Exporter Development
```python
#!/usr/bin/env python3
"""
Custom business metrics exporter example
"""

from prometheus_client import start_http_server, Gauge, Counter, Histogram
import random
import time
import threading

class BusinessMetricsExporter:
    def __init__(self, port=8000):
        self.port = port
        
        # Business metrics definitions
        self.order_count = Counter('business_orders_total', 'Total orders', ['status'])
        self.payment_amount = Gauge('business_payment_amount_yuan', 'Payment amount (yuan)')
        self.user_login_duration = Histogram('business_user_login_duration_seconds', 'User login duration',
                                           buckets=[0.1, 0.5, 1.0, 2.0, 5.0])
        self.system_health = Gauge('business_system_health_score', 'System health score')
        
    def collect_business_metrics(self):
        """Collect business metrics"""
        while True:
            # Simulate order data
            order_status = random.choice(['success', 'failed', 'pending'])
            self.order_count.labels(status=order_status).inc()
            
            # Simulate payment amount
            payment = random.uniform(10, 1000)
            self.payment_amount.set(payment)
            
            # Simulate login duration
            login_time = random.uniform(0.05, 3.0)
            self.user_login_duration.observe(login_time)
            
            # Simulate system health score
            health_score = random.uniform(85, 99.9)
            self.system_health.set(health_score)
            
            time.sleep(30)  # Collect every 30 seconds
            
    def start_exporter(self):
        """Start exporter service"""
        # Start HTTP server
        start_http_server(self.port)
        print(f"Business Metrics Exporter started on port {self.port}")
        
        # Start metrics collection thread
        collector_thread = threading.Thread(target=self.collect_business_metrics)
        collector_thread.daemon = True
        collector_thread.start()
        
        # Keep main thread running
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Exporter stopped")

# Usage example
if __name__ == "__main__":
    exporter = BusinessMetricsExporter(port=9091)
    exporter.start_exporter()
```

<!-- chunk: Metrics Analysis and Alerting -->
## Metrics Analysis and Alerting

### Intelligent Alerting Rule Configuration
```yaml
# Prometheus alerting rules
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: operations-metrics-alerts
  namespace: monitoring
spec:
  groups:
  - name: resource-utilization.rules
    rules:
    # CPU usage alert
    - alert: HighCPUUsage
      expr: (1 - avg(rate(node_cpu_seconds_total{mode="idle"}[5m])) by (instance)) * 100 > 80
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Node CPU usage is too high"
        description: "Instance {{ $labels.instance }} CPU usage reaches {{ $value }}%"
        
    # Memory usage alert
    - alert: HighMemoryUsage
      expr: (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100 > 85
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Node memory usage is too high"
        description: "Instance {{ $labels.instance }} memory usage reaches {{ $value }}%"
        
  - name: service-health.rules
    rules:
    # Service error rate alert
    - alert: HighErrorRate
      expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.01
      for: 2m
      labels:
        severity: critical
      annotations:
        summary: "Service error rate is too high"
        description: "Service error rate reaches {{ $value | humanizePercentage }}"
        
    # Service latency alert
    - alert: HighLatency
      expr: histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m])) > 1
      for: 2m
      labels:
        severity: warning
      annotations:
        summary: "Service response latency is too high"
        description: "95% request latency reaches {{ $value }} seconds"
```

### Anomaly Detection Algorithm
```python
#!/usr/bin/env python3
"""
Intelligent anomaly detection algorithm
"""

import numpy as np
from scipy import stats
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class AnomalyDetector:
    def __init__(self):
        self.scaler = StandardScaler()
        self.isolation_forest = IsolationForest(contamination=0.1, random_state=42)
        
    def detect_statistical_anomalies(self, data_series, threshold=2.5):
        """
        Statistical-based anomaly detection
        """
        # Z-Score method
        z_scores = np.abs(stats.zscore(data_series))
        anomalies = np.where(z_scores > threshold)[0]
        
        return anomalies, z_scores
    
    def detect_isolation_forest_anomalies(self, data_frame):
        """
        Isolation Forest based anomaly detection
        """
        # Standardize data
        scaled_data = self.scaler.fit_transform(data_frame)
        
        # Train isolation forest model
        self.isolation_forest.fit(scaled_data)
        
        # Predict anomalies
        anomaly_labels = self.isolation_forest.predict(scaled_data)
        anomaly_scores = self.isolation_forest.decision_function(scaled_data)
        
        return anomaly_labels, anomaly_scores
    
    def detect_seasonal_anomalies(self, time_series, seasonality=24):
        """
        Seasonal anomaly detection
        """
        # Calculate moving average and standard deviation
        rolling_mean = time_series.rolling(window=seasonality).mean()
        rolling_std = time_series.rolling(window=seasonality).std()
        
        # Calculate seasonal Z-Score
        seasonal_z_score = (time_series - rolling_mean) / rolling_std
        
        # Detect anomalies
        anomalies = np.where(np.abs(seasonal_z_score) > 2.5)[0]
        
        return anomalies, seasonal_z_score

# Usage example
detector = AnomalyDetector()

# Simulate CPU usage data
cpu_data = pd.Series([np.random.normal(50, 10) for _ in range(100)])
cpu_data.iloc[50] = 95  # Inject anomaly value

# Detect anomalies
anomalies, scores = detector.detect_statistical_anomalies(cpu_data.values)
print(f"Detected {len(anomalies)} anomaly points")
```

<!-- chunk: Operations Metrics Dashboard Design -->
## Operations Metrics Dashboard Design

### Grafana Dashboard Configuration
```json
{
  "dashboard": {
    "title": "Operations Metrics Overview",
    "panels": [
      {
        "title": "Cluster Health Status",
        "type": "stat",
        "gridPos": {"x": 0, "y": 0, "w": 6, "h": 4},
        "targets": [
          {
            "expr": "sum(up{job=\"kubernetes-apiservers\"})",
            "legendFormat": "API Server Online Count"
          }
        ]
      },
      {
        "title": "Resource Utilization Overview",
        "type": "gauge",
        "gridPos": {"x": 6, "y": 0, "w": 6, "h": 4},
        "targets": [
          {
            "expr": "avg(100 - (avg by (instance) (irate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100))",
            "legendFormat": "CPU Utilization"
          },
          {
            "expr": "avg(100 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes * 100))",
            "legendFormat": "Memory Utilization"
          }
        ]
      },
      {
        "title": "Service Performance Trend",
        "type": "graph",
        "gridPos": {"x": 0, "y": 4, "w": 12, "h": 6},
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(http_request_duration_seconds_bucket[5m]))",
            "legendFormat": "P95 Latency"
          },
          {
            "expr": "rate(http_requests_total[5m])",
            "legendFormat": "Request Rate"
          }
        ]
      },
      {
        "title": "Error Budget Consumption",
        "type": "graph",
        "gridPos": {"x": 0, "y": 10, "w": 12, "h": 6},
        "targets": [
          {
            "expr": "1 - (sum(increase(http_requests_total{status!~\"5..\"}[30d])) / sum(increase(http_requests_total[30d])))",
            "legendFormat": "Error Rate"
          },
          {
            "expr": "0.001",
            "legendFormat": "Error Budget Threshold"
          }
        ]
      }
    ]
  }
}
```

<!-- chunk: Metrics Application Practice -->
## Metrics Application Practice

### 1. Capacity Planning Metrics
```yaml
capacity_planning_indicators:
  resource_growth_trends:
    - node_cpu_usage_seconds_total_rate: "CPU usage growth rate"
    - node_memory_working_set_bytes_rate: "Memory usage growth rate"
    - node_filesystem_size_bytes_rate: "Storage usage growth rate"
    
  scaling_trigger_metrics:
    cpu_utilization_threshold: 70%
    memory_utilization_threshold: 75%
    disk_utilization_threshold: 80%
    
  predictive_scaling:
    forecast_horizon: "7 days"
    confidence_level: 95%
    minimum_buffer: 20%
```

### 2. Troubleshooting Metrics
``` bash
# 🟢 Low risk: read-only/information collection, usually no side effects
#!/bin/bash
# Troubleshooting metrics check script

troubleshooting_checklist() {
    echo "=== Troubleshooting Metrics Check ==="
    
    # Check cluster component status
    echo "1. Cluster component health check:"
    kubectl get componentstatuses
    
    # Check node status
    echo "2. Node status check:"
    kubectl get nodes
    
    # Check Pod status
    echo "3. Anomalous Pod check:"
    kubectl get pods --all-namespaces | grep -v Running
    
    # Check resource usage
    echo "4. Resource usage:"
    kubectl top nodes
    kubectl top pods --all-namespaces
    
    # Check event logs
    echo "5. Recent events check:"
    kubectl get events --sort-by='.lastTimestamp' | tail -20
}

troubleshooting_checklist
```
### 3. Performance Optimization Metrics
```yaml
performance_optimization_metrics:
  bottleneck_identification:
    - container_cpu_cfs_throttled_seconds_total: "CPU throttling time"
    - container_memory_failures_total: "Memory allocation failure count"
    - node_disk_io_time_seconds_total: "Disk I/O wait time"
    - container_network_transmit_errors_total: "Network transmission errors"
    
  optimization_effectiveness:
    before_after_comparison:
      - latency_reduction_percentage
      - resource_utilization_improvement
      - cost_savings_amount
      - user_experience_score_improvement
```

<!-- chunk: Metrics System Best Practices -->
## Metrics System Best Practices

### 1. Metrics Design Principles
```
SMART Principles:
• Specific: Clear metric definition without ambiguity
• Measurable: Can be quantified and collected
• Actionable: Can guide specific actions
• Relevant: Related to business objectives
• Time-bound: Has time constraints and update frequency
```

### 2. Hierarchical Metrics Management
```yaml
metric_hierarchy:
  strategic_level:     # Strategic level (monthly/quarterly)
    - business_availability
    - customer_satisfaction
    - revenue_impact
    
  tactical_level:      # Tactical level (weekly/monthly)
    - system_uptime
    - deployment_frequency
    - mean_time_to_recovery
    
  operational_level:   # Operational level (real-time/hourly)
    - api_response_time
    - error_rate
    - resource_utilization
    
  diagnostic_level:    # Diagnostic level (real-time)
    - component_health
    - log_error_count
    - metric_anomalies
```

### 3. Metrics Governance Framework
```yaml
metric_governance:
  ownership_model:
    business_metric_owner: "Product Manager"
    system_metric_owner: "Architect"
    operational_metric_owner: "SRE Engineer"
    
  quality_standards:
    accuracy_requirement: "> 99.5%"
    completeness_requirement: "> 99%"
    timeliness_requirement: "< 1 minute latency"
    
  lifecycle_management:
    metric_creation: "Requirements review → Design → Implementation → Validation"
    metric_review: "Quarterly review → Effectiveness assessment → Optimization adjustments"
    metric_retirement: "Usage assessment → Impact analysis → Formal decommissioning"
```

<!-- chunk: Metrics System Building Checklist -->
## Metrics System Building Checklist

```bash
#!/bin/bash
# Metrics system building checklist

metrics_system_checklist() {
    echo "=== Metrics System Building Checklist ==="
    
    # Metrics design check
    echo "□ Business objectives clearly defined"
    echo "□ Critical success factors identified"
    echo "□ Metrics system hierarchically designed"
    echo "□ Metric definitions standardized"
    
    # Technical implementation check
    echo "□ Data collection plan determined"
    echo "□ Storage and computing resources prepared"
    echo "□ Visualization display configured"
    echo "□ Alerting mechanism established"
    
    # Governance and management check
    echo "□ Metric owners clearly assigned"
    echo "□ Quality standards formulated"
    echo "□ Update and maintenance process established"
    echo "□ Training documentation completed"
    
    # Application effectiveness check
    echo "□ Business decisions supported by data"
    echo "□ Operations efficiency improved"
    echo "□ Problem detection more timely"
    echo "□ Cost control more precise"
}

metrics_system_checklist
```

By establishing a comprehensive operations metrics system, it is possible to achieve a transformation from passive response to active prevention in operations mode, providing strong support for platform stability and continuous optimization.

---

<!-- chunk: Obsidian Related Documents -->
## Obsidian Related Documents

- domain-07-platform-engineering KUDIG Database — Global MOC
- [[domain-07-platform-engineering/README.md|[[Platform Ops Domain|Platform Ops Domain]]]]
- index.md|Domain-9 Platform Ops — Open Source Project Index]]
- Platform Ops Overview
- Cluster Lifecycle Management
- [[domain-07-platform-engineering/governance/03-capacity-planning-resource-assessment.md|03 capacity planning resource assessment]]
- Performance Benchmarking & Tuning
- Monitoring Alerting System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization & FinOps
- Security & Compliance Management

## See Also

- 03-capacity-planning-resource-assessment
- 04-performance-benchmarking-tuning
- 06-monitoring-alerting-system
- 07-gitops-configuration-management

## Related

- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Graph Index]]


<!-- risk-assessed -->