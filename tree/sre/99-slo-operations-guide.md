---
title: SLO Operations Guide
description: Kubernetes production SLO operations guide covering SLI/SLO/SLA definitions, error budgets, burn-rate alerting, alert review mechanisms, and Dashboard-as-Code.
summary: SLO operations guide covering SLI/SLO/SLA, error budgets, burn-rate alerting, alert review, and Dashboard-as-Code.
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/99-slo-operations-guide.md
category: observability
tags:
- production
- best-practices
- playbook
- observability
- slo
- sli
- sla
- error-budget
- burn-rate
- dashboard-as-code
tier: core
created: '2026-07-01'
last_updated: '2026-07'
difficulty: advanced
reading_level: advanced
audience:
- SRE
- Infrastructure Engineer
- Platform Engineer
- Monitoring Engineer
estimated_read_time: 25min
intent_queries:
- What is an SLO operations guide
- How to define SLI/SLO/SLA in Kubernetes
- How to implement burn-rate alerts and error budgets
trigger_keywords:
- SLO
- SLI
- SLA
- Error budget
- Burn-rate
- Alert review
- Dashboard-as-Code
prerequisites:
- kubectl-basics
- prometheus-basics
- observability-basics
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
---

> **Production Environment Safety Warning**
>
> This document contains runnable operations commands. Before execution, please confirm: the target cluster and namespace are correct; you have sufficient RBAC permissions; you have verified in a non-production environment. Command risk levels: 🔴 High risk (may cause data loss or service disruption), 🟡 Medium risk (will modify cluster state but is usually reversible), 🟢 Low risk/read-only (information collection, no side effects).


# SLO Operations Guide

> **Scope**: Teams defining, monitoring, and operating SLOs for platform components and business services on Kubernetes.
> **Target Audience**: SRE, Platform Engineers, Monitoring Engineers.
> **Last Updated**: 2026-07-01

This guide is a specialized SLO runbook for [[domain-06-observability/99-production-readiness-operations-guide.md|the Observability Production Readiness Operations Guide]], addressing the "Observability / SLO Operations" gap identified in the [[_reports/domain-content-gap-analysis-2026-07-01.md|domain content gap analysis]]. It systematically covers SLI/SLO/SLA, error budgets, burn-rate alerting, alert review mechanisms, and Dashboard-as-Code.

---

## 1. Use Cases and Scope

- Define SLOs for Kubernetes platform components (Ingress, CoreDNS, GitOps controllers, etc.).
- Establish SLI, SLO, SLA, and error budget policies for business services.
- Configure burn-rate alerts for early warning during rapid budget depletion.
- Establish alert quality review cadence to reduce alert fatigue.
- Manage Grafana Dashboards and PrometheusRules using GitOps.

---

## 2. Prerequisites and Tools

``` bash
# 🟢 Low risk: read-only/information collection, typically no side effects
# Required tools
kubectl version --client
helm version
promtool --version
# Optional: slo-generator / pyrra
```
- Prometheus + Alertmanager + Grafana already deployed.
- Key service RED metrics (Request Rate, Errors, Duration) are being collected.
- Change management and incident response processes established.

---

## 3. Core Concepts and Architecture

| Term | Definition | Example |
|---|---|---|
| **SLI** | Service quality indicator, quantifiable | Percentage of requests with P99 latency < 200ms over 7 days |
| **SLO** | Service level objective, the target value for an SLI | Percentage of requests with P99 latency < 200ms >= 99.9% |
| **SLA** | External commitment, typically includes compensation | Monthly availability >= 99.95% |
| **Error Budget** | Allowed failure ratio within the SLO | Monthly unavailability budget ≈ 0.1% (approximately 43 minutes) |

Error budget consumption rate determines alert sensitivity: higher **burn rate** indicates more urgent issues.

---

## 4. Standard Operating Procedures

### 4.1 Selecting SLIs

Recommendations for common service types:

| Service Type | Recommended SLI | Notes |
|---|---|---|
| Web / API | Availability + Latency | 2xx/5xx ratio, P99 latency |
| Asynchronous Processing | Throughput + Error Rate | Processing rate, dead-letter queue length |
| Storage | Availability + Consistency | Read/write success rate, replication lag |
| Batch Processing | Completion Rate + Duration | Task success rate, P95 completion time |

### 4.2 Defining SLOs and Error Budgets

Example: API availability SLO = 99.9% (monthly).

```text
Monthly error budget = (1 - 0.999) × 30 days × 24 hours × 60 minutes = 43.2 minutes
```

```yaml
# PrometheusRule example: error budget and burn rate
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: api-slo
  namespace: monitoring
spec:
  groups:
  - name: slo
    rules:
    - record: slo:api_availability:ratio_rate30d
      expr: |
        sum(rate(http_requests_total{job="api",code!~"5.."}[30d]))
        /
        sum(rate(http_requests_total{job="api"}[30d]))

    - alert: APIErrorBudgetBurnFast
      expr: |
        (
          sum(rate(http_requests_total{job="api",code=~"5.."}[1h]))
          /
          sum(rate(http_requests_total{job="api"}[1h]))
        ) > (1 - 0.999) * 14.4
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "API error budget burning rapidly (2% in 1h)"

    - alert: APIErrorBudgetBurnSlow
      expr: |
        (
          sum(rate(http_requests_total{job="api",code=~"5.."}[6h]))
          /
          sum(rate(http_requests_total{job="api"}[6h]))
        ) > (1 - 0.999) * 6
      for: 30m
      labels:
        severity: warning
      annotations:
        summary: "API error budget burning slowly, expected to exceed monthly target"
EOF
```

### 4.3 Burn-Rate Alert Rules

Google SRE Workbook recommends multiwindow multi-burn-rate:

| Burn Rate | Window | Meaning | Response Target |
|---|---|---|---|
| 14.4x | 1h / 5m | 2% of budget will be consumed within 1h | Page immediately |
| 6x | 6h / 30m | 5% of budget will be consumed within 6h | Handle during business hours |
| 3x | 3d / 6h | Long-term degradation | Handle next day |

### 4.4 Dashboard-as-Code

``` bash
# 🟡 Medium risk: will modify cluster/resource state, confirm target, impact scope and authorization before execution
# Manage Dashboards using Grafana Operator or ConfigMap
kubectl create configmap grafana-dashboard-api-slo \
  --from-file=api-slo.json \
  -n monitoring \
  --dry-run=client -o yaml | kubectl apply -f -

# Recommend generating and validating in CI using Jsonnet / Grizzly
```
Essential dashboard panels:

- Real-time SLI value versus SLO threshold comparison.
- Remaining error budget percentage and consumption trend.
- Current burn-rate value.
- Alert list for the last 30 days and false positive rate.

### 4.5 Alert Review Cadence

```bash
# Weekly statistics on alert triggers and false positive rate
curl -s 'http://alertmanager:9093/api/v1/alerts' | \
  jq -r '.data[] | .labels.alertname' | sort | uniq -c | sort -rn
```

- **Weekly alert quality meeting**: Review critical alerts, target < 5 critical alerts/week, false positives < 5%.
- **Monthly SLO review**: Examine error budget consumption root causes, update SLOs or business targets.
- **Quarterly threshold review**: Adjust burn-rate coefficients and windows based on business changes.

---

## 5. Key Checkpoints and Validation Commands

| Checkpoint | Verification Command | Success Criteria |
|---|---|---|
| SLI metrics exist | `curl -s 'http://prometheus:9090/api/v1/label/__name__/values' \| grep slo` | Recording rule defined |
| SLO Dashboard accessible | `curl -s http://grafana:3000/api/dashboards/uid/<uid>` | 200 OK |
| Burn-rate alerts active | `kubectl get prometheusrules -n monitoring` | Exists and VALID |
| Error budget trend visible | Grafana panel | Remaining budget percentage updates continuously |
| Alert routing correct | `amtool config routes test` | Critical routes to PagerDuty |

---

## 6. Common Issues and Remediation

| Symptom | Possible Root Cause | Verification Command | Fix |
|---|---|---|---|
| SLO Dashboard shows error budget exhausted | Real incident or SLI calculation error | `promtool query instant` | Verify SLI expression; initiate incident response for real issues |
| Burn-rate alerts frequently false | SLO too strict or traffic fluctuation during low periods | `rate(http_requests_total[1h])` | Loosen SLO, increase for window, use minimum request count filter |
| Alert not triggered but service degraded | SLI missing or label mismatch | `curl /api/v1/query?query=<sli>` | Add missing metrics, fix label selector |
| Error budget artificially exhausted | Planned maintenance not excluded | `sum(rate(...{maintenance!="true"}))` | Exclude planned maintenance windows from SLI |
| Dashboard and rules inconsistent | GitOps not synced | `argocd app diff <app>` | Force sync or rollback to previous version |

---

## 7. Risks and Caveats

- **Higher SLO is not always better**: The cost of 99.999% availability may far exceed business value; set targets based on user-perceptible impact.
- **Error budget cannot accumulate indefinitely**: Unused budget does not mean it can be squandered arbitrarily; it should serve as a safe buffer for releases and innovation.
- **Planned maintenance should be excluded**: Otherwise, SLO will be dragged down by normal change windows and lose its guidance value.
- **Avoid single-metric-driven decisions**: Monitor latency, errors, and throughput simultaneously to prevent sacrificing latency for availability.
- **Dashboard-as-Code requires versioning**: All Dashboards and Rules must use GitOps; direct modifications in production are prohibited.

---

## 8. Related Runbooks / Recommended Reading

### Core Documents in This Domain

- [[domain-06-observability/99-production-readiness-operations-guide.md|Observability Production Readiness Operations Guide]]
- [[domain-06-observability/06-slo-sli/18-slo-sli-system.md|SLO/SLI System Building and Management]]
- [[domain-06-observability/06-slo-sli/01-slo-engineering-practice.md|SLO Engineering Practice]]
- [[domain-06-observability/06-slo-sli/02-error-budget-policy.md|Error Budget Policy]]
- [[domain-06-observability/06-slo-sli/03-sli-implementation-guide.md|SLI Implementation Guide]]
- [[domain-06-observability/02-metrics/99-prometheus-enterprise-guide.md|Prometheus Enterprise Monitoring Deployment Guide]]
- [[domain-06-observability/05-alerting/21-monitoring-playbooks.md|Monitoring Playbooks]]

### Cross-Domain References

- [[_reports/domain-content-gap-analysis-2026-07-01.md|Domain Content Gap Analysis]]
- [[domain-09-reliability-engineering/README.md|Reliability Engineering]]
- [[domain-11-production-operations/README.md|Production Operations]]

---

*This guide should be reviewed monthly based on error budget consumption, alert false positive rates, and business changes. Recommend including SLO achievement rate in team OKRs.*


<!-- risk-assessed -->
