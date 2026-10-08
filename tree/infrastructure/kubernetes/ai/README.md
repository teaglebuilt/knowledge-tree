---
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/README.md
---
---title: AI/ML Infrastructure
description: Consolidates AI infrastructure knowledge from the original domain-14-ai-ml-infra/41, covering GPU scheduling, distributed training, AI Agents, and MLOps.
summary: Consolidates AI infrastructure knowledge from the original domain-14-ai-ml-infra/41, covering GPU scheduling, distributed training, AI Agents, and MLOps.
category: domain
tags:
- ai
- ml
- gpu
- scheduling
- distributed-training
- agent
- rag
- daemonset
tier: core
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 5min
intent_queries:
- What is AI/ML Infrastructure
- How to AI/ML Infrastructure
- Kubernetes 14 ai ml infra best practices
trigger_keywords:
- AI
- ML
- Infrastructure
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
> This document contains operational commands that can be executed directly. Before executing, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have validated in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state, but generally reversible), 🟢 Low risk / Read-only (information gathering, no side effects).




# AI/ML Infrastructure

Consolidates AI infrastructure knowledge from the original domain-14-ai-ml-infra/41, covering GPU scheduling, distributed training, AI Agents, and MLOps.

## Directory Structure

| Subdirectory | Contents |
|---|---|
| 01-ai-infra/ | GPU scheduling, DCGM, distributed training frameworks |
| 02-ai-agents/ | AI Agent frameworks, RAG, tool calling, Agent Harness engineering |
| 03-agent-runtime/ | Agent runtime and production deployment |
| topic-ai-coding/ | AI coding tools (OpenRouter, OpenCode) integration |

## Relationship with Other Domains

- [[domain-02-workloads-applications/README.md|domain-02-workloads-applications]] — Workload scheduling
- [[domain-07-platform-engineering/README.md|domain-07-platform-engineering]] — Platform resource management

## Related

- Domain-34: CNCF Landscape Open Source Projects — Cross-reference
- networking|Release Notes Index — Networking]] — Cross-reference
- domain-03-networking-traffic KUDIG Database — Global MOC — Cross-reference
- Topic Application Layer Architecture Design Best Practices — Cross-reference
- topic-application-architecture MOC — Cross-reference
- [[concepts/bp-common-best-practices.md|Kubernetes Common Best Practices Reference]] — Cross-reference
- [[concepts/KUDIG Knowledge Base Architecture.md|KUDIG Knowledge Base Architecture]] — Cross-reference
- [[domain-14-ai-ml-infra/01-ai-infra/03-gpu-scheduling-management.md|GPU Scheduling and Management]] — Cross-reference
- [[domain-14-ai-ml-infra/01-ai-infra/05-distributed-training-frameworks.md|Distributed Training Frameworks]] — Cross-reference
- domain-08-release-change-management MOC — Cross-reference
- [[skills/learn-decision-tree-mermaid.md|Troubleshooting Decision Tree - Mermaid Visualization]] — Cross-reference
- [[skills/skill-22-daemonset-failure.md|DaemonSet Failure Diagnosis & Remediation]] — Cross-reference
- [[domain-07-platform-engineering/operate/06-monitoring-alerting-system.md|Monitoring and Alerting System]] — Cross-reference
- Domain 30: Enterprise Disaster Recovery & Business Continuity — Cross-reference
- [[entities/ecosystem-changelog.md|Ecosystem Component Changelog Index]] — Cross-reference
- [[domain-19-landscape-references/topic-index/cluster-index.md|Cluster Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/pvc-index.md|PVC Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/terway-index.md|Terway Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/nginx-ingress-index.md|nginx-ingress-controller Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/higress-index.md|Higress Knowledge Graph Index]]


<!-- risk-assessed -->
