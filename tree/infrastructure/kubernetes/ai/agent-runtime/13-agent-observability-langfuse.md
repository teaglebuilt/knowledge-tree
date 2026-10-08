---
title: Agent Observability
description: 'Langfuse/LangSmith/Phoenix/Weave Observability Platforms: Trace Tracking, Cost Monitoring, Prompt Management, and OpenTelemetry Integration'
summary: 'Langfuse/LangSmith/Phoenix/Weave Observability Platforms: Trace Tracking, Cost Monitoring, Prompt Management, and OpenTelemetry Integration'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- observability
- langfuse
- langsmith
- tracing
tier: supporting
created: '2026-07-02'
last_updated: 2026-07
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- Platform Engineer
- Architect
estimated_read_time: 20min
intent_queries:
- What is Agent Observability
- How to monitor Agent execution
- Langfuse integration in detail
trigger_keywords:
- langfuse
- langsmith
- observability
- tracing
- cost-monitoring
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/13-agent-observability-langfuse.md
---
# Agent Observability

## Overview

AI Agent observability is a core capability for production operations. Unlike traditional applications, an Agent's execution path is dynamically determined by the LLM, making it highly non-deterministic. A single Agent task may involve multiple LLM calls, multiple tool executions, and complex branching logic — traditional logs and metrics are insufficient for debugging and optimization.

This document introduces the major Agent observability platforms: Langfuse (open-source LLM observability), LangSmith (LangChain's official platform), Phoenix/Arize (OpenInference tracing), W&B Weave, and how to achieve a unified observability architecture via OpenTelemetry.

```
Three pillars of observability:

Traces:
  - Complete call chain for Agent execution
  - LLM calls, tool executions, branching logic
  - Latency analysis and bottleneck identification

Metrics:
  - Token usage and cost
  - Latency percentiles
  - Error rate and success rate

Logs:
  - Detailed input/output records
  - Prompt and Completion text
  - Debugging and auditing purposes
```

## Langfuse Integration

### Core Concepts

Langfuse provides a three-level tracing model: Trace, Generation, and Span:

```
Trace:
  - A complete Agent execution
  - Contains all sub-operations
  - Associates users, sessions, and metadata

Generation:
  - A single LLM call
  - Records Prompt, Completion, and Token usage
  - Associates model parameters

Span:
  - General-purpose operation record
  - Tool calls, retrieval operations, post-processing
  - Supports nested structures
```

### LangChain Integration

```python
from langfuse import Langfuse
from langfuse.callback import CallbackHandler
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai import ChatOpenAI

# Initialize Langfuse
langfuse = Langfuse(
    public_key="pk-...",
    secret_key="sk-...",
    host="https://cloud.langfuse.com",
)

# Create callback handler
langfuse_handler = CallbackHandler(
    trace_name="research-agent",
    user_id="user-123",
    session_id="session-456",
    metadata={
        "environment": "production",
        "version": "1.0.0",
    },
)

# Create Agent
llm = ChatOpenAI(model="gpt-4o", temperature=0.1)
agent = create_openai_tools_agent(llm, tools, prompt)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Execute Agent (automatically traced)
result = await executor.ainvoke(
    {"input": "Research Kubernetes network policies"},
    config={"callbacks": [langfuse_handler]},
)

# Manually record a custom Span
trace = langfuse_handler.get_trace()
with langfuse.span(
    name="post-processing",
    trace_id=trace.id,
) as span:
    processed = post_process(result["output"])
    span.output = processed
```

### LangGraph Integration

```python
from langfuse import Langfuse
from langfuse.callback import CallbackHandler
from langgraph.graph import StateGraph, END

# Create Langfuse callback
langfuse_handler = CallbackHandler(trace_name="langgraph-agent")

# Define LangGraph
workflow = StateGraph(AgentState)

workflow.add_node("agent", agent_node)
workflow.add_node("tools", tool_node)
workflow.add_node("human_review", human_review_node)

workflow.set_entry_point("agent")
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",
        "human_review": "human_review",
        "end": END,
    },
)
workflow.add_edge("tools", "agent")
workflow.add_edge("human_review", "agent")

graph = workflow.compile()

# Execute (automatically traced)
result = await graph.ainvoke(
    {"messages": [HumanMessage(content="Analyze system logs")]},
    config={"callbacks": [langfuse_handler]},
)
```

### OpenAI SDK Integration

```python
from langfuse import Langfuse
from langfuse.openai import openai  # Use Langfuse-wrapped OpenAI client
from openai import AsyncOpenAI

# Automatically trace all OpenAI calls
client = AsyncOpenAI()

# Use decorator for tracing
from langfuse.decorators import observe

@observe(as_type="generation")
async def llm_call(messages: list, model: str = "gpt-4o"):
    """LLM call automatically traced by Langfuse"""
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return response.choices[0].message.content


@observe(name="agent-execution")
async def execute_agent(query: str):
    """Agent execution traced by Langfuse"""
    messages = [
        {"role": "system", "content": "You are a research assistant."},
        {"role": "user", "content": query},
    ]

    # This call will be automatically traced
    response = await llm_call(messages)

    # Record additional metadata
    langfuse = Langfuse()
    span = langfuse.span(name="tool-execution")
    tool_result = await execute_search_tool(response)
    span.end(output=tool_result)

    return response
```

### Prompt Management

```python
from langfuse import Langfuse
from langfuse.prompt import PromptClient

langfuse = Langfuse()
prompt_client = PromptClient(langfuse)

# Retrieve Prompt from Langfuse (with version management support)
prompt = prompt_client.get_prompt(
    name="research-agent-system-prompt",
    version=3,
)

# Use the Prompt
system_prompt = prompt.compile(
    domain="kubernetes",
    expertise_level="expert",
)

# Execute Agent
response = await llm_call([
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": query},
])

# Associate Prompt version with Trace
langfuse.generation(
    name="research-agent",
    model="gpt-4o",
    prompt=prompt,
    metadata={"prompt_version": prompt.version},
)
```

### Evaluation and Testing

```python
from langfuse import Langfuse
from langfuse.evaluate import evaluate

langfuse = Langfuse()

# Define evaluation function
def correctness_evaluation(output: str, expected: str) -> float:
    """Evaluate answer correctness"""
    # Can use LLM-as-Judge
    score = llm_judge(
        prompt=f"""
        Evaluate the correctness of the following answer:
        Expected: {expected}
        Actual: {output}
        
        Return a score between 0 and 1.
        """,
    )
    return score

# Run evaluation
evaluation = evaluate(
    dataset_id="research-qa-dataset",
    experiment_name="v1.2-evaluation",
    target_fn=lambda input: execute_agent(input["query"]),
    scores=[correctness_evaluation],
    metadata={"model": "gpt-4o", "temperature": 0.1},
)
```
## LangSmith

### Run Tree Model

```python
from langsmith import Client, traceable
from langsmith.run_helpers import trace

client = Client()

# Track using decorator
@traceable(
    name="agent-execution",
    run_type="chain",
    metadata={"version": "1.0"},
)
async def execute_agent(query: str) -> str:
    """Agent execution tracked by LangSmith"""
    # LLM calls are automatically tracked
    response = await llm_call(query)
    return response

# Manually create Run Tree
from langsmith.run_trees import RunTree

run_tree = RunTree(
    name="agent-execution",
    run_type="chain",
    inputs={"query": "Research Kubernetes network policies"},
)

# Add child Run
child_run = run_tree.create_child(
    name="llm-call",
    run_type="llm",
    inputs={
        "messages": [...],
        "model": "gpt-4o",
    },
)

# Record LLM output
child_run.end(outputs={
    "content": response.content,
    "token_usage": response.usage,
})

# Submit Run
run_tree.post()
```

### Evaluation and Dataset

```python
from langsmith import Client
from langsmith.evaluation import evaluate

client = Client()

# Create Dataset
dataset = client.create_dataset(
    dataset_name="agent-qa-evaluation",
    description="Agent Q&A quality evaluation dataset",
)

# Add test cases
client.create_example(
    inputs={"query": "What is a Kubernetes network policy?"},
    outputs={"expected": "A Kubernetes network policy is..."},
    dataset_id=dataset.id,
)

# Define evaluation functions
def evaluate_correctness(run, example):
    """Evaluate answer correctness"""
    output = run.outputs.get("output", "")
    expected = example.outputs.get("expected", "")

    # LLM-as-Judge evaluation
    score = llm_judge(output, expected)
    return {"key": "correctness", "score": score}

def evaluate_completeness(run, example):
    """Evaluate answer completeness"""
    output = run.outputs.get("output", "")
    # Check key point coverage
    key_points = extract_key_points(example.outputs["expected"])
    coverage = calculate_coverage(output, key_points)
    return {"key": "completeness", "score": coverage}

# Run evaluation
experiment_results = evaluate(
    target_fn=lambda inputs: execute_agent(inputs["query"]),
    data="agent-qa-evaluation",
    evaluators=[
        evaluate_correctness,
        evaluate_completeness,
    ],
    experiment_prefix="v1.2",
    metadata={
        "model": "gpt-4o",
        "temperature": 0.1,
    },
)
```

## Phoenix/Arize (OpenInference)

### OpenInference Tracing

```python
import phoenix as px
from phoenix.otel import register
from openinference.instrumentation.langchain import LangChainInstrumentor
from openinference.instrumentation.openai import OpenAIInstrumentor

# Launch Phoenix
px.launch_app()

# Register OpenTelemetry tracing
tracer_provider = register(
    project_name="agent-observability",
    endpoint="http://localhost:6006/v1/traces",
)

# Auto-instrument LangChain
LangChainInstrumentor().instrument(tracer_provider=tracer_provider)

# Auto-instrument OpenAI
OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)

# Agent execution is automatically traced
from langchain.agents import AgentExecutor

executor = AgentExecutor(agent=agent, tools=tools)
result = executor.invoke({"input": "Analyze system performance"})
```

### Custom Span

```python
from opentelemetry import trace

tracer = trace.get_tracer("agent-tracer")

@tracer.start_as_current_span("tool-execution")
async def execute_tool(tool_name: str, arguments: dict) -> dict:
    """Custom tool execution Span"""
    span = trace.get_current_span()

    span.set_attribute("tool.name", tool_name)
    span.set_attribute("tool.arguments", json.dumps(arguments))

    try:
        result = await tool_handlers[tool_name](**arguments)
        span.set_attribute("tool.status", "success")
        return result
    except Exception as e:
        span.set_attribute("tool.status", "error")
        span.set_attribute("tool.error", str(e))
        raise
```

## W&B Weave

### Weave Integration

```python
import weave

# Initialize Weave
weave.init(project_name="agent-observability")

# Track using decorator
@weave.op()
async def llm_call(messages: list, model: str = "gpt-4o"):
    """LLM call tracked by Weave"""
    client = AsyncOpenAI()
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return response.choices[0].message.content

@weave.op()
async def execute_tool(tool_name: str, arguments: dict):
    """Tool execution tracked by Weave"""
    result = await tool_handlers[tool_name](**arguments)
    return result

@weave.op()
async def agent_execution(query: str):
    """Agent execution tracked by Weave"""
    messages = [
        {"role": "system", "content": "You are a research assistant."},
        {"role": "user", "content": query},
    ]

    response = await llm_call(messages)

    if should_use_tools(response):
        tool_results = []
        for tool_call in extract_tool_calls(response):
            result = await execute_tool(
                tool_call["name"],
                tool_call["arguments"],
            )
            tool_results.append(result)

        messages.append({"role": "assistant", "content": response})
        messages.append({"role": "tool", "content": json.dumps(tool_results)})
        response = await llm_call(messages)

    return response

# Execute (automatically tracked)
result = await agent_execution("Research Kubernetes best practices")
```

### Weave Evaluation

```python
import weave
from weave import Evaluation

# Define evaluation dataset
dataset = [
    {
        "query": "What is a Kubernetes network policy?",
        "expected": "A Kubernetes network policy is a kind of...",
    },
    {
        "query": "How do I configure a Pod security policy?",
        "expected": "Pod security policy configuration steps...",
    },
]

# Define evaluation functions
@weave.op()
def evaluate_correctness(output: str, expected: str) -> dict:
    score = calculate_similarity(output, expected)
    return {"correctness": score}

@weave.op()
def evaluate_latency(output: str, expected: str, latency: float) -> dict:
    return {"latency_score": 1.0 if latency < 5.0 else 0.5}

# Create evaluation
evaluation = Evaluation(
    dataset=dataset,
    scorers=[evaluate_correctness, evaluate_latency],
)

# Run evaluation
scores = await evaluation.evaluate(agent_execution)
```
## OpenTelemetry for LLM Agent

### Unified Tracing Architecture

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)
from opentelemetry.sdk.resources import Resource

# Configure OpenTelemetry
resource = Resource.create({
    "service.name": "agent-service",
    "service.version": "1.0.0",
    "deployment.environment": "production",
})

provider = TracerProvider(resource=resource)
processor = BatchSpanProcessor(
    OTLPSpanExporter(endpoint="http://otel-collector:4317")
)
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer("agent-tracer")
```

### LLM Semantic Conventions

```python
from opentelemetry import trace

tracer = trace.get_tracer("agent-tracer")

@tracer.start_as_current_span("llm.completion")
async def traced_llm_call(
    messages: list,
    model: str,
    temperature: float = 0.1,
):
    """LLM call tracing following OpenInference semantic conventions"""
    span = trace.get_current_span()

    # Set LLM-specific attributes
    span.set_attribute("llm.model_name", model)
    span.set_attribute("llm.temperature", temperature)
    span.set_attribute("llm.input_messages", json.dumps([
        {"role": m["role"], "content": m["content"][:100]}
        for m in messages
    ]))

    client = AsyncOpenAI()
    response = await client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )

    # Record output
    span.set_attribute("llm.output_message", response.choices[0].message.content[:200])
    span.set_attribute("llm.token_count.prompt", response.usage.prompt_tokens)
    span.set_attribute("llm.token_count.completion", response.usage.completion_tokens)
    span.set_attribute("llm.token_count.total", response.usage.total_tokens)
    span.set_attribute("llm.finish_reason", response.choices[0].finish_reason)

    return response
```

## Cost Tracking and Token Usage Monitoring

### Cost Calculator

```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class ModelPricing:
    """Model pricing information"""
    input_price_per_1k: float   # Price per 1K input tokens
    output_price_per_1k: float  # Price per 1K output tokens


# Model pricing table (example)
MODEL_PRICING = {
    "gpt-4o": ModelPricing(input_price_per_1k=0.005, output_price_per_1k=0.015),
    "gpt-4o-mini": ModelPricing(input_price_per_1k=0.00015, output_price_per_1k=0.0006),
    "claude-3-5-sonnet": ModelPricing(input_price_per_1k=0.003, output_price_per_1k=0.015),
}


class CostTracker:
    """Agent cost tracker"""

    def __init__(self):
        self.usage_records = []

    def record_usage(
        self,
        agent_id: str,
        model: str,
        input_tokens: int,
        output_tokens: int,
        metadata: dict = None,
    ):
        """Record token usage"""
        pricing = MODEL_PRICING.get(model)
        if not pricing:
            raise ValueError(f"Unknown model: {model}")

        input_cost = (input_tokens / 1000) * pricing.input_price_per_1k
        output_cost = (output_tokens / 1000) * pricing.output_price_per_1k
        total_cost = input_cost + output_cost

        record = UsageRecord(
            agent_id=agent_id,
            model=model,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            input_cost=input_cost,
            output_cost=output_cost,
            total_cost=total_cost,
            timestamp=datetime.utcnow(),
            metadata=metadata or {},
        )

        self.usage_records.append(record)
        return record

    def get_total_cost(
        self,
        agent_id: str = None,
        start_time: datetime = None,
        end_time: datetime = None,
    ) -> float:
        """Get total cost"""
        filtered = self.usage_records

        if agent_id:
            filtered = [r for r in filtered if r.agent_id == agent_id]
        if start_time:
            filtered = [r for r in filtered if r.timestamp >= start_time]
        if end_time:
            filtered = [r for r in filtered if r.timestamp <= end_time]

        return sum(r.total_cost for r in filtered)

    def get_usage_summary(
        self,
        agent_id: str = None,
    ) -> dict:
        """Get usage summary"""
        filtered = self.usage_records
        if agent_id:
            filtered = [r for r in filtered if r.agent_id == agent_id]

        return {
            "total_calls": len(filtered),
            "total_input_tokens": sum(r.input_tokens for r in filtered),
            "total_output_tokens": sum(r.output_tokens for r in filtered),
            "total_cost": sum(r.total_cost for r in filtered),
            "by_model": self._group_by_model(filtered),
        }

    def _group_by_model(self, records: list) -> dict:
        """Group statistics by model"""
        by_model = {}
        for record in records:
            if record.model not in by_model:
                by_model[record.model] = {
                    "calls": 0,
                    "input_tokens": 0,
                    "output_tokens": 0,
                    "cost": 0,
                }
            by_model[record.model]["calls"] += 1
            by_model[record.model]["input_tokens"] += record.input_tokens
            by_model[record.model]["output_tokens"] += record.output_tokens
            by_model[record.model]["cost"] += record.total_cost
        return by_model
```

### Prometheus Metrics

```python
from prometheus_client import Counter, Histogram, Gauge

# Define Agent metrics
agent_llm_calls = Counter(
    "agent_llm_calls_total",
    "Total LLM API calls",
    ["agent_id", "model", "status"],
)

agent_llm_tokens = Counter(
    "agent_llm_tokens_total",
    "Total tokens used",
    ["agent_id", "model", "direction"],  # direction: input/output
)

agent_llm_latency = Histogram(
    "agent_llm_latency_seconds",
    "LLM call latency",
    ["agent_id", "model"],
    buckets=[0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 30.0],
)

agent_cost = Counter(
    "agent_cost_dollars",
    "Total cost in dollars",
    ["agent_id", "model"],
)

agent_tool_calls = Counter(
    "agent_tool_calls_total",
    "Total tool calls",
    ["agent_id", "tool_name", "status"],
)

agent_active_tasks = Gauge(
    "agent_active_tasks",
    "Currently active agent tasks",
    ["agent_id"],
)


# Usage example
async def monitored_llm_call(
    agent_id: str,
    messages: list,
    model: str = "gpt-4o",
):
    """LLM call with Prometheus metrics"""
    agent_active_tasks.labels(agent_id=agent_id).inc()

    with agent_llm_latency.labels(
        agent_id=agent_id,
        model=model,
    ).time():
        try:
            response = await client.chat.completions.create(
                model=model,
                messages=messages,
            )

            agent_llm_calls.labels(
                agent_id=agent_id,
                model=model,
                status="success",
            ).inc()

            agent_llm_tokens.labels(
                agent_id=agent_id,
                model=model,
                direction="input",
            ).inc(response.usage.prompt_tokens)

            agent_llm_tokens.labels(
                agent_id=agent_id,
                model=model,
                direction="output",
            ).inc(response.usage.completion_tokens)

            # Record cost
            cost = calculate_cost(
                model,
                response.usage.prompt_tokens,
                response.usage.completion_tokens,
            )
            agent_cost.labels(
                agent_id=agent_id,
                model=model,
            ).inc(cost)

            return response

        except Exception as e:
            agent_llm_calls.labels(
                agent_id=agent_id,
                model=model,
                status="error",
            ).inc()
            raise
        finally:
            agent_active_tasks.labels(agent_id=agent_id).dec()
```

### Grafana Dashboard

```yaml
# Grafana Dashboard configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: agent-dashboard
data:
  dashboard.json: |
    {
      "dashboard": {
        "title": "Agent Observability",
        "panels": [
          {
            "title": "LLM Calls per Second",
            "targets": [
              {
                "expr": "rate(agent_llm_calls_total[5m])"
              }
            ]
          },
          {
            "title": "Token Usage",
            "targets": [
              {
                "expr": "rate(agent_llm_tokens_total[5m])"
              }
            ]
          },
          {
            "title": "Cost per Hour",
            "targets": [
              {
                "expr": "increase(agent_cost_dollars[1h])"
              }
            ]
          },
          {
            "title": "P95 Latency",
            "targets": [
              {
                "expr": "histogram_quantile(0.95, rate(agent_llm_latency_seconds_bucket[5m]))"
              }
            ]
          }
        ]
      }
    }
```

---

*Agent observability is key to understanding and optimizing Agent behavior. Platforms such as Langfuse/LangSmith enable full end-to-end monitoring from traces to cost.*
