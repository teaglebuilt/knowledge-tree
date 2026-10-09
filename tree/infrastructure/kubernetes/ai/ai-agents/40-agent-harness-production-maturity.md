---
title: Agent Harness Production Operations and Maturity Model (domain-14-ai-ml-infra)
description: 'title: Agent Harness Production Operations and Maturity Model'
summary: 'title: Agent Harness Production Operations and Maturity Model'
category: general
tags:
- ai
- ai-agent
- production
- prometheus
- grafana
- helm
- redis
- postgresql
- gateway
- llm
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- all engineers
estimated_read_time: 25min
intent_queries:
- Agent Harness Production Operations and Maturity Model is what
- how Agent Harness Production Operations and Maturity Model
- Kubernetes 14 ai ml infra best practices
trigger_keywords:
- Agent
- Harness
- Production Operations and Maturity Model
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- helm-basics
- prometheus-basics
- monitoring-basics
- redis-basics
- logging-basics
authors:
- name: Dillan Teagle
  role: contributor
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/40-agent-harness-production-maturity.md
---

# Agent Harness Production Operations and Maturity Model

> **Document Type**: Harness Engineering Deep Dive Series | **Last Updated**: 2026-04 | **Keywords**: [[entities/k8s-production-operations.md|Production Operations]], Maturity Model, Gray Release, Capacity Planning, SLA, Fault Recovery, Version Management, Configuration Management, Self-evolution, Operational Automation

---

## Overview

Deploying the Agent Harness from the development environment to production is a qualitative transformation process that moves from "usable" to "reliable and controllable." Production-grade Harnesses need to handle traditional operational challenges such as high availability, gray-scale releases, version management, fault recovery, capacity planning, while also managing the non-deterministic behavior of Agents.

This article systematically elaborates on the path to production for Harness, strategies for gray-scale releases, version management, configuration hot updates, fault recovery, SLA design, and the implementation guide for the Harness maturity model with five levels.

---

## 1. Production Deployment Architecture

## 1.1 Deployment Topology

```
# 🟢 Low Risk: Read-only/information collection, typically with no side effects
Agent Harness 生产部署拓扑:

┌─────────────────────────────────────────────────────────┐
│                     入口层（Gateway）                     │
│  API Gateway │ 认证鉴权 │ 限流 │ 路由                    │
├─────────────────────────────────────────────────────────┤
│                   Harness 服务层                          │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐      │
│  │ Harness v2.1│  │ Harness v2.0│  │ Harness v1.9│      │
│  │ (Canary 5%) │  │ (Stable 95%)│  │ (Rollback)  │      │
│  └─────────────┘  └─────────────┘  └─────────────┘      │
├─────────────────────────────────────────────────────────┤
│                   LLM 提供商层                            │
│  OpenAI API │ Anthropic API │ Azure OpenAI │ 本地模型    │
├─────────────────────────────────────────────────────────┤
│                   工具执行层                              │
│  kubectl │ Prometheus │ Loki │ Helm │ 自定义工具          │
├─────────────────────────────────────────────────────────┤
│                   数据层                                  │
│  Redis（缓存）│ Milvus（向量）│ PostgreSQL（审计）        │
├─────────────────────────────────────────────────────────┤
│                   可观测性层                              │
│  OTel Collector │ Prometheus │ Grafana │ Langfuse        │
└─────────────────────────────────────────────────────────┘
```
## 1.2 Kubernetes Deployment Manifests

```yaml
# harness-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: agent-harness
  namespace: agent-system
  labels:
    app: agent-harness
    version: v2.1
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1
      maxUnavailable: 0
  selector:
    matchLabels:
      app: agent-harness
  template:
    metadata:
      labels:
        app: agent-harness
        version: v2.1
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/port: "8080"
        prometheus.io/path: "/metrics"
    spec:
      containers:
      - name: harness
        image: agent-harness:v2.1
        ports:
        - containerPort: 8080
          name: http
        - containerPort: 8081
          name: metrics
        env:
        - name: HARNESS_VERSION
          value: "v2.1"
        - name: HARNESS_CONFIG_PATH
          value: "/config/harness-config.yaml"
        - name: OTEL_EXPORTER_OTLP_ENDPOINT
          value: "http://otel-collector:4317"
        - name: LANGFUSE_HOST
          value: "http://langfuse:3000"
        envFrom:
        - secretRef:
            name: llm-api-keys
        resources:
          requests:
            cpu: 500m
            memory: 1Gi
          limits:
            cpu: 2000m
            memory: 4Gi
        livenessProbe:
          httpGet:
            path: /healthz
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 30
        readinessProbe:
          httpGet:
            path: /readyz
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 10
        volumeMounts:
        - name: config
          mountPath: /config
        - name: soul-skill
          mountPath: /harness/prompts
      volumes:
      - name: config
        configMap:
          name: harness-config
      - name: soul-skill
        configMap:
          name: harness-prompts
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: harness-config
  namespace: agent-system
data:
  harness-config.yaml: |
    harness:
      version: v2.1
      loop:
        max_iterations: 15
        timeout_seconds: 300
      constraints:
        read_only: true
        max_tokens_per_task: 50000
        max_cost_per_task_usd: 2.0
        blocked_namespaces:
          - kube-system
          - kube-public
      verification:
        min_faithfulness: 0.85
        require_evidence: true
      model:
        default: gpt-4o
        fallback: gpt-4o-mini
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: harness-prompts
  namespace: agent-system
data:
  SOUL.md: |
    你是 K8S 运维诊断专家。
    你只能使用授权的工具进行信息收集。
    生产环境中禁止执行任何写操作。
    每个诊断结论必须引用具体的 Event 或日志证据。
  SKILL.md: |
    Pod Pending 诊断流程:
    1. kubectl describe pod → 检查 Events
    2. kubectl get events → 检查调度事件
    3. kubectl get nodes → 检查节点资源
    4. kubectl top nodes → 确认资源使用率
```

---

## 2. Gray-Scale Release Strategies

## 2.1 Four-Stage Gray-Scale Release

```
Harness 灰度发布四阶段:

Stage 1: Shadow Mode（影子模式）
  时间: 24-48h
  策略: 新旧 Harness 并行运行，新版不生效
  监控: 对比两个版本的输出质量
  退出条件:
    - 新版质量 >= 旧版质量 - 2%
    - 无安全问题

Stage 2: Canary（金丝雀）
  时间: 48h
  策略: 5% 流量切到新 Harness
  监控:
    - 任务成功率
    - 验证通过率
    - 延迟 P95
    - Token 消耗
    - 成本
  退出条件:
    - 所有指标不低于旧版 5%
    - 无约束违反
    - 无安全事件

Stage 3: Progressive Rollout（渐进发布）
  时间: 每阶段 24h
  策略: 5% → 25% → 50% → 75%
  监控: 同 Canary，每阶段至少 24h
  回滚条件:
    - 任何阶段任一指标退化 > 5%
    - 检测到安全事件
    - 约束违反率 > 0

Stage 4: Full Rollout（全量发布）
  时间: 24h 观察期
  策略: 100% 流量切到新版
  监控: 持续 24h 全量监控
  确认: 保留旧版 72h 用于回滚
```

## 2.2 Gray-Scale Controller

```python
class GrayReleaseController:
    """Gray-Scale Release Controller"""

    def __init__(self, metrics_collector, alert_manager):
        self.metrics = metrics_collector
        self.alerts = alert_manager
        self.current_stage = "shadow"
        self.traffic_ratio = 0.0
        self.stage_start_time = None

    STAGES = {
        "shadow": {"traffic": 0.0, "duration_hours": 24, "next": "canary"},
        "canary": {"traffic": 0.05, "duration_hours": 48, "next": "progressive_25"},
        "progressive_25": {"traffic": 0.25, "duration_hours": 24, "next": "progressive_50"},
        "progressive_50": {"traffic": 0.50, "duration_hours": 24, "next": "progressive_75"},
        "progressive_75": {"traffic": 0.75, "duration_hours": 24, "next": "full"},
        "full": {"traffic": 1.0, "duration_hours": 24, "next": None},
    }

    def advance_stage(self) -> dict:
        """Advance to the next stage"""
        stage_config = self.STAGES[self.current_stage]

        # Check security conditions
        safety_check = self._check_safety_conditions()
        if not safety_check["safe"]:
            return {
                "action": "hold",
                "reason": safety_check["reason"],
                "current_stage": self.current_stage,
            }

        # Check quality conditions
        quality_check = self._check_quality_conditions()
        if not quality_check["passed"]:
            return {
                "action": "rollback",
                "reason": quality_check["reason"],
                "current_stage": self.current_stage,
            }

        # Advance
        next_stage = stage_config["next"]
        if next_stage:
            self.current_stage = next_stage
            self.traffic_ratio = self.STAGES[next_stage]["traffic"]
            self.stage_start_time = time.time()
            return {
                "action": "advanced",
                "new_stage": next_stage,
                "traffic_ratio": self.traffic_ratio,
            }
        else:
            return {"action": "complete", "stage": "full"}

    def rollback(self, reason: str) -> dict:
        """Rollback to stable version"""
        self.current_stage = "shadow"
        self.traffic_ratio = 0.0
        self.alerts.send_alert(
            severity="critical",
            message=f"Harness 灰度回滚: {reason}",
        )
        return {"action": "rollback", "reason": reason}

    def _check_safety_conditions(self) -> dict:
        """Check security conditions"""
        violations = self.metrics.get_constraint_violations(
            window="1h"
        )
        if violations > 0:
            return {"safe": False, "reason": f"检测到 {violations} 次约束违反"}

        injection_attempts = self.metrics.get_injection_attempts(
            window="1h"
        )
        if injection_attempts > 5:
            return {"safe": False, "reason": "注入攻击频繁"}

        return {"safe": True}

    def _check_quality_conditions(self) -> dict:
        """Check quality conditions"""
        new_metrics = self.metrics.get_version_metrics("new")
        old_metrics = self.metrics.get_version_metrics("old")

        if not new_metrics or not old_metrics:
            return {"passed": True}

        # Success rate not less than 5% of the old version
        if new_metrics.get("success_rate", 0) < old_metrics.get("success_rate", 0) - 0.05:
            return {
                "passed": False,
                "reason": f"成功率退化: {new_metrics['success_rate']:.2%} < "
                         f"{old_metrics['success_rate']:.2%} - 5%",
            }

        # Verification pass rate not less than the old version
        if new_metrics.get("verification_rate", 0) < old_metrics.get("verification_rate", 0) - 0.05:
            return {
                "passed": False,
                "reason": "验证通过率退化",
            }

        return {"passed": True}
```

---

## 3. Configuration Management and Hot Updates

## 3.1 Configuration Hot Update Mechanism

```python
import yaml
import hashlib
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class HarnessConfigManager:
    """Harness Configuration Manager: Supports Hot Updates"""

    def __init__(self, config_path: str):
        self.config_path = config_path
        self._config: dict = {}
        self._config_hash: str = ""
        self._callbacks: list = []
        self._load_config()

    def _load_config(self):
        """Load Configuration"""
        with open(self.config_path) as f:
            new_config = yaml.safe_load(f)
        new_hash = hashlib.md5(
            yaml.dump(new_config).encode()
        ).hexdigest()

        if new_hash != self._config_hash:
            old_config = self._config
            self._config = new_config
            self._config_hash = new_hash

            # Trigger Callback
            for callback in self._callbacks:
                callback(old_config, new_config)

    def get(self, key: str, default=None):
        """Get Configuration Value (Supports Dot-Delimited Paths)"""
        keys = key.split(".")
        value = self._config
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return default
        return value

    def on_change(self, callback):
        """Register Configuration Change Callback"""
        self._callbacks.append(callback)

    def start_watching(self):
        """Start File Monitoring (Triggered on ConfigMap Mount Updates)"""
        handler = ConfigFileHandler(self._load_config)
        observer = Observer()
        observer.schedule(handler, path=self.config_path, recursive=False)
        observer.start()


class ConfigFileHandler(FileSystemEventHandler):
    def __init__(self, reload_fn):
        self.reload_fn = reload_fn

    def on_modified(self, event):
        self.reload_fn()
```

## 3.2 Prompt Version Management

```python
class PromptVersionManager:
    """Prompt Version Manager"""

    def __init__(self, storage_backend):
        self.storage = storage_backend

    def save_version(self, name: str, content: str,
                     metadata: dict = None) -> str:
        """Save New Version of Prompt"""
        version_id = f"{name}_v{int(time.time())}"
        self.storage.save(version_id, {
            "name": name,
            "content": content,
            "metadata": metadata or {},
            "created_at": datetime.utcnow().isoformat(),
            "hash": hashlib.md5(content.encode()).hexdigest(),
        })
        return version_id

    def get_version(self, name: str, version: str = "latest") -> dict:
        """Get Prompt Version"""
        if version == "latest":
            return self.storage.get_latest(name)
        return self.storage.get(f"{name}_{version}")

    def rollback(self, name: str, target_version: str) -> dict:
        """Rollback to a Specific Version"""
        target = self.get_version(name, target_version)
        if not target:
            return {"success": False, "error": "版本不存在"}
        self.save_version(
            name, target["content"],
            metadata={"rollback_from": "latest",
                       "rollback_to": target_version},
        )
        return {"success": True, "restored_version": target_version}

    def diff(self, name: str, v1: str, v2: str) -> dict:
        """Compare Two Versions"""
        version1 = self.get_version(name, v1)
        version2 = self.get_version(name, v2)
        import difflib
        diff = list(difflib.unified_diff(
            version1["content"].splitlines(),
            version2["content"].splitlines(),
            fromfile=f"{name}@{v1}",
            tofile=f"{name}@{v2}",
        ))
        return {"diff": "\n".join(diff), "v1": v1, "v2": v2}
```

---

## 4. Service Level Agreement Design

## 4.1 Agent Harness SLA System

```
Agent Harness SLA 指标:

可用性 SLA:
  目标: 99.9%（每月最多 43 分钟不可用）
  计算: 成功响应的请求 / 总请求
  排除: 计划内维护、LLM 提供商问题

质量 SLA:
  任务完成率: > 90%
  验证通过率: > 85%
  幻觉率: < 5%
  安全事件: 0 次 / 月

性能 SLA:
  P50 延迟: < 10 秒
  P95 延迟: < 30 秒
  P99 延迟: < 60 秒

成本 SLA:
  单任务平均成本: < $1.00
  日成本上限: 可配置
  Token 预算执行: 100% 生效
```

## 4.2 SLA Monitoring

```python
class SLAMonitor:
    """SLA Monitor"""

    def __init__(self, metrics_collector):
        self.metrics = metrics_collector
        self.sla_targets = {
            "availability": 0.999,
            "task_completion_rate": 0.90,
            "verification_pass_rate": 0.85,
            "hallucination_rate": 0.05,  # 上界
            "p50_latency_seconds": 10,
            "p95_latency_seconds": 30,
        }

    def check_sla(self, period: str = "24h") -> dict:
        """Check SLA Compliance"""
        actuals = self.metrics.get_sla_metrics(period)
        results = []

        for metric, target in self.sla_targets.items():
            actual = actuals.get(metric, 0)
            is_upper_bound = metric in ("hallucination_rate",
                                         "p50_latency_seconds",
                                         "p95_latency_seconds")

            if is_upper_bound:
                met = actual <= target
            else:
                met = actual >= target

            results.append({
                "metric": metric,
                "target": target,
                "actual": actual,
                "met": met,
                "margin": abs(actual - target),
            })

        all_met = all(r["met"] for r in results)
        return {
            "period": period,
            "sla_met": all_met,
            "results": results,
            "violations": [r for r in results if not r["met"]],
        }
```

---

## 5. Fault Recovery

## 5.1 Fault Recovery Strategy

```python
class HarnessFailoverManager:
    """Harness Fault Recovery Manager"""

    def __init__(self, primary_harness, fallback_harness,
                 health_checker):
        self.primary = primary_harness
        self.fallback = fallback_harness
        self.health = health_checker
        self.active = "primary"

    async def execute_with_failover(self, task: str, context: dict) -> dict:
        """Fault Tolerant Execution"""
        if self.active == "primary":
            try:
                # Health Check
                if not await self.health.check(self.primary):
                    self._switch_to_fallback("健康检查失败")
                    return await self._execute_fallback(task, context)

                result = await self.primary.async_run(task, context)

                # Result Quality Check
                if result.get("status") == "error":
                    self._switch_to_fallback("执行错误")
                    return await self._execute_fallback(task, context)

                return result

            except Exception as e:
                self._switch_to_fallback(str(e))
                return await self._execute_fallback(task, context)
        else:
            return await self._execute_fallback(task, context)

    async def _execute_fallback(self, task: str, context: dict) -> dict:
        """Degraded Harness Execution"""
        result = await self.fallback.async_run(task, context)
        result["_failover"] = True
        result["_failover_reason"] = "primary harness unavailable"
        return result

    def _switch_to_fallback(self, reason: str):
        """Switch to Backup Harness"""
        self.active = "fallback"
        logger.warning(f"切换到备用 Harness: {reason}")

    def recover_primary(self):
        """Recover Primary Harness"""
        if self.health.check_sync(self.primary):
            self.active = "primary"
            logger.info("主 Harness 恢复")
```

## 5.2 LLM Disaster Recovery

```python
class LLMProviderFailover:
    """LLM Disaster Recovery"""

    def __init__(self, providers: list[dict]):
        self.providers = providers  # 按优先级排序
        self.current_index = 0
        self.failure_counts: dict[str, int] = {}

    async def invoke(self, prompt: str, **kwargs) -> dict:
        """Disaster Tolerant LLM Calls"""
        for i, provider in enumerate(self.providers):
            name = provider["name"]
            try:
                result = await provider["client"].ainvoke(prompt, **kwargs)
                # Reset failure count on success
                self.failure_counts[name] = 0
                return {"result": result, "provider": name}
            except Exception as e:
                self.failure_counts[name] = self.failure_counts.get(name, 0) + 1
                logger.warning(f"LLM 提供商 {name} 失败 ({self.failure_counts[name]}次): {e}")

                if i < len(self.providers) - 1:
                    continue  # 尝试下一个
                else:
                    raise Exception(f"所有 LLM 提供商不可用: {[p['name'] for p in self.providers]}")

    def get_health_status(self) -> dict:
        """Get Provider Health Status"""
        return {
            p["name"]: {
                "recent_failures": self.failure_counts.get(p["name"], 0),
                "healthy": self.failure_counts.get(p["name"], 0) < 3,
            }
            for p in self.providers
        }
```

---

## 6. Mature Model Implementation Guide

## 6.1 Five Levels of Maturity Detailed Definitions

```
Agent Harness 成熟度五级:

L1 - 裸 Agent（Ad-hoc）
  特征:
    - 直接调用 LLM API
    - 无循环、无工具、无验证
    - 手动触发，手动查看结果
  风险: 幻觉率高、不可控、无审计
  适用: PoC 验证阶段
  
  升级到 L2 的关键动作:
    □ 实现基础 Agent Loop
    □ 接入至少 2 个工具
    □ 添加超时保护

L2 - 基础 Harness（Managed）
  特征:
    - 有 Agent Loop + 基本工具调用
    - 有超时和迭代限制
    - 但无验证、无约束、无持久化
  风险: 输出质量不稳定、无安全边界
  适用: 内部工具、非关键场景
  
  升级到 L3 的关键动作:
    □ 添加验证层（至少 3 个验证器）
    □ 实现约束层（只读+命令黑名单）
    □ 添加基本的 Prometheus 指标
    □ 建立 CI/CD 质量门禁

L3 - 生产就绪 Harness（Production-Ready）
  特征:
    - 六层架构完整
    - 有 CI/CD 质量门禁
    - 有基本监控和告警
    - 有基线对比和回归检测
  风险: 单点问题、扩展性有限
  适用: 生产级诊断 Agent、运维助手
  
  升级到 L4 的关键动作:
    □ 实现多 Agent 编排
    □ 部署灰度发布流程
    □ 完整 OTel + Langfuse 可观测性
    □ 实现 A/B 测试框架
    □ 部署红队测试

L4 - 企业级 Harness（Enterprise）
  特征:
    - 多 Agent 编排 + 分层 Harness
    - 灰度发布 + A/B 测试
    - 完整可观测性
    - 红队测试通过
    - LLM 提供商容灾
  风险: 运维复杂度高
  适用: 企业 AIOps 平台、核心业务系统
  
  升级到 L5 的关键动作:
    □ 实现 Meta-Agent 自动优化 Harness
    □ 自动调整工具集和上下文策略
    □ 失败模式自动学习和适应
    □ 跨任务知识迁移

L5 - 自进化 Harness（Self-Evolving）
  特征:
    - Harness 配置由 Meta-Agent 自动优化
    - 自动调整工具集、上下文策略、约束参数
    - 从失败中自动学习并改进
    - 跨集群/跨场景知识迁移
  风险: 控制复杂度（需要元约束层）
  适用: 下一代自适应 Agent 平台（前沿研究）
```

## 6.2 Maturity Assessment Checklist

```python
class MaturityAssessment:
    """Harness Maturity Assessment"""

    CHECKLIST = {
        "L1": [
            ("有 LLM 调用", True),
        ],
        "L2": [
            ("有 Agent Loop", True),
            ("有工具调用（>=2 个工具）", True),
            ("有超时保护", True),
            ("有最大迭代限制", True),
        ],
        "L3": [
            ("有验证层（>=3 个验证器）", True),
            ("有约束层（只读+黑名单）", True),
            ("有上下文管理（分层构建）", True),
            ("有持久化（执行记录持久存储）", True),
            ("有 Prometheus 指标", True),
            ("有 CI/CD 质量门禁", True),
            ("有基线对比", True),
            ("有基本告警规则", True),
        ],
        "L4": [
            ("有多 Agent 编排", True),
            ("有灰度发布流程", True),
            ("有 A/B 测试", True),
            ("有 OTel 全链路追踪", True),
            ("有 Langfuse 集成", True),
            ("有红队测试", True),
            ("有 LLM 提供商容灾", True),
            ("有 SLA 监控", True),
            ("有配置热更新", True),
            ("有 Prompt 版本管理", True),
        ],
        "L5": [
            ("有 Meta-Agent 自优化", True),
            ("有自动工具集调整", True),
            ("有失败模式自动学习", True),
            ("有跨场景知识迁移", True),
        ],
    }

    def assess(self, harness_capabilities: dict) -> dict:
        """Assess Maturity Level"""
        achieved_level = "L1"

        for level in ["L1", "L2", "L3", "L4", "L5"]:
            items = self.CHECKLIST[level]
            met = all(
                harness_capabilities.get(item[0], False)
                for item in items
            )
            if met:
                achieved_level = level
            else:
                break

        return {
            "current_level": achieved_level,
            "next_level": self._next_level(achieved_level),
            "gap_analysis": self._gap_analysis(achieved_level,
                                                harness_capabilities),
        }

    def _next_level(self, current: str) -> str:
        levels = ["L1", "L2", "L3", "L4", "L5"]
        idx = levels.index(current)
        return levels[idx + 1] if idx < len(levels) - 1 else "L5 (已达最高)"

    def _gap_analysis(self, current: str, capabilities: dict) -> list:
        """Gap Analysis: List the capabilities needed to upgrade to the next level"""
        next_level = self._next_level(current)
        if next_level.startswith("L5 "):
            return []

        items = self.CHECKLIST[next_level]
        gaps = []
        for item_name, _ in items:
            if not capabilities.get(item_name, False):
                gaps.append(item_name)
        return gaps
```

---

## 7. Best Practices

## 7.1 Core Principles of Production Operations

| Principle | Explanation | Practice Suggestions |
|------|------|---------|
| **Rollout First** | New Harness must undergo rollout validation | Four-stage rollout |
| **Rollbackable** | Any change can be quickly rolled back | Retain N-2 versions |
| **Separate Configuration** | Prompts and code are managed separately | ConfigMap + hot update |
| **Disaster Recovery Design** | Have a downgrade solution when LLM providers are unavailable | Multi-provider disaster recovery |
| **SLA Driven** | Have clear quality and performance targets | SLA monitoring + alerts |
| **Gradual Maturity** | Gradually improve based on maturity model | L1→L2→L3 gradual upgrade |

## 7.2 Anti-patterns

| Anti-pattern | Problem | Correct Approach |
|--------|------|----------|
| **Full Rollout Directly** | Quality of new Harness not verified | Four-stage rollout |
| **Hardcoded Prompts** | Modifications require redeployment | ConfigMap + hot update |
| **Single LLM Provider** | Provider issues = complete paralysis | Multi-provider disaster recovery |
| **No Version Management** | Changes to Prompts cannot be traced | Version management + diff |
| **Skipping Maturity Levels** | Foundation unstable, advanced features unreliable | Gradually build from L1 to L5 |

---

## Related Documents

| Document | Relevant Content |
|------|--------|
| [30 - Agent Harness Engineering](./30-agent-harness-engineering.md) | Overview of the Maturity Model |
| [34 - Verification and Quality Gates](./34-agent-harness-verification-quality.md) | CI/CD Quality Gates and Rollout Evaluation |
| [36 - Observability](./observability.md|36-agent-harness-observability]].md) | Production Monitoring and Alerting System |
| [09 - Production Deployment Guide](./09-production-deployment-guide.md) | K8S Deployment Infrastructure |

---

## References

| Source | Content | Date |
|------|------|------|
| Anthropic | Agent Production Deployment Best Practices | 2026-02 |
| Martin Fowler / Birgitta Böckeler | Harness Engineering Production Guide | 2026-02 |
| Google SRE | SLA/SLO/SLI Framework | Ongoing Updates |
| LangChain | Agent Gradual Release Practice | 2026-02 |

---

*This document is original content from the kudig-database project series 02-ai-agents, delving into the production operation and maturity model of Agent Harness.*

---

## Related Obsidian Documents

- 02-ai-agents MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|AI Agent Engineering Special Topic]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|AI Agent Fundamentals and Core Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|LLM Foundation Model Selection and Evaluation]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|Deep Comparison of Mainstream Agent Frameworks]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|Deep Guide to Retrieval-Augmented Generation (RAG)]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Design Guidelines for Tool Usage and Function Calling]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Deep Architecture of Multi-Agent Orchestration and Collaboration]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Engineering Memory Management and Context Window]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Deep Framework for Agent Evaluation and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]

## See Also

- 38-agent-harness-performance-cost
- 39-agent-harness-testing-benchmark
- 41-react-harness-identification-guide
- 42-model-harness-compatibility-matrix


<!-- risk-assessed -->
