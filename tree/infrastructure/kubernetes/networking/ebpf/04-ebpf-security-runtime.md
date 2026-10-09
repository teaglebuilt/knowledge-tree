---
title: eBPF Security Runtime
description: 'Tetragon Security Strategy, Falco eBPF Driver, KRSI and eBPF Auditing Strategy in Practice'
summary: 'Tetragon Security Strategy, Falco eBPF Driver, KRSI and eBPF Auditing Strategy in Practice'
category: specialized-tech
tags:
- ebpf
- tetragon
- falco
- krsi
- security
- runtime-security
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
- What is Tetragon Security Strategy
- How to Use Falco eBPF for Runtime Security
- What is KRSI
trigger_keywords:
- tetragon
- falco
- krsi
- ebpf
- runtime-security
- audit
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
source_path: tree/infrastructure/kubernetes/networking/ebpf/04-ebpf-security-runtime.md
---

> **Production Environment Security Reminders**
>
> Commands included in this document are executable directly. Before executing, please confirm: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk levels for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).


# eBPF Security Runtime

## 1. Runtime Security Architecture

```
Kernel event → eBPF sensor → policy engine → response action
    │              │            │          │
    │              │            │          └── alert/block/log
    │              │            └── TracingPolicy
    │              └── process/file/network/security
    └── kprobe/tracepoint/LSM
```

eBPF Secure Runtime Advantages:

| Feature | Traditional Solution | eBPF Solution |
|------|----------|-----------|
| Kernel Module | Required | Not Required |
| Performance Impact | High | Low (<3%) |
| Policy Flexibility | Fixed | Dynamically Programmable |
| Container Awareness | Limited | Fully Supported |

## 2. Tetragon Security Policies

### 2.1 Installation

``` bash
# 🟡 Medium Risk: modifies cluster/resource states; confirm target, impact scope, and authorization before execution
# Helm Installation
helm repo add cilium https://helm.cilium.io/
helm repo update

helm install tetragon cilium/tetragon \
  --namespace kube-system \
  --set tetragonOperator.image.repository=cilium/tetragon-operator \
  --set tetragon.image.repository=cilium/tetragon \
  --set tetragon.enableProcessCredScanning=true \
  --set tetragon.enableProcessNsScanning=true

# View Events
kubectl logs -n kube-system ds/tetragon -f
```
### 2.2 Process Execution Monitoring

```yaml
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: process-exec-monitor
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
                - "/usr/bin/coreutils"
        - matchActions:
            - action: FollowFD
    - call: "security_file_open"
      syscall: false
      args:
        - index: 0
          type: "file"
      selectors:
        - matchArgs:
            - index: 0
              operator: "Prefix"
              values:
                - "/etc/shadow"
                - "/etc/passwd"
                - "/root/.ssh"
```

### 2.3 Sensitivity File Access Control

```yaml
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: sensitive-file-protection
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
                - "/etc/gshadow"
                - "/etc/sudoers"
                - "/var/run/secrets/kubernetes.io"
        - matchBinaries:
            - operator: "NotIn"
              values:
                - "/usr/bin/sudo"
                - "/usr/bin/passwd"
        - matchNamespaces:
            - operator: "In"
              values:
                - "init_mnt"
        - matchActions:
            - action: Override
              argError: -13    # EACCES
```

### 2.4 Network Connection Monitoring

```yaml
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: network-connection-monitor
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
    - call: "tcp_close"
      syscall: false
      args:
        - index: 0
          type: "sock"
      selectors:
        - matchActions:
            - action: FollowFD
```

### 2.5 Signal/Override/FollowFD Actions

```yaml
# Signal - Send Signal to Terminate Process
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: block-malicious-process
spec:
  kprobes:
    - call: "security_bprm_check"
      syscall: false
      args:
        - index: 0
          type: "file"
      selectors:
        - matchBinaries:
            - operator: "In"
              values:
                - "/tmp/*"
                - "/dev/shm/*"
        - matchActions:
            - action: Sigkill
              rateLimit: "10/m"
---
# Override - Override System Call Return Values
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: block-unauthorized-mount
spec:
  kprobes:
    - call: "__x64_sys_mount"
      syscall: true
      args:
        - index: 0
          type: "string"
      selectors:
        - matchArgs:
            - index: 0
              operator: "Prefix"
              values:
                - "/proc"
                - "/sys"
        - matchActions:
            - action: Override
              argError: -1    # EPERM
```

### 2.6 Policy Combinations

```yaml
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: comprehensive-security
spec:
  kprobes:
    # Process Execution
    - call: "security_bprm_check"
      syscall: false
      args:
        - index: 0
          type: "file"
      selectors:
        - matchBinaries:
            - operator: "NotIn"
              values:
                - "/usr/bin/*"
                - "/usr/sbin/*"
        - matchActions:
            - action: Sigkill
              rateLimit: "5/m"
    # Sensitive File Writes
    - call: "security_file_open"
      syscall: false
      args:
        - index: 0
          type: "file"
        - index: 1
          type: "int"
      selectors:
        - matchArgs:
            - index: 0
              operator: "Prefix"
              values:
                - "/etc"
                - "/root"
            - index: 1
              operator: "Equal"
              values:
                - "2"    # O_WRONLY
        - matchActions:
            - action: Override
              argError: -13
```

## 3. Falco eBPF Driver

### 3.1 Installation

``` bash
# 🟡 Medium Risk: modifies cluster/resource states; confirm target, impact scope, and authorization before execution
# Helm Installation
helm repo add falcosecurity https://falcosecurity.github.io/charts
helm repo update

helm install falco falcosecurity/falco \
  --namespace falco \
  --create-namespace \
  --set driver.kind=ebpf \
  --set falcosidekick.enabled=true \
  --set falcosidekick.config.slack.webhookurl="https://hooks.slack.com/..."
```
### 3.2 Falco Rules

```yaml
# /etc/falco/falco_rules.yaml
- rule: Unauthorized Process in Sensitive Container
  desc: Detect process execution in sensitive containers
  condition: >
    spawned_process and container and
    container.image.repository in (database, redis, etcd) and
    not proc.name in (postgres, mysqld, redis-server, etcd)
  output: >
    Unauthorized process in sensitive container
    (user=%user.name command=%proc.cmdline container=%container.id
     image=%container.image.repository)
  priority: CRITICAL
  tags: [container, process, mitre_execution]

- rule: Sensitive File Access
  desc: Detect access to sensitive files
  condition: >
    open_read and container and
    fd.name in (/etc/shadow, /etc/passwd, /etc/kubernetes) and
    not proc.name in (sshd, sudo)
  output: >
    Sensitive file access detected
    (user=%user.name command=%proc.cmdline file=%fd.name
     container=%container.id image=%container.image.repository)
  priority: WARNING
  tags: [filesystem, mitre_credential_access]

- rule: Network Connection to Known Malicious IP
  desc: Detect outbound connections to known malicious IPs
  condition: >
    outbound and container and
    fd.sip in (malicious_ips)
  output: >
    Connection to known malicious IP
    (command=%proc.cmdline connection=%fd.name
     container=%container.id image=%container.image.repository)
  priority: CRITICAL
  tags: [network, mitre_command_and_control]
```

### 3.3 Custom Falco Rules

```yaml
# Detect Container Escalation Attempts
- rule: Container Escape Attempt
  desc: Detect potential container escape
  condition: >
    spawned_process and container and
    (proc.name in (nsenter, mount, chroot) or
     proc.cmdline contains "/proc/self/exe" or
     proc.cmdline contains "/proc/1/ns")
  output: >
    Container escape attempt detected
    (user=%user.name command=%proc.cmdline container=%container.id
     image=%container.image.repository k8s.pod=%k8s.pod.name)
  priority: CRITICAL
  tags: [container, escape, mitre_privilege_escalation]

# Detect Crypto Mining
- rule: Cryptocurrency Mining Detection
  desc: Detect cryptocurrency mining activity
  condition: >
    spawned_process and container and
    (proc.name in (xmrig, minerd, cpuminer) or
     proc.cmdline contains "stratum+tcp" or
     proc.cmdline contains "nicehash")
  output: >
    Cryptocurrency mining detected
    (command=%proc.cmdline container=%container.id
     image=%container.image.repository k8s.pod=%k8s.pod.name)
  priority: CRITICAL
  tags: [container, mining, mitre_execution]
```

## 4. KRSI (Kernel Runtime Security Instrumentation)

### 4.1 Overview

KRSI is a security framework for the Linux kernel, based on LSM (Linux Security Module):

```c
// KRSI eBPF Program Mount Point
SEC("lsm/file_open")
int BPF_PROG(file_open_audit, struct file *file, int ret) {
    // Audit File Access
    return ret;
}

SEC("lsm/bprm_creds_for_exec")
int BPF_PROG(exec_audit, struct linux_binprm *bprm, int ret) {
    // Audit Process Execution
    return ret;
}

SEC("lsm/socket_connect")
int BPF_PROG(connect_audit, struct socket *sock, struct sockaddr *address,
             int addrlen, int ret) {
    // Audit Network Connections
    return ret;
}
```

### 4.2 Integration with Tetragon

```yaml
# Tetragon Uses KRSI LSM Hook
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: lsm-file-protection
spec:
  lsmHooks:
    - hook: "file_open"
      args:
        - index: 0
          type: "file"
      selectors:
        - matchArgs:
            - index: 0
              operator: "Prefix"
              values:
                - "/etc/kubernetes"
                - "/var/run/secrets"
        - matchActions:
            - action: Override
              argError: -13
```

## 5. eBPF Auditing Policies

### 5.1 System Call Auditing

```c
// audit_syscalls.bpf.c
#include "vmlinux.h"
#include <bpf/bpf_helpers.h>

struct audit_event {
    u32 pid;
    u32 uid;
    u64 ts;
    char comm[16];
    char syscall[32];
    u64 args[6];
};

struct {
    __uint(type, BPF_MAP_TYPE_RINGBUF);
    __uint(max_entries, 256 * 1024);
} audit_events SEC(".maps");

SEC("tracepoint/raw_syscalls/sys_enter")
int audit_syscall(struct trace_event_raw_sys_enter *ctx) {
    struct audit_event *evt;
    u64 pid_tgid = bpf_get_current_pid_tgid();

    evt = bpf_ringbuf_reserve(&audit_events, sizeof(*evt), 0);
    if (!evt)
        return 0;

    evt->pid = pid_tgid >> 32;
    evt->uid = bpf_get_current_uid_gid();
    evt->ts = bpf_ktime_get_ns();
    bpf_get_current_comm(&evt->comm, sizeof(evt->comm));
    evt->syscall[0] = ctx->id;

    bpf_ringbuf_submit(evt, 0);
    return 0;
}
```

### 5.2 Kubernetes Audit Integration

```yaml
# Audit Policy Configuration (Complementary to eBPF)
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
  # Audit All Write Operations
  - level: RequestResponse
    resources:
      - group: ""
        resources: ["secrets", "configmaps"]
      - group: "apps"
        resources: ["deployments", "statefulsets"]
    verbs: ["create", "update", "patch", "delete"]

  # Audit Authentication Events
  - level: Metadata
    resources:
      - group: "authentication.k8s.io"
        resources: ["tokenreviews", "subjectaccessreviews"]
```

### 5.3 Comprehensive Auditing Architecture

```
Kernel event → eBPF audit → Tetragon/Falco → SIEM/SOAR
    │              │           │
    │              │           └── alert/response
    │              └── policy filter
    └── syscall/file/network/process

K8s API audit → Audit Sink → Webhook → backend storage
```

## 6. Security Response and Automation

### 6.1 Automated Blocking

```yaml
# Tetragon Automatically Blocks Malicious Processes
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: auto-block
spec:
  kprobes:
    - call: "security_bprm_check"
      syscall: false
      args:
        - index: 0
          type: "file"
      selectors:
        - matchBinaries:
            - operator: "In"
              values:
                - "/tmp/*"
                - "/dev/shm/*"
                - "/var/tmp/*"
        - matchActions:
            - action: Sigkill
              rateLimit: "5/m"
```

### 6.2 Integration with Falco Talon

```yaml
# Falco Talon Automatic Response
apiVersion: talon.falco.org/v1alpha1
kind: ResponseRule
metadata:
  name: block-crypto-mining
spec:
  match:
    rule: "Cryptocurrency Mining Detection"
    priority: "CRITICAL"
  actions:
    - type: kill
      parameters:
        signal: "SIGKILL"
    - type: label
      parameters:
        labels:
          "security.falco.org/blocked": "true"
```

## 7. Security Policy Templates

### 7.1 Baseline Security Policies

```yaml
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: baseline-security
spec:
  kprobes:
    # Prohibit dangerous operations in privileged containers
    - call: "__x64_sys_mount"
      syscall: true
      args:
        - index: 0
          type: "string"
      selectors:
        - matchNamespaces:
            - operator: "In"
              values:
                - "init_mnt"
        - matchActions:
            - action: Override
              argError: -1
    # Monitor sensitive file access
    - call: "security_file_open"
      syscall: false
      args:
        - index: 0
          type: "file"
      selectors:
        - matchArgs:
            - index: 0
              operator: "Prefix"
              values:
                - "/etc/shadow"
                - "/etc/sudoers"
                - "/root/.ssh"
```

### 7.2 Container Security Policies

```yaml
apiVersion: cilium.io/v1alpha1
kind: TracingPolicy
metadata:
  name: container-hardening
spec:
  kprobes:
    # Prevent privilege escalation in containers
    - call: "__x64_sys_setuid"
      syscall: true
      args:
        - index: 0
          type: "int"
      selectors:
        - matchArgs:
            - index: 0
              operator: "Equal"
              values:
                - "0"
        - matchActions:
            - action: Override
              argError: -1
    # Prevent loading kernel modules in containers
    - call: "__x64_sys_finit_module"
      syscall: true
      selectors:
        - matchNamespaces:
            - operator: "In"
              values:
                - "init_mnt"
        - matchActions:
            - action: Override
              argError: -1
```

## 8. Monitoring and Troubleshooting

``` bash
# 🟢 Low Risk: Read-only/information gathering, typically with no side effects
# Tetragon Status
kubectl get pods -n kube-system -l app.kubernetes.io/name=tetragon

# View Tetragon Events
kubectl logs -n kube-system ds/tetragon -f | tetra getevents

# Falco Status
kubectl get pods -n falco

# View Falco Alerts
kubectl logs -n falco ds/falco -f

# View Security Events
kubectl get events -A --field-selector reason=SecurityViolation
```
---

## Related

- [[domain-15-specialized-tech/05-ebpf-programming/01-ebpf-programming-fundamentals|eBPF Development Basics]]
- [[domain-15-specialized-tech/05-ebpf-programming/02-ebpf-observability-tools|eBPF Observability Tools]]
- [[domain-15-specialized-tech/05-ebpf-programming/03-ebpf-networking-applications|eBPF Networking Applications]]

## See Also

- [Tetragon Official Documentation](https://tetragon.io/)
- [Falco Official Documentation](https://falco.org/docs/)
- [KRSI Documentation](https://www.kernel.org/doc/html/latest/bpf/prog_lsm.html)


<!-- risk-assessed -->
