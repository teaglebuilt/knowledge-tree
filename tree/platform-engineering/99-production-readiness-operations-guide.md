---
title: 32 - API Aggregation Layer Configuration
description: '# 32 - API Aggregation Layer Configuration'
summary: 'opts := options.NewSecureServingOptions()'
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- apiserver
- prometheus
- rbac
- crd
- operator
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Platform Engineer
- Operations Engineer
estimated_read_time: 5min
intent_queries:
- What is API Aggregation Layer Configuration
- How to configure API Aggregation Layer
- Kubernetes 9 platform ops best practices
trigger_keywords:
- API aggregation layer configuration
- platform
- ops
prerequisites:
- kubectl-basics
- platform-engineering-basics
- prometheus-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: Dillan Teagle
  role: contributor
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
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./build/21-api-aggregation.md
original_language: Chinese
---

> **Production Environment Security Notice**
>
> This document contains operational commands that can be executed directly. Before execution, please confirm: that the target cluster and namespace are correct; that you have sufficient RBAC permissions; that the changes have been validated in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state but usually can be rolled back), 🟢 Low risk/read-only (information gathering, no side effects).




# 32 - API Aggregation Layer Configuration

<!-- chunk: API aggregation architecture -->
## API Aggregation Architecture

| Component | Function | Description |
|-----------|----------|-------------|
| kube-aggregator | API routing | Built into kube-apiserver |
| APIService | Service registration | Declares API group/version |
| Extension API Server | Extension server | Custom API implementation |

<!-- chunk: APIService configuration -->
## APIService Configuration

| Field | Type | Description |
|-------|------|-------------|
| `spec.group` | string | API group name |
| `spec.version` | string | API version |
| `spec.[[Service|service]].name` | string | Backend service name |
| `spec.service.namespace` | string | Backend service namespace |
| `spec.service.port` | int | Backend service port (default 443) |
| `spec.caBundle` | []byte | CA certificate |
| `spec.groupPriorityMinimum` | int | Group priority minimum value |
| `spec.versionPriority` | int | Version priority |
| `spec.insecureSkipTLSVerify` | bool | Skip TLS verification (not recommended) |

<!-- chunk: APIService example -->
## APIService Example

```yaml
apiVersion: apiregistration.k8s.io/v1
kind: APIService
metadata:
  name: v1beta1.metrics.k8s.io
spec:
  service:
    name: metrics-server
    namespace: kube-system
    port: 443
  group: metrics.k8s.io
  version: v1beta1
  groupPriorityMinimum: 100
  versionPriority: 100
  caBundle: <base64-encoded-ca>
---
# Local APIService (built-in API)
apiVersion: apiregistration.k8s.io/v1
kind: APIService
metadata:
  name: v1.
spec:
  group: ""
  version: v1
  groupPriorityMinimum: 18000
  versionPriority: 1
  # No service field means handled locally by kube-apiserver
```

<!-- chunk: Built-in aggregation API -->
## Built-in Aggregation API

| APIService | Service | Function |
|-----------|---------|----------|
| `v1beta1.metrics.k8s.io` | metrics-server | Resource metrics |
| `v1.custom.metrics.k8s.io` | prometheus-adapter | Custom metrics |
| `v1beta1.external.metrics.k8s.io` | - | External metrics |

<!-- chunk: Extension API Server development -->
## Extension API Server Development

| Step | Description |
|------|-------------|
| 1. Implement API handling | REST handler |
| 2. Configure TLS | Server certificate |
| 3. Deploy service | Deployment+Service |
| 4. Create APIService | Register with aggregation layer |
| 5. Configure RBAC | Authorize access |

<!-- chunk: Extension Server example structure -->
## Extension Server Example Structure

```go
// Use apiserver-builder or custom implementation
package main

import (
    "k8s.io/apiserver/pkg/server"
    "k8s.io/apiserver/pkg/server/options"
)

func main() {
    // Configure TLS
    opts := options.NewSecureServingOptions()
    
    // Register API handler
    apiGroupInfo := server.NewDefaultAPIGroupInfo(...)
    
    // Start server
    server.PrepareRun().Run(stopCh)
}
```

<!-- chunk: Authentication proxy configuration -->
## Authentication Proxy Configuration

| Parameter | Description |
|-----------|-------------|
| `--requestheader-client-ca-file` | Proxy client CA |
| `--requestheader-allowed-names` | Allowed CN |
| `--requestheader-extra-headers-prefix` | Extra header prefix |
| `--requestheader-group-headers` | Group header name |
| `--requestheader-username-headers` | Username header name |
| `--proxy-client-cert-file` | Proxy client certificate |
| `--proxy-client-key-file` | Proxy client key |

<!-- chunk: Aggregation layer troubleshooting -->
## Aggregation Layer Troubleshooting

| Problem | Diagnostic Command | Solution |
|---------|-------------------|----------|
| APIService unavailable | `kubectl get apiservices` | Check backend service |
| Certificate issues | `kubectl describe apiservice` | Update caBundle |
| Network unreachable | `kubectl logs kube-apiserver` | Check service connectivity |
| Insufficient permissions | `kubectl auth can-i` | Configure RBAC |

<!-- chunk: Status check commands -->
## Status Check Commands

``` bash
# 🟢 Low risk: read-only/information gathering, usually no side effects
# View all APIServices
kubectl get apiservices

# View aggregated API status
kubectl get apiservices v1beta1.metrics.k8s.io -o yaml

# Check availability
kubectl api-resources --api-group=metrics.k8s.io

# Test API
kubectl get --raw /apis/metrics.k8s.io/v1beta1/nodes
```
<!-- chunk: Version changelog -->
## Version Changelog

| Version | Changes |
|---------|---------|
| v1.25 | APIService status condition improvements |
| v1.27 | Aggregation discovery API improvements |
| v1.28 | API priority and fairness enhancements |
| v1.29 | Aggregation layer performance optimization |

---

**Table footer attribution**: Kusheet Project, author Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian related documentation -->
## Obsidian Related Documentation

- domain-07-platform-engineering KUDIG Database — Global MOC
- [[domain-07-platform-engineering/README.md|[[Platform Ops Domain|Platform Ops Domain]]]]
- index.md|Domain-9 Platform Operations — Open Source Project Index]]
- Platform Operations Overview
- Cluster Lifecycle Management
- Capacity Planning & Resource Assessment
- Performance Benchmarking & Tuning
- Operations Metrics System
- Monitoring and Alerting System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization & FinOps
- Cost Optimization & FinOps Practices

## See Also

- 19-lease-leader-election
- 20-crd-operator-development
- 22-client-libraries
- 23-cli-enhancement-tools


<!-- risk-assessed -->