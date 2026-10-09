---
title: 24 - LLM Model Version Management and Governance
description: '# 24 - LLM Model Version Management and Governance'
summary: 'preferredDuringSchedulingIgnoredDuringExecution:'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- prometheus
- postgresql
- statefulset
- ingress
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
- What is LLM Model Version Management and Governance
- How to manage LLM Model Version Management and Governance
- Kubernetes 11 AI Infrastructure Best Practices
trigger_keywords:
- LLM Model Version Management and Governance
- ai
- infra
prerequisites:
- kubectl-basics
- prometheus-basics
- gpu-scheduling-basics
- tls-basics
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
source_path: tree/infrastructure/kubernetes/ai/infrastructure/24-llm-model-versioning.md
---

> **Production Environment Security Tips**
>
> Commands included in this document can be directly executed. Before execution, please confirm: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information collection with no side effects).




# 24 - LLM Model Version Management and Governance

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **Difficulty**: Expert Level | **Reference**: [MLflow](https://mlflow.org/) | [DVC](https://dvc.org/) | [HuggingFace Hub](https://huggingface.co/) | CNCF Model Registry


## 1. Enterprise-Level Model Version Governance System

### 1.1 Model Lifecycle Management Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                     Enterprise Model Lifecycle Management                           │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                           Model Development Phase                             │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │ Experiment  │  │ Training    │  │ Validation  │  │ Model       │          │  │
│  │  │ Tracking    │  │ Pipeline    │  │ Testing     │  │ Registration │          │  │
│  │  │ (MLflow)    │  │ (Kubeflow)  │  │ (Unit Test) │  │ (Registry)   │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                           Model Staging Phase                                 │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │ A/B Testing │  │ Performance │  │ Security    │  │ Compliance  │          │  │
│  │  │ (Canary)    │  │ Benchmark   │  │ Scanning    │  │ Check       │          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                           Model Production Phase                              │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │ Deployment  │  │ Monitoring  │  │ Auto        │  │ Rollback    │          │  │
│  │  │ (Blue/Green)│  │ (Prometheus)│  │ Promotion   │  │ (Automated) │          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Enterprise-Level Version Management Strategies

| Strategy Dimension | Implementation Points | Technical Implementation | Operational Considerations |
|----------|----------|----------|----------|
| **Semantic Versioning** | MAJOR.MINOR.PATCH | Git tag + MLflow version | Automated version generation |
| **Branch Strategy** | Git Flow + model branch | feature/model-* branches | Branch merging review |
| **Environment Isolation** | dev/staging/prod three environments | Namespace isolation | Resource quota management |
| **Approval Process** | Multi-level approval mechanism | GitOps + Approvals | Approval time control |
| **Rollback Mechanism** | One-click rollback + progressive | Blue/Green + Canary | Rollback window time |
| **Audit Tracing** | Complete change logs | Git commits + MLflow logs | Compliance requirements |


## 2. MLflow Enterprise Deployment

### 2.1 High-Availability MLflow Architecture

```yaml
# mlflow-production-deployment.yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mlflow-postgres-primary
  namespace: mlflow
spec:
  serviceName: mlflow-postgres
  replicas: 3
  selector:
    matchLabels:
      app: mlflow-postgres
      role: primary
  template:
    metadata:
      labels:
        app: mlflow-postgres
        role: primary
    spec:
      containers:
      - name: postgres
        image: postgres:15-alpine
        env:
        - name: POSTGRES_DB
          value: mlflow
        - name: POSTGRES_USER
          valueFrom:
            secretKeyRef:
              name: mlflow-db-secret
              key: username
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mlflow-db-secret
              key: password
        - name: PGDATA
          value: /var/lib/postgresql/data/pgdata
        ports:
        - containerPort: 5432
        volumeMounts:
        - name: postgres-storage
          mountPath: /var/lib/postgresql/data
        resources:
          requests:
            cpu: "1"
            memory: "2Gi"
          limits:
            cpu: "2"
            memory: "4Gi"
        livenessProbe:
          exec:
            command:
            - pg_isready
            - -U
            - postgres
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          exec:
            command:
            - pg_isready
            - -U
            - postgres
          initialDelaySeconds: 5
          periodSeconds: 5
  volumeClaimTemplates:
  - metadata:
      name: postgres-storage
    spec:
      accessModes: ["ReadWriteOnce"]
      resources:
        requests:
          storage: 100Gi
      storageClassName: fast-ssd

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mlflow-server
  namespace: mlflow
spec:
  replicas: 5
  selector:
    matchLabels:
      app: mlflow-server
  template:
    metadata:
      labels:
        app: mlflow-server
    spec:
      containers:
      - name: mlflow
        image: ghcr.io/mlflow/mlflow:v2.10.0
        command:
        - mlflow
        - server
        - --host=0.0.0.0
        - --port=5000
        - --backend-store-uri=postgresql://$(DB_USER):$(DB_PASS)@mlflow-postgres-headless:5432/mlflow
        - --default-artifact-root=s3://mlflow-artifacts-production/
        - --workers=4
        env:
        - name: DB_USER
          valueFrom:
            secretKeyRef:
              name: mlflow-db-secret
              key: username
        - name: DB_PASS
          valueFrom:
            secretKeyRef:
              name: mlflow-db-secret
              key: password
        - name: AWS_ACCESS_KEY_ID
          valueFrom:
            secretKeyRef:
              name: mlflow-s3-secret
              key: access-key
        - name: AWS_SECRET_ACCESS_KEY
          valueFrom:
            secretKeyRef:
              name: mlflow-s3-secret
              key: secret-key
        - name: MLFLOW_S3_ENDPOINT_URL
          value: "https://s3.amazonaws.com"
        ports:
        - containerPort: 5000
        resources:
          requests:
            cpu: "500m"
            memory: "1Gi"
          limits:
            cpu: "1"
            memory: "2Gi"
        livenessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 60
          periodSeconds: 30
        readinessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 30
          periodSeconds: 10
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - mlflow-server
              topologyKey: kubernetes.io/hostname

---
apiVersion: v1
kind: Service
metadata:
  name: mlflow-service
  namespace: mlflow
spec:
  selector:
    app: mlflow-server
  ports:
  - port: 80
    targetPort: 5000
  type: LoadBalancer
  loadBalancerSourceRanges:
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mlflow-ingress
  namespace: mlflow
  annotations:
    nginx.ingress.kubernetes.io/auth-type: basic
    nginx.ingress.kubernetes.io/auth-secret: mlflow-basic-auth
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
  - hosts:
    - mlflow.company.com
    secretName: mlflow-tls
  rules:
  - host: mlflow.company.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: mlflow-service
            port:
              number: 80
```

### 2.2 Model Registration and Metadata Management

```python
# enterprise_model_registry.py
import mlflow
from mlflow.entities import ViewType
from mlflow.tracking import MlflowClient
from datetime import datetime, timedelta
import json
import yaml
from typing import Dict, List, Optional
import pandas as pd
from dataclasses import dataclass

@dataclass
class ModelMetadata:
    """model metadata structure"""
    model_name: str
    version: str
    description: str
    author: str
    team: str
    created_at: datetime
    training_dataset: str
    dataset_version: str
    hyperparameters: Dict
    performance_metrics: Dict
    hardware_requirements: Dict
    deployment_targets: List[str]
    compliance_tags: List[str]
    dependencies: List[str]
    model_card: str

class EnterpriseModelRegistry:
    def __init__(self, tracking_uri: str, registry_uri: str = None):
        self.client = MlflowClient(tracking_uri=tracking_uri)
        mlflow.set_tracking_uri(tracking_uri)
        if registry_uri:
            mlflow.set_registry_uri(registry_uri)
        
    def register_model_with_governance(self, 
                                     model_uri: str, 
                                     model_name: str,
                                     metadata: ModelMetadata) -> str:
        """register the model and apply governance policies"""
        
        # start the registration process
        with mlflow.start_run() as run:
            # record model metadata
            self._log_model_metadata(metadata)
            
            # record performance metrics
            for metric_name, value in metadata.performance_metrics.items():
                mlflow.log_metric(metric_name, value)
            
            # record hyperparameters
            mlflow.log_params(metadata.hyperparameters)
            
            # record dependencies
            mlflow.log_dict(
                {"dependencies": metadata.dependencies},
                "requirements.json"
            )
            
            # register the model
            model_info = mlflow.register_model(
                model_uri=model_uri,
                name=model_name,
                tags={
                    "team": metadata.team,
                    "author": metadata.author,
                    "compliance": ",".join(metadata.compliance_tags),
                    "hardware": json.dumps(metadata.hardware_requirements)
                }
            )
            
            # create the model card
            self._create_model_card(model_info, metadata)
            
            # trigger governance checks
            governance_passed = self._run_governance_checks(model_info, metadata)
            
            if governance_passed:
                # automatically advance to Staging
                self.client.transition_model_version_stage(
                    name=model_name,
                    version=model_info.version,
                    stage="Staging"
                )
                print(f"Model {model_name} v{model_info.version} registered and moved to Staging")
            else:
                print(f"Model {model_name} v{model_info.version} failed governance checks")
                
            return f"{model_name}/{model_info.version}"
    
    def _log_model_metadata(self, metadata: ModelMetadata):
        """record model metadata"""
        # record core metadata
        mlflow.set_tag("model.description", metadata.description)
        mlflow.set_tag("model.author", metadata.author)
        mlflow.set_tag("model.team", metadata.team)
        mlflow.set_tag("model.dataset", metadata.training_dataset)
        mlflow.set_tag("model.dataset_version", metadata.dataset_version)
        
        # record hardware requirements
        mlflow.set_tag("hardware.cpu", metadata.hardware_requirements.get("cpu", "unknown"))
        mlflow.set_tag("hardware.memory", metadata.hardware_requirements.get("memory", "unknown"))
        mlflow.set_tag("hardware.gpu", metadata.hardware_requirements.get("gpu", "none"))
        
        # record compliance tags
        mlflow.set_tag("compliance.tags", ",".join(metadata.compliance_tags))
        
    def _create_model_card(self, model_info, metadata: ModelMetadata):
        """create the model card"""
        model_card = {
            "model_identity": {
                "name": metadata.model_name,
                "version": metadata.version,
                "created_at": metadata.created_at.isoformat(),
                "author": metadata.author,
                "team": metadata.team
            },
            "model_details": {
                "description": metadata.description,
                "version": metadata.version,
                "license": "Apache 2.0",
                "contact": f"{metadata.author}@company.com"
            },
            "datasets": {
                "training_data": {
                    "name": metadata.training_dataset,
                    "version": metadata.dataset_version,
                    "description": "Training dataset used for model development"
                }
            },
            "testing": {
                "performance_metrics": metadata.performance_metrics,
                "validation_approach": "Cross-validation with holdout set"
            },
            "model_parameters": {
                "hyperparameters": metadata.hyperparameters,
                "model_architecture": "Transformer-based"
            },
            "considerations": {
                "limitations": [
                    "Performance may vary with out-of-distribution data",
                    "Requires specific hardware configuration"
                ],
                "tradeoffs": [
                    "Higher accuracy with increased computational requirements"
                ],
                "ethical_considerations": [
                    "Potential bias in training data",
                    "Privacy considerations for input data"
                ]
            },
            "deployment": {
                "hardware_requirements": metadata.hardware_requirements,
                "deployment_targets": metadata.deployment_targets,
                "dependencies": metadata.dependencies
            }
        }
        
        # save the model card
        mlflow.log_dict(model_card, "model_card.json")
        
    def _run_governance_checks(self, model_info, metadata: ModelMetadata) -> bool:
        """run governance checks"""
        checks_passed = []
        
        # 1. baseline performance check
        baseline_checks = self._check_performance_baseline(metadata)
        checks_passed.append(("performance_baseline", baseline_checks))
        
        # 2. compliance check
        compliance_checks = self._check_compliance(metadata)
        checks_passed.append(("compliance", compliance_checks))
        
        # 3. Security Scan
        security_checks = self._check_security(model_info)
        checks_passed.append(("security", security_checks))
        
        # 4. Dependency Check
        dependency_checks = self._check_dependencies(metadata)
        checks_passed.append(("dependencies", dependency_checks))
        
        # Summarize Results
        all_passed = all(check["passed"] for _, check in checks_passed)
        
        # Record Check Results
        mlflow.set_tag("governance.checks", json.dumps({
            "timestamp": datetime.now().isoformat(),
            "results": checks_passed,
            "overall_status": "passed" if all_passed else "failed"
        }))
        
        return all_passed
    
    def _check_performance_baseline(self, metadata: ModelMetadata) -> Dict:
        """Check Performance Baseline"""
        required_metrics = ["accuracy", "precision", "recall", "f1_score"]
        actual_metrics = list(metadata.performance_metrics.keys())
        
        missing_metrics = set(required_metrics) - set(actual_metrics)
        baseline_met = all(
            metadata.performance_metrics.get(metric, 0) >= 0.8 
            for metric in required_metrics 
            if metric in metadata.performance_metrics
        )
        
        return {
            "passed": len(missing_metrics) == 0 and baseline_met,
            "details": {
                "missing_metrics": list(missing_metrics),
                "baseline_met": baseline_met,
                "required_metrics": required_metrics
            }
        }
    
    def _check_compliance(self, metadata: ModelMetadata) -> Dict:
        """Compliance Check"""
        required_compliance = ["GDPR", "SOC2"]
        has_required = all(tag in metadata.compliance_tags for tag in required_compliance)
        
        return {
            "passed": has_required,
            "details": {
                "required_compliance": required_compliance,
                "provided_compliance": metadata.compliance_tags,
                "missing_compliance": [tag for tag in required_compliance if tag not in metadata.compliance_tags]
            }
        }
    
    def _check_security(self, model_info) -> Dict:
        """Security Check"""
        # Simulate Security Scan
        vulnerabilities_found = []  # 实际应该调用安全扫描工具
        
        return {
            "passed": len(vulnerabilities_found) == 0,
            "details": {
                "vulnerabilities_found": vulnerabilities_found,
                "scan_timestamp": datetime.now().isoformat()
            }
        }
    
    def _check_dependencies(self, metadata: ModelMetadata) -> Dict:
        """Dependency Check"""
        # Check for known security vulnerabilities dependencies
        insecure_deps = []  # 实际应该检查CVE数据库
        
        return {
            "passed": len(insecure_deps) == 0,
            "details": {
                "total_dependencies": len(metadata.dependencies),
                "insecure_dependencies": insecure_deps
            }
        }
    
    def promote_to_production(self, model_name: str, version: str) -> bool:
        """Promote the model to production environment"""
        try:
            # Get the current production version
            current_prod = self.client.get_latest_versions(model_name, stages=["Production"])
            
            # Rollback the current production version to archive
            if current_prod:
                self.client.transition_model_version_stage(
                    name=model_name,
                    version=current_prod[0].version,
                    stage="Archived"
                )
            
            # Promote the new version to production
            self.client.transition_model_version_stage(
                name=model_name,
                version=version,
                stage="Production"
            )
            
            print(f"Model {model_name} v{version} promoted to Production")
            return True
            
        except Exception as e:
            print(f"Failed to promote model: {e}")
            return False
    
    def get_model_lineage(self, model_name: str, version: str) -> Dict:
        """Get the model lineage information"""
        model_version = self.client.get_model_version(model_name, version)
        run_id = model_version.run_id
        
        # Get training run information
        run = self.client.get_run(run_id)
        
        lineage = {
            "model": {
                "name": model_name,
                "version": version,
                "created_at": model_version.creation_timestamp
            },
            "training_run": {
                "run_id": run_id,
                "start_time": run.info.start_time,
                "end_time": run.info.end_time,
                "user_id": run.info.user_id
            },
            "dataset": {
                "name": run.data.tags.get("model.dataset", "unknown"),
                "version": run.data.tags.get("model.dataset_version", "unknown")
            },
            "parameters": dict(run.data.params),
            "metrics": dict(run.data.metrics),
            "artifacts": [artifact.path for artifact in self.client.list_artifacts(run_id)]
        }
        
        return lineage

# Usage Example
if __name__ == "__main__":
    # Initialize Registry
    registry = EnterpriseModelRegistry(
        tracking_uri="http://mlflow.company.com",
        registry_uri="models://mlflow.company.com"
    )
    
    # Create Model Metadata
    metadata = ModelMetadata(
        model_name="customer-churn-predictor",
        version="2.1.0",
        description="Customer churn prediction model with improved accuracy",
        author="data-science-team",
        team="ml-platform",
        created_at=datetime.now(),
        training_dataset="customer-interactions-v2",
        dataset_version="2024-Q1",
        hyperparameters={
            "learning_rate": 0.001,
            "batch_size": 128,
            "epochs": 50,
            "hidden_layers": 3
        },
        performance_metrics={
            "accuracy": 0.92,
            "precision": 0.89,
            "recall": 0.91,
            "f1_score": 0.90
        },
        hardware_requirements={
            "cpu": "2 cores",
            "memory": "4GB",
            "gpu": "1x T4"
        },
        deployment_targets=["kubernetes", "sagemaker"],
        compliance_tags=["GDPR", "SOC2", "ISO27001"],
        dependencies=["scikit-learn==1.3.0", "pandas==2.0.3", "numpy==1.24.3"],
        model_card=""
    )
    
    # Register the Model
    model_uri = "runs:/abc123/model"
    registered_model = registry.register_model_with_governance(
        model_uri=model_uri,
        model_name="customer-churn-predictor",
        metadata=metadata
    )
    
    print(f"Registered model: {registered_model}")
```

### 2.3 Automated A/B Testing Framework

```python
# automated_ab_testing.py
import mlflow
from mlflow.tracking import MlflowClient
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import time
from typing import Dict, List, Tuple
import json

class AutomatedABTesting:
    def __init__(self, tracking_uri: str):
        self.client = MlflowClient(tracking_uri=tracking_uri)
        mlflow.set_tracking_uri(tracking_uri)
        
    def setup_canary_deployment(self, 
                              model_name: str,
                              baseline_version: str,
                              candidate_version: str,
                              traffic_split: float = 0.1) -> str:
        """Set Canary Deployment"""
        
        # Create A/B Test Experiment
        experiment_name = f"ab-test-{model_name}-{datetime.now().strftime('%Y%m%d')}"
        experiment_id = mlflow.create_experiment(experiment_name)
        
        with mlflow.start_run(experiment_id=experiment_id) as run:
            # Record test configuration
            mlflow.log_params({
                "model_name": model_name,
                "baseline_version": baseline_version,
                "candidate_version": candidate_version,
                "traffic_split": traffic_split,
                "duration_hours": 24,
                "success_criteria": "candidate_accuracy > baseline_accuracy + 0.02"
            })
            
            # Deploy Canary Configuration
            canary_config = {
                "baseline": {
                    "model_name": model_name,
                    "version": baseline_version,
                    "weight": 1 - traffic_split
                },
                "candidate": {
                    "model_name": model_name,
                    "version": candidate_version,
                    "weight": traffic_split
                },
                "monitoring": {
                    "metrics": ["accuracy", "latency", "error_rate"],
                    "check_interval_minutes": 5,
                    "minimum_samples": 1000
                }
            }
            
            mlflow.log_dict(canary_config, "canary_config.json")
            
            # Start monitoring
            self._start_monitoring(run.info.run_id, canary_config)
            
            return run.info.run_id
    
    def _start_monitoring(self, run_id: str, config: Dict):
        """Start A/B Test Monitoring"""
        baseline_metrics = []
        candidate_metrics = []
        
        monitoring_duration = 24 * 60 * 60  # 24小时
        check_interval = 5 * 60  # 5分钟
        start_time = time.time()
        
        while time.time() - start_time < monitoring_duration:
            # Simulate collecting metrics
            baseline_acc = self._collect_metrics(config["baseline"])
            candidate_acc = self._collect_metrics(config["candidate"])
            
            baseline_metrics.append(baseline_acc)
            candidate_metrics.append(candidate_acc)
            
            # Record metrics to MLflow
            with mlflow.start_run(run_id=run_id):
                mlflow.log_metrics({
                    "baseline_accuracy": baseline_acc,
                    "candidate_accuracy": candidate_acc,
                    "traffic_split": config["candidate"]["weight"]
                }, step=int((time.time() - start_time) / check_interval))
            
            # Check early stop conditions
            if len(baseline_metrics) >= 10:  # 至少10个样本点
                if self._should_stop_early(baseline_metrics, candidate_metrics):
                    print("Early stopping criteria met")
                    break
            
            time.sleep(check_interval)
        
        # Evaluate final result
        self._evaluate_ab_test(run_id, baseline_metrics, candidate_metrics)
    
    def _collect_metrics(self, model_config: Dict) -> float:
        """Collect Model Metrics (Simulated)"""
        # In actual implementation, real metrics should be collected from the monitoring system
        base_accuracy = 0.85 if "baseline" in model_config["version"] else 0.87
        noise = np.random.normal(0, 0.02)
        return max(0, min(1, base_accuracy + noise))
    
    def _should_stop_early(self, baseline_metrics: List[float], 
                          candidate_metrics: List[float]) -> bool:
        """Check if early stopping should occur"""
        if len(baseline_metrics) < 10:
            return False
            
        # Calculate the average of the last 10 points
        recent_baseline = np.mean(baseline_metrics[-10:])
        recent_candidate = np.mean(candidate_metrics[-10:])
        
        # If the candidate model significantly outperforms the baseline model, stop early
        if recent_candidate > recent_baseline + 0.03:
            return True
            
        # If the candidate model significantly underperforms the baseline model, stop early
        if recent_candidate < recent_baseline - 0.05:
            return True
            
        return False
    
    def _evaluate_ab_test(self, run_id: str, 
                         baseline_metrics: List[float],
                         candidate_metrics: List[float]):
        """Evaluate A/B Test Results"""
        baseline_mean = np.mean(baseline_metrics)
        candidate_mean = np.mean(candidate_metrics)
        baseline_std = np.std(baseline_metrics)
        candidate_std = np.std(candidate_metrics)
        
        # Simplified statistical significance test
        pooled_std = np.sqrt((baseline_std**2 + candidate_std**2) / 2)
        effect_size = (candidate_mean - baseline_mean) / pooled_std
        sample_size = len(baseline_metrics)
        
        # Simplified significance judgment
        is_significant = abs(effect_size) > 2.0 and sample_size > 30
        
        # Record results
        with mlflow.start_run(run_id=run_id):
            mlflow.log_metrics({
                "baseline_final_accuracy": baseline_mean,
                "candidate_final_accuracy": candidate_mean,
                "effect_size": effect_size,
                "statistical_significance": float(is_significant),
                "samples_collected": sample_size
            })
            
            # Decision logic
            if is_significant and candidate_mean > baseline_mean:
                decision = "promote_candidate"
                recommendation = "Promote candidate model to production"
            elif is_significant and candidate_mean < baseline_mean:
                decision = "keep_baseline"
                recommendation = "Keep baseline model, candidate underperforms"
            else:
                decision = "inconclusive"
                recommendation = "Results inconclusive, collect more data"
            
            mlflow.set_tag("ab_test_decision", decision)
            mlflow.set_tag("recommendation", recommendation)
            
            print(f"A/B Test Results:")
            print(f"Baseline accuracy: {baseline_mean:.4f} ± {baseline_std:.4f}")
            print(f"Candidate accuracy: {candidate_mean:.4f} ± {candidate_std:.4f}")
            print(f"Effect size: {effect_size:.4f}")
            print(f"Decision: {recommendation}")

# Usage example
if __name__ == "__main__":
    ab_tester = AutomatedABTesting("http://mlflow.company.com")
    
    # Set A/B test
    run_id = ab_tester.setup_canary_deployment(
        model_name="customer-churn-predictor",
        baseline_version="1.2.0",
        candidate_version="2.0.0",
        traffic_split=0.1
    )
    
    print(f"A/B test started with run ID: {run_id}")
```


## 1. Version Management System

| System | Feature | Integration | Applicable Scenarios |
|-----|------|------|---------|
| **MLflow** | Experiment tracking, model registration | Python SDK | General ML |
| **DVC** | Git-like version control | CLI/Python | Data + models |
| **Weights & Biases** | Visualization, collaboration | Python SDK | Research teams |
| **HuggingFace Hub** | Model hosting | transformers | HF models |


## 2. MLflow Deployment

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mlflow-postgres
spec:
  serviceName: mlflow-postgres
  replicas: 1
  template:
    spec:
      containers:
      - name: postgres
        image: postgres:15
        env:
        - name: POSTGRES_DB
          value: mlflow
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mlflow-server
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: mlflow
        image: ghcr.io/mlflow/mlflow:v2.9.2
        command:
        - mlflow
        - server
        - --host=0.0.0.0
        - --backend-store-uri=postgresql://mlflow@postgres/mlflow
        - --default-artifact-root=s3://mlflow-artifacts/
        ports:
        - containerPort: 5000
```


## 3. Model Registry

```python
import mlflow
from transformers import AutoModelForCausalLM

# Set MLflow URI
mlflow.set_tracking_uri("http://mlflow-server:5000")
mlflow.set_experiment("llama2-finetuning")

with mlflow.start_run(run_name="llama2-7b-alpaca"):
    # Record parameters
    mlflow.log_params({
        "model": "llama-2-7b",
        "learning_rate": 3e-4,
        "lora_r": 8
    })
    
    # Train
    model = train_model()
    
    # Record metrics
    mlflow.log_metrics({
        "val_loss": 0.45,
        "val_accuracy": 0.92
    })
    
    # Register model
    mlflow.pytorch.log_model(
        model,
        "model",
        registered_model_name="llama2-7b-alpaca"
    )
```


## 4. Version Management

```python
from mlflow.tracking import MlflowClient

client = MlflowClient("http://mlflow-server:5000")

# Get model version
versions = client.search_model_versions("name='llama2-7b-alpaca'")

# Version promotion
client.transition_model_version_stage(
    name="llama2-7b-alpaca",
    version=3,
    stage="Production"
)

# Version comparison
version_1 = client.get_model_version("llama2-7b-alpaca", 1)
version_3 = client.get_model_version("llama2-7b-alpaca", 3)

print(f"v1 accuracy: {version_1.run_data.metrics['accuracy']}")
print(f"v3 accuracy: {version_3.run_data.metrics['accuracy']}")
```


## 5. Model Metadata

```yaml
model_card:
  name: "llama2-7b-alpaca-v3"
  version: "3.0.0"
  date: "2024-01-15"
  
  description: "Llama2-7B fine-tuning model, using Alpaca instruction dataset"
  
  training:
    dataset: "tatsu-lab/alpaca"
    samples: 52000
    epochs: 3
    learning_rate: 3e-4
    
  performance:
    accuracy: 0.92
    val_loss: 0.45
    
  resources:
    gpu: "1×A10G"
    training_time: "6 hours"
    cost: "$36"
    
  limitations:
    - "Only supports English"
    - "Context length 2048"
```


## 6. A/B Testing

```yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: llama2-ab-test
spec:
  predictor:
    canaryTrafficPercent: 20  # 20%流量到v3
    containers:
    - name: model-v2
      image: model-registry/llama2-7b-alpaca:v2
    canary:
      containers:
      - name: model-v3
        image: model-registry/llama2-7b-alpaca:v3
---
# Monitor A/B test
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: ab-test-metrics
spec:
  groups:
  - name: ab_test
    rules:
    - record: model_accuracy_by_version
      expr: |
        sum(rate(model_correct_predictions[5m])) by (version)
        / sum(rate(model_total_predictions[5m])) by (version)
```


## 7. Rollback Strategy

```python
class ModelRollback:
    def __init__(self, mlflow_client):
        self.client = mlflow_client
    
    def rollback_to_version(self, model_name, target_version):
        """Roll back to a specified version"""
        # Get current production version
        current = self.client.get_latest_versions(
            model_name, 
            stages=["Production"]
        )[0]
        
        # Downgrade current version
        self.client.transition_model_version_stage(
            name=model_name,
            version=current.version,
            stage="Archived"
        )
        
        # Promote target version
        self.client.transition_model_version_stage(
            name=model_name,
            version=target_version,
            stage="Production"
        )
        
        print(f"Rolled back from v{current.version} to v{target_version}")
    
    def auto_rollback_if_degraded(self, model_name, threshold=0.05):
        """Auto roll back when metrics decrease"""
        current = self.client.get_latest_versions(model_name, ["Production"])[0]
        previous = self.client.get_model_version(model_name, current.version - 1)
        
        current_acc = current.run_data.metrics.get("accuracy", 0)
        previous_acc = previous.run_data.metrics.get("accuracy", 0)
        
        if current_acc < previous_acc - threshold:
            self.rollback_to_version(model_name, previous.version)
            return True
        
        return False

# Usage
rollback = ModelRollback(client)
if rollback.auto_rollback_if_degraded("llama2-7b-alpaca", threshold=0.05):
    print("Auto rollback triggered!")
```


## 8. Version Lifespan

```
Staging → Production → Archived
   ↑          ↓
   └──────Rollback────────┘

Life cycle rules:
- Staging: New version testing, retained for 30 days
- Production: Current service version, retained for 90 days
- Archived: Historical versions, retained for 365 days before deletion
```


## 9. Best Practices

1. **Version Naming**: Use semantic versioning (major.minor.patch)
2. **Experiment Naming**: Include date and key parameters
3. **Metric Recording**: Record training/validation/test metrics
4. **Artifact Saving**: Save all models, configurations, checkpoints
5. **Metadata**: Record Git commit, dataset versions, training environment


## 10. Cost Optimization

**Storage Policies:**
- Active Version: S3 Standard
- Archived Version: S3 Glacier (80% savings)
- Delete Policy: Archive versions deleted 1 year later

**Example Cost (100 model versions, each 7GB):**
- Standard: 700GB × $0.023 = $16/month
- Glacier: 700GB × $0.004 = $2.8/month
- Savings: 82%

---
**Related:** [113-AI model registry](../09-ai-model-registry.md) | **Version**: MLflow 2.9+

---


## Obsidian Related Documents

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]] - index.md|Domain-11 AI Infrastructure — Open Source Project Index] - AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations (AI/ML Workloads Operations) - GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipelines and Feature Engineering
- AI Experiment Management and MLOps Platforms
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management

## See Also

- 22-llm-privacy-security
- 23-llm-cost-monitoring
- 25-llm-observability
- 26-cost-optimization-overview


<!-- risk-assessed -->
