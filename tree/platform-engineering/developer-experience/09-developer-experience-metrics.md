---
title: kubectl Plugin Ecosystem Knowledge Manual
description: '## 1. Plugin Overview'
summary: 'kubectl has supported a plugin mechanism since v1.14. A plugin is essentially an executable file named `kubectl-<name>` placed anywhere in `PATH` (e.g., `/usr/local/bin/kubectl-foo`), and can be invoked via `kubectl foo`.'
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- coredns
- statefulset
- job
- cronjob
- rbac
- agent
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
- What is the kubectl plugin ecosystem knowledge manual
- How to use kubectl plugin ecosystem knowledge manual
- Kubernetes 9 platform ops best practices
trigger_keywords:
- kubectl
- plugin ecosystem knowledge manual
- platform
- ops
prerequisites:
- kubectl-basics
- platform-engineering-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: KUDIG Team
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
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./developer-experience/26-kubectl-plugin-ecosystem.md
original_language: Chinese
---

> **Production Environment Security Tip**
>
> This document contains operational commands that can be directly executed. Before executing, please verify:
> - Are the current target cluster and namespace correct?
> - Do you have sufficient RBAC permissions?
> - Have you tested in a non-production environment?
> Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state but usually reversible), 🟢 Low risk/read-only (information gathering, no side effects).




# kubectl Plugin Ecosystem Knowledge Manual

> **Document Type**: Tool Reference Manual | **Applicable Versions**: K8s 1.28-1.33 | **Last Updated**: 2026-05
> **Use Case**: Agent understanding of commonly used kubectl plugin capabilities to correctly handle issues where "a kubectl plugin command failed" in work orders

---

<!-- chunk: 1. Plugin Overview -->
## 1. Plugin Overview

kubectl has supported a plugin mechanism since v1.14. A plugin is essentially an executable file named `kubectl-<name>` placed anywhere in `PATH` (e.g., `/usr/local/bin/kubectl-foo`), and can be invoked via `kubectl foo`.

### 1.1 Plugin Management Tools

| Tool | Description | Installation Method |
|------|------|---------|
| **krew** | The official kubectl plugin manager recommended by Kubernetes | `kubectl krew install/upgrade/remove` |
| Manual Installation | Directly download binary and chmod +x | wget/curl |

### 1.2 Basic krew Usage

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
# Install krew (execute only once)
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/aarch64/arm64/')" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/krew-${OS}_${ARCH}.tar.gz" &&
  tar zxf krew-${OS}_${ARCH}.tar.gz &&
  ./krew-"${OS}_${ARCH}" install krew
)

# Common krew commands
kubectl krew update                    # Update plugin index
kubectl krew install <plugin>          # Install plugin
kubectl krew upgrade <plugin>         # Upgrade plugin
kubectl krew uninstall <plugin>       # Uninstall plugin
kubectl krew list                      # List installed plugins
kubectl krew search <keyword>          # Search for plugins
```
---

<!-- chunk: 2. High-Frequency Production Plugin Details -->
## 2. High-Frequency Production Plugin Details

### 2.1 kubectl-whoami (Authentication)

**Purpose**: View authentication information (User/Group/SA) of the current kubectl context

**Installation**: `kubectl krew install whoami`

**Use Cases**:
- "Verify identity when kubectl operation reports Forbidden"
- "Verify current user when debugging RBAC"
- "Confirm that the correct ServiceAccount token is being used"

**Sample Output**:
```
SYSTEM:masters   (system:master-group)
  └─ discovery: /api/v1  /apis/rbac.authorization.k8s.io/v1
```

**Typical Troubleshooting**:
``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
# Issue: kubectl execution reports not authorized
kubectl whoami
# Check if current identity is correct

# Issue: Incorrect kubeconfig context was used
kubectl whoami --context prod-cluster
```
### 2.2 kubectl-neat (Output Cleanup)

**Purpose**: Clean up redundant fields in kubectl output (managedFields, creationTimestamp, etc.)

**Installation**: `kubectl krew install neat`

**Use Cases**:
- "Clean up noise when redirecting kubectl get output to a YAML file"
- "Generate clean YAML configuration for Git"

**Sample Output**:
``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
# Raw output (kubectl get pod -o yaml)
# Contains large amounts of metadata.managedFields, metadata.resourceVersion, etc.

# After using neat
# Only retains critical fields: apiVersion, kind, metadata, spec, status
```
**Typical Usage**:
``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
kubectl get pod nginx -o yaml | kubectl neat
kubectl get deployment -o yaml | kubectl neat > clean-deployment.yaml
```
### 2.3 kubectl-tree (Resource Hierarchy View)

**Purpose**: Display hierarchy relationships between resources (e.g., which Pods are contained in a ReplicaSet, which Endpoints are referenced by a Service)

**Installation**: `kubectl krew install tree`

**Use Cases**:
- "Quickly understand how many Pods are under a Deployment (and their status)"
- "Trace which ReplicaSet/Deployment a Pod belongs to"
- "When troubleshooting ServiceSelector mismatch, view which Pods are actually covered by the selector"

**Sample Output**:
```
deployment/nginx
└── replicaset/nginx-7d9f6b8c5
    └── pod/nginx-7d9f6b8c5-xk2p4
    └── pod/nginx-7d9f6b8c5-xk2q1
    └── pod/nginx-7d9f6b8c5-xk2r2
```

**Typical Troubleshooting**:
``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
# Issue: A Pod is not part of a Service, find the ReplicaSet the Pod belongs to
kubectl tree deployment/my-app
# Find the anomalous Pod in the output

# Issue: ReplicaSet count does not match expectations
kubectl tree replicaset -n <namespace>
```
### 2.4 kubectl-debug (Safe Debugging, GA in K8s 1.28+)

**Purpose**: Replaces the deprecated `kubectl exec` / debug approach, safely adding debug tools or sidecars to Pod/container

**Installation**: `kubectl krew install debug`

**Use Cases**:
- "Start a debug container alongside a running Pod"
- "Execute diagnostic commands within a container without affecting the main container"
- "Use nsenter to enter the Pod's network namespace"
- "Copy a Pod to a new container and add debug tools"

**Main Commands**:
``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
# Start a debug container alongside the main container of a Pod (ephemeral debug container)
kubectl debug <pod> -it --image=busybox --share-processes --copy-to=debug-pod

# Start a debug container on a node (node-level debugging)
kubectl debug node/<node-name> -it --image=busybox

# Copy a Pod and add a debug container
kubectl debug <pod> --image=busybox --copy-to=debug-pod --share-processes

# Inject sidecar into an existing Pod
kubectl debug <pod> --inject=debug-tools --image=debug:latest

# View created debug Pods
kubectl get pods | grep debug

# Clean up debug Pods
kubectl debug --clean
```
**Built-in for K8s 1.28+ (no krew needed)**:
``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
# K8s 1.28+ has kubectl debug built-in (no plugin needed)
# Ephemeral Container
kubectl debug <pod> -it --image=busybox --target=<container-name>
# --target specifies the target container to attach to
```
**Typical Troubleshooting**:
``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
# Issue: Unable to exec into container (container runtime issue)
kubectl debug <pod> -it --image=busybox --share-processes
# Start a temporary debug container

# Issue: Pod cannot be scheduled (node issue)
kubectl debug node/<node-name> -it --image=busybox
# Start a debug container at node level for troubleshooting
```
### 2.5 kubectl-exec-all (Batch exec)

**Purpose**: Execute commands simultaneously on all Pods in the same Deployment/ReplicaSet/StatefulSet

**Installation**: `kubectl krew install exec-all`

**Use Cases**:
- "View logs from all Pods (tail)"
- "Execute the same diagnostic command on all Pods (e.g., view process list)"
- "Batch restart all Pods (send SIG HUP)"

**Sample Output**:

> ⚠️ **🟡 Medium risk change** — Modifies cluster resource state, recommend using --dry-run or diff to verify first
> - `kubectl exec`: Execute commands in container, may change container state

``` bash
# 🟡 Medium risk: modifies cluster/resource state, verify target, scope of impact, and authorization before executing
# Execute ls /app on all nginx Pods
kubectl exec-all -l app=nginx -- ls /app

# Output:
# [nginx-7d9f6b8c5-xk2p4] ls /app
# application
# [nginx-7d9f6b8c5-xk2q1] ls /app
# application
# [nginx-7d9f6b8c5-xk2r2] ls /app
# application
```
**Typical Troubleshooting**:

> ⚠️ **🟡 Medium risk change** — Modifies cluster resource state, recommend using --dry-run or diff to verify first
> - `kubectl exec`: Execute commands in container, may change container state

``` bash
# 🟡 Medium risk: modifies cluster/resource state, verify target, scope of impact, and authorization before executing
# Issue: Need to view logs from multiple Pods simultaneously
kubectl exec-all -l app=nginx -- tail -f /var/log/nginx/access.log

# Issue: Configuration inconsistent across all Pods, need to check each one
kubectl exec-all -l app=nginx -- cat /etc/nginx/nginx.conf
```
### 2.6 kubectl-cost (Cost Estimation)

**Purpose**: Estimate Kubernetes resource costs by namespace/Deployment/StatefulSet

**Installation**: `kubectl krew install cost`

**Use Cases**:
- "Find out which Deployments consume the most resources (are most expensive)"
- "Monthly Kubernetes cost analysis"
- "Determine priority when optimizing resource allocation"

**Sample Output**:
```
NAMESPACE    WORKLOAD              CPU REQUESTED   MEM REQUESTED   MONTHLY COST
default      nginx-deployment      500m            128Mi           $12.34
kube-system  coredns               200m            100Mi           $8.90
```

**Typical Troubleshooting**:
``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
# Issue: High cost with low resource utilization
kubectl cost --show-cost-details
# Find Deployments wasting resources

# Issue: Want to see how much was saved after optimization
kubectl cost --historical
```
### 2.7 kubectl-ns (Namespace Quick Switch)

**Purpose**: Quickly switch/view current namespace without needing to enter `-n <namespace>` each time

**Installation**: `kubectl krew install ns`

**Use Cases**:
- "Reduce typing when frequently operating on a namespace"
- "View the current namespace"

**Sample Output**:
```
Current namespace: default
```

**Typical Usage**:
``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
kubectl ns my-namespace  # Switch to my-namespace
kubectl ns               # View current namespace
kubectl ns -             # Return to previous namespace
```
### 2.8 kubectl-ctx (Context Switch)

**Purpose**: Quickly switch kubectl context (cluster)

**Installation**: `kubectl krew install ctx`

**Use Cases**:
- "Quick switching in multi-cluster environments"
- "Verify the current cluster being operated on (avoid misoperating on production)"

**Sample Output**:
```
CURRENT   NAME             CLUSTER          NAMESPACE
*         dev-cluster      dev.example.com  default
          prod-cluster     prod.example.com  default
          staging-cluster  staging.example.com  default
```

**Typical Usage**:
``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
kubectl ctx prod-cluster  # Switch to production cluster
kubectl ctx               # View all contexts
```
---

<!-- chunk: 3. Other Common Plugins -->
## 3. Other Common Plugins

### 3.1 kubectl-sniff (Network Packet Capture)

**Purpose**: Start tcpdump packet capture within a Pod (requires privileges)

**Installation**: `kubectl krew install sniff`

**Use Cases**:
- "Troubleshoot Service access issues via packet capture analysis"
- "Debug network issues between microservices"

**Typical Usage**:
``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
kubectl sniff <pod-name> -n <namespace>
# Generate wireshark-compatible pcap file
```
### 3.2 kubectl-view-secret (View Secret Contents)

**Purpose**: Decode and view Secret contents (replaces base64 -d)

**Installation**: `kubectl krew install view-secret`

**Use Cases**:
- "Quickly view Secret values"
- "Debug Secret mount issues"

**Typical Usage**:
``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
kubectl view-secret <secret-name> <key-name> -n <namespace>
kubectl view-secret <secret-name> -n <namespace>  # List all keys
```
### 3.3 kubectl-purge (Clean Up Terminated Resources)

**Purpose**: Batch delete terminated Pods, Jobs, CronJobs

**Installation**: `kubectl krew install purge`

**Use Cases**:
- "Clean up completed but undeleted Jobs"
- "Clean up Evicted Pods"

**Typical Usage**:
``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
kubectl purge jobs,deployments -n <namespace> --older-than=24h
# Delete resources completed 24 hours ago
```
### 3.4 kubectl-image-pull-secret (Manage Image Pull Credentials)

**Purpose**: Quickly create imagePullSecrets or view existing credentials

**Installation**: `kubectl krew install image-pull-secret`

**Use Cases**:
- "Configure private image registry credentials"
- "View configured imagePullSecrets"

---

<!-- chunk: 4. Plugin Installation Failure Troubleshooting -->
## 4. Plugin Installation Failure Troubleshooting

### 4.1 Common Errors

| Error | Reason | Solution |
|------|------|---------|
| `plugin not recognized` | File name is not `kubectl-<name>` or not in PATH | Check file path |
| `exec format error` | Binary is not Linux/amd64 architecture | Verify correct architecture version was downloaded |
| `permission denied` | File does not have execute permission | `chmod +x kubectl-<name>` |
| `krew install failed` | Network issue or download timeout | Manually download and place directly in PATH |

### 4.2 krew Self Issues

> ⚠️ **🔴 Catastrophic Operation** — Contains irreversible commands, must meet change window + dual approval + pre-backup + rollback plan before executing
> - `rm -rf (system/data path)`: Delete system or data files, may destroy node or lose all data

> **🔴 High Risk Operation Warning**
>
> The commands below are irreversible or high-impact operations. Before executing, please confirm:
> - Critical data and configuration have been backed up
> - Within an approved change window
> - Authorization obtained from relevant stakeholders
> - Rollback or recovery plan has been prepared
> - Target cluster, namespace, node/resource names are correct

``` bash
# 🔴 High risk: may cause data loss or service interruption, requires backup, change approval, and rollback plan before executing
# Reset krew (if krew command itself is erroring)
kubectl krew version
# If version shows normally but plugin installation fails:

# Clean and reinstall krew
rm -rf ~/.krew  # ⚠️ Delete system/data files
# Re-execute krew installation script
```
### 4.3 Verify Plugin Availability

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
# List all installed plugins
kubectl plugin list

# Or run directly (will display error)
kubectl-whoami
```
---

<!-- chunk: 5. Plugins and RBAC -->
## 5. Plugins and RBAC

### 5.1 kubectl whoami Permission Requirements

`kubectl-whoami` requires access to the `selfsubjectaccessreviews` API and does not require special RBAC permissions.

### 5.2 RBAC Requirements for Other Plugins

| Plugin | Minimum Required Permission | Description |
|------|------------|------|
| whoami | `create` on `selfsubjectaccessreviews` | Usually available to all users |
| neat | read permission (same as kubectl get) | - |
| tree | read permission (watch certain resources) | - |
| debug | `create` on `pods/ephemeral-containers` | Stable in K8s 1.28+ |
| cost | read permission (metrics) | Requires metrics-server |
| ns | no special permission | - |
| ctx | no special permission | - |

---

<!-- chunk: 6. Plugin Quick Reference -->
## 6. Plugin Quick Reference

| Plugin | Installation Command | Main Purpose | Problem Scenario |
|------|---------|---------|---------|
| `kubectl-whoami` | `kubectl krew install whoami` | View current identity | RBAC debugging |
| `kubectl-neat` | `kubectl krew install neat` | Clean YAML noise | Export configuration |
| `kubectl-tree` | `kubectl krew install tree` | Resource hierarchy view | Troubleshoot Pod/Deployment relationships |
| `kubectl-debug` | `kubectl krew install debug` | Safe debugging | When unable to exec |
| `kubectl-exec-all` | `kubectl krew install exec-all` | Batch exec | Batch log collection |
| `kubectl-cost` | `kubectl krew install cost` | Cost estimation | Cost analysis |
| `kubectl-ns` | `kubectl krew install ns` | Namespace switch | Frequent NS switching |
| `kubectl-ctx` | `kubectl krew install ctx` | Cluster switch | Multi-cluster switching |
| `kubectl-sniff` | `kubectl krew install sniff` | Network packet capture | Network debugging |
| `kubectl-purge` | `kubectl krew install purge` | Clean terminated resources | Batch cleanup |

---

<!-- chunk: Appendix: Manual Installation (non-krew) Example -->
## Appendix: Manual Installation (non-krew) Example

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
# Download binary
wget https://github.com/hjacobs/kubectl-whoami/releases/download/v1.0.0/kubectl-whoami-linux-amd64
mv kubectl-whoami-linux-amd64 /usr/local/bin/kubectl-whoami
chmod +x /usr/local/bin/kubectl-whoami

# Verify
kubectl whoami

# Uninstall
rm /usr/local/bin/kubectl-whoami
```
---

```yaml
---
id: KUBECTL-PLUGIN-001
domain: platform-ops
type: tool-reference
tags: [kubectl, plugins, tool-ecosystem, k8s-1.28-1.33, agent-corpus]
intent_queries:
  - "What kubectl plugins are available"
  - "What is kubectl whoami used for"
  - "How to use kubectl debug"
  - "What does kubectl tree do"
  - "How to install plugins with krew"
difficulty: intermediate
target_roles: [sre, ops-engineer]
k8s_versions: ["1.28", "1.29", "1.30", "1.31", "1.32", "1.33"]
related:
  - domain-07-platform-engineering/23-cli-enhancement-tools.md
  - domain-01-cluster-fundamentals/31-kubectl-complete-reference.md
---
```

---

<!-- chunk: Obsidian Related Documentation -->
## Obsidian Related Documentation

- domain-07-platform-engineering MOC
- [[domain-07-platform-engineering/README.md|Platform Ops Domain (Platform Operations Domain)]]
- Domain-9 Platform Operations — Open Source Project Index
- Platform Operations Overview
- Cluster Lifecycle Management
- Capacity Planning & Resource Assessment
- Performance Benchmarking & Tuning
- Operations Metrics System
- Monitoring and Alerting System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization & FinOps Practices

## See Also

- 24-addons-extensions
- 25-virtual-clusters
- 99-java-k8s-client-operator-guide
- 99-kubernetes-v1.33-platform-ops-guide

```

<!-- risk-assessed -->