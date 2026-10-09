---
title: AI Model Deployment and Lifecycle Management
description: '# AI Model Deployment and Lifecycle Management'
summary: 'serving.kserve.io/inferenceservice: enabled'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- prometheus
- istio
- minio
- postgresql
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
- What is AI Model Deployment and Lifecycle Management
- How to do AI Model Deployment and Lifecycle Management
- Kubernetes 11 ai infra best practices
trigger_keywords:
- AI Model Deployment and Lifecycle Management
- ai
- infra
prerequisites:
- kubectl-basics
- service-mesh-basics
- prometheus-basics
- gpu-scheduling-basics
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
- type: fta
  path: ../domain-10-troubleshooting-diagnostics/topic-fta/list/deployment-fta.md
  label: 'Fault Tree: deployment'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/10-model-deployment-management.md
---

> **Production Environment Security Tips**
>
> Commands included in this document can be directly executed. Before executing, please confirm: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify the cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information collection with no side effects).




# AI Model Deployment and Lifecycle Management

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **Last Updated**: 2026-02 | **References**: [[entities/kserve.md|KServe]](https://kserve.github.io/website/) | [Seldon Core](https://docs.seldon.io/projects/seldon-core/) | [BentoML](https://docs.bentoml.org/)


## 1. Model Deployment Architecture Overview

### 1.1 Production-Level Model Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                        AI Model Deployment Architecture                             │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                            Model Management Platform (Model Management)                      │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │  Model      │  │  Model      │  │  Model      │  │  Model      │          │  │
│  │  │  Registry   │  │  Versioning │  │  Metadata   │  │  Governance │          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  │ • Storage Management   │  │ • Version Control   │  │ • Metadata    │  │ • Audit Tracking   │          │  │
│  │  │ • Permission Control   │  │ • Lineage Relationship   │  │ • Tagging Classification   │  │ • Compliance Check   │          │  │
│  │  │ • Search Discovery   │  │ • A/B Testing    │  │ • Performance Metrics   │  │ • Security Scan   │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └─────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                          Deployment Orchestration Layer (Deployment Orchestration)                 │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │   KServe    │  │ Seldon Core │  │  BentoML    │  │  Custom     │          │  │
│  │  │             │  │             │  │             │  │  Operator   │          │  │
│  │  │ • Inference │  │ • Graph     │  │ • Serving   │  │ • Domain    │          │  │
│  │  │ • Canary    │  │ • Ensemble  │  │ • Batch     │  │ • Specific  │          │  │
│  │  │ • Blue/Green│  │ • Explain   │  │ • Streaming │  │ • Logic     │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └─────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                          Service Management Layer (Service Management)                       │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │   Service   │  │   Gateway   │  │   Traffic   │  │   Security  │          │  │
│  │  │   Mesh      │  │   (Istio)   │  │   Control   │  │   (mTLS)    │          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  │ • Service Discovery   │  │ • Routing Management   │  │ • Load Balancing   │  │ • Authentication   │          │  │
│  │  │ • Traffic Governance   │  │ • Circuit Breaker Degradation   │  │ • Failover   │  │ • Authorization Authentication   │          │  │
│  │  │ • Link Tracing   │  │ • Rate Limiting Control   │  │ • Health Checks   │  │ • Encryption Transmission   │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └─────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                          Infrastructure Layer (Infrastructure)                          │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │   K8s       │  │    GPU      │  │   Storage   │  │   Network   │          │  │
│  │  │   Cluster   │  │   Nodes     │  │   System    │  │   Fabric    │          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  │ • Scheduling Management   │  │ • Resource Pool    │  │ • PVC/PV    │  │ • CNI Plugin    │          │  │
│  │  │ • Auto Scaling   │  │ • Topology Optimization   │  │ • Snapshot Backup   │  │ • RDMA Network   │          │  │
│  │  │ • Fault Recovery   │  │ • Power Management   │  │ • Cache Acceleration   │  │ • Load Balancing   │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Deployment Mode Comparison

| Deployment Mode | Applicable Scenarios | Advantages | Disadvantages | Complexity |
|----------|----------|------|------|--------|
| **Serverless** | Sudden traffic, development/test | Auto-scaling, cost optimization | Cold start delay | ⭐⭐ |
| **Deployment** | Stable online services | Simple and reliable, easy to debug | Resource waste | ⭐ |
| **[[StatefulSet|StatefulSet]]** | Stateful model services | Data persistence, ordered deployment | High complexity | ⭐⭐⭐ |
| **[[DaemonSet|DaemonSet]]** | Node-local services | Local caching, low latency | Low resource utilization | ⭐⭐ |
| **Job/CronJob** | Batch inference | One-time tasks, scheduled execution | Not suitable for online services | ⭐⭐ |

---


## 2. KServe Production Deployment

### 2.1 Complete Deployment Configuration

```yaml
# kserve-production.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: ai-models
  labels:
    istio-injection: enabled
    serving.kserve.io/inferenceservice: enabled
---
# Core Components of KServe
apiVersion: operator.kserve.io/v1alpha1
kind: KServe
metadata:
  name: kserve-instance
  namespace: ai-models
spec:
  # Enable Components
  inferenceService:
    enabled: true
    resources:
      limits:
        cpu: "2"
        memory: 4Gi
      requests:
        cpu: "1"
        memory: 2Gi
        
  # Model Proxy Configuration
  agent:
    enabled: true
    resources:
      limits:
        cpu: "500m"
        memory: 1Gi
      requests:
        cpu: "250m"
        memory: 512Mi
        
  # Storage Initializer
  storageInitializer:
    enabled: true
    image: kserve/storage-initializer:v0.12.0
    resources:
      limits:
        cpu: "500m"
        memory: 1Gi
      requests:
        cpu: "250m"
        memory: 512Mi
---
# InferenceService Example - LLM Inference
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: llama3-70b-inference
  namespace: ai-models
  annotations:
    # Enable Canary Deployment
    autoscaling.knative.dev/class: kpa.autoscaling.knative.dev
    autoscaling.knative.dev/metric: concurrency
    autoscaling.knative.dev/target: "10"
    autoscaling.knative.dev/minScale: "2"
    autoscaling.knative.dev/maxScale: "20"
spec:
  predictor:
    # Model Version Management
    model:
      modelFormat:
        name: pytorch
        version: "2.1"
      runtime: kserve-lgbserver
      storageUri: s3://models-store/llama3/70b/v1.2
      protocolVersion: v2
      resources:
        limits:
          cpu: "8"
          memory: 64Gi
          nvidia.com/gpu: "4"
        requests:
          cpu: "4"
          memory: 32Gi
          nvidia.com/gpu: "4"
      env:
        - name: MODEL_NAME
          value: llama3-70b
        - name: TRANSFORMERS_CACHE
          value: /cache
        - name: HF_TOKEN
          valueFrom:
            secretKeyRef:
              name: huggingface-secret
              key: token
              
  # Transformer Preprocessing
  transformer:
    containers:
      - image: custom/llm-transformer:v1.0
        name: transformer
        ports:
          - containerPort: 8080
            protocol: TCP
        env:
          - name: PREPROCESS_CONFIG
            value: "config/preprocess.yaml"
        resources:
          limits:
            cpu: "2"
            memory: 4Gi
          requests:
            cpu: "1"
            memory: 2Gi
            
  # explainer Configuration
  explainer:
    type: LIME
    containers:
      - image: kserve/alibi-explainer:v0.12.0
        name: explainer
        env:
          - name: EXPLAINER_MODEL_NAME
            value: llama3-70b
```

### 2.2 Model Version Management Strategy

```yaml
# model-versioning-strategy.yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: model-canary-deployment
  namespace: ai-models
spec:
  # Blue-Green Deployment Configuration
  predictor:
    canaryTrafficPercent: 10  # 10%流量到新版本
    model:
      # Current Stable Version
      stable:
        name: llama3-70b-v1.0
        storageUri: s3://models/llama3-70b/v1.0
        resources:
          requests:
            nvidia.com/gpu: "4"
            
      # New Candidate Version
      canary:
        name: llama3-70b-v1.1
        storageUri: s3://models/llama3-70b/v1.1
        resources:
          requests:
            nvidia.com/gpu: "4"
            
  # A/B Testing Configuration
  router:
    traffic:
      - revisionName: llama3-70b-v1.0
        percent: 70
        headers:
          x-test-group: control
      - revisionName: llama3-70b-v1.1
        percent: 30
        headers:
          x-test-group: treatment
```

---


## 3. Model Registry Center Construction

### 3.1 MLflow Model Registry

```yaml
# mlflow-registry.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mlflow-server
  namespace: ai-models
spec:
  replicas: 2
  selector:
    matchLabels:
      app: mlflow
  template:
    metadata:
      labels:
        app: mlflow
    spec:
      containers:
      - name: mlflow
        image: ghcr.io/mlflow/mlflow:2.9.2
        ports:
        - containerPort: 5000
        env:
        - name: MLFLOW_S3_ENDPOINT_URL
          value: "http://minio:9000"
        - name: AWS_ACCESS_KEY_ID
          valueFrom:
            secretKeyRef:
              name: minio-secret
              key: access-key
        - name: AWS_SECRET_ACCESS_KEY
          valueFrom:
            secretKeyRef:
              name: minio-secret
              key: secret-key
        - name: MLFLOW_BACKEND_STORE_URI
          value: "postgresql://mlflow:password@postgres-mlflow:5432/mlflow"
        volumeMounts:
        - name: models-volume
          mountPath: /mlflow-artifacts
        resources:
          requests:
            cpu: "1"
            memory: 2Gi
          limits:
            cpu: "2"
            memory: 4Gi
---
apiVersion: v1
kind: Service
metadata:
  name: mlflow-service
  namespace: ai-models
spec:
  selector:
    app: mlflow
  ports:
  - port: 5000
    targetPort: 5000
  type: ClusterIP
```

### 3.2 Model Metadata Management

```python
# model_metadata_manager.py
import mlflow
from datetime import datetime
from typing import Dict, Any

class ModelMetadataManager:
    def __init__(self):
        self.client = mlflow.tracking.MlflowClient()
        
    def register_model_with_metadata(self, 
                                   model_uri: str,
                                   model_name: str,
                                   metadata: Dict[str, Any]):
        """Register the model and attach metadata"""
        
        # Register the model
        model_version = mlflow.register_model(model_uri, model_name)
        
        # Add custom tags
        self.client.set_model_version_tag(
            name=model_name,
            version=model_version.version,
            key="framework",
            value=metadata.get("framework", "unknown")
        )
        
        self.client.set_model_version_tag(
            name=model_name,
            version=model_version.version,
            key="gpu_memory_required",
            value=str(metadata.get("gpu_memory_gb", 0))
        )
        
        self.client.set_model_version_tag(
            name=model_name,
            version=model_version.version,
            key="inference_latency_ms",
            value=str(metadata.get("latency_ms", 0))
        )
        
        # Record performance metrics
        with mlflow.start_run():
            mlflow.log_params({
                "model_name": model_name,
                "version": model_version.version,
                "registered_at": datetime.now().isoformat(),
                **metadata.get("performance_metrics", {})
            })
            
        return model_version

# Usage Examples
manager = ModelMetadataManager()
model_info = manager.register_model_with_metadata(
    model_uri="runs:/abcd1234/model",
    model_name="llama3-70b",
    metadata={
        "framework": "pytorch",
        "gpu_memory_gb": 80,
        "latency_ms": 150,
        "performance_metrics": {
            "accuracy": 0.95,
            "throughput": 50,
            "max_tokens": 4096
        }
    }
)
```

---


## 4. Deployment Pipeline Automation

### 4.1 CI/CD Pipeline Configuration

```yaml
# .github/workflows/model-deployment.yaml
name: Model Deployment Pipeline
on:
  push:
    branches: [main]
    paths:
      - 'models/**'
  workflow_dispatch:

jobs:
  model-validation:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
        
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest mlflow
    
    - name: Run model validation
      run: |
        pytest tests/model_validation/
        
    - name: Performance benchmark
      run: |
        python scripts/benchmark_model.py --model-path ./model
    
  deploy-staging:
    needs: model-validation
    runs-on: ubuntu-latest
    environment: staging
    steps:
    - uses: actions/checkout@v4
    
    - name: Deploy to staging
      run: |
        # Deploy to Staging Environment
        kubectl apply -f k8s/staging/model-deployment.yaml
        kubectl rollout status deployment/model-staging
        
    - name: Run integration tests
      run: |
        pytest tests/integration/ --env staging
        
  canary-deployment:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production
    steps:
    - uses: actions/checkout@v4
    
    - name: Deploy canary release
      run: |
        # Update Canary Traffic Percentage
        kubectl patch inferenceservice model-production \
          -p '{"spec":{"predictor":{"canaryTrafficPercent": 10}}}' \
          --type=merge
          
    - name: Monitor canary metrics
      run: |
        # Monitor key metrics
        python scripts/monitor_canary.py --duration 30m
        
    - name: Promote to production
      if: success()
      run: |
        # Full-scale launch
        kubectl patch inferenceservice model-production \
          -p '{"spec":{"predictor":{"canaryTrafficPercent": 100}}}' \
          --type=merge
```

### 4.2 Deployment Quality Gates

```python
# deployment_gate.py
import requests
import time
from typing import Dict, List

class DeploymentQualityGate:
    def __init__(self, service_endpoint: str, thresholds: Dict):
        self.endpoint = service_endpoint
        self.thresholds = thresholds
        self.metrics_client = self._setup_metrics_client()
        
    def _setup_metrics_client(self):
        """Initialize monitoring client"""
        # Connect to Prometheus or other monitoring systems
        pass
        
    def check_deployment_health(self) -> bool:
        """Check the health of the deployment"""
        checks = [
            self._check_endpoint_availability(),
            self._check_response_time(),
            self._check_error_rate(),
            self._check_resource_utilization(),
            self._check_business_metrics()
        ]
        
        return all(checks)
        
    def _check_endpoint_availability(self) -> bool:
        """Check the availability of service endpoints"""
        try:
            response = requests.get(f"{self.endpoint}/health", timeout=5)
            return response.status_code == 200
        except Exception:
            return False
            
    def _check_response_time(self) -> bool:
        """Check response time"""
        # Retrieve P99 latency from the monitoring system
        p99_latency = self.metrics_client.query("histogram_quantile(0.99, ...)")
        return p99_latency <= self.thresholds.get("max_latency_ms", 500)
        
    def _check_error_rate(self) -> bool:
        """Check error rate"""
        error_rate = self.metrics_client.query("rate(http_requests_total{status=~'5..'}[5m])")
        return error_rate <= self.thresholds.get("max_error_rate", 0.01)
        
    def _check_resource_utilization(self) -> bool:
        """Check resource utilization"""
        # Check CPU, memory, GPU utilization
        gpu_util = self.metrics_client.query("avg(DCGM_FI_DEV_GPU_UTIL)")
        return gpu_util >= self.thresholds.get("min_gpu_utilization", 30)
        
    def _check_business_metrics(self) -> bool:
        """Check business metrics"""
        # Check accuracy, recall rates, and other business metrics
        accuracy = self.metrics_client.query("model_accuracy")
        return accuracy >= self.thresholds.get("min_accuracy", 0.9)

# Usage Example
gate = DeploymentQualityGate(
    service_endpoint="http://model-service.ai-models",
    thresholds={
        "max_latency_ms": 300,
        "max_error_rate": 0.005,
        "min_gpu_utilization": 40,
        "min_accuracy": 0.92
    }
)

if gate.check_deployment_health():
    print("✅ Deployment quality check passed")
else:
    print("❌ Deployment quality check failed")
    # Rollback operation
```

---


## 5. Fault Recovery and Disaster Recovery

### 5.1 Automatic Fault Detection

```yaml
# fault-detection.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: model-health-checker
  namespace: ai-models
spec:
  replicas: 1
  selector:
    matchLabels:
      app: health-checker
  template:
    metadata:
      labels:
        app: health-checker
    spec:
      containers:
      - name: health-checker
        image: custom/model-health-checker:v1.0
        env:
        - name: TARGET_SERVICES
          value: "llama3-inference,llm-router,model-registry"
        - name: CHECK_INTERVAL
          value: "30s"
        - name: FAILURE_THRESHOLD
          value: "3"
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
---
# Health check script
apiVersion: batch/v1
kind: CronJob
metadata:
  name: periodic-model-validation
  namespace: ai-models
spec:
  schedule: "*/15 * * * *"  # 每15分钟执行一次
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: validator
            image: custom/model-validator:v1.0
            command:
            - python
            - /scripts/validate_models.py
            env:
            - name: VALIDATION_DATASET
              value: "s3://datasets/validation/latest"
            - name: ALERT_WEBHOOK
              value: "https://hooks.slack.com/services/..."
            resources:
              requests:
                cpu: "500m"
                memory: "1Gi"
          restartPolicy: OnFailure
```

### 5.2 Automatic Rollback Strategy

```python
# auto_rollback.py
import logging
import time
from kubernetes import client, config
from prometheus_api_client import PrometheusConnect

logger = logging.getLogger(__name__)

class AutoRollbackManager:
    def __init__(self, service_name: str, namespace: str):
        config.load_kube_config()
        self.apps_v1 = client.AppsV1Api()
        self.prometheus = PrometheusConnect(url="http://prometheus:9090")
        self.service_name = service_name
        self.namespace = namespace
        
    def monitor_and_rollback(self, deployment_name: str, rollback_window_minutes: int = 10):
        """Monitor the deployment and automatically roll back if issues arise"""
        
        # Get the current deployment status
        deployment = self.apps_v1.read_namespaced_deployment(deployment_name, self.namespace)
        current_replicas = deployment.spec.replicas
        
        # Monitor metrics within the monitoring window
        start_time = time.time() - (rollback_window_minutes * 60)
        
        while time.time() - start_time < (rollback_window_minutes * 60):
            if self._should_rollback(deployment_name):
                logger.warning(f"Detected abnormality, triggering automatic rollback: {deployment_name}")
                self._perform_rollback(deployment_name)
                return True
                
            time.sleep(30)  # 每30秒检查一次
            
        logger.info(f"Deployment stable, no need to rollback: {deployment_name}")
        return False
        
    def _should_rollback(self, deployment_name: str) -> bool:
        """Determine if a rollback is needed"""
        
        # check error rate
        error_query = f'sum(rate(http_requests_total{{deployment="{deployment_name}",status=~"5.."}}[5m]))'
        error_rate = self._query_prometheus(error_query)
        if error_rate > 0.05:  # 错误率超过5%
            logger.warning(f"Error rate too high: {error_rate}")
            return True
            
        # check latency
        latency_query = f'histogram_quantile(0.99, rate(http_request_duration_seconds_bucket{{deployment="{deployment_name}"}}[5m]))'
        latency_99 = self._query_prometheus(latency_query)
        if latency_99 > 2.0:  # P99延迟超过2秒
            logger.warning(f"Too high latency: {latency_99}s")
            return True
            
        # check availability
        availability_query = f'avg(up{{deployment="{deployment_name}"}})'
        availability = self._query_prometheus(availability_query)
        if availability < 0.95:  # 可用性低于95%
            logger.warning(f"Not enough availability: {availability}")
            return True
            
        return False
        
    def _perform_rollback(self, deployment_name: str):
        """execute rollback operation"""
        try:
            # roll back to previous version
            rollback_body = {
                "kind": "DeploymentRollback",
                "apiVersion": "apps/v1",
                "name": deployment_name
            }
            
            self.apps_v1.create_namespaced_deployment_rollback(
                name=deployment_name,
                namespace=self.namespace,
                body=rollback_body
            )
            
            logger.info(f"Successfully rolled back deployment: {deployment_name}")
            
            # send alert notification
            self._send_alert_notification(deployment_name, "automatic_rollback")
            
        except Exception as e:
            logger.error(f"Rollback failed: {e}")
            raise
            
    def _query_prometheus(self, query: str) -> float:
        """query Prometheus metrics"""
        try:
            result = self.prometheus.custom_query(query=query)
            if result and len(result) > 0:
                return float(result[0]['value'][1])
            return 0.0
        except Exception as e:
            logger.error(f"Prometheus query failed: {e}")
            return 0.0
            
    def _send_alert_notification(self, deployment_name: str, reason: str):
        """send alert notification"""
        # implement notification logic (Slack, email, etc.)
        pass

# usage example
rollback_manager = AutoRollbackManager("llama3-inference", "ai-models")
rollback_manager.monitor_and_rollback("llama3-inference-deployment", rollback_window_minutes=15)
```

---


## 6. Best Practices for Operations

### 6.1 Deployment Checklist

✅ **Pre-deployment Checks**
- [ ] All validation tests pass for the model
- [ ] Performance benchmark testing is complete
- [ ] Security scans and vulnerability checks pass
- [ ] Cost assessment and budget approval are completed
- [ ] Rollback plans are formulated and tested

✅ **During Deployment**
- [ ] Canary traffic is gradually increased
- [ ] Key metrics are monitored in real time
- [ ] User feedback is promptly collected
- [ ] Abnormal situations are quickly responded to
- [ ] Deploy full logging records

✅ **Deploy and validate**
- [ ] Functional tests pass
- [ ] Performance metrics meet standards
- [ ] User experience is good
- [ ] Alerts are functioning normally
- [ ] Documentation is updated

### 6.2 Common Issue Handling

**Model loading fails**

> ⚠️ **🟡 Medium-risk change** — Change cluster resource state, suggest first running --dry-run or diff to confirm
> - `kubectl exec`: Enter container to execute commands, which may alter container state

``` bash
# 🟡 Medium risk: modifies cluster/resource state, confirm target, impact scope, and authorization before execution
# check storage access permissions
kubectl get pvc -n ai-models
kubectl describe pv <pv-name>

# verify model file integrity
kubectl exec -it <pod-name> -n ai-models -- ls -la /mnt/models/

# view load logs
kubectl logs <pod-name> -n ai-models -c model-loader
```
**Inference performance drops**

> ⚠️ **🟡 Medium-risk change** — Change cluster resource state, suggest first running --dry-run or diff to confirm
> - `kubectl exec`: Enter container to execute commands, which may alter container state

``` bash
# 🟡 Medium risk: modifies cluster/resource state, confirm target, impact scope, and authorization before execution
# check GPU resource usage
kubectl top nodes --selector=nvidia.com/gpu.present=true
dcgmi dmon -e 1001,1002,1003 -i 0

# analyze bottlenecks
kubectl exec -it <pod-name> -n ai-models -- nvidia-smi
kubectl exec -it <pod-name> -n ai-models -- nvtop
```
**Deployment stalls not progressing**
``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
# check deployment status
kubectl describe deployment <deployment-name> -n ai-models
kubectl get events --field-selector involvedObject.name=<deployment-name>

# view pod status details
kubectl describe pods -l app=<app-name> -n ai-models
```
---

---


## Obsidian Related Documentation

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Open Source Project Index
- AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed training frameworks
- AI data processing Pipeline and feature engineering
- AI experiment management and MLOps platform
- AutoML and hyperparameter tuning
- AI model registration center and version management

## See Also

- 08-automl-hyperparameter-tuning
- 09-model-registry
- 11-ai-security-model-protection
- 12-ai-cost-analysis-finops

## Related

- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Knowledge Graph Index]]


<!-- risk-assessed -->
