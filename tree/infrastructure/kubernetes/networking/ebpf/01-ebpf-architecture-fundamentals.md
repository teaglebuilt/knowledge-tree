---
title: eBPF Architecture Fundamentals and Program Types
description: A comprehensive guide to eBPF architecture fundamentals, covering the virtual machine design, verifier internals, JIT compilation, and the full range of eBPF program types used in networking, tracing, and security.
summary: 'eBPF (Extended Berkeley Packet Filter) is a revolutionary Linux kernel technology that allows sandboxed programs to run safely in kernel space without modifying kernel source code or loading kernel modules. It is essentially a virtual machine running inside the kernel, providing a safe and efficient way to extend kernel functionality.'
category: ebpf-technology
tags:
- k8s
- ebpf
- cilium
- networking
- observability
- docker
- ingress
- rag
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: expert
reading_level: expert
audience:
- SRE
- Network Engineer
- Kernel Engineer
estimated_read_time: 5min
intent_queries:
- What is eBPF Architecture Fundamentals and Program Types
- How to use eBPF Architecture Fundamentals and Program Types
- Kubernetes eBPF technology best practices
trigger_keywords:
- eBPF
- Architecture Fundamentals and Program Types
- Architecture
- Fundamentals
- and
- Program
- Types
prerequisites:
- kubectl-basics
- networking-basics
- ebpf-basics
- cilium-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: KUDIG Team
  role: contributor
---

> **Production Safety Notice**
>
> This document contains operational commands that can be executed directly. Before running them, confirm: the target cluster and Namespace are correct; you have sufficient RBAC permissions; and the commands have been validated in a non-production environment. Command risk levels: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state, usually rollbackable), 🟢 Low risk / read-only (information gathering, no side effects).




# eBPF Architecture Fundamentals and Program Types

> **Scope**: Kernel development, network acceleration, security monitoring | **Expert Level**: ⭐⭐⭐⭐⭐ | **Last Updated**: 2026-03-03
> **Kernel Requirements**: Linux Kernel >= 4.9 (basic) | >= 5.15 (BTF/CO-RE) | >= 6.1 (advanced features)

---

<!-- chunk: 📋 Table of Contents -->## 📋 Table of Contents

1. [eBPF Overview and Historical Evolution](#1-ebpf-overview-and-historical-evolution)
2. [eBPF Virtual Machine Architecture](#2-ebpf-virtual-machine-architecture)
3. [How the eBPF Verifier Works](#3-how-the-ebpf-verifier-works)
4. [JIT Compiler and Performance Optimization](#4-jit-compiler-and-performance-optimization)
5. [eBPF Program Types Explained](#5-ebpf-program-types-explained)
6. [eBPF Program Lifecycle Management](#6-ebpf-program-lifecycle-management)
7. [BTF and CO-RE](#7-btf-and-co-re)
8. [Best Practices and Common Issues](#8-best-practices-and-common-issues)

---

<!-- chunk: 1. eBPF Overview and Historical Evolution -->## 1. eBPF Overview and Historical Evolution

## 1.1 What is eBPF

eBPF (Extended Berkeley Packet Filter) is a revolutionary Linux kernel technology that allows sandboxed programs to run safely in kernel space without modifying kernel source code or loading kernel modules. It is essentially a virtual machine running inside the kernel, providing a safe and efficient way to extend kernel functionality.

**Core value proposition:**

| Characteristic | Traditional Approach | eBPF Approach |
|------|---------|----------|
| Kernel extension | Modify kernel source, compile kernel modules | Load eBPF programs, no reboot required |
| Security | A buggy kernel module can crash the system | The verifier guarantees program safety |
| Observability | Static probes, limited information | Dynamic instrumentation, full context |
| Network performance | High overhead in the user-space network stack | XDP processes packets at the earliest point in the kernel, near line-rate |
| Security policy | SELinux/AppArmor rules are fixed | LSM eBPF enables dynamic policies |

## 1.2 Historical Evolution: cBPF → eBPF

```
Timeline: Evolution of the Berkeley Packet Filter
─────────────────────────────────────────────────────────────────────────────

1992    ┌─────────────────────────────────────────────────────────────┐
        │ Birth of cBPF (Classic BPF)                                   │
        │ • Proposed by Steven McCanne & Van Jacobson on BSD systems    │
        │ • Paper: "The BSD Packet Filter: A New Architecture for       │
        │   User-level Packet Capture" (USENIX 1993)                    │
        │ • Two 32-bit registers (A: Accumulator, X: Index)             │
        │ • tcpdump uses cBPF for packet filtering                      │
        └─────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
2014    ┌─────────────────────────────────────────────────────────────┐
        │ Birth of eBPF (Extended BPF) - Linux 3.18                     │
        │ • Alexei Starovoitov redesigns the BPF virtual machine        │
        │ • 11 64-bit registers                                          │
        │ • Supports arbitrary program types (not just packet filters)  │
        │ • JIT compiler support for x86-64                              │
        │ • Maps data structure enables kernel/user-space communication │
        └─────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
2015    ┌─────────────────────────────────────────────────────────────┐
        │ kprobe support - Linux 4.1                                     │
        │ • eBPF programs can attach to kernel function probes          │
        │ • Begins replacing some SystemTap/DTrace functionality        │
        └─────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
2016    ┌─────────────────────────────────────────────────────────────┐
        │ XDP (eXpress Data Path) - Linux 4.8                            │
        │ • Earliest processing point in the network driver layer       │
        │ • Enables near line-rate packet processing                    │
        │ • Facebook uses XDP to defend against DDoS attacks            │
        └─────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
2017    ┌─────────────────────────────────────────────────────────────┐
        │ Cilium 1.0 released                                            │
        │ • eBPF-based container networking and security                │
        │ • L3/L4/L7 network policies                                    │
        └─────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
2020    ┌─────────────────────────────────────────────────────────────┐
        │ BTF + CO-RE - Linux 5.4/5.8                                    │
        │ • BPF Type Format type information shipped with the kernel    │
        │ • CO-RE: Compile Once - Run Everywhere                        │
        │ • Solves kernel version compatibility issues                  │
        └─────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
2021    ┌─────────────────────────────────────────────────────────────┐
        │ LSM BPF - Linux 5.7                                            │
        │ • eBPF programs can attach to LSM hooks                       │
        │ • Enables flexible kernel security policies                   │
        │ • Tetragon is built on this technology                        │
        └─────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
2022    ┌─────────────────────────────────────────────────────────────┐
        │ BPF Token, struct-based programs - Linux 5.15+                 │
        │ • bpf_loop() reduces verifier complexity                       │
        │ • Improved CO-RE relocations                                   │
        │ • eBPF for Windows (Microsoft project)                         │
        └─────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
2024+   ┌─────────────────────────────────────────────────────────────┐
        │ eBPF ecosystem matures                                         │
        │ • Cilium graduates as a CNCF project                          │
        │ • The Linux Foundation establishes the eBPF Foundation        │
        │ • Widely adopted in cloud computing, security, observability  │
        └─────────────────────────────────────────────────────────────┘
```

## 1.3 cBPF vs eBPF: Technical Comparison

```c
/* cBPF program example: filtering TCP packets (tcpdump -d 'tcp') */
/* Classic BPF - only 2 registers, a limited instruction set */
struct sock_filter cBPF_tcp_filter[] = {
    { 0x28, 0, 0, 0x0000000c },  /* ldh [12]  - load ethernet type */
    { 0x15, 0, 5, 0x000086dd },  /* jeq #0x86dd, IPv6 */
    { 0x30, 0, 0, 0x00000014 },  /* ldb [20]  - load protocol type */
    { 0x15, 6, 0, 0x00000006 },  /* jeq #6, TCP */
    { 0x15, 0, 15, 0x0000000800},/* jeq #0x800, IPv4 */
    { 0x30, 0, 0, 0x00000017 },  /* ldb [23]  */
    { 0x15, 3, 14, 0x00000006 }, /* jeq #6, TCP */
    { 0x6, 0, 0, 0x0000ffff },   /* ret #65535 - accept */
    { 0x6, 0, 0, 0x00000000 },   /* ret #0 - drop */
};

/* eBPF program example: XDP filtering TCP packets */
/* Extended BPF - 11 registers, supports function calls and Maps */
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include <bpf/bpf_helpers.h>

SEC("xdp")
int xdp_filter_tcp(struct xdp_md *ctx) {
    void *data_end = (void *)(long)ctx->data_end;
    void *data = (void *)(long)ctx->data;
    
    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        return XDP_DROP;
    
    if (eth->h_proto != bpf_htons(ETH_P_IP))
        return XDP_PASS;
    
    struct iphdr *ip = (void *)(eth + 1);
    if ((void *)(ip + 1) > data_end)
        return XDP_DROP;
    
    /* Full IPv4 header length calculation */
    if (ip->protocol != IPPROTO_TCP)
        return XDP_PASS;
    
    /* Update the statistics counter - using a Map */
    __u32 key = 0;
    __u64 *count = bpf_map_lookup_elem(&tcp_packets, &key);
    if (count)
        __sync_fetch_and_add(count, 1);
    
    return XDP_PASS;
}

char LICENSE[] SEC("license") = "GPL";
```

---

<!-- chunk: 2. eBPF Virtual Machine Architecture -->## 2. eBPF Virtual Machine Architecture

## 2.1 Overall Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        eBPF System Architecture                          │
│                                                                         │
│  User Space                                                            │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │  Application (libbpf / cilium-ebpf / bcc)                        │  │
│  │  ┌─────────────┐  ┌──────────────┐  ┌──────────────────────┐   │  │
│  │  │ BPF bytecode │  │  Map ops     │  │  Program control /   │   │  │
│  │  │ (.o file)    │  │ (read/write/ │  │  config (attach/     │   │  │
│  │  │              │  │  delete)     │  │  detach)             │   │  │
│  │  └──────┬──────┘  └──────┬───────┘  └──────────┬───────────┘   │  │
│  └─────────┼────────────────┼─────────────────────┼───────────────┘  │
│             │                │                     │                    │
│  ┌──────────▼────────────────▼─────────────────────▼───────────────┐  │
│  │                   bpf() System Call                              │  │
│  │   BPF_PROG_LOAD | BPF_MAP_CREATE | BPF_PROG_ATTACH | ...        │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│  Kernel Space                                                           │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                    eBPF Subsystem Core                            │  │
│  │                                                                   │  │
│  │  ┌─────────────┐    ┌─────────────┐    ┌──────────────────────┐ │  │
│  │  │  Verifier   │    │  JIT        │    │   BPF Virtual        │ │  │
│  │  │             │───▶│  Compiler   │    │   Machine             │ │  │
│  │  │             │    │ (x86/ARM/  │    │  (interpreted/JIT)    │ │  │
│  │  │             │    │  RISC-V..) │    │                      │ │  │
│  │  └─────────────┘    └─────────────┘    └──────────────────────┘ │  │
│  │                                                                   │  │
│  │  ┌─────────────────────────────────────────────────────────────┐ │  │
│  │  │                      eBPF Maps                              │ │  │
│  │  │  Hash | Array | LRU | RingBuf | PerfEvent | StackTrace ...  │ │  │
│  │  └─────────────────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────────────────┘  │
│                                                                         │
│  ┌──────────────────────────────────────────────────────────────────┐  │
│  │                    Kernel Hook Points                             │  │
│  │                                                                   │  │
│  │  NIC driver ──▶ XDP  ──▶ TC ingress ──▶ netfilter ──▶ TC egress  │  │
│  │                                                                   │  │
│  │  kprobe/kretprobe  tracepoint  LSM  cgroup  socket  perf event  │  │
│  └──────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
```

## 2.2 eBPF Register Set

The eBPF virtual machine has 11 64-bit general-purpose registers and one program counter:

```
eBPF Register Details
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Register  Purpose                            Mapping (x86-64)  Notes
────────  ────────────────────────────────  ────────────────  ──────────────────
r0        Function return value / exit code  rax               Holds return value at exit
r1        1st function-call argument          rdi                Program context (ctx)
r2        2nd function-call argument          rsi
r3        3rd function-call argument          rdx
r4        4th function-call argument          rcx
r5        5th function-call argument          r8
r6        Callee-saved                        rbx                Preserved across helper calls
r7        Callee-saved                        r13
r8        Callee-saved                        r14
r9        Callee-saved                        r15
r10       Read-only frame pointer             rbp                Points to top of the eBPF stack
pc        Program counter                     rip                Read-only, cannot be modified directly

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Key constraints:
• r1-r5 may be clobbered after a helper function call; save into r6-r9 if needed
• r10 always points to the bottom of the stack (BPF_STACK_SIZE = 512 bytes)
• When calling a subfunction, arguments are passed via r1-r5, and the return value is in r0
```

```c
/* Register usage example - eBPF assembly perspective */
/* BPF bytecode (human-readable form) */

// r1 = ctx (the xdp_md pointer for an XDP program)
// r2 = 0
// r0 = bpf_map_lookup_elem(map, &key)
// Equivalent to:
//   mov r2, r1          ; r2 = ctx
//   mov r1, map_fd      ; r1 = map file descriptor
//   call bpf_map_lookup_elem
//   ; r0 now holds the lookup result (pointer or NULL)

/* In C code, the compiler handles register allocation automatically */
SEC("xdp")
int demo_register_usage(struct xdp_md *ctx) {
    /* r1 = ctx (passed in by the kernel) */
    
    __u32 key = 0;           /* stack variable: [r10-4] */
    __u64 *value;
    
    /* Calling a helper - arguments in r1-r5 */
    /* r1 = &stats_map (resolved via BPF_CORE_READ) */
    /* r2 = &key */
    value = bpf_map_lookup_elem(&stats_map, &key);
    /* After the call: r0 = value (may be NULL) */
    /* Note: r1-r5 have been clobbered */
    
    if (value) {
        /* value is saved in r6 (callee-saved) to survive the helper call */
        (*value)++;
    }
    
    return XDP_PASS; /* r0 = 2 (XDP_PASS) */
}
```

## 2.3 Instruction Set Architecture

eBPF uses 64-bit fixed-length instructions (some instructions are 128 bits, used for immediate-value loads):

```
eBPF Instruction Format (64 bits)
┌───────────┬──────┬──────┬────────────┬────────────────────────────┐
│  opcode   │  dst │  src │   offset   │          imm               │
│  (8 bits) │(4bit)│(4bit)│ (16 bits)  │        (32 bits)           │
└───────────┴──────┴──────┴────────────┴────────────────────────────┘

Instruction classes (top 3 bits of the opcode):
┌──────────────────────────────────────────────────────────────────┐
│ BPF_LD    (0x00): load instruction (wide)                        │
│ BPF_LDX   (0x01): load from memory into a register               │
│ BPF_ST    (0x02): store an immediate value into memory           │
│ BPF_STX   (0x03): store a register into memory                   │
│ BPF_ALU   (0x04): 32-bit arithmetic/logic operations              │
│ BPF_JMP   (0x05): jump instruction                                │
│ BPF_JMP32 (0x06): 32-bit jump instruction                         │
│ BPF_ALU64 (0x07): 64-bit arithmetic/logic operations              │
└──────────────────────────────────────────────────────────────────┘
```

```c
/* Instruction set usage example */
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

/* ALU operation example */
SEC("tracepoint/syscalls/sys_enter_write")
int trace_write(struct trace_event_raw_sys_enter *ctx) {
    __u64 pid_tgid = bpf_get_current_pid_tgid();
    __u32 pid = pid_tgid >> 32;          /* 64-bit right shift: BPF_ALU64 | BPF_RSH */
    __u32 tgid = (__u32)pid_tgid;        /* truncate to 32 bits */
    
    /* Memory access - BPF_LDX */
    int fd = (int)ctx->args[0];          /* read a field from the struct */
    
    /* Conditional jump - BPF_JMP */
    if (fd < 0)
        return 0;
    
    /* Arithmetic operation - BPF_ALU64 */
    __u64 write_size = (__u64)ctx->args[2];
    __u64 scaled = write_size * 1024;    /* multiplication */
    
    bpf_printk("PID %d wrote %llu bytes to fd %d\n", pid, write_size, fd);
    
    return 0;
}
```

## 2.4 The eBPF Stack

eBPF programs have 512 bytes of stack space:

```
eBPF Stack Layout (512 bytes)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

High address
┌──────────────────────────────────────────┐ r10 (frame pointer)
│  [r10 - 8]   local variable 1             │
├──────────────────────────────────────────┤
│  [r10 - 16]  local variable 2             │
├──────────────────────────────────────────┤
│  [r10 - 24]  Map lookup key (temporary)   │
├──────────────────────────────────────────┤
│  ...                                      │
├──────────────────────────────────────────┤
│  [r10 - 256] subfunction call stack frame │
├──────────────────────────────────────────┤
│  ...                                      │
├──────────────────────────────────────────┤
│  [r10 - 512] bottom of stack (512-byte limit) │
└──────────────────────────────────────────┘
Low address

Key constraints:
• Maximum 512 bytes of stack space
• Function calls share this stack space (non-recursive)
• Storage can be extended via BPF_MAP_TYPE_PERCPU_ARRAY
• Stack contents must be initialized before being passed to helper functions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

```c
/* Stack space management example */
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

/* Use a Per-CPU Array to extend storage (beyond 512 bytes) */
struct large_event {
    __u64 timestamp;
    char comm[16];
    __u8 data[2048];  /* exceeds the stack size limit */
};

/* Use a Per-CPU Map as temporary storage */
struct {
    __uint(type, BPF_MAP_TYPE_PERCPU_ARRAY);
    __uint(max_entries, 1);
    __type(key, __u32);
    __type(value, struct large_event);
} heap_storage SEC(".maps");

SEC("kprobe/vfs_write")
int kprobe_vfs_write(struct pt_regs *ctx) {
    __u32 key = 0;
    
    /* Get "heap" space from the Per-CPU Map */
    struct large_event *event = bpf_map_lookup_elem(&heap_storage, &key);
    if (!event)
        return 0;
    
    /* Now a data structure larger than 512 bytes can be used */
    event->timestamp = bpf_ktime_get_ns();
    bpf_get_current_comm(event->comm, sizeof(event->comm));
    
    /* Read data... */
    
    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

## 2.5 The Helper Function System

```c
/* eBPF helper function categories and usage */

/* 1. Time-related */
__u64 time_ns = bpf_ktime_get_ns();        /* nanoseconds since kernel boot */
__u64 time_boot = bpf_ktime_get_boot_ns(); /* includes suspend time */
__u64 time_tai = bpf_ktime_get_tai_ns();   /* TAI time */

/* 2. Process/task related */
__u64 pid_tgid = bpf_get_current_pid_tgid();
__u32 pid = pid_tgid >> 32;    /* thread PID */
__u32 tgid = (__u32)pid_tgid;  /* process TGID */

__u64 uid_gid = bpf_get_current_uid_gid();
__u32 uid = (__u32)uid_gid;
__u32 gid = uid_gid >> 32;

char comm[16];
bpf_get_current_comm(comm, sizeof(comm));  /* process name */

/* 3. Map operations */
void *val = bpf_map_lookup_elem(&my_map, &key);
int ret = bpf_map_update_elem(&my_map, &key, &val, BPF_ANY);
int ret = bpf_map_delete_elem(&my_map, &key);
long ret = bpf_for_each_map_elem(&my_map, callback_fn, callback_ctx, 0);

/* 4. Memory operations */
bpf_probe_read_kernel(&dst, sizeof(dst), src);  /* safely read kernel memory */
bpf_probe_read_user(&dst, sizeof(dst), src);    /* safely read user memory */
long ret = bpf_probe_read_kernel_str(buf, sizeof(buf), str_ptr);

/* 5. Network related */
bpf_skb_load_bytes(skb, offset, &buf, len);    /* read data from an skb */
bpf_skb_store_bytes(skb, offset, from, len, flags);
bpf_l3_csum_replace(skb, offset, from, to, flags);
bpf_l4_csum_replace(skb, offset, from, to, flags);
bpf_redirect(ifindex, flags);                   /* redirect a packet */
bpf_clone_redirect(skb, ifindex, flags);

/* 6. Perf events */
bpf_perf_event_output(ctx, &events, BPF_F_CURRENT_CPU, &data, sizeof(data));
bpf_ringbuf_output(&rb, &data, sizeof(data), 0);

/* 7. Tail calls */
bpf_tail_call(ctx, &prog_array, index);         /* jump to another eBPF program */

/* 8. Trace output (debugging) */
bpf_printk("key=%u, value=%llu\n", key, value); /* /sys/kernel/debug/tracing/trace_pipe */

/* Helper function availability by program type */
/*
Type               Available helper examples
────────────────── ─────────────────────────────────────────
XDP                bpf_xdp_adjust_head/tail, bpf_redirect_map
TC (skb)           bpf_skb_*, bpf_redirect, bpf_clone_redirect
kprobe/tracepoint  bpf_probe_read_*, bpf_get_current_*, bpf_perf_event_output
LSM                bpf_ima_inode_hash, bpf_sk_storage_*
cgroup/sock        bpf_setsockopt, bpf_getsockopt, bpf_sock_ops_cb_flags_set
*/
```

---

<!-- chunk: 3. How the eBPF Verifier Works -->## 3. How the eBPF Verifier Works

## 3.1 Verifier Architecture

```
eBPF Verifier Workflow
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

User space loads a program
       │
       │ bpf(BPF_PROG_LOAD, ...)
       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          Verifier                                        │
│                                                                         │
│  Stage 1: Basic Checks                                                  │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ • Instruction count <= 1,000,000 (raised from 4096 in kernel 5.2+)│   │
│  │ • Instruction format validity (opcode, register ranges)          │   │
│  │ • No illegal instructions (privileged instructions, etc.)        │   │
│  │ • Program type matches allowed helper function permissions       │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                           │                                             │
│                           ▼                                             │
│  Stage 2: Control Flow Graph Analysis                                   │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ • Builds a directed acyclic graph (DAG)                          │   │
│  │ • Detects and forbids loops (classic eBPF; 5.3+ supports bounded │   │
│  │   loops)                                                         │   │
│  │ • Ensures every code path reaches BPF_EXIT                       │   │
│  │ • Detects unreachable (dead) code                                │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                           │                                             │
│                           ▼                                             │
│  Stage 3: Data Flow Analysis - simulated execution                     │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │ Register state tracking:                                        │   │
│  │   NOT_INIT | SCALAR_VALUE | PTR_TO_MAP_VALUE | PTR_TO_CTX |     │   │
│  │   PTR_TO_STACK | PTR_TO_PACKET | PTR_TO_FUNC | ...              │   │
│  │                                                                 │   │
│  │ Memory access checks:                                           │   │
│  │   • Pointer bounds checking                                     │   │
│  │   • Alignment checking                                          │   │
│  │   • Uninitialized-read checking                                 │   │
│  │                                                                 │   │
│  │ Pointer arithmetic:                                             │   │
│  │   • Only limited pointer arithmetic is allowed                  │   │
│  │   • Tracks offsets and possible value ranges                    │   │
│  │                                                                 │   │
│  │ Helper-call validation:                                         │   │
│  │   • Argument type checking                                      │   │
│  │   • Return value type tracking                                  │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                           │                                             │
│                     pass  │  fail                                       │
│                     ┌────┴────┐                                         │
│                     ▼         ▼                                         │
│               JIT compile   returns EPERM/EINVAL                        │
│                             + detailed error message                    │
└─────────────────────────────────────────────────────────────────────────┘
```

## 3.2 Register Type System

```c
/* Register states tracked by the verifier (simplified from kernel source) */

enum bpf_reg_type {
    NOT_INIT = 0,           /* uninitialized, cannot be read */
    SCALAR_VALUE,           /* scalar value (integer) */
    PTR_TO_CTX,             /* points to the program context (e.g. xdp_md) */
    CONST_PTR_TO_MAP,       /* constant pointer to a BPF Map */
    PTR_TO_MAP_VALUE,       /* points to a Map value */
    PTR_TO_MAP_KEY,         /* points to a Map key */
    PTR_TO_STACK,           /* points into the eBPF stack */
    PTR_TO_PACKET_META,     /* points to packet metadata */
    PTR_TO_PACKET,          /* points to packet data */
    PTR_TO_PACKET_END,      /* packet end pointer */
    PTR_TO_FLOW_KEYS,       /* points to flow_keys */
    PTR_TO_SOCKET,          /* points to a socket */
    PTR_TO_SOCK_COMMON,     /* points to sock_common */
    PTR_TO_TCP_SOCK,        /* points to tcp_sock */
    PTR_TO_TP_BUFFER,       /* points to a tracepoint buffer */
    PTR_TO_XDP_SOCK,        /* points to xdp_sock (AF_XDP) */
    PTR_TO_BTF_ID,          /* points to a kernel BTF type */
    PTR_TO_MEM,             /* generic memory pointer */
    PTR_TO_BUF,             /* generic buffer pointer */
    PTR_TO_FUNC,            /* points to a function */
    CONST_PTR_TO_DYNPTR,    /* points to a dynamic pointer */
};
```

## 3.3 Common Verification Failures and Fixes

```c
/* Error example 1: missing NULL pointer check */
/* Error: value is not null pointer; mem_size from mem ptr arithmetic */
SEC("xdp")
int bad_null_check(struct xdp_md *ctx) {
    __u32 key = 0;
    __u64 *value = bpf_map_lookup_elem(&my_map, &key);
    
    /* Error: NULL was never checked */
    *value += 1;  /* Rejected by the verifier: value could be NULL */
    
    return XDP_PASS;
}

/* Fix: NULL must be checked */
SEC("xdp")
int good_null_check(struct xdp_md *ctx) {
    __u32 key = 0;
    __u64 *value = bpf_map_lookup_elem(&my_map, &key);
    
    /* Correct: check for NULL before accessing */
    if (!value)
        return XDP_PASS;
    
    *value += 1;  /* Safe: verified non-NULL */
    
    return XDP_PASS;
}

/* Error example 2: missing packet boundary check */
SEC("xdp")
int bad_packet_access(struct xdp_md *ctx) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;
    
    struct ethhdr *eth = data;
    /* Error: accesses eth->h_proto without a bounds check */
    return eth->h_proto == bpf_htons(ETH_P_IP) ? XDP_PASS : XDP_DROP;
}

/* Fix: a bounds check is required */
SEC("xdp")
int good_packet_access(struct xdp_md *ctx) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;
    
    struct ethhdr *eth = data;
    /* Correct: check bounds first */
    if ((void *)(eth + 1) > data_end)
        return XDP_DROP;
    
    return eth->h_proto == bpf_htons(ETH_P_IP) ? XDP_PASS : XDP_DROP;
}

/* Error example 3: unbounded loop (kernel < 5.3) */
SEC("xdp")
int bad_unbounded_loop(struct xdp_md *ctx) {
    /* Error (older kernels): the verifier cannot prove loop termination */
    for (int i = 0; i < some_variable; i++) {
        /* ... */
    }
    return XDP_PASS;
}

/* Fix: use a bounded loop or pragma unroll */
SEC("xdp")
int good_bounded_loop(struct xdp_md *ctx) {
    /* Option 1: pragma unroll (unrolled at compile time) */
    #pragma unroll
    for (int i = 0; i < 10; i++) {
        /* ... */
    }
    
    /* Option 2: a compile-time constant bound */
    #define MAX_ITERATIONS 100
    for (int i = 0; i < MAX_ITERATIONS; i++) {
        /* ... */
    }
    
    /* Option 3: use bpf_loop() (5.17+) */
    bpf_loop(1024, loop_callback, &ctx_data, 0);
    
    return XDP_PASS;
}

/* Error example 4: stack overflow */
SEC("kprobe/sys_read")
int bad_stack_usage(struct pt_regs *ctx) {
    /* Error: 512-byte stack limit */
    char large_buf[1024];  /* exceeds 512 bytes */
    bpf_probe_read_user(large_buf, sizeof(large_buf), (void *)PT_REGS_PARM2(ctx));
    return 0;
}

/* Fix: use a Per-CPU Map as a "heap" */
struct {
    __uint(type, BPF_MAP_TYPE_PERCPU_ARRAY);
    __uint(max_entries, 1);
    __type(key, __u32);
    __type(value, char[2048]);
} heap SEC(".maps");

SEC("kprobe/sys_read")
int good_stack_usage(struct pt_regs *ctx) {
    __u32 key = 0;
    char *buf = bpf_map_lookup_elem(&heap, &key);
    if (!buf)
        return 0;
    
    bpf_probe_read_user(buf, 1024, (void *)PT_REGS_PARM2(ctx));
    return 0;
}
```

---

<!-- chunk: 4. JIT Compiler and Performance Optimization -->## 4. JIT Compiler and Performance Optimization

## 4.1 JIT Compilation Pipeline

```
eBPF JIT Compilation Pipeline
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

C source (eBPF program)
       │
       │ clang -target bpf -O2 -g
       ▼
eBPF bytecode (.o ELF file)
  • BPF instruction set (RISC-style)
  • BTF debug information
  • Map relocation information
       │
       │ bpf(BPF_PROG_LOAD)
       ▼
Verifier
  • Safety verification
  • Type checking
       │
       │ verification passes
       ▼
JIT compiler (arch/x86/net/bpf_jit_comp.c)
       │
       ├── x86-64 JIT
       ├── ARM64 JIT
       ├── RISC-V JIT
       ├── s390 JIT
       └── PowerPC JIT
       │
       ▼
Native machine code
  • Direct register mapping
  • No interpreter overhead
  • Performance nearly identical to compiled C code
       │
       ▼
Attached to a kernel hook point and executed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 4.2 JIT Compiler Configuration

```bash
# Enable JIT compilation (enabled by default on modern kernels)
echo 1 > /proc/sys/net/core/bpf_jit_enable

# Enable JIT hardening - protects against JIT spraying attacks
# 0: off, 1: enabled for unprivileged users, 2: enabled for all users
echo 2 > /proc/sys/net/core/bpf_jit_harden

# Show BPF programs in kallsyms
echo 1 > /proc/sys/net/core/bpf_jit_kallsyms

# View JIT-compiled machine code (for debugging)
cat /proc/sys/net/core/bpf_jit_enable
# Setting this to 2 also dumps JIT code to the kernel log

# View JIT code via bpftool
bpftool prog show id <prog_id>
bpftool prog dump jited id <prog_id>
bpftool prog dump xlated id <prog_id>  # view the eBPF bytecode (with BTF annotations)
```

## 4.3 JIT Performance Comparison

```
Performance Benchmark Comparison (XDP processing 64-byte packets)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Execution method            Throughput      Latency      Notes
─────────────────────── ─────────────── ─────────── ───────────────────
Traditional kernel stack    ~1 Mpps         ~5-10 μs    full TCP/IP processing
iptables/netfilter          ~2-3 Mpps       ~2-5 μs     linear rule matching
nftables                    ~3-5 Mpps       ~1-3 μs     more efficient rule engine
eBPF interpreter (no JIT)   ~5 Mpps         ~500 ns     pure interpretation
eBPF + JIT                  ~15-25 Mpps     ~100-200 ns JIT-compiled native code
XDP + JIT (driver mode)     ~40-60 Mpps     ~50-100 ns  earliest processing point
DPDK (for comparison)       ~80-100 Mpps    ~20-50 ns   user space, dedicated CPU

Note: actual performance depends on hardware, kernel version, and program complexity
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

<!-- chunk: 5. eBPF Program Types Explained -->## 5. eBPF Program Types Explained

## 5.1 XDP (eXpress Data Path) Network Acceleration

## How XDP Works

```
XDP Packet Processing Path
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

NIC receives a packet
       │
       ▼
┌─────────────────────────────────────────────────────────────────────┐
│  NIC Driver Layer                                                    │
│                                                                     │
│  XDP_HOOK: ndo_bpf / ndo_xdp_xmit                                  │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  XDP program execution (eBPF)                                 │  │
│  │                                                              │  │
│  │  Return values:                                              │  │
│  │  XDP_DROP (1)    ──▶ drop immediately, no skb allocated      │  │
│  │  XDP_PASS (2)    ──▶ continue into the kernel network stack  │  │
│  │  XDP_TX   (3)    ──▶ transmit back out the same NIC          │  │
│  │  XDP_REDIRECT(4) ──▶ redirect to another NIC/AF_XDP socket   │  │
│  │  XDP_ABORTED(0)  ──▶ error drop (raises a tracepoint)        │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  XDP modes:                                                         │
│  • Native XDP: directly supported by the NIC driver (highest perf) │
│    Supported: mlx4/mlx5, i40e, ixgbe, virtio-net, veth, tun ...   │
│  • Generic XDP: generic kernel implementation (better compat,      │
│    lower performance)                                              │
│  • Offloaded XDP: executed in NIC hardware (highest performance,   │
│    e.g. Netronome)                                                  │
└─────────────────────────────────────────────────────────────────────┘
       │ XDP_PASS
       ▼
  sk_buff allocation (memory allocation overhead)
       │
       ▼
  GRO (Generic Receive Offload)
       │
       ▼
  TC ingress hook
       │
       ▼
  Netfilter (iptables/nftables)
       │
       ▼
  Routing decision
       │
       ▼
  Socket receive buffer
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## XDP Program Practical Example

```c
/* XDP DDoS protection program - IP blacklist */
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/ipv6.h>
#include <linux/in.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_endian.h>

/* IP blacklist Map */
struct {
    __uint(type, BPF_MAP_TYPE_LPM_TRIE);      /* longest prefix match */
    __uint(max_entries, 10000);
    __uint(key_size, sizeof(struct bpf_lpm_trie_key) + 4);  /* IPv4 */
    __uint(value_size, sizeof(__u64));
    __uint(map_flags, BPF_F_NO_PREALLOC);
} blacklist_v4 SEC(".maps");

/* Statistics counters */
struct xdp_stats {
    __u64 rx_packets;
    __u64 dropped_packets;
    __u64 passed_packets;
};

struct {
    __uint(type, BPF_MAP_TYPE_PERCPU_ARRAY);
    __uint(max_entries, 1);
    __type(key, __u32);
    __type(value, struct xdp_stats);
} stats_map SEC(".maps");

/* LPM key structure */
struct ipv4_lpm_key {
    __u32 prefixlen;
    __u32 data;
};

static __always_inline int check_blacklist_v4(__u32 src_ip) {
    struct ipv4_lpm_key key = {
        .prefixlen = 32,
        .data = src_ip,
    };
    return bpf_map_lookup_elem(&blacklist_v4, &key) != NULL;
}

SEC("xdp")
int xdp_ddos_protection(struct xdp_md *ctx) {
    void *data_end = (void *)(long)ctx->data_end;
    void *data = (void *)(long)ctx->data;
    
    __u32 stats_key = 0;
    struct xdp_stats *stats = bpf_map_lookup_elem(&stats_map, &stats_key);
    if (stats)
        __sync_fetch_and_add(&stats->rx_packets, 1);
    
    /* Parse the ethernet header */
    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        goto drop;
    
    __u16 eth_proto = bpf_ntohs(eth->h_proto);
    
    if (eth_proto == ETH_P_IP) {
        /* IPv4 handling */
        struct iphdr *ip = (void *)(eth + 1);
        if ((void *)(ip + 1) > data_end)
            goto drop;
        
        /* Check the blacklist */
        if (check_blacklist_v4(ip->saddr)) {
            if (stats)
                __sync_fetch_and_add(&stats->dropped_packets, 1);
            return XDP_DROP;
        }
    }
    
    if (stats)
        __sync_fetch_and_add(&stats->passed_packets, 1);
    return XDP_PASS;

drop:
    if (stats)
        __sync_fetch_and_add(&stats->dropped_packets, 1);
    return XDP_DROP;
}

char LICENSE[] SEC("license") = "GPL";
```

```yaml
# XDP program loading and management - using bpftool
# Load the XDP program
apiVersion: v1
kind: ConfigMap
metadata:
  name: xdp-loader-script
data:
  load-xdp.sh: |
    #!/bin/bash
    
    # Compile the XDP program
    clang -target bpf -O2 -g \
      -I/usr/include/linux \
      -c xdp_ddos.c \
      -o xdp_ddos.o
    
    # Load onto the NIC (eth0)
    # Generic XDP (compatibility mode)
    ip link set dev eth0 xdpgeneric obj xdp_ddos.o sec xdp
    
    # Native XDP (requires driver support)
    ip link set dev eth0 xdp obj xdp_ddos.o sec xdp
    
    # Unload the XDP program
    ip link set dev eth0 xdp off
    
    # View the XDP program
    bpftool net show dev eth0
    
    # Add an IP to the blacklist
    bpftool map update pinned /sys/fs/bpf/blacklist_v4 \
      key 32 0 0 0 192 168 1 100 \
      value 1 0 0 0 0 0 0 0
    
    # View statistics
    bpftool map dump pinned /sys/fs/bpf/stats_map
```

## 5.2 TC (Traffic Control) Traffic Shaping

## TC Hook Points

```
TC (Traffic Control) eBPF Hook Points
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Ingress direction:
  NIC ──▶ XDP ──▶ [sk_buff allocation] ──▶ TC Ingress ──▶ Netfilter ──▶ Routing

Egress direction:
  App ──▶ Socket ──▶ Routing ──▶ Netfilter ──▶ TC Egress ──▶ NIC ──▶ Sent

TC eBPF actions:
  TC_ACT_OK       (0): continue normal processing
  TC_ACT_RECLASSIFY(1): reclassify
  TC_ACT_SHOT     (2): drop the packet
  TC_ACT_PIPE     (3): pass to the next action
  TC_ACT_STOLEN   (4): the packet is "stolen" (redirect)
  TC_ACT_QUEUED   (5): queued
  TC_ACT_REPEAT   (6): repeat the action
  TC_ACT_REDIRECT (7): redirect
  TC_ACT_TRAP     (8): trap to user space (tc program)

TC vs XDP:
  ┌────────────────┬──────────────┬────────────────────────────────────┐
  │ Characteristic │ XDP           │ TC                                 │
  ├────────────────┼──────────────┼────────────────────────────────────┤
  │ Execution point │ driver layer (earliest) │ kernel network stack (skb exists) │
  │ skb availability │ no skb       │ skb available, all fields read/write │
  │ Egress support  │ TX only       │ Ingress + Egress                   │
  │ Tunnel support  │ limited       │ full (vxlan, geneve, ipip)         │
  │ Performance     │ highest       │ high (after skb allocation)        │
  │ Container networking │ common at ingress │ heavily used by Cilium        │
  └────────────────┴──────────────┴────────────────────────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

```c
/* TC eBPF program example - service load balancing */
#include <linux/bpf.h>
#include <linux/pkt_cls.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_endian.h>

/* Backend server Map */
struct backend {
    __u32 ip;
    __u16 port;
    __u8  weight;
    __u8  active;
};

struct {
    __uint(type, BPF_MAP_TYPE_ARRAY);
    __uint(max_entries, 8);
    __type(key, __u32);
    __type(value, struct backend);
} backends SEC(".maps");

/* Connection tracking Map */
struct conn_key {
    __u32 src_ip;
    __u16 src_port;
    __u32 dst_ip;
    __u16 dst_port;
};

struct conn_val {
    __u32 backend_ip;
    __u16 backend_port;
    __u64 last_seen;
};

struct {
    __uint(type, BPF_MAP_TYPE_LRU_HASH);
    __uint(max_entries, 65536);
    __type(key, struct conn_key);
    __type(value, struct conn_val);
} conn_track SEC(".maps");

static __always_inline __u16 csum_fold(__u32 csum) {
    csum = (csum & 0xffff) + (csum >> 16);
    csum = (csum & 0xffff) + (csum >> 16);
    return (__u16)~csum;
}

SEC("tc")
int tc_load_balancer(struct __sk_buff *skb) {
    void *data_end = (void *)(long)skb->data_end;
    void *data = (void *)(long)skb->data;
    
    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        return TC_ACT_SHOT;
    
    if (eth->h_proto != bpf_htons(ETH_P_IP))
        return TC_ACT_OK;
    
    struct iphdr *ip = (void *)(eth + 1);
    if ((void *)(ip + 1) > data_end)
        return TC_ACT_SHOT;
    
    if (ip->protocol != IPPROTO_TCP)
        return TC_ACT_OK;
    
    __u32 ip_hdr_len = ip->ihl * 4;
    struct tcphdr *tcp = (void *)ip + ip_hdr_len;
    if ((void *)(tcp + 1) > data_end)
        return TC_ACT_SHOT;
    
    /* Check whether this traffic is destined for the VIP */
    __u32 vip = bpf_htonl(0xC0A80001);  /* 192.168.0.1 */
    if (ip->daddr != vip)
        return TC_ACT_OK;
    
    /* Look up an existing connection */
    struct conn_key ckey = {
        .src_ip = ip->saddr,
        .src_port = tcp->source,
        .dst_ip = ip->daddr,
        .dst_port = tcp->dest,
    };
    
    struct conn_val *cval = bpf_map_lookup_elem(&conn_track, &ckey);
    
    __u32 backend_ip;
    __u16 backend_port;
    
    if (cval) {
        /* Use the backend from the existing connection */
        backend_ip = cval->backend_ip;
        backend_port = cval->backend_port;
    } else {
        /* Pick a backend (simple round-robin) */
        __u32 idx = bpf_get_prandom_u32() % 3;
        struct backend *be = bpf_map_lookup_elem(&backends, &idx);
        if (!be || !be->active)
            return TC_ACT_SHOT;
        
        backend_ip = be->ip;
        backend_port = be->port;
        
        /* Record the connection */
        struct conn_val new_val = {
            .backend_ip = backend_ip,
            .backend_port = backend_port,
            .last_seen = bpf_ktime_get_ns(),
        };
        bpf_map_update_elem(&conn_track, &ckey, &new_val, BPF_ANY);
    }
    
    /* Rewrite the destination IP and port (DNAT) */
    /* Note: the checksum would actually need to be updated too */
    bpf_skb_store_bytes(skb, 
        (void *)&ip->daddr - data,
        &backend_ip, 4, BPF_F_RECOMPUTE_CSUM);
    bpf_skb_store_bytes(skb,
        (void *)&tcp->dest - data,
        &backend_port, 2, BPF_F_RECOMPUTE_CSUM);
    
    return TC_ACT_OK;
}

char LICENSE[] SEC("license") = "GPL";
```

```bash
# TC eBPF program loading
# Create a clsact qdisc (a virtual qdisc that supports eBPF)
tc qdisc add dev eth0 clsact

# Load the ingress program
tc filter add dev eth0 ingress bpf obj tc_lb.o sec tc

# Load the egress program
tc filter add dev eth0 egress bpf obj tc_lb.o sec tc

# View loaded filters
tc filter show dev eth0 ingress

# Delete a filter
tc filter del dev eth0 ingress
tc qdisc del dev eth0 clsact

# Manage TC programs with bpftool
bpftool net show
bpftool prog show tag <prog_tag>
```

## 5.3 kprobe/kretprobe Kernel Tracing

```c
/* kprobe example for tracing a kernel function */
#include <linux/bpf.h>
#include <linux/ptrace.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_tracing.h>
#include <bpf/bpf_core_read.h>

/* File-open event structure */
struct file_open_event {
    __u64 timestamp;
    __u32 pid;
    __u32 uid;
    char comm[16];
    char filename[256];
    int flags;
    int ret;  /* only valid for kretprobe */
};

/* Pass events via a Ring Buffer */
struct {
    __uint(type, BPF_MAP_TYPE_RINGBUF);
    __uint(max_entries, 1 << 24);  /* 16 MB */
} events SEC(".maps");

/* kprobe: executes at the entry of do_sys_openat2 */
SEC("kprobe/do_sys_openat2")
int BPF_KPROBE(kprobe_openat2, int dfd, const char __user *filename, 
               struct open_how *how) {
    struct file_open_event *event;
    
    /* Reserve space in the ring buffer */
    event = bpf_ringbuf_reserve(&events, sizeof(*event), 0);
    if (!event)
        return 0;
    
    event->timestamp = bpf_ktime_get_ns();
    event->pid = bpf_get_current_pid_tgid() >> 32;
    event->uid = bpf_get_current_uid_gid() & 0xFFFFFFFF;
    bpf_get_current_comm(event->comm, sizeof(event->comm));
    
    /* Safely read the user-space string */
    bpf_probe_read_user_str(event->filename, sizeof(event->filename), filename);
    
    /* Read the flags field of the open_how struct (using CO-RE) */
    event->flags = BPF_CORE_READ(how, flags);
    event->ret = 0;
    
    /* Submit the event */
    bpf_ringbuf_submit(event, 0);
    
    return 0;
}

/* kretprobe: executes when do_sys_openat2 returns */
SEC("kretprobe/do_sys_openat2")
int BPF_KRETPROBE(kretprobe_openat2, long ret) {
    /* Only care about failed open calls */
    if (ret >= 0)
        return 0;
    
    struct file_open_event *event;
    event = bpf_ringbuf_reserve(&events, sizeof(*event), 0);
    if (!event)
        return 0;
    
    event->timestamp = bpf_ktime_get_ns();
    event->pid = bpf_get_current_pid_tgid() >> 32;
    event->uid = bpf_get_current_uid_gid() & 0xFFFFFFFF;
    bpf_get_current_comm(event->comm, sizeof(event->comm));
    event->ret = ret;
    
    bpf_ringbuf_submit(event, 0);
    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

```c
/* Using fentry/fexit instead of kprobe (more efficient, 5.5+) */
/* fentry/fexit hook kernel functions directly, without an int3 breakpoint, for better performance */

SEC("fentry/tcp_connect")
int BPF_PROG(fentry_tcp_connect, struct sock *sk) {
    __u64 pid_tgid = bpf_get_current_pid_tgid();
    
    struct {
        __u32 pid;
        __u32 saddr;
        __u32 daddr;
        __u16 dport;
    } event = {
        .pid = pid_tgid >> 32,
        .saddr = BPF_CORE_READ(sk, __sk_common.skc_rcv_saddr),
        .daddr = BPF_CORE_READ(sk, __sk_common.skc_daddr),
        .dport = BPF_CORE_READ(sk, __sk_common.skc_dport),
    };
    
    bpf_perf_event_output(ctx, &events, BPF_F_CURRENT_CPU,
                          &event, sizeof(event));
    return 0;
}

SEC("fexit/tcp_connect")
int BPF_PROG(fexit_tcp_connect, struct sock *sk, int ret) {
    if (ret != 0) {
        bpf_printk("tcp_connect failed: ret=%d\n", ret);
    }
    return 0;
}
```

## 5.4 Tracepoints: Static Tracing

```c
/* Tracepoint example - tracing scheduler events */
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_tracing.h>
#include <bpf/bpf_core_read.h>

/* Tracepoint argument structure - obtained automatically via BTF */
/* Path: /sys/kernel/debug/tracing/events/sched/sched_switch/format */
struct sched_switch_args {
    unsigned long long pad;  /* common fields */
    char prev_comm[16];
    pid_t prev_pid;
    int prev_prio;
    long prev_state;
    char next_comm[16];
    pid_t next_pid;
    int next_prio;
};

/* Process scheduling latency tracking */
struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __uint(max_entries, 10240);
    __type(key, __u32);    /* pid */
    __type(value, __u64);  /* time the process entered the run queue */
} sched_start SEC(".maps");

/* Scheduling latency histogram */
struct {
    __uint(type, BPF_MAP_TYPE_ARRAY);
    __uint(max_entries, 64);  /* 64 time buckets */
    __type(key, __u32);
    __type(value, __u64);
} lat_hist SEC(".maps");

/* Process joins the run queue */
SEC("tracepoint/sched/sched_wakeup")
int tp_sched_wakeup(struct trace_event_raw_sched_wakeup *ctx) {
    __u32 pid = ctx->pid;
    __u64 ts = bpf_ktime_get_ns();
    bpf_map_update_elem(&sched_start, &pid, &ts, BPF_ANY);
    return 0;
}

/* Process starts executing */
SEC("tracepoint/sched/sched_switch")
int tp_sched_switch(struct sched_switch_args *ctx) {
    /* Record the process being switched out */
    __u32 prev_pid = ctx->prev_pid;
    __u32 next_pid = ctx->next_pid;
    
    /* Compute the scheduling latency for the next process */
    __u64 *start_ts = bpf_map_lookup_elem(&sched_start, &next_pid);
    if (start_ts) {
        __u64 now = bpf_ktime_get_ns();
        __u64 latency_ns = now - *start_ts;
        
        /* Update the histogram */
        __u32 slot = 0;
        __u64 lat_us = latency_ns / 1000;
        
        /* log2 approximation */
        if (lat_us >= 1) {
            slot = 1;
            __u64 v = lat_us;
            #pragma unroll
            for (int i = 0; i < 63; i++) {
                v >>= 1;
                if (v == 0) break;
                slot++;
            }
        }
        if (slot >= 64) slot = 63;
        
        __u64 *count = bpf_map_lookup_elem(&lat_hist, &slot);
        if (count)
            __sync_fetch_and_add(count, 1);
        
        bpf_map_delete_elem(&sched_start, &next_pid);
    }
    
    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

## 5.5 LSM (Linux Security Module) Security Hooks

```c
/* LSM eBPF program - runtime security policy */
#include <linux/bpf.h>
#include <linux/lsm_hook_defs.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_tracing.h>
#include <bpf/bpf_core_read.h>

/* Rule denying execution of a specific file */
struct deny_rule {
    char path[256];
    __u64 deny_count;
};

struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __uint(max_entries, 1024);
    __type(key, char[256]);
    __type(value, struct deny_rule);
} deny_exec_paths SEC(".maps");

/* Process execution audit log */
struct exec_audit {
    __u64 timestamp;
    __u32 pid;
    __u32 uid;
    char comm[16];
    char filename[256];
    int denied;
};

struct {
    __uint(type, BPF_MAP_TYPE_RINGBUF);
    __uint(max_entries, 1 << 24);
} audit_events SEC(".maps");

/* LSM hook: file_open */
SEC("lsm/file_open")
int BPF_PROG(lsm_file_open, struct file *file) {
    /* Get the file path */
    char path[256] = {};
    
    struct dentry *dentry = BPF_CORE_READ(file, f_path.dentry);
    struct qstr name = BPF_CORE_READ(dentry, d_name);
    
    /* Simplified: only checks the filename (a full path check would be needed in practice) */
    bpf_probe_read_kernel_str(path, sizeof(path), name.name);
    
    /* Check whether it's on the deny list */
    struct deny_rule *rule = bpf_map_lookup_elem(&deny_exec_paths, path);
    
    /* Record an audit log entry */
    struct exec_audit *event = bpf_ringbuf_reserve(&audit_events, sizeof(*event), 0);
    if (event) {
        event->timestamp = bpf_ktime_get_ns();
        event->pid = bpf_get_current_pid_tgid() >> 32;
        event->uid = bpf_get_current_uid_gid() & 0xFFFFFFFF;
        bpf_get_current_comm(event->comm, sizeof(event->comm));
        __builtin_memcpy(event->filename, path, sizeof(path));
        event->denied = rule ? 1 : 0;
        bpf_ringbuf_submit(event, 0);
    }
    
    if (rule) {
        /* Increment the deny counter */
        __sync_fetch_and_add(&rule->deny_count, 1);
        return -EPERM;  /* deny access */
    }
    
    return 0;  /* allow */
}

/* LSM hook: bprm_check_security - checks program execution */
SEC("lsm/bprm_check_security")
int BPF_PROG(lsm_bprm_check, struct linux_binprm *bprm) {
    char filename[256] = {};
    
    struct file *file = BPF_CORE_READ(bprm, file);
    struct dentry *dentry = BPF_CORE_READ(file, f_path.dentry);
    const unsigned char *name = BPF_CORE_READ(dentry, d_name.name);
    
    bpf_probe_read_kernel_str(filename, sizeof(filename), name);
    
    /* Check whether execution is allowed */
    struct deny_rule *rule = bpf_map_lookup_elem(&deny_exec_paths, filename);
    if (rule)
        return -EACCES;
    
    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

## 5.6 cgroup Program Types

```c
/* cgroup eBPF program - container network control */
#include <linux/bpf.h>
#include <linux/in.h>
#include <bpf/bpf_helpers.h>

/* Allowed port whitelist */
struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __uint(max_entries, 1024);
    __type(key, __u16);   /* port number */
    __type(value, __u8);  /* 1 = allowed */
} allowed_ports SEC(".maps");

/* cgroup/connect4: control IPv4 connections */
SEC("cgroup/connect4")
int cgroup_connect4(struct bpf_sock_addr *ctx) {
    /* Get the destination port */
    __u16 port = bpf_ntohs(ctx->user_port);
    
    /* Check whether the port is whitelisted */
    __u8 *allowed = bpf_map_lookup_elem(&allowed_ports, &port);
    if (!allowed)
        return 0;  /* deny the connection */
    
    return 1;  /* allow the connection */
}

/* cgroup/sock_create: control socket creation */
SEC("cgroup/sock_create")
int cgroup_sock_create(struct bpf_sock *sk) {
    /* Only allow TCP and UDP */
    if (sk->type != SOCK_STREAM && sk->type != SOCK_DGRAM)
        return 0;  /* deny */
    return 1;     /* allow */
}

/* cgroup/skb: control packets (similar to XDP/TC) */
SEC("cgroup_skb/ingress")
int cgroup_skb_ingress(struct __sk_buff *skb) {
    /* Only allow loopback traffic or established connections */
    __u32 src = skb->remote_ip4;
    
    /* Allow 127.0.0.0/8 */
    if ((bpf_ntohl(src) & 0xFF000000) == 0x7F000000)
        return 1;
    
    return 1;  /* allow by default */
}

char LICENSE[] SEC("license") = "GPL";
```

``` bash
# 🟢 Low risk: read-only/information gathering, generally no side effects
# cgroup eBPF program attachment
# Find the container's cgroup path
CONTAINER_ID=$(docker ps -q -f name=myapp)
CGROUP_PATH="/sys/fs/cgroup/unified/docker/${CONTAINER_ID}"

# Attach the cgroup program with bpftool
bpftool prog load cgroup_control.o /sys/fs/bpf/cgroup_prog

bpftool cgroup attach ${CGROUP_PATH} connect4 \
    pinned /sys/fs/bpf/cgroup_prog

# Used in Kubernetes (the Cilium approach)
# Cilium automatically attaches policy programs to each Pod's cgroup
```
## 5.7 Socket Filters

```c
/* Socket Filter program - capture specific traffic */
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_endian.h>

/* BPF_PROG_TYPE_SOCKET_FILTER:
   return 0 = drop the packet
   return > 0 = keep this many bytes */

SEC("socket")
int socket_filter_http(struct __sk_buff *skb) {
    /* Only keep HTTP traffic (destination port 80 or 8080) */
    
    __u8 ip_proto;
    /* Ethernet header: 14 bytes, IP protocol field at offset 23 */
    if (bpf_skb_load_bytes(skb, 23, &ip_proto, 1) < 0)
        return 0;
    
    if (ip_proto != IPPROTO_TCP)
        return 0;
    
    /* IP header length (assuming a standard 20 bytes) */
    /* TCP destination port: ethernet(14) + IP(20) + TCP_DST_PORT_OFFSET(2) */
    __u16 dst_port;
    if (bpf_skb_load_bytes(skb, 36, &dst_port, 2) < 0)
        return 0;
    
    dst_port = bpf_ntohs(dst_port);
    
    if (dst_port == 80 || dst_port == 8080 || dst_port == 443)
        return skb->len;  /* keep all the data */
    
    return 0;  /* drop */
}

char LICENSE[] SEC("license") = "GPL";
```

---

<!-- chunk: 6. eBPF Program Lifecycle Management -->## 6. eBPF Program Lifecycle Management

## 6.1 Program Lifecycle

```
eBPF Program Lifecycle
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Compilation stage
   C source ──[clang/llvm]──▶ eBPF bytecode (.o ELF)
                                    │
2. Loading stage                   │
   User process ──[bpf() syscall]──▶ Kernel
   • BPF_PROG_LOAD                  │
   • Verifier checks                │
   • JIT compilation                │
   • Returns prog_fd (file descriptor) │
                                    │
3. Attach stage                    │
   prog_fd ──[bpf() / ip / tc]──▶ Hook point
   • BPF_PROG_ATTACH                │
   • xdp via netlink                │
   • tc via netlink                 │
   • kprobe via perf_event          │
                                    │
4. Execution stage                 │
   Trigger condition ──▶ eBPF program runs ──▶ returns a result
                    │
                    ▼
              Operates on Maps
              Calls Helpers
              Emits events
                                    │
5. Unload stage                    │
   close(prog_fd) or explicit detach │
   Once all fds are closed and there are no pinned references,  │
   the program is freed by the kernel │
                                    │
6. Persistence (optional)          │
   bpf_obj_pin(prog_fd, "/sys/fs/bpf/my_prog")
   The program is pinned to the BPF filesystem and survives process exit
   Re-acquired via bpf_obj_get("/sys/fs/bpf/my_prog")

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 6.2 Managing Program Lifecycle with libbpf

```c
/* User-space program: loading and managing an eBPF program with libbpf */
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <errno.h>
#include <bpf/libbpf.h>
#include <bpf/bpf.h>
#include "xdp_ddos.skel.h"  /* generated by bpftool gen skeleton */

static volatile bool running = true;

static void sig_handler(int sig) {
    running = false;
}

int main(int argc, char *argv[]) {
    struct xdp_ddos_bpf *skel;
    int ifindex, err;
    
    if (argc < 2) {
        fprintf(stderr, "Usage: %s <interface>\n", argv[0]);
        return 1;
    }
    
    ifindex = if_nametoindex(argv[1]);
    if (!ifindex) {
        perror("if_nametoindex");
        return 1;
    }
    
    /* 1. Open the BPF object */
    skel = xdp_ddos_bpf__open();
    if (!skel) {
        fprintf(stderr, "Failed to open BPF object\n");
        return 1;
    }
    
    /* 2. Optional: adjust Map size and other parameters before loading */
    bpf_map__set_max_entries(skel->maps.blacklist_v4, 100000);
    
    /* 3. Load the eBPF program (verify + JIT) */
    err = xdp_ddos_bpf__load(skel);
    if (err) {
        fprintf(stderr, "Failed to load BPF object: %d\n", err);
        goto cleanup;
    }
    
    /* 4. Attach the XDP program */
    err = bpf_xdp_attach(ifindex, 
                          bpf_program__fd(skel->progs.xdp_ddos_protection),
                          XDP_FLAGS_DRV_MODE,  /* Native XDP */
                          NULL);
    if (err) {
        /* Fall back to Generic XDP */
        err = bpf_xdp_attach(ifindex,
                              bpf_program__fd(skel->progs.xdp_ddos_protection),
                              XDP_FLAGS_SKB_MODE,
                              NULL);
        if (err) {
            fprintf(stderr, "Failed to attach XDP: %d\n", err);
            goto cleanup;
        }
    }
    
    printf("XDP program loaded on %s (ifindex=%d)\n", argv[1], ifindex);
    
    /* 5. Pin the Maps to the BPF filesystem (optional, for tooling access) */
    err = bpf_map__pin(skel->maps.stats_map, "/sys/fs/bpf/xdp_stats");
    if (err)
        fprintf(stderr, "Warning: failed to pin stats map: %d\n", err);
    
    /* 6. Run loop */
    signal(SIGINT, sig_handler);
    signal(SIGTERM, sig_handler);
    
    while (running) {
        /* Read statistics */
        __u32 key = 0;
        struct xdp_stats stats[libbpf_num_possible_cpus()];
        
        err = bpf_map__lookup_elem(skel->maps.stats_map, 
                                    &key, sizeof(key),
                                    stats, sizeof(stats), 0);
        if (!err) {
            __u64 total_rx = 0, total_drop = 0;
            for (int i = 0; i < libbpf_num_possible_cpus(); i++) {
                total_rx += stats[i].rx_packets;
                total_drop += stats[i].dropped_packets;
            }
            printf("\rRX: %llu, Dropped: %llu (%.2f%%)",
                   total_rx, total_drop,
                   total_rx ? 100.0 * total_drop / total_rx : 0.0);
            fflush(stdout);
        }
        
        sleep(1);
    }
    
    printf("\nDetaching XDP program...\n");
    
    /* 7. Detach the XDP program */
    bpf_xdp_detach(ifindex, XDP_FLAGS_DRV_MODE, NULL);
    bpf_xdp_detach(ifindex, XDP_FLAGS_SKB_MODE, NULL);

cleanup:
    /* 8. Release resources */
    xdp_ddos_bpf__destroy(skel);
    return err;
}
```

## 6.3 The BPF Filesystem

```bash
# BPF filesystem operations
# Mount the BPF filesystem
mount -t bpf bpf /sys/fs/bpf

# View the BPF filesystem contents
ls -la /sys/fs/bpf/

# Pin a program
bpftool prog pin id <prog_id> /sys/fs/bpf/my_prog

# Pin a Map
bpftool map pin id <map_id> /sys/fs/bpf/my_map

# Reload from a pin
bpf_prog_fd = bpf_obj_get("/sys/fs/bpf/my_prog")
bpf_map_fd = bpf_obj_get("/sys/fs/bpf/my_map")

# List all BPF programs
bpftool prog list

# View program details
bpftool prog show id <id> -p

# List all BPF Maps
bpftool map list

# Dump Map contents
bpftool map dump id <id>

# Update Map contents
bpftool map update id <id> key 0x01 0x00 0x00 0x00 value 0x01

# View kernel BPF statistics
cat /proc/sys/kernel/bpf_stats_enabled
echo 1 > /proc/sys/kernel/bpf_stats_enabled
bpftool prog show  # now shows runtime statistics
```

---

<!-- chunk: 7. BTF and CO-RE -->## 7. BTF and CO-RE

## 7.1 BTF (BPF Type Format) Overview

```
BTF Architecture and Purpose
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BTF is a metadata format that describes the type information used by BPF programs and Maps.
It is a lightweight alternative to DWARF debug information, designed specifically for eBPF.

What BTF provides:
┌─────────────────────────────────────────────────────────────────┐
│ 1. Enhanced verification                                        │
│    • More precise type checking                                 │
│    • Better error messages                                      │
│                                                                 │
│ 2. Debug information                                            │
│    • bpftool prog dump xlated shows C source annotations        │
│    • BTF makes eBPF programs debuggable                         │
│                                                                 │
│ 3. Map pretty-printing                                          │
│    • bpftool map dump displays structured data                  │
│    • No need to manually parse binary data                      │
│                                                                 │
│ 4. Foundation for CO-RE                                          │
│    • Kernel type information is exposed via BTF                 │
│    • eBPF programs can access kernel struct fields               │
│    • No kernel headers required                                  │
│                                                                 │
│ 5. Ring Buffer type safety                                       │
│    • BPF_MAP_TYPE_RINGBUF uses BTF for type annotations          │
└─────────────────────────────────────────────────────────────────┘

Sources of BTF information:
  /sys/kernel/btf/vmlinux    <- kernel BTF
  the .BTF section in a program's .o file
  the .BTF.ext section in a program's .o file (line number info)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 7.2 CO-RE (Compile Once - Run Everywhere)

```c
/* CO-RE usage example */
/* Solves the problem of struct layout differences across kernel versions */

#include <vmlinux.h>        /* all kernel types generated from kernel BTF */
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_core_read.h>  /* CO-RE macros */
#include <bpf/bpf_tracing.h>

/* Option 1: use the BPF_CORE_READ macro (recommended) */
SEC("kprobe/tcp_sendmsg")
int kprobe_tcp_sendmsg(struct pt_regs *ctx) {
    struct sock *sk = (struct sock *)PT_REGS_PARM1(ctx);
    
    /* CO-RE-safe read: automatically handles field offset differences across kernel versions */
    __u32 src_ip = BPF_CORE_READ(sk, __sk_common.skc_rcv_saddr);
    __u32 dst_ip = BPF_CORE_READ(sk, __sk_common.skc_daddr);
    __u16 dst_port = BPF_CORE_READ(sk, __sk_common.skc_dport);
    
    /* Nested read */
    __u32 netns_ino = BPF_CORE_READ(sk, __sk_common.skc_net.net, 
                                     ns.inum);
    
    bpf_printk("TCP: %x -> %x:%d (ns=%u)\n", 
               src_ip, dst_ip, bpf_ntohs(dst_port), netns_ino);
    return 0;
}

/* Option 2: use the bpf_core_read() function */
SEC("kprobe/vfs_read")
int kprobe_vfs_read(struct pt_regs *ctx) {
    struct file *file = (struct file *)PT_REGS_PARM1(ctx);
    
    /* Read the file path */
    struct dentry *dentry;
    bpf_core_read(&dentry, sizeof(dentry), &file->f_path.dentry);
    
    struct qstr d_name;
    bpf_core_read(&d_name, sizeof(d_name), &dentry->d_name);
    
    char filename[256];
    bpf_probe_read_kernel_str(filename, sizeof(filename), d_name.name);
    
    bpf_printk("vfs_read: %s\n", filename);
    return 0;
}

/* Option 3: CO-RE enum value access */
SEC("kprobe/do_exit")
int kprobe_do_exit(struct pt_regs *ctx) {
    struct task_struct *task = (struct task_struct *)bpf_get_current_task();
    
    /* Read the process exit code */
    int exit_code = BPF_CORE_READ(task, exit_code);
    
    /* Read the process flags */
    unsigned int flags = BPF_CORE_READ(task, flags);
    
    /* Check whether this is a kernel thread */
    bool is_kthread = (flags & PF_KTHREAD) != 0;
    
    if (!is_kthread) {
        bpf_printk("Process exiting: pid=%d, exit_code=%d\n",
                   BPF_CORE_READ(task, pid), exit_code);
    }
    
    return 0;
}

/* Option 4: conditional compilation for compatibility across kernel versions */
struct task_struct___old {
    int pid;
    /* fields present on older kernels */
} __attribute__((preserve_access_index));

struct task_struct___new {
    int pid;
    __u64 random_seed;  /* a field added on newer kernels */
} __attribute__((preserve_access_index));

SEC("kprobe/sys_fork")
int handle_fork(struct pt_regs *ctx) {
    struct task_struct *task = (void *)bpf_get_current_task();
    
    /* CO-RE: check whether the field exists */
    if (bpf_core_field_exists(((struct task_struct___new *)0)->random_seed)) {
        /* Newer kernel: access the new field */
        __u64 seed = BPF_CORE_READ((struct task_struct___new *)task, random_seed);
        bpf_printk("New kernel, seed=%llu\n", seed);
    } else {
        /* Older kernel: use a compatible fallback */
        bpf_printk("Old kernel, no random_seed field\n");
    }
    
    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

```bash
# BTF/CO-RE tooling operations

# Check whether the kernel supports BTF
ls /sys/kernel/btf/vmlinux

# Generate vmlinux.h (contains all kernel types)
bpftool btf dump file /sys/kernel/btf/vmlinux format c > vmlinux.h

# View a program's BTF information
bpftool prog dump xlated id <id> linum  # show source line numbers
bpftool map dump id <id>                # show structured data

# Verify CO-RE relocation information
llvm-readelf -S my_prog.o | grep BTF   # view the BTF section
bpftool btf dump file my_prog.o        # view the program's BTF

# Use pahole to generate BTF information (older kernels)
pahole -J --btf_encode_detached external.btf vmlinux
```

## 7.3 Using vmlinux.h

```c
/* Using vmlinux.h avoids the need for kernel headers */

/* Traditional approach: requires many kernel headers */
#include <linux/types.h>
#include <linux/sched.h>
#include <linux/socket.h>
#include <linux/net.h>
#include <linux/in.h>
#include <linux/tcp.h>
// ... potentially dozens of headers, tied to a specific kernel version

/* CO-RE approach: only vmlinux.h is needed */
#include "vmlinux.h"  /* contains all kernel types */
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_core_read.h>

/* Now all kernel structs can be used directly */
SEC("fentry/tcp_v4_connect")
int BPF_PROG(fentry_tcp_v4_connect, struct sock *sk) {
    /* Directly access task_struct, sock, file, and other kernel structs */
    struct task_struct *task = (void *)bpf_get_current_task_btf();
    
    pid_t pid = BPF_CORE_READ(task, pid);
    uid_t uid = BPF_CORE_READ(task, cred, uid.val);
    
    /* Read socket information */
    __u32 daddr = BPF_CORE_READ(sk, __sk_common.skc_daddr);
    __u16 dport = BPF_CORE_READ(sk, __sk_common.skc_dport);
    
    bpf_printk("PID %d (uid=%d) connecting to %x:%d\n",
               pid, uid, bpf_ntohl(daddr), bpf_ntohs(dport));
    return 0;
}
```

---

<!-- chunk: 8. Best Practices and Common Issues -->## 8. Best Practices and Common Issues

## 8.1 Performance Best Practices

```c
/* Best practice 1: use Per-CPU Maps to avoid lock contention */

/* Not recommended: a global Hash Map (requires atomic operations) */
struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __type(key, __u32);
    __type(value, __u64);
} global_counters SEC(".maps");

/* Recommended: a Per-CPU Hash Map (lock-free) */
struct {
    __uint(type, BPF_MAP_TYPE_PERCPU_HASH);
    __type(key, __u32);
    __type(value, __u64);
} percpu_counters SEC(".maps");

/* Best practice 2: use Ring Buffer instead of Perf Event Array (5.8+) */

/* Old approach: Perf Event Array */
struct {
    __uint(type, BPF_MAP_TYPE_PERF_EVENT_ARRAY);
    __uint(key_size, sizeof(__u32));
    __uint(value_size, sizeof(__u32));
} old_events SEC(".maps");

/* Recommended approach: Ring Buffer (more memory-efficient) */
struct {
    __uint(type, BPF_MAP_TYPE_RINGBUF);
    __uint(max_entries, 1 << 24);
} ringbuf_events SEC(".maps");

/* Best practice 3: use __always_inline to reduce function-call overhead */
static __always_inline int parse_ethhdr(struct xdp_md *ctx,
                                         struct ethhdr **eth,
                                         __u16 *proto) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;
    
    *eth = data;
    if ((void *)(*eth + 1) > data_end)
        return -1;
    
    *proto = bpf_ntohs((*eth)->h_proto);
    return 0;
}

/* Best practice 4: return early to avoid unnecessary processing */
SEC("xdp")
int fast_filter(struct xdp_md *ctx) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;
    
    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        return XDP_DROP;  /* early return */
    
    /* Only handle IPv4 */
    if (eth->h_proto != bpf_htons(ETH_P_IP))
        return XDP_PASS;  /* early return */
    
    struct iphdr *ip = (void *)(eth + 1);
    if ((void *)(ip + 1) > data_end)
        return XDP_DROP;
    
    /* ... continue processing */
    return XDP_PASS;
}

/* Best practice 5: use BPF_MAP_TYPE_ARRAY instead of HASH for fixed-size data */
/* Array is ~3-5x faster than Hash, since direct indexing avoids hash computation */
struct {
    __uint(type, BPF_MAP_TYPE_ARRAY);  /* instead of BPF_MAP_TYPE_HASH */
    __uint(max_entries, 256);          /* indexed by protocol number */
    __type(key, __u32);
    __type(value, __u64);
} proto_stats SEC(".maps");
```

## 8.2 Debugging Tips

```bash
# Debugging tip 1: view verifier logs
# Enable verbose logging in libbpf
cat > debug_load.c << 'EOF'
#include <bpf/libbpf.h>

int main() {
    LIBBPF_OPTS(bpf_object_open_opts, opts,
        .kernel_log_level = 1 | 2,  /* verbose verifier logging */
    );
    
    struct bpf_object *obj = bpf_object__open_opts("my_prog.o", &opts);
    // ...
}
EOF

# Debugging tip 2: bpf_printk output
# Use bpf_printk inside the eBPF program to print debug information
# View the output:
cat /sys/kernel/debug/tracing/trace_pipe
# or
sudo cat /sys/kernel/tracing/trace_pipe

# Debugging tip 3: use bpftrace for quick verification
# One-liner tracing
bpftrace -e 'kprobe:do_sys_openat2 { printf("%s %s\n", comm, str(arg1)); }'
bpftrace -e 'tracepoint:syscalls:sys_enter_execve { printf("%s -> %s\n", comm, str(args->filename)); }'
bpftrace -e 'xdp:* { @[probe] = count(); }'

# Debugging tip 4: use bpftool to inspect program state
bpftool prog list                     # list all programs
bpftool prog show id <id> -p          # detailed info (JSON format)
bpftool prog dump xlated id <id>      # view bytecode (with BTF annotations)
bpftool prog dump jited id <id>       # view JIT code
bpftool prog tracelog                  # view bpf_printk output
bpftool prog profile id <id> duration 5 cycles instructions  # performance profiling

# Debugging tip 5: check program runtime statistics
echo 1 > /proc/sys/kernel/bpf_stats_enabled
bpftool prog show id <id>
# The output includes: run_cnt, run_time_ns

# Debugging tip 6: use strace to trace the bpf() syscall
strace -e bpf ./my_bpf_loader

# Debugging tip 7: check eBPF error logs
dmesg | grep -i bpf
journalctl -k | grep -i bpf
```

## 8.3 Common Issues and Solutions

```
Common Issues Quick Reference
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Issue                              Cause                    Solution
────────────────────────────────  ────────────────────── ──────────────────────────────
Verification failure: "R1 !read_ok" An uninitialized register was used   Initialize all variables
Verification failure: "invalid mem access" Pointer bounds check failed  Add a bounds check before accessing
Verification failure: "back-edge from..." A loop exists                 Use a bounded loop / pragma unroll
Verification failure: "combined stack size" Stack usage exceeds 512 bytes Use a Per-CPU Map as a heap
Load failure: EPERM               Insufficient permissions              Requires CAP_BPF or CAP_SYS_ADMIN
Load failure: EINVAL              Program type mismatch                  Check the SEC() declaration
Program rejected: "unknown func"  Called an unsupported helper           Check kernel version and program type
Map lookup returns NULL           The key does not exist (normal)        Check the return value, initialize a default
High XDP DROP rate                Program logic issue                    Use bpftrace to debug the data flow
kprobe cannot attach              The function was inlined               Use a tracepoint or raw_tracepoint instead
Missing BTF information           The kernel was not built with BTF      Use CONFIG_DEBUG_INFO_BTF=y

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

``` bash
# 🟢 Low risk: read-only/information gathering, generally no side effects
# eBPF-related configuration checks in Kubernetes
# Check the node kernel version
kubectl get nodes -o wide
kubectl debug node/<node-name> -it --image=ubuntu -- uname -r

# Check eBPF feature support
kubectl debug node/<node-name> -it --image=ubuntu -- bash -c "
  echo '=== Kernel Version ==='
  uname -r
  
  echo '=== BPF JIT ===' 
  cat /proc/sys/net/core/bpf_jit_enable
  
  echo '=== BTF Support ==='
  ls /sys/kernel/btf/vmlinux && echo 'BTF: YES' || echo 'BTF: NO'
  
  echo '=== eBPF Loaded Programs ==='
  bpftool prog list 2>/dev/null || echo 'bpftool not available'
  
  echo '=== Cilium eBPF Status ==='
  cilium status 2>/dev/null || echo 'cilium not available'
"

# Check Cilium eBPF programs
kubectl -n kube-system exec -it ds/cilium -- cilium bpf endpoint list
kubectl -n kube-system exec -it ds/cilium -- cilium bpf policy list
kubectl -n kube-system exec -it ds/cilium -- cilium bpf nat list
```
## 8.4 Security Considerations

```
eBPF Security Best Practices
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. Access control
   • Use CAP_BPF (5.8+) instead of CAP_SYS_ADMIN
   • Restrict unprivileged BPF: /proc/sys/kernel/unprivileged_bpf_disabled
   • Restrict BPF capabilities in containers via securityContext

2. Kernel version
   • Keep the kernel patched; the eBPF verifier has had known vulnerabilities
   • Enable JIT hardening: /proc/sys/net/core/bpf_jit_harden = 2
   • Enable CONFIG_BPF_JIT_ALWAYS_ON

3. Program auditing
   • Use bpftool prog show to audit loaded eBPF programs
   • Implement eBPF program signature verification
   • Use LSM BPF hooks to restrict the bpf() syscall

4. Map access control
   • Use BPF Token to control Map creation permissions
   • Limit Map size to prevent DoS
   • Regularly audit Map contents

5. Supply chain security
   • Verify the provenance of eBPF programs
   • Use build-time signing
   • Cilium uses image signing to guarantee program integrity
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

```yaml
# Kubernetes Pod security configuration - allowing eBPF (only the necessary capabilities)
apiVersion: v1
kind: Pod
metadata:
  name: ebpf-monitor
spec:
  containers:
  - name: monitor
    image: my-ebpf-monitor:latest
    securityContext:
      capabilities:
        add:
        - BPF           # CAP_BPF (Linux 5.8+)
        - PERFMON       # CAP_PERFMON (perf events)
        - SYS_RESOURCE  # adjust rlimit (MAP_LOCKED)
        drop:
        - ALL
      readOnlyRootFilesystem: true
      runAsNonRoot: false  # eBPF usually requires root
      privileged: false    # full privilege is not required
    volumeMounts:
    - name: bpf-fs
      mountPath: /sys/fs/bpf
    - name: debugfs
      mountPath: /sys/kernel/debug
      readOnly: true
  volumes:
  - name: bpf-fs
    hostPath:
      path: /sys/fs/bpf
      type: Directory
  - name: debugfs
    hostPath:
      path: /sys/kernel/debug
      type: Directory
  hostPID: true  # access to information about all processes (monitoring use case only)
  hostNetwork: true  # XDP/TC programs may require this
```

---

<!-- chunk: 📊 eBPF Program Type Quick Reference -->## 📊 eBPF Program Type Quick Reference

| Program Type | Trigger Point | Context | Return Value | Primary Use |
|----------|----------|--------|--------|----------|
| XDP | NIC driver packet receipt | `xdp_md` | XDP_DROP/PASS/TX/REDIRECT | DDoS protection, load balancing |
| TC (cls_bpf) | TC ingress/egress | `__sk_buff` | TC_ACT_OK/SHOT/REDIRECT | Traffic control, NAT |
| kprobe | Kernel function entry | `pt_regs` | 0 | Kernel function tracing |
| kretprobe | Kernel function return | `pt_regs` | 0 | Return value tracing |
| fentry/fexit | Kernel function (BTF) | Function arguments | 0 | High-performance tracing (recommended) |
| tracepoint | Static tracepoint | Event argument struct | 0 | Kernel event tracing |
| raw_tracepoint | Raw tracepoint | `bpf_raw_tracepoint_args` | 0 | High-performance event tracing |
| LSM | Security policy point | Security function arguments | 0/error code | Runtime security policy |
| cgroup_skb | cgroup packet | `__sk_buff` | 0/1 (drop/allow) | Container network control |
| cgroup_sock | Socket operation | `bpf_sock` | 0/1 | Socket control |
| socket_filter | Socket filtering | `__sk_buff` | packet length/0 | Traffic analysis |
| sk_msg | sendmsg path | `sk_msg_md` | SK_PASS/DROP | Message filtering/redirection |
| sk_skb | recv skb | `__sk_buff` | SK_PASS/DROP | Socket Map redirection |
| perf_event | Performance event | `bpf_perf_event_data` | 0 | CPU profiling, sampling |
| uprobe/uretprobe | User-space function | `pt_regs` | 0 | User-space tracing |
| USDT | User-space static probe | Probe arguments | 0 | Application observability |

---

<!-- chunk: 🔗 Related Resources -->## 🔗 Related Resources

- **Kernel documentation**: [kernel.org/doc/html/latest/bpf](https://www.kernel.org/doc/html/latest/bpf/index.html)

---

<!-- chunk: Obsidian Related Documents -->## Obsidian Related Documents

- domain-03-networking-traffic KUDIG Database — Global MOC
- [[domain-03-networking-traffic/README.md|Domain 03: eBPF Technology Stack]]
- Domain 03 eBPF Technology — Open Source Project Index
- [[domain-03-networking-traffic/04-ebpf/02-ebpf-map-types-data-structures.md|02 eBPF Map Types and Data Structures]]
- Cilium CNI Architecture and Deployment
- Cilium Network Policy L3/L4/L7
- Cilium Service Mesh Sidecar-less Architecture
- Tetragon Runtime Security
- Hubble Network Observability
- bcc and bpftrace Tools
- eBPF Performance Optimization Practice
- eBPF Security Applications and Use Cases

## See Also

- 09-ebpf-performance-optimization
- 10-ebpf-security-applications
- 02-ebpf-map-types-data-structures
- 03-cilium-cni-architecture


<!-- risk-assessed -->
