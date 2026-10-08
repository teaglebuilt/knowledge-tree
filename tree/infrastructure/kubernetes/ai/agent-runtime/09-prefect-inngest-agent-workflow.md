---
title: Prefect/Inngest Agent Workflow
description: 'Agent workflow orchestration based on Prefect and Inngest: Flow/Task model, event-driven Step Functions, Durable Execution semantics, and K8s deployment'
summary: 'Agent workflow orchestration based on Prefect and Inngest: Flow/Task model, event-driven Step Functions, Durable Execution semantics, and K8s deployment'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- prefect
- inngest
- workflow
- durable-execution
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
- What is Prefect Agent Workflow
- How to orchestrate Agent execution with Inngest
- Detailed explanation of Durable Execution semantics
trigger_keywords:
- prefect
- inngest
- agent-workflow
- durable-execution
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/09-prefect-inngest-agent-workflow.md
---
# Prefect/Inngest Agent Workflow

## Overview

Prefect and Inngest represent two different Agent workflow orchestration paradigms. Prefect provides a Python-native Flow/Task orchestration model, suitable for data-intensive Agent tasks requiring fine-grained control; Inngest is based on event-driven Step Functions, providing fully managed Durable Execution semantics, suitable for building reactive Agent systems. Both solve the core problem in Agent execution: how to reliably orchestrate long-running Agent tasks in a distributed environment.

## Prefect Flow/Task Orchestration for Agent Execution

### Core Concepts

Prefect's programming model is based on a two-level abstraction of Flow and Task:

```
Flow:
  - Top-level orchestration unit for Agent tasks
  - Manages overall execution flow and state
  - Supports parameterization, scheduling, and retries
  - Can nested-call other Flows

Task:
  - Smallest execution unit within a Flow
  - Automatic caching and retries
  - Supports concurrent execution
  - Configurable timeout and retry policies
```

### Agent Flow Implementation

```python
from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta
from typing import Optional

@task(
    retries=3,
    retry_delay_seconds=10,
    cache_key_fn=task_input_hash,
    cache_expiration=timedelta(hours=1),
    timeout_seconds=120,
)
async def llm_inference(
    system_prompt: str,
    messages: list,
    model: str = "gpt-4o",
) -> dict:
    """LLM inference task"""
    client = AsyncOpenAI()

    response = await client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": system_prompt}] + messages,
        tools=TOOL_DEFINITIONS,
        temperature=0.1,
    )

    return {
        "content": response.choices[0].message.content,
        "tool_calls": [
            {
                "id": tc.id,
                "name": tc.function.name,
                "arguments": json.loads(tc.function.arguments),
            }
            for tc in (response.choices[0].message.tool_calls or [])
        ],
        "usage": {
            "prompt_tokens": response.usage.prompt_tokens,
            "completion_tokens": response.usage.completion_tokens,
        },
    }


@task(retries=2, retry_delay_seconds=5, timeout_seconds=300)
async def execute_tool(
    tool_name: str,
    arguments: dict,
) -> dict:
    """Tool execution task"""
    tools = {
        "web_search": web_search_tool,
        "database_query": database_query_tool,
        "code_execute": code_execute_tool,
    }

    handler = tools.get(tool_name)
    if not handler:
        return {"status": "error", "output": f"Unknown tool: {tool_name}"}

    result = await handler(**arguments)
    return {"status": "success", "output": result}


@task(timeout_seconds=60)
async def evaluate_response(
    response: dict,
    evaluation_criteria: dict,
) -> dict:
    """Evaluate Agent response quality"""
    eval_prompt = f"""
    Evaluate the quality of the following Agent response:
    Response: {response['content']}
    Criteria: {json.dumps(evaluation_criteria)}

    Return a JSON-formatted score (0-100) and improvement suggestions.
    """

    eval_result = await llm_inference(
        system_prompt="You are an evaluation expert.",
        messages=[{"role": "user", "content": eval_prompt}],
        model="gpt-4o-mini",
    )

    return json.loads(eval_result["content"])


@flow(
    name="agent-execution-flow",
    description="Persistent Agent execution flow",
    retries=1,
    retry_delay_seconds=60,
    timeout_seconds=3600,
)
async def agent_flow(
    query: str,
    system_prompt: str,
    max_iterations: int = 20,
    evaluation_threshold: float = 80.0,
) -> dict:
    """Agent execution main flow"""
    conversation_history = [{"role": "user", "content": query}]
    tool_results = []
    total_tokens = {"prompt": 0, "completion": 0}

    for iteration in range(max_iterations):
        # LLM inference
        llm_response = await llm_inference(
            system_prompt=system_prompt,
            messages=conversation_history,
        )

        # Accumulate token usage
        total_tokens["prompt"] += llm_response["usage"]["prompt_tokens"]
        total_tokens["completion"] += llm_response["usage"]["completion_tokens"]

        if llm_response["tool_calls"]:
            # Execute tool calls
            for tool_call in llm_response["tool_calls"]:
                result = await execute_tool(
                    tool_name=tool_call["name"],
                    arguments=tool_call["arguments"],
                )
                tool_results.append({
                    "tool": tool_call["name"],
                    "result": result,
                })

                conversation_history.append({
                    "role": "assistant",
                    "content": None,
                    "tool_calls": [tool_call],
                })
                conversation_history.append({
                    "role": "tool",
                    "content": json.dumps(result["output"]),
                    "tool_call_id": tool_call["id"],
                })
        else:
            # Agent generates final response
            evaluation = await evaluate_response(
                response=llm_response,
                evaluation_criteria={
                    "accuracy": "Whether the response accurately answers the question",
                    "completeness": "Whether the response is complete",
                    "clarity": "Whether the response is clear and easy to understand",
                },
            )

            if evaluation["score"] >= evaluation_threshold:
                return {
                    "output": llm_response["content"],
                    "iterations": iteration + 1,
                    "tool_results": tool_results,
                    "total_tokens": total_tokens,
                    "evaluation": evaluation,
                    "status": "completed",
                }

            # Score below threshold, continue iterating
            conversation_history.append({
                "role": "user",
                "content": f"Please improve your answer. Evaluation feedback: {evaluation['feedback']}",
            })

        conversation_history.append({
            "role": "assistant",
            "content": llm_response["content"],
        })

    return {
        "output": "Maximum number of iterations reached",
        "iterations": max_iterations,
        "tool_results": tool_results,
        "total_tokens": total_tokens,
        "status": "max_iterations_exceeded",
    }
```

### Parallel Agent Orchestration

```python
@flow(name="parallel-agent-flow")
async def parallel_agent_flow(
    queries: list[str],
    system_prompts: list[str],
) -> list[dict]:
    """Execute multiple Agent tasks in parallel"""
    # Prefect automatically executes independent Flows/Tasks in parallel
    futures = []
    for query, prompt in zip(queries, system_prompts):
        future = agent_flow.submit(
            query=query,
            system_prompt=prompt,
        )
        futures.append(future)

    results = []
    for future in futures:
        result = await future.result()
        results.append(result)

    return results


@flow(name="hierarchical-agent-flow")
async def hierarchical_agent_flow(task: str) -> dict:
    """Hierarchical Agent orchestration - Supervisor + Workers"""
    # Supervisor Agent analyzes the task and delegates
    supervisor_response = await agent_flow(
        query=f"Analyze the following task and break it down into subtasks: {task}",
        system_prompt=SUPERVISOR_PROMPT,
    )

    subtasks = json.loads(supervisor_response["output"])["subtasks"]

    # Worker Agents execute subtasks in parallel
    worker_results = await parallel_agent_flow(
        queries=[st["description"] for st in subtasks],
        system_prompts=[WORKER_PROMPT] * len(subtasks),
    )

    # Aggregator Agent merges results
    aggregator_response = await agent_flow(
        query=f"Merge the following results: {json.dumps(worker_results)}",
        system_prompt=AGGREGATOR_PROMPT,
    )

    return {
        "final_output": aggregator_response["output"],
        "subtask_results": worker_results,
        "total_iterations": sum(r["iterations"] for r in worker_results),
    }
```

### Prefect Deployment Configuration

```yaml
# prefect-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: prefect-agent-worker
spec:
  replicas: 3
  selector:
    matchLabels:
      app: prefect-agent-worker
  template:
    spec:
      containers:
        - name: worker
          image: registry.example.com/prefect-agent:latest
          command: ["prefect", "worker", "start"]
          args:
            - "--pool"
            - "agent-pool"
            - "--type"
            - "process"
          env:
            - name: PREFECT_API_URL
              value: "https://prefect.example.com/api"
            - name: PREFECT_API_KEY
              valueFrom:
                secretKeyRef:
                  name: prefect-credentials
                  key: api-key
            - name: OPENAI_API_KEY
              valueFrom:
                secretKeyRef:
                  name: openai-credentials
                  key: api-key
          resources:
            requests:
              cpu: "500m"
              memory: "1Gi"
            limits:
              cpu: "2"
              memory: "4Gi"
```
## Inngest Step Functions Event-Driven Agent

### Inngest Core Concepts

Inngest is an event-driven Durable Execution platform that provides reliable asynchronous task orchestration through Step Functions:

```
Event:
  - A message that triggers Function execution
  - Contains type and data
  - Asynchronous delivery, supports batch processing

Function:
  - Logic that executes in response to events
  - Composed of multiple Steps
  - Automatic retry and persistence

Step:
  - The smallest execution unit within a Function
  - Results are automatically cached
  - Supports parallel execution
  - Provides sleep/waitUntil capabilities
```

### Inngest Agent Function

```typescript
import { inngest } from "./client";

// Define Agent event
export const agentRequested = inngest.createFunction(
  { id: "agent-execution", name: "Agent Execution" },
  { event: "agent/requested" },
  async ({ event, step }) => {
    const { query, config } = event.data;

    // Step 1: Initialize conversation
    const conversation = await step.run("init-conversation", async () => {
      return {
        messages: [{ role: "user", content: query }],
        tool_results: [],
      };
    });

    // Agent main loop
    let iteration = 0;
    const maxIterations = config.maxIterations || 20;

    while (iteration < maxIterations) {
      // Step 2: LLM inference (each step is persisted)
      const llmResponse = await step.run(
        `llm-inference-${iteration}`,
        async () => {
          const response = await openai.chat.completions.create({
            model: config.model || "gpt-4o",
            messages: [
              { role: "system", content: config.systemPrompt },
              ...conversation.messages,
            ],
            tools: TOOL_DEFINITIONS,
          });

          return {
            content: response.choices[0].message.content,
            toolCalls: response.choices[0].message.tool_calls || [],
            usage: response.usage,
          };
        }
      );

      if (llmResponse.toolCalls.length > 0) {
        // Step 3: Execute tool calls (supports parallel execution)
        const toolResults = await Promise.all(
          llmResponse.toolCalls.map((toolCall, index) =>
            step.run(`tool-exec-${iteration}-${index}`, async () => {
              return await executeTool(
                toolCall.function.name,
                JSON.parse(toolCall.function.arguments)
              );
            })
          )
        );

        // Update conversation history
        conversation.messages.push({
          role: "assistant",
          content: llmResponse.content,
          tool_calls: llmResponse.toolCalls,
        });

        toolResults.forEach((result, index) => {
          conversation.messages.push({
            role: "tool",
            content: JSON.stringify(result),
            tool_call_id: llmResponse.toolCalls[index].id,
          });
          conversation.tool_results.push(result);
        });
      } else {
        // Step 4: Wait for human approval (if required)
        if (config.requireApproval) {
          await step.waitForEvent("human-approval", {
            event: "agent/approval",
            timeout: "24h",
            match: "data.requestId",
          });
        }

        // Step 5: Return final result
        await step.sendEvent("agent-completed", {
          name: "agent/completed",
          data: {
            requestId: event.data.requestId,
            output: llmResponse.content,
            iterations: iteration + 1,
            toolResults: conversation.tool_results,
          },
        });

        return {
          output: llmResponse.content,
          iterations: iteration + 1,
          toolResults: conversation.tool_results,
        };
      }

      iteration++;

      // Step 6: Inter-iteration delay (to prevent rate limiting)
      await step.sleep("iteration-delay", "2s");
    }

    return {
      output: "Maximum iteration count reached",
      iterations: maxIterations,
      status: "max_iterations_exceeded",
    };
  }
);

// Multi-Agent collaboration Function
export const multiAgentOrchestration = inngest.createFunction(
  { id: "multi-agent", name: "Multi-Agent Orchestration" },
  { event: "agent/multi-agent-requested" },
  async ({ event, step }) => {
    const { task, agents } = event.data;

    // Step 1: Supervisor analyzes the task
    const plan = await step.run("supervisor-plan", async () => {
      const response = await agentExecute({
        query: `Analyze the task and formulate an execution plan: ${task}`,
        config: { systemPrompt: SUPERVISOR_PROMPT },
      });
      return JSON.parse(response.output);
    });

    // Step 2: Execute Worker Agents in parallel
    const workerResults = await Promise.all(
      plan.subtasks.map((subtask, index) =>
        step.run(`worker-${index}`, async () => {
          return await agentExecute({
            query: subtask.description,
            config: {
              systemPrompt: agents[subtask.agentType].prompt,
              model: agents[subtask.agentType].model,
            },
          });
        })
      )
    );

    // Step 3: Aggregator merges results
    const finalResult = await step.run("aggregator", async () => {
      return await agentExecute({
        query: `Merge the following results: ${JSON.stringify(workerResults)}`,
        config: { systemPrompt: AGGREGATOR_PROMPT },
      });
    });

    return {
      plan,
      workerResults,
      finalOutput: finalResult.output,
    };
  }
);
```

### Inngest Deployment Configuration

```typescript
// inngest/client.ts
import { Inngest } from "inngest";

export const inngest = new Inngest({
  id: "agent-service",
  eventKey: process.env.INNGEST_EVENT_KEY,
  // Production configuration
  middleware: [
    // OpenTelemetry integration
    inngestMiddleware({
      name: "otel-middleware",
      init() {
        return {
          onFunctionRun({ ctx }) {
            return {
              beforeExecution() {
                // Create Span
              },
              afterExecution() {
                // Close Span
              },
            };
          },
        };
      },
    }),
  ],
});
```

```yaml
# K8s deployment for Inngest Agent service
apiVersion: apps/v1
kind: Deployment
metadata:
  name: inngest-agent-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: inngest-agent
  template:
    spec:
      containers:
        - name: agent
          image: registry.example.com/inngest-agent:latest
          ports:
            - containerPort: 3000
          env:
            - name: INNGEST_EVENT_KEY
              valueFrom:
                secretKeyRef:
                  name: inngest-credentials
                  key: event-key
            - name: INNGEST_SIGNING_KEY
              valueFrom:
                secretKeyRef:
                  name: inngest-credentials
                  key: signing-key
            - name: OPENAI_API_KEY
              valueFrom:
                secretKeyRef:
                  name: openai-credentials
                  key: api-key
          resources:
            requests:
              cpu: "250m"
              memory: "512Mi"
            limits:
              cpu: "1"
              memory: "2Gi"
```
## Durable Execution Semantics

### Core Guarantees

Durable Execution provides the following key guarantees:

```
1. Automatic Checkpointing:
   - Results are automatically persisted after each Step completes
   - Recovery from crashes resumes from the last successful Step
   - Already-completed Steps are not re-executed

2. Exactly-Once Semantics:
   - Side effects of each Step are executed only once
   - Idempotency is guaranteed by the framework
   - Developers do not need to manually implement retry deduplication

3. Unlimited Runtime:
   - Functions can run for days or months
   - Supports long-duration sleep
   - Not limited by process lifecycle

4. Transparent Recovery:
   - Developers do not need to write recovery logic
   - The framework automatically handles state reconstruction
   - Code executes from the beginning; Step results are returned from cache
```

### Prefect vs Inngest Comparison

```
Feature Comparison:

Persistence Mechanism:
  Prefect: Database-based state tracking
  Inngest: Event-log-based Step caching

Programming Model:
  Prefect: Python decorators, sync/async support
  Inngest: TypeScript/Python, event-driven

Deployment Model:
  Prefect: Self-hosted or Prefect Cloud
  Inngest: Fully managed (Inngest Cloud)

Use Cases:
  Prefect: Data-intensive, batch processing, traditional workflows
  Inngest: Event-driven, real-time response, Serverless

Agent Features:
  Prefect: Mature concurrency control and resource management
  Inngest: Native event waiting and Step Functions

Monitoring Capabilities:
  Prefect: Built-in UI, metrics, logs
  Inngest: Built-in UI, real-time tracing, debugging tools
```

## Integration with Agent Frameworks

### Prefect + LangChain

```python
from prefect import flow, task
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_openai import ChatOpenAI

@task(retries=2)
async def run_langchain_agent(
    query: str,
    agent_config: dict,
) -> dict:
    """Execute a LangChain Agent inside a Prefect Task"""
    llm = ChatOpenAI(
        model=agent_config.get("model", "gpt-4o"),
        temperature=0.1,
    )

    agent = create_openai_tools_agent(
        llm=llm,
        tools=agent_config["tools"],
        prompt=agent_config["prompt"],
    )

    executor = AgentExecutor(
        agent=agent,
        tools=agent_config["tools"],
        max_iterations=agent_config.get("max_iterations", 10),
        verbose=True,
    )

    result = await executor.ainvoke({"input": query})
    return {
        "output": result["output"],
        "intermediate_steps": [
            {
                "action": step[0].tool,
                "input": step[0].tool_input,
                "output": step[1],
            }
            for step in result.get("intermediate_steps", [])
        ],
    }


@flow(name="langchain-agent-flow")
async def langchain_agent_flow(
    query: str,
    config: dict,
) -> dict:
    """Prefect Flow wrapper for a LangChain Agent"""
    result = await run_langchain_agent(
        query=query,
        agent_config=config,
    )
    return result
```

### Inngest + OpenAI Assistants

```typescript
import { inngest } from "./client";

export const openaiAssistantAgent = inngest.createFunction(
  { id: "openai-assistant", name: "OpenAI Assistant Agent" },
  { event: "agent/assistant-requested" },
  async ({ event, step }) => {
    const { assistantId, query } = event.data;

    // Step 1: Create Thread
    const thread = await step.run("create-thread", async () => {
      return await openai.beta.threads.create({
        messages: [{ role: "user", content: query }],
      });
    });

    // Step 2: Create Run
    const run = await step.run("create-run", async () => {
      return await openai.beta.threads.runs.create(thread.id, {
        assistant_id: assistantId,
      });
    });

    // Step 3: Poll Run status (with timeout)
    let runStatus = run;
    while (runStatus.status !== "completed") {
      runStatus = await step.run(
        `poll-run-${runStatus.id}`,
        async () => {
          return await openai.beta.threads.runs.retrieve(
            thread.id,
            run.id
          );
        }
      );

      if (runStatus.status === "requires_action") {
        // Handle tool calls
        const toolCalls =
          runStatus.required_action.submit_tool_outputs.tool_calls;

        const toolOutputs = await Promise.all(
          toolCalls.map((tc, i) =>
            step.run(`tool-${i}`, async () => {
              const result = await executeTool(
                tc.function.name,
                JSON.parse(tc.function.arguments)
              );
              return {
                tool_call_id: tc.id,
                output: JSON.stringify(result),
              };
            })
          )
        );

        await step.run("submit-tool-outputs", async () => {
          return await openai.beta.threads.runs.submitToolOutputs(
            thread.id,
            run.id,
            { outputs: toolOutputs }
          );
        });
      }

      // Wait before polling again
      await step.sleep("poll-delay", "2s");
    }

    // Step 4: Retrieve final messages
    const messages = await step.run("get-messages", async () => {
      return await openai.beta.threads.messages.list(thread.id);
    });

    const assistantMessage = messages.data.find(
      (m) => m.role === "assistant"
    );

    return {
      output: assistantMessage?.content[0]?.text?.value,
      threadId: thread.id,
      runId: run.id,
    };
  }
);
```
## Key Production Practices

### Monitoring & Alerting

```python
# Prefect monitoring configuration
from prefect import flow
from prefect.runtime import flow_run

@flow(
    name="monitored-agent-flow",
    on_failure=[send_alert],
    on_completion=[log_metrics],
)
async def monitored_agent_flow(query: str) -> dict:
    """Agent Flow with monitoring"""
    # Record custom metrics
    from prometheus_client import Counter, Histogram

    agent_iterations = Counter(
        "agent_iterations_total",
        "Total agent iterations",
        ["agent_type", "status"],
    )

    agent_duration = Histogram(
        "agent_duration_seconds",
        "Agent execution duration",
        ["agent_type"],
    )

    with agent_duration.labels(agent_type="default").time():
        result = await agent_flow(query=query, system_prompt=DEFAULT_PROMPT)

    agent_iterations.labels(
        agent_type="default",
        status=result["status"],
    ).inc(result["iterations"])

    return result
```

### Deployment Checklist

```
Prefect/Inngest Agent Deployment Checklist:

Prefect:
  □ Prefect Server high-availability deployment or use Prefect Cloud
  □ Worker Pool configuration (CPU/Memory limits, concurrency limits)
  □ Work Queue priority settings (for different Agent types)
  □ Storage backend configuration (S3/GCS for Flow results)
  □ Secret management (via Prefect Blocks or K8s Secrets)
  □ Monitoring integration (Prometheus metrics, log aggregation)

Inngest:
  □ Inngest Cloud account configuration or self-hosted deployment
  □ Event Key and Signing Key management
  □ Function concurrency limit configuration
  □ Step timeout settings
  □ Error handling and Dead Letter Queue configuration
  □ Monitoring integration (Inngest Dashboard, Webhook alerting)

General:
  □ LLM API key management
  □ Rate limiting and quota management
  □ Cost tracking and budget alerting
  □ Log aggregation and structured logging
  □ Distributed tracing integration
```

---

*Prefect and Inngest provide complementary durable orchestration capabilities for Agent execution; the choice depends on whether the use case is event-driven vs. batch processing.*
