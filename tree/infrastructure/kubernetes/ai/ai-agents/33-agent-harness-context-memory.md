---
title: Agent Harness Context and Memory Engineering
description: 'description: ''**Document Type**: Deep Engineering Topics in Harness | **Last Updated**: 2026-04 | **Keywords**:
  Context Engineering,'
summary: 'description: ''**Document Type**: Deep Engineering Topics in Harness | **Last Updated**: 2026-04 | **Keywords**: Context
  Engineering,'
category: general
tags:
- ai
- ai-agent
- llm
- rag
- agent
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- all engineers
estimated_read_time: 35min
intent_queries:
- Agent Harness Context and Memory Engineering is
- How does Agent Harness Context and Memory Engineering work
- Kubernetes 14 ai ml infra best practices
trigger_keywords:
- Agent
- Harness
- Context and Memory Engineering
- ai
- ml
- infra
prerequisites:
- kubectl-basics
authors:
- name: Dillan Teagle
  role: contributor
source_path: tree/infrastructure/kubernetes/ai/ai-agents/33-agent-harness-context-memory.md
---

# Agent Harness Context and Memory Engineering

> **Document Type**: Deep Engineering Topics in Harness | **Last Updated**: 2026-04 | **Keywords**: Context Engineering, Memory Systems, RAG, Context Window, Information Compression, Persistence, Vector Retrieval, Short-Term Memory, Long-Term Memory, Scenario Memory

---

## Overview

Context (context layer) and Persistence (persistence layer) are the third and fourth layers of the Agent Harness six-layer architecture. The context layer determines the "field of vision" of the Agent - what information is seen directly affects the quality of inference; the persistence layer allows the Agent to have "memory" - maintaining state and experience across sessions.

**"Context wrong, inference fails completely"** - this is the most underestimated truth in Agent engineering. The same model, given incorrect information, may produce completely opposite conclusions. Context Engineering is becoming the core battlefield for Agent engineering in 2026.

This article systematically expounds on strategies for building contexts, prioritizing information, window management, RAG integration, memory system architecture, and the complete implementation in a Kubernetes (K8S) operational scenario.

---

## 1. Core Theories of Context Engineering

## 1.1 Context as Decision Criteria

```
How context affects the output of the Agent (empirical data):

For the same model + the same task + different contexts:

  Context A (precise relevant information) → Diagnostic accuracy 95%
  Context B (information overload) → Diagnostic accuracy 60%
  Context C (lack of key information) → Diagnostic accuracy 35%
  Context D (contains erroneous information) → Diagnostic accuracy 15%

Key conclusion:
  1. The quality of context is more important than the model's capability
  2. Information overload (noise) and information gap (missing information) are equally deadly
  3. Erroneous information is more dangerous than no information
  4. Context construction is an engineering problem, not a prompt problem
```

## 1.2 Principle of Signal-to-Noise Ratio

```
Context signal-to-noise ratio (SNR) optimization:

High signal information (must include):
  ✓ Relevant documents/code for the current task
  ✓ Environment status (cluster information, configuration, version)
  ✓ Error logs and critical events
  ✓ Solutions to historical similar problems
  ✓ Constraints and security boundaries

Low signal information (should filter):
  ✗ Irrelevant system log noise
  ✗ Repeated successful operation records
  ✗ Outdated historical information
  ✗ Irrelevant knowledge documents
  ✗ Redundant metadata

Signal-to-noise ratio quantification formula:
  SNR = Number of High Signal Information Tokens / Total Context Tokens
  Goal: SNR > 0.7 (at least 70% of context is high signal information)
```

---

## 2. Hierarchical Context Construction Architecture

## 2.1 Four-Level Context Model

```
Context four-layer model:

Layer 1: System Context (System Layer)
  │  Role Definition (SOUL.md), Constraints, Output Format
  │  Priority: Highest | Change Frequency: Lowest
  │
Layer 2: Environment Context (Environment Layer)
  │  Cluster Status, List of Namespaces, Node Information, Current Configuration
  │  Priority: High | Change Frequency: Medium (once per task scan)
  │
Layer 3: Knowledge Context (Knowledge Layer)
  │  Relevant Documents from RAG Retrieval, Historical Similar Work Orders, SOP Processes
  │  Priority: Medium | Change Frequency: Dynamically Built on Each Query
  │
Layer 4: History Context (History Layer)
  │  Session Dialogue History, Execution Trajectory, Tool Outputs
  │  Priority: Dynamic | Change Frequency: Updated After Each Step
  │
Token budget allocation (using a 128K window example):
  System:      ~5K tokens  (4%)
  Environment: ~10K tokens (8%)
  Knowledge:   ~30K tokens (23%)
  History:     ~40K tokens (31%)
  Reserved:    ~43K tokens (34%,  reserved for model output and inference)
```

## 2.2 Complete Implementation of Context Manager

```python
from dataclasses import dataclass, field
from typing import Optional, Any
import tiktoken

@dataclass
class ContextBudget:
    """Context Token Budget"""
    total: int = 128000
    system: int = 5000
    environment: int = 10000
    knowledge: int = 30000
    history: int = 40000
    reserved: int = 43000  # 模型输出保留

class ContextManager:
    """Context Manager: Hierarchical Construction, Priority Sorting, Dynamic Compression"""

    def __init__(
        self,
        budget: ContextBudget = None,
        rag_retriever=None,
        encoder_name: str = "cl100k_base",
    ):
        self.budget = budget or ContextBudget()
        self.rag = rag_retriever
        self.encoder = tiktoken.get_encoding(encoder_name)

    def count_tokens(self, text: str) -> int:
        """Precisely calculate the number of tokens"""
        return len(self.encoder.encode(text))

    def build_context(
        self,
        task: str,
        system_prompt: str = None,
        environment: dict = None,
        history: list = None,
        additional_context: dict = None,
    ) -> str:
        """Hierarchical construction of context"""
        context_parts = []
        remaining_budget = self.budget.total - self.budget.reserved

        # Layer 1: System Context
        if system_prompt:
            system_text = self._format_system(system_prompt)
            system_tokens = self.count_tokens(system_text)
            if system_tokens <= self.budget.system:
                context_parts.append(("system", system_text, system_tokens))
                remaining_budget -= system_tokens

        # Layer 2: Environmental Context
        if environment:
            env_text = self._format_environment(environment)
            env_tokens = self.count_tokens(env_text)
            env_budget = min(self.budget.environment, remaining_budget)
            if env_tokens > env_budget:
                env_text = self._compress_environment(env_text, env_budget)
                env_tokens = self.count_tokens(env_text)
            context_parts.append(("environment", env_text, env_tokens))
            remaining_budget -= env_tokens

        # Layer 3: Knowledge Context (RAG Retrieval)
        if self.rag:
            knowledge_budget = min(self.budget.knowledge, remaining_budget)
            knowledge_text = self._retrieve_knowledge(task, knowledge_budget)
            knowledge_tokens = self.count_tokens(knowledge_text)
            context_parts.append(("knowledge", knowledge_text, knowledge_tokens))
            remaining_budget -= knowledge_tokens

        # Layer 4: Historical Context
        if history:
            history_budget = min(self.budget.history, remaining_budget)
            history_text = self._compress_history(history, history_budget)
            history_tokens = self.count_tokens(history_text)
            context_parts.append(("history", history_text, history_tokens))
            remaining_budget -= history_tokens

        # Assemble final context
        return self._assemble(context_parts)

    def _format_system(self, system_prompt: str) -> str:
        """Format system context"""
        return f"## System Commands\n\n{system_prompt}"

    def _format_environment(self, environment: dict) -> str:
        """Format the environment context"""
        parts = ["## Current Environment"]
        if "cluster" in environment:
            parts.append(f"Cluster: {environment['cluster']}")
        if "kubernetes_version" in environment:
            parts.append(f"k8s Version: {environment['kubernetes_version']}")
        if "nodes" in environment:
            parts.append(f"Node Count: {len(environment['nodes'])}")
            for node in environment["nodes"][:5]:  # 最多展示 5 个
                parts.append(f"  - {node['name']}: {node.get('status', 'Unknown')}")
        if "namespaces" in environment:
            parts.append(f"Active Namespaces: {', '.join(environment['namespaces'][:10])}")
        return "\n".join(parts)

    def _retrieve_knowledge(self, task: str, budget: int) -> str:
        """RAG Knowledge Retrieval"""
        documents = self.rag.retrieve(task, top_k=10)

        parts = ["## Related Knowledge"]
        current_tokens = self.count_tokens("## Related Knowledge\n")

        for doc in documents:
            doc_text = f"\n### {doc['title']}\n{doc['content']}\n"
            doc_tokens = self.count_tokens(doc_text)
            if current_tokens + doc_tokens > budget:
                # Try truncating documents
                available = budget - current_tokens - 50
                if available > 200:
                    truncated = self._truncate_to_tokens(doc['content'], available)
                    parts.append(f"\n### {doc['title']}\n{truncated}\n...")
                break
            parts.append(doc_text)
            current_tokens += doc_tokens

        return "\n".join(parts)

    def _compress_history(self, history: list, budget: int) -> str:
        """Smart History Compression"""
        parts = ["## Execution History"]
        current_tokens = self.count_tokens("## Execution History\n")

        # Strategy 1: Always retain critical steps
        key_steps = [h for h in history if h.get("is_key_step")]
        # Strategy 2: Always retain error steps
        error_steps = [h for h in history if h.get("error")]
        # Strategy 3: Retain the most recent N steps
        recent_steps = history[-3:]

        # Merge and deduplicate (maintain sequence)
        must_keep = set()
        for step in key_steps + error_steps + recent_steps:
            must_keep.add(id(step))

        # Prioritize adding steps that must be retained
        for step in history:
            if id(step) in must_keep:
                step_text = self._format_step(step)
                step_tokens = self.count_tokens(step_text)
                if current_tokens + step_tokens > budget:
                    break
                parts.append(step_text)
                current_tokens += step_tokens

        # If budget allows, add summaries of other steps
        remaining_steps = [h for h in history if id(h) not in must_keep]
        if remaining_steps and current_tokens < budget - 200:
            summary = f"\n[Skipped {len(remaining_steps)} intermediate steps]"
            parts.append(summary)

        return "\n".join(parts)

    def _format_step(self, step: dict) -> str:
        """Format single-step records"""
        parts = [f"\n### Step {step.get('iteration', '?')}"]
        if step.get("thought"):
            parts.append(f"Thought: {step['thought'][:200]}")
        if step.get("action"):
            parts.append(f"Action: {step['action']}")
        if step.get("tool_result"):
            result = str(step["tool_result"])[:300]
            parts.append(f"Result: {result}")
        if step.get("error"):
            parts.append(f"Error: {step['error']}")
        return "\n".join(parts)

    def _truncate_to_tokens(self, text: str, max_tokens: int) -> str:
        """Truncate text to a specified number of tokens"""
        tokens = self.encoder.encode(text)
        if len(tokens) <= max_tokens:
            return text
        return self.encoder.decode(tokens[:max_tokens])

    def _assemble(self, context_parts: list) -> str:
        """Assemble final context"""
        parts = []
        for name, text, tokens in context_parts:
            parts.append(text)
        return "\n\n---\n\n".join(parts)
```

---

## 3. RAG Integration Design

## 3.1 Knowledge Base Indexing Architecture

```
Kubernetes Operations Knowledge Base Index Architecture:

Data source:
  ├── kudig-database documentation (950+ Markdown files)
  ├── Official Kubernetes Documentation
  ├── Historical work order records
  ├── SOP Operation Manual
  └── Alert rules and handling guidelines

Index pipeline:
  document → chunking → embedding → vector storage

Chunk strategy:
  ├── Document-level chunking: split by ## headers, maintaining logical integrity
  ├── Paragraph-level chunking: 500-1000 tokens/chunk, overlapping 100 tokens
  ├── Code block splitting: Complete code blocks as independent chunk
  └── Table block: table + context explanation as independent chunk

Search strategy:
  ├── Semantic search: Embedding similarity Top-K
  ├── Keyword search: BM25 full-text search
  ├── Hybrid search: semantic + keyword weighted fusion
  └── Reorder: Cross-encoder fine-tuning
```

## 3.2 RAG Retrieval Engine Implementation

```python
from dataclasses import dataclass
from typing import Optional

@dataclass
class Document:
    """Document Model"""
    id: str
    title: str
    content: str
    source: str
    category: str
    metadata: dict = None
    score: float = 0.0

class HybridRAGRetriever:
    """Hybrid RAG Retrieval Engine: Semantic + Keyword + Reordering"""

    def __init__(
        self,
        vector_store,
        bm25_index,
        reranker=None,
        semantic_weight: float = 0.6,
        keyword_weight: float = 0.4,
    ):
        self.vector_store = vector_store
        self.bm25_index = bm25_index
        self.reranker = reranker
        self.semantic_weight = semantic_weight
        self.keyword_weight = keyword_weight

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        category_filter: str = None,
        min_score: float = 0.3,
    ) -> list[Document]:
        """Hybrid Retrieval"""
        # Stage 1: Preliminary sorting — semantic retrieval + keyword retrieval
        semantic_results = self.vector_store.search(
            query, top_k=top_k * 3, filter={"category": category_filter}
        )
        keyword_results = self.bm25_index.search(
            query, top_k=top_k * 3
        )

        # Stage 2: Score Fusion (Reciprocal Rank Fusion)
        fused = self._reciprocal_rank_fusion(
            semantic_results, keyword_results,
            weights=[self.semantic_weight, self.keyword_weight],
        )

        # Stage 3: Precise Ranking (Cross-encoder Reranking)
        if self.reranker:
            fused = self.reranker.rerank(query, fused, top_k=top_k)
        else:
            fused = fused[:top_k]

        # Stage 4: Filter Low-scoring Results
        return [doc for doc in fused if doc.score >= min_score]

    def _reciprocal_rank_fusion(
        self,
        *result_lists,
        weights: list[float] = None,
        k: int = 60,
    ) -> list[Document]:
        """Reciprocal Rank Fusion (RRF) Score Fusion"""
        if weights is None:
            weights = [1.0] * len(result_lists)

        doc_scores: dict[str, float] = {}
        doc_map: dict[str, Document] = {}

        for results, weight in zip(result_lists, weights):
            for rank, doc in enumerate(results):
                rrf_score = weight / (k + rank + 1)
                doc_scores[doc.id] = doc_scores.get(doc.id, 0) + rrf_score
                doc_map[doc.id] = doc

        # Sort by Fusion Score
        sorted_ids = sorted(doc_scores.keys(), key=lambda x: doc_scores[x], reverse=True)
        result = []
        for doc_id in sorted_ids:
            doc = doc_map[doc_id]
            doc.score = doc_scores[doc_id]
            result.append(doc)

        return result


class ContextAwareRetriever:
    """Context-Aware Retrieval System: Adjust Retrieval Strategies Based on Task Stages"""

    def __init__(self, base_retriever: HybridRAGRetriever):
        self.base = base_retriever

    def retrieve_for_phase(
        self,
        query: str,
        phase: str,
        existing_context: str = "",
    ) -> list[Document]:
        """Adjust Retrieval Based on Execution Stages"""
        if phase == "gather":
            # Information Gathering Phase: Broad Search
            return self.base.retrieve(query, top_k=8, min_score=0.2)
        elif phase == "analyze":
            # Analysis Phase: Precise Search + Exclude Existing Information
            docs = self.base.retrieve(query, top_k=5, min_score=0.5)
            return self._filter_redundant(docs, existing_context)
        elif phase == "act":
            # Execution Phase: Only Search for SOPs and Guidelines
            return self.base.retrieve(
                query, top_k=3, category_filter="sop", min_score=0.4
            )
        return self.base.retrieve(query, top_k=5)

    def _filter_redundant(self, docs: list, existing_context: str) -> list:
        """Filter Documents That Are Repeated with Existing Context"""
        filtered = []
        for doc in docs:
            # Simple De-duplication: Check if Document Titles are Already in Context
            if doc.title not in existing_context:
                filtered.append(doc)
        return filtered
```

---

## 4. Memory System Architecture

## 4.1 Three-Layer Memory Model

```
Agent memory three-layer model:

1. Short-term Memory (Working Memory)
   │  Current session's dialogue history and execution trajectory
   │  Lifecycle: Per session
   │  Storage: Memory
   │  Purpose: Maintain conversation coherence
   │
2. Episodic Memory
   │  Complete records of historical tasks
   │  Lifecycle: Persistent storage, retrievable
   │  Storage: Vector database + relational database
   │  Purpose: Learn from past experiences
   │
3. Semantic Memory
   │  Abstracted knowledge, rules, patterns
   │  Lifecycle: Permanent storage, periodically updated
   │  Storage: Knowledge graph + vector database
   │  Purpose: Provide domain knowledge

Memory flow:
  Short-term Memory ──(Extract after task completion)──→ Episodic Memory
  Episodic Memory ──(Pattern abstraction)──→ Semantic Memory
  semantic memory ──(retrieval injection)──→ short-term memory
```

## 4.2 Complete Implementation of the Memory System

```python
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional, Any
import json

@dataclass
class MemoryEntry:
    """Memory Entry"""
    id: str
    content: str
    memory_type: str        # short_term / episodic / semantic
    created_at: str
    task_id: Optional[str] = None
    tags: list = field(default_factory=list)
    importance: float = 0.5  # 0.0 - 1.0
    access_count: int = 0
    last_accessed: Optional[str] = None
    metadata: dict = field(default_factory=dict)

class MemorySystem:
    """Agent Memory System"""

    def __init__(self, vector_store, kv_store, max_short_term: int = 50):
        self.vector_store = vector_store
        self.kv_store = kv_store
        self.max_short_term = max_short_term
        self._short_term: list[MemoryEntry] = []

    # === Short-Term Memory ===

    def add_to_short_term(self, content: str, importance: float = 0.5,
                          metadata: dict = None):
        """Add Short-term Memory"""
        entry = MemoryEntry(
            id=f"st_{len(self._short_term)}",
            content=content,
            memory_type="short_term",
            created_at=datetime.utcnow().isoformat(),
            importance=importance,
            metadata=metadata or {},
        )
        self._short_term.append(entry)

        # Capacity Management: Evict Low-importance Memories When Exceeding Limits
        if len(self._short_term) > self.max_short_term:
            self._evict_short_term()

    def get_short_term(self, last_n: int = None) -> list[MemoryEntry]:
        """Get short-term memory"""
        if last_n:
            return self._short_term[-last_n:]
        return self._short_term

    def _evict_short_term(self):
        """Short-term memory eviction strategy: retain high importance + recent"""
        # Retain importance > 0.7 + The last 10
        important = [m for m in self._short_term if m.importance > 0.7]
        recent = self._short_term[-10:]
        keep = list({id(m): m for m in important + recent}.values())
        keep.sort(key=lambda m: m.created_at)
        self._short_term = keep[:self.max_short_term]

    # === Scenario Memory ===

    def save_episode(self, task_id: str, task: str, trajectory: list,
                     result: dict):
        """Save the scenario memory of task execution"""
        episode = {
            "task_id": task_id,
            "task": task,
            "result_status": result.get("status"),
            "answer": result.get("answer", "")[:500],
            "steps": len(trajectory),
            "key_findings": self._extract_key_findings(trajectory),
            "errors_encountered": self._extract_errors(trajectory),
            "tools_used": self._extract_tools(trajectory),
            "timestamp": datetime.utcnow().isoformat(),
        }

        # Store in Vector Database (supports semantic search)
        embedding_text = f"Task: {task}\nResult: {result.get('answer', '')[:200]}"
        self.vector_store.upsert(
            id=task_id,
            text=embedding_text,
            metadata=episode,
        )

        # Store in KV Storage (supports exact queries)
        self.kv_store.set(f"episode:{task_id}", json.dumps(episode))

    def recall_similar_episodes(self, task: str, top_k: int = 3) -> list:
        """Search for similar historical tasks"""
        results = self.vector_store.search(task, top_k=top_k)
        episodes = []
        for r in results:
            episodes.append({
                "task": r.metadata.get("task", ""),
                "result": r.metadata.get("result_status", ""),
                "key_findings": r.metadata.get("key_findings", []),
                "tools_used": r.metadata.get("tools_used", []),
                "similarity": r.score,
            })
        return episodes

    # === Semantic Memory ===

    def store_semantic(self, knowledge: str, tags: list, importance: float = 0.8):
        """Store semantic memory (abstract knowledge)"""
        entry = MemoryEntry(
            id=f"sem_{datetime.utcnow().timestamp()}",
            content=knowledge,
            memory_type="semantic",
            created_at=datetime.utcnow().isoformat(),
            tags=tags,
            importance=importance,
        )
        self.vector_store.upsert(
            id=entry.id,
            text=knowledge,
            metadata={"type": "semantic", "tags": tags,
                       "importance": importance},
        )

    def recall_semantic(self, query: str, tags: list = None,
                        top_k: int = 5) -> list:
        """Semantic Memory Retrieval"""
        filter_dict = {"type": "semantic"}
        if tags:
            filter_dict["tags"] = {"$in": tags}
        return self.vector_store.search(query, top_k=top_k, filter=filter_dict)

    # === Memory Extraction ===

    def consolidate(self, llm, recent_episodes: int = 20):
        """Memory consolidation: Extracting semantic memory from recent scenario memory"""
        episodes = self._get_recent_episodes(recent_episodes)
        if not episodes:
            return

        prompt = f"""
        分析以下 {len(episodes)} 个历史任务执行记录，
        提炼出可复用的模式和知识:
        
        {json.dumps(episodes, ensure_ascii=False, indent=2)}
        
        请输出:
        1. 常见故障模式及解决方案
        2. 高效的工具使用策略
        3. 需要注意的陷阱和反模式
        """
        insights = llm.invoke(prompt)
        self.store_semantic(
            insights,
            tags=["consolidated", "pattern"],
            importance=0.9,
        )

    # === Helper Methods ===

    def _extract_key_findings(self, trajectory: list) -> list:
        """Extract Key Discoveries from the Trajectory"""
        findings = []
        for step in trajectory:
            if step.get("is_key_step"):
                findings.append(step.get("thought", "")[:100])
        return findings

    def _extract_errors(self, trajectory: list) -> list:
        """Extract errors from the trajectory"""
        return [
            step.get("error", "")[:100]
            for step in trajectory
            if step.get("error")
        ]

    def _extract_tools(self, trajectory: list) -> list:
        """Extract a list of tools used from the trajectory"""
        tools = set()
        for step in trajectory:
            if step.get("tool_name"):
                tools.add(step["tool_name"])
        return list(tools)

    def _get_recent_episodes(self, n: int) -> list:
        """Get the most recent N short-term memories"""
        # Get from KV storage (descending by time)
        keys = self.kv_store.keys("episode:*")
        recent_keys = sorted(keys, reverse=True)[:n]
        return [json.loads(self.kv_store.get(k)) for k in recent_keys]
```

---

## 5. Context Window Management

## 5.1 Dynamic Window Strategy

```python
class DynamicWindowManager:
    """Dynamic Context Window Manager

    根据任务复杂度和执行阶段动态调整各层的 Token 预算。
    """

    def __init__(self, total_window: int = 128000):
        self.total = total_window
        self.reserved_for_output = int(total_window * 0.25)

    def allocate(self, task_complexity: str, phase: str,
                 history_length: int) -> ContextBudget:
        """Allocate Context Budget Dynamically"""
        available = self.total - self.reserved_for_output

        if task_complexity == "simple":
            return ContextBudget(
                total=self.total,
                system=3000,
                environment=5000,
                knowledge=int(available * 0.3),
                history=int(available * 0.2),
                reserved=self.reserved_for_output,
            )
        elif task_complexity == "complex":
            # Complex Tasks: More Knowledge and Historical Data
            return ContextBudget(
                total=self.total,
                system=5000,
                environment=10000,
                knowledge=int(available * 0.35),
                history=int(available * 0.3),
                reserved=self.reserved_for_output,
            )
        else:  # multi-step
            # Multi-step Tasks: Adjust Based on Stages
            if phase == "gather":
                knowledge_ratio = 0.4
                history_ratio = 0.15
            elif phase == "analyze":
                knowledge_ratio = 0.3
                history_ratio = 0.35
            else:  # act
                knowledge_ratio = 0.15
                history_ratio = 0.2

            return ContextBudget(
                total=self.total,
                system=5000,
                environment=8000,
                knowledge=int(available * knowledge_ratio),
                history=int(available * history_ratio),
                reserved=self.reserved_for_output,
            )
```

## 5.2 Incremental Context Update

```python
class IncrementalContextUpdater:
    """Incremental Context Updater: Avoid Rebuilding Complete Context Per Step"""

    def __init__(self, context_manager: ContextManager):
        self.ctx_mgr = context_manager
        self._cached_system: str = ""
        self._cached_environment: str = ""
        self._cached_knowledge: str = ""
        self._history_buffer: list = []

    def initial_build(self, task: str, system_prompt: str,
                      environment: dict) -> str:
        """Initial Build (First Step)"""
        self._cached_system = self.ctx_mgr._format_system(system_prompt)
        self._cached_environment = self.ctx_mgr._format_environment(environment)
        if self.ctx_mgr.rag:
            self._cached_knowledge = self.ctx_mgr._retrieve_knowledge(
                task, self.ctx_mgr.budget.knowledge
            )
        return self._assemble()

    def update_after_step(self, step: dict) -> str:
        """Incremental Update After Each Step (Only Update Historical Layers)"""
        self._history_buffer.append(step)

        # Historical Compression (Compress When Budget Exceeded)
        history_text = self.ctx_mgr._compress_history(
            self._history_buffer, self.ctx_mgr.budget.history
        )

        return self._assemble(history_override=history_text)

    def refresh_knowledge(self, new_query: str) -> str:
        """Knowledge Layer Refresh (When Task Direction Changes)"""
        if self.ctx_mgr.rag:
            self._cached_knowledge = self.ctx_mgr._retrieve_knowledge(
                new_query, self.ctx_mgr.budget.knowledge
            )
        return self._assemble()

    def _assemble(self, history_override: str = None) -> str:
        """Context Assembly"""
        parts = [self._cached_system, self._cached_environment]
        if self._cached_knowledge:
            parts.append(self._cached_knowledge)
        if history_override:
            parts.append(history_override)
        elif self._history_buffer:
            parts.append(self.ctx_mgr._compress_history(
                self._history_buffer, self.ctx_mgr.budget.history
            ))
        return "\n\n---\n\n".join(parts)
```

---

## 6. K8S Operational Context Templates

## 6.1 Cluster Environment Scanner

```python
class K8sEnvironmentScanner:
    """K8S Cluster Environment Scanner: Automatically Collects Environmental Context"""

    def __init__(self, kubectl_tool):
        self.kubectl = kubectl_tool

    def scan(self) -> dict:
        """Comprehensive Scan of Cluster Environment"""
        env = {}

        # Basic Information
        env["cluster_info"] = self._get_cluster_info()
        env["kubernetes_version"] = self._get_version()

        # Node Information
        env["nodes"] = self._get_node_summary()

        # Namespace
        env["namespaces"] = self._get_namespaces()

        # Resource Usage Overview
        env["resource_usage"] = self._get_resource_overview()

        # Recent Alarm Events
        env["recent_warnings"] = self._get_recent_warnings()

        return env

    def _get_node_summary(self) -> list:
        """Get node summary"""
        result = self.kubectl.execute(resource="nodes", output="wide")
        nodes = []
        for line in result.get("output", "").split("\n")[1:]:
            parts = line.split()
            if len(parts) >= 5:
                nodes.append({
                    "name": parts[0],
                    "status": parts[1],
                    "roles": parts[2],
                    "version": parts[4],
                })
        return nodes

    def _get_recent_warnings(self, limit: int = 20) -> list:
        """Get recent alarm events"""
        result = self.kubectl.execute(
            resource="events",
            namespace="--all-namespaces",
            extra_args="--field-selector type=Warning --sort-by=.lastTimestamp",
        )
        warnings = []
        for line in result.get("output", "").split("\n")[1:limit + 1]:
            if line.strip():
                warnings.append(line.strip())
        return warnings

    def format_for_context(self, env: dict) -> str:
        """Format environment information into context text"""
        parts = [
            "## Cluster Environment Information",
            f"k8s Version: {env.get('kubernetes_version', 'Unknown')}",
            f"Node Count: {len(env.get('nodes', []))}",
        ]

        # Node Status Summary
        nodes = env.get("nodes", [])
        ready_count = sum(1 for n in nodes if n.get("status") == "Ready")
        parts.append(f"Node Status: {ready_count}/{len(nodes)} Ready")

        if env.get("recent_warnings"):
            parts.append("\n### Recent Alarm Events")
            for w in env["recent_warnings"][:10]:
                parts.append(f"  - {w}")

        return "\n".join(parts)
```

## 6.2 Diagnostic Task Context Template

```python
class DiagnosisContextTemplate:
    """Diagnostic Task Context Template"""

    SYSTEM_PROMPT_TEMPLATE = """
你是 K8S 运维诊断专家 Agent。你的任务是根据提供的集群环境信息和工具输出，
诊断 Kubernetes 集群中的问题。

## Work Principles
1. 每个诊断结论必须有具体的 Event 或日志证据支撑
2. 优先使用只读命令收集信息
3. Unclear conclusions marked as "Need Manual Confirmation"
4. 输出的 YAML/命令必须语法正确

## Output Format
- 根因分析: [具体原因]
- 证据: [Event/日志引用]
- 建议操作: [操作步骤]
- 风险等级: [高/中/低]
- 置信度: [0-100%]
"""

    def build_diagnosis_context(
        self,
        task: str,
        env_scan: dict,
        knowledge: list,
        history: list = None,
    ) -> str:
        """Build the complete context for a diagnostic task"""
        parts = [
            self.SYSTEM_PROMPT_TEMPLATE,
            f"\n## Current Diagnosis Task\n{task}",
            self._format_env(env_scan),
        ]

        if knowledge:
            parts.append("\n## Relevant Knowledge")
            for doc in knowledge[:5]:
                parts.append(f"### {doc['title']}\n{doc['content'][:500]}\n")

        if history:
            parts.append("\n## Steps Executed")
            for step in history[-5:]:
                parts.append(f"Step {step.get('iteration')}: "
                           f"{step.get('thought', '')[:150]}")

        return "\n".join(parts)

    def _format_env(self, env: dict) -> str:
        """Format environment information"""
        scanner = K8sEnvironmentScanner(None)
        return scanner.format_for_context(env)
```

---

## 7. Best Practices

## 7.1 Core Principles of Context Engineering

| Principle | Explanation | Practice Suggestions |
|------|------|---------|
| **Signal-to-Noise Ratio Priority** | High signal information ratio in context > 70% | Strictly filter irrelevant information |
| **Layered Construction** | System → Environment → Knowledge → History clear layers | Each layer independently managed, dynamically adjusted |
| **Token Budget** | Clearly allocated token budget for each layer | Use ContextBudget to control |
| **Incremental Updates** | Avoid rebuilding the complete context at each step | Cache unchanged layers, only update changed layers |
| **Smart Compression** | Retain key steps in historical information | Errors + Key Discoveries + Last N Steps |
| **Pre-scan Environment** | Collect environmental information before tasks start | Use EnvironmentScanner |

## 7.2 Memory System Core Principles

| Principle | Explanation | Practice Suggestions |
|------|------|---------|
| **Three-Tier Separation** | Manage short-term/scene/semantic memory independently | Different storage backends, different lifecycle management |
| **Automatic Extraction** | Automatically extract semantic memory from scene memory | Regularly run consolidate |
| **Relevance Retrieval** | Retrieve relevant historical data based on current task | Use vector similarity retrieval |
| **Capacity Management** | Short-term memory has a limit | Eliminate low-importance memories |
| **Privacy Protection** | Do not store sensitive information in memory | De-sensitize before storing |

---

## Related Documents

| Document | Relevant Content |
|------|--------|
| [30 - Agent Harness Engineering](./30-agent-harness-engineering.md) | Definition of the Context Layer and Persistence Layer in the Six-Layer Architecture |
| [31 - Loop and Execution Engine](./31-agent-harness-loop-execution.md) | Flow of Context usage in the Loop |
| [04 - RAG Knowledge Retrieval](./04-rag-knowledge-retrieval.md) | Foundation theory and implementation of RAG |
| [07 - Memory Management](./07-memory-context-management.md) | Fundamental concepts of the Agent's memory system |

---

## References

| Source | Content | Date |
|------|------|------|
| Anthropic | Best practices for Context Engineering | February 2026 |
| LangChain | Experimental analysis of the impact of Context Management on Agent Performance | February 2026 |
| Simon Willison | Context Engineering vs Prompt Engineering | 2026-01 |
| Microsoft | Design of AutoGen Memory System | 2025-2026 |

---

*This document is original content from the kudig-database project series 02-ai-agents, delving into the Context and Memory Engineering in the Agent Harness.*

---

## Related Obsidian Documents

- 02-ai-agents KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|[[AI Agent Engineering Special Topic|AI Agent Engineering Special Topic]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|[[AI Agent Fundamentals and Core Architecture|AI Agent Fundamentals and Core Architecture]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|LLM Foundation Model Selection and Evaluation]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Mainstream Agent Framework Deep Comparison]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|RAG Retrieval Enhanced Generation Deep Guide]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Tool Usage and Function Calling Design Guidelines]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Multi-Agent Orchestration and Collaboration Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation System and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]

## See Also

- 31-agent-harness-loop-execution
- 32-agent-harness-tool-engineering
- 34-agent-harness-verification-quality
- 35-agent-harness-security-constraints


<!-- risk-assessed -->
