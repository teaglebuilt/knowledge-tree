---
title: 110 - CLI Enhancement and Efficiency Tools
description: '| **Stern** | Multi-Pod Log Aggregation | 85% | brew/apt |'
summary: '| **Stern** | Multi-Pod Log Aggregation | 85% | brew/apt |'
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- mysql
- statefulset
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Platform Engineers
- Operations Engineers
estimated_read_time: 5min
intent_queries:
- What is CLI Enhancement and Efficiency Tools
- How to use CLI Enhancement and Efficiency Tools
- Kubernetes 9 platform ops best practices
trigger_keywords:
- CLI
- Enhancement and Efficiency Tools
- CLI
- Enhancement
- platform
- ops
prerequisites:
- kubectl-basics
- platform-engineering-basics
- mysql-basics
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
  label: 'Related Knowledge Domain: domain-06-observability'
- type: domain
  path: ../domain-15-specialized-tech/
  label: 'Related Knowledge Domain: domain-15-specialized-tech'
- type: domain
  path: ../domain-10-troubleshooting-diagnostics/
  label: 'Related Knowledge Domain: domain-10-troubleshooting-diagnostics'
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./developer-experience/23-cli-enhancement-tools.md
original_language: Chinese
---

> **Production Environment Security Notice**
>
> This document contains operations commands that can be executed directly. Before executing, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have verified in a non-production environment. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state, but typically reversible), 🟢 Low Risk/Read-only (information gathering, no side effects).




# 110 - CLI Enhancement and Efficiency Tools

> **Applicable Versions**: v1.25 - v1.32 | **Last Updated**: 2026-01

<!-- chunk: CLI Efficiency Enhancement Tools -->
## CLI Efficiency Enhancement Tools

| Tool | Core Function | Efficiency Gain | Installation Method |
|------------|-------------------|---------|---------|
| **kubectx / kubens** | Quick context/namespace switching | 90% | brew/apt |
| **kube-capacity** | Resource capacity viewing | 80% | kubectl krew |
| **Stern** | Multi-Pod log aggregation | 85% | brew/apt |
| **kubectl-tree** | Resource dependency tree | 70% | kubectl krew |
| **kubectl-neat** | Clean YAML output | 75% | kubectl krew |

<!-- chunk: kubectx / kubens Quick Switching -->
## kubectx / kubens Quick Switching

### Basic Usage
```bash
# List all contexts
kubectx

# Switch context
kubectx production

# Switch back to previous context
kubectx -

# List all namespaces
kubens

# Switch namespace
kubens kube-system
```

### Alias Configuration
```bash
# ~/.bashrc or ~/.zshrc
alias kx='kubectx'
alias kn='kubens'
```

<!-- chunk: kube-capacity Resource Capacity -->
## kube-capacity Resource Capacity

### View Cluster Capacity
```bash
# View all nodes
kube-capacity

# Sort by CPU usage
kube-capacity --sort cpu.util

# View Pod-level information
kube-capacity --pods

# Output as JSON
kube-capacity -o json
```

### Output Example
```
NODE              CPU REQUESTS   CPU LIMITS    MEMORY REQUESTS   MEMORY LIMITS
node-1            1950m (48%)    3900m (97%)   7Gi (43%)         14Gi (87%)
node-2            1200m (30%)    2400m (60%)   5Gi (31%)         10Gi (62%)
```

<!-- chunk: kubectl-tree Resource Dependencies -->
## kubectl-tree Resource Dependencies

### View Resource Tree
``` bash
# 🟢 Low Risk: Read-only/information gathering, typically no side effects
# View Deployment dependencies
kubectl tree deployment myapp

# View StatefulSet dependencies
kubectl tree statefulset mysql

# Output Example
NAMESPACE  NAME                           READY  REASON  AGE
default    Deployment/myapp               -              5d
default    ├─ReplicaSet/myapp-7d8f9c      -              5d
default    │ ├─Pod/myapp-7d8f9c-abc       True           5d
default    │ └─Pod/myapp-7d8f9c-def       True           5d
```
<!-- chunk: kubectl-neat Clean Output -->
## kubectl-neat Clean Output

### Clean YAML
``` bash
# 🟢 Low Risk: Read-only/information gathering, typically no side effects
# Clean redundant fields such as managedFields
kubectl get pod myapp -o yaml | kubectl neat

# Clean and save
kubectl get deployment myapp -o yaml | kubectl neat > myapp-clean.yaml
```
<!-- chunk: kubectl Aliases and Functions -->
## kubectl Aliases and Functions

### Common Aliases

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend --dry-run or diff before confirming
> - `kubectl apply/create/replace`: Create/modify cluster resources
> - `kubectl delete`: Delete resources (can be recreated by declarative manifests)
> - `kubectl exec`: Enter container and execute commands, may change container state

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, confirm target, scope of impact and authorization before executing
# ~/.bashrc or ~/.zshrc
alias k='kubectl'
alias kg='kubectl get'
alias kd='kubectl describe'
alias kdel='kubectl delete'
alias kl='kubectl logs'
alias kex='kubectl exec -it'
alias kaf='kubectl apply -f'

# Quick view Pods
alias kgp='kubectl get pods'
alias kgpa='kubectl get pods --all-namespaces'

# Quick view Services
alias kgs='kubectl get svc'

# Quick view Nodes
alias kgn='kubectl get nodes'
```
### Useful Functions

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend --dry-run or diff before confirming
> - `kubectl delete`: Delete resources (can be recreated by declarative manifests)
> - `kubectl exec`: Enter container and execute commands, may change container state

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, confirm target, scope of impact and authorization before executing
# Quickly enter Pod Shell
ksh() {
  kubectl exec -it $1 -- /bin/bash
}

# Quickly view Pod logs
klog() {
  kubectl logs -f $1
}

# Quickly delete Evicted Pods
kdele() {
  kubectl get pods --all-namespaces | grep Evicted | awk '{print $2, "-n", $1}' | xargs kubectl delete pod
}
```
<!-- chunk: kubectl Plugin Management (Krew) -->
## kubectl Plugin Management (Krew)

### Install Krew
```bash
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)
```

### Recommended Plugins
``` bash
# 🟢 Low Risk: Read-only/information gathering, typically no side effects
kubectl krew install ctx        # kubectx
kubectl krew install ns         # kubens
kubectl krew install tree       # Resource tree
kubectl krew install neat       # YAML cleanup
kubectl krew install capacity   # Capacity viewing
kubectl krew install debug      # Debug tools
kubectl krew install tail       # Log tracing
```
<!-- chunk: Efficiency Enhancement Tips -->
## Efficiency Enhancement Tips

| Tip | Description |
|-----------|-------------------|
| **Auto-completion** | `source <(kubectl completion bash)` |
| **Alias Shortcuts** | Reduce input by 80% |
| **Plugin Ecosystem** | Krew plugin marketplace |
| **Context Management** | Quick switching with kubectx |
| **Resource Templates** | Save commonly used YAML templates |


---

**Table Footer Attribution**: Kusheet Project, Author Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian Related Documentation -->
## Obsidian Related Documentation

- domain-07-platform-engineering KUDIG Database — Global MOC
- [[domain-07-platform-engineering/README.md|[[Platform Ops Domain|Platform Ops Domain]]]]
- index.md|Domain-9 Platform Operations — Open Source Project Index]]
- Platform Operations Overview
- Cluster Lifecycle Management
- [[domain-07-platform-engineering/governance/03-capacity-planning-resource-assessment.md|03 capacity planning resource assessment]]
- Performance Benchmarking & Tuning
- Operations Metrics System
- Monitoring and Alerting System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization & FinOps Practices

## See Also

- 21-api-aggregation
- 22-client-libraries
- 24-addons-extensions
- 25-virtual-clusters


<!-- risk-assessed -->