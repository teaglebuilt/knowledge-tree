---
title: Observability Production Readiness Operations Guide
description: Complete handbook for Kubernetes observability system readiness checks, risk mitigation, and daily operations for production environments
summary: Complete handbook for Kubernetes observability system readiness checks, risk mitigation, and daily operations for production environments
category: observability
tags:
- production
- best-practices
- observability
- operations
- monitoring
- logging
- tracing
- alerting
- slo
tier: core
created: '2026-07-01'
last_updated: '2026-07'
difficulty: advanced
reading_level: advanced
audience:
- SRE
- Operations Engineers
- Platform Engineers
estimated_read_time: 20min
intent_queries:
- What is the Observability Production Readiness Operations Guide
- How to operate observability according to production environment requirements
trigger_keywords:
- production-ready
- operations guide
- observability
- observability
- Prometheus
- Grafana
- SLO
prerequisites:
- kubectl-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
- '1.33'
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/99-production-readiness-operations-guide.md
authors:
- name: KUDIG Team
  role: contributor
---

> **Production Environment Safety Notice**
>
> This document contains directly executable operations commands. Before execution, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether it has been verified in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state but is usually recoverable), 🟢 Low risk / read-only (information collection, no side effects).


# Observability Production Readiness Operations Guide

> **Applicable Versions**: v1.28 - v1.33 | **Last Updated**: 2026-07 | **Applicable Roles**: SRE / Platform Engineers / Monitoring Engineers

This guide, from the production readiness perspective, systematically covers key checkpoints and operational commands for the Kubernetes observability system before deployment, during daily operations, in incident response, and in cross-team collaboration. The core coverage spans five pillars—metrics, logging, tracing, alerting, and SLO/SLI—and emphasizes the stability and recoverability of the observability platform itself.

Three iron laws of production readiness are particularly important in this domain: First, the observability platform cannot depend on observed objects to discover its own failures, so self-monitoring and external probing must be established. Second, any configuration change must be rollback-capable; Dashboards, alerting rules, and collection configurations must all be included in GitOps. Third, data retention, costs, and compliance requirements must be clarified at the design stage, not as remedial measures afterwards.

---

## 1. Production Environment Checklist

Before integrating the observability system into a production cluster, you must confirm each of the following items. The checklist is organized by pillar for use in PRR (Production Readiness Review).

### 1.1 Metrics

- [ ] **Prometheus High Availability**: At least 2 replicas, with data persistence achieved through Thanos Sidecar / Remote Write to avoid loss of historical metrics due to single-point failures.
- [ ] **Scrape Target Completeness**: Core components including kube-state-metrics, node-exporter, cAdvisor, APIServer, etcd, kubelet, CoreDNS are all collected with no `down` targets.
- [ ] **Label Cardinality Governance**: Single metric cardinality not exceeding 100,000; trigger alerts when job-level cardinality abnormally increases. See Risk 1 in Section 2.
- [ ] **Retention Policy Matches Capacity**: `retentionSize` is less than 80% of PVC capacity; local disk Prometheus configured for 15-30 days; long-term storage uses Thanos / Cortex / VictoriaMetrics.
- [ ] **Recording Rules Enabled**: Core dashboards use pre-aggregation rules with P99 query latency < 1 second.

### 1.2 Logging

- [ ] **Log Collection Rate > 99%**: kube-system, business namespaces, and audit logs are all collected with no collection agent crash-induced data gaps.
- [ ] **Log Parsing Standardization**: Container standard output is structured as `timestamp level msg`; critical business fields are uniformly extracted as indexed labels.
- [ ] **Log Retention and Tiered Storage**: Hot storage 7 days, warm storage 30 days, cold storage retained per compliance requirements for 180+ days with quantifiable costs.
- [ ] **Collection Agent Resource Limits**: Fluent Bit / Fluentd / Promtail have CPU/Memory limits configured to prevent log spikes from crippling nodes.

### 1.3 Distributed Tracing

- [ ] **OpenTelemetry Collector High Availability**: Multi-replica Deployment + HPA with backpressure configured on the receiving end.
- [ ] **Sampling Strategy Configurable**: Production default 1%-10% head-based sampling with 100% retention for error traces to prevent storage explosion.
- [ ] **Trace ID Propagation**: Entry gateway, business Pods, and database/middleware call chains have consistent Trace IDs that can be cross-referenced in logs.

### 1.4 Alerting

- [ ] **Alert Severity and Routing**: Three levels—critical / warning / info—with critical alerts reaching on-call engineers (PagerDuty/phone) within five minutes.
- [ ] **Actionable Alerts**: Every alert must include Runbook link, confirmation commands, and impact assessment; no context-less alerts like "CPU high."
- [ ] **Suppression and Deduplication Working**: Alertmanager `inhibit_rules` and `group_by` configuration has been tested to prevent alert storms.

### 1.5 SLO/SLI and Platform Self-Observability

- [ ] **SLO Defined and Implemented**: Core service Latency, Error Rate, and Throughput SLIs are in Prometheus; error budget policy has been published.
- [ ] **Observability Stack Self-Monitoring**: Prometheus, Grafana, Alertmanager, Loki, and Collector themselves are monitored; their own failures are detected before business failures.
- [ ] **Runbook and Dashboard One-to-One Correspondence**: Each critical alert corresponds to at least 1 Grafana Dashboard and 1 troubleshooting Runbook.
- [ ] **Cost and Quota Visualization**: Display observability storage and query costs by namespace, team, and environment to prevent bill surprises.
- [ ] **Disaster Recovery and Recoverability Verification**: Quarterly Prometheus/Loki/Grafana configuration recovery drills to verify backups are usable with RTO < 30 minutes.

---

## 2. Key Risks and Mitigation Measures

### Risk 1: Metric Cardinality Explosion

**Impact**: Prometheus memory, disk, and query latency spike dramatically, potentially causing OOMKilled or query timeouts, resulting in loss of all monitoring capability.

**Mitigation Commands and Configuration**:

> **🔴 High Risk Operation Warning**
>
> The following commands are irreversible or high-impact operations. Before execution please confirm:
> - Critical data and configurations have been backed up
> - You are within an approved change window
> - You have received authorization from relevant stakeholders
> - A rollback or recovery plan is prepared
> - The target cluster, Namespace, node/resource names are correct

``` bash
# 🔴 High risk: May cause data loss or service interruption; backup, change approval, and rollback plan required before execution
# 1. Scan high-cardinality metrics (top 20)
curl -sG 'http://prometheus:9090/api/v1/label/__name__/values' | jq -r '.data[]' | \
  while read m; do
    count=$(curl -sG 'http://prometheus:9090/api/v1/series' --data-urlencode "match[]=$m" | jq '.data | length')
    echo "$count $m"
  done | sort -rn | head -20

# 2. Limit label counts in Prometheus
prometheus:
  prometheusSpec:
    tsdb:
      outOfOrderTimeWindow: 0
    # Prometheus v2.53+ / v3.x supports enabling metric limits
    enableFeatures:
    - memory-snapshot-on-shutdown
```

**Production Recommendations**:

- Forbid clients from exposing unbounded labels (such as `user_id`, `request_id`, `trace_id`).
- Use `metric_relabel_configs` to drop or aggregate high-cardinality metrics.
- Enable `promtool check metrics` in CI to perform cardinality scanning on application-exposed metrics.

### Risk 2: Observability Platform Self Single-Point Failure

**Impact**: Monitoring, logging, and alerting themselves become unavailable, making production failures impossible to detect and handle promptly.

**Mitigation Measures**:

``` bash
# 🟡 Medium risk: Modifies cluster/resource state; confirm target, scope, and authorization before execution
# 1. Check Prometheus / Alertmanager / Grafana Pod replica distribution
kubectl get pods -n monitoring -o wide -l "app.kubernetes.io/name in (prometheus,alertmanager,grafana)"

# 2. Confirm Alertmanager cluster membership status
kubectl exec -n monitoring alertmanager-0 -- amtool --alertmanager.url=http://localhost:9093 cluster status

# 3. Check object storage backups (Thanos / Loki / Tempo)
kubectl get secret -n monitoring thanos-objstore -o yaml | grep bucket
```

**Production Recommendations**:

- Prometheus uses StatefulSet + PVC with at least 2 replicas deployed across availability zones; Service automatically switches query traffic on single-instance failure.
- Alertmanager uses 3 replicas forming a Gossip cluster with Pod AntiAffinity configured to prevent alert notification interruption from single-node failure.
- Grafana uses external PostgreSQL/MySQL for configuration storage; Dashboards are version-controlled with GitOps; direct manual modifications in production are forbidden.
- Enable cross-region replication or versioning on object storage to ensure Thanos, Loki, and Tempo long-term data recoverability during zone-level failures.

### Risk 3: Log Collection Delay or Loss

**Impact**: Missing logs at incident scenes make root cause analysis impossible; missing audit logs may create compliance risks.

**Mitigation Commands and Configuration**:

``` bash
# 🟢 Low risk: Read-only / information collection, typically no side effects
# 1. Check log collection Agent running status
kubectl get ds -n logging
kubectl top pods -n logging --sort-by=memory

# 2. Check Loki / Elasticsearch index and write rates
kubectl logs -n logging -l app=loki-distributor --tail=100 | grep -i "rate\|error"

# 3. Fluent Bit output buffer limit example
[OUTPUT]
    Name            loki
    Match           kube.*
    Host            loki-gateway
    Port            80
    Retry_Limit     5
    storage.type    filesystem
    storage.path    /var/log/flb-storage
```

**Production Recommendations**:

- Collection Agent uses DaemonSet with `resources.limits` configured and `priorityClassName: system-node-critical`.
- Enable local disk buffering when backend write fails to prevent log loss.
- Audit logs are stored independently; sharing the same backend tenant with business logs is forbidden.

### Risk 4: Alert Fatigue Causing Critical Alerts to Be Overwhelmed

**Impact**: Engineers become desensitized to alerts; P0 alert response delays; eventual incident escalation.

**Mitigation Commands and Configuration**:

```yaml
# Alertmanager grouping and suppression example
route:
  group_by: ['alertname', 'namespace', 'severity']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 12h
  routes:
  - match:
      severity: critical
    receiver: pagerduty-critical
    continue: false
inhibit_rules:
- source_match:
    severity: critical
  target_match:
    severity: warning
  equal: ['namespace', 'alertname']
```

**Production Recommendations**:

- Hold weekly alert quality meetings with targets of < 5 critical alerts/week and false positive rate < 5%; alerts with 3 consecutive false positives must be adjusted or decommissioned.
- Use `alertmanager-config-reloader` for configuration validation to prevent routing errors; major changes are tested on staging Alertmanager before traffic switchover.
- Prioritize implementing automated remediation (e.g., auto-restart hung Pods, auto-scale HPA) for high-frequency warning alerts rather than relying on manual response.
- Establish audit mechanism for "silenced alerts"; all manual silences must record ticket number, expected recovery time, and responsible party to prevent issue recurrence after silence expiration.

---

## 3. Daily Operations

### 3.1 Daily Patrol Checks

``` bash
# 🟡 Medium risk: Modifies cluster/resource state; confirm target, scope, and authorization before execution
# 1. Observability component health status
kubectl get pods -n monitoring -o wide
kubectl get pods -n logging -n tracing -o wide 2>/dev/null

# 2. Prometheus target status
kubectl port-forward svc/prometheus-k8s 9090:9090 -n monitoring &
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets[] | {job, health, lastError}'

# 3. Today's alert statistics (by severity)
curl -s 'http://alertmanager:9093/api/v1/alerts' | \
  jq -r '.data[] | .labels.severity' | sort | uniq -c | sort -rn

# 4. SLO error budget consumption
kubectl port-forward svc/grafana 3000:3000 -n monitoring &
# Open SLO Dashboard in Grafana and check if this week's error budget consumption < 20%
```

### 3.2 Capacity Management

``` bash
# 🟡 Medium risk: Modifies cluster/resource state; confirm target, scope, and authorization before execution
# 1. Prometheus TSDB size
kubectl exec -n monitoring prometheus-k0 -- du -sh /prometheus

# 2. Loki / Elasticsearch storage growth trend
kubectl exec -n logging loki-0 -- df -h /data

# 3. Top 10 query loads
curl -s 'http://prometheus:9090/api/v1/status/runtimeinfo' | jq '.data | {queryEngine: .queryEngine}'
```

### 3.3 Configuration Changes

``` bash
# 🟡 Medium risk: Modifies cluster/resource state; confirm target, scope, and authorization before execution
# 1. Helm diff before upgrade
helm diff upgrade kube-prometheus-stack prometheus-community/kube-prometheus-stack \
  -n monitoring -f values-production.yaml

# 2. Update PrometheusRule
kubectl apply -f rules/kubernetes-apps.yaml
promtool check rules rules/kubernetes-apps.yaml

# 3. Reload Grafana Dashboard
# Recommended through GitOps (Argo CD/Flux) for automatic synchronization; manual import is discouraged
```

### 3.4 Backup and Recovery

``` bash
# 🟢 Low risk: Read-only / information collection, typically no side effects
# 1. Backup Grafana configuration (if using external database, follow DB backup strategy)
kubectl get configmaps -n monitoring -l grafana_dashboard=1 -o yaml > grafana-dashboards-backup.yaml

# 2. Backup Alertmanager configuration
kubectl get secret alertmanager-kube-prometheus-stack-alertmanager -n monitoring -o yaml > alertmanager-secret-backup.yaml

# 3. Thanos / Loki object storage bucket backup strategy is covered by cloud provider lifecycle management
```

### 3.5 Emergency Drills and Chaos Engineering

``` bash
# 🟡 Medium risk: Modifies cluster/resource state; confirm target, scope, and authorization before execution
# 1. Simulate Prometheus single-replica failure and verify Thanos Query still returns complete data
kubectl scale sts prometheus-k8s --replicas=1 -n monitoring
# Observe and restore to 2 replicas after 5 minutes

# 2. Simulate Alertmanager total failure and verify critical alerts can be received within 5 minutes through backup channels (e.g., cloud monitoring)
kubectl scale sts alertmanager --replicas=0 -n monitoring

# 3. Use Litmus/Chaos Mesh to inject Pod failures into logging namespace
kubectl apply -f experiments/logging-pod-kill.yaml
```

**Drill Objectives**: Critical alerts are still issued despite observability platform single-point failures; historical metrics and log queries are unaffected during single-replica degradation; post-drill update Runbooks and on-call Playbooks.

---

## 4. Troubleshooting Quick Reference

| Symptom | Possible Cause | Confirmation Command | Fix/Mitigation |
|------|---------|---------|----------|
| Grafana all Dashboards show no data | Prometheus down or data source configuration error | `kubectl get pods -n monitoring -l app.kubernetes.io/name=prometheus`<br>`curl http://prometheus:9090/api/v1/status/runtimeinfo` | Restore Prometheus Pod; check Grafana DataSource URL and TLS |
| Prometheus OOMKilled | High cardinality metrics / too many scrape targets / retention too large | `kubectl describe pod -n monitoring prometheus-k0`<br>`curl .../api/v1/label/__name__/values` then calculate cardinality | Increase memory limit; add relabel filters; reduce retention; shard Prometheus |
| Alertmanager not sending notifications | Route mismatch / receiver configuration error / inhibit rule overkill | `kubectl logs -n monitoring alertmanager-0`<br>`amtool config routes test` | Validate alertmanager.yml; disable incorrect inhibit_rule; test receiver |
| Log search returns empty | Fluent Bit not started / Loki index expired / label mismatch | `kubectl get ds -n logging`<br>`kubectl logs -n logging fluent-bit-xxxxx`<br>`logcli labels` | Restart DaemonSet; check retention; confirm label selector |
| Distributed trace sampling is 0 | Collector sampling policy 0% / Span not reported / network policy blocks | `kubectl logs -n tracing otel-collector-0`<br>`curl otel-collector:8888/metrics` | Adjust sampling config; check OTLP endpoint; allow network policy |
| SLO Dashboard shows error budget exhausted | Real service degradation / SLI calculation error / threshold too strict | `kubectl get prometheusrules -n monitoring`<br>`promtool query instant ...` | Review SLI per actual business impact; if service issue confirmed, start incident response |
| Missing metrics from certain node | node-exporter Pod not ready / kubelet metrics endpoint unreachable | `kubectl get pods -n monitoring -l app.kubernetes.io/name=node-exporter -o wide`<br>`curl https://<node>:10250/metrics` | Restart node-exporter; check kubelet certificate and network policy |

---

## 5. Collaboration Boundaries with Other Domains

Observability is not an isolated system and must maintain clear boundaries and collaboration interfaces with adjacent domains.

- **Collaboration with Cluster Fundamentals Domain**: Control plane component (API Server, etcd, Scheduler, Controller Manager) health metrics are deployed and upgraded by the cluster domain; the observability domain is responsible for collection, alerting, and Dashboards. See Cluster Health Check Guide.
- **Collaboration with Networking Domain**: CNI, CoreDNS, Ingress, and Service Mesh network latency and packet loss metrics are interpreted by the networking domain; the observability domain is responsible for unified presentation and cross-domain correlation. Network policy changes must confirm they won't block Prometheus / Loki / OTLP traffic.
- **Collaboration with Security and Compliance Domain**: Audit logs, Falco runtime events, and RBAC change logs must be ingested into SIEM/SOAR. The observability domain handles collection and forwarding; the security domain handles policy, archival, and compliance response. See Logging Audit Compliance.
- **Collaboration with Platform Engineering Domain**: Platform engineering is responsible for observability platform deployment, tenant isolation, cost apportionment, and GitOps version management; the observability domain is responsible for usage norms, SLO definition, and alert quality governance.
- **Collaboration with Reliability Engineering Domain**: Reliability engineering leads SLO/SLI, error budget, and chaos engineering experiment design; the observability domain provides data foundation and alert triggering capability. See SLO/SLI System Construction.
- **Collaboration with Troubleshooting and Diagnostics Domain**: Observability data is the entry point for troubleshooting; complex scenarios (kernel, multi-tenant, network partition) are addressed by the troubleshooting domain with deep tool chains (eBPF, kubectl debug, inspektor-gadget).

---

## 6. Recommended Reading

### Core Domain Documents

- Domain 06 — Observability
- Cluster Health Check Guide
- Prometheus Enterprise Monitoring Deployment Guide
- Monitoring Playbooks
- SLO/SLI System Construction and Management
- Observability Troubleshooting Tools

### Related Domain Documents

- Cluster Infrastructure
- Security and Compliance
- Reliability Engineering
- Troubleshooting and Diagnostics

### Directions for Future Supplementation (see Gap Analysis)

The following topics remain gaps in current Domain coverage and are recommended for supplementation as standalone documents: Prometheus metric cardinality governance, eBPF observability, synthetic monitoring (Blackbox Exporter), observability platform self-monitoring Runbook, GPU/AI workload monitoring, multi-tenant observability isolation.

---

## See Also

- Back to Domain 06 index
- Production Operations Domain
- Domain Content Gap Analysis 2026-07-01


<!-- risk-assessed -->
