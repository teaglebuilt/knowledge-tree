---
title: Agent Rate Limiting and Cost Control
description: 'Token Bucket rate limiting, budget control, model routing, caching strategies, degradation, and cost alerting for Agent systems'
summary: 'Token Bucket rate limiting, budget control, model routing, caching strategies, degradation, and cost alerting for Agent systems'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- rate-limiting
- cost-control
- caching
tier: supporting
created: '2026-07-02'
last_updated: 2026-07
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Platform Engineers
- Architects
estimated_read_time: 20min
intent_queries:
- What is Agent Rate Limiting and Cost Control
- How to control LLM API costs
- Token Bucket rate limiting implementation
- Agent cost optimization strategies
trigger_keywords:
- rate limiting
- cost control
- token budget
- model routing
- semantic cache
- fallback
prerequisites:
- llm-basics
- kubernetes-basics
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/17-agent-rate-limiting-cost-control.md
---
# Agent Rate Limiting and Cost Control

## Overview

The cost of an Agent system primarily comes from LLM API calls. A single Agent inference may include multiple rounds of LLM calls (think → tool selection → result processing → final answer), and the Token consumption per request is far higher than traditional APIs. Rate limiting and cost control are necessary conditions for productionizing an Agent platform.

This article covers rate limiting algorithms, budget management, model routing, caching strategies, degradation plans, and real-time alerting.

## 1. Rate Limiting Algorithms

### 1.1 Token Bucket

Token Bucket is the most suitable rate limiting algorithm for LLM APIs, because it allows burst traffic while controlling the average rate.

```python
import time
import threading

class TokenBucketRateLimiter:
    """Token bucket rate limiter for LLM API calls"""

    def __init__(self, rate: float, capacity: int):
        """
        rate: number of tokens generated per second
        capacity: bucket capacity (maximum burst size)
        """
        self.rate = rate
        self.capacity = capacity
        self.tokens = capacity
        self.last_refill = time.monotonic()
        self.lock = threading.Lock()

    def acquire(self, tokens: int = 1) -> bool:
        """Try to acquire tokens, non-blocking"""
        with self.lock:
            now = time.monotonic()
            elapsed = now - self.last_refill
            self.tokens = min(
                self.capacity,
                self.tokens + elapsed * self.rate
            )
            self.last_refill = now

            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

    def wait_and_acquire(self, tokens: int = 1, timeout: float = 30.0) -> bool:
        """Wait to acquire tokens, with timeout"""
        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            if self.acquire(tokens):
                return True
            time.sleep(0.1)
        return False


class MultiDimensionRateLimiter:
    """Multi-dimensional rate limiting: by user / Agent / global"""

    def __init__(self):
        # Global rate limit: 1000 RPM
        self.global_limiter = TokenBucketRateLimiter(
            rate=1000/60, capacity=100
        )
        # Per-user rate limit: 60 RPM/user
        self.user_limiters: dict[str, TokenBucketRateLimiter] = {}
        # Per-Agent rate limit: 200 RPM/Agent
        self.agent_limiters: dict[str, TokenBucketRateLimiter] = {}

    def check(self, user_id: str, agent_id: str) -> tuple[bool, str]:
        """Check whether a request is allowed"""
        # Global check
        if not self.global_limiter.acquire():
            return False, "global_rate_limit"

        # User-level check
        user_limiter = self._get_user_limiter(user_id)
        if not user_limiter.acquire():
            return False, f"user_rate_limit:{user_id}"

        # Agent-level check
        agent_limiter = self._get_agent_limiter(agent_id)
        if not agent_limiter.acquire():
            return False, f"agent_rate_limit:{agent_id}"

        return True, "ok"

    def _get_user_limiter(self, user_id: str) -> TokenBucketRateLimiter:
        if user_id not in self.user_limiters:
            self.user_limiters[user_id] = TokenBucketRateLimiter(
                rate=60/60, capacity=10
            )
        return self.user_limiters[user_id]

    def _get_agent_limiter(self, agent_id: str) -> TokenBucketRateLimiter:
        if agent_id not in self.agent_limiters:
            self.agent_limiters[agent_id] = TokenBucketRateLimiter(
                rate=200/60, capacity=30
            )
        return self.agent_limiters[agent_id]
```

### 1.2 Sliding Window

Sliding window provides more precise rate limiting control:

```python
import time
from collections import deque

class SlidingWindowRateLimiter:
    """Sliding window rate limiter for precise control of request count within a time window"""

    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests: deque[float] = deque()
        self.lock = threading.Lock()

    def is_allowed(self) -> bool:
        with self.lock:
            now = time.monotonic()
            window_start = now - self.window_seconds

            # Remove expired requests
            while self.requests and self.requests[0] < window_start:
                self.requests.popleft()

            if len(self.requests) < self.max_requests:
                self.requests.append(now)
                return True
            return False

    def retry_after(self) -> float:
        """Return the number of seconds to wait"""
        with self.lock:
            if not self.requests:
                return 0
            oldest = self.requests[0]
            return max(0, self.window_seconds - (time.monotonic() - oldest))


class TokenBasedSlidingWindow:
    """Sliding window rate limiting based on Token count"""

    def __init__(self, max_tokens: int, window_seconds: int):
        self.max_tokens = max_tokens
        self.window_seconds = window_seconds
        self.usage: deque[tuple[float, int]] = deque()  # (timestamp, tokens)
        self.lock = threading.Lock()

    def check_and_record(self, estimated_tokens: int) -> bool:
        """Check Token budget and record usage"""
        with self.lock:
            now = time.monotonic()
            window_start = now - self.window_seconds

            # Clean up expired records
            while self.usage and self.usage[0][0] < window_start:
                self.usage.popleft()

            # Calculate total Tokens within the window
            total = sum(t for _, t in self.usage)

            if total + estimated_tokens <= self.max_tokens:
                self.usage.append((now, estimated_tokens))
                return True
            return False
```

### 1.3 Distributed Rate Limiting

In a multi-replica Kubernetes deployment, distributed rate limiting is required:

```python
import redis
import time

class RedisRateLimiter:
    """Redis-based distributed rate limiter"""

    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client

    def token_bucket_acquire(
        self,
        key: str,
        rate: float,
        capacity: int,
        tokens: int = 1
    ) -> bool:
        """Atomic token bucket implemented with a Lua script"""
        lua_script = """
        local key = KEYS[1]
        local rate = tonumber(ARGV[1])
        local capacity = tonumber(ARGV[2])
        local tokens = tonumber(ARGV[3])
        local now = tonumber(ARGV[4])

        local bucket = redis.call('HMGET', key, 'tokens', 'last_refill')
        local current_tokens = tonumber(bucket[1]) or capacity
        local last_refill = tonumber(bucket[2]) or now

        local elapsed = now - last_refill
        current_tokens = math.min(capacity, current_tokens + elapsed * rate)

        local allowed = 0
        if current_tokens >= tokens then
            current_tokens = current_tokens - tokens
            allowed = 1
        end

        redis.call('HMSET', key, 'tokens', current_tokens, 'last_refill', now)
        redis.call('EXPIRE', key, math.ceil(capacity / rate) + 1)

        return allowed
        """

        result = self.redis.eval(
            lua_script,
            1,
            key,
            str(rate),
            str(capacity),
            str(tokens),
            str(time.time())
        )
        return bool(result)
```
## 2. Budget Control

### 2.1 Three-Tier Budget System

```python
from dataclasses import dataclass
from datetime import datetime, date

@dataclass
class BudgetConfig:
    daily_limit_usd: float
    monthly_limit_usd: float
    per_request_limit_usd: float
    alert_threshold_pct: float  # Alert threshold percentage

class BudgetManager:
    """Three-tier budget management: User / Agent / Global"""

    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client

    def check_budget(
        self,
        user_id: str,
        agent_id: str,
        estimated_cost_usd: float
    ) -> tuple[bool, str]:
        """Check whether the budget is sufficient"""

        # 1. Per-request budget
        per_request_limit = 0.50  # $0.50 per request
        if estimated_cost_usd > per_request_limit:
            return False, f"per_request_exceeded:{estimated_cost_usd:.4f}>{per_request_limit}"

        # 2. User daily budget
        user_daily = self._get_usage(f"user:{user_id}:daily")
        user_daily_limit = 10.0  # $10/day/user
        if user_daily + estimated_cost_usd > user_daily_limit:
            return False, f"user_daily_exceeded:{user_daily:.4f}+{estimated_cost_usd:.4f}>{user_daily_limit}"

        # 3. Agent daily budget
        agent_daily = self._get_usage(f"agent:{agent_id}:daily")
        agent_daily_limit = 100.0  # $100/day/Agent
        if agent_daily + estimated_cost_usd > agent_daily_limit:
            return False, f"agent_daily_exceeded:{agent_daily:.4f}+{estimated_cost_usd:.4f}>{agent_daily_limit}"

        # 4. Global monthly budget
        global_monthly = self._get_usage("global:monthly")
        global_monthly_limit = 10000.0  # $10,000/month
        if global_monthly + estimated_cost_usd > global_monthly_limit:
            return False, f"global_monthly_exceeded:{global_monthly:.4f}+{estimated_cost_usd:.4f}>{global_monthly_limit}"

        return True, "ok"

    def record_usage(
        self,
        user_id: str,
        agent_id: str,
        actual_cost_usd: float
    ):
        """Record actual consumption"""
        pipe = self.redis.pipeline()
        today = date.today().isoformat()
        month = today[:7]

        pipe.incrbyfloat(f"user:{user_id}:daily:{today}", actual_cost_usd)
        pipe.expire(f"user:{user_id}:daily:{today}", 86400 * 2)

        pipe.incrbyfloat(f"agent:{agent_id}:daily:{today}", actual_cost_usd)
        pipe.expire(f"agent:{agent_id}:daily:{today}", 86400 * 2)

        pipe.incrbyfloat(f"global:monthly:{month}", actual_cost_usd)
        pipe.expire(f"global:monthly:{month}", 86400 * 35)

        pipe.execute()

    def _get_usage(self, key_pattern: str) -> float:
        today = date.today().isoformat()
        month = today[:7]

        if "daily" in key_pattern:
            key = f"{key_pattern}:{today}"
        elif "monthly" in key_pattern:
            key = f"{key_pattern}:{month}"
        else:
            key = key_pattern

        value = self.redis.get(key)
        return float(value) if value else 0.0

    def get_usage_report(self, user_id: str) -> dict:
        """Get user usage report"""
        today = date.today().isoformat()
        month = today[:7]

        return {
            "user_daily": self._get_usage(f"user:{user_id}:daily:{today}"),
            "user_monthly": self._get_usage(f"user:{user_id}:monthly:{month}"),
            "global_monthly": self._get_usage(f"global:monthly:{month}"),
        }
```

### 2.2 Token Budget Estimation

```python
class TokenCostEstimator:
    """Token cost estimator"""

    # Q2 2026 pricing (USD per 1M tokens)
    MODEL_PRICING = {
        "gpt-4o": {"input": 2.50, "output": 10.00},
        "gpt-4o-mini": {"input": 0.15, "output": 0.60},
        "claude-sonnet": {"input": 3.00, "output": 15.00},
        "claude-haiku": {"input": 0.25, "output": 1.25},
        "gemini-1.5-pro": {"input": 1.25, "output": 5.00},
        "gemini-1.5-flash": {"input": 0.075, "output": 0.30},
        "qwen-max": {"input": 0.12, "output": 0.12},  # ¥0.12 per thousand tokens
        "deepseek-v3": {"input": 0.14, "output": 0.28},
    }

    @classmethod
    def estimate_cost(
        cls,
        model: str,
        input_tokens: int,
        output_tokens: int
    ) -> float:
        """Estimate the cost of a single call (USD)"""
        pricing = cls.MODEL_PRICING.get(model)
        if not pricing:
            raise ValueError(f"Unknown model: {model}")

        input_cost = (input_tokens / 1_000_000) * pricing["input"]
        output_cost = (output_tokens / 1_000_000) * pricing["output"]
        return input_cost + output_cost

    @classmethod
    def estimate_agent_cost(
        cls,
        model: str,
        num_tool_calls: int = 2,
        avg_input_per_step: int = 2000,
        avg_output_per_step: int = 500
    ) -> float:
        """Estimate the total cost of a single Agent request"""
        # Agent reasoning steps: thinking + tool calls + result processing + final answer
        total_steps = 1 + num_tool_calls * 2 + 1  # thinking + (call + process)*N + answer
        total_input = total_steps * avg_input_per_step
        total_output = total_steps * avg_output_per_step
        return cls.estimate_cost(model, total_input, total_output)
```

## 3. Model Routing

### 3.1 Intelligent Routing Strategy

Select the appropriate model based on request complexity; use smaller models for simple questions to reduce costs:

```python
from enum import Enum
from typing import Optional

class ComplexityLevel(Enum):
    SIMPLE = "simple"       # Simple Q&A
    MODERATE = "moderate"   # Moderate complexity
    COMPLEX = "complex"     # Complex reasoning
    CRITICAL = "critical"   # Critical tasks

class ModelRouter:
    """Intelligent model router"""

    # Routing strategy configuration
    ROUTING_TABLE = {
        ComplexityLevel.SIMPLE: {
            "primary": "gpt-4o-mini",
            "fallback": "claude-haiku",
            "cost_weight": 0.9,  # Prioritize cost
        },
        ComplexityLevel.MODERATE: {
            "primary": "claude-sonnet",
            "fallback": "gpt-4o",
            "cost_weight": 0.5,
        },
        ComplexityLevel.COMPLEX: {
            "primary": "gpt-4o",
            "fallback": "claude-sonnet",
            "cost_weight": 0.2,
        },
        ComplexityLevel.CRITICAL: {
            "primary": "gpt-4o",
            "fallback": "claude-sonnet",
            "cost_weight": 0.0,  # Ignore cost
        },
    }

    def route(
        self,
        query: str,
        context: Optional[dict] = None
    ) -> tuple[str, ComplexityLevel]:
        """Route the request to the appropriate model"""
        complexity = self._classify_complexity(query, context)
        config = self.ROUTING_TABLE[complexity]

        # Check primary model availability
        if self._is_model_available(config["primary"]):
            return config["primary"], complexity

        # Use fallback
        return config["fallback"], complexity

    def _classify_complexity(
        self,
        query: str,
        context: Optional[dict]
    ) -> ComplexityLevel:
        """Rule-based + statistical complexity classification"""
        # Rule matching
        simple_patterns = [
            "Hello", "Thank you", "Yes", "Okay",
            "what is", "how to", "define"
        ]
        complex_patterns = [
            "Analyze", "Compare", "Reason", "Design",
            "analyze", "compare", "reason", "design",
            "Multi-step", "Optimize", "debug"
        ]

        query_lower = query.lower()

        # Simple pattern matching
        if len(query) < 20 and any(p in query_lower for p in simple_patterns):
            return ComplexityLevel.SIMPLE

        # Complex pattern matching
        if any(p in query_lower for p in complex_patterns):
            return ComplexityLevel.COMPLEX

        # Context-based judgment
        if context and context.get("requires_tools"):
            return ComplexityLevel.COMPLEX

        # Length-based judgment
        if len(query) > 500:
            return ComplexityLevel.MODERATE

        return ComplexityLevel.SIMPLE

    def _is_model_available(self, model: str) -> bool:
        """Check whether the model is available"""
        # In actual implementation, check model health status
        return True
```

### 3.2 Cost-Optimized Routing

```python
class CostOptimizedRouter(ModelRouter):
    """Cost-optimized router"""

    def __init__(self, daily_budget_remaining: float):
        self.budget_remaining = daily_budget_remaining

    def route(self, query: str, context: Optional[dict] = None) -> tuple[str, ComplexityLevel]:
        """Budget-aware routing"""
        model, complexity = super().route(query, context)

        # Downgrade model when budget is tight
        if self.budget_remaining < 1.0:  # Remaining < $1
            if complexity in (ComplexityLevel.SIMPLE, ComplexityLevel.MODERATE):
                return "gpt-4o-mini", complexity  # Force use of smaller model
            elif complexity == ComplexityLevel.COMPLEX:
                return "claude-sonnet", complexity  # Downgrade but maintain quality

        # Use optimal model when budget is sufficient
        return model, complexity

    def update_budget(self, cost: float):
        self.budget_remaining -= cost
```
## 4. Caching Strategies

### 4.1 Exact Cache

```python
import hashlib
import json
from typing import Optional

class ExactCache:
    """Exact cache: returns cached result for identical inputs"""

    def __init__(self, redis_client: redis.Redis, ttl: int = 3600):
        self.redis = redis_client
        self.ttl = ttl

    def get_cache_key(self, agent_id: str, model: str, messages: list) -> str:
        """Generate cache key"""
        content = json.dumps({
            "agent": agent_id,
            "model": model,
            "messages": messages
        }, sort_keys=True)
        return f"llm_cache:{hashlib.sha256(content.encode()).hexdigest()}"

    def get(
        self,
        agent_id: str,
        model: str,
        messages: list
    ) -> Optional[str]:
        """Query cache"""
        key = self.get_cache_key(agent_id, model, messages)
        result = self.redis.get(key)
        return result.decode() if result else None

    def set(
        self,
        agent_id: str,
        model: str,
        messages: list,
        response: str
    ):
        """Write to cache"""
        key = self.get_cache_key(agent_id, model, messages)
        self.redis.setex(key, self.ttl, response)
```

### 4.2 Semantic Cache

```python
import numpy as np
from typing import Optional

class SemanticCache:
    """Semantic cache: returns cached result for semantically similar inputs"""

    def __init__(
        self,
        redis_client: redis.Redis,
        embedding_func,
        similarity_threshold: float = 0.92,
        ttl: int = 3600
    ):
        self.redis = redis_client
        self.embedding_func = embedding_func
        self.threshold = similarity_threshold
        self.ttl = ttl

    def get(
        self,
        agent_id: str,
        query: str
    ) -> Optional[tuple[str, float]]:
        """Semantic similarity retrieval"""
        query_embedding = self.embedding_func(query)

        # Retrieve all cached embeddings for this agent from Redis
        pattern = f"semantic_cache:{agent_id}:*"
        keys = self.redis.keys(pattern)

        best_match = None
        best_similarity = 0.0

        for key in keys:
            cached = self.redis.hgetall(key)
            cached_embedding = np.frombuffer(cached[b"embedding"], dtype=np.float32)

            # Cosine similarity
            similarity = np.dot(query_embedding, cached_embedding) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(cached_embedding)
            )

            if similarity > best_similarity and similarity >= self.threshold:
                best_similarity = similarity
                best_match = cached[b"response"].decode()

        if best_match:
            return best_match, best_similarity
        return None

    def set(
        self,
        agent_id: str,
        query: str,
        response: str
    ):
        """Write to semantic cache"""
        embedding = self.embedding_func(query)
        cache_id = hashlib.sha256(query.encode()).hexdigest()[:16]
        key = f"semantic_cache:{agent_id}:{cache_id}"

        self.redis.hset(key, mapping={
            "query": query,
            "response": response,
            "embedding": embedding.astype(np.float32).tobytes()
        })
        self.redis.expire(key, self.ttl)
```

### 4.3 Cache Strategy Selection

```
Cache Strategy Decision:

Exact Cache:
  Use case: FAQs, templated replies, fixed queries
  Hit rate: Low (5–15%)
  Accuracy: 100%
  Implementation complexity: Low

Semantic Cache:
  Use case: Customer service, knowledge Q&A, open-domain dialogue
  Hit rate: Medium (20–40%)
  Accuracy: 92%+ (depends on threshold)
  Implementation complexity: Medium

Hybrid Cache (recommended):
  Strategy: Exact first → Semantic second → LLM last
  Hit rate: High (30–50%)
  Accuracy: High
  Implementation complexity: Medium

Scenarios where caching is not recommended:
  - Real-time data queries (stocks, weather)
  - Personalized responses (require uniqueness)
  - Long-context conversations (context changes significantly)
  - Streaming output (caching offers little value)
```

## 5. Fallback Strategies

### 5.1 Fallback Model Chain

```python
class FallbackChain:
    """Model fallback chain"""

    def __init__(self):
        self.chain = [
            {"model": "gpt-4o", "timeout": 30, "retries": 2},
            {"model": "claude-sonnet", "timeout": 25, "retries": 2},
            {"model": "gpt-4o-mini", "timeout": 20, "retries": 3},
            {"model": "deepseek-v3", "timeout": 15, "retries": 3},
        ]

    async def execute(self, messages: list, **kwargs) -> str:
        """Execute along the fallback chain; return as soon as one succeeds"""
        errors = []

        for config in self.chain:
            try:
                result = await self._call_model(
                    model=config["model"],
                    messages=messages,
                    timeout=config["timeout"],
                    retries=config["retries"],
                    **kwargs
                )
                return result
            except Exception as e:
                errors.append({
                    "model": config["model"],
                    "error": str(e)
                })
                continue

        # All models failed
        raise AllModelsFailedError(errors)

    async def _call_model(self, model: str, messages: list, timeout: int, retries: int, **kwargs):
        """Call a single model"""
        for attempt in range(retries):
            try:
                # Actual API call
                pass
            except Exception as e:
                if attempt < retries - 1:
                    await asyncio.sleep(2 ** attempt)
                else:
                    raise
```

### 5.2 Fallback Trigger Conditions

```yaml
Fallback trigger conditions:

Model unavailable:
  - HTTP 429 (Rate Limited)
  - HTTP 500/502/503 (Server Error)
  - Timeout (30s)
  - 3 consecutive failures

Cost limit exceeded:
  - Estimated cost per request > $1
  - Daily budget remaining < 10%
  - Monthly budget remaining < 5%

Quality degradation:
  - Model output blocked by safety filter
  - Output format does not match expectations
  - Confidence too low
```
## 6. Real-Time Cost Alerting

### 6.1 Alert Rules

```python
from dataclasses import dataclass
from enum import Enum

class AlertLevel(Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"

@dataclass
class AlertRule:
    name: str
    level: AlertLevel
    condition: str  # "daily_cost > threshold"
    threshold: float
    window: str     # "1h", "1d", "1m"
    cooldown: int   # alert cooldown in seconds

class CostAlertManager:
    """Cost alert manager"""

    DEFAULT_RULES = [
        AlertRule(
            name="daily_budget_80pct",
            level=AlertLevel.WARNING,
            condition="daily_usage_pct > 80",
            threshold=0.8,
            window="1d",
            cooldown=3600
        ),
        AlertRule(
            name="daily_budget_95pct",
            level=AlertLevel.CRITICAL,
            condition="daily_usage_pct > 95",
            threshold=0.95,
            window="1d",
            cooldown=1800
        ),
        AlertRule(
            name="single_request_high_cost",
            level=AlertLevel.WARNING,
            condition="request_cost > 0.5",
            threshold=0.5,
            window="per_request",
            cooldown=0
        ),
        AlertRule(
            name="hourly_spike",
            level=AlertLevel.WARNING,
            condition="hourly_cost > avg_hourly * 3",
            threshold=3.0,
            window="1h",
            cooldown=3600
        ),
    ]

    def __init__(self, budget_manager: BudgetManager):
        self.budget_manager = budget_manager
        self.rules = self.DEFAULT_RULES
        self.last_alert_time: dict[str, float] = {}

    def check_alerts(self, agent_id: str) -> list[dict]:
        """Check whether alerts need to be triggered"""
        alerts = []
        usage = self.budget_manager.get_usage_report(agent_id)

        for rule in self.rules:
            if self._should_alert(rule, usage):
                alert = self._create_alert(rule, usage)
                alerts.append(alert)
                self.last_alert_time[rule.name] = time.time()

        return alerts

    def _should_alert(self, rule: AlertRule, usage: dict) -> bool:
        """Check whether an alert should be triggered"""
        # Cooldown check
        last_time = self.last_alert_time.get(rule.name, 0)
        if time.time() - last_time < rule.cooldown:
            return False

        # Condition check
        if rule.name == "daily_budget_80pct":
            return usage.get("daily_usage_pct", 0) > rule.threshold
        elif rule.name == "single_request_high_cost":
            return usage.get("last_request_cost", 0) > rule.threshold

        return False

    def _create_alert(self, rule: AlertRule, usage: dict) -> dict:
        return {
            "rule": rule.name,
            "level": rule.level.value,
            "message": f"[{rule.level.value.upper()}] {rule.condition}",
            "usage": usage,
            "timestamp": time.time()
        }
```

### 6.2 Alert Integration

```yaml
# Prometheus alert rules
groups:
  - name: agent_cost_alerts
    rules:
      - alert: AgentDailyBudgetHigh
        expr: agent_daily_cost_usd / agent_daily_budget_usd > 0.8
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Agent {{ $labels.agent_id }} daily budget usage exceeds 80%"

      - alert: AgentDailyBudgetCritical
        expr: agent_daily_cost_usd / agent_daily_budget_usd > 0.95
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Agent {{ $labels.agent_id }} daily budget usage exceeds 95%"

      - alert: AgentRequestCostHigh
        expr: agent_request_cost_usd > 0.5
        labels:
          severity: warning
        annotations:
          summary: "Agent {{ $labels.agent_id }} single request cost is too high"

# Grafana Dashboard key metrics
metrics:
  - agent_daily_cost_usd          # daily cost
  - agent_monthly_cost_usd        # monthly cost
  - agent_request_cost_usd        # per-request cost
  - agent_cache_hit_rate          # cache hit rate
  - agent_fallback_rate           # fallback rate
  - agent_rate_limit_hit_rate     # rate limit hit rate
```

## 7. K8s Deployment Configuration

```yaml
# Agent rate limiting and cost control component deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: agent-cost-controller
spec:
  replicas: 2
  selector:
    matchLabels:
      app: cost-controller
  template:
    metadata:
      labels:
        app: cost-controller
    spec:
      containers:
      - name: controller
        image: agent-cost-controller:latest
        env:
        - name: REDIS_URL
          value: "redis://redis:6379"
        - name: DAILY_GLOBAL_BUDGET
          value: "10000"  # $10,000/day
        - name: ALERT_WEBHOOK_URL
          valueFrom:
            secretKeyRef:
              name: alert-config
              key: webhook-url
        resources:
          requests:
            cpu: "250m"
            memory: "256Mi"
          limits:
            cpu: "1"
            memory: "1Gi"
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: rate-limit-config
data:
  config.yaml: |
    global:
      requests_per_minute: 1000
      tokens_per_minute: 1000000
    per_user:
      requests_per_minute: 60
      tokens_per_minute: 100000
    per_agent:
      requests_per_minute: 200
      tokens_per_minute: 500000
```

## Related Topics

- [[domain-14-ai-ml-infra/03-agent-runtime/18-agent-retry-resilience|Agent Resilience Design]]
- [[domain-14-ai-ml-infra/03-agent-runtime/15-cloud-agent-platforms|Cloud Agent Platform as a Service]]
- [[domain-14-ai-ml-infra/03-agent-runtime/21-agent-runtime-architecture-overview|Agent Runtime Architecture Overview]]
## References

- Token Bucket Algorithm
- Redis Distributed Rate Limiting
- LLM API Pricing Comparison
