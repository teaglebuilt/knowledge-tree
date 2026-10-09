---
title: Agent Harness Loop deeply designed with the execution engine (domain-14-ai-ml-infra)
description: 'title: Agent Harness Loop deeply designed with the execution engine'
summary: 'title: Agent Harness Loop deeply designed with the execution engine'
category: general
tags:
- ai
- ai-agent
- prometheus
- llm
- rag
- agent
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 35min
intent_queries:
- Agent Harness Loop with Execution Engine Deep Design Is
- How to Deeply Design Agent Harness Loop and Execution Engine
- Kubernetes 14 ai ml infra best practices
trigger_keywords:
- Agent
- Harness
- Loop
- Deep Design with Execution Engine
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- prometheus-basics
- logging-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/31-agent-harness-loop-execution.md
---

> **Production Environment Security Reminders**
>
> Commands included in this document are executable directly. Before executing, please confirm: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/ReadOnly (information gathering with no side effects).




title: Agent Harness Loop and Execution Engine Deep Design
description: '# Agent Harness Loop and Execution Engine Deep Design'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- [[Prometheus|prometheus]]
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- Architect
- SRE
estimated_read_time: 5min
intent_queries:
- What is Agent Harness Loop and Execution Engine Deep Design
- How to do Agent Harness Loop and Execution Engine Deep Engine Design
trigger_keywords:
- Agent
- Harness
- Loop
- Execution Engine Deep Design
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

# Agent Harness Loop and Execution Engine Deep Design

> **Document Type**: Harness Engineering Deep Dive Series | **Last Updated**: 2026-04 | **Keywords**: Agent Loop, Execution Engine, State Machine, ReAct Loop, Anti-drift, Timeout Protection, Asynchronous Execution, Finite State Machine, Trajectory, Execution Strategy

---

## Overview

Loop (loop layer) is the first layer of the six-layer architecture in Agent Harness and also the heart of Harness's execution. It determines how an Agent observes, thinks, acts, and when it terminates. A well-designed loop layer not only drives the Agent to complete tasks but also handles exceptions, drift detection, resource management, and records the execution trajectory.

This document delves into the deep design of the state machine model, execution strategy, anti-drift algorithm, concurrent control, fault recovery mechanism, and full implementation in Kubernetes operational scenarios.

---

## 1. Core Model of Loop Layer

## 1.1 Finite State Machine (FSM) Model

The essence of Agent Loop is a finite state machine. Each iteration of the loop transfers between the following states:

```
Agent Loop Finite State Machine:

INIT ──→ OBSERVE ──→ THINK ──→ DECIDE
                                  │
                        ┌─────────┴─────────┐
                        ▼                   ▼
                      ACT                FINALIZE
                        │                   │
                        ▼                   ▼
                   OBSERVE_RESULT        OUTPUT
                        │
                        ▼
                    EVALUATE
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
          CONTINUE              TERMINATE
              │                   │
              └──→ OBSERVE        ▼
                               OUTPUT

Termination Conditions:
  - Task completion (Agent determines is_final_answer)
  - Timeout (wall-clock timeout)
  - max_iterations (iteration limit)
  - wirl detection(drift detected)
  - constraint violation
  - unrecoverable error
```

## 1.2 State Definition and Transition Rules

```python
from enum import Enum, auto
from dataclasses import dataclass, field
from typing import Optional, Any
import time

class LoopState(Enum):
    """Agent Loop Status Enum"""
    INIT = auto()
    OBSERVE = auto()
    THINK = auto()
    DECIDE = auto()
    ACT = auto()
    OBSERVE_RESULT = auto()
    EVALUATE = auto()
    FINALIZE = auto()
    TERMINATED = auto()

@dataclass
class LoopStep:
    """Step Execution Record"""
    iteration: int
    state: LoopState
    timestamp: float
    thought: Optional[str] = None
    action: Optional[dict] = None
    observation: Optional[str] = None
    tool_call: Optional[dict] = None
    tool_result: Optional[dict] = None
    tokens_used: int = 0
    latency_ms: float = 0.0
    metadata: dict = field(default_factory=dict)

class TerminationReason(Enum):
    """Termination Reason Enum"""
    TASK_COMPLETE = "task_complete"
    TIMEOUT = "timeout"
    MAX_ITERATIONS = "max_iterations"
    DRIFT_DETECTED = "drift_detected"
    CONSTRAINT_VIOLATION = "constraint_violation"
    UNRECOVERABLE_ERROR = "unrecoverable_error"
    HUMAN_INTERRUPT = "human_interrupt"
    COST_BUDGET_EXCEEDED = "cost_budget_exceeded"
```

---

## 2. Execution Engine Architecture

## 2.1 Core Execution Engine Implementation

```python
import asyncio
import logging
from typing import Callable

logger = logging.getLogger("agent.loop")

class ExecutionEngine:
    """Core Execution Engine of Agent"""

    职责：
    1. 驱动 Agent Loop 的状态转移
    2. 管理执行生命周期（启动、暂停、恢复、终止）
    3. 记录完整执行轨迹
    4. 强制执行终止条件
    """

    def __init__(
        self,
        llm,
        tools,
        context_manager,
        constraint_enforcer,
        max_iterations: int = 20,
        timeout_seconds: int = 300,
        think_budget_ratio: float = 0.6,
    ):
        self.llm = llm
        self.tools = tools
        self.context_mgr = context_manager
        self.constraints = constraint_enforcer
        self.max_iterations = max_iterations
        self.timeout_seconds = timeout_seconds
        self.think_budget_ratio = think_budget_ratio

        # Execution Status
        self._state = LoopState.INIT
        self._trajectory: list[LoopStep] = []
        self._start_time: float = 0
        self._total_tokens: int = 0
        self._is_paused: bool = False

        # Callback Hooks
        self._on_step_complete: list[Callable] = []
        self._on_terminate: list[Callable] = []

    def run(self, task: str, initial_context: dict = None) -> dict:
        """Synchronous Execution of Agent Loop"""
        self._state = LoopState.INIT
        self._start_time = time.time()
        self._trajectory = []
        iteration = 0

        # Initial Context Construction
        context = self.context_mgr.build_context(task, initial_context)

        while iteration < self.max_iterations:
            # Termination Condition Check
            termination = self._check_termination_conditions(iteration)
            if termination:
                return self._build_result(termination, iteration)

            # Pause Check (Supports manual intervention)
            if self._is_paused:
                self._wait_for_resume()

            step_start = time.time()

            # OBSERVE: Collect current state
            self._state = LoopState.OBSERVE
            observation = self._observe(task, context, iteration)

            # THINK: LLM Inference
            self._state = LoopState.THINK
            thought = self._think(observation, iteration)

            # DECIDE: Determine if action is needed
            self._state = LoopState.DECIDE
            if thought.is_final_answer:
                self._state = LoopState.FINALIZE
                return self._build_result(
                    TerminationReason.TASK_COMPLETE,
                    iteration + 1,
                    answer=thought.answer,
                )

            # ACT: Invoke tool call
            self._state = LoopState.ACT
            action_result = self._act(thought.action, iteration)

            # OBSERVE_RESULT: Observe tool result
            self._state = LoopState.OBSERVE_RESULT
            context = self._update_context(context, thought, action_result)

            # EVALUATE: Evaluate whether to continue
            self._state = LoopState.EVALUATE
            step = LoopStep(
                iteration=iteration,
                state=self._state,
                timestamp=time.time(),
                thought=thought.reasoning,
                action=thought.action,
                tool_result=action_result,
                tokens_used=thought.tokens_used,
                latency_ms=(time.time() - step_start) * 1000,
            )
            self._trajectory.append(step)

            # Trigger Step Completion Callback
            for callback in self._on_step_complete:
                callback(step)

            iteration += 1

        return self._build_result(TerminationReason.MAX_ITERATIONS, iteration)

    def _check_termination_conditions(self, iteration: int) -> Optional[TerminationReason]:
        """Check all termination conditions"""
        # Timeout Check
        elapsed = time.time() - self._start_time
        if elapsed > self.timeout_seconds:
            logger.warning(f"Timeout after {elapsed:.1f}s (limit: {self.timeout_seconds}s)")
            return TerminationReason.TIMEOUT

        # Cost Budget Check
        allowed, reason = self.constraints.check_budget(self._total_tokens)
        if not allowed:
            logger.warning(f"Budget exceeded: {reason}")
            return TerminationReason.COST_BUDGET_EXCEEDED

        # drift detection
        if self._detect_drift():
            logger.warning("Drift detected in agent loop")
            return TerminationReason.DRIFT_DETECTED

        return None

    def _build_result(
        self,
        reason: TerminationReason,
        iterations: int,
        answer: str = None,
    ) -> dict:
        """build execution result"""
        elapsed = time.time() - self._start_time
        result = {
            "status": reason.value,
            "answer": answer,
            "iterations": iterations,
            "total_tokens": self._total_tokens,
            "elapsed_seconds": elapsed,
            "trajectory": self._trajectory,
            "termination_reason": reason.value,
        }

        # trigger termination callback
        for callback in self._on_terminate:
            callback(result)

        return result
```

## 2.2 Asynchronous Execution Engine

Within production environments, Agents typically need to handle multiple tasks concurrently or parallel calls to multiple tools:

```python
class AsyncExecutionEngine:
    """asynchronous execution engine: supports concurrent tool calls and non-blocking execution"""

    def __init__(self, llm, tools, max_concurrent_tools: int = 3, **kwargs):
        self.llm = llm
        self.tools = tools
        self.max_concurrent_tools = max_concurrent_tools
        self._semaphore = asyncio.Semaphore(max_concurrent_tools)

    async def run(self, task: str) -> dict:
        """asynchronous agent loop"""
        trajectory = []
        iteration = 0

        while iteration < self.max_iterations:
            # asynchronous LLM inference
            thought = await self._async_think(task, trajectory)

            if thought.is_final_answer:
                return {"status": "success", "answer": thought.answer,
                        "trajectory": trajectory}

            # parallel tool calls (if agent requests multiple tools)
            if thought.parallel_actions:
                results = await self._execute_parallel(thought.parallel_actions)
            else:
                results = [await self._execute_single(thought.action)]

            trajectory.append({
                "iteration": iteration,
                "thought": thought.reasoning,
                "actions": thought.parallel_actions or [thought.action],
                "results": results,
            })
            iteration += 1

        return {"status": "max_iterations", "trajectory": trajectory}

    async def _execute_parallel(self, actions: list) -> list:
        """parallel execution of multiple tool calls"""
        async def _execute_with_semaphore(action):
            async with self._semaphore:
                return await self._execute_single(action)

        tasks = [_execute_with_semaphore(a) for a in actions]
        return await asyncio.gather(*tasks, return_exceptions=True)

    async def _execute_single(self, action: dict) -> dict:
        """execute single tool call (with timeout protection)"""
        tool_name = action.get("tool")
        tool_args = action.get("args", {})

        try:
            result = await asyncio.wait_for(
                self.tools.async_execute(tool_name, tool_args),
                timeout=30.0,  # 单工具调用 30s 超时
            )
            return {"success": True, "result": result}
        except asyncio.TimeoutError:
            return {"success": False, "error": f"Tool {tool_name} timed out (30s)"}
        except Exception as e:
            return {"success": False, "error": str(e)}
```

---

## 3. Drift Detection Algorithm

## 3.1 Classification of Drift Types

During execution, Agents may fall into various drift modes:

```
# 🟢 Low-risk: read-only/information collection, typically with no side effects
Agent Drift Type Classification:

1. Action Repetition Drift
   Agent repeatedly executes identical actions
   Example: Execute kubectl get pods five times consecutively
   Detection: same action for N consecutive times

2. Content Loop Drift
   Agent repeatedly edits the same file/resource
   Example: modify YAML → error → rollback → modify → error → rollback
   Detection: Loop pattern of target action

3. Semantic Stagnation Drift
   Agent's reasoning has no substantive progress
   Example: content for each round of thinking is highly similar but does not progress
   Detection: Consider semantic similarity of content > Threshold

4. Error Loop Drift
   Agent repeatedly encounters the same error but cannot resolve it
   Example: Continuously encountering permission errors without changing policies
   Detection: Same error type occurs consecutively N times

5. Goal Deviation Drift
   Agent's actions become increasingly deviated from the original goal
   Example: Diagnosing Pod issues starts optimizing node network
   Detection: Semantic distance between actions and goals increases
```
## 3.2 Multi-dimensional Drift Detector

```python
from collections import Counter
import hashlib

class DriftDetector:
    """multi-dimensional drift detector"""

    def __init__(
        self,
        action_window: int = 3,
        error_window: int = 4,
        similarity_threshold: float = 0.92,
        max_same_target_edits: int = 3,
    ):
        self.action_window = action_window
        self.error_window = error_window
        self.similarity_threshold = similarity_threshold
        self.max_same_target_edits = max_same_target_edits

    def detect(self, trajectory: list) -> Optional[dict]:
        """multi-dimensional drift detection"""
        if len(trajectory) < self.action_window:
            return None

        # detection 1: action repetition drift
        action_drift = self._detect_action_repetition(trajectory)
        if action_drift:
            return action_drift

        # detection 2: content cyclic drift
        content_drift = self._detect_content_loop(trajectory)
        if content_drift:
            return content_drift

        # detection 3: error cyclic drift
        error_drift = self._detect_error_loop(trajectory)
        if error_drift:
            return error_drift

        # detection 4: semantic stagnation drift
        semantic_drift = self._detect_semantic_stagnation(trajectory)
        if semantic_drift:
            return semantic_drift

        return None

    def _detect_action_repetition(self, trajectory: list) -> Optional[dict]:
        """detect continuous identical actions"""
        recent = trajectory[-self.action_window:]
        action_hashes = [
            hashlib.md5(str(step.get("action", "")).encode()).hexdigest()
            for step in recent
        ]
        if len(set(action_hashes)) == 1:
            return {
                "type": "action_repetition",
                "severity": "high",
                "message": f"Continuous {self.action_window} executions of the same action",
                "repeated_action": recent[-1].get("action"),
                "recommendation": "Switch strategy or request manual intervention",
            }
        return None

    def _detect_content_loop(self, trajectory: list) -> Optional[dict]:
        """detect edit cyclic (A→B→A→B pattern)"""
        if len(trajectory) < 4:
            return None

        recent = trajectory[-6:]
        targets = [step.get("action", {}).get("target", "") for step in recent]
        target_counts = Counter(targets)
        for target, count in target_counts.items():
            if target and count >= self.max_same_target_edits:
                return {
                    "type": "content_loop",
                    "severity": "medium",
                    "message": f"Repeated operations on the same target '{target}' {count} times",
                    "target": target,
                    "recommendation": "Check if the operation produces expected results",
                }
        return None

    def _detect_error_loop(self, trajectory: list) -> Optional[dict]:
        """detect continuous identical errors"""
        recent = trajectory[-self.error_window:]
        errors = [
            step.get("tool_result", {}).get("error", "")
            for step in recent
            if step.get("tool_result", {}).get("error")
        ]
        if len(errors) >= self.error_window:
            error_hashes = [hashlib.md5(e.encode()).hexdigest() for e in errors]
            if len(set(error_hashes)) <= 2:  # 最多 2 种错误类型
                return {
                    "type": "error_loop",
                    "severity": "high",
                    "message": f"Continuous {len(errors)} occurrences of the same/similar errors",
                    "errors": errors[-2:],
                    "recommendation": "Need to switch diagnostic strategy or upgrade handling",
                }
        return None

    def _detect_semantic_stagnation(self, trajectory: list) -> Optional[dict]:
        """detect semantic stagnation (highly similar inference content but no progress)"""
        if len(trajectory) < 4:
            return None

        recent_thoughts = [
            step.get("thought", "")
            for step in trajectory[-4:]
            if step.get("thought")
        ]
        if len(recent_thoughts) < 3:
            return None

        # Use simple Jaccard similarity (production environment recommends embedding similarity)
        similarities = []
        for i in range(len(recent_thoughts) - 1):
            sim = self._jaccard_similarity(recent_thoughts[i], recent_thoughts[i + 1])
            similarities.append(sim)

        avg_sim = sum(similarities) / len(similarities)
        if avg_sim > self.similarity_threshold:
            return {
                "type": "semantic_stagnation",
                "severity": "medium",
                "message": f"Inference content similarity {avg_sim:.2f} exceeds threshold",
                "recommendation": "Inject new information or rebuild the problem",
            }
        return None

    @staticmethod
    def _jaccard_similarity(text1: str, text2: str) -> float:
        """Jaccard text similarity"""
        set1 = set(text1.split())
        set2 = set(text2.split())
        if not set1 or not set2:
            return 0.0
        intersection = set1 & set2
        union = set1 | set2
        return len(intersection) / len(union)
```

## 3.3 Drift Recovery Strategy

```python
class DriftRecoveryStrategy:
    """drift recovery strategy"""

    def __init__(self, llm, max_recovery_attempts: int = 2):
        self.llm = llm
        self.max_recovery_attempts = max_recovery_attempts

    def recover(self, drift_info: dict, trajectory: list, task: str) -> dict:
        """Choose recovery strategy based on drift type"""
        drift_type = drift_info["type"]

        strategies = {
            "action_repetition": self._strategy_reframe,
            "content_loop": self._strategy_backtrack,
            "error_loop": self._strategy_alternative_tools,
            "semantic_stagnation": self._strategy_inject_context,
        }

        strategy = strategies.get(drift_type, self._strategy_reframe)
        return strategy(drift_info, trajectory, task)

    def _strategy_reframe(self, drift_info, trajectory, task) -> dict:
        """Redesign strategy: have Agents re-understand the task"""
        recovery_prompt = f"""
        你在执行任务时陷入了重复循环。请停下来重新分析：
        
        原始任务: {task}
        已执行步骤: {len(trajectory)}
        问题: {drift_info['message']}
        
        请用完全不同的方法重新思考这个任务。不要重复之前的动作。
        """
        return {"strategy": "reframe", "prompt": recovery_prompt}

    def _strategy_backtrack(self, drift_info, trajectory, task) -> dict:
        """Rollback strategy: go back to the last successful state"""
        last_success = None
        for step in reversed(trajectory):
            if step.get("tool_result", {}).get("success"):
                last_success = step
                break
        return {
            "strategy": "backtrack",
            "restore_point": last_success,
            "prompt": "Restart from the previous successful state and try different paths",
        }

    def _strategy_alternative_tools(self, drift_info, trajectory, task) -> dict:
        """Replacement tool strategy: exclude failed tools"""
        failed_tools = set()
        for step in trajectory[-4:]:
            if not step.get("tool_result", {}).get("success"):
                failed_tools.add(step.get("action", {}).get("tool"))
        return {
            "strategy": "alternative_tools",
            "excluded_tools": list(failed_tools),
            "prompt": f"Below tools are currently unavailable: {failed_tools}, please complete the task using other tools",
        }

    def _strategy_inject_context(self, drift_info, trajectory, task) -> dict:
        """Context injection strategy: supplement new information to break stagnation"""
        return {
            "strategy": "inject_context",
            "prompt": "Consider the task from different angles, reconsidering previously overlooked information and methods",
            "additional_context": "Provide environmental information or related documents",
        }
```

---

## 4. Execution Strategy Patterns

## 4.1 Classification of Strategy Patterns

```
Agent executes strategy classification:

1. Sequential Execution Strategy
   Steps are executed in strict sequence
   Applicable: Standard processes driven by SOPs
   Example: Pod diagnostic SOP

2. Adaptive Execution Strategy
   Adjusts the next step dynamically based on each step's result
   Applicable: Exploratory tasks
   Example: Root cause analysis of unknown problems

3. Branching Execution Strategy
   Forks at critical decision points and explores multiple paths concurrently
   applicable: diagnosis for multiple possible reasons
   Example: check network, storage, scheduling simultaneously

4. Phased Execution Strategy (Phased)
   Divided into information gathering, analysis, and action phases
   applicable: complex operational tasks
   Example: Large-scale problem resolution

5. Recursive Execution Strategy (Recursive)
   Decomposes large tasks into subtasks and executes recursively
   applicable: multi-cluster batch operation
   Example: Cross-cluster upgrade
```

## 4.2 Phased Execution Engine

```python
class PhasedExecutionEngine:
    """Phased execution engine: divide tasks into collection→analysis→action three phases"""

    def __init__(self, llm, tools, phase_configs: dict = None):
        self.llm = llm
        self.tools = tools
        self.phase_configs = phase_configs or {
            "gather": {"max_steps": 5, "tools": ["kubectl_get", "kubectl_describe",
                                                   "kubectl_logs", "kubectl_events"]},
            "analyze": {"max_steps": 3, "tools": ["prometheus_query", "loki_search"]},
            "act": {"max_steps": 5, "tools": ["kubectl_apply", "kubectl_patch"],
                    "require_approval": True},
        }

    def run(self, task: str) -> dict:
        """Three-phase execution"""
        results = {}

        # Phase 1: Information Collection
        gather_result = self._execute_phase(
            "gather", task,
            system_prompt="You are in the information gathering phase. Collect only information without making any modifications."
        )
        results["gather"] = gather_result

        # Phase 2: Analysis and Reasoning
        analysis_context = self._build_analysis_context(gather_result)
        analyze_result = self._execute_phase(
            "analyze", task,
            context=analysis_context,
            system_prompt="Analyze the information collected to determine the root cause and repair plan."
        )
        results["analyze"] = analyze_result

        # Phase 3: Execution Repair (requires approval)
        if analyze_result.get("action_plan"):
            act_result = self._execute_phase(
                "act", task,
                context=analyze_result,
                system_prompt="Execute the repair operations according to the plan from the analysis phase."
            )
            results["act"] = act_result

        return results

    def _execute_phase(self, phase: str, task: str,
                       context: dict = None, system_prompt: str = None) -> dict:
        """Execute single phase"""
        config = self.phase_configs[phase]
        available_tools = [
            t for t in self.tools if t.name in config.get("tools", [])
        ]

        engine = ExecutionEngine(
            llm=self.llm,
            tools=available_tools,
            max_iterations=config["max_steps"],
        )

        return engine.run(task, initial_context=context)
```

---

## 5. Trajectory Management

## 5.1 Trajectory Data Model

```python
from dataclasses import dataclass, field
from typing import Optional, Any
from datetime import datetime
import json

@dataclass
class TrajectoryEntry:
    """Trajectory entry: record each step of the Agent"""
    step_id: str
    iteration: int
    timestamp: str
    phase: str                       # gather / analyze / act
    thought: str                     # Agent 的推理过程
    action: Optional[dict]           # 执行的动作
    observation: Optional[str]       # 观察到的结果
    tool_name: Optional[str]         # 使用的工具
    tool_args: Optional[dict]        # 工具参数
    tool_result: Optional[Any]       # 工具返回结果
    tool_success: bool = True
    tokens_input: int = 0
    tokens_output: int = 0
    latency_ms: float = 0.0
    is_key_step: bool = False        # 标记关键步骤
    error: Optional[str] = None

@dataclass
class ExecutionTrajectory:
    """Complete execution trajectory"""
    task_id: str
    task: str
    start_time: str
    end_time: Optional[str] = None
    status: str = "running"
    entries: list[TrajectoryEntry] = field(default_factory=list)
    total_tokens: int = 0
    total_cost_usd: float = 0.0
    termination_reason: Optional[str] = None

    def add_entry(self, entry: TrajectoryEntry):
        """Add trajectory entry"""
        self.entries.append(entry)
        self.total_tokens += entry.tokens_input + entry.tokens_output

    def get_key_steps(self) -> list:
        """Retrieve key steps (for historical compression)"""
        return [e for e in self.entries if e.is_key_step]

    def get_error_steps(self) -> list:
        """Retrieve error steps (for failure analysis)"""
        return [e for e in self.entries if e.error]

    def to_summary(self) -> str:
        """Generate trajectory summary (for logs/auditing)"""
        lines = [f"Task: {self.task}", f"Status: {self.status}",
                 f"Steps: {len(self.entries)}", f"Tokens: {self.total_tokens}"]
        for entry in self.entries:
            tool_info = f" [{entry.tool_name}]" if entry.tool_name else ""
            status = "✓" if entry.tool_success else "✗"
            lines.append(f"  {status} Step {entry.iteration}{tool_info}: "
                        f"{entry.thought[:80]}...")
        return "\n".join(lines)

    def export_json(self) -> str:
        """Export to JSON (for storage/analytics)"""
        return json.dumps({
            "task_id": self.task_id,
            "task": self.task,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "status": self.status,
            "total_tokens": self.total_tokens,
            "total_cost_usd": self.total_cost_usd,
            "termination_reason": self.termination_reason,
            "entries": [vars(e) for e in self.entries],
        }, indent=2, ensure_ascii=False)
```

## 5.2 Trajectory Analysis and Optimization

```python
class TrajectoryAnalyzer:
    """Trace Analyzer: Extract optimization insights from historical executions"""

    def analyze(self, trajectories: list[ExecutionTrajectory]) -> dict:
        """Analyze multiple execution traces"""
        return {
            "efficiency": self._analyze_efficiency(trajectories),
            "failure_patterns": self._analyze_failures(trajectories),
            "tool_usage": self._analyze_tool_usage(trajectories),
            "bottlenecks": self._identify_bottlenecks(trajectories),
        }

    def _analyze_efficiency(self, trajectories) -> dict:
        """Efficiency Analysis"""
        steps_list = [len(t.entries) for t in trajectories]
        token_list = [t.total_tokens for t in trajectories]
        success_count = sum(1 for t in trajectories if t.status == "success")
        return {
            "avg_steps": sum(steps_list) / len(steps_list) if steps_list else 0,
            "avg_tokens": sum(token_list) / len(token_list) if token_list else 0,
            "success_rate": success_count / len(trajectories) if trajectories else 0,
            "p95_steps": sorted(steps_list)[int(len(steps_list) * 0.95)]
            if steps_list else 0,
        }

    def _analyze_failures(self, trajectories) -> list:
        """Failure Mode Analysis"""
        failure_patterns = {}
        for t in trajectories:
            if t.status != "success":
                reason = t.termination_reason or "unknown"
                failure_patterns[reason] = failure_patterns.get(reason, 0) + 1
        return sorted(
            [{"reason": k, "count": v} for k, v in failure_patterns.items()],
            key=lambda x: x["count"], reverse=True,
        )

    def _analyze_tool_usage(self, trajectories) -> dict:
        """Tool Usage Analysis"""
        tool_stats = {}
        for t in trajectories:
            for entry in t.entries:
                if entry.tool_name:
                    if entry.tool_name not in tool_stats:
                        tool_stats[entry.tool_name] = {
                            "total_calls": 0, "success": 0, "failures": 0,
                            "avg_latency_ms": 0, "latencies": [],
                        }
                    stats = tool_stats[entry.tool_name]
                    stats["total_calls"] += 1
                    if entry.tool_success:
                        stats["success"] += 1
                    else:
                        stats["failures"] += 1
                    stats["latencies"].append(entry.latency_ms)

        for name, stats in tool_stats.items():
            stats["avg_latency_ms"] = (
                sum(stats["latencies"]) / len(stats["latencies"])
                if stats["latencies"] else 0
            )
            stats["success_rate"] = (
                stats["success"] / stats["total_calls"]
                if stats["total_calls"] else 0
            )
            del stats["latencies"]

        return tool_stats

    def _identify_bottlenecks(self, trajectories) -> list:
        """Identify Bottlenecks"""
        bottlenecks = []

        # Identify Slow Tools
        for t in trajectories:
            for entry in t.entries:
                if entry.latency_ms > 5000:  # > 5s
                    bottlenecks.append({
                        "type": "slow_tool",
                        "tool": entry.tool_name,
                        "latency_ms": entry.latency_ms,
                        "task_id": t.task_id,
                    })

        # Identify High Token Consumption Steps
        for t in trajectories:
            for entry in t.entries:
                total = entry.tokens_input + entry.tokens_output
                if total > 10000:
                    bottlenecks.append({
                        "type": "high_token_step",
                        "step": entry.iteration,
                        "tokens": total,
                        "task_id": t.task_id,
                    })

        return bottlenecks
```

---

## 6. Loop in K8S Operations Scenarios

## 6.1 Diagnosis Loop for Pod Pending

```python
class PodPendingDiagnosisLoop:
    """Standard Diagnostic Loop for Pod Pending Scenario"""

    DIAGNOSIS_SOP = [
        {"step": "describe_pod", "tool": "kubectl_describe",
         "args_template": "pod {pod_name} -n {namespace}",
         "extract": ["Events", "Conditions", "Status"]},
        {"step": "check_events", "tool": "kubectl_events",
         "args_template": "--field-selector involvedObject.name={pod_name} -n {namespace}",
         "extract": ["FailedScheduling", "InsufficientCPU", "InsufficientMemory"]},
        {"step": "check_nodes", "tool": "kubectl_get",
         "args_template": "nodes -o wide",
         "extract": ["Ready", "SchedulingDisabled", "allocatable"]},
        {"step": "check_node_resources", "tool": "kubectl_top",
         "args_template": "nodes",
         "extract": ["CPU%", "Memory%"]},
        {"step": "check_pvc", "tool": "kubectl_get",
         "args_template": "pvc -n {namespace}",
         "condition": "volume_mount_exists",
         "extract": ["Bound", "Pending"]},
    ]

    def run(self, pod_name: str, namespace: str) -> dict:
        """Execute Pod Pending Diagnosis"""
        context = {"pod_name": pod_name, "namespace": namespace}
        findings = []

        for sop_step in self.DIAGNOSIS_SOP:
            # Condition Check (some steps only execute under certain conditions)
            if sop_step.get("condition"):
                if not self._check_condition(sop_step["condition"], findings):
                    continue

            # Execute Tool Call
            args = sop_step["args_template"].format(**context)
            result = self.tools.execute(sop_step["tool"], args)

            # Extract Key Information
            extracted = self._extract_signals(result, sop_step["extract"])
            findings.append({
                "step": sop_step["step"],
                "result": result,
                "signals": extracted,
            })

            # Quick Path: Terminate early if an explicit root cause is found
            root_cause = self._check_root_cause(findings)
            if root_cause:
                return {
                    "status": "diagnosed",
                    "root_cause": root_cause,
                    "findings": findings,
                    "steps_taken": len(findings),
                }

        # All SOP steps completed, comprehensive analysis
        return self._synthesize_diagnosis(findings)
```

## 6.2 Problem Handling Execution Engine

```python
class IncidentExecutionEngine:
    """Problem Disposal Dedicated Execution Engine"""

    特点：
    1. 三阶段执行（诊断→决策→修复）
    2. 每个阶段有独立的超时和约束
    3. 修复阶段强制人工审批
    4. 全程轨迹记录和回滚支持
    """

    def __init__(self, llm, tools, approval_handler):
        self.llm = llm
        self.tools = tools
        self.approval = approval_handler

        self.phase_limits = {
            "diagnose": {"max_steps": 10, "timeout": 120, "read_only": True},
            "decide": {"max_steps": 3, "timeout": 60, "read_only": True},
            "remediate": {"max_steps": 5, "timeout": 180, "read_only": False},
        }

    async def handle_incident(self, incident: dict) -> dict:
        """Handle Problem"""
        trajectory = ExecutionTrajectory(
            task_id=incident["id"],
            task=incident["description"],
            start_time=datetime.utcnow().isoformat(),
        )

        # Phase 1: Diagnose
        diagnosis = await self._phase_diagnose(incident, trajectory)
        if diagnosis["confidence"] < 0.7:
            return {"status": "escalate", "reason": "Insufficient diagnostic confidence"}
                    "diagnosis": diagnosis, "trajectory": trajectory}

        # Phase 2: Make Decision
        action_plan = await self._phase_decide(diagnosis, trajectory)

        # Phase 3: Fix (requires approval)
        approved = await self.approval.request(
            action_plan,
            context={"incident": incident, "diagnosis": diagnosis},
        )
        if not approved:
            return {"status": "pending_approval", "action_plan": action_plan,
                    "trajectory": trajectory}

        result = await self._phase_remediate(action_plan, trajectory)

        trajectory.end_time = datetime.utcnow().isoformat()
        trajectory.status = result.get("status", "unknown")
        return {"status": result["status"], "trajectory": trajectory}
```

---

## 7. Best Practices

## 7.1 Loop Layer Design Core Principles

| Principle | Explanation | Practice Recommendations |
|------|------|---------|
| **Finite Execution** | All loops must have clear termination conditions | Set double protection with max_iterations + timeout |
| **Observability** | Every step must be recorded | Use TrajectoryEntry to record complete context |
| **Recovery** | Able to recover from checkpoints after abnormal interruptions | Regularly save checkpoint |
| **Anti-drift** | Actively detect and interrupt dead loops | Deploy multi-dimensional drift detectors |
| **Phased** | Complex tasks executed in stages | Information gathering → Analysis → Action three-stage process |
| **Rapid Path** | Known scenarios terminated early | Match SOP to skip exploration stage |

## 7.2 Anti-patterns

| Anti-pattern | Problem | Correct approach |
|--------|------|----------|
| **Infinite Loop** | No termination condition, resources exhausted | Timeout + Iteration limit + Budget constraint |
| **No Trajectory Recording** | Issues cannot be audited for traceability | Record complete TrajectoryEntry at each step |
| **Ignoring Drift** | Agent falls into a dead loop consuming resources | Deploy drift detection + recovery strategy |
| **Synchronous Blocking** | Serial tool calls low efficiency | Identify parallel tools, execute asynchronously |
| **Hardcoded Workflow** | Cannot adapt to different scenarios | Use strategy pattern, runtime selection of execution strategy |

---

## Associated Documentation

| Documentation | Related content |
|------|--------|
| [30 - Agent Harness Engineering](./30-agent-harness-engineering.md) | Overview of Harness six-layer architecture, basic definition of Loop layer |
| [32 - Harness Tool Engineering](./32-agent-harness-tool-engineering.md) | Design of tool calls driven by Loop layer |
| [33 - Context and Memory Engineering](./33-agent-harness-context-memory.md) | Management and persistence of context in Loop |
| [34 - Verification and Quality Gates](./34-agent-harness-verification-quality.md) | Validation layer after Loop ends |
| [01 - AI Agent Fundamentals](./01-ai-agent-fundamentals.md) | Theoretical foundation of Agent Loop, ReAct inference mode |

---

## References

| Source | Content | Date |
|------|------|------|
| Anthropic | "Building Effective Agents" Loop design patterns | 2025-12 |
| LangChain | Agent Loop drift detection experiment | 2026-02 |
| Sean Goedecke (GitHub) | Copilot Agent Mode execution engine design | 2025 |
| Microsoft Research | Analysis and optimization of agent execution trajectories | 2026-01 |

---

*This document is original content from the kudig-database project series 02-ai-agents, delving into the design of the Loop layer in the Harness architecture.*

---

## Obsidian Related Documentation

- 02-ai-agents KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|AI Agent Engineering Specialization]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|AI Agent Fundamentals and Core Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|LLM Foundation Models Selection and Evaluation]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Mainstream Agent Framework Deep Comparison]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|RAG Retrieval-Augmented Generation Deep Guide]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Tool Usage and Function Calling Design Guidelines]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Multi-Agent Orchestration and Collaboration Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation and Observability Framework]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]

## See Also

- 29-agentscope-studio-skill-demo
- 30-agent-harness-engineering
- 32-agent-harness-tool-engineering
- 33-agent-harness-context-memory


<!-- risk-assessed -->
