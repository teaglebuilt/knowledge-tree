---
title: 25 - LLM Observability and Monitoring System
description: '# 25 - LLM Observability and Monitoring System'
summary: 'from prometheus_client import Counter, Histogram, Gauge, Summary'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- prometheus
- grafana
- elasticsearch
- job
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- MLOps Engineers
- SRE
estimated_read_time: 5min
intent_queries:
- What is LLM Observability and Monitoring System
- How to implement LLM Observability and Monitoring System
- Kubernetes 11 ai infra best practices
trigger_keywords:
- LLM Observability and Monitoring System
- ai
- infra
prerequisites:
- kubectl-basics
- prometheus-basics
- monitoring-basics
- gpu-scheduling-basics
- logging-basics
- observability-basics
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
- type: domain
  path: ../domain-02-workloads-applications/
  label: 'Related Knowledge Domain: domain-02-workloads-applications'
- type: domain
  path: ../domain-03-networking-traffic/
  label: 'Related Knowledge Domain: domain-03-networking-traffic'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/25-llm-observability.md
---

> **Production Environment Security Reminders**
>
> This document contains executable operational commands. Execute them only after confirming: the correct target cluster and namespace; sufficient RBAC permissions; and that they have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# 25 - LLM Observability and Monitoring System

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **Difficulty**: Expert Level | **References**: [[entities/prometheus.md|Prometheus]](https://prometheus.io/) | [[entities/opentelemetry.md|OpenTelemetry]](https://opentelemetry.io/) | [Grafana](https://grafana.com/) | [Elasticsearch](https://www.elastic.co/)


## 1. Enterprise-Level LLM Observability Architecture

### 1.1 Five-Dimensional Observability Model

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                     Enterprise LLM Observability Framework                          │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                           Metrics Collection                                  │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │ Performance │  │ Resource    │  │ Business    │  │ Cost        │          │  │
│  │  │ Metrics     │  │ Metrics     │  │ Metrics     │  │ Metrics     │          │  │
│  │  │ (Latency)   │  │ (GPU/CPU)   │  │ (Accuracy)  │  │ ($/token)   │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                           Log Aggregation                                     │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │ Application │  │ System      │  │ Audit       │  │ Security    │          │  │
│  │  │ Logs        │  │ Logs        │  │ Logs        │  │ Logs        │          │  │
│  │  │ (business logic)  │  │ (system state)  │  │ (operation audit)  │  │ (security event)  │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                           Trace Analysis                                      │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │ Request     │  │ Model       │  │ Data        │  │ User        │          │  │
│  │  │ Tracing     │  │ Inference   │  │ Processing  │  │ Experience  │          │  │
│  │  │ (call chain)  │  │ (inference process)  │  │ (data flow)    │  │ (user experience)  │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                           Alert & Action                                      │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │ Real-time   │  │ Automated   │  │ Human       │  │ Escalation  │          │  │
│  │  │ Alerts      │  │ Remediation │  │ Review      │  │ Process     │          │  │
│  │  │ (real-time alert)  │  │ (automatic repair)  │  │ (manual review)  │  │ (upgrade process)  │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Key Observability Metric Framework

| Metric Category | Core Metrics | Monitoring Thresholds | Alert Level | Business Impact |
|----------|----------|----------|----------|----------|
| **Performance Metrics** | P50/P95/P99 latency | P99<2s | Critical | User Experience |
| | Queries Per Second/Transactions Per Second | According to SLA | Warning | System Capacity |
| | Throughput | tokens/sec | Info | Efficiency Monitoring |
| **Quality Metrics** | Accuracy | >90% | Critical | Business Correctness |
| | Correlation Score | >0.8 | Warning | Result Quality |
| | Phantom Rate | <5% | Critical | Trustworthiness |
| **Resource Metrics** | GPU Utilization | 70-90% | Warning | Resource Efficiency |
| | Memory Usage | <85% | Critical | System Stability |
| | Memory usage | <90% | Warning | OOM risk |
| **Cost Metrics** | Cost per 1K tokens | Budget Threshold | Info | Cost Control |
| | Instance Cost | Budget Threshold | Warning | Financial Monitoring |
| | Spot Interruption Rate | <10% | Info | Cost Optimization |
| **User Experience** | First token time | <300ms | Warning | Response Speed |
| | Generation Rate | >10 tokens/sec | Info | Smoothness |
| | Error Rate | <1% | Critical | Service Availability |


## 2. Prometheus Metric Implementation

### 2.1 Core Metric Definitions

```python
# llm_metrics.py
from prometheus_client import Counter, Histogram, Gauge, Summary
import time
from typing import Dict, Optional
import asyncio

class LLMMetricsCollector:
    def __init__(self, model_name: str = "default"):
        self.model_name = model_name
        
        # Request Counter
        self.requests_total = Counter(
            'llm_requests_total',
            'Total number of LLM requests',
            ['model', 'status', 'endpoint']
        )
        
        # Delay Histogram
        self.request_duration = Histogram(
            'llm_request_duration_seconds',
            'LLM request duration in seconds',
            ['model', 'endpoint'],
            buckets=[0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0]
        )
        
        # Token Counter
        self.tokens_processed = Counter(
            'llm_tokens_processed_total',
            'Total number of tokens processed',
            ['model', 'token_type']  # input/output
        )
        
        # GPU Metrics
        self.gpu_utilization = Gauge(
            'llm_gpu_utilization_percent',
            'GPU utilization percentage',
            ['model', 'gpu_id']
        )
        
        self.gpu_memory_used = Gauge(
            'llm_gpu_memory_used_bytes',
            'GPU memory used in bytes',
            ['model', 'gpu_id']
        )
        
        self.gpu_temperature = Gauge(
            'llm_gpu_temperature_celsius',
            'GPU temperature in celsius',
            ['model', 'gpu_id']
        )
        
        # Model Quality Metrics
        self.model_accuracy = Gauge(
            'llm_model_accuracy_score',
            'Model accuracy score (0-1)',
            ['model']
        )
        
        self.hallucination_rate = Gauge(
            'llm_hallucination_rate_percent',
            'Percentage of hallucinated responses',
            ['model']
        )
        
        # User Experience Metrics
        self.time_to_first_token = Histogram(
            'llm_time_to_first_token_seconds',
            'Time to first token in seconds',
            ['model'],
            buckets=[0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
        )
        
        self.tokens_per_second = Gauge(
            'llm_tokens_per_second',
            'Tokens generated per second',
            ['model']
        )
        
        # Cost Metrics
        self.cost_per_thousand_tokens = Gauge(
            'llm_cost_per_thousand_tokens',
            'Cost per thousand tokens in USD',
            ['model']
        )
        
        self.instance_cost_hourly = Gauge(
            'llm_instance_cost_hourly_usd',
            'Hourly instance cost in USD',
            ['model', 'instance_type']
        )

    def record_request(self, endpoint: str, status: str = "success"):
        """Record requests"""
        self.requests_total.labels(
            model=self.model_name,
            status=status,
            endpoint=endpoint
        ).inc()
    
    def record_duration(self, endpoint: str, duration: float):
        """Record request duration"""
        self.request_duration.labels(
            model=self.model_name,
            endpoint=endpoint
        ).observe(duration)
    
    def record_tokens(self, input_tokens: int, output_tokens: int):
        """Record token usage"""
        self.tokens_processed.labels(
            model=self.model_name,
            token_type="input"
        ).inc(input_tokens)
        
        self.tokens_processed.labels(
            model=self.model_name,
            token_type="output"
        ).inc(output_tokens)
    
    def record_gpu_metrics(self, gpu_id: str, utilization: float, 
                          memory_used: int, temperature: float):
        """Record GPU metrics"""
        self.gpu_utilization.labels(
            model=self.model_name,
            gpu_id=gpu_id
        ).set(utilization)
        
        self.gpu_memory_used.labels(
            model=self.model_name,
            gpu_id=gpu_id
        ).set(memory_used)
        
        self.gpu_temperature.labels(
            model=self.model_name,
            gpu_id=gpu_id
        ).set(temperature)
    
    def record_model_quality(self, accuracy: float, hallucination_rate: float):
        """Record model quality metrics"""
        self.model_accuracy.labels(model=self.model_name).set(accuracy)
        self.hallucination_rate.labels(model=self.model_name).set(hallucination_rate)
    
    def record_user_experience(self, time_to_first_token: float, tokens_per_sec: float):
        """Record user experience metrics"""
        self.time_to_first_token.labels(model=self.model_name).observe(time_to_first_token)
        self.tokens_per_second.labels(model=self.model_name).set(tokens_per_sec)
    
    def record_cost(self, cost_per_1k_tokens: float, instance_cost: float, instance_type: str):
        """Record cost metrics"""
        self.cost_per_thousand_tokens.labels(model=self.model_name).set(cost_per_1k_tokens)
        self.instance_cost_hourly.labels(
            model=self.model_name,
            instance_type=instance_type
        ).set(instance_cost)

# Usage Example
metrics_collector = LLMMetricsCollector("llama2-7b-chat")

class LLMService:
    def __init__(self, model_name: str):
        self.metrics = LLMMetricsCollector(model_name)
        self.model_name = model_name
    
    async def generate_response(self, prompt: str, max_tokens: int = 1000) -> Dict:
        """Generate response and record metrics"""
        start_time = time.time()
        
        try:
            # Simulate model inference
            response = await self._inference(prompt, max_tokens)
            
            # Record performance metrics
            duration = time.time() - start_time
            self.metrics.record_duration("generate", duration)
            self.metrics.record_request("generate", "success")
            
            # Record token usage
            input_tokens = len(prompt.split())
            output_tokens = len(response["text"].split())
            self.metrics.record_tokens(input_tokens, output_tokens)
            
            # Record user experience metrics
            ttft = response.get("time_to_first_token", 0.1)
            tps = output_tokens / (duration - ttft) if duration > ttft else 0
            self.metrics.record_user_experience(ttft, tps)
            
            # Record model quality (simulation)
            accuracy = response.get("accuracy_score", 0.95)
            hallucination_rate = response.get("hallucination_rate", 0.02)
            self.metrics.record_model_quality(accuracy, hallucination_rate)
            
            # Record cost (simulation)
            cost_per_1k = 0.002  # $0.002 per 1K tokens
            instance_cost = 1.5  # $1.5/hour
            self.metrics.record_cost(cost_per_1k, instance_cost, "g5.2xlarge")
            
            return response
            
        except Exception as e:
            self.metrics.record_request("generate", "error")
            raise
    
    async def _inference(self, prompt: str, max_tokens: int) -> Dict:
        """Simulate inference process"""
        # Simulate inference latency
        await asyncio.sleep(0.1 + max_tokens * 0.001)
        
        return {
            "text": "This is a simulated response to: " + prompt[:50] + "...",
            "time_to_first_token": 0.05,
            "accuracy_score": 0.95,
            "hallucination_rate": 0.02
        }

# FastAPI Integration Example
from fastapi import FastAPI, HTTPException
import uvicorn

app = FastAPI(title="LLM Observability Service")

@app.post("/generate")
async def generate(prompt: str, max_tokens: int = 100):
    service = LLMService("llama2-7b-chat")
    try:
        result = await service.generate_response(prompt, max_tokens)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/metrics")
async def metrics():
    from prometheus_client import generate_latest
    return generate_latest()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

### 2.2 Advanced Alert Rule Configurations

```yaml
# llm-alerting-rules.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: llm-observability-alerts
  namespace: monitoring
spec:
  groups:
  - name: llm-performance.rules
    rules:
    # Performance alert
    - alert: HighLLMLatency
      expr: |
        histogram_quantile(0.99, rate(llm_request_duration_seconds_bucket[5m])) > 2
      for: 2m
      labels:
        severity: critical
        team: ml-platform
      annotations:
        summary: "LLM P99 delay exceeds 2 seconds"
        description: "Model {{ $labels.model }} at endpoint {{ $labels.endpoint }} has a P99 delay of {{ $value }} seconds, exceeding the threshold of 2 seconds"
        runbook_url: "https://wiki.company.com/ml-ops/llm-performance-troubleshooting"
    
    - alert: LowLLMThroughput
      expr: |
        rate(llm_requests_total[5m]) < 10
      for: 5m
      labels:
        severity: warning
        team: ml-platform
      annotations:
        summary: "LLM request throughput is low"
        description: "Model {{ $labels.model }} has a request rate of {{ $value | printf \"%#.2f\" }}/minute, below the threshold of 10/min"
    
    - alert: HighErrorRate
      expr: |
        sum(rate(llm_requests_total{status="error"}[5m])) 
        / sum(rate(llm_requests_total[5m])) > 0.01
      for: 3m
      labels:
        severity: critical
        team: ml-platform
      annotations:
        summary: "LLM error rate exceeds 1%"
        description: "Model {{ $labels.model }} has an error rate of {{ $value | printf \"%#.4f\" }}, exceeding the threshold of 1%"

  - name: llm-quality.rules
    rules:
    # Quality alert
    - alert: LowModelAccuracy
      expr: |
        llm_model_accuracy_score < 0.85
      for: 10m
      labels:
        severity: critical
        team: data-science
      annotations:
        summary: "Model accuracy is below 85%"
        description: "Model {{ $labels.model }} has an accuracy rate of {{ $value | printf \"%#.4f\" }}, below the threshold of 85%"
    
    - alert: HighHallucinationRate
      expr: |
        llm_hallucination_rate_percent > 5
      for: 5m
      labels:
        severity: critical
        team: data-science
      annotations:
        summary: "Model hallucination rate exceeds 5%"
        description: "Model {{ $labels.model }} has a hallucination rate of {{ $value | printf \"%#.2f\" }}%, exceeding the threshold of 5%"

  - name: llm-resource.rules
    rules:
    # Resource alert
    - alert: HighGPUUtilization
      expr: |
        llm_gpu_utilization_percent > 95
      for: 5m
      labels:
        severity: warning
        team: ml-platform
      annotations:
        summary: "GPU utilization exceeds 95%"
        description: "Model {{ $labels.model }}'s GPU {{ $labels.gpu_id }} utilization is {{ $value | printf \"%#.1f\" }}%"
    
    - alert: HighGPUMemoryUsage
      expr: |
        llm_gpu_memory_used_bytes / (1024*1024*1024) > 20
      for: 3m
      labels:
        severity: critical
        team: ml-platform
      annotations:
        summary: "GPU memory usage exceeds 20GB"
        description: "Model {{ $labels.model }}'s GPU {{ $labels.gpu_id }} memory usage is {{ $value | printf \"%#.2f\" }}GB"
    
    - alert: HighGPUTemperature
      expr: |
        llm_gpu_temperature_celsius > 80
      for: 2m
      labels:
        severity: warning
        team: ml-platform
      annotations:
        summary: "GPU temperature exceeds 80°C"
        description: "Model {{ $labels.model }}'s GPU {{ $labels.gpu_id }} temperature is {{ $value | printf \"%#.1f\" }}°C"

  - name: llm-cost.rules
    rules:
    # Cost alert
    - alert: HighCostPerToken
      expr: |
        llm_cost_per_thousand_tokens > 5
      for: 15m
      labels:
        severity: info
        team: finance
      annotations:
        summary: "Cost per thousand tokens exceeds $5"
        description: "Model {{ $labels.model }}'s cost per thousand tokens is ${{ $value | printf \"%#.2f\" }}"
    
    - alert: HighInstanceCost
      expr: |
        llm_instance_cost_hourly_usd > 5
      for: 1h
      labels:
        severity: warning
        team: finance
      annotations:
        summary: "Instance hour cost exceeds $5"
        description: "Model {{ $labels.model }}'s instance {{ $labels.instance_type }} hourly cost is ${{ $value | printf \"%#.2f\" }}"

  - name: llm-user-experience.rules
    rules:
    # User experience alert
    - alert: SlowTimeToFirstToken
      expr: |
        histogram_quantile(0.95, rate(llm_time_to_first_token_seconds_bucket[5m])) > 0.5
      for: 3m
      labels:
        severity: warning
        team: product
      annotations:
        summary: "First token time exceeds 500ms"
        description: "Model {{ $labels.model }} P95 first token time is {{ $value | printf \"%.3f\" }} seconds"
    
    - alert: LowTokensPerSecond
      expr: |
        llm_tokens_per_second < 5
      for: 5m
      labels:
        severity: warning
        team: product
      annotations:
        summary: "Generation rate below 5 tokens/sec"
        description: "Model {{ $labels.model }} generation rate is {{ $value | printf \"%.1f\" }} tokens/sec"
```


## 3. Grafana Dashboard Configuration

### 3.1 Core Dashboard JSON

```json
{
  "dashboard": {
    "id": null,
    "title": "LLM Observability Dashboard",
    "tags": ["llm", "ai", "observability"],
    "timezone": "browser",
    "schemaVersion": 38,
    "version": 1,
    "refresh": "30s",
    "panels": [
      {
        "type": "stat",
        "title": "Overall Health",
        "gridPos": {"x": 0, "y": 0, "w": 4, "h": 4},
        "targets": [
          {
            "expr": "sum(up{job=\"llm-service\"})",
            "instant": true
          }
        ],
        "pluginVersion": "10.2.2"
      },
      {
        "type": "graph",
        "title": "Request Rate and Latency",
        "gridPos": {"x": 4, "y": 0, "w": 8, "h": 8},
        "targets": [
          {
            "expr": "rate(llm_requests_total[1m])",
            "legendFormat": "Requests/sec - {{status}}"
          },
          {
            "expr": "histogram_quantile(0.95, rate(llm_request_duration_seconds_bucket[5m]))",
            "legendFormat": "P95 Latency (s)"
          },
          {
            "expr": "histogram_quantile(0.99, rate(llm_request_duration_seconds_bucket[5m]))",
            "legendFormat": "P99 Latency (s)"
          }
        ]
      },
      {
        "type": "heatmap",
        "title": "Latency Distribution",
        "gridPos": {"x": 12, "y": 0, "w": 12, "h": 8},
        "targets": [
          {
            "expr": "rate(llm_request_duration_seconds_bucket[5m])",
            "format": "heatmap",
            "legendFormat": "{{le}}"
          }
        ]
      },
      {
        "type": "graph",
        "title": "GPU Metrics",
        "gridPos": {"x": 0, "y": 8, "w": 12, "h": 8},
        "targets": [
          {
            "expr": "llm_gpu_utilization_percent",
            "legendFormat": "GPU {{gpu_id}} Utilization %"
          },
          {
            "expr": "llm_gpu_memory_used_bytes / (1024*1024*1024)",
            "legendFormat": "GPU {{gpu_id}} Memory (GB)"
          },
          {
            "expr": "llm_gpu_temperature_celsius",
            "legendFormat": "GPU {{gpu_id}} Temperature (°C)"
          }
        ]
      },
      {
        "type": "graph",
        "title": "Model Quality Metrics",
        "gridPos": {"x": 12, "y": 8, "w": 12, "h": 8},
        "targets": [
          {
            "expr": "llm_model_accuracy_score",
            "legendFormat": "{{model}} Accuracy"
          },
          {
            "expr": "llm_hallucination_rate_percent",
            "legendFormat": "{{model}} Hallucination Rate %"
          }
        ],
        "thresholds": [
          {"color": "green", "value": null},
          {"color": "yellow", "value": 85},
          {"color": "red", "value": 95}
        ]
      },
      {
        "type": "graph",
        "title": "User Experience Metrics",
        "gridPos": {"x": 0, "y": 16, "w": 12, "h": 8},
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(llm_time_to_first_token_seconds_bucket[5m])) * 1000",
            "legendFormat": "P95 TTFT (ms)"
          },
          {
            "expr": "llm_tokens_per_second",
            "legendFormat": "{{model}} Tokens/sec"
          }
        ]
      },
      {
        "type": "graph",
        "title": "Cost Metrics",
        "gridPos": {"x": 12, "y": 16, "w": 12, "h": 8},
        "targets": [
          {
            "expr": "llm_cost_per_thousand_tokens",
            "legendFormat": "{{model}} Cost per 1K tokens ($)"
          },
          {
            "expr": "llm_instance_cost_hourly_usd",
            "legendFormat": "{{model}} {{instance_type}} Hourly Cost ($)"
          }
        ]
      },
      {
        "type": "table",
        "title": "Top Error Endpoints",
        "gridPos": {"x": 0, "y": 24, "w": 24, "h": 6},
        "targets": [
          {
            "expr": "topk(10, sum by(endpoint) (rate(llm_requests_total{status=\"error\"}[5m])))",
            "format": "table"
          }
        ]
      }
    ],
    "templating": {
      "list": [
        {
          "name": "model",
          "type": "query",
          "datasource": "Prometheus",
          "refresh": 1,
          "query": "label_values(llm_requests_total, model)"
        }
      ]
    }
  }
}
```


## 4. Distributed Tracing Implementation

### 4.1 OpenTelemetry Integration

```python
# opentelemetry_tracing.py
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
import asyncio
import time
from typing import Dict

# Initialize tracer
trace.set_tracer_provider(TracerProvider())
otlp_exporter = OTLPSpanExporter(endpoint="http://otel-collector:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

tracer = trace.get_tracer(__name__)

class LLMTracer:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.tracer = tracer
    
    def trace_inference(self, prompt: str, max_tokens: int) -> Dict:
        """Trace inference process"""
        with self.tracer.start_as_current_span("llm_inference") as span:
            span.set_attribute("model.name", self.model_name)
            span.set_attribute("input.prompt_length", len(prompt))
            span.set_attribute("input.max_tokens", max_tokens)
            
            # Tokenization stage
            with self.tracer.start_as_current_span("tokenization") as token_span:
                start_time = time.time()
                tokens = self._tokenize(prompt)
                token_span.set_attribute("processing.time_ms", (time.time() - start_time) * 1000)
                token_span.set_attribute("output.token_count", len(tokens))
            
            # Model inference stage
            with self.tracer.start_as_current_span("model_inference") as inference_span:
                start_time = time.time()
                model_output = self._model_forward(tokens, max_tokens)
                inference_time = time.time() - start_time
                inference_span.set_attribute("processing.time_ms", inference_time * 1000)
                inference_span.set_attribute("output.token_count", len(model_output["tokens"]))
                inference_span.set_attribute("throughput.tokens_per_sec", len(model_output["tokens"]) / inference_time)
            
            # Decoding stage
            with self.tracer.start_as_current_span("decoding") as decode_span:
                start_time = time.time()
                response_text = self._decode(model_output["tokens"])
                decode_span.set_attribute("processing.time_ms", (time.time() - start_time) * 1000)
                decode_span.set_attribute("output.text_length", len(response_text))
            
            # Record overall metrics
            span.set_attribute("output.text", response_text[:100] + "..." if len(response_text) > 100 else response_text)
            span.set_attribute("total.processing_time_ms", (time.time() - span.start_time) * 1000)
            
            return {
                "text": response_text,
                "tokens_generated": len(model_output["tokens"]),
                "processing_time_ms": (time.time() - span.start_time) * 1000
            }
    
    def trace_user_interaction(self, user_id: str, session_id: str, prompt: str) -> Dict:
        """Trace user interaction"""
        with self.tracer.start_as_current_span("user_interaction") as span:
            span.set_attribute("user.id", user_id)
            span.set_attribute("session.id", session_id)
            span.set_attribute("input.prompt", prompt[:200] + "..." if len(prompt) > 200 else prompt)
            
            # Record user context
            with self.tracer.start_as_current_span("context_retrieval") as context_span:
                context = self._retrieve_context(user_id, session_id)
                context_span.set_attribute("context.size", len(context))
            
            # Generate response
            response = self.trace_inference(prompt, max_tokens=500)
            
            # Record user feedback trace points
            span.add_event("response_generated", {
                "response_length": len(response["text"]),
                "tokens_generated": response["tokens_generated"]
            })
            
            return response
    
    def _tokenize(self, prompt: str) -> list:
        """Simulate tokenization"""
        time.sleep(0.01)  # 模拟处理时间
        return prompt.split()
    
    def _model_forward(self, tokens: list, max_tokens: int) -> Dict:
        """Simulate forward propagation of the model"""
        time.sleep(0.1 + max_tokens * 0.001)  # 模拟推理时间
        return {"tokens": ["token"] * min(max_tokens, 100)}
    
    def _decode(self, tokens: list) -> str:
        """Simulate decoding"""
        time.sleep(0.005)  # 模拟处理时间
        return " ".join(tokens)
    
    def _retrieve_context(self, user_id: str, session_id: str) -> str:
        """Simulate context retrieval"""
        time.sleep(0.02)  # 模拟检索时间
        return f"Context for user {user_id} in session {session_id}"

# Integrate FastAPI
from fastapi import FastAPI, Request
import uvicorn

app = FastAPI(title="LLM Tracing Service")

# Instrument FastAPI
FastAPIInstrumentor.instrument_app(app)
RequestsInstrumentor().instrument()

llm_tracer = LLMTracer("llama2-7b-chat")

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "")
    user_id = body.get("user_id", "anonymous")
    session_id = body.get("session_id", "default")
    
    # Track user interaction
    response = llm_tracer.trace_user_interaction(user_id, session_id, prompt)
    
    return {
        "response": response["text"],
        "tokens_generated": response["tokens_generated"],
        "processing_time_ms": response["processing_time_ms"]
    }

@app.get("/health")
async def health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
```


## 5. SLO and Error Budget Management

### 5.1 SLO Definition and Implementation

```yaml
# llm-slos.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: llm-slo-rules
  namespace: monitoring
spec:
  groups:
  - name: llm-slos
    rules:
    # Availability SLO (99.9%)
    - record: slo:availability:ratio
      expr: |
        sum(rate(llm_requests_total{status="success"}[30d]))
        / sum(rate(llm_requests_total[30d]))
    
    - alert: SLAViolation-Availability
      expr: |
        slo:availability:ratio < 0.999
      for: 1h
      labels:
        severity: critical
        slo: "availability"
      annotations:
        summary: "LLM service availability SLI violation"
        description: "30-day availability {{ $value | printf \"%.4f\" }} is below target 99.9%"
    
    # Latency SLO (P95 < 1s)
    - record: slo:latency:p95
      expr: |
        histogram_quantile(0.95, rate(llm_request_duration_seconds_bucket[30d]))
    
    - alert: SLAViolation-Latency
      expr: |
        slo:latency:p95 > 1
      for: 30m
      labels:
        severity: warning
        slo: "latency"
      annotations:
        summary: "LLM service latency SLI violation"
        description: "30-day P95 latency {{ $value | printf \"%.3f\" }}s exceeds target 1s"
    
    # Quality SLO (accuracy > 90%)
    - record: slo:quality:accuracy
      expr: |
        avg_over_time(llm_model_accuracy_score[30d])
    
    - alert: SLAViolation-Quality
      expr: |
        slo:quality:accuracy < 0.90
      for: 6h
      labels:
        severity: critical
        slo: "quality"
      annotations:
        summary: "LLM service quality SLI violation"
        description: "30-day average accuracy {{ $value | printf \"%.4f\" }} is below target 90%"

  - name: error-budget
    rules:
    # Error budget calculation
    - record: error_budget:availability:remaining
      expr: |
        0.001 - (1 - slo:availability:ratio)  # 0.1% error budget
    
    - record: error_budget:latency:remaining
      expr: |
        1 - slo:latency:p95  # Latency budget
    
    - alert: ErrorBudget-BurnRate
      expr: |
        # Quick burn rate: 1-hour error rate estimates 2% of the 30-day error budget
        (1 - avg(rate(llm_requests_total{status="success"}[1h])) / avg(rate(llm_requests_total[1h])))
        > (0.001 * 2 * 30)  # 2% of monthly error budget
      for: 2m
      labels:
        severity: critical
        budget: "fast-burn"
      annotations:
        summary: "LLM service error budget quickly exhausted"
        description: "Error rate abnormally rises, may affect SLO achievement"
```

---

**Maintainers**: LLM Observability Team | **Last Updated**: 2026-02 | **Version**: v2.0


## 1. Monitoring Metric Framework

| type | metric | threshold | alert |
|-----|------|------|------|
| **performance** | P99 latency | <2s | high |
| **throughput** | QPS | >100 | medium |
| **quality** | error rate | <1% | high |
| **resources** | GPU utilization | >70% | low |
| **cost** | $/1M tokens | monitoring | information |


## 2. Prometheus Metrics

```python
from prometheus_client import Counter, Histogram, Gauge
import time

# Request counting
request_count = Counter(
    'llm_requests_total',
    'Total LLM requests',
    ['model', 'status']
)

# Delay distribution
request_latency = Histogram(
    'llm_request_duration_seconds',
    'LLM request latency',
    ['model'],
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0]
)

# Token counting
token_count = Counter(
    'llm_tokens_total',
    'Total tokens processed',
    ['model', 'type']  # type: input/output
)

# GPU utilization
gpu_utilization = Gauge(
    'llm_gpu_utilization_percent',
    'GPU utilization',
    ['gpu_id']
)

# Usage example
@app.post("/v1/chat/completions")
async def chat(request: dict):
    start = time.time()
    
    try:
        response = llm.generate(request["messages"])
        
        # Record metrics
        request_count.labels(model=model_name, status="success").inc()
        token_count.labels(model=model_name, type="input").inc(input_tokens)
        token_count.labels(model=model_name, type="output").inc(output_tokens)
        
        return response
    except Exception as e:
        request_count.labels(model=model_name, status="error").inc()
        raise
    finally:
        duration = time.time() - start
        request_latency.labels(model=model_name).observe(duration)
```


## 3. Alert Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: llm-alerts
spec:
  groups:
  - name: llm_performance
    rules:
    - alert: HighInferenceLatency
      expr: histogram_quantile(0.99, rate(llm_request_duration_seconds_bucket[5m])) > 2
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "LLM P99 latency > 2 seconds"
    
    - alert: HighErrorRate
      expr: |
        sum(rate(llm_requests_total{status="error"}[5m]))
        / sum(rate(llm_requests_total[5m]))
        > 0.01
      for: 10m
      labels:
        severity: critical
      annotations:
        summary: "Error rate > 1%"
    
    - alert: LowGPUUtilization
      expr: avg(llm_gpu_utilization_percent) < 30
      for: 30m
      labels:
        severity: info
      annotations:
        summary: "GPU utilization < 30%, resource waste"
```


## 4. Grafana Dashboard

```json
{
  "dashboard": {
    "title": "LLM Monitoring",
    "panels": [
      {
        "title": "Requests Per Second",
        "targets": [{
          "expr": "rate(llm_requests_total[1m])"
        }]
      },
      {
        "title": "P50/P95/P99 Latency",
        "targets": [
          {"expr": "histogram_quantile(0.50, rate(llm_request_duration_seconds_bucket[5m]))"},
          {"expr": "histogram_quantile(0.95, rate(llm_request_duration_seconds_bucket[5m]))"},
          {"expr": "histogram_quantile(0.99, rate(llm_request_duration_seconds_bucket[5m]))"}
        ]
      },
      {
        "title": "Tokens Throughput",
        "targets": [{
          "expr": "rate(llm_tokens_total[1m])"
        }]
      }
    ]
  }
}
```


## 5. Distributed Tracing

```python
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

# Initialize tracing
tracer = trace.get_tracer(__name__)

@app.post("/v1/chat/completions")
async def chat(request: dict):
    with tracer.start_as_current_span("llm_inference") as span:
        # Record input
        span.set_attribute("input_tokens", len(request["messages"]))
        span.set_attribute("model", model_name)
        
        # Embedding
        with tracer.start_as_current_span("tokenization"):
            tokens = tokenizer.encode(request["messages"])
        
        # Inference
        with tracer.start_as_current_span("generation"):
            output = model.generate(tokens)
        
        # Decoding
        with tracer.start_as_current_span("decoding"):
            response = tokenizer.decode(output)
        
        span.set_attribute("output_tokens", len(output))
        
        return response
```


## 6. Log Aggregation

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluentd-config
data:
  fluent.conf: |
    <source>
      @type tail
      path /var/log/llm/*.log
      pos_file /var/log/llm.pos
      tag llm
      <parse>
        @type json
        time_key timestamp
      </parse>
    </source>
    
    <filter llm>
      @type record_transformer
      <record>
        cluster_id "#{ENV['CLUSTER_ID']}"
        namespace "#{ENV['NAMESPACE']}"
      </record>
    </filter>
    
    <match llm>
      @type elasticsearch
      host elasticsearch
      port 9200
      index_name llm-logs
    </match>
```


## 7. User Experience Monitoring

```python
class UserExperienceMetrics:
    def __init__(self):
        self.time_to_first_token = Histogram(
            'llm_time_to_first_token_seconds',
            'Time to first token'
        )
        self.token_generation_rate = Histogram(
            'llm_tokens_per_second',
            'Token generation rate'
        )
    
    def track_streaming_response(self, request_id):
        start_time = time.time()
        first_token_time = None
        token_count = 0
        
        for token in llm.stream_generate():
            if first_token_time is None:
                first_token_time = time.time()
                ttft = first_token_time - start_time
                self.time_to_first_token.observe(ttft)
            
            token_count += 1
            yield token
        
        total_time = time.time() - first_token_time
        tokens_per_second = token_count / total_time
        self.token_generation_rate.observe(tokens_per_second)
```


## 8. Cost Monitoring

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: cost-tracking
spec:
  groups:
  - name: llm_cost
    rules:
    - record: llm_cost_per_million_tokens
      expr: |
        (
          sum(rate(container_cpu_usage_seconds_total{pod=~"llm.*"}[1h])) * 0.05
          + sum(gpu_duty_cycle{pod=~"llm.*"}) / 100 * 2.5
        ) / (rate(llm_tokens_total[1h]) / 1000000)
```


## 9. SLO Definition

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: slo-definitions
spec:
  groups:
  - name: slo
    rules:
    - record: slo:availability:ratio
      expr: |
        sum(rate(llm_requests_total{status="success"}[30d]))
        / sum(rate(llm_requests_total[30d]))
      # Goal: 99.9% (allowing 43 minutes/month issues)
    
    - record: slo:latency:p99
      expr: histogram_quantile(0.99, rate(llm_request_duration_seconds_bucket[30d]))
      # Goal: P99 < 2 seconds
```


## 10. Best Practices

1. **key metrics**: latency, throughput, error rate, resource utilization
2. **alert grading**: Critical/Warning/Information three levels
3. **tracing sampling**: balance performance and visibility with a 1-10% sampling rate
4. **log retention**: 30 days hot storage + 90 days cold storage
5. **dashboard**: customize dashboards for different roles

---
**related**: [114-GPU monitoring](../04-gpu-monitoring.md) | **version**: Prometheus 2.45+

---


## Obsidian Documentation

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]] - index.md|Domain-11 AI Infrastructure — Open Source Project Index] - AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Framework
- AI Data Processing Pipeline and Feature Engineering
- Distributed training framework
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry Center and Version Management

## See Also

- 23-llm-cost-monitoring
- 24-llm-model-versioning
- 26-cost-optimization-overview
- 27-cost-management-kubecost

## Related

- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Index]]


<!-- risk-assessed -->
