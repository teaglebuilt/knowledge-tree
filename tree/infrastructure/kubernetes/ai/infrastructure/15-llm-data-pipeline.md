---
title: 142 - LLM Training Data Pipeline and Management
description: '# 142 - LLM Training Data Pipeline and Management'
summary: 'csi.storage.k8s.io/provisioner-secret-name: juicefs-secret'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- prometheus
- opa
- redis
- job
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
- What is LLM Training Data Pipeline and Management
- How to manage LLM Training Data Pipeline and Management
- Kubernetes 11 ai infra best practices
trigger_keywords:
- LLM Training Data Pipeline and Management
- LLM
- Data
- Pipeline
- Management
- ai
- infra
prerequisites:
- kubectl-basics
- prometheus-basics
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
source_path: tree/infrastructure/kubernetes/ai/infrastructure/15-llm-data-pipeline.md
---

> **Production Environment Security Tips**
>
> This document contains executable operational commands. Please confirm before execution: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether these commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information collection with no side effects).




# 142 - LLM training data Pipeline and Management (LLM Data Pipeline & Management)

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25-v1.32 | **Last Updated**: 2026-01 | **Reference**: [Ray Data](https://docs.ray.io/en/latest/data/data.html)

---


## 1. LLM Data Pipeline Architecture (Pipeline Architecture)

### 1.1 End-to-End Data Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LLM Training Data Pipeline Architecture                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                     Data Collection Layer (Data Collection)                       │ │
│  │  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐    │ │
│  │  │ Web Crawling │  │ API Fetching │  │ Database  │  │ Document Import│  │ User Data│    │ │
│  │  │ Scrapy  │  │ Requests│  │ Export  │  │ Unstructured │ Feedback│    │ │
│  │  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘  └────┬────┘    │ │
│  └───────┴────────────┴────────────┴────────────┴────────────┴──────────┘ │
│                                    │                                        │
│                                    ▼                                        │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                     Data Cleaning Layer (Data Cleaning)                         │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │ │
│  │  │ Deduplication        │  │ Quality Filtering    │  │ PII De-identification     │  │ Format Standardization  │  │ │
│  │  │ MinHash/LSH │  │ FastText    │  │ Presidio    │  │ JSON/Parquet│  │ │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘  │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                    │                                        │
│                                    ▼                                        │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                     Data Processing Layer (Data Processing)                       │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │ │
│  │  │ Tokenization│  │ Data Balancing    │  │ Data Augmentation    │  │ Sequence Packing    │  │ │
│  │  │ HF/SentenceP│  │ Mix Ratio   │  │ Augmentation│  │ Packing     │  │ │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘  │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                    │                                        │
│                                    ▼                                        │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                     Data Storage Layer (Data Storage)                          │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │ │
│  │  │ Object Storage    │  │ Distributed Caching  │  │ Vector Database  │  │ Metadata Management  │  │ │
│  │  │ S3/OSS/GCS  │  │ Alluxio     │  │ Milvus      │  │ MLflow      │  │ │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘  │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                    │                                        │
│                                    ▼                                        │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                     Data Loading Layer (Data Loading)                          │ │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  │ │
│  │  │ DataLoader  │  │ Prefetch Buffer    │  │ Distributed Sampling  │  │ Stream Loading    │  │ │
│  │  │ Ray Data    │  │ Prefetch    │  │ DistSampler │  │ Streaming   │  │ │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘  │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Comparison of Data Pipeline Components

| Component | Type | Processing Capacity | K8s Integration | GPU Support | Applicable Scenario |
|-----|------|---------|--------|--------|---------|
| **Ray Data** | Distributed Processing | TB-level | Ray Operator | Yes | ML data preprocessing |
| **Spark** | Batch Processing | PB-level | Spark Operator | Limited | Large-scale ETL |
| **Dask** | Parallel Computing | TB-level | Dask Operator | Yes | Native Python |
| **Flink** | Stream Processing | Infinite | Flink Operator | No | Real-time data streams |
| **[[domain-14-ai-ml-infra/03-agent-runtime/09-prefect-inngest-agent-workflow.md|Prefect]]** | Orchestration | Backend-dependent | K8s Agent | No | Workflow orchestration |
| **Airflow** | Orchestration | Backend-dependent | K8s Executor | No | DAG scheduling |

---


## 2. Data Format and Storage (Data Formats & Storage)

### 2.1 LLM Training Data Format

| Format | Compression Ratio | Read Speed | Column Pruning | Streaming Read | Applicable Scenario |
|-----|-------|---------|--------|---------|---------|
| **Parquet** | High(70%) | Fast | Supported | Supported | Structured data |
| **Arrow** | None | Very fast | Supported | Supported | Memory swapping |
| **WebDataset** | High | Very fast | Not supported | Native | Images/videos |
| **JSONL** | Low | Slow | Not supported | Native | LLM text |
| **MDS** | High | Very fast | Supported | Native | MosaicML optimization |
| **TFRecord** | Medium | Fast | Not supported | Supported | TensorFlow |

### 2.2 Data Format Conversion

```python
# JSONL to Parquet (Optimize Storage and Reading)
import pyarrow as pa
import pyarrow.parquet as pq
import json

def jsonl_to_parquet(input_path, output_path, batch_size=10000):
    """Convert JSONL to Parquet, supports streaming large files"""
    schema = None
    writer = None
    batch = []
    
    with open(input_path, 'r') as f:
        for line in f:
            batch.append(json.loads(line))
            
            if len(batch) >= batch_size:
                table = pa.Table.from_pylist(batch)
                
                if writer is None:
                    schema = table.schema
                    writer = pq.ParquetWriter(
                        output_path, 
                        schema,
                        compression='snappy'
                    )
                    
                writer.write_table(table)
                batch = []
                
    # Handle remaining data
    if batch:
        table = pa.Table.from_pylist(batch)
        writer.write_table(table)
        
    if writer:
        writer.close()
```

```yaml
# WebDataset format configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: webdataset-config
data:
  create_shards.py: |
    import webdataset as wds
    import json
    
    def create_shards(data_path, output_pattern, max_size=1e9):
        """Create WebDataset shards"""
        with wds.ShardWriter(
            output_pattern,
            maxsize=max_size,
            maxcount=10000
        ) as sink:
            for idx, sample in enumerate(load_samples(data_path)):
                sink.write({
                    "__key__": f"sample_{idx:08d}",
                    "json": json.dumps(sample).encode(),
                })
```

### 2.3 Distributed Storage Configuration

```yaml
# JuiceFS for LLM Data
apiVersion: v1
kind: Secret
metadata:
  name: juicefs-secret
  namespace: ml-data
type: Opaque
stringData:
  name: "llm-data"
  metaurl: "redis://:password@redis-master:6379/1"
  storage: "s3"
  bucket: "s3://llm-training-data"
  access-key: "${AWS_ACCESS_KEY_ID}"
  secret-key: "${AWS_SECRET_ACCESS_KEY}"
  
---
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: juicefs-llm-data
provisioner: csi.juicefs.com
reclaimPolicy: Retain
parameters:
  csi.storage.k8s.io/provisioner-secret-name: juicefs-secret
  csi.storage.k8s.io/provisioner-secret-namespace: ml-data
  csi.storage.k8s.io/node-publish-secret-name: juicefs-secret
  csi.storage.k8s.io/node-publish-secret-namespace: ml-data
  
---
# Alluxio Data Caching
apiVersion: data.fluid.io/v1alpha1
kind: Dataset
metadata:
  name: llm-training-data
  namespace: ml-training
spec:
  mounts:
  - mountPoint: "s3://llm-training-data/processed"
    name: training-data
    path: "/"
    options:
      aws.accessKeyId: "${AWS_ACCESS_KEY_ID}"
      aws.secretKey: "${AWS_SECRET_ACCESS_KEY}"
      aws.region: "us-east-1"
      
  # Data Warm-up Configuration
  dataRestoreLocation:
    path: "s3://llm-training-data/cache"
    
---
apiVersion: data.fluid.io/v1alpha1
kind: AlluxioRuntime
metadata:
  name: llm-training-data
  namespace: ml-training
spec:
  replicas: 10
  
  # Layered Storage
  tieredstore:
    levels:
    - mediumtype: MEM
      path: /dev/shm
      quota: 64Gi
      high: "0.95"
      low: "0.7"
    - mediumtype: SSD
      path: /mnt/nvme
      quota: 500Gi
      high: "0.95"
      low: "0.7"
      
  master:
    replicas: 3
    jvmOptions:
    - "-Xmx16g"
    - "-XX:+UseG1GC"
    resources:
      requests:
        cpu: "4"
        memory: "16Gi"
        
  worker:
    jvmOptions:
    - "-Xmx32g"
    - "-XX:MaxDirectMemorySize=64g"
    resources:
      requests:
        cpu: "8"
        memory: "64Gi"
      limits:
        cpu: "16"
        memory: "128Gi"
        
  fuse:
    jvmOptions:
    - "-Xmx8g"
    - "-Xms8g"
    args:
    - fuse
    - --fuse-opts=kernel_cache,entry_timeout=36000,attr_timeout=36000,max_readahead=134217728
    resources:
      requests:
        cpu: "2"
        memory: "8Gi"
```

---


## 3. Data Cleaning and Quality (Data Cleaning & Quality)

### 3.1 Data Quality Pipeline

```yaml
# Data Quality Check Job
apiVersion: batch/v1
kind: Job
metadata:
  name: data-quality-check
  namespace: ml-data
spec:
  template:
    spec:
      containers:
      - name: quality-checker
        image: ml-platform/data-quality:latest
        command: ["python", "quality_check.py"]
        args:
        - "--input=s3://raw-data/corpus"
        - "--output=s3://processed-data/corpus"
        - "--config=/config/quality_config.yaml"
        
        resources:
          requests:
            cpu: "16"
            memory: "64Gi"
          limits:
            cpu: "32"
            memory: "128Gi"
            
        volumeMounts:
        - name: config
          mountPath: /config
          
      volumes:
      - name: config
        configMap:
          name: quality-config
          
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: quality-config
data:
  quality_config.yaml: |
    # Data Quality Check Configuration
    
    # Text Length Filtering
    length_filter:
      min_chars: 100
      max_chars: 100000
      min_words: 20
      max_words: 20000
      
    # Language Detection
    language_filter:
      enabled: true
      languages: ["en", "zh"]
      min_confidence: 0.9
      
    # Quality Score
    quality_score:
      enabled: true
      model: "fasttext"
      min_score: 0.7
      
    # Duplicate Detection
    deduplication:
      enabled: true
      method: "minhash"
      threshold: 0.8
      num_perm: 128
      
    # PII Detection
    pii_detection:
      enabled: true
      entities: ["PERSON", "EMAIL", "PHONE", "SSN", "CREDIT_CARD"]
      action: "mask"  # mask/remove/flag
      
    # Harmful Content Filtering
    content_filter:
      enabled: true
      categories: ["hate", "violence", "sexual", "self_harm"]
      threshold: 0.5
```

### 3.2 Implementation of Data Deduplication

```python
# MinHash Deduplication (Kubernetes Job)
from datasketch import MinHash, MinHashLSH
import ray
from ray import data as ray_data

@ray.remote
class DeduplicationWorker:
    def __init__(self, num_perm=128, threshold=0.8):
        self.num_perm = num_perm
        self.threshold = threshold
        self.lsh = MinHashLSH(threshold=threshold, num_perm=num_perm)
        
    def compute_minhash(self, text):
        """Compute the MinHash signature of text"""
        m = MinHash(num_perm=self.num_perm)
        for word in text.split():
            m.update(word.encode('utf-8'))
        return m
        
    def is_duplicate(self, doc_id, text):
        """Check if it's a duplicate document"""
        minhash = self.compute_minhash(text)
        result = self.lsh.query(minhash)
        
        if not result:
            self.lsh.insert(doc_id, minhash)
            return False
        return True

def deduplicate_dataset(input_path, output_path):
    """Distributed Deduplication"""
    # Initialize Ray
    ray.init()
    
    # Create a deduplication Worker
    workers = [DeduplicationWorker.remote() for _ in range(100)]
    
    # Read data
    ds = ray_data.read_parquet(input_path)
    
    # Distributed deduplication
    def check_duplicate(batch, worker_idx):
        worker = workers[worker_idx % len(workers)]
        results = []
        for row in batch:
            is_dup = ray.get(worker.is_duplicate.remote(
                row['id'], 
                row['text']
            ))
            if not is_dup:
                results.append(row)
        return results
        
    # Execute deduplication
    deduped_ds = ds.map_batches(
        check_duplicate,
        batch_size=1000,
        num_cpus=1
    )
    
    # Write results
    deduped_ds.write_parquet(output_path)
```

### 3.3 Configuration for PII De-identification

```yaml
# Presidio PII deidentification service
apiVersion: apps/v1
kind: Deployment
metadata:
  name: presidio-analyzer
  namespace: ml-data
spec:
  replicas: 5
  selector:
    matchLabels:
      app: presidio-analyzer
  template:
    spec:
      containers:
      - name: analyzer
        image: mcr.microsoft.com/presidio-analyzer:latest
        ports:
        - containerPort: 3000
        resources:
          requests:
            cpu: "2"
            memory: "4Gi"
        env:
        - name: ANALYZER_CONF_FILE
          value: "/config/analyzer_config.yaml"
        volumeMounts:
        - name: config
          mountPath: /config
          
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: presidio-anonymizer
  namespace: ml-data
spec:
  replicas: 5
  selector:
    matchLabels:
      app: presidio-anonymizer
  template:
    spec:
      containers:
      - name: anonymizer
        image: mcr.microsoft.com/presidio-anonymizer:latest
        ports:
        - containerPort: 3001
        resources:
          requests:
            cpu: "1"
            memory: "2Gi"
            
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: presidio-config
data:
  analyzer_config.yaml: |
    nlp_engine_name: spacy
    models:
    - lang_code: en
      model_name: en_core_web_lg
    - lang_code: zh
      model_name: zh_core_web_lg
      
    supported_entities:
    - PERSON
    - EMAIL_ADDRESS
    - PHONE_NUMBER
    - CREDIT_CARD
    - US_SSN
    - IP_ADDRESS
    - LOCATION
    - DATE_TIME
    - NRP  # 国籍/宗教/政治
    
    recognizers:
    - name: CustomPhoneRecognizer
      supported_entity: PHONE_NUMBER
      patterns:
      - name: phone_pattern
        regex: "\\b\\d{3}[-.]?\\d{4}[-.]?\\d{4}\\b"
        score: 0.9
```

---


## 4. Ray Data Distributed Processing (Ray Data Processing)

### 4.1 Deployment of Ray Cluster

```yaml
# Ray Cluster for Data Processing
apiVersion: ray.io/v1
kind: RayCluster
metadata:
  name: ray-data-cluster
  namespace: ml-data
spec:
  rayVersion: '2.9.0'
  enableInTreeAutoscaling: true
  
  # Autoscaler configuration
  autoscalerOptions:
    upscalingMode: Default
    idleTimeoutSeconds: 60
    
  headGroupSpec:
    rayStartParams:
      dashboard-host: '0.0.0.0'
      block: 'true'
      num-cpus: '0'  # Head不运行任务
      
    template:
      spec:
        containers:
        - name: ray-head
          image: rayproject/ray:2.9.0-py310
          ports:
          - containerPort: 6379
            name: gcs
          - containerPort: 8265
            name: dashboard
          - containerPort: 10001
            name: client
          resources:
            limits:
              cpu: "8"
              memory: "32Gi"
            requests:
              cpu: "4"
              memory: "16Gi"
          volumeMounts:
          - name: ray-logs
            mountPath: /tmp/ray
        volumes:
        - name: ray-logs
          emptyDir: {}
          
  workerGroupSpecs:
  - groupName: data-workers
    replicas: 10
    minReplicas: 5
    maxReplicas: 50
    rayStartParams:
      block: 'true'
      
    template:
      spec:
        containers:
        - name: ray-worker
          image: rayproject/ray:2.9.0-py310
          resources:
            limits:
              cpu: "16"
              memory: "64Gi"
            requests:
              cpu: "8"
              memory: "32Gi"
          env:
          - name: RAY_worker_register_timeout_seconds
            value: "120"
          volumeMounts:
          - name: data-cache
            mountPath: /mnt/cache
        volumes:
        - name: data-cache
          emptyDir:
            sizeLimit: "100Gi"
```

### 4.2 Ray Data Processing Pipeline

```python
# LLM data processing Pipeline
import ray
from ray import data as ray_data
from transformers import AutoTokenizer
import pyarrow as pa

# Initialize Ray
ray.init(address="ray://ray-data-cluster-head-svc:10001")

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")

def tokenize_batch(batch):
    """Batch tokenize"""
    texts = batch["text"]
    encodings = tokenizer(
        texts,
        truncation=True,
        max_length=4096,
        padding=False,
        return_attention_mask=False
    )
    return {
        "input_ids": encodings["input_ids"],
        "length": [len(ids) for ids in encodings["input_ids"]]
    }

def filter_by_length(batch):
    """Length filter"""
    mask = [100 <= length <= 4096 for length in batch["length"]]
    return {
        k: [v for v, m in zip(batch[k], mask) if m]
        for k in batch.keys()
    }

def pack_sequences(batch, max_length=4096):
    """Sequence batching, to improve GPU utilization"""
    packed_input_ids = []
    current_pack = []
    current_length = 0
    
    for input_ids in batch["input_ids"]:
        if current_length + len(input_ids) + 1 <= max_length:
            if current_pack:
                current_pack.append(tokenizer.eos_token_id)
            current_pack.extend(input_ids)
            current_length = len(current_pack)
        else:
            if current_pack:
                # Pad to max_length
                current_pack.extend([tokenizer.pad_token_id] * (max_length - len(current_pack)))
                packed_input_ids.append(current_pack)
            current_pack = input_ids
            current_length = len(input_ids)
            
    if current_pack:
        current_pack.extend([tokenizer.pad_token_id] * (max_length - len(current_pack)))
        packed_input_ids.append(current_pack)
        
    return {"packed_input_ids": packed_input_ids}

# Build Pipeline
ds = ray_data.read_parquet("s3://llm-data/cleaned/")

processed_ds = (
    ds
    .map_batches(tokenize_batch, batch_size=1000, num_cpus=1)
    .map_batches(filter_by_length, batch_size=1000)
    .map_batches(pack_sequences, batch_size=10000, num_cpus=2)
)

# Write processed data
processed_ds.write_parquet(
    "s3://llm-data/tokenized/",
    num_rows_per_file=100000
)

# View statistics
print(f"Total samples: {processed_ds.count()}")
print(f"Schema: {processed_ds.schema()}")
```

### 4.3 Submission of RayJob

```yaml
# RayJob for Data Processing
apiVersion: ray.io/v1
kind: RayJob
metadata:
  name: llm-data-processing
  namespace: ml-data
spec:
  entrypoint: python /app/process_data.py --input s3://raw --output s3://processed
  
  shutdownAfterJobFinishes: true
  ttlSecondsAfterFinished: 300
  
  runtimeEnvYAML: |
    pip:
      - transformers==4.36.0
      - datasets==2.16.0
      - pyarrow==14.0.0
      - boto3==1.34.0
    env_vars:
      AWS_ACCESS_KEY_ID: "${AWS_ACCESS_KEY_ID}"
      AWS_SECRET_ACCESS_KEY: "${AWS_SECRET_ACCESS_KEY}"
      HF_TOKEN: "${HF_TOKEN}"
      
  rayClusterSpec:
    rayVersion: '2.9.0'
    headGroupSpec:
      rayStartParams:
        dashboard-host: '0.0.0.0'
      template:
        spec:
          containers:
          - name: ray-head
            image: rayproject/ray:2.9.0-py310
            resources:
              limits:
                cpu: "8"
                memory: "32Gi"
            volumeMounts:
            - name: app
              mountPath: /app
          volumes:
          - name: app
            configMap:
              name: data-processing-scripts
              
    workerGroupSpecs:
    - groupName: workers
      replicas: 20
      minReplicas: 10
      maxReplicas: 100
      rayStartParams: {}
      template:
        spec:
          containers:
          - name: ray-worker
            image: rayproject/ray:2.9.0-py310
            resources:
              limits:
                cpu: "16"
                memory: "64Gi"
```

---


## 5. Data Mixing and Sampling (Data Mixing & Sampling)

### 5.1 Data Mixing Strategy

| Data Type | Recommended Percentage | Description | Example Source |
|---------|---------|------|---------|
| **General Text** | 40-50% | Web pages, books, Wikipedia | CommonCrawl, Wikipedia |
| **Code** | 15-20% | Code from various programming languages | GitHub, StackOverflow |
| **Scientific Papers** | 5-10% | Academic papers, technical documents | ArXiv, PubMed |
| **Dialogue Data** | 10-15% | Multi-turn dialogues, QA | ShareGPT, OASST |
| **Instruction Data** | 10-15% | Instruction-response pairs | Alpaca, Dolly |
| **Mathematical Reasoning** | 5-10% | Mathematical problems, proofs | GSM8K, MATH |

### 5.2 Dynamic Data Mixing

```python
# Dynamic data mixing configuration
import ray
from ray import data as ray_data

class DynamicDataMixer:
    def __init__(self, datasets_config):
        """
        datasets_config: {
            "web_text": {"path": "s3://...", "weight": 0.4},
            "code": {"path": "s3://...", "weight": 0.2},
            "papers": {"path": "s3://...", "weight": 0.1},
            "conversations": {"path": "s3://...", "weight": 0.15},
            "instructions": {"path": "s3://...", "weight": 0.15}
        }
        """
        self.config = datasets_config
        self.datasets = {}
        
    def load_datasets(self):
        """Load all datasets"""
        for name, cfg in self.config.items():
            self.datasets[name] = ray_data.read_parquet(cfg["path"])
            
    def create_mixed_dataset(self, total_samples):
        """Combine datasets according to weights"""
        mixed_parts = []
        
        for name, cfg in self.config.items():
            ds = self.datasets[name]
            num_samples = int(total_samples * cfg["weight"])
            
            # Oversampling
            if ds.count() >= num_samples:
                sampled = ds.random_shuffle().limit(num_samples)
            else:
                # Oversampling
                repeats = (num_samples // ds.count()) + 1
                sampled = ds.repeat(repeats).limit(num_samples)
                
            mixed_parts.append(sampled)
            
        # Merge and shuffle
        mixed_ds = ray_data.from_blocks(
            [ds.get_internal_block_refs() for ds in mixed_parts]
        ).random_shuffle()
        
        return mixed_ds

# Usage Example
config = {
    "web_text": {"path": "s3://data/web_text/", "weight": 0.4},
    "code": {"path": "s3://data/code/", "weight": 0.2},
    "papers": {"path": "s3://data/papers/", "weight": 0.1},
    "conversations": {"path": "s3://data/conversations/", "weight": 0.15},
    "instructions": {"path": "s3://data/instructions/", "weight": 0.15}
}

mixer = DynamicDataMixer(config)
mixer.load_datasets()
mixed_ds = mixer.create_mixed_dataset(total_samples=10_000_000)
mixed_ds.write_parquet("s3://data/mixed_training_data/")
```

---


## 6. Data Version Management (Data Versioning)

### 6.1 DVC Integration

```yaml
# DVC Pipeline Configuration
apiVersion: batch/v1
kind: Job
metadata:
  name: dvc-data-pipeline
  namespace: ml-data
spec:
  template:
    spec:
      containers:
      - name: dvc
        image: ml-platform/dvc:latest
        command: ["dvc", "repro"]
        env:
        - name: AWS_ACCESS_KEY_ID
          valueFrom:
            secretKeyRef:
              name: aws-credentials
              key: access-key
        - name: AWS_SECRET_ACCESS_KEY
          valueFrom:
            secretKeyRef:
              name: aws-credentials
              key: secret-key
        volumeMounts:
        - name: repo
          mountPath: /repo
        - name: dvc-config
          mountPath: /repo/dvc.yaml
          subPath: dvc.yaml
          
      volumes:
      - name: repo
        persistentVolumeClaim:
          claimName: data-repo-pvc
      - name: dvc-config
        configMap:
          name: dvc-pipeline-config
          
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: dvc-pipeline-config
data:
  dvc.yaml: |
    stages:
      download:
        cmd: python scripts/download_raw.py
        deps:
          - scripts/download_raw.py
        outs:
          - data/raw
          
      clean:
        cmd: python scripts/clean_data.py
        deps:
          - scripts/clean_data.py
          - data/raw
        params:
          - clean.min_length
          - clean.max_length
          - clean.language
        outs:
          - data/cleaned
          
      deduplicate:
        cmd: python scripts/deduplicate.py
        deps:
          - scripts/deduplicate.py
          - data/cleaned
        params:
          - dedup.threshold
          - dedup.method
        outs:
          - data/deduped
          
      tokenize:
        cmd: python scripts/tokenize.py
        deps:
          - scripts/tokenize.py
          - data/deduped
        params:
          - tokenize.model
          - tokenize.max_length
        outs:
          - data/tokenized
          
      mix:
        cmd: python scripts/mix_datasets.py
        deps:
          - scripts/mix_datasets.py
          - data/tokenized
        params:
          - mix.ratios
        outs:
          - data/final
          
    params:
      - params.yaml
```

### 6.2 Data Lineage Tracking

```yaml
# MLflow Data Tracking
apiVersion: v1
kind: ConfigMap
metadata:
  name: data-lineage-config
data:
  track_data.py: |
    import mlflow
    from datetime import datetime
    
    class DataLineageTracker:
        def __init__(self, experiment_name):
            mlflow.set_experiment(experiment_name)
            
        def log_dataset_version(
            self,
            dataset_name,
            version,
            source_path,
            output_path,
            stats,
            params
        ):
            with mlflow.start_run(run_name=f"{dataset_name}_{version}"):
                # Record parameters
                mlflow.log_params(params)
                
                # Record data statistics
                mlflow.log_metrics({
                    "num_samples": stats["num_samples"],
                    "total_tokens": stats["total_tokens"],
                    "avg_length": stats["avg_length"],
                    "dedup_rate": stats["dedup_rate"]
                })
                
                # Record lineage
                mlflow.log_param("source_path", source_path)
                mlflow.log_param("output_path", output_path)
                mlflow.log_param("created_at", datetime.now().isoformat())
                
                # Record schema
                mlflow.log_dict(stats["schema"], "schema.json")
                
                # Mark version
                mlflow.set_tag("dataset_version", version)
                mlflow.set_tag("dataset_name", dataset_name)
```

---


## 7. Data Loading Optimization

### 7.1 High Performance DataLoader

```python
# Optimized Distributed DataLoader
import torch
from torch.utils.data import IterableDataset, DataLoader
import ray
from ray import data as ray_data

class StreamingLLMDataset(IterableDataset):
    """Stream LLM dataset supporting distributed training"""
    
    def __init__(
        self,
        data_path,
        tokenizer,
        max_length=4096,
        world_size=1,
        rank=0,
        buffer_size=10000,
        shuffle_buffer=5000
    ):
        self.data_path = data_path
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.world_size = world_size
        self.rank = rank
        self.buffer_size = buffer_size
        self.shuffle_buffer = shuffle_buffer
        
    def __iter__(self):
        # Use Ray Data for streaming read
        ds = ray_data.read_parquet(
            self.data_path,
            parallelism=200
        )
        
        # Shard to current worker
        ds = ds.split(self.world_size)[self.rank]
        
        # Stream iteration
        for batch in ds.iter_batches(batch_size=self.buffer_size):
            # Local shuffle
            indices = torch.randperm(len(batch["input_ids"]))
            
            for idx in indices[:self.shuffle_buffer]:
                input_ids = batch["input_ids"][idx]
                
                # Padding/truncation
                if len(input_ids) < self.max_length:
                    input_ids = input_ids + [self.tokenizer.pad_token_id] * (
                        self.max_length - len(input_ids)
                    )
                else:
                    input_ids = input_ids[:self.max_length]
                    
                yield {
                    "input_ids": torch.tensor(input_ids),
                    "labels": torch.tensor(input_ids)
                }

def create_distributed_dataloader(
    data_path,
    tokenizer,
    batch_size,
    world_size,
    rank,
    num_workers=4
):
    """Create Distributed DataLoader"""
    dataset = StreamingLLMDataset(
        data_path=data_path,
        tokenizer=tokenizer,
        world_size=world_size,
        rank=rank
    )
    
    return DataLoader(
        dataset,
        batch_size=batch_size,
        num_workers=num_workers,
        pin_memory=True,
        prefetch_factor=2,
        persistent_workers=True
    )
```

### 7.2 Data Prefetch Configuration

```yaml
# Kubernetes Job with Optimized Data Loading
apiVersion: batch/v1
kind: Job
metadata:
  name: llm-training-optimized
  namespace: ml-training
spec:
  template:
    spec:
      containers:
      - name: trainer
        image: nvcr.io/nvidia/pytorch:24.01-py3
        resources:
          limits:
            nvidia.com/gpu: 8
            
        env:
        # Data loading optimization
        - name: DATALOADER_NUM_WORKERS
          value: "8"
        - name: DATALOADER_PIN_MEMORY
          value: "true"
        - name: DATALOADER_PREFETCH_FACTOR
          value: "4"
        
        # Memory mapping optimization
        - name: PYTORCH_CUDA_ALLOC_CONF
          value: "max_split_size_mb:512"
          
        # NCCL optimization
        - name: NCCL_IB_DISABLE
          value: "0"
        - name: NCCL_NET_GDR_LEVEL
          value: "5"
          
        volumeMounts:
        - name: data-cache
          mountPath: /mnt/cache
        - name: shm
          mountPath: /dev/shm
          
      volumes:
      # Local data caching
      - name: data-cache
        hostPath:
          path: /mnt/nvme/cache
          type: DirectoryOrCreate
      # Shared memory
      - name: shm
        emptyDir:
          medium: Memory
          sizeLimit: "128Gi"
```

---


## 8. Monitoring & Alerting

### 8.1 Data Pipeline Monitoring Metrics

| Metric Category | Metric Name | Description | Alert Thresholds |
|---------|---------|------|---------|
| **Processing Progress** | samples_processed | Number of processed samples | Stalled > 1 hour |
| **Processing Progress** | processing_rate | Samples processed per second | < 1000/s |
| **Data Quality** | duplicate_rate | Duplication rate | > 10% |
| **Data Quality** | pii_detection_rate | Detection rate of PII | > 1% |
| **Data Quality** | filter_drop_rate | Drop rate due to filtering | > 50% |
| **Resource Usage** | worker_cpu_util | CPU usage by workers | > 90% |
| **Resource Usage** | memory_usage | Memory usage | > 85% |
| **Storage Status** | storage_write_rate | Storage write rate | < 100MB/s |
| **Error Rate** | processing_errors | Number of processing errors | > 0 |

### 8.2 Prometheus Alert Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: data-pipeline-alerts
  namespace: monitoring
spec:
  groups:
  - name: data-pipeline
    rules:
    # Stalled processing
    - alert: DataProcessingStalled
      expr: |
        rate(data_samples_processed_total[10m]) == 0
      for: 30m
      labels:
        severity: warning
      annotations:
        summary: "Data processing stalled"
        description: "Pipeline {{ $labels.pipeline }} no progress in the last 30 minutes"
        
    # High error rate
    - alert: DataProcessingHighErrorRate
      expr: |
        rate(data_processing_errors_total[5m]) / rate(data_samples_processed_total[5m]) > 0.01
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "High data processing error rate"
        description: "Error rate: {{ $value | humanizePercentage }}"
        
    # Quality decline
    - alert: DataQualityDegraded
      expr: |
        data_quality_score < 0.8
      for: 30m
      labels:
        severity: warning
      annotations:
        summary: "Data quality has declined"
        description: "Quality score: {{ $value }}"
        
    # Insufficient storage space
    - alert: DataStorageNearFull
      expr: |
        data_storage_used_bytes / data_storage_total_bytes > 0.85
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "Storage space for data is nearly full"
```

---


## 9. Quick Reference

### 9.1 Estimate Data Scale

| Model Size | Recommended Training Data | Tokens | Storage Space | Processing Time |
|---------|------------|-----------|---------|---------|
| 1B | 20-50GB | 20B+ | ~100GB | 1-2 days |
| 7B | 200-500GB | 200B+ | ~1TB | 3-5 days |
| 13B | 500GB-1TB | 500B+ | ~2TB | 1 week |
| 70B | 1-2TB | 1T+ | ~5TB | 2-3 weeks |

### 9.2 Common Commands

``` bash
# 🟢 Low risk: read-only/information gathering, typically with no side effects
# Ray Data status
ray status

# Check processing progress
kubectl logs -f job/data-processing -n ml-data

# Data statistics
python -c "import ray; ray.data.read_parquet('s3://...').count()"

# Storage usage
aws s3 ls --summarize --human-readable s3://llm-data/

# DVC status
dvc status
dvc dag
```
---

**Data Pipeline Principles**: Quality first → Complete deduplication → Uniform format → Version tracking → Cache acceleration

---

**Table footnotes**: Kusheet Project, author Allen Galler (allengaller@gmail.com)

---


## Obsidian Related Documentation

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Open Source Project Index
- AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations (AI/ML Workloads Operations)
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management

## See Also

- 13-ai-platform-observability
- 14-troubleshooting-performance
- 16-llm-finetuning
- 17-llm-inference-serving


<!-- risk-assessed -->
