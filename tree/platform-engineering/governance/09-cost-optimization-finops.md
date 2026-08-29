---
title: Production Troubleshooting
description: 'Target audience: SRE team, incident response engineers, operations personnel'
summary: 'Target audience: SRE team, incident response engineers, operations personnel'
category: general
tags:
- k8s
- devops
- daily-ops
- troubleshooting
- production
- apiserver
- scheduler
- calico
- ingress
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All engineers
estimated_read_time: 15min
intent_queries:
- What are common issues with 15-production-troubleshooting?
- How to troubleshoot 15-production-troubleshooting related issues?
- Failure handling methods for 15-production-troubleshooting
trigger_keywords:
- Production environment fault diagnosis
- Production
- Troubleshooting
- platform
- engineering
prerequisites:
- kubectl-basics
- platform-engineering-basics
- cni-basics
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./operate/15-production-troubleshooting.md
original_language: Chinese
---

> **Production Environment Security Tips**
>
> This document contains directly executable operations commands. Before execution, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have tested in non-production environments. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state, but usually reversible), 🟢 Low risk/read-only (information gathering, no side effects).




title: Production Troubleshooting
description: 'Target audience: SRE team, incident response engineers, operations personnel'
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- scheduler
- [[Ingress|ingress]]
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Platform engineers
- Operations engineers
estimated_read_time: 5min
intent_queries:
- What is Production Environment Fault Diagnosis (Production Troubleshooting)
- How to perform Production Environment Fault Diagnosis (Production Troubleshooting)
- [[Kubernetes|Kubernetes]] 9 platform ops best practices
- Production Environment Fault Diagnosis (Production Troubleshooting) troubleshooting
- Production Environment Fault Diagnosis (Production Troubleshooting) troubleshooting steps
trigger_keywords:
- Production environment fault diagnosis
- Production
- Troubleshooting
- platform
- ops
cross_refs:
- type: domain
  path: ../domain-06-observability/
  label: 'Related knowledge domain: domain-06-observability'
- type: domain
  path: ../domain-15-specialized-tech/
  label: 'Related knowledge domain: domain-15-specialized-tech'
- type: domain
  path: ../domain-10-troubleshooting-diagnostics/
  label: 'Related knowledge domain: domain-10-troubleshooting-diagnostics'
authors:
- name: KUDIG Team
  role: contributor
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
---
# Production Troubleshooting

> **Applicable versions**: Kubernetes v1.25 - v1.32 | **Document version**: v1.0 | **Last updated**: 2026-02
> **Target audience**: SRE team, incident response engineers, operations personnel

<!-- chunk: Overview -->
## Overview

Production troubleshooting is a key capability for ensuring business continuity. This document provides systematic troubleshooting methodologies, common problem resolution techniques, and automated diagnostic tools to help operations teams quickly identify and resolve production environment issues.

<!-- chunk: Production Troubleshooting System Architecture -->
## Production Troubleshooting System Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   Production Environment Troubleshooting System              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│  │  Problem        │  │  Information    │  │  Root Cause     │            │
│  │  Detection      │  │  Collection     │  │  Analysis       │            │
│  │                 │  │                 │  │                 │            │
│  │ • Monitoring    │  │ • Log           │  │ • Correlation   │            │
│  │   alerts        │  │   collection    │  │   analysis      │            │
│  │ • User          │  │ • Metrics       │  │ • Pattern       │            │
│  │   feedback      │  │   analysis      │  │   recognition   │            │
│  │ • Auto          │  │ • Tracing       │  │ • Hypothesis    │            │
│  │   detection     │  │                 │  │   verification  │            │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘            │
│          │                     │                     │                     │
│          ▼                     ▼                     ▼                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│  │  Solution       │  │  Verification   │  │  Post-incident  │            │
│  │  Implementation │  │  of Fix          │  │  Review         │            │
│  │                 │  │                 │  │                 │            │
│  │ • Temporary     │  │ • Effectiveness │  │ • Root cause    │            │
│  │   mitigation    │  │   confirmation  │  │   archiving     │            │
│  │ • Permanent     │  │ • Regression    │  │ • Prevention    │            │
│  │   resolution    │  │   testing       │  │   measures      │            │
│  │ • Prevention    │  │ • Enhanced      │  │ • Knowledge     │            │
│  │   mechanisms    │  │   monitoring    │  │   accumulation  │            │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- chunk: Systematic Troubleshooting Methodology -->
## Systematic Troubleshooting Methodology

### 1. Golden Signals Troubleshooting Method
```yaml
golden_signals_troubleshooting:
  latency_issues:
    diagnosis_steps:
      - check_service_mesh_metrics: "Check service mesh latency"
      - analyze_application_logs: "Analyze slow queries in application logs"
      - examine_network_latency: "Check network latency"
      - review_resource_limits: "Check CPU/memory limits"
      
  traffic_issues:
    diagnosis_steps:
      - verify_load_balancer_config: "Verify load balancer configuration"
      - check_service_discovery: "Check service discovery issues"
      - analyze_ingress_controller: "Analyze ingress controller status"
      - review_autoscaling_settings: "Check auto-scaling configuration"
      
  error_issues:
    diagnosis_steps:
      - examine_error_logs: "Check error logs"
      - analyze_return_codes: "Analyze return code distribution"
      - check_dependency_services: "Check dependent service status"
      - review_security_policies: "Check security policy impacts"
      
  saturation_issues:
    diagnosis_steps:
      - monitor_resource_utilization: "Monitor resource utilization"
      - check_pending_workloads: "Check pending workloads"
      - analyze_queue_depth: "Analyze queue depth"
      - review_capacity_planning: "Check capacity planning"
```

### 2. Layered Troubleshooting Method
``` bash
# 🟡 Medium risk: Modifies cluster/resource state, confirm target, scope and authorization before execution
#!/bin/bash
# Layered troubleshooting script

layered_troubleshooting() {
    local service_name=$1
    local namespace=${2:-default}
    
    echo "=== Layered Troubleshooting: $service_name ==="
    
    # Layer 1: Infrastructure layer diagnostics
    echo "1. Infrastructure Layer Diagnostics:"
    echo "   □ Node status check"
    kubectl get nodes | grep -v Ready
    echo "   □ Network connectivity check"
    kubectl run debug-pod --image=busybox --rm -it -- ping -c 3 8.8.8.8
    
    # Layer 2: Kubernetes component layer diagnostics
    echo "2. Kubernetes Component Layer Diagnostics:"
    echo "   □ API Server status"
    kubectl get componentstatuses
    echo "   □ Controller status"
    kubectl get pods -n kube-system | grep -E "(controller|scheduler)"
    
    # Layer 3: Application layer diagnostics
    echo "3. Application Layer Diagnostics:"
    echo "   □ Pod status check"
    kubectl get pods -n $namespace | grep $service_name
    echo "   □ Service status check"
    kubectl get svc -n $namespace | grep $service_name
    
    # Layer 4: Business logic layer diagnostics
    echo "4. Business Logic Layer Diagnostics:"
    echo "   □ Application log analysis"
    kubectl logs -n $namespace -l app=$service_name --tail=100
    echo "   □ Dependent service check"
    kubectl get endpoints -n $namespace
}

# Usage example
layered_troubleshooting "user-service" "production"
```
<!-- chunk: Common Problem Scenarios and Solutions -->
## Common Problem Scenarios and Solutions

### 1. Pod-Related Issues

#### Pod Pending Status
``` bash
# 🟢 Low risk: Read-only/information gathering, typically no side effects
#!/bin/bash
# Pod Pending troubleshooting script

diagnose_pending_pods() {
    local namespace=${1:-default}
    
    echo "=== Pod Pending Status Diagnosis ==="
    
    # Check pending pods
    pending_pods=$(kubectl get pods -n $namespace --field-selector=status.phase=Pending -o name)
    
    if [ -z "$pending_pods" ]; then
        echo "No pods in Pending status"
        return
    fi
    
    echo "Found Pending Pods:"
    echo "$pending_pods"
    echo ""
    
    # Analyze each pending pod
    for pod in $pending_pods; do
        echo "Analyzing Pod: $pod"
        
        # Check events
        echo "Related Events:"
        kubectl describe $pod -n $namespace | grep -A 10 "Events:"
        echo ""
        
        # Check resource requests
        echo "Resource Requests:"
        kubectl get $pod -n $namespace -o jsonpath='{.spec.containers[*].resources}'
        echo ""
        
        # Check node selector
        echo "Node Selector:"
        kubectl get $pod -n $namespace -o jsonpath='{.spec.nodeSelector}'
        echo ""
        
        echo "---"
    done
}

# Usage example
diagnose_pending_pods "production"
```
Through systematic troubleshooting methodologies and tools, you can significantly improve incident resolution efficiency, reduce service interruption time, and ensure stable operations of the production environment.

---

<!-- chunk: Obsidian Related Documentation -->
## Obsidian Related Documentation

- domain-07-platform-engineering MOC
- [[domain-07-platform-engineering/README.md|Platform Ops Domain]]
- Domain-9 Platform Operations — Open Source Project Index
- Platform Operations Overview
- Cluster Lifecycle Management
- Capacity Planning & Resource Assessment
- Performance Benchmarking & Tuning
- Operations Metrics System
- Monitoring and Alerting System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization & FinOps
- [[domain-10-troubleshooting-diagnostics/topic-fta/list/apiserver-fta.md|API Server Fault Tree Analysis]]
- [[domain-10-troubleshooting-diagnostics/topic-fta/list/backup-restore-fta.md|Backup/Restore Fault Tree Analysis]]
- [[domain-10-troubleshooting-diagnostics/topic-fta/list/calico-fta.md|Calico FTA: Calico CNI Troubleshooting]]

## Related

- 22-production-checklist
- [[kudig-prompts-catalog]]
- [[domain-02-workloads-applications/02-spring-boot-kubernetes-production.md|02-spring-boot-kubernetes-production]]

## See Also

- 13-multi-cluster-management
- 14-large-scale-cluster-optimization
- 16-platform-upgrade-migration
- 17-multi-tenant-management


<!-- risk-assessed -->