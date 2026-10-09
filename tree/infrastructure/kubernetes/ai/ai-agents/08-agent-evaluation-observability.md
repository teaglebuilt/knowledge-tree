---
title: Agent Evaluation System and Observability (domain-14-ai-ml-infra)
description: 'description: ''**Document Type**: Quality Engineering Topic | **Last Updated**: 2026-03 | **Keywords**: Agent
  evaluation, LLM-as-Judge,
summary: 'description: ''**Document Type**: Quality Engineering Topic | **Last Updated**: 2026-03 | **Keywords**: Agent evaluation,
  LLM-as-Judge,'
category: general
tags:
- ai
- ai-agent
- observability
- prometheus
- grafana
- helm
- postgresql
- job
- ingress
- llm
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 25min
intent_queries:
- What is Agent Evaluation System and Observability
- How is Agent Evaluation System and Observability
- Best Practices for Kubernetes 14 ai ml infra
trigger_keywords:
- Agent
- What is Agent Evaluation System and Observability
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- helm-basics
- prometheus-basics
- monitoring-basics
- observability-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/08-agent-evaluation-observability.md
---

> **Production Environment Security Reminders**
>
> Commands contained within this document are executable and should be run only after confirming: the correct target cluster and namespace; sufficient RBAC permissions; and that the commands have been validated in a non-production environment. Risk levels for commands are annotated: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but can usually be rolled back), 🟢 Low Risk/ReadOnly (information gathering with no side effects).




title: Agent Evaluation Framework and Observability
description: '**Document Type**: Engineering Quality Series | **Last Updated**: 2026-03 | **Keywords**: Agent Evaluation, LLM-as-Judge,
  RAGAS, Langfuse, LangSmith, Phoenix, Track Assessment, [[OpenTelemetry|OpenTelemetry]], Observability, Agent Metrics'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- [[Prometheus|prometheus]]
- grafana
- [[Helm|helm]]
- postgresql
- job
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- Architect
- SRE
estimated_read_time: 5min
intent_queries:
- What is the Agent Evaluation Framework and Observability?
- How does the Agent Evaluation Framework and Observability work?
trigger_keywords:
- Agent
- What is the Agent Evaluation Framework and Observability?
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

# Agent Evaluation System and Observability

> **Document Type**: Engineering Quality Series | **Last Updated**: 2026-03 | **Keywords**: Agent Evaluation, LLM-as-Judge, RAGAS, Langfuse, LangSmith, Phoenix, Track Assessment, OpenTelemetry, Observability, Agent Metrics

---

## 1. Overview

Unrated Agents are black-box. The evaluation framework addresses the question "Is the Agent quality up to standard," while observability tackles "Why did the Agent do that." This document covers a comprehensive evaluation framework from single-turn Q&A to multi-step trajectories, implementation methods for RAGAS/LLM-as-Judge, configurations and usage of LangSmith/[[domain-14-ai-ml-infra/03-agent-runtime/13-agent-observability-langfuse.md|Langfuse]]/Phoenix, and key monitoring metrics for production Agents.

---

## 1.1 Evaluation Panorama

## 1.1.1 Evaluation Dimensions

```
Agent Evaluation Four Dimensions
│
├── 1. Accuracy (Correctness)
│      Is the answer correct, are the facts accurate
│      Metrics: Accuracy Rate, Recall Rate, F1
│
├── 2. Efficiency (Efficiency)
│      Number of tool calls, Token consumption, completion time
│      Metrics: Average Steps, Token/Task, Delay P50/P95
│
├── 3. Reliability (Reliability)
│      Success rate, error rate, hallucination rate
│      Metrics: Task Completion Rate, Tool Call Success Rate, Retry Rate
│
└── 4. Safety (Safety)
       Harmful output rate, prompt injection resistance, compliance adherence
       Metrics: Safety Intercept Rate, PII Leakage Rate
```

## 1.2 Granularity Level

| Level | Evaluation Object | Method | Tool |
|------|---------|------|------|
| **Single Turn Q&A** | Quality of a single LLM call | Manual/Auto Scoring | RAGAS |
| **Tool Invocation** | Accuracy of a single tool selection and parameterization | Comparison against expected tool calls | Custom Test Set |
| **Trajectory Evaluation** | Entire Agent execution path | Trajectory vs Optimal Path | LangSmith |
| **End-to-End** | Whether the user's goal was ultimately achieved | Task Completion Rate | Manual Annotation + Automation |

---

## 2. RAGAS Evaluation Framework

## 2.1 Core Metrics Detailed

```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness,           # 忠实度
    answer_relevancy,       # 答案相关性
    context_precision,      # 上下文精确率
    context_recall,         # 上下文召回率
    answer_correctness,     # 答案正确性（需 ground_truth）
    answer_similarity,      # 答案语义相似度
)
from ragas.metrics.critique import harmfulness  # 有害性检测

# Meaning of each metric:
METRIC_EXPLANATIONS = {
    "faithfulness": """
        答案中的每个声明是否都能在检索到的上下文中找到支撑。
        计算方式：能在上下文中验证的声明数 / 总声明数
        目标值：> 0.90（K8s 运维场景，不能有幻觉）
    """,
    "answer_relevancy": """
        答案是否真正回答了问题（而非偏题）。
        计算方式：从答案反向生成问题，与原问题的语义相似度
        目标值：> 0.80
    """,
    "context_precision": """
        检索到的上下文中，有多少比例是真正有用的。
        measure the "noise" level of retrieval
        目标值：> 0.75
    """,
    "context_recall": """
        回答问题所需的信息是否都被检索到了。
        目标值：> 0.70
    """,
}
```

## 2.2 Complete RAGAS Evaluation Pipeline

```python
from datasets import Dataset
from ragas import evaluate
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import pandas as pd

class RAGASEvaluator:
    def __init__(self, eval_llm_model: str = "gpt-4o"):
        # Evaluation using LLM (suggested to use strong models)
        self.eval_llm = LangchainLLMWrapper(
            ChatOpenAI(model=eval_llm_model, temperature=0)
        )
        self.eval_embeddings = LangchainEmbeddingsWrapper(
            OpenAIEmbeddings(model="text-embedding-3-small")
        )
    
    def evaluate_rag_pipeline(
        self,
        test_cases: list[dict],
        rag_pipeline,
    ) -> pd.DataFrame:
        """
        test_cases 格式:
        [
          {
            "question": "Pod Pending most common reason?",
            "ground_truth": "Common reasons: 1. Resource shortage 2. Node affinity...",
          },
          ...
        ]
        """
        # Generate answers using RAG Pipeline
        results = []
        for case in test_cases:
            rag_result = rag_pipeline.query(case["question"])
            results.append({
                "question": case["question"],
                "answer": rag_result["answer"],
                "contexts": [rag_result["sources"]],
                "ground_truth": case.get("ground_truth", ""),
            })
        
        # Build evaluation dataset
        dataset = Dataset.from_list(results)
        
        # Choose applicable metrics
        metrics = [faithfulness, answer_relevancy, context_precision]
        if any(r.get("ground_truth") for r in results):
            metrics.extend([context_recall, answer_correctness])
        
        # Execute evaluation
        eval_result = evaluate(
            dataset=dataset,
            metrics=metrics,
            llm=self.eval_llm,
            embeddings=self.eval_embeddings,
        )
        
        # Generate report
        df = eval_result.to_pandas()
        
        print("\n=== RAG Evaluation Report ===")
        print(f"Faithfulness:       {eval_result['faithfulness']:.3f}")
        print(f"Answer Relevancy:   {eval_result['answer_relevancy']:.3f}")
        print(f"Context Precision:  {eval_result['context_precision']:.3f}")
        
        # Find poor performing cases (scores below 0.7)
        poor_cases = df[df["faithfulness"] < 0.7]
        if len(poor_cases) > 0:
            print(f"\nWarning: {len(poor_cases)} cases have faithfulness < 0.7, need focused review:")
            print(poor_cases"question", "faithfulness".to_string())
        
        return df
```

---

## 3. LLM-as-Judge: Automated Evaluation

## 3.1 Basic Principle

Utilize an LLM as the evaluator (Judge) to score the quality of an Agent's output:

```python
from enum import Enum

class JudgeScore(Enum):
    EXCELLENT = 5  # 完美回答，无任何问题
    GOOD = 4       # 良好，有轻微不足
    ACCEPTABLE = 3 # 可接受，有明显改进空间
    POOR = 2       # 差，有重大问题
    FAILING = 1    # 不合格，需要完全重写

class LLMJudge:
    """LLM-as-Judge Evaluator"""
    
    JUDGE_PROMPT_TEMPLATE = """
    你是 Kubernetes 运维领域的专家评委。请评估以下 AI Agent 回答的质量。
    
    【问题】
    {question}
    
    【参考答案（Ground Truth）】
    {ground_truth}
    
    【Agent 回答】
    {agent_answer}
    
    请从以下维度评分（1-5分，5分最高）：
    
    1. **技术准确性**（0-5）：技术内容是否正确，有无事实错误
    2. **完整性**（0-5）：是否覆盖了问题的核心方面
    3. **可操作性**（0-5）：给出的命令/步骤是否可以实际执行
    4. **安全性**（0-5）：是否有潜在危险的建议（如误删数据）
    
    输出格式：
    {{
        "technical_accuracy": <1-5>,
        "completeness": <1-5>,
        "actionability": <1-5>,
        "safety": <1-5>,
        "overall_score": <1-5>,
        "reasoning": "<rationale, 100 words or less>",
        "critical_issues": ["<critical issue 1>", "<critical issue 2>"],
        "improvement_suggestions": ["<improvement suggestion 1>", "<improvement suggestion 2>"]
    }}
    """
    
    def __init__(self, judge_llm):
        self.judge = judge_llm
    
    def evaluate(
        self,
        question: str,
        agent_answer: str,
        ground_truth: str = "",
    ) -> dict:
        """Evaluate single response"""
        prompt = self.JUDGE_PROMPT_TEMPLATE.format(
            question=question,
            ground_truth=ground_truth or "(no reference answer)",
            agent_answer=agent_answer,
        )
        
        response = self.judge.invoke(prompt)
        
        try:
            scores = json.loads(response.content)
        except json.JSONDecodeError:
            # Degradation handling on failure
            scores = self._parse_scores_fallback(response.content)
        
        return scores
    
    def batch_evaluate(
        self,
        test_cases: list[dict],
        batch_size: int = 5,
    ) -> pd.DataFrame:
        """Batch evaluation"""
        results = []
        
        for i in range(0, len(test_cases), batch_size):
            batch = test_cases[i:i+batch_size]
            
            for case in batch:
                score = self.evaluate(
                    question=case["question"],
                    agent_answer=case["agent_answer"],
                    ground_truth=case.get("ground_truth", ""),
                )
                results.append({
                    "question": case["question"],
                    **score
                })
        
        df = pd.DataFrame(results)
        
        print(f"\n=== LLM-as-Judge Evaluation Results ===")
        print(f"Average score: {df['overall_score'].mean():.2f} / 5.0")
        print(f"Pass rate (>=3 points): {(df['overall_score'] >= 3).mean():.1%}")
        
        return df
```

## 3.2 Trajectory Evaluation (Trajectory Evaluation)

Evaluate the Agent's **execution path** rather than just its final answer:

```python
@dataclass
class AgentTrajectory:
    """Agent Execution Trajectory"""
    task: str
    steps: list[dict]  # [{"thought": "...", "action": "...", "observation": "..."}]
    final_answer: str
    total_steps: int
    total_tokens: int
    success: bool

class TrajectoryEvaluator:
    """Evaluate quality of Agent execution trajectory"""
    
    def evaluate_trajectory(
        self,
        trajectory: AgentTrajectory,
        optimal_step_count: int = None,
    ) -> dict:
        """Multi-dimensional evaluation of trajectory"""
        
        scores = {}
        
        # 1. Efficiency score (steps)
        if optimal_step_count:
            efficiency = min(optimal_step_count / trajectory.total_steps, 1.0)
            scores["efficiency"] = efficiency
        
        # 2. Quality of tool calls
        tool_calls = [s for s in trajectory.steps if s.get("action")]
        scores["tool_selection_accuracy"] = self._evaluate_tool_selection(tool_calls)
        
        # 3. Consistency of reasoning
        scores["reasoning_coherence"] = self._evaluate_reasoning_chain(trajectory.steps)
        
        # 4. Error recovery capability
        errors = [s for s in trajectory.steps if "error" in str(s.get("observation", "")).lower()]
        scores["error_recovery"] = 1.0 if not errors else self._evaluate_recovery(errors, trajectory)
        
        # 5. Task completion
        scores["task_completion"] = 1.0 if trajectory.success else 0.0
        
        # Overall Score
        weights = {
            "efficiency": 0.2,
            "tool_selection_accuracy": 0.3,
            "reasoning_coherence": 0.2,
            "error_recovery": 0.1,
            "task_completion": 0.2,
        }
        
        scores["overall"] = sum(
            scores.get(k, 0) * w for k, w in weights.items()
        )
        
        return scores
    
    def _evaluate_tool_selection(self, tool_calls: list) -> float:
        """Evaluate whether tool selection is reasonable"""
        if not tool_calls:
            return 1.0
        
        issues = 0
        for i, call in enumerate(tool_calls):
            action = call.get("action", "")
            observation = str(call.get("observation", ""))
            
            # Check if the same tool was called repeatedly (waste)
            if i > 0 and action == tool_calls[i-1].get("action"):
                issues += 1
            
            # Check if the tool call returned clearly unrelated results
            # (Simplified: actual need for LLM evaluation)
        
        return max(0.0, 1.0 - issues * 0.2)
```

---

## 4. Observability Platform

## 4.1 Langfuse (Recommended: Open Source Self-Hosted)

```python
from langfuse import Langfuse
from langfuse.decorators import observe, langfuse_context

# Initialization
langfuse = Langfuse(
    public_key="pk-lf-...",
    secret_key="sk-lf-...",
    host="http://langfuse.your-domain.com",  # 自托管实例
)

# Method 1: Using Decorator (simplest)
@observe(name="k8s_diagnosis_agent")
def run_diagnosis_agent(problem: str) -> str:
    """The execution of the entire function will be traced"""
    
    # Update span metadata
    langfuse_context.update_current_trace(
        name=f"diagnosis: {problem[:50]}"
        tags=["production", "k8s-ops"],
        user_id="ops-engineer-001",
    )
    
    # Execute Agent
    result = agent_executor.invoke({"input": problem})
    
    # Record evaluation score
    langfuse_context.score_current_trace(
        name="task_completion",
        value=1 if result["success"] else 0,
    )
    
    return result["output"]

# Method 2: Manual Tracing (more fine-grained control)
def traced_tool_call(tool_name: str, args: dict, trace_id: str) -> str:
    span = langfuse.span(
        trace_id=trace_id,
        name=f"tool:{tool_name}",
        input=args,
    )
    
    try:
        result = execute_tool(tool_name, args)
        span.end(output=result, level="DEFAULT")
        return result
    except Exception as e:
        span.end(
            output=str(e),
            level="ERROR",
            status_message=f"tool invocation failed: {type(e).__name__}"
        )
        raise
```

## 4.2 Langfuse K8s Self-Hosted Deployment

```yaml
# Langfuse Helm Deployment
helm repo add langfuse https://langfuse.github.io/langfuse-k8s
helm install langfuse langfuse/langfuse \
  --namespace ai-observability \
  --create-namespace \
  --set nextauth.secret="your-random-secret" \
  --set langfuse.salt="your-random-salt" \
  --set postgresql.auth.password="your-db-password" \
  --set ingress.enabled=true \
  --set ingress.hosts[0].host="langfuse.your-domain.com" \
  -f langfuse-values.yaml
```

```yaml
# langfuse-values.yaml
langfuse:
  nextPublicSignUpDisabled: "true"  # 生产环境禁止公开注册
  enableExperimentalFeatures: "true"
  
postgresql:
  enabled: true
  primary:
    persistence:
      size: 50Gi
      storageClass: fast-ssd

clickhouse:
  enabled: true  # 用于高性能分析查询
  
resources:
  requests:
    memory: "1Gi"
    cpu: "500m"
  limits:
    memory: "2Gi"
    cpu: "1"
```

## 4.3 LangSmith (Most Comprehensive in the OpenAI Ecosystem)

```python
from langchain.callbacks.tracers import LangChainTracer
from langsmith import Client

# Configure LangSmith
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "ls__..."
os.environ["LANGCHAIN_PROJECT"] = "kudig-k8s-agent"

# LangChain will automatically trace (no additional code needed)
result = agent_executor.invoke({"input": "diagnosis Pod Pending issue"})

# Manually submit evaluation
client = Client()

def submit_evaluation(run_id: str, score: float, comment: str):
    client.create_feedback(
        run_id=run_id,
        key="technical_accuracy",
        score=score,
        comment=comment,
        source_info={"evaluator": "human_expert"},
    )
```

## 4.4 Phoenix (Arize): Local Observability

```python
import phoenix as px
from phoenix.trace.langchain import LangChainInstrumentor

# Start local Phoenix service
px.launch_app()

# Automatically trace LangChain calls
LangChainInstrumentor().instrument()

# View tracing after execution at http://localhost:6006
result = agent_executor.invoke({"input": "issue description"})
```

---

## 5. Production Monitoring Metric System

## 5.1 Prometheus Metric Definitions

```python
from prometheus_client import Counter, Histogram, Gauge, Summary

# Agent Business Metrics
agent_requests_total = Counter(
    'agent_requests_total',
    'Number of total requests processed by Agent',
    ['agent_type', 'status', 'problem_type']
)

agent_task_duration_seconds = Histogram(
    'agent_task_duration_seconds',
    'Total execution time of Agent tasks (seconds)',
    ['agent_type'],
    buckets=[0.5, 1, 2, 5, 10, 30, 60, 120]
)

agent_tool_calls_total = Counter(
    'agent_tool_calls_total',
    'Total number of tool invocations by Agent',
    ['tool_name', 'status']
)

agent_llm_tokens_total = Counter(
    'agent_llm_tokens_total',
    'Total LLM tokens consumed'
    ['model', 'token_type']  # token_type: input/output
)

agent_iteration_count = Histogram(
    'agent_iteration_count',
    'Agent single task iteration count',
    ['agent_type'],
    buckets=[1, 2, 3, 5, 8, 10, 15, 20]
)

agent_hallucination_rate = Gauge(
    'agent_hallucination_rate',
    'Agent hallucination rate (sliding window)',
    ['agent_type']
)

agent_task_success_rate = Gauge(
    'agent_task_success_rate',
    'Task success rate (last 100 times)',
    ['agent_type']
)

# In-agent instrumentation
class InstrumentedAgent:
    def run(self, task: str, agent_type: str = "general") -> dict:
        start_time = time.time()
        
        try:
            result = self._execute(task)
            status = "success" if result.get("success") else "failed"
        except Exception:
            status = "error"
            raise
        finally:
            # Record metrics
            duration = time.time() - start_time
            problem_type = classify_problem(task)
            
            agent_requests_total.labels(
                agent_type=agent_type,
                status=status,
                problem_type=problem_type
            ).inc()
            
            agent_task_duration_seconds.labels(agent_type=agent_type).observe(duration)
        
        return result
```

## 5.2 Key Alert Rules

```yaml
# Prometheus AlertManager rules
groups:
  - name: agent_alerts
    rules:
    
    # Task success rate is too low
    - alert: AgentTaskSuccessRateLow
      expr: agent_task_success_rate < 0.7
      for: 10m
      labels:
        severity: critical
      annotations:
        summary: "Agent task success rate is too low ({{ $value | humanizePercentage }})",
        description: "{{ $labels.agent_type }}'s success rate has dropped below 70%, immediate inspection is required",
    
    # LLM response latency is high
    - alert: LLMHighLatency
      expr: |
        histogram_quantile(0.95, 
          rate(agent_task_duration_seconds_bucket[5m])
        ) > 30
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Agent response P95 latency exceeds 30 seconds",
    
    # Token consumption is abnormal
    - alert: TokenConsumptionSpike
      expr: |
        rate(agent_llm_tokens_total[5m]) > 
        rate(agent_llm_tokens_total[1h] offset 1h) * 3
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Token consumption abnormally increases (more than 3 times the historical baseline)",
        description: "There may be an infinite loop or excessive requests",
    
    # High failure rate of tool calls
    - alert: ToolCallFailureRateHigh
      expr: |
        rate(agent_tool_calls_total{status="error"}[5m]) /
        rate(agent_tool_calls_total[5m]) > 0.3
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Tool invocation failure rate exceeds 30%"
```

## 5.3 Critical Panels in Grafana Dashboard

```
# 🟢 Low-risk: read-only/information collection, usually with no side effects
Agent Monitoring Dashboard Recommendation Panel:

┌─────────────────────────────────────────┐
│  Task Success Rate  │  Average Delay  │  Tokens/Hour  │
│   96.3%    │  4.2s     │  125K/h     │
├─────────────────────────────────────────┤
│      Distribution of task completion times (P50/P95/P99)       │
│  P50: 2.1s  P95: 8.3s  P99: 24s       │
├─────────────────────────────────────────┤
│  Statistics of tool calls      │  Distribution by problem type        │
│  - kubectl: 45%   │  - Network: 32%          │
│  - rag_query: 30% │  - Storage: 18%          │
│  - search: 25%    │  - Scheduling: 28%          │
├─────────────────────────────────────────┤
│         The Token consumption trend over time           │
│  [Cost monitoring chart]                           │
├─────────────────────────────────────────┤
│     A list of recently failed tasks (click to view Trace)      │
└─────────────────────────────────────────┘
```
---

## 6. Automated Evaluation of CI/CD Integration

```yaml
# GitHub Actions: Agent quality gateways
name: Agent Quality Gate

on:
  pull_request:
    paths:
      - 'agent/**'
      - 'prompts/**'

jobs:
  evaluate:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Run Agent Evaluation
      env:
        OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        LANGFUSE_PUBLIC_KEY: ${{ secrets.LANGFUSE_PUBLIC_KEY }}
      run: |
        python scripts/run_agent_evaluation.py \
          --test-set tests/agent_test_cases.json \
          --min-faithfulness 0.85 \
          --min-success-rate 0.90 \
          --output evaluation_report.json
    
    - name: Check Quality Gate
      run: |
        python scripts/check_quality_gate.py \
          --report evaluation_report.json \
          --fail-on-regression
    
    - name: Upload Evaluation Report
      uses: actions/upload-artifact@v4
      with:
        name: evaluation-report
        path: evaluation_report.json
```

```python
# scripts/check_quality_gate.py
import json
import sys

def check_quality_gate(report_path: str, fail_on_regression: bool = True):
    with open(report_path) as f:
        report = json.load(f)
    
    THRESHOLDS = {
        "faithfulness": 0.85,
        "answer_relevancy": 0.80,
        "task_completion_rate": 0.90,
        "hallucination_rate": 0.05,
    }
    
    failed_metrics = []
    for metric, threshold in THRESHOLDS.items():
        if metric in report:
            actual = report[metric]
            if metric == "hallucination_rate":
                if actual > threshold:
                    failed_metrics.append(f"{metric}: {actual:.3f} > {threshold}")
            else:
                if actual < threshold:
                    failed_metrics.append(f"{metric}: {actual:.3f} < {threshold}")
    
    if failed_metrics:
        print("Quality Gate FAILED:")
        for failure in failed_metrics:
            print(f"  ✗ {failure}")
        if fail_on_regression:
            sys.exit(1)
    else:
        print("Quality Gate PASSED")
        for metric in THRESHOLDS:
            print(f"  ✓ {metric}: {report.get(metric, 'N/A'):.3f}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", required=True)
    parser.add_argument("--fail-on-regression", action="store_true")
    args = parser.parse_args()
    check_quality_gate(args.report, args.fail_on_regression)
```

---

## 7. Best Practices and Anti-patterns

## Best Practices

- **Evaluation Sets must be realistic**: Sample real problems from production logs rather than crafting idealized use cases.
- **continuous evaluation**: automatically run evaluations after each code/prompt change to prevent quality regression
- **multi-layer monitoring**: monitor system-level metrics (latency/cost) and business-level metrics (accuracy/completeness) simultaneously
- **observability from day one**: integrate tracing upon production launch, not after issues arise
- **use LLM-as-Judge to save manpower**: use manual scoring as a calibration set, the rest use LLM for judging

## Anti-patterns

- **only evaluate the happy path**: test sets are simple problems, but the system crashes on edge cases after deployment
- **ignore faithfulness**: focus solely on final accuracy without checking hallucinations—hallucinations can cause real issues in Kubernetes ops scenarios
- **no baseline comparison**: no historical assessment scores recorded, unable to determine if version upgrades are progress or regressions
- **evaluate with the same model**: generate answers with GPT-4o and assess them with GPT-4o, leading to homogenization bias

---

## Related Documentation

| document | related content |
|------|---------|
| [04 - RAG to search](./04-rag-knowledge-retrieval.md) | RAGAS evaluates the quality of the RAG pipeline |
| [09 - Production Deployment](./09-production-deployment-guide.md) | Prometheus/Grafana in K8s Configuration |
| [domain-20-enterprise-monitoring-alerting](../domain-06-observability/) | Enterprise-grade monitoring and alerting system |
| [domain-06-observability](../domain-06-observability/) | Observability infrastructure |

---

*This document is original content for the kudig-database project's 02-ai-agents topic.*

---

## Obsidian-related Documentation

- 02-ai-agents KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|AI Agent Engineering Topic]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|Foundation and Core Architecture of AI Agents]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|Selection and Evaluation of LLM Foundation Models]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Deep Comparison of Mainstream Agent Frameworks]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|RAG Retrieval Enhancement Guide]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Design Guidelines for Tool Use and Function Calling]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Multi-Agent Orchestration and Collaboration Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]
- [[domain-14-ai-ml-infra/02-ai-agents/11-cost-latency-optimization.md|Cost and Latency Optimization Strategies]]

## Related

- 48-openclaw-skill-mechanism
- 13-trusted-agent-system-fiscal-plan
- 39-agent-harness-testing-benchmark
- 42-model-harness-compatibility-matrix
- 12-enterprise-case-studies
- 02-llm-foundation-models
- 23-agent-cli-fundamentals
- 50-openclaw-identity-mechanism
- 01-ai-agent-fundamentals
- 03-agent-frameworks-comparison
- 47-openclaw-tools-mechanism
- 37-agent-harness-multi-agent
- 20-agentscope-multi-agent-orchestration
- 40-agent-harness-production-maturity
- 25-agent-cli-mcp-integration
- 26-agent-cli-development-workflow
- 07-memory-context-management
- 11-cost-latency-optimization
- 44-openclaw-soul-mechanism
- 45-openclaw-user-mechanism
- 31-agent-harness-loop-execution
- 27-agent-cli-security-governance
- 06-multi-agent-orchestration
- 41-react-harness-identification-guide

## See Also

- 06-multi-agent-orchestration
- 07-memory-context-management
- 09-production-deployment-guide
- 10-security-guardrails


<!-- risk-assessed -->
