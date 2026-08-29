I'll translate this Chinese document to English and return the complete translated markdown file.

```markdown
---
title: Production Readiness Review (PRR) Template
description: Production Readiness Review template for Kubernetes platform engineering teams, including checklists, risk matrices, release gates, rollback standards, and multi-party sign-off forms.
summary: Production Readiness Review template for Kubernetes platform engineering teams, including checklists, risk matrices, release gates, rollback standards, and multi-party sign-off forms, applicable to initial platform component releases, major version upgrades, and architecture changes.
category: platform-engineering
tags:
- production
- best-practices
- playbook
- platform-engineering
- prr
- readiness
tier: core
created: '2026-07-01'
last_updated: '2026-07'
difficulty: advanced
reading_level: advanced
audience:
- SRE
- Operations Engineer
- Platform Engineer
- Architect
estimated_read_time: 25min
intent_queries:
- What is the Production Readiness Review template
- How to conduct Kubernetes PRR
- How to create PRR checklists and risk matrices
trigger_keywords:
- PRR
- Production Readiness Review
- readiness review
- Release Gate
- Risk Matrix
- rollback criteria
prerequisites:
- kubectl-basics
- platform-engineering-basics
- risk-management-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
- '1.33'
authors:
- name: KUDIG Team
  role: contributor
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./99-production-readiness-review-template.md
original_language: Chinese
---

> **Production Environment Safety Alert**
>
> This document contains executable operations commands. Before execution, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether the changes have been validated in non-production environments. Command risk levels: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state, usually reversible), 🟢 Low Risk/Read-only (information gathering, no side effects).


# Production Readiness Review (PRR) Template

> **Scope**: Production readiness review for Kubernetes platform engineering components, IDP services, and critical infrastructure before release.  
> **Target Audience**: SRE, Platform Engineers, Product Managers, Security Representatives, Architects.  
> **Last Updated**: 2026-07-01

This template provides a customizable **Production Readiness Review (PRR)** checklist, risk matrix, release gates, rollback standards, and sign-off form. PRR is a key change control gate in platform engineering, positioned after architecture review and before production release. Review results should be archived as attachments in the change management system and undergo the first post-release review within 30 days of deployment.

---

## 1. Applicable Scenarios and Scope

- **Applicable Scenarios**: Initial platform component releases (GitOps controllers, auto-scaling, Secret management, service mesh control planes, etc.); major version upgrades or architecture changes (e.g., Karpenter major versions, Argo CD sharding restructuring); multi-tenant templates, ResourceQuota, and admission policy changes.
- **Not Applicable**: Pure business application releases (refer to [[domain-08-release-change-management/README.md|Release and Change Management domain]]); changes that only modify documentation or non-production configurations and do not impact SLO.

---

## 2. Prerequisites and Tools

| Condition | Requirement |
|---|---|
| Documentation | Architecture design, operations Runbook, and rollback plan submitted |
| Environment | staging environment has completed at least one full-scale exercise |
| Monitoring | Critical metrics already integrated with Prometheus/Grafana, alert rules in effect |
| Security | Security team has completed RBAC, NetworkPolicy, Secret, and image signature audits |
| Backup | Configuration and data have recoverable backups |

``` bash
# 🟢 Low Risk: read-only/information gathering, typically no side effects
kubectl version --client
helm version
argocd version --client  # if using Argo CD
```
---

## 3. Core Concepts/Architecture

The core objective of PRR is to: identify architecture, operations, security, and observability risks before changes enter production; ensure all critical checklist items have clear acceptance criteria, verification methods, and responsible parties; establish an auditable release gate and rollback decision basis. SRE is responsible for assessing the impact of changes on SLO, confirming whether monitoring, alerting, capacity, and rollback plans are in place, and sign-off indicates agreement to proceed with the release window.

---

## 4. Standard Operating Procedure

### 4.1 Initiate PRR

1. The change owner completes the first half of this template (applicable scenarios, prerequisites, self-check of checklist).
2. Collect architecture design documents, operations Runbook, monitoring dashboard links, and security audit reports.
3. Create a PRR ticket in the change management system and invite SRE, Security, Architecture, and Network teams for review.

### 4.2 Checklist Review

#### Architecture and High Availability

| Number | Checklist Item | Acceptance Criteria | Verification Command/Method | Result |
|---|---|---|---|---|
| A1 | Multi-replica component deployment | replicas ≥ 2, distributed across availability zones | `kubectl get pods -o wide` | □ Pass □ Deferred |
| A2 | PodDisruptionBudget | minAvailable ≥ 1 | `kubectl get pdb -n <ns>` | □ Pass □ Deferred |
| A3 | Degradation plan for dependent services | Clear degradation strategy when downstream services fail | Design document | □ Pass □ Deferred |
| A4 | Data persistence and backup | Critical configuration/data is recoverable | Backup and recovery exercise records | □ Pass □ Deferred |

#### Observability

| Number | Checklist Item | Acceptance Criteria | Verification Command/Method | Result |
|---|---|---|---|---|
| O1 | RED/USE metrics coverage | Request, error, latency, saturation are monitorable | `kubectl get servicemonitor -n <ns>` | □ Pass □ Deferred |
| O2 | Alert tiering and routing | Critical alerts reach On-Call within 5 minutes | Alertmanager configuration | □ Pass □ Deferred |
| O3 | Dashboard readiness | Each critical alert has corresponding Dashboard | Grafana link | □ Pass □ Deferred |
| O4 | Log collection | Logs integrated with Loki/Elasticsearch/SLS | `kubectl logs` / logging platform | □ Pass □ Deferred |

#### Security and Compliance

| Number | Checklist Item | Acceptance Criteria | Verification Command/Method | Result |
|---|---|---|---|---|
| S1 | RBAC least privilege | No cluster-admin abuse | `kubectl auth can-i --list` | □ Pass □ Deferred |
| S2 | NetworkPolicy | Default deny + whitelist | `kubectl get networkpolicy -n <ns>` | □ Pass □ Deferred |
| S3 | Secret management | Use External Secrets/Sealed Secrets/Vault | `kubectl get externalsecrets -n <ns>` | □ Pass □ Deferred |
| S4 | Image signature/scanning | Production images scanned and signed | Harbor/ACR scan reports | □ Pass □ Deferred |

#### Change and Rollback

| Number | Checklist Item | Acceptance Criteria | Verification Command/Method | Result |
|---|---|---|---|---|
| C1 | GitOps synchronization | Configuration managed under GitOps | `argocd app list` | □ Pass □ Deferred |
| C2 | Historical version retention | Retain ≥ 10 versions | `helm history <release>` | □ Pass □ Deferred |
| C3 | Rollback command verification | Rollback tested in staging | Rollback exercise records | □ Pass □ Deferred |
| C4 | Change window | Low-traffic window confirmed | Change request | □ Pass □ Deferred |

### 4.3 Risk Matrix Review

| Risk Item | Impact Scope | Probability | Risk Level | Mitigation Measures | Responsible Party | Status |
|---|---|---|---|---|---|---|
| Controller single point of failure | Cluster-level | Medium | High | Multi-replica + PDB + anti-affinity | SRE-A | □ |
| Certificate expiration causing service interruption | Component-level | Low | High | cert-manager + 30-day alert | SRE-B | □ |
| GitOps configuration drift | Cluster-level | Medium | Medium | Prohibit manual edit, enable drift detection | Platform Engineer | □ |
| Upgrade causing API deprecation | Application-level | Medium | Medium | Scan deprecated APIs before upgrade | Architect | □ |
| Monitoring gaps leading to mistaken release | Event Response | Low | Medium | Each alert includes Runbook | SRE-A | □ |
| Cost overrun | Financial | Low | Low | ResourceQuota + FinOps tags | Platform Engineer | □ |

**Risk Level Definition**: High = Must resolve or obtain risk acceptance before release; Medium = Requires mitigation measures and deferred item registration; Low = Acceptable, but requires ongoing monitoring.

### 4.4 Release Gate Confirmation

- [ ] **Gate 1: Self-Check Complete** — Owner completes PRR checklist and submits evidence.
- [ ] **Gate 2: Cross-Team Review** — SRE, Security, Architecture, and Network teams approve.
- [ ] **Gate 3: Risk Acceptance** — All high/medium risks are closed or deferred items have written management acceptance.
- [ ] **Gate 4: Exercise Complete** — staging environment has completed upgrade, rollback, and failover exercises.
- [ ] **Gate 5: Change Request Approved** — Approval completed in change management system, window confirmed.
- [ ] **Gate 6: Monitoring Ready** — Critical alerts, Dashboard, and Runbook all in place.

### 4.5 Sign-Off and Archival

After all relevant parties sign the sign-off form, PRR is approved. Review records, risk matrices, and checklist scans are archived in the change management system.

---

## 5. Key Checkpoints and Verification Commands

``` bash
# 🟢 Low Risk: read-only/information gathering, typically no side effects
# Verify Pod distribution
kubectl get pods -n <ns> -o wide --sort-by='.spec.nodeName'

# Verify PDB
kubectl get pdb -n <ns>

# Verify ServiceAccount permissions
kubectl auth can-i --list --as=system:serviceaccount:<ns>:<sa> | grep -E 'create|delete|patch'

# Verify NetworkPolicy
kubectl get networkpolicy -n <ns> -o yaml

# Verify Helm version history
helm history <release> -n <ns>

# Verify Argo CD synchronization status
argocd app get <app-name>

# Verify alert rules
kubectl get prometheusrules -n <ns>
```
---

## 6. Common Failures and Remediation

| Symptom | Possible Root Cause | Confirmation Command | Remediation |
|---|---|---|---|
| Many deferred items in PRR checklist | Incomplete documentation or exercises | Review each item | Supplement documentation, redo exercises, and re-evaluate |
| Dispute over risk level | Inconsistent assessment of impact scope or probability | Reference historical incident data | Engage third-party SRE/Architect for arbitration |
| Release gate not passed | Monitoring/alerting/rollback not ready | `kubectl get pods` / `argocd app get` | Defer release, complete gate requirements |
| Rollback exercise timeout | Complex dependencies or unscripted commands | Review exercise records | Script rollback steps and optimize |
| Configuration drift after review | Manual modifications not synced to GitOps | `argocd app diff` | Prohibit manual changes, enable drift detection |

---

## 7. Risks and Precautions

1. **PRR is not a formality**: Unchecked checklists leave production hazards; review meetings must verify evidence for each item.
2. **High-risk deferred items must be escalated**: Any high-risk deferred item without written management acceptance must not enter the release window.
3. **Rollback plan must be executable**: Rollback commands must be executed in staging and timed; documentation alone is insufficient.
4. **Alert rules must pass testing**: Untested alert rules must not be marked as passing in PRR.
5. **PRR records should be retained long-term**: Recommend retention for at least one year after component retirement to meet audit and review requirements.
6. **Post-release review cannot be omitted**: A first post-release review should be conducted within 30 days of release to verify SLO achievement, check for new alerts, and confirm rollback plan validity.


### 4.6 Review Output and Continuous Improvement

After PRR review is complete, record review conclusions, deferred item list, release gate status, and rollback commands in the change ticket. Within 30 days of release, conduct a post-release review meeting to verify whether SLO targets were met, identify any new alerts, and confirm rollback plan effectiveness. Post-release review conclusions should be fed back into this template to continuously optimize checklists and risk matrices, forming organizational knowledge accumulation.

---

## 8. Related Runbooks / Recommended Reading

- [[domain-07-platform-engineering/99-production-readiness-operations-guide.md|Platform Engineering Production Readiness Operations Guide]]
- [[domain-07-platform-engineering/99-karpenter-node-autoscaling-guide.md|Karpenter Node Auto-Scaling Practice Guide]]
- [[domain-07-platform-engineering/99-keda-event-driven-autoscaling-guide.md|KEDA Event-Driven Auto-Scaling Practice Guide]]
- [[domain-07-platform-engineering/12-automated-operations-toolchain.md|Automated Operations Toolchain]]
- [[domain-11-production-operations/02-change-management-guide.md|Change Management Guide]]
- [[domain-11-production-operations/99-production-readiness-operations-guide.md|Production Operations Domain Production Readiness Operations Guide]]

---

*This template should be customized based on organization size and component criticality. High-risk components are recommended to use more rigorous review processes and conduct the first post-release review within 30 days of deployment.*


<!-- risk-assessed -->
```