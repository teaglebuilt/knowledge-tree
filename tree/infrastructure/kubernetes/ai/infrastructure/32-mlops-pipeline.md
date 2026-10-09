---
title: 32 - MLOps End-to-End Pipeline
description: '## One,MLOps Pipeline Architecture'
summary: 'from kfp.components import create_component_from_func'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- istio
- docker
- kafka
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
- What is MLOps End-to-End Pipeline
- How MLOps End-to-End Pipeline
- Kubernetes 11 ai infra Best Practices
trigger_keywords:
- MLOps End-to-End Pipeline
- ai
- infra
prerequisites:
- kubectl-basics
- service-mesh-basics
- kafka-basics
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
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/32-mlops-pipeline.md
---

> **Production Environment Security Reminders**
>
> Commands included in this document are executable directly. Please confirm before execution: that the target cluster and namespace are correct; that you have sufficient RBAC permissions; and that the commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but can usually be rolled back), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# 32 - MLOps End-to-End Pipeline

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **Difficulty**: Advanced | **Reference**: [[entities/kubeflow.md|Kubeflow]] Pipelines](https://www.kubeflow.org/docs/components/pipelines/) | [MLflow](https://mlflow.org/) | [[entities/argo.md|Argo]]go Workflows|Argo Workflows]]](https://argoproj.github.io/argo-workflows/)


## 1. Overall Pipeline Architecture

### 1.1 Overview of End-to-End Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           MLOps End-to-End Pipeline                                 │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│  │  Data       │───▶│ Feature     │───▶│ Model       │───▶│ Model       │          │
│  │  Ingestion  │    │ Engineering │    │ Training    │    │ Evaluation  │          │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘          │
│        │                    │                    │                    │              │
│        ▼                    ▼                    ▼                    ▼              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│  │ Data        │    │ Feature     │    │ Experiment  │    │ Performance │          │
│  │ Validation  │    │ Store       │    │ Tracking    │    │ Testing     │          │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘          │
│        │                    │                    │                    │              │
│        ▼                    ▼                    ▼                    ▼              │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐          │
│  │ Data        │    │ Feature     │    │ Hyperparam  │    │ Model       │          │
│  │ Quality     │    │ Validation  │    │ Tuning      │    │ Registry    │          │
│  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘          │
│                                                                                      │
│                              │              │              │                        │
│                              ▼              ▼              ▼                        │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                              Model Deployment                                 │  │
│  │  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    │  │
│  │  │ Model       │───▶│ A/B         │───▶│ Canary      │───▶│ Production  │    │  │
│  │  │ Packaging   │    │ Testing     │    │ Rollout     │    │ Monitoring  │    │  │
│  │  └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Detailed Explanation of Pipeline Components

| Component | Function | Technology Stack | Monitoring Focus |
|------|------|--------|------------|
| **Data Ingestion** | Data collection, cleaning, validation | Airflow/Kafka | Consistency, latency monitoring |
| **Feature Engineering** | Feature extraction, transformation, storage | Feast/TF Transform | Feature drift, version management |
| **Model Training** | Distributed training, hyperparameter tuning | Kubeflow/Katib | GPU utilization, training time |
| **Model Evaluation** | Performance evaluation, fairness checks | MLflow/Evidently | Accuracy assessment, bias detection |
| **Model Deployment** | Packaging, deployment, traffic switchover | [[KServe|KServe]]/Seldon | Deployment success rate, SLA metrics |
| **Online Services** | Inference services, auto-scaling | Istio/Knative | QPS, error rate, SLA |

---


## 2. Kubeflow Pipelines Implementation

### 2.1 Definition of Pipeline DSL

```python
# pipeline_definition.py
import kfp
from kfp import dsl
from kfp.components import create_component_from_func
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import mlflow
import evidently

@create_component_from_func
def data_ingestion(
    data_source: str,
    output_data_path: str
) -> str:
    \"\"\"Data ingestion component\"\"\"
    import pandas as pd
    import boto3
    
    # Read data from S3
    s3 = boto3.client('s3')
    bucket, key = data_source.replace('s3://', '').split('/', 1)
    s3.download_file(bucket, key, '/tmp/raw_data.csv')
    
    df = pd.read_csv('/tmp/raw_data.csv')
    
    # Data validation
    assert df.shape[0] > 1000, \"Data volume insufficient\"
    assert 'label' in df.columns, \"Missing label column\"
    
    # Data cleaning
    df = df.dropna()
    df.to_csv(output_data_path, index=False)
    
    return f\"Successfully processed {len(df)} records\"

@create_component_from_func
def feature_engineering(
    input_data_path: str,
    output_features_path: str,
    output_labels_path: str
) -> dict:
    \"\"\"Feature engineering component\"\"\"
    import pandas as pd
    from sklearn.preprocessing import StandardScaler, LabelEncoder
    import json
    
    df = pd.read_csv(input_data_path)
    
    # Feature selection
    feature_columns = [col for col in df.columns if col != 'label']
    X = df[feature_columns]
    y = df['label']
    
    # Feature standardization
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Label encoding
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    
    # Save features and labels
    pd.DataFrame(X_scaled).to_csv(output_features_path, index=False, header=False)
    pd.Series(y_encoded).to_csv(output_labels_path, index=False, header=False)
    
    # Return feature statistics
    stats = {
        'feature_count': len(feature_columns),
        'sample_count': len(df),
        'label_classes': len(le.classes_),
        'scaling_params': {
            'mean': scaler.mean_.tolist(),
            'std': scaler.scale_.tolist()
        }
    }
    
    return json.dumps(stats)

@create_component_from_func
def model_training(
    features_path: str,
    labels_path: str,
    model_output_path: str,
    experiment_name: str
) -> dict:
    \"\"\"Model training component\"\"\"
    import pandas as pd
    import numpy as np
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.model_selection import cross_val_score
    import mlflow
    import json
    import joblib
    
    # Load data
    X = pd.read_csv(features_path, header=None).values
    y = pd.read_csv(labels_path, header=None).values.ravel()
    
    # Start MLflow experiment
    mlflow.set_experiment(experiment_name)
    
    with mlflow.start_run() as run:
        # Model training
        model = RandomForestClassifier(
            n_estimators=100,
            max_depth=10,
            random_state=42
        )
        
        # Cross-validation
        cv_scores = cross_val_score(model, X, y, cv=5)
        
        # Final training
        model.fit(X, y)
        
        # Evaluation
        train_accuracy = model.score(X, y)
        
        # Record MLflow parameters
        mlflow.log_param(\"n_estimators\", 100)
        mlflow.log_param(\"max_depth\", 10)
        mlflow.log_metric(\"train_accuracy\", train_accuracy)
        mlflow.log_metric(\"cv_mean_accuracy\", cv_scores.mean())
        mlflow.log_metric(\"cv_std_accuracy\", cv_scores.std())
        
        # Save model
        joblib.dump(model, model_output_path)
        mlflow.log_artifact(model_output_path)
        
        # Return results
        result = {
            'run_id': run.info.run_id,
            'train_accuracy': float(train_accuracy),
            'cv_accuracy': float(cv_scores.mean()),
            'cv_std': float(cv_scores.std()),
            'model_path': model_output_path
        }
        
        return json.dumps(result)

@create_component_from_func
def model_evaluation(
    model_path: str,
    test_features_path: str,
    test_labels_path: str,
    evaluation_output_path: str
) -> dict:
    \"\"\"Model evaluation component\"\"\"
    import pandas as pd
    import numpy as np
    import joblib
    from sklearn.metrics import (accuracy_score, precision_score, 
                               recall_score, f1_score, confusion_matrix)
    import json
    import evidently
    from evidently.model_profile import Profile
    from evidently.model_profile.sections import (
        DataDriftProfileSection,
        ClassificationPerformanceProfileSection
    )
    
    # Load model and test data
    model = joblib.load(model_path)
    X_test = pd.read_csv(test_features_path, header=None).values
    y_test = pd.read_csv(test_labels_path, header=None).values.ravel()
    
    # Prediction
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)
    
    # Baseline metric calculation
    metrics = {
        'accuracy': float(accuracy_score(y_test, y_pred)),
        'precision': float(precision_score(y_test, y_pred, average='weighted')),
        'recall': float(recall_score(y_test, y_pred, average='weighted')),
        'f1_score': float(f1_score(y_test, y_pred, average='weighted'))
    }
    
    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred).tolist()
    metrics['confusion_matrix'] = cm
    
    # Evidently Model Analysis
    profile = Profile(sections=[
        ClassificationPerformanceProfileSection(),
        DataDriftProfileSection()
    ])
    
    # Create DataFrame for Evidently
    reference_data = pd.DataFrame({
        'prediction': y_pred,
        'target': y_test,
        **{f'prob_{i}': y_proba[:, i] for i in range(y_proba.shape[1])}
    })
    
    current_data = reference_data.copy()  # 在实际场景中应该是新数据
    
    profile.calculate(reference_data, current_data, column_mapping=None)
    
    # Add Evidently Metrics
    metrics['classification_performance'] = profile.get_content()['classification_performance']
    
    # Save Evaluation Results
    with open(evaluation_output_path, 'w') as f:
        json.dump(metrics, f, indent=2)
    
    return json.dumps(metrics)

@dsl.pipeline(
    name='ml-training-pipeline',
    description='End-to-end machine learning training pipeline'
)
def ml_training_pipeline(
    data_source: str = 's3://company-data/training/dataset.csv',
    experiment_name: str = 'customer-churn-prediction'
):
    # Step 1: Data Ingestion
    data_op = data_ingestion(
        data_source=data_source,
        output_data_path='/tmp/cleaned_data.csv'
    )
    
    # Step 2: Feature Engineering
    feature_op = feature_engineering(
        input_data_path=data_op.output,
        output_features_path='/tmp/features.csv',
        output_labels_path='/tmp/labels.csv'
    )
    
    # Step 3: Model Training
    train_op = model_training(
        features_path=feature_op.outputs['output'],
        labels_path='/tmp/labels.csv',
        model_output_path='/tmp/model.pkl',
        experiment_name=experiment_name
    )
    
    # Step 4: Model Evaluation
    eval_op = model_evaluation(
        model_path=train_op.outputs['output'],
        test_features_path='/tmp/features.csv',  # 实际应使用独立测试集
        test_labels_path='/tmp/labels.csv',
        evaluation_output_path='/tmp/evaluation.json'
    )
    
    # Set dependencies
    feature_op.after(data_op)
    train_op.after(feature_op)
    eval_op.after(train_op)

# Compile Pipeline
if __name__ == '__main__':
    kfp.compiler.Compiler().compile(ml_training_pipeline, 'ml_training_pipeline.yaml')
```

---


## 3. CI/CD Pipeline Integration

### 3.1 Configuration of GitHub Actions

```yaml
# .github/workflows/ml-pipeline.yaml
name: ML Pipeline CI/CD

on:
  push:
    branches: [main, develop]
    paths:
      - 'ml-pipeline/**'
      - 'models/**'
      - '.github/workflows/ml-pipeline.yaml'
  pull_request:
    branches: [main]
    paths:
      - 'ml-pipeline/**'
      - 'models/**'

env:
  PYTHON_VERSION: '3.9'
  MLFLOW_TRACKING_URI: 'http://mlflow-server:5000'

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ env.PYTHON_VERSION }}
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run unit tests
      run: |
        pytest tests/unit/ -v --cov=ml_pipeline
    
    - name: Run integration tests
      run: |
        pytest tests/integration/ -v
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3

  build:
    needs: test
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Docker Buildx
      uses: docker/setup-buildx-action@v2
    
    - name: Login to Container Registry
      uses: docker/login-action@v2
      with:
        registry: ${{ secrets.CONTAINER_REGISTRY }}
        username: ${{ secrets.REGISTRY_USERNAME }}
        password: ${{ secrets.REGISTRY_PASSWORD }}
    
    - name: Build and push pipeline components
      uses: docker/build-push-action@v4
      with:
        context: ./ml-pipeline
        file: ./ml-pipeline/Dockerfile
        push: true
        tags: |
          company/ml-pipeline:${{ github.sha }}
          company/ml-pipeline:latest
        platforms: linux/amd64,linux/arm64

  deploy-staging:
    needs: build
    runs-on: ubuntu-latest
    environment: staging
    steps:
    - uses: actions/checkout@v3
    
    - name: Deploy to staging
      run: |
        # Update Kubernetes Deployment
        kubectl set image deployment/ml-pipeline \
          data-ingestion=company/ml-pipeline:${{ github.sha }} \
          feature-engineering=company/ml-pipeline:${{ github.sha }} \
          model-training=company/ml-pipeline:${{ github.sha }} \
          model-evaluation=company/ml-pipeline:${{ github.sha }} \
          -n ml-staging
        
        # Run Test Pipeline
        kubectl create -f test-pipeline-staging.yaml
    
    - name: Wait for pipeline completion
      run: |
        timeout 3600 bash -c \"
        while \\$(kubectl get workflow -n ml-staging --sort-by=.metadata.creationTimestamp -o jsonpath='{.items[-1:].status.phase}') != 'Succeeded'; do
          echo 'Waiting for pipeline completion...'
          sleep 30
        done
        \"

  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment: production
    if: github.ref == 'refs/heads/main'
    steps:
    - uses: actions/checkout@v3
    
    - name: Manual approval
      uses: trstringer/manual-approval@v1
      with:
        secret: ${{ secrets.APPROVAL_TOKEN }}
        approvers: ml-team-lead,data-science-manager
        minimum_approvals: 1
    
    - name: Promote to production
      run: |
        # Blue-Green Deployment
        kubectl patch deployment ml-pipeline-blue -p \
          '{\"spec\":{\"template\":{\"spec\":{\"containers\":[{\"name\":\"data-ingestion\",\"image\":\"company/ml-pipeline:${{ github.sha }}\"}]}}}}'
        
        # Traffic Switchover
        kubectl patch service ml-pipeline -p \
          '{\"spec\":{\"selector\":{\"version\":\"blue\"}}}'
```

---


## 4. Production Environment Best Practices

### 4.1 Reliability Assurance for Pipelines

```yaml
# pipeline-reliability.yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pipeline-health-check
spec:
  template:
    spec:
      containers:
      - name: health-check
        image: company/pipeline-tools:health-check-v1.0
        command:
        - /bin/sh
        - -c
        - |
          # Check Health Status of Components
          COMPONENTS=(\"data-ingestion\" \"feature-engineering\" \"model-training\" \"model-evaluation\")
          
          for component in ${COMPONENTS[@]}; do
            echo \"Checking $component...\"
            
            # Check Pod Status
            if ! kubectl get pods -l app=$component -n ml-pipeline | grep Running; then
              echo \"ERROR: $component is not running\"
              exit 1
            fi
            
            # Check Recent Execution Status
            recent_workflows=$(kubectl get workflows -l component=$component --sort-by=.metadata.creationTimestamp -o jsonpath='{.items[-5:].status.phase}')
            success_count=$(echo $recent_workflows | grep -o Succeeded | wc -l)
            
            if [ $success_count -lt 4 ]; then
              echo \"WARNING: Low success rate for $component\"
            fi
          done
          
          echo \"All pipeline components are healthy\"
        env:
        - name: KUBECONFIG
          value: /etc/kubernetes/admin.conf
        volumeMounts:
        - name: kubeconfig
          mountPath: /etc/kubernetes
      restartPolicy: Never
      volumes:
      - name: kubeconfig
        configMap:
          name: kubeconfig-admin
```

### 4.2 Cost Optimization Strategies

```python
# cost_optimizer.py
import boto3
import kubernetes
from datetime import datetime, timedelta

class MLPipelineCostOptimizer:
    def __init__(self):
        self.ec2_client = boto3.client('ec2')
        self.k8s_client = kubernetes.client.ApiClient()
        
    def optimize_spot_instances(self):
        \"\"\"Optimize Spot instance usage\"\"\"
        # Get Spot Instance Price History
        pricing = self.ec2_client.describe_spot_price_history(
            InstanceTypes=['p3.2xlarge', 'p3.8xlarge'],
            ProductDescriptions=['Linux/UNIX'],
            StartTime=datetime.utcnow() - timedelta(hours=24)
        )
        
        # Choose Most Cost-Effective Instance Type
        best_instance = min(pricing['SpotPriceHistory'], 
                          key=lambda x: float(x['SpotPrice']))
        
        return {
            'instance_type': best_instance['InstanceType'],
            'spot_price': best_instance['SpotPrice'],
            'availability_zone': best_instance['AvailabilityZone']
        }
    
    def scale_pipeline_resources(self, pipeline_demand):
        \"\"\"Adjust resources dynamically based on pipeline needs\"\"""
        base_resources = {
            'data_ingestion': {'cpu': '1', 'memory': '2Gi'},
            'feature_engineering': {'cpu': '2', 'memory': '4Gi'},
            'model_training': {'cpu': '8', 'memory': '32Gi', 'gpu': '1'},
            'model_evaluation': {'cpu': '2', 'memory': '8Gi'}
        }
        
        # Adjust resource requests according to requirements
        optimized_resources = {}
        for component, resources in base_resources.items():
            demand_factor = pipeline_demand.get(component, 1.0)
            optimized_resources[component] = {
                'requests': {
                    'cpu': str(int(resources['cpu'].rstrip('m')) * demand_factor) + '000m',
                    'memory': str(int(resources['memory'].rstrip('Gi')) * demand_factor) + 'Gi'
                },
                'limits': {
                    'cpu': str(int(resources['cpu'].rstrip('m')) * demand_factor * 1.5) + '000m',
                    'memory': str(int(resources['memory'].rstrip('Gi')) * demand_factor * 1.5) + 'Gi'
                }
            }
            
            if 'gpu' in resources:
                optimized_resources[component]['requests']['nvidia.com/gpu'] = resources['gpu']
                optimized_resources[component]['limits']['nvidia.com/gpu'] = resources['gpu']
        
        return optimized_resources

# Usage Example
optimizer = MLPipelineCostOptimizer()
spot_config = optimizer.optimize_spot_instances()
resource_config = optimizer.scale_pipeline_resources({
    'model_training': 2.0,  # 高需求
    'data_ingestion': 0.5   # 低需求
})
```

---


## 5. Pipeline Governance and Security

### 5.1 Configuration for Security Hardening

```yaml
# pipeline-security.yaml
apiVersion: security.kubeflow.org/v1
kind: PipelineSecurityPolicy
metadata:
  name: ml-pipeline-security
spec:
  # Data Security
  dataProtection:
    encryption:
      atRest: true
      inTransit: true
      algorithm: \"AES-256\"
    
    accessControl:
      enabled: true
      policies:
        - resource: \"s3://training-data/*\"
          principals: [\"ml-training-pipeline\"]
          actions: [\"s3:GetObject\", \"s3:PutObject\"]
          condition:
            StringEquals:
              \"s3:prefix\": [\"training/\", \"validation/\"]
    
    # Sensitive Data Masking
    dataMasking:
      enabled: true
      rules:
        - pattern: \"\\\\b\\\\d{11}\\\\b\"  # 身份证号
          replacement: \"***********\"
        - pattern: \"\\\\b1[3-9]\\\\d{9}\\\\b\"  # 手机号
          replacement: \"138****8888\"

  # Model Security
  modelSecurity:
    scanning:
      enabled: true
      engines:
        - name: \"model-scanner\"
          type: \"static-analysis\"
          rules:
            - \"no_hardcoded_credentials\"
            - \"no_sensitive_data_in_model\"
            - \"model_integrity_check\"
    
    signing:
      enabled: true
      keyManagement:
        provider: \"vault\"
        keyName: \"model-signing-key\"
      
      verification:
        enabled: true
        required: true

  # Runtime Security
  networkSecurity:
    isolation:
      enabled: true
      namespaces:
        - \"ml-pipeline\"
        - \"ml-training\"
        - \"ml-serving\"
    
    egressControl:
      enabled: true
      rules:
        - to:
            cidr: \"10.0.0.0/8\"
          ports:
            - protocol: TCP
              port: 443
        - to:
            dnsName: \"mlflow-tracking.company.com\"
          ports:
            - protocol: TCP
              port: 5000

  # Network Security
  runtimeSecurity:
    podSecurityStandards:
      enforce: \"restricted\"
      audit: \"baseline\"
      warn: \"baseline\"
    
    seccompProfiles:
      enabled: true
      profile: \"runtime/default\"
    
    appArmorProfiles:
      enabled: true
      profiles:
        - \"docker-default\"
```

---

**Maintainers**: MLOps Team | **Last Updated**: 2026-02 | **Version**: v1.0

---


## Obsidian Related Documentation

- domain-11-ai-infra MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Open Source Project Index
- AI Infrastructure Architecture
- 132 - AI/ML Workload Operations
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management

## See Also

- 30-ai-security-compliance
- 31-ai-platform-governance
- 33-model-explainability
- 34-federated-learning


<!-- risk-assessed -->
