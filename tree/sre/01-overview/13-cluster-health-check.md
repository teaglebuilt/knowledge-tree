---
title: 13 - Cluster Health Check Guide
description: Comprehensive guide for checking and monitoring Kubernetes cluster health across control plane, nodes, pods, network, and storage layers
summary: Automated cluster health monitoring with diagnostic scripts and Prometheus metrics
category: observability
tags:
- k8s
- observability
- monitoring
- logging
- tracing
- etcd
- apiserver
- kubelet
- scheduler
- controller-manager
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Operations Engineer
- Monitoring Engineer
estimated_read_time: 5min
intent_queries:
- What is the Cluster Health Check Guide
- How to use the Cluster Health Check Guide
- Kubernetes observability best practices
trigger_keywords:
- Cluster Health Check
- Cluster
- Health
- Check
- Guide
- observability
prerequisites:
- kubectl-basics
- observability-basics
- prometheus-basics
- cilium-basics
- cni-basics
- etcd-basics
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
  path: ../domain-01-cluster-fundamentals/
  label: 'Related knowledge domain: domain-01-cluster-fundamentals'
- type: domain
  path: ../domain-02-workloads-applications/
  label: 'Related knowledge domain: domain-02-workloads-applications'
- type: domain
  path: ../domain-03-networking-traffic/
  label: 'Related knowledge domain: domain-03-networking-traffic'
- type: domain
  path: ../domain-07-platform-engineering/
  label: 'Related knowledge domain: domain-07-platform-engineering'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/promql.md
  label: 'Quick reference: promql'
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/01-overview/13-cluster-health-check.md
---

> **Production Environment Safety Notice**
>
> This document contains directly executable operations commands. Before execution, confirm: the current target cluster and namespace are correct; you have sufficient RBAC permissions; commands have been verified in non-production environments. Command risk levels: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state but usually reversible), 🟢 Low risk/read-only (information gathering, no side effects).




# 13 - Cluster Health Check Guide

> **Applicable versions**: v1.25 - v1.32 | **Last updated**: 2026-01 | **Reference**: [kubernetes.io/docs/tasks/debug/debug-cluster/](https://kubernetes.io/docs/tasks/debug/debug-cluster/)

<!-- chunk: Cluster Health Check Architecture -->
## Cluster Health Check Architecture

```
# 🟢 Low risk: read-only/information gathering, typically no side effects
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Kubernetes Cluster Health Check System                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                     Layer 1: Control Plane Health                    │  │
│   │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │  │
│   │  │ API Server  │ │    etcd     │ │ Scheduler   │ │ Controller  │   │  │
│   │  │  /healthz   │ │ /health     │ │ /healthz    │ │  Manager    │   │  │
│   │  │  /readyz    │ │ /readiness  │ │             │ │  /healthz   │   │  │
│   │  │  /livez     │ │             │ │             │ │             │   │  │
│   │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                        │                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                     Layer 2: Node Health                             │  │
│   │  ┌────────────────────────────────────────────────────────────┐    │  │
│   │  │                     Worker Node                             │    │  │
│   │  │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐           │    │  │
│   │  │  │   kubelet   │ │ containerd  │ │ kube-proxy  │           │    │  │
│   │  │  │  /healthz   │ │  systemctl  │ │  /healthz   │           │    │  │
│   │  │  └─────────────┘ └─────────────┘ └─────────────┘           │    │  │
│   │  │  ┌────────────────────────────────────────────────────┐    │    │  │
│   │  │  │ Node Conditions:                                    │    │    │  │
│   │  │  │ Ready | MemoryPressure | DiskPressure | PIDPressure│    │    │  │
│   │  │  └────────────────────────────────────────────────────┘    │    │  │
│   │  └────────────────────────────────────────────────────────────┘    │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                        │                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                     Layer 3: Network Health                          │  │
│   │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │  │
│   │  │   CoreDNS   │ │    CNI      │ │  Ingress    │ │ NetworkPolicy│  │  │
│   │  │  DNS lookup │ │ Pod network │ │ Entry traffic   │ Network policy  │  │
│   │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                        │                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                     Layer 4: Storage Health                          │  │
│   │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │  │
│   │  │ PV/PVC state│ │ StorageClass│ │ CSI Driver  │ │ Backend    │   │  │
│   │  │ Bound/      │ │ Provisioner │ │ health check│ │ Storage    │   │  │
│   │  │ Available   │ │ availability│ │             │ │ connectivity   │   │  │
│   │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                        │                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                     Layer 5: Workload Health                        │  │
│   │  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐   │  │
│   │  │  Pod state  │ │ Deployment  │ │ StatefulSet │ │  DaemonSet  │   │  │
│   │  │ Running/    │ │ replicas    │ │ ordered     │ │ node        │   │  │
│   │  │ Pending     │ │ ready state │ │ updates     │ │ coverage    │   │  │
│   │  └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```
<!-- chunk: Control Plane Health Check -->
## Control Plane Health Check

### API Server Health Check Matrix

| Endpoint | Purpose | Check Content | Expected Response | Version Changes |
|-----|------|---------|---------|---------|
| `/healthz` | Liveness check | Whether API Server is alive | `ok` | Stable |
| `/livez` | Liveness probe | Whether process is alive | `ok` | v1.16+ |
| `/readyz` | Readiness probe | Whether ready to handle requests | `ok` | v1.16+ |
| `/readyz?verbose` | Detailed readiness | Status of all subsystems | Each check status | v1.28 enhanced |
| `/healthz/etcd` | etcd connection | etcd backend health | `ok` | Stable |
| `/healthz/poststarthook/*` | Startup hooks | Each startup hook status | `ok` | Stable |

### Control Plane Check Commands

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
#!/bin/bash
# control-plane-health-check.sh

echo "====== Control Plane Health Check ======"
echo "Time: $(date)"
echo ""

# 1. API Server Health Check
echo "=== 1. API Server Health Status ==="
echo "Basic health: $(kubectl get --raw='/healthz' 2>/dev/null || echo 'FAILED')"
echo "Liveness check: $(kubectl get --raw='/livez' 2>/dev/null || echo 'FAILED')"
echo "Readiness check: $(kubectl get --raw='/readyz' 2>/dev/null || echo 'FAILED')"

# Detailed readiness check
echo -e "\n--- /readyz detailed status ---"
kubectl get --raw='/readyz?verbose' 2>/dev/null | grep -E "^\[|\-\]" | head -20

# 2. etcd Health Check
echo -e "\n=== 2. etcd Health Status ==="
echo "etcd health: $(kubectl get --raw='/healthz/etcd' 2>/dev/null || echo 'FAILED')"

# If etcdctl is available
if command -v etcdctl &> /dev/null; then
    export ETCDCTL_API=3
    ETCD_ENDPOINTS=${ETCD_ENDPOINTS:-"https://127.0.0.1:2379"}
    ETCD_CACERT=${ETCD_CACERT:-"/etc/kubernetes/pki/etcd/ca.crt"}
    ETCD_CERT=${ETCD_CERT:-"/etc/kubernetes/pki/etcd/healthcheck-client.crt"}
    ETCD_KEY=${ETCD_KEY:-"/etc/kubernetes/pki/etcd/healthcheck-client.key"}
    
    echo -e "\n--- etcd endpoint status ---"
    etcdctl --endpoints="$ETCD_ENDPOINTS" \
            --cacert="$ETCD_CACERT" \
            --cert="$ETCD_CERT" \
            --key="$ETCD_KEY" \
            endpoint health 2>/dev/null || echo "Unable to connect to etcd"
            
    echo -e "\n--- etcd member list ---"
    etcdctl --endpoints="$ETCD_ENDPOINTS" \
            --cacert="$ETCD_CACERT" \
            --cert="$ETCD_CERT" \
            --key="$ETCD_KEY" \
            member list 2>/dev/null || echo "Unable to retrieve member list"
fi

# 3. Scheduler Health Check
echo -e "\n=== 3. Scheduler Health Status ==="
kubectl get --raw='/healthz/kube-scheduler' 2>/dev/null || \
kubectl get pods -n kube-system -l component=kube-scheduler -o wide

# 4. Controller Manager Health Check
echo -e "\n=== 4. Controller Manager Health Status ==="
kubectl get --raw='/healthz/kube-controller-manager' 2>/dev/null || \
kubectl get pods -n kube-system -l component=kube-controller-manager -o wide

# 5. Component Status (deprecated but still available)
echo -e "\n=== 5. Component Status (componentstatuses) ==="
kubectl get componentstatuses 2>/dev/null || echo "componentstatuses API is deprecated"

# 6. kube-system core component pods
echo -e "\n=== 6. kube-system Core Pod Status ==="
kubectl get pods -n kube-system -o wide | grep -E "etcd|apiserver|scheduler|controller"
```
### etcd Deep Health Check

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
#!/bin/bash
# etcd-health-check.sh

echo "====== etcd Deep Health Check ======"

export ETCDCTL_API=3
ETCD_ENDPOINTS=${ETCD_ENDPOINTS:-"https://127.0.0.1:2379"}
ETCD_CACERT=${ETCD_CACERT:-"/etc/kubernetes/pki/etcd/ca.crt"}
ETCD_CERT=${ETCD_CERT:-"/etc/kubernetes/pki/etcd/healthcheck-client.crt"}
ETCD_KEY=${ETCD_KEY:-"/etc/kubernetes/pki/etcd/healthcheck-client.key"}

ETCD_OPTS="--endpoints=$ETCD_ENDPOINTS --cacert=$ETCD_CACERT --cert=$ETCD_CERT --key=$ETCD_KEY"

# 1. Cluster health
echo "=== 1. Cluster Health Status ==="
etcdctl $ETCD_OPTS endpoint health --cluster

# 2. Cluster status
echo -e "\n=== 2. Cluster Status ==="
etcdctl $ETCD_OPTS endpoint status --cluster -w table

# 3. Member list
echo -e "\n=== 3. Member List ==="
etcdctl $ETCD_OPTS member list -w table

# 4. Database size
echo -e "\n=== 4. Database Size ==="
etcdctl $ETCD_OPTS endpoint status --cluster -w json | jq -r '.[] | "\(.Endpoint): \(.Status.dbSize / 1024 / 1024 | floor) MB"'

# 5. Leader information
echo -e "\n=== 5. Leader Information ==="
etcdctl $ETCD_OPTS endpoint status --cluster -w json | jq -r '.[] | select(.Status.leader == .Status.header.member_id) | "Leader: \(.Endpoint)"'

# 6. Alarm check
echo -e "\n=== 6. Alarm Check ==="
etcdctl $ETCD_OPTS alarm list

# 7. Key count
echo -e "\n=== 7. Key Count Statistics ==="
echo "Total keys: $(etcdctl $ETCD_OPTS get / --prefix --keys-only 2>/dev/null | wc -l)"

# 8. Performance check
echo -e "\n=== 8. Performance Check (read/write latency) ==="
etcdctl $ETCD_OPTS check perf --load="s" 2>/dev/null || echo "Performance check not available"
```
<!-- chunk: Node Health Check -->
## Node Health Check

### Node Condition Status Details

| Condition | True Meaning | False Meaning | Unknown Meaning | Check Method |
|----------|---------|----------|------------|---------|
| **Ready** | Node healthy, schedulable | Node not healthy | kubelet stopped reporting | kubelet status |
| **MemoryPressure** | Memory below threshold | Memory sufficient | - | free -h |
| **DiskPressure** | Insufficient disk space | Disk sufficient | - | df -h |
| **PIDPressure** | PID approaching limit | PID sufficient | - | ps aux \| wc -l |
| **NetworkUnavailable** | Network not configured | Network normal | - | CNI status |

### Node Health Check Commands

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
#!/bin/bash
# node-health-check.sh

echo "====== Node Health Check ======"
echo "Time: $(date)"
echo ""

# 1. Node overall status
echo "=== 1. Node Status Overview ==="
kubectl get nodes -o wide
echo ""
echo "Ready nodes: $(kubectl get nodes --no-headers | grep " Ready" | wc -l)"
echo "NotReady nodes: $(kubectl get nodes --no-headers | grep -v " Ready" | wc -l)"

# 2. Node Conditions details
echo -e "\n=== 2. Node Conditions ==="
kubectl get nodes -o json | jq -r '
.items[] | 
"\(.metadata.name):" + 
(.status.conditions | map("\n  \(.type): \(.status)") | join(""))'

# 3. Node resource usage
echo -e "\n=== 3. Node Resource Usage ==="
kubectl top nodes 2>/dev/null || echo "Metrics Server not installed"

# 4. Node resource allocation
echo -e "\n=== 4. Node Resource Allocation ==="
for node in $(kubectl get nodes -o name); do
    echo "--- $node ---"
    kubectl describe $node | grep -A 10 "Allocated resources:"
    echo ""
done

# 5. Node Taints
echo -e "\n=== 5. Node Taints ==="
kubectl get nodes -o json | jq -r '.items[] | "\(.metadata.name): \(.spec.taints // "no taints")"'

# 6. Abnormal node details
echo -e "\n=== 6. Abnormal Node Details ==="
for node in $(kubectl get nodes --no-headers | grep -v " Ready" | awk '{print $1}'); do
    echo "=== Abnormal node: $node ==="
    kubectl describe node $node | grep -A 20 "Conditions:"
done
```
### Node Internal Health Check

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
#!/bin/bash
# node-internal-health.sh (run on node)

echo "====== Node Internal Health Check ======"
echo "Hostname: $(hostname)"
echo "Time: $(date)"
echo ""

# 1. System service status
echo "=== 1. Critical Service Status ==="
for svc in kubelet containerd; do
    status=$(systemctl is-active $svc 2>/dev/null)
    echo "$svc: $status"
done

# 2. kubelet health
echo -e "\n=== 2. kubelet Health Check ==="
curl -sk https://localhost:10250/healthz 2>/dev/null || echo "kubelet healthz not accessible"

# 3. Container runtime
echo -e "\n=== 3. Container Runtime Status ==="
crictl info 2>/dev/null | head -20 || echo "crictl not available"

# 4. System resources
echo -e "\n=== 4. System Resources ==="
echo "--- Memory ---"
free -h
echo -e "\n--- Disk ---"
df -h | grep -E "Filesystem|^/dev"
echo -e "\n--- CPU Load ---"
uptime

# 5. Process count
echo -e "\n=== 5. Process Status ==="
echo "Current process count: $(ps aux | wc -l)"
echo "Zombie processes: $(ps aux | grep -c "Z")"

# 6. Network status
echo -e "\n=== 6. Network Status ==="
ip addr show | grep -E "^[0-9]+:|inet " | head -10
echo ""
echo "Default route: $(ip route show default)"

# 7. Time synchronization
echo -e "\n=== 7. Time Synchronization ==="
timedatectl status | grep -E "Local time|System clock|NTP"

# 8. Recent kernel errors
echo -e "\n=== 8. Recent Kernel Errors ==="
dmesg | tail -50 | grep -iE "error|fail|warn|oom" | tail -10
```
<!-- chunk: Pod Health Check -->
## Pod Health Check

### Pod Status Check Matrix

| Status | Meaning | Common Causes | Troubleshooting |
|-----|------|---------|---------|
| **Pending** | Waiting for scheduling | Insufficient resources/affinity/PVC | kubectl describe pod |
| **Running** | Running normally | - | Check container status |
| **Succeeded** | Successfully completed | Job/one-time task | - |
| **Failed** | Failed | Container exit non-zero | kubectl logs |
| **Unknown** | Status unknown | Node unreachable | Check node status |
| **CrashLoopBackOff** | Repeated crashes | Application error/config issue | kubectl logs --previous |
| **ImagePullBackOff** | Image pull failed | Image not found/auth failed | Check image and secrets |
| **ContainerCreating** | Creating | Waiting for resources/mount volumes | kubectl describe pod |

### Pod Health Check Commands

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
#!/bin/bash
# pod-health-check.sh

NAMESPACE=${1:-"--all-namespaces"}

echo "====== Pod Health Check ======"
echo "Namespace: $NAMESPACE"
echo "Time: $(date)"
echo ""

# 1. Pod status statistics
echo "=== 1. Pod Status Statistics ==="
if [ "$NAMESPACE" == "--all-namespaces" ]; then
    kubectl get pods -A --no-headers | awk '{print $4}' | sort | uniq -c | sort -rn
else
    kubectl get pods -n "$NAMESPACE" --no-headers | awk '{print $3}' | sort | uniq -c | sort -rn
fi

# 2. Problem pod list
echo -e "\n=== 2. Problem Pod List ==="
kubectl get pods $NAMESPACE --field-selector=status.phase!=Running,status.phase!=Succeeded --no-headers 2>/dev/null | head -20

# 3. High restart pods
echo -e "\n=== 3. High Restart Pods (>3 times) ==="
kubectl get pods $NAMESPACE -o json | jq -r '
.items[] | 
select(.status.containerStatuses != null) |
select([.status.containerStatuses[].restartCount] | add > 3) |
"\(.metadata.namespace)/\(.metadata.name): \([.status.containerStatuses[].restartCount] | add) restarts"' | head -20

# 4. Not ready pods
echo -e "\n=== 4. Not Ready Pods ==="
kubectl get pods $NAMESPACE -o json | jq -r '
.items[] |
select(.status.containerStatuses != null) |
select([.status.containerStatuses[].ready] | all | not) |
"\(.metadata.namespace)/\(.metadata.name): not ready"' | head -20

# 5. Pending pod details
echo -e "\n=== 5. Pending Pods ==="
for pod in $(kubectl get pods $NAMESPACE --field-selector=status.phase=Pending -o name 2>/dev/null | head -5); do
    echo "--- $pod ---"
    kubectl describe $pod 2>/dev/null | grep -A 10 "Events:" | tail -5
done

# 6. Recent failed events
echo -e "\n=== 6. Recent Pod Warning Events ==="
kubectl get events $NAMESPACE --field-selector=type=Warning --sort-by='.lastTimestamp' 2>/dev/null | tail -20
```
### Pod Resource Usage Check

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
#!/bin/bash
# pod-resource-check.sh

echo "====== Pod Resource Usage Check ======"

# 1. Top 10 memory usage
echo "=== 1. Top 10 Memory Usage Pods ==="
kubectl top pods -A --sort-by=memory 2>/dev/null | head -11

# 2. Top 10 CPU usage
echo -e "\n=== 2. Top 10 CPU Usage Pods ==="
kubectl top pods -A --sort-by=cpu 2>/dev/null | head -11

# 3. High memory usage pods
echo -e "\n=== 3. Pods with Memory Usage >80% ==="
kubectl get pods -A -o json | jq -r '
.items[] |
select(.spec.containers[].resources.limits.memory != null) |
"\(.metadata.namespace)/\(.metadata.name)"' | while read pod; do
    ns=$(echo $pod | cut -d'/' -f1)
    name=$(echo $pod | cut -d'/' -f2)
    usage=$(kubectl top pod $name -n $ns --no-headers 2>/dev/null | awk '{print $3}')
    limit=$(kubectl get pod $name -n $ns -o jsonpath='{.spec.containers[0].resources.limits.memory}' 2>/dev/null)
    if [ -n "$usage" ] && [ -n "$limit" ]; then
        echo "$pod: $usage / $limit"
    fi
done 2>/dev/null | head -20

# 4. Pods without resource limits
echo -e "\n=== 4. Pods Without Memory Limits ==="
kubectl get pods -A -o json | jq -r '
.items[] |
select(.status.phase == "Running") |
select(.spec.containers[].resources.limits.memory == null) |
"\(.metadata.namespace)/\(.metadata.name)"' | head -20
```
<!-- chunk: Network Health Check -->
## Network Health Check

### Network Component Check

``` bash
# 🟡 Medium risk: modifies cluster/resource state, confirm target and authorization before executing
#!/bin/bash
# network-health-check.sh

echo "====== Network Health Check ======"
echo "Time: $(date)"
echo ""

# 1. CoreDNS status
echo "=== 1. CoreDNS Status ==="
kubectl get pods -n kube-system -l k8s-app=kube-dns -o wide
kubectl get svc -n kube-system kube-dns

# 2. kube-proxy status
echo -e "\n=== 2. kube-proxy Status ==="
kubectl get pods -n kube-system -l k8s-app=kube-proxy -o wide | head -10
kubectl get ds -n kube-system kube-proxy

# 3. CNI status (Calico example)
echo -e "\n=== 3. CNI Component Status ==="
# Calico
kubectl get pods -n kube-system -l k8s-app=calico-node -o wide 2>/dev/null | head -10
# Cilium
kubectl get pods -n kube-system -l k8s-app=cilium -o wide 2>/dev/null | head -10
# Flannel
kubectl get pods -n kube-system -l app=flannel -o wide 2>/dev/null | head -10

# 4. Service Endpoints
echo -e "\n=== 4. Services Without Endpoints ==="
kubectl get endpoints -A -o json | jq -r '
.items[] |
select(.subsets == null or .subsets == []) |
"\(.metadata.namespace)/\(.metadata.name)"' | head -20

# 5. DNS resolution test
echo -e "\n=== 5. DNS Resolution Test ==="
kubectl run dns-test --image=busybox:1.36 --rm -it --restart=Never --timeout=60s -- \
    nslookup kubernetes.default.svc.cluster.local 2>/dev/null || echo "DNS test failed or timed out"

# 6. NetworkPolicy count
echo -e "\n=== 6. NetworkPolicy Statistics ==="
kubectl get networkpolicy -A --no-headers 2>/dev/null | wc -l
```
### Network Connectivity Test

> ⚠️ **🔴 Catastrophic operation** — contains irreversible commands, must satisfy change window + dual approval + pre-backup + rollback plan before execution
> - `kubectl delete pod --force`: forcibly delete pod, skip graceful termination and data sync
> - `kubectl apply/create/replace`: create/modify cluster resources
> - `kubectl exec`: enter container to execute commands, may change container state

> **🔴 High Risk Operation Warning**
>
> The commands below are irreversible or high-impact operations. Before execution, confirm:
> - Critical data and configs have been backed up
> - During an approved change window
> - Approved by relevant responsible parties
> - Rollback or recovery plan is prepared
> - Target cluster, namespace, node/resource names are correct

``` bash
# 🔴 High risk: may cause data loss or service interruption, requires backup, change approval, and rollback plan before execution
#!/bin/bash
# network-connectivity-test.sh

echo "====== Network Connectivity Test ======"

# Create test pod
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: network-test
  namespace: default
spec:
  containers:
  - name: test
    image: nicolaka/netshoot:latest
    command: ["sleep", "3600"]
EOF

echo "Waiting for test pod to be ready..."
kubectl wait --for=condition=Ready pod/network-test --timeout=120s

# 1. DNS test
echo -e "\n=== 1. DNS Resolution Test ==="
kubectl exec network-test -- nslookup kubernetes.default.svc.cluster.local
kubectl exec network-test -- nslookup google.com

# 2. Service access test
echo -e "\n=== 2. Kubernetes API Access ==="
kubectl exec network-test -- curl -sk https://kubernetes.default.svc:443/healthz

# 3. External network test
echo -e "\n=== 3. External Network Test ==="
kubectl exec network-test -- curl -s -o /dev/null -w "%{http_code}" https://www.google.com --connect-timeout 5 || echo "External network unreachable"

# 4. Cross-node pod communication
echo -e "\n=== 4. Cross-node Communication Test ==="
# Get pod IP on another node
OTHER_POD_IP=$(kubectl get pods -A -o wide --no-headers | grep -v "$(kubectl get pod network-test -o jsonpath='{.spec.nodeName}')" | head -1 | awk '{print $7}')
if [ -n "$OTHER_POD_IP" ]; then
    kubectl exec network-test -- ping -c 3 $OTHER_POD_IP || echo "Cross-node communication failed"
fi

# Cleanup
kubectl delete pod network-test --force --grace-period=0 2>/dev/null  # ⚠️ Skip graceful termination, may lose data
```
<!-- chunk: Storage Health Check -->
## Storage Health Check

### Storage Component Check

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
#!/bin/bash
# storage-health-check.sh

echo "====== Storage Health Check ======"
echo "Time: $(date)"
echo ""

# 1. StorageClass
echo "=== 1. StorageClass ==="
kubectl get sc
echo ""
DEFAULT_SC=$(kubectl get sc -o json | jq -r '.items[] | select(.metadata.annotations["storageclass.kubernetes.io/is-default-class"]=="true") | .metadata.name')
echo "Default StorageClass: ${DEFAULT_SC:-none}"

# 2. PV status
echo -e "\n=== 2. PersistentVolume Status ==="
kubectl get pv
echo ""
echo "PV status statistics:"
kubectl get pv -o json | jq -r '.items[].status.phase' | sort | uniq -c

# 3. PVC status
echo -e "\n=== 3. PersistentVolumeClaim Status ==="
kubectl get pvc -A
echo ""
echo "PVC status statistics:"
kubectl get pvc -A -o json | jq -r '.items[].status.phase' | sort | uniq -c

# 4. Pending PVC
echo -e "\n=== 4. Pending PVC ==="
kubectl get pvc -A --field-selector=status.phase=Pending --no-headers 2>/dev/null

# 5. Released PV (requires manual handling)
echo -e "\n=== 5. Released PV (waiting for cleanup) ==="
kubectl get pv --field-selector=status.phase=Released --no-headers 2>/dev/null

# 6. CSI Driver
echo -e "\n=== 6. CSI Driver ==="
kubectl get csidrivers 2>/dev/null || echo "No CSI Driver"

# 7. VolumeAttachment
echo -e "\n=== 7. VolumeAttachment Status ==="
kubectl get volumeattachment 2>/dev/null | head -10
```
<!-- chunk: Security Health Check -->
## Security Health Check

### Security Configuration Check

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
#!/bin/bash
# security-health-check.sh

echo "====== Security Health Check ======"
echo "Time: $(date)"
echo ""

# 1. RBAC status
echo "=== 1. RBAC Status ==="
kubectl api-versions | grep -q "rbac.authorization.k8s.io" && echo "RBAC enabled" || echo "⚠️ RBAC not enabled"

# 2. Pod Security Standards
echo -e "\n=== 2. Pod Security Standards ==="
kubectl get ns -L pod-security.kubernetes.io/enforce | grep -v "NAME"

# 3. ServiceAccount check
echo -e "\n=== 3. Pods Using Default SA ==="
kubectl get pods -A -o json | jq -r '
.items[] |
select(.spec.serviceAccountName == "default" or .spec.serviceAccountName == null) |
"\(.metadata.namespace)/\(.metadata.name)"' | head -20

# 4. Privileged containers
echo -e "\n=== 4. Privileged Containers ==="
kubectl get pods -A -o json | jq -r '
.items[] |
select(.spec.containers[].securityContext.privileged == true) |
"\(.metadata.namespace)/\(.metadata.name)"' | head -20

# 5. hostNetwork pods
echo -e "\n=== 5. hostNetwork Pods ==="
kubectl get pods -A -o json | jq -r '
.items[] |
select(.spec.hostNetwork == true) |
"\(.metadata.namespace)/\(.metadata.name)"' | head -20

# 6. Secret check
echo -e "\n=== 6. Secret Statistics ==="
kubectl get secrets -A --no-headers | wc -l
echo "Type distribution:"
kubectl get secrets -A -o json | jq -r '.items[].type' | sort | uniq -c | sort -rn | head -10

# 7. NetworkPolicy coverage
echo -e "\n=== 7. NetworkPolicy Coverage ==="
TOTAL_NS=$(kubectl get ns --no-headers | wc -l)
NS_WITH_NP=$(kubectl get networkpolicy -A -o json | jq -r '.items[].metadata.namespace' | sort -u | wc -l)
echo "Namespaces with NetworkPolicy: $NS_WITH_NP / $TOTAL_NS"
```
<!-- chunk: Automated Health Check Script -->
## Automated Health Check Script

### Complete Health Check Script

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
#!/bin/bash
# k8s-full-health-check.sh - Kubernetes Cluster Full Health Check

set -e

OUTPUT_FILE=${1:-"/tmp/k8s-health-report-$(date +%Y%m%d-%H%M%S).txt"}

exec > >(tee -a "$OUTPUT_FILE") 2>&1

echo "============================================================"
echo "       Kubernetes Cluster Health Check Report"
echo "============================================================"
echo "Check time: $(date)"
echo "Cluster info: $(kubectl cluster-info | head -1)"
echo "Kubernetes version: $(kubectl version --short 2>/dev/null | grep Server || kubectl version -o json | jq -r '.serverVersion.gitVersion')"
echo ""

# Health status counter
WARNINGS=0
ERRORS=0

check_pass() {
    echo "[PASS] $1"
}

check_warn() {
    echo "[WARN] $1"
    ((WARNINGS++))
}

check_fail() {
    echo "[FAIL] $1"
    ((ERRORS++))
}

# ==================== Control Plane Check ====================
echo ""
echo "==================== 1. Control Plane Health ===================="

# API Server
API_HEALTH=$(kubectl get --raw='/healthz' 2>/dev/null || echo "failed")
if [ "$API_HEALTH" == "ok" ]; then
    check_pass "API Server healthy"
else
    check_fail "API Server not healthy"
fi

# etcd
ETCD_HEALTH=$(kubectl get --raw='/healthz/etcd' 2>/dev/null || echo "failed")
if [ "$ETCD_HEALTH" == "ok" ]; then
    check_pass "etcd healthy"
else
    check_fail "etcd not healthy"
fi

# Scheduler pod
SCHEDULER_RUNNING=$(kubectl get pods -n kube-system -l component=kube-scheduler --no-headers 2>/dev/null | grep -c Running)
if [ "$SCHEDULER_RUNNING" -ge 1 ]; then
    check_pass "Scheduler running ($SCHEDULER_RUNNING instances)"
else
    check_fail "Scheduler not running"
fi

# Controller Manager pod
CM_RUNNING=$(kubectl get pods -n kube-system -l component=kube-controller-manager --no-headers 2>/dev/null | grep -c Running)
if [ "$CM_RUNNING" -ge 1 ]; then
    check_pass "Controller Manager running ($CM_RUNNING instances)"
else
    check_fail "Controller Manager not running"
fi

# ==================== Node Check ====================
echo ""
echo "==================== 2. Node Health ===================="

TOTAL_NODES=$(kubectl get nodes --no-headers | wc -l)
READY_NODES=$(kubectl get nodes --no-headers | grep " Ready" | wc -l)
NOTREADY_NODES=$((TOTAL_NODES - READY_NODES))

echo "Total nodes: $TOTAL_NODES"
echo "Ready nodes: $READY_NODES"
echo "NotReady nodes: $NOTREADY_NODES"

if [ "$NOTREADY_NODES" -eq 0 ]; then
    check_pass "All nodes Ready"
else
    check_fail "$NOTREADY_NODES NotReady nodes exist"
    kubectl get nodes | grep -v " Ready"
fi

# Node resource pressure
PRESSURE_NODES=$(kubectl get nodes -o json | jq -r '.items[] | select(.status.conditions[] | select(.type != "Ready" and .status == "True")) | .metadata.name' | wc -l)
if [ "$PRESSURE_NODES" -eq 0 ]; then
    check_pass "No node resource pressure"
else
    check_warn "$PRESSURE_NODES nodes have resource pressure"
fi

# ==================== Pod Check ====================
echo ""
echo "==================== 3. Pod Health ===================="

# Problem pods
PENDING_PODS=$(kubectl get pods -A --field-selector=status.phase=Pending --no-headers 2>/dev/null | wc -l)
FAILED_PODS=$(kubectl get pods -A --field-selector=status.phase=Failed --no-headers 2>/dev/null | wc -l)
CRASHLOOP_PODS=$(kubectl get pods -A --no-headers 2>/dev/null | grep -c CrashLoopBackOff || echo 0)

if [ "$PENDING_PODS" -eq 0 ]; then
    check_pass "No Pending pods"
else
    check_warn "$PENDING_PODS Pending pods exist"
fi

if [ "$FAILED_PODS" -eq 0 ]; then
    check_pass "No Failed pods"
else
    check_warn "$FAILED_PODS Failed pods exist"
fi

if [ "$CRASHLOOP_PODS" -eq 0 ]; then
    check_pass "No CrashLoopBackOff pods"
else
    check_fail "$CRASHLOOP_PODS CrashLoopBackOff pods exist"
fi

# kube-system pods
KUBE_SYSTEM_ISSUES=$(kubectl get pods -n kube-system --no-headers | grep -v Running | grep -v Completed | wc -l)
if [ "$KUBE_SYSTEM_ISSUES" -eq 0 ]; then
    check_pass "kube-system all pods normal"
else
    check_fail "kube-system has $KUBE_SYSTEM_ISSUES problem pods"
    kubectl get pods -n kube-system | grep -v Running | grep -v Completed
fi

# ==================== Network Check ====================
echo ""
echo "==================== 4. Network Health ===================="

# CoreDNS
COREDNS_READY=$(kubectl get pods -n kube-system -l k8s-app=kube-dns --no-headers 2>/dev/null | grep -c Running)
if [ "$COREDNS_READY" -ge 1 ]; then
    check_pass "CoreDNS running ($COREDNS_READY replicas)"
else
    check_fail "CoreDNS not running"
fi

# kube-proxy
KUBE_PROXY_READY=$(kubectl get pods -n kube-system -l k8s-app=kube-proxy --no-headers 2>/dev/null | grep -c Running)
if [ "$KUBE_PROXY_READY" -ge 1 ]; then
    check_pass "kube-proxy running ($KUBE_PROXY_READY nodes)"
else
    check_fail "kube-proxy not running"
fi

# Services without endpoints
NO_ENDPOINTS=$(kubectl get endpoints -A -o json | jq -r '.items[] | select(.subsets == null or .subsets == []) | select(.metadata.name != "kubernetes") | .metadata.name' | wc -l)
if [ "$NO_ENDPOINTS" -eq 0 ]; then
    check_pass "All services have endpoints"
else
    check_warn "$NO_ENDPOINTS services have no endpoints"
fi

# ==================== Storage Check ====================
echo ""
echo "==================== 5. Storage Health ===================="

# PVC status
PENDING_PVC=$(kubectl get pvc -A --field-selector=status.phase=Pending --no-headers 2>/dev/null | wc -l)
if [ "$PENDING_PVC" -eq 0 ]; then
    check_pass "No Pending PVC"
else
    check_warn "$PENDING_PVC Pending PVC exist"
fi

# Released PV
RELEASED_PV=$(kubectl get pv --field-selector=status.phase=Released --no-headers 2>/dev/null | wc -l)
if [ "$RELEASED_PV" -eq 0 ]; then
    check_pass "No Released PV"
else
    check_warn "$RELEASED_PV Released PV need handling"
fi

# ==================== Security Check ====================
echo ""
echo "==================== 6. Security Status ===================="

# RBAC
if kubectl api-versions | grep -q "rbac.authorization.k8s.io"; then
    check_pass "RBAC enabled"
else
    check_fail "RBAC not enabled"
fi

# Privileged containers
PRIVILEGED_PODS=$(kubectl get pods -A -o json | jq -r '.items[] | select(.spec.containers[].securityContext.privileged == true) | .metadata.name' | wc -l)
if [ "$PRIVILEGED_PODS" -lt 10 ]; then
    check_pass "Privileged container count reasonable ($PRIVILEGED_PODS)"
else
    check_warn "High privileged container count ($PRIVILEGED_PODS)"
fi

# ==================== Summary ====================
echo ""
echo "============================================================"
echo "                      Check Summary"
echo "============================================================"
echo "Warnings: $WARNINGS"
echo "Errors: $ERRORS"
echo ""

if [ "$ERRORS" -eq 0 ] && [ "$WARNINGS" -eq 0 ]; then
    echo "Status: ✅ Cluster healthy"
elif [ "$ERRORS" -eq 0 ]; then
    echo "Status: ⚠️ Cluster basically healthy, $WARNINGS warnings need attention"
else
    echo "Status: ❌ Cluster has issues, $ERRORS errors need immediate handling"
fi

echo ""
echo "Report saved to: $OUTPUT_FILE"
```
<!-- chunk: Prometheus Monitoring Metrics -->
## Prometheus Monitoring Metrics

### Key Health Metrics

| Metric | Alert Condition | Severity | Description |
|-----|---------|-------|------|
| `up{job="kubernetes-apiservers"}` | == 0 | Critical | API Server unavailable |
| `etcd_server_has_leader` | == 0 | Critical | etcd has no leader |
| `kube_node_status_condition{condition="Ready",status="true"}` | == 0 | Critical | Node NotReady |
| `kube_pod_status_phase{phase="Failed"}` | > 0 for 5m | Warning | Pod failed |
| `kubelet_pleg_relist_duration_seconds_bucket` | P99 > 3s | Warning | kubelet PLEG slow |
| `scheduler_pending_pods` | > 100 for 10m | Warning | Scheduling backlog |
| `etcd_mvcc_db_total_size_in_bytes` | > 6GB | Warning | etcd database too large |
| `apiserver_request_duration_seconds_bucket` | P99 > 1s | Warning | API request slow |

### Prometheus Alert Rules

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: cluster-health-alerts
  namespace: monitoring
spec:
  groups:
  - name: cluster.health
    interval: 30s
    rules:
    # API Server alerts
    - alert: KubeAPIServerDown
      expr: up{job="kubernetes-apiservers"} == 0
      for: 3m
      labels:
        severity: critical
      annotations:
        summary: "Kubernetes API Server unavailable"
        
    - alert: KubeAPIServerLatencyHigh
      expr: |
        histogram_quantile(0.99, sum(rate(apiserver_request_duration_seconds_bucket{verb!="WATCH"}[5m])) by (verb, le)) > 1
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "API Server request latency high"
        
    # etcd alerts
    - alert: EtcdNoLeader
      expr: etcd_server_has_leader == 0
      for: 1m
      labels:
        severity: critical
      annotations:
        summary: "etcd cluster has no leader"
        
    - alert: EtcdDatabaseSizeHigh
      expr: etcd_mvcc_db_total_size_in_bytes > 6*1024*1024*1024
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "etcd database size exceeds 6GB"
        
    # Node alerts
    - alert: KubeNodeNotReady
      expr: kube_node_status_condition{condition="Ready",status="true"} == 0
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "Node {{ $labels.node }} NotReady"
        
    # Pod alerts
    - alert: KubePodCrashLooping
      expr: |
        rate(kube_pod_container_status_restarts_total[15m]) * 60 * 5 > 0
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Pod {{ $labels.namespace }}/{{ $labels.pod }} frequently restarting"
        
    # Scheduling alerts
    - alert: KubeSchedulerPendingPods
      expr: scheduler_pending_pods > 100
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "Scheduling queue backlog exceeds 100 pods"
```

<!-- chunk: ACK Health Check -->
## ACK Health Check

### Alibaba Cloud ACK Specific Check

| Feature | Entry | Check Content | Description |
|-----|------|---------|------|
| **Cluster Diagnostics** | Console-Operations Management | Comprehensive health check | One-click diagnosis |
| **Node Diagnostics** | Console-Node Management | Node issue troubleshooting | Single node diagnosis |
| **Network Diagnostics** | Console-Network | Network connectivity | VPC/ENI check |
| **ARMS Monitoring** | ARMS Console | Component metrics | Deep monitoring |
| **Logging Service** | SLS Console | Log analysis | Audit/diagnostic logs |

```bash
# ACK Cluster Diagnostics CLI
# Install ack-diagnose tool
curl -O https://alibabacloud-china.github.io/diagnose-tools/scripts/installer.sh
bash installer.sh

# Cluster diagnostics
ack-diagnose cluster --cluster-id <cluster-id>

# Node diagnostics
ack-diagnose node --cluster-id <cluster-id> --node-name <node-name>

# Network diagnostics
ack-diagnose network --cluster-id <cluster-id> --source-pod <pod-name> --target-pod <pod-name>

# Use aliyun CLI
aliyun cs DescribeClusterDetail --ClusterId <cluster-id>
aliyun cs DescribeClusterNodes --ClusterId <cluster-id>
```

<!-- chunk: Best Practices -->
## Best Practices

### Health Check Frequency Recommendation

| Check Type | Recommended Frequency | Automation | Description |
|---------|---------|-------|------|
| Control Plane | 1 minute | Yes | Prometheus monitoring |
| Node Status | 1 minute | Yes | Node exporter |
| Pod Status | 5 minutes | Yes | kube-state-metrics |
| Network Connectivity | 15 minutes | Yes | Black-box probing |
| Storage Status | 5 minutes | Yes | CSI monitoring |
| Security Audit | Daily | Yes | Periodic scanning |
| Full Report | Daily | Yes | Automated script |

### Health Check Checklist Summary

```
□ Control Plane
  ├── API Server /healthz, /readyz
  ├── etcd health and cluster status
  ├── Scheduler running status
  └── Controller Manager running status

□ Nodes
  ├── All nodes Ready
  ├── No resource pressure (Memory/Disk/PID)
  ├── kubelet and containerd normal
  └── Resource usage rates reasonable

□ Pods
  ├── No Pending/Failed/CrashLoopBackOff
  ├── kube-system components normal
  ├── Restart count reasonable
  └── Resource configuration reasonable

□ Network
  ├── CoreDNS normal
  ├── kube-proxy normal
  ├── CNI components normal
  └── Services have endpoints

□ Storage
  ├── All PVC Bound
  ├── No Released PV
  └── CSI Driver normal

□ Security
  ├── RBAC enabled
  ├── PSS/PSA configured
  └── Privileged container audited
```

<!-- chunk: Version Change History -->
## Version Change History

| Version | Changes | Impact |
|-----|---------|------|
| v1.16 | /livez and /readyz endpoints | Finer-grained health checks |
| v1.24 | componentstatuses deprecated | Use /readyz instead |
| v1.26 | Node logging API | Remote kubelet log retrieval |
| v1.28 | /readyz?verbose enhanced | More detailed status info |
| v1.29 | Health check metrics enhanced | More diagnostic metrics |
| v1.30 | Node problem detector enhanced | Better problem detection |

---

**Health Check Principle**: Regular checks → Automated monitoring → Quick response → Root cause analysis → Continuous improvement

---

**Table Footer Attribution**: Kusheet Project, author Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian Related Documents -->
## Obsidian Related Documents

- [domain-06-observability MOC](domain-06-observability/MOC.md)
- [Observability Domain](domain-06-observability/README.md)
- [Domain-8 Observability - Open Source Project Index](index.md)
- Kubernetes Observability Architecture System
- Metrics Monitoring System Explained
- 03 - Logging Architecture Explained
- Distributed Tracing System
- 05 - Alert Management Strategy
- 06 - Monitoring Alert Practice and Best Practices
- 04 - Monitoring Dashboard Design and Best Practices
- 08 - Logging Audit and Compliance Management
- 05 - Event and Audit Log Management

## See Also

- 11-custom-metrics-adapter
- 12-logging-auditing
- 14-chaos-engineering
- 15-enterprise-scale-monitoring

- [Back to index](domain-06-observability/README.md)

## Related

- [Observability Knowledge Map Index](domain-19-landscape-references/topic-index/observability-index.md)

```

<!-- risk-assessed -->
