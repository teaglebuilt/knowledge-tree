---
title: LlamaIndex Data Agent In-Depth Guide
description: 'Comprehensive breakdown of LlamaIndex core architecture and Data Agents, covering Vector Store Index, Knowledge Graph Index, RAG Pipeline orchestration, Tool abstraction, and K8s production deployment'
summary: 'Comprehensive breakdown of LlamaIndex core architecture and Data Agents'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- llamaindex
- rag
- vector-store
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
- What is a LlamaIndex Data Agent
- How to use LlamaIndex Data Agents
- LlamaIndex RAG Pipeline
trigger_keywords:
- llamaindex
- rag
- vector-store-index
- knowledge-graph
- data-agent
prerequisites:
- llm-basics
- python-basics
- kubectl-basics
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/02-llamaindex-data-agent.md
---
> **Production Environment Safety Notice**
>
> This document contains operational commands that can be executed directly. Before executing, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have validated in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state, but is generally reversible), 🟢 Low risk/read-only (information gathering, no side effects).


# LlamaIndex Data Agent In-Depth Guide

## 1. LlamaIndex Core Architecture

### 1.1 Design Positioning

LlamaIndex (formerly GPT Index) focuses on **data connection and indexing**. Its core philosophy is to transform private data into a knowledge base that LLMs can query. Unlike LangChain's general-purpose orchestration positioning, LlamaIndex's strengths lie in:

- **Ingestion Pipeline**: Load documents from 160+ data sources
- **Index Abstraction**: Multiple index structures adapted to different query patterns
- **Query Engine**: Exposes indexes as a natural language query interface
- **Data Agent**: Builds tool-calling Agents on top of indexes

```
┌─────────────────────────────────────────────────────┐
│                  LlamaIndex Architecture             │
│                                                     │
│  ┌───────────┐    ┌──────────┐    ┌──────────────┐  │
│  │ Data      │    │ Index    │    │ Query        │  │
│  │ Connectors│───→│ Builder  │───→│ Engine       │  │
│  └───────────┘    └──────────┘    └──────┬───────┘  │
│       │                                  │          │
│  ┌────┴────┐                        ┌────┴─────┐    │
│  │ Loader  │                        │  Agent   │    │
│  │ (160+)  │                        │ (Tool)   │    │
│  └─────────┘                        └──────────┘    │
│                                                     │
│  ┌─────────────────────────────────────────────┐    │
│  │         Storage Context Layer               │    │
│  │  ┌──────────┐ ┌──────────┐ ┌─────────────┐  │    │
│  │  │ Docstore│ │ Index    │ │ Vector      │  │    │
│  │  │         │ │ Store    │ │ Store       │  │    │
│  │  └──────────┘ └──────────┘ └─────────────┘  │    │
│  └─────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────┘
```

### 1.2 Data Ingestion Pipeline

```python
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
    Settings,
    StorageContext,
)
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding

# Global configuration
Settings.llm = OpenAI(model="gpt-4o", temperature=0)
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
Settings.chunk_size = 512
Settings.chunk_overlap = 64

# Load documents from directory
documents = SimpleDirectoryReader(
    input_dir="./k8s-docs",
    recursive=True,
    required_exts=[".md", ".txt", ".pdf"],
).load_data()

# Custom Reader
from llama_index.core.readers.base import BaseReader

class K8sEventReader(BaseReader):
    """Load data from Kubernetes Event logs."""

    def load_data(self, namespace: str = "default", **kwargs):
        import subprocess
        result = subprocess.run(
            ["kubectl", "get", "events", "-n", namespace, "-o", "json"],
            capture_output=True, text=True
        )
        events = json.loads(result.stdout)["items"]
        documents = []
        for event in events:
            text = (
                f"Type: {event['type']}\n"
                f"Reason: {event['reason']}\n"
                f"Message: {event['message']}\n"
                f"Object: {event['involvedObject']['kind']}/"
                f"{event['involvedObject']['name']}"
            )
            documents.append(Document(text=text, metadata={
                "namespace": namespace,
                "timestamp": event.get("lastTimestamp", ""),
                "type": event["type"],
            }))
        return documents
```

### 1.3 Ingestion Pipeline (Production-Grade)

```python
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import (
    TitleExtractor,
    QuestionsAnsweredExtractor,
    SummaryExtractor,
)
from llama_index.core.ingestion.cache import IngestionCache

# Production-grade ingestion pipeline
pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=512, chunk_overlap=64),
        TitleExtractor(llm=Settings.llm, nodes=5),
        QuestionsAnsweredExtractor(llm=Settings.llm, questions=3),
        SummaryExtractor(llm=Settings.llm, summaries=["self"]),
        Settings.embed_model,
    ],
    # Cache to avoid reprocessing
    cache=IngestionCache(
        collection="k8s_docs",
        persist_dir="./cache"
    ),
    vector_store=vector_store,  # Write directly to the vector database
)

# Execute ingestion
nodes = pipeline.run(documents=documents)

# Incremental ingestion (only process new documents)
from llama_index.core.ingestion import IngestionPipeline
pipeline.run(
    documents=new_documents,
    in_place=True,
    show_progress=True,
)
```

---

## 2. Index Types Explained

### 2.1 Vector Store Index

The most commonly used index type, based on vector similarity retrieval:

```python
from llama_index.core import VectorStoreIndex, StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
import qdrant_client

# Qdrant vector store
client = qdrant_client.QdrantClient(host="qdrant", port=6333)
vector_store = QdrantVectorStore(
    client=client,
    collection_name="k8s_knowledge",
)

# Build index
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex(
    nodes=nodes,
    storage_context=storage_context,
    show_progress=True,
)

# Query
query_engine = index.as_query_engine(
    similarity_top_k=5,
    response_mode="compact",  # Compact mode reduces tokens
)
response = query_engine.query("What are the common causes of Pod OOMKilled?")
print(response.source_nodes)  # View the matched document fragments
```

**Vector Store Backend Comparison:**

| Backend | Distributed | Hybrid Search | Use Case |
|---------|-------------|---------------|----------|
| Qdrant | Yes | Yes | Recommended for production |
| Chroma | No | Yes | Development and testing |
| Pinecone | Yes | Yes | Fully managed SaaS |
| Weaviate | Yes | Yes | Requires BM25 hybrid |
| Milvus | Yes | Yes | Large-scale vectors |
| pgvector | Integrated with PG | No | Existing PostgreSQL |

### 2.2 Knowledge Graph Index

Builds an entity-relationship graph, suitable for structured knowledge queries:

```python
from llama_index.core import KnowledgeGraphIndex
from llama_index.core.storage.storage_context import StorageContext
from llama_index.graph_stores.neo4j import Neo4jGraphStore

# Neo4j graph store
graph_store = Neo4jGraphStore(
    url="bolt://neo4j:7687",
    username="neo4j",
    password="password",
    database="k8s_graph",
)

storage_context = StorageContext.from_defaults(graph_store=graph_store)

# Build knowledge graph index (automatically extracts entities and relationships)
kg_index = KnowledgeGraphIndex(
    nodes=nodes,
    storage_context=storage_context,
    max_triplets_per_chunk=5,
    include_embeddings=True,  # Also generate embeddings for hybrid queries
)

# Query the graph
kg_query_engine = kg_index.as_query_engine(
    response_mode="tree_summarize",
    verbose=True,
)
response = kg_query_engine.query("Which Deployments depend on Redis?")
```

### 2.3 Summary Index

Suitable for document summarization and global overview queries:

```python
from llama_index.core import SummaryIndex

summary_index = SummaryIndex(nodes=nodes)
summary_engine = summary_index.as_query_engine(
    response_mode="tree_summarize",  # Recursive summarization
)
response = summary_engine.query("Summarize the core points of this K8s operations manual")
```

### 2.4 Composite Index Strategy

```python
from llama_index.core import ComposableGraph
from llama_index.core.indices.keyword_table import SimpleKeywordTableIndex

# Combine multiple index types
vector_index = VectorStoreIndex(nodes, storage_context=ctx)
keyword_index = SimpleKeywordTableIndex(nodes, storage_context=ctx)

# Build composite graph
graph = ComposableGraph.from_indices(
    SimpleKeywordTableIndex,
    children_indices=[vector_index, keyword_index],
    index_summaries=[
        "Vector semantic retrieval, suitable for natural language Q&A",
        "Exact keyword matching, suitable for technical terminology queries"
    ],
)

# Automatically route to the appropriate sub-index
query_engine = graph.as_query_engine(
    query_configs=[
        {"index_struct_type": "keyword_table", "query_mode": "simple"},
        {"index_struct_type": "simple_dict", "query_mode": "default"},
    ],
)
```

---
## 3. Data Agent

### 3.1 OpenAI Function Agent

Building an Agent using OpenAI function calling capabilities:

```python
from llama_index.core.agent import OpenAIAgent
from llama_index.core.tools import QueryEngineTool, ToolMetadata

# Wrap query engines as tools
tools = [
    QueryEngineTool(
        query_engine=kg_query_engine,
        metadata=ToolMetadata(
            name="k8s_knowledge_base",
            description=(
                "Kubernetes knowledge base containing documentation, best practices,"
                " and troubleshooting guides for resources such as Pod, Service, and Deployment."
                " Suitable for answering K8s-related questions."
            ),
        ),
    ),
    QueryEngineTool(
        query_engine=log_query_engine,
        metadata=ToolMetadata(
            name="k8s_event_log",
            description=(
                "Kubernetes cluster event log query tool."
                " Query real-time events such as Pod scheduling failures, container crashes, and insufficient resources."
            ),
        ),
    ),
]

# Create a Function Agent
agent = OpenAIAgent.from_tools(
    tools=tools,
    llm=OpenAI(model="gpt-4o"),
    verbose=True,
    system_prompt=(
        "You are a KuDig K8s operations expert."
        " Prefer querying the knowledge base for documentation; use the event log to check real-time status."
        " Answers should include specific commands and cite sources."
    ),
)

# Interactive chat
response = agent.chat("The nginx Pod in the default namespace keeps restarting. Help me troubleshoot.")
print(response)

# Streaming output
stream_response = agent.stream_chat("Analyze cluster resource usage")
for token in stream_response.response_gen:
    print(token, end="", flush=True)
```

### 3.2 ReAct Agent

An Agent based on the ReAct reasoning paradigm:

```python
from llama_index.core.agent import ReActAgent
from llama_index.core.tools import FunctionTool

# Custom function tools
def query_pod_status(namespace: str, pod_name: str) -> str:
    """Query the status details of the specified Pod."""
    import subprocess
    result = subprocess.run(
        ["kubectl", "get", "pod", pod_name, "-n", namespace, "-o", "yaml"],
        capture_output=True, text=True, timeout=30
    )
    return result.stdout

def describe_node(node_name: str) -> str:
    """View resource allocation and health status of a node."""
    import subprocess
    result = subprocess.run(
        ["kubectl", "describe", "node", node_name],
        capture_output=True, text=True, timeout=30
    )
    return result.stdout

# Wrap as LlamaIndex tools
tools = [
    FunctionTool.from_defaults(fn=query_pod_status),
    FunctionTool.from_defaults(fn=describe_node),
    QueryEngineTool(
        query_engine=knowledge_engine,
        metadata=ToolMetadata(
            name="knowledge",
            description="K8s knowledge base for querying best practices and troubleshooting guides"
        ),
    ),
]

# Create a ReAct Agent
react_agent = ReActAgent.from_tools(
    tools=tools,
    llm=OpenAI(model="gpt-4o"),
    verbose=True,
    max_iterations=10,  # Maximum number of reasoning steps
)

response = react_agent.chat("Check the resource usage of node-1. Are any Pods being evicted?")
```

### 3.3 Multi-Document Agent

A multi-document Agent where each document has its own independent sub-Agent:

```python
from llama_index.core.agent import FnAgentWorker
from llama_index.core import SummaryIndex

# Create a sub-Agent for each document
doc_agents = []
for doc_path in doc_files:
    docs = SimpleDirectoryReader(input_files=[doc_path]).load_data()
    index = VectorStoreIndex.from_documents(docs)

    doc_agent = OpenAIAgent.from_tools(
        index.as_query_engine().as_tools(
            tool_metadata=ToolMetadata(
                name=f"doc_{Path(doc_path).stem}",
                description=f"Query document {Path(doc_path).name}"
            )
        ),
        system_prompt=f"You are responsible for answering questions about {Path(doc_path).name}.",
    )
    doc_agents.append(doc_agent)

# Create a top-level Agent to manage multiple sub-Agents
top_agent = FnAgentWorker(
    agents=doc_agents,
    llm=OpenAI(model="gpt-4o"),
).as_agent()
```

---

## 4. Advanced RAG Pipeline Features

### 4.1 Hybrid Search

```python
from llama_index.core.vector_stores import (
    VectorStoreQuery,
    MetadataFilters,
    ExactMatchFilter,
)
from llama_index.core.retrievers import VectorIndexRetriever

# Vector retrieval + metadata filtering
retriever = VectorIndexRetriever(
    index=index,
    similarity_top_k=10,
    filters=MetadataFilters(
        filters=[
            ExactMatchFilter(key="namespace", value="production"),
            ExactMatchFilter(key="severity", value="critical"),
        ]
    ),
)

# Hybrid retrieval (vector + BM25)
from llama_index.core.retrievers import QueryFusionRetriever

hybrid_retriever = QueryFusionRetriever(
    retrievers=[vector_retriever, bm25_retriever],
    similarity_top_k=5,
    num_queries=4,  # Generate multiple query variants
    mode="reciprocal_rerank",  # RRF fusion
)
```

### 4.2 Node Post-processing

```python
from llama_index.core.postprocessor import (
    SimilarityPostprocessor,
    KeywordNodePostprocessor,
    SentenceEmbeddingPostprocessor,
    MetadataReplacementPostProcessor,
)

query_engine = index.as_query_engine(
    node_postprocessors=[
        # Filter out low-similarity nodes
        SimilarityPostprocessor(similarity_cutoff=0.7),
        # Keyword filtering
        KeywordNodePostprocessor(required_keywords=["OOM", "memory"]),
        # Replace chunk with original text
        MetadataReplacementPostProcessor(target_metadata_key="window"),
        # Embedding similarity filtering
        SentenceEmbeddingPostprocessor(embedding_cutoff=0.75),
    ],
)
```

### 4.3 Response Synthesis Strategies

```python
from llama_index.core.response_synthesizers import (
    ResponseMode,
    get_response_synthesizer,
)

# Different response modes
strategies = {
    # Simply concatenate context and call LLM once
    "compact": ResponseMode.COMPACT,
    # Recursive summarization (suitable for long documents)
    "tree_summarize": ResponseMode.TREE_SUMMARIZE,
    # Generate per node, then aggregate at the end
    "accumulate": ResponseMode.ACCUMULATE,
    # Compact + iterative refine
    "compact_accumulate": ResponseMode.COMPACT_ACCUMULATE,
}

# Refine mode: progressively refine the answer
refine_synthesizer = get_response_synthesizer(
    response_mode=ResponseMode.REFINE,
    verbose=True,
)
```

### 4.4 Evaluation Framework

```python
from llama_index.core.evaluation import (
    FaithfulnessEvaluator,
    RelevancyEvaluator,
    CorrectnessEvaluator,
    BatchEvalRunner,
)

# Faithfulness evaluation (whether the answer is grounded in context)
faithfulness = FaithfulnessEvaluator(llm=OpenAI(model="gpt-4o-mini"))

# Relevancy evaluation (whether the answer addresses the question)
relevancy = RelevancyEvaluator(llm=OpenAI(model="gpt-4o-mini"))

# Correctness evaluation (comparison with reference answers)
correctness = CorrectnessEvaluator(llm=OpenAI(model="gpt-4o-mini"))

# Batch evaluation
runner = BatchEvalRunner(
    evaluators={
        "faithfulness": faithfulness,
        "relevancy": relevancy,
    },
    workers=8,
)
eval_results = await runner.aevaluate_queries(
    query_engine=query_engine,
    queries=test_queries,
    reference_answers=reference_answers,
)
```

---
## 5. Comparison and Selection: LlamaIndex vs LangChain

| Dimension | LlamaIndex | LangChain |
|------|-----------|-----------|
| Core Focus | Data indexing and RAG | General-purpose LLM orchestration |
| Data Connectivity | 160+ native connectors | Requires third-party integrations |
| Index Types | Vector/KG/Summary/Tree | No native index abstraction |
| Agent Capabilities | OpenAI/ReAct Agent | Richer (multi-framework) |
| State Management | Basic | LangGraph is powerful |
| Learning Curve | Medium | Medium-low |
| Production Maturity | High | High |

**Selection Recommendations:**
- Data-intensive RAG applications → LlamaIndex
- Complex Agent orchestration → LangChain + LangGraph
- Mixed usage → LlamaIndex for the data layer, LangChain for the orchestration layer

```python
# Example of hybrid usage
from llama_index.core import VectorStoreIndex
from langchain.agents import AgentExecutor, create_openai_functions_agent

# LlamaIndex provides data tools
llama_index = VectorStoreIndex.from_documents(docs)
query_engine = llama_index.as_query_engine()
llama_tool = query_engine.as_tool("k8s_docs", "Query K8s documentation")

# LangChain handles Agent orchestration
agent = create_openai_functions_agent(llm, [llama_tool, other_tools])
executor = AgentExecutor(agent=agent, tools=[llama_tool, other_tools])
```

---

## 6. K8s Deployment

### 6.1 Dockerization

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/

# Health check
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
    CMD curl -f http://localhost:8000/healthz || exit 1

EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### 6.2 K8s Resource Configuration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: llamaindex-agent
  namespace: ai-agents
spec:
  replicas: 2
  selector:
    matchLabels:
      app: llamaindex-agent
  template:
    metadata:
      labels:
        app: llamaindex-agent
    spec:
      serviceAccountName: llamaindex-agent
      containers:
        - name: agent
          image: registry.example.com/llamaindex-agent:1.0.0
          resources:
            requests:
              cpu: "500m"
              memory: "1Gi"
            limits:
              cpu: "2000m"
              memory: "4Gi"
          env:
            - name: OPENAI_API_KEY
              valueFrom:
                secretKeyRef:
                  name: llm-secrets
                  key: openai-api-key
            - name: QDRANT_URL
              value: "http://qdrant:6333"
            - name: NEO4J_URL
              value: "bolt://neo4j:7687"
          ports:
            - containerPort: 8000
          livenessProbe:
            httpGet:
              path: /healthz
              port: 8000
            initialDelaySeconds: 15
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /readyz
              port: 8000
            initialDelaySeconds: 5
            periodSeconds: 5
```

### 6.3 RBAC Configuration

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: llamaindex-agent
  namespace: ai-agents
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: k8s-reader
  namespace: default
rules:
  - apiGroups: [""]
    resources: ["pods", "services", "events", "nodes"]
    verbs: ["get", "list", "watch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: llamaindex-reader
  namespace: default
subjects:
  - kind: ServiceAccount
    name: llamaindex-agent
    namespace: ai-agents
roleRef:
  kind: Role
  name: k8s-reader
  apiGroup: rbac.authorization.k8s.io
```

---

## Related

- [[domain-14-ai-ml-infra/03-agent-runtime/01-langchain-langgraph-deep-dive|LangChain/LangGraph Deep Dive Guide]]
- [[domain-14-ai-ml-infra/03-agent-runtime/07-agent-framework-selection-guide|Agent Framework Selection Decision Tree]]

## See Also

- [[domain-14-ai-ml-infra/03-agent-runtime/03-crewai-multi-agent-framework|CrewAI Multi-Agent Framework]]
- [[domain-14-ai-ml-infra/03-agent-runtime/05-dify-agent-platform|Dify Agent Platform]]


<!-- risk-assessed -->
