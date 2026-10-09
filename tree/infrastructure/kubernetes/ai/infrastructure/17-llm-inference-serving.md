---
title: 144 - LLM Inference Service Deployment
description: 'title: 144 - LLM Inference Service Deployment'
summary: 'title: 144 - LLM Inference Service Deployment'
category: general
tags:
- k8s
- ai
- gpu
- deep-dive
- scheduler
- prometheus
- grafana
- jaeger
- istio
- opa
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 1h
intent_queries:
- What is llm-inference-serving?
- How to use llm-inference-serving
- Best practices for llm-inference-serving
trigger_keywords:
- Deployment of LLM Inference Service
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- service-mesh-basics
- prometheus-basics
- monitoring-basics
- gpu-scheduling-basics
- tls-basics
- policy-basics
- tracing-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/17-llm-inference-serving.md
---

> **Production Environment Security Reminders**
>
> This document contains executable operational commands. Please confirm before execution: that the target cluster and Namespace are correct; that you have sufficient RBAC permissions; and that these commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




title: 144 - LLM Inference Service Deployment
description: '# 144 - LLM Inference Service Deployment'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- scheduler
- [[Prometheus|prometheus]]
- grafana
- [[Jaeger|jaeger]]
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- MLOps Engineer
- SRE
estimated_read_time: 5min
intent_queries:
- What is LLM Inference Service Deployment
- How to deploy LLM Inference Service Deployment
- [[Kubernetes|Kubernetes]] 11 ai infra best practices
trigger_keywords:
- LLM Inference Service Deployment
- ai
- infra
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
authors:
- name: Dillan Teagle
  role: contributor
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
---

# 144 - LLM inference service deployment

> **Applicable Versions**: Kubernetes v1.25 - v1.32 | **Difficulty**: Advanced | **Reference**: [vLLM](https://docs.vllm.ai/) | [TGI](https://huggingface.co/docs/text-generation-inference) | [TensorRT-LLM](https://nvidia.github.io/TensorRT-LLM/)


## 1. Overall Inference Service Architecture Overview

### 1.1 Production-Level LLM Inference Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           LLM Inference Service Architecture                         │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────────────────────────────────┐  │
│  │   Client    │    │   Gateway   │    │           Kubernetes Cluster            │  │
│  │  Requests   │───▶│  (Istio/    │───▶│                                         │  │
│  │             │    │  Kong/NGINX)│    │  ┌─────────────────────────────────────┐│  │
│  └─────────────┘    └─────────────┘    │  │       Load Balancer (Service)       ││  │
│                           │            │  └───────────────────┬─────────────────┘│  │
│                           │            │                      │                   │  │
│                           ▼            │  ┌───────────────────▼─────────────────┐│  │
│  ┌─────────────────────────────────┐   │  │          Inference Router           ││  │
│  │         Rate Limiter            │   │  │    (Request Routing & Batching)     ││  │
│  │  ┌───────────────────────────┐  │   │  └───────────────────┬─────────────────┘│  │
│  │  │ Per-User: 100 req/min     │  │   │                      │                   │  │
│  │  │ Per-API-Key: 1000 req/min │  │   │  ┌──────────┬────────┴─────┬──────────┐│  │
│  │  │ Global: 10000 req/min     │  │   │  │          │              │          ││  │
│  │  └───────────────────────────┘  │   │  ▼          ▼              ▼          ▼│  │
│  └─────────────────────────────────┘   │┌─────┐  ┌─────┐       ┌─────┐  ┌─────┐│  │
│                                        ││vLLM │  │vLLM │  ...  │vLLM │  │vLLM ││  │
│  ┌─────────────────────────────────┐   ││Pod 1│  │Pod 2│       │Pod N│  │Pod M││  │
│  │      Request Queue              │   │└──┬──┘  └──┬──┘       └──┬──┘  └──┬──┘│  │
│  │  ┌─────────────────────────────┐│   │   │        │             │        │   │  │
│  │  │ Priority: Critical > Normal ││   │   └────────┼─────────────┼────────┘   │  │
│  │  │ Queue Depth: 50-100 requests││   │            │             │            │  │
│  │  │ Timeout: 30-60 seconds      ││   │  ┌────────▼─────────────▼────────┐   │  │
│  │  └─────────────────────────────┘│   │  │         GPU Nodes              │   │  │
│  └─────────────────────────────────┘   │  │  A100/H100/L40S/A10G           │   │  │
│                                        │  └───────────────────────────────────┘   │  │
│  ┌─────────────────────────────────┐   │                                         │  │
│  │        Model Registry           │   │  ┌─────────────────────────────────────┐│  │
│  │  ┌───────────────────────────┐  │   │  │         Model Storage              ││  │
│  │  │ S3/GCS/Azure Blob         │  │   │  │   PVC (NVMe SSD) + S3 Cache        ││  │
│  │  │ HuggingFace Hub           │  │◀─▶│  │   JuiceFS / Alluxio / FSx          ││  │
│  │  │ MLflow Registry           │  │   │  └─────────────────────────────────────┘│  │
│  │  └───────────────────────────┘  │   │                                         │  │
│  └─────────────────────────────────┘   └─────────────────────────────────────────┘  │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Comprehensive Comparison of Inference Engines

| Inference Engine | Throughput | Latency | Memory Efficiency | Quantization Support | Distributed Inference | Stream Output | Suitable GPU | Production Ready |
|---------|--------|------|----------|----------|-----------|----------|---------|---------|
| **vLLM** | ★★★★★ | Medium | 95% | AWQ/GPTQ/FP8 | TP | ✓ | A100/H100/A10G | ✓ |
| **TGI** | ★★★★☆ | Low | 90% | GPTQ/AWQ/EETQ | TP | ✓ | All series | ✓ |
| **TensorRT-LLM** | ★★★★★ | Very Low | 98% | INT8/FP8/INT4 | TP+PP | ✓ | NVIDIA-specific | ✓ |
| **llama.cpp** | ★★☆☆☆ | Medium | 85% | GGUF Q2-Q8 | ✗ | ✓ | CPU/low-end GPU | ✓ |
| **DeepSpeed-MII** | ★★★★☆ | Low | 92% | ZeroQuant | TP | ✓ | A100/H100 | ✓ |
| **SGLang** | ★★★★★ | Very Low | 95% | AWQ/GPTQ | TP | ✓ | A100/H100 | ✓ |
| **LMDeploy** | ★★★★☆ | low | 93% | W4A16/W8A8 | TP | ✓ | All series | ✓ |

### 1.3 Comprehensive Comparison of Key Technology Features

| Technical Features | vLLM | TGI | TensorRT-LLM | SGLang |
|---------|------|-----|--------------|--------|
| **PagedAttention** | ✓ | ✓ | ✓ | ✓ |
| **Continuous Batching** | ✓ | ✓ | ✓ | ✓ |
| **Speculative Decoding** | ✓ | ✓ | ✓ | ✓ |
| **Flash Attention 2** | ✓ | ✓ | ✓ | ✓ |
| **Prefix Caching** | ✓ | ✗ | ✓ | ✓ |
| **RadixAttention** | ✗ | ✗ | ✗ | ✓ |
| **Multi-LoRA** | ✓ | ✓ | ✓ | ✓ |
| **Structured Output** | ✓ | ✓ | ✗ | ✓ |
| **Vision Models** | ✓ | ✓ | ✓ | ✓ |
| **OpenAI Compatible API** | ✓ | ✓ | ✓ | ✓ |

---


## 2. vLLM Production Deployment

### 2.1 Complete Deployment Configuration

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: llm-inference
  labels:
    istio-injection: enabled
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: vllm-config
  namespace: llm-inference
data:
  # vLLM Server Configuration
  VLLM_HOST: "0.0.0.0"
  VLLM_PORT: "8000"
  
  # Performance Optimization
  VLLM_GPU_MEMORY_UTILIZATION: "0.90"
  VLLM_MAX_MODEL_LEN: "8192"
  VLLM_MAX_NUM_SEQS: "256"
  VLLM_MAX_NUM_BATCHED_TOKENS: "32768"
  
  # Parallel Configuration
  VLLM_TENSOR_PARALLEL_SIZE: "1"
  VLLM_PIPELINE_PARALLEL_SIZE: "1"
  
  # Quantization Configuration
  VLLM_QUANTIZATION: "awq"
  VLLM_DTYPE: "float16"
  
  # Cache Configuration
  VLLM_ENABLE_PREFIX_CACHING: "true"
  VLLM_BLOCK_SIZE: "16"
  
  # Log Configuration
  VLLM_LOG_LEVEL: "info"
---
apiVersion: v1
kind: Secret
metadata:
  name: vllm-secrets
  namespace: llm-inference
type: Opaque
stringData:
  # HuggingFace Token (Private Model Access)
  HF_TOKEN: "hf_xxxxxxxxxxxxxxxxxxxx"
  # API Key (Optional)
  VLLM_API_KEY: "sk-xxxxxxxxxxxxxxxxxxxx"
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-llama3-70b
  namespace: llm-inference
  labels:
    app: vllm
    model: llama3-70b
    version: v1
spec:
  replicas: 4
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: vllm
      model: llama3-70b
  template:
    metadata:
      labels:
        app: vllm
        model: llama3-70b
        version: v1
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8000"
        prometheus.io/path: "/metrics"
    spec:
      # Scheduling Constraints
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: nvidia.com/gpu.product
                operator: In
                values:
                - NVIDIA-A100-SXM4-80GB
                - NVIDIA-H100-SXM5-80GB
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchLabels:
                  app: vllm
              topologyKey: kubernetes.io/hostname
      
      # Tolerate GPU Node Scrubbing
      tolerations:
      - key: nvidia.com/gpu
        operator: Exists
        effect: NoSchedule
      - key: dedicated
        operator: Equal
        value: gpu-inference
        effect: NoSchedule
      
      # Initialization Container - Model Warmup
      initContainers:
      - name: model-downloader
        image: python:3.11-slim
        command:
        - /bin/bash
        - -c
        - |
          pip install huggingface_hub
          python -c "
          from huggingface_hub import snapshot_download
          import os
          snapshot_download(
              repo_id='meta-llama/Meta-Llama-3-70B-Instruct-AWQ',
              local_dir='/models/llama3-70b-awq',
              token=os.environ.get('HF_TOKEN'),
              local_dir_use_symlinks=False
          )
          "
        env:
        - name: HF_TOKEN
          valueFrom:
            secretKeyRef:
              name: vllm-secrets
              key: HF_TOKEN
        volumeMounts:
        - name: model-cache
          mountPath: /models
        resources:
          requests:
            cpu: "2"
            memory: "8Gi"
          limits:
            cpu: "4"
            memory: "16Gi"
      
      containers:
      - name: vllm
        image: vllm/vllm-openai:v0.4.2
        imagePullPolicy: Always
        
        args:
        - --model=/models/llama3-70b-awq
        - --served-model-name=llama3-70b
        - --host=0.0.0.0
        - --port=8000
        # Performance Parameters
        - --tensor-parallel-size=4
        - --dtype=float16
        - --quantization=awq
        - --gpu-memory-utilization=0.90
        - --max-model-len=8192
        - --max-num-seqs=256
        - --max-num-batched-tokens=32768
        # Optimization Parameters
        - --enable-prefix-caching
        - --block-size=16
        - --swap-space=16
        - --disable-log-requests
        # API Parameters
        - --api-key=$(VLLM_API_KEY)
        - --chat-template=/etc/vllm/chat_template.jinja
        
        env:
        - name: VLLM_API_KEY
          valueFrom:
            secretKeyRef:
              name: vllm-secrets
              key: VLLM_API_KEY
        - name: CUDA_VISIBLE_DEVICES
          value: "0,1,2,3"
        - name: NCCL_DEBUG
          value: "WARN"
        - name: NCCL_IB_DISABLE
          value: "0"
        - name: NCCL_NET_GDR_LEVEL
          value: "5"
        
        ports:
        - containerPort: 8000
          name: http
          protocol: TCP
        
        # Resource Configuration - 4x A100 80GB
        resources:
          requests:
            cpu: "16"
            memory: "64Gi"
            nvidia.com/gpu: "4"
          limits:
            cpu: "32"
            memory: "128Gi"
            nvidia.com/gpu: "4"
        
        # Health Checks
        startupProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 60
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 30  # 允许5分钟启动时间
        
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 10
          periodSeconds: 30
          timeoutSeconds: 10
          failureThreshold: 3
        
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 10
          timeoutSeconds: 5
          failureThreshold: 3
        
        volumeMounts:
        - name: model-cache
          mountPath: /models
          readOnly: true
        - name: chat-template
          mountPath: /etc/vllm
        - name: shm
          mountPath: /dev/shm
      
      volumes:
      - name: model-cache
        persistentVolumeClaim:
          claimName: model-storage-pvc
      - name: chat-template
        configMap:
          name: vllm-chat-template
      - name: shm
        emptyDir:
          medium: Memory
          sizeLimit: 32Gi
      
      terminationGracePeriodSeconds: 120
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: vllm-chat-template
  namespace: llm-inference
data:
  chat_template.jinja: |
    {% for message in messages %}
    {% if message['role'] == 'system' %}
    <|begin_of_text|><|start_header_id|>system<|end_header_id|>
    {{ message['content'] }}<|eot_id|>
    {% elif message['role'] == 'user' %}
    <|start_header_id|>user<|end_header_id|>
    {{ message['content'] }}<|eot_id|>
    {% elif message['role'] == 'assistant' %}
    <|start_header_id|>assistant<|end_header_id|>
    {{ message['content'] }}<|eot_id|>
    {% endif %}
    {% endfor %}
    <|start_header_id|>assistant<|end_header_id|>
```

### 2.2 Service and Ingress Configuration

```yaml
apiVersion: v1
kind: Service
metadata:
  name: vllm-service
  namespace: llm-inference
  labels:
    app: vllm
  annotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "8000"
spec:
  type: ClusterIP
  sessionAffinity: None
  ports:
  - name: http
    port: 8000
    targetPort: 8000
    protocol: TCP
  selector:
    app: vllm
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: vllm-ingress
  namespace: llm-inference
  annotations:
    kubernetes.io/ingress.class: nginx
    nginx.ingress.kubernetes.io/proxy-body-size: "100m"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "600"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "600"
    nginx.ingress.kubernetes.io/proxy-connect-timeout: "60"
    # WebSocket Support (Streaming Output)
    nginx.ingress.kubernetes.io/proxy-http-version: "1.1"
    nginx.ingress.kubernetes.io/upstream-hash-by: "$request_uri"
    # SSL Configuration
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
  - hosts:
    - llm-api.example.com
    secretName: llm-api-tls
  rules:
  - host: llm-api.example.com
    http:
      paths:
      - path: /v1
        pathType: Prefix
        backend:
          service:
            name: vllm-service
            port:
              number: 8000
---
# Istio VirtualService (Optional)
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: vllm-vs
  namespace: llm-inference
spec:
  hosts:
  - llm-api.example.com
  gateways:
  - istio-system/main-gateway
  http:
  - matchers:
    - - uri=""
    - prefix="/v1"
    - route=""
    - - destination=""
    - host="vllm-service"
    - port=""
    - number="8000"
    - timeout="600s"
    - retries=""
    - attempts="3"
    - perTryTimeout="200s"
    - retryOn="5xx,reset,connect-failure"
```

### 2.3 Auto Scaling Configuration

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: vllm-hpa
  namespace: llm-inference
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: vllm-llama3-70b
  minReplicas: 2
  maxReplicas: 16
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60
      policies:
      - type: Pods
        value: 2
        periodSeconds: 60
      - type: Percent
        value: 50
        periodSeconds: 60
      selectPolicy: Max
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
      - type: Pods
        value: 1
        periodSeconds: 120
      selectPolicy: Min
  metrics:
  # GPU Utilization
  - type: External
    external:
      metric:
        name: DCGM_FI_DEV_GPU_UTIL
        selector:
          matchLabels:
            app: vllm
      target:
        type: AverageValue
        averageValue: "70"
  # Request queue depth
  - type: Pods
    pods:
      metric:
        name: vllm_num_requests_waiting
      target:
        type: AverageValue
        averageValue: "10"
  # Number of requests being processed
  - type: Pods
    pods:
      metric:
        name: vllm_num_requests_running
      target:
        type: AverageValue
        averageValue: "50"
---
# KEDA ScaledObject (more precise control)
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: vllm-scaledobject
  namespace: llm-inference
spec:
  scaleTargetRef:
    name: vllm-llama3-70b
  minReplicaCount: 2
  maxReplicaCount: 16
  pollingInterval: 15
  cooldownPeriod: 300
  triggers:
  # Prometheus metric
  - type: prometheus
    metadata:
      serverAddress: http://prometheus.monitoring:9090
      metricName: vllm_queue_depth
      threshold: "20"
      query: |
        sum(vllm_num_requests_waiting{namespace="llm-inference"}) / 
        count(vllm_num_requests_waiting{namespace="llm-inference"})
  # GPU Memory Utilization
  - type: prometheus
    metadata:
      serverAddress: http://prometheus.monitoring:9090
      metricName: gpu_memory_util
      threshold: "85"
      query: |
        avg(DCGM_FI_DEV_MEM_COPY_UTIL{namespace="llm-inference"})
  # Inference latency
  - type: prometheus
    metadata:
      serverAddress: http://prometheus.monitoring:9090
      metricName: inference_latency_p99
      threshold: "5"
      query: |
        histogram_quantile(0.99, sum(rate(vllm_request_duration_seconds_bucket{namespace="llm-inference"}[5m])) by (le))
```

---


## 3. TensorRT-LLM High-Performance Deployment

### 3.1 TensorRT-LLM Engine Build

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: trtllm-engine-builder
  namespace: llm-inference
spec:
  ttlSecondsAfterFinished: 86400
  template:
    spec:
      restartPolicy: OnFailure
      containers:
      - name: builder
        image: nvcr.io/nvidia/tritonserver:24.01-trtllm-python-py3
        command:
        - /bin/bash
        - -c
        - |
          set -ex
          
          # Download model
          huggingface-cli download meta-llama/Meta-Llama-3-70B-Instruct \
            --local-dir /models/llama3-70b-hf
          
          # Convert to TensorRT-LLM format
          python /opt/tensorrt_llm/examples/llama/convert_checkpoint.py \
            --model_dir /models/llama3-70b-hf \
            --output_dir /models/llama3-70b-ckpt \
            --dtype float16 \
            --tp_size 4 \
            --pp_size 1
          
          # Build TensorRT engine
          trtllm-build \
            --checkpoint_dir /models/llama3-70b-ckpt \
            --output_dir /engines/llama3-70b \
            --gemm_plugin float16 \
            --gpt_attention_plugin float16 \
            --max_batch_size 64 \
            --max_input_len 4096 \
            --max_output_len 4096 \
            --max_num_tokens 32768 \
            --use_paged_context_fmha enable \
            --multiple_profiles enable \
            --workers 4
          
          echo "Engine build completed!"
        
        env:
        - name: HF_TOKEN
          valueFrom:
            secretKeyRef:
              name: vllm-secrets
              key: HF_TOKEN
        
        resources:
          requests:
            cpu: "32"
            memory: "256Gi"
            nvidia.com/gpu: "4"
          limits:
            cpu: "64"
            memory: "512Gi"
            nvidia.com/gpu: "4"
        
        volumeMounts:
        - name: model-storage
          mountPath: /models
        - name: engine-storage
          mountPath: /engines
      
      volumes:
      - name: model-storage
        persistentVolumeClaim:
          claimName: model-storage-pvc
      - name: engine-storage
        persistentVolumeClaim:
          claimName: engine-storage-pvc
      
      nodeSelector:
        nvidia.com/gpu.product: NVIDIA-A100-SXM4-80GB
```

### 3.2 Triton Inference Server Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: triton-llama3-70b
  namespace: llm-inference
spec:
  replicas: 4
  selector:
    matchLabels:
      app: triton
      model: llama3-70b
  template:
    metadata:
      labels:
        app: triton
        model: llama3-70b
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8002"
    spec:
      containers:
      - name: triton
        image: nvcr.io/nvidia/tritonserver:24.01-trtllm-python-py3
        command:
        - tritonserver
        args:
        - --model-repository=/models
        - --http-port=8000
        - --grpc-port=8001
        - --metrics-port=8002
        - --log-verbose=1
        - --strict-model-config=false
        - --backend-config=tensorrtllm,decoupled_mode=true
        - --backend-config=tensorrtllm,batching_type=inflight_fused
        - --backend-config=tensorrtllm,max_queue_delay_microseconds=100000
        
        ports:
        - containerPort: 8000
          name: http
        - containerPort: 8001
          name: grpc
        - containerPort: 8002
          name: metrics
        
        resources:
          requests:
            cpu: "16"
            memory: "64Gi"
            nvidia.com/gpu: "4"
          limits:
            cpu: "32"
            memory: "128Gi"
            nvidia.com/gpu: "4"
        
        volumeMounts:
        - name: model-repository
          mountPath: /models
        - name: shm
          mountPath: /dev/shm
        
        livenessProbe:
          httpGet:
            path: /v2/health/live
            port: 8000
          initialDelaySeconds: 60
          periodSeconds: 30
        
        readinessProbe:
          httpGet:
            path: /v2/health/ready
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
      
      volumes:
      - name: model-repository
        persistentVolumeClaim:
          claimName: triton-model-repo-pvc
      - name: shm
        emptyDir:
          medium: Memory
          sizeLimit: 64Gi
      
      nodeSelector:
        nvidia.com/gpu.product: NVIDIA-H100-SXM5-80GB
```

### 3.3 Triton Model Configuration

```protobuf
# config.pbtxt - Triton Model Configuration
name: "llama3-70b"
backend: "tensorrtllm"
max_batch_size: 64

model_transaction_policy {
  decoupled: true
}

dynamic_batching {
  preferred_batch_size: [8, 16, 32, 64]
  max_queue_delay_microseconds: 100000
}

input [
  {
    name: "input_ids"
    data_type: TYPE_INT32
    dims: [-1]
  },
  {
    name: "input_lengths"
    data_type: TYPE_INT32
    dims: [1]
    reshape { shape: [] }
  },
  {
    name: "request_output_len"
    data_type: TYPE_INT32
    dims: [1]
    reshape { shape: [] }
  },
  {
    name: "streaming"
    data_type: TYPE_BOOL
    dims: [1]
    reshape { shape: [] }
    optional: true
  },
  {
    name: "temperature"
    data_type: TYPE_FP32
    dims: [1]
    reshape { shape: [] }
    optional: true
  },
  {
    name: "top_p"
    data_type: TYPE_FP32
    dims: [1]
    reshape { shape: [] }
    optional: true
  },
  {
    name: "top_k"
    data_type: TYPE_INT32
    dims: [1]
    reshape { shape: [] }
    optional: true
  }
]

output [
  {
    name: "output_ids"
    data_type: TYPE_INT32
    dims: [-1, -1]
  },
  {
    name: "sequence_length"
    data_type: TYPE_INT32
    dims: [-1]
  }
]

instance_group [
  {
    count: 1
    kind: KIND_GPU
    gpus: [0, 1, 2, 3]
  }
]

parameters: {
  key: "gpt_model_type"
  value: {
    string_value: "inflight_fused_batching"
  }
}

parameters: {
  key: "gpt_model_path"
  value: {
    string_value: "/models/llama3-70b/engines"
  }
}

parameters: {
  key: "max_tokens_in_paged_kv_cache"
  value: {
    string_value: "2621440"
  }
}

parameters: {
  key: "batch_scheduler_policy"
  value: {
    string_value: "max_utilization"
  }
}

parameters: {
  key: "kv_cache_free_gpu_mem_fraction"
  value: {
    string_value: "0.90"
  }
}
```

---


## 4. Text Generation Inference (TGI) Deployment

### 4.1 Complete Deployment Configuration for TGI

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tgi-llama3-70b
  namespace: llm-inference
spec:
  replicas: 4
  selector:
    matchLabels:
      app: tgi
      model: llama3-70b
  template:
    metadata:
      labels:
        app: tgi
        model: llama3-70b
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "80"
    spec:
      containers:
      - name: tgi
        image: ghcr.io/huggingface/text-generation-inference:2.0.3
        
        args:
        # Model configuration
        - --model-id=meta-llama/Meta-Llama-3-70B-Instruct
        - --quantize=awq
        - --dtype=float16
        
        # Parallel configuration
        - --num-shard=4
        - --sharded=true
        
        # Performance configuration
        - --max-batch-size=64
        - --max-batch-prefill-tokens=4096
        - --max-total-tokens=8192
        - --max-input-length=4096
        - --max-concurrent-requests=256
        
        # Optimize configuration
        - --enable-cuda-graphs
        - --cuda-memory-fraction=0.90
        - --waiting-served-ratio=0.3
        
        # Service configuration
        - --hostname=0.0.0.0
        - --port=80
        - --json-output
        
        env:
        - name: HUGGING_FACE_HUB_TOKEN
          valueFrom:
            secretKeyRef:
              name: vllm-secrets
              key: HF_TOKEN
        - name: CUDA_VISIBLE_DEVICES
          value: "0,1,2,3"
        - name: NCCL_DEBUG
          value: "WARN"
        
        ports:
        - containerPort: 80
          name: http
        
        resources:
          requests:
            cpu: "16"
            memory: "64Gi"
            nvidia.com/gpu: "4"
          limits:
            cpu: "32"
            memory: "128Gi"
            nvidia.com/gpu: "4"
        
        volumeMounts:
        - name: model-cache
          mountPath: /data
        - name: shm
          mountPath: /dev/shm
        
        livenessProbe:
          httpGet:
            path: /health
            port: 80
          initialDelaySeconds: 120
          periodSeconds: 30
          timeoutSeconds: 10
        
        readinessProbe:
          httpGet:
            path: /health
            port: 80
          initialDelaySeconds: 60
          periodSeconds: 10
      
      volumes:
      - name: model-cache
        persistentVolumeClaim:
          claimName: model-storage-pvc
      - name: shm
        emptyDir:
          medium: Memory
          sizeLimit: 32Gi
      
      nodeSelector:
        nvidia.com/gpu.product: NVIDIA-A100-SXM4-80GB
---
apiVersion: v1
kind: Service
metadata:
  name: tgi-service
  namespace: llm-inference
spec:
  ports:
  - port: 80
    targetPort: 80
    name: http
  selector:
    app: tgi
```

---


## 5. Multi-LoRA Dynamic Loading

### 5.1 Management of LoRA Adapters

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: lora-adapter-config
  namespace: llm-inference
data:
  adapters.yaml: |
    adapters:
      # Code generation LoRA
      code-assistant:
        path: /adapters/code-assistant
        base_model: llama3-70b
        enabled: true
        
      # Customer conversation LoRA
      customer-service:
        path: /adapters/customer-service
        base_model: llama3-70b
        enabled: true
        
      # Medical QA LoRA
      medical-qa:
        path: /adapters/medical-qa
        base_model: llama3-70b
        enabled: true
        
      # Legal consultation LoRA
      legal-advisor:
        path: /adapters/legal-advisor
        base_model: llama3-70b
        enabled: true
    
    # Default adapter
    default_adapter: null
    
    # Maximum number of concurrently loaded adapters
    max_loaded_adapters: 8
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-multi-lora
  namespace: llm-inference
spec:
  replicas: 4
  selector:
    matchLabels:
      app: vllm-multi-lora
  template:
    metadata:
      labels:
        app: vllm-multi-lora
    spec:
      containers:
      - name: vllm
        image: vllm/vllm-openai:v0.4.2
        args:
        - --model=/models/llama3-70b
        - --enable-lora
        - --max-loras=8
        - --max-lora-rank=64
        - --lora-modules
        - code-assistant=/adapters/code-assistant
        - customer-service=/adapters/customer-service
        - medical-qa=/adapters/medical-qa
        - legal-advisor=/adapters/legal-advisor
        - --tensor-parallel-size=4
        - --gpu-memory-utilization=0.85
        
        resources:
          limits:
            nvidia.com/gpu: "4"
        
        volumeMounts:
        - name: base-model
          mountPath: /models
        - name: lora-adapters
          mountPath: /adapters
      
      volumes:
      - name: base-model
        persistentVolumeClaim:
          claimName: base-model-pvc
      - name: lora-adapters
        persistentVolumeClaim:
          claimName: lora-adapters-pvc
```

### 5.2 Dynamic Switching API for LoRA

```python
# lora_manager.py - LoRA adapter management service
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, Dict, List
import httpx
import asyncio

app = FastAPI(title="LoRA Adapter Manager")

class LoRARequest(BaseModel):
    """LoRA requests model"""
    model: str = "llama3-70b"
    adapter: Optional[str] = None  # LoRA适配器名称
    messages: List[Dict[str, str]]
    max_tokens: int = 1024
    temperature: float = 0.7
    stream: bool = False

class AdapterInfo(BaseModel):
    """Adapter information"""
    name: str
    path: str
    loaded: bool
    requests_count: int

# Adapter statistics
adapter_stats: Dict[str, int] = {}

@app.post("/v1/chat/completions")
async def chat_completions(request: LoRARequest):
    """Chat completion with LoRA adapters"""
    
    # Build vLLM request
    vllm_request = {
        "model": request.model,
        "messages": request.messages,
        "max_tokens": request.max_tokens,
        "temperature": request.temperature,
        "stream": request.stream,
    }
    
    # If an adapter is specified, add it to the model name
    if request.adapter:
        vllm_request["model"] = f"{request.model}:{request.adapter}"
        adapter_stats[request.adapter] = adapter_stats.get(request.adapter, 0) + 1
    
    # Forward to vLLM
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://vllm-service:8000/v1/chat/completions",
            json=vllm_request,
            timeout=120.0
        )
    
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )
    
    return response.json()

@app.get("/v1/adapters")
async def list_adapters() -> List[AdapterInfo]:
    """List all available LoRA adapters"""
    
    # Query vLLM for models that have been loaded
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "http://vllm-service:8000/v1/models"
        )
    
    models_data = response.json()
    adapters = []
    
    for model in models_data.get("data", []):
        model_id = model["id"]
        if ":" in model_id:
            base, adapter = model_id.split(":", 1)
            adapters.append(AdapterInfo(
                name=adapter,
                path=f"/adapters/{adapter}",
                loaded=True,
                requests_count=adapter_stats.get(adapter, 0)
            ))
    
    return adapters

@app.post("/v1/adapters/{adapter_name}/load")
async def load_adapter(adapter_name: str):
    """Dynamic loading of LoRA adapters"""
    # Implement dynamic loading logic
    return {"status": "loaded", "adapter": adapter_name}

@app.delete("/v1/adapters/{adapter_name}")
async def unload_adapter(adapter_name: str):
    """Unloading LoRA adapters"""
    # Implement dynamic unloading logic
    return {"status": "unloaded", "adapter": adapter_name}

@app.get("/v1/adapters/stats")
async def adapter_stats_endpoint():
    """Get adapter usage statistics"""
    return {
        "total_requests": sum(adapter_stats.values()),
        "per_adapter": adapter_stats
    }
```

---


## 6. Speculative Decoding Acceleration

### 6.1 Speculative Decoding Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    Speculative Decoding Architecture                     │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────┐                      ┌─────────────────────────┐   │
│  │   Draft Model   │                      │     Target Model        │   │
│  │  (Small, Fast)  │                      │   (Large, Accurate)     │   │
│  │                 │                      │                         │   │
│  │  Llama-3-8B     │                      │    Llama-3-70B          │   │
│  │  ~1ms/token     │                      │    ~50ms/token          │   │
│  └────────┬────────┘                      └────────────┬────────────┘   │
│           │                                            │                 │
│           │ Generate k tokens                          │ Verify          │
│           │ speculatively                              │ in parallel     │
│           ▼                                            ▼                 │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │                     Verification Process                         │    │
│  │                                                                   │    │
│  │  Draft tokens:    [t1, t2, t3, t4, t5]                           │    │
│  │                    ↓   ↓   ↓   ↓   ↓                             │    │
│  │  Target verify:   [✓   ✓   ✓   ✗   -]                            │    │
│  │                                                                   │    │
│  │  Accept 3 tokens, reject from t4                                 │    │
│  │  Sample new token from target model                               │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│  Performance Gain:                                                       │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │  Standard decoding:  50ms × 100 tokens = 5000ms                  │    │
│  │  Speculative (k=5):  (50ms + 5ms) × 25 iterations = 1375ms       │    │
│  │  Speedup: ~3.6x                                                   │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

### 6.2 vLLM Speculative Decoding Configuration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-speculative
  namespace: llm-inference
spec:
  replicas: 4
  selector:
    matchLabels:
      app: vllm-speculative
  template:
    metadata:
      labels:
        app: vllm-speculative
    spec:
      containers:
      - name: vllm
        image: vllm/vllm-openai:v0.4.2
        args:
        # Target model
        - --model=/models/llama3-70b
        - --served-model-name=llama3-70b
        
        # Opportunistic decoding configuration
        - --speculative-model=/models/llama3-8b
        - --num-speculative-tokens=5
        - --speculative-draft-tensor-parallel-size=1
        - --use-v2-block-manager
        
        # Performance configuration
        - --tensor-parallel-size=4
        - --gpu-memory-utilization=0.90
        - --max-model-len=8192
        - --enable-prefix-caching
        
        resources:
          limits:
            nvidia.com/gpu: "4"
        
        volumeMounts:
        - name: models
          mountPath: /models
      
      volumes:
      - name: models
        persistentVolumeClaim:
          claimName: model-storage-pvc
```

### 6.3 Performance Baseline Comparison

| Configuration | Model | Throughput (tok/s) | P50 Delay | P99 Delay | Acceleration Ratio |
|-----|------|---------------|---------|---------|--------|
| Standard Decoding | Llama3-70B | 45 | 22ms/tok | 35ms/tok | 1.0x |
| Speculative (k=3) | 70B + 8B | 95 | 11ms/tok | 18ms/tok | 2.1x |
| Speculative (k=5) | 70B + 8B | 120 | 8ms/tok | 15ms/tok | 2.7x |
| Speculative (k=7) | 70B + 8B | 135 | 7ms/tok | 14ms/tok | 3.0x |
| Speculative + AWQ | 70B + 8B | 180 | 5ms/tok | 10ms/tok | 4.0x |

---


## 7. KV Cache Optimization

### 7.1 PagedAttention Configuration

```python
# kv_cache_config.py - KV Cache configuration
from dataclasses import dataclass
from typing import Optional

@dataclass
class KVCacheConfig:
    """KV Cache configuration parameters"""
    
    # Block configuration
    block_size: int = 16  # 每个block的token数
    num_gpu_blocks: Optional[int] = None  # GPU blocks数量,自动计算
    num_cpu_blocks: int = 512  # CPU swap blocks数量
    
    # Memory configuration
    gpu_memory_utilization: float = 0.90  # GPU显存利用率
    swap_space_gb: float = 16  # CPU交换空间 (GB)
    
    # Cache strategy
    enable_prefix_caching: bool = True  # 启用前缀缓存
    sliding_window: Optional[int] = None  # 滑动窗口大小
    
    # Advanced configuration
    cache_dtype: str = "auto"  # 缓存数据类型
    max_num_seqs: int = 256  # 最大并发序列数
    max_num_batched_tokens: int = 32768  # 最大批处理tokens

# vLLM startup parameters
VLLM_KV_CACHE_ARGS = [
    "--block-size=16",
    "--gpu-memory-utilization=0.90",
    "--swap-space=16",
    "--enable-prefix-caching",
    "--max-num-seqs=256",
    "--max-num-batched-tokens=32768",
]
```

### 7.2 Prefix Caching Strategy

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: prefix-cache-config
  namespace: llm-inference
data:
  # System prompt cache
  system_prompts.yaml: |
    prompts:
      # General assistant
      general_assistant:
        hash: "sha256:abc123..."
        text: |
          You are a helpful AI assistant. You provide accurate, 
          helpful, and harmless responses to user queries.
        cache_priority: high
        
      # Code assistant
      code_assistant:
        hash: "sha256:def456..."
        text: |
          You are an expert programmer. You write clean, efficient, 
          and well-documented code. You follow best practices.
        cache_priority: high
        
      # Customer service assistant
      customer_service:
        hash: "sha256:ghi789..."
        text: |
          You are a professional customer service representative.
          You are polite, helpful, and solution-oriented.
        cache_priority: medium
    
    # Cache configuration
    cache_config:
      max_cached_prompts: 100
      eviction_policy: lru
      preload_on_startup: true
```

### 7.3 KV Cache Monitoring

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: kv-cache-alerts
  namespace: llm-inference
spec:
  groups:
  - name: kv-cache
    rules:
    # KV Cache utilization
    - record: vllm:kv_cache_utilization
      expr: |
        vllm_gpu_cache_usage_perc
    
    # Cache hit rate
    - record: vllm:prefix_cache_hit_rate
      expr: |
        rate(vllm_prefix_cache_hit_total[5m]) / 
        (rate(vllm_prefix_cache_hit_total[5m]) + rate(vllm_prefix_cache_miss_total[5m]))
    
    # Warning: KV Cache nearly full
    - alert: KVCacheHighUtilization
      expr: vllm_gpu_cache_usage_perc > 95
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "KV Cache utilization is too high"
        description: "Pod {{ $labels.pod }} KV Cache utilization {{ $value }}%"
    
    # Warning: Prefix cache hit rate low
    - alert: LowPrefixCacheHitRate
      expr: vllm:prefix_cache_hit_rate < 0.3
      for: 15m
      labels:
        severity: info
      annotations:
        summary: "Prefix cache hit rate is low"
        description: "Hit rate {{ $value | humanizePercentage }}"
    
    # Warning: Frequent Swap
    - alert: FrequentKVCacheSwap
      expr: rate(vllm_cache_swap_out_total[5m]) > 100
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "KV Cache frequently swaps to CPU"
```

---


## 8. Load Balancing and Traffic Management

### 8.1 Intelligent Routing Configuration

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: llm-routing
  namespace: llm-inference
spec:
  hosts:
  - llm-api.example.com
  gateways:
  - llm-gateway
  http:
  # Long context requests routed to dedicated instances
  - matchers:
    - - headers=""
    - x-max-tokens=""
    - regex="^([89][0-9]{3}|[1-9][0-9]{4,})$"  # >8000 tokens"
    - route=""
    - - destination=""
    - host="vllm-long-context"
    - port=""
    - number="8000"
    - timeout="600s"
  # Enable WebSocket for streaming requests
  - matchers:
    - - headers=""
    - x-stream=""
    - exact="true"
    - route=""
    - - destination=""
    - host="vllm-service"
    - port=""
    - number="8000"
    - timeout="300s"
  # Specific model routing
  - matchers:
    - - headers=""
    - x-model=""
    - exact="llama3-70b-code"
    - route=""
    - - destination=""
    - host="vllm-code-model"
    - port=""
    - number="8000"
  # Default route - weighted load balancing
  - route:
    - destination:
        host: vllm-service
        port:
          number: 8000
      weight: 70
    - destination:
        host: tgi-service
        port:
          number: 80
      weight: 30
    timeout: 120s
    retries:
      attempts: 3
      perTryTimeout: 45s
      retryOn: "5xx,reset,connect-failure,retriable-4xx"
---
apiVersion: networking.istio.io/v1beta1
kind: DestinationRule
metadata:
  name: vllm-destination
  namespace: llm-inference
spec:
  host: vllm-service
  trafficPolicy:
    connectionPool:
      tcp:
        maxConnections: 1000
        connectTimeout: 30s
      http:
        http1MaxPendingRequests: 500
        http2MaxRequests: 1000
        maxRequestsPerConnection: 100
        maxRetries: 3
    loadBalancer:
      simple: LEAST_REQUEST
    outlierDetection:
      consecutive5xxErrors: 5
      interval: 30s
      baseEjectionTime: 60s
      maxEjectionPercent: 30
```

### 8.2 Request Priority Queue

```python
# priority_queue.py - request priority queue
from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict
import asyncio
import heapq
from datetime import datetime
from enum import IntEnum

class Priority(IntEnum):
    // request priority
    CRITICAL = 0    # 最高优先级
    HIGH = 1
    NORMAL = 2
    LOW = 3
    BATCH = 4       # 最低优先级

class InferenceRequest(BaseModel):
    // inference request
    request_id: str
    model: str
    messages: List[Dict]
    max_tokens: int = 1024
    priority: Priority = Priority.NORMAL
    user_tier: str = "free"  # free, pro, enterprise
    created_at: float = None

class PriorityQueue:
    // priority request queue
    
    def __init__(self, max_size: int = 1000):
        self.max_size = max_size
        self.queue: List[tuple] = []  # (priority, timestamp, request)
        self.lock = asyncio.Lock()
        
        # quota for each priority
        self.quotas = {
            Priority.CRITICAL: 100,
            Priority.HIGH: 200,
            Priority.NORMAL: 500,
            Priority.LOW: 150,
            Priority.BATCH: 50
        }
        self.current_counts = {p: 0 for p in Priority}
    
    async def enqueue(self, request: InferenceRequest) -> bool:
        // request enqueued
        async with self.lock:
            # Check if the queue is full
            if len(self.queue) >= self.max_size:
                # Try to evict low-priority requests
                if not await self._evict_lower_priority(request.priority):
                    raise HTTPException(
                        status_code=429,
                        detail="Queue full, please retry later"
                    )
            
            # Check priority quota
            if self.current_counts[request.priority] >= self.quotas[request.priority]:
                raise HTTPException(
                    status_code=429,
                    detail=f"Priority {request.priority.name} quota exceeded"
                )
            
            # enqueue
            timestamp = request.created_at or datetime.now().timestamp()
            heapq.heappush(self.queue, (request.priority, timestamp, request))
            self.current_counts[request.priority] += 1
            
            return True
    
    async def dequeue(self) -> Optional[InferenceRequest]:
        // dequeue request
        async with self.lock:
            if not self.queue:
                return None
            
            priority, _, request = heapq.heappop(self.queue)
            self.current_counts[priority] -= 1
            
            return request
    
    async def _evict_lower_priority(self, min_priority: Priority) -> bool:
        // evict low-priority requests
        # Find and remove the request with the lowest priority
        for i in range(len(self.queue) - 1, -1, -1):
            if self.queue[i][0] > min_priority:
                evicted = self.queue.pop(i)
                self.current_counts[evicted[0]] -= 1
                heapq.heapify(self.queue)
                return True
        return False
    
    def get_stats(self) -> Dict:
        // get queue statistics
        return {
            "total_queued": len(self.queue),
            "by_priority": dict(self.current_counts),
            "utilization": len(self.queue) / self.max_size
        }

# Determine priority based on user level
USER_TIER_PRIORITY = {
    "enterprise": Priority.HIGH,
    "pro": Priority.NORMAL,
    "free": Priority.LOW
}

app = FastAPI()
queue = PriorityQueue(max_size=1000)

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    // chat completion with priority
    body = await request.json()
    
    # Get user level
    user_tier = request.headers.get("x-user-tier", "free")
    api_key = request.headers.get("authorization", "")
    
    # Create inference request
    inference_request = InferenceRequest(
        request_id=str(uuid.uuid4()),
        model=body.get("model", "llama3-70b"),
        messages=body.get("messages", []),
        max_tokens=body.get("max_tokens", 1024),
        priority=USER_TIER_PRIORITY.get(user_tier, Priority.NORMAL),
        user_tier=user_tier,
        created_at=datetime.now().timestamp()
    )
    
    # enqueue
    await queue.enqueue(inference_request)
    
    # handle request…
    # (actual implementation will asynchronously process the queue)

@app.get("/v1/queue/stats")
async def queue_stats():
    """Get queue statistics"""
    return queue.get_stats()
```

---


## 9. Monitoring and Observability

### 9.1 Complete Monitoring Dashboard

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: llm-inference-rules
  namespace: llm-inference
spec:
  groups:
  - name: llm-inference-slos
    rules:
    # SLO: 99% request delay < 5s
    - record: llm:request_latency_p99
      expr: |
        histogram_quantile(0.99, 
          sum(rate(vllm_request_duration_seconds_bucket[5m])) by (le, model)
        )
    
    # SLO: Throughput
    - record: llm:throughput_tokens_per_second
      expr: |
        sum(rate(vllm_generation_tokens_total[5m])) by (model)
    
    # SLO: Availability
    - record: llm:availability
      expr: |
        sum(rate(vllm_request_success_total[5m])) by (model) /
        sum(rate(vllm_request_total[5m])) by (model)
    
    # Error rate
    - record: llm:error_rate
      expr: |
        sum(rate(vllm_request_error_total[5m])) by (model, error_type) /
        sum(rate(vllm_request_total[5m])) by (model)
  
  - name: llm-inference-alerts
    rules:
    # High-latency alert
    - alert: LLMHighLatency
      expr: llm:request_latency_p99 > 10
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "LLM inference latency is too high"
        description: "Model {{ $labels.model }} P99 latency {{ $value }} seconds"
    
    # Low-throughput alert
    - alert: LLMLowThroughput
      expr: llm:throughput_tokens_per_second < 100
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "LLM throughput drops"
        description: "Throughput of model {{ $labels.model }} {{ $value }} tokens per second"
    
    # High-error-rate alert
    - alert: LLMHighErrorRate
      expr: llm:error_rate > 0.05
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "LLM error rate is too high"
        description: "Error rate of model {{ $labels.model }} {{ $value | humanizePercentage }}"
    
    # GPU memory insufficient
    - alert: LLMGPUMemoryHigh
      expr: DCGM_FI_DEV_MEM_COPY_UTIL > 95
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "GPU memory utilization is too high"
        description: "Memory utilization of GPU {{ $labels.gpu }} {{ $value }}%"
    
    # Queue Backlog
    - alert: LLMQueueBacklog
      expr: vllm_num_requests_waiting > 100
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Inference request queue backlog"
        description: "Queue backlog {{ $value }} requests"
    
    # A Pod is not healthy
    - alert: LLMPodUnhealthy
      expr: |
        kube_pod_status_ready{namespace="llm-inference", condition="true"} == 0
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "LLM Pod is unhealthy"
        description: "Pod {{ $labels.pod }} unavailable"
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: grafana-llm-dashboard
  namespace: monitoring
  labels:
    grafana_dashboard: "1"
data:
  llm-inference.json: |
    {
      "dashboard": {
        "title": "LLM Inference Monitoring",
        "panels": [
          {
            "title": "Requests per Second",
            "type": "graph",
            "targets": [
              {
                "expr": "sum(rate(vllm_request_total[5m])) by (model)",
                "legendFormat": "{{ model }}"
              }
            ]
          },
          {
            "title": "P50/P95/P99 Latency",
            "type": "graph",
            "targets": [
              {
                "expr": "histogram_quantile(0.50, sum(rate(vllm_request_duration_seconds_bucket[5m])) by (le))",
                "legendFormat": "P50"
              },
              {
                "expr": "histogram_quantile(0.95, sum(rate(vllm_request_duration_seconds_bucket[5m])) by (le))",
                "legendFormat": "P95"
              },
              {
                "expr": "histogram_quantile(0.99, sum(rate(vllm_request_duration_seconds_bucket[5m])) by (le))",
                "legendFormat": "P99"
              }
            ]
          },
          {
            "title": "Throughput (tokens/s)",
            "type": "graph",
            "targets": [
              {
                "expr": "sum(rate(vllm_generation_tokens_total[5m])) by (model)",
                "legendFormat": "{{ model }}"
              }
            ]
          },
          {
            "title": "GPU Utilization",
            "type": "graph",
            "targets": [
              {
                "expr": "DCGM_FI_DEV_GPU_UTIL",
                "legendFormat": "GPU {{ gpu }}"
              }
            ]
          },
          {
            "title": "KV Cache Utilization",
            "type": "gauge",
            "targets": [
              {
                "expr": "avg(vllm_gpu_cache_usage_perc)"
              }
            ]
          },
          {
            "title": "Queue Depth",
            "type": "graph",
            "targets": [
              {
                "expr": "vllm_num_requests_waiting",
                "legendFormat": "Waiting"
              },
              {
                "expr": "vllm_num_requests_running",
                "legendFormat": "Running"
              }
            ]
          }
        ]
      }
    }
```

### 9.2 Request Tracing Configuration

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: otel-collector-config
  namespace: llm-inference
data:
  config.yaml: |
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
          http:
            endpoint: 0.0.0.0:4318
    
    processors:
      batch:
        timeout: 1s
        send_batch_size: 1000
      
      attributes:
        actions:
        - key: service.name
          value: llm-inference
          action: upsert
        - key: deployment.environment
          value: production
          action: upsert
    
    exporters:
      jaeger:
        endpoint: jaeger-collector:14250
        tls:
          insecure: true
      
      prometheus:
        endpoint: 0.0.0.0:8889
        namespace: llm_inference
    
    service:
      pipelines:
        traces:
          receivers: [otlp]
          processors: [batch, attributes]
          exporters: [jaeger]
        metrics:
          receivers: [otlp]
          processors: [batch]
          exporters: [prometheus]
```

---


## 10. Performance Benchmarks and Tuning

### 10.1 Model Performance Baseline (A100 80GB)

| Model | Configuration | Throughput (tok/s) | P50 Latency | P99 Latency | Memory Usage | Cost/1M tokens |
|-----|------|---------------|---------|---------|----------|---------------|
| **Llama3-8B** |
| | FP16, 1×A100 | 2,800 | 8ms | 15ms | 18GB | $0.02 |
| | INT8, 1×A100 | 3,500 | 6ms | 12ms | 10GB | $0.015 |
| | AWQ-4bit, 1×A100 | 4,200 | 5ms | 10ms | 6GB | $0.012 |
| **Llama3-70B** |
| | FP16, 4×A100 | 350 | 65ms | 120ms | 160GB | $0.18 |
| | INT8, 2×A100 | 420 | 55ms | 100ms | 80GB | $0.12 |
| | AWQ-4bit, 1×A100 | 480 | 48ms | 90ms | 42GB | $0.08 |
| **Mixtral-8x7B** |
| | FP16, 2×A100 | 800 | 28ms | 55ms | 100GB | $0.08 |
| | AWQ-4bit, 1×A100 | 1,100 | 20ms | 40ms | 28GB | $0.045 |
| **Llama3-405B** |
| | FP16, 8×H100 | 120 | 180ms | 350ms | 810GB | $0.65 |
| | FP8, 4×H100 | 180 | 120ms | 230ms | 420GB | $0.35 |
| | INT4, 2×H100 | 220 | 100ms | 200ms | 220GB | $0.22 |

### 10.2 Inference Engine Performance Comparison

| Engine | Model | Batch Size | Throughput (tok/s) | 99th Percentile Latency | Memory Efficiency |
|-----|------|-----------|---------------|---------|----------|
| **vLLM** | Llama3-70B-AWQ | 64 | 4,800 | 95ms | 92% |
| **TGI** | Llama3-70B-AWQ | 64 | 4,200 | 110ms | 88% |
| **TensorRT-LLM** | Llama3-70B-FP8 | 64 | 6,500 | 72ms | 95% |
| **SGLang** | Llama3-70B-AWQ | 64 | 5,200 | 85ms | 93% |
| **DeepSpeed-MII** | Llama3-70B | 64 | 3,800 | 125ms | 85% |

### 10.3 Tuning Parameter Guide

```yaml
# Performance Tuning Parameters Reference
performance_tuning:
  # Throughput optimization
  high_throughput:
    max_num_seqs: 512
    max_num_batched_tokens: 65536
    gpu_memory_utilization: 0.95
    enable_prefix_caching: true
    block_size: 32
    swap_space: 32
    
  # Delay optimization
  low_latency:
    max_num_seqs: 64
    max_num_batched_tokens: 8192
    gpu_memory_utilization: 0.80
    enable_prefix_caching: true
    block_size: 16
    use_speculative_decoding: true
    num_speculative_tokens: 5
    
  # Cost optimization
  cost_optimized:
    quantization: awq
    dtype: float16
    tensor_parallel_size: 1  # 最小化GPU使用
    gpu_memory_utilization: 0.95
    enable_prefix_caching: true
    
  # Optimize Long Context
  long_context:
    max_model_len: 128000
    max_num_seqs: 32
    enable_chunked_prefill: true
    max_num_batched_tokens: 32768
    gpu_memory_utilization: 0.90
```

---


## 11. Fault Diagnosis

### 11.1 Common Issue Diagnosis

| Problem | Symptoms | Possible Causes | Solutions |
|-----|------|---------|---------|
| **OOM Error** | CUDA out of memory | Model too large/batch too large | Reduce gpu_memory_utilization, decrease max_num_seqs |
| **Slow to Start** | Model loading >10 minutes | Network slow/Storage slow | Use local NVMe SSD, pre-download model |
| **Throughput Low** | <Expected 50% | CPU Bottleneck/IO Bottleneck | Increase CPU cores, use faster storage |
| **Latency Jitter** | P99>P50 | GC/Swap | Increase swap_space, adjust block_size |
| **Request Timeout** | 504 Error | Queue backlog/resource shortage | Increase replicas, adjust HPA thresholds |
| **NCCL Error** | Multi-GPU communication failure | Network configuration error | Check NCCL environment variables, IB configuration |

### 11.2 Diagnostic Commands

> ⚠️ **Yellow High Change** — Change cluster resource status, suggest to first run --dry-run or diff to confirm
> - `kubectl exec`: enter container to execute commands, may change container state

``` bash
# 🔴 Medium risk: modifies cluster/resource status; confirm target, impact scope, and authorization before proceeding
#!/bin/bash
# llm-diagnosis.sh - LLM inference service diagnostic script

# 1. Check Pod status
echo "=== Pod status ==="
kubectl get pods -n llm-inference -o wide

# Check GPU status
echo "=== GPU status ==="
kubectl exec -n llm-inference deployment/vllm-llama3-70b -- nvidia-smi

# Check vLLM health
echo "=== vLLM health check ==="
kubectl exec -n llm-inference deployment/vllm-llama3-70b -- \
  curl -s localhost:8000/health | jq .

# Check queue status
echo "=== Queue Status ==="
kubectl exec -n llm-inference deployment/vllm-llama3-70b -- \
  curl -s localhost:8000/metrics | grep -E "vllm_num_requests"

# Check KV Cache
echo "=== KV Cache Status ==="
kubectl exec -n llm-inference deployment/vllm-llama3-70b -- \
  curl -s localhost:8000/metrics | grep -E "vllm_.*cache"

# Check error logs
echo "=== Most Recent Error ==="
kubectl logs -n llm-inference deployment/vllm-llama3-70b --tail=100 | grep -i error

# Check resource usage
echo "=== Resource Usage ==="
kubectl top pods -n llm-inference

# Check HPA status
echo "=== HPA Status ==="
kubectl get hpa -n llm-inference

# Performance test
echo "=== Performance Test ==="
curl -X POST http://vllm-service.llm-inference:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama3-70b",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 100
  }' -w "\nTotal time: %{time_total}s\n"
```
---


## 12. Quick Reference

### 12.1 vLLM Startup Parameters Quick Reference

```bash
# Base startup
python -m vllm.entrypoints.openai.api_server \
  --model meta-llama/Meta-Llama-3-70B-Instruct \
  --tensor-parallel-size 4

# Production configuration
python -m vllm.entrypoints.openai.api_server \
  --model /models/llama3-70b-awq \
  --quantization awq \
  --tensor-parallel-size 4 \
  --dtype float16 \
  --max-model-len 8192 \
  --max-num-seqs 256 \
  --gpu-memory-utilization 0.90 \
  --enable-prefix-caching \
  --api-key $API_KEY

# Opportunistic decoding
python -m vllm.entrypoints.openai.api_server \
  --model /models/llama3-70b \
  --speculative-model /models/llama3-8b \
  --num-speculative-tokens 5 \
  --tensor-parallel-size 4

# Multi-LoRA
python -m vllm.entrypoints.openai.api_server \
  --model /models/llama3-70b \
  --enable-lora \
  --max-loras 8 \
  --lora-modules adapter1=/adapters/adapter1 adapter2=/adapters/adapter2
```

### 12.2 API Call Examples

```python
# OpenAI compatible API calls
import openai

client = openai.OpenAI(
    base_url="http://vllm-service:8000/v1",
    api_key="sk-xxx"
)

# Synchronous call
response = client.chat.completions.create(
    model="llama3-70b",
    messages=[{"role": "user", "content": "Hello"}],
    max_tokens=1024,
    temperature=0.7
)

# Streaming call
stream = client.chat.completions.create(
    model="llama3-70b",
    messages=[{"role": "user", "content": "Write a story"}],
    max_tokens=2048,
    stream=True
)
for chunk in stream:
    print(chunk.choices[0].delta.content, end="")

# Use LoRA adapter
response = client.chat.completions.create(
    model="llama3-70b:code-assistant",  # 指定适配器
    messages=[{"role": "user", "content": "Write a Python function"}],
    max_tokens=1024
)
```

### 12.3 Performance Monitoring Metrics

| Metric | Prometheus Query | Health Threshold |
|-----|------------------|----------|
| Request Latency P99 | `histogram_quantile(0.99, rate(vllm_request_duration_seconds_bucket[5m]))` | <5s |
| Throughput | `sum(rate(vllm_generation_tokens_total[5m]))` | >1000 tok/s |
| Queue Depth | `vllm_num_requests_waiting` | <50 |
| GPU Utilization | `DCGM_FI_DEV_GPU_UTIL` | 60-90% |
| KV Cache Usage Rate | `vllm_gpu_cache_usage_perc` | <95% |
| Error Rate | `rate(vllm_request_error_total[5m])/rate(vllm_request_total[5m])` | <1% |

---


## Thirteen - Best Practices Summary

### Production Deployment Checklist

- [ ] **High Availability**: At least 2 replicas, cross-AZ deployment
- [ ] **Resource Isolation**: GPU nodes with node taints, pod affinity
- [ ] **Health Checks**: Configure startup/liveness/readiness probes
- [ ] **Auto Scaling**: HPA based on GPU utilization and queue depth
- [ ] **Monitoring & Alerts**: Prometheus metrics, Grafana Dashboard
- [ ] **Logging Tracing**: Structured logs, distributed tracing
- [ ] **Security**: API authentication, network policies, Secret management
- [ ] **Cost Optimization**: Quantized models, Spot instances, auto-scaling
- [ ] **Disaster Recovery**: Model backup, recovery process

---

**Related Documentation**: [145-LLM Serving Architecture](145-llm-serving-architecture.md) | [146-LLM Quantization](146-llm-quantization.md) | [133-GPU Scheduling Management](133-gpu-scheduling-management.md)

**Version**: vLLM 0.4.2+ | TGI 2.0+ | TensorRT-LLM 0.9+ | Kubernetes v1.27+

---


## Obsidian Related Documentation

- domain-11-ai-infra MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Open Source Project Index
- AI Infrastructure Architecture
- 132 - AI/ML Workload Operations (AI/ML Workloads Operations)
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed training framework
- AI data processing Pipeline and feature engineering
- AI experiment management and MLOps platform
- AutoML and hyperparameter tuning
- AI model registry center and version management

## See Also

- 15-llm-data-pipeline
- 16-llm-finetuning
- 18-llm-serving-architecture
- 19-llm-quantization

## Related

- [[deep-dive|#deep-dive Hub]] — tag hub

- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Knowledge Graph Index]]


<!-- risk-assessed -->
