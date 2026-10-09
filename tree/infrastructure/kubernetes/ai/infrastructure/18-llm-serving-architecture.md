---
title: LLM Model Serving Architecture and Inference Optimization
description: '# LLM Model Serving Architecture and Inference Optimization'
summary: 'python -m vllm.entrypoints.openai.api_server \'
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
- jaeger
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
- What is LLM Model Serving Architecture and Inference Optimization
- How to optimize LLM Model Serving Architecture and Inference Optimization
- Kubernetes 11 ai infra best practices
trigger_keywords:
- LLM Model Serving Architecture and Inference Optimization
- ai
- infra
prerequisites:
- kubectl-basics
- service-mesh-basics
- prometheus-basics
- monitoring-basics
- redis-basics
- gpu-scheduling-basics
- logging-basics
- tracing-basics
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
source_path: tree/infrastructure/kubernetes/ai/infrastructure/18-llm-serving-architecture.md
---

> **Production Environment Security Reminders**
>
> This document contains executable operational commands. Execute them only after confirming: the correct target cluster and namespace; sufficient RBAC permissions; validation in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering, no side effects).




# LLM Model Serving Architecture and Inference Optimization


## 1. LLM Inference Architecture Overview

```
┌──────────────────────────────────────────────────────────────────────────┐
│                        LLM Serving complete architecture                                │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│  ┌────────────┐       ┌────────────┐       ┌────────────┐               │
│  │  Load Balancing   │──────▶│  Routing Layer     │──────▶│  Inference Engine   │               │
│  │ Istio/Nginx│       │ KServe     │       │ vLLM/TGI   │               │
│  └────────────┘       │ Seldon Core│       │ TensorRT   │               │
│       │               └────────────┘       │ Triton     │               │
│       │                     │              └────────────┘               │
│       ▼                     ▼                    │                       │
│  ┌────────────┐       ┌────────────┐            ▼                       │
│  │  Authentication   │       │  Model Management   │       ┌────────────┐               │
│  │  API Key   │       │  Version Control   │       │  GPU Scheduling    │               │
│  │  OAuth2    │       │  A/B Testing   │       │  MIG/MPS   │               │
│  └────────────┘       └────────────┘       │  Time-Slice│               │
│                                             └────────────┘               │
│  ┌────────────┐       ┌────────────┐       ┌────────────┐               │
│  │  Request Queue   │──────▶│  Batch Processing Layer   │──────▶│  Cache Layer     │               │
│  │  Priority     │       │ Continuous │       │  Redis     │               │
│  │  Rate Limiting   │       │  Batching  │       │  KV Cache  │               │
│  └────────────┘       └────────────┘       └────────────┘               │
│                                                                            │
│  ┌────────────────────────────────────────────────────────┐              │
│  │              Observability Layer                                 │              │
│  │  • Prometheus Metrics  • Jaeger Trace  • Log Aggregation        │              │
│  └────────────────────────────────────────────────────────┘              │
└──────────────────────────────────────────────────────────────────────────┘
```

---


## 2. vLLM High-Performance Inference Engine

### 2.1 vLLM Core Technologies

**PagedAttention mechanism:**
- Store KV Cache in pages, similar to operating system virtual memory
- Memory utilization increases to 95% (traditional method at 60%)
- Supports dynamic batching, throughput improves by 10-20 times

**Continuous Batching:**
- Traditional batching: waits for all requests in a batch to complete
- Continuous Batching: replaces new requests immediately upon completion, maximizing GPU utilization

### 2.2 vLLM Deployment Configuration

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: vllm-config
  namespace: ai-platform
data:
  start_server.sh: |
    #!/bin/bash
    python -m vllm.entrypoints.openai.api_server \
      --model /models/llama-2-13b \
      --tensor-parallel-size 4 \
      --gpu-memory-utilization 0.95 \
      --max-num-seqs 256 \
      --max-model-len 4096 \
      --dtype float16 \
      --enforce-eager \
      --disable-log-requests \
      --trust-remote-code
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-llama2-13b
  namespace: ai-platform
spec:
  replicas: 2
  selector:
    matchLabels:
      app: vllm-server
      model: llama2-13b
  template:
    metadata:
      labels:
        app: vllm-server
        model: llama2-13b
    spec:
      # Bind to GPU node
      nodeSelector:
        nvidia.com/gpu.product: NVIDIA-A100-SXM4-80GB
      
      # Anti-affinity: improve availability across different nodes
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
                  - vllm-server
              topologyKey: kubernetes.io/hostname
      
      containers:
      - name: vllm-server
        image: vllm/vllm-openai:v0.3.0
        command: ["/bin/bash", "/config/start_server.sh"]
        ports:
        - containerPort: 8000
          name: http
          protocol: TCP
        
        env:
        - name: HF_HOME
          value: "/models/.cache"
        - name: CUDA_VISIBLE_DEVICES
          value: "0,1,2,3"  # 4卡张量并行
        
        # GPU resource request
        resources:
          requests:
            cpu: "16"
            memory: "64Gi"
            nvidia.com/gpu: 4
          limits:
            cpu: "32"
            memory: "128Gi"
            nvidia.com/gpu: 4
        
        # Health check
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 120
          periodSeconds: 30
          timeoutSeconds: 10
        
        readinessProbe:
          httpGet:
            path: /v1/models
            port: 8000
          initialDelaySeconds: 60
          periodSeconds: 10
        
        volumeMounts:
        - name: model-storage
          mountPath: /models
          readOnly: true
        - name: config
          mountPath: /config
        - name: shm
          mountPath: /dev/shm
      
      volumes:
      - name: model-storage
        persistentVolumeClaim:
          claimName: llama2-13b-pvc
      - name: config
        configMap:
          name: vllm-config
          defaultMode: 0755
      - name: shm
        emptyDir:
          medium: Memory
          sizeLimit: 32Gi  # 共享内存用于张量并行通信
---
apiVersion: v1
kind: Service
metadata:
  name: vllm-llama2-13b-svc
  namespace: ai-platform
spec:
  type: ClusterIP
  ports:
  - port: 8000
    targetPort: 8000
    protocol: TCP
    name: http
  selector:
    app: vllm-server
    model: llama2-13b
```

### 2.3 vLLM Client Calls

```python
# OpenAI compatible API call
from openai import OpenAI

client = OpenAI(
    base_url="http://vllm-llama2-13b-svc.ai-platform.svc.cluster.local:8000/v1",
    api_key="dummy-key"  # vLLM默认不需要真实key
)

# Stream generation
stream = client.chat.completions.create(
    model="llama-2-13b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain quantum computing in simple terms."}
    ],
    temperature=0.7,
    max_tokens=512,
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)

# Batch inference (non-streaming)
responses = client.completions.create(
    model="llama-2-13b",
    prompt=[
        "Translate to French: Hello",
        "Translate to Spanish: Hello",
        "Translate to German: Hello"
    ],
    max_tokens=50,
    temperature=0.3
)

for resp in responses.choices:
    print(resp.text)
```

### 2.4 vLLM Performance Optimization

```python
# vLLM advanced configuration
"""
关键参数调优：

1. --tensor-parallel-size 4
   • 模型跨4张GPU切分
   • 适用于单模型无法放入单卡的情况
   • 通信开销：NVLink <5%, PCIe ~20%

2. --gpu-memory-utilization 0.95
   • KV Cache使用95% GPU显存
   • 更高值=更多并发，但可能OOM
   • 推荐：A100 80GB用0.95，A10 24GB用0.90

3. --max-num-seqs 256
   • 最大并发序列数（批量大小）
   • 决定吞吐量上限
   • 受限于GPU显存和模型大小

4. --max-model-len 4096
   • 最大上下文长度
   • 影响KV Cache显存占用
   • Llama2支持4096，可设为2048节省显存

5. --dtype float16
   • 推理精度：float16（FP16）或bfloat16
   • FP16比FP32快2倍，显存减半
   • 精度损失<1%

6. --enforce-eager
   • 禁用CUDA Graph优化
   • 调试时启用，生产环境移除
   • CUDA Graph可再提速10-15%
"""

# Performance monitoring
import requests
response = requests.get("http://vllm-server:8000/metrics")
print(response.text)
# Key metrics:
# - vllm:num_requests_running(current request count)
# - vllm:gpu_cache_usage_perc(KV Cache usage rate)
# - vllm:time_to_first_token(TTFT)
# - vllm:time_per_output_token(TPOT)
```

---


## 3. Text Generation Inference (TGI)

### 3.1 TGI Features

Hugging Face official inference framework, optimized specifically for generative models.

**Core Advantages:**
- Flash Attention 2 integration (speedup by 2x)
- Paged Attention support
- Quantized inference (GPTQ, AWQ, bitsandbytes)
- Native support for Hugging Face Hub

### 3.2 TGI Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tgi-mistral-7b
  namespace: ai-platform
spec:
  replicas: 3
  selector:
    matchLabels:
      app: tgi-server
      model: mistral-7b
  template:
    metadata:
      labels:
        app: tgi-server
        model: mistral-7b
    spec:
      containers:
      - name: tgi
        image: ghcr.io/huggingface/text-generation-inference:1.4.0
        args:
        - --model-id
        - mistralai/Mistral-7B-Instruct-v0.2
        - --num-shard
        - "1"
        - --max-concurrent-requests
        - "128"
        - --max-input-length
        - "4096"
        - --max-total-tokens
        - "8192"
        - --dtype
        - float16
        - --quantize
        - bitsandbytes-nf4  # 4-bit量化
        
        ports:
        - containerPort: 80
          name: http
        
        env:
        - name: HUGGING_FACE_HUB_TOKEN
          valueFrom:
            secretKeyRef:
              name: hf-token
              key: token
        - name: MAX_BATCH_TOTAL_TOKENS
          value: "1048576"  # 1M tokens批处理
        - name: CUDA_VISIBLE_DEVICES
          value: "0"
        
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
        - name: cache
          mountPath: /data
        - name: shm
          mountPath: /dev/shm
      
      volumes:
      - name: cache
        emptyDir: {}
      - name: shm
        emptyDir:
          medium: Memory
          sizeLimit: 16Gi
---
# HorizontalPodAutoscaler implements automatic scaling
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: tgi-mistral-7b-hpa
  namespace: ai-platform
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: tgi-mistral-7b
  minReplicas: 2
  maxReplicas: 10
  metrics:
  # Scale based on custom metrics
  - type: Pods
    pods:
      metric:
        name: tgi_queue_size
      target:
        type: AverageValue
        averageValue: "10"  # 队列>10时扩容
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300  # 5分钟稳定期
      policies:
      - type: Percent
        value: 50  # 每次最多缩容50%
        periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0  # 立即扩容
      policies:
      - type: Percent
        value: 100  # 每次最多扩容100%
        periodSeconds: 30
```

### 3.3 TGI Quantized Inference

``` bash
# 🟢 Low risk: read-only/information gathering, typically with no side effects
# GPTQ 4-bit quantized inference
docker run --gpus all \
  -p 8080:80 \
  -e MODEL_ID=TheBloke/Llama-2-13B-chat-GPTQ \
  -e QUANTIZE=gptq \
  -e MAX_INPUT_LENGTH=4096 \
  -e MAX_TOTAL_TOKENS=8192 \
  ghcr.io/huggingface/text-generation-inference:1.4.0

# Quantization effect comparison
# Llama-2-13B:
# - FP16: 26GB memory, 30 tokens/s
# - INT8: 13GB memory, 28 tokens/s (speed-7%)
# - INT4(GPTQ): 7GB memory, 25 tokens/s (speed-17%)
# - NF4(bitsandbytes): 7GB memory, 22 tokens/s (speed-27%)
```
---


## 4. NVIDIA Triton Inference Server

### 4.1 Triton Multi-model Serving

Triton supports deploying multiple models simultaneously, sharing GPU resources.

```
┌─────────────────────────────────────┐
│       Triton Inference Server       │
├─────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐          │
│  │ Model 1 │  │ Model 2 │          │
│  │ (BERT)  │  │ (GPT-2) │  ...     │
│  └─────────┘  └─────────┘          │
│        │            │               │
│  ┌─────────────────────────┐       │
│  │   Dynamic Batching      │       │
│  │   GPU Resource Scheduling            │       │
│  └─────────────────────────┘       │
│              GPU                    │
└─────────────────────────────────────┘
```

### 4.2 Triton Model Repository Structure

```bash
model_repository/
├── llama2_13b/
│   ├── config.pbtxt          # Model Configuration
│   └── 1/                    # Version 1
│       └── model.plan        # TensorRT Engine
├── bert_base/
│   ├── config.pbtxt
│   └── 1/
│       └── model.onnx
└── gpt2/
    ├── config.pbtxt
    └── 1/
        ├── model.py          # Python Backend
        └── model_weights/
```

**config.pbtxt example (Llama2-13B):**
```protobuf
name: "llama2_13b"
backend: "tensorrtllm"
max_batch_size: 128

# Dynamic batch configuration
dynamic_batching {
  preferred_batch_size: [8, 16, 32]
  max_queue_delay_microseconds: 5000
}

# Instance group configuration
instance_group [
  {
    count: 2  # 2个模型实例
    kind: KIND_GPU
    gpus: [0, 1]  # 绑定GPU 0和1
  }
]

# Input output
input [
  {
    name: "input_ids"
    data_type: TYPE_INT32
    dims: [-1]  # 动态长度
  },
  {
    name: "attention_mask"
    data_type: TYPE_INT32
    dims: [-1]
  }
]

output [
  {
    name: "output_ids"
    data_type: TYPE_INT32
    dims: [-1]
  }
]

# Model parameters
parameters: {
  key: "max_tokens"
  value: { string_value: "512" }
}
parameters: {
  key: "temperature"
  value: { string_value: "0.7" }
}
```

### 4.3 Triton Kubernetes Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: triton-inference-server
  namespace: ai-platform
spec:
  replicas: 2
  selector:
    matchLabels:
      app: triton-server
  template:
    metadata:
      labels:
        app: triton-server
    spec:
      containers:
      - name: triton
        image: nvcr.io/nvidia/tritonserver:23.12-py3
        command:
        - tritonserver
        - --model-repository=s3://models/triton_repository
        - --model-control-mode=poll
        - --repository-poll-secs=60
        - --log-verbose=1
        - --metrics-port=8002
        
        ports:
        - containerPort: 8000
          name: http
        - containerPort: 8001
          name: grpc
        - containerPort: 8002
          name: metrics
        
        env:
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
        - name: LD_LIBRARY_PATH
          value: "/opt/tritonserver/backends/tensorrtllm:/usr/local/cuda/lib64"
        
        resources:
          requests:
            cpu: "8"
            memory: "32Gi"
            nvidia.com/gpu: 2
          limits:
            cpu: "16"
            memory: "64Gi"
            nvidia.com/gpu: 2
        
        livenessProbe:
          httpGet:
            path: /v2/health/live
            port: 8000
          initialDelaySeconds: 90
          periodSeconds: 30
        
        readinessProbe:
          httpGet:
            path: /v2/health/ready
            port: 8000
          initialDelaySeconds: 60
          periodSeconds: 10
---
# ServiceMonitor collects Triton metrics
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: triton-metrics
  namespace: ai-platform
spec:
  selector:
    matchLabels:
      app: triton-server
  endpoints:
  - port: metrics
    interval: 15s
    path: /metrics
```

### 4.4 Triton Client Calls

```python
import tritonclient.http as httpclient
import numpy as np

# Initialize client
client = httpclient.InferenceServerClient(
    url="triton-server.ai-platform.svc.cluster.local:8000"
)

# Check model status
if client.is_model_ready("llama2_13b"):
    print("Model is ready")

# Prepare input
input_ids = np.array(1, 2, 3, 4, 5, dtype=np.int32)
attention_mask = np.array(1, 1, 1, 1, 1, dtype=np.int32)

inputs = [
    httpclient.InferInput("input_ids", input_ids.shape, "INT32"),
    httpclient.InferInput("attention_mask", attention_mask.shape, "INT32")
]
inputs[0].set_data_from_numpy(input_ids)
inputs[1].set_data_from_numpy(attention_mask)

# Specify output
outputs = [httpclient.InferRequestedOutput("output_ids")]

# Inference request
response = client.infer(
    model_name="llama2_13b",
    inputs=inputs,
    outputs=outputs,
    request_id="123"
)

# Get results
output_ids = response.as_numpy("output_ids")
print(f"Generated IDs: {output_ids}")

# Query model statistics
stats = client.get_inference_statistics(model_name="llama2_13b")
print(stats)
```

---


## 5. TensorRT-LLM Acceleration

### 5.1 Converting Models to TensorRT Engines

```bash
# 1. Install TensorRT-LLM
pip install tensorrt-llm==0.7.1

# 2. Convert Llama2-7B model
git clone https://github.com/NVIDIA/TensorRT-LLM.git
cd TensorRT-LLM/examples/llama

# Download original weights
huggingface-cli download meta-llama/Llama-2-7b-hf --local-dir ./llama-2-7b-hf

# Convert to TensorRT-LLM format (FP16)
python convert_checkpoint.py \
  --model_dir ./llama-2-7b-hf \
  --output_dir ./llama-2-7b-trtllm \
  --dtype float16

# Build TensorRT engine (single GPU)
trtllm-build \
  --checkpoint_dir ./llama-2-7b-trtllm \
  --output_dir ./llama-2-7b-engine \
  --gemm_plugin float16 \
  --max_batch_size 128 \
  --max_input_len 2048 \
  --max_output_len 512 \
  --max_beam_width 1

# Build TensorRT engine (4-GPU tensor parallelism)
trtllm-build \
  --checkpoint_dir ./llama-2-7b-trtllm \
  --output_dir ./llama-2-7b-engine-tp4 \
  --gemm_plugin float16 \
  --max_batch_size 256 \
  --max_input_len 4096 \
  --max_output_len 1024 \
  --tp_size 4 \
  --workers 4

# Performance comparison (Llama2-7B, A100 80GB):
# PyTorch FP16:           45 tokens/s
# vLLM FP16:             180 tokens/s  (4x)
# TensorRT-LLM FP16:     280 tokens/s  (6.2x)
# TensorRT-LLM INT8:     420 tokens/s  (9.3x)
```

### 5.2 TensorRT-LLM Inference Scripts

```python
import tensorrt_llm
from tensorrt_llm.runtime import ModelRunner

# Load TensorRT engine
runner = ModelRunner.from_dir(
    engine_dir="./llama-2-7b-engine",
    rank=0  # 多GPU时指定rank
)

# Inference
input_text = "Once upon a time"
output = runner.generate(
    input_text,
    max_new_tokens=512,
    temperature=0.7,
    top_p=0.9,
    top_k=50,
    repetition_penalty=1.1
)

print(output)
```

---


## 6. KServe Model Service Orchestration

### 6.1 InferenceService definition

```yaml
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: llama2-13b-inference
  namespace: ai-platform
spec:
  predictor:
    minReplicas: 2
    maxReplicas: 10
    
    # Auto-scaling configuration
    scaleTarget: 80  # 目标并发请求数
    scaleMetric: concurrency
    
    containers:
    - name: kserve-container
      image: vllm/vllm-openai:v0.3.0
      command:
      - python
      - -m
      - vllm.entrypoints.openai.api_server
      args:
      - --model=/mnt/models/llama-2-13b
      - --tensor-parallel-size=4
      - --dtype=float16
      
      resources:
        requests:
          cpu: "16"
          memory: "64Gi"
          nvidia.com/gpu: 4
        limits:
          cpu: "32"
          memory: "128Gi"
          nvidia.com/gpu: 4
      
      ports:
      - containerPort: 8000
        protocol: TCP
      
      volumeMounts:
      - name: model-volume
        mountPath: /mnt/models
    
    volumes:
    - name: model-volume
      persistentVolumeClaim:
        claimName: llama2-13b-pvc
  
  # Transformer preprocessing (optional)
  transformer:
    containers:
    - name: transformer
      image: myregistry/text-preprocessor:latest
      env:
      - name: PREDICTOR_HOST
        value: "llama2-13b-inference-predictor-default"
---
# Traffic splitting (canary release)
apiVersion: serving.kserve.io/v1beta1
kind: InferenceService
metadata:
  name: llama2-13b-canary
  namespace: ai-platform
spec:
  predictor:
    canaryTrafficPercent: 10  # 10%流量到新版本
    minReplicas: 1
    containers:
    - name: kserve-container
      image: vllm/vllm-openai:v0.3.1  # 新版本
      # ... other configurations as above
```

### 6.2 KServe request routing

```python
import requests
import json

# InferenceService automatically generated URL
url = "http://llama2-13b-inference.ai-platform.example.com/v1/chat/completions"

headers = {
    "Content-Type": "application/json"
}

payload = {
    "model": "llama-2-13b",
    "messages": [
        {"role": "user", "content": "What is Kubernetes?"}
    ],
    "temperature": 0.7,
    "max_tokens": 256
}

response = requests.post(url, headers=headers, json=payload)
result = response.json()
print(result['choices'][0]['message']['content'])
```

---


## 7. Inference Performance Optimization Techniques

### 7.1 KV Cache optimization

```python
"""
KV Cache原理：
Transformer解码时，每个token生成需要访问之前所有token的K和V。
缓存这些K/V可以避免重复计算。

显存占用计算（Llama2-13B）：
- 单个token的KV: 2 * num_layers * hidden_size * 2 (K+V) * 2 bytes (FP16)
- Llama2-13B: 2 * 40 * 5120 * 2 * 2 = 1.6 MB/token
- 4096 context: 1.6 MB * 4096 = 6.5 GB
- 批次32: 6.5 GB * 32 = 208 GB (超出A100 80GB!)

PagedAttention解决方案：
- 分页存储KV，页大小16 tokens
- 非连续内存分配，类似OS虚拟内存
- 共享KV Cache（相同前缀的请求共享）
"""

# vLLM automatically manages KV Cache, no manual configuration required
# Memory allocation:
# - Model weights: ~26GB (FP16)
# - KV Cache: 80GB * 0.95 - 26GB = 50GB
# - Concurrent support: 50GB / (1.6MB * 4096) ≈ 8 long context requests
```

### 7.2 Flash Attention 2

```python
"""
Flash Attention优化：
- 传统Attention: O(N^2)内存，N是序列长度
- Flash Attention: 分块计算，减少HBM访问
- Flash Attention 2: 进一步优化，速度提升2倍

性能对比（Llama2-7B, A100）：
Context Length | Standard | Flash Attn | Flash Attn 2
     512       |  120ms   |   40ms     |    25ms
    2048       |  480ms   |  160ms     |   100ms
    4096       | 1920ms   |  640ms     |   400ms
"""

# TGI defaults to Flash Attention 2
# vLLM requires manual compilation for support:
# pip install vllm[flashinfer]
```

### 7.3 Speculative Decoding

```python
"""
投机解码（Speculative Decoding）：
1. 使用小模型快速生成多个候选token
2. 大模型并行验证候选token
3. 接受正确的token，拒绝错误的

加速比：
- GPT-2-XL (1.5B) + GPT-2 (117M): 2.3x
- Llama2-70B + Llama2-7B: 2.1x
- 适用于推理密集型任务
"""

# vLLM supports Speculative Decoding (experimental)
from vllm import LLM, SamplingParams

llm = LLM(
    model="meta-llama/Llama-2-70b-hf",
    speculative_model="meta-llama/Llama-2-7b-hf",  # draft model
    num_speculative_tokens=5,
    use_v2_block_manager=True
)

prompts = ["Explain quantum computing"]
sampling_params = SamplingParams(temperature=0.7, max_tokens=512)
outputs = llm.generate(prompts, sampling_params)
```

---


## 8. Cost Optimization Strategies

### 8.1 GPU sharing solution comparison

| Solution | Isolation | Memory Utilization | Applicable Scenario | Implementation Complexity |
|-----|-------|-----------|---------|-----------|
| **Time-Slicing** | Weak (time slices) | Low (60%) | Development/Test | Low |
| **MPS** | Moderate (process isolation) | Moderate (75%) | Small model inference | Moderate |
| **MIG** | Strong (hardware isolation) | High (90%) | Production multi-tenancy | High (only A100/H100) |
| **vGPU** | Strong (virtualization) | High (85%) | Cloud service provider | High (requires License) |

### 8.2 MIG configuration practice

``` bash
# 🟢 Low-risk: read-only/information gathering, typically no side effects
# A100 80GB MIG configuration
# Split into 3 * 3g.40gb instances

# Enable MIG mode
sudo nvidia-smi -mig 1

# Create GPU instance
sudo nvidia-smi mig -cgi 19,19,19 -C

# Verify
nvidia-smi mig -lgi
# +-------------------------------------------------------+
# | GPU instance profiles:                                |
# | GPU   GI ID  Profile                   Placement      |
# |        ID                                Start:Size   |
# |=======================================================|
# |   0    0      MIG 3g.40gb                   0:4       |
# |        1      MIG 3g.40gb                   4:4       |
# |        2      MIG 3g.40gb                   8:4       |
# +-------------------------------------------------------+

# Kubernetes device plugin identifies MIG
kubectl get node gpu-node-01 -o yaml | grep nvidia.com/mig
#  nvidia.com/mig-3g.40gb: 3
```
```yaml
# Pod uses MIG instance
apiVersion: v1
kind: Pod
metadata:
  name: llama2-7b-mig
spec:
  containers:
  - name: inference
    image: vllm/vllm-openai:v0.3.0
    resources:
      limits:
        nvidia.com/mig-3g.40gb: 1  # 请求一个MIG实例
```

### 8.3 Spot instances mixed deployment

```yaml
# Karpenter auto-scaling configuration
apiVersion: karpenter.sh/v1alpha5
kind: Provisioner
metadata:
  name: gpu-spot-provisioner
spec:
  requirements:
  - key: karpenter.sh/capacity-type
    operator: In
    values: ["spot", "on-demand"]
  - key: node.kubernetes.io/instance-type
    operator: In
    values: ["g5.12xlarge", "p4d.24xlarge"]
  - key: nvidia.com/gpu
    operator: Exists
  
  # Spot instance weight (give priority to)
  weight: 100
  
  # Spot interruption handling
  ttlSecondsAfterEmpty: 30
  ttlSecondsUntilExpired: 604800  # 7天
  
  limits:
    resources:
      nvidia.com/gpu: 100
---
# Critical services use On-Demand, non-critical use Spot
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-llama2-70b-prod
spec:
  template:
    spec:
      nodeSelector:
        karpenter.sh/capacity-type: on-demand  # 生产环境
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-llama2-7b-dev
spec:
  template:
    spec:
      affinity:
        nodeAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            preference:
              matchExpressions:
              - key: karpenter.sh/capacity-type
                operator: In
                values: ["spot"]  # 开发环境优先Spot
```

**Cost Savings:**
- Spot instances discount: 60-90% off On-Demand price
- MIG improves utilization: 3 7B models share an A100, cost reduction by 65%
- Inference optimization (vLLM): throughput 10 times higher = required GPUs reduced by 90%

---


## 9. Monitoring and Observability

### 9.1 Key inference metrics

```yaml
# Prometheus alert rules
groups:
- name: llm_inference
  interval: 15s
  rules:
  - alert: HighInferenceLatency
    expr: histogram_quantile(0.99, rate(tgi_request_duration_seconds_bucket[5m])) > 5
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "LLM inference P99 latency > 5s"
      description: "Model: {{ $labels.model }}, current P99: {{ $value }}s"
  
  - alert: HighQueueSize
    expr: vllm_num_requests_waiting > 50
    for: 3m
    labels:
      severity: warning
    annotations:
      summary: "vLLM request queue backlog > 50"
      description: "Consider scaling up instances"
  
  - alert: LowGPUUtilization
    expr: avg_over_time(DCGM_FI_DEV_GPU_UTIL[10m]) < 30
    for: 15m
    labels:
      severity: info
    annotations:
      summary: "GPU utilization < 30%, resource waste"
  
  - alert: OOMRisk
    expr: (vllm_gpu_cache_usage_perc > 95)
    for: 2m
    labels:
      severity: critical
    annotations:
      summary: "KV Cache usage rate > 95%, OOM risk"
```

### 9.2 Grafana Dashboard

```json
{
  "dashboard": {
    "title": "LLM Inference Performance",
    "panels": [
      {
        "title": "Requests Per Second",
        "targets": [
          {
            "expr": "rate(tgi_request_count[5m])",
            "legendFormat": "{{model}}"
          }
        ]
      },
      {
        "title": "Time to First Token (TTFT)",
        "targets": [
          {
            "expr": "histogram_quantile(0.95, rate(vllm_time_to_first_token_seconds_bucket[5m]))",
            "legendFormat": "P95"
          },
          {
            "expr": "histogram_quantile(0.99, rate(vllm_time_to_first_token_seconds_bucket[5m]))",
            "legendFormat": "P99"
          }
        ]
      },
      {
        "title": "Tokens Per Second (Throughput)",
        "targets": [
          {
            "expr": "rate(vllm_num_generation_tokens_total[1m])",
            "legendFormat": "{{pod}}"
          }
        ]
      },
      {
        "title": "KV Cache Usage",
        "targets": [
          {
            "expr": "vllm_gpu_cache_usage_perc",
            "legendFormat": "GPU {{gpu_id}}"
          }
        ]
      },
      {
        "title": "Cost Per 1M Tokens",
        "targets": [
          {
            "expr": "(sum(rate(container_cpu_usage_seconds_total{pod=~\"vllm.*\"}[1h])) * 0.05 + sum(nvidia_gpu_duty_cycle{pod=~\"vllm.*\"}) / 100 * 2.5) / (rate(vllm_num_generation_tokens_total[1h]) / 1000000)",
            "legendFormat": "Cost"
          }
        ]
      }
    ]
  }
}
```

---


## 10. Production Environment Checklist

### 10.1 Pre-deployment checks

- [ ] **Model Selection**: Choose appropriate model size based on task
  - Simple tasks: 7B model (Mistral-7B, Llama2-7B)
  - Complex inference: 13B-70B (Llama2-70B, Mixtral-8x7B)
- [ ] **Quantization Strategy**: Balance between accuracy and performance
  - Production environment: FP16 or INT8 (GPTQ)
  - Resource-constrained: INT4 (AWQ, NF4)
- [ ] **Inference Framework**:
  - General: vLLM (best throughput)
  - HF ecosystem: TGI (native integration)
  - Multi-model: Triton (enterprise-level)
  - Extreme performance: TensorRT-LLM (NVIDIA GPU)
- [ ] **GPU Configuration**:
  - Single model size > single card memory: tensor parallelism
  - Share GPU among multiple models: MIG or Time-Slicing
  - cost-sensitive: Spot instances + auto-scaling
- [ ] **high availability**:
  - at least 2 replicas
  - deployed across AZs
  - health checks and automatic restarts
- [ ] **observability**:
  - Prometheus metric collection
  - Grafana Dashboard
  - distributed tracing ([[Jaeger|Jaeger]])
  - log aggregation (ELK/Loki)

### 10.2 Performance benchmarks

| model | framework | GPU | batch size | throughput(tokens/s) | P99 latency(ms) | cost($/1M tokens) |
|-----|------|-----|---------|----------------|------------|------------------|
| Llama2-7B | vLLM | A100 40GB | 128 | 4800 | 850 | $0.12 |
| Llama2-7B | TensorRT-LLM | A100 40GB | 256 | 7200 | 620 | $0.08 |
| Llama2-13B | vLLM | A100 80GB | 64 | 2400 | 1200 | $0.28 |
| Llama2-70B | vLLM | 4×A100 80GB | 32 | 1200 | 2400 | $1.20 |
| Mistral-7B | TGI | A10G 24GB | 64 | 2200 | 980 | $0.18 |

---


## 11. Fault Diagnosis

### 11.1 Common issues

**Problem 1: OOM (Out of Memory)**
```
Error: CUDA out of memory
Reason: KV Cache or model weights exceed GPU memory

Solution:
1. Reduce --gpu-memory-utilization (from 0.95→0.90)
2. Decrease the number of concurrent --max-num-seqs
3. Reduce --max-model-len context length
4. Use quantization (INT8/INT4)
5. Increase the number of GPU for tensor parallelism
```

**Problem 2: low inference throughput**
```
Symptoms: GPU utilization < 50%

Examination steps:
1. Check batch size: is max_batch_size too small
2. Check queue depth: are there enough requests (<10 concurrent requests cannot leverage batching advantages)
3. Check CPU bottleneck: is tokenization a bottleneck
4. Check network bandwidth: how fast does the model load from S3
5. Enable CUDA Graph: vLLM remove --enforce-eager

Optimization:
- Increase max_num_seqs to 256+
- Use Triton Dynamic Batching
- Batch client requests instead of single requests
```

**Problem 3: high first token delay (TTFT)**
```
symptom: TTFT > 3 seconds

Reason:
1. Prefill stage has large computation (long context)
2. Batch processing causes waiting
3. Model loading to GPU is slow

Optimization:
- Use FlashAttention 2
- Separate Prefill and Decode services
- Warm up the model (send dummy requests at startup)
- Add a priority queue (higher priority for paid users)
```

### 11.2 Log analysis

``` bash
# 🟢 Low risk: read-only/information collection, usually no side effects
# vLLM debug logs
kubectl logs -f vllm-pod --namespace ai-platform | grep -E "ERROR|WARNING|OOM"

# Key log example:
# [WARNING] KV cache is full. The request will be blocked until some requests finish.
#   → Need to scale up or reduce concurrency

# [ERROR] CUDA out of memory. Tried to allocate 20.00 GiB
#   → OOM, adjust configuration

# [INFO] Avg prompt throughput: 1234.5 tokens/s, generation: 45.6 tokens/s
#   → Performance benchmark reference
```
---

**Related tables:**
- [111-AI Infrastructure Architecture](./01-ai-infrastructure.md)
- [112-Distributed Training Frameworks](./05-distributed-training-frameworks.md)
- [113-AI Model Registry](./09-model-registry.md)
- [114-GPU Monitoring and Observability](./04-gpu-monitoring.md)
- [115-AI Data Processing Pipeline](./06-ai-data-pipeline.md)

**Version Information:**
- vLLM: v0.3.0+
- Text Generation Inference: v1.4.0+
- Triton Inference Server: 23.12+
- TensorRT-LLM: v0.7.0+
- KServe: v0.11+
- Kubernetes: v1.27+

---


## Obsidian related documents

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Open Source Project Index
- AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations (AI/ML Workloads Operations)
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management

## See Also

- 16-llm-finetuning
- 17-llm-inference-serving
- 19-llm-quantization
- 20-vector-database-rag

## Related

- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Knowledge Graph Index]]


<!-- risk-assessed -->
