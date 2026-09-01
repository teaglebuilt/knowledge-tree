---
title: PagerDuty and Opsgenie Alert Integration
description: 'Alert platform integration: PagerDuty Service/Integration Key configuration, Opsgenie Team/Responder configuration, on-call scheduling, escalation policies, alert deduplication'
summary: 'PagerDuty/Opsgenie integration, on-call scheduling, and escalation policy configuration'
category: observability
tags:
- pagerduty
- opsgenie
- oncall
- escalation
- alert-integration
tier: supporting
created: '2026-07-02'
last_updated: 2026-07
difficulty: advanced
reading_level: advanced
audience:
- SRE
- Security Engineer
- Platform Engineer
estimated_read_time: 15min
intent_queries:
- What is PagerDuty and Opsgenie alert integration
- How to configure PagerDuty Service
trigger_keywords:
- PagerDuty
- Opsgenie
- On-call scheduling
- Escalation policy
- Alert deduplication
prerequisites:
- kubectl-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: Dillan Teagle
  role: contributor
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/05-alerting/02-pagerduty-opsgenie-integration.md
---

> **Production Environment Security Notice**
>
> This document contains operationally executable commands. Before execution, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have tested in a non-production environment. Command risk levels are marked: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state but usually reversible), 🟢 Low risk/read-only (information collection, no side effects).


# PagerDuty and Opsgenie Alert Integration

## Overview

PagerDuty and Opsgenie are mainstream event management platforms that provide alert reception, on-call scheduling, escalation policies, and collaborative response capabilities. This document covers a complete integration solution between both platforms and Kubernetes alert systems.

## 1. PagerDuty Integration

### 1.1 Service Configuration

```bash
# Create PagerDuty Service
# 1. Log in to PagerDuty → Services → New Service
# 2. Select "Use our API directly" as Integration Type
# 3. Record Integration Key

# Integration Key example: a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
```

### 1.2 Alertmanager Configuration

```yaml
# alertmanager.yaml
global:
  pagerduty_url: 'https://events.pagerduty.com/v2/enqueue'

receivers:
# P0 critical alert
- name: pagerduty-p0
  pagerduty_configs:
  - routing_key: '<p0-integration-key>'
    severity: critical
    description: '[P0] {{ .CommonLabels.alertname }} - {{ .CommonLabels.namespace }}'
    details:
      firing_count: '{{ .Alerts.Firing | len }}'
      resolved_count: '{{ .Alerts.Resolved | len }}'
      cluster: '{{ .CommonLabels.cluster }}'
      namespace: '{{ .CommonLabels.namespace }}'
      runbook_url: '{{ (index .Alerts 0).Annotations.runbook_url }}'
      grafana_url: '{{ (index .Alerts 0).GeneratorURL }}'
    source: '{{ .CommonLabels.source }}'
    component: '{{ .CommonLabels.component }}'
    group: '{{ .GroupLabels.namespace }}'
    class: '{{ .GroupLabels.alertname }}'
    links:
    - href: '{{ (index .Alerts 0).GeneratorURL }}'
      text: 'View in Grafana'
    - href: '{{ (index .Alerts 0).Annotations.runbook_url }}'
      text: 'Runbook'

# P1 high priority alert
- name: pagerduty-p1
  pagerduty_configs:
  - routing_key: '<p1-integration-key>'
    severity: error
    description: '[P1] {{ .CommonLabels.alertname }} - {{ .CommonLabels.namespace }}'
    details:
      cluster: '{{ .CommonLabels.cluster }}'
      namespace: '{{ .CommonLabels.namespace }}'

# General alerts
- name: pagerduty-general
  pagerduty_configs:
  - routing_key: '<general-integration-key>'
    severity: '{{ .CommonLabels.severity }}'
    description: '{{ .CommonLabels.alertname }}'
```

### 1.3 Event Deduplication

```yaml
# PagerDuty automatic deduplication (based on routing_key + source + severity)
# Alertmanager has already deduplicated by group_by, but duplicates may still occur
# Use custom_details.dedup_key to control deduplication

receivers:
- name: pagerduty-dedup
  pagerduty_configs:
  - routing_key: '<integration-key>'
    description: '{{ .CommonLabels.alertname }}'
    details:
      dedup_key: '{{ .CommonLabels.alertname }}-{{ .CommonLabels.namespace }}-{{ .CommonLabels.pod }}'
```

### 1.4 Escalation Policy Configuration

```yaml
# PagerDuty Escalation Policy (configured via API)
# Level 1: On-call engineer (immediate notification)
# Level 2: Team lead (after 5 minutes)
# Level 3: Engineering manager (after 15 minutes)
# Level 4: VP Engineering (after 30 minutes)

# API configuration example
curl -X POST https://api.pagerduty.com/escalation_policies \
  -H "Authorization: Token token=<api-token>" \
  -H "Content-Type: application/json" \
  -d '{
    "escalation_policy": {
      "name": "K8s Production Escalation",
      "description": "Escalation policy for K8s production alerts",
      "num_loops": 3,
      "escalation_rules": [
        {
          "escalation_delay_in_minutes": 5,
          "targets": [
            { "id": "<sre-team-id>", "type": "schedule_reference" }
          ]
        },
        {
          "escalation_delay_in_minutes": 10,
          "targets": [
            { "id": "<team-lead-id>", "type": "user_reference" }
          ]
        },
        {
          "escalation_delay_in_minutes": 15,
          "targets": [
            { "id": "<engineering-manager-id>", "type": "user_reference" }
          ]
        }
      ]
    }
  }'
```

## 2. Opsgenie Integration

### 2.1 Team and Integration Configuration

```bash
# Create Opsgenie Integration
# 1. Log in to Opsgenie → Teams → Create Team
# 2. Add Integration → Prometheus
# 3. Record API Key

# API Key example: 12345678-1234-1234-1234-123456789012
```

### 2.2 Alertmanager Configuration

```yaml
# alertmanager.yaml
receivers:
- name: opsgenie-production
  opsgenie_configs:
  - api_key: '<opsgenie-api-key>'
    api_url: 'https://api.opsgenie.com'
    message: '[{{ .Status | toUpper }}] {{ .CommonLabels.alertname }}'
    description: |
      {{ .CommonLabels.alertname }}
      Namespace: {{ .CommonLabels.namespace }}
      Severity: {{ .CommonLabels.severity }}
    source: '{{ .CommonLabels.source }}'
    tags:
    - '{{ .CommonLabels.severity }}'
    - '{{ .CommonLabels.namespace }}'
    - '{{ .CommonLabels.alertname }}'
    details:
      firing: '{{ .Alerts.Firing | len }}'
      resolved: '{{ .Alerts.Resolved | len }}'
      cluster: '{{ .CommonLabels.cluster }}'
      runbook_url: '{{ (index .Alerts 0).Annotations.runbook_url }}'
    responders:
    - name: 'SRE Team'
      type: team
    - name: 'On-Call Schedule'
      type: schedule
    priority: '{{ if eq .CommonLabels.severity "critical" }}P1{{ else if eq .CommonLabels.severity "warning" }}P3{{ else }}P5{{ end }}'
    entity: '{{ .CommonLabels.namespace }}'
    note: 'Auto-generated alert from Prometheus'
```

### 2.3 Opsgenie On-Call Scheduling

```yaml
# Opsgenie Schedule configuration (via Terraform)
resource "opsgenie_schedule" "sre_oncall" {
  name        = "SRE On-Call"
  description = "SRE team on-call rotation"
  timezone    = "Asia/Shanghai"

  rules {
    frequency  = "weekly"
    start_day  = "monday"
    end_day    = "sunday"
    start_hour = 0
    start_min  = 0
    end_hour   = 24
    end_min    = 0
    participants {
      type = "user"
      id   = opsgenie_user.sre1.id
    }
    participants {
      type = "user"
      id   = opsgenie_user.sre2.id
    }
    participants {
      type = "user"
      id   = opsgenie_user.sre3.id
    }
  }

  overrides {
    name        = "Holiday Coverage"
    start_date  = "2026-07-04T00:00:00+08:00"
    end_date    = "2026-07-05T00:00:00+08:00"
    recipient {
      type = "user"
      id   = opsgenie_user.backup_sre.id
    }
  }
}
```

### 2.4 Opsgenie Escalation Policy

```yaml
# Opsgenie Escalation configuration
resource "opsgenie_escalation" "production" {
  name = "Production Escalation"

  rule {
    delay    = 0
    recipient {
      type = "schedule"
      id   = opsgenie_schedule.sre_oncall.id
    }
    notify_type = "default"
  }

  rule {
    delay    = 5
    recipient {
      type = "team"
      id   = opsgenie_team.platform.id
    }
    notify_type = "default"
  }

  rule {
    delay    = 15
    recipient {
      type = "user"
      id   = opsgenge_user.engineering_manager.id
    }
    notify_type = "all"
  }

  rule {
    delay    = 30
    recipient {
      type = "user"
      id   = opsgenie_user.vp_engineering.id
    }
    notify_type = "all"
  }

  repeat {
    wait_interval = 15
    count         = 3
    reset_recipient_type = "to-previous"
  }
}
```

## 3. Alert Deduplication Strategy

### 3.1 Alertmanager Deduplication

```yaml
# Deduplication based on group_by
route:
  group_by: ['alertname', 'namespace', 'severity']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h

  routes:
  # Fine-grained deduplication by pod
  - match:
      app: api-gateway
    group_by: ['alertname', 'namespace', 'pod']
```

### 3.2 Platform-Level Deduplication

```yaml
# PagerDuty deduplication (based on routing_key + source + severity)
# Automatic deduplication window: default 24 hours

# Opsgenie deduplication (based on alias)
receivers:
- name: opsgenie-dedup
  opsgenie_configs:
  - api_key: '<api-key>'
    alias: '{{ .CommonLabels.alertname }}-{{ .CommonLabels.namespace }}-{{ .CommonLabels.severity }}'
```

## 4. Best Practices

```
Alert platform integration checklist:

□ Configure PagerDuty/Opsgenie Service and Integration Key
□ Set up tiered alert routing (P0/P1/P2/P3)
□ Configure on-call scheduling (Schedule)
□ Set up escalation policy (Escalation Policy)
□ Configure alert deduplication (group_by + alias)
□ Set up notification channels (Push/SMS/Email/Phone)
□ Configure silence and maintenance windows
□ Regularly review alert rules
□ Test alert escalation process
□ Monitor alert response SLA
```

## Related

- [[domain-06-observability/05-alerting/01-alertmanager-deep-configuration|Alertmanager Deep Configuration]]
- [[domain-06-observability/05-alerting/03-alert-fatigue-reduction-strategies|Alert Fatigue Governance]]

## See Also

- [PagerDuty API Documentation](https://developer.pagerduty.com/docs/rest-api-v2/)
- [Opsgenie API Documentation](https://docs.opsgenie.com/docs/api-overview)


<!-- risk-assessed -->
