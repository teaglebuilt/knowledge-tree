---
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/04-rag-knowledge-retrieval.md
---
---title: RAG Retrieval-Augmented Generation In-Depth Guide (domain-14-ai-ml-infra)
description: 'title: RAG Retrieval-Augmented Generation In-Depth Guide'
summary: 'title: RAG Retrieval-Augmented Generation In-Depth Guide'
category: general
tags:
- ai
- ai-agent
- helm
- redis
- postgresql
- hpa
- statefulset
- operator
- cuda
- llm
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 25min
intent_queries:
- What is the RAG Retrieval-Augmented Generation In-Depth Guide
- How to RAG Retrieval-Augmented Generation In-Depth Guide
- Kubernetes 14 ai ml infra best practices
trigger_keywords:
- RAG
- Retrieval-Augmented Generation In-Depth Guide
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- helm-basics
- redis-basics
authors:
- name: Dillan Teagle
  role: contributor

---

> **Production Environment Safety Notice**
>
> This document contains directly executable operational commands. Before executing, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have validated in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state, but generally reversible), 🟢 Low risk / read-only (information gathering, no side effects).




title: RAG Retrieval-Augmented Generation In-Depth Guide
description: '# RAG Retrieval-Augmented Generation In-Depth Guide'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- [[Helm|helm]]
- redis
- postgresql
- hpa
- [[StatefulSet|statefulset]]
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Architects
- SRE
estimated_read_time: 5min
intent_queries:
- What is the RAG Retrieval-Augmented Generation In-Depth Guide
- How to RAG Retrieval-Augmented Generation In-Depth Guide
trigger_keywords:
- RAG
- Retrieval-Augmented Generation In-Depth Guide
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

# RAG Retrieval-Augmented Generation In-Depth Guide

> **Document Type**: Core Technical Topic | **Last Updated**: 2026-03 | **Keywords**: RAG, Retrieval-Augmented Generation, Embedding, Vector Database, Hybrid Retrieval, Re-ranking, Chunking Strategy, Chunking, Weaviate, Milvus, pgvector

---

<!-- chunk: Overview -->## Overview

RAG (Retrieval-Augmented Generation) is a core technology that combines external knowledge bases with LLM generation capabilities, and is the standard solution for addressing LLM knowledge cutoff dates, missing domain knowledge, and hallucination problems. This article covers the full engineering pipeline from data preparation, chunking strategies, Embedding selection, and vector database comparison, to hybrid retrieval, Re-ranking, Advanced RAG, and production optimization.

---

<!-- chunk: 1. RAG Architecture Overview -->## 1. RAG Architecture Overview

## 1.1 Basic RAG Pipeline

```
                    ┌─────────────────────────────────────────┐
                    │         Offline Phase (Index Building)   │
                    │                                          │
                    │  Documents → Preprocessing → Chunking → Embedding → Vector DB  │
                    └─────────────────────────────────────────┘
                                         │ Index
                                         ▼
User Query → Query Embedding → [Vector Similarity Search] → Top-K Candidate Documents
                │                              │
                │                              ▼ Re-ranking
                │                    Re-ranked Relevant Documents
                │                              │
                └──────────────────────────────┘
                                 │
                                 ▼
                         LLM Generates Answer (with retrieved context)
```

## 1.2 RAG Evolution Path

```
Naive RAG
  ↓ Addresses retrieval accuracy issues
Advanced RAG
  - Pre-retrieval: Query rewriting, HyDE hypothetical document expansion
  - Retrieval: Hybrid retrieval, multi-path recall
  - Post-retrieval: Re-ranking, context compression
  ↓ Addresses complex reasoning problems
Modular RAG
  - Routing (selecting different retrieval strategies based on query type)
  - Iterative Retrieval (Iterative RAG)
  - Recursive Retrieval (Recursive RAG)
  ↓ Combined with Agent capabilities
Agentic RAG
  - Agent autonomously decides whether to retrieve and what to retrieve
  - Multi-turn retrieval, self-reflection
  - Tool calling + RAG hybrid
```

---

<!-- chunk: 2. Data Preparation and Chunking Strategies -->## 2. Data Preparation and Chunking Strategies

## 2.1 Document Preprocessing

```python
import re
from pathlib import Path
from typing import Optional

class DocumentPreprocessor:
    """Production-grade document preprocessor"""
    
    def preprocess_markdown(self, content: str, source_path: str) -> dict:
        """Process Markdown documents (optimized for kudig-database)"""
        
        # 1. Extract metadata
        metadata = self._extract_metadata(content, source_path)
        
        # 2. Clean content
        cleaned = self._clean_markdown(content)
        
        # 3. Preserve code block markers (important! code blocks should not be split in the middle)
        code_blocks = self._extract_code_blocks(cleaned)
        
        return {
            "content": cleaned,
            "metadata": metadata,
            "code_blocks": code_blocks,
        }
    
    def _extract_metadata(self, content: str, source_path: str) -> dict:
        """Extract document metadata"""
        path = Path(source_path)
        
        # Extract keywords and other information from Markdown frontmatter
        keywords = []
        keyword_match = re.search(r'\*\*Keywords\*\*[：:]\s*(.+)', content)
        if keyword_match:
            keywords = [k.strip() for k in keyword_match.group(1).split(',')]
        
        return {
            "source": source_path,
            "domain": path.parent.name,
            "filename": path.stem,
            "keywords": keywords,
            "doc_type": self._infer_doc_type(content),
        }
    
    def _clean_markdown(self, content: str) -> str:
        """Clean Markdown formatting"""
        # Remove HTML comments
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        # Normalize blank lines
        content = re.sub(r'\n{3,}', '\n\n', content)
        return content.strip()
```
## 2.2 Chunking Strategies in Detail

Chunking is a critical decision for RAG quality, and different strategies involve different trade-offs:

## Fixed-Size Chunking

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

# General configuration
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # approximately 1000 characters per chunk
    chunk_overlap=200,      # 200-character overlap to ensure context continuity
    separators=[
        "\n<!-- chunk: ",   # split by level-2 headings first -->## ",   # split by level-2 headings first
        "\n#<!-- chunk: ",  # then by level-3 headings -->## ",  # then by level-3 headings
        "\n\n",    # then by paragraph
        "\n",      # then by line
        " ",       # finally by space
        ""
    ],
    length_function=len,
)
```

## Semantic Chunking (Recommended for Technical Documentation)

```python
from llama_index.core.node_parser import SemanticSplitterNodeParser
from llama_index.embeddings.openai import OpenAIEmbedding

# Semantic chunking: determines split points based on semantic similarity
semantic_splitter = SemanticSplitterNodeParser(
    buffer_size=1,                   # compare semantic similarity of adjacent sentences
    breakpoint_percentile_threshold=95,  # split when similarity falls below the 95th percentile
    embed_model=OpenAIEmbedding(model="text-embedding-3-small"),
)

# Outperforms fixed-size chunking for kudig-database technical documentation
nodes = semantic_splitter.get_nodes_from_documents(documents)
```

## Hierarchical Chunking (Parent-Child Chunking)

The strategy best suited for technical documentation: **parent chunks retain context, child chunks ensure precise retrieval**:

```python
from langchain.retrievers import ParentDocumentRetriever
from langchain.storage import InMemoryStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Large chunks (parent): used for LLM context, retains complete semantics
parent_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)

# Small chunks (child): used for vector retrieval, precise matching
child_splitter = RecursiveCharacterTextSplitter(chunk_size=400, chunk_overlap=50)

vectorstore = Chroma(embedding_function=embedding_model)
store = InMemoryStore()  # use Redis or a database in production

retriever = ParentDocumentRetriever(
    vectorstore=vectorstore,
    docstore=store,
    child_splitter=child_splitter,
    parent_splitter=parent_splitter,
)

# During retrieval: child chunk matched → return corresponding parent chunk (with full context)
retriever.add_documents(documents)
relevant_docs = retriever.get_relevant_documents("Reasons for Pod Pending")
```

## 2.3 Chunking Strategy Selection Guide

| Scenario | Recommended Strategy | chunk_size | overlap |
|------|---------|-----------|---------|
| General documents | Recursive character chunking | 800–1200 | 150–200 |
| Technical documentation (e.g. kudig-database) | Parent-child chunking | Parent: 2000 / Child: 400 | 200/50 |
| Code files | AST-based code chunking | By function/class | None |
| Tables / structured data | Row-based chunking + preserve header | By row count | Preserve header |
| Conversation logs / logs | Time-window chunking | By time interval | 1–2 entries |
| Long documents (>100 pages) | Semantic chunking | Dynamic | - |

---

<!-- chunk: 3. Embedding Model Selection -->## 3. Embedding Model Selection

## 3.1 Comparison of Mainstream Embedding Models

| Model | Dimensions | Max Tokens | MTEB Score | Chinese Capability | Cost | Highlights |
|------|------|-----------|---------|---------|------|------|
| **text-embedding-3-large** | 3072 | 8191 | 64.6 | ★★★★☆ | $0.13/1M | OpenAI's strongest |
| **text-embedding-3-small** | 1536 | 8191 | 62.3 | ★★★★☆ | $0.02/1M | Best value |
| **BGE-M3** | 1024 | 8192 | 54.9 | ★★★★★ | Open-source, free | Best multilingual |
| **Jina Embeddings v3** | 1024 | 8192 | 65.0 | ★★★★☆ | $0.02/1M | Latest and strongest |
| **BGE-large-zh-v1.5** | 1024 | 512 | - | ★★★★★ | Open-source, free | Chinese-specialized |
| **m3e-large** | 768 | 512 | - | ★★★★☆ | Open-source, free | Domestic Chinese model |

## 3.2 Embedding Dimension vs. Accuracy Trade-off

```python
# text-embedding-3 supports variable dimensions (reduce dimensions to lower cost)
from openai import OpenAI

client = OpenAI()

# High precision (archival / offline scenarios)
embedding_full = client.embeddings.create(
    model="text-embedding-3-large",
    input="Pod Pending insufficient resources",
    dimensions=3072,  # maximum dimensions
).data[0].embedding

# Balanced (recommended for online retrieval)
embedding_balanced = client.embeddings.create(
    model="text-embedding-3-large",
    input="Pod Pending insufficient resources",
    dimensions=1024,  # 67% dimension reduction, faster storage and queries, ~3% accuracy loss
).data[0].embedding

# Lightweight (high-frequency simple scenarios)
embedding_lite = client.embeddings.create(
    model="text-embedding-3-small",
    input="Pod Pending insufficient resources",
    dimensions=512,
).data[0].embedding
```

---

<!-- chunk: 4. Vector Database Selection -->## 4. Vector Database Selection

## 4.1 Comparison of Mainstream Vector Stores

| Feature | Chroma | Weaviate | Qdrant | Milvus | pgvector |
|------|-------|---------|-------|-------|---------|
| **Positioning** | Development / prototyping | Production-grade | Production-grade | Massive scale | PostgreSQL extension |
| **Deployment** | Embedded / service | Distributed service | Service / cloud | Distributed cluster | PostgreSQL plugin |
| **Vector scale** | <1M | 1M–100M | 1M–100M | >1B | <10M |
| **Hybrid search** | ❌ | ✅ Native | ✅ Native | ✅ | ✅ (manual setup required) |
| **Metadata filtering** | ✅ Basic | ✅ GraphQL | ✅ Powerful | ✅ | ✅ SQL |
| **Multi-tenancy** | ❌ | ✅ | ✅ | ✅ | Schema-based |
| **Horizontal scaling** | ❌ | ✅ | ✅ | ✅ | Limited |
| **K8s deployment** | Simple | Full Helm | Full Helm | Operator | Direct use |
| **Managed service** | ✅ | ✅ WCS | ✅ Qdrant Cloud | ✅ Zilliz | ✅ Supabase |

## 4.2 Qdrant Production Deployment (Recommended)

Qdrant offers the best overall balance of performance, features, and ease of use:

```yaml
# Qdrant K8s deployment
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: qdrant
  namespace: ai-infra
spec:
  serviceName: qdrant
  replicas: 3  # 3 replicas recommended for production
  selector:
    matchLabels:
      app: qdrant
  template:
    spec:
      containers:
      - name: qdrant
        image: qdrant/qdrant:v1.9.0
        ports:
        - containerPort: 6333  # HTTP
        - containerPort: 6334  # gRPC
        env:
        - name: QDRANT__SERVICE__API_KEY
          valueFrom:
            secretKeyRef:
              name: qdrant-secret
              key: api-key
        - name: QDRANT__CLUSTER__ENABLED
          value: "true"
        resources:
          requests:
            memory: "4Gi"
            cpu: "2"
          limits:
            memory: "8Gi"
            cpu: "4"
        volumeMounts:
        - name: qdrant-storage
          mountPath: /qdrant/storage
  volumeClaimTemplates:
  - metadata:
      name: qdrant-storage
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: "fast-ssd"
      resources:
        requests:
          storage: 100Gi
```

```python
from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance, VectorParams, PointStruct,
    Filter, FieldCondition, MatchValue, SearchParams
)

client = QdrantClient(
    url="http://qdrant.ai-infra.svc:6333",
    api_key="your-api-key",
)

# Create collection (K8s knowledge base)
client.create_collection(
    collection_name="kudig_knowledge",
    vectors_config=VectorParams(
        size=1536,           # text-embedding-3-small dimensions
        distance=Distance.COSINE,
        on_disk=True,        # store large-scale data on disk
    ),
    # Enable payload index (speeds up metadata filtering)
    on_disk_payload=True,
)

# Create metadata indexes
client.create_payload_index(
    collection_name="kudig_knowledge",
    field_name="domain",
    field_schema="keyword",
)

client.create_payload_index(
    collection_name="kudig_knowledge",
    field_name="doc_type",
    field_schema="keyword",
)

# Semantic retrieval with metadata filtering
results = client.search(
    collection_name="kudig_knowledge",
    query_vector=query_embedding,
    query_filter=Filter(
        must=[
            FieldCondition(
                key="domain",
                match=MatchValue(value="domain-10-troubleshooting-diagnostics")
            )
        ]
    ),
    limit=10,
    search_params=SearchParams(hnsw_ef=128, exact=False),
)
```

---

<!-- chunk: 5. Hybrid Search -->## 5. Hybrid Search

Pure vector retrieval performs poorly for exact matches (such as proper nouns and error codes). Hybrid search combines dense vector retrieval with sparse BM25 retrieval:
## 5.1 BM25 + Vector Retrieval Fusion

```python
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from langchain_community.vectorstores import Qdrant as QdrantVectorStore

# 1. Vector retriever (semantic relevance)
vector_retriever = QdrantVectorStore(
    client=qdrant_client,
    collection_name="kudig_knowledge",
    embedding=embedding_model,
).as_retriever(search_kwargs={"k": 10})

# 2. BM25 retriever (exact keyword matching)
bm25_retriever = BM25Retriever.from_documents(
    documents,
    k=10,
)

# 3. Fusion retrieval (Reciprocal Rank Fusion)
ensemble_retriever = EnsembleRetriever(
    retrievers=[bm25_retriever, vector_retriever],
    weights=[0.4, 0.6],  # BM25:vector = 4:6 (tunable)
)

# Use hybrid retrieval
docs = ensemble_retriever.get_relevant_documents(
    "CrashLoopBackOff OOMKilled out of memory"
)
```

## 5.2 Qdrant Native Hybrid Retrieval

```python
from qdrant_client.models import SparseVector, NamedSparseVector, NamedVector, Query

# Generate sparse vectors using FastEmbed
from fastembed import SparseTextEmbedding

sparse_model = SparseTextEmbedding(model_name="Qdrant/bm25")
sparse_embeddings = list(sparse_model.embed(["Pod Pending insufficient resources"]))

# Hybrid retrieval request
results = client.query_points(
    collection_name="kudig_knowledge",
    prefetch=[
        # Vector retrieval branch
        models.Prefetch(
            query=dense_vector,
            using="dense",
            limit=20,
        ),
        # Sparse (BM25) retrieval branch
        models.Prefetch(
            query=models.SparseVector(
                indices=sparse_embeddings[0].indices.tolist(),
                values=sparse_embeddings[0].values.tolist(),
            ),
            using="sparse",
            limit=20,
        ),
    ],
    # RRF fusion of both result sets
    query=models.FusionQuery(fusion=models.Fusion.RRF),
    limit=10,
)
```

---

<!-- chunk: 6. Re-ranking -->## 6. Re-ranking

Re-ranking is the most effective technique in the RAG pipeline for improving retrieval precision — it re-orders the initial Top-50 results and takes the Top-5:

```python
from sentence_transformers import CrossEncoder
import torch

class Reranker:
    def __init__(self, model_name: str = "BAAI/bge-reranker-v2-m3"):
        # Cross-encoder model: scores (query, doc) pairs directly, far more accurate than Bi-encoder
        self.model = CrossEncoder(
            model_name,
            device="cuda" if torch.cuda.is_available() else "cpu",
        )
    
    def rerank(
        self, 
        query: str, 
        documents: list[str], 
        top_k: int = 5
    ) -> list[tuple[str, float]]:
        """Re-rank documents"""
        # Build (query, doc) pairs
        pairs = [[query, doc] for doc in documents]
        
        # Cross-encoder scoring
        scores = self.model.predict(pairs)
        
        # Sort by score
        scored_docs = sorted(
            zip(documents, scores),
            key=lambda x: x[1],
            reverse=True
        )
        
        return scored_docs[:top_k]

# Use in the RAG pipeline
reranker = Reranker("BAAI/bge-reranker-v2-m3")

# 1. Broad recall (Top-30)
candidates = retriever.get_relevant_documents(query, k=30)

# 2. Precise ranking (Top-5)
reranked = reranker.rerank(
    query=query,
    documents=[doc.page_content for doc in candidates],
    top_k=5
)

# 3. Generate answer using re-ranked results
context = "\n\n".join([doc for doc, score in reranked])
```

---

<!-- chunk: 7. Advanced RAG Techniques -->## 7. Advanced RAG Techniques

## 7.1 Query Rewriting

```python
# HyDE (Hypothetical Document Embeddings): generate a hypothetical answer, then retrieve
def hyde_retrieval(query: str, retriever) -> list:
    """HyDE: first generate a hypothetical document, then use its vector to retrieve real documents"""
    
    # Step 1: Have the LLM generate a hypothetical answer
    hyde_prompt = f"""Please generate a detailed technical documentation paragraph to answer the following K8s question:
    Question: {query}
    
    Generate a professional, technically accurate paragraph even if you are unsure of the answer."""
    
    hypothetical_doc = llm.invoke(hyde_prompt).content
    
    # Step 2: Use the hypothetical document's vector to retrieve real documents (far better than querying directly with the question)
    results = retriever.get_relevant_documents(hypothetical_doc)
    return results

# Multi-query Retrieval: rewrite the query from multiple perspectives
from langchain.retrievers.multi_query import MultiQueryRetriever

multi_query_retriever = MultiQueryRetriever.from_llm(
    retriever=base_retriever,
    llm=llm,
    prompt=PromptTemplate.from_template("""
    You are a K8s operations expert.
    Original question: {question}
    
    Please rewrite this question from 3 different angles to retrieve more comprehensive information:
    1. From the symptom perspective
    2. From the root cause perspective  
    3. From the solution perspective
    
    Output 3 rewritten queries, one per line.
    """)
)
```

## 7.2 Context Compression

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor

# Extract fragments directly relevant to the question from retrieved documents
compressor = LLMChainExtractor.from_llm(
    llm=ChatOpenAI(model="gpt-4o-mini"),  # Use a cheaper model for compression
)

compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever,
)

# Return only sentences/paragraphs in the documents directly relevant to the query
compressed_docs = compression_retriever.get_relevant_documents(
    "Diagnostic steps for Pod Pending"
)
```

## 7.3 Iterative RAG (Iterative/Recursive RAG)

```python
class IterativeRAG:
    """Multi-round iterative retrieval: after each retrieval, decide whether more information is needed"""
    
    def __init__(self, retriever, llm, max_iterations: int = 3):
        self.retriever = retriever
        self.llm = llm
        self.max_iterations = max_iterations
    
    def answer(self, question: str) -> dict:
        collected_context = []
        queries_used = []
        
        for i in range(self.max_iterations):
            # Retrieve
            search_query = self._generate_query(question, collected_context, i)
            queries_used.append(search_query)
            new_docs = self.retriever.get_relevant_documents(search_query)
            
            # Merge and deduplicate
            for doc in new_docs:
                if doc.page_content not in [c.page_content for c in collected_context]:
                    collected_context.append(doc)
            
            # Check whether the information is sufficient
            sufficiency_check = self.llm.invoke(f"""
            Question: {question}
            Collected information: {[d.page_content for d in collected_context]}
            
            Is the above information sufficient to answer the question? Answer only "YES" or "NO".
            If NO, explain what information is still missing.
            """).content
            
            if sufficiency_check.startswith("YES"):
                break
        
        # Final generation
        final_answer = self._generate_answer(question, collected_context)
        return {
            "answer": final_answer,
            "sources": collected_context,
            "queries_used": queries_used,
            "iterations": i + 1
        }
```

---

<!-- chunk: 8. RAG Evaluation Metrics -->## 8. RAG Evaluation Metrics
## 8.1 RAGAS Evaluation Framework

```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness,           # Faithfulness: whether the answer is grounded in retrieved content
    answer_relevancy,       # Answer Relevancy: whether the answer addresses the question
    context_precision,      # Context Precision: whether all retrieved content is useful
    context_recall,         # Context Recall: whether all necessary information was retrieved
    context_entity_recall,  # Entity Recall
    answer_correctness,     # Answer Correctness
)
from datasets import Dataset

# Build evaluation dataset
eval_data = {
    "question": [
        "What are the most common reasons for a Pod to be in Pending state?",
        "How do you check resource usage on K8s nodes?",
    ],
    "answer": [
        "The most common reasons for Pod Pending include: insufficient resources, node affinity mismatch...",
        "Use the kubectl top nodes command...",
    ],
    "contexts": [
        ["When the scheduler cannot find a suitable node, the Pod will be in Pending state..."],
        ["The kubectl top command requires metrics-server support..."],
    ],
    "ground_truth": [
        "Common reasons for Pod Pending: 1. Insufficient resources 2. Node affinity 3. Taint/Toleration...",
        "kubectl top nodes shows node CPU/memory usage and requires metrics-server...",
    ],
}

dataset = Dataset.from_dict(eval_data)
result = evaluate(
    dataset=dataset,
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall],
    llm=llm,
    embeddings=embedding_model,
)

print(result)
# Output:
# {'faithfulness': 0.92, 'answer_relevancy': 0.88, 
#  'context_precision': 0.85, 'context_recall': 0.79}
```

## 8.2 RAG Quality Benchmark Targets

| Metric | Acceptable | Excellent | Description |
|------|-------|------|------|
| **Faithfulness** | >0.80 | >0.95 | Answers must be grounded in retrieved content; no fabrication |
| **Answer Relevancy** | >0.75 | >0.90 | The answer genuinely addresses what was asked |
| **Context Precision** | >0.70 | >0.85 | Retrieved content must have a high signal-to-noise ratio |
| **Context Recall** | >0.65 | >0.80 | Key information must not be missed |
| **Retrieval Latency** | <500ms | <200ms | P95 latency |
| **End-to-End Latency** | <3s | <1.5s | Total time including retrieval + generation |

---

<!-- chunk: 9. Production RAG Pipeline Complete Implementation -->## 9. Production RAG Pipeline Complete Implementation

```python
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.prompts import PromptTemplate

# Production-grade RAG Prompt (K8s operations scenario)
K8S_RAG_PROMPT = PromptTemplate.from_template("""
You are a Kubernetes production operations expert. Answer questions based on the following knowledge base content.

[Knowledge Base Sources]
{summaries}

[Question]
{question}

[Response Guidelines]
1. Only answer based on information in the knowledge base; do not fabricate
2. If knowledge base information is insufficient, clearly state "No relevant information in the knowledge base"
3. Provide specific kubectl commands or YAML examples
4. Point out operational risks (if any)
5. Cite reference sources at the end of your answer

Answer:
""")

class ProductionRAGPipeline:
    def __init__(
        self,
        vectorstore,
        llm,
        embedding_model,
        reranker: Optional[Reranker] = None,
        enable_hybrid_search: bool = True,
    ):
        self.vectorstore = vectorstore
        self.llm = llm
        self.reranker = reranker
        
        # Configure retriever
        base_retriever = vectorstore.as_retriever(
            search_type="mmr",  # Max Marginal Relevance, reduces duplication
            search_kwargs={
                "k": 20,
                "fetch_k": 50,   # Fetch 50 first, MMR selects 20
                "lambda_mult": 0.7,  # Relevance vs diversity trade-off
            }
        )
        
        self.retriever = base_retriever
    
    def query(
        self,
        question: str,
        domain_filter: Optional[str] = None,
        top_k: int = 5,
    ) -> dict:
        """Execute a RAG query"""
        
        # 1. Retrieval
        raw_docs = self.retriever.get_relevant_documents(question)
        
        # 2. Domain filtering (optional)
        if domain_filter:
            raw_docs = [d for d in raw_docs 
                       if d.metadata.get("domain") == domain_filter]
        
        # 3. Re-ranking (optional)
        if self.reranker and raw_docs:
            reranked = self.reranker.rerank(
                query=question,
                documents=[d.page_content for d in raw_docs],
                top_k=top_k,
            )
            final_docs = [content for content, score in reranked]
        else:
            final_docs = [d.page_content for d in raw_docs[:top_k]]
        
        # 4. Generation
        context = "\n\n---\n\n".join(final_docs)
        response = self.llm.invoke(
            K8S_RAG_PROMPT.format(
                summaries=context,
                question=question,
            )
        )
        
        return {
            "answer": response.content,
            "sources": [d.metadata.get("source") for d in raw_docs[:top_k]],
            "retrieved_count": len(raw_docs),
        }
```

---

<!-- chunk: 10. Best Practices and Common Pitfalls -->## 10. Best Practices and Common Pitfalls

## Best Practices

- **Design metadata first**: Metadata fields in the vector store directly affect filtering efficiency; design them carefully before building the index
- **Optimize retrieval before generation**: Poor RAG quality is usually a retrieval problem; don't rush to swap out the model
- **Re-ranking significantly improves quality**: Re-ranking from Top-30 down to Top-5 typically outperforms simply increasing the retrieval count
- **Multi-path recall fusion**: Combining BM25 + vector search almost always outperforms a single retrieval method in every scenario
- **Evaluate regularly**: Use RAGAS to establish automated quality monitoring and detect regressions after knowledge base updates

## Common Pitfalls

- **chunk_size too large**: Too much information per chunk causes the vector semantics to become vague, degrading retrieval accuracy (recommended: 400–800 character sub-chunks)
- **Ignoring overlap**: Setting chunk_overlap to 0 causes sentences to be cut at chunk boundaries, losing context
- **Not indexing metadata**: Without indexed metadata fields in the vector store, filtered queries are extremely slow
- **Embedding dimension mismatch**: Indexed with 1536 dimensions but queried with a 3072-dimension API — results are meaningless
- **Forgetting embedding invalidation**: After updating the chunking strategy or embedding model, all documents must be re-indexed

---

<!-- chunk: Related Documents -->## Related Documents

| Document | Related Content |
|------|---------|
| [03 - Agent Framework Comparison](./03-agent-frameworks-comparison.md) | LlamaIndex/LangChain RAG implementation |
| [07 - Memory Management](./07-memory-context-management.md) | Boundary between long-term memory and RAG |
| [08 - Evaluation & Observability](./08-agent-evaluation-observability.md) | Detailed RAGAS evaluation framework configuration |
| [domain-14-ai-ml-infra/20-vector-database-rag.md](../domain-14-ai-ml-infra/20-vector-database-rag.md) | Vector database infrastructure |
| [15 - Agent Corpus Gap Analysis](./15-agent-corpus-gap-analysis.md) | Analysis of kudig-database as RAG corpus |

---

*This document is original content from the kudig-database project, 02-ai-agents topic.*

---

<!-- chunk: Obsidian Related Documents -->## Obsidian Related Documents

- 02-ai-agents MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|AI Agent Engineering Topic]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|AI Agent Fundamentals and Core Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|LLM Foundation Model Selection and Evaluation]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|In-Depth Comparison of Mainstream Agent Frameworks]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Tool Use & Function Calling Design Specifications]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Multi-Agent Orchestration and Collaboration Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation Framework and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]
- [[domain-14-ai-ml-infra/02-ai-agents/11-cost-latency-optimization.md|Cost and Latency Optimization Strategies]]
## See Also

- 02-llm-foundation-models
- 03-agent-frameworks-comparison
- 05-tool-use-function-calling
- 06-multi-agent-orchestration


<!-- risk-assessed -->
