---
title: Agent Cost Optimization and Caching
description: 'LLM Request Caching, Token Usage Optimization, Model Routing and Cost Monitoring for a Complete Implementation'
summary: 'LLM Request Caching, Token Usage Optimization, Model Routing and Cost Monitoring for a Complete Implementation'
category: platform-engineering
tags:
- ai-agent
- cost-optimization
- llm-cache
- token-optimization
- model-routing
tier: supporting
created: '2026-07-02'
last_updated: 2026-07
difficulty: advanced
reading_level: advanced
audience:
- All Engineers
- Architects
- SRE
estimated_read_time: 15min
intent_queries:
- What is Agent Cost Optimization
- How to Reduce the Cost of LLM Calls
trigger_keywords:
- Agent Cost
- LLM Caching
- Token Optimization
- Model Routing
- Cost Monitoring
prerequisites:
- kubectl-basics
- microservice-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: Dillan Teagle
  role: contributor
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/52-agent-cost-optimization-caching.md
---

> **Production Environment Security Notice**
>
> This document contains executable operational commands. Execute at your own risk: confirm that the target cluster and Namespace are correct; have sufficient RBAC permissions; and have validated these commands in a non-production environment. Risk level annotations: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (modifies cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering, no side effects).


# Agent Cost Optimization and Caching

## 1. Overview

LLM call costs are the primary expense in AI Agent operations. This document covers four core optimization strategies: request caching, token usage optimization, intelligent model routing, and cost monitoring alerts, helping reduce LLM call costs by 50-80%.

## 2. Optimization Landscape

```
LLM cost optimization strategies:

1. Cache Optimization
   → Semantic caching: reuse answers for similar questions
   → Precise caching: Return identical requests directly
   → Expected savings: 30-50%

2. Token Optimization (Token)
   → Prompt Compress: Remove redundant context
   → Context truncation: Intelligent selection of historical messages
   → Expected savings: 20-40%

3. Model Routing (Routing)
   → Simple problem → Small model (GPT-3.5)
   → Complex problems → Large models (GPT-4)
   → Expected savings: 40-60%

4. Batch Merge (Batching)
   → Batch process similar requests
   → Asynchronous non-critical requests
   → Expected savings: 10-20%

Comprehensive strategy: Cache + Token + Routing → 50-80% Cost reduction
```

## 3. LLM Request Caching

### 3.1 Precise Caching (Exact Cache)

```python
# Based on Redis Precise Caching
import hashlib
import json
import redis
from typing import Optional, Dict

class LLMExactCache:
    """Precise Matching Caching: Return cached results for identical inputs"""

    def __init__(self, redis_url: str, ttl: int = 3600):
        self.redis = redis.from_url(redis_url)
        self.ttl = ttl

    def _build_cache_key(self, model: str, messages: list, **kwargs) -> str:
        """Build cache key"""
        cache_input = {
            "model": model,
            "messages": messages,
            **{k: v for k, v in kwargs.items() if k in ["temperature", "max_tokens"]}
        }
        # Remove unstable parameters
        cache_str = json.dumps(cache_input, sort_keys=True)
        return f"llm:exact:{hashlib.sha256(cache_str.encode()).hexdigest()}"

    def get(self, model: str, messages: list, **kwargs) -> Optional[Dict]:
        """Query cache"""
        key = self._build_cache_key(model, messages, **kwargs)
        cached = self.redis.get(key)
        if cached:
            return json.loads(cached)
        return None

    def set(self, model: str, messages: list, response: Dict, **kwargs):
        """Write to cache"""
        key = self._build_cache_key(model, messages, **kwargs)
        self.redis.setex(key, self.ttl, json.dumps(response))

    def get_or_call(self, model: str, messages: list, llm_call_fn, **kwargs) -> Dict:
        """Cache Priority: Return from cache if hit, otherwise call LLM"""
        cached = self.get(model, messages, **kwargs)
        if cached:
            cached["cache_hit"] = True
            return cached

        response = llm_call_fn(model, messages, **kwargs)
        self.set(model, messages, response, **kwargs)
        response["cache_hit"] = False
        return response

# Usage Example
cache = LLMExactCache("redis://localhost:6379")
response = cache.get_or_call(
    model="gpt-4",
    messages=[{"role": "user", "content": "What is Kubernetes?"}],
    llm_call_fn=openai_chat_completion
)
```

### 3.2 Semantic Cache (Semantic Cache)

```python
# Based on Vector Similarity Semantic Caching
import numpy as np
from typing import Optional, Tuple
import faiss
from sentence_transformers import SentenceTransformer

class SemanticCache:
    """Semantic Caching: Reuse answers for similar questions"""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2", threshold: float = 0.92):
        self.encoder = SentenceTransformer(model_name)
        self.threshold = threshold
        self.index = None
        self.responses = []
        self.questions = []

    def _encode(self, text: str) -> np.ndarray:
        """Encode text into vectors"""
        return self.encoder.encode([text])[0]

    def add(self, question: str, response: dict):
        """Add cache entry"""
        embedding = self._encode(question)

        if self.index is None:
            dimension = embedding.shape[0]
            self.index = faiss.IndexFlatIP(dimension)  # 内积相似度

        # Normalize vectors
        faiss.normalize_L2(embedding.reshape(1, -1))
        self.index.add(embedding.reshape(1, -1))
        self.questions.append(question)
        self.responses.append(response)

    def search(self, question: str) -> Tuple[Optional[dict], float]:
        """Search similar questions"""
        if self.index is None or self.index.ntotal == 0:
            return None, 0.0

        query_embedding = self._encode(question)
        faiss.normalize_L2(query_embedding.reshape(1, -1))

        scores, indices = self.index.search(query_embedding.reshape(1, -1), k=1)
        similarity = scores[0][0]

        if similarity >= self.threshold:
            return self.responses[indices[0][0]], float(similarity)
        return None, float(similarity)

# Usage Example
semantic_cache = SemanticCache(threshold=0.90)
response, similarity = semantic_cache.search("K8s is what?")
if response:
    print(f"Semantic cache hit, similarity: {similarity:.2f}")
else:
    response = call_llm(...)
    semantic_cache.add("K8s is what?", response)
```

### 3.3 Hybrid Caching Strategy

```python
# Hybrid Caching: Precise + Semantic
class HybridLLMCache:
    """Hybrid Caching Strategy"""

    def __init__(self, redis_url: str):
        self.exact_cache = LLMExactCache(redis_url)
        self.semantic_cache = SemanticCache(threshold=0.92)

    def get_or_call(self, model: str, messages: list, llm_call_fn, **kwargs) -> Dict:
        """Three-level caching strategy"""
        # Level 1: Precise Caching
        cached = self.exact_cache.get(model, messages, **kwargs)
        if cached:
            cached["cache_type"] = "exact"
            cached["cache_hit"] = True
            return cached

        # Level 2: Semantic Caching
        user_message = self._extract_user_message(messages)
        semantic_result, similarity = self.semantic_cache.search(user_message)
        if semantic_result:
            semantic_result["cache_type"] = "semantic"
            semantic_result["cache_hit"] = True
            semantic_result["similarity"] = similarity
            return semantic_result

        # Level 3: Invoke LLM
        response = llm_call_fn(model, messages, **kwargs)
        response["cache_hit"] = False

        # Write to Cache
        self.exact_cache.set(model, messages, response, **kwargs)
        self.semantic_cache.add(user_message, response)

        return response

    def _extract_user_message(self, messages: list) -> str:
        for msg in reversed(messages):
            if msg["role"] == "user":
                return msg["content"]
        return ""
```

## 4. Token Usage Optimization

### 4.1 Compress Prompt

```python
# Compress Prompt Strategy
class PromptCompressor:
    """Compress Prompt to Reduce Token Usage"""

    def __init__(self, max_tokens: int = 4000):
        self.max_tokens = max_tokens

    def compress(self, messages: list) -> list:
        """Compress Message List"""
        compressed = []

        # 1. Retain System Messages
        system_msgs = [m for m in messages if m["role"] == "system"]
        compressed.extend(system_msgs)

        # 2. Compress Historical Messages
        history_msgs = [m for m in messages if m["role"] in ["user", "assistant"]]
        if len(history_msgs) > 10:
            # Retain Recent 5 Rounds of Conversation
            recent = history_msgs[-10:]
            # Preserve summaries for early conversations
            early = history_msgs[:-10]
            summary = self._summarize_history(early)
            compressed.append({"role": "system", "content": f"Historical dialogue summary: {summary}"})
            compressed.extend(recent)
        else:
            compressed.extend(history_msgs)

        return compressed

    def _summarize_history(self, messages: list) -> str:
        """Summarize Historical Conversations"""
        topics = []
        for msg in messages:
            if msg["role"] == "user":
                # Extract Key Information
                content = msg["content"][:100]
                topics.append(content)
        return "; ".join(topics[:5])

    def estimate_tokens(self, messages: list) -> int:
        """Estimate Token Count"""
        total_chars = sum(len(m["content"]) for m in messages)
        # Chinese is approximately 1.5 characters/token, English is approximately 4 characters/token
        return int(total_chars / 2.5)
```

### 4.2 Context Pruning

```python
# Intelligent Context Pruning
class ContextTrimmer:
    """Intelligently prune context to retain most relevant information"""

    def __init__(self, max_context_tokens: int = 3000):
        self.max_tokens = max_context_tokens

    def trim(self, messages: list, current_query: str) -> list:
        """Trim context to the specified size"""
        if self._estimate_tokens(messages) <= self.max_tokens:
            return messages

        # Strategy: retain system messages + recent dialog + relevant history
        system_msgs = [m for m in messages if m["role"] == "system"]
        other_msgs = [m for m in messages if m["role"] != "system"]

        # Calculate available tokens
        system_tokens = self._estimate_tokens(system_msgs)
        available_tokens = self.max_tokens - system_tokens

        # Prioritize recent dialog
        recent_msgs = []
        recent_tokens = 0
        for msg in reversed(other_msgs):
            msg_tokens = self._estimate_tokens([msg])
            if recent_tokens + msg_tokens > available_tokens * 0.7:
                break
            recent_msgs.insert(0, msg)
            recent_tokens += msg_tokens

        # Allocate remaining space to relevant history
        remaining_tokens = available_tokens - recent_tokens
        relevant_msgs = self._find_relevant(
            other_msgs[:-len(recent_msgs)],
            current_query,
            remaining_tokens
        )

        return system_msgs + relevant_msgs + recent_msgs

    def _find_relevant(self, messages: list, query: str, max_tokens: int) -> list:
        """Find historical messages relevant to the current query"""
        # Simplified implementation: keyword matching
        query_words = set(query.lower().split())
        scored_msgs = []

        for msg in messages:
            content_words = set(msg["content"].lower().split())
            overlap = len(query_words & content_words)
            scored_msgs.append((overlap, msg))

        # Sort by relevance
        scored_msgs.sort(key=lambda x: x[0], reverse=True)

        relevant = []
        tokens = 0
        for score, msg in scored_msgs:
            if score == 0:
                continue
            msg_tokens = self._estimate_tokens([msg])
            if tokens + msg_tokens > max_tokens:
                break
            relevant.append(msg)
            tokens += msg_tokens

        return relevant

    def _estimate_tokens(self, messages: list) -> int:
        return sum(len(m["content"]) // 2.5 for m in messages)
```

### 4.3 Token Usage Monitoring

```python
# Token Usage Tracking
from dataclasses import dataclass
from datetime import datetime
from typing import Dict
import redis

@dataclass
class TokenUsage:
    input_tokens: int
    output_tokens: int
    model: str
    timestamp: datetime
    cost: float

class TokenTracker:
    """Token Usage Tracker"""

    MODEL_PRICING = {
        "gpt-4": {"input": 0.03, "output": 0.06},           # per 1K tokens
        "gpt-4-turbo": {"input": 0.01, "output": 0.03},
        "gpt-3.5-turbo": {"input": 0.0005, "output": 0.0015},
        "claude-3-opus": {"input": 0.015, "output": 0.075},
        "claude-3-sonnet": {"input": 0.003, "output": 0.015},
    }

    def __init__(self, redis_url: str):
        self.redis = redis.from_url(redis_url)

    def track(self, usage: TokenUsage):
        """Record Token Usage"""
        # Aggregate by hour
        hour_key = usage.timestamp.strftime("%Y%m%d%H")
        self.redis.hincrby(f"tokens:{hour_key}", "input", usage.input_tokens)
        self.redis.hincrby(f"tokens:{hour_key}", "output", usage.output_tokens)
        self.redis.hincrbyfloat(f"tokens:{hour_key}", "cost", usage.cost)

        # Aggregate by model
        model_key = f"tokens:model:{usage.model}:{hour_key}"
        self.redis.hincrby(model_key, "input", usage.input_tokens)
        self.redis.hincrby(model_key, "output", usage.output_tokens)

    def calculate_cost(self, model: str, input_tokens: int, output_tokens: int) -> float:
        """Calculate cost"""
        pricing = self.MODEL_PRICING.get(model, {"input": 0.01, "output": 0.03})
        input_cost = (input_tokens / 1000) * pricing["input"]
        output_cost = (output_tokens / 1000) * pricing["output"]
        return input_cost + output_cost

    def get_daily_summary(self, date: str) -> Dict:
        """Get daily summary"""
        total_input = 0
        total_output = 0
        total_cost = 0.0

        for hour in range(24):
            key = f"tokens:{date}{hour:02d}"
            data = self.redis.hgetall(key)
            if data:
                total_input += int(data.get(b"input", 0))
                total_output += int(data.get(b"output", 0))
                total_cost += float(data.get(b"cost", 0))

        return {
            "date": date,
            "total_input_tokens": total_input,
            "total_output_tokens": total_output,
            "total_cost_usd": round(total_cost, 2)
        }
```

## 5. Model Routing

### 5.1 Intelligent Routing Strategy

```python
# Intelligent Model Routing
from typing import Dict, List
from enum import Enum

class QueryComplexity(Enum):
    SIMPLE = "simple"        # 简单查询
    MODERATE = "moderate"    # 中等复杂
    COMPLEX = "complex"      # 复杂推理

class ModelRouter:
    """Route queries to different models based on complexity"""

    MODEL_MAP = {
        QueryComplexity.SIMPLE: "gpt-3.5-turbo",
        QueryComplexity.MODERATE: "gpt-4-turbo",
        QueryComplexity.COMPLEX: "gpt-4",
    }

    def __init__(self):
        self.complexity_classifier = ComplexityClassifier()

    def route(self, query: str, context: List[Dict] = None) -> str:
        """route to the appropriate model"""
        complexity = self.complexity_classifier.classify(query, context)
        model = self.MODEL_MAP[complexity]
        return model

    def route_with_cost_estimate(self, query: str, context: List[Dict] = None) -> Dict:
        """route and return cost estimate"""
        complexity = self.complexity_classifier.classify(query, context)
        model = self.MODEL_MAP[complexity]

        # Estimate Tokens
        estimated_tokens = len(query) // 2.5
        if context:
            estimated_tokens += sum(len(m["content"]) // 2.5 for m in context)

        return {
            "model": model,
            "complexity": complexity.value,
            "estimated_tokens": int(estimated_tokens),
            "estimated_cost": self._estimate_cost(model, int(estimated_tokens))
        }

    def _estimate_cost(self, model: str, tokens: int) -> float:
        pricing = TokenTracker.MODEL_PRICING.get(model, {"input": 0.01, "output": 0.03})
        return (tokens / 1000) * pricing["input"] * 1.5  # 假设输出是输入的 1.5 倍


class ComplexityClassifier:
    """query complexity classifier"""

    COMPLEX_INDICATORS = [
        "analysis", "comparison", "evaluation", "design", "optimization", "explain reasons",
        "analyze", "compare", "evaluate", "design", "optimize"
    ]

    SIMPLE_INDICATORS = [
        "what is", "define", "list", "query", "status",
        "what is", "define", "list", "status", "check"
    ]

    def classify(self, query: str, context: List[Dict] = None) -> QueryComplexity:
        """classify query complexity"""
        query_lower = query.lower()

        # Check complexity metrics
        complex_score = sum(1 for ind in self.COMPLEX_INDICATORS if ind in query_lower)
        simple_score = sum(1 for ind in self.SIMPLE_INDICATORS if ind in query_lower)

        # Query length is also a metric
        if len(query) > 500:
            complex_score += 2
        elif len(query) < 50:
            simple_score += 1

        # Context length
        if context and len(context) > 10:
            complex_score += 1

        if complex_score > simple_score + 1:
            return QueryComplexity.COMPLEX
        elif simple_score > complex_score:
            return QueryComplexity.SIMPLE
        return QueryComplexity.MODERATE
```

### 5.2 Kubernetes-based Model Routing Service

```yaml
# Model Routing Service
apiVersion: apps/v1
kind: Deployment
metadata:
  name: model-router
  namespace: ai-agent
spec:
  replicas: 2
  selector:
    matchLabels:
      app: model-router
  template:
    metadata:
      labels:
        app: model-router
    spec:
      containers:
        - name: router
          image: registry.company.com/model-router:v1.0.0
          ports:
            - containerPort: 8080
          env:
            - name: OPENAI_API_KEY
              valueFrom:
                secretKeyRef:
                  name: openai-api
                  key: api-key
            - name: REDIS_URL
              value: "redis://redis:6379"
            - name: CACHE_TTL
              value: "3600"
            - name: SEMANTIC_CACHE_THRESHOLD
              value: "0.92"
          resources:
            requests:
              cpu: 250m
              memory: 512Mi
            limits:
              cpu: "1"
              memory: 2Gi
```

## 6. Cost Monitoring and Alerts

### 6.1 Cost Monitoring Dashboard

```yaml
# Grafana Dashboard
apiVersion: v1
kind: ConfigMap
metadata:
  name: llm-cost-dashboard
  namespace: monitoring
data:
  dashboard.json: |
    {
      "panels": [
        {
          "title": "Hourly LLM Cost",
          "targets": [{
            "expr": "sum(rate(llm_cost_usd_total[1h]))",
            "legendFormat": "Total Cost"
          }]
        },
        {
          "title": "Cache Hit Rate",
          "targets": [{
            "expr": "rate(llm_cache_hits_total[5m]) / rate(llm_requests_total[5m]) * 100",
            "legendFormat": "Hit Rate %"
          }]
        },
        {
          "title": "Model Usage Distribution",
          "targets": [{
            "expr": "sum by (model)(rate(llm_requests_total[5m]))",
            "legendFormat": "{{ model }}"
          }]
        },
        {
          "title": "Token Usage",
          "targets": [{
            "expr": "sum(rate(llm_input_tokens_total[5m]))",
            "legendFormat": "Input Tokens/s"
          }, {
            "expr": "sum(rate(llm_output_tokens_total[5m]))",
            "legendFormat": "Output Tokens/s"
          }]
        },
        {
          "title": "Daily Cost Trend",
          "targets": [{
            "expr": "sum(increase(llm_cost_usd_total[24h]))",
            "legendFormat": "Daily Cost"
          }]
        }
      ]
    }
```

### 6.2 Cost Alert Rules

```yaml
# Cost Alert Rules
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: llm-cost-alerts
  namespace: ai-agent
spec:
  groups:
    - name: llm-cost
      rules:
        - alert: DailyCostExceeded
          expr: |
            sum(increase(llm_cost_usd_total[24h])) > 1000
          for: 5m
          labels:
            severity: warning
          annotations:
            summary: "Daily LLM Cost Exceeds $1000"
            description: "Current daily cost: ${{ $value }}"

        - alert: HourlyCostSpike
          expr: |
            rate(llm_cost_usd_total[1h]) > rate(llm_cost_usd_total[1h] offset 24h) * 3
          for: 15m
          labels:
            severity: warning
          annotations:
            summary: "Hourly cost has increased three times compared to yesterday"

        - alert: CacheHitRateLow
          expr: |
            rate(llm_cache_hits_total[1h]) / rate(llm_requests_total[1h]) < 0.3
          for: 1h
          labels:
            severity: info
          annotations:
            summary: "Cache hit rate below 30%"
            description: "Current hit rate: {{ $value | humanizePercentage }}"

        - alert: ExpensiveModelUsageHigh
          expr: |
            rate(llm_requests_total{model=~"gpt-4.*"}[1h]) / rate(llm_requests_total[1h]) > 0.5
          for: 2h
          labels:
            severity: info
          annotations:
            summary: "Advanced model usage exceeds 50%"
            description: "Consider optimizing routing strategies to route more simple requests to small models"
```

## 7. Cost Optimization Report

```python
# Cost Optimization Report Generation
class CostOptimizationReport:
    """generate cost optimization report"""

    def __init__(self, tracker: TokenTracker, cache: HybridLLMCache):
        self.tracker = tracker
        self.cache = cache

    def generate(self, start_date: str, end_date: str) -> Dict:
        """generate cost report for a specified time period"""
        summary = self.tracker.get_daily_summary(start_date)
        cache_stats = self._get_cache_stats()

        # Calculate optimization effect
        total_requests = cache_stats["total_requests"]
        cache_hits = cache_stats["cache_hits"]
        cache_savings = cache_stats["estimated_savings"]

        # Calculate model routing savings
        routing_savings = self._calculate_routing_savings(start_date)

        return {
            "period": {"start": start_date, "end": end_date},
            "total_cost_usd": summary["total_cost_usd"],
            "total_tokens": {
                "input": summary["total_input_tokens"],
                "output": summary["total_output_tokens"]
            },
            "optimization": {
                "cache": {
                    "hit_rate": f"{cache_hits / max(total_requests, 1) * 100:.1f}%",
                    "savings_usd": cache_savings,
                    "savings_percentage": f"{cache_savings / max(summary['total_cost_usd'], 1) * 100:.1f}%"
                },
                "model_routing": {
                    "savings_usd": routing_savings["savings"],
                    "simple_queries_routed": routing_savings["simple_count"]
                },
                "total_savings_usd": cache_savings + routing_savings["savings"],
                "total_savings_percentage": f"{(cache_savings + routing_savings['savings']) / max(summary['total_cost_usd'] + cache_savings + routing_savings['savings'], 1) * 100:.1f}%"
            },
            "recommendations": self._generate_recommendations(summary, cache_stats)
        }

    def _get_cache_stats(self) -> Dict:
        return {
            "total_requests": 10000,
            "cache_hits": 4500,
            "estimated_savings": 450.0
        }

    def _calculate_routing_savings(self, date: str) -> Dict:
        return {
            "savings": 300.0,
            "simple_count": 6000
        }

    def _generate_recommendations(self, summary: Dict, cache_stats: Dict) -> list:
        """Generate optimization suggestions"""
        recommendations = []

        hit_rate = cache_stats["cache_hits"] / max(cache_stats["total_requests"], 1)
        if hit_rate < 0.3:
            recommendations.append("Cache hit rate is low, suggest checking caching strategy and similarity threshold")

        if summary["total_cost_usd"] > 500:
            recommendations.append("Daily cost is high, suggest increasing small model routing ratio")

        return recommendations
```

## 8. Best Practices

```
LLM cost optimization checklist:

Cache strategy:
  □ Precise caching is enabled
  □ Semantic cache threshold has been optimized
  □ Cache TTL settings are reasonable
  □ Cache hit rate monitoring

Token optimization:
  □ Prompt compression is enabled
  □ Context truncation strategy has been configured
  □ Token usage monitoring

Model routing:
  □ Complexity classifier has been trained
  □ Model mapping table has been configured
  □ Routing decision logs are complete

monitoring alerts:
  □ Cost Dashboard has been created
  □ Cost over-limit alert has been configured
  □ Cache hit rate alert
  □ Regular cost report generation
```

## Related

- [[domain-14-ai-ml-infra/02-ai-agents/51-agent-guardrails-content-safety|Agent Safety Barriers]]
- domain-14-ai-ml-infra/
- domain-06-observability/

## See Also

- OpenAI Pricing Document
- LLM Cache Best Practices
- Cost Optimization Strategies


<!-- risk-assessed -->
