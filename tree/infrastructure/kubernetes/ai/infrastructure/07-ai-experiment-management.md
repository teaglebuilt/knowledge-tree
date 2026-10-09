---
title: AI Experiment Management and MLOps Platform
description: '# AI Experiment Management and MLOps Platform'
summary: 'nginx.ingress.kubernetes.io/proxy-body-size: "500m"'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- scheduler
- prometheus
- postgresql
- statefulset
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- MLOps Engineer
- SRE
estimated_read_time: 5min
intent_queries:
- What is AI Experiment Management and MLOps Platform
- How to use AI Experiment Management and MLOps Platform
- Kubernetes 11 ai infra best practices
trigger_keywords:
- AI Experiment Management and MLOps Platform
- ai
- infra
prerequisites:
- kubectl-basics
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
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/07-ai-experiment-management.md
---

> **Production Environment Security Reminders**
>
> Commands contained herein are executable directly. Execute with confirmation that the target cluster and Namespace are correct, that sufficient RBAC permissions exist, and that the commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but typically can be rolled back), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# AI Experiment Management and MLOps Platform


## 1. Experiment Management Platform Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        MLOps Experiment Management Overview                                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐              │
│  │  Experiment Tracking     │───▶│  Hyperparameter Optimization     │───▶│  Model Evaluation     │              │
│  │  MLflow      │    │  Optuna      │    │  Metrics     │              │
│  │  W&B         │    │  Ray Tune    │    │  Validation  │              │
│  └──────────────┘    └──────────────┘    └──────────────┘              │
│       ▲                    ▲                    │                       │
│       │                    │                    ▼                       │
│  ┌────┴──────┐       ┌────┴──────┐       ┌────────────┐               │
│  │  Code Version  │       │  Data Version  │       │  Model Registry   │               │
│  │  Git      │       │  DVC      │       │  Registry  │               │
│  └───────────┘       └───────────┘       └────────────┘               │
│                                                │                        │
│                                                ▼                        │
│  ┌──────────────────────────────────────────────────┐                  │
│  │              CI/CD Pipeline                       │                  │
│  │  train → evaluate → register → deploy → monitor                  │                  │
│  └──────────────────────────────────────────────────┘                  │
│                                                                           │
│  ┌──────────────────────────────────────────────────┐                  │
│  │         Kubernetes infrastructure                  │                  │
│  │  • GPU Scheduling  • Distributed Training  • Model Serving           │                  │
│  └──────────────────────────────────────────────────┘                  │
└─────────────────────────────────────────────────────────────────────────┘
```

---


## 2. MLflow Experiment Tracking

### 2.1 Full Deployment of MLflow

```yaml
# PostgreSQL backend storage
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mlflow-postgres
  namespace: ai-platform
spec:
  serviceName: mlflow-postgres
  replicas: 1
  selector:
    matchLabels:
      app: mlflow-postgres
  template:
    metadata:
      labels:
        app: mlflow-postgres
    spec:
      containers:
      - name: postgres
        image: postgres:15-alpine
        ports:
        - containerPort: 5432
          name: postgres
        env:
        - name: POSTGRES_DB
          value: mlflow
        - name: POSTGRES_USER
          value: mlflow
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mlflow-postgres-secret
              key: password
        volumeMounts:
        - name: data
          mountPath: /var/lib/postgresql/data
        resources:
          requests:
            cpu: "2"
            memory: "4Gi"
          limits:
            cpu: "4"
            memory: "8Gi"
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: fast-ssd
      resources:
        requests:
          storage: 100Gi
---
# MLflow Tracking Server
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mlflow-server
  namespace: ai-platform
spec:
  replicas: 3
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
        image: ghcr.io/mlflow/mlflow:v2.9.2
        command:
        - mlflow
        - server
        - --host=0.0.0.0
        - --port=5000
        - --backend-store-uri=postgresql://mlflow:$(POSTGRES_PASSWORD)@mlflow-postgres:5432/mlflow
        - --default-artifact-root=s3://mlflow-artifacts/
        - --serve-artifacts
        - --gunicorn-opts=--workers 4 --timeout 120
        
        ports:
        - containerPort: 5000
          name: http
        
        env:
        - name: POSTGRES_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mlflow-postgres-secret
              key: password
        - name: AWS_ACCESS_KEY_ID
          valueFrom:
            secretKeyRef:
              name: s3-credentials
              key: access-key-id
        - name: AWS_SECRET_ACCESS_KEY
          valueFrom:
            secretKeyRef:
              name: s3-credentials
              key: secret-access-key
        - name: MLFLOW_S3_ENDPOINT_URL
          value: "https://s3.amazonaws.com"
        
        livenessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 30
          periodSeconds: 30
        
        readinessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 10
          periodSeconds: 10
        
        resources:
          requests:
            cpu: "2"
            memory: "4Gi"
          limits:
            cpu: "4"
            memory: "8Gi"
---
apiVersion: v1
kind: Service
metadata:
  name: mlflow-server
  namespace: ai-platform
spec:
  type: ClusterIP
  ports:
  - port: 5000
    targetPort: 5000
    protocol: TCP
    name: http
  selector:
    app: mlflow-server
---
# Expose via Ingress externally
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mlflow-ingress
  namespace: ai-platform
  annotations:
    nginx.ingress.kubernetes.io/proxy-body-size: "500m"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "600"
spec:
  ingressClassName: nginx
  rules:
  - host: mlflow.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: mlflow-server
            port:
              number: 5000
  tls:
  - hosts:
    - mlflow.example.com
    secretName: mlflow-tls-secret
```

### 2.2 Integration of Training Scripts with MLflow

```python
import mlflow
import mlflow.pytorch
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AdamW
from datasets import load_dataset
import os

# Set MLflow tracking URI
mlflow.set_tracking_uri("http://mlflow-server.ai-platform.svc.cluster.local:5000")
mlflow.set_experiment("bert-sentiment-classification")

# Hyperparameters
params = {
    "model_name": "bert-base-uncased",
    "learning_rate": 2e-5,
    "batch_size": 32,
    "num_epochs": 3,
    "max_length": 128,
    "warmup_steps": 500,
    "weight_decay": 0.01
}

# Start MLflow Run
with mlflow.start_run(run_name="bert-base-lr2e5-bs32") as run:
    
    # 1. Record hyperparameters
    mlflow.log_params(params)
    
    # 2. Record code version
    mlflow.log_param("git_commit", os.popen("git rev-parse HEAD").read().strip())
    
    # 3. Record environment information
    mlflow.log_param("cuda_version", torch.version.cuda)
    mlflow.log_param("gpu_name", torch.cuda.get_device_name(0))
    mlflow.log_param("num_gpus", torch.cuda.device_count())
    
    # Load model and data
    model = AutoModelForSequenceClassification.from_pretrained(
        params["model_name"],
        num_labels=2
    )
    tokenizer = AutoTokenizer.from_pretrained(params["model_name"])
    
    # Dataset
    dataset = load_dataset("imdb")
    train_dataset = dataset["train"].shuffle(seed=42).select(range(10000))
    val_dataset = dataset["test"].select(range(1000))
    
    def tokenize_function(examples):
        return tokenizer(
            examples["text"],
            padding="max_length",
            truncation=True,
            max_length=params["max_length"]
        )
    
    train_dataset = train_dataset.map(tokenize_function, batched=True)
    val_dataset = val_dataset.map(tokenize_function, batched=True)
    
    train_loader = DataLoader(train_dataset, batch_size=params["batch_size"], shuffle=True)
    val_loader = DataLoader(val_dataset, batch_size=params["batch_size"])
    
    # Optimizer
    optimizer = AdamW(
        model.parameters(),
        lr=params["learning_rate"],
        weight_decay=params["weight_decay"]
    )
    
    # Training loop
    model.cuda()
    model.train()
    
    global_step = 0
    for epoch in range(params["num_epochs"]):
        total_loss = 0
        for batch_idx, batch in enumerate(train_loader):
            inputs = {k: v.cuda() for k, v in batch.items() if k in ["input_ids", "attention_mask"]}
            labels = batch["label"].cuda()
            
            outputs = model(**inputs, labels=labels)
            loss = outputs.loss
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            
            total_loss += loss.item()
            global_step += 1
            
            # 4. Record training metrics (every 10 steps)
            if global_step % 10 == 0:
                mlflow.log_metric("train_loss", loss.item(), step=global_step)
                mlflow.log_metric("learning_rate", optimizer.param_groups[0]["lr"], step=global_step)
        
        avg_train_loss = total_loss / len(train_loader)
        
        # 5. Validation evaluation
        model.eval()
        val_loss = 0
        correct = 0
        total = 0
        
        with torch.no_grad():
            for batch in val_loader:
                inputs = {k: v.cuda() for k, v in batch.items() if k in ["input_ids", "attention_mask"]}
                labels = batch["label"].cuda()
                
                outputs = model(**inputs, labels=labels)
                val_loss += outputs.loss.item()
                
                predictions = torch.argmax(outputs.logits, dim=-1)
                correct += (predictions == labels).sum().item()
                total += labels.size(0)
        
        avg_val_loss = val_loss / len(val_loader)
        accuracy = correct / total
        
        # 6. Record validation metrics
        mlflow.log_metric("val_loss", avg_val_loss, step=epoch)
        mlflow.log_metric("val_accuracy", accuracy, step=epoch)
        
        print(f"Epoch {epoch+1}/{params['num_epochs']} - "
              f"Train Loss: {avg_train_loss:.4f}, Val Loss: {avg_val_loss:.4f}, "
              f"Val Accuracy: {accuracy:.4f}")
        
        model.train()
    
    # 7. Save model to MLflow
    mlflow.pytorch.log_model(
        model,
        "model",
        registered_model_name="bert-sentiment-classifier"
    )
    
    # Record additional artifacts
    # Save confusion matrix image
    import matplotlib.pyplot as plt
    from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
    
    # Generate predictions
    all_preds = []
    all_labels = []
    with torch.no_grad():
        for batch in val_loader:
            inputs = {k: v.cuda() for k, v in batch.items() if k in ["input_ids", "attention_mask"]}
            labels = batch["label"]
            outputs = model(**inputs)
            predictions = torch.argmax(outputs.logits, dim=-1).cpu()
            all_preds.extend(predictions.tolist())
            all_labels.extend(labels.tolist())
    
    cm = confusion_matrix(all_labels, all_preds)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Negative", "Positive"])
    disp.plot()
    plt.savefig("confusion_matrix.png")
    mlflow.log_artifact("confusion_matrix.png")
    
    # 9. Record model signature
    from mlflow.models.signature import infer_signature
    sample_input = {
        "input_ids": torch.randint(0, 30522, (1, params["max_length"])),
        "attention_mask": torch.ones(1, params["max_length"])
    }
    sample_output = model(**sample_input).logits.detach()
    signature = infer_signature(sample_input, sample_output)
    mlflow.pytorch.log_model(model, "model_with_signature", signature=signature)
    
    # Add label
    mlflow.set_tag("model_type", "transformer")
    mlflow.set_tag("task", "sentiment-classification")
    mlflow.set_tag("framework", "pytorch")
    mlflow.set_tag("status", "production-ready")
    
    print(f"Run ID: {run.info.run_id}")
    print(f"MLflow UI: http://mlflow.example.com/#/experiments/{run.info.experiment_id}/runs/{run.info.run_id}")
```

### 2.3 MLflow Kubernetes Training Job

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: bert-training-mlflow
  namespace: ai-platform
spec:
  template:
    metadata:
      labels:
        app: bert-training
    spec:
      restartPolicy: OnFailure
      containers:
      - name: trainer
        image: myregistry/pytorch-trainer:latest
        command:
        - python
        - /workspace/train.py
        
        env:
        - name: MLFLOW_TRACKING_URI
          value: "http://mlflow-server.ai-platform.svc.cluster.local:5000"
        - name: MLFLOW_EXPERIMENT_NAME
          value: "bert-sentiment-classification"
        - name: AWS_ACCESS_KEY_ID
          valueFrom:
            secretKeyRef:
              name: s3-credentials
              key: access-key-id
        - name: AWS_SECRET_ACCESS_KEY
          valueFrom:
            secretKeyRef:
              name: s3-credentials
              key: secret-access-key
        
        resources:
          requests:
            cpu: "8"
            memory: "32Gi"
            nvidia.com/gpu: 1
          limits:
            cpu: "16"
            memory: "64Gi"
            nvidia.com/gpu: 1
        
        volumeMounts:
        - name: workspace
          mountPath: /workspace
        - name: dshm
          mountPath: /dev/shm
      
      volumes:
      - name: workspace
        configMap:
          name: training-code
      - name: dshm
        emptyDir:
          medium: Memory
          sizeLimit: 16Gi
```

---


## 3. Integrating Weights & Biases

### 3.1 Advantages of W&B Features

Compared to MLflow, W&B offers more extensive visualization and collaboration features:

- **Real-time Visualization**: Training curves update in real time
- **Hyperparameter Comparison**: Parallel Coordinates chart
- **Model Comparison**: Run Comparison Table
- **Report Generation**: Markdown-formatted experiment report
- **Team Collaboration**: Share experiments, comments, discussions

### 3.2 Integration of W&B with Training

```python
import wandb
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, Trainer, TrainingArguments
from datasets import load_dataset

# Initialize W&B
wandb.init(
    project="llama2-finetuning",
    name="llama2-7b-alpaca-lora",
    config={
        "model": "meta-llama/Llama-2-7b-hf",
        "dataset": "alpaca",
        "learning_rate": 3e-4,
        "batch_size": 4,
        "gradient_accumulation_steps": 4,
        "num_epochs": 3,
        "lora_r": 8,
        "lora_alpha": 16,
        "lora_dropout": 0.05
    },
    tags=["lora", "instruction-tuning", "llama2"]
)

config = wandb.config

# Load model and data
model = AutoModelForCausalLM.from_pretrained(
    config.model,
    load_in_8bit=True,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(config.model)

# LoRA configuration
from peft import LoraConfig, get_peft_model, TaskType

lora_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM,
    r=config.lora_r,
    lora_alpha=config.lora_alpha,
    lora_dropout=config.lora_dropout,
    target_modules=["q_proj", "v_proj", "k_proj", "o_proj"]
)
model = get_peft_model(model, lora_config)

# Dataset
dataset = load_dataset("tatsu-lab/alpaca")

# Training parameters
training_args = TrainingArguments(
    output_dir="./checkpoints",
    per_device_train_batch_size=config.batch_size,
    gradient_accumulation_steps=config.gradient_accumulation_steps,
    learning_rate=config.learning_rate,
    num_train_epochs=config.num_epochs,
    logging_steps=10,
    save_steps=500,
    eval_steps=500,
    evaluation_strategy="steps",
    report_to="wandb",  # 自动同步到W&B
    run_name=wandb.run.name
)

# Trainer will automatically record metrics to W&B
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset["train"],
    eval_dataset=dataset["test"]
)

# Train
trainer.train()

# Manually record additional information
wandb.log({
    "trainable_params": sum(p.numel() for p in model.parameters() if p.requires_grad),
    "total_params": sum(p.numel() for p in model.parameters())
})

# Save model to W&B Artifacts
artifact = wandb.Artifact("llama2-7b-alpaca-lora", type="model")
artifact.add_dir("./checkpoints/checkpoint-final")
wandb.log_artifact(artifact)

wandb.finish()
```

### 3.3 W&B Sweeps Hyperparameter Search

```yaml
# sweep_config.yaml
program: train.py
method: bayes  # 贝叶斯优化
metric:
  name: eval/loss
  goal: minimize
parameters:
  learning_rate:
    distribution: log_uniform_values
    min: 1e-5
    max: 1e-3
  lora_r:
    values: [4, 8, 16, 32]
  lora_alpha:
    values: [8, 16, 32, 64]
  batch_size:
    values: [2, 4, 8]
  gradient_accumulation_steps:
    values: [2, 4, 8, 16]
early_terminate:
  type: hyperband
  min_iter: 3
  eta: 2
```

```python
# Start Sweep
import wandb

# Create Sweep
sweep_id = wandb.sweep(
    sweep_config,
    project="llama2-finetuning"
)

# Run Sweep Agent (can run on multiple nodes)
wandb.agent(sweep_id, function=train, count=20)
```

**Kubernetes Parallel Sweeps:**
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: wandb-sweep-agent
  namespace: ai-platform
spec:
  parallelism: 10  # 10个并行agent
  completions: 20   # 总共20次实验
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: sweep-agent
        image: myregistry/wandb-trainer:latest
        command:
        - wandb
        - agent
        - user/project/sweep-id
        env:
        - name: WANDB_API_KEY
          valueFrom:
            secretKeyRef:
              name: wandb-secret
              key: api-key
        resources:
          requests:
            nvidia.com/gpu: 1
          limits:
            nvidia.com/gpu: 1
```

---


## 4. Kubeflow Pipelines

### 4.1 Complete Definition of ML Pipeline

```python
from kfp import dsl, compiler
from kfp.dsl import Input, Output, Dataset, Model, Metrics

@dsl.component(
    base_image="python:3.9",
    packages_to_install=["pandas", "scikit-learn", "boto3"]
)
def data_preprocessing(
    raw_data_path: str,
    processed_data: Output[Dataset],
    train_test_split_ratio: float = 0.8
):
    """Data preprocessing component"""
    import pandas as pd
    from sklearn.model_selection import train_test_split
    import pickle
    
    # Read data
    df = pd.read_csv(raw_data_path)
    
    # Clean
    df = df.dropna()
    df = df[df['amount'] > 0]
    
    # Split
    train_df, test_df = train_test_split(df, test_size=1-train_test_split_ratio, random_state=42)
    
    # Save
    output_data = {
        "train": train_df.to_dict(),
        "test": test_df.to_dict()
    }
    with open(processed_data.path, 'wb') as f:
        pickle.dump(output_data, f)

@dsl.component(
    base_image="pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime",
    packages_to_install=["transformers", "mlflow"]
)
def model_training(
    processed_data: Input[Dataset],
    model_output: Output[Model],
    metrics_output: Output[Metrics],
    learning_rate: float = 2e-5,
    num_epochs: int = 3
):
    """Model training component"""
    import torch
    from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments
    import pickle
    import mlflow
    import json
    
    # Load data
    with open(processed_data.path, 'rb') as f:
        data = pickle.load(f)
    
    # Train model
    model = AutoModelForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)
    
    training_args = TrainingArguments(
        output_dir="/tmp/model",
        learning_rate=learning_rate,
        num_train_epochs=num_epochs,
        per_device_train_batch_size=32
    )
    
    trainer = Trainer(model=model, args=training_args, train_dataset=data["train"])
    trainer.train()
    
    # Evaluate
    eval_results = trainer.evaluate(data["test"])
    
    # Save model
    model.save_pretrained(model_output.path)
    
    # Save metrics
    metrics_output.log_metric("accuracy", eval_results["eval_accuracy"])
    metrics_output.log_metric("loss", eval_results["eval_loss"])

@dsl.component(
    base_image="python:3.9",
    packages_to_install=["mlflow", "boto3"]
)
def model_registration(
    model: Input[Model],
    metrics: Input[Metrics],
    accuracy_threshold: float = 0.85
) -> str:
    """Model registration component"""
    import mlflow
    
    # Read metrics
    accuracy = metrics.metadata["accuracy"]
    
    if accuracy >= accuracy_threshold:
        # Register to MLflow
        mlflow.set_tracking_uri("http://mlflow-server.ai-platform.svc.cluster.local:5000")
        
        with mlflow.start_run():
            mlflow.log_metric("accuracy", accuracy)
            model_uri = mlflow.pytorch.log_model(model.path, "model")
            
            # Register model
            result = mlflow.register_model(
                model_uri,
                "bert-classifier",
                tags={"stage": "production"}
            )
            return result.version
    else:
        raise ValueError(f"model accuracy {accuracy} below threshold {accuracy_threshold}")

@dsl.pipeline(
    name="ML Training Pipeline",
    description="the complete ML training Pipeline"
)
def ml_training_pipeline(
    data_path: str = "s3://data/raw/dataset.csv",
    learning_rate: float = 2e-5,
    num_epochs: int = 3,
    accuracy_threshold: float = 0.85
):
    # Data preprocessing
    preprocess_task = data_preprocessing(raw_data_path=data_path)
    
    # Model training
    train_task = model_training(
        processed_data=preprocess_task.outputs["processed_data"],
        learning_rate=learning_rate,
        num_epochs=num_epochs
    )
    
    # Model registration
    register_task = model_registration(
        model=train_task.outputs["model_output"],
        metrics=train_task.outputs["metrics_output"],
        accuracy_threshold=accuracy_threshold
    )

# Compile Pipeline
compiler.Compiler().compile(
    pipeline_func=ml_training_pipeline,
    package_path="ml_pipeline.yaml"
)
```

### 4.2 Deployment of Kubeflow

> ⚠️ **🟡 Medium Risk Change** — Modify cluster resource state, recommend using --dry-run or diff first
> - `kubectl apply/create/replace`: Create/modify cluster resources

``` bash
# 🟡 Medium-risk: modifies cluster/resource state, confirm target, impact scope, and authorization before execution
# Install Kubeflow Pipelines
export PIPELINE_VERSION=2.0.5
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/cluster-scoped-resources?ref=$PIPELINE_VERSION"
kubectl wait --for condition=established --timeout=60s crd/applications.app.k8s.io
kubectl apply -k "github.com/kubeflow/pipelines/manifests/kustomize/env/platform-agnostic?ref=$PIPELINE_VERSION"

# Port forwarding to access UI
kubectl port-forward -n kubeflow svc/ml-pipeline-ui 8080:80
# Access http://localhost:8080
```
### 4.3 Submission of Pipeline Runs

```python
import kfp

# Connect to Kubeflow Pipelines
client = kfp.Client(host="http://ml-pipeline-ui.kubeflow.svc.cluster.local")

# Upload Pipeline
pipeline_id = client.upload_pipeline(
    pipeline_package_path="ml_pipeline.yaml",
    pipeline_name="ML Training Pipeline v1.0"
)

# Create experiment
experiment = client.create_experiment(name="bert-classification-experiments")

# Submit run
run = client.run_pipeline(
    experiment_id=experiment.id,
    job_name="bert-training-run-001",
    pipeline_id=pipeline_id,
    params={
        "data_path": "s3://data/raw/reviews.csv",
        "learning_rate": 3e-5,
        "num_epochs": 5,
        "accuracy_threshold": 0.90
    }
)

print(f"Run ID: {run.id}")
print(f"Run URL: http://localhost:8080/#/runs/details/{run.id}")
```

---


## 5. Experiment Comparison and Analysis

### 5.1 Experiment Comparison in MLflow UI

```python
from mlflow.tracking import MlflowClient

client = MlflowClient("http://mlflow-server.ai-platform.svc.cluster.local:5000")

# Get all runs of an experiment
experiment_id = "1"
runs = client.search_runs(
    experiment_ids=[experiment_id],
    filter_string="metrics.val_accuracy > 0.85",
    order_by=["metrics.val_accuracy DESC"],
    max_results=10
)

# Compare best runs
import pandas as pd

comparison_data = []
for run in runs:
    comparison_data.append({
        "run_id": run.info.run_id,
        "learning_rate": run.data.params.get("learning_rate"),
        "batch_size": run.data.params.get("batch_size"),
        "val_accuracy": run.data.metrics.get("val_accuracy"),
        "val_loss": run.data.metrics.get("val_loss"),
        "duration": run.info.end_time - run.info.start_time
    })

df = pd.DataFrame(comparison_data)
print(df.to_string())

# Output example:
#        run_id  learning_rate batch_size  val_accuracy  val_loss  duration(ms)
# 0  abc123def45           2e-5         32        0.9234    0.2145      1234567
# 1  ghi789jkl01           3e-5         32        0.9187    0.2298      1198765
# 2  mno456pqr78           2e-5         64        0.9156    0.2401      987654
```

### 5.2 Generation of Experiment Reports

```python
import mlflow
from mlflow.tracking import MlflowClient
import matplotlib.pyplot as plt

client = MlflowClient()

experiment_id = "1"
runs = client.search_runs(experiment_ids=[experiment_id], max_results=20)

# Generate learning curve comparison chart
plt.figure(figsize=(12, 6))

for run in runs[:5]:  # 前5个最佳runs
    run_id = run.info.run_id
    metrics = client.get_metric_history(run_id, "val_accuracy")
    steps = [m.step for m in metrics]
    values = [m.value for m in metrics]
    
    label = f"LR={run.data.params['learning_rate']}, BS={run.data.params['batch_size']}"
    plt.plot(steps, values, label=label, marker='o')

plt.xlabel("Epoch")
plt.ylabel("Validation Accuracy")
plt.title("Validation Accuracy Comparison")
plt.legend()
plt.grid(True)
plt.savefig("accuracy_comparison.png", dpi=300)

# Record to MLflow
with mlflow.start_run():
    mlflow.log_artifact("accuracy_comparison.png")
```

---


## 6. Distributed Hyperparameter Optimization

### 6.1 Integration of Ray Tune

```python
from ray import tune
from ray.tune.schedulers import ASHAScheduler
from ray.tune.integration.mlflow import MLflowLoggerCallback
import torch
from transformers import AutoModelForSequenceClassification, Trainer, TrainingArguments

def train_model(config):
    """Training function"""
    model = AutoModelForSequenceClassification.from_pretrained(
        "bert-base-uncased",
        num_labels=2
    )
    
    training_args = TrainingArguments(
        output_dir="/tmp/model",
        learning_rate=config["learning_rate"],
        per_device_train_batch_size=config["batch_size"],
        num_train_epochs=3,
        evaluation_strategy="epoch"
    )
    
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset,
        eval_dataset=eval_dataset
    )
    
    # Train and return result
    result = trainer.train()
    eval_result = trainer.evaluate()
    
    # Report metrics to Ray Tune
    tune.report(
        accuracy=eval_result["eval_accuracy"],
        loss=eval_result["eval_loss"]
    )

# Ray Tune search space
search_space = {
    "learning_rate": tune.loguniform(1e-5, 1e-3),
    "batch_size": tune.choice([16, 32, 64]),
    "weight_decay": tune.uniform(0.0, 0.1)
}

# ASHA scheduler (early stopping)
scheduler = ASHAScheduler(
    metric="accuracy",
    mode="max",
    max_t=10,
    grace_period=1,
    reduction_factor=2
)

# Run hyperparameter search
analysis = tune.run(
    train_model,
    config=search_space,
    num_samples=20,  # 20次试验
    scheduler=scheduler,
    resources_per_trial={"cpu": 8, "gpu": 1},
    callbacks=[
        MLflowLoggerCallback(
            tracking_uri="http://mlflow-server.ai-platform.svc.cluster.local:5000",
            experiment_name="ray-tune-hpo",
            save_artifact=True
        )
    ]
)

# Best configuration
best_config = analysis.best_config
print(f"Best config: {best_config}")
print(f"Best accuracy: {analysis.best_result['accuracy']}")
```

### 6.2 Optimizer Optuna

```python
import optuna
import mlflow

def objective(trial):
    """Objective function for Optuna"""
    # Define hyperparameter search space
    learning_rate = trial.suggest_float("learning_rate", 1e-5, 1e-3, log=True)
    batch_size = trial.suggest_categorical("batch_size", [16, 32, 64])
    num_layers = trial.suggest_int("num_layers", 6, 12)
    dropout = trial.suggest_float("dropout", 0.1, 0.5)
    
    # Train model
    model = build_model(num_layers=num_layers, dropout=dropout)
    accuracy = train_and_evaluate(model, learning_rate, batch_size)
    
    # Record to MLflow
    with mlflow.start_run(nested=True):
        mlflow.log_params({
            "learning_rate": learning_rate,
            "batch_size": batch_size,
            "num_layers": num_layers,
            "dropout": dropout
        })
        mlflow.log_metric("accuracy", accuracy)
    
    return accuracy

# Create Optuna Study
study = optuna.create_study(
    study_name="bert-optimization",
    direction="maximize",
    storage="postgresql://optuna:password@postgres:5432/optuna",  # 持久化
    load_if_exists=True,
    sampler=optuna.samplers.TPESampler(),  # Tree-structured Parzen Estimator
    pruner=optuna.pruners.MedianPruner(n_startup_trials=5, n_warmup_steps=3)
)

# Run optimization (distributed)
with mlflow.start_run():
    study.optimize(objective, n_trials=50, timeout=3600)
    
    # Record best results
    mlflow.log_params(study.best_params)
    mlflow.log_metric("best_accuracy", study.best_value)

print(f"Best trial: {study.best_trial.number}")
print(f"Best params: {study.best_params}")
print(f"Best accuracy: {study.best_value}")

# Visualize
import optuna.visualization as vis

# Optimization History
fig = vis.plot_optimization_history(study)
fig.write_html("optimization_history.html")

# Parameter Importance
fig = vis.plot_param_importances(study)
fig.write_html("param_importances.html")
```

**Kubernetes Distributed Optuna:**
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: optuna-worker
spec:
  parallelism: 10  # 10个并行worker
  completions: 50   # 总共50次trial
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: worker
        image: myregistry/optuna-trainer:latest
        command:
        - python
        - optimize.py
        env:
        - name: OPTUNA_STORAGE
          value: "postgresql://optuna:password@postgres.ai-platform:5432/optuna"
        - name: STUDY_NAME
          value: "bert-optimization"
        resources:
          limits:
            nvidia.com/gpu: 1
```

---


## 7. CI/CD for ML

### 7.1 GitLab CI ML Pipeline

```yaml
# .gitlab-ci.yml
stages:
  - data-validation
  - train
  - evaluate
  - register
  - deploy

variables:
  MLFLOW_TRACKING_URI: "http://mlflow-server.ai-platform.svc.cluster.local:5000"
  EXPERIMENT_NAME: "bert-classification-ci"

data-validation:
  stage: data-validation
  image: python:3.9
  script:
    - pip install great-expectations pandas
    - python scripts/validate_data.py
    - echo "Data validation passed"
  artifacts:
    reports:
      junit: validation-report.xml
  only:
    - main
    - merge_requests

train-model:
  stage: train
  image: pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime
  script:
    - pip install -r requirements.txt
    - python train.py --experiment-name $EXPERIMENT_NAME
    - echo $MLFLOW_RUN_ID > run_id.txt
  artifacts:
    paths:
      - run_id.txt
      - model/
    expire_in: 7 days
  tags:
    - gpu
  only:
    - main

evaluate-model:
  stage: evaluate
  image: python:3.9
  script:
    - pip install mlflow scikit-learn
    - export RUN_ID=$(cat run_id.txt)
    - python scripts/evaluate_model.py --run-id $RUN_ID
    - export ACCURACY=$(python scripts/get_metric.py --run-id $RUN_ID --metric accuracy)
    - echo "Model accuracy: $ACCURACY"
    - |
      if (( $(echo "$ACCURACY < 0.85" | bc -l) )); then
        echo "Accuracy below threshold, failing pipeline"
        exit 1
      fi
  dependencies:
    - train-model
  only:
    - main

register-model:
  stage: register
  image: python:3.9
  script:
    - pip install mlflow
    - export RUN_ID=$(cat run_id.txt)
    - python scripts/register_model.py --run-id $RUN_ID --model-name bert-classifier
  dependencies:
    - train-model
    - evaluate-model
  only:
    - main

deploy-to-staging:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context staging-cluster
    - export MODEL_VERSION=$(cat model_version.txt)
    - envsubst < k8s/inference-service.yaml | kubectl apply -f -
  environment:
    name: staging
    url: https://model-staging.example.com
  dependencies:
    - register-model
  only:
    - main

deploy-to-production:
  stage: deploy
  image: bitnami/kubectl:latest
  script:
    - kubectl config use-context prod-cluster
    - export MODEL_VERSION=$(cat model_version.txt)
    - envsubst < k8s/inference-service.yaml | kubectl apply -f -
  environment:
    name: production
    url: https://model.example.com
  when: manual  # 手动触发生产部署
  dependencies:
    - register-model
  only:
    - main
```

---


## 8. Experiment Management Best Practices

### 8.1 Experiment Naming Conventions

```python
"""
推荐的实验命名格式：
{model}_{task}_{date}_{variant}

示例：
- bert_sentiment_20240115_baseline
- llama2-7b_instruction_20240115_lora-r8
- resnet50_imagenet_20240115_mixup
"""

import mlflow
from datetime import datetime

def create_run_name(model_name, task, variant=""):
    date_str = datetime.now().strftime("%Y%m%d")
    parts = [model_name, task, date_str]
    if variant:
        parts.append(variant)
    return "_".join(parts)

# Usage
run_name = create_run_name("bert-base", "sentiment", "lr2e5")
with mlflow.start_run(run_name=run_name):
    # Training Code
    pass
```

### 8.2 Information That Must Be Recorded

**1. Code Version:**
```python
import subprocess

git_commit = subprocess.check_output(['git', 'rev-parse', 'HEAD']).decode('ascii').strip()
git_branch = subprocess.check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).decode('ascii').strip()

mlflow.log_param("git_commit", git_commit)
mlflow.log_param("git_branch", git_branch)
mlflow.set_tag("git_repo", "github.com/org/repo")
```

**2. Data Version:**
```python
# Usage DVC
import dvc.api

data_version = dvc.api.get_url("data/train.csv", rev="main")
mlflow.log_param("data_version", data_version)
mlflow.log_param("data_commit", dvc.api.get_rev())
```

**3. Environment Information:**
```python
import torch
import transformers
import sys

mlflow.log_param("python_version", sys.version)
mlflow.log_param("pytorch_version", torch.__version__)
mlflow.log_param("transformers_version", transformers.__version__)
mlflow.log_param("cuda_version", torch.version.cuda)
mlflow.log_param("gpu_count", torch.cuda.device_count())
mlflow.log_param("gpu_name", torch.cuda.get_device_name(0))
```

**4. Data Statistics:**
```python
mlflow.log_param("train_samples", len(train_dataset))
mlflow.log_param("val_samples", len(val_dataset))
mlflow.log_param("num_classes", num_classes)
mlflow.log_param("avg_sequence_length", avg_seq_len)
```

### 8.3 Model Performance Tracking

```python
# Training Process Tracking
class MLflowCallback:
    def __init__(self, log_every_n_steps=10):
        self.log_every_n_steps = log_every_n_steps
        self.step = 0
    
    def on_batch_end(self, loss, metrics):
        self.step += 1
        if self.step % self.log_every_n_steps == 0:
            mlflow.log_metric("train_loss", loss, step=self.step)
            for key, value in metrics.items():
                mlflow.log_metric(f"train_{key}", value, step=self.step)
    
    def on_epoch_end(self, epoch, val_metrics):
        for key, value in val_metrics.items():
            mlflow.log_metric(f"val_{key}", value, step=epoch)

# Usage
callback = MLflowCallback(log_every_n_steps=10)

for epoch in range(num_epochs):
    for batch in train_loader:
        loss = train_step(batch)
        callback.on_batch_end(loss, {"accuracy": acc})
    
    val_metrics = evaluate()
    callback.on_epoch_end(epoch, val_metrics)
```

---


## 9. Cost and ROI Analysis

| Platform | Deployment Cost | Maintenance Cost | Functionality Integrity | Recommended Scenarios |
|-----|---------|---------|-----------|---------|
| **MLflow** | Low (self-hosted) | Low | ★★★☆☆ | Small teams, basic tracking |
| **W&B** | Medium (SaaS) | Very Low | ★★★★★ | Research teams, rapid iteration |
| **Kubeflow** | High (complex) | High | ★★★★☆ | Enterprise-level, end-to-end |
| **self-built solution** | extremely high | extremely high | customized | large companies, strong customization needs |

**cost-saving strategies:**
- MLflow self-built: $200/month (K8s cluster + PostgreSQL + S3)
- W&B Team edition: $50/user/month (but saves development time)
- Hybrid solution: MLflow tracking + W&B visualization (optimal value for money)

---


## 10. Monitoring Alerts

```yaml
# Prometheus Alert Rules
groups:
- name: mlflow_alerts
  interval: 30s
  rules:
  - alert: MLflowServerDown
    expr: up{job="mlflow-server"} == 0
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "MLflow service unavailable"
  
  - alert: ExperimentRunFailureRateHigh
    expr: rate(mlflow_run_failures_total[10m]) > 0.1
    for: 15m
    labels:
      severity: warning
    annotations:
      summary: "exceeds 10% failure rate in experiments"
  
  - alert: ModelRegistrationStuck
    expr: (time() - mlflow_last_model_registration_timestamp) > 86400
    for: 1h
    labels:
      severity: info
    annotations:
      summary: "more than 24 hours without new model registration"
```

---

**related tables:**
- [111-AI infrastructure architecture](./01-ai-infrastructure.md)
- [112-Distributed training frameworks](./05-distributed-training-frameworks.md)
- [113-AI model registry center](./09-model-registry.md)
- [115-AI data processing Pipeline](./06-ai-data-pipeline.md)
- [116-LLM model Serving architecture](./18-llm-serving-architecture.md)

**version information:**
- MLflow: v2.9.0+
- Weights & Biases: latest
- Kubeflow Pipelines: v2.0+
- Ray Tune: v2.9.0+
- Optuna: v3.5.0+
- Kubernetes: v1.27+

---


## Obsidian Related Documentation

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- index.md|Domain-11 AI Infrastructure — Open Source Project Index]
- AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations (AI/ML Workloads Operations)
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management
- AI Model Deployment and Lifecycle Management

## See Also

- 05-distributed-training-frameworks
- 06-ai-data-pipeline
- 08-automl-hyperparameter-tuning
- 09-model-registry

## Related

- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Knowledge Graph Index]]


<!-- risk-assessed -->
