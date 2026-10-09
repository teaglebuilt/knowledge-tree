---
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/42-model-harness-compatibility-matrix.md
---
---title: Model × Harness Compatibility Matrix (2025-2026) [02-ai-agents]
description: 'description: ''**Document Type**: Practical Reference Guide | **Last Updated**: 2026-04 | **Keywords**: Model
  Compatibility,'
summary: 'description: ''**Document Type**: Practical Reference Guide | **Last Updated**: 2026-04 | **Keywords**: Model Compatibility,'
category: general
tags:
- ai
- ai-agent
- gpu
- vllm
- llm
- rag
- agent
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 15min
intent_queries:
- What is the Model × Harness Compatibility Matrix (2025-2026)
- How to use the Model × Harness Compatibility Matrix (2025-2026)
- Kubernetes 14 ai ml infra best practices
trigger_keywords:
- Model
- Harness
- Compatibility Matrix
- 2025-2026
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- gpu-scheduling-basics
authors:
- name: Dillan Teagle
  role: contributor

---

> **Production Environment Safety Notice**
>
> This document contains directly executable operational commands. Before executing, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have validated in a non-production environment. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state, but generally reversible), 🟢 Low Risk / Read-Only (information gathering, no side effects).




title: Model × Harness Compatibility Matrix (2025-2026)
description: '**Document Type**: Practical Reference Guide | **Last Updated**: 2026-04 | **Keywords**: Model Compatibility,
  Harness Support, Function Calling, Tool Use, Structured Output, Agent Ready, GPT,
  Claude, Gemini, Qwen, DeepSeek, Llama'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- gpu
- vllm
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Architects
- SRE
estimated_read_time: 10min
intent_queries:
- What is the Model × Harness Compatibility Matrix (2025-2026)
- How to use the Model × Harness Compatibility Matrix (2025-2026)
trigger_keywords:
- Model
- Harness
- Compatibility Matrix
- 2025-2026
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

# Model × Harness Compatibility Matrix (2025-2026)

> **Document Type**: Practical Reference Guide | **Last Updated**: 2026-04 | **Keywords**: Model Compatibility, Harness Support, Function Calling, Tool Use, Structured Output, Agent Ready, GPT, Claude, Gemini, Qwen, DeepSeek, Llama

---

## Overview

The Agent Harness has explicit capability requirements for the underlying model: **not all models can drive the full six-layer Harness**. A model must support key capabilities such as Function Calling, Structured Output, System Prompts, and Streaming Output in order to operate reliably as the Harness "engine."

This document provides a complete Harness compatibility list for mainstream models in 2025-2026, helping engineers quickly determine which models can be used directly in a Harness architecture, which require additional adaptation, and which are unsuitable.

---

## 1. Six Core Capability Requirements the Harness Places on Models

```
Key Harness capabilities a model must support:

1. Function Calling / Tool Use                    ← Layer 2: Tools
   The model natively supports function calls and can generate structured tool call requests
   Importance: ★★★★★ (Required)

2. Structured Output                              ← Layer 5: Verification
   The model can output structured formats such as JSON for the verification layer to parse
   Importance: ★★★★★ (Required)

3. System Prompt                                  ← Layer 6: Constraints
   Supports system role messages, used to inject constraints and behavioral rules
   Importance: ★★★★★ (Required)

4. Streaming                                      ← Layer 1: Loop
   Supports SSE streaming responses, used for real-time UI and long-running tasks
   Importance: ★★★★☆ (Strongly Recommended)

5. Large Context Window (≥128K)                   ← Layer 3: Context
   Sufficient context space to accommodate tool output, history traces, and RAG results
   Importance: ★★★★☆ (Strongly Recommended)

6. Parallel Tool Calls                            ← Layer 2: Tools
   Invoking multiple tools simultaneously within a single inference, improving execution efficiency
   Importance: ★★★☆☆ (Recommended)
```

---

## 2. Closed-Source Commercial Model Harness Compatibility List

### 2.1 OpenAI Series

| Model | Version / Release Date | Function Calling | Structured Output | System Prompt | Streaming | Context Window | Parallel Tool Calls | Harness Readiness |
|------|-------------|-----------------|-------------------|---------------|-----------|-----------|------------|--------------|
| **GPT-4.1** | 2025-04 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 1M | ✅ | ★★★★★ |
| **GPT-4.1 mini** | 2025-04 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 1M | ✅ | ★★★★★ |
| **GPT-4.1 nano** | 2025-04 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 1M | ✅ | ★★★★☆ |
| **GPT-4o** | 2024-05 (November update) | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 128K | ✅ | ★★★★★ |
| **GPT-4o mini** | 2024-07 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 128K | ✅ | ★★★★★ |
| **o3** | 2025-04 | ✅ Native | ✅ | ✅ | ✅ | 200K | ✅ | ★★★★★ |
| **o4-mini** | 2025-04 | ✅ Native | ✅ | ✅ | ✅ | 200K | ✅ | ★★★★★ |
| **o3-mini** | 2025-01 | ✅ Native | ✅ | ✅ | ✅ | 200K | ✅ | ★★★★☆ |
| **o1** | 2024-09 | ⚠️ Limited | ✅ | ⚠️ developer | ✅ | 200K | ❌ | ★★★☆☆ |
| **GPT-5** | 2025-05~ | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 400K | ✅ | ★★★★★ |
| **GPT-5.2** | Late 2025~ | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 400K | ✅ | ★★★★★ |

**OpenAI Series Harness Characteristics**:
- The GPT-4.1 series is **one of the best choices for Harness**: 1M context + native Function Calling + Structured Output
- **o3/o4-mini reasoning models now fully support tool calls**, suitable for Harness scenarios requiring deep reasoning
- o1's tool calling capability is limited (no parallel support) and is not recommended as the primary Harness engine
- The GPT-5 series unifies reasoning and tool calling capabilities, making it the flagship Harness engine for the second half of 2025

### 2.2 Anthropic Series

| Model | Version / Release Date | Function Calling | Structured Output | System Prompt | Streaming | Context Window | Parallel Tool Calls | Harness Readiness |
|------|-------------|-----------------|-------------------|---------------|-----------|-----------|------------|--------------|
| **Claude Sonnet 4** | 2025-05 | ✅ Native | ✅ Tool Use | ✅ | ✅ | 200K | ✅ | ★★★★★ |
| **Claude Opus 4** | 2025-05 | ✅ Native | ✅ Tool Use | ✅ | ✅ | 200K | ✅ | ★★★★★ |
| **Claude 3.7 Sonnet** | 2025-02 | ✅ Native | ✅ Tool Use | ✅ | ✅ | 200K | ✅ | ★★★★★ |
| **Claude 3.5 Sonnet** | 2024-06 (October update) | ✅ Native | ✅ Tool Use | ✅ | ✅ | 200K | ✅ | ★★★★★ |
| **Claude 3.5 Haiku** | 2024-10 | ✅ Native | ✅ Tool Use | ✅ | ✅ | 200K | ✅ | ★★★★★ |
| **Claude Sonnet 4.5** | Late 2025 | ✅ Native | ✅ | ✅ | ✅ | 200K | ✅ | ★★★★★ |
| **Claude Sonnet 4.6** | 2026 | ✅ Native | ✅ | ✅ | ✅ | 200K | ✅ | ★★★★★ |
| **Claude Opus 4.6** | 2026 | ✅ Native | ✅ | ✅ | ✅ | 200K | ✅ | ★★★★★ |

**Anthropic Series Harness Characteristics**:
- The entire Claude lineup starting from 3.5 **fully supports all capabilities required by Harness**
- Claude's **Extended Thinking mode** is naturally suited for the Harness Verification layer (self-checking reasoning)
- Claude Code (command-line Agent) is itself a **benchmark implementation of Harness architecture**
- SWE-bench score (80.8%) is the highest on Harness-sensitive benchmarks, proving the Harness × Claude combination delivers the best results

### 2.3 Google Series

| Model | Version / Release Date | Function Calling | Structured Output | System Prompt | Streaming | Context Window | Parallel Tool Calls | Harness Readiness |
|------|-------------|-----------------|-------------------|---------------|-----------|-----------|------------|--------------|
| **Gemini 2.5 Pro** | 2025-03 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 1M | ✅ | ★★★★★ |
| **Gemini 2.5 Flash** | 2025-04 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 1M | ✅ | ★★★★★ |
| **Gemini 2.0 Flash** | 2025-01 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 1M | ✅ | ★★★★☆ |
| **Gemini 1.5 Pro** | 2024 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 2M | ✅ | ★★★★☆ |
| **Gemini 3.0 / 3.1 Pro** | 2026 | ✅ Native | ✅ | ✅ | ✅ | 2M | ✅ | ★★★★★ |

**Google Series Harness Characteristics**:
- **Largest context window** (1M–2M), naturally suited for scenarios where the Harness Context layer requires large amounts of information
- Gemini 2.5 Pro's **Thinking mode** is similar to Claude Extended Thinking, enhancing self-checking capability
- Gemini 2.5 Flash is the **most cost-effective Harness engine** ($0.15/$0.60 per 1M tokens)
- GPQA Diamond 94.3% (Gemini 3.1 Pro), strongest scientific reasoning capability

### 2.4 xAI Series

| Model | Version / Release Date | Function Calling | Structured Output | System Prompt | Streaming | Context Window | Parallel Tool Calls | Harness Readiness |
|------|-------------|-----------------|-------------------|---------------|-----------|-----------|------------|--------------|
| **Grok 3** | 2025-02 | ✅ Native | ✅ | ✅ | ✅ | 128K | ✅ | ★★★★☆ |
| **Grok 4** | 2026 | ✅ Native | ✅ | ✅ | ✅ | 256K+ | ✅ | ★★★★★ |

---
## 3. Open-Source / Semi-Open-Source Model Harness Compatibility Checklist

### 3.1 DeepSeek Series

| Model | Version/Release Date | Function Calling | Structured Output | System Prompt | Streaming | Context Window | Parallel Tool Calls | Harness Readiness |
|------|-------------|-----------------|-------------------|---------------|-----------|-----------|------------|--------------|
| **DeepSeek-V3** | 2024-12 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 128K | ✅ | ★★★★☆ |
| **DeepSeek-R1** | 2025-01 | ⚠️ Limited | ⚠️ Unstable | ✅ | ✅ | 128K | ❌ | ★★☆☆☆ |
| **DeepSeek-R1-Distill Series** | 2025-01 | ⚠️ Limited | ⚠️ Unstable | ✅ | ✅ | 128K | ❌ | ★★☆☆☆ |
| **DeepSeek V3.2** | 2026 | ✅ Enhanced | ✅ | ✅ | ✅ | 128K | ✅ | ★★★★☆ |

**DeepSeek Series Harness Characteristics**:
- DeepSeek-V3 offers **exceptional cost-performance** ($0.27/$1.1 per 1M), suitable for cost-sensitive Harness deployments
- DeepSeek-R1 is **not recommended as a Harness engine**: tool calls are unstable, structured output is poor; suitable only for pure reasoning tasks
- DeepSeek V3.2 fixes tool-calling issues, SWE-bench 67.8%, usable for production Harness
- Chinese language capability ★★★★★, **the top open-source model choice for domestic-scenario Harness**

### 3.2 Alibaba Qwen Series

| Model | Version/Release Date | Function Calling | Structured Output | System Prompt | Streaming | Context Window | Parallel Tool Calls | Harness Readiness |
|------|-------------|-----------------|-------------------|---------------|-----------|-----------|------------|--------------|
| **Qwen2.5-72B-Instruct** | 2024-09 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 128K | ✅ | ★★★★☆ |
| **Qwen2.5-32B-Instruct** | 2024-09 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 128K | ✅ | ★★★★☆ |
| **Qwen2.5-14B-Instruct** | 2024-09 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 128K | ✅ | ★★★☆☆ |
| **Qwen2.5-7B-Instruct** | 2024-09 | ✅ Native | ⚠️ Not stable enough | ✅ | ✅ | 128K | ⚠️ Limited | ★★★☆☆ |
| **Qwen2.5-Coder-32B** | 2024-11 | ✅ Native | ✅ | ✅ | ✅ | 128K | ✅ | ★★★★☆ |
| **Qwen3-235B (MoE)** | 2025-04 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 128K | ✅ | ★★★★★ |
| **Qwen3-32B** | 2025-04 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 128K | ✅ | ★★★★☆ |
| **Qwen3.5-397B** | 2026-03 | ✅ Native | ✅ | ✅ | ✅ | 128K | ✅ | ★★★★★ |

**Qwen Series Harness Characteristics**:
- The Qwen3 series **natively supports the MCP protocol**, naturally matching the tool registration and discovery mechanism of the Harness Tools layer
- Qwen2.5-72B and Qwen3-235B are the **optimal choices for private-deployment Harness** (Chinese ★★★★★ + reliable tool calls)
- Models below 7B have insufficiently reliable tool calls; not recommended for production-grade Harness
- Qwen3.5-397B SWE-bench 76.4%, **the ceiling for open-source model Harness capability**
- Deepest integration with AgentScope when called via Alibaba Cloud Bailian API

### 3.3 Meta Llama Series

| Model | Version/Release Date | Function Calling | Structured Output | System Prompt | Streaming | Context Window | Parallel Tool Calls | Harness Readiness |
|------|-------------|-----------------|-------------------|---------------|-----------|-----------|------------|--------------|
| **Llama 3.3 70B** | 2024-12 | ✅ Native | ✅ | ✅ | ✅ | 128K | ✅ | ★★★★☆ |
| **Llama 3.1 405B** | 2024-07 | ✅ Native | ✅ | ✅ | ✅ | 128K | ✅ | ★★★★☆ |
| **Llama 3.1 70B** | 2024-07 | ✅ Native | ✅ | ✅ | ✅ | 128K | ✅ | ★★★★☆ |
| **Llama 3.1 8B** | 2024-07 | ⚠️ Limited | ⚠️ Unstable | ✅ | ✅ | 128K | ❌ | ★★☆☆☆ |
| **Llama 4 Scout (17B MoE)** | 2025-04 | ✅ Native | ✅ | ✅ | ✅ | 10M | ✅ | ★★★★☆ |
| **Llama 4 Maverick (17B MoE)** | 2025-04 | ✅ Native | ✅ | ✅ | ✅ | 1M | ✅ | ★★★★☆ |

**Llama Series Harness Characteristics**:
- Llama 4 Scout has a **10M context window**, making it the extreme choice for the Harness Context layer
- Llama 3.1 8B tool calls are not reliable enough; not recommended for use as the Harness main engine
- The Llama series **performs excellently in English scenarios**; Chinese language capability is weaker than Qwen/DeepSeek

### 3.4 Mistral Series

| Model | Version/Release Date | Function Calling | Structured Output | System Prompt | Streaming | Context Window | Parallel Tool Calls | Harness Readiness |
|------|-------------|-----------------|-------------------|---------------|-----------|-----------|------------|--------------|
| **Mistral Large 2** | 2024-07 | ✅ Native | ✅ JSON Mode | ✅ | ✅ | 128K | ✅ | ★★★★☆ |
| **Mistral Nemo (12B)** | 2024-07 | ✅ Native | ✅ | ✅ | ✅ | 128K | ✅ | ★★★☆☆ |
| **Mistral Small 3.1 (24B)** | 2025 | ✅ Native | ✅ | ✅ | ✅ | 128K | ✅ | ★★★★☆ |
| **Codestral (22B)** | 2024 | ✅ Native | ✅ | ✅ | ✅ | 32K | ✅ | ★★★☆☆ |

**Mistral Series Harness Characteristics**:
- Mistral's Function Calling implementation quality is high; **works out of the box with no special prompting required**
- Mistral Small 3.1 is a **great choice for lightweight Harness** (24B parameters, runnable on a single GPU)

### 3.5 Other Noteworthy Models

| Model | Vendor | Release Date | Function Calling | Context Window | Harness Readiness | Notes |
|------|------|---------|-----------------|-----------|--------------|------|
| **GLM-5** | Zhipu AI | 2026 | ✅ | 128K | ★★★★☆ | SWE-bench 77.8%, rising domestic contender |
| **Kimi K2.5** | Moonshot | 2026 | ✅ | 128K | ★★★★☆ | SWE-bench 76.8%, strong tool-calling capability |
| **MiniMax M2.5** | MiniMax | 2026 | ✅ | 128K | ★★★★☆ | SWE-bench 80.2%, promising open-source Harness candidate |
| **Step-3.5-Flash** | StepFun | 2026 | ✅ | 128K | ★★★☆☆ | SWE-bench 74.4%, strong reasoning capability |
| **Gemma 3 (27B)** | Google | 2025 | ⚠️ Limited | 128K | ★★☆☆☆ | Lightweight, limited tool-calling capability |
| **Phi-4 (14B)** | Microsoft | 2025 | ⚠️ Limited | 16K | ★★☆☆☆ | Edge-side model, small context window |

---

## 4. Harness Scenario Model Selection Recommendations

### 4.1 Selecting Models by Harness Layer Requirements

| Harness Layer Requirement | Recommended Model (API) | Recommended Model (Self-Hosted) | Reason |
|-----------------|----------------|------------------|------|
| **Loop Layer (High-Frequency Calls)** | GPT-4o-mini / Gemini 2.5 Flash | Qwen3-32B / Mistral Small 3.1 | Low latency + low cost + reliable tool calls |
| **Tools Layer (Complex Tool Orchestration)** | Claude Sonnet 4 / GPT-4.1 | Qwen3-235B / DeepSeek V3.2 | Highest tool selection accuracy |
| **Context Layer (Ultra-Long Context)** | Gemini 2.5 Pro (1M) / GPT-4.1 (1M) | Llama 4 Scout (10M) | Large context window |
| **Verification Layer (Self-Check Reasoning)** | Claude Opus 4 / o3 | DeepSeek-R1 (pure reasoning verification) | Deep reasoning + strong self-correction capability |
| **Constraints Layer (Instruction Following)** | GPT-4o / Claude Sonnet 4 | Qwen2.5-72B | Instruction following capability ★★★★★ |

### 4.2 Selecting Models by Deployment Scenario

| Scenario | Recommended Model | Alternative | Cost Reference |
|------|---------|------|---------|
| **Cloud API (Quick Start)** | Claude Sonnet 4 | GPT-4.1, Gemini 2.5 Pro | $3–15/1M tokens |
| **Cloud API (Cost-Sensitive)** | Gemini 2.5 Flash | GPT-4o-mini, DeepSeek-V3 | $0.1–0.6/1M tokens |
| **Private Deployment (Domestic Compliance)** | Qwen3-235B / Qwen2.5-72B | DeepSeek V3.2 | GPU cost (4–8×A100) |
| **Private Deployment (International)** | Llama 4 Maverick | Mistral Large 2 | GPU cost |
| **Lightweight / Edge Deployment** | Qwen3-32B | Mistral Small 3.1, Llama 3.3 70B | Single GPU / dual GPU |
| **K8s Ops Agent (Chinese)** | Qwen3-235B (API) | DeepSeek V3.2 | Self-hosted or Bailian API |
| **K8s Ops Agent (English)** | Claude Sonnet 4 | GPT-4.1 | API calls |

### 4.3 Multi-Model Routing Strategy (Harness Best Practices)

```
Harness Multi-Model Routing Architecture:

┌─────────────────────────────────────────────────────┐
│                   Model Router                       │
│                                                      │
│  Task Input → Complexity Assessment → Model Selection → Execution → Result │
│                                                      │
│  Routing Rules:                                      │
│                                                      │
│  ├── Simple queries / High-frequency calls           │
│  │   └── Gemini 2.5 Flash / GPT-4o-mini             │
│  │       Cost: ~$0.15/1M tokens, Latency: <0.5s     │
│  │                                                    │
│  ├── Medium complexity / Tool orchestration          │
│  │   └── Claude Sonnet 4 / GPT-4.1                  │
│  │       Cost: ~$3-5/1M tokens, Latency: ~1s        │
│  │                                                    │
│  ├── Deep reasoning / Complex analysis (latency-insensitive) │
│  │   └── Claude Opus 4 / o3 / DeepSeek-R1           │
│  │       Cost: ~$10-15/1M tokens, Latency: 5-60s    │
│  │                                                    │
│  └── Ultra-long context / Full log analysis          │
│      └── Gemini 2.5 Pro (1M) / Llama 4 Scout (10M) │
│          Suitable for diagnostic tasks requiring large context processing │
│                                                      │
│  Fallback Chain:                                     │
│  Primary Model → Fallback Model → Degraded Model    │
│  Claude Sonnet 4 → GPT-4.1 → Gemini 2.5 Flash      │
└─────────────────────────────────────────────────────┘
```

---

## 5. Models Not Supported / Not Recommended for Harness

| Model | Reason | Alternative Recommendation |
|------|------|---------|
| **DeepSeek-R1** | Unstable tool calls, poor structured output | Replace with DeepSeek-V3/V3.2; R1 is only suitable for pure reasoning verification in the Verification layer |
| **DeepSeek-R1-Distill Series** | Distilled models have even weaker tool-calling capability | Replace with Qwen3-32B or Llama 3.3 70B |
| **o1 (initial version)** | No parallel tool calls, system prompt restrictions | Upgrade to o3 or o4-mini |
| **Llama 3.1 8B** | Small-parameter model, unreliable tool calls | Use at least 70B or Llama 4 Scout |
| **Qwen2.5-7B** | Unstable structured output | Use at least 14B or 32B |
| **Phi-4 (14B)** | Context window only 16K, limited tool calls | Replace with Mistral Nemo 12B or Qwen3-32B |
| **Gemma 3 (27B)** | Limited tool-calling capability | Replace with Qwen3-32B or Mistral Small 3.1 |
| **Pure Embedding Models** | No generation capability | Use only for RAG retrieval; cannot drive Harness |

---

## 6. Version Evolution Timeline

```
2024–2026 Model Harness Support Evolution:

2024 Q2  GPT-4o                  ← First batch of mature Harness engines
         Claude 3.5 Sonnet

2024 Q3  Llama 3.1 (8B/70B/405B) ← Open-source model Function Calling matures
         Qwen2.5 Series
         Mistral Large 2

2024 Q4  Claude 3.5 Sonnet V2   ← Best SWE-bench score
         GPT-4o-mini
         DeepSeek-V3
         Llama 3.3 70B

2025 Q1  DeepSeek-R1             ← Strong reasoning but weak tool calls (not suitable as main Harness engine)
         Gemini 2.0 Flash
         o3-mini
         Claude 3.7 Sonnet

2025 Q2  GPT-4.1 Series (1M)    ← Major Harness engine upgrade: 1M context
         Gemini 2.5 Pro/Flash
         Claude Sonnet 4 / Opus 4
         o3 / o4-mini
         Qwen3 Series             ← Native MCP support
         Llama 4 Scout/Maverick   ← 10M context
         GPT-5

2025 H2
         GPT-5.2
         Claude 4.5 Sonnet

2026 Q1  Gemini 3.0 / 3.1 Pro   ← GPQA 94.3%
         Qwen3.5-397B            ← Open-source Harness capability ceiling
         DeepSeek V3.2           ← Tool-calling issues fixed
         GLM-5, Kimi K2.5        ← Domestic contenders rise
         Claude 4.6 Series
         Grok 4
         MiniMax M2.5            ← Open-source SWE-bench 80.2%

Trends:
  ✓ 2024: Function Calling moves from experimental to stable
  ✓ 2025: All top-tier models fully support Harness-required capabilities
  ✓ 2026: Harness capability gap between models narrows; Harness design matters more than model selection
```

---
## 7. AgentScope Framework Compatibility

When using Harness within the AgentScope framework, the matching relationship between models and Formatters:

| Model Provider | AgentScope Model Class | Formatter Class | Harness Ready |
|-----------|---------------------|-------------|-------------|
| Alibaba Cloud Bailian (Qwen) | `DashScopeChatModel` | `DashScopeChatFormatter` | ✅ Best Integration |
| OpenAI (GPT) | `OpenAIChatModel` | `OpenAIChatFormatter` | ✅ |
| Anthropic (Claude) | `AnthropicChatModel` | `AnthropicChatFormatter` | ✅ |
| Local Ollama | `OllamaChatModel` | `OllamaChatFormatter` | ✅ (model-dependent) |
| vLLM (OpenAI-compatible) | `OpenAIChatModel` | `OpenAIChatFormatter` | ✅ |

```python
# Switching different model-driven Harnesses in AgentScope
from agentscope.agent import ReActAgent

# Option 1: Alibaba Cloud Bailian (recommended for domestic use)
from agentscope.model import DashScopeChatModel
from agentscope.formatter import DashScopeChatFormatter

agent = ReActAgent(
    name="K8s-Expert",
    model=DashScopeChatModel(model_name="qwen-max", stream=True, ...),
    formatter=DashScopeChatFormatter(),
    ...
)

# Option 2: OpenAI
from agentscope.model import OpenAIChatModel
from agentscope.formatter import OpenAIChatFormatter

agent = ReActAgent(
    name="K8s-Expert",
    model=OpenAIChatModel(model_name="gpt-4.1", stream=True, ...),
    formatter=OpenAIChatFormatter(),
    ...
)

# Option 3: Self-hosted vLLM (OpenAI-compatible protocol)
agent = ReActAgent(
    name="K8s-Expert",
    model=OpenAIChatModel(
        model_name="qwen2.5-72b",
        base_url="http://vllm-service:8000/v1",
        stream=True,
        ...
    ),
    formatter=OpenAIChatFormatter(),
    ...
)
```

---

## Related Documents

| Document | Related Content |
|------|---------|
| [02 - LLM Foundation Model Selection and Evaluation](./02-llm-foundation-models.md) | Full-dimensional model performance comparison, cost analysis, deployment guide |
| [30 - Agent Harness Engineering](./30-agent-harness-engineering.md) | Harness six-layer architecture definition, model capability requirements |
| [32 - Harness Tool Engineering](./32-agent-harness-tool-engineering.md) | Tool layer Schema standards, Function Calling best practices |
| [38 - Harness Performance and Cost Optimization](./38-agent-harness-performance-cost.md) | Multi-model routing, cost control strategies |
| [41 - ReAct Agent and Harness Identification Guide](./41-react-harness-identification-guide.md) | Harness judgment criteria and maturity model |
| [17 - AgentScope Core Concepts](./17-agentscope-core-concepts.md) | Model and Formatter matching in AgentScope |

---

## References

| Source | Content | Date |
|------|------|------|
| Iternal Technologies | "The Definitive LLM Selection & Benchmarks Guide" 2026 Edition | 2026-03 |
| Creole Studios | "Top LLMs to Use in 2026" | 2025-12 |
| LMSYS Chatbot Arena | Arena Elo Leaderboard | 2026-03 |
| OpenAI | GPT-4.1 / o3 / GPT-5 series release documentation | 2025 |
| Anthropic | Claude Sonnet 4 / Opus 4 release documentation | 2025-05 |
| Google | Gemini 2.5 series release documentation | 2025-03 |
| Alibaba Cloud | Qwen3 / Qwen3.5 Technical Report | 2025-2026 |
| Birgitta Böckeler (Martin Fowler) | "Harness Engineering" | 2026-02 |

---

*This document is original content from the kudig-database project 02-ai-agents series, based on the latest industry data from 2025-2026, providing a complete reference list for model Harness compatibility.*

---

## Obsidian Related Documents

- 02-ai-agents KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|AI Agent Engineering Topics]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|AI Agent Fundamentals and Core Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|LLM Foundation Model Selection and Evaluation]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|In-Depth Comparison of Mainstream Agent Frameworks]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|RAG Retrieval-Augmented Generation In-Depth Guide]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Tool Use & Function Calling Design Specifications]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Multi-Agent Orchestration and Collaboration Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation Framework and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]

## See Also

- 40-agent-harness-production-maturity
- 41-react-harness-identification-guide
- 43-openclaw-framework-integration
- 44-openclaw-soul-mechanism


<!-- risk-assessed -->
