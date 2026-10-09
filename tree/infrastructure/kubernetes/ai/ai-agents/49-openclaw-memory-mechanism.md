---
title: OpenClaw MEMORY.md Mechanism Deep Dive (domain-14-ai-ml-infra)
description: 'title: OpenClaw MEMORY.md Mechanism Deep Dive'
summary: 'title: OpenClaw MEMORY.md Mechanism Deep Dive'
category: general
tags:
- ai
- ai-agent
- etcd
- kubelet
- coredns
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
- What is OpenClaw MEMORY.md Mechanism Deep Dive
- How to do OpenClaw MEMORY.md Mechanism Deep Dive
- Best Practices for OpenClaw MEMORY.md Mechanism Deep Dive in Kubernetes 14 ai ml infra
trigger_keywords:
- OpenClaw
- MEMORY.md
- What is OpenClaw MEMORY.md Mechanism Deep Dive
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- etcd-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/49-openclaw-memory-mechanism.md
---

> **Production Environment Security Reminders**
>
> This document contains executable operational commands. Please confirm before execution: that the target cluster and Namespace are correct; that you have sufficient RBAC permissions; and that the commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




title: OpenClaw MEMORY.md Mechanism Deep Dive
description: '# OpenClaw MEMORY.md Mechanism Deep Dive'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- [[etcd|etcd]]
- [[kubelet|kubelet]]
- [[CoreDNS|coredns]]
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- Architect
- SRE
estimated_read_time: 5min
intent_queries:
- What is OpenClaw MEMORY.md Mechanism Deep Dive
- How to OpenClaw MEMORY.md Mechanism Deep Dive
trigger_keywords:
- OpenClaw
- MEMORY.md
- Mechanism Deep Dive
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

# OpenClaw MEMORY.md Mechanism Deep Dive

> **Document Type**: Frontier Engineering Special Topic | **Last Updated**: 2026-04 | **Keywords**: OpenClaw, MEMORY.md, Memory System, Persistence Layer, Long-Term Memory, Short-Term Memory, Metabolism, Experience Accumulation

---

## Overview

MEMORY.md is a configuration file in the OpenClaw File-First architecture responsible for managing **Agent's long-term memory**. It stores cross-session experiences, patterns, and deterministic rules, enabling the Agent to possess "learning capability"—each diagnostic experience can be accumulated over time, gradually improving diagnostic efficiency and accuracy. In Harness Engineering, it primarily maps to the **Persistence Layer**.

MEMORY.md works in conjunction with the `memory/` directory (short-term memory) to form a complete memory system: MEMORY.md stores long-term rules and patterns, while `memory/YYYY-MM-DD.md` stores daily diagnostic logs.

---

## 1. Design Principles

## 1.1 Three-Level Memory Model

```
# 🟢 Low Risk: read-only/information collection, usually with no side effects
MEMORY.md three-layer memory model:

Layer 1: deterministic rules (maintained manually)
  │  Cluster baseline: number of nodes, version, CNI, storage solution
  │  Known issues: KI-001 Terway ENI latency, KI-002 ESSD Multi-Attach
  │  Team agreement: namespace naming conventions, change process
  │  Characteristics: 100% accurate, manually created and updated
  │
Layer 2: empirical mode (Agent automatically abstracts)
  │  Frequent failure patterns: statistical laws of symptoms to root causes
  │  Effective diagnostic path: which steps are most efficient
  │  Lessons learned: detours and misjudgments
  │  Characteristics: probabilistic knowledge, must annotate confidence
  │
Layer 3: user preferences (interactive learning)
     Common commands: kubectl usage habits of users
     Key metrics: monitoring dimensions that users care about most
     Historical feedback: positive/negative feedback on Agent outputs
     Characteristics: personalized customization, enriched with use
```
## 1.2 Memory Flow Mechanism

```
Memory lifecycle:

Generated during routine diagnosis
  │
  ▼
Short-term memory: memory/2026-04-03.md
  │  Key findings in each diagnosis, commands used, diagnostic path
  │  Retention period: 7 days
  │
  ▼ Extraction weekly (manually or automatically)
Situational memory: important events and solutions
  │  "2026-04-03 ack-prod cluster experienced a large-scale OOM, root cause was Java application memory leak"
  │  Retention period: 3 months
  │
  ▼ Pattern abstraction (after 3+ similar events)
Semantic memory: rules and patterns in MEMORY.md
  │  "FP-001: Frequent fault pattern — Java application OOM, first check JVM heap configuration"
  │  Retention period: Based on confidence and usage frequency
  │
  ▼ Query injection
Next session: MEMORY.md + recent 3 days memory/ → injection context
```

## 1.3 Metabolism Mechanism

```
Memory metabolism (to prevent memory expansion):

Retention strategy:
  Certain rules → Permanent retention (manual deletion)
  High-confidence patterns → Retain for 6 months
  Medium-confidence patterns → Retain for 3 months
  Low-confidence patterns → Retain for 1 month

Elimination criteria:
  - Exceeds retention period
  - Not referenced within 30 days
  - Covered by new memories

quality metrics:
  avg_confidence: 0.82       # average confidence
  utilization_rate: 0.75     # 75% of patterns were referenced in the last 30 days
  stale_entries: 2           # number of entries older than 3 months

goal: keep the "signal-to-noise ratio" of memories > 0.7
  memories are not better when more exist, outdated memories = noise = misleading decisions
```

---

## 2. Harness Engineering Mapping

## 2.1 Mapping Relationships

```
MEMORY.md × Harness six-layer mapping:

               │ Loop │ Tools │ Context │ Persist │ Verify │ Constrain │
──────────────┼──────┼───────┼─────────┼─────────┼────────┼───────────│
MEMORY.md     │      │       │    ◐    │    ●    │        │           │

● = main mapping (Persistence layer — persistent storage)
◐ = secondary mapping (Context layer — memory injection context)
```

## 2.2 Persistence Layer Mapping Details

| MEMORY.md Content | Harness Persistence Implementation | Storage Method |
|---------------|------------------------|---------|
| Deterministic Rules (1) | `RuleStore` — Rule Persistence | YAML format, manually maintained |
| Experience Patterns (2) | `PatternStore` — Pattern Persistence | Agent automatically writes, with confidence level |
| User Preferences (3) | `PreferenceStore` — Preference Persistence | Interactive learning, automatically updated |
| Metadata Management (4) | `MemoryMetadata` — Metadata Management | Automatically tracked and maintained |
| `memory/` Directory | `DailyLog` — Daily Diagnostic Logs | One Markdown file per day |

## 2.3 Context Layer Mapping

```
MEMORY.md Memory injection LLM context strategy:

at the start of each session (Step 3 of wake-up protocol):

1. Load the full MEMORY.md document (long-term memory)
   → Deterministic rules + frequent patterns
   → ~800 tokens

2. Load recent 3 days' memory/ (short-term memory)
   → Most recent diagnostic context
   → ~500 tokens

3. Assemble memory context
   system_prompt += f"""
   ## Long-term Memory
   {memory_md_summary}

   ## Recent Context
   {recent_daily_logs}
   """

total memory token budget: ~1300 tokens (15-20% of system_prompt)
```

---

## 3. Kubernetes Operational Case Studies

## 3.1 Case Study: Known Issue Hit

```
# 🟢 Low Risk: read-only/information collection, usually with no side effects
scenario: User reports "Pod startup is very slow, waited 30+ seconds"

MEMORY.md Known issues match:
  KI-001: "Terway ENI mode Pod IP allocation delay"
  Symptoms: "Pod starts slowly (>30s)"
  Root cause: "Allocation of ENI elastic network interface requires calling the ECS API, which has delays during peak hours"

Agent response (quickly identifies known issue):
  "Symptoms match known issue KI-001: Terway ENI allocation delay.
   Verification: kubectl describe pod <pod> -n <ns> | grep 'waiting for ENI'
   If confirmed:
   1. Check ENI availability on nodes: kubectl get eniconfig
   2. Consider preheating ENI pool
   Reference: domain-10-troubleshooting-diagnostics/03-networking-cni-troubleshooting.md"

Effect: Skips the routine diagnostic process and directly provides a known solution
  Diagnostic time: Shortened from 5 minutes to 30 seconds
```
## 3.2 Case Study: Learning from Experience

```
First diagnosis (no experience):
  Problem: Java application OOMKilled
  Diagnosis path: Routine process → Check resource limits → Check logs → Finds JVM heap overflow
  Time: 8 minutes

Agent records in memory/2026-04-01.md:
  "Java application OOMKilled → First check JVM heap configuration (-Xmx vs container memory limit)"

Third diagnosis (after experience accumulation):
  Problem: Another Java application OOMKilled
  MEMORY.md High Frequency Pattern Matching: FP-001
  Agent Direct Execution: Check container resources + JVM -Xmx parameter
  Duration: 2 minutes

Experience Extracted to MEMORY.md:
  FP-001:
    pattern: "Java application OOMKilled"
    first_check: "JVM -Xmx vs container memory limit"
    confidence: 0.85
    occurrences: 5
```

## 3.3 Case Study: Record of Failures

```
Failed Case:
  Problem: DNS resolution occasional timeout
  Incorrect Diagnosis: Agent Suggests Restarting CoreDNS → Issue Unresolved
  Correct Root Cause: conntrack race condition (KI-003)

Recorded to MEMORY.md:
  LL-001:
    title: "DNS Timeout Avoid Restarting CoreDNS"
    wrong_approach: "Restart CoreDNS Pod"
    correct_approach: "Check conntrack race condition, configure force_tcp"
    lesson: "5s timeout is a feature of conntrack, not a problem with CoreDNS itself"

Next Time DNS Timeout Occurs:
  Agent Matches LL-001 → Avoid Repetitive Mistakes
  Directly Check conntrack Instead of Restarting CoreDNS
```

---

## 4. Configuration Collaboration Mechanism

## 4.1 Collaboration between MEMORY.md and Other Files

```
MEMORY.md Role in Configuration Memory System:

AGENTS.md ──→ MEMORY.md
  │           Wakeup Protocol Step 3: Load MEMORY.md
  │           Phase 5: Write diagnostic results to memory/
  │
SOUL.md ──→ MEMORY.md
  │          SOUL.md  honesty principle constrains memory quality
  │          Only conclusions supported by data can be written
  │
SKILL.md ──→ MEMORY.md
  │           SKILL.md provide SOP → diagnosed new mode in diagnosis → record to MEMORY.md
  │           MEMORY.md frequent patterns → feedback for optimization of SKILL.md SOP
  │
USER.md ──→ MEMORY.md
             USER.md define initial preferences
             MEMORY.md learn more preferences from interactions
```

## 4.2 Management of the memory/ Directory

```
# 🟢 Low Risk: read-only/information collection, usually with no side effects
Short-term memory directory structure:

memory/
├── 2026-04-01.md    # Day 1 diagnostic flow
├── 2026-04-02.md    # Day 2 diagnostic flow
├── 2026-04-03.md    # Day 3 diagnostic flow (today)
└── ...

Daily file format:
  # 2026-04-03 Diagnostic Logs
  ## Session 1 (09:15)
  - Problem: Pod coredns-xxx Pending
  - Root cause: node taint does not match
  - Solution: add tolerations
  - Tag: routine (routine issue)

  ## Session 2 (14:30)
  - Problem: API Server response is slow
  - Root cause: etcd compaction was not executed in time
  - Solution: manually execute etcdctl compact
  - Tag: key_insight (important discovery, suggest to be refined to MEMORY.md)

Deletion strategy:
  retain the last 7 days
  Mark as key_insight content → Condense to MEMORY.md after deletion
  Over 7 days' files → Automatically archive or delete
```
---

## 5. Integration Code for AgentScope

## 5.1 Implementation of MemoryManager

```python
import os
import yaml
from datetime import datetime, timedelta
from typing import Optional


class MemoryManager:
    """Based on MEMORY.md's memory manager"""

    def __init__(self, workspace_path: str):
        self.workspace_path = workspace_path
        self.memory_path = os.path.join(workspace_path, "MEMORY.md")
        self.daily_dir = os.path.join(workspace_path, "memory")
        self.long_term = self._load_long_term()

    def _load_long_term(self) -> str:
        """Load MEMORY.md long-term memory"""
        if os.path.exists(self.memory_path):
            with open(self.memory_path) as f:
                return f.read()
        return ""

    def load_context(self, days: int = 3) -> str:
        """Load context memory (long-term + last N days' short-term)"""
        context_parts = []

        # Long-term Memory
        context_parts.append("## Long-term memory\n")
        context_parts.append(self._summarize_long_term())

        # Short-term Memory
        context_parts.append("\n## Recent context\n")
        recent_logs = self._load_recent_daily(days)
        if recent_logs:
            context_parts.append(recent_logs)
        else:
            context_parts.append("(No recent diagnostic records)")

        return "\n".join(context_parts)

    def _summarize_long_term(self) -> str:
        """Extract long-term memory summary (control Token consumption)"""
        content = self.long_term
        sections = []

        # Extract Known Issues
        if "known_issues:" in content:
            sections.append("Known issues: FP-001(Java OOM→check JVM), "
                          "KI-002(ESSD Multi-Attach), "
                          "KI-003(DNS 5s conntrack)")

        # Extract High-Frequency Patterns
        if "fault_patterns:" in content:
            sections.append("High-frequency mode: FP-002(Pod Pending→check resources+taint), "
                          "FP-003(API Server slow→check etcd)")
                          sections.append("Lessons learned: LL-001(DNS timeout≠CoreDNS issue), "

        # Extract Failure Lessons
        if "lessons_learned:" in content:
            sections.append("Lessons learned: LL-001(DNS timeout≠CoreDNS issue), "
                          "LL-002(Node NotReady check kubelet)")

        return "\n".join(sections) if sections else "(Long-term memory is empty)"

    def _load_recent_daily(self, days: int) -> str:
        """Load daily diagnostic logs for the last N days"""
        if not os.path.exists(self.daily_dir):
            return ""

        logs = []
        for i in range(days):
            date = datetime.now() - timedelta(days=i)
            filename = date.strftime("%Y-%m-%d.md")
            filepath = os.path.join(self.daily_dir, filename)
            if os.path.exists(filepath):
                with open(filepath) as f:
                    content = f.read()
                    # Only take the first 500 characters (control Token)
                    logs.append(content[:500])

        return "\n---\n".join(logs)

    def record_daily(self, session_summary: str, is_key_insight: bool = False):
        """Record daily diagnostic flow"""
        os.makedirs(self.daily_dir, exist_ok=True)
        today = datetime.now().strftime("%Y-%m-%d")
        filepath = os.path.join(self.daily_dir, f"{today}.md")

        timestamp = datetime.now().strftime("%H:%M")
        marker = " [key_insight]" if is_key_insight else ""

        entry = f"\n## Session ({timestamp}){marker}\n{session_summary}\n"

        with open(filepath, "a") as f:
            f.write(entry)

    def check_known_issues(self, symptoms: str) -> Optional[str]:
        """Check if symptoms match known issues"""
        known_issues = {
            "Startup slow": "KI-001: Terway ENI allocation delay",
            "waiting for ENI": "KI-001: Terway ENI allocation delay",
            "Multi-Attach": "KI-002: ESSD cloud disk Multi-Attach residual",
            "DNS.*5s": "KI-003: conntrack race condition",
            "DNS.*timeout": "KI-003: conntrack race condition",
        }
        for pattern, issue in known_issues.items():
            if pattern.lower() in symptoms.lower():
                return issue
        return None


# === Usage Examples ===
memory = MemoryManager("domain-14-ai-ml-infra/02-ai-agents/openclaw-workspace")

# Load the context of memory (Step 3 of the wake upprotocol)
context = memory.load_context(days=3)

# Check known issues
match = memory.check_known_issues("Pod startup very slow, waited over 30 seconds")
# → "KI-001: Terway ENI allocation delay"

# Record diagnostic results
memory.record_daily(
    "Problem: Pod OOM, root cause: JVM -Xmx > container limit, fix: adjust limits"
    is_key_insight=False,
)
```

---

## 6. Problem Resolution

## 6.1 Common Issues

| Issue | Reason | Solution |
|------|------|---------|
| Agent does not reference known issues | MEMORY.md is not loaded during wake-up | Confirm that the AGENTS.md wake-up protocol includes Step 3 |
| Memory Expansion Leading to Token Explosion | Unmet Metabolism Cleanup | Set retention policies, regularly clean low-value entries |
| Outdated Memory Misleads Decision Making | MEMORY.md not updated after environmental changes | Synchronize updating the environmental baseline after cluster changes |
| Short-Term Memories Lost | memory/ Directory not persistentized | Ensure directory is persisted in Git or use persistent storage |
| Confidence of Experience Mode Inaccurate | High confidence marked with insufficient sample size | Mark high confidence after 5+ similar events |
| Agent Records Low-Quality Memories | Unverified guesses are also recorded | SOUL.md Honesty Principle Constraint: Only record conclusions supported by data |

## 6.2 Debugging Checklist

```
MEMORY.md configuration validation:

□ Environment baseline: Does it reflect the current cluster's real configuration?
□ Known issues: Are there clear symptom descriptions and solutions?
□ Experience mode: Are confidence levels and occurrences annotated?
□ Failure lessons: Are wrong methods and right methods recorded?
□ Retention policy: Is the expiration time for each level of memory defined?
□ memory/ directory: Are there daily logs from the last 7 days?
□ Metadata: Are total_entries / stale_entries reasonable?
□ Token control: Is the total memory context < 1500 tokens?
```

---

## Related Documentation

| Document | Related Content |
|------|--------|
| [43 - OpenClaw File-First Architecture Integration Guide](./43-openclaw-framework-integration.md) | Position of MEMORY.md in the 7-file system in the kudig-database project |
| [33 - Harness Context and Memory Engineering](./33-agent-harness-context-memory.md) | Engineering implementation of a three-layer memory model |
| [openclaw-workspace/MEMORY.md](./openclaw-workspace/MEMORY.md) | Kubernetes Operations Agent Memory System Complete Configuration |
| [46 - AGENTS.md Mechanism Analysis](./46-openclaw-agents-mechanism.md) | Step 3 of the Wake-up Protocol loads MEMORY.md |
| [48 - SKILL.md Mechanism Analysis](./48-openclaw-skill-mechanism.md) | Flows of diagnostic experience from SKILL.md to MEMORY.md |

---

*This document is original content created by the kudig-database project's 02-ai-agents topic, deeply analyzing the design mechanism and engineering implementation of OpenClaw MEMORY.md.*

---

## Obsidian-related Documentation

- 02-ai-agents MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|AI Agent Engineering Topic]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|Foundation and Core Architecture of AI Agents]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|Selection and Evaluation of LLM Foundation Models]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Deep Comparison of Mainstream Agent Frameworks]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|Deep Guide on Retrieval-Augmented Generation with RAG]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Design Guidelines for Tool Use and Function Calling]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Architecture of Multi-Agent Orchestration and Collaboration]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Engineering Implementation of Memory Management and Context Window]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation Framework and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]

## See Also

- 47-openclaw-tools-mechanism
- 48-openclaw-skill-mechanism
- 50-openclaw-identity-mechanism
- 01-ai-agent-fundamentals


<!-- risk-assessed -->
