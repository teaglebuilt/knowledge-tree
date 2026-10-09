---
title: eBPF Development Basics
description: 'Types of eBPF programs, libbpf/CO-RE development mode, detailed explanation of Map types and toolchains'
summary: 'Types of eBPF programs, libbpf/CO-RE development mode, detailed explanation of Map types and toolchains'
category: specialized-tech
tags:
- ebpf
- libbpf
- xdp
- btf
- co-re
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
- What is eBPF
- How to develop eBPF programs
- What is libbpf and CO-RE
trigger_keywords:
- ebpf
- libbpf
- bpf
- xdp
- tracepoint
- kprobe
- btf
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
source_path: tree/infrastructure/kubernetes/networking/ebpf/01-ebpf-programming-fundamentals.md
---

> **Production Environment Security Tips**
>
> Commands included in this document are executable directly. Please confirm before execution: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether the commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High risk (may cause data loss or service disruption), 🟡 Medium risk (will modify the cluster state but usually rollbackable), 🟢 Low risk/readonly (information collection, no side effects).


# eBPF Development Basics

## 1. Overview of eBPF

eBPF (extended Berkeley Packet Filter) is a programmable virtual machine within the Linux kernel, allowing custom programs to run safely in the kernel space without modifying the kernel code.

```
用户态程序 → 加载 eBPF 字节码 → 内核验证器(Verifier) → JIT 编译 → 内核中执行
     │                                                              │
     └── 读取 Map 数据 ←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←←
```

Key advantages:

| Feature | Description |
|------|------|
| **Security** | Kernel validator ensures the program does not crash the kernel |
| Security | Kernel verifier ensures the program will not crash the kernel |
| Performance | JIT compiled to native instructions, near the performance of kernel modules |
| Programmability | User-space programs can communicate with the kernel via Maps |

## 2. Types of eBPF Programs

### 2.1 Network Classes

```c
// XDP (eXpress Data Path) - earliest network entry point
SEC("xdp")
int xdp_drop_icmp(struct xdp_md *ctx) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;

    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        return XDP_PASS;

    if (eth->h_proto != bpf_htons(ETH_P_IP))
        return XDP_PASS;

    struct iphdr *iph = (void *)(eth + 1);
    if ((void *)(iph + 1) > data_end)
        return XDP_PASS;

    // Drop ICMP packets
    if (iph->protocol == IPPROTO_ICMP)
        return XDP_DROP;

    return XDP_PASS;
}
```

```c
// TC (Traffic Control) - Traffic Control layer
SEC("tc")
int tc_filter_egress(struct __sk_buff *skb) {
    void *data = (void *)(long)skb->data;
    void *data_end = (void *)(long)skb->data_end;

    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        return TC_ACT_OK;

    // Mark specific traffic
    if (eth->h_proto == bpf_htons(ETH_P_IP)) {
        struct iphdr *iph = (void *)(eth + 1);
        if ((void *)(iph + 1) > data_end)
            return TC_ACT_OK;

        // Set DSCP mark
        iph->tos = (iph->tos & 0x03) | (0x2E << 2);
    }

    return TC_ACT_OK;
}
```

### 2.2 Tracking Classes

```c
// kprobe - Dynamic kernel function tracing
SEC("kprobe/do_sys_openat2")
int trace_open(struct pt_regs *ctx) {
    u64 pid = bpf_get_current_pid_tgid() >> 32;
    u64 ts = bpf_ktime_get_ns();

    // Record each open system call
    struct event evt = {
        .pid = pid,
        .ts = ts,
    };
    bpf_get_current_comm(&evt.comm, sizeof(evt.comm));

    bpf_map_update_elem(&events, &pid, &evt, BPF_ANY);
    return 0;
}
```

```c
// tracepoint - Static kernel tracing points
SEC("tracepoint/syscalls/sys_enter_write")
int trace_write(struct trace_event_raw_sys_enter *ctx) {
    u64 pid = bpf_get_current_pid_tgid() >> 32;
    int fd = ctx->args[0];
    size_t count = ctx->args[2];

    struct write_event evt = {
        .pid = pid,
        .fd = fd,
        .count = count,
    };
    bpf_perf_event_output(ctx, &events, BPF_F_CURRENT_CPU,
                          &evt, sizeof(evt));
    return 0;
}
```

```c
// uprobe - User-space function tracing
SEC("uprobe/libc.so.6:malloc")
int trace_malloc(struct pt_regs *ctx) {
    u64 pid = bpf_get_current_pid_tgid() >> 32;
    size_t size = PT_REGS_PARM1(ctx);

    bpf_printk("malloc(%lu) pid=%lu", size, pid);
    return 0;
}
```

### 2.3 Type Quick Reference

| Type | Hook Point | Typical Use Case |
|------|---------|----------|
| `XDP` | Network driver layer | DDoS protection, load balancing |
| `TC` | Traffic Control layer | Traffic shaping, marking |
| `kprobe` | Kernel function entry | Dynamic tracing |
| `kretprobe` | Kernel function return | Return value tracking |
| `tracepoint` | Static tracing points | System event monitoring |
| `uprobe` | User-space function | Application-level tracing |
| `LSM` | Linux Security Module | Security policy |
| `cgroup` | cgroup network | Container Network Policy |

## 3. eBPF Map Types

### 3.1 Hash Map

```c
// Definition
struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __uint(max_entries, 10240);
    __type(key, u32);           // PID
    __type(value, struct event); // 事件数据
    __uint(pinning, LIBBPF_PIN_BY_NAME);
} events SEC(".maps");

// Usage
SEC("kprobe/tcp_connect")
int trace_tcp_connect(struct pt_regs *ctx) {
    u32 pid = bpf_get_current_pid_tgid() >> 32;
    struct event evt = {};

    bpf_get_current_comm(&evt.comm, sizeof(evt.comm));
    evt.ts = bpf_ktime_get_ns();

    bpf_map_update_elem(&events, &pid, &evt, BPF_ANY);
    return 0;
}
```

### 3.2 Array Map

```c
struct {
    __uint(type, BPF_MAP_TYPE_ARRAY);
    __uint(max_entries, 256);
    __type(key, u32);
    __type(value, u64);
} counters SEC(".maps");

// Counter Increment
static __always_inline void increment_counter(u32 idx) {
    u64 *val = bpf_map_lookup_elem(&counters, &idx);
    if (val)
        __sync_fetch_and_add(val, 1);
}
```

### 3.3 Ring Buffer

```c
// Efficient Output Mechanism for Performance Events
struct {
    __uint(type, BPF_MAP_TYPE_RINGBUF);
    __uint(max_entries, 256 * 1024);  // 256KB
} rb SEC(".maps");

SEC("kprobe/tcp_sendmsg")
int trace_tcp_send(struct pt_regs *ctx) {
    struct event *evt;
    evt = bpf_ringbuf_reserve(&rb, sizeof(*evt), 0);
    if (!evt)
        return 0;

    evt->pid = bpf_get_current_pid_tgid() >> 32;
    evt->ts = bpf_ktime_get_ns();
    bpf_get_current_comm(&evt->comm, sizeof(evt->comm));

    bpf_ringbuf_submit(evt, 0);
    return 0;
}
```

### 3.4 Map Types Quick Reference

| Type | Features | Use Cases |
|------|------|----------|
| `HASH` | Key-value pairs, O(1) lookup | State tracking, caching |
| `ARRAY` | Fixed size, indexed access | Counters, statistics |
| `RINGBUF` | Circular buffer, efficient output | Event streams |
| `PERF_EVENT` | Per-CPU circular buffer | Event output (old) |
| `LRU_HASH` | LRU eviction | Large-scale caching |
| `LPM_TRIE` | Longest Prefix Match | IP routing lookups |
| `PERCPU_HASH` | Per-CPU hash table | Non-blocking statistics |
| `STACK` | Stack structure | Call stack |

## 4. libbpf and CO-RE

### 4.1 libbpf Development Mode

```c
// minimal.bpf.c - Kernel Mode Program
#include "vmlinux.h"
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_tracing.h>
#include <bpf/bpf_core_read.h>

char LICENSE[] SEC("license") = "GPL";

struct {
    __uint(type, BPF_MAP_TYPE_RINGBUF);
    __uint(max_entries, 256 * 1024);
} rb SEC(".maps");

SEC("tp/syscalls/sys_enter_execve")
int handle_execve(struct trace_event_raw_sys_enter *ctx)
{
    struct event *e;
    u64 pid_tgid = bpf_get_current_pid_tgid();

    e = bpf_ringbuf_reserve(&rb, sizeof(*e), 0);
    if (!e)
        return 0;

    e->pid = pid_tgid >> 32;
    e->tgid = (u32)pid_tgid;
    bpf_get_current_comm(&e->comm, sizeof(e->comm));

    // CO-RE: Reading kernel structure field
    struct task_struct *task = (struct task_struct *)bpf_get_current_task();
    e->ppid = BPF_CORE_READ(task, real_parent, tgid);

    bpf_ringbuf_submit(e, 0);
    return 0;
}
```

### 4.2 User Mode Loader Program

```c
// minimal.c - User Mode Program
#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <bpf/libbpf.h>
#include "minimal.skel.h"    // generated by bpftool

static volatile bool exiting = false;

static void sig_handler(int sig) {
    exiting = true;
}

static int handle_event(void *ctx, void *data, size_t data_sz) {
    const struct event *e = data;
    printf("exec: pid=%d ppid=%d comm=%s\n", e->pid, e->ppid, e->comm);
    return 0;
}

int main() {
    struct minimal_bpf *skel;
    struct ring_buffer *rb;

    signal(SIGINT, sig_handler);
    signal(SIGTERM, sig_handler);

    // Open and load BPF program
    skel = minimal_bpf__open_and_load();
    if (!skel) {
        fprintf(stderr, "Failed to open BPF skeleton\n");
        return 1;
    }

    // Attach to hook point
    if (minimal_bpf__attach(skel)) {
        fprintf(stderr, "Failed to attach BPF skeleton\n");
        goto cleanup;
    }

    // Set ring buffer callback
    rb = ring_buffer__new(bpf_map__fd(skel->maps.rb),
                          handle_event, NULL, NULL);
    if (!rb) {
        fprintf(stderr, "Failed to create ring buffer\n");
        goto cleanup;
    }

    printf("Tracing execve... Ctrl+C to exit\n");
    while (!exiting) {
        ring_buffer__poll(rb, 100);
    }

cleanup:
    ring_buffer__free(rb);
    minimal_bpf__destroy(skel);
    return 0;
}
```

### 4.3 CO-RE (Compile Once - Run Everywhere)

```c
// CO-RE: Access kernel structures without kernel headers
struct task_struct *task = (struct task_struct *)bpf_get_current_task();

// BPF_CORE_READ handles byte offsets automatically
int pid = BPF_CORE_READ(task, pid);
int tgid = BPF_CORE_READ(task, tgid);
const char *comm = BPF_CORE_READ(task, comm);

// BPF_CORE_READ_INTO reads into target variable
struct task_struct *parent;
BPF_CORE_READ_INTO(&parent, task, real_parent);
int ppid = BPF_CORE_READ(parent, tgid);
```

CO-RE works as follows:

```
编译时：记录字段重定位信息（BTF）
加载时：根据目标内核 BTF 调整偏移量
运行时：直接访问内核结构体字段
```

## 5. Development Toolchain

### 5.1 bpftool

```bash
# List loaded BPF programs
bpftool prog list

# View program details
bpftool prog show id 42

# Disassemble BPF program
bpftool prog dump xlated id 42

# List all Maps
bpftool map list

# View Map contents
bpftool map dump id 123

# Export BTF information
bpftool btf dump file /sys/kernel/btf/vmlinux format c > vmlinux.h
```

### 5.2 BTF Generation

```bash
# Generate vmlinux.h from current kernel
bpftool btf dump file /sys/kernel/btf/vmlinux format c > vmlinux.h

# Check if the kernel supports BTF
ls -la /sys/kernel/btf/vmlinux

# Generate from specific kernel header files
bpftool btf dump file /boot/vmlinux-$(uname -r) format c > vmlinux.h
```

### 5.3 Makefile Template

```makefile
# Makefile for eBPF programs
CLANG ?= clang
BPFTOOL ?= bpftool
ARCH := $(shell uname -m | sed 's/x86_64/x86/' | sed 's/aarch64/arm64/')

BPF_CFLAGS := -g -O2 -target bpf -D__TARGET_ARCH_$(ARCH) \
              -I$(OUTPUT) -Wall

.PHONY: all clean

all: minimal.skel.h minimal

# Generate vmlinux.h
$(OUTPUT)/vmlinux.h:
	$(BPFTOOL) btf dump file /sys/kernel/btf/vmlinux format c > $@

# Compile BPF programs
$(OUTPUT)/minimal.bpf.o: minimal.bpf.c $(OUTPUT)/vmlinux.h
	$(CLANG) $(BPF_CFLAGS) -c $< -o $@

# Generate skeleton
$(OUTPUT)/minimal.skel.h: $(OUTPUT)/minimal.bpf.o
	$(BPFTOOL) gen skeleton $< > $@

# Compile user-space program
minimal: minimal.c $(OUTPUT)/minimal.skel.h
	$(CC) -Wall -I$(OUTPUT) -o $@ $< -lbpf -lelf -lz

clean:
	rm -rf $(OUTPUT) minimal
```

### 5.4 libbpf-bootstrap

```bash
# Quick start using libbpf-bootstrap
git clone https://github.com/libbpf/libbpf-bootstrap.git
cd libbpf-bootstrap/examples/c

# Create a new project
make minimal    # 编译示例
sudo ./minimal  # 运行
```

---

## Related

- [[domain-15-specialized-tech/05-ebpf-programming/02-ebpf-observability-tools|eBPF Observability Tools]]
- [[domain-15-specialized-tech/05-ebpf-programming/03-ebpf-networking-applications|eBPF Networking Applications]]
- [[domain-15-specialized-tech/05-ebpf-programming/04-ebpf-security-runtime|eBPF Security Runtime]]

## See Also

- [eBPF Official Website](https://ebpf.io/)
- [libbpf Documentation](https://libbpf.readthedocs.io/)
- [eBPF Map Reference](https://ebpf.io/ebpf-map/)


<!-- risk-assessed -->
