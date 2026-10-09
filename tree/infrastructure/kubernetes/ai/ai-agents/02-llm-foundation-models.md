---
title: LLM Base Model Selection and Evaluation (domain-14-ai-ml-infra)
description: 'description: ''**Document Type**: Technical Selection Guide | **Last Updated**: 2026-03 | **Keywords**: LLM Selection,
  GPT-4o, Claude'
summary: 'description: ''**Document Type**: Technical Selection Guide | **Last Updated**: 2026-03 | **Keywords**: LLM Selection, GPT-4o,
  Claude'
category: general
tags:
- ai
- ai-agent
- docker
- networkpolicy
- operator
- gpu
- nvidia
- vllm
- llm
- rag
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 15min
intent_queries:
- LLM Base Model Selection and Evaluation is what
- How to do LLM Base Model Selection and Evaluation
- Kubernetes 14 ai ml infra Best Practices
trigger_keywords:
- LLM
- Base Model Selection and Evaluation
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- gpu-scheduling-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/02-llm-foundation-models.md
---

# LLM Base Model Selection and Evaluation

## Overview

LLM selection is the primary decision in building an Agent system, directly determining the upper limit of the Agent's reasoning ability, the reliability of tool invocation, cost structure, and compliance boundaries. This article provides a comprehensive matrix comparison of mainstream models, specialized evaluation metrics for the Agent scenario, a decision framework for fine-tuning versus RAG, and model routing strategies for production environments.

---

## 1. Model Panorama Overview

## 1.1 Mainstream Model Classification

```
LLM 生态全景
│
├── 闭源商业模型（API 调用）
│   ├── OpenAI 系列: GPT-4o, GPT-4o-mini, o1, o3-mini
│   ├── Anthropic 系列: Claude 3.5 Sonnet, Claude 3.5 Haiku, Claude 3 Opus
│   ├── Google 系列: Gemini 2.0 Flash, Gemini 1.5 Pro, Gemini Ultra
│   └── 国内: 通义千问、文心一言、智谱 GLM-4、Moonshot Kimi
│
├── 开源/半开源模型（自部署）
│   ├── Meta: Llama 3.1 (8B/70B/405B), Llama 3.3 70B
│   ├── 阿里: Qwen2.5 (7B/14B/32B/72B), Qwen2.5-Coder
│   ├── DeepSeek: DeepSeek-V3, DeepSeek-R1, DeepSeek-R1-Distill
│   ├── Mistral: Mistral Large, Mixtral 8x22B, Mistral Nemo
│   └── Google: Gemma 2 (9B/27B)
│
└── 专用模型
    ├── 代码: DeepSeek-Coder-V2, Qwen2.5-Coder-32B, CodeLlama
    ├── 嵌入: text-embedding-3-large, BGE-M3, Jina v3
    └── 多模态: GPT-4V, Claude 3.5 (视觉), Gemini 1.5 Pro
```

---

## 2. Model Performance Comparison Matrix

## 2.1 Comprehensive Capability Comparison (Benchmark by the end of 2025)

| Model | Parameters | Context Window | Reasoning Ability | Code Ability | Tool Invocation | Chinese Ability | Cost/$1M Tokens | Latency (First Token) |
|------|-------|-----------|---------|---------|---------|---------|--------------|-------------|
| **GPT-4o** | Unknown | 128K | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★☆ | $2.5/$10 | ~0.5s |
| **GPT-4o-mini** | Unknown | 128K | ★★★★☆ | ★★★★☆ | ★★★★★ | ★★★★☆ | $0.15/$0.6 | ~0.3s |
| **o1** | Unknown | 200K | ★★★★★+ | ★★★★★ | ★★★★☆ | ★★★★☆ | $15/$60 | 5-30s |
| **Claude 3.5 Sonnet** | Unknown | 200K | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★☆ | $3/$15 | ~0.5s |
| **Claude 3.5 Haiku** | Unknown | 200K | ★★★★☆ | ★★★★☆ | ★★★★★ | ★★★★☆ | $0.8/$4 | ~0.3s |
| **Gemini 2.0 Flash** | Unknown | 1M | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★★★☆ | $0.1/$0.4 | ~0.4s |
| **Gemini 1.5 Pro** | Unknown | 2M | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★★★☆ | $1.25/$5 | ~1s |
| **Llama 3.3 70B** | 70B | 128K | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★★☆☆ | Self-deployed | Dependent on hardware |
| **Qwen2.5-72B** | 72B | 128K | ★★★★☆ | ★★★★★ | ★★★★☆ | ★★★★★ | Self-deployed | Dependent on hardware |
| **DeepSeek-V3** | 671B(MoE) | 128K | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★★ | $0.27/$1.1 | ~1s |
| **DeepSeek-R1** | 671B(MoE) | 128K | ★★★★★+ | ★★★★★ | ★★★☆☆ | ★★★★★ | $0.55/$2.19 | 10-60s |

> Note: Prices are per Input/Output Token, based on API calls, which may vary with vendor adjustments. Self-deployment costs depend on GPU resources.

## 2.2 Specialized Agent Capabilities Comparison

| Model | Tool Invocation Reliability | Multi-step Planning | Command Following | Self-correction | Long-context Understanding | Parallel Tool Invocation |
|------|-------------|---------|---------|---------|------------|------------|
| GPT-4o | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★☆ | Native support |
| GPT-4o-mini | ★★★★☆ | ★★★★☆ | ★★★★★ | ★★★★☆ | ★★★★☆ | Native Support |
| Claude 3.5 Sonnet | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | Native Support |
| Gemini 2.0 Flash | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★★★★ | Native Support |
| Llama 3.3 70B | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★★★☆ | Support |
| Qwen2.5-72B | ★★★★☆ | ★★★★☆ | ★★★★★ | ★★★★☆ | ★★★★☆ | Support |
| DeepSeek-V3 | ★★★★☆ | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★☆ | Support |
| DeepSeek-R1 | ★★★☆☆ | ★★★★★+ | ★★★★☆ | ★★★★★ | ★★★★☆ | Limited Support |

---

## 3. Scenario Selection Decision Tree

## 3.1 Main Decision Framework

```
选型决策起点
│
├── 数据是否可以发送到外部 API?
│   ├── 否（合规/安全要求内部部署）
│   │   └── → 开源模型自部署（Llama/Qwen/DeepSeek）
│   │
│   └── 是
│       ├── 预算是否充裕（>$50/月）?
│       │   ├── 是
│       │   │   ├── 需要最强推理能力? → GPT-4o 或 Claude 3.5 Sonnet
│       │   │   ├── 需要超长上下文(>200K)? → Gemini 1.5 Pro (2M)
│       │   │   └── 主要处理中文? → DeepSeek-V3 或 通义千问-Max
│       │   │
│       │   └── 否（成本敏感）
│       │       ├── 简单任务/高频调用 → GPT-4o-mini 或 Gemini Flash
│       │       └── 中文场景成本敏感 → DeepSeek-V3 (极低价格)
│       │
│       └── 是否有严格的工具调用要求?
│           ├── 是 → GPT-4o 或 Claude 3.5 Sonnet（工具调用最可靠）
│           └── 否 → 根据成本/性能比选择
```

## 3.2 Kubernetes Operations Agent Special Selection Recommendations

| Agent Type | Recommended Model | Alternative Model | Reason |
|-----------|---------|---------|------|
| Real-time Diagnosis Agent | GPT-4o-mini | Claude 3.5 Haiku | Frequent calls require low latency and cost-effectiveness, sufficient capabilities |
| Complex Fault Analysis | Claude 3.5 Sonnet | GPT-4o | Requires multi-step reasoning + long contextual understanding of large amounts of logs |
| Configuration Generation Agent | GPT-4o | Qwen2.5-72B | YAML generation requires high precision instructions to follow |
| Offline Root Cause Analysis | DeepSeek-R1 | o1 | Deep inference tasks, insensitive to latency |
| Private Deployment | Qwen2.5-72B | Llama 3.3 70B | Strong Chinese capability + tool invocation + open-source |

---

## 4. Model Evaluation Methodology

## 4.1 Evaluation Dimensions for Agents

```python
# Agent Capability Baseline Test Framework
class AgentBenchmark:
    
    def evaluate_tool_calling_accuracy(self, model, test_cases: list) -> float:
        """Evaluation of Call Accuracy for Evaluation Tools"""
        # Test Points:
        # 1. Did the right tools get selected
        # 2. Are the tool parameters correctly filled
        # 3. Are errors from tools properly handled and retried
        # 4. Are unnecessary tool calls avoided
        correct = 0
        for case in test_cases:
            result = model.invoke(case["input"], tools=case["tools"])
            if self._check_tool_call(result, case["expected_tool_call"]):
                correct += 1
        return correct / len(test_cases)
    
    def evaluate_multi_step_planning(self, model, scenarios: list) -> dict:
        """Evaluate multi-step planning capability"""
        metrics = {
            "task_completion_rate": 0,
            "avg_steps_efficiency": 0,  # 实际步骤/最优步骤
            "hallucination_rate": 0,    # 无凭据声明的比例
        }
        # ... Evaluate Implementation
        return metrics
    
    def evaluate_context_retention(self, model, long_conv: list) -> float:
        """Evaluate context retention ability in long dialogues"""
        # Ask information from the third round after the twentieth round of dialogue
        # Measure recall accuracy
        pass
```

## 4.2 Recommend Evaluation Baseline Sets

| Baseline Set | Measurement Dimension | Applicable Scenario |
|--------|---------|---------|
| **MMLU** | Multidisciplinary Knowledge | General Capability Baseline |
| **HumanEval / MBPP** | Code Generation Ability | Code Agent |
| **ToolBench** | Accuracy of Tool Calls | Tool Call Agent |
| **AgentBench** | Task Completion Rate of Agents | Comprehensive Agent Evaluation |
| **GAIA** | Real-world Tasks | General Agent |
| **SWE-bench** | Software Engineering Tasks | Code/DevOps Agent |
| **τ-bench** | Comprehensive Tool + Reasoning | Complex Agent Scenarios |
| **K8s Special Test Set** | Depth of Kubernetes Knowledge | Maintenance Agent (Self-built) |

## 4.3 Self-built Evaluation Set (K8s Operations Scenario)

```python
K8S_AGENT_TEST_CASES = [
    {
        "id": "pod-pending-001",
        "category": "故障诊断",
        "difficulty": "medium",
        "input": "Pod nginx-xxx 一直处于 Pending 状态，已经 10 分钟了",
        "required_tools": ["kubectl_describe", "kubectl_get_nodes"],
        "expected_root_causes": ["资源不足", "节点亲和性", "PVC 未绑定", "Taint 不匹配"],
        "evaluation_rubric": {
            "tool_sequence_correct": 0.3,  # 30% 分权重
            "root_cause_identified": 0.4,
            "fix_suggestion_correct": 0.3,
        }
    },
    {
        "id": "service-unreachable-001",
        "category": "网络诊断",
        "difficulty": "hard",
        "input": "frontend Pod 无法访问 backend Service，但 Service 存在",
        "required_tools": ["kubectl_get_endpoints", "kubectl_exec_curl", "kubectl_get_networkpolicy"],
        "expected_root_causes": ["Endpoints 为空", "NetworkPolicy 阻断", "kube-proxy 问题"],
    }
]
```

---

## 5. Fine-tuning vs RAG Decision Framework

## 5.1 Decision Matrix

| Dimension | Fine-tuning (Micro-tuning) | RAG |
|------|-------------------|-----|
| **Applicable Scenarios** | Fixed format output, domain style, technical terms | Frequent knowledge updates, need to cite sources, large knowledge volume |
| **Knowledge Update Cost** | High (retraining required) | Low (update knowledge base only) |
| **Training Data Requirements** | Requires high-quality annotated data (hundreds to thousands of entries) | No training data needed |
| **Inference Cost** | Low (no additional search required) | Higher (search + generation) |
| **Latency** | Low | Higher (+100~500ms search time) |
| **Hallucination Risk** | High (model may overgeneralize) | Low (supported by search results) |
| **Interpretability** | Poor (knowledge embedding weights) | Good (traceable search sources) |
| **Initial Investment** | High (training cost + infrastructure) | Moderate (build knowledge base + vectorization)|

## 5.2 Decision Judgment Tree

```
选择微调 还是 RAG?
│
├── 知识更新频率 > 每月一次?
│   └── 是 → 优先 RAG（微调太慢）
│
├── 需要引用具体来源/文档?
│   └── 是 → 必须 RAG
│
├── 目标是改变输出格式/风格（如固定 JSON 结构）?
│   └── 是 → 考虑微调（或 Prompt Engineering 先试）
│
├── 专业术语/缩略语大量出现，基座模型不理解?
│   └── 是 → 微调（词汇层面的问题 RAG 难以解决）
│
├── 知识库超过 100 万 tokens?
│   └── 是 → 必须 RAG（塞不进上下文）
│
└── 两者都需要? → RAG + Fine-tuning 组合
    示例: 微调模型学习输出格式 + RAG 提供最新知识
```

## 5.3 Practical Recommendations

```
尝试顺序（成本从低到高）:
  1. 先尝试 Prompt Engineering（系统提示 + Few-shot 示例）
  2. 效果不佳 → 尝试 RAG
  3. RAG 后仍有格式/风格问题 → 考虑少量 Fine-tuning
  4. 以上都不够 → 组合策略（RAG + Fine-tuning）

常见误区:
  × 直接跳到微调，忽略 Prompt Engineering 的潜力
  × 以为微调了就不需要 RAG（知识更新仍然需要）
  × 只用 RAG 不做质量评估，导致检索质量差影响生成
```

---

## 6. Model Routing Strategy (Production Environment)

In a production Agent system, typically multiple model routing is needed to balance cost and quality:

```python
from enum import Enum
from dataclasses import dataclass

class TaskComplexity(Enum):
    SIMPLE = "simple"     # 简单问答、格式转换
    MEDIUM = "medium"     # 多步骤工具调用
    COMPLEX = "complex"   # 深度推理、复杂分析

@dataclass
class ModelConfig:
    name: str
    api_key_env: str
    cost_per_1m_input: float  # USD
    cost_per_1m_output: float
    max_context: int
    avg_latency_ms: int

MODEL_REGISTRY = {
    "gpt-4o": ModelConfig("gpt-4o", "OPENAI_API_KEY", 2.5, 10.0, 128000, 500),
    "gpt-4o-mini": ModelConfig("gpt-4o-mini", "OPENAI_API_KEY", 0.15, 0.6, 128000, 300),
    "claude-3-5-sonnet": ModelConfig("claude-3-5-sonnet-20241022", "ANTHROPIC_API_KEY", 3.0, 15.0, 200000, 500),
    "claude-3-5-haiku": ModelConfig("claude-3-5-haiku-20241022", "ANTHROPIC_API_KEY", 0.8, 4.0, 200000, 300),
    "deepseek-v3": ModelConfig("deepseek-chat", "DEEPSEEK_API_KEY", 0.27, 1.1, 128000, 1000),
}

class ModelRouter:
    def route(self, task: dict) -> str:
        """Choose the optimal model based on task characteristics"""
        complexity = self._assess_complexity(task)
        requires_chinese = self._needs_chinese(task)
        is_latency_sensitive = task.get("latency_sensitive", False)
        context_length = self._estimate_context(task)
        
        # Long context
        if context_length > 128_000:
            return "gemini-1.5-pro"  # 2M context
        
        # Deep inference tasks (latency-insensitive)
        if complexity == TaskComplexity.COMPLEX and not is_latency_sensitive:
            if requires_chinese:
                return "deepseek-r1"
            return "claude-3-5-sonnet"
        
        # High-frequency simple tasks (cost-sensitive)
        if complexity == TaskComplexity.SIMPLE:
            if requires_chinese:
                return "deepseek-v3"  # 极低价格 + 强中文
            return "gpt-4o-mini"
        
        # Medium complexity (default main force)
        if requires_chinese:
            return "deepseek-v3"
        return "gpt-4o-mini"
    
    def _assess_complexity(self, task: dict) -> TaskComplexity:
        """Assess complexity based on task description"""
        description = task.get("description", "")
        tool_count = len(task.get("available_tools", []))
        
        if tool_count > 10 or "分析" in description or "规划" in description:
            return TaskComplexity.COMPLEX
        elif tool_count > 3 or "诊断" in description:
            return TaskComplexity.MEDIUM
        return TaskComplexity.SIMPLE
```

---

## 7. Open-source model self-deployment guide

## 7.1 Hardware Requirements Quick Reference

| Model | Minimum GPU | Recommended GPU | Memory Requirement (FP16) | Inference Throughput (vLLM) |
|------|---------|---------|--------------|----------------|
| Qwen2.5-7B | 1x RTX 3090 | 1x A100 | ~16GB | ~50 req/s |
| Llama 3.1 8B | 1x RTX 3090 | 1x A100 | ~16GB | ~50 req/s |
| Qwen2.5-14B | 1x A100 40G | 2x A100 | ~28GB | ~30 req/s |
| Qwen2.5-32B | 2x A100 80G | 4x A100 | ~64GB | ~15 req/s |
| Llama 3.3 70B | 4x A100 80G | 8x A100 | ~140GB | ~8 req/s |
| Qwen2.5-72B | 4x A100 80G | 8x A100 | ~144GB | ~8 req/s |
| DeepSeek-V3 671B | 8x H100 (FP8) | 16x H100 | ~350GB(FP8) | ~3 req/s |

## 7.2 vLLM Deployment Example

``` bash
# 🟢 Low-risk: Read-only/information collection, usually no side effects
# Recommended configuration for deploying Qwen2.5-72B
docker run --gpus all \
  -v /data/models:/models \
  -p 8000:8000 \
  vllm/vllm-openai:latest \
  --model /models/Qwen2.5-72B-Instruct \
  --served-model-name qwen2.5-72b \
  --tensor-parallel-size 4 \      # 4 GPUs for tensor parallelism
  --pipeline-parallel-size 1 \
  --max-model-len 32768 \         # Maximum context length (memory limit)
  --max-num-seqs 256 \            # Maximum concurrent requests
  --enable-chunked-prefill \      # Improve efficiency for long texts
  --trust-remote-code \
  --dtype bfloat16 \
  --api-key "your-secret-key"
```
```yaml
# Kubernetes deploy vLLM (integrate with production environment)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vllm-qwen25-72b
  namespace: ai-serving
spec:
  replicas: 1
  selector:
    matchLabels:
      app: vllm-qwen25-72b
  template:
    metadata:
      labels:
        app: vllm-qwen25-72b
    spec:
      containers:
      - name: vllm
        image: vllm/vllm-openai:v0.6.3
        args:
          - "--model=/models/Qwen2.5-72B-Instruct"
          - "--tensor-parallel-size=4"
          - "--max-model-len=32768"
          - "--served-model-name=qwen2.5-72b"
        resources:
          limits:
            nvidia.com/gpu: "4"
            memory: "200Gi"
          requests:
            nvidia.com/gpu: "4"
            memory: "180Gi"
        volumeMounts:
        - name: model-storage
          mountPath: /models
        - name: shm
          mountPath: /dev/shm
      volumes:
      - name: model-storage
        persistentVolumeClaim:
          claimName: model-storage-pvc
      - name: shm
        emptyDir:
          medium: Memory
          sizeLimit: "20Gi"
      tolerations:
      - key: "nvidia.com/gpu"
        operator: "Exists"
        effect: "NoSchedule"
      nodeSelector:
        gpu-type: a100-80g
```

---

## 8. Compliance and data security considerations

## 8.1 Data Classification and Model Selection

```
数据密级 → 模型选择规则:

  公开数据 / 脱敏数据
  └── 可使用任何 API 模型（GPT-4o、Claude、Gemini）

  内部数据（业务数据、代码）
  ├── 签署 DPA（数据处理协议）后可用 API 模型
  └── 敏感时优先考虑私有化部署

  敏感/机密数据（客户 PII、财务数据、密钥）
  ├── 强烈建议私有化部署开源模型
  ├── 如用 API，必须开启数据不训练选项 + 签署保密协议
  └── 参考: 10-security-guardrails.md 中的 PII 处理规范

  监管数据（医疗/金融/政府）
  └── 通常要求完全本地化部署，不允许数据出境
```

## 8.2 Domestic compliance requirements

```
中国大陆合规要点:
  1. 《生成式人工智能服务管理暂行办法》
     - 向中国用户提供服务的 AIGC 产品需向国家互联网信息办公室备案
  
  2. 数据本地化要求
     - 重要数据和个人信息原则上在境内存储
     - 推荐使用国内 API（阿里云百炼、字节豆包、智谱 AI）或自部署
  
  3. 内容安全要求
     - 需部署内容安全过滤层
     - 推荐: 阿里云内容安全 SDK 或百度文字审核
```

---

## 9. Best Practices and Anti-patterns

## Best Practices

- **Multi-model strategy**: Don't send all tasks to the most expensive model at once; route by complexity to save up to 60-80% in costs
- **Type selection driven by evaluation**: Test with your own dataset instead of relying solely on public benchmarks—there's a gap between benchmark scores and actual business outcomes
- **Version Locking**: Production environment fixed model version (e.g., `gpt-4o-2024-11-20`), avoiding supplier silent upgrades affecting output consistency
- **Temperature Configuration**: Set `temperature=0` for batch tasks, and `temperature=0.7` for creative tasks
- **Stream Output**: Use Streaming for scenarios sensitive to latency, reducing user perception of waiting time

## Anti-patterns

- **Using Only the Most Expensive Model**: Simple classification tasks using GPT-4o is a huge waste; GPT-4o-mini is sufficient
- **Not Locking Versions**:`gpt-4o-latest` will automatically upgrade, potentially causing sudden changes in output format
- **Ignoring Token Counting**: No monitoring of token usage leads to rapid cost overruns
- **Over-Dependence on a Single Supplier**: Without alternatives when OpenAI services are unstable, design fallbacks for multiple suppliers

---

## Related Documents

| Document | Relevant Content |
|------|---------|
| [01 - AI Agent Basics](./01-ai-agent-fundamentals.md) | Dependency of model capabilities in the AI agent inference framework |
| [03 - Agent Framework Comparison](./03-agent-frameworks-comparison.md) | Compatibility between different frameworks and models |
| [11 - Cost and Latency Optimization](./11-cost-latency-optimization.md) | Practical practices for cost optimization in model routing |
| [domain-14-ai-ml-infra/17-llm-inference-serving.md](../domain-14-ai-ml-infra/17-llm-inference-serving.md) | Details of vLLM/TGI deployment |
| [domain-14-ai-ml-infra/03-gpu-scheduling-management.md](../domain-14-ai-ml-infra/03-gpu-scheduling-management.md) | GPU resource scheduling |

---

*This document is original content from the kudig-database project's 02-ai-agents topic.*

---

## Related Obsidian Documents

- 02-ai-agents KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|[[AI Agent Engineering Topic|AI Agent Engineering Topic]]]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|AI Agent Basics and Core Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Deep Comparison of Mainstream Agent Frameworks]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|RAG Retrieval-Augmented Generation Deep Guide]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Tool Usage & Function Calling Design Guidelines]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Multi-Agent Orchestration and Collaboration Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation and Observability Framework]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]
- [[domain-14-ai-ml-infra/02-ai-agents/11-cost-latency-optimization.md|Cost and Latency Optimization Strategies]]

## See Also

- 50-openclaw-identity-mechanism
- 01-ai-agent-fundamentals
- 03-agent-frameworks-comparison
- 04-rag-knowledge-retrieval


<!-- risk-assessed -->
