---
title: Platform Engineering
description: Consolidate platform knowledge from the original domain-07-platform-engineering/36, covering platform construction (IDP/Backstage), platform operations execution, and platform governance.
summary: Consolidate platform knowledge from the original domain-07-platform-engineering/36, covering platform construction (IDP/Backstage), platform operations execution, and platform governance.
category: domain
tags:
- platform-engineering
- idp
- backstage
- devops
- platform-ops
- daemonset
- gpu
tier: core
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All engineers
estimated_read_time: 5min
intent_queries:
- What is Platform Engineering
- How to implement Platform Engineering
- Kubernetes domain 07 platform engineering best practices
trigger_keywords:
- Platform
- Engineering
- platform
- engineering
prerequisites:
- kubectl-basics
- platform-engineering-basics
- gpu-scheduling-basics
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./README.md
original_language: Chinese
---

> **Production Environment Security Tips**
>
> This document contains directly executable operations commands. Before execution, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether it has been validated in a non-production environment. Command risk levels are marked: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state, but usually reversible), 🟢 Low risk/Read-only (information collection, no side effects).




# Platform Engineering

Consolidate platform knowledge from the original domain-07-platform-engineering/36, covering platform construction (IDP/Backstage), platform operations execution, and platform governance.

## Directory Structure

| Subdirectory | Content |
|---|---|
| build/ | IDP Design, [[Backstage|Backstage]], Kratix, [[Crossplane|Crossplane]] |
| operate/ | Cluster lifecycle, multi-cluster management, monitoring and alerting, automation |
| governance/ | Capacity planning, cost optimization, multi-tenancy, security and compliance |
| developer-experience/ | DevEx metrics, team topology, CLI plugins |
| topic-code-analysis/ | Code analysis and quality governance |

## Relationship with other Domains

- [[domain-08-release-change-management/README.md|domain-08-release-change-management]] — Release management
- observability/README.md|domain-06-observability]] — Observability construction

## Related

- Domain-34: CNCF Landscape open source projects — Cross-reference
- [[entities/release-notes-networking.md|Release notes index — Networking]] — Cross-reference
- domain-03-networking-traffic MOC — Cross-reference
- Topic Application architecture design best practices — Cross-reference
- topic-application-architecture MOC — Cross-reference
- [[concepts/bp-common-best-practices.md|Kubernetes Common Best Practices Reference]] — Cross-reference
- [[concepts/KUDIG Knowledge Base Architecture.md|KUDIG Knowledge Base Architecture]] — Cross-reference
- [[domain-14-ai-ml-infra/01-ai-infra/03-gpu-scheduling-management.md|GPU Scheduling and Management]] — Cross-reference
- [[domain-14-ai-ml-infra/01-ai-infra/05-distributed-training-frameworks.md|Distributed Training Frameworks]] — Cross-reference
- domain-08-release-change-management MOC — Cross-reference
- [[skills/learn-decision-tree-mermaid.md|Troubleshooting Decision Tree - Mermaid Visualization]] — Cross-reference
- [[skills/skill-22-daemonset-failure.md|DaemonSet Failure Diagnosis & Remediation / DaemonSet Failure Diagnosis & Remediation]] — Cross-reference
- [[domain-07-platform-engineering/operate/06-monitoring-alerting-system.md|Monitoring and Alerting System]] — Cross-reference
- Domain 30: Enterprise Disaster Recovery & Business Continuity (Enterprise Disaster Recovery & Business Continuity) — Cross-reference
- [[entities/ecosystem-changelog.md|Ecosystem Component Change Log Index]] — Cross-reference
- [[domain-19-landscape-references/topic-index/cluster-index.md|Cluster Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/pvc-index.md|PVC Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/terway-index.md|Terway Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/nginx-ingress-index.md|nginx-ingress-controller Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/higress-index.md|Higress Knowledge Graph Index]]


<!-- risk-assessed -->