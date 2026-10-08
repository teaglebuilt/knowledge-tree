---
title: Agent Resilience Design
description: 'Agent system retry strategies, circuit breakers, timeout control, idempotency, dead letter queues, and Chaos Testing'
summary: 'Agent system retry strategies, circuit breakers, timeout control, idempotency, dead letter queues, and Chaos Testing'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- resilience
- retry
- circuit-breaker
tier: supporting
created: '2026-07-02'
last_updated: 2026-07
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Platform Engineers
- SRE
estimated_read_time: 20min
intent_queries:
- What is Agent Resilience Design
- How to implement Agent retry strategies
- LLM API circuit breaker
- Agent idempotency guarantees
trigger_keywords:
- resilience
- retry
- circuit breaker
- timeout
- idempotency
- dead letter queue
- chaos testing
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/18-agent-retry-resilience.md
---
# Agent Resilience Design

## Overview

The reliability challenges of Agent systems differ from those of traditional microservices. LLM APIs have unique failure modes: 429 rate limiting, high latency fluctuations, non-deterministic outputs, and tool call timeouts. A single Agent execution chain may include 5–10 LLM calls and multiple tool calls, where a failure at any point affects the overall success rate.

This article covers retry strategies, circuit breakers, timeout control, idempotency, dead-letter queues, and chaos testing to build an end-to-end Agent resilience system.

## 1. Retry Strategies

### 1.1 Exponential Backoff + Jitter

LLM API 429 errors require backoff retries, but simple exponential backoff can cause a "thundering herd" effect. Adding Jitter randomization spreads out retry timing:

```python
import asyncio
import random
import time
from typing import Callable, Any, Optional
from dataclasses import dataclass

@dataclass
class RetryConfig:
    max_retries: int = 3
    base_delay: float = 1.0        # Base delay (seconds)
    max_delay: float = 60.0        # Maximum delay
    exponential_base: float = 2.0  # Exponential base
    jitter_range: float = 0.5      # Jitter range (0-1)

class LLMRetryError(Exception):
    """Final error after retries are exhausted"""
    def __init__(self, last_error: Exception, attempts: int):
        self.last_error = last_error
        self.attempts = attempts
        super().__init__(f"Failed after {attempts} attempts: {last_error}")


async def retry_with_backoff(
    func: Callable,
    config: RetryConfig = RetryConfig(),
    retryable_errors: tuple = (Exception,),
    on_retry: Optional[Callable] = None
) -> Any:
    """Exponential backoff + Jitter retry"""
    last_error = None

    for attempt in range(config.max_retries + 1):
        try:
            return await func()
        except retryable_errors as e:
            last_error = e

            if attempt == config.max_retries:
                break

            # Exponential backoff
            delay = min(
                config.base_delay * (config.exponential_base ** attempt),
                config.max_delay
            )

            # Jitter: full-range random
            jitter = delay * config.jitter_range * random.random()
            actual_delay = delay + jitter

            # Special handling for 429: use Retry-After header
            if hasattr(e, 'response') and e.response and e.response.status == 429:
                retry_after = e.response.headers.get('Retry-After')
                if retry_after:
                    actual_delay = max(actual_delay, float(retry_after))

            if on_retry:
                await on_retry(attempt + 1, actual_delay, e)

            await asyncio.sleep(actual_delay)

    raise LLMRetryError(last_error, config.max_retries + 1)
```

### 1.2 Retry Strategies for Different Error Types

```python
class SmartRetryStrategy:
    """Applies different retry strategies based on error type"""

    # Error classification and strategies
    ERROR_STRATEGIES = {
        # Rate limit errors: long backoff
        "rate_limit": {
            "retryable": True,
            "base_delay": 5.0,
            "max_retries": 5,
            "max_delay": 120.0,
        },
        # Server errors: standard backoff
        "server_error": {
            "retryable": True,
            "base_delay": 1.0,
            "max_retries": 3,
            "max_delay": 30.0,
        },
        # Timeouts: moderate backoff
        "timeout": {
            "retryable": True,
            "base_delay": 2.0,
            "max_retries": 2,
            "max_delay": 30.0,
        },
        # Context too long: no retry
        "context_length": {
            "retryable": False,
        },
        # Authentication failure: no retry
        "auth_error": {
            "retryable": False,
        },
        # Content filter: no retry
        "content_filter": {
            "retryable": False,
        },
    }

    @classmethod
    def classify_error(cls, error: Exception) -> str:
        """Classify the error type"""
        error_msg = str(error).lower()

        if hasattr(error, 'status_code'):
            status = error.status_code
            if status == 429:
                return "rate_limit"
            elif status >= 500:
                return "server_error"
            elif status == 401 or status == 403:
                return "auth_error"

        if "timeout" in error_msg or "timed out" in error_msg:
            return "timeout"
        elif "context_length" in error_msg or "too long" in error_msg:
            return "context_length"
        elif "content_filter" in error_msg or "safety" in error_msg:
            return "content_filter"

        return "server_error"  # Default classification

    @classmethod
    def get_retry_config(cls, error: Exception) -> RetryConfig:
        """Get retry configuration based on error type"""
        error_type = cls.classify_error(error)
        strategy = cls.ERROR_STRATEGIES[error_type]

        if not strategy["retryable"]:
            raise error  # Not retryable, raise immediately

        return RetryConfig(
            max_retries=strategy["max_retries"],
            base_delay=strategy["base_delay"],
            max_delay=strategy["max_delay"],
        )
```

### 1.3 Agent-Level Retry

Retrying after Agent reasoning failures requires special handling:

```python
class AgentRetryHandler:
    """Retry at the Agent reasoning level"""

    def __init__(self, llm_client, max_round_retries: int = 2):
        self.llm = llm_client
        self.max_round_retries = max_round_retries

    async def execute_with_retry(self, agent_config: dict, user_input: str) -> str:
        """Execute Agent with retry"""
        messages = [{"role": "user", "content": user_input}]

        for round_attempt in range(self.max_round_retries + 1):
            try:
                result = await self._run_agent_loop(agent_config, messages)
                return result
            except AgentLoopError as e:
                if round_attempt == self.max_round_retries:
                    raise

                # Inject error context on retry
                messages.append({
                    "role": "system",
                    "content": f"Previous reasoning round failed: {e.reason}. Please adjust your strategy and retry."
                })
                continue

    async def _run_agent_loop(self, config: dict, messages: list) -> str:
        """Execute the Agent reasoning loop"""
        for step in range(config.get("max_steps", 10)):
            response = await retry_with_backoff(
                lambda: self.llm.chat(messages, tools=config.get("tools")),
                config=RetryConfig(max_retries=2)
            )

            if response.tool_calls:
                # Execute tool calls
                tool_results = await self._execute_tools(response.tool_calls)
                messages.append(response)
                messages.extend(tool_results)
            else:
                return response.content

        raise AgentLoopError("Max steps exceeded")
```
## 2. Circuit Breaker

### 2.1 Circuit Breaker State Machine

```
┌──────────┐  consecutive failures ≥ threshold   ┌──────────┐  after timeout   ┌──────────┐
│  CLOSED  │ ──────────────────────────────────→ │   OPEN   │ ──────────────→ │HALF-OPEN │
│ (normal) │                                      │ (tripped)│                  │ (probing)│
└──────────┘                                      └──────────┘                  └──────────┘
     ↑                                                 │                             │
     │                                                 │ probe failed                │ probe succeeded
     │                                                 ▼                             │
     │                                            ┌──────────┐                      │
     └────────────────────────────────────────────│   OPEN   │←─────────────────────┘
                                                  └──────────┘
```

```python
import time
from enum import Enum
from dataclasses import dataclass, field

class CircuitState(Enum):
    CLOSED = "closed"         # Normal state, requests allowed
    OPEN = "open"             # Tripped state, requests rejected
    HALF_OPEN = "half_open"   # Probing state, limited requests allowed

@dataclass
class CircuitBreakerConfig:
    failure_threshold: int = 5       # Consecutive failure threshold
    recovery_timeout: float = 30.0   # Circuit recovery timeout (seconds)
    half_open_max_calls: int = 3     # Maximum probe calls in half-open state
    success_threshold: int = 2       # Consecutive success threshold in half-open state

class CircuitBreaker:
    """Circuit Breaker: protects unavailable Tools/Models"""

    def __init__(self, name: str, config: CircuitBreakerConfig = CircuitBreakerConfig()):
        self.name = name
        self.config = config
        self.state = CircuitState.CLOSED
        self.failure_count = 0
        self.success_count = 0
        self.last_failure_time = 0
        self.half_open_calls = 0

    async def call(self, func, *args, **kwargs):
        """Execute a call through the circuit breaker"""
        if self.state == CircuitState.OPEN:
            if time.time() - self.last_failure_time > self.config.recovery_timeout:
                self.state = CircuitState.HALF_OPEN
                self.half_open_calls = 0
                self.success_count = 0
            else:
                raise CircuitOpenError(
                    f"Circuit {self.name} is OPEN. "
                    f"Retry after {self.config.recovery_timeout}s"
                )

        if self.state == CircuitState.HALF_OPEN:
            if self.half_open_calls >= self.config.half_open_max_calls:
                raise CircuitOpenError(
                    f"Circuit {self.name} half-open limit reached"
                )
            self.half_open_calls += 1

        try:
            result = await func(*args, **kwargs)
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            raise

    def _on_success(self):
        """Success callback"""
        if self.state == CircuitState.HALF_OPEN:
            self.success_count += 1
            if self.success_count >= self.config.success_threshold:
                self.state = CircuitState.CLOSED
                self.failure_count = 0
        else:
            self.failure_count = 0

    def _on_failure(self):
        """Failure callback"""
        self.failure_count += 1
        self.last_failure_time = time.time()

        if self.state == CircuitState.HALF_OPEN:
            self.state = CircuitState.OPEN
        elif self.failure_count >= self.config.failure_threshold:
            self.state = CircuitState.OPEN

    def get_state(self) -> dict:
        return {
            "name": self.name,
            "state": self.state.value,
            "failure_count": self.failure_count,
            "last_failure": self.last_failure_time,
        }


class CircuitOpenError(Exception):
    """Circuit breaker open exception"""
    pass
```

### 2.2 Multi-Target Circuit Breaker Management

```python
class CircuitBreakerManager:
    """Manages multiple circuit breakers (one per Tool/Model)"""

    def __init__(self):
        self.breakers: dict[str, CircuitBreaker] = {}

    def get_breaker(self, target: str) -> CircuitBreaker:
        """Get the circuit breaker for a target"""
        if target not in self.breakers:
            self.breakers[target] = CircuitBreaker(target)
        return self.breakers[target]

    async def call(self, target: str, func, *args, **kwargs):
        """Call a target through its circuit breaker"""
        breaker = self.get_breaker(target)
        return await breaker.call(func, *args, **kwargs)

    def get_all_states(self) -> list[dict]:
        """Get the state of all circuit breakers"""
        return [b.get_state() for b in self.breakers.values()]

    def reset(self, target: str):
        """Reset the specified circuit breaker"""
        if target in self.breakers:
            self.breakers[target] = CircuitBreaker(target)


# Usage example
manager = CircuitBreakerManager()

# Tool calls through the circuit breaker
async def call_tool(tool_name: str, params: dict):
    return await manager.call(
        f"tool:{tool_name}",
        lambda: tool_registry.execute(tool_name, params)
    )

# Model calls through the circuit breaker
async def call_model(model_name: str, messages: list):
    return await manager.call(
        f"model:{model_name}",
        lambda: llm_client.chat(model=model_name, messages=messages)
    )
```

## 3. Timeout Control

### 3.1 Three-Level Timeout System

```python
import asyncio
from dataclasses import dataclass

@dataclass
class TimeoutConfig:
    step_timeout: float = 30.0       # Step timeout (single LLM/Tool call)
    round_timeout: float = 120.0     # Round timeout (one Agent reasoning loop)
    global_timeout: float = 300.0    # Global timeout (entire Agent execution)
    stream_timeout: float = 60.0     # Streaming first-token timeout

class TimeoutManager:
    """Agent Timeout Manager"""

    def __init__(self, config: TimeoutConfig = TimeoutConfig()):
        self.config = config

    async def execute_with_timeout(self, func, timeout_type: str = "step"):
        """Execute with timeout"""
        timeout_map = {
            "step": self.config.step_timeout,
            "round": self.config.round_timeout,
            "global": self.config.global_timeout,
            "stream": self.config.stream_timeout,
        }

        timeout = timeout_map.get(timeout_type, self.config.step_timeout)

        try:
            return await asyncio.wait_for(func(), timeout=timeout)
        except asyncio.TimeoutError:
            raise AgentTimeoutError(
                f"{timeout_type} timeout exceeded ({timeout}s)"
            )

    async def execute_agent(self, agent_func, user_input: str):
        """Agent execution with full timeout control"""
        async def _inner():
            return await agent_func(user_input)

        return await self.execute_with_timeout(_inner, "global")

    async def execute_step(self, step_func):
        """Single-step execution with timeout"""
        return await self.execute_with_timeout(step_func, "step")

    async def execute_streaming(self, stream_func):
        """Streaming execution with timeout"""
        async def _first_token():
            async for chunk in stream_func():
                yield chunk
                break  # Only check the first token

        return await self.execute_with_timeout(_first_token, "stream")


class AgentTimeoutError(Exception):
    """Agent timeout exception"""
    pass
```

### 3.2 Streaming Timeout

```python
class StreamingTimeoutHandler:
    """Timeout handling for streaming scenarios"""

    def __init__(
        self,
        first_token_timeout: float = 10.0,
        inter_token_timeout: float = 5.0
    ):
        self.first_token_timeout = first_token_timeout
        self.inter_token_timeout = inter_token_timeout

    async def stream_with_timeout(self, stream_gen):
        """Streaming consumption with timeout"""
        first_token = True
        last_token_time = time.monotonic()

        async for chunk in stream_gen:
            now = time.monotonic()

            if first_token:
                # First-token timeout check
                elapsed = now - last_token_time
                if elapsed > self.first_token_timeout:
                    raise StreamingTimeoutError(
                        f"First token timeout: {elapsed:.1f}s > {self.first_token_timeout}s"
                    )
                first_token = False
            else:
                # Inter-token timeout check
                elapsed = now - last_token_time
                if elapsed > self.inter_token_timeout:
                    raise StreamingTimeoutError(
                        f"Inter-token timeout: {elapsed:.1f}s > {self.inter_token_timeout}s"
                    )

            last_token_time = now
            yield chunk


class StreamingTimeoutError(Exception):
    pass
```
## 4. Idempotency Guarantees

### 4.1 Tool Call Deduplication

Agent retries may cause the same Tool to be called multiple times. Use idempotency keys to ensure the same call is only executed once:

```python
import hashlib
import json
from typing import Optional

class IdempotencyManager:
    """Idempotency management for Tool calls"""

    def __init__(self, redis_client, ttl: int = 3600):
        self.redis = redis_client
        self.ttl = ttl

    def generate_idempotency_key(
        self,
        agent_id: str,
        tool_name: str,
        parameters: dict
    ) -> str:
        """Generate an idempotency key"""
        content = json.dumps({
            "agent": agent_id,
            "tool": tool_name,
            "params": parameters
        }, sort_keys=True)
        return f"idempotent:{hashlib.sha256(content.encode()).hexdigest()}"

    async def execute_once(
        self,
        agent_id: str,
        tool_name: str,
        parameters: dict,
        tool_func
    ) -> dict:
        """Ensure the Tool is only executed once"""
        key = self.generate_idempotency_key(agent_id, tool_name, parameters)

        # Check if already executed
        cached = self.redis.get(key)
        if cached:
            return json.loads(cached)

        # Distributed lock to prevent concurrent duplicate execution
        lock_key = f"lock:{key}"
        lock = self.redis.lock(lock_key, timeout=30)

        if lock.acquire(blocking=True, blocking_timeout=5):
            try:
                # Double-check
                cached = self.redis.get(key)
                if cached:
                    return json.loads(cached)

                # Execute Tool
                result = await tool_func(parameters)

                # Cache result
                self.redis.setex(key, self.ttl, json.dumps(result))
                return result
            finally:
                lock.release()
        else:
            raise IdempotencyLockError(f"Failed to acquire lock for {tool_name}")

    def invalidate(self, agent_id: str, tool_name: str, parameters: dict):
        """Invalidate cache (for scenarios that require re-execution)"""
        key = self.generate_idempotency_key(agent_id, tool_name, parameters)
        self.redis.delete(key)


class IdempotencyLockError(Exception):
    pass
```

### 4.2 Agent Session Idempotency

```python
class AgentSessionIdempotency:
    """Session-level idempotency for Agents"""

    def __init__(self, redis_client):
        self.redis = redis_client

    def check_request_id(
        self,
        request_id: str,
        agent_id: str
    ) -> Optional[dict]:
        """Check whether the request has already been processed"""
        key = f"request:{agent_id}:{request_id}"
        result = self.redis.get(key)
        if result:
            return json.loads(result)
        return None

    def record_result(
        self,
        request_id: str,
        agent_id: str,
        result: dict,
        ttl: int = 86400
    ):
        """Record the request result"""
        key = f"request:{agent_id}:{request_id}"
        self.redis.setex(key, ttl, json.dumps(result))

    async def execute_idempotent(
        self,
        request_id: str,
        agent_id: str,
        agent_func
    ) -> dict:
        """Execute Agent idempotently"""
        # Check if already processed
        cached = self.check_request_id(request_id, agent_id)
        if cached:
            return cached

        # Execute and record
        result = await agent_func()
        self.record_result(request_id, agent_id, result)
        return result
```

## 5. Dead Letter Queue

### 5.1 Failed Task Handling

```python
import json
from datetime import datetime
from enum import Enum

class DLQStatus(Enum):
    PENDING = "pending"
    RETRYING = "retrying"
    RESOLVED = "resolved"
    ABANDONED = "abandoned"

class DeadLetterQueue:
    """Dead letter queue for failed Agent tasks"""

    def __init__(self, redis_client):
        self.redis = redis_client
        self.queue_key = "agent:dlq"

    def enqueue(
        self,
        agent_id: str,
        task_id: str,
        error: Exception,
        context: dict
    ):
        """Add a failed task to the dead letter queue"""
        entry = {
            "agent_id": agent_id,
            "task_id": task_id,
            "error": str(error),
            "error_type": type(error).__name__,
            "context": context,
            "enqueued_at": datetime.utcnow().isoformat(),
            "retry_count": 0,
            "status": DLQStatus.PENDING.value,
        }

        self.redis.lpush(self.queue_key, json.dumps(entry))

    def dequeue(self) -> Optional[dict]:
        """Pop one pending task"""
        data = self.redis.rpop(self.queue_key)
        if data:
            return json.loads(data)
        return None

    def get_pending(self, limit: int = 100) -> list[dict]:
        """Get the list of pending tasks"""
        items = self.redis.lrange(self.queue_key, 0, limit - 1)
        return [json.loads(item) for item in items]

    def retry_task(self, task_id: str, max_retries: int = 3) -> bool:
        """Retry a specific task"""
        items = self.redis.lrange(self.queue_key, 0, -1)

        for i, item_data in enumerate(items):
            item = json.loads(item_data)
            if item["task_id"] == task_id:
                if item["retry_count"] >= max_retries:
                    item["status"] = DLQStatus.ABANDONED.value
                    self.redis.lset(self.queue_key, i, json.dumps(item))
                    return False

                item["retry_count"] += 1
                item["status"] = DLQStatus.RETRYING.value
                item["last_retry_at"] = datetime.utcnow().isoformat()
                self.redis.lset(self.queue_key, i, json.dumps(item))
                return True

        return False

    def resolve_task(self, task_id: str):
        """Mark a task as resolved"""
        items = self.redis.lrange(self.queue_key, 0, -1)

        for i, item_data in enumerate(items):
            item = json.loads(item_data)
            if item["task_id"] == task_id:
                item["status"] = DLQStatus.RESOLVED.value
                item["resolved_at"] = datetime.utcnow().isoformat()
                self.redis.lset(self.queue_key, i, json.dumps(item))
                return

    def get_stats(self) -> dict:
        """Get DLQ statistics"""
        items = self.get_pending(limit=10000)
        stats = {"total": len(items), "by_status": {}, "by_agent": {}}

        for item in items:
            status = item.get("status", "unknown")
            agent = item.get("agent_id", "unknown")
            stats["by_status"][status] = stats["by_status"].get(status, 0) + 1
            stats["by_agent"][agent] = stats["by_agent"].get(agent, 0) + 1

        return stats
```
## 6. Chaos Testing for Agent

### 6.1 Fault Injection Framework

```python
import asyncio
import random
from typing import Callable, Optional
from enum import Enum

class ChaosType(Enum):
    LATENCY = "latency"           # Latency injection
    ERROR = "error"               # Error injection
    TIMEOUT = "timeout"           # Timeout injection
    RATE_LIMIT = "rate_limit"     # Rate limit injection
    PARTIAL_RESPONSE = "partial"  # Partial response
    SLOW_STREAM = "slow_stream"   # Slow streaming

class ChaosConfig:
    """Chaos testing configuration"""
    def __init__(
        self,
        chaos_type: ChaosType,
        probability: float = 0.1,  # 10% probability of triggering
        latency_ms: int = 5000,
        error_rate: float = 0.5
    ):
        self.chaos_type = chaos_type
        self.probability = probability
        self.latency_ms = latency_ms
        self.error_rate = error_rate

class ChaosAgent:
    """Agent chaos testing injector"""

    def __init__(self, configs: list[ChaosConfig]):
        self.configs = configs
        self.active = True

    async def inject_chaos(self, original_func: Callable, *args, **kwargs):
        """Inject chaos before invocation"""
        if not self.active:
            return await original_func(*args, **kwargs)

        for config in self.configs:
            if random.random() < config.probability:
                return await self._apply_chaos(config, original_func, *args, **kwargs)

        return await original_func(*args, **kwargs)

    async def _apply_chaos(
        self,
        config: ChaosConfig,
        original_func: Callable,
        *args,
        **kwargs
    ):
        """Apply chaos fault"""
        if config.chaos_type == ChaosType.LATENCY:
            delay = random.uniform(0, config.latency_ms / 1000)
            await asyncio.sleep(delay)
            return await original_func(*args, **kwargs)

        elif config.chaos_type == ChaosType.ERROR:
            raise ChaosInjectedError("Chaos: Injected LLM error")

        elif config.chaos_type == ChaosType.TIMEOUT:
            await asyncio.sleep(999)  # Trigger timeout
            raise asyncio.TimeoutError("Chaos: Injected timeout")

        elif config.chaos_type == ChaosType.RATE_LIMIT:
            raise ChaosRateLimitError("Chaos: Rate limited (429)")

        elif config.chaos_type == ChaosType.PARTIAL_RESPONSE:
            result = await original_func(*args, **kwargs)
            # Truncate response
            if isinstance(result, str):
                return result[:len(result)//2]
            return result

    def enable(self):
        self.active = True

    def disable(self):
        self.active = False


class ChaosInjectedError(Exception):
    pass

class ChaosRateLimitError(Exception):
    pass
```

### 6.2 Agent Chaos Test Suite

```python
class AgentChaosTestSuite:
    """Agent resilience test suite"""

    def __init__(self, agent_factory: Callable):
        self.agent_factory = agent_factory
        self.results: list[dict] = []

    async def test_retry_resilience(self):
        """Test retry resilience"""
        chaos = ChaosAgent([
            ChaosConfig(ChaosType.ERROR, probability=0.5),
        ])

        agent = self.agent_factory()
        success_count = 0
        total = 10

        for i in range(total):
            try:
                result = await chaos.inject_chaos(
                    lambda: agent.execute("test query")
                )
                success_count += 1
            except Exception:
                pass

        self.results.append({
            "test": "retry_resilience",
            "success_rate": success_count / total,
            "passed": success_count / total > 0.7,
        })

    async def test_circuit_breaker(self):
        """Test circuit breaker"""
        chaos = ChaosAgent([
            ChaosConfig(ChaosType.ERROR, probability=1.0),
        ])

        agent = self.agent_factory()
        open_detected = False

        for i in range(20):
            try:
                await chaos.inject_chaos(lambda: agent.execute("test"))
            except CircuitOpenError:
                open_detected = True
                break
            except Exception:
                pass

        self.results.append({
            "test": "circuit_breaker",
            "circuit_opened": open_detected,
            "passed": open_detected,
        })

    async def test_timeout_handling(self):
        """Test timeout handling"""
        chaos = ChaosAgent([
            ChaosConfig(ChaosType.LATENCY, probability=1.0, latency_ms=60000),
        ])

        agent = self.agent_factory()
        timeout_detected = False

        try:
            await asyncio.wait_for(
                chaos.inject_chaos(lambda: agent.execute("test")),
                timeout=5.0
            )
        except (asyncio.TimeoutError, AgentTimeoutError):
            timeout_detected = True

        self.results.append({
            "test": "timeout_handling",
            "timeout_detected": timeout_detected,
            "passed": timeout_detected,
        })

    async def test_graceful_degradation(self):
        """Test graceful degradation"""
        chaos = ChaosAgent([
            ChaosConfig(ChaosType.RATE_LIMIT, probability=0.8),
        ])

        agent = self.agent_factory()
        degraded_success = 0
        total = 10

        for i in range(total):
            try:
                result = await chaos.inject_chaos(
                    lambda: agent.execute("test", allow_degraded=True)
                )
                if result:
                    degraded_success += 1
            except Exception:
                pass

        self.results.append({
            "test": "graceful_degradation",
            "degraded_success_rate": degraded_success / total,
            "passed": degraded_success / total > 0.5,
        })

    def get_report(self) -> dict:
        """Generate test report"""
        total = len(self.results)
        passed = sum(1 for r in self.results if r.get("passed"))

        return {
            "total_tests": total,
            "passed": passed,
            "failed": total - passed,
            "pass_rate": passed / total if total > 0 else 0,
            "details": self.results,
        }
```

### 6.3 K8s Chaos Experiments

```yaml
# Litmus Chaos experiment: LLM API fault injection
apiVersion: litmuschaos.io/v1alpha1
kind: ChaosEngine
metadata:
  name: agent-chaos-engine
spec:
  appinfo:
    appns: agent-system
    applabel: app=agent-runtime
    appkind: deployment
  chaosServiceAccount: litmus-admin
  experiments:
    - name: pod-network-latency
      spec:
        components:
          env:
            - name: NETWORK_LATENCY
              value: "5000"   # 5-second delay
            - name: DESTINATION_PORTS
              value: "443"    # HTTPS port
        probe:
          - name: agent-success-rate-check
            type: httpProbe
            httpProbe/inputs:
              url: http://agent-service/health
              method:
                get:
                  criteria: "=="
                  responseCode: "200"
            mode: Continuous
            runProperties:
              probeTimeout: 5s
              interval: 10s

    - name: pod-delete
      spec:
        components:
          env:
            - name: TOTAL_CHAOS_DURATION
              value: "30"
            - name: CHAOS_INTERVAL
              value: "10"
        probe:
          - name: agent-recovery-check
            type: httpProbe
            httpProbe/inputs:
              url: http://agent-service/ready
              method:
                get:
                  criteria: "=="
                  responseCode: "200"
            mode: Edge
```
## Related Topics

- [[domain-14-ai-ml-infra/03-agent-runtime/17-agent-rate-limiting-cost-control|Agent Rate Limiting and Cost Control]]
- [[domain-14-ai-ml-infra/03-agent-runtime/19-agent-ci-cd-pipeline|Agent CI/CD Pipeline]]
- [[domain-14-ai-ml-infra/03-agent-runtime/21-agent-runtime-architecture-overview|Agent Runtime Architecture Overview]]

## References

- Exponential Backoff and Jitter
- Circuit Breaker Pattern
- Chaos Engineering Principles
- Litmus Chaos Documentation
