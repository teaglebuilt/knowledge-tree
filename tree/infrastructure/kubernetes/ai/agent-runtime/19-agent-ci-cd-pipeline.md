---
title: Agent CI/CD Pipeline
description: 'Agent as Code, Prompt Version Management, Automated Testing, Progressive Deployment and Rollback Strategies'
summary: 'Agent as Code, Prompt Version Management, Automated Testing, Progressive Deployment and Rollback Strategies'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- ci-cd
- testing
- deployment
tier: supporting
created: '2026-07-02'
last_updated: 2026-07
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- DevOps Engineers
- Platform Engineers
estimated_read_time: 20min
intent_queries:
- What is an Agent CI/CD Pipeline
- How to implement continuous deployment for Agents
- Prompt version management
- Agent automated testing
trigger_keywords:
- agent ci cd
- prompt versioning
- agent testing
- canary deployment
- rollback
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/19-agent-ci-cd-pipeline.md
---
> **Production Environment Safety Notice**
>
> This document contains operational commands that can be executed directly. Before execution, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether validation has been performed in a non-production environment. Command risk levels are annotated as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state, but generally reversible), 🟢 Low risk / read-only (information gathering, no side effects).


# Agent CI/CD Pipeline

## Overview

Agent CI/CD differs from traditional software: an Agent's behavior is jointly determined by Prompts, tool configurations, and model parameters — changes to this "code" cannot be verified by a traditional compiler. Minor modifications to a Prompt can cause dramatic shifts in Agent behavior, and the non-deterministic nature of LLMs makes regression testing especially critical.

This document covers the Agent as Code philosophy, Prompt version management, three-layer automated testing, progressive deployment, and Rollback strategies.

## 1. Agent as Code

### 1.1 Agent Configuration Versioning

Manage all Agent configurations — Prompts, tool definitions, model parameters, knowledge base bindings — as code:

```yaml
# agent-config.yaml - Complete Agent configuration
apiVersion: agent/v1
kind: AgentConfig
metadata:
  name: customer-service-agent
  version: "2.3.1"
  labels:
    team: platform
    env: production

spec:
  # Model configuration
  model:
    primary: gpt-4o
    fallback: claude-sonnet
    parameters:
      temperature: 0.7
      max_tokens: 4096
      top_p: 0.9

  # System prompt
  system_prompt: |
    You are the customer service assistant for {{company_name}}.
    Rules:
    1. Answer questions in a friendly and professional tone
    2. For questions you cannot answer, transfer to a human agent
    3. Do not disclose internal system information
    4. Cite the source when referencing knowledge base content

  # Tool definitions
  tools:
    - name: search_products
      description: Search the product catalog
      schema:
        type: object
        properties:
          keyword:
            type: string
          category:
            type: string
      implementation:
        type: http
        endpoint: https://api.internal/products/search
        method: GET
        timeout: 5s

    - name: create_ticket
      description: Create a support ticket
      schema:
        type: object
        properties:
          title:
            type: string
          description:
            type: string
          priority:
            type: string
            enum: [low, medium, high]
      implementation:
        type: http
        endpoint: https://api.internal/tickets
        method: POST
        timeout: 10s

  # Knowledge bases
  knowledge_bases:
    - id: product-docs
      retrieval:
        top_k: 5
        similarity_threshold: 0.7
        rerank: true

  # Safety policy
  safety:
    content_filter: true
    max_tool_calls_per_turn: 5
    allowed_domains:
      - "*.internal.com"
    blocked_patterns:
      - "密码|password|secret"

  # Deployment strategy
  deployment:
    strategy: canary
    canary_percentage: 10
    health_check:
      endpoint: /health
      interval: 30s
      timeout: 5s
```

### 1.2 GitOps Workflow

```
┌─────────────────────────────────────────────────────────┐
│                 Agent GitOps Pipeline                    │
│                                                          │
│  ┌──────┐    ┌──────────┐    ┌──────────┐    ┌───────┐│
│  │ Git  │───→│  CI Build │───→│  Test    │───→│Deploy ││
│  │ Push │    │          │    │          │    │       ││
│  └──────┘    │ - Lint   │    │ - Unit   │    │ Canary││
│              │ - Valid  │    │ - Integ  │    │ Blue/ ││
│              │ - Diff   │    │ - E2E    │    │ Green ││
│              └──────────┘    └──────────┘    └───────┘│
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │  ArgoCD / Flux → K8s Agent Runtime               │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

```yaml
# GitHub Actions: Agent CI/CD Pipeline
name: Agent CI/CD

on:
  push:
    paths:
      - 'agents/**'
      - 'prompts/**'
  pull_request:
    paths:
      - 'agents/**'

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Lint Agent Config
        run: |
          # YAML Schema validation
          ajv validate -s agent-schema.json -d agents/*.yaml
          # Prompt quality check
          python scripts/lint_prompts.py agents/

      - name: Diff Analysis
        run: |
          # Analyze change impact
          python scripts/diff_analysis.py \
            --base main \
            --head ${{ github.sha }} \
            --output impact-report.json

  test:
    needs: validate
    runs-on: ubuntu-latest
    strategy:
      matrix:
        test-suite: [unit, integration, regression]
    steps:
      - name: Run ${{ matrix.test-suite }} Tests
        run: |
          python -m pytest tests/${{ matrix.test-suite }}/ \
            --junitxml=results/${{ matrix.test-suite }}.xml

  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - name: Deploy Canary
        run: |
          kubectl apply -f agents/canary-deployment.yaml

      - name: Monitor Canary
        run: |
          python scripts/canary_monitor.py \
            --duration 300 \
            --success-threshold 0.95

      - name: Promote or Rollback
        run: |
          python scripts/promote_or_rollback.py
```

## 2. Prompt Version Management

### 2.1 Prompt Versioned Storage

```python
from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional
import hashlib

@dataclass
class PromptVersion:
    """Prompt version"""
    version_id: str
    content: str
    hash: str
    created_at: datetime
    author: str
    message: str
    tags: list[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

    @staticmethod
    def compute_hash(content: str) -> str:
        return hashlib.sha256(content.encode()).hexdigest()[:12]


class PromptVersionManager:
    """Prompt version manager"""

    def __init__(self, storage_backend):
        self.storage = storage_backend

    def commit(
        self,
        prompt_name: str,
        content: str,
        author: str,
        message: str,
        tags: Optional[list[str]] = None
    ) -> PromptVersion:
        """Commit a new version"""
        version_id = self._next_version(prompt_name)
        version = PromptVersion(
            version_id=version_id,
            content=content,
            hash=PromptVersion.compute_hash(content),
            created_at=datetime.utcnow(),
            author=author,
            message=message,
            tags=tags or [],
        )

        self.storage.save(prompt_name, version)
        return version

    def get(self, prompt_name: str, version: str) -> PromptVersion:
        """Get a specific version"""
        return self.storage.load(prompt_name, version)

    def get_latest(self, prompt_name: str) -> PromptVersion:
        """Get the latest version"""
        return self.storage.load_latest(prompt_name)

    def list_versions(self, prompt_name: str) -> list[PromptVersion]:
        """List all versions"""
        return self.storage.list_all(prompt_name)

    def diff(self, prompt_name: str, v1: str, v2: str) -> str:
        """Compare the difference between two versions"""
        p1 = self.get(prompt_name, v1)
        p2 = self.get(prompt_name, v2)

        import difflib
        diff = difflib.unified_diff(
            p1.content.splitlines(keepends=True),
            p2.content.splitlines(keepends=True),
            fromfile=f"{prompt_name}@{v1}",
            tofile=f"{prompt_name}@{v2}",
        )
        return ''.join(diff)

    def tag(self, prompt_name: str, version: str, tag: str):
        """Tag a version"""
        v = self.get(prompt_name, version)
        if tag not in v.tags:
            v.tags.append(tag)
            self.storage.save(prompt_name, v)

    def _next_version(self, prompt_name: str) -> str:
        versions = self.list_versions(prompt_name)
        if not versions:
            return "v1.0.0"
        latest = versions[-1].version_id
        # Semantic versioning
        major, minor, patch = latest.lstrip('v').split('.')
        return f"v{major}.{minor}.{int(patch) + 1}"
```

### 2.2 Prompt Evaluation and Testing

```python
@dataclass
class EvalCase:
    """Evaluation case"""
    input: str
    expected_output: str
    expected_contains: list[str] = field(default_factory=list)
    expected_tools: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)

@dataclass
class EvalResult:
    """Evaluation result"""
    case_id: str
    passed: bool
    score: float
    actual_output: str
    metrics: dict

class PromptEvaluator:
    """Prompt evaluator"""

    def __init__(self, agent_factory, eval_cases: list[EvalCase]):
        self.agent_factory = agent_factory
        self.cases = eval_cases

    async def evaluate(self, prompt_version: str) -> dict:
        """Evaluate the Prompt for a specified version"""
        agent = self.agent_factory(prompt_version=prompt_version)
        results: list[EvalResult] = []

        for i, case in enumerate(self.cases):
            result = await self._run_case(agent, case, i)
            results.append(result)

        # Aggregate statistics
        total = len(results)
        passed = sum(1 for r in results if r.passed)
        avg_score = sum(r.score for r in results) / total

        return {
            "prompt_version": prompt_version,
            "total_cases": total,
            "passed": passed,
            "failed": total - passed,
            "pass_rate": passed / total,
            "avg_score": avg_score,
            "details": results,
        }

    async def _run_case(self, agent, case: EvalCase, case_id: int) -> EvalResult:
        """Run a single evaluation case"""
        actual_output = await agent.execute(case.input)

        # Content matching
        contains_pass = all(
            keyword in actual_output for keyword in case.expected_contains
        )

        # Semantic similarity (judged using LLM)
        semantic_score = await self._semantic_similarity(
            case.expected_output, actual_output
        )

        passed = contains_pass and semantic_score > 0.7
        score = semantic_score

        return EvalResult(
            case_id=f"case_{case_id}",
            passed=passed,
            score=score,
            actual_output=actual_output,
            metrics={
                "contains_pass": contains_pass,
                "semantic_score": semantic_score,
            }
        )

    async def _semantic_similarity(self, expected: str, actual: str) -> float:
        """Semantic similarity scoring"""
        # Judged using LLM
        judge_prompt = f"""
        Scoring criteria: semantic similarity between the response and the expected answer (0-1 score)
        Expected answer: {expected}
        Actual answer: {actual}
        Output only the score (a number between 0 and 1).
        """
        # Simplified implementation
        return 0.85
```
## 3. Automated Testing

### 3.1 Three-Layer Testing Architecture

```
┌─────────────────────────────────────────────────────┐
│              Agent Testing Pyramid                   │
│                                                      │
│                    ┌──────┐                          │
│                    │ E2E  │  Real API + Golden Dataset│
│                    │      │  Few, High Cost, High Confidence │
│                   ─┴──────┴─                         │
│                  ┌──────────┐                        │
│                  │Integration│  Real API + Mock Tools │
│                  │   Tests   │  Medium Volume, Medium Cost │
│                 ─┴──────────┴─                       │
│                ┌──────────────┐                      │
│                │  Unit Tests   │  Mock LLM + Mock Tools │
│                │               │  High Volume, Low Cost, Fast │
│               ─┴──────────────┴─                     │
└─────────────────────────────────────────────────────┘
```

### 3.2 Unit Tests (Mock LLM)

```python
import pytest
from unittest.mock import AsyncMock, MagicMock

class MockLLMClient:
    """Mock LLM client"""

    def __init__(self, responses: list[dict]):
        self.responses = responses
        self.call_count = 0
        self.call_history: list[dict] = []

    async def chat(self, messages, tools=None, **kwargs):
        response = self.responses[self.call_count % len(self.responses)]
        self.call_count += 1
        self.call_history.append({
            "messages": messages,
            "tools": tools,
            "kwargs": kwargs,
        })
        return MagicMock(**response)


class TestAgentUnit:
    """Agent unit tests"""

    @pytest.fixture
    def mock_llm(self):
        return MockLLMClient(responses=[
            {"content": "Hello! How can I assist you?", "tool_calls": []},
        ])

    @pytest.fixture
    def agent(self, mock_llm):
        return Agent(
            llm=mock_llm,
            system_prompt="You are a customer service assistant",
            tools=[],
        )

    @pytest.mark.asyncio
    async def test_basic_response(self, agent):
        """Test basic response"""
        result = await agent.execute("Hello")
        assert "Hello" in result or "hello" in result

    @pytest.mark.asyncio
    async def test_tool_calling(self, mock_llm):
        """Test tool calling"""
        mock_llm.responses = [
            {"content": "", "tool_calls": [
                MagicMock(name="search", arguments='{"keyword": "iPhone"}')
            ]},
            {"content": "iPhone 15 is priced at $999", "tool_calls": []},
        ]

        mock_tool = AsyncMock(return_value='{"products": [{"name": "iPhone 15", "price": 999}]}')

        agent = Agent(
            llm=mock_llm,
            tools=[{"name": "search", "func": mock_tool}],
        )

        result = await agent.execute("Search for iPhone price")
        mock_tool.assert_called_once()
        assert "999" in result

    @pytest.mark.asyncio
    async def test_max_tool_calls(self, mock_llm):
        """Test tool call count limit"""
        # Always return a tool call
        mock_llm.responses = [
            {"content": "", "tool_calls": [
                MagicMock(name="search", arguments='{}')
            ]},
        ] * 20

        agent = Agent(
            llm=mock_llm,
            tools=[{"name": "search", "func": AsyncMock(return_value="{}")}],
            max_tool_calls=5,
        )

        result = await agent.execute("Search")
        assert mock_llm.call_count <= 6  # 5 tool calls + 1 final answer
```

### 3.3 Integration Tests (Real API + Mock Tools)

```python
class TestAgentIntegration:
    """Agent integration tests (using real LLM API)"""

    @pytest.fixture
    def agent(self):
        return Agent(
            llm=RealLLMClient(model="gpt-4o-mini"),  # Use smaller model to reduce cost
            system_prompt="You are a test assistant",
            tools=[
                {
                    "name": "get_time",
                    "description": "Get the current time",
                    "func": lambda: datetime.now().isoformat(),
                }
            ],
        )

    @pytest.mark.asyncio
    async def test_tool_selection(self, agent):
        """Test tool selection accuracy"""
        result = await agent.execute("What time is it now?")
        # Verify the tool was called
        assert any(t["name"] == "get_time" for t in agent.last_tool_calls)

    @pytest.mark.asyncio
    async def test_no_unnecessary_tool_call(self, agent):
        """Test that no unnecessary tools are called"""
        result = await agent.execute("What is 1+1?")
        # Verify no tools were called
        assert len(agent.last_tool_calls) == 0

    @pytest.mark.asyncio
    async def test_error_handling(self, agent):
        """Test error handling"""
        agent.tools[0]["func"] = lambda: (_ for _ in ()).throw(Exception("API error"))
        result = await agent.execute("What time is it now?")
        # Verify error is handled gracefully
        assert "error" in result or "sorry" in result or "problem" in result
```

### 3.4 Regression Tests (Golden Dataset)

```python
@dataclass
class GoldenCase:
    """Golden Dataset test case"""
    id: str
    category: str
    input: str
    expected_behavior: str
    expected_contains: list[str]
    expected_tools: list[str]
    max_latency_ms: int
    max_cost_usd: float

class GoldenDatasetRegression:
    """Golden Dataset regression tests"""

    def __init__(self, golden_cases: list[GoldenCase]):
        self.cases = golden_cases
        self.results: list[dict] = []

    async def run_regression(
        self,
        agent_factory,
        model: str = "gpt-4o-mini"
    ) -> dict:
        """Run full regression tests"""
        agent = agent_factory(model=model)

        for case in self.cases:
            start_time = time.time()
            result = await agent.execute(case.input)
            latency_ms = (time.time() - start_time) * 1000

            # Validation
            contains_pass = all(kw in result for kw in case.expected_contains)
            tools_pass = self._check_tools(agent.last_tool_calls, case.expected_tools)
            latency_pass = latency_ms <= case.max_latency_ms

            self.results.append({
                "case_id": case.id,
                "category": case.category,
                "contains_pass": contains_pass,
                "tools_pass": tools_pass,
                "latency_pass": latency_pass,
                "latency_ms": latency_ms,
                "passed": contains_pass and tools_pass and latency_pass,
            })

        return self._generate_report()

    def _check_tools(self, actual_calls: list, expected_tools: list[str]) -> bool:
        if not expected_tools:
            return len(actual_calls) == 0
        actual_names = [c["name"] for c in actual_calls]
        return all(t in actual_names for t in expected_tools)

    def _generate_report(self) -> dict:
        total = len(self.results)
        passed = sum(1 for r in self.results if r["passed"])

        by_category = {}
        for r in self.results:
            cat = r["category"]
            if cat not in by_category:
                by_category[cat] = {"total": 0, "passed": 0}
            by_category[cat]["total"] += 1
            if r["passed"]:
                by_category[cat]["passed"] += 1

        return {
            "total": total,
            "passed": passed,
            "pass_rate": passed / total,
            "by_category": by_category,
            "failures": [r for r in self.results if not r["passed"]],
        }
```
## 4. Progressive Deployment

### 4.1 Canary Agent Deployment

```yaml
# Canary Agent Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: customer-agent-canary
  labels:
    app: customer-agent
    version: canary
spec:
  replicas: 1  # Canary with only 1 replica
  selector:
    matchLabels:
      app: customer-agent
      version: canary
  template:
    metadata:
      labels:
        app: customer-agent
        version: canary
    spec:
      containers:
      - name: agent
        image: agent-runtime:v2.3.1-canary
        env:
        - name: AGENT_VERSION
          value: "v2.3.1"
        - name: CANARY_WEIGHT
          value: "10"  # 10% of traffic
        resources:
          requests:
            cpu: "500m"
            memory: "512Mi"
          limits:
            cpu: "2"
            memory: "2Gi"
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 5
---
# Stable Version Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: customer-agent-stable
  labels:
    app: customer-agent
    version: stable
spec:
  replicas: 9  # Stable version with 9 replicas
  selector:
    matchLabels:
      app: customer-agent
      version: stable
  template:
    metadata:
      labels:
        app: customer-agent
        version: stable
    spec:
      containers:
      - name: agent
        image: agent-runtime:v2.3.0
        env:
        - name: AGENT_VERSION
          value: "v2.3.0"
        - name: CANARY_WEIGHT
          value: "90"  # 90% of traffic
---
# Istio Traffic Splitting
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
  name: customer-agent-vs
spec:
  hosts:
  - customer-agent
  http:
  - route:
    - destination:
        host: customer-agent
        subset: stable
      weight: 90
    - destination:
        host: customer-agent
        subset: canary
      weight: 10
```

### 4.2 Canary Monitoring and Automated Decision-Making

```python
class CanaryMonitor:
    """Canary deployment monitor"""

    def __init__(
        self,
        duration_seconds: int = 300,
        success_threshold: float = 0.95,
        latency_threshold_ms: float = 2000,
    ):
        self.duration = duration_seconds
        self.success_threshold = success_threshold
        self.latency_threshold = latency_threshold_ms
        self.metrics: list[dict] = []

    async def monitor(self, canary_endpoint: str, stable_endpoint: str) -> dict:
        """Monitor the comparison between Canary and Stable"""
        start_time = time.time()

        while time.time() - start_time < self.duration:
            # Collect Canary metrics
            canary_metrics = await self._collect_metrics(canary_endpoint)
            stable_metrics = await self._collect_metrics(stable_endpoint)

            self.metrics.append({
                "timestamp": time.time(),
                "canary": canary_metrics,
                "stable": stable_metrics,
            })

            # Real-time check for whether a rollback is needed
            if self._should_rollback(canary_metrics, stable_metrics):
                return {
                    "decision": "rollback",
                    "reason": "Canary metrics are significantly worse than Stable",
                    "metrics": self.metrics[-1],
                }

            await asyncio.sleep(10)

        # Analyze results
        return self._analyze_results()

    def _should_rollback(self, canary: dict, stable: dict) -> bool:
        """Determine whether a rollback is needed"""
        # Success rate drops by more than 5%
        if canary["success_rate"] < stable["success_rate"] - 0.05:
            return True
        # Latency increases by more than 50%
        if canary["p99_latency"] > stable["p99_latency"] * 1.5:
            return True
        # Error rate exceeds threshold
        if canary["error_rate"] > 0.1:
            return True
        return False

    def _analyze_results(self) -> dict:
        """Analyze Canary results"""
        canary_avg_success = sum(m["canary"]["success_rate"] for m in self.metrics) / len(self.metrics)
        canary_avg_latency = sum(m["canary"]["p99_latency"] for m in self.metrics) / len(self.metrics)

        if canary_avg_success >= self.success_threshold and canary_avg_latency <= self.latency_threshold:
            decision = "promote"
        else:
            decision = "rollback"

        return {
            "decision": decision,
            "avg_success_rate": canary_avg_success,
            "avg_p99_latency": canary_avg_latency,
            "sample_count": len(self.metrics),
        }
```

## 5. Rollback Strategy

### 5.1 Multi-Level Rollback

```yaml
Rollback Strategy:

Level 1: Traffic Rollback (seconds)
  Method: Istio VirtualService weight adjustment
  Action: canary weight=0, stable weight=100
  Impact: No interruption, seamless switchover
  Applicable: Canary metrics anomalies

Level 2: Version Rollback (minutes)
  Method: Deployment rollback
  Action: kubectl rollout undo deployment/agent
  Impact: Brief interruption (rolling update)
  Applicable: When Level 1 cannot resolve the issue

Level 3: Configuration Rollback (minutes)
  Method: Git revert + ArgoCD sync
  Action: git revert <commit> && argocd app sync
  Impact: Full configuration revert
  Applicable: Issues caused by Prompt/configuration changes

Level 4: Data Rollback (hours)
  Method: Knowledge base / vector database restore
  Action: Restore knowledge base from backup
  Impact: Data rollback, potential loss of new data
  Applicable: Increased hallucinations caused by knowledge base updates
```

### 5.2 Automated Rollback Script

```python
class AgentRollbackManager:
    """Agent rollback manager"""

    def __init__(self, k8s_client, argocd_client):
        self.k8s = k8s_client
        self.argocd = argocd_client

    async def auto_rollback(self, deployment: str, namespace: str, level: int = 1):
        """Automated rollback"""
        if level == 1:
            await self._traffic_rollback(deployment, namespace)
        elif level == 2:
            await self._version_rollback(deployment, namespace)
        elif level == 3:
            await self._config_rollback(deployment, namespace)

    async def _traffic_rollback(self, deployment: str, namespace: str):
        """Level 1: Traffic rollback"""
        # Istio VirtualService weight adjustment
        vs_patch = {
            "spec": {
                "http": [{
                    "route": [
                        {"destination": {"host": f"{deployment}", "subset": "stable"}, "weight": 100},
                        {"destination": {"host": f"{deployment}", "subset": "canary"}, "weight": 0},
                    ]
                }]
            }
        }
        await self.k8s.patch_virtual_service(deployment, namespace, vs_patch)

    async def _version_rollback(self, deployment: str, namespace: str):
        """Level 2: Version rollback"""
        await self.k8s.rollback_deployment(deployment, namespace)

    async def _config_rollback(self, deployment: str, namespace: str):
        """Level 3: Configuration rollback"""
        await self.argocd.rollback(deployment)
```

### 5.3 K8s Deployment Configuration

```yaml
# Agent CI/CD Components
apiVersion: apps/v1
kind: Deployment
metadata:
  name: agent-cicd-controller
  namespace: agent-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: agent-cicd
  template:
    spec:
      containers:
      - name: controller
        image: agent-cicd-controller:latest
        env:
        - name: ARGOCD_SERVER
          value: "argocd.argocd.svc.cluster.local"
        - name: PROMETHEUS_URL
          value: "http://prometheus.monitoring.svc.cluster.local:9090"
        - name: CANARY_DURATION
          value: "300"
        - name: SUCCESS_THRESHOLD
          value: "0.95"
        resources:
          requests:
            cpu: "250m"
            memory: "256Mi"
```
## Related Topics

- [[domain-14-ai-ml-infra/03-agent-runtime/18-agent-retry-resilience|Agent Resilience Design]]
- [[domain-14-ai-ml-infra/03-agent-runtime/20-agent-multi-tenancy|Agent Multi-Tenancy Architecture]]
- [[domain-14-ai-ml-infra/03-agent-runtime/21-agent-runtime-architecture-overview|Agent Runtime Architecture Overview]]

## References

- Prompt Engineering Guide
- Promptfoo Evaluation Framework
- ArgoCD GitOps
- Istio Traffic Management


<!-- risk-assessed -->
