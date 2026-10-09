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
    title: "Terway ENI Mode Pod IP Allocation Delay"
    symptoms:
      - "Pod startup slow ( >30s )"
      - "Events appears 'waiting for ENI' related information"
    root_cause: "ENI elastic network interface allocation needs to call the ECS API, there is a delay during peak hours"
    workaround: "Confirm ENI capacity of the node, preheat the ENI pool if necessary"
    reference: "domain-10-troubleshooting-diagnostics/03-networking-cni-troubleshooting.md"
    discovered: 2026-01-15

  - id: KI-002
    title: "ESSD Cloud Disk Mount Multi-Attach Error"
    symptoms:
      - "PVC Mount Failed"
      - "Events: 'Multi-Attach error for volume'"
    root_cause: "Previous Pod did not release the volume normally, VolumeAttachment residue"
    workaround: "Check and delete residual VolumeAttachment"
    reference: "domain-10-troubleshooting-diagnostics/14-pvc-storage-troubleshooting.md"
    discovered: 2026-02-20

  - id: KI-003
    title: "CoreDNS 5s Delay Issue (conntrack race condition)"
    symptoms:
      - "DNS Query occasional 5-second timeout"
      - "about 1% of DNS requests were affected"
    root_cause: "Linux conntrack race condition causes UDP DNS packets to be dropped"
    workaround: "CoreDNS configuration force_tcp or Pod uses single-request-reopen"
    reference: "domain-10-troubleshooting-diagnostics/26-dns-troubleshooting.md"
    discovered: 2025-11-10
```

### 1.3 Team Agreements

```yaml
team_conventions:
  naming:
    - "Namespace Name: {team}-{env}, such as payment-prod, order-staging"
    - "Deployment Name: {app}-{component}, such as gateway-nginx, api-server"
    - "ConfigMap/Secret: {app}-{type}, such as api-server-config, api-server-tls"

  labeling:
    required_labels:
      - "app.kubernetes.io/name"
      - "app.kubernetes.io/version"
      - "app.kubernetes.io/managed-by"
      - "team"
      - "env"

  resource_policy:
    - "All Deployments must set requests and limits"
    - "CPU requests do not exceed limits by 50%"
    - "Memory requests = limits (avoid unpredictable behavior in OOM scenarios)"
    - "All production Deployments must set PDB"

  change_management:
    - "Changes in production environment need to be recorded in the work order system"
    - "Major changes (affecting more than 10% of nodes) require approval"
    - "From 02:00 to 06:00 AM is a silent window for changes"
```

## 2. Experience-Based Patterns (Agent Automatically Extracted)

### 2.1 Frequent Fault Patterns

```yaml
frequent_patterns:
  - pattern_id: FP-001
    title: "Java Application OOM — Heap Configuration and Container Limits Do Not Match"
    frequency: 12 次/月
    trigger: "Pod OOMKilled, exit code 137"
    root_cause: "JVM -Xmx set close to container memory limits, leaving insufficient space for non-heap memory"
    effective_diagnosis_path:
      - "kubectl describe pod → Confirm OOMKilled"
      - "kubectl get pod -o jsonpath resources → Check limits"
      - "kubectl logs --previous → Check JVM GC logs"
      - "Calculation: Xmx should be 70-80% of limits"
    confidence: 高
    last_seen: 2026-03-28

  - pattern_id: FP-002
    title: "HPA Frequent Scaling Causes Service Jitter"
    frequency: 5 次/月
    trigger: "Pod count fluctuates rapidly within a short period"
    root_cause: "HPA scaleDown stabilization window is too short, or CPU metric fluctuations are large"
    effective_diagnosis_path:
      - "kubectl get hpa -n <ns> → Confirm current status"
      - "kubectl describe hpa → Check events and metrics"
      - "PromQL: Check CPU utilization fluctuation situation"
    confidence: 高
    last_seen: 2026-03-25

  - pattern_id: FP-003
    title: "Ingress 502 — Backend Pods Are Not Ready"
    frequency: 8 次/月
    trigger: "Ingress returns 502/503"
    root_cause: "ReadinessProbe configuration is incorrect, Pod has not yet been ready but is added to Endpoints"
    effective_diagnosis_path:
      - "kubectl get endpoints <svc> → confirm if Endpoints is empty"
      - "kubectl get pods -l <selector> → confirm if Pod is Ready"
      - "kubectl describe pod → check readinessProbe configuration"
    confidence: 高
    last_seen: 2026-04-01
```

### 2.2 Effective Diagnosis Paths

```yaml
effective_paths:
  - scenario: "Pod Pending + FailedScheduling"
    optimal_path:
      - "kubectl describe pod(look at Events, 80% of the time it can be directly pinpointed)"
      - "kubectl get events --field-selector(supplement event information)"
      - "kubectl top nodes(confirm if resources are truly insufficient)"
    avg_steps: 3
    success_rate: 92%

  - scenario: "Node NotReady"
    optimal_path:
      - "kubectl describe node(check Conditions, distinguish between Ready/Pressure/Network)"
      - "kubectl get events --field-selector involvedObject.name=<node>"
      - "kubectl top node(confirm resource pressure level)"
    avg_steps: 3
    success_rate: 88%

  - scenario: "Service is unreachable"
    optimal_path:
      - "kubectl get endpoints(first step! 80% of issues are due to Endpoints being empty)"
      - "kubectl get pods -l <selector>(confirm if Pod selector matches)"
      - "kubectl get networkpolicy(check if NetworkPolicy intercepts)"
    avg_steps: 3
    success_rate: 85%
```

### 2.3 Failure Cases and Lessons Learned

```yaml
lessons_learned:
  - id: LL-001
    date: 2026-02-15
    mistake: "directly suggest customers increase memory limits to solve OOM"
    impact: "the cluster has insufficient total resources, increasing limits makes other Pods more likely to be evicted"
    lesson: "before adjusting limits, must check remaining resources on the node and overall cluster capacity"
    prevention: "SKILL.md Add a step to check cluster capacity in the OOM repair decision tree"

  - id: LL-002
    date: 2026-03-10
    mistake: "when diagnosing DNS issues, did not first check if the CoreDNS Pod is normal"
    impact: "after applying 30 minutes of application-layer troubleshooting, only then realized that CoreDNS itself crashed in a CrashLoop"
    lesson: "DNS diagnosis always starts with kubectl get pods -n kube-system -l k8s-app=kube-dns"
    prevention: "SKILL.md In the DNS SOP, move the CoreDNS status check to the first step"
```

## 3. User Preference Memory

```yaml
user_preferences:
  output_format:
    - "Preference table-based display of comparison data"
    - "Command outputs wrapped in code blocks"
    - "Fix steps listed in ordered lists"

  frequently_used_commands:
    - "kubectl get pods -o wide -n <ns>"
    - "kubectl describe pod <pod> -n <ns>"
    - "kubectl top nodes"

  focus_areas:
    - "Q2 2026: Work order diagnosis efficiency, Agent auxiliary diagnosis"
    - "Focus on Terway network and ESSD storage-related issues"
```

## 4. Memory Metadata Management

```yaml
memory_metadata:
  total_entries: 15
  last_consolidation: 2026-04-01
  next_scheduled_consolidation: 2026-04-08

  retention_policy:
    confirmed_rules: "Permanently retained"
    high_confidence_patterns: "Retained for 6 months, downgraded or deleted upon expiration"
    medium_confidence_patterns: "Retained for 3 months"
    low_confidence_patterns: "Retained for 1 month, automatically deleted if unused"

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
