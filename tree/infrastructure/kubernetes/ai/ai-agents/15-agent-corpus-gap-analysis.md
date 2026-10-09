---
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/ai-agents/15-agent-corpus-gap-analysis.md
---
---title: Agent Corpus Gap Analysis: What Is kudig-database Still Missing as K8s Operations Agent Training Data? [02-ai-agents]
description: 'title: Agent Corpus Gap Analysis: What Is kudig-database Still Missing as K8s Operations Agent Training Data?'
summary: 'title: Agent Corpus Gap Analysis: What Is kudig-database Still Missing as K8s Operations Agent Training Data?'
category: general
tags:
- ai
- ai-agent
- etcd
- apiserver
- kubelet
- scheduler
- prometheus
- cilium
- flannel
- calico
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 35min
intent_queries:
- What is Agent Corpus Gap Analysis: What Is kudig-database Still Missing as K8s Operations Agent Training Data?
- How to Agent Corpus Gap Analysis: What Is kudig-database Still Missing as K8s Operations Agent Training Data?
- Kubernetes 14 ai ml infra best practices
trigger_keywords:
- Agent
- Corpus Gap Analysis: kudig-database
- as
- K8s
- Operations
- Agent
- Training Data Missing?
- ai
prerequisites:
- kubectl-basics
- helm-basics
- prometheus-basics
- gitops-basics
- ebpf-basics
- cilium-basics
- cni-basics
- etcd-basics
- gpu-scheduling-basics
- backup-basics
authors:
- name: Dillan Teagle
  role: contributor

---

> **Production Environment Safety Notice**
>
> This document contains operational commands that can be executed directly. Before executing, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have validated in a non-production environment. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state, but generally reversible), 🟢 Low Risk / Read-Only (information gathering, no side effects).




title: Agent Corpus Gap Analysis: What Is kudig-database Still Missing as K8s Operations Agent Training Data?
description: '# Agent Corpus Gap Analysis: What Is kudig-database Still Missing as K8s Operations Agent Training Data?'
category: ai-agent
tags:
- ai
- agent
- llm
- rag
- multi-agent
- [[etcd|etcd]]
- apiserver
- [[kubelet|kubelet]]
- scheduler
- [[Prometheus|prometheus]]
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Architects
- SRE
estimated_read_time: 15min
intent_queries:
- What is Agent Corpus Gap Analysis: What Is kudig-database Still Missing as K8s Operations Agent Training Data?
- How to Agent Corpus Gap Analysis: What Is kudig-database Still Missing as K8s Operations Agent Training Data?
trigger_keywords:
- Agent
- Corpus Gap Analysis: kudig-database
- as
- K8s
- Operations
- Agent
- Training Data Missing?
- ai
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
# Agent Corpus Gap Analysis: What Does kudig-database Still Lack as K8s Operations Agent Corpus?

> **Document Type**: In-depth Gap Analysis | **Last Updated**: 2026-03 | **Keywords**: Agent corpus, corpus gap, structured knowledge, K8s operations agent, knowledge completion, RAG, SOP, symptom mapping, safety guardrails

---

## Overview

kudig-database already covers 39 knowledge domains, 1,477 files, and 43 million characters, making it an extremely comprehensive [[Kubernetes|Kubernetes]] production operations knowledge base. However, there is a **structural gap** between "human-readable knowledge bases" and "Agent-usable corpora."

This document systematically examines existing content from an **Agent perspective**, identifies **10 major categories of gaps**, and for each provides:
- File-by-file audit of existing assets
- Precise inventory of missing content
- Target format required by Agent (including actionable data structures)
- Concrete transformation paths from existing content
- Effort estimates

### Methodology

This analysis follows the **Agent Readiness Assessment** three-layer model:

```
Layer 3: Interaction Layer    → How the Agent converses, confirms, and teaches
Layer 2: Reasoning Layer      → How the Agent judges, decides, and selects paths
Layer 1: Knowledge Layer      → How the Agent retrieves, understands, and cites knowledge

Gaps at each layer directly limit the Agent's capability ceiling:
  Layer 1 gap → Agent "doesn't know" → Wrong or unanswerable responses
  Layer 2 gap → Agent "can't judge" → Inappropriate recommendations
  Layer 3 gap → Agent "can't communicate" → Poor user experience, low trust
```

### Panoramic Inventory of Existing Assets

| Asset Category | Directory | File Count | Total Size | Agent Value Assessment |
|---------|------|-------|--------|---------------|
| Troubleshooting Compendium | `domain-10-troubleshooting-diagnostics/` | 42 | ~1.5M chars | ★★★★★ Core corpus for troubleshooting Agent |
| Structured Troubleshooting | `domain-10-troubleshooting-diagnostics/topic-structural-trouble-shooting/` | 48+ | ~600K chars | ★★★★★ Already has decision tree structure |
| FTA Fault Trees | `domain-10-troubleshooting-diagnostics/topic-fta/list/` | 37 | ~1.5M chars | ★★★★★ Direct input for Agent reasoning chains |
| YAML Manifest Handbook | `domain-18-manifests-patterns/` | 36 | ~1.7M chars | ★★★★☆ Foundation for template-generation Agent |
| K8s Events Compendium | `domain-17-system-foundation/` | 15 | ~800K chars | ★★★★☆ Key for event-interpretation Agent |
| Operations Dictionary | `domain-17-system-foundation/topic-dictionary/` | 16 | ~1.4M chars | ★★★★☆ Terminology and best practices |
| FEBM Forensic Evidence | `domain-10-troubleshooting-diagnostics/topic-febm/` | 11 | ~1.0M chars | ★★★★☆ Diagnostic methodology |
| FTA Methodology | `domain-10-troubleshooting-diagnostics/topic-fta/` (non-list) | 30 | ~500K chars | ★★★★☆ Agent orchestration theory |
| Control Plane | `domain-01-cluster-fundamentals/` | 28 | ~1.1M chars | ★★★★☆ Deep knowledge of core components |
| Networking | `domain-03-networking-traffic/` | 41 | ~900K chars | ★★★★☆ Network troubleshooting Agent |
| Security | `domain-05-security-compliance/` | 21 | ~440K chars | ★★★☆☆ Security audit Agent |
| Observability | `domain-06-observability/` | 27 | ~600K chars | ★★★☆☆ Monitoring Agent |
| Production Operations | `domain-11-production-operations/` | 24 | ~500K chars | ★★★☆☆ SOP transformation foundation |
| Cheat Sheets | `domain-17-system-foundation/topic-cheat-sheet/` | 3 | ~130K chars | ★★★☆☆ Directly retrievable |
| Migration Guides | `domain-08-release-change-management/topic-migration/` | 10 | ~150K chars | ★★★☆☆ Blueprint for migration Agent |
| Cloud Providers | `domain-12-cloud-providers/` | 13 dirs | ~200K chars | ★★☆☆☆ ACK relatively complete, others thin |

---

## Gap Summary

```
Assessment Dimension          Existing Coverage    Agent Usability    Priority
─────────────────────────────────────────────────────────────────────────────
1. Structured metadata             ★☆☆☆☆              ★☆☆☆☆           🔴 P0 - Highest
2. Standard Operating Procedures   ★★★☆☆              ★★☆☆☆           🔴 P0 - Highest
3. Symptom→Cause mapping tables    ★★★☆☆              ★★☆☆☆           🔴 P0 - Highest
4. Command output interpretation   ★★☆☆☆              ★☆☆☆☆           🟡 P1 - High
5. Real-world cases/ticket corpus  ★★☆☆☆              ★☆☆☆☆           🟡 P1 - High
6. Conversational interaction corpus ☆☆☆☆☆            ☆☆☆☆☆           🟡 P1 - High
7. Version difference matrices     ★★☆☆☆              ★☆☆☆☆           🟢 P2 - Medium
8. Judgment and decision criteria  ★★★☆☆              ★★☆☆☆           🟢 P2 - Medium
9. Safety guardrail rules          ★☆☆☆☆              ☆☆☆☆☆           🟢 P2 - Medium
10. Multi-language/multi-cloud     ★★☆☆☆              ★☆☆☆☆           ⚪ P3 - Low
```

---

## 🔴 P0-Level Gaps: Agent Core Capability Dependencies (Knowledge Layer 1)

> P0 gaps directly determine whether the Agent can correctly retrieve and understand knowledge. Without resolving these gaps, the Agent fundamentally cannot function.

### 1. Structured Metadata Layer

**Current Audit**: All 1,477 documents are pure Markdown long-form text with no YAML Front Matter or machine-readable metadata whatsoever. There are no semantic chunking markers within documents. During RAG retrieval, the Agent can only rely on text similarity and cannot leverage metadata filtering.

**Per-Domain Impact Assessment**:

| Affected Domain | File Count | Missing Metadata Types | Impact Level |
|---------|-------|----------------|----------|
| `domain-10-troubleshooting-diagnostics/` | 42 | Missing intent_queries, severity, symptom_tags | Fatal — low retrieval accuracy in troubleshooting scenarios |
| `domain-18-manifests-patterns/` | 36 | Missing resource_type, api_version, use_case | Severe — YAML-generation Agent cannot filter by resource type |
| `domain-17-system-foundation/` | 15 | Missing event_type, source_component, severity | Severe — event-interpretation Agent cannot match precisely |
| `domain-01-cluster-fundamentals/` | 28 | Missing component, layer, failure_mode | High — control plane diagnosis retrieval takes longer |
| `domain-10-troubleshooting-diagnostics/topic-fta/list/` | 37 | Missing component, top_event, gate_count | Medium — FTA already has structure but lacks lookup entry points |

**Detailed Description of 10 Categories of Missing Metadata Fields**:

| Missing Field | Description | Agent Use Case | Example Value |
|---------|------|----------------|--------|
| `id` | Unique document identifier | Cross-referencing, relationship graphs | `D12-05` |
| `domain` | Owning knowledge domain | Narrowing retrieval scope | `troubleshooting` |
| `tags` | Semantic tags | RAG vector retrieval enhancement | `[pod, pending, scheduling]` |
| `difficulty` | Difficulty level | Learning Agent path planning | `intermediate` |
| `target_roles` | Target roles | Filter content by role | `[sre, ops-engineer]` |
| `k8s_versions` | Applicable versions | Version-specific query filtering | `[1.28, 1.29, 1.30]` |
| `intent_queries` | Possible user query phrasings | Intent recognition → document matching | `"What to do when Pod is Pending"` |
| `requires` | Prerequisite knowledge | Knowledge graph navigation | `[D4-01, D4-19]` |
| `related` | Related documents | Recommend further reading | `[D12-06, D12-07]` |
| `chunk_markers` | Intra-document chunking markers | Fine-grained retrieval granularity | `<!-- chunk: diagnosis-step-3 -->` |
**Suggested Completion Plan — Complete Front Matter Specification**:

```yaml
# Example: domain-10-troubleshooting-diagnostics/05-pod-pending-diagnosis.md
---
id: D12-05
domain: troubleshooting
title: Pod Pending State In-Depth Diagnosis
tags: [pod, pending, scheduling, resource, node, taint, affinity]
difficulty: intermediate
target_roles: [sre, ops-engineer, developer]
k8s_versions: [1.25, 1.26, 1.27, 1.28, 1.29, 1.30, 1.31, 1.32]
severity_context: P0-P2  # Severity level range covered by this document
intent_queries:
  - "Pod 一直 Pending 怎么办"
  - "Pod stuck in Pending state"
  - "调度失败怎么排查"
  - "Insufficient cpu/memory"
  - "no nodes available to schedule"
requires: [D4-01, D4-19, D1-01]  # Workload overview, scheduler config, architecture overview
related: [D12-06, D12-07, D12-24, D33-05]  # Node NotReady, OOM, Quota, scheduling events
fta_ref: domain-10-troubleshooting-diagnostics/topic-fta/list/pod-fta.md  # Associated fault tree
structural_ref: domain-10-troubleshooting-diagnostics/topic-structural-trouble-shooting/05-workloads/01-pod-troubleshooting.md
---
```

**Effort Estimate**:
- Batch-add basic front matter (50% can be auto-generated by scripts): ~3 days
- Manually complete intent_queries and relationship mappings: ~7 days
- Annotate chunk_markers inside documents (core 100 docs): ~5 days
- **Total: ~15 person-days**

### 2. Standard Operating Procedures (SOP / Runbook)

**Current State Audit**:

Existing SOP-related content is distributed across multiple locations, but the format leans toward "knowledge explanation" rather than "executable instruction sequences":

| Existing Resource | Content | Agent SOP Usability | Gap Distance |
|---------|------|------------------|----------|
| `domain-17-system-foundation/topic-dictionary/12-incident-management-runbooks.md` | 3245 lines, incident management framework + process | ★★★☆☆ Has framework but lacks executable steps | Medium – needs to be extracted into structured SOP |
| `domain-11-production-operations/23-incident-response-handling.md` | Emergency response handling | ★★☆☆☆ Theory-heavy | Large – needs rewrite into minute-level steps |
| `domain-11-production-operations/22-change-management-process.md` | Change management process (62K) | ★★★☆☆ Fairly complete but not Agent format | Medium |
| `domain-11-production-operations/17-disaster-recovery-drills.md` | Disaster recovery drills (45K) | ★★★☆☆ Has steps but unstructured | Medium |
| `domain-01-cluster-fundamentals/10-plane-backup-disaster-recovery.md` | etcd backup/recovery (58K) | ★★★★☆ Has concrete commands | Small – needs extraction and consolidation |
| `domain-05-security-compliance/10-certificate-management.md` | Certificate management (40K) | ★★★☆☆ Has principles and commands | Medium – needs splitting into per-component SOPs |
| `domain-01-cluster-fundamentals/07-upgrade-paths-strategy.md` | Upgrade strategy | ★★☆☆☆ Strategy-focused | Large – missing per-version operation checklists |
| `domain-08-release-change-management/topic-migration/` | 10 migration guides | ★★★☆☆ Clear process but not SOP format | Medium |

**Complete List of 30 Missing Core SOPs**:

| # | SOP Name | Trigger Scenario | Severity | Reusable Existing Content | Rework Effort |
|---|---------|---------|--------|----------------|----------|
| 1 | etcd Emergency Backup & Recovery | etcd unavailable / data corruption | P0 | domain-01-cluster-fundamentals/10, domain-01-cluster-fundamentals/19 | Small |
| 2 | API Server Unavailability Emergency | apiserver unresponsive | P0 | domain-10-troubleshooting-diagnostics/01, domain-01-cluster-fundamentals/12 | Medium |
| 3 | Cluster Certificate Expiry Rotation | Certificate expiring / already expired | P0 | domain-05-security-compliance/10, domain-10-troubleshooting-diagnostics/13 | Medium |
| 4 | Mass CrashLoop of Pods in Production | Core service crash | P0 | domain-10-troubleshooting-diagnostics/08 | Medium |
| 5 | Node NotReady Emergency Response | Multiple nodes NotReady simultaneously | P0 | domain-10-troubleshooting-diagnostics/06, domain-10-troubleshooting-diagnostics/09 | Medium |
| 6 | Cluster Network Partition Handling | Cross-node network failure | P0 | domain-10-troubleshooting-diagnostics/03, domain-10-troubleshooting-diagnostics/25 | Large |
| 7 | Daily Inspection SOP | Daily/weekly inspection | P1 | domain-06-observability/13 | Large |
| 8 | Node Cordon/Drain (drain/cordon) | Node maintenance | P1 | Scattered | Large |
| 9 | Cluster Version Upgrade | Planned upgrade | P1 | domain-01-cluster-fundamentals/07, domain-01-cluster-fundamentals/18 | Large |
| 10 | Application Rolling Update / Rollback | Deployment update failure | P1 | domain-10-troubleshooting-diagnostics/11, domain-02-workloads-applications/02 | Medium |
| 11 | HPA/VPA Adjustment | Autoscaling anomaly | P1 | domain-10-troubleshooting-diagnostics/17, domain-02-workloads-applications/21 | Medium |
| 12 | DNS Issue Emergency Response | Service discovery failure | P1 | domain-10-troubleshooting-diagnostics/26, domain-03-networking-traffic/28 | Medium |
| 13 | PVC Storage Failure Handling | PVC Pending / mount failure | P1 | domain-10-troubleshooting-diagnostics/14, domain-04-storage-data/09 | Medium |
| 14 | Ingress/Gateway Failure Handling | External access anomaly | P1 | domain-10-troubleshooting-diagnostics/15, domain-03-networking-traffic/19-26 | Medium |
| 15 | RBAC Permission Issue Handling | Insufficient / excessive permissions | P1 | domain-10-troubleshooting-diagnostics/12, domain-05-security-compliance/07 | Medium |
| 16 | Secret/ConfigMap Hot Reload | Configuration changes not taking effect | P2 | domain-10-troubleshooting-diagnostics/19 | Small |
| 17 | CronJob Failure Handling | Scheduled task not triggering | P2 | domain-10-troubleshooting-diagnostics/18 | Small |
| 18 | DaemonSet Failure Handling | System component anomaly | P2 | domain-10-troubleshooting-diagnostics/20 | Small |
| 19 | StatefulSet Failure Handling | Stateful service anomaly | P2 | domain-10-troubleshooting-diagnostics/21 | Small |
| 20 | Monitoring & Alerting System Issues | Prometheus/Alertmanager anomaly | P2 | domain-10-troubleshooting-diagnostics/30 | Medium |
| 21 | Helm Release Failure Handling | Chart deployment/upgrade failure | P2 | domain-10-troubleshooting-diagnostics/36 | Medium |
| 22 | ArgoCD Sync Failure Handling | GitOps sync failure | P2 | domain-10-troubleshooting-diagnostics/38 | Medium |
| 23 | Image Registry Failure Handling | Image pull failure | P2 | domain-10-troubleshooting-diagnostics/27 | Medium |
| 24 | Cluster Autoscaling Issues | Cluster Autoscaler anomaly | P2 | domain-10-troubleshooting-diagnostics/28 | Medium |
| 25 | NetworkPolicy Failure Handling | Network policy anomaly | P2 | domain-10-troubleshooting-diagnostics/16 | Small |
| 26 | GPU Device Failure Handling | GPU not visible / allocation failure | P2 | domain-14-ai-ml-infra/03-04 | Large |
| 27 | Velero Backup & Recovery SOP | Cluster-level backup & recovery | P2 | domain-10-troubleshooting-diagnostics/31 | Medium |
| 28 | Multi-Cluster Failover | Cross-cluster switchover | P3 | domain-10-troubleshooting-diagnostics/37 | Large |
| 29 | Chaos Engineering Drill SOP | Fault injection testing | P3 | domain-10-troubleshooting-diagnostics/42 | Large |
| 30 | Security Incident Emergency Response | Security vulnerability / intrusion | P3 | domain-05-security-compliance/20 | Large |

**Agent-Executable SOP Target Format**:

```yaml
sop:
  id: SOP-001
  name: "etcd Emergency Backup & Recovery"
  trigger: "etcd cluster unavailable / data corruption / majority nodes unhealthy"
  severity: P0
  estimated_time: "30-60min"
  risk_level: high  # Agent should use Level 1 recommendation mode
  prerequisites:
    - check: "Has SSH access to etcd nodes"
      command: "ssh etcd-node-1 'echo ok'"
    - check: "etcdctl v3.5+ is installed"
      command: "etcdctl version"
      expected: "etcdctl version: 3.5"
  steps:
    - id: 1
      action: "Confirm etcd cluster status"
      command: "ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/healthcheck-client.crt --key=/etc/kubernetes/pki/etcd/healthcheck-client.key endpoint health --cluster"
      expected_output: "is healthy: true"
      on_failure:
        action: "Skip to step 4 (single-node recovery)"
        reason: "Cluster cannot respond normally; restore from snapshot required"
    - id: 2
      action: "Check member list"
      command: "etcdctl member list --write-out=table"
      parse_fields: ["ID", "STATUS", "NAME", "PEER_ADDRS"]
      check: "STATUS all show started"
    - id: 3
      action: "Perform snapshot backup"
      command: "etcdctl snapshot save /backup/etcd-$(date +%Y%m%d-%H%M%S).db"
      validation:
        command: "etcdctl snapshot status /backup/etcd-*.db --write-out=table"
        expected: "revision > 0"
    - id: 4
      action: "Restore from snapshot (only when cluster is unavailable)"
      danger_level: critical
      confirm_required: true
      confirm_message: "About to restore etcd from snapshot. This will discard all changes after the snapshot. Confirm to continue?"
      command: "etcdctl snapshot restore /backup/etcd-latest.db --data-dir=/var/lib/etcd-restored"
  rollback:
    - "Stop the restore operation; preserve the original data directory"
    - "Rebuild from another healthy node: etcdctl member add"
  knowledge_refs:
    - domain-01-cluster-fundamentals/10-plane-backup-disaster-recovery.md
    - domain-01-cluster-fundamentals/19-etcd-operations.md
    - domain-10-troubleshooting-diagnostics/02-control-plane-etcd-troubleshooting.md
```
**Workload Estimation**:
- P0-level SOPs (6): ~6 person-days (1 day each, requires extraction + structuring from existing documents)
- P1-level SOPs (9): ~9 person-days
- P2/P3-level SOPs (15): ~10 person-days
- **Total: ~25 person-days**

### 3. Symptom-Cause Mapping Table (Symptom-Cause Matrix)

**Current State Audit**:

In the existing knowledge base, the relationships between symptoms and causes are scattered across documents at multiple levels:

| Existing Data Source | Structuring Level | Number of Symptoms | Directly Usable by Agent? |
|---------|-----------|-----------|---------------|
| `domain-10-troubleshooting-diagnostics/topic-fta/list/` 37 fault trees | ★★★★★ Tree structure | ~200+ | ✗ Needs to be flattened into lookup table |
| `domain-10-troubleshooting-diagnostics/topic-structural-trouble-shooting/` 48+ articles | ★★★★☆ Decision tree | ~150+ | ✗ Needs to be extracted into mapping table |
| `domain-10-troubleshooting-diagnostics/` 42 troubleshooting documents | ★★★☆☆ Long-form narrative | ~300+ | ✗ Needs structured extraction |
| `domain-17-system-foundation/` 15 event documents | ★★★☆☆ Categorized by event | ~100+ | ✗ Needs to be mapped to symptoms |
| `domain-10-troubleshooting-diagnostics/08` Pod status quick reference | ★★★★☆ Has tables | ~10 | △ Close but missing diagnostic commands |

**Target Format Required by Agent — Quick Lookup Table**:

```yaml
symptom_cause_map:
  # === Pod Abnormal Status Category (15 types) ===
  - symptom: "Pod status CrashLoopBackOff"
    category: pod_status
    urgency: high
    possible_causes:
      - cause: "Application startup failure"
        probability: high
        diagnosis:
          commands:
            - "kubectl logs <pod> --previous"
            - "kubectl logs <pod> -c <container>"
          indicators: ["Exit Code 1", "Error in logs", "panic", "fatal"]
          next_step: "Check the specific error in the application log"
        fix_pattern: "Fix application code or configuration"
        knowledge_ref: "domain-10-troubleshooting-diagnostics/08-pod-comprehensive-troubleshooting.md#crashloopbackoff"
      - cause: "OOMKilled"
        probability: medium
        diagnosis:
          commands:
            - "kubectl describe pod <pod> | grep -A5 'Last State'"
            - "kubectl describe pod <pod> | grep -i oom"
          indicators: ["OOMKilled", "Exit Code 137", "reason: OOMKilled"]
          next_step: "Check container memory limits and actual application memory usage"
        fix_pattern: "Increase limits.memory or optimize application memory"
        knowledge_ref: "domain-10-troubleshooting-diagnostics/07-oom-memory-diagnosis.md"
        fta_ref: "domain-10-troubleshooting-diagnostics/topic-fta/list/pod-fta.md#oomkilled"
      - cause: "Liveness Probe failure"
        probability: medium
        diagnosis:
          commands:
            - "kubectl describe pod <pod> | grep -A10 'Liveness'"
            - "kubectl get events --field-selector involvedObject.name=<pod>"
          indicators: ["Liveness probe failed", "Unhealthy"]
          next_step: "Check Probe configuration and application health check endpoint"
        fix_pattern: "Adjust Probe parameters or fix health check endpoint"
        knowledge_ref: "domain-17-system-foundation/04-probe-health-check-events.md"
      - cause: "Configuration error (ConfigMap/Secret missing)"
        probability: low
        diagnosis:
          commands:
            - "kubectl describe pod <pod> | grep -A5 'Events'"
            - "kubectl get configmap <cm> -n <ns>"
          indicators: ["CreateContainerConfigError", "configmap not found"]
        knowledge_ref: "domain-10-troubleshooting-diagnostics/19-configmap-secret-troubleshooting.md"

  - symptom: "Pod status Pending"
    category: pod_status
    urgency: varies  # P0 (production core) to P2 (test environment)
    possible_causes:
      - cause: "Insufficient cluster resources (CPU/memory)"
        probability: high
        diagnosis:
          commands:
            - "kubectl describe pod <pod> | grep -A20 'Events'"
            - "kubectl describe nodes | grep -A5 'Allocated resources'"
            - "kubectl top nodes"
          indicators: ["Insufficient cpu", "Insufficient memory", "0/N nodes are available"]
        knowledge_ref: "domain-10-troubleshooting-diagnostics/05-pod-pending-diagnosis.md#3"
      - cause: "Node taint/affinity mismatch"
        probability: high
        diagnosis:
          commands:
            - "kubectl get nodes --show-labels"
            - "kubectl describe nodes | grep Taints"
            - "kubectl get pod <pod> -o yaml | grep -A10 'nodeSelector|affinity|tolerations'"
          indicators: ["didn't match Pod's node affinity", "had taint", "node(s) didn't match"]
        knowledge_ref: "domain-10-troubleshooting-diagnostics/05-pod-pending-diagnosis.md#4"
      - cause: "PVC not bound"
        probability: medium
        diagnosis:
          commands:
            - "kubectl get pvc -n <ns>"
            - "kubectl describe pvc <pvc>"
          indicators: ["Pending", "waiting for a volume", "no persistent volumes available"]
        knowledge_ref: "domain-10-troubleshooting-diagnostics/14-pvc-storage-troubleshooting.md"

  # === Service/Network Anomaly Category (12 types) ===
  - symptom: "Service inaccessible"
    category: network
    urgency: high
    possible_causes:
      - cause: "Endpoint is empty"
        probability: high
        diagnosis:
          commands:
            - "kubectl get endpoints <svc> -n <ns>"
            - "kubectl get pods -l <selector> -n <ns>"
          indicators: ["<none>", "ENDPOINTS: "]
        knowledge_ref: "domain-10-troubleshooting-diagnostics/10-service-comprehensive-troubleshooting.md"
      - cause: "Selector mismatch"
        probability: high
        diagnosis:
          commands:
            - "kubectl get svc <svc> -o yaml | grep -A5 selector"
            - "kubectl get pods --show-labels -n <ns>"
          indicators: ["Inconsistent labels"]
      - cause: "Pod not ready"
        probability: medium
        diagnosis:
          commands: ["kubectl get pods -l <selector> -o wide"]
          indicators: ["0/1 Running", "CrashLoopBackOff"]
      - cause: "NetworkPolicy blocking"
        probability: low
        diagnosis:
          commands: ["kubectl get networkpolicy -n <ns> -o yaml"]
        knowledge_ref: "domain-10-troubleshooting-diagnostics/16-networkpolicy-troubleshooting.md"
```
**Complete List of 70+ Symptoms to Be Covered**:

| Symptom Category | Specific Symptoms | Count | Source Documents |
|---------|---------|------|----------|
| **Pod Abnormal States** | CrashLoopBackOff, Pending, ImagePullBackOff, OOMKilled, Evicted, ContainerCreating, Init:Error, Terminating, Unknown, RunContainerError, CreateContainerConfigError, PreemptionByScheduler, BackOff, ErrImageNeverPull, InvalidImageName | 15 | domain-10-troubleshooting-diagnostics/05,07,08 |
| **Node Abnormalities** | NotReady, MemoryPressure, DiskPressure, PIDPressure, NetworkUnavailable, CordonedUnexpectedly, KubeletDown, ContainerRuntimeDown, ClockSkew, KernelDeadlock | 10 | domain-10-troubleshooting-diagnostics/06,09,35 |
| **Service/Network** | ServiceUnavailable, EmptyEndpoints, DNSResolutionFailed, IngressRouteError, TLSHandshakeFailed, ConnectionRefused, ConnectionTimeout, LoadBalancerPending, ExternalIPNotAssigned, GatewayRouteNotMatched, CrossNodeNetworkFailure, MTLSCertificateError | 12 | domain-10-troubleshooting-diagnostics/10,15,16,25,26 |
| **Storage Abnormalities** | PVCPending, VolumeAttachFailed, VolumeMountFailed, CSIDriverError, StorageClassNotFound, VolumeResizeFailed, SnapshotFailed, DataCorruption | 8 | domain-10-troubleshooting-diagnostics/04,14 |
| **Control Plane** | APIServerUnresponsive, APIServer5xx, etcdLeaderLost, etcdHighLatency, SchedulerBacklog, ControllerManagerStuck, WebhookTimeout, APFThrottling, etcdDiskSpaceLow, CertificateExpired | 10 | domain-10-troubleshooting-diagnostics/01,02 |
| **Scheduling Abnormalities** | Unschedulable, PreemptionFailure, PriorityClassMissing, TopologySpreadViolation, ResourceQuotaExceeded, LimitRangeViolation | 6 | domain-10-troubleshooting-diagnostics/05,17,24 |
| **Security/Permissions** | Forbidden, Unauthorized, CertificateExpired, PodSecurityViolation, NetworkPolicyDrop, AuditPolicyError, SecretNotFound, ServiceAccountTokenExpired | 8 | domain-10-troubleshooting-diagnostics/12,13,32 |
| **Operations Tools** | HelmReleaseFailed, ArgoCDOutOfSync, VeleroBackupFailed, ClusterAutoscalerNoScale | 4 | domain-10-troubleshooting-diagnostics/28,36,38 |
| **Total** | | **73** | |

**Workload Estimate**:
- Automated extraction and mapping from FTA fault trees (50%): ~3 days
- Manual extraction and supplementation from domain-10-troubleshooting-diagnostics documents: ~5 days
- Correlation mapping from domain-17-system-foundation event documents: ~2 days
- Writing diagnostic commands and indicators: ~5 days
- **Total: ~15 person-days**

---
## 🟡 P1 Level Missing: Agent Quality Improvement Dependencies (Reasoning Layer 2 + Interaction Layer 3)

> P1 gaps won't completely disable the Agent, but they will significantly reduce answer quality and user trust.

### 4. Command Output Interpretation Corpus

**Current State Audit**:

The documentation contains a large number of kubectl commands (`domain-12` alone has 3000+ executable commands), but **very few include field-by-field interpretation of command output**. This means the Agent can tell users "run this command," but cannot help users "interpret the output."

**Per-Category Audit**:

| Command Category | Existing Coverage | Agent Needs | Gap | Priority |
|---------|---------|---------|------|--------|
| `kubectl describe pod` | Command present but no output interpretation | Field-by-field parsing of Conditions, Events, Container Status | **Large** | 🔴 Highest |
| `kubectl describe node` | Command present but no interpretation | Meaning of each Condition state, Allocated resources assessment | **Large** | 🔴 Highest |
| `kubectl get events` | domain-17-system-foundation has event classification | Abnormal pattern recognition, time-series analysis | **Medium** | 🔴 Highest |
| `kubectl top node/pod` | None | Performance judgment thresholds (CPU >80%, Memory >85%) | **Large** | 🟡 High |
| `etcdctl endpoint status` | domain-01-cluster-fundamentals/19 has partial coverage | Health judgment criteria, Raft state interpretation | **Medium** | 🟡 High |
| `etcdctl endpoint health` | domain-01-cluster-fundamentals/19 has coverage | Abnormal pattern recognition | **Small** | 🟡 High |
| `crictl ps/inspect` | domain-01-cluster-fundamentals/21 has partial coverage | Runtime state interpretation | **Medium** | 🟢 Medium |
| `helm status/list` | domain-10-troubleshooting-diagnostics/36 has partial coverage | Release state interpretation, abnormal patterns | **Medium** | 🟢 Medium |
| `argocd app get` | domain-10-troubleshooting-diagnostics/38 has partial coverage | Sync state interpretation, Health/Sync assessment | **Medium** | 🟢 Medium |
| Prometheus alert rules | domain-06-observability has rules but no interpretation | Alert meaning mapping, severity assessment | **Large** | 🟢 Medium |

**Target Format Required by Agent — Output Interpretation Template**:

```yaml
command_output_interpretation:
  command: "kubectl describe pod <pod>"
  sections:
    - section: "Conditions"
      fields:
        - field: "PodScheduled"
          normal: "True"
          abnormal_patterns:
            - value: "False"
              meaning: "Pod not scheduled, check resources/nodes/taints"
              next_action: "Check FailedScheduling info in Events"
        - field: "Ready"
          normal: "True"
          abnormal_patterns:
            - value: "False"
              meaning: "Pod not ready, possibly Readiness Probe failure"
              next_action: "Check Readiness Probe configuration and application status"
    - section: "Events"
      pattern_matching:
        - pattern: "FailedScheduling.*Insufficient (cpu|memory)"
          meaning: "Insufficient cluster resources"
          severity: high
          action: "Check node resource usage, consider scaling out"
        - pattern: "FailedMount.*timeout"
          meaning: "Volume mount timeout"
          severity: high
          action: "Check CSI driver, storage backend status"
        - pattern: "Unhealthy.*Liveness probe failed"
          meaning: "Liveness probe failed, container will be restarted"
          severity: medium
          action: "Check probe configuration and application health status"
    - section: "Container Status"
      fields:
        - field: "State.Waiting.Reason"
          patterns:
            - value: "CrashLoopBackOff"
              meaning: "Container repeatedly crashing"
              next: "Check --previous logs"
            - value: "ImagePullBackOff"
              meaning: "Image pull failed"
              next: "Check image name, credentials, network"
            - value: "CreateContainerConfigError"
              meaning: "ConfigMap/Secret configuration error"
              next: "Check whether referenced CM/Secret exists"

  command: "kubectl top nodes"
  interpretation:
    thresholds:
      cpu_warning: "80%"   # Alert when CPU usage > 80%
      cpu_critical: "90%"  # Critical when CPU usage > 90%
      memory_warning: "85%"
      memory_critical: "95%"
    output_format: "NAME  CPU(cores)  CPU%  MEMORY(bytes)  MEMORY%"
    abnormal_patterns:
      - pattern: "CPU% > 90"
        meaning: "Node CPU severely overloaded, may affect new Pod scheduling"
      - pattern: "MEMORY% > 95"
        meaning: "Memory nearly exhausted, eviction may be triggered"
```

**Effort Estimate**: ~12 person-days (Top 20 high-frequency commands × 0.5 days each + pattern library writing)

### 5. Real-world Cases / Ticket Corpus

**Current State Audit**:

| Existing Case Source | Case Count | Format Quality | Agent Usability |
|---------|-------|---------|----------|
| `domain-08-release-change-management/topic-migration/10-real-world-case-study.md` | 1 complete migration case | ★★★★☆ | Medium - covers migration scenarios only |
| Scattered cases throughout `domain-10-troubleshooting-diagnostics/` documents | ~20 fragments | ★★☆☆☆ | Low - unstructured |
| `domain-17-system-foundation/topic-dictionary/02-failure-patterns-analysis.md` | ~15 patterns | ★★★☆☆ | Medium - patterns rather than tickets |
| `domain-06-observability/22-best-practices-case-studies.md` | ~5 cases | ★★★☆☆ | Medium - skewed toward monitoring scenarios |
**Agent-Required Ticket Format (50–100 tickets)**:

```yaml
incident:
  id: INC-2025-001
  severity: P1
  reported_at: "2025-12-15 14:32"
  reported_by: "Developer Engineer A"
  symptom: "Order service Pod in production is restarting frequently — 12 restarts in the past 1 hour"
  environment:
    cluster_version: "v1.28.3"
    node_count: 50
    cni: "Calico 3.26"
    affected_service: "order-service (Deployment, 6 replicas)"
  diagnosis_process:
    - step: 1
      action: "kubectl get pods -n production | grep order"
      finding: "RestartCount keeps increasing, current value 12"
    - step: 2
      action: "kubectl logs order-service-xxx --previous"
      finding: "java.lang.OutOfMemoryError: Java heap space"
    - step: 3
      action: "kubectl describe pod order-service-xxx"
      finding: "Last State: Terminated, Reason: OOMKilled, Exit Code: 137, limits.memory=512Mi"
    - step: 4
      action: "Check application JVM parameters"
      finding: "JVM -Xmx not set; defaults to 1/4 of container memory = 128Mi, but application actually needs 400Mi+"
  root_cause: "JVM default heap size exceeds container memory limits, triggering OOMKilled"
  fix:
    immediate: "Set -Xmx=384m, adjust limits.memory=1Gi"
    permanent: "CI/CD pipeline enforces check that JVM parameters match container limits"
  lesson_learned:
    rule: "Java applications must explicitly set JVM heap size ≤ 75% of container memory limits"
    category: "resource-management"
  knowledge_refs:
    - domain-10-troubleshooting-diagnostics/07-oom-memory-diagnosis.md
    - domain-10-troubleshooting-diagnostics/08-pod-comprehensive-troubleshooting.md#oomkilled
  tags: [java, oom, memory, crashloop, production, jvm]
  resolution_time: "35min"
```

**Ticket Scenario Distribution to Cover**:

| Scenario Category | Tickets Needed | Typical Scenarios | Source |
|---------|-----------|---------|------|
| Pod Anomalies | 15 | CrashLoop/OOM/Pending/Evicted/ImagePull | domain-10-troubleshooting-diagnostics/05,07,08 |
| Network Issues | 10 | DNS failure/Service unreachable/Ingress anomaly/Cross-node unreachable | domain-10-troubleshooting-diagnostics/03,10,15,25,26 |
| Storage Issues | 8 | PVC Pending/Mount failure/Performance degradation | domain-10-troubleshooting-diagnostics/04,14 |
| Control Plane | 8 | apiserver slow/etcd unhealthy/Certificate expired | domain-10-troubleshooting-diagnostics/01,02,13 |
| Security & Permissions | 5 | RBAC denied/ServiceAccount invalid | domain-10-troubleshooting-diagnostics/12,32 |
| Scaling | 5 | HPA not triggering/CA not scaling out | domain-10-troubleshooting-diagnostics/17,28 |
| Upgrades & Migration | 5 | Version incompatibility/Rolling upgrade stuck | domain-10-troubleshooting-diagnostics/34 |
| Toolchain | 5 | Helm failure/ArgoCD out of sync | domain-10-troubleshooting-diagnostics/36,38 |
| Performance Issues | 5 | CPU bottleneck/IO latency/Network latency | domain-10-troubleshooting-diagnostics/33 |
| **Total** | **66** | | |

**Effort Estimate**: ~20 person-days (66 tickets × 0.3 days each; can be extracted structurally from existing domain-10-troubleshooting-diagnostics content)

### 6. Conversational Corpus

**Current Audit**: **Completely absent**. All 1,477 documents are one-directional narrative; the Agent lacks any reference for "how to interact with users."

**Detailed Description of 6 Missing Dialogue Patterns**:

| Dialogue Type | Description | Impact on Agent Capability | Templates Needed |
|---------|------|--------------|----------|
| **Multi-turn Troubleshooting Dialogue** | How the Agent progressively asks questions to locate a problem | Troubleshooting efficiency | 15 |
| **Follow-up When Information Is Insufficient** | How to ask follow-up questions when information is missing | Diagnostic accuracy | 5 |
| **Dangerous Operation Confirmation** | Confirmation workflow before executing destructive operations | Safety | 5 |
| **Explanation & Teaching** | Dialogue patterns for explaining concepts and principles | Learning experience | 5 |
| **Step-by-Step Operation Guidance** | Dialogues that guide users through operations hands-on | Beginner experience | 5 |
| **Solution Comparison & Decision Support** | How to guide users in making decisions when comparing multiple solutions | Decision support | 5 |

**Dialogue Template Example — Multi-turn Troubleshooting Dialogue**:

```yaml
conversation_template:
  id: CONV-TS-001
  scenario: "Pod Pending Troubleshooting"
  trigger: "User reports Pod is Pending"
  target_outcome: "Identify the cause of Pending and provide a fix recommendation"
  knowledge_refs: [D12-05, D12-24, D33-05]
  dialogue:
    - turn: 1
      user: "My Pod is stuck in Pending state. What should I do?"
      agent_intent: "Gather basic information"
      agent: |
        Understood. I need some information to help diagnose this:
        1. Please run: `kubectl describe pod <pod-name> -n <namespace>`
        2. Please share the output of the Events section
        3. Is this a production environment or a test environment?
      required_info: ["describe output", "environment type"]

    - turn: 2
      user: "Production environment. Events show: 0/10 nodes are available: 4 Insufficient cpu, 6 had taint"
      agent_intent: "Parse Events and narrow down the scope"
      agent: |
        Based on the Events, the problem is clear:
        - **4 nodes have insufficient CPU** → Resource bottleneck
        - **6 nodes have taints** → Pod is missing the corresponding tolerations

        Let me confirm a few things:
        1. `kubectl top nodes` → Check actual resource usage on nodes
        2. `kubectl describe nodes | grep Taints` → Check taint details
        3. `kubectl get pod <pod> -o yaml | grep -A5 resources` → Check Pod resource requests
      reasoning: "Combined with D12-05 diagnostic decision tree: dual resource + taint issue"

    - turn: 3
      user: "top nodes shows 4 nodes with CPU at 92%. Taints shows 6 nodes have gpu=true:NoSchedule"
      agent_intent: "Provide recommendations"
      agent: |
        Clear picture now! Your cluster has two problems:

        **Problem 1: Insufficient CPU resources (40% of nodes are overloaded)**
        - Short-term solution: Check for low-priority Pods that can be reclaimed
        - Medium-term solution: Scale out regular nodes
        ```bash
        kubectl get pods -A --sort-by='.spec.containers[0].resources.requests.cpu' | tail -20
        ```

        **Problem 2: 6 GPU nodes have taints, preventing regular Pod scheduling**
        - If this Pod does not need GPU, this behavior is correct
        - If GPU is needed, add a toleration:
        ```yaml
        tolerations:
        - key: "gpu"
          operator: "Equal"
          value: "true"
          effect: "NoSchedule"
        ```

        Which problem would you like to address first?
```
**Effort Estimate**: ~10 person-days (40 dialogue templates × 0.25 days)

---
## 🟢 P2 Level Missing: Agent Precision and Safety Dependencies (Reasoning Layer 2)

> P2 gaps affect Agent decision precision and safety boundaries, which are especially critical in production environments.

### 7. Version Compatibility Matrix

**Current Audit**: Document headers annotate applicable version ranges (e.g., v1.25–v1.32), but lack **precise mapping of API and behavioral differences across versions**.

Existing version-related content distribution:

| Document | Version-related Content | Agent Usability |
|------|-----------|----------|
| `domain-01-cluster-fundamentals/03-api-versions-features.md` | API version evolution | ★★★☆☆ Present but not precise enough |
| `domain-01-cluster-fundamentals/07-upgrade-paths-strategy.md` | Upgrade strategy | ★★☆☆☆ Strategy-oriented |
| `domain-10-troubleshooting-diagnostics/05` Section 13 | Pod Pending version-specific changes | ★★★☆☆ Partial coverage |
| `domain-18-manifests-patterns/` | apiVersion in YAML examples | ★★☆☆☆ Implied but not organized |

**Target format required by Agent**:

```yaml
version_diff_matrix:
  - feature: "Pod Security Standards"
    changes:
      - version: "1.25"
        status: "GA"
        breaking: true
        # PodSecurityPolicy removed, PSS becomes the default
        note: "PodSecurityPolicy removed, PSS becomes the default"
        migration: "Migrate from PSP to PSS"
        ref: "domain-05-security-compliance/06-pod-security-standards.md"
      - version: "1.28"
        note: "AppArmor field added"
      - version: "1.30"
        note: "UserNamespace support beta"

  - feature: "Gateway API"
    changes:
      - version: "1.26"
        status: "beta"
        api: "gateway.networking.k8s.io/v1beta1"
      - version: "1.29"
        status: "GA"
        api: "gateway.networking.k8s.io/v1"
        breaking: true
        note: "Some v1beta1 fields deprecated"
        ref: "domain-03-networking-traffic/35-gateway-api-overview.md"

  - feature: "Sidecar Containers"
    changes:
      - version: "1.28"
        status: "alpha"
        note: "restartPolicy: Always for init containers"
      - version: "1.29"
        status: "beta"
        note: "SidecarContainers feature gate enabled by default"
        ref: "domain-02-workloads-applications/14-sidecar-containers-patterns.md"
```

**Version difference categories to be covered**:

| Category | Estimated Entries | Priority | Existing Reusable |
|------|-----------|--------|----------|
| API deprecation/removal timeline | ~15 | 🔴 High | Extractable from domain-01-cluster-fundamentals/03 |
| Default behavior changes | ~20 | 🔴 High | Scattered |
| Feature Gate status | ~15 | 🟡 Medium | K8s official docs |
| Component parameter changes | ~10 | 🟡 Medium | Extractable from domain-01-cluster-fundamentals |
| **Total** | **~60** | | |

**Effort estimate**: ~8 person-days

### 8. Decision Criteria

**Current Audit**: Documents present multiple option choices but lack **quantified decision conditions** for Agent automatic judgment.

| Existing Document | Decision Content | Missing |
|---------|---------|------|
| `domain-03-networking-traffic/03-cni-plugins-comparison.md` | CNI plugin comparison | Missing quantified selection conditions |
| `domain-04-storage-data/04-storageclass-dynamic-provisioning.md` | Storage class selection | Missing performance/cost judgment metrics |
| `domain-02-workloads-applications/22-cluster-capacity-planning.md` | Capacity planning | Missing automated calculation formulas |
| `domain-01-cluster-fundamentals/12-cluster-deployment-patterns.md` | Deployment patterns | Missing scenario→pattern mapping |

**Target format required by Agent**:

```yaml
decision_rules:
  - id: DR-001
    decision: "Choose CNI plugin"
    conditions:
      - if: "node count > 500 AND NetworkPolicy required"
        then: "Cilium (eBPF mode)"
        reason: "kube-proxy is a performance bottleneck at large scale; Cilium eBPF requires no iptables"
        ref: "domain-03-networking-traffic/03-cni-plugins-comparison.md"
      - if: "Alibaba Cloud ACK environment"
        then: "Terway"
        reason: "Native ENI integration, best performance, supports VPC-native networking"
        ref: "domain-03-networking-traffic/05-terway-advanced-guide.md"
      - if: "node count < 100 AND no complex networking requirements"
        then: "Flannel (VXLAN)"
        reason: "Simple and stable, low operational overhead"
      - default: "Calico"
        reason: "Widely used, full-featured, strong community support"

  - id: DR-002
    decision: "Pod memory limits setting"
    conditions:
      - if: "Java application"
        formula: "limits.memory = JVM_Xmx * 1.3 + 200Mi (non-heap + metaspace)"
        example: "Xmx=512m → limits=896Mi ≈ 1Gi"
        warning: "Must explicitly set -Xmx; otherwise JVM may exhaust container memory"
        ref: "domain-10-troubleshooting-diagnostics/07-oom-memory-diagnosis.md"
      - if: "Go application"
        formula: "limits.memory = observed P99 memory * 1.5"
        note: "Go GC triggers near GOMEMLIMIT; setting GOMEMLIMIT is recommended"
      - if: "Node.js application"
        formula: "limits.memory = --max-old-space-size * 1.4 + 100Mi"
      - if: "Python application"
        formula: "limits.memory = observed peak * 2.0"
        note: "Python memory management is less predictable; leave a larger buffer"

  - id: DR-003
    decision: "Choose data backup solution"
    conditions:
      - if: "K8s resource backup (stateless)"
        then: "Velero"
      - if: "etcd data backup"
        then: "etcdctl snapshot"
      - if: "Stateful service data"
        then: "Application-native backup + Velero orchestration"
        ref: "domain-07-platform-engineering/12-backup-recovery-strategy.md"
```
**Decision scenarios to be covered**:

| Decision Scenario | Estimated Rule Count | Source |
|---------|-----------|------|
| CNI/network plugin selection | 5 | domain-03-networking-traffic/03 |
| Storage class/CSI driver selection | 5 | domain-04-storage-data/04-05 |
| Resource requests/limits configuration | 5 | domain-02-workloads-applications/23, domain-10-troubleshooting-diagnostics/07 |
| Cluster scale/architecture selection | 5 | domain-01-cluster-fundamentals/12 |
| Monitoring solution selection | 3 | domain-06-observability/01 |
| Ingress/Gateway selection | 5 | domain-03-networking-traffic/19,35 |
| Backup strategy selection | 3 | domain-07-platform-engineering/12 |
| Security policy selection | 5 | domain-05-security-compliance |
| Scaling strategy selection | 3 | domain-02-workloads-applications/21 |
| **Total** | **~39** | |

**Effort estimate**: ~8 person-days

### 9. Safety Guardrails

**Current audit**: `domain-05-security-compliance/` and `domain-05-security-compliance/` contain security knowledge, but lack a **pre-execution safety check ruleset for Agents**. This is a **prerequisite** for Agents entering production environments.

**Safety guardrail system required by Agents**:

```yaml
safety_guardrails:
  # === Level 1: Absolutely forbidden (Agent should never execute) ===
  forbidden_actions:
    - pattern: "kubectl delete namespace (kube-system|kube-public|kube-node-lease)"
      reason: "Deleting system namespaces will render the cluster unavailable"
      severity: catastrophic
    - pattern: "kubectl delete node"
      reason: "Directly deleting a node may cause data loss"
    - pattern: "etcdctl del .* --prefix"
      reason: "Clearing etcd will destroy the entire cluster"
    - pattern: "kubectl delete pv"
      reason: "Deleting a PV may cause permanent data loss"
    - pattern: "kubectl.*--force --grace-period=0.*-n (production|prod)"
      reason: "Force-deleting production Pods may interrupt services"
    - pattern: "kubectl apply.*--server-side --force-conflicts"
      reason: "Forcing server-side apply may overwrite critical configurations"

  # === Level 2: Requires confirmation (Agent must display a warning and wait for user confirmation) ===
  confirm_required:
    - pattern: "kubectl delete pod .* -n (production|prod|prd)"
      warning: "↠️ About to delete a production Pod, please confirm the impact scope"
      show_info: ["kubectl get pod <pod> -o wide", "kubectl get endpoints"]
    - pattern: "kubectl drain"
      warning: "↠️ Draining a node will migrate all workloads"
      pre_check: ["kubectl get pods -o wide --field-selector spec.nodeName=<node>"]
    - pattern: "kubectl scale.*replicas=0"
      warning: "↠️ Setting replicas to 0 will stop all instances"
    - pattern: "kubectl edit.*-n (production|prod)"
      warning: "↠️ Directly editing production resources; it is recommended to make changes via GitOps"
    - pattern: "kubectl rollout undo"
      warning: "↠️ About to roll back a Deployment, please confirm the target version"
    - pattern: "helm uninstall|helm delete"
      warning: "↠️ Uninstalling a Helm Release will delete all associated resources"

  # === Level 3: Time window constraints ===
  time_constraints:
    - rule: "Do not perform cluster upgrades during business hours (9:00–18:00 on working days)"
      reason: "Sufficient rollback window is required"
    - rule: "Freeze changes during major sales events (Double 11, 618)"
      reason: "Minimize risk during peak business periods"

  # === Level 4: Pre-checks ===
  pre_checks:
    - before: "Deleting a PVC"
      checks:
        - "Confirm no Pod is mounting it: kubectl get pods --all-namespaces -o json | jq '.items[] | select(.spec.volumes[]?.persistentVolumeClaim.claimName==\"<pvc>\")'"
        - "Confirm data has been backed up"
    - before: "Modifying RBAC"
      checks:
        - "Check affected ServiceAccounts: kubectl get rolebinding,clusterrolebinding -A -o json | jq '.items[] | select(.roleRef.name==\"<role>\")'"
    - before: "Deleting a Namespace"
      checks:
        - "Confirm there are no running workloads in the namespace"
        - "Confirm there are no bound PVC/PVs"
```

**Effort estimate**: ~5 person-days

---
## ⚪ P3 Level Missing: Agent Ecosystem Expansion

### 10. Multi-Cloud Adaptation Corpus

**Current state**: In `domain-12-cloud-providers/`, Alibaba Cloud ACK has 8 files with good coverage, but AWS EKS, GKE, and AKS each have only 1 file.

**Missing**:
- Comparison table of K8s service differences across cloud providers
- Cloud provider-specific annotation/label mappings
- Configuration conversion rules for cross-cloud deployments

---

## Completion Roadmap

```
# 🟢 Low risk: read-only / information gathering, generally no side effects
Phase 1 (4-6 weeks) - Knowledge Layer Infrastructure                  Total effort: ~30 person-days
├── Add YAML front matter metadata to all documents            ~15 person-days
│   ├── Script to auto-generate base fields (id, domain, title, tags)   ~3 days
│   ├── Manually complete intent_queries and associations       ~7 days
│   └── chunk_markers annotation for core 100 documents         ~5 days
└── Extract symptom→cause mapping table (73 entries)           ~15 person-days
    ├── Auto-extract from FTA fault trees                         ~3 days
    ├── Manually extract supplements from domain-10-troubleshooting-diagnostics                      ~5 days
    ├── Associate with event documents from domain-17-system-foundation                       ~2 days
    └── Write diagnostic commands and indicators                  ~5 days

Phase 2 (4-6 weeks) - SOP and Command Corpus                          Total effort: ~57 person-days
├── Write 30 core O&M SOPs (structured executable format)       ~25 person-days
│   ├── P0-level SOPs (6)                                           ~6 days
│   ├── P1-level SOPs (9)                                           ~9 days
│   └── P2/P3-level SOPs (15)                                       ~10 days
├── Complete Top 20 high-frequency kubectl command output interpretations   ~12 person-days
└── Collect/write 66+ real issue ticket cases                   ~20 person-days

Phase 3 (3-4 weeks) - Interaction and Security Layer                  Total effort: ~23 person-days
├── Write 40 high-frequency scenario dialogue templates         ~10 person-days
├── Establish safety guardrail ruleset                           ~5 person-days
└── Complete version difference matrix (v1.25-v1.32, ~60 entries)   ~8 person-days

Phase 4 (2-3 weeks) - Decision and Validation Layer                   Total effort: ~16 person-days
├── Extract quantified decision conditions (~39 entries)         ~8 person-days
├── Establish Agent evaluation benchmark (Benchmark)             ~5 person-days
└── Complete multi-cloud adaptation corpus                       ~3 person-days

Total: ~126 person-days ≈ 1 person 6 months / 2 people 3 months / 3 people 2 months
```
---

## Existing Asset Reuse Matrix

| Existing Asset | File Count | Reusable For | Transformation Effort |
|---------|-------|---------|-----------|
| `domain-10-troubleshooting-diagnostics/` | 42 | Symptom→cause mapping table, SOPs | Medium - requires structured extraction |
| `domain-10-troubleshooting-diagnostics/topic-structural-trouble-shooting/` | 48+ | Decision trees, symptom mapping | Low - already semi-structured |
| `domain-10-troubleshooting-diagnostics/topic-fta/list/` | 37 | Fault tree reasoning chains | Low - already structured |
| `domain-18-manifests-patterns/` | 36 | YAML generation templates | Low - already standardized |
| `domain-17-system-foundation/` | 15 | Event interpretation corpus | Medium - requires extraction mapping |
| `domain-17-system-foundation/topic-dictionary/` | 16 | Glossary, best practices | Medium - requires chunking |
| `domain-17-system-foundation/topic-cheat-sheet/` | 3 | Command quick reference | Low - directly usable |
| `domain-08-release-change-management/topic-migration/` | 10 | Migration SOPs | Medium - requires SOP-ification |
| `domain-10-troubleshooting-diagnostics/topic-febm/` | 11 | Diagnostic methodology | Medium - requires templating |

---

## Quantitative Gap Estimation

| Dimension | Current Count | Agent Required | Gap | Estimated Effort | Priority |
|------|---------|----------|------|-----------|--------|
| Documents with structured metadata coverage | 0 | 1477 | **1477 docs** | ~15 person-days | P0 |
| Executable SOP count | ~5 (scattered) | 30 | **~25** | ~25 person-days | P0 |
| Symptom→cause mapping entries | 0 (scattered across docs) | 73+ | **~73 entries** | ~15 person-days | P0 |
| Command output interpretation templates | ~20 (scattered) | 50+ | **~30** | ~12 person-days | P1 |
| Issue ticket cases | ~3 | 66+ | **~63** | ~20 person-days | P1 |
| Dialogue templates | 0 | 40+ | **40+ sets** | ~10 person-days | P1 |
| Version difference matrix entries | ~10 (scattered) | 60+ | **~50 entries** | ~8 person-days | P2 |
| Quantified decision conditions | ~15 (scattered) | 39+ | **~24 entries** | ~8 person-days | P2 |
| Safety guardrail rules | 0 | 30+ | **30+ entries** | ~5 person-days | P2 |
| **Total** | | | | **~126 person-days** | |

---

## Conclusion

kudig-database, as a **human-readable knowledge base**, is already very mature (★★★★★), but as an **Agent-ready corpus** (★★★☆☆) there are still structural gaps. The core problem is not missing content, but rather:

> **Content is rich but not sufficiently Agent-friendly** —— needs to be transformed from "long-form human reading" into structured corpus that is "machine-retrievable, machine-reasoned, and machine-executable."

**Key Insights**:

| Dimension | Current State | Target |
|------|------|------|
| Knowledge Layer (Layer 1) | Content rich but no metadata | Structured, retrievable, with associations |
| Reasoning Layer (Layer 2) | Has knowledge but lacks decision rules | Quantified conditions, safety guardrails, version matrix |
| Interaction Layer (Layer 3) | Completely blank | Dialogue templates, ticket corpus, operation confirmations |

**Good news**: **~80% of the gap can be addressed through structural transformation of existing content**, with truly new content accounting for only 20% (primarily dialogue corpus, ticket cases, and safety guardrails).

**Total estimated investment: ~126 person-days**, completable in 4 phases over 16 weeks. It is recommended to start with Phase 1 (structured metadata + symptom mapping), as this is the foundation of Agent capability.

---
## Related Documents

| Document | Description |
|------|------|
| [Agent Design Philosophy and Implementation Path](./14-agent-kudig-design-strategy.md) | Overall design philosophy for Agent empowerment |
| [domain-10-troubleshooting-diagnostics/topic-fta/09-fta-as-agent-knowledge-skeleton.md](../domain-10-troubleshooting-diagnostics/topic-fta/09-fta-as-agent-knowledge-skeleton.md) | FTA as Agent Knowledge Skeleton |
| [domain-10-troubleshooting-diagnostics/topic-fta/10-agent-orchestration-patterns.md](../domain-10-troubleshooting-diagnostics/topic-fta/10-agent-orchestration-patterns.md) | Agent Orchestration Patterns |
| [domain-10-troubleshooting-diagnostics/topic-febm/04-febm-agent-ticket-processing.md](../domain-10-troubleshooting-diagnostics/topic-febm/04-febm-agent-ticket-processing.md) | FEBM Agent Ticket Processing |

---

*This document is a gap analysis report for the 02-ai-agents topic of the kudig-database project; the original topic-agent topic has been consolidated here.*

---

## Obsidian Related Documents

- 02-ai-agents MOC
- [[domain-14-ai-ml-infra/02-ai-agents/README.md|AI Agent Engineering Topic]]
- [[domain-14-ai-ml-infra/02-ai-agents/01-ai-agent-fundamentals.md|AI Agent Fundamentals and Core Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/02-llm-foundation-models.md|LLM Foundation Model Selection and Evaluation]]
- [[domain-14-ai-ml-infra/02-ai-agents/03-agent-frameworks-comparison.md|In-Depth Comparison of Mainstream Agent Frameworks]]
- [[domain-14-ai-ml-infra/02-ai-agents/04-rag-knowledge-retrieval.md|RAG Retrieval-Augmented Generation In-Depth Guide]]
- [[domain-14-ai-ml-infra/02-ai-agents/05-tool-use-function-calling.md|Tool Use & Function Calling Design Specification]]
- [[domain-14-ai-ml-infra/02-ai-agents/06-multi-agent-orchestration.md|Multi-Agent Orchestration and Collaboration Architecture]]
- [[domain-14-ai-ml-infra/02-ai-agents/07-memory-context-management.md|Memory Management and Context Window Engineering]]
- [[domain-14-ai-ml-infra/02-ai-agents/08-agent-evaluation-observability.md|Agent Evaluation System and Observability]]
- [[domain-14-ai-ml-infra/02-ai-agents/09-production-deployment-guide.md|Production Deployment Guide: Running Agent Services on K8s]]
- [[domain-14-ai-ml-infra/02-ai-agents/10-security-guardrails.md|Security Guardrails, Prompt Injection Protection, and Compliance]]

## Related

- 13-trusted-agent-system-fiscal-plan
- 39-agent-harness-testing-benchmark
- 42-model-harness-compatibility-matrix
- 12-enterprise-case-studies
- 02-llm-foundation-models
- 23-agent-cli-fundamentals
- 50-openclaw-identity-mechanism
- 01-ai-agent-fundamentals
- 03-agent-frameworks-comparison
- 47-openclaw-tools-mechanism
- 37-agent-harness-multi-agent
- 20-agentscope-multi-agent-orchestration
- 25-agent-cli-mcp-integration
- 26-agent-cli-development-workflow
- 07-memory-context-management
- 11-cost-latency-optimization
- 44-openclaw-soul-mechanism
- 45-openclaw-user-mechanism
- 31-agent-harness-loop-execution
- 06-multi-agent-orchestration

## See Also

- 13-trusted-agent-system-fiscal-plan
- 14-agent-kudig-design-strategy
- 16-agentscope-overview-installation
- 17-agentscope-core-concepts


<!-- risk-assessed -->
