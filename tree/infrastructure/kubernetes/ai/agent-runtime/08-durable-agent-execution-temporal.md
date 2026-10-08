---
title: Temporal Durable Agent Execution
description: 'Temporal-based durable agent execution architecture: Workflow/Activity model, checkpoint recovery, Human-in-the-Loop, K8s deployment, and LLM framework integration'
summary: 'Temporal-based durable agent execution architecture: Workflow/Activity model, checkpoint recovery, Human-in-the-Loop, K8s deployment, and LLM framework integration'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- temporal
- durable-execution
- workflow
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
- What is Temporal durable agent execution
- How to build a durable agent with Temporal
- Temporal Workflow Agent best practices
trigger_keywords:
- temporal
- durable-execution
- agent-workflow
- checkpoint
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/08-durable-agent-execution-temporal.md
---
# Temporal Durable Agent Execution

## Overview

Temporal is a durable execution platform that provides two levels of abstraction — Workflow and Activity — naturally suited for building long-running AI Agents. Unlike traditional Agent frameworks, Temporal guarantees state persistence, fault recovery, and exactly-once semantics throughout execution, addressing the core challenge LLM Agents face in production: how to maintain reliability across Agent tasks that span hours or even days.

Traditional Agent execution models assume a continuously running process; if it crashes, all intermediate state is lost. Temporal records every operation as an immutable event through an Event Sourcing mechanism, allowing any failure to be recovered precisely from the last checkpoint. This guarantee is critical for complex Agent tasks that require multiple rounds of LLM calls, external tool interactions, and Human-in-the-Loop approvals.

## Workflow/Activity Model

### Core Abstractions

Temporal's programming model consists of two core concepts:

```
Workflow:
  - Orchestration logic executed deterministically
  - Defines the invocation order and control flow of Activities
  - State is persisted via Event History
  - Can run for days, months, or even years
  - Direct execution of side-effect operations is not allowed

Activity:
  - Executes actual side-effect operations (API calls, database reads/writes, LLM inference)
  - Can be retried, timed out, or cancelled
  - Idempotency is a key requirement
  - Supports the Heartbeat mechanism for reporting progress of long-running operations
```

### Agent as Workflow Pattern

Modelling an Agent as a Temporal Workflow is the core pattern for building durable Agents:

```python
from temporalio import workflow
from datetime import timedelta

@workflow.defn
class AgentWorkflow:
    """Main workflow for durable Agent execution"""

    def __init__(self):
        self.conversation_history = []
        self.tool_results = []
        self.iteration_count = 0

    @workflow.run
    async def run(self, agent_config: AgentConfig) -> AgentResult:
        max_iterations = agent_config.max_iterations or 20

        while self.iteration_count < max_iterations:
            # LLM inference - executed as an Activity, supports retries
            llm_response = await workflow.execute_activity(
                llm_inference,
                args=[agent_config.system_prompt, self.conversation_history],
                start_to_close_timeout=timedelta(seconds=120),
                retry_policy=RetryPolicy(
                    maximum_attempts=3,
                    initial_interval=timedelta(seconds=5),
                    backoff_coefficient=2.0,
                ),
            )

            # Parse the LLM response to determine whether tool calls are needed
            if llm_response.has_tool_calls:
                for tool_call in llm_response.tool_calls:
                    # Tool execution - may involve external systems
                    tool_result = await workflow.execute_activity(
                        execute_tool,
                        args=[tool_call.name, tool_call.arguments],
                        start_to_close_timeout=timedelta(seconds=300),
                        heartbeat_timeout=timedelta(seconds=30),
                    )
                    self.tool_results.append(tool_result)
                    self.conversation_history.append({
                        "role": "tool",
                        "content": tool_result.output,
                        "tool_call_id": tool_call.id,
                    })
            else:
                # Agent considers the task complete
                return AgentResult(
                    output=llm_response.content,
                    iterations=self.iteration_count,
                    tool_results=self.tool_results,
                )

            self.iteration_count += 1
            self.conversation_history.append({
                "role": "assistant",
                "content": llm_response.content,
            })

        return AgentResult(
            output="Maximum iteration limit reached",
            iterations=self.iteration_count,
            tool_results=self.tool_results,
            status="max_iterations_exceeded",
        )
```

### Activity Implementation Details

```python
from temporalio import activity

@activity.defn
async def llm_inference(
    system_prompt: str,
    conversation_history: list,
) -> LLMResponse:
    """Call the LLM for inference, with support for streaming responses and timeout control"""
    client = AsyncOpenAI()

    messages = [{"role": "system", "content": system_prompt}]
    messages.extend(conversation_history)

    # Heartbeat mechanism: report progress during long-running inference
    activity.heartbeat("Starting LLM inference")

    response = await client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=TOOL_DEFINITIONS,
        temperature=0.1,
    )

    activity.heartbeat("LLM inference complete")

    return LLMResponse(
        content=response.choices[0].message.content,
        has_tool_calls=response.choices[0].message.tool_calls is not None,
        tool_calls=response.choices[0].message.tool_calls or [],
        token_usage=response.usage,
    )


@activity.defn
async def execute_tool(
    tool_name: str,
    tool_arguments: dict,
) -> ToolResult:
    """Execute Agent tool calls, supporting multiple tool types"""
    activity.heartbeat(f"Executing tool: {tool_name}")

    tool_map = {
        "search_web": search_web_tool,
        "query_database": query_database_tool,
        "read_file": read_file_tool,
        "execute_code": execute_code_sandbox_tool,
    }

    handler = tool_map.get(tool_name)
    if not handler:
        return ToolResult(
            output=f"Unknown tool: {tool_name}",
            status="error",
        )

    try:
        result = await handler(**tool_arguments)
        return ToolResult(output=result, status="success")
    except Exception as e:
        return ToolResult(output=str(e), status="error")
```

## Checkpointing and Recovery

### Event Sourcing Mechanism

Temporal implements automatic checkpointing through Event History. Every decision made during a Workflow execution (Activity invocation, Timer creation, Signal sending) is recorded as an immutable event:

```
Example Event History:

Event 1: WorkflowExecutionStarted
  - Input: {agent_config: {...}}
  - Task Queue: agent-task-queue

Event 2: ActivityTaskScheduled
  - Activity: llm_inference
  - Arguments: [system_prompt, conversation_history]

Event 3: ActivityTaskCompleted
  - Result: LLMResponse{content: "...", has_tool_calls: true}

Event 4: ActivityTaskScheduled
  - Activity: execute_tool
  - Arguments: ["search_web", {"query": "kubernetes best practices"}]

Event 5: ActivityTaskCompleted
  - Result: ToolResult{output: "...", status: "success"}
```

### Recovery Process

When a Worker crashes, Temporal automatically performs recovery:

```python
# Worker startup - Temporal automatically recovers Workflow state from Event History
async def main():
    worker = Worker(
        client,
        task_queue="agent-task-queue",
        workflows=[AgentWorkflow],
        activities=[llm_inference, execute_tool],
        # Concurrency control
        max_concurrent_activities=10,
        max_concurrent_workflow_tasks=5,
    )
    await worker.run()
```

During recovery, the Workflow code executes from the beginning, but all Activity calls return cached results (because the Event History has already recorded their completed state). This guarantees determinism and prevents side effects from being executed again.

### Manual Checkpoints

For particularly long Agent executions, child Workflows can be created as manual checkpoints:

```python
@workflow.defn
class AgentSubtaskWorkflow:
    """Subtask workflow - serves as a checkpoint boundary"""

    @workflow.run
    async def run(self, subtask: SubtaskInput) -> SubtaskResult:
        result = await workflow.execute_activity(
            process_subtask,
            args=[subtask],
            start_to_close_timeout=timedelta(hours=1),
        )
        return result


@workflow.defn
class LongRunningAgentWorkflow:
    """Long-running Agent - uses subtasks as checkpoints"""

    @workflow.run
    async def run(self, task: ComplexTask) -> AgentResult:
        results = []

        for subtask in task.subtasks:
            # Each subtask is an independent child Workflow
            subtask_result = await workflow.execute_child_workflow(
                AgentSubtaskWorkflow.run,
                args=[subtask],
                id=f"{workflow.info().workflow_id}-subtask-{subtask.id}",
            )
            results.append(subtask_result)

        return AgentResult(subtask_results=results)
```
## Human-in-the-Loop Signals

### Signal Mechanism

Temporal's Signals allow external systems to send messages to running Workflows, making them ideal for implementing Human-in-the-Loop:

```python
@workflow.defn
class HumanInTheLoopAgentWorkflow:
    """Agent workflow with support for human intervention"""

    def __init__(self):
        self.human_feedback = None
        self.approval_received = False
        self.cancel_requested = False

    @workflow.signal
    async def provide_feedback(self, feedback: HumanFeedback):
        """Human provides feedback or corrections"""
        self.human_feedback = feedback

    @workflow.signal
    async def approve(self, approval: ApprovalDecision):
        """Human approval decision"""
        self.approval_received = True
        self.approval_decision = approval

    @workflow.signal
    async def cancel(self):
        """Cancel Agent execution"""
        self.cancel_requested = True

    @workflow.query
    def get_status(self) -> AgentStatus:
        """Query the Agent's current status"""
        return AgentStatus(
            iteration=self.iteration_count,
            current_step=self.current_step,
            waiting_for_human=self.waiting_for_human,
            conversation_length=len(self.conversation_history),
        )

    @workflow.run
    async def run(self, config: AgentConfig) -> AgentResult:
        while not self.cancel_requested:
            # LLM inference
            llm_response = await workflow.execute_activity(
                llm_inference,
                args=[config.system_prompt, self.conversation_history],
                start_to_close_timeout=timedelta(seconds=120),
            )

            # Check whether human approval is required
            if self._needs_human_approval(llm_response):
                self.waiting_for_human = True

                # Wait for human feedback with a timeout
                try:
                    await workflow.wait_condition(
                        lambda: self.approval_received or self.human_feedback,
                        timeout=timedelta(hours=24),
                    )
                except asyncio.TimeoutError:
                    return AgentResult(
                        status="human_approval_timeout",
                        output="Timed out waiting for human approval",
                    )

                self.waiting_for_human = False

                # Handle the human decision
                if self.approval_received:
                    if not self.approval_decision.approved:
                        return AgentResult(
                            status="rejected_by_human",
                            output=self.approval_decision.reason,
                        )
                elif self.human_feedback:
                    # Add human feedback to the conversation history
                    self.conversation_history.append({
                        "role": "user",
                        "content": self.human_feedback.message,
                    })

            # Continue normal execution...
            self.conversation_history.append({
                "role": "assistant",
                "content": llm_response.content,
            })

        return AgentResult(status="cancelled")
```

### Query Mechanism

Queries allow external systems to read Workflow state without affecting execution:

```python
# Client queries Agent status
async def monitor_agent(client: Client, workflow_id: str):
    handle = client.get_workflow_handle(workflow_id)

    while True:
        status = await handle.query(HumanInTheLoopAgentWorkflow.get_status)
        print(f"Agent status: iteration={status.iteration}, "
              f"current_step={status.current_step}, "
              f"waiting_for_human={status.waiting_for_human}")

        if status.waiting_for_human:
            print("Agent is waiting for human approval")
            # Trigger alert notification

        await asyncio.sleep(10)
```

## Timeout and Retry Strategies

### Multi-Level Timeouts

```python
# Workflow-level timeout
@workflow.defn
class BoundedAgentWorkflow:
    @workflow.run
    async def run(self, config: AgentConfig) -> AgentResult:
        # Set an upper bound on the total Workflow execution time
        # Controlled via start_to_close_timeout or schedule_to_close_timeout
        pass

# Set timeouts when starting the Workflow
await client.execute_workflow(
    BoundedAgentWorkflow.run,
    config,
    id="agent-task-001",
    task_queue="agent-queue",
    execution_timeout=timedelta(hours=2),  # Total Workflow timeout
    run_timeout=timedelta(hours=1),         # Single-run timeout
    task_timeout=timedelta(seconds=30),     # Single Decision Task timeout
)
```

### Activity Retry Policy

```python
from temporalio.common import RetryPolicy

# LLM inference retry - exponential backoff
llm_retry_policy = RetryPolicy(
    maximum_attempts=5,
    initial_interval=timedelta(seconds=2),
    backoff_coefficient=2.0,
    maximum_interval=timedelta(seconds=60),
    # Error types that should not be retried
    non_retryable_error_types=[
        "InvalidAPIKeyError",
        "ContentFilterError",
    ],
)

# Tool execution retry - more conservative policy
tool_retry_policy = RetryPolicy(
    maximum_attempts=3,
    initial_interval=timedelta(seconds=5),
    backoff_coefficient=1.5,
    maximum_interval=timedelta(seconds=30),
    non_retryable_error_types=[
        "InvalidToolArgumentsError",
        "ToolNotFoundError",
    ],
)
```

### Heartbeat Mechanism

For long-running Activities, heartbeats prevent them from being incorrectly flagged as timed out:

```python
@activity.defn
async def execute_long_running_tool(
    tool_name: str,
    arguments: dict,
) -> ToolResult:
    """Long-running tool execution that sends periodic heartbeats"""
    for step in execute_tool_steps(tool_name, arguments):
        # Check whether a cancellation has been requested
        if activity.is_cancelled():
            return ToolResult(status="cancelled")

        # Send a heartbeat to report progress
        activity.heartbeat(f"Processing step: {step.name}")

        result = await step.execute()
        if result.should_abort:
            return ToolResult(
                output=result.error,
                status="aborted",
            )

    return ToolResult(output="Done", status="success")
```
## K8s Deployment of Temporal Server

### Helm Deployment

```yaml
# temporal-values.yaml
server:
  image:
    repository: temporalio/auto-setup
    tag: 1.24.0

  config:
    persistence:
      default:
        driver: "sql"
        sql:
          driver: "postgres"
          host: "temporal-postgresql"
          port: 5432
          database: "temporal"
          user: "temporal"
          existingSecret: "temporal-db-credentials"

      visibility:
        driver: "sql"
        sql:
          driver: "postgres"
          host: "temporal-postgresql"
          port: 5432
          database: "temporal_visibility"
          user: "temporal"
          existingSecret: "temporal-db-credentials"

  resources:
    requests:
      cpu: "500m"
      memory: "512Mi"
    limits:
      cpu: "2"
      memory: "2Gi"

  replicas: 2

web:
  enabled: true
  replicas: 2
  ingress:
    enabled: true
    className: "nginx"
    hosts:
      - temporal.example.com

prometheus:
  enabled: true
  serviceMonitor:
    enabled: true

postgresql:
  enabled: true
  auth:
    existingSecret: "temporal-db-credentials"
  primary:
    persistence:
      size: 50Gi
```

### Agent Worker Deployment

```yaml
# agent-worker-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: agent-worker
  namespace: temporal
spec:
  replicas: 3
  selector:
    matchLabels:
      app: agent-worker
  template:
    metadata:
      labels:
        app: agent-worker
    spec:
      serviceAccountName: agent-worker-sa
      containers:
        - name: worker
          image: registry.example.com/agent-worker:latest
          env:
            - name: TEMPORAL_ADDRESS
              value: "temporal-frontend.temporal:7233"
            - name: TEMPORAL_NAMESPACE
              value: "agent-namespace"
            - name: TASK_QUEUE
              value: "agent-task-queue"
            - name: OPENAI_API_KEY
              valueFrom:
                secretKeyRef:
                  name: openai-credentials
                  key: api-key
            - name: MAX_CONCURRENT_ACTIVITIES
              value: "10"
            - name: MAX_CONCURRENT_WORKFLOWS
              value: "5"
          resources:
            requests:
              cpu: "500m"
              memory: "1Gi"
            limits:
              cpu: "2"
              memory: "4Gi"
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: agent-worker-hpa
  namespace: temporal
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: agent-worker
  minReplicas: 2
  maxReplicas: 20
  metrics:
    - type: Pods
      pods:
        metric:
          name: temporal_workflow_task_queue_length
        target:
          type: AverageValue
          averageValue: "5"
```

## Integration with LangGraph/CrewAI

### Temporal + LangGraph

```python
from langgraph.graph import StateGraph, END
from temporalio import workflow, activity

@workflow.defn
class LangGraphAgentWorkflow:
    """Wraps LangGraph graph execution as a Temporal Workflow"""

    @workflow.run
    async def run(self, input_data: AgentInput) -> AgentResult:
        # LangGraph's state graph executes step by step within Temporal
        state = {"messages": [HumanMessage(content=input_data.query)]}

        # Each node executes as an independent Activity
        current_node = "agent"

        while current_node != END:
            if current_node == "agent":
                state = await workflow.execute_activity(
                    agent_node_activity,
                    args=[state],
                    start_to_close_timeout=timedelta(seconds=120),
                )
            elif current_node == "tools":
                state = await workflow.execute_activity(
                    tools_node_activity,
                    args=[state],
                    start_to_close_timeout=timedelta(seconds=300),
                )
            elif current_node == "human_review":
                # Wait for human approval
                await workflow.wait_condition(
                    lambda: self.human_approved,
                    timeout=timedelta(hours=24),
                )

            current_node = state.get("next_node", END)

        return AgentResult(
            output=state["messages"][-1].content,
            state=state,
        )
```

### Temporal + CrewAI

```python
@workflow.defn
class CrewAIAgentWorkflow:
    """CrewAI multi-agent collaborative workflow"""

    @workflow.run
    async def run(self, crew_config: CrewConfig) -> CrewResult:
        task_results = []

        for task in crew_config.tasks:
            # Select the appropriate Agent for each task
            agent_config = crew_config.agents[task.agent_role]

            # Execute the Agent task
            result = await workflow.execute_activity(
                execute_agent_task,
                args=[agent_config, task, task_results],
                start_to_close_timeout=timedelta(minutes=30),
                retry_policy=RetryPolicy(maximum_attempts=2),
            )

            task_results.append({
                "task": task.description,
                "agent": agent_config.role,
                "result": result.output,
            })

            # CrewAI-style context passing
            # Subsequent tasks can see the results of previous tasks

        return CrewResult(task_results=task_results)
```
## Production Practice Key Points

### Observability Integration

```python
# Integrate with OpenTelemetry tracing
from opentelemetry import trace

@activity.defn
async def traced_llm_inference(
    system_prompt: str,
    messages: list,
) -> LLMResponse:
    tracer = trace.get_tracer("agent-temporal")

    with tracer.start_as_current_span("llm_inference") as span:
        span.set_attribute("model", "gpt-4o")
        span.set_attribute("message_count", len(messages))

        response = await call_llm(system_prompt, messages)

        span.set_attribute("tokens_used", response.token_usage.total_tokens)
        span.set_attribute("finish_reason", response.finish_reason)

        return response
```

### Deployment Checklist

```
Temporal Agent Deployment Checklist:

□ Temporal Server high-availability deployment (at least 2 Frontend, 2 History, 2 Matching)
□ PostgreSQL primary-replica replication or cloud-managed database
□ Agent Worker horizontal auto-scaling configuration
□ Worker resource limits (CPU/Memory) set according to LLM concurrency requirements
□ Secret management (API Keys injected via K8s Secrets)
□ Network policies (Workers can only access necessary external services)
□ Monitoring and alerting (Workflow failure rate, Activity timeout rate, queue depth)
□ Log aggregation (structured logs, correlated with WorkflowID)
□ Disaster recovery plan (Temporal supports cross-datacenter replication)
```

---

*Temporal provides production-grade durable execution guarantees for LLM Agents, upgrading Agents from a fragile in-memory state model to a reliable durable execution model.*
