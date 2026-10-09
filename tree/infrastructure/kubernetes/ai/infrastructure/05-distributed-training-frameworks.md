---
title: Distributed Training Framework
description: Deeply analyze the deployment of AI distributed training frameworks on K8s: PyTorch DDP/FSDP, TensorFlow MultiWorkerMirroredStrategy, DeepSpeed, Horovod, MPI
  job scheduling and NCCL optimization
summary: Deeply analyze the deployment of AI distributed training frameworks on K8s: PyTorch DDP/FSDP, TensorFlow MultiWorkerMirroredStrategy, DeepSpeed, Horovod, MPI
  ask scheduling and NCCL uning
category: domain-11-ai-infra
tags:
- k8s
- ai
- distributed-training
- pytorch
- tensorflow
- deepspeed
- horovod
- nccl
- mpi
- scheduler
tier: core
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- MLOps Engineer
- SRE
estimated_read_time: 5min
intent_queries:
- What is a distributed training framework
- How to use a distributed training framework
- Kubernetes 11 ai infra best practices
trigger_keywords:
- Distributed Training Framework
- ai
- infra
prerequisites:
- kubectl-basics
- redis-basics
- gpu-scheduling-basics
k8s_versions:
- '1.25'
- '1.26'
- '1.27'
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
related_docs:
- path: 01-ai-infrastructure-overview.md
  type: depth
  desc: AI Infrastructure Architecture
- path: 03-gpu-scheduling-management.md
  type: depth
  desc: GPU Scheduling and Management
- path: ../domain-14-ai-ml-infra/02-ai-agents/
  type: ai-agent
  desc: AI Agent Engineering
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/05-distributed-training-frameworks.md
---

> **Production Environment Security Tips**
>
> Commands included in this document can be directly executed. Before executing, please confirm: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information collection with no side effects).




# Distributed Training Frameworks

> **Applicable Version**: v1.25 - v1.32 | **Last Updated**: 2026-01 | **Reference**: [PyTorch Distributed](https://pytorch.org/tutorials/beginner/dist_overview.html) | [DeepSpeed](https://www.deepspeed.ai/)


## Distributed Training Architecture Comparison

```
┌─────────────────────────────────────────────────────────────┐
│             Data Parallelism                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Full Model │  │ Full Model │  │ Full Model │  │ Full Model │   │
│  │ GPU 0    │  │ GPU 1    │  │ GPU 2    │  │ GPU 3    │   │
│  │ Shard 1    │  │ Shard 2    │  │ Shard 3    │  │ Shard 4    │   │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘   │
│       └──────────────┴──────────────┴──────────────┘       │
│                    Gradient Synchronization (AllReduce) │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│             Model Parallelism                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ level 1-10  │─→│ level11-20  │─→│ level21-30  │─→│ level31-40  │   │
│  │ GPU 0    │  │ GPU 1    │  │ GPU 2    │  │ GPU 3    │   │
│  │ Full Data  │  │ Full Data  │  │ Full Data  │  │ Full Data  │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                    Pipeline Parallelism                │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│        3D Parallelism (DP + PP + TP - DeepSpeed/Megatron) │
│  ┌────────────────────────────────────────────────────┐    │
│  │  Data Parallel Group 1                             │    │
│  │  ┌──────────┐  ┌──────────┐  (Tensor Parallel)    │    │
│  │  │ Shard 1-20 │  │ Shard 21-40 │                        │    │
│  │  │  GPU 0   │  │  GPU 1   │  ← Pipeline Stage 1  │    │
│  │  └──────────┘  └──────────┘                        │    │
│  │  ┌──────────┐  ┌──────────┐                        │    │
│  │  │ Shard 41-60 │ │ Shard 61-80 │                        │    │
│  │  │  GPU 2   │  │  GPU 3   │  ← Pipeline Stage 2  │    │
│  │  └──────────┘  └──────────┘                        │    │
│  └────────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

---


## 1. PyTorch Distributed Training

### 1. DistributedDataParallel (DDP)

#### Training Script

```python
import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.data.distributed import DistributedSampler

def setup(rank, world_size):
    """Initialize distributed environment"""
    dist.init_process_group(
        backend="nccl",  # GPU推荐nccl
        init_method="env://",  # 从环境变量读取配置
        world_size=world_size,
        rank=rank
    )
    torch.cuda.set_device(rank)

def cleanup():
    dist.destroy_process_group()

def train(rank, world_size):
    setup(rank, world_size)
    
    # Model wrapper
    model = YourModel().cuda(rank)
    model = DDP(model, device_ids=[rank])
    
    # Data loader (key)
    train_dataset = YourDataset()
    train_sampler = DistributedSampler(
        train_dataset,
        num_replicas=world_size,
        rank=rank,
        shuffle=True
    )
    train_loader = DataLoader(
        train_dataset,
        batch_size=32,
        sampler=train_sampler,  # 使用DistributedSampler
        num_workers=4,
        pin_memory=True
    )
    
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
    
    # Training loop
    for epoch in range(10):
        train_sampler.set_epoch(epoch)  # 打乱数据
        
        for batch in train_loader:
            inputs, labels = batch
            inputs = inputs.cuda(rank)
            labels = labels.cuda(rank)
            
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            
            optimizer.zero_grad()
            loss.backward()  # 自动梯度同步
            optimizer.step()
        
        # Save checkpoints only for rank 0
        if rank == 0:
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.module.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
            }, f'checkpoint_epoch_{epoch}.pt')
    
    cleanup()

if __name__ == "__main__":
    world_size = int(os.environ['WORLD_SIZE'])
    rank = int(os.environ['RANK'])
    train(rank, world_size)
```

#### PyTorchJob Configuration

```yaml
apiVersion: kubeflow.org/v1
kind: PyTorchJob
metadata:
  name: ddp-training
  namespace: ai-training
spec:
  pytorchReplicaSpecs:
    Master:
      replicas: 1
      restartPolicy: OnFailure
      template:
        spec:
          containers:
            - name: pytorch
              image: pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime
              command:
                - torchrun
                - --nproc_per_node=8  # 单节点8卡
                - --nnodes=4          # 4个节点
                - --node_rank=$(RANK)
                - --master_addr=$(MASTER_ADDR)
                - --master_port=23456
                - train.py
              env:
                - name: NCCL_DEBUG
                  value: "INFO"
                - name: NCCL_IB_DISABLE
                  value: "0"  # 启用InfiniBand
              resources:
                limits:
                  nvidia.com/gpu: 8
              volumeMounts:
                - name: training-data
                  mountPath: /data
                - name: checkpoint
                  mountPath: /checkpoint
          volumes:
            - name: training-data
              persistentVolumeClaim:
                claimName: imagenet-pvc
            - name: checkpoint
              persistentVolumeClaim:
                claimName: checkpoint-pvc
    
    Worker:
      replicas: 3
      restartPolicy: OnFailure
      template:
        spec:
          containers:
            - name: pytorch
              image: pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime
              command:
                - torchrun
                - --nproc_per_node=8
                - --nnodes=4
                - --node_rank=$(RANK)
                - --master_addr=$(MASTER_ADDR)
                - --master_port=23456
                - train.py
              resources:
                limits:
                  nvidia.com/gpu: 8
              volumeMounts:
                - name: training-data
                  mountPath: /data
                - name: checkpoint
                  mountPath: /checkpoint
          volumes:
            - name: training-data
              persistentVolumeClaim:
                claimName: imagenet-pvc
            - name: checkpoint
              persistentVolumeClaim:
                claimName: checkpoint-pvc
```

---

### 2. FSDP (Fully Sharded Data Parallel)

#### Core Advantages

- **Memory Optimization**: Splitting model parameters, gradients, and optimizer states
- **Zero Redundancy**: Saves 8x GPU memory compared to DDP (8xA100 scenario)
- **Communication Optimization**: AllGather + ReduceScatter

#### FSDP Configuration

```python
import torch
from torch.distributed.fsdp import (
    FullyShardedDataParallel as FSDP,
    CPUOffload,
    MixedPrecision,
    ShardingStrategy,
)
from torch.distributed.fsdp.wrap import (
    size_based_auto_wrap_policy,
    transformer_auto_wrap_policy,
)

# Mixed precision configuration
mixed_precision_policy = MixedPrecision(
    param_dtype=torch.float16,
    reduce_dtype=torch.float16,
    buffer_dtype=torch.float16,
)

# Automatic packaging strategy (by layer size)
auto_wrap_policy = size_based_auto_wrap_policy(
    min_num_params=1e8  # 1亿参数以上的层独立分片
)

# Or package by Transformer layers
from transformers.models.llama.modeling_llama import LlamaDecoderLayer
auto_wrap_policy = partial(
    transformer_auto_wrap_policy,
    transformer_layer_cls={LlamaDecoderLayer},
)

model = YourLargeModel()
model = FSDP(
    model,
    sharding_strategy=ShardingStrategy.FULL_SHARD,  # 全分片
    mixed_precision=mixed_precision_policy,
    auto_wrap_policy=auto_wrap_policy,
    cpu_offload=CPUOffload(offload_params=False),  # CPU offload(可选)
    device_id=torch.cuda.current_device(),
)

# Training loop and DDP are the same
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
```

#### FSDP vs DDP Memory Comparison

| Model Size | DDP (8xA100) | FSDP (8xA100) | Savings |
|---------|-------------|--------------|------|
| **7B** | 56GB | 20GB | 64% |
| **13B** | OOM | 35GB | Trainable |
| **70B** | OOM | OOM (requires CPU offloading) | - |
| **70B+CPU Offload** | - | 60GB | Trainable |

---


## 2. DeepSpeed

### Zero Optimization Phase

| Zero-Ro Stage | Split Content | Memory Savings | Communication Overhead | Applicable Scenario |
|---------|---------|---------|---------|---------|
| **Zero-Ro-0** | No Split | 1x | 1x | Baseline |
| **Zero-Ro-1** | Optimizer State | 4x | 1.5x | <10B models |
| **Zero-Ro-2** | Optimizer + Gradients | 8x | 2x | 10-50B models |
| **Zero-Ro-3** | Optimizer + Gradients + Parameters | Nd times | 1.5x | 50B+ models |

---

### DeepSpeed Configuration

#### ds_config.json

```json
{
  "train_batch_size": 256,
  "train_micro_batch_size_per_gpu": 4,
  "gradient_accumulation_steps": 8,
  
  "optimizer": {
    "type": "AdamW",
    "params": {
      "lr": 1e-5,
      "betas": [0.9, 0.999],
      "eps": 1e-8,
      "weight_decay": 0.01
    }
  },
  
  "scheduler": {
    "type": "WarmupDecayLR",
    "params": {
      "warmup_min_lr": 0,
      "warmup_max_lr": 1e-5,
      "warmup_num_steps": 1000,
      "total_num_steps": 100000
    }
  },
  
  "fp16": {
    "enabled": true,
    "loss_scale": 0,
    "loss_scale_window": 1000,
    "initial_scale_power": 16,
    "hysteresis": 2,
    "min_loss_scale": 1
  },
  
  "zero_optimization": {
    "stage": 3,
    "offload_optimizer": {
      "device": "cpu",
      "pin_memory": true
    },
    "offload_param": {
      "device": "cpu",
      "pin_memory": true
    },
    "overlap_comm": true,
    "contiguous_gradients": true,
    "sub_group_size": 1e9,
    "reduce_bucket_size": 5e8,
    "stage3_prefetch_bucket_size": 5e8,
    "stage3_param_persistence_threshold": 1e6,
    "stage3_max_live_parameters": 1e9,
    "stage3_max_reuse_distance": 1e9,
    "stage3_gather_16bit_weights_on_model_save": true
  },
  
  "gradient_clipping": 1.0,
  "prescale_gradients": false,
  "wall_clock_breakdown": false,
  
  "flops_profiler": {
    "enabled": true,
    "profile_step": 1,
    "module_depth": -1,
    "top_modules": 1,
    "detailed": true
  }
}
```

#### Training Script

```python
import deepspeed
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Model loading
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-70b-hf")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-70b-hf")

# DeepSpeed initialization
model_engine, optimizer, _, _ = deepspeed.initialize(
    model=model,
    model_parameters=model.parameters(),
    config="ds_config.json"
)

# Training loop
for step, batch in enumerate(train_dataloader):
    inputs = tokenizer(batch["text"], return_tensors="pt", padding=True)
    inputs = {k: v.to(model_engine.device) for k, v in inputs.items()}
    
    outputs = model_engine(**inputs, labels=inputs["input_ids"])
    loss = outputs.loss
    
    model_engine.backward(loss)
    model_engine.step()
    
    if step % 100 == 0:
        print(f"Step {step}, Loss: {loss.item()}")
    
    # Save checkpoints
    if step % 1000 == 0:
        model_engine.save_checkpoint("/checkpoint", tag=f"step_{step}")
```

---

### DeepSpeed on [[Kubernetes|Kubernetes]]

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: deepspeed-training
  namespace: ai-training
spec:
  parallelism: 4  # 4个节点
  completions: 4
  template:
    spec:
      containers:
        - name: deepspeed
          image: deepspeed/deepspeed:latest
          command:
            - deepspeed
            - --hostfile=/etc/deepspeed/hostfile
            - --num_gpus=8
            - --master_addr=$(MASTER_ADDR)
            - train.py
            - --deepspeed
            - --deepspeed_config=ds_config.json
          env:
            - name: NCCL_IB_DISABLE
              value: "0"
          resources:
            limits:
              nvidia.com/gpu: 8
          volumeMounts:
            - name: training-data
              mountPath: /data
            - name: checkpoint
              mountPath: /checkpoint
            - name: deepspeed-config
              mountPath: /etc/deepspeed
      volumes:
        - name: training-data
          persistentVolumeClaim:
            claimName: training-data-pvc
        - name: checkpoint
          persistentVolumeClaim:
            claimName: checkpoint-pvc
        - name: deepspeed-config
          configMap:
            name: deepspeed-hostfile
```

---


## 3. Megatron-LM (NVIDIA)

### 3D Parallel Configuration

```bash
# Megatron-LM training command
python pretrain_gpt.py \
  --tensor-model-parallel-size 8 \    # Tensor parallelism (8 GPUs per node)
  --pipeline-model-parallel-size 4 \  # Pipeline parallelism (4 stages)
  --num-layers 96 \                   # Number of layers
  --hidden-size 12288 \               # Hidden layer size
  --num-attention-heads 96 \          # Number of attention heads
  --seq-length 2048 \                 # Sequence length
  --max-position-embeddings 2048 \
  --micro-batch-size 4 \              # Micro-batch size
  --global-batch-size 512 \           # Global batch size
  --train-iters 500000 \              # Number of training iterations
  --lr 1.5e-4 \                       # Learning rate
  --lr-decay-style cosine \
  --min-lr 1.0e-5 \
  --weight-decay 0.1 \
  --clip-grad 1.0 \
  --fp16 \                            # Mixed precision
  --data-path /data/my-dataset \
  --vocab-file /data/vocab.json \
  --merge-file /data/merges.txt \
  --save-interval 10000 \
  --save /checkpoint \
  --load /checkpoint
```

---


## 4. Ray Train (Distributed Training Orchestration)

### Ray Cluster on K8s

```yaml
apiVersion: ray.io/v1alpha1
kind: RayCluster
metadata:
  name: ray-cluster
  namespace: ai-training
spec:
  rayVersion: '2.9.0'
  
  # Head node
  headGroupSpec:
    serviceType: ClusterIP
    rayStartParams:
      dashboard-host: '0.0.0.0'
      num-cpus: '0'  # Head节点不参与计算
    template:
      spec:
        containers:
          - name: ray-head
            image: rayproject/ray:2.9.0-py310-gpu
            ports:
              - containerPort: 6379  # Redis
              - containerPort: 8265  # Dashboard
            resources:
              requests:
                cpu: 4
                memory: 16Gi
              limits:
                cpu: 8
                memory: 32Gi
  
  # Worker node
  workerGroupSpecs:
    - replicas: 8
      minReplicas: 4
      maxReplicas: 16
      groupName: gpu-workers
      rayStartParams:
        num-gpus: '8'
      template:
        spec:
          containers:
            - name: ray-worker
              image: rayproject/ray:2.9.0-py310-gpu
              resources:
                limits:
                  nvidia.com/gpu: 8
                  cpu: 32
                  memory: 256Gi
              volumeMounts:
                - name: training-data
                  mountPath: /data
          volumes:
            - name: training-data
              persistentVolumeClaim:
                claimName: training-data-pvc
```

### Ray Train Training Script

```python
import ray
from ray import train
from ray.train.torch import TorchTrainer
from ray.train import ScalingConfig, RunConfig

def train_func(config):
    import torch
    from torch.nn.parallel import DistributedDataParallel as DDP
    
    # Ray automates distributed environment management
    model = YourModel()
    model = train.torch.prepare_model(model)  # 自动DDP包装
    
    train_dataset = train.torch.prepare_data_loader(
        torch.utils.data.DataLoader(YourDataset(), batch_size=32)
    )
    
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
    
    for epoch in range(10):
        for batch in train_dataset:
            loss = model(batch)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        
        # Report Metrics
        train.report({"loss": loss.item(), "epoch": epoch})

# Configure Trainer
trainer = TorchTrainer(
    train_func,
    scaling_config=ScalingConfig(
        num_workers=32,         # 32个worker
        use_gpu=True,
        resources_per_worker={"GPU": 1}
    ),
    run_config=RunConfig(
        name="my-training",
        storage_path="s3://my-bucket/ray_results",
        checkpoint_config=train.CheckpointConfig(
            num_to_keep=3,
            checkpoint_score_attribute="loss",
            checkpoint_score_order="min",
        ),
    ),
)

# Start training
result = trainer.fit()
```

---


## 5. Communication Backend Optimization

### NCCL Best Practices Configuration

```bash
# Foundation Configuration
export NCCL_DEBUG=INFO
export NCCL_DEBUG_SUBSYS=ALL

# InfiniBand/RoCE Configuration
export NCCL_IB_DISABLE=0
export NCCL_IB_HCA=mlx5_0:1,mlx5_1:1,mlx5_2:1,mlx5_3:1
export NCCL_IB_GID_INDEX=3
export NCCL_NET_GDR_LEVEL=5  # GPU Direct RDMA
export NCCL_IB_TC=106        # 流量类别

# Peer-to-Peer Communication
export NCCL_P2P_DISABLE=0
export NCCL_P2P_LEVEL=SYS    # NVLink优先

# Network interface
export NCCL_SOCKET_IFNAME=eth0
export NCCL_IB_TIMEOUT=22

# Performance Tuning
export NCCL_BUFFSIZE=8388608       # 8MB buffer
export NCCL_NTHREADS=512           # 线程数
export NCCL_NSOCKS_PERTHREAD=8     # 每线程socket数
export NCCL_SOCKET_NTHREADS=8

# Topology Optimization
export NCCL_TOPO_FILE=/etc/nccl_topo.xml
export NCCL_GRAPH_FILE=/etc/nccl_graph.txt
```

### Communication Performance Testing

```bash
# NCCL Tests
git clone https://github.com/NVIDIA/nccl-tests.git
cd nccl-tests
make

# AllReduce test (simulate gradient synchronization)
./build/all_reduce_perf -b 8 -e 128M -f 2 -g 8

# Example Output:
# #    bytes   #iters  time(us)  algbw(GB/s)  busbw(GB/s)
#   8388608      100    1243.2       6.75       11.81
#  16777216      100    2198.4       7.63       13.35
#  33554432      100    4102.7       8.18       14.31
```

---


## 6. Framework Selection Decisions

### Training Size Recommendations

| Model Size | Number of GPUs | Recommended Solution | Configuration Points |
|---------|---------|---------|---------|
| **<1B** | 1-8 | PyTorch DDP | Standard Data Parallelism |
| **1B-10B** | 8-64 | PyTorch FSDP | Equivalent to Zero-Ro-2 |
| **10B-100B** | 64-512 | DeepSpeed ZeRO-3 | CPU offload |
| **100B+** | 512+ | Megatron-LM 3D | TP+PP+DP |

### Framework Feature Comparison

| Feature | PyTorch DDP | FSDP | DeepSpeed | Megatron |
|------|------------|------|-----------|----------|
| **Usability** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **Memory Optimization** | ⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Communication Efficiency** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Model Size** | <10B | <50B | <200B | 1T+ |
| **Ecosystem Maturity** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ |

---


## 7. Production Best Practices

### Training Stability

- ✅ Enable gradient clipping
- ✅ Configure automatic restart strategy
- ✅ Save checkpoints frequently (every N steps)
- ✅ Monitor GPU temperature and ECC errors
- ✅ Configure OOM retry mechanism

### Performance Optimization

- ✅ Use mixed precision training (FP16/BF16)
- ✅ Enable gradient accumulation
- ✅ Optimize DataLoader (num_workers/pin_memory)
- ✅ Enable compilation optimization (torch.compile)
- ✅ Use Flash Attention 2

### Cost Optimization

- ✅ Spot instances + checkpoint fault tolerance
- ✅ Hybrid use of multi-generational GPUs (A100+V100)
- ✅ Dynamically adjust batch size
- ✅ Offline data preprocessing
- ✅ Automatic model parallelism tuning

---

**Table Maintenance**: Kusheet Project | **Author**: Allen Galler (allengaller@gmail.com)

---


## Obsidian Documentation

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- index.md|Domain-11 AI Infrastructure — Open Source Project Index]]
- AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations
- GPU Scheduling and Management
- GPU Monitoring and Observability
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management
- AI Model Deployment and Lifecycle Management

## Related

- [[README]]
- [[MOC]]

- AI Infrastructure Architecture
- GPU Scheduling and Management
- Related Knowledge Domain: domain-02-workloads-applications
- Related Knowledge Domain: domain-03-networking-traffic
- [[domain-17-system-foundation/topic-cheat-sheet/go.md|Cheat Sheet: go]]
- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Knowledge Graph Index]]

## See Also

- 03-gpu-scheduling-management
- 04-gpu-monitoring-dcgm
- 06-ai-data-pipeline
- 07-ai-experiment-management


<!-- risk-assessed -->
