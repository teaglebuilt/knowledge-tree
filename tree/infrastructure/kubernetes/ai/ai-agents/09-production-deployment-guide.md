---
title: Production Deployment Guide: Running Agent Service on K8s
description: 'title: Production Deployment Guide: Running Agent Service on K8s'
summary: 'title: Production Deployment Guide: Running Agent Service on K8s'
category: general
tags:
- ai
- ai-agent
- deployment
- production
- guide
- prometheus
- istio
- redis
- postgresql
- hpa
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 25min
intent_queries:
- What is Production Deployment Guide: Running Agent Service on K8s
- How to Production Deployment Guide: Running Agent Service on K8s
- Best Practices for K8s 14 AI ML Infra
trigger_keywords:
- Production Deployment Guide: K8s
- Running
- Agent
- Service
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- service-mesh-basics
- prometheus-basics
- redis-basics
- gpu-scheduling-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/09-production-deployment-guide.md
---

> **Production Environment Security Reminders**
>
> This document contains executable operational commands. Please confirm before execution: that the target cluster and Namespace are correct; that you have sufficient RBAC permissions; and that these commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering, no side effects).




title: Production Deployment Guide: Running Agent Services on K8s
description: '# Production Deployment Guide: Running Agent Services on K8s'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- [[Prometheus|prometheus]]
- [[Istio|istio]]
- redis
- postgresql
- hpa
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- Architect
- SRE
estimated_read_time: 5min
intent_queries:
- AI Engineer
- Architect
trigger_keywords:
- What is Production Deployment Guide: K8s Running Agent Services
- How does Production Deployment Guide: K8s Running Agent Services work
- Agent
- K8s
- ai
- agent
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

# Production Deployment Guide: Running Agent Services on K8s

> **Document Type**: Production Operations Special Topic | **Last Updated**: 2026-03 | **Keywords**: Agent Deployment, K8s Production, GPU Scheduling, HPA, Rate Limiting, Gray Release, FastAPI, vLLM, Ray Serve, ServiceMesh

---

## Overview

Deploy the Agent service to a production environment running on [[Kubernetes|Kubernetes]]. This requires addressing resource management for LLM inference services on GPUs, network processing for long-lived connections and streaming outputs, elastic scaling based on queue length, and specific rate limiting and cost control needs for the Agent service. This article provides a complete production-level deployment architecture, YAML manifests, and operational manual.

---

## 1. Agent Service Architecture Design

## 1.1 Overall Architecture Perspective

```
                    External Traffic
                       │
         ┌─────────────▼─────────────┐
         │        Ingress / Gateway   │
         │  (Kong / Nginx / Istio)    │
         │  - SSL Termination               │
         │  - Authentication and Authorization               │
         │  - Rate Limiting               │
         └─────────────┬─────────────┘
                       │
         ┌─────────────▼─────────────┐
         │      Agent API Gateway     │
         │  (FastAPI / Flask)         │
         │  - Request Routing               │
         │  - User Quota Check            │
         │  - Asynchronous Task Queueing            │
         └──────────┬────────────────┘
                    │
       ┌────────────┼────────────┐
       ▼            ▼            ▼
┌──────────┐ ┌──────────┐ ┌──────────┐
│  Agent   │ │  Agent   │ │  Agent   │
│  Worker  │ │  Worker  │ │  Worker  │
│  Pod #1  │ │  Pod #2  │ │  Pod #3  │
└──────────┘ └──────────┘ └──────────┘
       │            │            │
       └────────────┼────────────┘
                    ▼
       ┌─────────────────────────┐
       │    LLM Inference Layer  │
       │  vLLM / TGI (GPU)      │
       │  + OpenAI API (External)    │
       └─────────────────────────┘
                    │
       ┌─────────────────────────┐
       │    Data & Storage Layer │
       │  Qdrant (Vector Library)         │
       │  Redis (Cache/Task Queue)   │
       │  PostgreSQL (Memory/Configuration)  │
       └─────────────────────────┘
```

## 1.2 Choosing Synchronous vs Asynchronous Modes

| Pattern | Applicable Scenario | Maximum Timeout | Implementation Complexity |
|------|---------|---------|-----------|
| **Synchronized Request** | Simple Q&A, Real-time Chatting | 30-60s | Low |
| **Streamed Output (SSE)** | Conversational scenarios, real-time user experience | Unlimited | Medium |
| **Asynchronous Tasks** | Long-running analysis, batch processing, multi-Agent | Unlimited | High |

---

## 2. Agent API Service

## 2.1 FastAPI Agent Service

```python
from fastapi import FastAPI, HTTPException, Depends, BackgroundTasks
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from typing import Optional, AsyncGenerator
import asyncio
import json
import uuid
from datetime import datetime

app = FastAPI(title="K8s Agent API", version="1.0.0")

# Request/Response Model
class AgentRequest(BaseModel):
    task: str = Field(..., description="task description", max_length=2000)
    session_id: Optional[str] = Field(None, description="session id, for multi-turn dialogue")
    agent_type: str = Field("general", description="Agent type: general/network/storage/security")
    stream: bool = Field(False, description="whether to stream output")
    max_steps: int = Field(10, ge=1, le=20, description="maximum number of execution steps")
    timeout_seconds: int = Field(60, ge=10, le=300)

class AgentResponse(BaseModel):
    request_id: str
    session_id: str
    answer: str
    steps_taken: int
    tools_used: list[str]
    success: bool
    duration_ms: float
    tokens_used: int

# Asynchronous Stream Output
async def agent_stream_generator(
    task: str,
    agent_executor,
    session_id: str,
) -> AsyncGenerator[str, None]:
    """Generate Server-Sent Events formatted stream output"""
    
    async for event in agent_executor.astream_events(
        {"input": task},
        version="v2",
    ):
        event_type = event["event"]
        
        if event_type == "on_chat_model_stream":
            # LLM generate text fragment
            content = event["data"]["chunk"].content
            if content:
                yield f"data: {json.dumps({'type': 'token', 'content': content})}\n\n"
        
        elif event_type == "on_tool_start":
            # Tool invocation begins
            tool_name = event["name"]
            tool_input = event["data"]["input"]
            yield f"data: {json.dumps({'type': 'tool_start', 'tool': tool_name, 'input': tool_input})}\n\n"
        
        elif event_type == "on_tool_end":
            # Tool invocation ends
            tool_name = event["name"]
            yield f"data: {json.dumps({'type': 'tool_end', 'tool': tool_name})}\n\n"
        
        elif event_type == "on_chain_end" and event.get("name") == "AgentExecutor":
            # Agent execution completes
            final_output = event["data"]["output"]["output"]
            yield f"data: {json.dumps({'type': 'done', 'content': final_output})}\n\n"
    
    yield "data: [DONE]\n\n"

@app.post("/v1/agent/run")
async def run_agent(
    request: AgentRequest,
    background_tasks: BackgroundTasks,
):
    """Synchronously or asynchronously execute Agent tasks"""
    
    request_id = str(uuid.uuid4())
    session_id = request.session_id or str(uuid.uuid4())
    
    # Get corresponding type of Agent
    agent_executor = get_agent(request.agent_type, request.max_steps)
    
    if request.stream:
        return StreamingResponse(
            agent_stream_generator(request.task, agent_executor, session_id),
            media_type="text/event-stream",
            headers={
                "X-Request-ID": request_id,
                "X-Session-ID": session_id,
                "Cache-Control": "no-cache",
                "Connection": "keep-alive",
            }
        )
    else:
        # Synchronous execution (with timeout)
        try:
            start_time = asyncio.get_event_loop().time()
            result = await asyncio.wait_for(
                agent_executor.ainvoke({"input": request.task}),
                timeout=request.timeout_seconds,
            )
            duration_ms = (asyncio.get_event_loop().time() - start_time) * 1000
            
            # Asynchronous audit log recording
            background_tasks.add_task(
                log_agent_execution,
                request_id=request_id,
                session_id=session_id,
                task=request.task,
                result=result,
                duration_ms=duration_ms,
            )
            
            return AgentResponse(
                request_id=request_id,
                session_id=session_id,
                answer=result.get("output", ""),
                steps_taken=len(result.get("intermediate_steps", [])),
                tools_used=list(set(
                    step[0].tool for step in result.get("intermediate_steps", [])
                )),
                success=True,
                duration_ms=duration_ms,
                tokens_used=result.get("tokens_used", 0),
            )
        
        except asyncio.TimeoutError:
            raise HTTPException(
                status_code=408,
                detail=f"Agent execution timeout ({request.timeout_seconds}s)"
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

# Health Checks
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat(),
        "version": "1.0.0",
    }

@app.get("/ready")
async def readiness_check():
    """Readiness check: validate key dependencies are available"""
    checks = {}
    
    # Check LLM availability
    try:
        # Lightweight ping check
        checks["llm"] = await check_llm_health()
    except Exception as e:
        checks["llm"] = f"unhealthy: {e}"
    
    # Check vector library
    try:
        checks["vector_store"] = await check_qdrant_health()
    except Exception as e:
        checks["vector_store"] = f"unhealthy: {e}"
    
    all_healthy = all(v == "healthy" for v in checks.values())
    
    if not all_healthy:
        raise HTTPException(status_code=503, detail=checks)
    
    return {"status": "ready", "checks": checks}
```

---

## 3. K8s Production Deployment Checklist

## 3.1 Agent Service Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: k8s-agent-api
  namespace: ai-agents
  labels:
    app: k8s-agent-api
    version: v1.2.0
    env: production
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0  # 零停机滚动更新
  selector:
    matchLabels:
      app: k8s-agent-api
  template:
    metadata:
      labels:
        app: k8s-agent-api
        version: v1.2.0
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
        prometheus.io/path: "/metrics"
    spec:
      serviceAccountName: agent-api-sa
      
      # Graceful shutdown: wait for existing requests to complete
      terminationGracePeriodSeconds: 120
      
      containers:
      - name: agent-api
        image: your-registry/k8s-agent-api:v1.2.0
        imagePullPolicy: Always
        
        ports:
        - name: http
          containerPort: 8080
        
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: llm-credentials
              key: openai-api-key
        - name: LANGFUSE_PUBLIC_KEY
          valueFrom:
            secretKeyRef:
              name: observability-keys
              key: langfuse-public-key
        - name: QDRANT_URL
          value: "http://qdrant.ai-infra.svc:6333"
        - name: REDIS_URL
          value: "redis://redis-master.ai-infra.svc:6379"
        - name: LOG_LEVEL
          value: "INFO"
        - name: WORKERS
          value: "4"  # Uvicorn worker 数
        - name: MAX_CONCURRENT_REQUESTS
          value: "20"
        
        resources:
          requests:
            cpu: "500m"
            memory: "1Gi"
          limits:
            cpu: "2"
            memory: "2Gi"
        
        # Readiness probe: accept traffic only after dependencies are ready
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 20
          periodSeconds: 10
          failureThreshold: 3
        
        # Health probe: detect deadlocks and other issues
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 30
          failureThreshold: 3
        
        # Graceful shutdown handling
        lifecycle:
          preStop:
            exec:
              command: ["/bin/sh", "-c", "sleep 10"]  # 等待 LB 摘流
      
      # Node Affinity: Deploy Agent service to non-GPU nodes
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchLabels:
                  app: k8s-agent-api
              topologyKey: kubernetes.io/hostname
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: node-type
                operator: NotIn
                values: ["gpu"]  # 不占用 GPU 节点
      
      topologySpreadConstraints:
      - maxSkew: 1
        topologyKey: topology.kubernetes.io/zone
        whenUnsatisfiable: DoNotSchedule
        labelSelector:
          matchLabels:
            app: k8s-agent-api
```

## 3.2 HPA (Based on Custom Metrics)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: k8s-agent-api-hpa
  namespace: ai-agents
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: k8s-agent-api
  minReplicas: 2
  maxReplicas: 20
  
  metrics:
  # Based on CPU Utilization
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 60
  
  # Based on Memory Utilization
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 70
  
  # Based on Request Queue Depth (custom metric)
  - type: External
    external:
      metric:
        name: redis_queue_length
        selector:
          matchLabels:
            queue: agent_task_queue
      target:
        type: AverageValue
        averageValue: "5"  # 每个 Pod 处理 5 个待处理任务
  
  behavior:
    scaleUp:
      stabilizationWindowSeconds: 60   # 扩容稳定窗口 1 分钟
      policies:
      - type: Pods
        value: 3
        periodSeconds: 60
    scaleDown:
      stabilizationWindowSeconds: 300  # 缩容稳定窗口 5 分钟（防止震荡）
      policies:
      - type: Pods
        value: 1
        periodSeconds: 120
```

## 3.3 Service and Ingress

```yaml
apiVersion: v1
kind: Service
metadata:
  name: k8s-agent-api
  namespace: ai-agents
  annotations:
    # Support WebSocket and Long Polling (SSE streaming output)
    nginx.ingress.kubernetes.io/proxy-read-timeout: "600"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "600"
spec:
  selector:
    app: k8s-agent-api
  ports:
  - name: http
    port: 80
    targetPort: 8080
  type: ClusterIP

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: k8s-agent-api
  namespace: ai-agents
  annotations:
    nginx.ingress.kubernetes.io/rewrite-target: /
    # Global Rate Limiting
    nginx.ingress.kubernetes.io/limit-rpm: "60"
    nginx.ingress.kubernetes.io/limit-burst-multiplier: "5"
    # Timeout Configuration (Agent tasks may run longer)
    nginx.ingress.kubernetes.io/proxy-connect-timeout: "10"
    nginx.ingress.kubernetes.io/proxy-read-timeout: "300"
    nginx.ingress.kubernetes.io/proxy-send-timeout: "300"
    # Request Body Size Limitation
    nginx.ingress.kubernetes.io/proxy-body-size: "10m"
    # Enable gzip Compression
    nginx.ingress.kubernetes.io/enable-access-log: "true"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - agent-api.your-domain.com
    secretName: agent-api-tls
  rules:
  - host: agent-api.your-domain.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: k8s-agent-api
            port:
              number: 80
```

---

## 4. Deploying LLM Inference Services (vLLM)

## 4.1 Production Configuration for vLLM

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-qwen25-72b
  namespace: ai-serving
spec:
  replicas: 1  # GPU 资源有限，通常单副本
  selector:
    matchLabels:
      app: vllm-qwen25-72b
  template:
    spec:
      containers:
      - name: vllm
        image: vllm/vllm-openai:v0.6.3
        command:
        - python3
        - -m
        - vllm.entrypoints.openai.api_server
        args:
        - --model=/models/Qwen2.5-72B-Instruct
        - --served-model-name=qwen2.5-72b
        - --tensor-parallel-size=4
        - --max-model-len=32768
        - --max-num-seqs=256
        - --enable-chunked-prefill
        - --enable-prefix-caching    # KV Cache 复用，降低重复 Prefix 的延迟
        - --gpu-memory-utilization=0.9
        - --dtype=bfloat16
        - --trust-remote-code
        - --port=8000
        
        ports:
        - containerPort: 8000
        
        env:
        - name: VLLM_API_KEY
          valueFrom:
            secretKeyRef:
              name: vllm-secret
              key: api-key
        
        resources:
          limits:
            nvidia.com/gpu: "4"
            memory: "200Gi"
          requests:
            nvidia.com/gpu: "4"
            memory: "180Gi"
            cpu: "8"
        
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 120  # 模型加载需要时间
          periodSeconds: 10
          failureThreshold: 30
        
        volumeMounts:
        - name: model-storage
          mountPath: /models
          readOnly: true
        - name: shm
          mountPath: /dev/shm
      
      volumes:
      - name: model-storage
        persistentVolumeClaim:
          claimName: model-storage-pvc
      - name: shm
        emptyDir:
          medium: Memory
          sizeLimit: "20Gi"
      
      tolerations:
      - key: "nvidia.com/gpu"
        operator: "Exists"
        effect: "NoSchedule"
      
      nodeSelector:
        gpu-type: a100-80g
      
      priorityClassName: gpu-high-priority
```

## 4.2 Multi-replica Routing for LLM Services

```yaml
# Unified Entry Point for Multi-model Services (distinguished by Label)
apiVersion: v1
kind: Service
metadata:
  name: llm-router
  namespace: ai-serving
spec:
  selector:
    # No specific app specified, managed manually via endpoints
  ports:
  - port: 8000
    targetPort: 8000

---
# Use KEDA to scale based on GPU Utilization
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: vllm-scaler
  namespace: ai-serving
spec:
  scaleTargetRef:
    name: vllm-qwen25-7b  # 7B 模型可以多副本
  minReplicaCount: 1
  maxReplicaCount: 4
  triggers:
  - type: prometheus
    metadata:
      serverAddress: http://prometheus.monitoring.svc:9090
      metricName: vllm_requests_waiting
      query: sum(vllm:num_requests_waiting{job="vllm"})
      threshold: "10"  # 等待队列超过 10 时扩容
```

---

## 5. Gray Release Strategy

## 5.1 Canary Release

```yaml
# Stable Version (90% Traffic)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: k8s-agent-api-stable
  labels:
    app: k8s-agent-api
    track: stable
spec:
  replicas: 9
  selector:
    matchLabels:
      app: k8s-agent-api
      track: stable
  template:
    metadata:
      labels:
        app: k8s-agent-api
        track: stable
        version: v1.1.0

---
# Canary Version (10% Traffic)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: k8s-agent-api-canary
  labels:
    app: k8s-agent-api
    track: canary
spec:
  replicas: 1  # 1 副本 = 约 10% 流量
  selector:
    matchLabels:
      app: k8s-agent-api
      track: canary
  template:
    metadata:
      labels:
        app: k8s-agent-api
        track: canary
        version: v1.2.0

---
# Select two Deployments for Service (based on app label)
apiVersion: v1
kind: Service
metadata:
  name: k8s-agent-api
spec:
  selector:
    app: k8s-agent-api  # 同时匹配 stable 和 canary
  ports:
  - port: 80
    targetPort: 8080
```

## 5.2 Intelligent Gray Release Based on Argo Rollouts

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: k8s-agent-api
  namespace: ai-agents
spec:
  replicas: 10
  strategy:
    canary:
      # Phased Canary, automatically advancing based on success rate
      analysis:
        templates:
        - templateName: agent-success-rate
        startingStep: 1
      steps:
      - setWeight: 5    # 先放 5% 流量
      - pause: {duration: 10m}  # 观察 10 分钟
      - setWeight: 20
      - pause: {duration: 10m}
      - setWeight: 50
      - pause: {duration: 10m}
      - setWeight: 100  # 全量

---
# Rollback Template: Automatically rollback if success rate is below 95%
apiVersion: argoproj.io/v1alpha1
kind: AnalysisTemplate
metadata:
  name: agent-success-rate
  namespace: ai-agents
spec:
  metrics:
  - name: success-rate
    interval: 2m
    successCondition: result[0] >= 0.95
    failureLimit: 2  # 连续 2 次失败触发回滚
    provider:
      prometheus:
        address: http://prometheus.monitoring.svc:9090
        query: |
          sum(rate(agent_requests_total{status="success"}[2m])) /
          sum(rate(agent_requests_total[2m]))
```

---

## 6. Rate Limiting and Quota Management

## 6.1 User-Level Rate Limiting

```python
import redis.asyncio as aioredis
from fastapi import Request, HTTPException

class RateLimiter:
    """Based on Redis Sliding Window Rate Limiting"""
    
    def __init__(self, redis_url: str):
        self.redis = aioredis.from_url(redis_url)
    
    async def check_rate_limit(
        self,
        user_id: str,
        limit: int,
        window_seconds: int,
    ) -> tuple[bool, dict]:
        """Check if rate limiting has been exceeded"""
        
        key = f"rate_limit:{user_id}"
        current_time = time.time()
        window_start = current_time - window_seconds
        
        pipe = self.redis.pipeline()
        pipe.zremrangebyscore(key, 0, window_start)  # 清理过期记录
        pipe.zadd(key, {str(current_time): current_time})
        pipe.zcard(key)
        pipe.expire(key, window_seconds)
        _, _, count, _ = await pipe.execute()
        
        remaining = max(0, limit - count)
        allowed = count <= limit
        
        headers = {
            "X-RateLimit-Limit": str(limit),
            "X-RateLimit-Remaining": str(remaining),
            "X-RateLimit-Reset": str(int(current_time + window_seconds)),
        }
        
        return allowed, headers

# Define User-level Quotas
USER_RATE_LIMITS = {
    "free": {"rpm": 5, "rpd": 50, "tokens_per_day": 100_000},
    "pro": {"rpm": 30, "rpd": 500, "tokens_per_day": 2_000_000},
    "enterprise": {"rpm": 200, "rpd": 10000, "tokens_per_day": 50_000_000},
}

@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    user_id = request.headers.get("X-User-ID", "anonymous")
    user_tier = await get_user_tier(user_id)
    limits = USER_RATE_LIMITS.get(user_tier, USER_RATE_LIMITS["free"])
    
    allowed, headers = await rate_limiter.check_rate_limit(
        user_id=user_id,
        limit=limits["rpm"],
        window_seconds=60,
    )
    
    if not allowed:
        raise HTTPException(
            status_code=429,
            detail="request frequency exceeds limit, please retry later",
            headers=headers,
        )
    
    response = await call_next(request)
    response.headers.update(headers)
    return response
```

---

## 7. Production Operations Runbook

## 7.1 Common Fault Handling

> ⚠️ **🟡 Medium Risk Change** — Modify cluster resource status, suggest first using --dry-run or diff to confirm
> - `kubectl exec`: Execute commands inside a container, which may alter container state
> - `kubectl rollout undo/restart`: Trigger rolling updates, affecting replicas

```
# 🔴 Medium risk: modifies cluster/resource status; confirm target, impact scope, and authorization before execution
Question 1: Agent API Response Time Spike (>10s P95)

Steps for Diagnosis:
  1. kubectl top pods -n ai-agents
  2. kubectl get hpa -n ai-agents  # Check if scaling is needed
  3. Check LLM service latency: curl http://vllm.ai-serving/health
  4. Check Redis connection: redis-cli ping
  5. Review Langfuse/LangSmith traces to identify which step is slow

Common Causes and Solutions:
  a. LLM response slow → Check GPU utilization, increase vLLM replicas or switch to a backup API if necessary
  b. Queue backlog → Increase Agent Worker replicas
  c. Vector search slow → Qdrant index not hot-loaded, restart and preheat

Recovery verification:
  kubectl run test-pod --rm -it --image=curlimages/curl -- \
    curl -X POST http://k8s-agent-api.ai-agents/v1/agent/run \
    -d '{"task": "simple test"}'

Problem 2: Agent Pod OOMKilled

Analysis:
  1. kubectl describe pod <pod-name> -n ai-agents | grep -A5 OOM
  2. Check for large context requests (Tokens over 50K)
  3. Check if embedding cache is abnormally large

Treatment:
  1. Temporarily: Increase memory limits.memory
  2. Root cause: Limit maximum Tokens per request
     MAX_INPUT_TOKENS=10000 (environment variable)
  3. Add memory alert: agent_memory_usage > 1.5Gi

Problem 3: vLLM OOM (GPU memory shortage)

Analysis:
  1. kubectl exec -n ai-serving <vllm-pod> -- nvidia-smi
  2. Check vLLM metrics: /metrics endpoint's gpu_cache_usage_perc

Treatment:
  1. Reduce --max-num-seqs (concurrent requests)
  2. Reduce --max-model-len (maximum context length)
  3. Lower --gpu-memory-utilization to 0.85
  4. Restart Pod: kubectl rollout restart deployment/vllm-xxx
```
## 7.2 Key Monitoring Checklist

> ⚠️ **🟡 Medium Risk Changes** — Modify cluster resource states, suggest first using --dry-run or diff to confirm
> - `kubectl exec`: Enter container to execute commands, which may alter container state

``` bash
# 🔴 Medium risk: modifies cluster/resource status; confirm target, impact scope, and authorization before execution
# Agent system health inspection script
#!/bin/bash

echo "=== Agent System Health Check ==="
echo "Time: $(date)"

# 1. Pod status
echo "\n[Pod Status]"
kubectl get pods -n ai-agents -o wide

# 2. HPA status
echo "\n[HPA Status]"
kubectl get hpa -n ai-agents

# 3. Agent API health
echo "\n[API Health]"
curl -s http://k8s-agent-api.ai-agents/health | python3 -m json.tool

# 4. Success rate (last hour)
echo "\n[Success Rate in Last Hour]"
curl -s "http://prometheus.monitoring.svc:9090/api/v1/query?query=\
  sum(rate(agent_requests_total{status='success'}[1h]))/\
  sum(rate(agent_requests_total[1h]))*100" | \
  python3 -c "import sys,json; data=json.load(sys.stdin); \
  print(f\"success rate: {float(data['data']['result'][0]['value'][1]):.1f}%\")"

# 5. LLM service status
echo "\n[LLM Service Status]"
kubectl get pods -n ai-serving -l app=vllm

# 6. Redis status
echo "\n[Redis Queue Depth]"
kubectl exec -n ai-infra redis-master-0 -- redis-cli llen agent_task_queue
```
---

## 8. Best Practices and Anti-patterns

## Best Practices

- **Zero Downtime Deployment**: Combining `maxUnavailable: 0`, `preStop sleep`, and readiness probes ensures smooth rolling updates
- **Prioritize Streamlined Output**: Dialog scenarios must support SSE for streaming output, significantly improving user experience
- **Use Custom Metrics for HPA**: CPU utilization cannot accurately reflect Agent load; use task queue depth for more accurate measurement
- **Deploy vLLM and Agent Services Independently**: Separate deployment of vLLM and Agent services avoids mutual interference and facilitates independent scaling
- **Must Include Quality Analysis in Gradual Releases**: Pure proportional Canaries are insufficient; add automatic rollback detection for success rate

## Anti-patterns

- **Share Pods Between Agent and LLM**: Both require vastly different resources, leading to waste or OOM if combined
- **Unlimited Request Body Size**: Without setting `proxy-body-size`, large Prompts can overwhelm the service
- **Readiness Probes Do Not Check LLM**: Agent starts but LLM fails to connect, still passing readiness probes; traffic ingress results in total failure
- **No `terminationGracePeriodSeconds` Set**: Forcing terminated ongoing Agent tasks during rolling updates breaks user experience

---

## Related Documentation

| Document | Related Content |
|------|---------|
| [06 - Multi-Agent Orchestration](./06-multi-agent-orchestration.md) | Coordination among multiple Worker Pods |
| [08 - Evaluation and Observability](./08-agent-evaluation-observability.md) | Prometheus Indicators and Langfuse |
| [11 - Cost Optimization](./11-cost-latency-optimization.md) | Resource Quotas and Cost Control |
| [domain-14-ai-ml-infra/17-llm-inference-serving.md](../domain-14-ai-ml-infra/17-llm-inference-serving.md) | Details of vLLM/TGI Inference Service |
| [domain-02-workloads-applications](../domain-02-workloads-applications/) | Best Practices for K8s Deployments |
| [domain-32-yaml-manifests](../domain-18-manifests-patterns/) | Comprehensive YAML Template Reference |

---

*This document is original content from the kudig-database project's 02-ai-agents topic.*

---

## Obsidian Related Documentation

- 02-ai-agents MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|AI Agent Engineering Topic]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|AI Agent Fundamentals and Core Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|LLM Foundation Models Selection and Evaluation]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Mainstream Agent Framework Deep Comparison]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|RAG Retrieval-Augmented Generation Deep Guide]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Tool Usage and Function Calling Design Guidelines]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Multi-Agent Orchestration and Collaboration Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation and Observability System]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]
- [[domain-14-ai-ml-infra/02-ai-agents/11-cost-latency-optimization.md|Cost and Latency Optimization Strategies]]

## Related

- 40-agent-harness-production-maturity
- 41-react-harness-identification-guide

## See Also

- 07-memory-context-management
- 08-agent-evaluation-observability
- 10-security-guardrails
- 11-cost-latency-optimization


<!-- risk-assessed -->
