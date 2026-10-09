---
title: Kubeflow AI Platform Deployment and Practice Guide
description: '# Kubeflow AI Platform Deployment and Practice Guide'
summary: 'def preprocess_data(input_path: str, output_path: str):'
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
- istio
- harbor
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
- What is Kubeflow AI Platform Deployment and Practice Guide
- How Kubeflow AI Platform Deployment and Practice Guide
- Kubernetes 11 ai infra best practices
trigger_keywords:
- Kubeflow
- AI
- Platform Deployment and Practice Guide
- ai
- infra
prerequisites:
- kubectl-basics
- service-mesh-basics
- prometheus-basics
- monitoring-basics
- gpu-scheduling-basics
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
source_path: tree/infrastructure/kubernetes/ai/infrastructure/99-kubeflow-ai-platform-guide.md
---

> **Production Environment Security Reminders**
>
> This document contains executable operational commands. Execute them only after confirming: the correct target cluster and namespace; sufficient RBAC permissions; and successful validation in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (modifies cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# [[Kubeflow|Kubeflow]] AI Platform Deployment and Practice Guide

> **Applicable Version**: Kubeflow v1.10.0  
> **Last Updated**: 2026-04-24  
> **Difficulty**: Advanced

---


## 📋 Table of Contents

- [- Core Component Architecture](#1-core-component-architecture)
- [- Deployment Method](#2-deployment-methods)
- [- Notebook Workspace](#3-jupyter-notebooks-workspace)
- [- Pipelines Workflow Orchestration](#4-pipeline-workflow-orchestration)
- [- Katib Hyperparameter Tuning](#5-katib-hyperparameter-tuning)
- [- Training Operator Distributed Training](#6-training-operator-distributed-training)
- [Seven, [[KServe|KServe]] Model Service Integration](#seven-kserve-model-service-integration)
- [- Multi-Tenant and Isolation](#8-multi-tenancy-and-isolation)
- [- Production Environment Checklist](#9-production-environment-checklist)

---


## 1. Core Component Architecture

```
Kubeflow platform
├── Central Dashboard (unified entry)
├── Notebooks (Jupyter / VSCode workspace)
├── Pipelines (ML pipelines based on Argo Workflows)
│   └── SDK: kfp
├── Katib (hyperparameter tuning / AutoML / NAS)
├── Training Operator (distributed training jobs)
│   ├── TFJob (TensorFlow)
│   ├── PyTorchJob (PyTorch)
│   ├── MPIJob (MPI)
│   └── XGBoostJob
├── KServe (inference service for models, optionally independent)
└── Manifests (unified installation configuration)
```

---


## 2. Deployment Methods

### 2.1 Installing with Manifests (Official Recommended)

> ⚠️ **🟡 Medium Risk Change** — Modify cluster resource status, recommend using --dry-run or diff first
> - `kubectl apply/create/replace`: Create/Modify Cluster Resources

``` bash
# 🟡 Yellow risk: modifies cluster/resource status; confirm target, impact scope, and authorization before execution
# Set environment variables
export KUBEFLOW_VERSION=v1.10.0

# Download and install
wget https://github.com/kubeflow/manifests/archive/refs/tags/${KUBEFLOW_VERSION}.tar.gz
tar -xzf ${KUBEFLOW_VERSION}.tar.gz
cd manifests-${KUBEFLOW_VERSION}

# Complete installation (includes all components)
while ! kustomize build example | kubectl apply -f -; do
  echo "Retrying to apply resources..."
  sleep 20
done
```
### 2.2 Selective Installation of Components

> ⚠️ **🟡 Medium Risk Change** — Modify cluster resource status, recommend using --dry-run or diff first
> - `kubectl apply/create/replace`: Create/Modify Cluster Resources

``` bash
# 🟡 Yellow risk: modifies cluster/resource status; confirm target, impact scope, and authorization before execution
# Only install core + Pipelines + Training
kustomize build apps/pipeline/upstream | kubectl apply -f -
kustomize build apps/training-operator/upstream | kubectl apply -f -
```
### 2.3 Important Pre-requisites

| Checkpoint | Requirement |
|:---|:---|
| K8s Version | v1.29+ |
| Storage | Default StorageClass (PVC) |
| [[Ingress|Ingress]] | Istio / NGINIX / Cloud Provider LB |
| GPU (optional) | NVIDIA GPU Operator pre-installed |
| Resources | At least 8C16G control plane nodes |

---


## 3. Jupyter Notebooks Workspace

```yaml
apiVersion: kubeflow.org/v1
kind: Notebook
metadata:
  name: data-science-workspace
  namespace: kubeflow-user-example-com
spec:
  template:
    spec:
      containers:
      - name: notebook
        image: kubeflownotebookswg/jupyter-scipy:v1.10.0
        resources:
          requests:
            cpu: "1"
            memory: 4Gi
          limits:
            cpu: "4"
            memory: 16Gi
            nvidia.com/gpu: "1"  # GPU 工作空间
        volumeMounts:
        - name: workspace
          mountPath: /home/jovyan
      volumes:
      - name: workspace
        persistentVolumeClaim:
          claimName: workspace-pvc
```

**Common Images**
- `jupyter-scipy`: Basic Scientific Computing
- `jupyter-pytorch`: PyTorch + CUDA
- `jupyter-tensorflow`: TensorFlow + CUDA
- `jupyter-pytorch-full`: PyTorch + Common ML Libraries

---


## 4. Pipeline Workflow Orchestration

### 4.1 Defining Pipelines with Python SDK

```python
from kfp import dsl
from kfp import client

@dsl.component(base_image="python:3.11")
def preprocess_data(input_path: str, output_path: str):
    import pandas as pd
    df = pd.read_csv(input_path)
    df = df.dropna()
    df.to_csv(output_path, index=False)

@dsl.component(base_image="pytorch/pytorch:2.4.0-cuda12.1-cudnn9-runtime")
def train_model(data_path: str, model_path: str, epochs: int):
    import torch
    # Train logic
    torch.save(model.state_dict(), model_path)

@dsl.pipeline(name="ml-training-pipeline")
def my_pipeline(
    input_data: str = "s3://bucket/raw-data.csv",
    epochs: int = 10
):
    preprocess_task = preprocess_data(
        input_path=input_data,
        output_path="/tmp/processed.csv"
    )
    train_task = train_model(
        data_path=preprocess_task.outputs["output_path"],
        model_path="/tmp/model.pt",
        epochs=epochs
    )

# Submit for execution
kfp_client = client.Client(host="http://ml-pipeline.kubeflow:8888")
run = kfp_client.create_run_from_pipeline_func(
    my_pipeline,
    arguments={"input_data": "s3://mybucket/data.csv", "epochs": 20}
)
```

---


## 5. Katib Hyperparameter Tuning

```yaml
apiVersion: kubeflow.org/v1beta1
kind: Experiment
metadata:
  name: hyperparameter-tuning
  namespace: kubeflow
spec:
  objective:
    type: maximize
    goal: 0.99
    objectiveMetricName: accuracy
  algorithm:
    algorithmName: random
  parallelTrialCount: 3
  maxTrialCount: 12
  maxFailedTrialCount: 3
  parameters:
  - name: learning_rate
    parameterType: double
    feasibleSpace:
      min: "0.001"
      max: "0.1"
  - name: batch_size
    parameterType: int
    feasibleSpace:
      min: "16"
      max: "128"
  trialTemplate:
    primaryContainerName: training-container
    trialParameters:
    - name: learningRate
      description: Learning rate for the training model
      reference: learning_rate
    - name: batchSize
      description: Batch size for the training model
      reference: batch_size
    trialSpec:
      apiVersion: batch/v1
      kind: Job
      spec:
        template:
          spec:
            containers:
            - name: training-container
              image: my-registry/training:latest
              command:
              - python
              - train.py
              - --lr=${trialParameters.learningRate}
              - --batch-size=${trialParameters.batchSize}
            restartPolicy: Never
```

---


## 6. Training Operator Distributed Training

### 6.1 PyTorchJob (DDP)

```yaml
apiVersion: kubeflow.org/v1
kind: PyTorchJob
metadata:
  name: pytorch-ddp-training
spec:
  pytorchReplicaSpecs:
    Master:
      replicas: 1
      restartPolicy: OnFailure
      template:
        spec:
          containers:
          - name: pytorch
            image: my-registry/pytorch-train:latest
            command:
            - python
            - -m
            - torch.distributed.run
            - --nproc_per_node=4
            - train.py
            resources:
              limits:
                nvidia.com/gpu: 4
    Worker:
      replicas: 3
      restartPolicy: OnFailure
      template:
        spec:
          containers:
          - name: pytorch
            image: my-registry/pytorch-train:latest
            command:
            - python
            - -m
            - torch.distributed.run
            - --nproc_per_node=4
            - train.py
            resources:
              limits:
                nvidia.com/gpu: 4
```

---


## 7. KServe Model Serving Integration

```yaml
# Integrate KServe into Kubeflow
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: sklearn-iris
  namespace: kubeflow-user-example-com
  annotations:
    sidecar.istio.io/inject: "false"
spec:
  predictor:
    model:
      modelFormat:
        name: sklearn
      storageUri: "pvc://model-pvc/sklearn/iris"
```

---


## 8. Multi-tenancy and Isolation

### 8.1 Profile (Namespace + RBAC)

```yaml
apiVersion: kubeflow.org/v1
kind: Profile
metadata:
  name: team-data-science
spec:
  owner:
    kind: User
    name: data-lead@example.com
  resourceQuotaSpec:
    hard:
      cpu: "100"
      memory: 500Gi
      nvidia.com/gpu: "20"
      requests.storage: 2Ti
```

---


## 9. Production Environment Checklist

| Item | Requirement |
|:---|:---|
| Persistent Storage | PVC + Backup Strategy |
| Isolate GPU Nodes | Taints/Tolerations + Node Selector |
| Network Policies | Limit Notebook access scope |
| Resource Quotas | Profile-level restrictions |
| Image Security | Harbor + cosign signature verification |
| Log Collection | Fluent Bit → Loki/Elasticsearch |
| Monitoring Alerts | Prometheus + Grafana |
| Pipeline Security | ServiceAccount with minimal permissions |
| Data Isolation | S3/OSS Bucket isolated by team |
| Cost Tracking | OpenCost attributed to Namespace |

---


## References

- [Kubeflow Official Documentation](https://www.kubeflow.org/docs/)
- [Kubeflow Manifests](https://github.com/kubeflow/manifests)
- [KServe Documentation](https://kserve.github.io/website/latest/)
- [Kubeflow Pipelines SDK](https://kubeflow-pipelines.readthedocs.io/)

---


## Related Documents in Obsidian

- domain-11-ai-infra MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Open Source Project Index
- AI Infrastructure Architecture
- 132 - AI/ML Workload Operations (AI/ML Workloads Operations)
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipelines and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry Center and Version Management

## See Also

- 36-ai-platform-observability-enhanced
- 37-agent-sandbox-security
- 01-ai-infrastructure-overview
- 02-ai-ml-workloads

## Related

- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Knowledge Graph Index]]

```

<!-- risk-assessed -->
