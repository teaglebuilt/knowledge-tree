---
title: Memory System (02-ai-agents)
description: 'description: KuDig Doctor Agent ’s Long-Term Memory System, storing cross-session experiences, patterns, and deterministic rules'
summary: 'description: KuDig Doctor Agent ’s Long-Term Memory System, storing cross-session experiences, patterns, and deterministic rules'
category: general
tags:
- ai
- ai-agent
- etcd
- prometheus
- grafana
- coredns
- hpa
- pdb
- ingress
- gateway
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- all engineers
estimated_read_time: 15min
intent_queries:
- what is the Memory System
- how does the Memory System work
- Kubernetes 14 ai ml infra best practices
trigger_keywords:
- Memory System
- ai
- ml
- infra
prerequisites:
- kubectl-basics
- prometheus-basics
- monitoring-basics
- etcd-basics
- gpu-scheduling-basics
- logging-basics
authors:
- name: Dillan Teagle
  role: contributor

original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/openclaw-workspace/MEMORY.md
---

> **production environment security tips**
>
> This document contains executable operational commands. Execute at your own risk: confirm that the target cluster and Namespace are correct; ensure you have sufficient RBAC permissions; verify these commands in a non-production environment first. Risk level annotations for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (modifies cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering, no side effects).




title: Memory System
description: KuDig Doctor Agent ’s Long-Term Memory System, storing cross-session experiences, patterns, and deterministic rules
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- [[etcd|etcd]]
- [[Prometheus|prometheus]]
- grafana
- [[CoreDNS|coredns]]
- hpa
last_updated: 2026-04
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Architects
- SRE
estimated_read_time: 5min
intent_queries:
- what is the Memory System
- how does the Memory System work
trigger_keywords:
- Memory System
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
# Memory System

## 1. Deterministic Rules (Manual Maintenance)

### 1.1 Baseline Cluster Environment

> Here is a template; please fill in the actual environment when using it.

```yaml
cluster_profiles:
  - name: "ack-prod-hangzhou"
    provider: ACK (阿里云容器服务)
    region: cn-hangzhou
    k8s_version: "1.28.x"
    node_count: 50
    node_pool:
      - name: system
        instance_type: ecs.g7.2xlarge
        count: 3
        role: master+etcd
      - name: app
        instance_type: ecs.g7.4xlarge
        count: 40
        role: worker
      - name: ai
        instance_type: ecs.gn7i-c16g1.4xlarge
        count: 7
        role: gpu-worker
    networking:
      cni: Terway
      service_cidr: 172.21.0.0/20
      pod_cidr: 172.22.0.0/16
    storage:
      default_sc: alicloud-disk-essd
      csi_driver: diskplugin.csi.alibabacloud.com
    monitoring:
      prometheus: true
      grafana: true
      loki: true
      alertmanager: true
    known_limits:
      max_pods_per_node: 110
      max_services: 10000
      etcd_quota: 8GB
```

### 1.2 Known Issues and Mitigation Strategies

```yaml
known_issues:
  - id: KI-001
    title: "Terway ENI 模式 Pod IP 分配延迟"
    symptoms:
      - "Pod 启动慢（>30s）"
      - "Events 中出现 'waiting for ENI' 相关信息"
    root_cause: "ENI 弹性网卡分配需要调用 ECS API，高峰期有延迟"
    workaround: "确认节点 ENI 余量，必要时预热 ENI 池"
    reference: "domain-10-troubleshooting-diagnostics/03-networking-cni-troubleshooting.md"
    discovered: 2026-01-15

  - id: KI-002
    title: "ESSD 云盘挂载 Multi-Attach 报错"
    symptoms:
      - "PVC 挂载失败"
      - "Events: 'Multi-Attach error for volume'"
    root_cause: "上一个 Pod 未正常释放卷，VolumeAttachment 残留"
    workaround: "检查并删除残留的 VolumeAttachment"
    reference: "domain-10-troubleshooting-diagnostics/14-pvc-storage-troubleshooting.md"
    discovered: 2026-02-20

  - id: KI-003
    title: "CoreDNS 5s 延迟问题（conntrack race condition）"
    symptoms:
      - "DNS 查询偶发 5 秒超时"
      - "约 1% 的 DNS 请求受影响"
    root_cause: "Linux conntrack 竞态条件导致 UDP DNS 包被丢弃"
    workaround: "CoreDNS 配置 force_tcp 或 Pod 使用 single-request-reopen"
    reference: "domain-10-troubleshooting-diagnostics/26-dns-troubleshooting.md"
    discovered: 2025-11-10
```

### 1.3 Team Agreements

```yaml
team_conventions:
  naming:
    - "Namespace 命名: {team}-{env}，如 payment-prod, order-staging"
    - "Deployment 命名: {app}-{component}，如 gateway-nginx, api-server"
    - "ConfigMap/Secret: {app}-{type}，如 api-server-config, api-server-tls"

  labeling:
    required_labels:
      - "app.kubernetes.io/name"
      - "app.kubernetes.io/version"
      - "app.kubernetes.io/managed-by"
      - "team"
      - "env"

  resource_policy:
    - "所有 Deployment 必须设置 requests 和 limits"
    - "CPU requests 不超过 limits 的 50%"
    - "Memory requests = limits（避免 OOM 场景下的不可预测行为）"
    - "所有生产 Deployment 必须设置 PDB"

  change_management:
    - "生产环境变更需要在工单系统中记录"
    - "大规模变更（影响 >10% 节点）需要审批"
    - "凌晨 02:00-06:00 为变更静默窗口"
```

## 2. Experience-Based Patterns (Agent Automatically Extracted)

### 2.1 Frequent Fault Patterns

```yaml
frequent_patterns:
  - pattern_id: FP-001
    title: "Java 应用 OOM — Heap 配置与容器 limits 不匹配"
    frequency: 12 次/月
    trigger: "Pod OOMKilled，退出码 137"
    root_cause: "JVM -Xmx 设置接近容器 memory limits，未留余量给非堆内存"
    effective_diagnosis_path:
      - "kubectl describe pod → 确认 OOMKilled"
      - "kubectl get pod -o jsonpath resources → 查看 limits"
      - "kubectl logs --previous → 查看 JVM GC 日志"
      - "计算: Xmx 应为 limits 的 70-80%"
    confidence: 高
    last_seen: 2026-03-28

  - pattern_id: FP-002
    title: "HPA 频繁扩缩导致服务抖动"
    frequency: 5 次/月
    trigger: "Pod 数量在短时间内频繁波动"
    root_cause: "HPA scaleDown stabilization 窗口太短，或 CPU 指标波动大"
    effective_diagnosis_path:
      - "kubectl get hpa -n <ns> → 确认当前状态"
      - "kubectl describe hpa → 查看 events 和 metrics"
      - "PromQL: 查看 CPU 利用率波动情况"
    confidence: 高
    last_seen: 2026-03-25

  - pattern_id: FP-003
    title: "Ingress 502 — 后端 Pod 未就绪"
    frequency: 8 次/月
    trigger: "Ingress 返回 502/503"
    root_cause: "readinessProbe 配置不当，Pod 还未就绪就被加入 Endpoints"
    effective_diagnosis_path:
      - "kubectl get endpoints <svc> → 确认 Endpoints 是否为空"
      - "kubectl get pods -l <selector> → 确认 Pod Ready 状态"
      - "kubectl describe pod → 检查 readinessProbe 配置"
    confidence: 高
    last_seen: 2026-04-01
```

### 2.2 Effective Diagnosis Paths

```yaml
effective_paths:
  - scenario: "Pod Pending + FailedScheduling"
    optimal_path:
      - "kubectl describe pod（看 Events，80% 情况下能直接定位）"
      - "kubectl get events --field-selector（补充事件信息）"
      - "kubectl top nodes（确认资源是否真的不足）"
    avg_steps: 3
    success_rate: 92%

  - scenario: "Node NotReady"
    optimal_path:
      - "kubectl describe node（看 Conditions，区分 Ready/Pressure/Network）"
      - "kubectl get events --field-selector involvedObject.name=<node>"
      - "kubectl top node（确认资源压力程度）"
    avg_steps: 3
    success_rate: 88%

  - scenario: "Service 不通"
    optimal_path:
      - "kubectl get endpoints（第一步！80% 问题在 Endpoints 为空）"
      - "kubectl get pods -l <selector>（确认 Pod 选择器匹配）"
      - "kubectl get networkpolicy（检查是否被 NetworkPolicy 拦截）"
    avg_steps: 3
    success_rate: 85%
```

### 2.3 Failure Cases and Lessons Learned

```yaml
lessons_learned:
  - id: LL-001
    date: 2026-02-15
    mistake: "直接建议客户调大 memory limits 解决 OOM"
    impact: "客户集群总资源不足，扩 limits 后其他 Pod 更容易被驱逐"
    lesson: "调整 limits 前必须检查节点剩余资源和集群整体容量"
    prevention: "SKILL.md OOM 修复决策树中增加集群容量检查步骤"

  - id: LL-002
    date: 2026-03-10
    mistake: "在诊断 DNS 问题时，没有先检查 CoreDNS Pod 是否正常"
    impact: "在应用层排查了 30 分钟才发现 CoreDNS 自己 CrashLoop"
    lesson: "DNS 诊断第一步永远是 kubectl get pods -n kube-system -l k8s-app=kube-dns"
    prevention: "SKILL.md DNS SOP 中将 CoreDNS 状态检查提到第一步"
```

## 3. User Preference Memory

```yaml
user_preferences:
  output_format:
    - "偏好表格形式展示对比数据"
    - "命令输出用代码块包裹"
    - "修复步骤用有序列表"

  frequently_used_commands:
    - "kubectl get pods -o wide -n <ns>"
    - "kubectl describe pod <pod> -n <ns>"
    - "kubectl top nodes"

  focus_areas:
    - "2026 Q2: 工单诊断效率、Agent 辅助诊断"
    - "关注 Terway 网络和 ESSD 存储相关问题"
```

## 4. Memory Metadata Management

```yaml
memory_metadata:
  total_entries: 15
  last_consolidation: 2026-04-01
  next_scheduled_consolidation: 2026-04-08

  retention_policy:
    confirmed_rules: "永久保留"
    high_confidence_patterns: "保留 6 个月，到期后降级或删除"
    medium_confidence_patterns: "保留 3 个月"
    low_confidence_patterns: "保留 1 个月，未被引用则自动删除"

  quality_metrics:
    avg_pattern_confidence: 0.82
    pattern_utilization_rate: 0.75  # 75% 的模式在近 30 天被引用过
    stale_entries: 2  # 超过 3 个月未被引用的条目数
```

---

*This document stores long-term memory for the Agent. Experience-based patterns are automatically extracted by the Agent, while deterministic rules are manually maintained. Regular reviews are conducted to maintain the quality of the memory.*

## Related

- [[domain-17-system-foundation/topic-cheat-sheet/go.md|[[Go Production Environment Quick Reference Card|go]]]]
- [[domain-17-system-foundation/topic-cheat-sheet/k8s.md|[[Kubernetes Production Environment Quick Reference Card|k8s]]]]
- [[entities/coredns.md|coredns]]

## See Also

- AGENTS
- IDENTITY
- SKILL
- SOUL


<!-- risk-assessed -->
