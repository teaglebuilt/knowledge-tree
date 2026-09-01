---
title: Platform Engineering Production Readiness Operations Guide
description: Comprehensive operations guide for production readiness checks, risk mitigation, daily operations, and troubleshooting for Kubernetes platform engineering domains
summary: Platform engineering domain production readiness checklist, critical risk mitigation, daily operations commands, and troubleshooting quick reference
category: domain/platform-engineering
tags:
- production
- best-practices
- platform-engineering
- operations
- readiness
- sre
tier: core
created: '2026-07-01'
last_updated: '2026-07'
difficulty: advanced
reading_level: advanced
audience:
- SRE
- Operations Engineer
- Platform Engineer
estimated_read_time: 20min
intent_queries:
- What is the Platform Engineering Production Readiness Operations Guide
- How to operate platform engineering according to production environment requirements
trigger_keywords:
- production ready
- operations guide
- platform engineering
- platform engineering
- PRR
prerequisites:
- kubectl-basics
- platform-engineering-basics
- helm-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
- '1.33'
authors:
- name: Dillan Teagle
  role: contributor
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/99-production-readiness-operations-guide.md
original_language: Chinese
---

> **Production Environment Security Notice**
>
> This document contains operations commands that can be executed directly. Before execution, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have verified in non-production environments. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (modifies cluster state but usually reversible), 🟢 Low Risk/Read-only (information gathering with no side effects).


# Platform Engineering Production Readiness Operations Guide

> **Scope**: Internal Developer Platforms (IDP) and platform engineering teams based on Kubernetes  
> **Last Updated**: 2026-07-01  
> **Difficulty**: Advanced

This guide covers the complete lifecycle of platform engineering from production readiness review (PRR) to daily operations and troubleshooting, with a focus on addressing the shortcomings identified in [[_reports/domain-content-gap-analysis-2026-07-01.md|domain content gap analysis]] including "production readiness checklist, patches and node lifecycle, certificate rotation, platform-level secret management, incident response" and other gaps.

The core responsibility of the Platform Engineering team is to provide stable, secure, and self-healing internal developer platforms (IDP) to application teams. Production readiness means not only successful component installation but also requires observability, rollback capability, recoverability, and clear incident response paths. This guide integrates checklists, risk mitigation, operations procedures, and troubleshooting quick reference into one executable entry document for SREs and platform engineers to use directly in PRR, pre-launch verification, and daily inspections.

---

## I. Production Environment Checklist

Before declaring platform engineering components (IDP portal, GitOps controllers, auto-scaling, multi-tenancy governance, secret sync, etc.) as production-ready, you must confirm the following 12 checkpoints item by item. Each item includes verification commands and clear passing criteria for easy checkoff in PRR meetings or launch gates.

| # | Checklist Item | Verification Command / Method | Passing Criteria |
|:---|:---|:---|:---|
| 1 | Control Plane High Availability | `kubectl get nodes -l node-role.kubernetes.io/control-plane` | At least 3 control plane nodes with Ready status |
| 2 | etcd Backup Recoverability | `etcdctl snapshot status /backup/etcd-$(date +%F).db` | Daily backups, recovery drill completed within 72 hours |
| 3 | Platform Core Component PDB | `kubectl get pdb -n argocd` / `-n keda` / `-n karpenter` | minAvailable ≥ 1, covering all controller Pods |
| 4 | Multi-tenant Resource Isolation | `kubectl get resourcequota -n <team>` | Each namespace configured with CPU / Memory / Pod / PVC quotas |
| 5 | Default Deny Network Policy | `kubectl get networkpolicies -A` | Platform namespaces with default deny enabled, only whitelisted ports allowed |
| 6 | Secret Encryption and Rotation | `kubectl get secret -n platform` with KMS / Vault audit | Secrets encrypted at rest, platform-level credentials rotated every 90 days |
| 7 | Certificate Expiration Monitoring | `kubectl get certificates -A` / cert-manager metrics | All certificates have remaining validity ≥ 30 days |
| 8 | GitOps Source Integrity | `argocd app list` + `argocd repo list` | Repositories have GPG / SSH signature verification enabled |
| 9 | Auto-scaling Baseline | `kubectl get nodepool,scaledobject -A` | NodePool / ScaledObject configurations verified through load testing |
| 10 | Observability Full Coverage | `kubectl get servicemonitor,probe -A` | Platform components expose RED/USE metrics with alerts configured |
| 11 | Disaster Recovery Runbook | Check corresponding playbooks in `domain-09-reliability-engineering` | RTO/RPO confirmed by business, quarterly drills conducted |
| 12 | Change Window and Rollback | `argocd app history` / Helm release history | All platform components retain ≥ 10 historical versions |

Each item in the checklist should be assigned to a responsible owner with a check frequency. It is recommended to maintain an auditable PRR record sheet in Confluence, Notion, or internal Git repository, documenting each review date, findings, remediation owner, and re-verification results. For multi-cluster platforms, repeat this checklist on each production cluster and version the cluster baseline configuration through GitOps to ensure any deviations are quickly detected.

---

## II. Critical Risks and Mitigation Measures

The high-impact risks faced by the platform engineering domain in production and corresponding mitigation solutions are as follows. Each risk includes commands or configuration snippets that can be executed directly for inclusion in runbooks or automation scripts.

### 2.1 GitOps Controller Single Point of Failure

- **Risk**: Argo CD / Flux controller crashes causing application sync failure and inability to rollback.
- **Mitigation**:
  ```bash
  # Check controller high availability replicas
  kubectl get deploy argocd-server argocd-repo-server argocd-application-controller -n argocd -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.replicas}{"\n"}{end}'
  # Recommendation: server ≥ 2, repo-server ≥ 2, application-controller enable sharding (--replicas > 1)
  ```
- **Configuration Notes**: Set PodDisruptionBudget, anti-affinity, and persistent Redis for all controllers. Additionally, it is recommended to configure Argo CD's `application-controller` in sharding mode to improve sync throughput in large-scale clusters; deploy Redis using Sentinel or Redis Cluster mode to avoid single points of failure. The platform team should regularly execute `argocd admin settings validate` to validate configuration consistency.

### 2.2 Certificate Expiration Causing Service Interruption

- **Risk**: cert-manager, Ingress, and platform webhook certificate expiration causing API unavailability.
- **Mitigation**:
  ```bash
  # View certificate status managed by cert-manager
  kubectl get certificate -A
  kubectl get certificaterequest,order,challenge -n cert-manager
  # Emergency renewal
  kubectl cert-manager renew --namespace=<ns> <certificate-name>
  ```
- **Configuration Notes**: Configure `Certificate` with `renewBefore: 720h`, Prometheus alert on `certmanager_certificate_expiration_timestamp_seconds < 30*24*3600`. For Kubernetes internal CA (front-proxy, etcd, kubelet) and Ingress mTLS certificates, establish independent tracking tables with clear expiration times, owners, and rotation windows. It is recommended to categorize certificate expiration alerts: ≤ 30 days warning, ≤ 7 days critical, ≤ 1 day page.

### 2.3 Node Patches and Lifecycle Out of Control

- **Risk**: OS kernel vulnerabilities left unpatched for extended periods, or node replacement causing stateful service disruption.
- **Mitigation**:
  ```bash
  # Set node expiration policy when using Karpenter
  kubectl patch nodepool default --type merge -p '{"spec":{"disruption":{"expireAfter":"720h"}}}'
  # Manual node maintenance
  kubectl drain <node> --ignore-daemonsets --delete-emptydir-data --pod-selector='app!=critical-db'
  ```
- **Configuration Notes**: Coordinate with EKS Node Update / GKE Node Auto-Repair / ACK node pool image upgrade strategies. Establish a node maintenance window, preferring immutable infrastructure (cattle node) node replacement over in-place upgrades. For stateful workloads, use PodDisruptionBudget, topology spread constraints, and persistent volume snapshots to ensure data availability during node replacement. All node replacement operations must go through change management approval and notify affected business units before maintenance.

### 2.4 Platform-Level Secret Leakage

- **Risk**: Git repository mistakenly commits secrets, third-party scaler credentials stored in plaintext.
- **Mitigation**:
  ```bash
  # Verify Sealed Secrets / External Secrets status
  kubectl get sealedsecrets -A
  kubectl get externalsecrets -n platform
  # Prohibit direct use of opaque Secrets for storing cloud credentials
  kubectl get secrets -A --field-selector=type=Opaque -o custom-columns='NS:.metadata.namespace,NAME:.metadata.name' | grep -E 'aws|azure|gcp'
  ```
- **Configuration Notes**: Use External Secrets Operator to integrate with Vault / AWS Secrets Manager / Azure Key Vault with automatic secret rotation enabled. Prohibit storing any raw secrets in Git repositories. CI/CD pipelines should integrate `git-secrets`, `truffleHog`, or `gitleaks` for pre-commit scanning. For critical secrets like KEDA TriggerAuthentication and Argo CD repository credentials, implement least privilege principles and regularly audit `kubectl get secret` access logs.

### 2.5 Multi-tenant Resource Contention and Noisy Neighbor

- **Risk**: A team's Pod exhausts node resources, affecting platform core services.
- **Mitigation**:
  ```bash
  # Check LimitRange / ResourceQuota
  kubectl describe limitrange -n <team>
  kubectl describe resourcequota -n <team>
  # Enable PriorityClass and admission policies
  kubectl get priorityclass
  ```
- **Configuration Notes**: Platform core components use `system-cluster-critical` PriorityClass; tenant namespaces default to limiting CPU / memory requests and limits. It is recommended to create ResourceQuota, LimitRange, and NetworkPolicy templates for each tenant, enforcing injection through Kyverno, OPA Gatekeeper, or ValidatingAdmissionPolicy. For shared node pools, enable cgroup v2 and strict CPU / memory request matching for scheduling to prevent resource overselling leading to tail latency.

---

## III. Daily Operations

Daily operations should follow the principle of "observe first, confirm, then change", with all changes preferably initiated through GitOps and maintaining audit trails. The following commands are categorized by inspection frequency: daily, weekly, and monthly.

### 3.1 Daily Inspection

``` bash
# 🟢 Low Risk: Read-only/information gathering, usually no side effects
# 1. Core namespace Pod status
kubectl get pods -n argocd -n keda -n karpenter -n cert-manager -n vault --show-labels

# 2. Platform component resource usage
kubectl top pods -n argocd
kubectl top nodes -l node-role.kubernetes.io/platform=true

# 3. Event check (excluding Normal)
kubectl get events -A --field-selector type!=Normal --sort-by=.lastTimestamp | tail -50

# 4. Node status and taints
kubectl get nodes -o custom-columns='NAME:.metadata.name,STATUS:.status.conditions[-1].type,TAINTS:.spec.taints[*].key'
```
The focus of daily inspection is discovering anomalous events, Pod restarts, and sudden increases in resource usage as early signals. It is recommended to encapsulate the above commands into a `platform-daily-check` script and run it on designated SRE tool nodes through CronJob, with output pushed to Slack or enterprise WeChat.

### 3.2 Weekly Inspection

``` bash
# 🟢 Low Risk: Read-only/information gathering, usually no side effects
# Check platform component versions and upgrade availability
helm list -n argocd
helm list -n keda
helm list -n karpenter

# Check certificate remaining validity
kubectl get certificate -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{"\t"}{.status.notAfter}{"\n"}{end}' | sort -k2

# Check unused ConfigMap / Secret garbage
kubectl get configmaps,secrets -A --field-selector=type=Opaque | wc -l
```
Weekly inspections focus on version drift, certificate health, and resource garbage. It is recommended to compile available upgrades into a weekly report for platform team review and inclusion in next week's change plan.

### 3.3 Monthly Inspection

``` bash
# 🟢 Low Risk: Read-only/information gathering, usually no side effects
# Check platform component RBAC and permission convergence
kubectl auth can-i --list -n argocd | grep -E 'create|delete|update'

# Check node operating system and kernel version
kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.status.nodeInfo.osImage}{"\t"}{.status.nodeInfo.kernelVersion}{"\n"}{end}'

# Check NodePool / ScaledObject resource limits
kubectl get nodepool -A -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.limits}{"\n"}{end}'
```
Monthly inspections focus on permission convergence, node lifecycle, and resource limits. It is recommended to share inspection results with the FinOps team to identify long-term underutilized node pools or over-configured ScaledObjects.

### 3.4 GitOps Application Sync and Rollback

```bash
# View application health status
argocd app list
argocd app get <app-name>

# Manually sync and wait
argocd app sync <app-name> --prune --timeout 300

# Rollback to previous version
argocd app rollback <app-name> 0
```

When executing GitOps sync during change windows, it is recommended to first use `argocd app diff <app-name>` to confirm the actual change scope and avoid accidental resource deletion. For critical platform components, rollback operations should undergo two-person review and the rollback reason should be recorded in the change management tool.

### 3.5 Auto-scaling Routine Checks

``` bash
# 🟢 Low Risk: Read-only/information gathering, usually no side effects
# Karpenter
kubectl get nodeclaims -A
kubectl get nodepool -A -o wide

# KEDA
kubectl get scaledobject -A
kubectl get hpa -A -l app.kubernetes.io/managed-by=keda-operator
```
Auto-scaling routine checks should be conducted in combination with business load patterns. Focus on whether NodePool is approaching limits, whether ScaledObject has triggered maxReplicas, and whether HPA metrics show anomalous fluctuations.

### 3.6 Platform-Level Certificate and Secret Rotation

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, please confirm target, impact scope, and authorization before execution
# Trigger cert-manager certificate rotation
kubectl cert-manager renew --namespace=platform --all

# Rolling restart workloads that depend on the Secret
kubectl rollout restart deploy/<workload> -n <ns>
```
Secret rotation should preferably be executed during business off-peak hours, with advance verification in the staging environment for dependent workload rolling restart behavior. For components that cannot hot-reload, notify business units in advance and prepare maintenance windows.

---

## IV. Troubleshooting Quick Reference

The quick reference table below covers the most common failure scenarios in the platform engineering domain. Each row is organized by the structure "Symptom → Possible Root Cause → Verification Command → Resolution", enabling on-call engineers to quickly locate and contain issues during incidents.

| Symptom | Possible Root Cause | Verification Command | Resolution |
|:---|:---|:---|:---|
| Argo CD application long stuck in `Unknown` | Application controller sharding imbalance or Redis disconnection | `kubectl logs -n argocd deploy/argocd-application-controller` | Restart controller shard leader; check Redis HA |
| `ScaledObject` status `False` | TriggerAuthentication missing or credentials expired | `kubectl describe scaledobject <name> -n <ns>` | Update Secret / TriggerAuthentication, recreate ScaledObject |
| Karpenter unable to create NodeClaim | IAM / subnet / security group label mismatch | `kubectl logs -n karpenter deploy/karpenter-controller` | Check EC2NodeClass selector consistency with cloud resource labels |
| Platform Pod frequently evicted | Node resource pressure or taint drift | `kubectl describe node <node>` | Scale up node pool; adjust Pod requests / QoS |
| cert-manager order stuck | ACME verification failure or DNS configuration error | `kubectl describe challenge -n <ns>` | Fix DNS records; clean up challenge to let cert-manager rebuild |
| Tenant application unable to pull image | Image repository credentials missing or expired | `kubectl get secret regcred -n <ns>` | Update imagePullSecret or enable ECR credential helper |
| Platform API slow response or timeout | API server high load or etcd high latency | `kubectl top node -l node-role.kubernetes.io/control-plane` / `etcdctl endpoint health` | Scale up control plane nodes; check etcd disk I/O and fragmentation |
| GitOps sync causes resource deletion | prune enabled and repository path misconfigured | `argocd app diff <app-name>` | Immediately disable auto-sync and prune, rollback application definition |
| KEDA slow scale-down causing resource waste | stabilizationWindowSeconds too long | `kubectl get hpa <name> -o yaml` | Adjust scale-down stability window and policy |
| Multi-tenant namespace exceeds quota | ResourceQuota configuration missing or too large | `kubectl describe resourcequota -n <team>` | Tighten quota, enable admission policy to auto-inject default quotas |

When troubleshooting, prioritize using `kubectl get events -A --sort-by=.lastTimestamp` to get cluster-level event context, then combine with specific component logs for deeper diagnosis. For incidents with business impact, immediately create an incident ticket after containment, documenting timeline, root cause hypotheses, and measures taken.

---

## V. Collaboration Boundaries with Other Domains

Platform engineering is in a bridging position that requires clarifying responsibility boundaries and collaboration interfaces with the following domains. Clear boundaries prevent "gray zones" where everyone thinks it's the other's responsibility and improve incident response efficiency.

- **Collaboration with [[domain-08-release-change-management/README.md|Release and Change Management]]**: Platform team responsible for high availability of GitOps controllers, image repositories, secret sync and other infrastructure; change management team responsible for application release strategies, canary deployment and rollback procedures.
- **Collaboration with [[domain-05-security-compliance/README.md|Security and Compliance]]**: Platform team implements network policies, secret management, admission policies, and Pod Security Standards; security compliance team sets policy baselines, audits, and incident response standards.
- **Collaboration with [[domain-06-observability/README.md|Observability]]**: Platform team exposes platform component metrics, logs, and traces; observability team responsible for SLO/SLI system, alert routing, and long-term storage.
- **Collaboration with [[domain-09-reliability-engineering/README.md|Reliability Engineering]]**: Platform team maintains node lifecycle, auto-scaling, and certificate rotation; reliability team responsible for RTO/RPO design, disaster recovery drills, and chaos engineering.
- **Collaboration with [[domain-11-production-operations/README.md|Production Operations]]**: Platform team provides IDP self-service capabilities and operations toolchain; production operations team responsible for on-call, ticketing, FinOps, and incident communication.

Beyond the collaboration relationships above, the platform engineering domain should also stay synchronized with the [[domain-12-cloud-providers/README.md|Cloud Providers]] domain to keep informed of new features, version lifecycles, and known issues with managed Kubernetes; collaborate with the [[domain-13-container-runtime/README.md|Container Runtime]] domain to advance image security scanning, runtime upgrades, and node image standardization.

---

## VI. Recommended Reading

### Key Documents in this Domain

- [[domain-07-platform-engineering/99-karpenter-node-autoscaling-guide.md|Karpenter Node Auto-scaling Practical Guide]]
- [[domain-07-platform-engineering/99-keda-event-driven-autoscaling-guide.md|KEDA Event-Driven Auto-scaling Practical Guide]]
- [[domain-07-platform-engineering/12-automated-operations-toolchain.md|Automated Operations Toolchain]]
- [[domain-07-platform-engineering/operate/06-monitoring-alerting-system.md|Monitoring and Alerting System]]

### Core Documents from Related Domains

- [[domain-08-release-change-management/README.md|Release and Change Management]]
- [[domain-05-security-compliance/README.md|Security and Compliance]]
- [[domain-09-reliability-engineering/README.md|Reliability Engineering]]
- [[domain-06-observability/README.md|Observability]]

---

*This guide serves as an entry document for platform engineering production readiness. It is recommended to be used in combination with domain-specific documents on auto-scaling, GitOps, monitoring and alerting, and should be updated quarterly based on actual drill results.*


<!-- risk-assessed -->