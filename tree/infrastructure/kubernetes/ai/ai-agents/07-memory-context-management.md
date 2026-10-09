---
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/07-memory-context-management.md
---
title: Memory Management and Context Window Engineering (domain-14-ai-ml-infra)
description: 'title: Memory Management and Context Window Engineering'
summary: 'title: Memory Management and Context Window Engineering'
category: general
tags:
- ai
- ai-agent
- redis
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
- all engineers
estimated_read_time: 25min
intent_queries:
- What is memory management and contextual window engineering
- How to do memory management and contextual window engineering
- Kubernetes 14 ai ml infra best practices
trigger_keywords:
- Memory Management and Contextual Window Engineering
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- redis-basics
authors:
- name: Dillan Teagle
  role: contributor

---

> **Production Environment Security Tips**
>
> This document contains executable operational commands. Execute only after confirming: the target cluster and namespace are correct; you have sufficient RBAC permissions; and the commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High risk (may cause data loss or service disruption), 🟡 Medium risk (modifies cluster state but usually rollbackable), 🟢 Low risk/readonly (information gathering, no side effects).




title: Memory Management and Contextual Window Engineering
description: '# Memory Management and Contextual Window Engineering'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- redis
- postgresql
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Architects
- SRE
estimated_read_time: 5min
intent_queries:
- What is memory management and contextual window engineering
- How to do memory management and contextual window engineering
trigger_keywords:
- Memory Management and Contextual Window Engineering
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

# Memory Management and Contextual Window Engineering

> **Document Type**: Core Technology Topic | **Last Updated**: 2026-03 | **Keywords**: memory management, contextual window, short-term memory, long-term memory, narrative memory, semantic memory, contextual compression, token management, session memory, vector memory

---

## Overview

Memory is a core capability for Agents to achieve cross-session continuity, avoid repetitive user inquiries, and accumulate experience. Context window management determines how much information an Agent can effectively utilize in a single conversation. This article comprehensively covers the four types of memories (perception, working, plot, semantic) used by Agents, context compression techniques, long-term memory storage and retrieval architectures, and the implementation of memory systems in production environments.

---

## 1. Agent Memory Classification System

```
Agent 记忆体系
│
├── 感知记忆（Sensory Memory）
│   - 最近的原始输入（当前对话轮次）
│   - 极短暂，处理后丢弃
│
├── 工作记忆（Working Memory）
│   - 当前任务的活跃上下文（LLM 上下文窗口）
│   - 工具调用中间结果
│   - 存储形式: LLM 的 messages 列表
│   - 容量: 受 Token 限制（4K~2M tokens）
│
├── 情节记忆（Episodic Memory）
│   - 过去的对话历史和操作记录
│   - "我上次怎么解决这个问题的"
│   - 存储形式: 数据库 + 向量索引
│   - 检索方式: 基于相似度的语义检索
│
└── 语义记忆（Semantic Memory）
    - 结构化的领域知识和事实
    - "K8s 的 Pod 有哪些状态"
    - 存储形式: 知识库（RAG）/ Fine-tuning
    - 来源: kudig-database 等知识库
```

---

## 2. Working Memory: Context Window Management

## 2.1 Token Budget Planning

```python
# Context windows and recommendations for each model
CONTEXT_BUDGETS = {
    "gpt-4o": {
        "max_tokens": 128_000,
        "output_reserve": 4_096,  # 为输出预留
        "system_reserve": 2_000,  # 系统提示
        "tool_reserve": 3_000,    # 工具定义
        "usable_for_history": 118_904,
    },
    "claude-3-5-sonnet": {
        "max_tokens": 200_000,
        "output_reserve": 8_192,
        "system_reserve": 2_000,
        "tool_reserve": 3_000,
        "usable_for_history": 186_808,
    },
    "gpt-4o-mini": {
        "max_tokens": 128_000,
        "output_reserve": 4_096,
        "system_reserve": 1_000,
        "tool_reserve": 2_000,
        "usable_for_history": 120_904,
    },
}

class TokenBudgetManager:
    def __init__(self, model: str = "gpt-4o"):
        self.budget = CONTEXT_BUDGETS.get(model, CONTEXT_BUDGETS["gpt-4o"])
        self.encoding = tiktoken.encoding_for_model(model)
    
    def count_tokens(self, text: str) -> int:
        return len(self.encoding.encode(text))
    
    def count_messages_tokens(self, messages: list[dict]) -> int:
        total = 0
        for msg in messages:
            # Each message has a fixed overhead of 4 tokens
            total += 4
            total += self.count_tokens(str(msg.get("content", "")))
            if "tool_calls" in msg:
                total += self.count_tokens(str(msg["tool_calls"]))
        return total + 2  # 最终 2 token 开销
    
    def available_tokens_for_history(
        self, 
        system_prompt: str, 
        tool_definitions: list
    ) -> int:
        used = (
            self.count_tokens(system_prompt) +
            self.count_tokens(str(tool_definitions)) +
            self.budget["output_reserve"]
        )
        return self.budget["max_tokens"] - used
```

## 2.2 Smart Context Truncation

```python
from enum import Enum

class TrimStrategy(Enum):
    SLIDING_WINDOW = "sliding_window"      # 保留最近 N 条
    SUMMARY_COMPRESSION = "summary"        # 旧消息压缩为摘要
    IMPORTANCE_BASED = "importance"        # 保留重要消息
    HYBRID = "hybrid"                      # 混合策略

class ContextWindowManager:
    def __init__(
        self,
        model: str = "gpt-4o",
        strategy: TrimStrategy = TrimStrategy.HYBRID,
        summary_llm = None,
    ):
        self.budget_manager = TokenBudgetManager(model)
        self.strategy = strategy
        self.summary_llm = summary_llm
    
    def trim(
        self,
        messages: list[dict],
        system_prompt: str,
        tools: list = None,
    ) -> list[dict]:
        """Trim historical messages to ensure they do not exceed the token limit"""
        
        available = self.budget_manager.available_tokens_for_history(
            system_prompt, tools or []
        )
        
        current_tokens = self.budget_manager.count_messages_tokens(messages)
        
        if current_tokens <= available:
            return messages  # 不需要修剪
        
        if self.strategy == TrimStrategy.SLIDING_WINDOW:
            return self._sliding_window(messages, available)
        elif self.strategy == TrimStrategy.SUMMARY_COMPRESSION:
            return self._summary_compression(messages, available)
        elif self.strategy == TrimStrategy.IMPORTANCE_BASED:
            return self._importance_based(messages, available)
        else:  # HYBRID
            return self._hybrid_trim(messages, available)
    
    def _sliding_window(
        self, messages: list[dict], available_tokens: int
    ) -> list[dict]:
        """Retain recent messages until the token limit is reached, then delete from the oldest"""
        # Always retain system messages
        system_msgs = [m for m in messages if m["role"] == "system"]
        other_msgs = [m for m in messages if m["role"] != "system"]
        
        # Retain the most recent messages until the token limit is reached
        kept = []
        token_count = 0
        
        for msg in reversed(other_msgs):
            msg_tokens = self.budget_manager.count_messages_tokens([msg])
            if token_count + msg_tokens > available_tokens:
                break
            kept.insert(0, msg)
            token_count += msg_tokens
        
        return system_msgs + kept
    
    def _summary_compression(
        self, messages: list[dict], available_tokens: int
    ) -> list[dict]:
        """Compress early conversations into summaries"""
        if not self.summary_llm:
            return self._sliding_window(messages, available_tokens)
        
        system_msgs = [m for m in messages if m["role"] == "system"]
        other_msgs = [m for m in messages if m["role"] != "system"]
        
        # Retain the most recent 1/3 of messages
        recent_count = max(4, len(other_msgs) // 3)
        recent_msgs = other_msgs[-recent_count:]
        old_msgs = other_msgs[:-recent_count]
        
        if not old_msgs:
            return messages
        
        # Compress old messages
        summary_prompt = f"""请将以下对话历史压缩为简洁摘要（200字以内），
        保留：关键决策、已执行的操作、发现的问题、重要配置信息：
        
        {self._format_messages_for_summary(old_msgs)}"""
        
        summary = self.summary_llm.invoke(summary_prompt).content
        
        summary_msg = {
            "role": "system",
            "content": f"[历史对话摘要]\n{summary}"
        }
        
        return system_msgs + [summary_msg] + recent_msgs
    
    def _importance_based(
        self, messages: list[dict], available_tokens: int
    ) -> list[dict]:
        """Preserve messages based on importance"""
        system_msgs = [m for m in messages if m["role"] == "system"]
        other_msgs = [m for m in messages if m["role"] != "system"]
        
        # Importance scoring
        scored_msgs = []
        for i, msg in enumerate(other_msgs):
            score = self._importance_score(msg, i, len(other_msgs))
            scored_msgs.append((score, i, msg))
        
        # Sort by importance but maintain sequence
        scored_msgs.sort(key=lambda x: x[0], reverse=True)
        
        kept_indices = set()
        token_count = 0
        
        for score, idx, msg in scored_msgs:
            msg_tokens = self.budget_manager.count_messages_tokens([msg])
            if token_count + msg_tokens <= available_tokens:
                kept_indices.add(idx)
                token_count += msg_tokens
        
        # Return in original order (maintain sequence)
        kept = [msg for i, msg in enumerate(other_msgs) if i in kept_indices]
        return system_msgs + kept
    
    def _importance_score(self, msg: dict, idx: int, total: int) -> float:
        """Calculate message importance scores"""
        score = 0.0
        
        # The most recent messages are more important
        recency = idx / total
        score += recency * 0.4
        
        content = str(msg.get("content", ""))
        
        # Include error messages that are important
        if any(keyword in content.lower() for keyword in 
               ["error", "failed", "exception", "warning", "错误", "失败"]):
            score += 0.3
        
        # Tool call results are important
        if msg.get("role") == "tool":
            score += 0.2
        
        # Messages containing critical Kubernetes resources are important
        if any(keyword in content for keyword in 
               ["kubectl", "yaml", "apiVersion", "namespace", "Pod"]):
            score += 0.1
        
        return min(score, 1.0)
```

---

## 3. Story Recall: Cross-session History

## 3.1 Design for Story Recall Storage

```python
from datetime import datetime, UTC
from dataclasses import dataclass, asdict

@dataclass
class EpisodeRecord:
    """A complete record of a single conversation/action"""
    episode_id: str
    user_id: str
    agent_id: str
    timestamp: str
    summary: str              # 本次对话的摘要（100字以内）
    key_entities: list[str]   # 涉及的关键实体（Pod名、集群名等）
    problem_type: str         # 问题类型（网络/存储/应用）
    outcome: str              # 结果（resolved/escalated/pending）
    actions_taken: list[str]  # 执行的关键操作
    lessons_learned: str      # 经验教训（用于未来检索）
    raw_transcript: str       # 完整对话记录（可选，压缩存储）
    embedding: list[float]    # 向量化后的摘要（用于语义检索）

class EpisodicMemoryStore:
    """Story Recall storage based on PostgreSQL + pgvector"""
    
    def __init__(self, db_url: str, embedding_model):
        self.db_url = db_url
        self.embedding_model = embedding_model
        self._init_db()
    
    def _init_db(self):
        """Initialize database tables"""
        # PostgreSQL with pgvector
        CREATE_TABLE_SQL = """
        CREATE TABLE IF NOT EXISTS episode_memory (
            episode_id VARCHAR PRIMARY KEY,
            user_id VARCHAR NOT NULL,
            agent_id VARCHAR NOT NULL,
            timestamp TIMESTAMPTZ NOT NULL,
            summary TEXT,
            key_entities TEXT[],
            problem_type VARCHAR,
            outcome VARCHAR,
            actions_taken TEXT[],
            lessons_learned TEXT,
            embedding vector(1536),
            created_at TIMESTAMPTZ DEFAULT NOW()
        );
        
        CREATE INDEX IF NOT EXISTS episode_embedding_idx 
        ON episode_memory USING ivfflat (embedding vector_cosine_ops)
        WITH (lists = 100);
        
        CREATE INDEX IF NOT EXISTS episode_user_idx 
        ON episode_memory (user_id, timestamp DESC);
        """
        # Execute table creation
    
    def save_episode(self, episode: EpisodeRecord):
        """Save a conversation record"""
        # Generate embedding
        embedding_text = f"{episode.summary} {episode.lessons_learned}"
        embedding = self.embedding_model.embed_query(embedding_text)
        episode.embedding = embedding
        
        # Insert into database
        INSERT_SQL = """
        INSERT INTO episode_memory 
        (episode_id, user_id, agent_id, timestamp, summary, key_entities,
         problem_type, outcome, actions_taken, lessons_learned, embedding)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11)
        """
        # Execute insertion
    
    def search_relevant_episodes(
        self,
        query: str,
        user_id: str = None,
        limit: int = 5,
        problem_type: str = None,
    ) -> list[EpisodeRecord]:
        """Semantic search related past experiences"""
        query_embedding = self.embedding_model.embed_query(query)
        
        # Filtered vector similarity search
        SEARCH_SQL = """
        SELECT *, 1 - (embedding <=> $1) AS similarity
        FROM episode_memory
        WHERE 1=1
          {user_filter}
          {type_filter}
          AND outcome = 'resolved'  -- 只检索成功解决的案例
        ORDER BY embedding <=> $1
        LIMIT $2
        """
        # Execute query and return results
```

## 3.2 Automatic Generation of Story Recalls

```python
class EpisodeExtractor:
    """Automatically extract structured story recollections from historical dialogues"""
    
    def __init__(self, llm):
        self.llm = llm
    
    def extract_episode(
        self, 
        messages: list[dict],
        outcome: str
    ) -> EpisodeRecord:
        """Extract structured memories from dialogue records"""
        
        transcript = self._format_transcript(messages)
        
        extraction_result = self.llm.invoke(f"""
        请从以下对话记录中提取结构化信息，以 JSON 格式输出：
        
        {transcript}
        
        提取以下字段：
        - summary: 100字以内的对话摘要
        - key_entities: 涉及的关键实体列表（Pod名、Service名、集群名等）
        - problem_type: 问题类型（network/storage/scheduling/application/security/other）
        - actions_taken: 执行的关键操作列表
        - lessons_learned: 经验教训（下次遇到类似问题时的关键提示，50字以内）
        
        输出格式：
        {{
            "summary": "...",
            "key_entities": ["..."],
            "problem_type": "...",
            "actions_taken": ["..."],
            "lessons_learned": "..."
        }}
        """)
        
        data = json.loads(extraction_result.content)
        
        return EpisodeRecord(
            episode_id=generate_id(),
            user_id=extract_user_id(messages),
            agent_id=self.agent_id,
            timestamp=datetime.now(UTC).isoformat(),
            summary=data["summary"],
            key_entities=data["key_entities"],
            problem_type=data["problem_type"],
            outcome=outcome,
            actions_taken=data["actions_taken"],
            lessons_learned=data["lessons_learned"],
            raw_transcript=transcript,
            embedding=[],  # 在 save 时生成
        )
```

---

## 4. Semantic Memory: Integration of Structured Knowledge Base

## 4.1 Semantic Memory vs RAG Relationship

```
语义记忆（Semantic Memory）与 RAG 的区别：

RAG（检索增强生成）:
  - 来源: 外部知识库文档（如 kudig-database）
  - 粒度: 文档块级别
  - 更新: 更新知识库文档
  - 适合: 大量文档型知识

语义记忆（Semantic Memory）:
  - 来源: Agent 自主学习和总结的知识
  - 粒度: 结构化事实、规则、关系
  - 更新: 通过新经验自动更新
  - 适合: 精炼的领域事实和操作规则

实践建议: 两者配合使用
  - RAG 提供背景知识（知识库）
  - 语义记忆存储 Agent 自己总结的经验规则
```

## 4.2 Implementation of Semantic Memory

```python
class SemanticMemoryStore:
    """Agent's Semantic Memory (Structured Knowledge)"""
    
    def __init__(self, vector_store, llm):
        self.vector_store = vector_store
        self.llm = llm
    
    def learn_from_episode(self, episode: EpisodeRecord):
        """Learn from the plot to extract reusable knowledge points"""
        if episode.outcome != "resolved":
            return  # 只从成功案例中学习
        
        knowledge_extraction = self.llm.invoke(f"""
        基于以下成功解决的案例，提取1-3条可复用的知识点：
        
        问题类型: {episode.problem_type}
        摘要: {episode.summary}
        解决步骤: {episode.actions_taken}
        经验教训: {episode.lessons_learned}
        
        提取格式（每条知识点）：
        - 触发条件：什么情况下适用
        - 知识内容：具体的规则/方法/结论
        - 置信度：0-1（基于案例的充分程度）
        """)
        
        # Parse and Store Knowledge Points
        knowledge_points = self._parse_knowledge(knowledge_extraction.content)
        for kp in knowledge_points:
            self.vector_store.add_texts(
                texts=[kp["content"]],
                metadatas=[{
                    "type": "semantic_memory",
                    "problem_type": episode.problem_type,
                    "trigger": kp["trigger"],
                    "confidence": kp["confidence"],
                    "source_episode": episode.episode_id,
                }]
            )
    
    def recall(self, situation: str, limit: int = 3) -> list[str]:
        """Recall relevant knowledge points based on current context"""
        results = self.vector_store.similarity_search(
            situation,
            k=limit,
            filter={"type": "semantic_memory"}
        )
        return [r.page_content for r in results]
```

---

## 5. Integration of Complete Memory System

```python
class AgentMemorySystem:
    """Complete Agent Memory System (Integrating Four Types of Memories)"""
    
    def __init__(
        self,
        model: str = "gpt-4o",
        episodic_store: EpisodicMemoryStore = None,
        semantic_store: SemanticMemoryStore = None,
        rag_retriever = None,
        summary_llm = None,
    ):
        self.working_memory = []  # 当前会话消息列表
        self.context_manager = ContextWindowManager(
            model=model,
            strategy=TrimStrategy.HYBRID,
            summary_llm=summary_llm,
        )
        self.episodic_store = episodic_store
        self.semantic_store = semantic_store
        self.rag_retriever = rag_retriever
        self.episode_extractor = EpisodeExtractor(summary_llm) if summary_llm else None
    
    def add_message(self, message: dict):
        """Add new messages to working memory"""
        self.working_memory.append(message)
    
    def get_context(
        self,
        system_prompt: str,
        tools: list = None,
        current_query: str = "",
    ) -> list[dict]:
        """
        组装完整的上下文：
        工作记忆 + 相关情节记忆 + 相关语义知识 + RAG 检索结果
        """
        # 1. Retrieve Relevant Historical Experiences
        episodic_context = ""
        if self.episodic_store and current_query:
            relevant_episodes = self.episodic_store.search_relevant_episodes(
                current_query, limit=3
            )
            if relevant_episodes:
                episodic_context = "\n[相关历史案例]\n" + "\n".join([
                    f"- {ep.summary}（结论: {ep.lessons_learned}）"
                    for ep in relevant_episodes
                ])
        
        # 2. Retrieve Relevant Semantic Knowledge
        semantic_context = ""
        if self.semantic_store and current_query:
            knowledge_points = self.semantic_store.recall(current_query)
            if knowledge_points:
                semantic_context = "\n[相关知识点]\n" + "\n".join([
                    f"- {kp}" for kp in knowledge_points
                ])
        
        # 3. RAG Retrieval
        rag_context = ""
        if self.rag_retriever and current_query:
            rag_docs = self.rag_retriever.get_relevant_documents(current_query)
            if rag_docs:
                rag_context = "\n[知识库参考]\n" + "\n\n".join([
                    d.page_content for d in rag_docs[:3]
                ])
        
        # 4. Combine Enhanced System Prompt
        enhanced_system = system_prompt
        if episodic_context or semantic_context or rag_context:
            enhanced_system += f"\n\n{episodic_context}{semantic_context}{rag_context}"
        
        # 5. Prune Working Memory (Ensure within Token Limit)
        trimmed_messages = self.context_manager.trim(
            messages=self.working_memory,
            system_prompt=enhanced_system,
            tools=tools,
        )
        
        return [{"role": "system", "content": enhanced_system}] + trimmed_messages
    
    def finalize_session(self, outcome: str = "resolved"):
        """End a session by converting this conversation to plot memory"""
        if self.episodic_store and self.episode_extractor and self.working_memory:
            episode = self.episode_extractor.extract_episode(
                self.working_memory, outcome
            )
            self.episodic_store.save_episode(episode)
            
            # Learn from the plot to update semantic memory
            if self.semantic_store and outcome == "resolved":
                self.semantic_store.learn_from_episode(episode)
        
        # Clear Working Memory (New session starts)
        self.working_memory = []
```

---

## 6. Privacy and Security of Memory Systems

```python
class PrivacyAwareMemorySystem(AgentMemorySystem):
    """Privacy-Preserving Memory System"""
    
    # Detection Regular Expressions for PII
    PII_PATTERNS = {
        "ip_address": r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        "api_key": r'(?i)(api[_-]?key|token|secret)["\s:=]+[a-zA-Z0-9+/=]{20,}',
        "password": r'(?i)(password|passwd|pwd)["\s:=]+\S+',
        "email": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    }
    
    def _sanitize_before_storage(self, text: str) -> str:
        """store data de-identified beforehand"""
        import re
        sanitized = text
        
        for pii_type, pattern in self.PII_PATTERNS.items():
            sanitized = re.sub(pattern, f'[{pii_type.upper()}_REDACTED]', sanitized)
        
        return sanitized
    
    def save_episode(self, episode: EpisodeRecord):
        """de-identify and then store"""
        episode.summary = self._sanitize_before_storage(episode.summary)
        episode.lessons_learned = self._sanitize_before_storage(episode.lessons_learned)
        # Store complete dialogue records without storing sensitive information
        episode.raw_transcript = ""
        super().save_episode(episode)
    
    def user_data_deletion(self, user_id: str):
        """GDPR compliance: right to delete user data"""
        DELETE_SQL = "DELETE FROM episode_memory WHERE user_id = $1"
        # Execute deletion
        
    def get_user_data_export(self, user_id: str) -> list[dict]:
        """GDPR compliance: right to export user data"""
        # Return all plot memories for this user (without embeddings)
        pass
```

---

## 7. Memory System Performance Optimization

## 7.1 Redis Cache Layer

```python
import redis
import json
import hashlib

class CachedMemorySystem:
    """memory system with Redis caching"""
    
    def __init__(self, memory_system: AgentMemorySystem, redis_client: redis.Redis):
        self.memory = memory_system
        self.redis = redis_client
        self.cache_ttl = 3600  # 1小时
    
    def get_context_cached(
        self,
        system_prompt: str,
        current_query: str,
        tools: list = None,
    ) -> list[dict]:
        """assemble cache context results (RAG retrieval results change infrequently)"""
        
        cache_key = hashlib.md5(
            f"{current_query}:{system_prompt[:100]}".encode()
        ).hexdigest()
        
        cached = self.redis.get(f"agent_context:{cache_key}")
        if cached:
            return json.loads(cached)
        
        context = self.memory.get_context(system_prompt, tools, current_query)
        
        # Cache only parts of the context that do not include working memory (retrieval results)
        # Working memory needs to be assembled in real time each time
        
        return context
```

---

## 8. Best Practices and Anti-patterns

## Best Practices

- **hierarchical memory**: short-term use working memory (context window), medium-term use plot memories, long-term use semantic memories
- **retrieve historical selectively**: don't stuff all history into the context; first search for relevant ones before injecting
- **compress summary before truncation**: try summarization compression first rather than directly deleting messages (less information loss)
- **de-identify before storage**: plot memories and semantic memories must have PII and key information removed before storage
- **cold start for plot memories**: new deployed agents lack history; should pre-import typical cases as seed data

## Anti-patterns

- **Infinite Accumulated History**: No context window management, inference quality declines and costs skyrocket with longer dialogues
- **Discard All History**: Each new session resets completely, users need to repeat context descriptions
- **Store Raw Dialogues**: Unredacted raw dialogues may contain passwords, keys, PII, etc., sensitive information
- **No Distinction Between Memory Types**: All information stuffed into system prompts without reasonable layering by type
- **Persistent Plot Memory**: Three years ago's case might be outdated (K8s versions differ greatly), aging mechanisms should be set

---

## Related Documents

| Document | Associated Content |
|------|---------|
| [01 - Agent Basics](./01-ai-agent-fundamentals.md) | The role of context windows in the Agent Loop |
| [04 - RAG Retrieval](./04-rag-knowledge-retrieval.md) | Semantic memory integration with RAG |
| [06 - Multi-Agent Orchestration](./06-multi-agent-orchestration.md) | Architectures for shared memory among multiple agents |
| [11 - Cost Optimization](./11-cost-latency-optimization.md) | Impact of token compression on cost |
| [domain-14-ai-ml-infra/20-vector-database-rag.md](../domain-14-ai-ml-infra/20-vector-database-rag.md) | Selection of vector databases |

---

*This document is original content from the kudig-database project's 02-ai-agents topic.*

---

## Related Obsidian Documents

- 02-ai-agents KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|[[AI Agent Engineering Topic|AI Agent Engineering Topic]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|[[AI Agent Basics and Core Architecture|AI Agent Basics and Core Architecture]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|[[LLM Foundation Model Selection and Evaluation|LLM Foundation Model Selection and Evaluation]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|[[Deep Comparison of Main Agent Frameworks|Deep Comparison of Main Agent Frameworks]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|RAG Retrieval Deep Guide]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Tool Use & Function Calling Design Guidelines]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Multi-Agent Orchestration and Collaboration Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation and Observability Framework]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]
- [[domain-14-ai-ml-infra/02-ai-agents/11-cost-latency-optimization.md|Cost and Latency Optimization Strategies]]

## See Also

- 05-tool-use-function-calling
- 06-multi-agent-orchestration
- 08-agent-evaluation-observability
- 09-production-deployment-guide


<!-- risk-assessed -->
