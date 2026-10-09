---
title: Coze Agent Platform
description: 'Coze(pin)Agentplatform architecture, multiAgentorchestration, plugin development, release channels and enterprise deployment'
summary: 'Coze(pin)Agentplatform architecture, multiAgentorchestration, plugin development, release channels and enterprise deployment'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- coze
- low-code
- workflow
tier: supporting
created: '2026-07-02'
last_updated: 2026-07
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- Platform Engineer
- Architect
estimated_read_time: 20min
intent_queries:
- What is Coze Agent Platform
- How to use Coze to build an Agent
- Coze Platform Architecture
- Coze Multi-Agent Orchestration
trigger_keywords:
- coze
- Coze
- agent platform
- low-code agent
- workflow
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/16-coze-agent-platform.md
---

# Coze Agent Platform

## Overview

Coze (Button) is an AI Agent development platform launched by ByteDance, positioning itself as a low-code Agent development tool. The platform packages the components required for Agent building—model invocation, knowledge base, plugins, workflows, and memory—into visual configuration items to reduce the barrier to Agent development. It supports the international version (coze.com) and the domestic version (coze.cn), respectively, to connect with different model ecosystems.

## 1. Platform Architecture

### 1.1 Core Components

```
┌─────────────────────────────────────────────────────────┐
│                    Coze 平台架构                          │
│                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐│
│  │   Bot    │  │  Plugin  │  │ Workflow │  │ 知识库   ││
│  │  (Agent) │  │  (插件)  │  │ (工作流) │  │ (RAG)   ││
│  │          │  │          │  │          │  │         ││
│  │ 人设     │  │ API调用  │  │ 逻辑编排 │  │ 文档    ││
│  │ 能力     │  │ 代码执行 │  │ 条件分支 │  │ 表格    ││
│  │ 提示词   │  │ 数据查询 │  │ 循环     │  │ 网页    ││
│  └──────────┘  └──────────┘  └──────────┘  └─────────┘│
│                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌─────────┐│
│  │  Memory  │  │ Database │  │ Variable │  │ 多Agent ││
│  │  (记忆)  │  │ (数据库) │  │ (变量)   │  │ (编排)  ││
│  └──────────┘  └──────────┘  └──────────┘  └─────────┘│
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │  发布渠道: 飞书/微信/Discord/Telegram/Web/API     │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### 1.2 Bot (Agent Entity)

Bot is a component of Coze, core configuration items:

```yaml
Bot配置:
  基础信息:
    name: "客服助手"
    description: "处理客户咨询"
    avatar: "avatar.png"

  模型选择:
    国际版: GPT-4o / Claude 3.5 / Gemini 1.5
    国内版: 豆包(Doubao) / 通义千问 / Kimi / DeepSeek

  人设与提示词:
    persona: |
      你是XX公司的客服助手，负责回答产品咨询。
      语气友好专业，遇到无法回答的问题转人工。
    system_prompt: |
      规则：
      1. 只回答产品相关问题
      2. 不透露内部信息
      3. 复杂问题使用工作流处理

  能力绑定:
    plugins:
      - product-search    # 产品搜索插件
      - order-query       # 订单查询插件
    workflows:
      - complaint-flow    # 投诉处理流程
    knowledge_bases:
      - product-docs      # 产品文档
      - faq-kb            # FAQ知识库
    memory:
      enabled: true
      window: 50          # 记忆窗口50轮
```

### 1.3 Model Configuration

```
模型选择策略:

国际版可用模型:
  - GPT-4o / GPT-4o-mini
  - Claude 3.5 Sonnet / Claude 3 Haiku
  - Gemini 1.5 Pro / Gemini 1.5 Flash
  - 豆包(Doubao)系列
  - DeepSeek系列

国内版可用模型:
  - 豆包(Doubao)系列（默认）
  - 通义千问系列
  - Kimi系列
  - DeepSeek系列
  - GLM系列
  - 百度文心系列

高级设置:
  temperature: 0.7          # 创造性
  max_tokens: 4096          # 最大输出
  top_p: 0.9               # 采样参数
  frequency_penalty: 0.0   # 频率惩罚
  presence_penalty: 0.0    # 存在惩罚
  stop_sequences: []       # 停止序列
```

## 2. Multi-Agent Orchestration Patterns

### 2.1 Agent-to-Agent Call

Coze supports calling other Bots within a Workflow for multi-Agent collaboration:

```
┌──────────────────────────────────────────┐
│         主Bot (客服总代理)                 │
│                                          │
│  ┌──────────────────────────────────┐   │
│  │          Workflow                 │   │
│  │                                   │   │
│  │  ┌─────────┐    ┌─────────────┐ │   │
│  │  │ 意图识别 │───→│ 条件路由     │ │   │
│  │  └─────────┘    └──────┬──────┘ │   │
│  │                        │         │   │
│  │         ┌──────────────┼──────┐ │   │
│  │         ▼              ▼      ▼ │   │
│  │  ┌──────────┐ ┌───────┐ ┌────┐│   │
│  │  │ 订单Bot  │ │ 技术Bot│ │FAQ ││   │
│  │  │(子Agent) │ │(子Agent)│ │Bot ││   │
│  │  └──────────┘ └───────┘ └────┘│   │
│  │         │              │      │ │   │
│  │         └──────────────┼──────┘ │   │
│  │                        ▼         │   │
│  │                 ┌──────────┐     │   │
│  │                 │ 结果汇总  │     │   │
│  │                 └──────────┘     │   │
│  └──────────────────────────────────┘   │
└──────────────────────────────────────────┘
```

### 2.2 Orchestration Patterns

```yaml
模式一: 串行链式
  描述: Agent A → Agent B → Agent C，依次处理
  适用: 多步骤流程，每步依赖上一步结果
  示例: 意图识别 → 信息提取 → 业务处理 → 结果生成

模式二: 并行扇出
  描述: 同时调用多个Agent，汇总结果
  适用: 多维度分析，独立子任务
  示例: 同时查询订单+产品+物流信息

模式三: 路由分发
  描述: 根据条件选择不同Agent处理
  适用: 不同场景需要不同专长Agent
  示例: 按意图路由到订单/技术/投诉Bot

模式四: 循环迭代
  描述: Agent反复执行直到满足条件
  适用: 需要多轮推理或迭代优化
  示例: 代码生成→测试→修复循环

模式五: 人工介入
  描述: 流程中暂停等待人工审批
  适用: 关键决策需人工确认
  示例: 退款审批→人工确认→执行退款
```

## 3. Plugin Development

### 3.1 Plugin Architecture

Coze plugins are divided into two types:

**Cloud Plugins**:
```
用户请求 → Coze Agent → Plugin API调用 → 外部服务
                                    ↓
                              结果返回Agent
```

**Local Plugins**:
- Written using Node.js or Python on the Coze platform
- No external server required
- Suitable for lightweight logic such as data processing and format conversion

### 3.2 Plugin Development Example

**Node.js Plugin**:

```javascript
// coze-plugin: Data analysis plugin
// Entry function
async function handler(event, context) {
  const { data, operation } = JSON.parse(event.body);

  switch (operation) {
    case 'summarize':
      return {
        statusCode: 200,
        body: JSON.stringify({
          summary: summarize(data),
          count: data.length,
          avg: data.reduce((a, b) => a + b, 0) / data.length
        })
      };

    case 'filter':
      const { field, value } = context.params;
      return {
        statusCode: 200,
        body: JSON.stringify({
          results: data.filter(item => item[field] === value)
        })
      };

    default:
      return {
        statusCode: 400,
        body: JSON.stringify({ error: 'Unknown operation' })
      };
  }
}

function summarize(data) {
  // Summary logic
  return {
    min: Math.min(...data),
    max: Math.max(...data),
    mean: data.reduce((a, b) => a + b, 0) / data.length
  };
}

module.exports = { handler };
```

**Python Plugin**:

```python
# coze-plugin: Text Processing Plugin
import json

def handler(event, context):
    body = json.loads(event['body'])
    text = body.get('text', '')
    operation = body.get('operation', '')

    if operation == 'extract_keywords':
        # Simple Keyword Extraction
        words = text.split()
        keywords = [w for w in words if len(w) > 3]
        return {
            'statusCode': 200,
            'body': json.dumps({
                'keywords': keywords[:10],
                'count': len(keywords)
            })
        }

    elif operation == 'sentiment':
        # Simple Sentiment Analysis
        positive_words = {'好', '棒', '喜欢', '满意', '优秀'}
        negative_words = {'差', '糟', '不满', '失望', '问题'}
        pos = sum(1 for w in text if w in positive_words)
        neg = sum(1 for w in text if w in negative_words)
        sentiment = 'positive' if pos > neg else 'negative' if neg > pos else 'neutral'
        return {
            'statusCode': 200,
            'body': json.dumps({
                'sentiment': sentiment,
                'confidence': abs(pos - neg) / max(pos + neg, 1)
            })
        }

    return {'statusCode': 400, 'body': json.dumps({'error': 'Unknown operation'})}
```

### 3.3 API Plugin Configuration

```yaml
# API Plugin Definition (OpenAPI Format)
openapi: 3.0.0
info:
  title: 产品搜索API
  version: 1.0.0
servers:
  - url: https://api.example.com
paths:
  /products/search:
    get:
      operationId: searchProducts
      summary: 搜索产品
      parameters:
        - name: keyword
          in: query
          required: true
          schema:
            type: string
          description: 搜索关键词
        - name: limit
          in: query
          schema:
            type: integer
            default: 10
      responses:
        '200':
          description: 搜索结果
          content:
            application/json:
              schema:
                type: object
                properties:
                  products:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: string
                        name:
                          type: string
                        price:
                          type: number
```

## 4. Workflow (Workflow)

### 4.1 Workflow Node Types

```
节点类型:

1. 开始节点
   - 输入参数定义
   - 触发条件

2. LLM节点
   - 选择模型
   - 自定义提示词
   - 输出格式化

3. 代码节点
   - Node.js / Python
   - 数据转换/计算
   - 外部API调用

4. 条件节点
   - if/else分支
   - 多条件表达式

5. 知识库节点
   - 检索指定知识库
   - 返回相关文档

6. 插件节点
   - 调用已配置的插件
   - 传入参数

7. 变量节点
   - 读写变量
   - 数据库操作

8. Bot节点
   - 调用其他Bot（子Agent）
   - 传入上下文

9. 结束节点
   - 输出结果定义
   - 输出格式
```

### 4.2 Workflow Example

```yaml
# Intelligent Customer Service Workflow
workflow:
  name: "智能客服处理流程"
  nodes:
    - id: start
      type: start
      outputs: [user_message, user_id]

    - id: intent
      type: llm
      model: doubao-pro
      prompt: |
        分析用户意图: {{user_message}}
        可选意图: order_query, product_info, complaint, other
        输出JSON: {"intent": "...", "confidence": 0.95}

    - id: route
      type: condition
      conditions:
        - if: "{{intent.intent}} == 'order_query'"
          goto: order_bot
        - if: "{{intent.intent}} == 'complaint'"
          goto: complaint_flow
        - default: faq_bot

    - id: order_bot
      type: bot
      bot_id: "order-query-bot"
      inputs:
        query: "{{user_message}}"
        user_id: "{{user_id}}"

    - id: complaint_flow
      type: workflow
      workflow_id: "complaint-handling"
      inputs:
        complaint: "{{user_message}}"
        user_id: "{{user_id}}"

    - id: faq_bot
      type: knowledge_base
      kb_id: "faq-knowledge-base"
      query: "{{user_message}}"

    - id: end
      type: end
      output: "{{result}}"
```

## 5. Release Channels

### 5.1 Channel Matrix

```yaml
发布渠道:

即时通讯:
  飞书:
    类型: 企业IM
    配置: OAuth应用授权
    特性: 富文本/卡片消息/群聊@提及
    适用: 企业内部助手

  微信:
    类型: 公众号/小程序
    配置: 微信开放平台
    特性: 公众号对话/小程序内嵌
    适用: C端用户服务

  Discord:
    类型: 社区IM
    配置: Discord Bot Token
    特性: 频道/线程/斜杠命令
    适用: 社区/游戏/开源项目

  Telegram:
    类型: 即时通讯
    配置: BotFather Token
    特性: 私聊/群组/内联查询
    适用: 海外用户/技术社区

  Slack:
    类型: 企业IM
    配置: Slack App
    特性: 频道/App Home/Block Kit
    适用: 海外企业

Web接入:
  Web Widget:
    类型: 网页嵌入
    配置: JavaScript SDK
    特性: 可定制UI/悬浮窗
    适用: 官网/应用内嵌

  API:
    类型: REST API
    配置: API Key
    特性: 完全控制/自定义前端
    适用: 自建应用集成

  分享链接:
    类型: 独立页面
    配置: 无需配置
    特性: 即开即用
    适用: 快速分享/测试
```

### 5.2 API Access Example

```python
# Coze API Access
import requests

class CozeClient:
    def __init__(self, bot_id, api_token):
        self.bot_id = bot_id
        self.api_token = api_token
        self.base_url = "https://api.coze.cn/v1"  # 国内版
        # self.base_url = "https://api.coze.com/v1"  # International Edition

    def chat(self, user_message, conversation_id=None):
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "bot_id": self.bot_id,
            "user": "user-001",
            "query": user_message,
            "stream": False
        }

        if conversation_id:
            payload["conversation_id"] = conversation_id

        response = requests.post(
            f"{self.base_url}/chat",
            headers=headers,
            json=payload
        )

        return response.json()

    def chat_stream(self, user_message, conversation_id=None):
        """Streamlined Output"""
        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "bot_id": self.bot_id,
            "user": "user-001",
            "query": user_message,
            "stream": True
        }

        response = requests.post(
            f"{self.base_url}/chat",
            headers=headers,
            json=payload,
            stream=True
        )

        for line in response.iter_lines():
            if line:
                yield line.decode('utf-8')

# Usage Examples
client = CozeClient(
    bot_id="your-bot-id",
    api_token="your-api-token"
)

result = client.chat("查询订单状态")
print(result)
```

## 6. Enterprise Deployment

### 6.1 Private Deployment Architecture

```
┌──────────────────────────────────────────────────┐
│            Coze Enterprise 私有化部署               │
│                                                    │
│  ┌──────────────────────────────────────────────┐│
│  │               Coze Platform                   ││
│  │  ┌──────┐ ┌──────┐ ┌──────┐ ┌──────────────┐││
│  │  │ Bot  │ │Plugin│ │  WF  │ │   Knowledge   │││
│  │  │Engine│ │Engine│ │Engine│ │    Engine     │││
│  │  └──────┘ └──────┘ └──────┘ └──────────────┘││
│  └──────────────────────────────────────────────┘│
│                                                    │
│  ┌──────────────────────────────────────────────┐│
│  │             模型接入层                         ││
│  │  ┌──────────┐ ┌──────────┐ ┌──────────────┐ ││
│  │  │ 豆包API  │ │ 私有模型  │ │ 第三方模型   │ ││
│  │  │          │ │(vLLM等)  │ │ (OpenAI等)   │ ││
│  │  └──────────┘ └──────────┘ └──────────────┘ ││
│  └──────────────────────────────────────────────┘│
│                                                    │
│  ┌──────────────────────────────────────────────┐│
│  │             基础设施层                         ││
│  │  K8s集群 / 对象存储 / 向量数据库 / 消息队列   ││
│  └──────────────────────────────────────────────┘│
└──────────────────────────────────────────────────┘
```

### 6.2 Enterprise Edition Features

```yaml
企业增强:
  私有化部署:
    - 部署到客户私有云/混合云
    - 数据完全隔离
    - 支持国产化环境（信创）

  安全合规:
    - SSO/LDAP集成
    - 细粒度权限控制
    - 数据脱敏
    - 操作审计日志
    - 内容审核策略定制

  运维管理:
    - 多租户管理
    - 用量监控与配额
    - 模型路由与负载均衡
    - 日志收集与分析

  集成能力:
    - 私有知识库对接
    - 内部系统API集成
    - 统一身份认证
    - 自定义发布渠道
```

## 7. Comparison with Dify

| Dimension | Coze | Dify |
|------|------|------|
| **Positioning** | Low-code Agent Platform | Open-source LLM Application Development Platform |
| **Deployment** | SaaS + Enterprise Edition Private Deployment | Self-hosted + Cloud |
| **Model Support** | Dobby/GPT/Claude/Gemini | 100+ Models (via API) |
| **Visualization Editing** | Excellent (Drag-and-Drop) | Good (Node-based) |
| **Workflow** | Built-in, complete functionality | Built-in, supports complex orchestration |
| **Knowledge Base** | Built-in RAG | Built-in RAG |
| **Plugin Ecosystem** | Rich (Official Market) | Moderate (Community Contributions) |
| **Release Channels** | WeChat/Flybook/Discord, etc. | API/Web/Embedded |
| **Multi-Agent** | Supported (Bot calling Bot) | Supported (Agent orchestration) |
| **Code Capability** | Limited (Node.js/Python sandbox) | More flexible (API/Code nodes) |
| **Open Source** | No | Yes (Apache 2.0) |
| **Pricing** | Free tier + paid | Open-source free / Cloud-paid |
| **Use Cases** | Quick chatbot building | Complex LLM application development |
| **Skill Level** | Low | Medium |
| **Customization Ability** | Platform-restricted | High (Source code modification possible) |

```
选型建议:

选择Coze:
  - 需要快速上线，不想自建基础设施
  - 主要面向聊天/客服场景
  - 需要飞书/微信等渠道直接发布
  - 团队技术能力有限

选择Dify:
  - 需要完全控制数据和部署
  - 有复杂的LLM应用需求
  - 需要深度定制和二次开发
  - 已有K8s运维能力
  - 对开源有要求
```

## Related Topics

- [[domain-14-ai-ml-infra/03-agent-runtime/15-cloud-agent-platforms|Cloud Agent Platform as a Service]]
- [[domain-14-ai-ml-infra/03-agent-runtime/17-agent-rate-limiting-cost-control|Agent Rate Limiting and Cost Control]]
- [[domain-14-ai-ml-infra/03-agent-runtime/21-agent-runtime-architecture-overview|Agent Runtime Architecture Overview]]

## References

- Coze Official Documentation
- Coze API Reference
- Dify GitHub
- Dify Official Documentation
