---
title: 132 - AI/ML Workload Operations
description: '# 132 - AI/ML Workload Operations'
summary: '"synchronize_checkpoint_boundary": false,'
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
- grafana
- istio
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
- What is AI/ML Workload Operations
- How to do AI/ML Workload Operations
- Kubernetes 11 AI infra Best Practices
trigger_keywords:
- AI
- ML Workload Operations
- AI
- ML
- Workloads
- Operations
- ai
- infra
prerequisites:
- kubectl-basics
- pod-lifecycle
- service-mesh-basics
- prometheus-basics
- monitoring-basics
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
source_path: tree/infrastructure/kubernetes/ai/infrastructure/02-ai-ml-workloads.md
---

> **Production Environment Security Tips**
>
> Commands contained herein are executable directly. Execute only after confirming: the target cluster and namespace are correct; you have sufficient RBAC permissions; and the commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but can usually be rolled back), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# 132 - AI/ML Workloads Operations

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25-v1.32 | **Last Updated**: 2026-01 | **Reference**: [[entities/kubeflow.md|Kubeflow]]](https://www.kubeflow.org/), [Ray](https://ray.io/)

---


## 1. AI Workloads Overview

### 1.1 AI/ML Workloads Lifecycle

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AI/ML Workload Lifecycle                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐      │
│  │ data preparation │──→│ model training │──→│ model evaluation │──→│ model deployment │──→│ model monitoring │      │
│  │  Data   │   │ Training│   │  Eval   │   │ Serving │   │Monitor │      │
│  └────┬────┘   └────┬────┘   └────┬────┘   └────┬────┘   └────┬────┘      │
│       │             │             │             │             │            │
│       ▼             ▼             ▼             ▼             ▼            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                        Resource Requirements Characteristics              │  │
│  ├──────────┬──────────┬──────────┬──────────┬──────────────────────────┤  │
│  │ High I/O │ Large GPU │ Medium GPU │ Stable GPU │ Low Resources (Monitoring) │  │
│  │ High Storage │ High Bandwidth │ Batch Processing │ Low Latency │ Frequent Sampling │  │
│  │ Batch Processing │ Long Time │ Short Time │ Continuous Run │ Long Term Storage │  │
│  └──────────┴──────────┴──────────┴──────────┴──────────────────────────┘  │
│       │             │             │             │             │            │
│       ▼             ▼             ▼             ▼             ▼            │
│  ┌─────────────────────────────────────────────────────────────────────┐  │
│  │                        Kubernetes Resources                              │  │
│  ├──────────┬──────────┬──────────┬──────────┬──────────────────────────┤  │
│  │ Spark    │PyTorchJob│   Job    │Deployment│ Prometheus               │  │
│  │ Ray Data │ TFJob    │  CronJob │ KServe   │ Grafana                  │  │
│  │ Argo     │ MPIJob   │          │ Triton   │ MLflow                   │  │
│  └──────────┴──────────┴──────────┴──────────┴──────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Workload Types Comparison

| Workload Type | CPU Requirement | GPU Requirement | Memory Requirement | Storage Requirement | Network Requirement | Runtime Length | Fault Tolerance Requirements |
|-------------|---------|---------|---------|---------|---------|---------|---------|
| **Data Preprocessing** | High | Low/None | High | Very High | Medium | Hours | Medium |
| **Feature Engineering** | High | Medium | High | High | Medium | Hours | Medium |
| **Model Pretraining** | Medium | Very High | High | High | Very High | Days/Weeks | High |
| **Model Fine-tuning** | Medium | High | High | High | High | Hours/Days | High |
| **Hyperparameter Search** | High | High | Medium | Medium | Medium | Days | Medium |
| **Model Evaluation** | Medium | Medium | Medium | Medium | Low | Minutes/Hours | Low |
| **Online Inference** | Medium | High/Medium | High | Low | High | Continuous | Very High |
| **Batch Inference** | Medium | High | High | High | Medium | Hours | Medium |

---


## 2. Distributed Training Architecture (Distributed Training)

### 2.1 Distributed Training Paradigms

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      Distributed Training Parallel Strategies                  │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Data Parallel (Data Parallel)                                                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Worker 0      Worker 1      Worker 2      Worker 3                 │   │
│  │  ┌───────┐    ┌───────┐    ┌───────┐    ┌───────┐                  │   │
│  │  │Model  │    │Model  │    │Model  │    │Model  │                  │   │
│  │  │Copy   │    │Copy   │    │Copy   │    │Copy   │                  │   │
│  │  └───┬───┘    └───┬───┘    └───┬───┘    └───┬───┘                  │   │
│  │      │            │            │            │                       │   │
│  │  ┌───┴───┐    ┌───┴───┐    ┌───┴───┐    ┌───┴───┐                  │   │
│  │  │Data   │    │Data   │    │Data   │    │Data   │                  │   │
│  │  │Shard 0│    │Shard 1│    │Shard 2│    │Shard 3│                  │   │
│  │  └───────┘    └───────┘    └───────┘    └───────┘                  │   │
│  │                    ↓ All-Reduce Gradient Synchronization ↓                          │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Model Parallel - Tensor Parallel                                        │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                         Model Layer                                  │   │
│  │  ┌───────────┬───────────┬───────────┬───────────┐                  │   │
│  │  │ Tensor    │ Tensor    │ Tensor    │ Tensor    │                  │   │
│  │  │ Shard 0   │ Shard 1   │ Shard 2   │ Shard 3   │                  │   │
│  │  │ (GPU 0)   │ (GPU 1)   │ (GPU 2)   │ (GPU 3)   │                  │   │
│  │  └───────────┴───────────┴───────────┴───────────┘                  │   │
│  │                    ↔ All-Gather/Reduce-Scatter ↔                    │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Pipeline Parallel (Pipeline Parallel)                                     │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Stage 0        Stage 1        Stage 2        Stage 3               │   │
│  │  (Layers 0-7)   (Layers 8-15)  (Layers 16-23) (Layers 24-31)       │   │
│  │  ┌───────┐     ┌───────┐      ┌───────┐      ┌───────┐             │   │
│  │  │ GPU 0 │ ──→ │ GPU 1 │ ──→  │ GPU 2 │ ──→  │ GPU 3 │             │   │
│  │  └───────┘     └───────┘      └───────┘      └───────┘             │   │
│  │     ↑                                            │                  │   │
│  │     └────────────── Backward ────────────────────┘                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Kubeflow Training Operator

```yaml
# PyTorchJob Production Configuration
apiVersion: "kubeflow.org/v1"
kind: PyTorchJob
metadata:
  name: llama-70b-finetune
  namespace: ml-training
  labels:
    app: llm-training
    model: llama-70b
    stage: finetune
spec:
  # Elastic Training Configuration
  elasticPolicy:
    rdzvBackend: c10d
    minReplicas: 4
    maxReplicas: 8
    maxRestarts: 100
    metrics:
    - type: Resource
      resource:
        name: nvidia.com/gpu
        target:
          type: Utilization
          averageUtilization: 80
          
  # Task Completion Strategy
  runPolicy:
    cleanPodPolicy: None
    backoffLimit: 3
    activeDeadlineSeconds: 604800   # 7天超时
    
  pytorchReplicaSpecs:
    Master:
      replicas: 1
      restartPolicy: OnFailure
      template:
        metadata:
          labels:
            role: master
          annotations:
            prometheus.io/scrape: "true"
            prometheus.io/port: "8080"
        spec:
          priorityClassName: high-priority
          
          # Scheduling Constraints
          nodeSelector:
            nvidia.com/gpu.product: "NVIDIA-A100-SXM4-80GB"
          tolerations:
          - key: "nvidia.com/gpu"
            operator: "Exists"
            effect: "NoSchedule"
            
          containers:
          - name: pytorch
            image: nvcr.io/nvidia/pytorch:24.01-py3
            imagePullPolicy: Always
            
            command: ["torchrun"]
            args:
            - "--nproc_per_node=8"
            - "--nnodes=$(WORLD_SIZE)"
            - "--node_rank=$(RANK)"
            - "--master_addr=$(MASTER_ADDR)"
            - "--master_port=$(MASTER_PORT)"
            - "train.py"
            - "--model_name=meta-llama/Llama-2-70b-hf"
            - "--dataset=/data/finetune_data"
            - "--output_dir=/output"
            - "--per_device_train_batch_size=1"
            - "--gradient_accumulation_steps=8"
            - "--learning_rate=2e-5"
            - "--num_train_epochs=3"
            - "--fp16"
            - "--deepspeed=/config/ds_config.json"
            
            resources:
              requests:
                cpu: "64"
                memory: "512Gi"
                nvidia.com/gpu: "8"
              limits:
                cpu: "64"
                memory: "512Gi"
                nvidia.com/gpu: "8"
                
            env:
            # PyTorch Distributed
            - name: WORLD_SIZE
              value: "4"
            - name: NCCL_DEBUG
              value: "INFO"
            - name: NCCL_IB_DISABLE
              value: "0"
            - name: NCCL_NET_GDR_LEVEL
              value: "5"
            # CUDA Optimization
            - name: CUDA_DEVICE_MAX_CONNECTIONS
              value: "1"
            - name: PYTORCH_CUDA_ALLOC_CONF
              value: "max_split_size_mb:512"
              
            volumeMounts:
            - name: shm
              mountPath: /dev/shm
            - name: data
              mountPath: /data
            - name: output
              mountPath: /output
            - name: config
              mountPath: /config
              
            # Health Checks
            livenessProbe:
              exec:
                command:
                - python
                - -c
                - "import torch; assert torch.cuda.is_available()"
              initialDelaySeconds: 60
              periodSeconds: 60
              
          volumes:
          - name: shm
            emptyDir:
              medium: Memory
              sizeLimit: "128Gi"
          - name: data
            persistentVolumeClaim:
              claimName: training-data-pvc
          - name: output
            persistentVolumeClaim:
              claimName: model-output-pvc
          - name: config
            configMap:
              name: deepspeed-config
              
    Worker:
      replicas: 3
      restartPolicy: OnFailure
      template:
        spec:
          # Same Configuration as Master...
          nodeSelector:
            nvidia.com/gpu.product: "NVIDIA-A100-SXM4-80GB"
          tolerations:
          - key: "nvidia.com/gpu"
            operator: "Exists"
            effect: "NoSchedule"
          containers:
          - name: pytorch
            image: nvcr.io/nvidia/pytorch:24.01-py3
            resources:
              limits:
                nvidia.com/gpu: "8"
            # Other Configurations Same as Master...
```

### 2.3 DeepSpeed Configuration

```yaml
# DeepSpeed ZeRO-3 Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: deepspeed-config
  namespace: ml-training
data:
  ds_config.json: |
    {
      "train_batch_size": "auto",
      "train_micro_batch_size_per_gpu": "auto",
      "gradient_accumulation_steps": "auto",
      
      "zero_optimization": {
        "stage": 3,
        "offload_optimizer": {
          "device": "cpu",
          "pin_memory": true
        },
        "offload_param": {
          "device": "cpu",
          "pin_memory": true
        },
        "overlap_comm": true,
        "contiguous_gradients": true,
        "sub_group_size": 1e9,
        "reduce_bucket_size": "auto",
        "stage3_prefetch_bucket_size": "auto",
        "stage3_param_persistence_threshold": "auto",
        "stage3_max_live_parameters": 1e9,
        "stage3_max_reuse_distance": 1e9,
        "stage3_gather_16bit_weights_on_model_save": true
      },
      
      "fp16": {
        "enabled": true,
        "loss_scale": 0,
        "loss_scale_window": 1000,
        "initial_scale_power": 16,
        "hysteresis": 2,
        "min_loss_scale": 1
      },
      
      "bf16": {
        "enabled": false
      },
      
      "gradient_clipping": 1.0,
      
      "optimizer": {
        "type": "AdamW",
        "params": {
          "lr": "auto",
          "betas": [0.9, 0.999],
          "eps": 1e-8,
          "weight_decay": "auto"
        }
      },
      
      "scheduler": {
        "type": "WarmupDecayLR",
        "params": {
          "warmup_min_lr": 0,
          "warmup_max_lr": "auto",
          "warmup_num_steps": "auto",
          "total_num_steps": "auto"
        }
      },
      
      "activation_checkpointing": {
        "partition_activations": true,
        "cpu_checkpointing": true,
        "contiguous_memory_optimization": true,
        "number_checkpoints": null,
        "synchronize_checkpoint_boundary": false,
        "profile": false
      },
      
      "wall_clock_breakdown": false,
      "tensorboard": {
        "enabled": true,
        "output_path": "/output/tensorboard",
        "job_name": "llama-70b-finetune"
      }
    }
```

---


## 3. Model Inference Services (Model Serving)

### 3.1 Serving Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      Model Inference Service Architecture                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        Traffic Entry Layer                                    │   │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │   │
│  │  │   Ingress    │  │ Gateway API  │  │   Istio      │              │   │
│  │  │   (NGINX)    │  │              │  │  VirtualSvc  │              │   │
│  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘              │   │
│  │         └─────────────────┼─────────────────┘                       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                              │
│                              ▼                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        Inference Gateway Layer                                    │   │
│  │  ┌──────────────────────────────────────────────────────────────┐   │   │
│  │  │  KServe Predictor / Triton Inference Server                  │   │   │
│  │  │  ├── Request Routing                                                 │   │   │
│  │  │  ├── Load Balancing                                                 │   │   │
│  │  │  ├── Traffic Mirroring                                                 │   │   │
│  │  │  ├── Canary Release                                               │   │   │
│  │  │  └── A/B Testing                                                  │   │   │
│  │  └──────────────────────────────────────────────────────────────┘   │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                              │                                              │
│          ┌───────────────────┼───────────────────┐                         │
│          ▼                   ▼                   ▼                         │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐                    │
│  │  Predictor  │    │  Predictor  │    │  Predictor  │                    │
│  │  (vLLM)     │    │  (TGI)      │    │  (Triton)   │                    │
│  │  ┌───────┐  │    │  ┌───────┐  │    │  ┌───────┐  │                    │
│  │  │LLaMA  │  │    │  │Falcon │  │    │  │BERT   │  │                    │
│  │  │70B    │  │    │  │40B    │  │    │  │Base   │  │                    │
│  │  └───────┘  │    │  └───────┘  │    │  └───────┘  │                    │
│  │  4x A100    │    │  2x A100    │    │  1x T4      │                    │
│  └─────────────┘    └─────────────┘    └─────────────┘                    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 3.2 KServe Deployment Configuration

```yaml
# KServe InferenceService (Production Configuration)
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: llama-70b-chat
  namespace: ml-serving
  annotations:
    # Auto-scaling Configuration
    autoscaling.knative.dev/class: "kpa.autoscaling.knative.dev"
    autoscaling.knative.dev/metric: "concurrency"
    autoscaling.knative.dev/target: "10"
    autoscaling.knative.dev/minScale: "2"
    autoscaling.knative.dev/maxScale: "10"
    # GPU Scheduling
    serving.kserve.io/enable-prometheus-scraping: "true"
spec:
  predictor:
    # Canary Release
    canaryTrafficPercent: 10
    
    # Model Configuration
    model:
      modelFormat:
        name: pytorch
      runtime: kserve-vllm
      storageUri: "s3://models/llama-2-70b-chat"
      
    # Container Configuration
    containers:
    - name: kserve-container
      image: vllm/vllm-openai:latest
      args:
      - "--model=/mnt/models"
      - "--tensor-parallel-size=4"
      - "--max-model-len=4096"
      - "--gpu-memory-utilization=0.9"
      - "--quantization=awq"
      
      resources:
        requests:
          cpu: "16"
          memory: "64Gi"
          nvidia.com/gpu: "4"
        limits:
          cpu: "32"
          memory: "128Gi"
          nvidia.com/gpu: "4"
          
      env:
      - name: CUDA_VISIBLE_DEVICES
        value: "0,1,2,3"
      - name: VLLM_WORKER_MULTIPROC_METHOD
        value: "spawn"
        
      # Health Checks
      readinessProbe:
        httpGet:
          path: /health
          port: 8080
        initialDelaySeconds: 120
        periodSeconds: 10
        failureThreshold: 3
        
      livenessProbe:
        httpGet:
          path: /health
          port: 8080
        initialDelaySeconds: 180
        periodSeconds: 30
        
    # Node Selection
    nodeSelector:
      nvidia.com/gpu.product: "NVIDIA-A100-SXM4-80GB"
    tolerations:
    - key: "nvidia.com/gpu"
      operator: "Exists"
      effect: "NoSchedule"
      
  # Transformer (Optional Preprocessing)
  transformer:
    containers:
    - name: transformer
      image: ml-platform/llm-transformer:latest
      resources:
        requests:
          cpu: "2"
          memory: "4Gi"
          
---
# HPA Configuration (GPU Utilization Scaling)
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: llama-70b-chat-hpa
  namespace: ml-serving
spec:
  scaleTargetRef:
    apiVersion: serving.kserve.io/v1beta1
    kind: InferenceService
    name: llama-70b-chat
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: External
    external:
      metric:
        name: "prometheus-adapter/gpu_utilization"
        selector:
          matchLabels:
            service: llama-70b-chat
      target:
        type: AverageValue
        averageValue: "80"
```

### 3.3 vLLM High-Performance Inference

```yaml
# vLLM Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-llama-70b
  namespace: ml-serving
spec:
  replicas: 2
  selector:
    matchLabels:
      app: vllm-llama-70b
  template:
    metadata:
      labels:
        app: vllm-llama-70b
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8000"
    spec:
      containers:
      - name: vllm
        image: vllm/vllm-openai:latest
        
        args:
        - "--model=/models/llama-2-70b-chat-hf"
        - "--tensor-parallel-size=4"
        - "--pipeline-parallel-size=1"
        - "--max-model-len=8192"
        - "--max-num-seqs=256"
        - "--gpu-memory-utilization=0.92"
        - "--quantization=awq"
        - "--dtype=float16"
        # Performance Optimization
        - "--enable-prefix-caching"
        - "--use-v2-block-manager"
        - "--enable-chunked-prefill"
        # API Configuration
        - "--host=0.0.0.0"
        - "--port=8000"
        - "--api-key=$(API_KEY)"
        
        ports:
        - containerPort: 8000
          name: http
          
        resources:
          requests:
            cpu: "32"
            memory: "128Gi"
            nvidia.com/gpu: "4"
          limits:
            cpu: "64"
            memory: "256Gi"
            nvidia.com/gpu: "4"
            
        env:
        - name: API_KEY
          valueFrom:
            secretKeyRef:
              name: vllm-secrets
              key: api-key
        - name: CUDA_VISIBLE_DEVICES
          value: "0,1,2,3"
        - name: NCCL_DEBUG
          value: "WARN"
        - name: VLLM_ATTENTION_BACKEND
          value: "FLASH_ATTN"
          
        volumeMounts:
        - name: models
          mountPath: /models
        - name: shm
          mountPath: /dev/shm
          
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 180
          periodSeconds: 10
          
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 300
          periodSeconds: 30
          timeoutSeconds: 10
          
      volumes:
      - name: models
        persistentVolumeClaim:
          claimName: llm-models-pvc
      - name: shm
        emptyDir:
          medium: Memory
          sizeLimit: "32Gi"
          
      nodeSelector:
        nvidia.com/gpu.product: "NVIDIA-A100-SXM4-80GB"
      tolerations:
      - key: "nvidia.com/gpu"
        operator: "Exists"
        effect: "NoSchedule"
```

---


## 4. Data Processing Pipeline

### 4.1 Spark on Kubernetes

```yaml
# SparkApplication for Data Processing
apiVersion: sparkoperator.k8s.io/v1beta2
kind: SparkApplication
metadata:
  name: data-preprocessing
  namespace: ml-data
spec:
  type: Python
  pythonVersion: "3"
  mode: cluster
  image: "spark-py:3.5.0"
  imagePullPolicy: Always
  mainApplicationFile: "s3a://scripts/preprocess.py"
  
  arguments:
  - "--input=s3a://raw-data/dataset"
  - "--output=s3a://processed-data/dataset"
  - "--partitions=1000"
  
  sparkVersion: "3.5.0"
  
  # Spark Configuration
  sparkConf:
    "spark.kubernetes.allocation.batch.size": "10"
    "spark.sql.shuffle.partitions": "1000"
    "spark.sql.adaptive.enabled": "true"
    "spark.sql.adaptive.coalescePartitions.enabled": "true"
    "spark.serializer": "org.apache.spark.serializer.KryoSerializer"
    # S3 Configuration
    "spark.hadoop.fs.s3a.impl": "org.apache.hadoop.fs.s3a.S3AFileSystem"
    "spark.hadoop.fs.s3a.fast.upload": "true"
    "spark.hadoop.fs.s3a.fast.upload.buffer": "bytebuffer"
    
  # Driver Configuration
  driver:
    cores: 4
    coreLimit: "4"
    memory: "16g"
    labels:
      version: "3.5.0"
    serviceAccount: spark-sa
    
  # Executor Configuration
  executor:
    cores: 4
    instances: 50
    memory: "32g"
    labels:
      version: "3.5.0"
    
  # Dynamic Allocation
  dynamicAllocation:
    enabled: true
    initialExecutors: 10
    minExecutors: 5
    maxExecutors: 100
    
  restartPolicy:
    type: OnFailure
    onFailureRetries: 3
    onFailureRetryInterval: 10
    onSubmissionFailureRetries: 5
    onSubmissionFailureRetryInterval: 20
```

### 4.2 Ray Data Processing

```yaml
# RayJob for Data Processing
apiVersion: ray.io/v1
kind: RayJob
metadata:
  name: data-pipeline
  namespace: ml-data
spec:
  entrypoint: python /app/data_pipeline.py
  
  runtimeEnvYAML: |
    pip:
      - pandas==2.0.0
      - pyarrow==14.0.0
      - datasets==2.16.0
    env_vars:
      DATA_PATH: "s3://raw-data"
      OUTPUT_PATH: "s3://processed-data"
      
  rayClusterSpec:
    rayVersion: '2.9.0'
    
    headGroupSpec:
      rayStartParams:
        dashboard-host: '0.0.0.0'
      template:
        spec:
          containers:
          - name: ray-head
            image: rayproject/ray:2.9.0-py310
            resources:
              limits:
                cpu: "8"
                memory: "32Gi"
              requests:
                cpu: "4"
                memory: "16Gi"
            volumeMounts:
            - name: app-code
              mountPath: /app
          volumes:
          - name: app-code
            configMap:
              name: data-pipeline-code
              
    workerGroupSpecs:
    - replicas: 10
      minReplicas: 5
      maxReplicas: 50
      groupName: data-workers
      rayStartParams: {}
      template:
        spec:
          containers:
          - name: ray-worker
            image: rayproject/ray:2.9.0-py310
            resources:
              limits:
                cpu: "16"
                memory: "64Gi"
              requests:
                cpu: "8"
                memory: "32Gi"
                
  submitterPodTemplate:
    spec:
      restartPolicy: Never
      containers:
      - name: submitter
        image: rayproject/ray:2.9.0-py310
```

---


## 5. Experiment Management and MLOps (Experiment Management)

### 5.1 MLflow Deployment

```yaml
# MLflow Tracking Server
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mlflow-tracking
  namespace: mlops
spec:
  replicas: 2
  selector:
    matchLabels:
      app: mlflow-tracking
  template:
    metadata:
      labels:
        app: mlflow-tracking
    spec:
      containers:
      - name: mlflow
        image: ghcr.io/mlflow/mlflow:v2.10.0
        
        command: ["mlflow", "server"]
        args:
        - "--host=0.0.0.0"
        - "--port=5000"
        - "--backend-store-uri=postgresql://$(DB_USER):$(DB_PASSWORD)@postgres:5432/mlflow"
        - "--default-artifact-root=s3://mlflow-artifacts"
        - "--serve-artifacts"
        
        ports:
        - containerPort: 5000
          name: http
          
        resources:
          requests:
            cpu: "2"
            memory: "4Gi"
          limits:
            cpu: "4"
            memory: "8Gi"
            
        env:
        - name: DB_USER
          valueFrom:
            secretKeyRef:
              name: mlflow-secrets
              key: db-user
        - name: DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mlflow-secrets
              key: db-password
        - name: AWS_ACCESS_KEY_ID
          valueFrom:
            secretKeyRef:
              name: mlflow-secrets
              key: aws-access-key
        - name: AWS_SECRET_ACCESS_KEY
          valueFrom:
            secretKeyRef:
              name: mlflow-secrets
              key: aws-secret-key
              
        livenessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 30
          periodSeconds: 10
          
        readinessProbe:
          httpGet:
            path: /health
            port: 5000
          initialDelaySeconds: 10
          periodSeconds: 5
```

### 5.2 Kubeflow Pipelines

```yaml
# Kubeflow Pipeline Component
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  generateName: ml-training-pipeline-
  namespace: kubeflow
spec:
  entrypoint: ml-pipeline
  
  templates:
  - name: ml-pipeline
    dag:
      tasks:
      # Data Preprocessing
      - name: data-preprocessing
        template: preprocess
        
      # Feature Engineering
      - name: feature-engineering
        template: feature-eng
        dependencies: [data-preprocessing]
        
      # Model Training
      - name: model-training
        template: train
        dependencies: [feature-engineering]
        
      # Model Evaluation
      - name: model-evaluation
        template: evaluate
        dependencies: [model-training]
        
      # Model Registration
      - name: model-registration
        template: register
        dependencies: [model-evaluation]
        when: "{{tasks.model-evaluation.outputs.result}} > 0.85"
        
  - name: preprocess
    container:
      image: ml-platform/preprocessor:latest
      command: [python, preprocess.py]
      resources:
        requests:
          cpu: "8"
          memory: "32Gi"
          
  - name: feature-eng
    container:
      image: ml-platform/feature-eng:latest
      command: [python, feature_engineering.py]
      resources:
        requests:
          cpu: "16"
          memory: "64Gi"
          
  - name: train
    container:
      image: ml-platform/trainer:latest
      command: [python, train.py]
      resources:
        requests:
          cpu: "32"
          memory: "128Gi"
          nvidia.com/gpu: "8"
    nodeSelector:
      nvidia.com/gpu.present: "true"
      
  - name: evaluate
    container:
      image: ml-platform/evaluator:latest
      command: [python, evaluate.py]
      resources:
        requests:
          cpu: "4"
          memory: "16Gi"
          nvidia.com/gpu: "1"
          
  - name: register
    container:
      image: ml-platform/model-registry:latest
      command: [python, register_model.py]
```

---


## 6. Monitoring & Alerting

### 6.1 AI Workload Monitoring Metrics

| Metric Category | Metric Name | Description | Alert Threshold |
|---------|---------|------|---------|
| **Training Progress** | epoch_progress | Current Epoch Progress | Stagnation > 1h |
| **Training Progress** | training_loss | Training Loss | Abnormal Fluctuation |
| **Training Progress** | validation_loss | Validation Loss | Persistent Increase |
| **Resource Efficiency** | gpu_utilization | GPU Utilization | < 50% |
| **Resource Efficiency** | gpu_memory_used | GPU Memory Usage | > 95% |
| **Resource Efficiency** | samples_per_second | Training Throughput | Decrease > 20% |
| **Inference Performance** | inference_latency_p99 | P99 Inference Latency | > SLA |
| **Inference Performance** | tokens_per_second | Token generation speed | < Baseline |
| **Inference Performance** | queue_depth | Request queue depth | > 100 |
| **System Health** | pod_restart_count | Pod restart count | > 3 |
| **System Health** | oom_kill_count | Out Of Memory count | > 0 |
| **System Health** | nccl_errors | NCCL communication errors | > 0 |

### 6.2 Prometheus Alert Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: ai-workload-alerts
  namespace: monitoring
spec:
  groups:
  - name: ai-training-alerts
    rules:
    # Training Task Stuck
    - alert: TrainingStalled
      expr: |
        rate(training_step_total[30m]) == 0
        and on(job_name) training_job_running == 1
      for: 30m
      labels:
        severity: warning
      annotations:
        summary: "Training task stalled"
        description: "Task {{ $labels.job_name }} no progress in the last 30 minutes"
        
    # Training Loss Abnormal
    - alert: TrainingLossAnomaly
      expr: |
        (training_loss - training_loss offset 1h) / training_loss offset 1h > 0.5
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "Training Loss abnormally increased"
        description: "Task {{ $labels.job_name }} Loss increased by more than 50%"
        
    # Low GPU Utilization
    - alert: TrainingGPUUnderutilized
      expr: |
        avg by (job_name) (DCGM_FI_DEV_GPU_UTIL{job_type="training"}) < 50
      for: 30m
      labels:
        severity: warning
      annotations:
        summary: "Training GPU utilization low"
        description: "Task {{ $labels.job_name }} GPU utilization {{ $value }}%"
        
    # Failed to Save Checkpoint
    - alert: CheckpointSaveFailed
      expr: |
        increase(checkpoint_save_errors_total[1h]) > 0
      for: 0m
      labels:
        severity: critical
      annotations:
        summary: "Checkpoint save failed"
        description: "Task {{ $labels.job_name }} checkpoint save abnormal"
        
  - name: ai-inference-alerts
    rules:
    # High Inference Latency
    - alert: InferenceLatencyHigh
      expr: |
        histogram_quantile(0.99, rate(inference_latency_seconds_bucket[5m])) > 2
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Inference P99 latency exceeds 2 seconds"
        description: "Service {{ $labels.service }} P99 latency: {{ $value }}s"
        
    # Inference Queue Backlog
    - alert: InferenceQueueBacklog
      expr: |
        inference_queue_depth > 100
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Inference request queue backlog"
        description: "Service {{ $labels.service }} queue depth: {{ $value }}"
        
    # High Inference Error Rate
    - alert: InferenceErrorRateHigh
      expr: |
        rate(inference_errors_total[5m]) / rate(inference_requests_total[5m]) > 0.01
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Inference error rate exceeds 1%"
        description: "Service {{ $labels.service }} error rate: {{ $value | humanizePercentage }}"
        
    # GPU OOM
    - alert: InferenceGPUOOM
      expr: |
        increase(inference_oom_errors_total[5m]) > 0
      for: 0m
      labels:
        severity: critical
      annotations:
        summary: "Inference service GPU OOM"
        description: "Service {{ $labels.service }} GPU memory shortage occurs"
```

---


## wo,Storage and Network Acceleration

### 7.1 High-Performance Storage Configuration

```yaml
# JuiceFS for AI Data
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: ai-training-data
  namespace: ml-training
spec:
  accessModes:
  - ReadWriteMany
  resources:
    requests:
      storage: 10Ti
  storageClassName: juicefs-sc
  
---
# JuiceFS StorageClass
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: juicefs-sc
provisioner: csi.juicefs.com
parameters:
  csi.storage.k8s.io/provisioner-secret-name: juicefs-secret
  csi.storage.k8s.io/provisioner-secret-namespace: kube-system
  csi.storage.k8s.io/node-publish-secret-name: juicefs-secret
  csi.storage.k8s.io/node-publish-secret-namespace: kube-system
  
---
# Fluid Dataset Warmup
apiVersion: data.fluid.io/v1alpha1
kind: Dataset
metadata:
  name: training-dataset
  namespace: ml-training
spec:
  mounts:
  - mountPoint: "s3://ml-datasets/imagenet"
    name: imagenet
    options:
      region: us-east-1
      
---
apiVersion: data.fluid.io/v1alpha1
kind: AlluxioRuntime
metadata:
  name: training-dataset
  namespace: ml-training
spec:
  replicas: 10
  tieredstore:
    levels:
    - mediumtype: MEM
      path: /dev/shm
      quota: 64Gi
      high: "0.95"
      low: "0.7"
    - mediumtype: SSD
      path: /mnt/ssd
      quota: 500Gi
      high: "0.95"
      low: "0.7"
  master:
    replicas: 3
  worker:
    resources:
      requests:
        cpu: "8"
        memory: "32Gi"
      limits:
        cpu: "16"
        memory: "64Gi"
```

### 7.2 RDMA Network Configuration

```yaml
# Multus RDMA Network Configuration
apiVersion: k8s.cni.cncf.io/v1
kind: NetworkAttachmentDefinition
metadata:
  name: rdma-net
  namespace: ml-training
spec:
  config: |
    {
      "cniVersion": "0.3.1",
      "type": "host-device",
      "device": "mlx5_0",
      "ipam": {
        "type": "whereabouts",
        "range": "192.168.100.0/24"
      }
    }
    
---
# Use RDMA Network for Training Pods
apiVersion: v1
kind: Pod
metadata:
  name: rdma-training-pod
  namespace: ml-training
  annotations:
    k8s.v1.cni.cncf.io/networks: rdma-net
spec:
  containers:
  - name: trainer
    image: nvcr.io/nvidia/pytorch:24.01-py3
    resources:
      limits:
        nvidia.com/gpu: 8
        rdma/rdma_shared_device_a: 1
    env:
    - name: NCCL_IB_DISABLE
      value: "0"
    - name: NCCL_NET_GDR_LEVEL
      value: "5"
    - name: NCCL_IB_HCA
      value: "mlx5"
    - name: NCCL_DEBUG
      value: "INFO"
```

---


## 8. Quick Reference

### 8.1 Common Commands

> ⚠️ **Yellow Alert Change** — Change cluster resource status, suggest first using --dry-run or diff to confirm
> - `kubectl exec`: Enter container to execute commands, which may change container state

``` bash
# 🟡 Medium Risk: Will modify cluster/resource status, please confirm target, impact scope, and authorization before execution
# ========== Training Task Management ==========

# View PyTorchJob
kubectl get pytorchjobs -n ml-training
kubectl describe pytorchjob <name> -n ml-training

# View Training Logs
kubectl logs -n ml-training <master-pod> -f

# View Training Metrics
kubectl exec -it <pod> -- nvidia-smi dmon -s pucvmet

# ========== Inference Service Management ==========

# View InferenceService
kubectl get inferenceservices -n ml-serving
kubectl describe inferenceservice <name> -n ml-serving

# Test Inference Service
curl -X POST http://<service>/v1/completions \
  -H "Content-Type: application/json" \
  -d '{"prompt": "Hello", "max_tokens": 100}'

# ========== Queue Management ==========

# Kueue Queue Status
kubectl get clusterqueues
kubectl get localqueues -n ml-training
kubectl get workloads -n ml-training

# Volcano Queue Status
kubectl get queues -n volcano-system
kubectl get podgroups -n ml-training
```
### 8.2 Resource Requirements Quick Reference

| Model Size | GPU Type | GPU Count | Memory Requirement | Training Duration |
|---------|--------|--------|---------|---------|
| 1B | A10G | 1-2 | 24GB | 1-2 days |
| 7B | A100 40GB | 2-4 | 80-160GB | 3-7 days |
| 13B | A100 80GB | 4-8 | 160-320GB | 1-2 weeks |
| 70B | A100 80GB | 16-32 | 640-1280GB | 2-4 weeks |
| 175B | H100 | 64-128 | 2.5-5TB | 1-2 months |

---

**AI Workload Principles**: Resource estimation sufficient → Monitoring coverage complete → Checkpoint strategy sound → Elastic scaling configuration

---

**Table Bottom Markers**: Kusheet Project, Author Allen Galler (allengaller@gmail.com)

---


## Obsidian Documentation

- domain-11-ai-infra MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Open Source Project Index
- AI Infrastructure Architecture
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed training framework
- AI data processing Pipeline and feature engineering
- AI experiment management and MLOps platform
- AutoML and hyperparameter tuning
- AI model registration center and version management
- AI model deployment and lifecycle management

## See Also

- 99-kubeflow-ai-platform-guide
- 01-ai-infrastructure-overview
- 03-gpu-scheduling-management
- 04-gpu-monitoring-dcgm

## Related

- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Knowledge Graph Index]]


<!-- risk-assessed -->
