---
title: 143 - LLM Fine-tuning Techniques & Practices
description: '# 143 - LLM uned techniques and practices (LLM Fine-tuning Techniques & Practices)'
summary: 'parser.add_argument("--gradient_accumulation_steps", type=int, default=4)'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- scheduler
- job
- operator
- cuda
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers - AI Engineers
- MLOps Engineers - MLOps Engineers
- SRE
estimated_read_time: 5min
intent_queries:
- LLM Fine-tuning Techniques & Practices is what
- How LLM Fine-tuning Techniques & Practices (LLM Fine-tuning Techniques & Practices)
- Kubernetes 11 ai infra best practices
trigger_keywords:
- LLMS Tuning Technology and Practice
- LLM
- Fine-tuning
- Techniques
- Practices
- ai
- infra
prerequisites:
- kubectl-basics
- gpu-scheduling-basics
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
source_path: tree/infrastructure/kubernetes/ai/infrastructure/16-llm-finetuning.md
---

> **Production Environment Security Tips**
>
> This document contains executable operational commands. Please confirm before execution: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether these commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information collection with no side effects).




# 143 - LLM Fine-tuning Techniques & Practices

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25-v1.32 | **Last Updated**: 2026-01 | **Reference**: [PEFT](https://huggingface.co/docs/peft/), [TRL](https://huggingface.co/docs/trl/)

---


## 1. Overall Fine-tuning Landscape (Fine-tuning Landscape)

### 1.1 Tuning Methods Classification

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      LLM Fine-tuning Technology Overview                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                    Full Parameter Fine-tuning                       │ │
│  │  ┌─────────────────────────────────────────────────────────────────┐ │ │
│  │  │  Update all parameters | High memory requirement | Best effect | Suitable for verticalization           │ │ │
│  │  │  Typical scenarios: Pre-training resuming, domain adaptation, multi-language expansion                       │ │ │
│  │  └─────────────────────────────────────────────────────────────────┘ │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                    Parameter Efficient Fine-tuning (PEFT)                                 │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               │ │
│  │  │    LoRA      │  │   QLoRA      │  │   Adapter    │               │ │
│  │  │ Rank-Sparse Decomposition    │  │ Quantization+LoRA    │  │ Adapter Layer    │               │ │
│  │  │  0.1% Parameter  │  │  4-bit Quantization  │  │  Insert Module  │               │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘               │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               │ │
│  │  │  IA³         │  │  Prefix      │  │  P-Tuning    │               │ │
│  │  │  Activate Scaling  │  │  Prefix Tuning  │  │  Soft Prompt  │               │ │
│  │  │  0.01% parameter  │  │  virtual token  │  │  learnable embedding  │               │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘               │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │                    Alignment Tuning                                │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               │ │
│  │  │    SFT       │  │    RLHF      │  │    DPO       │               │ │
│  │  │  Supervised Fine-tuning  │  │ Human Feedback Reinforcement  │  │ Direct Preference Optimization  │               │ │
│  │  │  Command-response  │  │  Reward model  │  │  No RM        │               │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘               │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐               │ │
│  │  │    PPO       │  │    ORPO      │  │    KTO       │               │ │
│  │  │  Near-end Policy  │  │ Odd Ratio Preference  │  │ Kahneman-T  │               │ │
│  │  │  Complex but stable  │  │  No reference model required│  │  Unilateral data    │               │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘               │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Tuning Methods Comparison

| Method | Number of Trainable Parameters | Memory Requirement (7B) | Training Speed | Effect | Applicable Scenario |
|-----|-----------|-------------|---------|------|---------|
| **Full FT** | 100% | 112GB+ | Slow | Best | Vertical domain specialization |
| **LoRA** | 0.1-1% | 16-24GB | Fast | Excellent | General instruction fine-tuning |
| **QLoRA** | 0.1-1% | 6-12GB | Moderate | Excellent | Resource-constrained scenarios |
| **Adapter** | 1-5% | 20-30GB | Fast | Good | Multi-task adaptation |
| **IA³** | 0.01% | 14-16GB | Very fast | Good | Lightweight adaptation |
| **Prefix Tuning** | <0.1% | 14-16GB | Very fast | Good | Few-shot enhancement |
| **P-Tuning v2** | <0.1% | 14-16GB | Very fast | Good | NLU tasks |

### 1.3 Memory Estimation Formula

| Component | Formula | Estimation for 7B Model |
|-----|---------|-----------|
| **Model Weights** | Parameter Quantity × Precision Bytes | 7B × 2B = 14GB (FP16) |
| **Gradients** | Parameter Quantity × 4B | 7B × 4B = 28GB |
| **Optimizer State** | Parameter Quantity × 8B (AdamW) | 7B × 8B = 56GB |
| **Activation Values** | Batch × Sequence × Hidden × Layers | ~10-20GB |
| **LoRA Memory** | Base Model + rank × Hidden × 2 | 14GB + 1GB |

---


## 2. LoRA Fine-tuning Explained (LoRA Fine-tuning)

### 2.1 LoRA Principle

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         LoRA Low-rank Decomposition Principle                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Original weight matrix W (d × k)                                                     │
│  ┌───────────────────────────────┐                                         │
│  │                               │                                         │
│  │           Frozen W₀           │                                         │
│  │         (d × k)               │                                         │
│  │                               │                                         │
│  └───────────────────────────────┘                                         │
│                  +                                                          │
│  ┌───────────────────────────────┐                                         │
│  │  LoRA Increment: ΔW = B × A        │                                         │
│  │  ┌─────┐     ┌───────────┐   │                                         │
│  │  │  B  │  ×  │     A     │   │                                         │
│  │  │(d×r)│     │   (r×k)   │   │                                         │
│  │  └─────┘     └───────────┘   │                                         │
│  │                               │                                         │
│  │  r << min(d, k), such as r=8      │                                         │
│  │  Trainable parameters: r×(d+k)          │                                         │
│  └───────────────────────────────┘                                         │
│                                                                             │
│  Forward calculation: h = W₀x + ΔWx = W₀x + BAx                                       │
│  Scaling factor: h = W₀x + (α/r) × BAx                                           │
│                                                                             │
│  Parameter comparison (Llama-7B, Attention):                                          │
│  - Original: 4096 × 4096 = 16.8M/layer                                            │
│  - LoRA(r=8): 8 × (4096 + 4096) = 65K/layer (saved 99.6%)                       │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### 2.2 LoRA Configuration Best Practices

```yaml
# LoRA Fine-Tuning Kubernetes Job
apiVersion: batch/v1
kind: Job
metadata:
  name: llama2-7b-lora-finetune
  namespace: ml-training
spec:
  backoffLimit: 3
  template:
    metadata:
      labels:
        app: lora-training
    spec:
      restartPolicy: OnFailure
      
      nodeSelector:
        nvidia.com/gpu.product: "NVIDIA-A100-SXM4-40GB"
      tolerations:
      - key: "nvidia.com/gpu"
        operator: "Exists"
        effect: "NoSchedule"
        
      containers:
      - name: trainer
        image: huggingface/transformers-pytorch-gpu:latest
        
        command: ["python", "-m", "torch.distributed.launch"]
        args:
        - "--nproc_per_node=4"
        - "train_lora.py"
        - "--model_name_or_path=meta-llama/Llama-2-7b-hf"
        - "--dataset_path=/data/training_data"
        - "--output_dir=/output/llama2-7b-lora"
        - "--lora_r=16"
        - "--lora_alpha=32"
        - "--lora_dropout=0.05"
        - "--target_modules=q_proj,k_proj,v_proj,o_proj,gate_proj,up_proj,down_proj"
        - "--per_device_train_batch_size=4"
        - "--gradient_accumulation_steps=4"
        - "--learning_rate=2e-4"
        - "--num_train_epochs=3"
        - "--warmup_ratio=0.03"
        - "--lr_scheduler_type=cosine"
        - "--bf16"
        - "--gradient_checkpointing"
        - "--logging_steps=10"
        - "--save_steps=500"
        - "--save_total_limit=3"
        - "--report_to=wandb"
        
        resources:
          requests:
            cpu: "32"
            memory: "128Gi"
            nvidia.com/gpu: "4"
          limits:
            cpu: "64"
            memory: "256Gi"
            nvidia.com/gpu: "4"
            
        env:
        - name: HF_TOKEN
          valueFrom:
            secretKeyRef:
              name: hf-token
              key: token
        - name: WANDB_API_KEY
          valueFrom:
            secretKeyRef:
              name: wandb-secret
              key: api-key
        - name: WANDB_PROJECT
          value: "llm-finetuning"
        - name: CUDA_VISIBLE_DEVICES
          value: "0,1,2,3"
          
        volumeMounts:
        - name: training-data
          mountPath: /data
        - name: output
          mountPath: /output
        - name: shm
          mountPath: /dev/shm
        - name: hf-cache
          mountPath: /root/.cache/huggingface
          
      volumes:
      - name: training-data
        persistentVolumeClaim:
          claimName: training-data-pvc
      - name: output
        persistentVolumeClaim:
          claimName: model-output-pvc
      - name: shm
        emptyDir:
          medium: Memory
          sizeLimit: "32Gi"
      - name: hf-cache
        persistentVolumeClaim:
          claimName: hf-cache-pvc
```

### 2.3 LoRA Training Script

```python
# train_lora.py
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from peft import (
    LoraConfig,
    get_peft_model,
    prepare_model_for_kbit_training,
    TaskType
)
from datasets import load_from_disk
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name_or_path", type=str, required=True)
    parser.add_argument("--dataset_path", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)
    parser.add_argument("--lora_r", type=int, default=16)
    parser.add_argument("--lora_alpha", type=int, default=32)
    parser.add_argument("--lora_dropout", type=float, default=0.05)
    parser.add_argument("--target_modules", type=str, default="q_proj,v_proj")
    parser.add_argument("--per_device_train_batch_size", type=int, default=4)
    parser.add_argument("--gradient_accumulation_steps", type=int, default=4)
    parser.add_argument("--learning_rate", type=float, default=2e-4)
    parser.add_argument("--num_train_epochs", type=int, default=3)
    parser.add_argument("--warmup_ratio", type=float, default=0.03)
    parser.add_argument("--lr_scheduler_type", type=str, default="cosine")
    parser.add_argument("--bf16", action="store_true")
    parser.add_argument("--gradient_checkpointing", action="store_true")
    parser.add_argument("--logging_steps", type=int, default=10)
    parser.add_argument("--save_steps", type=int, default=500)
    parser.add_argument("--save_total_limit", type=int, default=3)
    parser.add_argument("--report_to", type=str, default="wandb")
    args = parser.parse_args()

    # Load tokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path)
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "right"

    # Load model
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name_or_path,
        torch_dtype=torch.bfloat16 if args.bf16 else torch.float16,
        device_map="auto",
        trust_remote_code=True
    )

    # Enable gradient checkpointing
    if args.gradient_checkpointing:
        model.gradient_checkpointing_enable()
        model.enable_input_require_grads()

    # LORA configuration
    lora_config = LoraConfig(
        r=args.lora_r,
        lora_alpha=args.lora_alpha,
        lora_dropout=args.lora_dropout,
        target_modules=args.target_modules.split(","),
        bias="none",
        task_type=TaskType.CAUSAL_LM
    )

    # Apply LORA
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # Load dataset
    dataset = load_from_disk(args.dataset_path)

    # Training parameters
    training_args = TrainingArguments(
        output_dir=args.output_dir,
        per_device_train_batch_size=args.per_device_train_batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.learning_rate,
        num_train_epochs=args.num_train_epochs,
        warmup_ratio=args.warmup_ratio,
        lr_scheduler_type=args.lr_scheduler_type,
        bf16=args.bf16,
        logging_steps=args.logging_steps,
        save_steps=args.save_steps,
        save_total_limit=args.save_total_limit,
        report_to=args.report_to,
        ddp_find_unused_parameters=False,
        group_by_length=True,
        dataloader_num_workers=4,
        dataloader_pin_memory=True
    )

    # Data preparer
    data_collator = DataCollatorForLanguageModeling(
        tokenizer=tokenizer,
        mlm=False
    )

    # Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset.get("validation"),
        data_collator=data_collator
    )

    # Start training
    trainer.train()

    # Save model
    trainer.save_model()
    tokenizer.save_pretrained(args.output_dir)

if __name__ == "__main__":
    main()
```

---


## 3. QLoRA Quantized Fine-tuning (QLoRA)

### 3.1 QLoRA Configuration

```yaml
# QLoRA Fine-Tuning Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: qlora-config
data:
  qlora_config.yaml: |
    # Quantization configuration
    quantization:
      load_in_4bit: true
      bnb_4bit_compute_dtype: bfloat16
      bnb_4bit_use_double_quant: true
      bnb_4bit_quant_type: nf4
      
    # LORA configuration
    lora:
      r: 64
      lora_alpha: 16
      lora_dropout: 0.1
      target_modules:
        - q_proj
        - k_proj
        - v_proj
        - o_proj
        - gate_proj
        - up_proj
        - down_proj
      bias: none
      task_type: CAUSAL_LM
      
    # Training configuration
    training:
      per_device_train_batch_size: 1
      gradient_accumulation_steps: 16
      learning_rate: 2e-4
      max_steps: 10000
      warmup_steps: 100
      fp16: false
      bf16: true
      optim: paged_adamw_32bit
      gradient_checkpointing: true
      max_grad_norm: 0.3
      
---
apiVersion: batch/v1
kind: Job
metadata:
  name: llama2-70b-qlora
  namespace: ml-training
spec:
  template:
    spec:
      containers:
      - name: trainer
        image: ml-platform/qlora-trainer:latest
        command: ["python", "train_qlora.py"]
        args:
        - "--model_name=meta-llama/Llama-2-70b-hf"
        - "--dataset=/data/alpaca"
        - "--output_dir=/output/llama2-70b-qlora"
        - "--config=/config/qlora_config.yaml"
        
        resources:
          limits:
            nvidia.com/gpu: 1        # 单卡即可微调70B
            memory: "48Gi"
            
        volumeMounts:
        - name: config
          mountPath: /config
          
      volumes:
      - name: config
        configMap:
          name: qlora-config
```

### 3.2 QLoRA Training Script

```python
# train_qlora.py
import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    TrainingArguments
)
from peft import (
    LoraConfig,
    get_peft_model,
    prepare_model_for_kbit_training
)
from trl import SFTTrainer
from datasets import load_from_disk
import yaml

def load_config(config_path):
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def main(args):
    config = load_config(args.config)
    
    # 4bit quantization configuration
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=config['quantization']['load_in_4bit'],
        bnb_4bit_compute_dtype=getattr(
            torch, 
            config['quantization']['bnb_4bit_compute_dtype']
        ),
        bnb_4bit_use_double_quant=config['quantization']['bnb_4bit_use_double_quant'],
        bnb_4bit_quant_type=config['quantization']['bnb_4bit_quant_type']
    )
    
    # Load quantized model
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        quantization_config=bnb_config,
        device_map="auto",
        trust_remote_code=True
    )
    
    # Prepare for quantized training
    model = prepare_model_for_kbit_training(model)
    
    # LORA configuration
    lora_config = LoraConfig(
        r=config['lora']['r'],
        lora_alpha=config['lora']['lora_alpha'],
        lora_dropout=config['lora']['lora_dropout'],
        target_modules=config['lora']['target_modules'],
        bias=config['lora']['bias'],
        task_type=config['lora']['task_type']
    )
    
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()
    
    # Load tokenizer and data
    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    tokenizer.pad_token = tokenizer.eos_token
    
    dataset = load_from_disk(args.dataset)
    
    # Training Parameters
    training_args = TrainingArguments(
        output_dir=args.output_dir,
        per_device_train_batch_size=config['training']['per_device_train_batch_size'],
        gradient_accumulation_steps=config['training']['gradient_accumulation_steps'],
        learning_rate=config['training']['learning_rate'],
        max_steps=config['training']['max_steps'],
        warmup_steps=config['training']['warmup_steps'],
        bf16=config['training']['bf16'],
        optim=config['training']['optim'],
        gradient_checkpointing=config['training']['gradient_checkpointing'],
        max_grad_norm=config['training']['max_grad_norm'],
        logging_steps=10,
        save_steps=100,
        report_to="wandb"
    )
    
    # SFT Trainer
    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset["train"],
        tokenizer=tokenizer,
        args=training_args,
        dataset_text_field="text",
        max_seq_length=2048,
        packing=True
    )
    
    trainer.train()
    trainer.save_model()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--model_name", type=str, required=True)
    parser.add_argument("--dataset", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)
    parser.add_argument("--config", type=str, required=True)
    args = parser.parse_args()
    main(args)
```

---


## 4. Alignment Fine-tuning

### 4.1 SFT Supervised Fine-tuning

```yaml
# SFT Training Job
apiVersion: "kubeflow.org/v1"
kind: PyTorchJob
metadata:
  name: llama2-sft
  namespace: ml-training
spec:
  pytorchReplicaSpecs:
    Master:
      replicas: 1
      template:
        spec:
          containers:
          - name: pytorch
            image: ml-platform/sft-trainer:latest
            command: ["accelerate", "launch"]
            args:
            - "--config_file=/config/accelerate_config.yaml"
            - "train_sft.py"
            - "--model_name=meta-llama/Llama-2-7b-hf"
            - "--dataset_name=/data/sft_dataset"
            - "--output_dir=/output/llama2-sft"
            - "--num_train_epochs=3"
            - "--per_device_train_batch_size=4"
            - "--learning_rate=2e-5"
            resources:
              limits:
                nvidia.com/gpu: 8
                
    Worker:
      replicas: 3
      template:
        spec:
          containers:
          - name: pytorch
            image: ml-platform/sft-trainer:latest
            resources:
              limits:
                nvidia.com/gpu: 8
```

### 4.2 Direct Preference Optimization

```python
# DPO Training Configuration
from trl import DPOTrainer, DPOConfig
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig
from datasets import load_from_disk

def train_dpo():
    # Load SFT Model
    model = AutoModelForCausalLM.from_pretrained(
        "llama2-7b-sft",
        torch_dtype=torch.bfloat16,
        device_map="auto"
    )
    
    # Reference Model (frozen SFT model)
    ref_model = AutoModelForCausalLM.from_pretrained(
        "llama2-7b-sft",
        torch_dtype=torch.bfloat16,
        device_map="auto"
    )
    
    tokenizer = AutoTokenizer.from_pretrained("llama2-7b-sft")
    tokenizer.pad_token = tokenizer.eos_token
    
    # LoRA Configuration (optional)
    peft_config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        target_modules=["q_proj", "v_proj", "k_proj", "o_proj"],
        bias="none",
        task_type="CAUSAL_LM"
    )
    
    # DPO Configuration
    dpo_config = DPOConfig(
        output_dir="llama2-7b-dpo",
        beta=0.1,                      # KL散度系数
        loss_type="sigmoid",           # sigmoid/hinge/ipo
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        learning_rate=5e-7,
        num_train_epochs=1,
        warmup_ratio=0.1,
        bf16=True,
        logging_steps=10,
        save_steps=100,
        gradient_checkpointing=True,
        max_length=1024,
        max_prompt_length=512,
        report_to="wandb"
    )
    
    # Load Preference Dataset
    # Format: {"prompt": str, "chosen": str, "rejected": str}
    dataset = load_from_disk("/data/dpo_dataset")
    
    # DPO Trainer
    trainer = DPOTrainer(
        model=model,
        ref_model=ref_model,
        args=dpo_config,
        train_dataset=dataset["train"],
        eval_dataset=dataset["validation"],
        tokenizer=tokenizer,
        peft_config=peft_config
    )
    
    trainer.train()
    trainer.save_model()

if __name__ == "__main__":
    train_dpo()
```

### 4.3 RLHF Training Pipeline

```yaml
# RLHF Three-Stage Training Pipeline
apiVersion: argoproj.io/v1alpha1
kind: Workflow
metadata:
  name: rlhf-pipeline
  namespace: ml-training
spec:
  entrypoint: rlhf-training
  
  templates:
  - name: rlhf-training
    dag:
      tasks:
      # Stage 1: SFT
      - name: sft-training
        template: sft
        
      # Stage 2: Reward Model Training
      - name: reward-model-training
        template: reward-model
        dependencies: [sft-training]
        
      # Stage 3: PPO Training
      - name: ppo-training
        template: ppo
        dependencies: [reward-model-training]
        
  - name: sft
    container:
      image: ml-platform/sft-trainer:latest
      command: ["python", "train_sft.py"]
      resources:
        limits:
          nvidia.com/gpu: 8
          
  - name: reward-model
    container:
      image: ml-platform/reward-trainer:latest
      command: ["python", "train_reward.py"]
      args:
      - "--base_model={{tasks.sft-training.outputs.result}}"
      resources:
        limits:
          nvidia.com/gpu: 4
          
  - name: ppo
    container:
      image: ml-platform/ppo-trainer:latest
      command: ["python", "train_ppo.py"]
      args:
      - "--sft_model={{tasks.sft-training.outputs.result}}"
      - "--reward_model={{tasks.reward-model-training.outputs.result}}"
      resources:
        limits:
          nvidia.com/gpu: 8
```

---


## 5. Distributed Fine-tuning (Distributed Fine-tuning)

### 5.1 DeepSpeed ZeRO Configuration

```yaml
# DeepSpeed Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: deepspeed-config
data:
  ds_config_zero3.json: |
    {
      "train_batch_size": "auto",
      "train_micro_batch_size_per_gpu": "auto",
      "gradient_accumulation_steps": "auto",
      
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
        "reduce_bucket_size": "auto",
        "stage3_prefetch_bucket_size": "auto",
        "stage3_param_persistence_threshold": "auto",
        "sub_group_size": 1e9,
        "stage3_max_live_parameters": 1e9,
        "stage3_max_reuse_distance": 1e9,
        "stage3_gather_16bit_weights_on_model_save": true
      },
      
      "bf16": {
        "enabled": true
      },
      
      "gradient_clipping": 1.0,
      
      "optimizer": {
        "type": "AdamW",
        "params": {
          "lr": "auto",
          "betas": [0.9, 0.999],
          "eps": 1e-8,
          "weight_decay": "auto"
        }
      },
      
      "scheduler": {
        "type": "WarmupDecayLR",
        "params": {
          "warmup_min_lr": 0,
          "warmup_max_lr": "auto",
          "warmup_num_steps": "auto",
          "total_num_steps": "auto"
        }
      },
      
      "activation_checkpointing": {
        "partition_activations": true,
        "cpu_checkpointing": true,
        "contiguous_memory_optimization": true
      },
      
      "wall_clock_breakdown": false
    }
```

### 5.2 Multi-node Training

```yaml
# PyTorchJob Multi-node Fine-tuning
apiVersion: "kubeflow.org/v1"
kind: PyTorchJob
metadata:
  name: llama2-70b-finetune
  namespace: ml-training
spec:
  elasticPolicy:
    rdzvBackend: c10d
    minReplicas: 4
    maxReplicas: 8
    
  pytorchReplicaSpecs:
    Master:
      replicas: 1
      template:
        spec:
          containers:
          - name: pytorch
            image: nvcr.io/nvidia/pytorch:24.01-py3
            command: ["deepspeed"]
            args:
            - "--num_gpus=8"
            - "--num_nodes=$(WORLD_SIZE)"
            - "--hostfile=/etc/mpi/hostfile"
            - "train.py"
            - "--model_name=meta-llama/Llama-2-70b-hf"
            - "--deepspeed=/config/ds_config_zero3.json"
            - "--bf16"
            - "--gradient_checkpointing"
            
            resources:
              limits:
                nvidia.com/gpu: 8
                rdma/rdma_shared_device_a: 1
                
            env:
            - name: NCCL_IB_DISABLE
              value: "0"
            - name: NCCL_NET_GDR_LEVEL
              value: "5"
              
    Worker:
      replicas: 3
      template:
        spec:
          containers:
          - name: pytorch
            image: nvcr.io/nvidia/pytorch:24.01-py3
            resources:
              limits:
                nvidia.com/gpu: 8
                rdma/rdma_shared_device_a: 1
```

---


## 6. Tuning Monitoring & Evaluation (Monitoring & Evaluation)

### 6.1 Train Monitoring Metrics

| Metric | Description | Alert Threshold |
|-----|------|---------|
| **train_loss** | Training Loss | Stagnation >1000 steps |
| **eval_loss** | Evaluation Loss | Rising continuously |
| **learning_rate** | Learning Rate | Zeroes Out Abnormalities |
| **grad_norm** | Gradient Norm | > 10 (Gradient Explosion) |
| **gpu_util** | GPU Utilization | < 50% |
| **gpu_memory** | GPU Memory Usage | > 95% |
| **throughput** | Samples/Second | Decreases >20% |

### 6.2 Evaluate Pipeline

```yaml
# Model Evaluation Job
apiVersion: batch/v1
kind: Job
metadata:
  name: model-evaluation
  namespace: ml-training
spec:
  template:
    spec:
      containers:
      - name: evaluator
        image: ml-platform/lm-evaluation:latest
        command: ["python", "-m", "lm_eval"]
        args:
        - "--model=hf"
        - "--model_args=pretrained=/models/llama2-7b-finetuned"
        - "--tasks=hellaswag,arc_challenge,winogrande,mmlu"
        - "--batch_size=auto"
        - "--output_path=/output/eval_results.json"
        
        resources:
          limits:
            nvidia.com/gpu: 1
            
        volumeMounts:
        - name: models
          mountPath: /models
        - name: output
          mountPath: /output
          
      volumes:
      - name: models
        persistentVolumeClaim:
          claimName: model-pvc
      - name: output
        persistentVolumeClaim:
          claimName: eval-output-pvc
```

---


## 7. Cost Optimization (Cost Optimization)

### 7.1 Cost Comparison

| Parameter | GPU | Cost for Training a 7B Model | Cost for Training an 70B Model |
|-----|-----|---------------|----------------|
| **Full FT** | 2×A100 80GB | $200/day | $1,600/day |
| **LoRA** | 1×A100 40GB | $50/day | $400/day |
| **QLoRA** | 1×A10G 24GB | $8/day | $64/day |
| **Spot + QLoRA** | 1×A10G Spot | $2.4/day | $19/day |

### 7.2 Spot Instance Strategy

```yaml
# Spot Instance Fine-tuning Configuration
apiVersion: karpenter.sh/v1alpha5
kind: Provisioner
metadata:
  name: finetuning-spot
spec:
  requirements:
  - key: "karpenter.sh/capacity-type"
    operator: In
    values: ["spot"]
  - key: "node.kubernetes.io/instance-type"
    operator: In
    values: ["g5.2xlarge", "g5.4xlarge", "p3.2xlarge"]
    
  limits:
    resources:
      nvidia.com/gpu: 32
      
  ttlSecondsAfterEmpty: 30
  
---
# Resume Training
apiVersion: batch/v1
kind: Job
metadata:
  name: finetuning-with-checkpoint
spec:
  backoffLimit: 100  # 允许多次重试
  template:
    spec:
      containers:
      - name: trainer
        image: ml-platform/trainer:latest
        args:
        - "--resume_from_checkpoint=auto"  # 自动从最新checkpoint恢复
        - "--save_steps=100"                # 频繁保存
        
        volumeMounts:
        - name: checkpoints
          mountPath: /checkpoints
          
      volumes:
      - name: checkpoints
        persistentVolumeClaim:
          claimName: checkpoint-pvc  # 持久化checkpoint
```

---


## 8. Quick Reference (Quick Reference)

### 8.1 LoRA Parameter Selection

| Parameter | Small Models (<7B) | Medium Models (7-13B) | Large Models (>30B) |
|-----|------------|--------------|-------------|
| **r (rank)** | 8-16 | 16-32 | 32-64 |
| **alpha** | 16-32 | 32-64 | 64-128 |
| **dropout** | 0.05-0.1 | 0.05-0.1 | 0.05 |
| **target_modules** | q,v | q,k,v,o | all linear |
| **learning_rate** | 1e-4 - 3e-4 | 1e-4 - 2e-4 | 5e-5 - 1e-4 |

### 8.2 Common Commands

> ⚠️ **Yellow Alert Change** — Change cluster resource status, suggest first using --dry-run or diff to confirm
> - `kubectl exec`: Enter container to execute commands, may change container state

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, confirm target, impact scope, and authorization before execution
# Check Training Status
kubectl logs -f job/lora-training -n ml-training

# Check GPU Usage
kubectl exec -it <pod> -- nvidia-smi

# Load LoRA weights
from peft import PeftModel
model = PeftModel.from_pretrained(base_model, "path/to/lora")

# Merge LoRA to the base model
merged_model = model.merge_and_unload()
merged_model.save_pretrained("merged_model")
```
---

**Micro-Fine Tuning Best Practices**: Start from QLoRA → Validate effects before upgrading LoRA → Necessary then Full FT → Continuously Evaluate

---

**Table Bottom Markers**: Kusheet Project, Author Allen Galler (allengaller@gmail.com)

---


## 9. Obsidian Documentation (Obsidian Documentation)

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Index of Open Source Projects
- AI Infrastructure Architecture
- 132 - AI/ML Workload Operations (AI/ML Workloads Operations)
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry Center and Version Management

## See Also

- 14-troubleshooting-performance
- 15-llm-data-pipeline
- 17-llm-inference-serving
- 18-llm-serving-architecture


<!-- risk-assessed -->
