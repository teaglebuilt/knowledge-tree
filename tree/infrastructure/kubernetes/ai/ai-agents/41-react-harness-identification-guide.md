---
title: ReAct Agent And Harness Identification Guide (domain-14-ai-ml-infra)
description: 'title: ReAct Agent And Harness Identification Guide'
summary: 'title: ReAct Agent And Harness Identification Guide'
category: general
tags:
- ai
- ai-agent
- guide
- prometheus
- postgresql
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
estimated_read_time: 15min
intent_queries:
- What is ReAct Agent with Harness identification guide
- How ReAct Agent and Harness Reference Guides Recognize
- Kubernetes 14 ai ml infra best practices
trigger_keywords:
- ReAct
- Agent
- Harness
- What is the recognition guide
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- prometheus-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/41-react-harness-identification-guide.md
---

> **Production Environment Security Reminders**
>
> Commands included in this document are executable directly. Before executing, please confirm: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/ReadOnly (information gathering with no side effects).




title: ReAct Agent and Harness Identification Guide
description: '# ReAct Agent and Harness Identification Guide'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- [[Prometheus|prometheus]]
- postgresql
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- Architect
- SRE
estimated_read_time: 5min
intent_queries:
- What is ReAct Agent and Harness Identification Guide
- How to use ReAct Agent and Harness Identification Guide
trigger_keywords:
- ReAct
- Agent
- Harness
- Identification Guide
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

# ReAct Agent and Harness Identification Guide

> **Document Type**: Practice Reference Guide | **Last Updated**: 2026-04 | **Keywords**: ReAct, Agent Harness, Identification Judgment, Inference Framework, Maturity Model, Classification Standards, Agent Loop, Verification, Constraints

---

## 1. Introduction

In building and evaluating an Agent system, two fundamental questions are: "Is this Agent a ReAct?" and "Does this Agent have a Harness?". The former determines the inference mode and capability boundaries of the Agent, while the latter determines whether the Agent has production-level reliability and controllability.

This document provides systematic judgment criteria, checklists, and code-level identification methods to help engineers quickly assess the inference mode and completeness of the Harness in the Agent.

---

## 1. How to determine if an Agent is ReAct

## 1.1 Core definition of ReAct

**ReAct = Reasoning + Acting** is the most widely used inference mode for Agents. Its core feature is **alternating between reasoning (Thought) and action (Action)**:

```
ReAct Loop:
  Thought: Analyze current situation, decide on next action
  Action: Call tool/execute operation
  Observation: Get tool return result
  ... (loop until task completes)
  Final Answer: Give the final answer
```

## 1.2 Three-element judgment method

The three elements of ReAct must be **all present simultaneously**:

| Feature | Description | Judgment Method |
|------|------|---------|
| **Thought (Thought)** | Explicit reasoning or analysis steps at each step | Check if the output contains `Thought:` or reasoning steps |
| **Action (Action)** | Calls tools/actions based on reasoning | Check if there is `Action:` followed by tool call |
| **Observation (Observation)** | Feedbacks tool execution results back to the next round | Check if there is `Observation:` followed by result parsing |

## 1.3 Complete judgment checklist

```
✅ Is a marker for ReAct Agent:
  1. Has Agent Loop (cyclic execution, not one-time request-response)
  2. oggle between Thought → Action → Observation oggle loop
  3. Have tool calling capability (Function Calling / Tool Use)
  4. LLM decide autonomously when to call the tool and which tool to call
  5. LLM autonomously decide when to end (output Final Answer)
  6. Each inference step is traceable (has trajectory)

❌ Not a ReAct case:
  - Pure CoT: Only chain of thoughts, no tool invocation
  - Pure Plan-and-Execute: Generate a complete plan upfront before execution, rather than alternating inference and action
  - Pure dialogue: No Agent Loop, just multi-round dialogue
  - Predefined flow: Fixed execution path, LLM does not make dynamic decisions
```

## 1.4 Code-level judgment

## AgentScope framework

Directly check if `ReActAgent` or inherits from `ReActAgentBase` is used:

```python
# ✅ This is the ReAct Agent
from agentscope.agent import ReActAgent
agent = ReActAgent(name="Friday", model=model, toolkit=toolkit, ...)

# AgentScope agent inheritance system:
# AgentBase          → Base class, not necessarily ReAct
# ReActAgentBase     → Has _reasoning() + _acting(), is ReAct
# ReActAgent         → Usable out-of-the-box ReAct implementation, is ReAct
# UserAgent          → User agent, not ReAct
```

## LangChain framework

```python
# ✅ ReAct
from langchain.agents import create_react_agent
agent = create_react_agent(llm=llm, tools=tools, prompt=react_prompt)

# ❌ Not ReAct (is Plan-and-Execute)
from langgraph.prebuilt import create_plan_and_execute_agent
```

## Custom Agent

Check if it has the following structure:

```python
# The minimum implementational skeleton of ReAct
class ReActAgent:
    def run(self, task: str) -> str:
        while not done:
            # 1. Thought: LLM inference
            thought = self.llm.reason(context)

            # 2. Check if done
            if thought.is_final_answer:
                return thought.answer

            # 3. Action: Call tool
            result = self.execute_tool(thought.action)

            # 4. Observation: Add result to context
            context.add_observation(result)
```

## 1.5 Comparison of ReAct with other inference frameworks

| Framework | Has Loop? | Has Tool Call? | Inference Method | Is ReAct? |
|------|----------|-----------|---------|-----------|
| **ReAct** | ✅ | ✅ | Alternating Thought/Action | ✅ |
| CoT | ❌ | ❌ | Linear Chain of Reasoning | ❌ |
| ToT | ❌ | ❌ | Tree Branch Search | ❌ |
| Plan-and-Execute | ✅ | ✅ | Plan then Execute | ❌ |
| Reflexion | ✅ | Optional | Self-reflection Iteration | ❌ (but composable) |

## 1.6 Boundary cases

```
Gray area — Requires further judgment:

1\. Plan-then-ReAct (plan before ReAct execution)
   Plan-and-Execute
   ReAct
   Judgement: Execution layer is ReAct, overall is hybrid architecture

2. ReAct + Reflexion (ReAct with Reflection)
   ReAct Loop Executes Tasks
   Fail and trigger Reflection reflect
   Judgement: Core is ReAct, Reflexion is enhancement

3. Multi-Agent in ReAct Worker
   Orchestrator  use Plan-and-Execute
   Worker Agent each use ReAct
   Judge: Worker is ReAct, the system as a whole is a hybrid architecture
```

---

## 2. How to determine if an Agent has Harness

## 2.1 Core definition of Harness

**Harness = Wraps the entire operational system around an AI model**, converting the model's raw cognitive capabilities into reliable production outputs.

```
Normal LLM Usage (No Harness):
  User Input → LLM Generation → Output Result
  Problem: Unstable answers, hallucinations, loss of context, inability to execute, lack of safety boundaries

Agent + Harness (Complete System):
  Goal → Iterative Execution → Tool Invocation → Context Management → State Persistence → Self-check Validation → Constraint Control → Reliable Output
  Effect: Stable, reliable, auditable, controllable, measurable

Key Metaphor:
  Model is the horse, Harness is the tack (reins, saddle, breastplate, blindfold)
  Bridles do not make horses stronger but make horse strength reliably usable for useful work
```

## 2.2 Six-layer architecture check method

Harness consists of six layers. **Not all layers are required to be a Harness**, but the more complete the layers, the more mature the Harness:

```
Agent Harness Six-layer architecture (layer-by-layer check):

Layer 1: Loop(Loop)
  □ Has Agent Loop (runs until goal is achieved)
  □ Has timeout protection
  □ Has a maximum iteration limit
  □ Have drift detection (to prevent dead loops)
  □ Has trajectory record (trajectory)

Layer 2: Tools(Tools)
  □ Have tool registration/discovery mechanism
  □ Parameter validation
  □ Have tool permission control
  □ Have tool error handling and retry

Layer 3: Context(Context)
  □ Have context window management
  □ Have information priority sorting
  □ Have RAG retrieval integration
  □ Have contextual compression/summary

Layer 4: Persistence(Persistence)
  □ Have cross-session memory
  □ Have execution records persisted storage
  □ Stateful recovery capability

Layer 5: Verification(verification layer)      ← key milestone
  □ Has self-check loop
  □ Has fact verification
  □ Has format check
  □ Has hallucination detection

Layer 6: Constraints(constraints layer)
  □ Has security boundary (read-only/command blacklist)
  □ Has cost control (Token budget)
  □ Has audit logs
  □ Has manual approval mechanism
```

## 2.3 Five-tier maturity model judgment method

| Level | Name | Feature | Has Harness? |
|------|------|------|--------------|
| **L1** | Bare Agent (Ad-hoc) | Directly calls LLM API, no loop, no tool, no validation | ❌ No Harness |
| **L2** | Managed Harness (Basic) | Has Agent Loop + Tool Call + Timeout Protection, but no validation, no constraints | ⚠️ Minimum Harness |
| **L3** | Production-Ready (Production) | Six-layer architecture complete + CI/CD quality gates + basic monitoring | ✅ Has Harness |
| **L4** | Enterprise (Enterprise) | Multi-Agent orchestration + gray-scale release + A/B testing + complete observability | ✅ Mature Harness |
| **L5** | Self-Evolving (Self-Evolving) | Meta-Agent automatically optimizes Harness parameters | ✅ Advanced Harness |

## 2.4 Quick judgment checklist

## Minimum Harness Judgment (L2 — At least meet all the following)

```
□ Has Agent Loop(loop execution, not single call)
□ Has tool invocation (>= 2 tools)
□ Has timeout protection
□ Has maximum iteration limit
```

## Production-grade Harness Judgment (L3 — Add on top of L2)

```
□ Has verification layer (>= 3 verifiers)           ← key milestone
□ Has constraints layer (read-only + command blacklist)
□ Has context management (layered construction)
□ Has persistence (persistent storage of execution records)
□ Has Prometheus metrics
□ Has CI/CD quality gates
□ Has baseline comparison
□ Has basic alert rules
```

## Enterprise-grade Harness Judgment (L4 — Add on top of L3)

```
□ Has multi-Agent orchestration
□ Has gray release process
□ Has A/B testing
□ Has OTel full-trace
□ Has Langfuse integration
□ Has red team tests
□ Has LLM provider disaster recovery
□ Has SLA monitoring
□ Has configuration hot update
□ Has prompt version management
```

## 2.5 Code-Level Harness Recognition

## Agents with Harnesses (Typical Structure)

```python
class HarnessedAgent:
    def __init__(self):
        # Layer 1: Loop
        self.max_iterations = 15
        self.timeout_seconds = 300

        # Layer 2: Tools
        self.tool_registry = ToolRegistry()

        # Layer 3: Context
        self.context_manager = ContextManager(max_tokens=100000)

        # Layer 4: Persistence
        self.memory = AsyncSQLAlchemyMemory(url="postgresql://...")

        # Layer 5: Verification  ← Watershed
        self.verifiers = [
            FaithfulnessVerifier(),
            FormatVerifier(),
            SafetyVerifier(),
        ]

        # Layer 6: Constraints
        self.constraints = ConstraintEngine(
            read_only=True,
            blocked_commands=["kubectl delete", "rm -rf"],
            max_cost_usd=2.0,
        )

    async def run(self, task: str) -> dict:
        for i in range(self.max_iterations):
            # Loop-driven
            thought = await self.llm.reason(context)
            if thought.is_final:
                # Verification: Validate
                verified = await self.verify(thought.answer)
                if verified:
                    return {"status": "success", "answer": thought.answer}
                else:
                    continue  # 自检失败，重试

            # Constraints: Check constraints
            if not self.constraints.allow(thought.action):
                return {"status": "blocked", "reason": "constraint_violation"}

            # Tools: Execute
            result = await self.tool_registry.execute(thought.action)

            # Context: Update
            self.context_manager.add_observation(result)

            # Persistence: Record
            await self.memory.save_step(thought, result)
```

## Agents without Harnesses (Bare Agents)

```python
# ❌ Bare Agent: Directly call LLM + tools, no verification, no constraints, no persistence
class NakedAgent:
    def run(self, task: str) -> str:
        response = self.llm.chat(task)
        if response.tool_calls:
            result = self.execute_tool(response.tool_calls[0])
            return self.llm.chat(f"Tool returns: {result}")
        return response.content
```

## 2.6 Critical Milestone: Validation Layer

Industry empirical data shows that **the validation layer is the key differentiator between Harness and "bare Agent"**:

```
Validation layer ROI empirical:

LangChain coding Agent (2026-02 experiment):
  No validation:        Baseline score 52.8%
  Add self-check loop: baseline score 66.5% → +13.7% absolute improvement (highest single-item enhancement)

Anthropic long-running Agent:
  No validation:        Task completion rate 71%
  Verified:      Task completion rate 89%  → +18% absolute improvement

Verify the type of issues to intercept:
  - Spurious output: 40%
  - Format error: 25%
  - Logical inconsistency: 20%
  - Security risk: 15%
```

## 2.7 One-Liner Summary

```
Bare Agent = LLM + Tool + Loop
With Harness = Bare Agent + Validation (self-check loop) + Constraints (security boundary) + Context Management + Persistence + Observability

Simplest judgment:
  ✅ Have self-check validation + Have constraint control → Have Harness
  ❌ Only LLM + tool loop call → bare Agent
```

---

## 3. Comprehensive Identification Matrix

| System Feature | Pure LLM | Bare Agent | Basic Harness (L2) | Production Harness (L3+)| 
|---------|--------|---------|------------------|-------------------|
| LLM Inference | ✅ | ✅ | ✅ | ✅ |
| Tool Call | ❌ | ✅ | ✅ | ✅ |
| Agent Loop | ❌ | ✅ | ✅ | ✅ |
| Timeout/Iteration Limitations | ❌ | ❌/⚠️ | ✅ | ✅ |
| Drift Detection | ❌ | ❌ | ⚠️ Optional | ✅ |
| Context Management | ❌ | ❌ | ⚠️ Foundation | ✅ |
| Persistence | ❌ | ❌ | ❌ | ✅ |
| **Validation Layer** | ❌ | ❌ | ❌ | **✅ Watershed** | 
| Constraint Layer | ❌ | ❌ | ❌ | ✅ |
| Observability | ❌ | ❌ | ❌ | ✅ |
| Trace Logging | ❌ | ⚠️ | ✅ | ✅ |
| Audit Logs | ❌ | ❌ | ❌ | ✅ |

---

## 4. Real-World Application Examples

## 4.1 Assessment of Existing Agent Systems

```python
class AgentSystemAssessment:
    """Agent system quick evaluation tool"""

    def assess(self, agent_system: dict) -> dict:
        """
        输入 agent_system 描述，输出评估结果

        agent_system 示例:
        {
            "has_agent_loop": True,
            "has_tools": True,
            "tool_count": 5,
            "has_timeout": True,
            "has_max_iterations": True,
            "has_drift_detection": False,
            "has_verification": False,
            "has_constraints": False,
            "has_persistence": False,
            "has_observability": False,
        }
        """
        # 1. Determine inference mode
        is_react = (
            agent_system.get("has_agent_loop", False)
            and agent_system.get("has_tools", False)
            and agent_system.get("has_thought_action_observation", True)
        )

        # 2. Determine Harness grade
        harness_level = self._assess_harness_level(agent_system)

        # 3. Analyze differences
        gaps = self._gap_analysis(harness_level, agent_system)

        return {
            "is_react": is_react,
            "harness_level": harness_level,
            "gaps_to_next_level": gaps,
            "recommendation": self._recommend(harness_level),
        }

    def _assess_harness_level(self, s: dict) -> str:
        if not s.get("has_agent_loop"):
            return "L1"
        if not all([
            s.get("has_tools"),
            s.get("has_timeout"),
            s.get("has_max_iterations"),
        ]):
            return "L1"
        if not all([
            s.get("has_verification"),
            s.get("has_constraints"),
        ]):
            return "L2"
        if not all([
            s.get("has_observability"),
            s.get("has_persistence"),
        ]):
            return "L3"
        return "L4"

    def _recommend(self, level: str) -> str:
        recommendations = {
            "L1": "Add Agent Loop + Tool + Timeout Protection, upgrade to L2",
            "L2": "Add Validation Layer (highest ROI improvement) + Constraint Layer, upgrade to L3",
            "L3": "Add full observability + Canary Release, upgrade to L4",
            "L4": "Explore Meta-Agent self-optimization, evolve to L5",
        }
        return recommendations.get(level, "Reached highest maturity level")
```

## 4.2 Classification of Agents in Team Code Reviews

In team Code Reviews, you can use the following questions to quickly categorize:

```
Agent Classification Code Review Checklist:

1. Inference mode recognition
   Q: Are thoughts/actions/observations alternated during execution?
   → Yes → ReAct
   → No → Check if it is Plan-and-Execute or CoT

2. Harness level recognition
   Q: Is there any output validation (self-check)?
   → None → Maximum L2 (Foundation Harness or lower)
   → have → at least L3

   Q: Are there any security constraints (command blacklist/read-only mode)?
   → Not applicable → Unsuitable for production environment
   → There → Continue checking other dimensions

   Q: Are there observability (metrics/traces/logs)?
   → None → Maintenance operations difficult
   → have → possess
```

---

## Related Documentation

| Documentation | Associated Content |
|------|---------|
| [01 - AI Agent Fundamentals and Core Architecture](./01-ai-agent-fundamentals.md) | ReAct/CoT/ToT/Reflexion Inference Framework Theoretical Foundations |
| [17 - AgentScope Core Concepts](./17-agentscope-core-concepts.md) | ReActAgent Inheritance System in AgentScope |
| [30 - Harness Engineering](./30-agent-harness-engineering.md) | Six-layer Architecture Overview, Design Patterns, Industry Proofs |
| [31 - Harness Loop and Execution Engine](./31-agent-harness-loop-execution.md) | State Machine at Loop Layer, Anti-drift Detection |
| [34 - Harness Verification and Quality Gates](./34-agent-harness-verification-quality.md) | Validation Layer (Watershed) Detailed Design |
| [35 - Harness Security and Constraint Engineering](./35-agent-harness-security-constraints.md) | Four-layer Model of Constraint Layer |
| [40 - Harness Production Operations and Maturity Model](./40-agent-harness-production-maturity.md) | Five-stage Maturity Assessment Checklist |

---

## References

| Source | Content | Date |
|------|------|------|
| Yao et al. | "ReAct: Synergizing Reasoning and Acting in Language Models" | 2022-10 |
| Birgitta Böckeler (Martin Fowler) | "Harness Engineering" Concept Introduced | 2026-02 |
| Anthropic | "Building Effective Agents", "Effective Harnesses for Long-Running Agents" | 2025-12 |
| LangChain | Agent Loop Drift Detection Experiment, Self-check Loop ROI Data | 2026-02 |
| Sean Goedecke (GitHub) | Copilot Agent Mode Execution Engine Design | 2025 |

---

*This document is original content from the kudig-database project series 02-ai-agents, providing a systematic identification method for ReAct Agents and Harness.*

---

## Obsidian-related Documentation

- 02-ai-agents KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|[[AI Agent Engineering Topic|AI Agent Engineering Topic]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|AI Agent Fundamentals and Core Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|[[LLM Foundation Model Selection and Evaluation|LLM Foundation Model Selection and Evaluation]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Deep Comparison of Main Agent Frameworks]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|Deep Guide to Retrieval-Augmented Generation (RAG)]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Design Guidelines for Tool Use and Function Calling]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Architecture for Multi-Agent Orchestration and Collaboration]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Engineering Memory Management and Context Window]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|System for Agent Evaluation and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]

## See Also

- 39-agent-harness-testing-benchmark
- 40-agent-harness-production-maturity
- 42-model-harness-compatibility-matrix
- 43-openclaw-framework-integration


<!-- risk-assessed -->
