---
title: 36 - AI Platform Enhance Observability
description: '## One,AI Platform Observability Panoramic Architecture'
summary: 'avg_over_time(nvidia_gpu_utilization[5m])'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- prometheus
- jaeger
- job
- nvidia
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
- What is AI Platform Enhance Observability
- How to AI Platform Enhance Observability
- Kubernetes 11 ai infra best practices
trigger_keywords:
- AI Platform Enhance Observability
- ai
- infra
prerequisites:
- kubectl-basics
- prometheus-basics
- gpu-scheduling-basics
- tracing-basics
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
source_path: tree/infrastructure/kubernetes/ai/infrastructure/36-ai-platform-observability-enhanced.md
---

> **Production Environment Security Reminders**
>
> Commands included in this document are executable directly. Before executing, please confirm: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# 36 - AI Platform Enhance Observability

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **AI Stack Version**: [[Prometheus|Prometheus]] 2.40+ | **Last Updated**: 2026-02 | **Quality Level**: Expert Level


## 1. Overall Observability Architecture for AI Platforms

### 1.1 Five-Dimensional Observability Model

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    AI Platform Observability Framework                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  📊 Metrics (Metrics)                                                 │
│  ├─ System metrics: CPU, memory, GPU, network                                      │
│  ├─ Application metrics: QPS, latency, error rate                                         │
│  ├─ AI metrics: accuracy, perplexity, generation quality                                    │
│  ├─ Business metrics: revenue, conversion rate, user satisfaction                                  │
│  └─ Cost metrics: resource consumption, unit cost                                        │
│                                                                         │
│  🪵 Logs Analysis (Logs)                                                    │
│  ├─ Application logs: business logic, error information                                        │
│  ├─ System logs: kernel, container runtime                                          │
│  ├─ Security logs: access control, threat detection                                        │
│  ├─ Audit logs: operational records, compliance tracking                                  │
│  └─ Debug logs: development debugging, performance analysis                                  │
│                                                                         │
│  🔍 Tracing (Tracing)                                                 │
│  ├─ Request chain: end-to-end call path                                            │
│  ├─ Dependency: service call graph                                              │
│  ├─ Performance bottlenecks: hotspot analysis, delay decomposition                                        │
│  ├─ Error propagation: exception tracing, impact analysis                                        │
│  └─ AI chain: prompt processing, inference process                                        │
│                                                                         │
│  🚨 Alert Management (Alerting)                                                │
│  ├─ threshold alarm: static threshold monitoring                                              │
│  ├─ Anomaly detection: Machine learning anomaly identification              │
│  ├─ Predictive alerts: trend forecasting, capacity warnings               │
│  ├─ Intelligent alerts: root cause analysis, related alerts               │
│  └─ Self-healing capability: Automatic repair, degradation handling           │
│                                                                         │
│  📈 Visualization (Visualization)                                         │
│  ├─ real-time dashboard: operational status, key metrics                                      │
│  ├─ Historical trend: Performance evolution, capacity planning              │
│  ├─ Comparative analysis: A/B testing, version comparison                  │
│  ├─ drill-down analysis: problem location, root cause finding                                        │
│  └─ Report generation: automatic reports, compliance reports                                        │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Special Challenges in AI Observability

| Challenge Type | Specific Problem | Impact | Solution Approach |
|---------|---------|------|---------|
| **Dimension Complexity** | Multimodal Input/Output | Explosion of Monitoring Metrics | Unified Metric Framework, Dimension Abstraction |
| **Real-time Requirement** | Delay-sensitive Inference | Significant Impact on User Experience | Edge Computing, Stream Processing |
| **Semantic Understanding** | Unstructured Data | Traditional Monitoring Fails | AI-assisted Analysis, Semantic Monitoring |
| **Dynamic Characteristics** | Model Continuous Evolution | Baselines Continuously Changing | Adaptive Thresholds, Online Learning |
| **Cost Sensitivity** | Large-scale Deployment | High Monitoring Costs | Intelligent Sampling, Layered Monitoring |


## 2. Enterprise-Level AI Monitoring Metrics Framework

### 2.1 Classification of Core Metrics

```yaml
# ai-monitoring-metrics.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: ai-platform-metrics-spec
  namespace: monitoring
data:
  metrics-specification.yaml: |
    # AI Platform Monitoring Metrics Specification
    metrics:
      system_level:
        - name: "node_gpu_utilization"
          type: "gauge"
          description: "GPU utilization percentage"
          labels: ["node", "gpu_id", "model"]
          sampling_interval: "15s"
          retention: "30d"
        
        - name: "node_gpu_temperature"
          type: "gauge"
          description: "GPU temperature (Celsius)"
          labels: ["node", "gpu_id"]
          sampling_interval: "30s"
          retention: "7d"
        
        - name: "container_memory_working_set_bytes"
          type: "gauge"
          description: "Actual memory usage by container"
          labels: ["namespace", "pod", "container"]
          sampling_interval: "15s"
          retention: "14d"
      
      application_level:
        - name: "http_requests_total"
          type: "counter"
          description: "Total HTTP requests"
          labels: ["service", "method", "status_code", "model_name"]
          sampling_interval: "5s"
          retention: "90d"
        
        - name: "http_request_duration_seconds"
          type: "histogram"
          description: "Distribution of HTTP request delays"
          labels: ["service", "method", "model_name"]
          buckets: [0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 2.5, 5.0, 10.0]
          sampling_interval: "5s"
          retention: "30d"
        
        - name: "model_inference_duration_seconds"
          type: "histogram"
          description: "Model inference delay"
          labels: ["model_name", "batch_size", "hardware_type"]
          buckets: [0.01, 0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0]
          sampling_interval: "1s"
          retention: "15d"
      
      ai_specific:
        - name: "model_accuracy"
          type: "gauge"
          description: "Model accuracy"
          labels: ["model_name", "dataset", "version"]
          sampling_interval: "1h"
          retention: "365d"
        
        - name: "prompt_tokens_total"
          type: "counter"
          description: "Prompt tokens consumed total"
          labels: ["model_name", "user_id", "application"]
          sampling_interval: "1m"
          retention: "90d"
        
        - name: "generation_tokens_total"
          type: "counter"
          description: "Tokens consumed by model generation"
          labels: ["model_name", "user_id", "application"]
          sampling_interval: "1m"
          retention: "90d"
        
        - name: "model_drift_score"
          type: "gauge"
          description: "Model drift detection score"
          labels: ["model_name", "feature_name", "drift_type"]
          sampling_interval: "1h"
          retention: "180d"
      
      business_level:
        - name: "api_cost_usd"
          type: "counter"
          description: "API call cost ($)"
          labels: ["service", "model_name", "customer_tier"]
          sampling_interval: "1m"
          retention: "365d"
        
        - name: "user_satisfaction_score"
          type: "gauge"
          description: "User satisfaction score"
          labels: ["application", "model_name", "user_segment"]
          sampling_interval: "1d"
          retention: "365d"
        
        - name: "revenue_generated_usd"
          type: "counter"
          description: "Generated revenue ($)"
          labels: ["product", "model_name", "region"]
          sampling_interval: "1h"
          retention: "365d"
```

### 2.2 Prometheus Monitoring Rules

```yaml
# ai-prometheus-rules.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: ai-platform-monitoring-rules
  namespace: monitoring
spec:
  groups:
  - name: ai-platform.rules
    rules:
    # System Health Check
    - alert: HighGPUMemoryUsage
      expr: |
        avg by(node, gpu_id) (
          nvidia_gpu_memory_used_bytes / nvidia_gpu_memory_total_bytes * 100
        ) > 90
      for: 5m
      labels:
        severity: critical
        team: ai-platform
      annotations:
        summary: "GPU memory usage is high ({{ $labels.node }}-{{ $labels.gpu_id }})"
        description: "GPU memory usage has reached {{ $value }}%, which may cause OOM errors"
        runbook_url: "https://internal/wiki/gpu-troubleshooting"
    
    - alert: GPUPowerAnomaly
      expr: |
        stddev_over_time(nvidia_gpu_power_usage_watts[10m]) > 50
      for: 15m
      labels:
        severity: warning
        team: ai-platform
      annotations:
        summary: "Abnormal fluctuations in GPU power consumption"
        description: "Standard deviation of GPU power consumption is too large, which may indicate hardware issues"
    
    # Application Performance Monitoring
    - alert: HighInferenceLatency
      expr: |
        histogram_quantile(0.95, 
          sum by(model_name) (
            rate(model_inference_duration_seconds_bucket[5m])
          )
        ) > 2.0
      for: 2m
      labels:
        severity: warning
        team: ml-engineering
      annotations:
        summary: "High model inference delay ({{ $labels.model_name }})"
        description: "P95 inference delay has reached {{ $value }} seconds, exceeding SLA requirements"
    
    - alert: LowModelAccuracy
      expr: |
        model_accuracy < 0.85
      for: 1h
      labels:
        severity: critical
        team: ml-engineering
      annotations:
        summary: "Model accuracy has dropped ({{ $labels.model_name }})"
        description: "Model accuracy {{ $value }} is below the threshold of 0.85, needs investigation"
    
    # Business Metric Monitoring
    - alert: HighAPICost
      expr: |
        sum by(service) (
          rate(api_cost_usd[1h])
        ) > 100
      for: 30m
      labels:
        severity: warning
        team: finance
      annotations:
        summary: "API costs are too high ({{ $labels.service }})"
        description: "Hourly API cost reaches ${{ $value }}, exceeds budget"
    
    - alert: UserSatisfactionDrop
      expr: |
        user_satisfaction_score < 3.5
      for: 24h
      labels:
        severity: critical
        team: product
      annotations:
        summary: "User satisfaction drops"
        description: "User satisfaction score {{ $value }} is below the threshold of 3.5"
    
    # Special Problems for AI
    - alert: ModelDriftDetected
      expr: |
        model_drift_score > 0.1
      for: 6h
      labels:
        severity: warning
        team: ml-engineering
      annotations:
        summary: "Model drift detected ({{ $labels.model_name }})"
        description: "Model drift score {{ $value }}, suggests retraining the model"
    
    - alert: TokenConsumptionSpike
      expr: |
        rate(prompt_tokens_total[5m]) > 100000
      for: 10m
      labels:
        severity: info
        team: ml-engineering
      annotations:
        summary: "Token consumption surges"
        description: "Prompt token consumption rate abnormally increases to {{ $value }}/sec"

  - name: ai-platform-recording.rules
    rules:
    # Common Metrics for Precomputation
    - record: "node:gpu_utilization:avg5m"
      expr: |
        avg_over_time(nvidia_gpu_utilization[5m])
    
    - record: "model:inference_p95_latency:1h"
      expr: |
        histogram_quantile(0.95, 
          sum by(model_name) (
            rate(model_inference_duration_seconds_bucket[1h])
          )
        )
    
    - record: "service:daily_cost:usd"
      expr: |
        sum by(service) (
          increase(api_cost_usd[24h])
        )
    
    - record: "model:drift_trend:7d"
      expr: |
        avg_over_time(model_drift_score[7d])
```


## 3. Distributed Tracing and Link Analysis

### 3.1 AI Service Tracing Architecture

```python
# ai-tracing-instrumentation.py
import asyncio
import time
from typing import Dict, List, Optional, Any
import uuid
from dataclasses import dataclass, field
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.trace import SpanKind
import logging
import json

# Initialize OpenTelemetry
trace.set_tracer_provider(TracerProvider())
otlp_exporter = OTLPSpanExporter(endpoint="http://jaeger-collector:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

tracer = trace.get_tracer(__name__)

@dataclass
class AIRequestContext:
    request_id: str
    model_name: str
    user_id: str
    prompt: str
    timestamp: float = field(default_factory=time.time)
    metadata: Dict[str, Any] = field(default_factory=dict)

class AITracingInstrumentation:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def trace_model_inference(self, context: AIRequestContext, batch_size: int = 1):
        """Trace the entire process of model inference"""
        with tracer.start_as_current_span(
            f"model_inference_{context.model_name}",
            kind=SpanKind.SERVER,
            attributes={
                "ai.request_id": context.request_id,
                "ai.model_name": context.model_name,
                "ai.user_id": context.user_id,
                "ai.batch_size": batch_size,
                "ai.prompt_length": len(context.prompt),
            }
        ) as span:
            
            # Preprocessing stage
            preprocessing_result = self._trace_preprocessing(context, span)
            
            # Model inference stage
            inference_result = self._trace_model_inference(preprocessing_result, span)
            
            # Post-processing stage
            postprocessing_result = self._trace_postprocessing(inference_result, span)
            
            # Set final attributes
            span.set_attribute("ai.response_length", len(postprocessing_result.get("response", "")))
            span.set_attribute("ai.tokens_input", preprocessing_result.get("input_tokens", 0))
            span.set_attribute("ai.tokens_output", postprocessing_result.get("output_tokens", 0))
            
            return postprocessing_result
    
    def _trace_preprocessing(self, context: AIRequestContext, parent_span) -> Dict:
        """Trace the preprocessing stage"""
        with tracer.start_as_current_span(
            "preprocessing",
            context=trace.set_span_in_context(parent_span),
            attributes={
                "component": "tokenizer",
                "ai.model_name": context.model_name,
            }
        ) as span:
            
            start_time = time.time()
            
            # Simulate preprocessing logic
            tokens = self._tokenize_prompt(context.prompt, context.model_name)
            input_ids = tokens["input_ids"]
            
            processing_time = time.time() - start_time
            
            span.set_attribute("ai.input_tokens", len(input_ids))
            span.set_attribute("ai.preprocessing_time", processing_time)
            span.set_status(trace.Status(trace.StatusCode.OK))
            
            return {
                "input_ids": input_ids,
                "attention_mask": tokens["attention_mask"],
                "input_tokens": len(input_ids),
                "processing_time": processing_time
            }
    
    def _trace_model_inference(self, preprocessed_data: Dict, parent_span) -> Dict:
        """Trace the model inference stage"""
        with tracer.start_as_current_span(
            "model_inference",
            context=trace.set_span_in_context(parent_span),
            attributes={
                "component": "model",
                "ai.model_name": preprocessed_data.get("model_name", "unknown"),
                "ai.input_tokens": preprocessed_data.get("input_tokens", 0),
            }
        ) as span:
            
            start_time = time.time()
            
            # Simulate model inference
            logits, hidden_states = self._run_model_inference(
                preprocessed_data["input_ids"],
                preprocessed_data["attention_mask"]
            )
            
            inference_time = time.time() - start_time
            
            span.set_attribute("ai.inference_time", inference_time)
            span.set_attribute("ai.output_logits_shape", str(logits.shape))
            span.set_status(trace.Status(trace.StatusCode.OK))
            
            return {
                "logits": logits,
                "hidden_states": hidden_states,
                "inference_time": inference_time
            }
    
    def _trace_postprocessing(self, inference_result: Dict, parent_span) -> Dict:
        """Trace the post-processing stage"""
        with tracer.start_as_current_span(
            "postprocessing",
            context=trace.set_span_in_context(parent_span),
            attributes={
                "component": "decoder",
                "ai.model_name": inference_result.get("model_name", "unknown"),
            }
        ) as span:
            
            start_time = time.time()
            
            # Simulate post-processing logic
            response_text, output_tokens = self._decode_output(inference_result["logits"])
            
            processing_time = time.time() - start_time
            
            span.set_attribute("ai.output_tokens", output_tokens)
            span.set_attribute("ai.postprocessing_time", processing_time)
            span.set_status(trace.Status(trace.StatusCode.OK))
            
            return {
                "response": response_text,
                "output_tokens": output_tokens,
                "processing_time": processing_time
            }
    
    def _tokenize_prompt(self, prompt: str, model_name: str) -> Dict:
        """Simulate tokenization"""
        # Simplified tokenization logic
        tokens = prompt.split()
        return {
            "input_ids": list(range(len(tokens))),
            "attention_mask": [1] * len(tokens)
        }
    
    def _run_model_inference(self, input_ids: List[int], attention_mask: List[int]):
        """simulate model inference"""
        # Simulate inference latency
        time.sleep(0.1 + len(input_ids) * 0.001)
        
        # Simulation Output
        import numpy as np
        batch_size = 1
        seq_len = len(input_ids)
        vocab_size = 32000
        
        logits = np.random.randn(batch_size, seq_len, vocab_size).astype(np.float32)
        hidden_states = np.random.randn(batch_size, seq_len, 4096).astype(np.float32)
        
        return logits, hidden_states
    
    def _decode_output(self, logits) -> tuple:
        """simulate decoding output"""
        # Simplified decoding logic
        import numpy as np
        batch_size, seq_len, vocab_size = logits.shape
        
        # Choose the token with the highest probability
        output_ids = np.argmax(logits, axis=-1)[0]  # 取第一个样本
        output_tokens = len(output_ids)
        
        # Convert to text (simplified)
        response_text = " ".join([f"token_{token_id}" for token_id in output_ids[:50]])
        
        return response_text, output_tokens

class AIPerformanceAnalyzer:
    def __init__(self):
        self.tracer = trace.get_tracer(__name__)
        self.logger = logging.getLogger(__name__)
    
    def analyze_inference_performance(self, traces: List[Dict]) -> Dict:
        """reasoning performance"""
        if not traces:
            return {}
        
        # Extract key performance indicators
        preprocessing_times = []
        inference_times = []
        postprocessing_times = []
        total_times = []
        
        for trace_data in traces:
            spans = trace_data.get("spans", [])
            
            # Extract time taken at each stage
            for span in spans:
                if span.get("name") == "preprocessing":
                    preprocessing_times.append(span.get("attributes", {}).get("ai.preprocessing_time", 0))
                elif span.get("name") == "model_inference":
                    inference_times.append(span.get("attributes", {}).get("ai.inference_time", 0))
                elif span.get("name") == "postprocessing":
                    postprocessing_times.append(span.get("attributes", {}).get("ai.postprocessing_time", 0))
                elif span.get("name", "").startswith("model_inference_"):
                    total_times.append(span.get("duration", 0) / 1_000_000_000)  # 纳秒转秒
        
        # Calculate statistical information
        analysis = {
            "total_requests": len(traces),
            "performance_metrics": {
                "preprocessing": self._calculate_stats(preprocessing_times),
                "inference": self._calculate_stats(inference_times),
                "postprocessing": self._calculate_stats(postprocessing_times),
                "total": self._calculate_stats(total_times)
            },
            "bottlenecks": self._identify_bottlenecks({
                "preprocessing": preprocessing_times,
                "inference": inference_times,
                "postprocessing": postprocessing_times
            }),
            "recommendations": self._generate_recommendations({
                "preprocessing": preprocessing_times,
                "inference": inference_times,
                "postprocessing": postprocessing_times
            })
        }
        
        return analysis
    
    def _calculate_stats(self, times: List[float]) -> Dict:
        """compute statistical information"""
        if not times:
            return {}
        
        import numpy as np
        times_array = np.array(times)
        
        return {
            "count": len(times),
            "mean": float(np.mean(times_array)),
            "median": float(np.median(times_array)),
            "p95": float(np.percentile(times_array, 95)),
            "p99": float(np.percentile(times_array, 99)),
            "min": float(np.min(times_array)),
            "max": float(np.max(times_array)),
            "std": float(np.std(times_array))
        }
    
    def _identify_bottlenecks(self, timing_data: Dict) -> List[str]:
        """Identify performance bottlenecks"""
        bottlenecks = []
        
        # Calculate proportion of average time for each stage
        total_avg = sum(np.mean(times) for times in timing_data.values() if times)
        
        if total_avg > 0:
            for stage, times in timing_data.items():
                if times:
                    avg_time = np.mean(times)
                    percentage = (avg_time / total_avg) * 100
                    if percentage > 50:  # 如果某阶段占总时间超过50%
                        bottlenecks.append(f"{stage} stage is the main bottleneck ({percentage:.1f}%)")
        
        return bottlenecks
    
    def _generate_recommendations(self, timing_data: Dict) -> List[str]:
        """Generate optimization suggestions"""
        recommendations = []
        
        # Preprocessing optimization suggestions
        if timing_data.get("preprocessing") and np.mean(timing_data["preprocessing"]) > 0.05:
            recommendations.append("Preprocessing takes too long, consider optimizing the tokenization algorithm or using a faster tokenizer")
        
        # Inference optimization recommendations
        if timing_data.get("inference") and np.mean(timing_data["inference"]) > 0.5:
            recommendations.append("Model inference is too slow, consider model quantization, batching, or using a more efficient inference engine")
        
        # Post-processing optimization suggestions
        if timing_data.get("postprocessing") and np.mean(timing_data["postprocessing"]) > 0.05:
            recommendations.append("Postprocessing takes too long, consider optimizing the decoding algorithm or parallel processing")
        
        # General recommendation
        recommendations.append("Enable continuous performance monitoring, establish a performance baseline")
        recommendations.append("Implement auto-scaling to respond to load changes")
        
        return recommendations

# Usage Example
async def main():
    instrumentation = AITracingInstrumentation()
    analyzer = AIPerformanceAnalyzer()
    
    # Simulate multiple inference requests
    traces_collected = []
    
    for i in range(10):
        request_context = AIRequestContext(
            request_id=str(uuid.uuid4()),
            model_name="llama2-7b",
            user_id=f"user_{i}",
            prompt="Write a short story about AI observability"
        )
        
        # Execute inference with tracing
        result = instrumentation.trace_model_inference(request_context, batch_size=1)
        traces_collected.append(result)
        
        print(f"Request {i+1} completed in {result.get('total_time', 0):.3f}s")
    
    # Analyze performance
    performance_analysis = analyzer.analyze_inference_performance(traces_collected)
    print("\nPerformance Analysis:")
    print(json.dumps(performance_analysis, indent=2))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```

### 3.2 Jaeger Tracing Configuration

```yaml
# jaeger-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jaeger-all-in-one
  namespace: observability
spec:
  replicas: 1
  selector:
    matchLabels:
      app: jaeger
  template:
    metadata:
      labels:
        app: jaeger
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "14269"
    spec:
      containers:
      - name: jaeger
        image: jaegertracing/all-in-one:1.42
        ports:
        - containerPort: 5775
          protocol: UDP
        - containerPort: 6831
          protocol: UDP
        - containerPort: 6832
          protocol: UDP
        - containerPort: 5778
          protocol: TCP
        - containerPort: 16686
          protocol: TCP
        - containerPort: 14250
          protocol: TCP
        - containerPort: 14268
          protocol: TCP
        - containerPort: 14269
          protocol: TCP
        - containerPort: 4317
          protocol: TCP
        - containerPort: 4318
          protocol: TCP
        env:
        - name: SPAN_STORAGE_TYPE
          value: badger
        - name: BADGER_EPHEMERAL
          value: "false"
        - name: BADGER_DIRECTORY_VALUE
          value: "/badger/data"
        - name: BADGER_DIRECTORY_KEY
          value: "/badger/key"
        - name: COLLECTOR_OTLP_ENABLED
          value: "true"
        - name: LOG_LEVEL
          value: info
        livenessProbe:
          httpGet:
            path: "/"
            port: 14269
          initialDelaySeconds: 5
        readinessProbe:
          httpGet:
            path: "/"
            port: 14269
          initialDelaySeconds: 1
        volumeMounts:
        - name: badger-data
          mountPath: /badger
      volumes:
      - name: badger-data
        persistentVolumeClaim:
          claimName: jaeger-pvc

---
apiVersion: v1
kind: Service
metadata:
  name: jaeger-query
  namespace: observability
spec:
  ports:
  - name: query-http
    port: 16686
    protocol: TCP
    targetPort: 16686
  selector:
    app: jaeger
  type: ClusterIP

---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: jaeger-pvc
  namespace: observability
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 50Gi
  storageClassName: fast-ssd
```


## 4. Intelligent Alerts and Self-healing System

### 4.1 Machine Learning Driven Anomaly Detection

```python
# ml-anomaly-detection.py
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
import joblib
from typing import Dict, List, Tuple, Optional
import asyncio
import logging
from datetime import datetime, timedelta
import json

class MLAnomalyDetector:
    def __init__(self, model_name: str = "isolation_forest"):
        self.model_name = model_name
        self.model = None
        self.scaler = StandardScaler()
        self.feature_columns = []
        self.is_fitted = False
        self.logger = logging.getLogger(__name__)
        
    def prepare_features(self, metrics_data: pd.DataFrame) -> pd.DataFrame:
        """Prepare feature data"""
        # Select numerical indicators
        numeric_columns = metrics_data.select_dtypes(include=[np.number]).columns.tolist()
        
        # Remove timestamp column
        feature_columns = [col for col in numeric_columns if col != 'timestamp']
        self.feature_columns = feature_columns
        
        # Extract features
        features = metrics_data[feature_columns].copy()
        
        # Add derived features
        for col in feature_columns:
            if col.startswith(('cpu_', 'memory_', 'gpu_')):
                # Calculate rate of change
                features[f'{col}_rate'] = features[col].diff().fillna(0)
                # Calculate moving average
                features[f'{col}_ma_5'] = features[col].rolling(window=5, min_periods=1).mean()
                features[f'{col}_ma_15'] = features[col].rolling(window=15, min_periods=1).mean()
        
        return features
    
    def train(self, training_data: pd.DataFrame, contamination: float = 0.1) -> Dict:
        """Train anomaly detection model"""
        try:
            # Prepare features
            features = self.prepare_features(training_data)
            
            # Standardize
            scaled_features = self.scaler.fit_transform(features)
            
            # Train model
            self.model = IsolationForest(
                contamination=contamination,
                random_state=42,
                n_estimators=100
            )
            self.model.fit(scaled_features)
            
            self.is_fitted = True
            
            # Evaluate model
            predictions = self.model.predict(scaled_features)
            anomaly_rate = np.sum(predictions == -1) / len(predictions)
            
            return {
                "status": "success",
                "anomaly_rate": float(anomaly_rate),
                "training_samples": len(training_data),
                "features_used": len(self.feature_columns),
                "model_parameters": {
                    "contamination": contamination,
                    "n_estimators": 100
                }
            }
            
        except Exception as e:
            self.logger.error(f"Training failed: {e}")
            return {"status": "error", "message": str(e)}
    
    def predict(self, test_data: pd.DataFrame) -> Dict:
        """Predict anomalies"""
        if not self.is_fitted:
            raise ValueError("Model not trained yet")
        
        try:
            # Prepare features
            features = self.prepare_features(test_data)
            
            # Standardize
            scaled_features = self.scaler.transform(features)
            
            # Predict
            predictions = self.model.predict(scaled_features)
            anomaly_scores = self.model.decision_function(scaled_features)
            
            # Return result
            results = []
            for i, (pred, score) in enumerate(zip(predictions, anomaly_scores)):
                results.append({
                    "index": i,
                    "is_anomaly": pred == -1,
                    "anomaly_score": float(score),
                    "confidence": float(abs(score)),
                    "timestamp": test_data.iloc[i]['timestamp'] if 'timestamp' in test_data.columns else None
                })
            
            return {
                "predictions": results,
                "anomaly_count": int(np.sum(predictions == -1)),
                "anomaly_percentage": float(np.mean(predictions == -1) * 100)
            }
            
        except Exception as e:
            self.logger.error(f"Prediction failed: {e}")
            return {"status": "error", "message": str(e)}
    
    def save_model(self, filepath: str) -> bool:
        """save model"""
        try:
            model_data = {
                'model': self.model,
                'scaler': self.scaler,
                'feature_columns': self.feature_columns,
                'is_fitted': self.is_fitted
            }
            joblib.dump(model_data, filepath)
            return True
        except Exception as e:
            self.logger.error(f"Failed to save model: {e}")
            return False
    
    def load_model(self, filepath: str) -> bool:
        """load model"""
        try:
            model_data = joblib.load(filepath)
            self.model = model_data['model']
            self.scaler = model_data['scaler']
            self.feature_columns = model_data['feature_columns']
            self.is_fitted = model_data['is_fitted']
            return True
        except Exception as e:
            self.logger.error(f"Failed to load model: {e}")
            return False

class AlertCorrelationEngine:
    def __init__(self):
        self.alert_history = []
        self.correlation_window = timedelta(hours=1)
        self.logger = logging.getLogger(__name__)
    
    def correlate_alerts(self, new_alerts: List[Dict]) -> List[Dict]:
        """associate alert"""
        correlated_alerts = []
        
        for alert in new_alerts:
            # check related historical alerts
            related_alerts = self._find_related_alerts(alert)
            
            if related_alerts:
                # create associated alert
                correlated_alert = {
                    "alert_id": alert.get("alert_id"),
                    "type": "correlated",
                    "primary_alert": alert,
                    "related_alerts": related_alerts,
                    "correlation_score": self._calculate_correlation_score(alert, related_alerts),
                    "root_cause_analysis": self._analyze_root_cause(alert, related_alerts),
                    "recommended_actions": self._suggest_actions(alert, related_alerts)
                }
                correlated_alerts.append(correlated_alert)
            else:
                # single alert
                correlated_alerts.append({
                    "alert_id": alert.get("alert_id"),
                    "type": "isolated",
                    "alert": alert
                })
        
        # update history record
        self.alert_history.extend(new_alerts)
        self._cleanup_old_alerts()
        
        return correlated_alerts
    
    def _find_related_alerts(self, target_alert: Dict) -> List[Dict]:
        """find related alerts"""
        related = []
        target_time = datetime.fromisoformat(target_alert.get("timestamp", datetime.now().isoformat()))
        
        for historical_alert in self.alert_history:
            hist_time = datetime.fromisoformat(historical_alert.get("timestamp", datetime.now().isoformat()))
            
            # time window check
            if abs((target_time - hist_time).total_seconds()) <= self.correlation_window.total_seconds():
                # relevance check
                if self._are_alerts_related(target_alert, historical_alert):
                    related.append(historical_alert)
        
        return related
    
    def _are_alerts_related(self, alert1: Dict, alert2: Dict) -> bool:
        """determine if two alerts are related"""
        # relevance based on tags
        labels1 = set(alert1.get("labels", {}).keys())
        labels2 = set(alert2.get("labels", {}).keys())
        
        common_labels = labels1.intersection(labels2)
        if len(common_labels) >= 2:  # 至少有两个共同标签
            return True
        
        # relevance based on service
        service1 = alert1.get("labels", {}).get("service")
        service2 = alert2.get("labels", {}).get("service")
        if service1 and service2 and service1 == service2:
            return True
        
        # relevance based on node
        node1 = alert1.get("labels", {}).get("node")
        node2 = alert2.get("labels", {}).get("node")
        if node1 and node2 and node1 == node2:
            return True
        
        return False
    
    def _calculate_correlation_score(self, target_alert: Dict, related_alerts: List[Dict]) -> float:
        """calculate association score"""
        if not related_alerts:
            return 0.0
        
        scores = []
        target_labels = set(target_alert.get("labels", {}).keys())
        
        for related_alert in related_alerts:
            related_labels = set(related_alert.get("labels", {}).keys())
            common_labels = len(target_labels.intersection(related_labels))
            total_labels = len(target_labels.union(related_labels))
            
            if total_labels > 0:
                jaccard_similarity = common_labels / total_labels
                scores.append(jaccard_similarity)
        
        return float(np.mean(scores)) if scores else 0.0
    
    def _analyze_root_cause(self, target_alert: Dict, related_alerts: List[Dict]) -> Dict:
        """analyze root cause"""
        analysis = {
            "primary_indicators": [],
            "supporting_evidence": [],
            "likely_root_causes": []
        }
        
        # analyze key metrics
        target_severity = target_alert.get("labels", {}).get("severity", "")
        if target_severity == "critical":
            analysis["primary_indicators"].append("Critical alert level")
        
        # collect supporting evidence
        for related in related_alerts:
            evidence = {
                "alert": related.get("alertname", "Unknown"),
                "severity": related.get("labels", {}).get("severity", ""),
                "description": related.get("annotations", {}).get("description", "")
            }
            analysis["supporting_evidence"].append(evidence)
        
        # infer possible root causes
        services_involved = set()
        for alert in [target_alert] + related_alerts:
            service = alert.get("labels", {}).get("service")
            if service:
                services_involved.add(service)
        
        if len(services_involved) == 1:
            analysis["likely_root_causes"].append(f"Service {list(services_involved)[0]}'s problem")
        else:
            analysis["likely_root_causes"].append("Problems at the infrastructure level")
        
        return analysis
    
    def _suggest_actions(self, target_alert: Dict, related_alerts: List[Dict]) -> List[str]:
        """suggest action plan"""
        actions = []
        
        # Suggestion based on severity
        severity = target_alert.get("labels", {}).get("severity", "")
        if severity == "critical":
            actions.append("Immediately investigate and take emergency measures")
            actions.append("Notify relevant team leaders")
        
        # Suggestion based on alert type
        alert_name = target_alert.get("alertname", "")
        if "HighLatency" in alert_name:
            actions.append("check network connectivity and service dependencies")
        elif "HighErrorRate" in alert_name:
            actions.append("view application logs and error stacks")
        elif "HighCPULoad" in alert_name:
            actions.append("analyze CPU usage patterns and process activities")
        
        # Suggestion based on associated alerts
        if related_alerts:
            actions.append("conduct comprehensive analysis of correlated alerts")
            actions.append("check utilization of shared resources")
        
        return actions
    
    def _cleanup_old_alerts(self):
        """Clean old alert records"""
        cutoff_time = datetime.now() - timedelta(days=7)
        self.alert_history = [
            alert for alert in self.alert_history
            if datetime.fromisoformat(alert.get("timestamp", datetime.now().isoformat())) > cutoff_time
        ]

# Usage Example
async def main():
    # Simulate monitoring data
    timestamps = pd.date_range(start='2024-01-01', periods=1000, freq='5T')
    metrics_data = pd.DataFrame({
        'timestamp': timestamps,
        'cpu_utilization': np.random.normal(50, 15, 1000),
        'memory_utilization': np.random.normal(60, 20, 1000),
        'gpu_utilization': np.random.normal(70, 25, 1000),
        'request_latency': np.random.exponential(0.1, 1000),
        'error_rate': np.random.beta(1, 50, 1000)  # 低错误率
    })
    
    # Inject some abnormal data
    anomaly_indices = np.random.choice(1000, 20, replace=False)
    metrics_data.loc[anomaly_indices, 'cpu_utilization'] += 40
    metrics_data.loc[anomaly_indices, 'request_latency'] *= 5
    
    # Train model
    detector = MLAnomalyDetector()
    training_result = detector.train(metrics_data.head(800))
    print(f"Training result: {training_result}")
    
    # Abnormal prediction
    test_data = metrics_data.tail(200)
    prediction_result = detector.predict(test_data)
    print(f"Anomalies detected: {prediction_result['anomaly_count']} "
          f"({prediction_result['anomaly_percentage']:.1f}%)")
    
    # Alert association analysis
    engine = AlertCorrelationEngine()
    
    sample_alerts = [
        {
            "alert_id": "alert_001",
            "alertname": "HighCPULoad",
            "labels": {"severity": "warning", "service": "llm-inference", "node": "node-01"},
            "annotations": {"description": "CPU usage exceeds 80%"},
            "timestamp": datetime.now().isoformat()
        },
        {
            "alert_id": "alert_002",
            "alertname": "HighLatency",
            "labels": {"severity": "warning", "service": "llm-inference", "node": "node-01"},
            "annotations": {"description": "request latency exceeds 1 second"}
            "timestamp": (datetime.now() - timedelta(minutes=5)).isoformat()
        }
    ]
    
    correlated_results = engine.correlate_alerts(sample_alerts)
    print(f"\nCorrelated alerts: {len(correlated_results)}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```


## 5. Production-Level Observability Best Practices

---


## Obsidian Related Documentation

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Open Source Project Index
- AI Infrastructure Architecture
- 132 - AI/ML Workload Operations (AI/ML Workloads Operations)
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management

## See Also

- 34-federated-learning
- 35-model-drift-monitoring
- 37-agent-sandbox-security
- 99-kubeflow-ai-platform-guide

## Related

- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Observability knowledge graph index]]


<!-- risk-assessed -->
