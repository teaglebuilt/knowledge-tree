---
title: 10 - Kubernetes Production Environment Troubleshooting Guide
description: Comprehensive guide to troubleshooting Kubernetes production environments with proven methodologies and deep diagnostic techniques
summary: Systematic troubleshooting methodologies, toolchains, and best practices for Kubernetes production environments covering Pod, Node, networking, storage, control plane and other components
category: general
tags:
- k8s
- observability
- prometheus
- monitoring
- troubleshooting
- deep-dive
- etcd
- apiserver
- kubelet
- scheduler
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All engineers
estimated_read_time: 1h
intent_queries:
- What is 25-troubleshooting-overview?
- What are the core concepts of 25-troubleshooting-overview?
- How to understand 25-troubleshooting-overview?
trigger_keywords:
- Kubernetes
- Production Environment Troubleshooting Guide
- Production
- Troubleshooting
- Guide
- observability
prerequisites:
- kubectl-basics
- observability-basics
- prometheus-basics
- monitoring-basics
- cilium-basics
- cni-basics
- etcd-basics
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/01-overview/25-troubleshooting-overview.md
---

> **Production Environment Security Notice**
>
> This document contains directly executable operations commands. Before executing, please verify: the target cluster and namespace are correct; you have sufficient RBAC permissions; the commands have been tested in non-production environments. Command risk levels: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state but usually reversible), 🟢 Low risk/read-only (information collection, no side effects).

# 10 - Kubernetes Production Environment Troubleshooting Guide

> **Applicable versions**: v1.25 - v1.32 | **Last updated**: 2026-01 | **Reference**: [kubernetes.io/docs/tasks/debug](https://kubernetes.io/docs/tasks/debug/)

This document provides comprehensive guidance on Kubernetes production environment troubleshooting from a senior SRE operations expert perspective, systematically describing troubleshooting methodologies, toolchains, and best practices. It covers deep diagnostic techniques for Pods, Nodes, networking, storage, control plane and other components, combined with large-scale cluster operations experience, providing complete guidance for enterprises to build standardized and automated problem response systems.

---

<!-- chunk: Table of Contents -->
## Table of Contents

- [Troubleshooting Methodology](#troubleshooting-methodology)
- [Pod Troubleshooting](#pod-troubleshooting)
- [Node Troubleshooting](#node-troubleshooting)
- [Service/Network Troubleshooting](#servicenetwork-troubleshooting)
- [Storage Troubleshooting](#storage-troubleshooting)
- [Control Plane Troubleshooting](#control-plane-troubleshooting)
- [Scheduler Troubleshooting](#scheduler-troubleshooting)
- [Application Deployment Troubleshooting](#application-deployment-troubleshooting)
- [Security/Permission Troubleshooting](#securitypermission-troubleshooting)
- [Performance Issue Troubleshooting](#performance-issue-troubleshooting)
- [Cluster Upgrade Troubleshooting](#cluster-upgrade-troubleshooting)
- [Version-Specific Known Issues](#version-specific-known-issues)
- [Production-Grade Diagnostic Toolset](#production-grade-diagnostic-toolset)
- [Monitoring Alert Integration](#monitoring-alert-integration)
- [Production SOP Process](#production-sop-process)

---

<!-- chunk: Troubleshooting Methodology -->
## Troubleshooting Methodology

### Golden Troubleshooting Principles

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    Four-Step Troubleshooting Method                        │
├─────────────────────────────────────────────────────────────────────────────┤
│  Step 1: Symptom Identification → Resource state, Events, condition checks │
│  Step 2: Scope Definition → Single-point vs global issue, timeline tracing │
│  Step 3: Root Cause Analysis → Log analysis, metric correlation, audit     │
│  Step 4: Fix Verification → Fix implementation, regression test, prevention │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Generic Diagnostic Command Matrix

| Layer | Diagnostic Command | Purpose | Version Notes |
|:---:|:---|:---|:---|
| **Cluster** | `kubectl cluster-info` | Cluster connectivity verification | All versions |
| **Cluster** | `kubectl get --raw='/readyz?verbose'` | API Server health check | v1.16+ |
| **Cluster** | `kubectl get componentstatuses` | Control plane component status (deprecated) | Before v1.25 |
| **Node** | `kubectl get nodes -o wide` | Node status overview | All versions |
| **Node** | `kubectl describe node <name>` | Node details/conditions/events | All versions |
| **Node** | `kubectl top nodes` | Node resource usage | Requires Metrics Server |
| **Pod** | `kubectl get pods -A --field-selector=status.phase!=Running,status.phase!=Succeeded` | Abnormal Pod filtering | All versions |
| **Pod** | `kubectl describe pod <name>` | Pod details/Events | All versions |
| **Pod** | `kubectl logs <pod> [-c container] [--previous]` | Container logs | All versions |
| **Pod** | `kubectl debug <pod> --image=busybox -it` | Temporary debug container | v1.25+ GA |
| **Events** | `kubectl get events -A --sort-by='.lastTimestamp'` | Global event sorting | All versions |
| **Network** | `kubectl exec <pod> -- curl -v <service>` | Service connectivity test | All versions |
| **Storage** | `kubectl get pv,pvc -A` | Storage resource status | All versions |

---

<!-- chunk: Pod Troubleshooting -->
## Pod Troubleshooting

### Pod Status Machine and Problem Mapping

```yaml
# Pod lifecycle status machine
Pod status flow:
  Pending:
    - Scheduling: Waiting for scheduler to allocate node
    - Volume mounting: Waiting for storage volume to be ready
    - Image pulling: Waiting for container image download
  Running:
    - Normal operation: At least one container is running
    - Probe failure: Liveness/readiness probe detection failure
  Succeeded: All containers exited normally (exit 0)
  Failed: At least one container exited abnormally
  Unknown: Node disconnected, status cannot be obtained
```

### Pod Pending Deep Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **Pending - Insufficient Resources** | CPU/Memory insufficient | `kubectl describe pod`, `kubectl describe node` | - | Check ResourceQuota, scale up node pool | Configure Cluster Autoscaler, set reasonable resource requests |
| **Pending - Scheduling Constraints** | nodeSelector/affinity cannot be satisfied | `kubectl describe pod` check Events | v1.25+ topology constraint enhancement | Check node labels, adjust scheduling constraints | Use preferredDuringScheduling instead of required |
| **Pending - PVC Unbound** | StorageClass has no provisioner | `kubectl get pvc`, `kubectl describe pvc` | v1.27+ storage capacity tracking | Check StorageClass, verify provisioner is available | Configure default StorageClass, monitor storage quota |
| **Pending - Taint Not Tolerated** | Node has Taint without corresponding Toleration | `kubectl describe node \| grep Taint` | - | Add Toleration or remove Taint | Document Taint policy, CI/CD validation |
| **Pending - Pod Affinity** | requiredDuringScheduling cannot be satisfied | `kubectl describe pod`, check other Pod distribution | v1.26 topology awareness enhancement | Adjust affinity rules or add matching Pod | Use soft affinity, set reasonable topologyKey |
| **Pending - Node Selector** | Label mismatch | `kubectl get nodes --show-labels` | - | Check node labels, correct selector | Use nodeAffinity instead of nodeSelector |
| **Pending - ResourceQuota** | Namespace quota exhausted | `kubectl describe quota -n <ns>` | - | Request more quota or optimize resource usage | Monitor quota usage, set alerts |
| **Pending - LimitRange** | Resource request exceeds limits | `kubectl describe limitrange -n <ns>` | - | Adjust Pod resource request or modify LimitRange | Set reasonable defaults |
| **Pending - PodDisruptionBudget** | PDB blocks scheduling | `kubectl get pdb -A` | v1.27 unhealthyPodEvictionPolicy | Check PDB config, wait for existing Pod recovery | Configure reasonable minAvailable |
| **Pending - Node Unschedulable** | Node is cordoned | `kubectl get nodes` check SCHEDULE status | - | Uncordon node or select other node | Monitor node schedulable status |

#### Pending Diagnosis Script

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
#!/bin/bash
# pending-pod-diagnose.sh - Pod Pending deep diagnosis

POD_NAME=$1
NAMESPACE=${2:-default}

echo "=== Pod Pending Diagnosis Report ==="
echo "Pod: $POD_NAME, Namespace: $NAMESPACE"
echo ""

# 1. Pod Events
echo "=== Pod Events ==="
kubectl describe pod $POD_NAME -n $NAMESPACE | grep -A 20 "Events:"

# 2. Scheduler-related logs
echo -e "\n=== Scheduler-related Logs ==="
kubectl logs -n kube-system -l component=kube-scheduler --tail=50 2>/dev/null | grep -i "$POD_NAME" || echo "No relevant scheduler logs found"

# 3. Node resource status
echo -e "\n=== Node Resource Overview ==="
kubectl top nodes 2>/dev/null || echo "Metrics Server not installed"

# 4. Node schedulable conditions
echo -e "\n=== Node Schedulable Status ==="
kubectl get nodes -o custom-columns=NAME:.metadata.name,STATUS:.status.conditions[-1].type,SCHEDULABLE:.spec.unschedulable

# 5. ResourceQuota check
echo -e "\n=== ResourceQuota Status ==="
kubectl describe quota -n $NAMESPACE 2>/dev/null || echo "No ResourceQuota"

# 6. PVC status check
echo -e "\n=== Related PVC Status ==="
kubectl get pod $POD_NAME -n $NAMESPACE -o jsonpath='{range .spec.volumes[*]}{.persistentVolumeClaim.claimName}{"\n"}{end}' | xargs -I {} kubectl get pvc {} -n $NAMESPACE 2>/dev/null

# 7. Node Taints
echo -e "\n=== Node Taints ==="
kubectl get nodes -o custom-columns=NAME:.metadata.name,TAINTS:.spec.taints

```

### Pod CrashLoopBackOff Deep Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **Immediate Crash** | Application code exception | `kubectl logs <pod> --previous` | - | Check application logs, fix code bug | Local testing, robust error handling |
| **Dependency Service Unavailable** | Startup dependency not satisfied | `kubectl logs <pod>`, check Service status | v1.28 Native Sidecar | Use init container to wait for dependency, configure retry | Dependency service health check, readiness probe |
| **Configuration Error** | ConfigMap/Secret error | `kubectl describe pod`, check mount | - | Check configuration content, correct mount path | Configuration versioning, change audit |
| **Missing Environment Variables** | Required environment variable not set | `kubectl exec <pod> -- env` | - | Supplement missing environment variables | Configuration validation, use ConfigMap |
| **Insufficient Permissions** | File/directory permission issue | `kubectl logs <pod>`, check fsGroup | - | Configure securityContext, fsGroup | Standardize security context config |
| **Resource Limit** | CPU throttling/OOMKilled | `kubectl describe pod`, check Terminated reason | v1.27 in-place adjustment | Increase resource limits, optimize application | Reasonable resource requests, performance testing |
| **Liveness Probe Failure** | Probe configuration improper | `kubectl describe pod`, Liveness probe failed | - | Adjust probe timeout/threshold, fix health endpoint | Reasonable initialDelaySeconds |
| **Command/Argument Error** | Entrypoint configuration error | `kubectl describe pod`, check command/args | - | Correct container command config | Dockerfile best practices |
| **Image Issue** | Image entrypoint missing | `kubectl logs <pod>` | - | Check image, specify correct command | Image build specification |
| **Init Container Failure** | Initialization phase failure | `kubectl logs <pod> -c <init-container>` | v1.28 Sidecar enhancement | Check init container logs, fix initialization | Init container idempotency design |

#### CrashLoopBackOff Diagnosis Script

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
#!/bin/bash
# crashloop-diagnose.sh - CrashLoopBackOff deep diagnosis

POD_NAME=$1
NAMESPACE=${2:-default}

echo "=== CrashLoopBackOff Diagnosis Report ==="
echo "Pod: $POD_NAME, Namespace: $NAMESPACE"

# 1. Get container exit status
echo -e "\n=== Container Status Details ==="
kubectl get pod $POD_NAME -n $NAMESPACE -o jsonpath='{range .status.containerStatuses[*]}Container: {.name}
  Ready: {.ready}
  RestartCount: {.restartCount}
  LastState: {.lastState}
  State: {.state}
{end}'

# 2. Get previous logs
echo -e "\n=== Previous Container Logs ==="
kubectl logs $POD_NAME -n $NAMESPACE --previous --tail=100 2>/dev/null || echo "Cannot get previous logs"

# 3. Current logs
echo -e "\n=== Current Container Logs ==="
kubectl logs $POD_NAME -n $NAMESPACE --tail=50 2>/dev/null || echo "Container not running"

# 4. Events
echo -e "\n=== Pod Events ==="
kubectl get events -n $NAMESPACE --field-selector involvedObject.name=$POD_NAME --sort-by='.lastTimestamp'

# 5. Container command check
echo -e "\n=== Container Command Configuration ==="
kubectl get pod $POD_NAME -n $NAMESPACE -o jsonpath='{range .spec.containers[*]}Container: {.name}
  Image: {.image}
  Command: {.command}
  Args: {.args}
{end}'

# 6. Probe configuration
echo -e "\n=== Probe Configuration ==="
kubectl get pod $POD_NAME -n $NAMESPACE -o jsonpath='{range .spec.containers[*]}Container: {.name}
  LivenessProbe: {.livenessProbe}
  ReadinessProbe: {.readinessProbe}
{end}'
```

### Pod OOMKilled Deep Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **Container OOMKilled** | Memory exceeds limits | `kubectl describe pod`, check lastState.terminated.reason | v1.27 in-place Pod adjustment | Increase memory limits, optimize memory usage | Load testing to determine memory requirements, monitor memory usage |
| **System OOM** | Node memory insufficient | `dmesg \| grep -i oom`, `journalctl -k \| grep -i oom` | v1.26 eviction enhancement | Evict Pod, scale up nodes | Configure system reserved resources, eviction-hard |
| **Memory Leak** | Application memory continuously growing | Prometheus memory metrics, profiling | - | Fix application memory leak | Regular profiling, memory limit alerts |
| **JVM Heap Configuration** | Java heap exceeds limits | JVM logs, `-XX:+HeapDumpOnOutOfMemoryError` | - | Configure -Xmx smaller than limits | Container-aware JVM params (-XX:+UseContainerSupport) |
| **Cache Unlimited Growth** | Application cache has no upper limit | Application metrics, heap analysis | - | Configure cache eviction policy | Monitor cache size, set reasonable TTL |

#### OOMKilled Diagnosis YAML

```yaml
# oom-debug-pod.yaml - Memory diagnosis Pod
apiVersion: v1
kind: Pod
metadata:
  name: oom-debug
spec:
  containers:
  - name: debug
    image: alpine:3.19
    command: ["sh", "-c", "while true; do cat /sys/fs/cgroup/memory/memory.usage_in_bytes 2>/dev/null || cat /sys/fs/cgroup/memory.current; sleep 5; done"]
    resources:
      requests:
        memory: "64Mi"
      limits:
        memory: "128Mi"
  restartPolicy: Never
```

### Pod ImagePullBackOff Deep Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **Image Not Found** | Tag error/image deleted | `kubectl describe pod`, Events | - | Check image name and tag, push correct image | CI/CD verify image exists, use immutable tag |
| **Authentication Failure** | imagePullSecrets configuration error | `kubectl describe pod`, `kubectl get secret` | - | Check Secret content, update authentication info | Secret auto-rotation, use ImagePullJob prewarming |
| **Network Issue** | Cannot access registry | Test `curl https://registry/v2/` on node | - | Check network policy, proxy config | Use private registry mirror, configure mirror |
| **Rate Limiting** | Docker Hub/Registry throttling | Events show 429 error | - | Wait for retry, use authenticated account | Private registry, configure pull-through cache |
| **Platform Mismatch** | arm64 vs amd64 | `kubectl describe pod`, exec format error | v1.25+ multi-arch enhancement | Use multi-arch image, specify correct platform | Build multi-arch images, node affinity |
| **TLS Certificate Issue** | Private registry certificate untrusted | containerd/Docker logs | - | Configure insecure-registries or add CA cert | Use public CA signed certificates |

#### ImagePull Diagnosis Script

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
#!/bin/bash
# imagepull-diagnose.sh - Image pull issue diagnosis

POD_NAME=$1
NAMESPACE=${2:-default}

echo "=== ImagePull Diagnosis Report ==="

# 1. Get image information
echo "=== Container Images ==="
kubectl get pod $POD_NAME -n $NAMESPACE -o jsonpath='{range .spec.containers[*]}{.name}: {.image}{"\n"}{end}'
kubectl get pod $POD_NAME -n $NAMESPACE -o jsonpath='{range .spec.initContainers[*]}{.name}(init): {.image}{"\n"}{end}'

# 2. Check imagePullSecrets
echo -e "\n=== ImagePullSecrets ==="
SECRETS=$(kubectl get pod $POD_NAME -n $NAMESPACE -o jsonpath='{.spec.imagePullSecrets[*].name}')
if [ -z "$SECRETS" ]; then
  echo "No imagePullSecrets configured"
else
  for secret in $SECRETS; do
    echo "Secret: $secret"
    kubectl get secret $secret -n $NAMESPACE -o jsonpath='{.data.\.dockerconfigjson}' | base64 -d | jq '.auths | keys' 2>/dev/null || echo "Cannot parse Secret"
  done
fi

# 3. Events
echo -e "\n=== Pod Events ==="
kubectl get events -n $NAMESPACE --field-selector involvedObject.name=$POD_NAME | grep -i "pull|image"

# 4. Images on node
NODE=$(kubectl get pod $POD_NAME -n $NAMESPACE -o jsonpath='{.spec.nodeName}')
if [ -n "$NODE" ]; then
  echo -e "\n=== Images on Node $NODE ==="
  kubectl debug node/$NODE -it --image=busybox -- crictl images 2>/dev/null | head -20
fi

```

### Pod Network Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **Pod Cannot Access Service** | kube-proxy issue | `kubectl exec <pod> -- nslookup kubernetes` | v1.29 IPVS enhancement | Check CoreDNS, kube-proxy status | Monitor DNS resolution latency |
| **Pod-to-Pod Network Unavailable** | CNI issue | `kubectl exec <pod> -- ping <pod-ip>` | v1.25 dual-stack enhancement | Check CNI Pod status, routing table | CNI health monitoring |
| **NetworkPolicy Blocking** | Inbound/outbound rules | `kubectl get networkpolicy -A` | v1.25+ enhancement | Check NetworkPolicy rules | NetworkPolicy test cases |
| **DNS Resolution Failure** | CoreDNS issue | `kubectl exec <pod> -- nslookup google.com` | v1.28 DNS caching | Check CoreDNS logs and config | Backup DNS, NodeLocal DNS Cache |
| **Cross-Node Unavailable** | Node routing/firewall | `kubectl exec <pod> -- traceroute <target-ip>` | - | Check node network, cloud security group | Network test automation |

---

<!-- chunk: Node Troubleshooting -->
## Node Troubleshooting

### Node Status Condition Interpretation

```yaml
# Node Conditions complete description
Ready:              # kubelet running normally, can accept Pod
MemoryPressure:     # Node memory pressure
DiskPressure:       # Node disk pressure
PIDPressure:        # Process ID exhaustion
NetworkUnavailable: # Node network configuration incorrect
```

### Node NotReady Deep Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **kubelet Stopped** | Process crash/resource exhaustion | `systemctl status kubelet`, `journalctl -u kubelet` | - | Check kubelet logs, restart kubelet | Monitor kubelet process, auto-recovery |
| **Node Network Disconnected** | Network issue | Check from API Server, node SSH unavailable | - | Check network connectivity, fix network | Multi-NIC redundancy, network monitoring |
| **Container Runtime Issue** | containerd/CRI-O problem | `systemctl status containerd`, `crictl info` | v1.26 containerd 1.6+ | Restart container runtime, check disk space | Runtime health monitoring |
| **Certificate Expired** | kubelet certificate expired | `openssl x509 -in /var/lib/kubelet/pki/kubelet-client-current.pem -noout -dates` | v1.27 certificate rotation GA | Regenerate certificate or configure auto-rotation | Certificate expiration alert, auto-rotation |
| **Disk Full** | Root/data partition full | `df -h`, `du -sh /var/lib/kubelet/*` | v1.26 eviction enhancement | Clean logs/images, expand disk | Disk usage monitoring and alerting |
| **Memory Exhausted** | Node OOM | `dmesg \| grep -i oom`, `free -h` | - | Restart node, evict Pod | Configure system-reserved |
| **API Server Unreachable** | Control plane issue | Node `curl -k https://api-server:6443/healthz` | - | Check API Server status, network | API Server HA deployment |
| **Time Not Synchronized** | NTP issue | `timedatectl`, `chronyc tracking` | - | Sync time, configure NTP | NTP monitoring and alerting |
| **Kernel Panic** | Kernel bug/hardware issue | `/var/log/kern.log`, `dmesg` | - | Analyze crash dump, update kernel | Kernel version management, hardware monitoring |

#### Node NotReady Diagnosis Script

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
#!/bin/bash
# node-notready-diagnose.sh - Node NotReady deep diagnosis

NODE_NAME=$1

echo "=== Node NotReady Diagnosis Report ==="
echo "Node: $NODE_NAME"

# 1. Node Conditions
echo -e "\n=== Node Conditions ==="
kubectl get node $NODE_NAME -o jsonpath='{range .status.conditions[*]}{.type}: {.status} (Reason: {.reason}, Message: {.message}){"\n"}{end}'

# 2. Node Events
echo -e "\n=== Node Events ==="
kubectl get events --field-selector involvedObject.name=$NODE_NAME,involvedObject.kind=Node --sort-by='.lastTimestamp'

# 3. Node resources
echo -e "\n=== Node Resource Allocation ==="
kubectl describe node $NODE_NAME | grep -A 10 "Allocated resources"

# 4. Pods on node
echo -e "\n=== Pod Count on Node ==="
kubectl get pods -A --field-selector spec.nodeName=$NODE_NAME --no-headers | wc -l

# 5. If can SSH to node
echo -e "\n=== Commands to Run on Node ==="
cat << 'EOF'
# 1. kubelet status
systemctl status kubelet
journalctl -u kubelet --since "30 minutes ago" --no-pager | tail -50

# 2. Container runtime
systemctl status containerd
crictl info
crictl ps -a | head -20

# 3. System resources
free -h
df -h
cat /proc/loadavg

# 4. Certificate status
openssl x509 -in /var/lib/kubelet/pki/kubelet-client-current.pem -noout -dates 2>/dev/null

# 5. Network connectivity
curl -k https://<API_SERVER>:6443/healthz
EOF
```

### Node Resource Pressure Troubleshooting

| Pressure Type | Trigger Condition | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **MemoryPressure** | memory.available < eviction-hard | `free -h`, `cat /proc/meminfo` | v1.26 eviction enhancement | Evict Pod, add memory | Configure memory.available eviction threshold |
| **DiskPressure** | nodefs.available < 10% | `df -h`, `du -sh /var/lib/*` | - | Clean logs/images/containers | Configure imagefs.available threshold |
| **PIDPressure** | pid.available < 100 | `ps aux \| wc -l`, `/proc/sys/kernel/pid_max` | v1.25+ PID limit | Clean zombie processes, restart service | Configure --pod-max-pids |

#### Resource Pressure Relief Script

> ⚠️ **🔴 Destructive Operation** — Contains irreversible commands, must satisfy change window + dual review + pre-backup + rollback plan before execution
> - `rm -rf (system/data path)`: Delete system or data files, may destroy node or lose all data

> **🔴 High-Risk Operation Warning**
>
> The following commands are irreversible or high-impact operations. Before executing, confirm:
> - Critical data and configuration have been backed up
> - Within an approved change window
> - Authorization obtained from relevant stakeholders
> - Rollback or recovery plan prepared
> - Target cluster, namespace, node/resource name are correct

``` bash
# 🔴 High risk: May cause data loss or service interruption, requires backup, change approval and rollback plan before execution
#!/bin/bash
# node-pressure-relief.sh - Node resource pressure relief

NODE_NAME=$1

echo "=== Node Resource Pressure Relief ==="

# 1. Check current pressure status
echo "=== Current Conditions ==="
kubectl get node $NODE_NAME -o jsonpath='{range .status.conditions[*]}{.type}={.status} {end}'

# 2. DiskPressure relief
echo -e "\n\n=== DiskPressure Relief Commands (Execute on Node) ==="
cat << 'EOF'
# Clean exited containers
crictl rm $(crictl ps -a -q --state exited)

# Clean unused images
crictl rmi --prune

# Clean logs (carefully)
find /var/log -name "*.log" -mtime +7 -delete

# Clean kubelet temporary files
rm -rf /var/lib/kubelet/pods/*/volumes/kubernetes.io~empty-dir/*/lost+found  # ⚠️ Delete system/data files
EOF

# 3. MemoryPressure relief
echo -e "\n=== MemoryPressure Relief ==="
echo "Evict BestEffort Pod:"
kubectl get pods -A --field-selector spec.nodeName=$NODE_NAME -o json | jq -r '.items[] | select(.status.qosClass=="BestEffort") | "\(.metadata.namespace)/\(.metadata.name)"'

# 4. PIDPressure relief
echo -e "\n=== PIDPressure Relief Commands (Execute on Node) ==="
cat << 'EOF'
# Find zombie processes
ps aux | awk '{if ($8 == "Z") print $0}'

# Find user with most processes
ps -eo user | sort | uniq -c | sort -rn | head -10
EOF
```
---

<!-- chunk: Service/Network Troubleshooting -->
## Service/Network Troubleshooting

### Service Unreachable Deep Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **ClusterIP No Response** | Endpoints empty | `kubectl get endpoints <svc>` | - | Check selector and Pod labels match | Service monitoring, automation testing |
| **Endpoints Unhealthy** | Pod readiness probe failure | `kubectl describe endpoints <svc>` | - | Fix Pod readiness probe | Probe configuration validation |
| **kube-proxy Rules Missing** | kube-proxy issue | `iptables-save \| grep <svc-ip>` or `ipvsadm -ln` | v1.29 IPVS improvement | Restart kube-proxy, check logs | kube-proxy monitoring |
| **NodePort Unavailable** | Node firewall | `curl <node-ip>:<nodeport>` | - | Check security group/firewall rules | Security group auto-configuration |
| **LoadBalancer Pending** | Cloud controller issue | `kubectl describe svc` | - | Check CCM logs, cloud API permissions | Cloud API quota monitoring |
| **ExternalName Resolution Failure** | DNS issue | `nslookup <external-name>` | - | Check external DNS config | External dependency monitoring |
| **Session Affinity Issue** | sessionAffinity config | `kubectl get svc -o yaml` | - | Configure sessionAffinity: ClientIP | Test session persistence |
| **Port Configuration Error** | targetPort mismatch | `kubectl describe svc`, `kubectl get pod -o yaml` | - | Correct targetPort config | Port configuration validation |

#### Service Diagnosis Script

``` bash
# 🟡 Medium risk: Modifies cluster/resource state, confirm target, scope and authorization before execution
#!/bin/bash
# service-diagnose.sh - Service deep diagnosis

SVC_NAME=$1
NAMESPACE=${2:-default}

echo "=== Service Diagnosis Report ==="
echo "Service: $SVC_NAME, Namespace: $NAMESPACE"

# 1. Service details
echo -e "\n=== Service Configuration ==="
kubectl get svc $SVC_NAME -n $NAMESPACE -o yaml

# 2. Endpoints
echo -e "\n=== Endpoints ==="
kubectl get endpoints $SVC_NAME -n $NAMESPACE -o yaml

# 3. Backend Pod status
echo -e "\n=== Backend Pods ==="
SELECTOR=$(kubectl get svc $SVC_NAME -n $NAMESPACE -o jsonpath='{.spec.selector}' | jq -r 'to_entries | map("\(.key)=\(.value)") | join(",")')
kubectl get pods -n $NAMESPACE -l $SELECTOR -o wide

# 4. Readiness check
echo -e "\n=== Pod Readiness Status ==="
kubectl get pods -n $NAMESPACE -l $SELECTOR -o jsonpath='{range .items[*]}{.metadata.name}: Ready={.status.conditions[?(@.type=="Ready")].status}{"\n"}{end}'

# 5. From test Pod connectivity test
echo -e "\n=== Connectivity Test Command ==="
SVC_IP=$(kubectl get svc $SVC_NAME -n $NAMESPACE -o jsonpath='{.spec.clusterIP}')
SVC_PORT=$(kubectl get svc $SVC_NAME -n $NAMESPACE -o jsonpath='{.spec.ports[0].port}')
echo "kubectl run test-conn --rm -it --image=curlimages/curl --restart=Never -- curl -v http://$SVC_IP:$SVC_PORT"

```

### DNS Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **DNS Resolution Timeout** | CoreDNS overload/Pod issue | `kubectl exec <pod> -- nslookup kubernetes` | v1.28 DNS caching enhancement | Scale CoreDNS, check load | NodeLocal DNS Cache |
| **Resolution Error Domain Name** | CoreDNS configuration error | `kubectl get cm coredns -n kube-system -o yaml` | - | Check Corefile config | Configuration change audit |
| **External Domain Resolution Failure** | Upstream DNS issue | `kubectl exec <pod> -- nslookup google.com` | - | Check upstream DNS config | Configure backup upstream DNS |
| **Intermittent Failure** | CoreDNS Pod restart | `kubectl get pods -n kube-system -l k8s-app=kube-dns` | - | Check CoreDNS resources, OOM | Reasonable resource limit config |
| **ndots Configuration Issue** | Too many search domains | Pod /etc/resolv.conf | - | Adjust dnsConfig.options | Custom dnsPolicy |
| **Search Domain Issue** | FQDN vs short name | `kubectl exec <pod> -- cat /etc/resolv.conf` | - | Use FQDN or adjust search domain | Application use FQDN |

#### DNS Diagnosis Script

``` bash
# 🟡 Medium risk: Modifies cluster/resource state, confirm target, scope and authorization before execution
#!/bin/bash
# dns-diagnose.sh - DNS deep diagnosis

echo "=== DNS Diagnosis Report ==="

# 1. CoreDNS Pod status
echo "=== CoreDNS Pod Status ==="
kubectl get pods -n kube-system -l k8s-app=kube-dns -o wide

# 2. CoreDNS resource usage
echo -e "\n=== CoreDNS Resource Usage ==="
kubectl top pods -n kube-system -l k8s-app=kube-dns 2>/dev/null || echo "Metrics Server not installed"

# 3. CoreDNS logs
echo -e "\n=== CoreDNS Recent Logs ==="
kubectl logs -n kube-system -l k8s-app=kube-dns --tail=30

# 4. Corefile configuration
echo -e "\n=== Corefile Configuration ==="
kubectl get cm coredns -n kube-system -o jsonpath='{.data.Corefile}'

# 5. DNS Service
echo -e "\n=== kube-dns Service ==="
kubectl get svc kube-dns -n kube-system -o yaml

# 6. Test DNS resolution
echo -e "\n=== DNS Resolution Test Commands ==="
cat << 'EOF'
# Cluster internal resolution test
kubectl run dnstest --rm -it --image=busybox:1.36 --restart=Never -- nslookup kubernetes.default

# External domain resolution test
kubectl run dnstest --rm -it --image=busybox:1.36 --restart=Never -- nslookup google.com

# Detailed DNS query
kubectl run dnstest --rm -it --image=tutum/dnsutils --restart=Never -- dig kubernetes.default.svc.cluster.local
EOF
```

### NetworkPolicy Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **Inbound Traffic Blocked** | Ingress rule restriction | `kubectl get networkpolicy -n <ns> -o yaml` | v1.25+ enhancement | Add allowed ingress rules | NetworkPolicy testing |
| **Outbound Traffic Blocked** | Egress rule restriction | Same as above | - | Add allowed egress rules | Gradually tighten policy |
| **DNS Blocked** | kube-dns not allowed | Check for DNS egress rules | - | Add egress rule to kube-dns | Default allow DNS |
| **CNI Not Supported** | Using unsupported CNI | Check CNI type | - | Use Calico/Cilium etc. supported CNI | Consider NetworkPolicy at selection |

```yaml
# Allow DNS NetworkPolicy template
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-dns
spec:
  podSelector: {}
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: kube-system
    ports:
    - protocol: UDP
      port: 53
    - protocol: TCP
      port: 53
  policyTypes:
  - Egress
```

---

<!-- chunk: Storage Troubleshooting -->
## Storage Troubleshooting

### PVC/PV Issue Deep Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **PVC Pending** | No matching PV/StorageClass issue | `kubectl describe pvc <name>` | v1.29 CSI enhancement | Check StorageClass, create PV | Configure default StorageClass |
| **PVC Pending - WaitForFirstConsumer** | Delayed binding waiting for scheduling | `kubectl describe pvc` | - | Create Pod using that PVC | Understand VolumeBindingMode |
| **PV Mount Failure** | CSI driver issue | `kubectl describe pod`, CSI controller logs | v1.27 CSI enhancement | Check CSI driver Pod status | CSI driver health monitoring |
| **Mount Permission Issue** | fsGroup/securityContext | `kubectl logs <pod>`, mount error | - | Configure correct fsGroup | Standardize securityContext |
| **Multi-Pod Mount Conflict** | RWO access mode limit | `kubectl describe pv` | - | Use RWX storage or StatefulSet | Clarify AccessMode requirement |
| **Volume Expansion Failure** | StorageClass doesn't support expansion | `kubectl describe pvc` | v1.27 expansion enhancement | Use StorageClass supporting expansion | Configure allowVolumeExpansion |
| **Snapshot Creation Failure** | VolumeSnapshotClass config | `kubectl describe volumesnapshot` | v1.27 snapshot GA | Check VolumeSnapshotClass | Snapshot policy testing |
| **PV Reclamation Issue** | Reclaim policy is Retain | `kubectl get pv` | - | Manual cleanup or modify reclaim policy | Understand Reclaim Policy |

#### Storage Diagnosis Script

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
#!/bin/bash
# storage-diagnose.sh - Storage deep diagnosis

echo "=== Storage Diagnosis Report ==="

# 1. StorageClass
echo "=== StorageClasses ==="
kubectl get sc -o wide

# 2. Default StorageClass
echo -e "\n=== Default StorageClass ==="
kubectl get sc -o jsonpath='{range .items[?(@.metadata.annotations.storageclass\.kubernetes\.io/is-default-class=="true")]}{.metadata.name}{"\n"}{end}'

# 3. Problem PVC
echo -e "\n=== Unbound PVCs ==="
kubectl get pvc -A | grep -v Bound

# 4. Problem PV
echo -e "\n=== Released/Failed PVs ==="
kubectl get pv | grep -E "Released|Failed"

# 5. CSI driver status
echo -e "\n=== CSI Driver Pods ==="
kubectl get pods -A | grep -E "csi|provisioner|attacher"

# 6. CSI node status
echo -e "\n=== CSINode ==="
kubectl get csinodes -o wide

# Specific PVC diagnosis
if [ -n "$1" ]; then
  PVC_NAME=$1
  NAMESPACE=${2:-default}
  echo -e "\n=== PVC Details: $PVC_NAME ==="
  kubectl describe pvc $PVC_NAME -n $NAMESPACE
  
  # Pods using that PVC
  echo -e "\n=== Pods Using that PVC ==="
  kubectl get pods -n $NAMESPACE -o json | jq -r ".items[] | select(.spec.volumes[]?.persistentVolumeClaim.claimName==\"$PVC_NAME\") | .metadata.name"
fi
```

### CSI Driver Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **provisioner Pod Abnormal** | Resource insufficient/configuration error | `kubectl logs <csi-provisioner>` | v1.29 CSI enhancement | Check provisioner logs | Provisioner monitoring |
| **attacher Timeout** | Cloud API issue | `kubectl logs <csi-attacher>` | - | Check cloud API permissions/quota | Cloud API monitoring |
| **node Driver Issue** | CSI driver abnormal on node | `kubectl logs <csi-node> -c <driver>` | - | Restart CSI driver Pod | DaemonSet health monitoring |
| **Mount Point Leak** | Not unmounted properly | Mount `\| grep <pv>` on node | - | Manual umount, cleanup | Proper Pod deletion handling |

---

<!-- chunk: Control Plane Troubleshooting -->
## Control Plane Troubleshooting

### API Server Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **API Server 5xx Error** | etcd issue/overload | `kubectl get --raw /healthz/etcd` | v1.29 audit enhancement | Check etcd health, increase rate limit | API Server HA, APF rate limit |
| **Request Timeout** | API Server overload | `kubectl logs kube-apiserver` | - | Check load, scale up, APF config | Reasonable APF config |
| **Authentication Failure** | Certificate expired/token invalid | Check kubeconfig, certificate expiry | v1.27 certificate rotation GA | Update certificate/token | Certificate auto-rotation |
| **Authorization Failure** | RBAC config issue | `kubectl auth can-i --as <user> ...` | - | Check ClusterRole/RoleBinding | RBAC audit |
| **Admission Control Failure** | Webhook issue | `kubectl logs`, Webhook logs | - | Check Webhook availability | Webhook HA deployment |
| **Rate Limit (429)** | APF rate limiting | Prometheus `apiserver_flowcontrol*` metrics | v1.29 APF enhancement | Adjust FlowSchema/PriorityLevel | Monitor APF queue |
| **Audit Log Too Large** | Audit policy issue | Check audit policy, disk usage | v1.29 audit enhancement | Optimize audit policy | Log rotation, external storage |

#### API Server Diagnosis Script

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
#!/bin/bash
# apiserver-diagnose.sh - API Server deep diagnosis

echo "=== API Server Diagnosis Report ==="

# 1. Health check
echo "=== Health Check ==="
kubectl get --raw='/healthz?verbose' 2>/dev/null | grep -v "^+" || kubectl get --raw='/healthz'

# 2. Readiness check
echo -e "\n=== Readiness Check ==="
kubectl get --raw='/readyz?verbose' 2>/dev/null | grep -v "^+" || kubectl get --raw='/readyz'

# 3. API Server Pod status
echo -e "\n=== API Server Pod ==="
kubectl get pods -n kube-system -l component=kube-apiserver -o wide

# 4. API Server logs (if accessible)
echo -e "\n=== API Server Recent Error Logs ==="
kubectl logs -n kube-system -l component=kube-apiserver --tail=50 2>/dev/null | grep -iE "error|failed|timeout" || echo "Cannot access logs"

# 5. APF status
echo -e "\n=== APF FlowSchemas ==="
kubectl get flowschemas

echo -e "\n=== APF PriorityLevelConfigurations ==="
kubectl get prioritylevelconfigurations

# 6. API resource version
echo -e "\n=== API Resources ==="
kubectl api-resources --verbs=list --namespaced=false | head -20
```

### etcd Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **etcd Storage Full** | Data growth/compaction failure | `etcdctl endpoint status --write-out=table` | - | Compact+defrag, increase quota | Regular compaction, storage monitoring |
| **Leader Frequent Switching** | Network issue/slow disk | `etcdctl endpoint status`, etcd logs | - | Check network latency, use SSD | Dedicated etcd nodes, network optimization |
| **Cluster Unhealthy** | Member disconnected | `etcdctl member list`, `etcdctl endpoint health` | - | Check member status, recover disconnected node | 3/5 node high availability |
| **Performance Degradation** | Too many requests/slow disk | Prometheus etcd metrics | - | Optimize requests, use fast disk | SSD, dedicated disk |
| **Data Inconsistency** | Split-brain/recovery issue | Check logs on each node | - | Recover from healthy member | Regular backup |
| **Snapshot Failure** | Disk space/permission | Check snapshot command output | - | Ensure disk space, check permission | Automated backup script |

#### etcd Diagnosis Script

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
#!/bin/bash
# etcd-diagnose.sh - etcd deep diagnosis

echo "=== etcd Diagnosis Report ==="

# Must be executed on etcd node or with etcd access

# 1. Cluster status
echo "=== Cluster Status ==="
ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  endpoint status --write-out=table

# 2. Cluster health
echo -e "\n=== Cluster Health ==="
ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  endpoint health --write-out=table

# 3. Member list
echo -e "\n=== Member List ==="
ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  member list --write-out=table

# 4. Database size
echo -e "\n=== Database Size ==="
ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  endpoint status --write-out=json | jq '.[].Status.dbSize'

# 5. Alarms
echo -e "\n=== etcd Alarms ==="
ETCDCTL_API=3 etcdctl --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key \
  alarm list
```

### Controller Manager Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **Controller Not Working** | Leader election failure | `kubectl get lease -n kube-system` | - | Check leader election, restart | HA deployment |
| **Deployment Not Updating** | Deployment controller issue | `kubectl logs kube-controller-manager` | - | Check controller logs | Controller monitoring |
| **GC Not Executing** | GC controller issue | Check for orphan resources | - | Manual cleanup, check GC setting | GC monitoring |
| **Work Queue Backlog** | Too many requests | Prometheus `workqueue_depth` | - | Increase concurrency | Queue depth alerts |

---

<!-- chunk: Scheduler Troubleshooting -->
## Scheduler Troubleshooting

### Scheduling Failure Deep Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **0/N nodes available** | Insufficient resources | `kubectl describe pod`, node resources | - | Scale up nodes, adjust resource request | Cluster Autoscaler |
| **node(s) had taint** | Taint not tolerated | `kubectl get nodes -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.taints}{"\n"}{end}'` | - | Add Toleration or remove Taint | Taint policy documentation |
| **node(s) didn't match selector** | nodeSelector mismatch | `kubectl get nodes --show-labels` | - | Check node labels | Use nodeAffinity |
| **pod affinity/anti-affinity** | Affinity cannot be satisfied | `kubectl describe pod` | v1.26 topology enhancement | Adjust affinity rules | Use soft affinity |
| **volume node affinity** | Storage topology limit | `kubectl describe pv` | - | Check volume's nodeAffinity | Understand storage topology |
| **PodTopologySpread** | Topology spread limit | `kubectl describe pod` | v1.27 enhancement | Adjust maxSkew or whenUnsatisfiable | Reasonable topology constraint |
| **Scheduler Overload** | Scheduling delay high | `kubectl logs kube-scheduler` | v1.25 framework optimization | Check scheduler load | Scheduler monitoring |

#### Scheduler Diagnosis Script

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
#!/bin/bash
# scheduler-diagnose.sh - Scheduler deep diagnosis

POD_NAME=$1
NAMESPACE=${2:-default}

echo "=== Scheduler Diagnosis Report ==="
echo "Pod: $POD_NAME"

# 1. Pod scheduling requirement
echo "=== Pod Scheduling Constraints ==="
kubectl get pod $POD_NAME -n $NAMESPACE -o jsonpath='
nodeSelector: {.spec.nodeSelector}
nodeName: {.spec.nodeName}
affinity: {.spec.affinity}
tolerations: {.spec.tolerations}
topologySpreadConstraints: {.spec.topologySpreadConstraints}
'

# 2. Pod resource request
echo -e "\n\n=== Pod Resource Request ==="
kubectl get pod $POD_NAME -n $NAMESPACE -o jsonpath='{range .spec.containers[*]}Container: {.name}
  CPU Request: {.resources.requests.cpu}
  Memory Request: {.resources.requests.memory}
{end}'

# 3. Node allocatable resources
echo -e "\n=== Node Allocatable Resources ==="
kubectl get nodes -o custom-columns=NAME:.metadata.name,CPU:.status.allocatable.cpu,MEMORY:.status.allocatable.memory,PODS:.status.allocatable.pods

# 4. Node Taints
echo -e "\n=== Node Taints ==="
kubectl get nodes -o custom-columns=NAME:.metadata.name,TAINTS:.spec.taints

# 5. Scheduler logs
echo -e "\n=== Scheduler Related Logs ==="
kubectl logs -n kube-system -l component=kube-scheduler --tail=20 2>/dev/null | grep -i "$POD_NAME" || echo "No related logs found"

# 6. Simulate scheduling
echo -e "\n=== Schedulable Node Analysis ==="
echo "Nodes matching nodeSelector:"
if [ "$(kubectl get pod $POD_NAME -n $NAMESPACE -o jsonpath='{.spec.nodeSelector}')" != "" ]; then
  SELECTOR=$(kubectl get pod $POD_NAME -n $NAMESPACE -o jsonpath='{.spec.nodeSelector}' | jq -r 'to_entries | map("\(.key)=\(.value)") | join(",")')
  kubectl get nodes -l $SELECTOR --no-headers | wc -l
else
  echo "No nodeSelector restriction"
fi
```

---

<!-- chunk: Application Deployment Troubleshooting -->
## Application Deployment Troubleshooting

### Deployment Rolling Update Issues

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **Update Stuck** | New Pod cannot become ready | `kubectl rollout status deployment/<name>` | - | Check new Pod status, rollback | Readiness probe config |
| **Update Timeout** | progressDeadlineSeconds | `kubectl describe deployment` | - | Increase timeout or fix issue | Reasonable timeout setting |
| **Rollback Failure** | Historical version unavailable | `kubectl rollout history deployment/<name>` | - | Check revisionHistoryLimit | Retain sufficient history versions |
| **RollingUpdate Too Slow** | maxUnavailable/maxSurge | `kubectl get deployment -o yaml` | - | Adjust rolling update strategy | Set strategy based on SLA |
| **PDB Blocks Update** | minAvailable/maxUnavailable | `kubectl get pdb` | v1.27 unhealthyPodEvictionPolicy | Adjust PDB config | Understand PDB impact |

#### Deployment Diagnosis Script

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
#!/bin/bash
# deployment-diagnose.sh - Deployment deep diagnosis

DEPLOY_NAME=$1
NAMESPACE=${2:-default}

echo "=== Deployment Diagnosis Report ==="
echo "Deployment: $DEPLOY_NAME"

# 1. Deployment status
echo "=== Deployment Status ==="
kubectl get deployment $DEPLOY_NAME -n $NAMESPACE -o wide

# 2. Rollout status
echo -e "\n=== Rollout Status ==="
kubectl rollout status deployment/$DEPLOY_NAME -n $NAMESPACE --timeout=5s 2>&1

# 3. ReplicaSets
echo -e "\n=== ReplicaSets ==="
kubectl get rs -n $NAMESPACE -l $(kubectl get deployment $DEPLOY_NAME -n $NAMESPACE -o jsonpath='{.spec.selector.matchLabels}' | jq -r 'to_entries | map("\(.key)=\(.value)") | join(",")')

# 4. Pods status
echo -e "\n=== Pods Status ==="
kubectl get pods -n $NAMESPACE -l $(kubectl get deployment $DEPLOY_NAME -n $NAMESPACE -o jsonpath='{.spec.selector.matchLabels}' | jq -r 'to_entries | map("\(.key)=\(.value)") | join(",")') -o wide

# 5. Conditions
echo -e "\n=== Deployment Conditions ==="
kubectl get deployment $DEPLOY_NAME -n $NAMESPACE -o jsonpath='{range .status.conditions[*]}{.type}: {.status} ({.reason}: {.message}){"\n"}{end}'

# 6. History versions
echo -e "\n=== History Versions ==="
kubectl rollout history deployment/$DEPLOY_NAME -n $NAMESPACE

# 7. Related Events
echo -e "\n=== Events ==="
kubectl get events -n $NAMESPACE --field-selector involvedObject.name=$DEPLOY_NAME --sort-by='.lastTimestamp'
```

### HPA Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **HPA Not Scaling** | Metrics unavailable | `kubectl describe hpa`, `kubectl top pods` | v1.23 HPA v2 GA | Check Metrics Server | Metrics monitoring |
| **Targets Unknown** | Custom metric issue | `kubectl get --raw "/apis/metrics.k8s.io/v1beta1/pods"` | v1.25 ContainerResource | Check metrics-adapter | Metric availability test |
| **Scaling Oscillation** | Threshold setting issue | HPA Events | - | Adjust stabilizationWindowSeconds | Reasonable scaling strategy |
| **Reached Upper Limit** | maxReplicas limit | `kubectl describe hpa` | - | Adjust maxReplicas or optimize app | Capacity planning |

---

<!-- chunk: Security/Permission Troubleshooting -->
## Security/Permission Troubleshooting

### RBAC Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **Forbidden Error** | Insufficient permission | `kubectl auth can-i <verb> <resource> --as <user>` | - | Add appropriate RBAC rules | Least privilege principle |
| **ServiceAccount No Permission** | SA not bound to role | `kubectl get rolebinding,clusterrolebinding -A \| grep <sa>` | - | Create RoleBinding | SA permission audit |
| **Cross-namespace Access Failure** | Need ClusterRole | Check Role vs ClusterRole | - | Use ClusterRole | Understand Role scope |
| **API Group Error** | Resource apiGroups config error | `kubectl api-resources` check apiGroup | - | Correct apiGroups config | Use correct apiGroups |

#### RBAC Diagnosis Script

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
#!/bin/bash
# rbac-diagnose.sh - RBAC deep diagnosis

USER_OR_SA=$1
NAMESPACE=${2:-default}

echo "=== RBAC Diagnosis Report ==="
echo "Subject: $USER_OR_SA"

# 1. Check if ServiceAccount
if $USER_OR_SA == *":"*; then
  SA_NS=$(echo $USER_OR_SA | cut -d: -f1)
  SA_NAME=$(echo $USER_OR_SA | cut -d: -f2)
  echo -e "\n=== ServiceAccount: $SA_NAME in $SA_NS ==="
  kubectl get sa $SA_NAME -n $SA_NS
fi

# 2. Related RoleBindings
echo -e "\n=== RoleBindings ==="
kubectl get rolebindings -A -o json | jq -r ".items[] | select(.subjects[]?.name==\"$USER_OR_SA\" or .subjects[]?.name==\"system:serviceaccount:$NAMESPACE:$USER_OR_SA\") | \"\(.metadata.namespace)/\(.metadata.name) -> \(.roleRef.kind)/\(.roleRef.name)\""

# 3. Related ClusterRoleBindings
echo -e "\n=== ClusterRoleBindings ==="
kubectl get clusterrolebindings -o json | jq -r ".items[] | select(.subjects[]?.name==\"$USER_OR_SA\" or .subjects[]?.name==\"system:serviceaccount:$NAMESPACE:$USER_OR_SA\") | \"\(.metadata.name) -> \(.roleRef.kind)/\(.roleRef.name)\""

# 4. Permission test
echo -e "\n=== Permission Test ==="
SUBJECT="--as=system:serviceaccount:$NAMESPACE:$USER_OR_SA"
for resource in pods deployments services configmaps secrets; do
  for verb in get list create delete; do
    result=$(kubectl auth can-i $verb $resource -n $NAMESPACE $SUBJECT 2>/dev/null)
    echo "$verb $resource: $result"
  done
done
```

### Pod Security Standards Troubleshooting

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **Pod Rejected** | PSS violation | `kubectl describe pod`, Events | v1.25 PSS GA | Check namespace PSS labels | Gradually tighten PSS level |
| **privileged Container Rejected** | baseline/restricted restriction | Check securityContext config | - | Adjust securityContext or PSS level | Application security hardening |
| **hostPath Rejected** | restricted level restriction | Check volumes config | - | Use alternative or adjust PSS | Avoid hostPath |
| **runAsRoot Rejected** | restricted level restriction | Check runAsNonRoot config | - | Run as non-root user | Image build best practices |

---

<!-- chunk: Performance Issue Troubleshooting -->
## Performance Issue Troubleshooting

### Cluster Performance Issue Matrix

| Performance Symptom | Possible Cause | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **API Latency High** | etcd slow/API Server overload | Prometheus `apiserver_request_duration_seconds` | v1.29 APF enhancement | Optimize etcd, extend API Server | API Server monitoring |
| **Scheduling Latency High** | Scheduler overload | `scheduler_pending_pods`, `scheduler_scheduling_duration_seconds` | v1.25 framework optimization | Check scheduler performance | Scheduler monitoring |
| **Pod Startup Slow** | Image pull/mount slow | Pod Events | - | Image prewarming, local storage | Image preload |
| **DNS Resolution Slow** | CoreDNS overload | CoreDNS metrics | v1.28 DNS caching | Scale CoreDNS, NodeLocal DNS | DNS monitoring |
| **Network Latency High** | CNI issue | Network latency metrics | - | Optimize CNI config | Network performance baseline |
| **Storage IO Slow** | CSI/backend storage issue | iostat, storage metrics | - | Optimize storage config | Storage performance monitoring |

#### Performance Diagnosis Script

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
#!/bin/bash
# performance-diagnose.sh - Performance issue diagnosis

echo "=== Cluster Performance Diagnosis Report ==="

# 1. API Server latency (requires Prometheus)
echo "=== API Server Latency ==="
echo "Check Prometheus metric: apiserver_request_duration_seconds_bucket"

# 2. Node load
echo -e "\n=== Node Load ==="
kubectl top nodes 2>/dev/null || echo "Metrics Server not installed"

# 3. High resource consumption Pod
echo -e "\n=== Top 10 CPU Usage Pods ==="
kubectl top pods -A --sort-by=cpu 2>/dev/null | head -11

echo -e "\n=== Top 10 Memory Usage Pods ==="
kubectl top pods -A --sort-by=memory 2>/dev/null | head -11

# 4. Pending Pod
echo -e "\n=== Pending Pods ==="
kubectl get pods -A --field-selector=status.phase=Pending

# 5. High restart count Pod
echo -e "\n=== High Restart Count Pods ==="
kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"\t"}{.metadata.name}{"\t"}{range .status.containerStatuses[*]}{.restartCount}{"\t"}{end}{"\n"}{end}' | awk -F'\t' '$3 > 5 {print $0}' | sort -t$'\t' -k3 -nr | head -10

# 6. Event frequency
echo -e "\n=== High-Frequency Events in Last 1 Hour ==="
kubectl get events -A --sort-by='.count' | tail -20
```

---

<!-- chunk: Cluster Upgrade Troubleshooting -->
## Cluster Upgrade Troubleshooting

### Upgrade Issue Matrix

| Problem Symptom | Root Cause Classification | Diagnostic Command | Version Feature | Solution | Production Prevention |
|:---|:---|:---|:---|:---|:---|
| **Control Plane Upgrade Failure** | kubeadm/component issue | `kubeadm upgrade plan`, component logs | - | Check compatibility, gradual upgrade | Pre-upgrade backup |
| **Node Upgrade Failure** | kubelet/runtime issue | `systemctl status kubelet`, `journalctl -u kubelet` | - | Check kubelet logs | Node upgrade SOP |
| **API Version Deprecated** | Using deprecated API | `kubectl deprecations` (third-party tool) | Version-specific | Update resource manifest | API compatibility check |
| **Webhook Incompatible** | Admission controller version issue | Check ValidatingWebhookConfiguration | - | Upgrade Webhook component | Webhook compatibility test |
| **CNI Incompatible** | CNI version mismatch | CNI Pod logs | - | Upgrade CNI | CNI compatibility matrix |
| **Storage Driver Issue** | CSI version incompatible | CSI Pod logs | - | Upgrade CSI driver | CSI compatibility check |

#### Pre-Upgrade Check Script

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
#!/bin/bash
# upgrade-precheck.sh - Pre-upgrade check

TARGET_VERSION=${1:-"v1.32"}

echo "=== Pre-Upgrade Check Report ==="
echo "Target Version: $TARGET_VERSION"

# 1. Current version
echo -e "\n=== Current Cluster Version ==="
kubectl version --short 2>/dev/null || kubectl version

# 2. Node version
echo -e "\n=== Node Version ==="
kubectl get nodes -o custom-columns=NAME:.metadata.name,VERSION:.status.nodeInfo.kubeletVersion

# 3. etcd backup status
echo -e "\n=== etcd Backup Check ==="
echo "Please confirm etcd snapshot backup has been performed"

# 4. Control plane health
echo -e "\n=== Control Plane Health ==="
kubectl get pods -n kube-system -l tier=control-plane

# 5. Deprecated API check
echo -e "\n=== Deprecated API Check ==="
echo "Recommend using kubectl deprecations or pluto tool to check deprecated APIs"

# 6. PDB check
echo -e "\n=== PodDisruptionBudget ==="
kubectl get pdb -A

# 7. Node evictability
echo -e "\n=== Node Pod Distribution ==="
for node in $(kubectl get nodes -o name | cut -d'/' -f2); do
  count=$(kubectl get pods -A --field-selector spec.nodeName=$node --no-headers | wc -l)
  echo "$node: $count pods"
done
```

---

<!-- chunk: Version-Specific Known Issues -->
## Version-Specific Known Issues

### v1.32 Known Issues and Notes

| Issue Type | Description | Impact Scope | Solution |
|:---|:---|:---|:---|
| **Feature Gate Change** | Some Alpha features default disabled change | Clusters using related features | Check Feature Gate config |
| **API Deprecated** | flowcontrol.apiserver.k8s.io/v1beta3 deprecated | APF config | Migrate to v1 |

### v1.31 Known Issues and Notes

| Issue Type | Description | Impact Scope | Solution |
|:---|:---|:---|:---|
| **Kubelet Memory Management** | Memory manager enhancement | Memory-sensitive applications | Test memory limit behavior |
| **AppArmor GA** | AppArmor field format changed | Pod using AppArmor | Update config format |

### v1.30 Known Issues and Notes

| Issue Type | Description | Impact Scope | Solution |
|:---|:---|:---|:---|
| **VolumeAttributesClass** | Storage parameter dynamic adjustment Beta | Advanced storage scenarios | Test usage |
| **Pod Scheduling Ready** | Pod scheduling readiness condition enhancement | Scheduling control scenarios | Understand new scheduling behavior |

### v1.29 Known Issues and Notes

| Issue Type | Description | Impact Scope | Solution |
|:---|:---|:---|:---|
| **nftables Support** | kube-proxy nftables mode Beta | Network proxy | Test nftables mode |
| **APF Enhancement** | Flow control API v1 official release | API rate limiting config | Migrate FlowSchema config |

### v1.28 Known Issues and Notes

| Issue Type | Description | Impact Scope | Solution |
|:---|:---|:---|:---|
| **Native Sidecar** | Native Sidecar container support | Sidecar application scenarios | Test restartPolicy: Always |
| **ValidatingAdmissionPolicy** | CEL validation policy Beta | Admission control | Test migration plan |

### v1.27 Known Issues and Notes

| Issue Type | Description | Impact Scope | Solution |
|:---|:---|:---|:---|
| **In-place Pod Adjustment** | Pod resources can be dynamically adjusted (Alpha) | Resource management | Enable Feature Gate to test |
| **Certificate Rotation GA** | kubelet certificate auto-rotation | Certificate management | Confirm auto-rotation enabled |

### v1.26 Known Issues and Notes

| Issue Type | Description | Impact Scope | Solution |
|:---|:---|:---|:---|
| **Graceful Shutdown GA** | Node graceful shutdown official release | Node maintenance | Configure shutdownGracePeriod |
| **Scheduler Optimization** | Scheduler performance improvement | Large-scale cluster | Leverage scheduler improvement |

### v1.25 Known Issues and Notes

| Issue Type | Description | Impact Scope | Solution |
|:---|:---|:---|:---|
| **PSP Removed** | PodSecurityPolicy completely removed | Security policy | Migrate to PSS |
| **Ephemeral Containers GA** | Ephemeral containers official release | Pod debugging | Use kubectl debug |
| **CronJob Timezone** | Timezone support official release | Scheduled tasks | Configure .spec.timeZone |

---

<!-- chunk: Production-Grade Diagnostic Toolset -->
## Production-Grade Diagnostic Toolset

### Comprehensive Diagnosis Script

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
#!/bin/bash
# k8s-full-diagnose.sh - Kubernetes production environment comprehensive diagnosis

set -e

NAMESPACE=${1:-""}
OUTPUT_DIR="/tmp/k8s-diagnose-$(date +%Y%m%d-%H%M%S)"
mkdir -p $OUTPUT_DIR

echo "=== Kubernetes Comprehensive Diagnosis Report ==="
echo "Output Directory: $OUTPUT_DIR"
echo "Start Time: $(date)"

# 1. Cluster basic information
echo -e "\n[1/10] Collecting cluster basic information..."
{
  echo "=== Cluster Info ==="
  kubectl cluster-info
  echo -e "\n=== Server Version ==="
  kubectl version --short 2>/dev/null || kubectl version
  echo -e "\n=== API Resources ==="
  kubectl api-resources --verbs=list --no-headers | wc -l
} > $OUTPUT_DIR/01-cluster-info.txt

# 2. Node status
echo "[2/10] Collecting node status..."
{
  echo "=== Nodes ==="
  kubectl get nodes -o wide
  echo -e "\n=== Node Conditions ==="
  kubectl get nodes -o custom-columns=NAME:.metadata.name,READY:.status.conditions[-1].status,PRESSURE:.status.conditions[0].status,.status.conditions[1].status,.status.conditions[2].status
  echo -e "\n=== Node Resources ==="
  kubectl top nodes 2>/dev/null || echo "Metrics Server not installed"
} > $OUTPUT_DIR/02-nodes.txt

# 3. Control plane
echo "[3/10] Collecting control plane status..."
{
  echo "=== Control Plane Pods ==="
  kubectl get pods -n kube-system -l tier=control-plane -o wide
  echo -e "\n=== Health Check ==="
  kubectl get --raw='/healthz?verbose' 2>/dev/null | head -30 || kubectl get --raw='/healthz'
  echo -e "\n=== Readiness Check ==="
  kubectl get --raw='/readyz?verbose' 2>/dev/null | head -30 || kubectl get --raw='/readyz'
} > $OUTPUT_DIR/03-control-plane.txt

# 4. Problem Pods
echo "[4/10] Collecting problem Pods..."
{
  echo "=== Non-Running Pods ==="
  kubectl get pods -A --field-selector=status.phase!=Running,status.phase!=Succeeded -o wide
  echo -e "\n=== High Restart Pods ==="
  kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"\t"}{.metadata.name}{"\t"}{range .status.containerStatuses[*]}{.restartCount}{"\t"}{end}{"\n"}{end}' | awk -F'\t' '$3 > 3 {print $0}' | sort -t$'\t' -k3 -nr | head -20
} > $OUTPUT_DIR/04-problem-pods.txt

# 5. Events
echo "[5/10] Collecting events..."
{
  echo "=== Recent Warning Events ==="
  kubectl get events -A --field-selector type=Warning --sort-by='.lastTimestamp' | tail -50
} > $OUTPUT_DIR/05-events.txt

# 6. Network
echo "[6/10] Collecting network status..."
{
  echo "=== CoreDNS ==="
  kubectl get pods -n kube-system -l k8s-app=kube-dns -o wide
  echo -e "\n=== Services (ClusterIP Issues) ==="
  kubectl get svc -A | grep -v ClusterIP | grep -v TYPE
  echo -e "\n=== Ingress ==="
  kubectl get ingress -A 2>/dev/null || echo "No Ingress resource"
} > $OUTPUT_DIR/06-network.txt

# 7. Storage
echo "[7/10] Collecting storage status..."
{
  echo "=== StorageClasses ==="
  kubectl get sc
  echo -e "\n=== Unbound PVCs ==="
  kubectl get pvc -A | grep -v Bound
  echo -e "\n=== Released/Failed PVs ==="
  kubectl get pv | grep -E "Released|Failed"
} > $OUTPUT_DIR/07-storage.txt

# 8. Security
echo "[8/10] Collecting security config..."
{
  echo "=== Namespace PSS Labels ==="
  kubectl get ns -o custom-columns=NAME:.metadata.name,PSS:.metadata.labels.pod-security\\.kubernetes\\.io/enforce
  echo -e "\n=== ClusterRoleBindings (cluster-admin) ==="
  kubectl get clusterrolebindings -o json | jq -r '.items[] | select(.roleRef.name=="cluster-admin") | "\(.metadata.name): \(.subjects)"'
} > $OUTPUT_DIR/08-security.txt

# 9. Resource usage
echo "[9/10] Collecting resource usage..."
{
  echo "=== ResourceQuotas ==="
  kubectl get quota -A
  echo -e "\n=== LimitRanges ==="
  kubectl get limitrange -A
  echo -e "\n=== Top Pods by CPU ==="
  kubectl top pods -A --sort-by=cpu 2>/dev/null | head -20 || echo "Metrics not installed"
} > $OUTPUT_DIR/09-resources.txt

# 10. Specific namespace (if specified)
if [ -n "$NAMESPACE" ]; then
  echo "[10/10] Collecting namespace $NAMESPACE details..."
  {
    echo "=== Namespace: $NAMESPACE ==="
    kubectl get all -n $NAMESPACE -o wide
    echo -e "\n=== Events ==="
    kubectl get events -n $NAMESPACE --sort-by='.lastTimestamp'
    echo -e "\n=== Pod Logs (last 50 lines each) ==="
    for pod in $(kubectl get pods -n $NAMESPACE -o name | head -5); do
      echo "--- $pod ---"
      kubectl logs $pod -n $NAMESPACE --tail=50 2>/dev/null || echo "Cannot get logs"
    done
  } > $OUTPUT_DIR/10-namespace-$NAMESPACE.txt
else
  echo "[10/10] No namespace specified, skip detailed collection"
fi

# Package
echo -e "\n=== Diagnosis Complete ==="
echo "Report Directory: $OUTPUT_DIR"
tar -czf $OUTPUT_DIR.tar.gz -C /tmp $(basename $OUTPUT_DIR)
echo "Compressed Package: $OUTPUT_DIR.tar.gz"
echo "Completion Time: $(date)"
```

### Real-time Monitoring Script

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
#!/bin/bash
# k8s-realtime-monitor.sh - Real-time monitoring script

watch -n 5 '
echo "=== $(date) ==="
echo ""
echo "=== Node Status ==="
kubectl get nodes -o custom-columns=NAME:.metadata.name,STATUS:.status.conditions[-1].type,READY:.status.conditions[-1].status,CPU:.status.capacity.cpu,MEMORY:.status.capacity.memory

echo ""
echo "=== Problem Pods ==="
kubectl get pods -A --field-selector=status.phase!=Running,status.phase!=Succeeded --no-headers | head -10

echo ""
echo "=== Recent Events ==="
kubectl get events -A --field-selector type=Warning --sort-by=".lastTimestamp" --no-headers | tail -5
'
```

### kubectl debug Advanced Usage

``` bash
# 🟢 Low risk: Read-only/information collection, usually no side effects
# 1. Debug running Pod (ephemeral container)
kubectl debug <pod-name> -it --image=busybox --target=<container-name>

# 2. Debug node (v1.25+ GA)
kubectl debug node/<node-name> -it --image=busybox

# 3. Create Pod copy for debugging
kubectl debug <pod-name> -it --copy-to=debug-pod --container=debug --image=busybox

# 4. Debug CrashLoopBackOff Pod (modify command)
kubectl debug <pod-name> -it --copy-to=debug-pod --container=app -- sh

# 5. Use network diagnosis image
kubectl debug <pod-name> -it --image=nicolaka/netshoot --target=<container-name>
```

---

<!-- chunk: Monitoring Alert Integration -->
## Monitoring Alert Integration

### Critical Prometheus Alert Rules

```yaml
# kubernetes-troubleshooting-alerts.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: kubernetes-troubleshooting-alerts
  namespace: monitoring
spec:
  groups:
  - name: kubernetes-pod-alerts
    rules:
    # Pod abnormality alerts
    - alert: KubernetesPodCrashLooping
      expr: |
        increase(kube_pod_container_status_restarts_total[1h]) > 5
      for: 15m
      labels:
        severity: warning
      annotations:
        summary: "Pod {{ $labels.namespace }}/{{ $labels.pod }} frequent restart"
        description: "Pod restarted more than 5 times in the last 1 hour"
    
    - alert: KubernetesPodNotReady
      expr: |
        kube_pod_status_ready{condition="false"} == 1
      for: 15m
      labels:
        severity: warning
      annotations:
        summary: "Pod {{ $labels.namespace }}/{{ $labels.pod }} not ready"
        description: "Pod did not enter Ready state for 15 minutes"
    
    # Node alerts
    - alert: KubernetesNodeNotReady
      expr: |
        kube_node_status_condition{condition="Ready",status="true"} == 0
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "Node {{ $labels.node }} NotReady"
        description: "Node remained NotReady for 5 minutes"
    
    - alert: KubernetesNodeMemoryPressure
      expr: |
        kube_node_status_condition{condition="MemoryPressure",status="true"} == 1
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Node {{ $labels.node }} memory pressure"
        description: "Node is under MemoryPressure"
    
    - alert: KubernetesNodeDiskPressure
      expr: |
        kube_node_status_condition{condition="DiskPressure",status="true"} == 1
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Node {{ $labels.node }} disk pressure"
        description: "Node is under DiskPressure"
    
    # Control plane alerts
    - alert: KubernetesAPIServerLatencyHigh
      expr: |
        histogram_quantile(0.99, sum(rate(apiserver_request_duration_seconds_bucket{verb!~"WATCH|CONNECT"}[5m])) by (verb, resource, le)) > 1
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "API Server latency too high"
        description: "API request P99 latency exceeds 1 second"
    
    - alert: KubernetesAPIServerErrors
      expr: |
        sum(rate(apiserver_request_total{code=~"5.."}[5m])) / sum(rate(apiserver_request_total[5m])) > 0.01
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "API Server error rate too high"
        description: "API Server 5xx error rate exceeds 1%"
    
    # etcd alerts
    - alert: EtcdHighCommitDurations
      expr: |
        histogram_quantile(0.99, rate(etcd_disk_backend_commit_duration_seconds_bucket[5m])) > 0.25
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "etcd commit latency too high"
        description: "etcd disk commit P99 latency exceeds 250ms"
    
    - alert: EtcdInsufficientMembers
      expr: |
        count(etcd_server_has_leader) < 3
      for: 3m
      labels:
        severity: critical
      annotations:
        summary: "etcd members insufficient"
        description: "etcd cluster has fewer than 3 members"
    
    # Storage alerts
    - alert: KubernetesPVCPending
      expr: |
        kube_persistentvolumeclaim_status_phase{phase="Pending"} == 1
      for: 15m
      labels:
        severity: warning
      annotations:
        summary: "PVC {{ $labels.namespace }}/{{ $labels.persistentvolumeclaim }} Pending"
        description: "PVC remained Pending for 15 minutes"
    
    # Scheduling alerts
    - alert: KubernetesPodSchedulingFailed
      expr: |
        sum(kube_pod_status_phase{phase="Pending"}) by (namespace, pod) > 0
        and on(namespace, pod) 
        sum(kube_pod_status_scheduled{condition="false"}) by (namespace, pod) > 0
      for: 15m
      labels:
        severity: warning
      annotations:
        summary: "Pod {{ $labels.namespace }}/{{ $labels.pod }} scheduling failed"
        description: "Pod could not be scheduled for 15 minutes"
```

### Grafana Dashboard Key Panels

```json
{
  "title": "Kubernetes Troubleshooting Dashboard",
  "panels": [
    {
      "title": "Problem Pod Statistics",
      "type": "stat",
      "targets": [
        {
          "expr": "count(kube_pod_status_phase{phase=~\"Pending|Failed|Unknown\"}) or vector(0)",
          "legendFormat": "Problem Pod Count"
        }
      ]
    },
    {
      "title": "NotReady Nodes",
      "type": "stat",
      "targets": [
        {
          "expr": "count(kube_node_status_condition{condition=\"Ready\",status!=\"true\"}) or vector(0)",
          "legendFormat": "NotReady Node Count"
        }
      ]
    },
    {
      "title": "Top 10 Pod Restarts",
      "type": "table",
      "targets": [
        {
          "expr": "topk(10, sum(increase(kube_pod_container_status_restarts_total[1h])) by (namespace, pod))",
          "format": "table"
        }
      ]
    },
    {
      "title": "API Server Error Rate",
      "type": "graph",
      "targets": [
        {
          "expr": "sum(rate(apiserver_request_total{code=~\"5..\"}[5m])) / sum(rate(apiserver_request_total[5m])) * 100",
          "legendFormat": "5xx Error Rate%"
        }
      ]
    },
    {
      "title": "etcd Latency",
      "type": "graph",
      "targets": [
        {
          "expr": "histogram_quantile(0.99, rate(etcd_disk_backend_commit_duration_seconds_bucket[5m]))",
          "legendFormat": "P99 Latency"
        }
      ]
    }
  ]
}
```

---

<!-- chunk: Production SOP Process -->
## Production SOP Process

### Problem Response Flow

```
# 🟢 Low risk: Read-only/information collection, usually no side effects
┌─────────────────────────────────────────────────────────────────────────────┐
│                        Problem Response SOP Flow                            │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  1. Alert Triggered ────────────────────────────────────────────────────── │
│     │                                                                       │
│     ▼                                                                       │
│  2. Impact Assessment (P0/P1/P2/P3)                                         │
│     │  P0: Global unavailable    P1: Core function impaired               │
│     │  P2: Partial function impaired  P3: Edge function impaired          │
│     ▼                                                                       │
│  3. Initial Diagnosis (within 5 minutes)                                    │
│     │  - Cluster status: kubectl cluster-info                             │
│     │  - Node status: kubectl get nodes                                   │
│     │  - Problem Pod: kubectl get pods -A (abnormal filter)               │
│     ▼                                                                       │
│  4. Quick Recovery (prioritize service recovery)                             │
│     │  - Scale up/restart                                                  │
│     │  - Rollback                                                          │
│     │  - Traffic switch                                                    │
│     ▼                                                                       │
│  5. Root Cause Analysis (after service recovery)                            │
│     │  - Log analysis                                                      │
│     │  - Metric correlation                                               │
│     │  - Change audit                                                      │
│     ▼                                                                       │
│  6. Review and Prevention                                                    │
│     │  - Problem report                                                    │
│     │  - Monitoring supplement                                             │
│     │  - Prevention measures                                               │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘

```

### Quick Recovery Checklist

| Scenario | Quick Recovery Action | Estimated Recovery Time |
|:---|:---|:---:|
| **Single Pod Issue** | `kubectl delete pod <pod>` trigger rebuild | <1min |
| **Deployment Abnormal** | `kubectl rollout undo deployment/<name>` | <5min |
| **Node NotReady** | `kubectl drain/uncordon` or restart kubelet | 5-15min |
| **Control Plane Issue** | Restart control plane component, or switch to backup node | 5-30min |
| **etcd Issue** | Restore from backup, or remove problem member | 10-60min |
| **Global Network Issue** | Restart CNI, check config | 5-30min |
| **Storage Mount Issue** | Restart CSI driver, check backend storage | 10-30min |

### On-Duty Engineer Quick Reference

> ⚠️ **🔴 Destructive Operation** — Contains irreversible commands, must satisfy change window + dual review + pre-backup + rollback plan before execution
> - `kubectl delete pod --force`: Force delete Pod, skip graceful termination and data flush
> - `kubectl drain`: Evict all Pods from node, business traffic affected
> - `kubectl rollout undo/restart`: Trigger rolling change, affect replicas

> **🔴 High-Risk Operation Warning**
>
> The following commands are irreversible or high-impact operations. Before executing, confirm:
> - Critical data and configuration have been backed up
> - Within an approved change window
> - Authorization obtained from relevant stakeholders
> - Rollback or recovery plan prepared
> - Target cluster, namespace, node/resource name are correct

``` bash
# 🔴 High risk: May cause data loss or service interruption, requires backup, change approval and rollback plan before execution
# ========== Emergency Problem Quick Diagnosis Commands ==========

# 1. Quick check cluster status
kubectl cluster-info && kubectl get nodes && kubectl get pods -A --field-selector=status.phase!=Running,status.phase!=Succeeded | head -20

# 2. Recent critical events
kubectl get events -A --field-selector type=Warning --sort-by='.lastTimestamp' | tail -20

# 3. Control plane health
kubectl get --raw='/healthz?verbose' | grep -v "^+"

# 4. Problem Pod quick locate
kubectl get pods -A -o wide | grep -vE "Running|Completed"

# 5. High restart Pod
kubectl get pods -A -o jsonpath='{range .items[*]}{.metadata.namespace}/{.metadata.name}: {range .status.containerStatuses[*]}{.restartCount}{" "}{end}{"\n"}{end}' | awk -F': ' '$2 > 3'

# 6. Node resource pressure
kubectl describe nodes | grep -A 5 "Conditions:"

# 7. DNS quick test
kubectl run dns-test --rm -it --image=busybox:1.36 --restart=Never -- nslookup kubernetes.default

# 8. Quick rollback
kubectl rollout undo deployment/<name> -n <namespace>

# 9. Force delete stuck Pod
kubectl delete pod <pod> -n <namespace> --grace-period=0 --force  # ⚠️ Skip graceful termination, may lose data

# 10. Node maintenance
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data
kubectl uncordon <node>
```

---

**Troubleshooting Golden Rules**:
1. Look at Events first (what happened)
2. Then look at Logs (why it happened)
3. Then Describe (current state)
4. Finally Metrics (trend analysis)

**Production Environment Principles**:
- Prioritize service recovery, then analyze root cause
- Changes must be reversible
- All operations must have audit records
- Problems must be reviewed and prevented

---

**Table Bottom Mark**: Kusheet Project, Author Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian Related Documents -->
## Obsidian Related Documents

- domain-06-observability MOC
- [[domain-06-observability/README.md|Observability Domain]]
- [[domain-06-observability/00-open-source-projects-index.md|Domain-8 Observability — Open Source Project Index]]
- Kubernetes Observability Architecture System
- Metrics Monitoring System Detailed Explanation
- 03 - Logging Collection Architecture Detailed Explanation
- Distributed Tracing System
- 05 - Alert Management Strategy
- 06 - Monitoring Alert Practice and Best Practices
- 04 - Monitoring Dashboard Design and Best Practices
- 08 - Logging Audit and Compliance Management
- 05 - Events and Audit Logs Management
- [[domain-10-troubleshooting-diagnostics/topic-fta/list/apiserver-fta.md|API Server Abnormal Fault Tree Analysis]]
- [[domain-10-troubleshooting-diagnostics/topic-fta/list/backup-restore-fta.md|Backup/Recovery Abnormal Fault Tree Analysis]]
- [[domain-10-troubleshooting-diagnostics/topic-fta/list/calico-fta.md|calico FTA Tree: Calico CNI Troubleshooting]]

## Related

- [[deep-dive|#deep-dive Hub]] — tag hub

- [[kudig-prompts-catalog]]

- [[domain-06-observability/README.md|Back to index]] - [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Map Index]]

## See Also

- 23-enterprise-implementation-roadmap
- 24-observability-tool-ecosystem
- 26-troubleshooting-tools
- 27-performance-profiling-tools

```

<!-- risk-assessed -->
