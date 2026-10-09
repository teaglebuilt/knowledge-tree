---
title: eBPF Observability Tools Practical
description: 'bcc/bpftrace toolset, Pixie non-intrusive observability, Parca continuous performance profiling, and Tetragon security observation'
summary: 'bcc/bpftrace toolset, Pixie non-intrusive observability, Parca continuous performance profiling, and Tetragon security observation'
category: specialized-tech
tags:
- ebpf
- bcc
- bpftrace
- pixie
- parca
- tetragon
tier: supporting
created: '2026-07-02'
last_updated: 2026-07
difficulty: advanced
reading_level: advanced
audience:
- SRE
- Operations Engineer
- Platform Engineer
estimated_read_time: 15min
intent_queries:
- What are eBPF observability tools
- How to use bpftrace for system analysis
- What is Pixie
trigger_keywords:
- ebpf
- bcc
- bpftrace
- pixie
- parca
- tetragon
- observability
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
source_path: tree/infrastructure/kubernetes/networking/ebpf/02-ebpf-observability-tools.md
---

> **Production Environment Security Tips**
>
> This document contains executable operational commands. Please confirm before execution: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the command has been validated in a non-production environment. Command risk levels: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).


# eBPF Observability Tools Practical

## 1. bcc Toolset

### 1.1 Installation

```bash
# Ubuntu/Debian
sudo apt-get install bpfcc-tools linux-headers-$(uname -r)

# RHEL/CentOS
sudo yum install bcc-tools bcc-doc

# Binary Path
/usr/share/bcc/tools/
```

### 1.2 Process and System Call Analysis

```bash
# Track all execve calls
sudo /usr/share/bcc/tools/execsnoop

# Track specific process system calls (alternative to strace)
sudo /usr/share/bcc/tools/opensnoop -p 1234

# Track file opens
sudo /usr/share/bcc/tools/opensnoop -n nginx

# Track all system call delays
sudo /usr/share/bcc/tools/syscount -d 5

# Stat system calls (alternative to strace -c)
sudo /usr/share/bcc/tools/syscount -p 1234
```

### 1.3 CPU Analysis

```bash
# CPU Usage Flame Graph Data Collection
sudo /usr/share/bcc/tools/profile -F 99 -f 10 > profile.stacks

# Scheduling Latency Analysis
sudo /usr/share/bcc/tools/runqlat

# Histogram of Scheduling Latency Per CPU
sudo /usr/share/bcc/tools/runqlat -C

# Tracking CPU Migration
sudo /usr/share/bcc/tools/migrate
```

### 1.4 I/O Analysis

```bash
# Block I/O Latency Analysis
sudo /usr/share/bcc/tools/biolatency

# Distribution of Block I/O Sizes
sudo /usr/share/bcc/tools/biosize

# File System I/O Latency
sudo /usr/share/bcc/tools/fslatency

# Statistics of I/O for Each Process
sudo /usr/share/bcc/tools/biotop

# Tracking VFS Operations
sudo /usr/share/bcc/tools/vfsstat
```

### 1.5 Network Analysis

```bash
# Tracking TCP Connections
sudo /usr/share/bcc/tools/tcplife

# Tracking TCP Retransmissions
sudo /usr/share/bcc/tools/tcpretrans

# TCP Receive Window Shrinking
sudo /usr/share/bcc/tools/tcprcvbuf

# Tracking DNS Queries
sudo /usr/share/bcc/tools/dnssnoop

# Socket Lifecycle
sudo /usr/share/bcc/tools/socklife
```

## 2. bpftrace Tool

### 2.1 Installation and Basics

```bash
# Ubuntu/Debian
sudo apt-get install bpftrace

# RHEL/CentOS
sudo yum install bpftrace

# Version Check
bpftrace --version
```

### 2.2 Single Line Script

```bash
# Track System Call Entrypoints (Similar to strace)
bpftrace -e 'tracepoint:syscalls:sys_enter_* { @[probe] = count(); }'

# Count system calls per second
bpftrace -e 'tracepoint:raw_syscalls:sys_enter { @calls = count(); } interval:s:1 { print(@calls); clear(@calls); }'

# Track open system call
bpftrace -e 'tracepoint:syscalls:sys_enter_openat { printf("%s %s\n", comm, str(args->filename)); }'

# Histogram of delays
bpftrace -e 'kprobe:do_sys_open { @start[tid] = nsecs; } kretprobe:do_sys_open /@start[tid]/ { @ns = hist(nsecs - @start[tid]); delete(@start[tid]); }'
```

### 2.3 Useful Scripts

```bash
#!/usr/bin/env bpftrace
// tcpconnect.bt - Track TCP Connections
kprobe:tcp_connect
{
    $sk = (struct sock *)arg0;
    $daddr = ntop($sk->__sk_common.skc_daddr);
    printf("PID: %d COMM: %s -> %s:%d\n",
           pid, comm, $daddr,
           $sk->__sk_common.skc_dport);
}
```

```bash
#!/usr/bin/env bpftrace
// runqlat.bt - Schedule Delay Distribution
tracepoint:sched:sched_wakeup
{
    @qtime[args->pid] = nsecs;
}

tracepoint:sched:sched_switch
/args->prev_state == TASK_RUNNING/
{
    $pid = args->prev_pid;
    if (@qtime[$pid]) {
        @usecs = hist((nsecs - @qtime[$pid]) / 1000);
        delete(@qtime[$pid]);
    }
}
```

### 2.4 Container-Level Analysis for Kubernetes

```bash
# Track system calls for specific containers
bpftrace -e '
tracepoint:syscalls:sys_enter_write
/cgroup == 0x100001/    // 容器 cgroup ID
{
    printf("container-pid=%d comm=%s fd=%d\n", pid, comm, args->fd);
}
'

# Statistic CPU usage by container
bpftrace -e '
profile:hz:99
{
    @cpu[cgroup] = count();
}
'
```

## 3. Pixie Invasive Observability

### 3.1 Architecture

```
Pixie Edge Module (PEM) -> Vizier (data layer) -> Cloud / Self-hosted
    │
    └── Automatic collection: HTTP/gRPC/MySQL/Postgres/Kafka/DNS/Process
```

### 3.2 Installation

``` bash
# 🟡 Medium Risk: Modifies cluster/resource states, confirm target, impact scope, and authorization before execution
# Use Helm to install
helm repo add pixie https://pixie-operator-charts.storage.googleapis.com
helm repo update

helm install pixie pixie/pixie-operator-chart \
  --namespace pl \
  --create-namespace \
  --set clusterName=my-cluster \
  --set deployKey=<your-deploy-key>

# Or use px CLI
px deploy
```
### 3.3 pxL Query Language

```python
# Query HTTP request latency
import px

df = px.DataFrame(table='http_events', start_time='-5m')
df = df[['time_', 'source_addr', 'destination_addr',
         'req_method', 'req_path', 'resp_status', 'resp_latency_ns']]
df.resp_latency_ms = df.resp_latency_ns / 1e6
px.display(df, 'http_requests')
```

```python
# Statistic error rate by service
import px

df = px.DataFrame(table='http_events', start_time='-15m')
df = df.groupby(['source_service', 'destination_service']).agg(
    total=('resp_status', 'count'),
    errors=('resp_status', lambda x: (x >= 400).sum())
)
df.error_rate = df.errors / df.total * 100
px.display(df[df.error_rate > 1], 'error_services')
```

```python
# Count CPU Usage by Pod
import px

df = px.DataFrame(table='cpu_cycles', start_time='-5m')
df = df.groupby(['upid']).agg(cycles=('cpu_cycles', 'sum'))
px.display(df, 'pod_cpu')
```

### 3.4 Automatic Collection Protocol

| Protocol | Collection Content | Port Detection |
|------|----------|----------|
| HTTP/1.1 | Request/Response, Delay, Status Code | 80, 8080, 443 |
| HTTP/2 | gRPC Methods, Delay, Status Code | Dynamic Detection |
| MySQL | Query, Delay, Error | 3306 |
| PostgreSQL | Query, Delay, Error | 5432 |
| Kafka | Message, Delay, Topic | 9092 |
| DNS | Query, Response, Delay | 53 |
| Redis | Command, Delay | 6379 |

## 4. Parca Continuous Performance Profiling

### 4.1 Architecture

```
Parca Agent -> eBPF Collection (CPU profiling) -> Parca Server -> Web UI
    │
    └── Support: Go, Rust, C/C++, Python, Java, Node.js
```

### 4.2 Installation

``` bash
# 🟡 Medium Risk: Will modify cluster/resource status, please confirm target, impact scope, and authorization before execution
# Helm Installation
helm repo add parca https://parca-dev.github.io/helm-charts
helm repo update

helm install parca parca/parca \
  --namespace parca \
  --create-namespace \
  --set server.enabled=true

# Agent DaemonSet
helm install parca-agent parca/parca-agent \
  --namespace parca \
  --create-namespace
```
### 4.3 Use Cases

``` bash
# 🟡 Medium Risk: Will modify cluster/resource status, please confirm target, impact scope, and authorization before execution
# Access Web UI
kubectl port-forward svc/parca 7070:7070 -n parca

# API Query
curl "http://localhost:7070/query?query=cpu%3Asamples%3Acount%3Acpu%3Ananoseconds%3Arate%3A5m&time=$(date +%s)"
```
Advantages of Continuous Profiling:

| Traditional Profiling | Parca Continuous Profiling |
|----------------|---------------------|
| Manual Trigger | Automatic Continuous Collection |
| Single Point in Time | Full Coverage of Timeline |
| Requires Application Cooperation | Non-Intrusive (eBPF) |
| Production Environment Risks | Production Safety |

## 5. Tetragon Observations

### 5.1 Architecture

```
Tetragon Agent -> eBPF kernel sensor -> TracingPolicy -> Event/Action
    │
    └── Support: process, file, network, security events
```

### 5.2 Installation

``` bash
# 🟡 Medium Risk: Modifies cluster/resource states, confirm target, impact scope, and authorization before execution
# Helm Installation
helm repo add cilium https://helm.cilium.io/
helm repo update

helm install tetragon cilium/tetragon \
  --namespace kube-system \
  --set tetragonOperator.image.repository=cilium/tetragon-operator \
  --set tetragon.image.repository=cilium/tetragon

# View Events
kubectl logs -n kube-system ds/tetragon -f
```
### 5.3 TracingPolicy Example

```yaml
# Track Access to Sensitive Files
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: sensitive-file-access
spec:
  kprobes:
    - call: "fd_install"
      syscall: false
      args:
        - index: 0
          type: int
        - index: 1
          type: "file"
      selectors:
        - matchArgs:
            - index: 1
              operator: "Prefix"
              values:
                - "/etc/shadow"
                - "/etc/passwd"
                - "/var/run/secrets"
```

```yaml
# Track Process Execution
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: process-execution
spec:
  kprobes:
    - call: "security_bprm_check"
      syscall: false
      args:
        - index: 0
          type: "file"
      selectors:
        - matchBinaries:
            - operator: "NotIn"
              values:
                - "/usr/bin/kubectl"
                - "/bin/bash"
```

```yaml
# Track Network Connections
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: network-connections
spec:
  kprobes:
    - call: "tcp_connect"
      syscall: false
      args:
        - index: 0
          type: "sock"
      selectors:
        - matchActions:
            - action: FollowFD
```

### 5.4 Security Response Actions

```yaml
# Generate Automated Security Event Alerts
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: security-alerts
spec:
  kprobes:
    - call: "security_bprm_check"
      syscall: false
      args:
        - index: 0
          type: "file"
      selectors:
        - matchActions:
            - action: Sigkill    # 终止进程
              rateLimit: "1/m"
            - action: Override   # 覆盖返回值
              argError: -1       # 返回 EPERM
```

## 6. Tool Comparison and Selection

| Tool | Main Purpose | Intrusiveness | Performance Impact | Applicable Scenarios |
|------|----------|--------|----------|----------|
| **bcc** | System Call Analysis | Low | <1% | Development Debugging, Deep Analysis |
| **bpftrace** | Quick Prototype | Low | <1% | Temporary troubleshooting, quick validation |
| **Pixie** | Application Observability | None | 2-5% | K8s Full-stack observability |
| **Parca** | Performance Profiling | None | <0.5% | Continuous CPU analysis |
| **Tetragon** | Security Observability | Low | 1-3% | Runtime security |

---

## Related

- [[domain-15-specialized-tech/05-ebpf-programming/01-ebpf-programming-fundamentals|eBPF Development Foundation]]
- [[domain-15-specialized-tech/05-ebpf-programming/03-ebpf-networking-applications|eBPF Networking Applications]]
- [[domain-15-specialized-tech/05-ebpf-programming/04-ebpf-security-runtime|eBPF Security Runtime]]

## See Also

- [bcc Toolset](https://github.com/iovisor/bcc)
- [bpftrace Documentation](https://github.com/bpftrace/bpftrace)
- [Pixie](https://px.dev/)
- [Parca](https://www.parca.dev/)
- [Tetragon](https://tetragon.io/)


<!-- risk-assessed -->
