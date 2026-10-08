---
title: Agent State Management Patterns
description: 'Stateless vs. stateful Agent architecture, checkpoint strategies, state storage solutions, state replay debugging, and long-term memory hierarchical design'
summary: 'Stateless vs. stateful Agent architecture, checkpoint strategies, state storage solutions, state replay debugging, and long-term memory hierarchical design'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- state-management
- checkpoint
- memory
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
- What is Agent State Management Patterns
- How to manage Agent state
- Detailed explanation of Agent checkpoint strategies
trigger_keywords:
- agent-state
- checkpoint
- memory-management
- state-replay
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/10-agent-state-management-patterns.md
---
# Agent State Management Patterns

## Overview

Agent state management is the core challenge in building production-grade AI Agents. LLM Agent execution often spans multiple conversation turns, multiple tool calls, and even multiple sessions. How to efficiently manage these states while ensuring reliability directly determines the maintainability and scalability of an Agent system.

This document systematically introduces the complete methodology for Agent state management: architecture selection from stateless to stateful, checkpoint strategy design, state storage solution comparison, state replay debugging techniques, and the layered architecture of long-term memory.

## Stateless vs. Stateful Agents

### Stateless Agent

A stateless Agent starts from scratch on every execution and retains no historical state:

```python
class StatelessAgent:
    """Stateless Agent - each call is independent"""

    def __init__(self, system_prompt: str, tools: list):
        self.system_prompt = system_prompt
        self.tools = tools

    async def execute(self, user_input: str) -> str:
        """Execute a single Agent task without retaining history"""
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_input},
        ]

        response = await self.llm_call(messages)

        while response.has_tool_calls:
            tool_results = []
            for tool_call in response.tool_calls:
                result = await self.execute_tool(tool_call)
                tool_results.append(result)

            messages.append(response.message)
            messages.extend(tool_results)
            response = await self.llm_call(messages)

        return response.content
```

Advantages of a stateless Agent:

```
Advantages:
  - Simple and reliable, no risk of state loss
  - Easy horizontal scaling, no affinity requirements
  - Simple debugging, each execution is independent
  - Suitable for single-turn tasks (Q&A, translation, summarization)

Disadvantages:
  - Cannot maintain multi-turn conversation context
  - Cannot learn or accumulate experience
  - Complex tasks require repeated context input
  - Higher token consumption (repeatedly passing history)
```

### Stateful Agent

A stateful Agent maintains execution state across calls:

```python
class StatefulAgent:
    """Stateful Agent - maintains execution history and memory"""

    def __init__(self, agent_id: str, state_store: StateStore):
        self.agent_id = agent_id
        self.state_store = state_store

    async def execute(self, user_input: str) -> str:
        # Load historical state
        state = await self.state_store.load(self.agent_id)

        if state is None:
            state = AgentState(
                conversation_history=[],
                tool_results=[],
                memory=AgentMemory(),
                metadata={},
            )

        # Add user input
        state.conversation_history.append({
            "role": "user",
            "content": user_input,
        })

        # Build messages including history
        messages = self._build_messages(state)

        response = await self.llm_call(messages)

        while response.has_tool_calls:
            for tool_call in response.tool_calls:
                result = await self.execute_tool(tool_call)
                state.tool_results.append({
                    "tool": tool_call.name,
                    "input": tool_call.arguments,
                    "output": result.output,
                    "timestamp": datetime.utcnow(),
                })

            state.conversation_history.append(response.message)
            state.conversation_history.append({
                "role": "tool",
                "content": result.output,
                "tool_call_id": tool_call.id,
            })

            response = await self.llm_call(self._build_messages(state))

        # Save Agent response
        state.conversation_history.append({
            "role": "assistant",
            "content": response.content,
        })

        # Update memory
        await state.memory.update(state.conversation_history)

        # Persist state
        await self.state_store.save(self.agent_id, state)

        return response.content

    def _build_messages(self, state: AgentState) -> list:
        """Build LLM messages, potentially compressing history"""
        messages = [{"role": "system", "content": self.system_prompt}]

        # History may need to be compressed to fit the context window
        compressed_history = self._compress_history(
            state.conversation_history
        )
        messages.extend(compressed_history)

        return messages
```

### Architecture Selection Guide

```
Selection Decision Tree:

Does the task require cross-call context?
  ├── No → Stateless Agent
  └── Yes → Is context limited to a single session?
      ├── Yes → Session-level stateful Agent
      └── No → Is cross-session memory needed?
          ├── No → Session-level stateful Agent + session timeout
          └── Yes → Persistent stateful Agent + layered memory

Recommended solutions:
  Simple Q&A → Stateless
  Customer service dialogue → Session-level stateful (TTL 30 minutes)
  Code assistant → Session-level stateful (TTL 2 hours)
  Research assistant → Persistent stateful + long-term memory
  Autonomous Agent → Persistent stateful + full layered memory
```

## Checkpoint Strategies

### Checkpoint Timing

```python
from enum import Enum

class CheckpointStrategy(Enum):
    EVERY_STEP = "every_step"           # Checkpoint at every step
    KEY_NODES = "key_nodes"             # Checkpoint at key nodes
    TIME_BASED = "time_based"           # Time-based checkpoint
    ADAPTIVE = "adaptive"               # Adaptive checkpoint


class CheckpointManager:
    """Agent checkpoint manager"""

    def __init__(
        self,
        strategy: CheckpointStrategy,
        checkpoint_store: CheckpointStore,
    ):
        self.strategy = strategy
        self.store = checkpoint_store
        self.last_checkpoint_time = datetime.utcnow()
        self.step_count = 0

    async def maybe_checkpoint(
        self,
        agent_id: str,
        state: AgentState,
        step_type: str,
    ) -> bool:
        """Decide whether to create a checkpoint based on the strategy"""
        should_checkpoint = False

        if self.strategy == CheckpointStrategy.EVERY_STEP:
            should_checkpoint = True

        elif self.strategy == CheckpointStrategy.KEY_NODES:
            # Create checkpoints only at key nodes
            key_step_types = {
                "llm_inference",
                "tool_execution",
                "human_approval",
                "state_transition",
            }
            should_checkpoint = step_type in key_step_types

        elif self.strategy == CheckpointStrategy.TIME_BASED:
            # Create a checkpoint every N seconds
            elapsed = (datetime.utcnow() - self.last_checkpoint_time).total_seconds()
            should_checkpoint = elapsed >= 30  # every 30 seconds

        elif self.strategy == CheckpointStrategy.ADAPTIVE:
            # Adaptive strategy: adjust based on execution complexity
            should_checkpoint = self._adaptive_decision(state, step_type)

        if should_checkpoint:
            await self._create_checkpoint(agent_id, state)
            self.last_checkpoint_time = datetime.utcnow()
            self.step_count += 1
            return True

        return False

    def _adaptive_decision(
        self,
        state: AgentState,
        step_type: str,
    ) -> bool:
        """Adaptive checkpoint decision"""
        # Checkpoint immediately after high-risk operations
        high_risk_steps = {"tool_execution", "state_mutation"}
        if step_type in high_risk_steps:
            return True

        # Checkpoint when state size exceeds threshold
        state_size = self._estimate_state_size(state)
        if state_size > 1024 * 1024:  # 1MB
            return True

        # Checkpoint after a certain number of steps since the last checkpoint
        if self.step_count % 5 == 0:
            return True

        return False

    async def _create_checkpoint(
        self,
        agent_id: str,
        state: AgentState,
    ) -> str:
        """Create a checkpoint"""
        checkpoint_id = f"{agent_id}-{uuid.uuid4().hex[:8]}"

        checkpoint = Checkpoint(
            id=checkpoint_id,
            agent_id=agent_id,
            state=state.serialize(),
            created_at=datetime.utcnow(),
            step_count=self.step_count,
        )

        await self.store.save(checkpoint)
        return checkpoint_id
```

### Checkpoint Storage Structure

```python
@dataclass
class Checkpoint:
    """Checkpoint data structure"""
    id: str
    agent_id: str
    state: bytes              # Serialized Agent state
    created_at: datetime
    step_count: int
    metadata: dict = field(default_factory=dict)

    # Checkpoint chain
    parent_checkpoint_id: Optional[str] = None

    # State summary (for quick browsing)
    summary: Optional[str] = None

    # Recovery information
    recovery_point: Optional[str] = None  # Recovery point identifier


@dataclass
class AgentState:
    """Complete Agent state"""
    # Conversation history
    conversation_history: list[Message]

    # Tool call results
    tool_results: list[ToolResult]

    # Agent memory
    memory: AgentMemory

    # Execution context
    context: dict

    # Intermediate reasoning state
    reasoning_state: Optional[dict] = None

    # Custom metadata
    metadata: dict = field(default_factory=dict)
```
## State Storage Solutions

### Redis Storage

```python
import redis.asyncio as redis
import pickle

class RedisStateStore:
    """Redis-based state storage"""

    def __init__(self, redis_url: str, ttl: int = 3600):
        self.client = redis.from_url(redis_url)
        self.ttl = ttl

    async def save(self, agent_id: str, state: AgentState):
        """Save Agent state"""
        key = f"agent:state:{agent_id}"
        serialized = pickle.dumps(state)

        await self.client.setex(
            name=key,
            time=self.ttl,
            value=serialized,
        )

        # Save state index
        await self.client.zadd(
            f"agent:checkpoints:{agent_id",
            {state.checkpoint_id: state.step_count},
        )

    async def load(self, agent_id: str) -> Optional[AgentState]:
        """Load Agent state"""
        key = f"agent:state:{agent_id}"
        data = await self.client.get(key)

        if data is None:
            return None

        return pickle.loads(data)

    async def save_checkpoint(
        self,
        agent_id: str,
        checkpoint: Checkpoint,
    ):
        """Save checkpoint"""
        key = f"agent:checkpoint:{checkpoint.id}"
        serialized = pickle.dumps(checkpoint)

        await self.client.setex(
            name=key,
            time=86400 * 7,  # Retain for 7 days
            value=serialized,
        )

    async def load_checkpoint(
        self,
        checkpoint_id: str,
    ) -> Optional[Checkpoint]:
        """Load checkpoint"""
        key = f"agent:checkpoint:{checkpoint_id}"
        data = await self.client.get(key)

        if data is None:
            return None

        return pickle.loads(data)
```

### PostgreSQL Storage

```python
from sqlalchemy import Column, String, DateTime, LargeBinary, Integer
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class AgentStateModel(Base):
    """Agent state database model"""
    __tablename__ = "agent_states"

    agent_id = Column(String, primary_key=True)
    state_data = Column(LargeBinary, nullable=False)
    step_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    metadata_json = Column(String, default="{}")


class CheckpointModel(Base):
    """Checkpoint database model"""
    __tablename__ = "agent_checkpoints"

    id = Column(String, primary_key=True)
    agent_id = Column(String, index=True)
    state_data = Column(LargeBinary, nullable=False)
    parent_checkpoint_id = Column(String, nullable=True)
    step_count = Column(Integer)
    summary = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class PostgreSQLStateStore:
    """PostgreSQL-based state storage"""

    def __init__(self, database_url: str):
        self.engine = create_async_engine(database_url)
        self.session_factory = AsyncSession(self.engine)

    async def save(self, agent_id: str, state: AgentState):
        async with self.session_factory() as session:
            serialized = pickle.dumps(state)

            existing = await session.get(AgentStateModel, agent_id)
            if existing:
                existing.state_data = serialized
                existing.step_count = state.step_count
                existing.updated_at = datetime.utcnow()
            else:
                session.add(AgentStateModel(
                    agent_id=agent_id,
                    state_data=serialized,
                    step_count=state.step_count,
                ))

            await session.commit()

    async def load(self, agent_id: str) -> Optional[AgentState]:
        async with self.session_factory() as session:
            model = await session.get(AgentStateModel, agent_id)
            if model is None:
                return None
            return pickle.loads(model.state_data)

    async def list_checkpoints(
        self,
        agent_id: str,
        limit: int = 20,
    ) -> list[Checkpoint]:
        async with self.session_factory() as session:
            result = await session.execute(
                select(CheckpointModel)
                .where(CheckpointModel.agent_id == agent_id)
                .order_by(CheckpointModel.created_at.desc())
                .limit(limit)
            )
            return [
                pickle.loads(row.state_data) for row in result.scalars()
            ]
```

### S3 Object Storage

```python
import boto3
import json

class S3StateStore:
    """S3-based state storage, suitable for large-scale long-term storage"""

    def __init__(self, bucket: str, prefix: str = "agent-states"):
        self.client = boto3.client("s3")
        self.bucket = bucket
        self.prefix = prefix

    async def save(self, agent_id: str, state: AgentState):
        key = f"{self.prefix}/{agent_id}/current/state.pkl"
        serialized = pickle.dumps(state)

        self.client.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=serialized,
            ContentType="application/octet-stream",
            Metadata={
                "agent_id": agent_id,
                "step_count": str(state.step_count),
                "updated_at": datetime.utcnow().isoformat(),
            },
        )

    async def save_checkpoint(
        self,
        agent_id: str,
        checkpoint: Checkpoint,
    ):
        key = f"{self.prefix}/{agent_id}/checkpoints/{checkpoint.id}.pkl"
        serialized = pickle.dumps(checkpoint)

        self.client.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=serialized,
            ContentType="application/octet-stream",
        )

    async def load(self, agent_id: str) -> Optional[AgentState]:
        key = f"{self.prefix}/{agent_id}/current/state.pkl"

        try:
            response = self.client.get_object(
                Bucket=self.bucket,
                Key=key,
            )
            return pickle.loads(response["Body"].read())
        except self.client.exceptions.NoSuchKey:
            return None
```

### Storage Solution Comparison

```
Solution Comparison:

Redis:
  Latency: <1ms
  Capacity: Limited by memory (typically GB-scale)
  Persistence: Optional RDB/AOF
  Best for: Session-level state, high-frequency reads/writes
  Cost: High (memory cost)

PostgreSQL:
  Latency: 1-10ms
  Capacity: TB-scale
  Persistence: Native ACID
  Best for: Structured state, query requirements
  Cost: Moderate

S3/Object Storage:
  Latency: 50-200ms
  Capacity: Unlimited
  Persistence: 11 nines durability
  Best for: Long-term storage, large objects
  Cost: Low

Recommended Combination:
  Hot state  → Redis (current session)
  Warm state → PostgreSQL (recent history)
  Cold state → S3 (long-term archive)
```
## State Replay and Debugging

### Replay Engine

```python
class StateReplayEngine:
    """Agent state replay engine for debugging and analysis"""

    def __init__(self, checkpoint_store: CheckpointStore):
        self.checkpoint_store = checkpoint_store

    async def replay(
        self,
        agent_id: str,
        from_checkpoint: Optional[str] = None,
        to_checkpoint: Optional[str] = None,
    ) -> list[ReplayStep]:
        """Replay the Agent execution process"""
        checkpoints = await self.checkpoint_store.list_checkpoints(
            agent_id,
        )

        if from_checkpoint:
            start_idx = next(
                i for i, c in enumerate(checkpoints)
                if c.id == from_checkpoint
            )
        else:
            start_idx = 0

        if to_checkpoint:
            end_idx = next(
                i for i, c in enumerate(checkpoints)
                if c.id == to_checkpoint
            )
        else:
            end_idx = len(checkpoints) - 1

        replay_steps = []
        for i in range(start_idx, end_idx + 1):
            checkpoint = checkpoints[i]
            state = pickle.loads(checkpoint.state)

            step = ReplayStep(
                checkpoint_id=checkpoint.id,
                step_number=checkpoint.step_count,
                timestamp=checkpoint.created_at,
                state_snapshot=state,
                summary=checkpoint.summary,
                diff=self._compute_diff(
                    checkpoints[i - 1] if i > 0 else None,
                    checkpoint,
                ),
            )
            replay_steps.append(step)

        return replay_steps

    def _compute_diff(
        self,
        prev_checkpoint: Optional[Checkpoint],
        current_checkpoint: Checkpoint,
    ) -> StateDiff:
        """Compute the difference between two checkpoints"""
        if prev_checkpoint is None:
            return StateDiff(
                added_messages=len(
                    pickle.loads(current_checkpoint.state)
                    .conversation_history
                ),
                tool_calls=0,
                state_changes=["initial_state"],
            )

        prev_state = pickle.loads(prev_checkpoint.state)
        curr_state = pickle.loads(current_checkpoint.state)

        return StateDiff(
            added_messages=(
                len(curr_state.conversation_history)
                - len(prev_state.conversation_history)
            ),
            tool_calls=(
                len(curr_state.tool_results)
                - len(prev_state.tool_results)
            ),
            state_changes=self._diff_state_fields(
                prev_state, curr_state
            ),
        )
```

### Debugging Tools

```python
class AgentDebugger:
    """Agent debugging tool"""

    def __init__(self, replay_engine: StateReplayEngine):
        self.replay = replay_engine

    async def inspect_state(
        self,
        agent_id: str,
        checkpoint_id: str,
    ) -> StateInspection:
        """Inspect the state at a specific checkpoint"""
        checkpoint = await self.replay.checkpoint_store.load_checkpoint(
            checkpoint_id,
        )
        state = pickle.loads(checkpoint.state)

        return StateInspection(
            checkpoint_id=checkpoint_id,
            conversation_length=len(state.conversation_history),
            tool_calls_count=len(state.tool_results),
            memory_size=state.memory.size(),
            token_usage=self._estimate_tokens(state),
            messages_preview=state.conversation_history[-5:],
        )

    async def find_anomaly(
        self,
        agent_id: str,
    ) -> list[Anomaly]:
        """Detect execution anomalies"""
        checkpoints = await self.replay.replay(agent_id)
        anomalies = []

        for i, step in enumerate(checkpoints):
            # Detect duplicate tool calls
            if i > 0:
                prev = checkpoints[i - 1]
                if (step.state_snapshot.tool_results ==
                    prev.state_snapshot.tool_results):
                    anomalies.append(Anomaly(
                        type="duplicate_tool_call",
                        checkpoint_id=step.checkpoint_id,
                        description="Tool call results unchanged",
                    ))

            # Detect abnormally long conversations
            if step.state_snapshot.conversation_length > 100:
                anomalies.append(Anomaly(
                    type="long_conversation",
                    checkpoint_id=step.checkpoint_id,
                    description=f"Abnormal conversation length: {step.state_snapshot.conversation_length}",
                ))

        return anomalies
```

## Conversation History Compression

### Compression Strategies

```python
from abc import ABC, abstractmethod

class HistoryCompressor(ABC):
    """Base class for conversation history compressors"""

    @abstractmethod
    async def compress(
        self,
        messages: list[Message],
        target_length: int,
    ) -> list[Message]:
        pass


class SummaryCompressor(HistoryCompressor):
    """Summary compressor - uses an LLM to generate a summary in place of old messages"""

    def __init__(self, llm_client):
        self.llm = llm_client

    async def compress(
        self,
        messages: list[Message],
        target_length: int,
    ) -> list[Message]:
        if len(messages) <= target_length:
            return messages

        # Retain the most recent messages
        recent_messages = messages[-target_length:]
        old_messages = messages[:-target_length]

        # Generate a summary
        summary_prompt = f"""Please compress the following conversation history into a concise summary,
retaining key information, decisions, and context:

{self._format_messages(old_messages)}

Output format:
- Key decisions: ...
- Important context: ...
- Incomplete tasks: ..."""

        summary_response = await self.llm.chat(
            messages=[{"role": "user", "content": summary_prompt}],
        )

        # Replace old messages with the summary
        return [
            {
                "role": "system",
                "content": f"[Historical Conversation Summary]\n{summary_response.content}",
            },
            *recent_messages,
        ]


class SlidingWindowCompressor(HistoryCompressor):
    """Sliding window compressor - retains the most recent N rounds of conversation"""

    async def compress(
        self,
        messages: list[Message],
        target_length: int,
    ) -> list[Message]:
        return messages[-target_length:]


class ImportanceBasedCompressor(HistoryCompressor):
    """Importance-based compressor - retains high-importance messages"""

    def __init__(self, importance_scorer):
        self.scorer = importance_scorer

    async def compress(
        self,
        messages: list[Message],
        target_length: int,
    ) -> list[Message]:
        if len(messages) <= target_length:
            return messages

        # Score each message
        scored_messages = []
        for msg in messages:
            score = await self.scorer.score(msg)
            scored_messages.append((score, msg))

        # Sort by importance
        scored_messages.sort(key=lambda x: x[0], reverse=True)

        # Retain the most important messages
        important_messages = [
            msg for _, msg in scored_messages[:target_length]
        ]

        # Arrange in original order
        important_messages.sort(
            key=lambda m: messages.index(m)
        )

        return important_messages
```
## Long-Term Memory Layering

### Three-Layer Memory Architecture

```python
class AgentMemory:
    """Hierarchical Agent memory system"""

    def __init__(
        self,
        short_term_store: StateStore,
        long_term_store: VectorStore,
        episodic_store: DatabaseStore,
    ):
        self.short_term = ShortTermMemory(short_term_store)
        self.long_term = LongTermMemory(long_term_store)
        self.episodic = EpisodicMemory(episodic_store)

    async def update(self, conversation: list[Message]):
        """Update all memory layers"""
        # Short-term memory: update current session context
        await self.short_term.update(conversation)

        # Long-term memory: extract important information and store in vector database
        important_info = await self._extract_important_info(conversation)
        for info in important_info:
            await self.long_term.store(info)

        # Episodic memory: record complete interaction events
        await self.episodic.record_episode(conversation)

    async def recall(
        self,
        query: str,
        context: dict,
    ) -> MemoryRecallResult:
        """Recall relevant information from all memory layers"""
        # Short-term memory: recent conversation context
        recent = await self.short_term.get_recent(limit=10)

        # Long-term memory: semantically relevant historical knowledge
        relevant = await self.long_term.search(query, top_k=5)

        # Episodic memory: similar historical scenarios
        similar_episodes = await self.episodic.find_similar(
            query=query,
            context=context,
            top_k=3,
        )

        return MemoryRecallResult(
            short_term=recent,
            long_term=relevant,
            episodic=similar_episodes,
        )


class ShortTermMemory:
    """Short-term memory - current session context"""

    def __init__(self, store: StateStore):
        self.store = store
        self.ttl = 3600  # 1-hour TTL

    async def update(self, conversation: list[Message]):
        await self.store.save("short_term", {
            "messages": conversation,
            "updated_at": datetime.utcnow(),
        })

    async def get_recent(self, limit: int) -> list[Message]:
        data = await self.store.load("short_term")
        if data is None:
            return []
        return data["messages"][-limit:]


class LongTermMemory:
    """Long-term memory - vectorized persistent knowledge"""

    def __init__(self, vector_store: VectorStore):
        self.vector_store = vector_store

    async def store(self, knowledge: KnowledgeUnit):
        embedding = await self._embed(knowledge.text)
        await self.vector_store.upsert(
            id=knowledge.id,
            vector=embedding,
            metadata={
                "text": knowledge.text,
                "source": knowledge.source,
                "importance": knowledge.importance,
                "created_at": datetime.utcnow().isoformat(),
            },
        )

    async def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[KnowledgeUnit]:
        embedding = await self._embed(query)
        results = await self.vector_store.query(
            vector=embedding,
            top_k=top_k,
        )
        return [
            KnowledgeUnit(
                id=r.id,
                text=r.metadata["text"],
                score=r.score,
            )
            for r in results
        ]


class EpisodicMemory:
    """Episodic memory - complete interaction event records"""

    def __init__(self, db: DatabaseStore):
        self.db = db

    async def record_episode(self, conversation: list[Message]):
        episode = Episode(
            id=str(uuid.uuid4()),
            conversation=conversation,
            summary=await self._generate_summary(conversation),
            timestamp=datetime.utcnow(),
            metadata={
                "turn_count": len(conversation),
                "tool_calls": self._count_tool_calls(conversation),
            },
        )
        await self.db.insert("episodes", episode)

    async def find_similar(
        self,
        query: str,
        context: dict,
        top_k: int = 3,
    ) -> list[Episode]:
        # Semantic search based on summaries
        results = await self.db.vector_search(
            collection="episodes",
            query=query,
            filters=context,
            top_k=top_k,
        )
        return results
```

---

*Agent state management is the foundational infrastructure for building reliable Agent systems, and the layered memory architecture enables Agents to continuously learn and accumulate experience.*
