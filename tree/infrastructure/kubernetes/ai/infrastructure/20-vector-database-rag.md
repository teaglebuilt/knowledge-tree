---
title: 147 - Vector Databases and RAG Architecture
description: '# 147 - Vector Databases and RAG Architecture'
summary: 'service.beta.kubernetes.io/aws-load-balancer-type: nlb'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- etcd
- prometheus
- helm
- opa
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- MLOps Engineers
- SRE
estimated_read_time: 5min
intent_queries:
- What is vector databases and RAG architecture
- How to understand vector databases and RAG architecture
- Kubernetes 11 AI infra best practices
trigger_keywords:
- Vector Databases and RAG Architecture
- ai
- infra
prerequisites:
- kubectl-basics
- helm-basics
- prometheus-basics
- etcd-basics
- redis-basics
- gpu-scheduling-basics
- policy-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: Dillan Teagle
  role: contributor
cross_refs:
- type: domain
  path: ../domain-02-workloads-applications/
  label: 'Related Knowledge Domain: domain-02-workloads-applications'
- type: domain
  path: ../domain-03-networking-traffic/
  label: 'Related Knowledge Domain: domain-03-networking-traffic'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/20-vector-database-rag.md
---

> **Production Environment Security Tips**
>
> Commands included in this document can be directly executed. Before executing, please confirm: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information collection with no side effects).




# 147 - Vector Database and RAG Architecture

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **Difficulty**: Advanced | **Reference**: [Milvus](https://milvus.io/docs) | [Weaviate](https://weaviate.io/developers/weaviate) | [LangChain](https://python.langchain.com/)


## 1. RAG System Architecture Overview

### 1.1 Production-Level RAG Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                        Production RAG System Architecture                            │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌─────────────────────────────────────────────────────────────────────────────┐    │
│  │                           Data Ingestion Pipeline                            │    │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐           │    │
│  │  │  Docs   │  │  Parse  │  │  Chunk  │  │ Embed   │  │  Store  │           │    │
│  │  │ (PDF/   │─▶│ Extract │─▶│ Split   │─▶│ Vectors │─▶│ Vector  │           │    │
│  │  │ Web/DB) │  │ Clean   │  │ Overlap │  │ (E5/BGE)│  │   DB    │           │    │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘           │    │
│  └─────────────────────────────────────────────────────────────────────────────┘    │
│                                         │                                            │
│  ┌──────────────────────────────────────▼──────────────────────────────────────┐    │
│  │                              Vector Database                                 │    │
│  │  ┌─────────────────────────────────────────────────────────────────────┐   │    │
│  │  │                     Milvus / Weaviate / Qdrant                      │   │    │
│  │  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────────┐ │   │    │
│  │  │  │   Index     │  │   Storage   │  │      Query Engine          │ │   │    │
│  │  │  │  (HNSW/     │  │  (Segments, │  │  - ANN Search              │ │   │    │
│  │  │  │   IVF/      │  │   Shards,   │  │  - Hybrid Search           │ │   │    │
│  │  │  │   DiskANN)  │  │   Replicas) │  │  - Filtered Search         │ │   │    │
│  │  │  └─────────────┘  └─────────────┘  └─────────────────────────────┘ │   │    │
│  │  └─────────────────────────────────────────────────────────────────────┘   │    │
│  └─────────────────────────────────────────────────────────────────────────────┘    │
│                                         │                                            │
│  ┌──────────────────────────────────────▼──────────────────────────────────────┐    │
│  │                            Retrieval Pipeline                                │    │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐           │    │
│  │  │  Query  │  │ Rewrite │  │ Vector  │  │ Rerank  │  │ Context │           │    │
│  │  │  Input  │─▶│ Expand  │─▶│ Search  │─▶│ Filter  │─▶│ Build   │           │    │
│  │  │         │  │ (HyDE)  │  │ +BM25   │  │ (Cohere)│  │         │           │    │
│  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘           │    │
│  └─────────────────────────────────────────────────────────────────────────────┘    │
│                                         │                                            │
│  ┌──────────────────────────────────────▼──────────────────────────────────────┐    │
│  │                           Generation Pipeline                                │    │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────────────────┐ │    │
│  │  │   Prompt        │  │      LLM        │  │     Post-Processing        │ │    │
│  │  │   Template      │─▶│   (vLLM/TGI)    │─▶│   Citation, Validation     │ │    │
│  │  │   + Context     │  │   Generation    │  │   Fact-checking            │ │    │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────────────────┘ │    │
│  └─────────────────────────────────────────────────────────────────────────────┘    │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Comprehensive Comparison of Vector Databases

| Database | QPS | P99 latency | Maximum vector | Distributed | GPU acceleration | Open Source | Managed Service | Applicable Scenario |
|--------|-----|---------|----------|-------|---------|------|----------|---------|
| **Milvus** | 10K+ | <10ms | 10B+ | ✓ | ✓ | ✓ | Zilliz | Large-scale production |
| **Weaviate** | 5K | <20ms | 1B+ | ✓ | ✗ | ✓ | Weaviate Cloud | Enterprise-level |
| **Qdrant** | 8K | <15ms | 1B+ | ✓ | ✗ | ✓ | Qdrant Cloud | High-performance |
| **Pinecone** | 10K+ | <20ms | 1B+ | ✓ | ✓ | ✗ | Pinecone | Preferred managed service |
| **Chroma** | 1K | <50ms | 10M | ✗ | ✗ | ✓ | - | Development/test |
| **pgvector** | 500 | <100ms | 100M | ✗ | ✗ | ✓ | - | PostgreSQL users |
| **Elasticsearch** | 3K | <50ms | 1B+ | ✓ | ✗ | ✓ | Elastic Cloud | Hybrid search |
| **Redis Stack** | 15K+ | <5ms | 100M | ✓ | ✗ | ✓ | Redis Cloud | Low latency |

### 1.3 Model Comparison of Embeddings

| Model | Dimensions | MTEB Score | Chinese Support | Speed | Applicable Scenario |
|-----|------|---------|---------|------|---------|
| **text-embedding-3-large** | 3072 | 64.6 | ✓ | Medium | General preferred |
| **text-embedding-3-small** | 1536 | 62.3 | ✓ | Fast | Cost-sensitive |
| **E5-large-v2** | 1024 | 62.0 | ✓ | Medium | Open-source preferred |
| **BGE-large-zh-v1.5** | 1024 | 64.5 | ★★★ | Medium | Chinese preferred |
| **Cohere embed-v3** | 1024 | 64.5 | ✓ | Fast | Multilingual |
| **Jina-embeddings-v2** | 768 | 60.4 | ✓ | Fast | Long text |
| **GTE-large** | 1024 | 63.1 | ✓ | Medium | General |
| **instructor-xl** | 768 | 61.8 | ✓ | slow | instruction-following |

---


## 2. Milvus Production Deployment

### 2.1 Milvus Cluster Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                           Milvus Cluster Architecture                                │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌──────────────────────────────────────────────────────────────────────────────┐   │
│  │                              Access Layer                                     │   │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐               │   │
│  │  │   Proxy Node    │  │   Proxy Node    │  │   Proxy Node    │               │   │
│  │  │   (gRPC/HTTP)   │  │   (gRPC/HTTP)   │  │   (gRPC/HTTP)   │               │   │
│  │  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘               │   │
│  └───────────┼────────────────────┼────────────────────┼────────────────────────┘   │
│              │                    │                    │                             │
│  ┌───────────▼────────────────────▼────────────────────▼────────────────────────┐   │
│  │                           Coordinator Layer                                   │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │   │
│  │  │  Root Coord │  │ Query Coord │  │ Data Coord  │  │ Index Coord │          │   │
│  │  │  (DDL/DCL)  │  │ (Query Mgmt)│  │ (Data Mgmt) │  │ (Index Mgmt)│          │   │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │   │
│  └──────────────────────────────────────────────────────────────────────────────┘   │
│                                         │                                            │
│  ┌──────────────────────────────────────▼───────────────────────────────────────┐   │
│  │                              Worker Layer                                     │   │
│  │  ┌─────────────────────────────────────────────────────────────────────────┐ │   │
│  │  │                          Query Nodes                                     │ │   │
│  │  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐       │ │   │
│  │  │  │  QN-1   │  │  QN-2   │  │  QN-3   │  │  QN-4   │  │  QN-5   │       │ │   │
│  │  │  │ Shard 1 │  │ Shard 2 │  │ Shard 3 │  │ Shard 1 │  │ Shard 2 │       │ │   │
│  │  │  │ (Rep 1) │  │ (Rep 1) │  │ (Rep 1) │  │ (Rep 2) │  │ (Rep 2) │       │ │   │
│  │  │  └─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘       │ │   │
│  │  └─────────────────────────────────────────────────────────────────────────┘ │   │
│  │  ┌─────────────────────────────────────────────────────────────────────────┐ │   │
│  │  │                          Data Nodes                                      │ │   │
│  │  │  ┌─────────┐  ┌─────────┐  ┌─────────┐                                  │ │   │
│  │  │  │  DN-1   │  │  DN-2   │  │  DN-3   │                                  │ │   │
│  │  │  │ Insert  │  │ Insert  │  │ Insert  │                                  │ │   │
│  │  │  │ Buffer  │  │ Buffer  │  │ Buffer  │                                  │ │   │
│  │  │  └─────────┘  └─────────┘  └─────────┘                                  │ │   │
│  │  └─────────────────────────────────────────────────────────────────────────┘ │   │
│  │  ┌─────────────────────────────────────────────────────────────────────────┐ │   │
│  │  │                          Index Nodes (GPU)                               │ │   │
│  │  │  ┌─────────┐  ┌─────────┐                                               │ │   │
│  │  │  │  IN-1   │  │  IN-2   │                                               │ │   │
│  │  │  │ A100 GPU│  │ A100 GPU│                                               │ │   │
│  │  │  └─────────┘  └─────────┘                                               │ │   │
│  │  └─────────────────────────────────────────────────────────────────────────┘ │   │
│  └──────────────────────────────────────────────────────────────────────────────┘   │
│                                         │                                            │
│  ┌──────────────────────────────────────▼───────────────────────────────────────┐   │
│  │                              Storage Layer                                    │   │
│  │  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐               │   │
│  │  │     etcd        │  │     Pulsar      │  │   MinIO/S3      │               │   │
│  │  │  (Metadata)     │  │  (Log Broker)   │  │  (Object Store) │               │   │
│  │  │  3 replicas     │  │  3 brokers      │  │  Tiered Storage │               │   │
│  │  └─────────────────┘  └─────────────────┘  └─────────────────┘               │   │
│  └──────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 Deployment of Milvus Operator

```yaml
# Milvus Operator Installation
apiVersion: v1
kind: Namespace
metadata:
  name: milvus
---
# Install Operator Using Helm
# helm repo add milvus-operator https://zilliztech.github.io/milvus-operator/
# helm install milvus-operator milvus-operator/milvus-operator -n milvus
---
apiVersion: milvus.io/v1beta1
kind: Milvus
metadata:
  name: milvus-cluster
  namespace: milvus
spec:
  mode: cluster
  
  # Component Configuration
  dependencies:
    # etcd Configuration
    etcd:
      inCluster:
        deletionPolicy: Delete
        pvcDeletion: true
        values:
          replicaCount: 3
          resources:
            requests:
              cpu: "1"
              memory: "2Gi"
            limits:
              cpu: "2"
              memory: "4Gi"
          persistence:
            storageClass: fast-ssd
            size: 50Gi
    
    # Pulsar Configuration
    pulsar:
      inCluster:
        deletionPolicy: Delete
        pvcDeletion: true
        values:
          components:
            autorecovery: true
            proxy: true
            toolset: false
          broker:
            replicaCount: 3
            resources:
              requests:
                cpu: "2"
                memory: "8Gi"
          bookkeeper:
            replicaCount: 3
            resources:
              requests:
                cpu: "2"
                memory: "8Gi"
            volumes:
              journal:
                size: 100Gi
                storageClass: fast-ssd
              ledgers:
                size: 200Gi
                storageClass: fast-ssd
          zookeeper:
            replicaCount: 3
    
    # Object Storage Configuration
    storage:
      type: S3
      secretRef: milvus-s3-secret
      external: true
      endpoint: s3.amazonaws.com
      bucket: milvus-data
      useSSL: true
      useIAM: true
  
  # Component Configuration
  components:
    # Proxy Configuration
    proxy:
      replicas: 3
      resources:
        requests:
          cpu: "2"
          memory: "4Gi"
        limits:
          cpu: "4"
          memory: "8Gi"
      serviceType: LoadBalancer
      annotations:
        service.beta.kubernetes.io/aws-load-balancer-type: nlb
        service.beta.kubernetes.io/aws-load-balancer-internal: "true"
    
    # QueryNode Configuration
    queryNode:
      replicas: 5
      resources:
        requests:
          cpu: "4"
          memory: "16Gi"
        limits:
          cpu: "8"
          memory: "32Gi"
    
    # DataNode Configuration
    dataNode:
      replicas: 3
      resources:
        requests:
          cpu: "2"
          memory: "8Gi"
        limits:
          cpu: "4"
          memory: "16Gi"
    
    # IndexNode Configuration (GPU Acceleration)
    indexNode:
      replicas: 2
      resources:
        requests:
          cpu: "4"
          memory: "16Gi"
          nvidia.com/gpu: "1"
        limits:
          cpu: "8"
          memory: "32Gi"
          nvidia.com/gpu: "1"
    
    # RootCoord Configuration
    rootCoord:
      replicas: 1
      resources:
        requests:
          cpu: "1"
          memory: "2Gi"
    
    # QueryCoord Configuration
    queryCoord:
      replicas: 1
      resources:
        requests:
          cpu: "1"
          memory: "2Gi"
    
    # DataCoord Configuration
    dataCoord:
      replicas: 1
      resources:
        requests:
          cpu: "1"
          memory: "2Gi"
    
    # IndexCoord Configuration
    indexCoord:
      replicas: 1
      resources:
        requests:
          cpu: "1"
          memory: "2Gi"
  
  # Configuration Parameters
  config:
    # General Configuration
    common:
      gracefulTime: 5000
      gracefulStopTimeout: 30
    
    # Proxy Configuration
    proxy:
      maxTaskNum: 1024
      maxConnectionNum: 10000
      accessLog:
        enable: true
        filename: access.log
    
    # QueryNode Configuration
    queryNode:
      gracefulTime: 5000
      enableDisk: true
      cache:
        enabled: true
        memoryLimit: 8589934592  # 8GB
    
    # Index Configuration
    indexNode:
      enableDisk: true
    
    # Data Configuration
    dataCoord:
      segment:
        maxSize: 512
        sealProportion: 0.23
      compaction:
        enableAutoCompaction: true
---
apiVersion: v1
kind: Secret
metadata:
  name: milvus-s3-secret
  namespace: milvus
type: Opaque
stringData:
  accesskey: "AKIAXXXXXXXXXXXXXXXX"
  secretkey: "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### 2.3 Configuration of Collections and Indexes

```python
# milvus_collection.py - Milvus Collection Management
from pymilvus import (
    connections, Collection, FieldSchema, CollectionSchema, 
    DataType, utility, MilvusClient
)
from typing import List, Dict, Optional
import numpy as np

class MilvusCollectionManager:
    """Milvus Collection Manager"""
    
    def __init__(
        self,
        host: str = "milvus-cluster-proxy.milvus",
        port: int = 19530,
        db_name: str = "default"
    ):
        self.host = host
        self.port = port
        self.db_name = db_name
        
        # Connect to Milvus
        connections.connect(
            alias="default",
            host=host,
            port=port,
            db_name=db_name
        )
    
    def create_collection(
        self,
        collection_name: str,
        dim: int = 1024,
        index_type: str = "HNSW",
        metric_type: str = "COSINE",
        enable_dynamic_field: bool = True,
    ):
        """Create Collection"""
        
        # Define Schema
        fields = [
            FieldSchema(
                name="id",
                dtype=DataType.VARCHAR,
                is_primary=True,
                max_length=64
            ),
            FieldSchema(
                name="vector",
                dtype=DataType.FLOAT_VECTOR,
                dim=dim
            ),
            FieldSchema(
                name="text",
                dtype=DataType.VARCHAR,
                max_length=65535
            ),
            FieldSchema(
                name="metadata",
                dtype=DataType.JSON
            ),
            FieldSchema(
                name="created_at",
                dtype=DataType.INT64
            ),
        ]
        
        schema = CollectionSchema(
            fields=fields,
            description=f"RAG Collection: {collection_name}",
            enable_dynamic_field=enable_dynamic_field
        )
        
        # Create Collection
        collection = Collection(
            name=collection_name,
            schema=schema,
            using="default",
            shards_num=4,  # 分片数
            num_partitions=16  # 分区数
        )
        
        # Create Index
        index_params = self._get_index_params(index_type, metric_type)
        collection.create_index(
            field_name="vector",
            index_params=index_params,
            index_name="vector_index"
        )
        
        # Create Scalar Index
        collection.create_index(
            field_name="created_at",
            index_name="created_at_index"
        )
        
        # Load into Memory
        collection.load()
        
        return collection
    
    def _get_index_params(
        self,
        index_type: str,
        metric_type: str
    ) -> dict:
        """Get Index Parameters"""
        
        index_configs = {
            "HNSW": {
                "index_type": "HNSW",
                "metric_type": metric_type,
                "params": {
                    "M": 16,  # 每个节点的连接数
                    "efConstruction": 256  # 构建时的搜索范围
                }
            },
            "IVF_FLAT": {
                "index_type": "IVF_FLAT",
                "metric_type": metric_type,
                "params": {
                    "nlist": 1024  # 聚类中心数
                }
            },
            "IVF_SQ8": {
                "index_type": "IVF_SQ8",
                "metric_type": metric_type,
                "params": {
                    "nlist": 1024
                }
            },
            "IVF_PQ": {
                "index_type": "IVF_PQ",
                "metric_type": metric_type,
                "params": {
                    "nlist": 1024,
                    "m": 16,  # 子向量数
                    "nbits": 8  # 每个子向量的位数
                }
            },
            "DISKANN": {
                "index_type": "DISKANN",
                "metric_type": metric_type,
                "params": {}
            },
            "GPU_IVF_FLAT": {
                "index_type": "GPU_IVF_FLAT",
                "metric_type": metric_type,
                "params": {
                    "nlist": 1024
                }
            },
            "GPU_IVF_PQ": {
                "index_type": "GPU_IVF_PQ",
                "metric_type": metric_type,
                "params": {
                    "nlist": 1024,
                    "m": 16,
                    "nbits": 8
                }
            }
        }
        
        return index_configs.get(index_type, index_configs["HNSW"])
    
    def insert_vectors(
        self,
        collection_name: str,
        vectors: List[List[float]],
        texts: List[str],
        ids: List[str],
        metadata: List[dict],
        batch_size: int = 1000
    ):
        """Batch Insert Vectors"""
        
        collection = Collection(collection_name)
        
        # Batch Insert
        total = len(vectors)
        for i in range(0, total, batch_size):
            batch_end = min(i + batch_size, total)
            
            data = [
                ids[i:batch_end],
                vectors[i:batch_end],
                texts[i:batch_end],
                metadata[i:batch_end],
                [int(time.time()) for _ in range(batch_end - i)]
            ]
            
            collection.insert(data)
        
        # Flush to Storage
        collection.flush()
        
        return total
    
    def search(
        self,
        collection_name: str,
        query_vectors: List[List[float]],
        top_k: int = 10,
        filter_expr: str = None,
        output_fields: List[str] = None,
        search_params: dict = None
    ):
        """Vector Search"""
        
        collection = Collection(collection_name)
        
        if search_params is None:
            search_params = {
                "metric_type": "COSINE",
                "params": {"ef": 128}  # HNSW搜索参数
            }
        
        if output_fields is None:
            output_fields = ["id", "text", "metadata"]
        
        results = collection.search(
            data=query_vectors,
            anns_field="vector",
            param=search_params,
            limit=top_k,
            expr=filter_expr,
            output_fields=output_fields,
            consistency_level="Strong"
        )
        
        return results
    
    def hybrid_search(
        self,
        collection_name: str,
        query_vector: List[float],
        query_text: str,
        top_k: int = 10,
        alpha: float = 0.5,  # 向量权重
        filter_expr: str = None
    ):
        """Hybrid Search (Vector + BM25)"""
        
        collection = Collection(collection_name)
        
        # Vector Search
        vector_results = self.search(
            collection_name,
            [query_vector],
            top_k=top_k * 2,
            filter_expr=filter_expr
        )[0]
        
        # Combine Scores
        combined_results = []
        for hit in vector_results:
            combined_score = hit.score * alpha
            combined_results.append({
                "id": hit.id,
                "score": combined_score,
                "text": hit.entity.get("text"),
                "metadata": hit.entity.get("metadata")
            })
        
        # Sort and return top_k
        combined_results.sort(key=lambda x: x["score"], reverse=True)
        return combined_results[:top_k]

# Index Type Selection Guide
INDEX_SELECTION_GUIDE = """
索引选择指南:

1. HNSW (推荐默认):
   - 优点: 高召回率, 低延迟
   - 缺点: 内存占用大
   - 适用: <1亿向量, 高精度需求

2. IVF_FLAT:
   - 优点: 内存占用适中
   - 缺点: 延迟较高
   - 适用: 精度敏感, 可接受延迟

3. IVF_PQ:
   - 优点: 极低内存占用
   - 缺点: 召回率下降
   - 适用: 超大规模, 成本敏感

4. DiskANN:
   - 优点: SSD存储, 无限扩展
   - 缺点: 延迟较高
   - 适用: >1亿向量

5. GPU索引:
   - 优点: 极高吞吐量
   - 缺点: 需要GPU
   - 适用: 高并发, 实时搜索
"""
```

### 2.4 Configuration of Milvus Monitoring

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: milvus-monitor
  namespace: milvus
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: milvus
  endpoints:
  - port: metrics
    interval: 15s
    path: /metrics
---
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: milvus-alerts
  namespace: milvus
spec:
  groups:
  - name: milvus-health
    rules:
    # Search latency alarm
    - alert: MilvusHighSearchLatency
      expr: |
        histogram_quantile(0.99, sum(rate(milvus_proxy_search_vectors_duration_seconds_bucket[5m])) by (le)) > 0.5
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Milvus search latency is too high"
        description: "P99 latency {{ $value }} seconds"
    
    # QPS drop alarm
    - alert: MilvusLowQPS
      expr: |
        sum(rate(milvus_proxy_search_vectors_total[5m])) < 100
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "Milvus QPS drops"
    
    # Memory usage alarm
    - alert: MilvusHighMemoryUsage
      expr: |
        milvus_querynode_memory_usage_ratio > 0.85
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "QueryNode memory usage is too high"
    
    # Disk space alarm
    - alert: MilvusLowDiskSpace
      expr: |
        milvus_storage_disk_usage_ratio > 0.80
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "Storage disk space is insufficient"
    
    # Component unhealthy
    - alert: MilvusComponentUnhealthy
      expr: |
        milvus_component_healthy == 0
      for: 2m
      labels:
        severity: critical
      annotations:
        summary: "Milvus component is unhealthy"
        description: "Component {{ $labels.component }} status is abnormal"
  
  - name: milvus-performance
    rules:
    # Search QPS
    - record: milvus:search_qps
      expr: sum(rate(milvus_proxy_search_vectors_total[5m]))
    
    # Insert QPS
    - record: milvus:insert_qps
      expr: sum(rate(milvus_proxy_insert_vectors_total[5m]))
    
    # Search latency P50/P95/P99
    - record: milvus:search_latency_p50
      expr: |
        histogram_quantile(0.50, sum(rate(milvus_proxy_search_vectors_duration_seconds_bucket[5m])) by (le))
    
    - record: milvus:search_latency_p95
      expr: |
        histogram_quantile(0.95, sum(rate(milvus_proxy_search_vectors_duration_seconds_bucket[5m])) by (le))
    
    - record: milvus:search_latency_p99
      expr: |
        histogram_quantile(0.99, sum(rate(milvus_proxy_search_vectors_duration_seconds_bucket[5m])) by (le))
```

---


## 3. Weaviate Deployment

### 3.1 Configuration of Weaviate Cluster

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: weaviate
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: weaviate
  namespace: weaviate
spec:
  serviceName: weaviate-headless
  replicas: 3
  selector:
    matchLabels:
      app: weaviate
  template:
    metadata:
      labels:
        app: weaviate
    spec:
      containers:
      - name: weaviate
        image: semitechnologies/weaviate:1.24.1
        
        env:
        # Cluster configuration
        - name: CLUSTER_HOSTNAME
          valueFrom:
            fieldRef:
              fieldPath: metadata.name
        - name: CLUSTER_GOSSIP_BIND_PORT
          value: "7100"
        - name: CLUSTER_DATA_BIND_PORT
          value: "7101"
        - name: CLUSTER_JOIN
          value: "weaviate-0.weaviate-headless.weaviate.svc.cluster.local:7100,weaviate-1.weaviate-headless.weaviate.svc.cluster.local:7100,weaviate-2.weaviate-headless.weaviate.svc.cluster.local:7100"
        
        # Performance configuration
        - name: QUERY_DEFAULTS_LIMIT
          value: "25"
        - name: QUERY_MAXIMUM_RESULTS
          value: "10000"
        - name: PERSISTENCE_DATA_PATH
          value: "/var/lib/weaviate"
        
        # Module configuration
        - name: ENABLE_MODULES
          value: "text2vec-openai,text2vec-cohere,text2vec-huggingface,generative-openai,generative-cohere,qna-openai,reranker-cohere"
        - name: DEFAULT_VECTORIZER_MODULE
          value: "text2vec-openai"
        
        # Authentication configuration
        - name: AUTHENTICATION_APIKEY_ENABLED
          value: "true"
        - name: AUTHENTICATION_APIKEY_ALLOWED_KEYS
          valueFrom:
            secretKeyRef:
              name: weaviate-secrets
              key: api-keys
        - name: AUTHENTICATION_APIKEY_USERS
          value: "admin,readonly"
        
        # Resource limits
        - name: LIMIT_RESOURCES
          value: "true"
        - name: MAXIMUM_CONCURRENT_GET_REQUESTS
          value: "500"
        
        ports:
        - containerPort: 8080
          name: http
        - containerPort: 50051
          name: grpc
        - containerPort: 7100
          name: gossip
        - containerPort: 7101
          name: data
        
        resources:
          requests:
            cpu: "4"
            memory: "16Gi"
          limits:
            cpu: "8"
            memory: "32Gi"
        
        volumeMounts:
        - name: data
          mountPath: /var/lib/weaviate
        
        livenessProbe:
          httpGet:
            path: /v1/.well-known/live
            port: 8080
          initialDelaySeconds: 120
          periodSeconds: 30
        
        readinessProbe:
          httpGet:
            path: /v1/.well-known/ready
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
      
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchLabels:
                app: weaviate
            topologyKey: kubernetes.io/hostname
  
  volumeClaimTemplates:
  - metadata:
      name: data
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: fast-ssd
      resources:
        requests:
          storage: 500Gi
---
apiVersion: v1
kind: Service
metadata:
  name: weaviate
  namespace: weaviate
spec:
  type: LoadBalancer
  ports:
  - port: 8080
    targetPort: 8080
    name: http
  - port: 50051
    targetPort: 50051
    name: grpc
  selector:
    app: weaviate
---
apiVersion: v1
kind: Service
metadata:
  name: weaviate-headless
  namespace: weaviate
spec:
  clusterIP: None
  ports:
  - port: 7100
    name: gossip
  - port: 7101
    name: data
  selector:
    app: weaviate
---
apiVersion: v1
kind: Secret
metadata:
  name: weaviate-secrets
  namespace: weaviate
type: Opaque
stringData:
  api-keys: "admin-key-xxxxx,readonly-key-xxxxx"
```

### 3.2 Schema and Data Operations of Weaviate

```python
# weaviate_operations.py - Weaviate operations
import weaviate
from weaviate.classes.config import Configure, Property, DataType
from weaviate.classes.query import MetadataQuery, Filter
from typing import List, Dict, Optional
import json

class WeaviateManager:
    """Weaviate manager"""
    
    def __init__(
        self,
        url: str = "http://weaviate.weaviate:8080",
        api_key: str = None,
        openai_api_key: str = None
    ):
        headers = {}
        if openai_api_key:
            headers["X-OpenAI-Api-Key"] = openai_api_key
        
        self.client = weaviate.connect_to_custom(
            http_host=url.replace("http://", "").split(":")[0],
            http_port=8080,
            http_secure=False,
            grpc_host=url.replace("http://", "").split(":")[0],
            grpc_port=50051,
            grpc_secure=False,
            auth_credentials=weaviate.auth.AuthApiKey(api_key) if api_key else None,
            headers=headers
        )
    
    def create_collection(
        self,
        name: str,
        vectorizer: str = "text2vec-openai",
        generative: str = "generative-openai",
        replication_factor: int = 3,
    ):
        """Create Collection"""
        
        # Configure vectorizer
        vectorizer_config = None
        if vectorizer == "text2vec-openai":
            vectorizer_config = Configure.Vectorizer.text2vec_openai(
                model="text-embedding-3-small",
                vectorize_collection_name=False
            )
        elif vectorizer == "text2vec-cohere":
            vectorizer_config = Configure.Vectorizer.text2vec_cohere(
                model="embed-multilingual-v3.0"
            )
        
        # Configure generator
        generative_config = None
        if generative == "generative-openai":
            generative_config = Configure.Generative.openai(
                model="gpt-4-turbo-preview"
            )
        
        # Create Collection
        collection = self.client.collections.create(
            name=name,
            vectorizer_config=vectorizer_config,
            generative_config=generative_config,
            replication_config=Configure.replication(
                factor=replication_factor
            ),
            properties=[
                Property(
                    name="content",
                    data_type=DataType.TEXT,
                    vectorize_property_name=False,
                    tokenization=weaviate.classes.config.Tokenization.WORD
                ),
                Property(
                    name="title",
                    data_type=DataType.TEXT,
                    vectorize_property_name=False
                ),
                Property(
                    name="source",
                    data_type=DataType.TEXT,
                    vectorize_property_name=False,
                    skip_vectorization=True
                ),
                Property(
                    name="metadata",
                    data_type=DataType.OBJECT,
                    skip_vectorization=True
                ),
                Property(
                    name="created_at",
                    data_type=DataType.DATE,
                    skip_vectorization=True
                ),
            ],
            # Vector index configuration
            vector_index_config=Configure.VectorIndex.hnsw(
                distance_metric=weaviate.classes.config.VectorDistances.COSINE,
                ef_construction=256,
                max_connections=64,
                ef=128
            ),
            # Inverted Index Configuration
            inverted_index_config=Configure.inverted_index(
                bm25_b=0.75,
                bm25_k1=1.2,
                index_timestamps=True,
                index_null_state=True,
                index_property_length=True
            )
        )
        
        return collection
    
    def insert_data(
        self,
        collection_name: str,
        data: List[Dict],
        batch_size: int = 100
    ):
        """Batch Insert Data"""
        
        collection = self.client.collections.get(collection_name)
        
        with collection.batch.dynamic() as batch:
            for item in data:
                batch.add_object(
                    properties={
                        "content": item["content"],
                        "title": item.get("title", ""),
                        "source": item.get("source", ""),
                        "metadata": item.get("metadata", {}),
                        "created_at": item.get("created_at")
                    },
                    uuid=item.get("id"),
                    vector=item.get("vector")  # 可选,如果不提供则自动向量化
                )
        
        return len(data)
    
    def search(
        self,
        collection_name: str,
        query: str,
        top_k: int = 10,
        filters: dict = None,
        alpha: float = 0.5  # 混合搜索权重
    ):
        """Hybrid Search"""
        
        collection = self.client.collections.get(collection_name)
        
        # Build Filter
        filter_obj = None
        if filters:
            filter_obj = self._build_filter(filters)
        
        # Execute Hybrid Search
        response = collection.query.hybrid(
            query=query,
            alpha=alpha,  # 0=纯BM25, 1=纯向量
            limit=top_k,
            filters=filter_obj,
            return_metadata=MetadataQuery(
                score=True,
                explain_score=True
            )
        )
        
        results = []
        for obj in response.objects:
            results.append({
                "id": str(obj.uuid),
                "content": obj.properties.get("content"),
                "title": obj.properties.get("title"),
                "source": obj.properties.get("source"),
                "score": obj.metadata.score,
                "explain_score": obj.metadata.explain_score
            })
        
        return results
    
    def generate_with_context(
        self,
        collection_name: str,
        query: str,
        prompt: str,
        top_k: int = 5
    ):
        """RAG Generation"""
        
        collection = self.client.collections.get(collection_name)
        
        response = collection.generate.near_text(
            query=query,
            limit=top_k,
            single_prompt=prompt,
            grouped_task=f"""
            Based on the following context, answer the question: {query}
            
            Context:
            {{content}}
            
            Answer:
            """
        )
        
        return {
            "generated": response.generated,
            "sources": [
                {
                    "content": obj.properties.get("content"),
                    "source": obj.properties.get("source")
                }
                for obj in response.objects
            ]
        }
    
    def _build_filter(self, filters: dict):
        """Build Filter"""
        conditions = []
        
        for key, value in filters.items():
            if isinstance(value, dict):
                operator = value.get("operator", "equal")
                val = value.get("value")
                
                if operator == "equal":
                    conditions.append(Filter.by_property(key).equal(val))
                elif operator == "greater_than":
                    conditions.append(Filter.by_property(key).greater_than(val))
                elif operator == "less_than":
                    conditions.append(Filter.by_property(key).less_than(val))
                elif operator == "contains":
                    conditions.append(Filter.by_property(key).contains_any(val))
            else:
                conditions.append(Filter.by_property(key).equal(value))
        
        if len(conditions) == 1:
            return conditions[0]
        elif len(conditions) > 1:
            return Filter.all_of(conditions)
        return None
    
    def close(self):
        """Close Connection"""
        self.client.close()
```

---


## 4. Qdrant Deployment

### 4.1 Configuration of Qdrant Cluster

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: qdrant
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: qdrant
  namespace: qdrant
spec:
  serviceName: qdrant-headless
  replicas: 3
  selector:
    matchLabels:
      app: qdrant
  template:
    metadata:
      labels:
        app: qdrant
    spec:
      containers:
      - name: qdrant
        image: qdrant/qdrant:v1.8.1
        
        env:
        - name: QDRANT__CLUSTER__ENABLED
          value: "true"
        - name: QDRANT__CLUSTER__P2P__PORT
          value: "6335"
        - name: QDRANT__SERVICE__GRPC_PORT
          value: "6334"
        - name: QDRANT__SERVICE__HTTP_PORT
          value: "6333"
        - name: QDRANT__STORAGE__STORAGE_PATH
          value: "/qdrant/storage"
        - name: QDRANT__STORAGE__SNAPSHOTS_PATH
          value: "/qdrant/snapshots"
        
        # Performance Configuration
        - name: QDRANT__STORAGE__ON_DISK_PAYLOAD
          value: "true"
        - name: QDRANT__STORAGE__OPTIMIZERS__INDEXING_THRESHOLD
          value: "20000"
        - name: QDRANT__STORAGE__PERFORMANCE__MAX_SEARCH_THREADS
          value: "0"  # 使用所有CPU
        
        # API Key Authentication
        - name: QDRANT__SERVICE__API_KEY
          valueFrom:
            secretKeyRef:
              name: qdrant-secrets
              key: api-key
        
        ports:
        - containerPort: 6333
          name: http
        - containerPort: 6334
          name: grpc
        - containerPort: 6335
          name: p2p
        
        resources:
          requests:
            cpu: "4"
            memory: "16Gi"
          limits:
            cpu: "8"
            memory: "32Gi"
        
        volumeMounts:
        - name: storage
          mountPath: /qdrant/storage
        - name: snapshots
          mountPath: /qdrant/snapshots
        
        livenessProbe:
          httpGet:
            path: /
            port: 6333
          initialDelaySeconds: 30
          periodSeconds: 30
        
        readinessProbe:
          httpGet:
            path: /readyz
            port: 6333
          initialDelaySeconds: 10
          periodSeconds: 10
  
  volumeClaimTemplates:
  - metadata:
      name: storage
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: fast-ssd
      resources:
        requests:
          storage: 500Gi
  - metadata:
      name: snapshots
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: standard
      resources:
        requests:
          storage: 100Gi
---
apiVersion: v1
kind: Service
metadata:
  name: qdrant
  namespace: qdrant
spec:
  type: LoadBalancer
  ports:
  - port: 6333
    targetPort: 6333
    name: http
  - port: 6334
    targetPort: 6334
    name: grpc
  selector:
    app: qdrant
```

### 4.2 Qdrant Python Client

```python
# qdrant_client.py - Qdrant Operations
from qdrant_client import QdrantClient, models
from typing import List, Dict, Optional
import uuid

class QdrantManager:
    """Qdrant Manager"""
    
    def __init__(
        self,
        url: str = "http://qdrant.qdrant:6333",
        api_key: str = None
    ):
        self.client = QdrantClient(
            url=url,
            api_key=api_key,
            prefer_grpc=True
        )
    
    def create_collection(
        self,
        name: str,
        vector_size: int = 1024,
        distance: str = "Cosine",
        on_disk: bool = False,
        quantization: str = None,  # "scalar", "product", "binary"
        replication_factor: int = 2,
        shard_number: int = 4
    ):
        """Create Collection"""
        
        # Quantized Configuration
        quantization_config = None
        if quantization == "scalar":
            quantization_config = models.ScalarQuantization(
                scalar=models.ScalarQuantizationConfig(
                    type=models.ScalarType.INT8,
                    quantile=0.99,
                    always_ram=True
                )
            )
        elif quantization == "product":
            quantization_config = models.ProductQuantization(
                product=models.ProductQuantizationConfig(
                    compression=models.CompressionRatio.X16,
                    always_ram=True
                )
            )
        elif quantization == "binary":
            quantization_config = models.BinaryQuantization(
                binary=models.BinaryQuantizationConfig(
                    always_ram=True
                )
            )
        
        # Quantization Configuration
        self.client.create_collection(
            collection_name=name,
            vectors_config=models.VectorParams(
                size=vector_size,
                distance=getattr(models.Distance, distance.upper()),
                on_disk=on_disk
            ),
            hnsw_config=models.HnswConfigDiff(
                m=16,
                ef_construct=256,
                full_scan_threshold=10000,
                on_disk=on_disk
            ),
            optimizers_config=models.OptimizersConfigDiff(
                indexing_threshold=20000,
                memmap_threshold=50000
            ),
            quantization_config=quantization_config,
            replication_factor=replication_factor,
            shard_number=shard_number
        )
        
        # Create Collection
        self.client.create_payload_index(
            collection_name=name,
            field_name="source",
            field_schema=models.PayloadSchemaType.KEYWORD
        )
        self.client.create_payload_index(
            collection_name=name,
            field_name="created_at",
            field_schema=models.PayloadSchemaType.INTEGER
        )
        
        return True
    
    def upsert(
        self,
        collection_name: str,
        vectors: List[List[float]],
        payloads: List[Dict],
        ids: List[str] = None,
        batch_size: int = 100
    ):
        """Batch Update/Insert"""
        
        if ids is None:
            ids = [str(uuid.uuid4()) for _ in range(len(vectors))]
        
        points = [
            models.PointStruct(
                id=ids[i],
                vector=vectors[i],
                payload=payloads[i]
            )
            for i in range(len(vectors))
        ]
        
        # Batch Upload
        for i in range(0, len(points), batch_size):
            batch = points[i:i + batch_size]
            self.client.upsert(
                collection_name=collection_name,
                points=batch,
                wait=True
            )
        
        return len(points)
    
    def search(
        self,
        collection_name: str,
        query_vector: List[float],
        top_k: int = 10,
        filter_conditions: Dict = None,
        score_threshold: float = None
    ):
        """Vector Search"""
        
        # Build Filter
        query_filter = None
        if filter_conditions:
            must_conditions = []
            for key, value in filter_conditions.items():
                if isinstance(value, dict):
                    if "gte" in value:
                        must_conditions.append(
                            models.FieldCondition(
                                key=key,
                                range=models.Range(gte=value["gte"])
                            )
                        )
                    if "lte" in value:
                        must_conditions.append(
                            models.FieldCondition(
                                key=key,
                                range=models.Range(lte=value["lte"])
                            )
                        )
                else:
                    must_conditions.append(
                        models.FieldCondition(
                            key=key,
                            match=models.MatchValue(value=value)
                        )
                    )
            
            if must_conditions:
                query_filter = models.Filter(must=must_conditions)
        
        results = self.client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            limit=top_k,
            query_filter=query_filter,
            score_threshold=score_threshold,
            with_payload=True,
            with_vectors=False
        )
        
        return [
            {
                "id": str(hit.id),
                "score": hit.score,
                "payload": hit.payload
            }
            for hit in results
        ]
    
    def recommend(
        self,
        collection_name: str,
        positive_ids: List[str],
        negative_ids: List[str] = None,
        top_k: int = 10,
        filter_conditions: Dict = None
    ):
        """Recommended Search (based on Positive and Negative Samples)"""
        
        results = self.client.recommend(
            collection_name=collection_name,
            positive=positive_ids,
            negative=negative_ids or [],
            limit=top_k,
            with_payload=True
        )
        
        return [
            {
                "id": str(hit.id),
                "score": hit.score,
                "payload": hit.payload
            }
            for hit in results
        ]
```

---


## 5. Implementation of RAG Pipeline

### 5.1 Complete RAG Pipeline

```python
# rag_pipeline.py - Production-Level RAG Pipeline
from typing import List, Dict, Optional, AsyncIterator
import asyncio
from dataclasses import dataclass
from enum import Enum
import hashlib
import json

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from sentence_transformers import CrossEncoder
import tiktoken

class SearchStrategy(Enum):
    """Search Strategy"""
    VECTOR = "vector"
    HYBRID = "hybrid"
    MULTI_QUERY = "multi_query"
    HYDE = "hyde"

@dataclass
class Document:
    """Document Object"""
    id: str
    content: str
    metadata: Dict
    embedding: Optional[List[float]] = None
    score: float = 0.0

@dataclass
class RAGResponse:
    """RAG Response"""
    answer: str
    sources: List[Document]
    confidence: float
    tokens_used: int

class RAGPipeline:
    """Production-Level RAG Pipeline"""
    
    def __init__(
        self,
        vector_db,  # Milvus/Weaviate/Qdrant客户端
        llm_client,  # vLLM/TGI客户端
        embedding_model: str = "BAAI/bge-large-zh-v1.5",
        reranker_model: str = "BAAI/bge-reranker-large",
        chunk_size: int = 512,
        chunk_overlap: int = 50,
    ):
        self.vector_db = vector_db
        self.llm_client = llm_client
        
        # Initialize Embedding Model
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=embedding_model,
            model_kwargs={'device': 'cuda'},
            encode_kwargs={'normalize_embeddings': True}
        )
        
        # Initialize Reranker
        self.reranker = CrossEncoder(
            reranker_model,
            device='cuda'
        )
        
        # Text Splitter
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=["\n\n", "\n", ".", "!", "?", ".", "!", "?", " "]
        )
        
        # Token Counter
        self.tokenizer = tiktoken.get_encoding("cl100k_base")
    
    async def ingest_documents(
        self,
        documents: List[Dict],
        collection_name: str,
        batch_size: int = 100
    ):
        """Document Ingestion"""
        
        all_chunks = []
        
        for doc in documents:
            # Chunking
            chunks = self.text_splitter.split_text(doc["content"])
            
            for i, chunk in enumerate(chunks):
                chunk_id = hashlib.md5(
                    f"{doc['id']}_{i}".encode()
                ).hexdigest()
                
                all_chunks.append({
                    "id": chunk_id,
                    "content": chunk,
                    "metadata": {
                        **doc.get("metadata", {}),
                        "source_id": doc["id"],
                        "chunk_index": i,
                        "total_chunks": len(chunks)
                    }
                })
        
        # Batch Generation of Embeddings
        embeddings = await self._batch_embed(
            [c["content"] for c in all_chunks],
            batch_size
        )
        
        # Add embedding to chunks
        for i, chunk in enumerate(all_chunks):
            chunk["embedding"] = embeddings[i]
        
        # Insert into Vector Database
        await self._batch_insert(collection_name, all_chunks, batch_size)
        
        return len(all_chunks)
    
    async def query(
        self,
        question: str,
        collection_name: str,
        strategy: SearchStrategy = SearchStrategy.HYBRID,
        top_k: int = 10,
        rerank_top_k: int = 5,
        filter_conditions: Dict = None,
        stream: bool = False
    ) -> RAGResponse:
        """RAG Query"""
        
        # Step 1: Query Rewrite/Expansion
        enhanced_queries = await self._enhance_query(question, strategy)
        
        # Step 2: Retrieval
        candidates = await self._retrieve(
            enhanced_queries,
            collection_name,
            top_k,
            filter_conditions,
            strategy
        )
        
        # Step 3: Reordering
        reranked_docs = await self._rerank(
            question,
            candidates,
            rerank_top_k
        )
        
        # Step 4: Context Construction
        context = self._build_context(reranked_docs)
        
        # Step 5: Generate an answer
        if stream:
            return self._generate_stream(question, context, reranked_docs)
        else:
            answer, tokens = await self._generate(question, context)
            
            # Calculate confidence
            confidence = self._calculate_confidence(reranked_docs)
            
            return RAGResponse(
                answer=answer,
                sources=reranked_docs,
                confidence=confidence,
                tokens_used=tokens
            )
    
    async def _enhance_query(
        self,
        question: str,
        strategy: SearchStrategy
    ) -> List[str]:
        """Query Enhancement"""
        
        if strategy == SearchStrategy.MULTI_QUERY:
            # Generate multiple query variants
            prompt = f"""Given the question: "{question}"
            
Generate 3 different search queries that would help find relevant information.
Output only the queries, one per line."""
            
            response = await self.llm_client.generate(prompt, max_tokens=200)
            queries = [question] + response.strip().split("\n")
            return queries[:4]
        
        elif strategy == SearchStrategy.HYDE:
            # Generate hypothetical answers
            prompt = f"""Question: {question}

Write a detailed answer to this question as if you were an expert. 
This will be used to search for similar content."""
            
            hypothetical_answer = await self.llm_client.generate(
                prompt, max_tokens=300
            )
            return [question, hypothetical_answer]
        
        return [question]
    
    async def _retrieve(
        self,
        queries: List[str],
        collection_name: str,
        top_k: int,
        filter_conditions: Dict,
        strategy: SearchStrategy
    ) -> List[Document]:
        """Retrieve Documents"""
        
        all_results = {}
        
        for query in queries:
            # Generate query vectors
            query_embedding = self.embedding_model.embed_query(query)
            
            if strategy == SearchStrategy.HYBRID:
                # Hybrid search
                results = await self.vector_db.hybrid_search(
                    collection_name,
                    query_embedding,
                    query,
                    top_k,
                    filter_conditions
                )
            else:
                # Pure vector search
                results = await self.vector_db.search(
                    collection_name,
                    query_embedding,
                    top_k,
                    filter_conditions
                )
            
            # Merge results, retain highest score
            for r in results:
                doc_id = r["id"]
                if doc_id not in all_results or r["score"] > all_results[doc_id].score:
                    all_results[doc_id] = Document(
                        id=doc_id,
                        content=r["content"],
                        metadata=r.get("metadata", {}),
                        score=r["score"]
                    )
        
        # Sort by score
        sorted_results = sorted(
            all_results.values(),
            key=lambda x: x.score,
            reverse=True
        )
        
        return sorted_results[:top_k * 2]  # 返回更多给reranker
    
    async def _rerank(
        self,
        question: str,
        documents: List[Document],
        top_k: int
    ) -> List[Document]:
        """Reorder"""
        
        if not documents:
            return []
        
        # Prepare input pairs
        pairs = [(question, doc.content) for doc in documents]
        
        # Calculate reorder scores
        scores = self.reranker.predict(pairs)
        
        # Update scores
        for i, doc in enumerate(documents):
            doc.score = float(scores[i])
        
        # Sort and return top_k
        reranked = sorted(documents, key=lambda x: x.score, reverse=True)
        return reranked[:top_k]
    
    def _build_context(
        self,
        documents: List[Document],
        max_tokens: int = 4000
    ) -> str:
        """Build Context"""
        
        context_parts = []
        total_tokens = 0
        
        for i, doc in enumerate(documents):
            doc_text = f"[{i+1}] {doc.content}"
            doc_tokens = len(self.tokenizer.encode(doc_text))
            
            if total_tokens + doc_tokens > max_tokens:
                break
            
            context_parts.append(doc_text)
            total_tokens += doc_tokens
        
        return "\n\n".join(context_parts)
    
    async def _generate(
        self,
        question: str,
        context: str
    ) -> tuple:
        """Generate Answer"""
        
        prompt = f"""Based on the following context, answer the question accurately and concisely.
If the context doesn't contain enough information, say so.
Always cite the source numbers [1], [2], etc. when using information from the context.

Context:
{context}

Question: {question}

Answer:"""
        
        response = await self.llm_client.generate(
            prompt,
            max_tokens=1024,
            temperature=0.1
        )
        
        tokens = len(self.tokenizer.encode(prompt + response))
        
        return response, tokens
    
    async def _generate_stream(
        self,
        question: str,
        context: str,
        sources: List[Document]
    ) -> AsyncIterator[str]:
        """Stream Generation"""
        
        prompt = f"""Based on the following context, answer the question.

Context:
{context}

Question: {question}

Answer:"""
        
        async for chunk in self.llm_client.generate_stream(
            prompt,
            max_tokens=1024,
            temperature=0.1
        ):
            yield chunk
    
    def _calculate_confidence(self, documents: List[Document]) -> float:
        """Calculate confidence"""
        
        if not documents:
            return 0.0
        
        # Calculate ranking score based on permutation
        avg_score = sum(doc.score for doc in documents) / len(documents)
        top_score = documents[0].score if documents else 0
        
        # Combine confidence
        confidence = (avg_score * 0.4 + top_score * 0.6)
        return min(max(confidence, 0.0), 1.0)
    
    async def _batch_embed(
        self,
        texts: List[str],
        batch_size: int
    ) -> List[List[float]]:
        """Batch generate Embedding"""
        
        embeddings = []
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            batch_embeddings = self.embedding_model.embed_documents(batch)
            embeddings.extend(batch_embeddings)
        
        return embeddings
    
    async def _batch_insert(
        self,
        collection_name: str,
        chunks: List[Dict],
        batch_size: int
    ):
        """Batch insert"""
        
        for i in range(0, len(chunks), batch_size):
            batch = chunks[i:i + batch_size]
            await self.vector_db.insert(collection_name, batch)
```

### 5.2 Advanced Search Strategies

```python
# advanced_retrieval.py - Advanced search strategies
from typing import List, Dict, Optional
import numpy as np
from collections import defaultdict

class AdvancedRetriever:
    """Advanced retriever"""
    
    def __init__(self, vector_db, embedding_model, llm_client):
        self.vector_db = vector_db
        self.embedding_model = embedding_model
        self.llm_client = llm_client
    
    async def parent_document_retrieval(
        self,
        query: str,
        collection_name: str,
        top_k: int = 5
    ) -> List[Dict]:
        """Parent document retrieval - Retrieve small chunks, return large blocks"""
        
        # Search small chunks
        query_embedding = self.embedding_model.embed_query(query)
        small_chunks = await self.vector_db.search(
            collection_name + "_small",
            query_embedding,
            top_k * 3
        )
        
        # Get corresponding parent document ID
        parent_ids = set()
        for chunk in small_chunks:
            parent_id = chunk["metadata"].get("parent_id")
            if parent_id:
                parent_ids.add(parent_id)
        
        # Retrieve parent document
        parent_docs = await self.vector_db.get_by_ids(
            collection_name + "_large",
            list(parent_ids)[:top_k]
        )
        
        return parent_docs
    
    async def self_query_retrieval(
        self,
        query: str,
        collection_name: str,
        top_k: int = 5
    ) -> List[Dict]:
        """Self-query retrieval - Parse query with LLM to generate filter conditions"""
        
        # Use LLM to parse query
        parse_prompt = f"""Parse the following query into search parameters.

Query: "{query}"

Output JSON with:
- search_query: the main search text
- filters: metadata filters (e.g., date, category, author)

Example output:
{{"search_query": "machine learning", "filters": {{"category": "technology", "year_gte": 2023}}}}

Output:"""
        
        parsed = await self.llm_client.generate(parse_prompt, max_tokens=200)
        
        try:
            params = json.loads(parsed)
            search_query = params.get("search_query", query)
            filters = params.get("filters", {})
        except:
            search_query = query
            filters = {}
        
        # Execute filtered search
        query_embedding = self.embedding_model.embed_query(search_query)
        results = await self.vector_db.search(
            collection_name,
            query_embedding,
            top_k,
            filter_conditions=filters
        )
        
        return results
    
    async def contextual_compression(
        self,
        query: str,
        documents: List[Dict],
        max_length: int = 500
    ) -> List[Dict]:
        """Context compression - Extract parts related to the query"""
        
        compressed = []
        
        for doc in documents:
            prompt = f"""Extract only the parts of the following text that are relevant to the query.
If no parts are relevant, output "NOT_RELEVANT".

Query: {query}

Text: {doc["content"]}

Relevant extract:"""
            
            extract = await self.llm_client.generate(
                prompt,
                max_tokens=max_length
            )
            
            if extract.strip() != "NOT_RELEVANT":
                compressed.append({
                    **doc,
                    "content": extract,
                    "original_content": doc["content"]
                })
        
        return compressed
    
    async def ensemble_retrieval(
        self,
        query: str,
        collection_name: str,
        top_k: int = 10,
        weights: Dict[str, float] = None
    ) -> List[Dict]:
        """Integration retrieval - Fusion of multiple strategies"""
        
        if weights is None:
            weights = {
                "vector": 0.4,
                "bm25": 0.3,
                "multi_query": 0.3
            }
        
        all_results = defaultdict(lambda: {"score": 0, "doc": None})
        
        # Vector retrieval
        query_embedding = self.embedding_model.embed_query(query)
        vector_results = await self.vector_db.search(
            collection_name,
            query_embedding,
            top_k * 2
        )
        
        for r in vector_results:
            all_results[r["id"]]["score"] += r["score"] * weights["vector"]
            all_results[r["id"]]["doc"] = r
        
        # BM25 retrieval (if supported)
        if hasattr(self.vector_db, "bm25_search"):
            bm25_results = await self.vector_db.bm25_search(
                collection_name,
                query,
                top_k * 2
            )
            
            for r in bm25_results:
                all_results[r["id"]]["score"] += r["score"] * weights["bm25"]
                if all_results[r["id"]]["doc"] is None:
                    all_results[r["id"]]["doc"] = r
        
        # Multi-query retrieval
        multi_queries = await self._generate_multi_queries(query)
        for mq in multi_queries:
            mq_embedding = self.embedding_model.embed_query(mq)
            mq_results = await self.vector_db.search(
                collection_name,
                mq_embedding,
                top_k
            )
            
            for r in mq_results:
                all_results[r["id"]]["score"] += (
                    r["score"] * weights["multi_query"] / len(multi_queries)
                )
                if all_results[r["id"]]["doc"] is None:
                    all_results[r["id"]]["doc"] = r
        
        # Merge sort
        sorted_results = sorted(
            [{"id": k, "score": v["score"], **v["doc"]} 
             for k, v in all_results.items() if v["doc"]],
            key=lambda x: x["score"],
            reverse=True
        )
        
        return sorted_results[:top_k]
    
    async def mmr_retrieval(
        self,
        query: str,
        collection_name: str,
        top_k: int = 10,
        lambda_mult: float = 0.5
    ) -> List[Dict]:
        """MMR (Maximal Marginal Relevance) - Diversified retrieval"""
        
        # Get more candidates
        query_embedding = self.embedding_model.embed_query(query)
        candidates = await self.vector_db.search(
            collection_name,
            query_embedding,
            top_k * 4
        )
        
        if not candidates:
            return []
        
        # Get candidate vector
        candidate_embeddings = np.array([
            c.get("embedding", self.embedding_model.embed_query(c["content"]))
            for c in candidates
        ])
        query_embedding = np.array(query_embedding)
        
        # MMR selection
        selected = []
        selected_indices = set()
        
        for _ in range(min(top_k, len(candidates))):
            best_score = -float("inf")
            best_idx = -1
            
            for i, candidate in enumerate(candidates):
                if i in selected_indices:
                    continue
                
                # Relevance score
                relevance = np.dot(query_embedding, candidate_embeddings[i])
                
                # Diversity score
                diversity = 0
                if selected:
                    similarities = [
                        np.dot(candidate_embeddings[i], candidate_embeddings[j])
                        for j in selected_indices
                    ]
                    diversity = max(similarities)
                
                # MMR score
                mmr_score = lambda_mult * relevance - (1 - lambda_mult) * diversity
                
                if mmr_score > best_score:
                    best_score = mmr_score
                    best_idx = i
            
            if best_idx >= 0:
                selected.append(candidates[best_idx])
                selected_indices.add(best_idx)
        
        return selected
    
    async def _generate_multi_queries(self, query: str) -> List[str]:
        """Generate multiple query variants"""
        
        prompt = f"""Generate 3 different ways to ask this question:
"{query}"

Output only the questions, one per line."""
        
        response = await self.llm_client.generate(prompt, max_tokens=200)
        queries = response.strip().split("\n")
        return [q.strip() for q in queries if q.strip()][:3]
```

---


## 6. Embedding Service Deployment

### 6.1 TEI (Text Embeddings Inference) Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tei-bge-large
  namespace: rag
spec:
  replicas: 4
  selector:
    matchLabels:
      app: tei
  template:
    metadata:
      labels:
        app: tei
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "80"
    spec:
      containers:
      - name: tei
        image: ghcr.io/huggingface/text-embeddings-inference:1.2
        
        args:
        - --model-id=BAAI/bge-large-zh-v1.5
        - --port=80
        - --max-concurrent-requests=512
        - --max-batch-tokens=16384
        - --max-client-batch-size=32
        
        env:
        - name: HUGGING_FACE_HUB_TOKEN
          valueFrom:
            secretKeyRef:
              name: hf-secrets
              key: token
        
        ports:
        - containerPort: 80
          name: http
        
        resources:
          requests:
            cpu: "2"
            memory: "4Gi"
            nvidia.com/gpu: "1"
          limits:
            cpu: "4"
            memory: "8Gi"
            nvidia.com/gpu: "1"
        
        livenessProbe:
          httpGet:
            path: /health
            port: 80
          initialDelaySeconds: 60
          periodSeconds: 30
        
        readinessProbe:
          httpGet:
            path: /health
            port: 80
          initialDelaySeconds: 30
          periodSeconds: 10
---
apiVersion: v1
kind: Service
metadata:
  name: tei-service
  namespace: rag
spec:
  ports:
  - port: 80
    targetPort: 80
  selector:
    app: tei
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: tei-hpa
  namespace: rag
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: tei-bge-large
  minReplicas: 2
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Pods
    pods:
      metric:
        name: http_requests_per_second
      target:
        type: AverageValue
        averageValue: "100"
```

### 6.2 Reranker Service Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: reranker-service
  namespace: rag
spec:
  replicas: 2
  selector:
    matchLabels:
      app: reranker
  template:
    metadata:
      labels:
        app: reranker
    spec:
      containers:
      - name: reranker
        image: ghcr.io/huggingface/text-embeddings-inference:1.2
        
        args:
        - --model-id=BAAI/bge-reranker-v2-m3
        - --port=80
        - --max-concurrent-requests=128
        
        resources:
          requests:
            nvidia.com/gpu: "1"
          limits:
            nvidia.com/gpu: "1"
        
        ports:
        - containerPort: 80
---
apiVersion: v1
kind: Service
metadata:
  name: reranker-service
  namespace: rag
spec:
  ports:
  - port: 80
    targetPort: 80
  selector:
    app: reranker
```

---


## 7. Monitoring and Observability

### 7.1 RAG System Monitoring

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: rag-system-alerts
  namespace: rag
spec:
  groups:
  - name: rag-quality
    rules:
    # Retrieval quality metrics
    - record: rag:retrieval_recall
      expr: |
        sum(rag_retrieval_relevant_docs) / sum(rag_retrieval_total_relevant)
    
    - record: rag:retrieval_precision
      expr: |
        sum(rag_retrieval_relevant_docs) / sum(rag_retrieval_returned_docs)
    
    # Response quality alert
    - alert: RAGLowRetrievalRecall
      expr: rag:retrieval_recall < 0.7
      for: 30m
      labels:
        severity: warning
      annotations:
        summary: "RAG retrieval recall rate is low"
        description: "Recall rate {{ $value | humanizePercentage }}"
    
    # Latency alert
    - alert: RAGHighLatency
      expr: |
        histogram_quantile(0.99, sum(rate(rag_query_duration_seconds_bucket[5m])) by (le)) > 5
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "RAG query latency is too high"
        description: "P99 latency {{ $value }} seconds"
    
    # Embedding service alert
    - alert: EmbeddingServiceDown
      expr: up{job="tei-service"} == 0
      for: 2m
      labels:
        severity: critical
      annotations:
        summary: "Embedding service is unavailable"
  
  - name: rag-performance
    rules:
    # QPS
    - record: rag:query_qps
      expr: sum(rate(rag_query_total[5m]))
    
    # Latency percentile
    - record: rag:query_latency_p50
      expr: |
        histogram_quantile(0.50, sum(rate(rag_query_duration_seconds_bucket[5m])) by (le))
    
    - record: rag:query_latency_p95
      expr: |
        histogram_quantile(0.95, sum(rate(rag_query_duration_seconds_bucket[5m])) by (le))
    
    # Token usage
    - record: rag:tokens_per_query
      expr: |
        sum(rate(rag_tokens_used_total[5m])) / sum(rate(rag_query_total[5m]))
```

### 7.2 RAG Evaluation Metrics

```python
# rag_evaluation.py - RAG evaluation
from typing import List, Dict
import numpy as np
from dataclasses import dataclass

@dataclass
class RAGMetrics:
    """RAG evaluation metrics"""
    # Retrieval metrics
    recall_at_k: float
    precision_at_k: float
    mrr: float  # Mean Reciprocal Rank
    ndcg: float  # Normalized Discounted Cumulative Gain
    
    # Generation metrics
    faithfulness: float  # 答案是否基于上下文
    relevance: float  # 答案与问题的相关性
    coherence: float  # 答案的连贯性
    
    # System metrics
    latency_p50: float
    latency_p99: float
    tokens_used: int

class RAGEvaluator:
    """RAG evaluator"""
    
    def __init__(self, llm_client):
        self.llm_client = llm_client
    
    def evaluate_retrieval(
        self,
        retrieved_docs: List[str],
        relevant_docs: List[str],
        k: int = 5
    ) -> Dict[str, float]:
        """Evaluate retrieval quality"""
        
        retrieved_set = set(retrieved_docs[:k])
        relevant_set = set(relevant_docs)
        
        # Recall@K
        recall = len(retrieved_set & relevant_set) / len(relevant_set) if relevant_set else 0
        
        # Precision@K
        precision = len(retrieved_set & relevant_set) / k
        
        # MRR
        mrr = 0
        for i, doc in enumerate(retrieved_docs):
            if doc in relevant_set:
                mrr = 1 / (i + 1)
                break
        
        # NDCG
        dcg = sum(
            (1 if doc in relevant_set else 0) / np.log2(i + 2)
            for i, doc in enumerate(retrieved_docs[:k])
        )
        idcg = sum(1 / np.log2(i + 2) for i in range(min(k, len(relevant_set))))
        ndcg = dcg / idcg if idcg > 0 else 0
        
        return {
            "recall_at_k": recall,
            "precision_at_k": precision,
            "mrr": mrr,
            "ndcg": ndcg
        }
    
    async def evaluate_generation(
        self,
        question: str,
        answer: str,
        context: str
    ) -> Dict[str, float]:
        """Evaluate generation quality"""
        
        # Fidelity evaluation
        faithfulness_prompt = f"""Rate how faithful the answer is to the provided context.
Score from 0-1, where 1 means the answer only contains information from the context.

Context: {context}
Answer: {answer}

Score (0-1):"""
        
        faithfulness = await self._get_score(faithfulness_prompt)
        
        # Relevance evaluation
        relevance_prompt = f"""Rate how relevant the answer is to the question.
Score from 0-1, where 1 means the answer directly addresses the question.

Question: {question}
Answer: {answer}

Score (0-1):"""
        
        relevance = await self._get_score(relevance_prompt)
        
        # Coherence evaluation
        coherence_prompt = f"""Rate the coherence and clarity of the answer.
Score from 0-1, where 1 means the answer is clear, well-structured, and easy to understand.

Answer: {answer}

Score (0-1):"""
        
        coherence = await self._get_score(coherence_prompt)
        
        return {
            "faithfulness": faithfulness,
            "relevance": relevance,
            "coherence": coherence
        }
    
    async def _get_score(self, prompt: str) -> float:
        """Get score"""
        response = await self.llm_client.generate(prompt, max_tokens=10)
        try:
            score = float(response.strip())
            return min(max(score, 0), 1)
        except:
            return 0.5
```

---


## 8. Performance Optimization

### 8.1 Performance Optimization Strategies

| Improvement Item | Method | Effect | Applicable Scenario |
|--------|------|------|---------|
| Index Optimization | HNSW parameter tuning (M=32, ef=256) | Recall+5%, Delay+10% | High precision requirement |
| Quantized Index | Scalar/Product Quantization | Memory-50%, Delay+20% | Large-scale data |
| Batch Requests | Batch embedding/search | Throughput+5x | Batch processing scenario |
| Cache | Redis cache hot queries | Hit rate 30%+, Delay-80% | Many repeated queries |
| Pre-computation | Warm index to memory | First delay-90% | Cold start optimization |
| Sharding | Shard by time/topic | Single shard query delay-50% | Large data volume |
| GPU Acceleration | GPU index build/search | Throughput+10x | High concurrency |

### 8.2 Caching Strategies

```python
# rag_cache.py - RAG cache
import redis
import hashlib
import json
from typing import Optional, List, Dict

class RAGCache:
    """RAG cache management"""
    
    def __init__(
        self,
        redis_url: str = "redis://redis:6379",
        embedding_ttl: int = 86400,  # 1天
        result_ttl: int = 3600,  # 1小时
    ):
        self.redis = redis.from_url(redis_url)
        self.embedding_ttl = embedding_ttl
        self.result_ttl = result_ttl
    
    def _hash_key(self, text: str) -> str:
        """Generate cache key"""
        return hashlib.md5(text.encode()).hexdigest()
    
    async def get_embedding(self, text: str) -> Optional[List[float]]:
        """Get cache embedding"""
        key = f"emb:{self._hash_key(text)}"
        cached = self.redis.get(key)
        if cached:
            return json.loads(cached)
        return None
    
    async def set_embedding(self, text: str, embedding: List[float]):
        """Cache embedding"""
        key = f"emb:{self._hash_key(text)}"
        self.redis.setex(key, self.embedding_ttl, json.dumps(embedding))
    
    async def get_search_result(
        self,
        query: str,
        collection: str,
        top_k: int
    ) -> Optional[List[Dict]]:
        """Get cache search results"""
        key = f"search:{collection}:{top_k}:{self._hash_key(query)}"
        cached = self.redis.get(key)
        if cached:
            return json.loads(cached)
        return None
    
    async def set_search_result(
        self,
        query: str,
        collection: str,
        top_k: int,
        results: List[Dict]
    ):
        """Cache search results"""
        key = f"search:{collection}:{top_k}:{self._hash_key(query)}"
        self.redis.setex(key, self.result_ttl, json.dumps(results))
    
    async def get_rag_response(
        self,
        query: str,
        collection: str
    ) -> Optional[Dict]:
        """Get cache RAG response"""
        key = f"rag:{collection}:{self._hash_key(query)}"
        cached = self.redis.get(key)
        if cached:
            return json.loads(cached)
        return None
    
    async def set_rag_response(
        self,
        query: str,
        collection: str,
        response: Dict
    ):
        """Cache RAG response"""
        key = f"rag:{collection}:{self._hash_key(query)}"
        self.redis.setex(key, self.result_ttl, json.dumps(response))
    
    def invalidate_collection(self, collection: str):
        """clear the cache of a certain collection"""
        pattern = f"*:{collection}:*"
        keys = self.redis.keys(pattern)
        if keys:
            self.redis.delete(*keys)
```

---


## 9. Quick Reference

### 9.1 Vector Database Selection

| Requirement | Recommended Solution | Reason |
|-----|---------|------|
| Production Scale (>100 million vectors) | Milvus | Distributed, GPU acceleration, high availability |
| Enterprise Features | Weaviate | GraphQL, modular, easy integration |
| High Performance Rust | Qdrant | Low latency, high throughput, lightweight |
| Zero Maintenance | Pinecone | Fully managed, no maintenance |
| Quick Prototype | Chroma | Simple, local run |
| Existing PG Users | pgvector | No need for new infrastructure |

### 9.2 Embedding Model Selection

| Scenario | Recommended Model | Dimension | Note |
|-----|---------|------|------|
| General English | text-embedding-3-small | 1536 | OpenAI, high quality |
| General Chinese | BGE-large-zh-v1.5 | 1024 | Open-source best |
| Multilingual | Cohere embed-v3 | 1024 | 100+ languages |
| Long Text | Jina-embeddings-v2 | 768 | 8K Context |
| Cost-sensitive | E5-small-v2 | 384 | Small Model |

### 9.3 Common APIs

```python
# Milvus
from pymilvus import Collection
collection = Collection("my_collection")
results = collection.search(vectors, "embedding", {"metric_type": "COSINE"}, limit=10)

# Weaviate
client.query.get("Document", ["content"]).with_near_text({"concepts": ["query"]}).with_limit(10).do()

# Qdrant
client.search(collection_name="my_collection", query_vector=vector, limit=10)

# LangChain
from langchain.vectorstores import Milvus
vectorstore = Milvus.from_documents(docs, embedding, connection_args={"host": "localhost"})
results = vectorstore.similarity_search(query, k=10)
```

---


## 10. Best Practices

### RAG System Checklist

- [ ] **Data Preparation**: Clean, chunk, deduplicate
- [ ] **Embedding Selection**: Choose model based on language and scenario
- [ ] **Vector Database**: Choose based on scale and need
- [ ] **Index Configuration**: Optimize HNSW parameters
- [ ] **Retrieval Strategy**: Hybrid search, reordering
- [ ] **Prompt Engineering**: Optimize RAG prompt templates
- [ ] **Caching Strategy**: Cache hot queries
- [ ] **Monitoring Alerts**: Latency, recall rate, error rate
- [ ] **Evaluation System**: Regularly evaluate retrieval and generation quality
- [ ] **Iterative Optimization**: Continuously improve based on user feedback

---

**Related Documentation**: [144-LLM Inference Serving](144-llm-inference-serving.md) | [142-LLM Data Pipeline](142-llm-data-pipeline.md) | [132-AI/ML Workloads](132-ai-ml-workloads.md)

**Version**: Milvus 2.3+ | Weaviate 1.24+ | Qdrant 1.8+ | LangChain 0.1+

---


## Obsidian Related Documentation

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Open Source Project Index
- AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry Center and Version Management

## See Also

- 18-llm-serving-architecture
- 19-llm-quantization
- 21-multimodal-models
- 22-llm-privacy-security

## Related

- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Knowledge Graph Index]]


<!-- risk-assessed -->
