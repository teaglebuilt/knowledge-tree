---
title: eBPF Map Types and Data Structures
description: A detailed reference for eBPF Map types and data structures, covering Hash, Array, Ring Buffer, Perf Event Array, Stack/Queue, LPM Trie, and Map-in-Map, along with kernel/user-space communication patterns and performance tuning guidance.
summary: eBPF Maps are key-value storage data structures in the kernel and are the core mechanism for communication between eBPF programs and between eBPF programs and user-space applications. This guide covers every Map type, their internal structures, usage patterns, and performance characteristics.
category: ebpf-technology
tags:
- k8s
- ebpf
- cilium
- networking
- observability
- daemonset
- rag
tier: supporting
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
- What is eBPF Map Types and Data Structures
- How to use eBPF Map Types and Data Structures
- Kubernetes eBPF technology best practices
trigger_keywords:
- eBPF
- Map
- Types and Data Structures
- eBPF
- Map
- Types
- and
- Data
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
- name: Dillan Teagle
  role: contributor
---

> **Production Safety Notice**
>
> This document contains operational commands that can be executed directly. Before running them, confirm: the target cluster and Namespace are correct; you have sufficient RBAC permissions; and the commands have been validated in a non-production environment. Command risk levels: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state, usually rollbackable), 🟢 Low risk / read-only (information gathering, no side effects).




# eBPF Map Types and Data Structures

> **Scope**: eBPF program development, kernel/user-space communication | **Expert Level**: ⭐⭐⭐⭐⭐ | **Last Updated**: 2026-03-03
> **Kernel Requirements**: Linux Kernel >= 4.3 (basic Maps) | >= 5.1 (Ring Buffer) | >= 5.8 (newer features)

---

<!-- chunk: 📋 Table of Contents -->## 📋 Table of Contents

1. [eBPF Map Overview and Purpose](#1-ebpf-map-overview-and-purpose)
2. [Hash Map Types](#2-hash-map-types)
3. [Array Map Types](#3-array-map-types)
4. [Ring Buffer: High-Performance Event Delivery](#4-ring-buffer-high-performance-event-delivery)
5. [Perf Event Array](#5-perf-event-array)
6. [Stack and Queue Maps](#6-stack-and-queue-maps)
7. [LPM Trie Map](#7-lpm-trie-map)
8. [Map-in-Map Nested Structures](#8-map-in-map-nested-structures)
9. [User-Space and Kernel-Space Communication Patterns](#9-user-space-and-kernel-space-communication-patterns)
10. [Map Performance Optimization and Tuning](#10-map-performance-optimization-and-tuning)
11. [Practical bpftool Map Operations](#11-practical-bpftool-map-operations)

---

<!-- chunk: 1. eBPF Map Overview and Purpose -->## 1. eBPF Map Overview and Purpose

## 1.1 What is an eBPF Map

An eBPF Map is a key-value storage data structure in the kernel, and it is the core mechanism for communication between eBPF programs and between eBPF programs and user-space applications. It provides functionality such as persistent storage, state sharing, and data transfer.

```
Core Roles of eBPF Maps
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────────────────────────────────────────────────────────────────┐
│                     eBPF Map Use Cases                               │
│                                                                     │
│  1. State persistence                                               │
│     Each invocation of an eBPF program is stateless; Maps provide  │
│     persistent state across invocations                            │
│     Examples: connection tracking tables, statistics counters,     │
│     IP blacklists                                                   │
│                                                                     │
│  2. Communication between eBPF programs                            │
│     Multiple eBPF programs exchange data via a shared Map          │
│     Example: an XDP program writes a forwarding decision to a Map, │
│     and a TC program reads it                                      │
│                                                                     │
│  3. User-space ↔ kernel-space communication                        │
│     A user-space program reads eBPF statistics                     │
│     A user-space program pushes configuration to an eBPF program   │
│                                                                     │
│  4. Tail call table                                                 │
│     BPF_MAP_TYPE_PROG_ARRAY: stores program references to build a  │
│     program chain                                                   │
│                                                                     │
│  5. Event output                                                    │
│     Ring Buffer / Perf Event Array: kernel → user-space event flow │
└─────────────────────────────────────────────────────────────────────┘

eBPF Map access interfaces:

  Kernel side (eBPF program):        User side (user-space program):
  ┌──────────────────────────┐      ┌──────────────────────────────┐
  │ bpf_map_lookup_elem()    │      │ bpf_map_lookup_elem()        │
  │ bpf_map_update_elem()    │      │ bpf_map_update_elem()        │
  │ bpf_map_delete_elem()    │      │ bpf_map_delete_elem()        │
  │ bpf_map_push_elem()      │      │ bpf_map_get_next_key()       │
  │ bpf_map_pop_elem()       │      │ bpf_map_lookup_batch()       │
  │ bpf_for_each_map_elem()  │      │ bpf_map_update_batch()       │
  └──────────────────────────┘      └──────────────────────────────┘
               │                                 │
               └─────────────┬───────────────────┘
                             ▼
                    ┌──────────────────┐
                    │   eBPF Map       │
                    │  (kernel memory) │
                    └──────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 1.2 Overview of All Map Types

```
eBPF Map Type Classification (Linux 6.x)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Category          Map Type                               Introduced  Primary Use
──────────────── ────────────────────────────────────── ──────── ────────────────────
Hash             BPF_MAP_TYPE_HASH                      4.3      general-purpose key-value storage
                 BPF_MAP_TYPE_PERCPU_HASH               4.6      lock-free per-CPU counting
                 BPF_MAP_TYPE_LRU_HASH                  4.10     bounded-capacity cache
                 BPF_MAP_TYPE_LRU_PERCPU_HASH           4.10     Per-CPU LRU
                 BPF_MAP_TYPE_HASH_OF_MAPS              4.12     Map nesting

Array            BPF_MAP_TYPE_ARRAY                     3.19     fixed-size array
                 BPF_MAP_TYPE_PERCPU_ARRAY              4.6      Per-CPU array
                 BPF_MAP_TYPE_PROG_ARRAY                4.2      tail-call program table
                 BPF_MAP_TYPE_ARRAY_OF_MAPS             4.12     nested Map array

Events           BPF_MAP_TYPE_PERF_EVENT_ARRAY          4.3      perf event output
                 BPF_MAP_TYPE_RINGBUF                   5.8      high-performance ring buffer

Networking       BPF_MAP_TYPE_SOCKMAP                   4.14     socket redirection
                 BPF_MAP_TYPE_SOCKHASH                  4.18     socket hash
                 BPF_MAP_TYPE_DEVMAP                    4.14     device redirection
                 BPF_MAP_TYPE_DEVMAP_HASH               5.4      hashed device Map
                 BPF_MAP_TYPE_CPUMAP                    4.15     CPU redirection
                 BPF_MAP_TYPE_XSKMAP                    4.18     AF_XDP sockets
                 BPF_MAP_TYPE_REUSEPORT_SOCKARRAY        4.19    port reuse

Storage          BPF_MAP_TYPE_SK_STORAGE                5.2      per-socket local storage
                 BPF_MAP_TYPE_INODE_STORAGE             5.10     per-inode local storage
                 BPF_MAP_TYPE_TASK_STORAGE               5.11     per-task local storage
                 BPF_MAP_TYPE_CGROUP_STORAGE            4.19     cgroup storage
                 BPF_MAP_TYPE_PERCPU_CGROUP_STORAGE      4.20    Per-CPU cgroup storage

Other            BPF_MAP_TYPE_STACK_TRACE               4.6      call-stack tracing
                 BPF_MAP_TYPE_CGROUP_ARRAY              4.8      cgroup path array
                 BPF_MAP_TYPE_LPM_TRIE                  4.11     longest prefix match
                 BPF_MAP_TYPE_STACK                     4.20     LIFO queue
                 BPF_MAP_TYPE_QUEUE                     4.20     FIFO queue
                 BPF_MAP_TYPE_STRUCT_OPS                5.6      kernel struct operations
                 BPF_MAP_TYPE_BLOOM_FILTER              5.16     Bloom filter
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 1.3 Map Creation and Basic Operations

```c
/* Ways to define a Map inside an eBPF program */
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

/* Option 1: BTF style (recommended, the modern approach) */
struct {
    __uint(type, BPF_MAP_TYPE_HASH);          /* Map type */
    __uint(max_entries, 10240);               /* maximum number of entries */
    __type(key, __u32);                       /* key type (size inferred automatically) */
    __type(value, __u64);                     /* value type */
    __uint(map_flags, BPF_F_NO_PREALLOC);    /* optional flags */
} my_hash_map SEC(".maps");

/* Option 2: traditional style (for compatibility with older code) */
struct bpf_map_def SEC("maps") my_old_map = {
    .type = BPF_MAP_TYPE_HASH,
    .key_size = sizeof(__u32),
    .value_size = sizeof(__u64),
    .max_entries = 10240,
};

/* Option 3: created from user space (libbpf) */
/* Used for dynamic creation, or for Maps that must be configured before program load */
```

```c
/* User-space Map operations */
#include <bpf/libbpf.h>
#include <bpf/bpf.h>

int main() {
    /* Create a Hash Map */
    LIBBPF_OPTS(bpf_map_create_opts, opts,
        .map_flags = BPF_F_NO_PREALLOC,
    );
    
    int map_fd = bpf_map_create(
        BPF_MAP_TYPE_HASH,    /* type */
        "my_map",             /* name (optional) */
        sizeof(__u32),        /* key_size */
        sizeof(__u64),        /* value_size */
        10240,                /* max_entries */
        &opts
    );
    
    if (map_fd < 0) {
        perror("bpf_map_create");
        return 1;
    }
    
    /* CRUD operations */
    __u32 key = 42;
    __u64 value = 1000;
    
    /* Create/update */
    bpf_map_update_elem(map_fd, &key, &value, BPF_ANY);
    /* BPF_ANY: create if absent, update if present */
    /* BPF_NOEXIST: only create (if absent) */
    /* BPF_EXIST: only update (if present) */
    
    /* Lookup */
    __u64 result;
    int ret = bpf_map_lookup_elem(map_fd, &key, &result);
    if (ret == 0)
        printf("key=%u, value=%llu\n", key, result);
    
    /* Delete */
    bpf_map_delete_elem(map_fd, &key);
    
    /* Iterate over all keys */
    __u32 prev_key, next_key;
    memset(&prev_key, 0, sizeof(prev_key));
    while (bpf_map_get_next_key(map_fd, &prev_key, &next_key) == 0) {
        bpf_map_lookup_elem(map_fd, &next_key, &result);
        printf("key=%u, value=%llu\n", next_key, result);
        prev_key = next_key;
    }
    
    /* Batch operations (5.6+) */
    __u32 keys[100];
    __u64 values[100];
    __u32 count = 100;
    void *in_batch = NULL, *out_batch;
    
    LIBBPF_OPTS(bpf_map_batch_opts, batch_opts,
        .elem_flags = 0,
        .flags = 0,
    );
    
    bpf_map_lookup_batch(map_fd, &in_batch, &out_batch,
                         keys, values, &count, &batch_opts);
    
    close(map_fd);
    return 0;
}
```

---

<!-- chunk: 2. Hash Map Types -->## 2. Hash Map Types

## 2.1 BPF_MAP_TYPE_HASH: The Basic Hash Table

```
Hash Map Internal Structure
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌──────────────────────────────────────────────────────────────────┐
│                   BPF_MAP_TYPE_HASH                              │
│                                                                  │
│  Implementation: the kernel hashtab (kernel/bpf/hashtab.c)      │
│  Locking: a per-bucket spinlock (one lock per hash bucket)       │
│  Memory: preallocated (default) or allocated on demand           │
│  (BPF_F_NO_PREALLOC)                                             │
│                                                                  │
│  Hash bucket array                                               │
│  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐            │
│  │  0  │  1  │  2  │  3  │  4  │  5  │  6  │  7  │ ...        │
│  └──┬──┴──┬──┴──┬──┴──┬──┴─────┴─────┴─────┴─────┘            │
│     │     │     │     │                                         │
│     ▼     ▼     ▼     ▼                                         │
│  ┌─────┐ NULL ┌─────┐ NULL                                      │
│  │k1:v1│     │k3:v3│                                            │
│  └──┬──┘     └─────┘                                            │
│     │                                                           │
│     ▼                                                           │
│  ┌─────┐                                                        │
│  │k2:v2│  (hash collision, chained)                             │
│  └─────┘                                                        │
│                                                                  │
│  Operation complexity:                                          │
│  • Lookup: O(1) average, O(n) worst case                        │
│  • Insert: O(1) average                                          │
│  • Delete: O(1) average                                          │
│  • Iterate: O(capacity) (must scan every bucket)                │
└──────────────────────────────────────────────────────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

```c
/* Full Hash Map usage example - TCP connection tracking */
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <linux/tcp.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_endian.h>

/* Connection 4-tuple used as the key */
struct conn_tuple {
    __u32 src_ip;
    __u32 dst_ip;
    __u16 src_port;
    __u16 dst_port;
    __u8  proto;
    __u8  _pad[3];  /* alignment padding */
};

/* Connection statistics used as the value */
struct conn_stats {
    __u64 bytes_rx;
    __u64 bytes_tx;
    __u64 pkts_rx;
    __u64 pkts_tx;
    __u64 last_seen_ns;
    __u8  state;  /* TCP state */
};

/* Connection-tracking Hash Map */
struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __uint(max_entries, 65536);
    __type(key, struct conn_tuple);
    __type(value, struct conn_stats);
    __uint(map_flags, BPF_F_NO_PREALLOC);  /* allocate on demand to save memory */
} conn_track SEC(".maps");

static __always_inline void
update_conn_stats(struct conn_tuple *tuple, __u32 pkt_len, bool is_rx) {
    struct conn_stats *stats = bpf_map_lookup_elem(&conn_track, tuple);
    
    if (stats) {
        /* Update an existing connection */
        if (is_rx) {
            __sync_fetch_and_add(&stats->bytes_rx, pkt_len);
            __sync_fetch_and_add(&stats->pkts_rx, 1);
        } else {
            __sync_fetch_and_add(&stats->bytes_tx, pkt_len);
            __sync_fetch_and_add(&stats->pkts_tx, 1);
        }
        stats->last_seen_ns = bpf_ktime_get_ns();
    } else {
        /* Create a new connection */
        struct conn_stats new_stats = {
            .last_seen_ns = bpf_ktime_get_ns(),
        };
        if (is_rx) {
            new_stats.bytes_rx = pkt_len;
            new_stats.pkts_rx = 1;
        } else {
            new_stats.bytes_tx = pkt_len;
            new_stats.pkts_tx = 1;
        }
        /* BPF_NOEXIST: avoid a race condition */
        bpf_map_update_elem(&conn_track, tuple, &new_stats, BPF_NOEXIST);
    }
}

SEC("xdp")
int xdp_conn_track(struct xdp_md *ctx) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;
    __u32 pkt_len = ctx->data_end - ctx->data;
    
    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        return XDP_PASS;
    
    if (eth->h_proto != bpf_htons(ETH_P_IP))
        return XDP_PASS;
    
    struct iphdr *ip = (void *)(eth + 1);
    if ((void *)(ip + 1) > data_end)
        return XDP_PASS;
    
    struct conn_tuple tuple = {
        .src_ip = ip->saddr,
        .dst_ip = ip->daddr,
        .proto = ip->protocol,
    };
    
    if (ip->protocol == IPPROTO_TCP) {
        __u32 ip_hdr_len = ip->ihl * 4;
        struct tcphdr *tcp = (void *)ip + ip_hdr_len;
        if ((void *)(tcp + 1) > data_end)
            return XDP_PASS;
        
        tuple.src_port = tcp->source;
        tuple.dst_port = tcp->dest;
    } else if (ip->protocol == IPPROTO_UDP) {
        /* Similar handling... */
    }
    
    update_conn_stats(&tuple, pkt_len, true);
    return XDP_PASS;
}

char LICENSE[] SEC("license") = "GPL";
```

## 2.2 BPF_MAP_TYPE_PERCPU_HASH: The Per-CPU Hash Table

```c
/* Per-CPU Hash Map - lock-free, high-concurrency counting */
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

/* Per-CPU Hash: each CPU core maintains its own independent copy of the data */
struct {
    __uint(type, BPF_MAP_TYPE_PERCPU_HASH);
    __uint(max_entries, 1024);
    __type(key, __u32);    /* process PID */
    __type(value, __u64);  /* syscall count */
} syscall_counts SEC(".maps");

SEC("tracepoint/raw_syscalls/sys_enter")
int count_syscalls(struct trace_event_raw_sys_enter *ctx) {
    __u32 pid = bpf_get_current_pid_tgid() >> 32;
    
    /* Per-CPU Map operations require no atomic instructions; they access the current CPU's own copy directly */
    __u64 *count = bpf_map_lookup_elem(&syscall_counts, &pid);
    if (count) {
        (*count)++;  /* no atomic op needed, faster than PERCPU_ARRAY */
    } else {
        __u64 init = 1;
        bpf_map_update_elem(&syscall_counts, &pid, &init, BPF_NOEXIST);
    }
    
    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

```c
/* Reading a Per-CPU Hash Map from user space */
#include <bpf/libbpf.h>
#include <bpf/bpf.h>

void read_percpu_hash(int map_fd) {
    int num_cpus = libbpf_num_possible_cpus();
    __u64 values[num_cpus];
    __u32 key, next_key;
    
    /* Iterate over all keys */
    memset(&key, 0, sizeof(key));
    while (bpf_map_get_next_key(map_fd, &key, &next_key) == 0) {
        /* Each lookup returns an array of values, one per CPU */
        if (bpf_map_lookup_elem(map_fd, &next_key, values) == 0) {
            __u64 total = 0;
            for (int i = 0; i < num_cpus; i++) {
                total += values[i];
            }
            printf("PID %u: %llu syscalls (across %d CPUs)\n",
                   next_key, total, num_cpus);
        }
        key = next_key;
    }
}
```

## 2.3 BPF_MAP_TYPE_LRU_HASH: The LRU Hash Table

```c
/* LRU Hash Map - automatically evicts the least-recently-used entries */
/* Suitable for connection tracking, caching, and similar scenarios */

#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

/* 
 * LRU Hash characteristics:
 * • When the Map is full, the least-recently-accessed entry is evicted automatically
 * • Each NUMA node maintains an independent LRU list
 * • Supports the BPF_F_NO_COMMON_LRU flag: a separate per-CPU LRU (less contention)
 */

struct flow_entry {
    __u64 bytes;
    __u64 packets;
    __u64 last_active;
    __u8  tcp_flags;
};

struct {
    __uint(type, BPF_MAP_TYPE_LRU_HASH);
    __uint(max_entries, 1000000);  /* one million connections */
    __type(key, __u64);           /* flow hash value */
    __type(value, struct flow_entry);
    /* Note: LRU Hash does not support BPF_F_NO_PREALLOC */
    /* Memory is preallocated at creation time: max_entries * (key_size + value_size + header) */
} flow_table SEC(".maps");

/* LRU variant: an independent LRU per CPU, reducing lock contention */
struct {
    __uint(type, BPF_MAP_TYPE_LRU_PERCPU_HASH);
    __uint(max_entries, 100000);
    __type(key, __u32);
    __type(value, __u64);
} percpu_lru_map SEC(".maps");

SEC("xdp")
int track_flows(struct xdp_md *ctx) {
    /* Simplified: use the packet's RX queue index as the flow ID */
    __u64 flow_id = ctx->rx_queue_index;  /* a real implementation should hash the 5-tuple */
    
    struct flow_entry *entry = bpf_map_lookup_elem(&flow_table, &flow_id);
    if (entry) {
        /* Update an existing flow - the LRU updates the access time automatically */
        __sync_fetch_and_add(&entry->packets, 1);
        entry->last_active = bpf_ktime_get_ns();
    } else {
        /* A new flow - if the Map is full, the LRU automatically evicts the oldest entry */
        struct flow_entry new_entry = {
            .packets = 1,
            .bytes = ctx->data_end - ctx->data,
            .last_active = bpf_ktime_get_ns(),
        };
        bpf_map_update_elem(&flow_table, &flow_id, &new_entry, BPF_ANY);
    }
    
    return XDP_PASS;
}

char LICENSE[] SEC("license") = "GPL";
```

## 2.4 Hash Map Comparison Table

```
Hash Map Type Comparison
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Characteristic          HASH    PERCPU_HASH  LRU_HASH   LRU_PERCPU_HASH
────────────────────── ─────── ─────────── ─────────── ───────────────
Concurrency safety      bucket lock  lock-free  bucket lock  lock-free
Memory efficiency       medium   low (N copies) high (prealloc) low (prealloc×N)
Automatic eviction      no       no           yes          yes
Memory allocation       on-demand/prealloc on-demand/prealloc prealloc-only prealloc-only
Real max-entry memory   small    large (×CPU count) fixed  fixed (×CPU count)
Read/write performance  medium   highest      medium       high
Iteration support       yes      yes          yes          yes
Suitable use case       general  high-frequency lock-free  connection    high-concurrency
                        key-value store  counting/stats   tracking cache traffic stats

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

<!-- chunk: 3. Array Map Types -->## 3. Array Map Types

## 3.1 BPF_MAP_TYPE_ARRAY: The Basic Array

```
Array Map Internal Structure
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌──────────────────────────────────────────────────────────────────┐
│                   BPF_MAP_TYPE_ARRAY                             │
│                                                                  │
│  Implementation: a preallocated, contiguous memory array         │
│  Key: must be of type __u32 (an index), range [0, max_entries-1]│
│  Characteristics:                                                │
│  • All memory is preallocated and zero-initialized at creation  │
│  • Deletion is not supported (entries can only be zeroed)        │
│  • Atomic updates                                                │
│  • ~3-5x faster than a Hash Map (no hash computation, direct    │
│    indexing)                                                     │
│                                                                  │
│  Memory layout:                                                  │
│  index:  [0]      [1]      [2]      [3]    ...   [N-1]         │
│         ┌───────┬────────┬────────┬────────┬────┬────────┐     │
│         │value_0│value_1 │value_2 │value_3 │... │value_N │     │
│         └───────┴────────┴────────┴────────┴────┴────────┘     │
│          ↑ contiguous memory, L1/L2 cache-friendly              │
│                                                                  │
│  Operation complexity:                                          │
│  • Lookup: O(1) (direct memory access)                           │
│  • Update: O(1) (direct memory write)                             │
│  • Delete is not supported (achieved by writing a zero value)   │
│  • Iterate: O(n) (linear scan)                                   │
└──────────────────────────────────────────────────────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

```c
/* Array Map usage example - protocol statistics */
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <bpf/bpf_helpers.h>

/* Statistics indexed by protocol number (0-255, the IP protocol number) */
struct proto_stats {
    __u64 packets;
    __u64 bytes;
};

struct {
    __uint(type, BPF_MAP_TYPE_ARRAY);
    __uint(max_entries, 256);         /* up to 256 IP protocol numbers */
    __type(key, __u32);              /* protocol number (0-255) */
    __type(value, struct proto_stats);
} proto_counters SEC(".maps");

/* Global statistics array */
struct global_stats {
    __u64 total_packets;
    __u64 total_bytes;
    __u64 ipv4_packets;
    __u64 ipv6_packets;
    __u64 other_packets;
};

struct {
    __uint(type, BPF_MAP_TYPE_ARRAY);
    __uint(max_entries, 1);  /* a single global stats object */
    __type(key, __u32);
    __type(value, struct global_stats);
} global_counter SEC(".maps");

SEC("xdp")
int xdp_count_protos(struct xdp_md *ctx) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;
    __u32 pkt_len = ctx->data_end - ctx->data;
    
    /* Update global statistics */
    __u32 gkey = 0;
    struct global_stats *gs = bpf_map_lookup_elem(&global_counter, &gkey);
    if (gs) {
        __sync_fetch_and_add(&gs->total_packets, 1);
        __sync_fetch_and_add(&gs->total_bytes, pkt_len);
    }
    
    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        return XDP_PASS;
    
    __u16 proto = bpf_ntohs(eth->h_proto);
    
    if (proto == ETH_P_IP) {
        struct iphdr *ip = (void *)(eth + 1);
        if ((void *)(ip + 1) > data_end)
            return XDP_PASS;
        
        if (gs)
            __sync_fetch_and_add(&gs->ipv4_packets, 1);
        
        /* Track statistics by IP protocol number */
        __u32 ip_proto = ip->protocol;
        struct proto_stats *ps = bpf_map_lookup_elem(&proto_counters, &ip_proto);
        if (ps) {
            __sync_fetch_and_add(&ps->packets, 1);
            __sync_fetch_and_add(&ps->bytes, pkt_len);
        }
    }
    
    return XDP_PASS;
}

char LICENSE[] SEC("license") = "GPL";
```

## 3.2 BPF_MAP_TYPE_PERCPU_ARRAY: The Per-CPU Array

```c
/* Per-CPU Array - the highest-performance counter implementation */
/* Each CPU maintains an independent copy, with no locks or atomic operations */

#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

/*
 * Per-CPU Array is the fastest counter implementation in eBPF:
 * • Completely lock-free (independent per-CPU copies)
 * • No atomic operations needed (only a single core accesses each per-CPU copy)
 * • CPU cache-friendly (good data locality)
 * • Well suited to high-frequency update scenarios
 */

/* XDP action statistics */
struct xdp_action_stats {
    __u64 aborted;
    __u64 drop;
    __u64 pass;
    __u64 tx;
    __u64 redirect;
};

struct {
    __uint(type, BPF_MAP_TYPE_PERCPU_ARRAY);
    __uint(max_entries, 1);
    __type(key, __u32);
    __type(value, struct xdp_action_stats);
} xdp_stats SEC(".maps");

/* Use a Per-CPU Array as a "heap" (a temporary large memory buffer) */
struct large_scratch {
    char buf[4096];  /* a 4 KB temporary buffer */
    __u64 timestamp;
    char comm[16];
};

struct {
    __uint(type, BPF_MAP_TYPE_PERCPU_ARRAY);
    __uint(max_entries, 1);
    __type(key, __u32);
    __type(value, struct large_scratch);
} scratch_mem SEC(".maps");

SEC("xdp")
int xdp_with_percpu_stats(struct xdp_md *ctx) {
    __u32 key = 0;
    struct xdp_action_stats *stats = bpf_map_lookup_elem(&xdp_stats, &key);
    
    /* Processing logic... */
    int action = XDP_PASS;
    
    if (stats) {
        /* No locks or atomic operations needed, just increment directly */
        switch (action) {
        case XDP_ABORTED: stats->aborted++; break;
        case XDP_DROP:    stats->drop++;    break;
        case XDP_PASS:    stats->pass++;    break;
        case XDP_TX:      stats->tx++;      break;
        case XDP_REDIRECT:stats->redirect++;break;
        }
    }
    
    return action;
}

char LICENSE[] SEC("license") = "GPL";
```

```c
/* Aggregating a Per-CPU Array from user space */
#include <bpf/libbpf.h>
#include <bpf/bpf.h>

struct xdp_action_stats {
    __u64 aborted;
    __u64 drop;
    __u64 pass;
    __u64 tx;
    __u64 redirect;
};

void print_xdp_stats(int map_fd) {
    int ncpus = libbpf_num_possible_cpus();
    struct xdp_action_stats percpu_stats[ncpus];
    struct xdp_action_stats total = {};
    __u32 key = 0;
    
    /* Read the data for every CPU */
    if (bpf_map_lookup_elem(map_fd, &key, percpu_stats) != 0) {
        perror("bpf_map_lookup_elem");
        return;
    }
    
    /* Aggregate */
    for (int i = 0; i < ncpus; i++) {
        total.aborted  += percpu_stats[i].aborted;
        total.drop     += percpu_stats[i].drop;
        total.pass     += percpu_stats[i].pass;
        total.tx       += percpu_stats[i].tx;
        total.redirect += percpu_stats[i].redirect;
    }
    
    printf("XDP Stats (Total across %d CPUs):\n", ncpus);
    printf("  ABORTED:  %llu\n", total.aborted);
    printf("  DROP:     %llu\n", total.drop);
    printf("  PASS:     %llu\n", total.pass);
    printf("  TX:       %llu\n", total.tx);
    printf("  REDIRECT: %llu\n", total.redirect);
}
```

## 3.3 BPF_MAP_TYPE_PROG_ARRAY: The Program Array (Tail Calls)

```c
/* Prog Array - implements eBPF program chains (Tail Calls) */
/*
 * Tail Call:
 * • Jumps to another eBPF program without returning
 * • Allows complex logic to be split across multiple programs
 * • Maximum nesting depth: 33 levels
 * • Behaves like assembly's JMP rather than CALL
 */

#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

/* Program index definitions */
#define PROG_IDX_TCP    0
#define PROG_IDX_UDP    1
#define PROG_IDX_ICMP   2
#define PROG_IDX_OTHER  3

/* Program array Map */
struct {
    __uint(type, BPF_MAP_TYPE_PROG_ARRAY);
    __uint(max_entries, 8);
    __type(key, __u32);
    __type(value, __u32);  /* program fd */
} prog_array SEC(".maps");

/* Dispatcher program */
SEC("xdp/dispatcher")
int xdp_dispatcher(struct xdp_md *ctx) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;
    
    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        return XDP_DROP;
    
    if (eth->h_proto != bpf_htons(ETH_P_IP))
        return XDP_PASS;
    
    struct iphdr *ip = (void *)(eth + 1);
    if ((void *)(ip + 1) > data_end)
        return XDP_DROP;
    
    /* Jump to the corresponding handler based on the protocol type */
    __u32 idx;
    switch (ip->protocol) {
    case IPPROTO_TCP:  idx = PROG_IDX_TCP;  break;
    case IPPROTO_UDP:  idx = PROG_IDX_UDP;  break;
    case IPPROTO_ICMP: idx = PROG_IDX_ICMP; break;
    default:           idx = PROG_IDX_OTHER; break;
    }
    
    /* Tail call: jump to the subprogram, does not return */
    bpf_tail_call(ctx, &prog_array, idx);
    
    /* If the tail call fails (the program was never registered), execution continues here */
    return XDP_PASS;
}

/* TCP handler */
SEC("xdp/tcp_handler")
int xdp_tcp(struct xdp_md *ctx) {
    /* Handle TCP packets */
    bpf_printk("TCP packet received\n");
    return XDP_PASS;
}

/* UDP handler */
SEC("xdp/udp_handler")
int xdp_udp(struct xdp_md *ctx) {
    /* Handle UDP packets */
    bpf_printk("UDP packet received\n");
    return XDP_PASS;
}

char LICENSE[] SEC("license") = "GPL";
```

```c
/* Registering tail-call programs from user space */
#include <bpf/libbpf.h>

void setup_tail_calls(struct bpf_object *obj) {
    struct bpf_map *prog_map = bpf_object__find_map_by_name(obj, "prog_array");
    int map_fd = bpf_map__fd(prog_map);
    
    /* Get the fd of each subprogram */
    struct bpf_program *tcp_prog = bpf_object__find_program_by_name(obj, "xdp_tcp");
    struct bpf_program *udp_prog = bpf_object__find_program_by_name(obj, "xdp_udp");
    
    int tcp_fd = bpf_program__fd(tcp_prog);
    int udp_fd = bpf_program__fd(udp_prog);
    
    /* Register into the program array */
    __u32 key_tcp = 0, key_udp = 1;
    bpf_map_update_elem(map_fd, &key_tcp, &tcp_fd, BPF_ANY);
    bpf_map_update_elem(map_fd, &key_udp, &udp_fd, BPF_ANY);
    
    printf("Tail call programs registered\n");
}
```

---

<!-- chunk: 4. Ring Buffer: High-Performance Event Delivery -->## 4. Ring Buffer: High-Performance Event Delivery

## 4.1 Ring Buffer Architecture

```
Ring Buffer vs Perf Event Array Comparison
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BPF_MAP_TYPE_PERF_EVENT_ARRAY (older approach):
┌─────────────────────────────────────────────────────────────────┐
│  Per-CPU ring buffers                                            │
│                                                                 │
│  CPU0: [ev1][ev3][ev5][    ]  ← independent buffer             │
│  CPU1: [ev2][ev4][ev6][    ]  ← independent buffer             │
│  CPU2: [   ][   ][   ][    ]  ← may be idle                    │
│  CPU3: [ev7][   ][   ][    ]  ← independent buffer             │
│                                                                 │
│  Problems:                                                      │
│  • Independent per-CPU buffers; total memory = buffer_size ×   │
│    CPU count                                                     │
│  • Events may arrive out of order (arrival order across CPUs   │
│    is not guaranteed)                                            │
│  • User space must poll the fd for every CPU                    │
│  • Data must be copied into the per-CPU buffer, then copied     │
│    again into user space (two copies)                           │
└─────────────────────────────────────────────────────────────────┘

BPF_MAP_TYPE_RINGBUF (5.8+, recommended):
┌─────────────────────────────────────────────────────────────────┐
│  A single shared ring buffer                                    │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ [event hdr][data1] [event hdr][data2] [event hdr][data3] ...│  │
│  │  ↑                                               ↑       │  │
│  │ consumer_pos (read pointer)          producer_pos (write) │  │
│  └──────────────────────────────────────────────────────────┘  │
│                                                                 │
│  Advantages:                                                     │
│  • Shared memory: total memory is fixed (does not grow with    │
│    CPU count)                                                    │
│  • Ordered events: globally ordered                              │
│  • Zero-copy: read directly via mmap, no copying required       │
│  • A single epoll fd (rather than one fd per CPU)                │
│  • Supports a reserve+submit model with atomic commits          │
└─────────────────────────────────────────────────────────────────┘

Performance comparison:
  Scenario               Perf Event Array    Ring Buffer
  ──────────────────── ─────────────────── ──────────────
  Memory usage (100KB×32CPU) 3.2 GB         100 KB
  User-space CPU usage   high (polling 32 fds) low (single fd epoll)
  Event ordering         unordered          ordered
  Number of copies       2                  0 (mmap)
  Throughput (events/s)  ~1M                ~5M
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 4.2 A Complete Ring Buffer Usage Example

```c
/* eBPF program side - using a Ring Buffer */
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_tracing.h>
#include <bpf/bpf_core_read.h>
#include "vmlinux.h"

/* Security event structure */
struct security_event {
    /* Event metadata */
    __u64 timestamp;
    __u32 pid;
    __u32 uid;
    __u32 gid;
    __u32 event_type;
    
    /* Process information */
    char comm[16];
    __u32 ppid;
    
    /* Event data (by type) */
    union {
        /* File operation */
        struct {
            char filename[256];
            int flags;
            int mode;
        } file;
        
        /* Network connection */
        struct {
            __u32 src_ip;
            __u32 dst_ip;
            __u16 src_port;
            __u16 dst_port;
            __u8  proto;
        } net;
        
        /* Process execution */
        struct {
            char exe[256];
            char args[512];
        } exec;
    };
};

/* Event types */
#define EVENT_FILE_OPEN     1
#define EVENT_FILE_EXEC     2
#define EVENT_NET_CONNECT   3
#define EVENT_NET_LISTEN    4

/* Ring Buffer Map */
struct {
    __uint(type, BPF_MAP_TYPE_RINGBUF);
    __uint(max_entries, 1 << 26);  /* a 64 MB ring buffer */
} security_events SEC(".maps");

/* Helper: fill in the common event header */
static __always_inline void
fill_event_header(struct security_event *event, __u32 type) {
    event->timestamp = bpf_ktime_get_boot_ns();
    event->pid = bpf_get_current_pid_tgid() >> 32;
    event->uid = bpf_get_current_uid_gid() & 0xFFFFFFFF;
    event->gid = bpf_get_current_uid_gid() >> 32;
    event->event_type = type;
    bpf_get_current_comm(event->comm, sizeof(event->comm));
}

/* Option 1: reserve + submit (suited to variable-size data) */
SEC("lsm/file_open")
int BPF_PROG(lsm_track_file_open, struct file *file) {
    struct security_event *event;
    
    /* Reserve space (not sent immediately) */
    event = bpf_ringbuf_reserve(&security_events, sizeof(*event), 0);
    if (!event)
        return 0;  /* buffer full, drop the event */
    
    /* Fill in the data */
    fill_event_header(event, EVENT_FILE_OPEN);
    
    /* Read the filename */
    struct dentry *dentry = BPF_CORE_READ(file, f_path.dentry);
    bpf_probe_read_kernel_str(event->file.filename, 
                               sizeof(event->file.filename),
                               BPF_CORE_READ(dentry, d_name.name));
    
    event->file.flags = BPF_CORE_READ(file, f_flags);
    
    /* Submit the event to user space */
    bpf_ringbuf_submit(event, 0);
    /* Note: the event cannot be accessed again after being submitted */
    
    return 0;
}

/* Option 2: direct output (suited to fixed-size data) */
SEC("kprobe/tcp_connect")
int BPF_KPROBE(kprobe_tcp_conn, struct sock *sk) {
    struct security_event event = {};
    
    fill_event_header(&event, EVENT_NET_CONNECT);
    
    event.net.src_ip = BPF_CORE_READ(sk, __sk_common.skc_rcv_saddr);
    event.net.dst_ip = BPF_CORE_READ(sk, __sk_common.skc_daddr);
    event.net.dst_port = BPF_CORE_READ(sk, __sk_common.skc_dport);
    event.net.proto = IPPROTO_TCP;
    
    /* Direct output, internally performs reserve+submit */
    bpf_ringbuf_output(&security_events, &event, sizeof(event), 0);
    
    return 0;
}

/* Option 3: discard a reservation (when a condition is not met) */
SEC("kprobe/vfs_write")
int BPF_KPROBE(kprobe_vfs_write, struct file *file, const char __user *buf,
               size_t count, loff_t *pos) {
    struct security_event *event;
    
    /* Only track writes larger than 1 MB */
    if (count < 1024 * 1024)
        return 0;
    
    event = bpf_ringbuf_reserve(&security_events, sizeof(*event), 0);
    if (!event)
        return 0;
    
    /* Check whether we still want to continue */
    __u32 uid = bpf_get_current_uid_gid() & 0xFFFFFFFF;
    if (uid == 0) {
        /* root user, do not monitor */
        bpf_ringbuf_discard(event, 0);  /* discard, do not send */
        return 0;
    }
    
    fill_event_header(event, EVENT_FILE_OPEN);
    bpf_ringbuf_submit(event, 0);
    
    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

```c
/* User-space side - consuming Ring Buffer events */
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <bpf/libbpf.h>
#include "security_monitor.skel.h"

static volatile bool running = true;

/* Event handling callback */
static int handle_event(void *ctx, void *data, size_t data_sz) {
    struct security_event *event = data;
    
    /* Format the timestamp */
    __u64 ts_ns = event->timestamp;
    __u64 ts_ms = ts_ns / 1000000;
    
    printf("[%llu.%03llu] ", ts_ms / 1000, ts_ms % 1000);
    printf("PID=%-6d UID=%-5d COMM=%-16s ", 
           event->pid, event->uid, event->comm);
    
    switch (event->event_type) {
    case EVENT_FILE_OPEN:
        printf("FILE_OPEN flags=0x%x file=%s\n",
               event->file.flags, event->file.filename);
        break;
        
    case EVENT_NET_CONNECT: {
        char src[16], dst[16];
        uint32_t src_ip = ntohl(event->net.src_ip);
        uint32_t dst_ip = ntohl(event->net.dst_ip);
        snprintf(src, sizeof(src), "%d.%d.%d.%d",
                 (src_ip >> 24) & 0xFF, (src_ip >> 16) & 0xFF,
                 (src_ip >> 8) & 0xFF, src_ip & 0xFF);
        snprintf(dst, sizeof(dst), "%d.%d.%d.%d",
                 (dst_ip >> 24) & 0xFF, (dst_ip >> 16) & 0xFF,
                 (dst_ip >> 8) & 0xFF, dst_ip & 0xFF);
        printf("NET_CONNECT %s -> %s:%d\n",
               src, dst, ntohs(event->net.dst_port));
        break;
    }
    
    default:
        printf("UNKNOWN event_type=%d\n", event->event_type);
    }
    
    return 0;
}

int main(int argc, char *argv[]) {
    struct security_monitor_bpf *skel;
    struct ring_buffer *rb;
    int err;
    
    /* Load the eBPF program */
    skel = security_monitor_bpf__open_and_load();
    if (!skel) {
        fprintf(stderr, "Failed to load BPF\n");
        return 1;
    }
    
    /* Attach the LSM/kprobe programs */
    err = security_monitor_bpf__attach(skel);
    if (err) {
        fprintf(stderr, "Failed to attach BPF\n");
        goto cleanup;
    }
    
    /* Create the Ring Buffer consumer */
    rb = ring_buffer__new(
        bpf_map__fd(skel->maps.security_events),
        handle_event,   /* callback function */
        NULL,           /* callback context */
        NULL            /* options */
    );
    if (!rb) {
        fprintf(stderr, "Failed to create ring buffer\n");
        goto cleanup;
    }
    
    printf("Monitoring security events (Ctrl-C to stop)...\n");
    
    signal(SIGINT, [](int s){ running = false; });
    
    /* Event loop */
    while (running) {
        /* Wait for and process events, with a 100ms timeout */
        err = ring_buffer__poll(rb, 100);
        if (err == -EINTR)
            break;
        if (err < 0) {
            fprintf(stderr, "Ring buffer poll error: %d\n", err);
            break;
        }
        /* err == 0: timeout, no events
           err > 0: processed err events */
    }
    
    ring_buffer__free(rb);

cleanup:
    security_monitor_bpf__destroy(skel);
    return 0;
}
```

## 4.3 Advanced Ring Buffer Features

```c
/* Advanced Ring Buffer features */

/* Feature 1: BPF_RB_NO_WAKEUP / BPF_RB_FORCE_WAKEUP flags */
/* Control when user space is woken up */
SEC("kprobe/batch_events")
int batch_events(struct pt_regs *ctx) {
    /* When submitting in a batch, only the last event wakes up user space */
    struct event *e1 = bpf_ringbuf_reserve(&rb, sizeof(*e1), 0);
    if (e1) {
        /* Fill in data... */
        bpf_ringbuf_submit(e1, BPF_RB_NO_WAKEUP);  /* do not wake up */
    }
    
    struct event *e2 = bpf_ringbuf_reserve(&rb, sizeof(*e2), 0);
    if (e2) {
        /* Fill in data... */
        bpf_ringbuf_submit(e2, BPF_RB_FORCE_WAKEUP);  /* force a wakeup */
    }
    
    return 0;
}

/* Feature 2: query the remaining Ring Buffer space */
SEC("kprobe/check_space")
int check_ringbuf_space(struct pt_regs *ctx) {
    /* Check whether there is enough space */
    __u64 avail = bpf_ringbuf_query(&rb, BPF_RB_AVAIL_DATA);
    __u64 ring_size = bpf_ringbuf_query(&rb, BPF_RB_RING_SIZE);
    __u64 cons_pos = bpf_ringbuf_query(&rb, BPF_RB_CONS_POS);
    __u64 prod_pos = bpf_ringbuf_query(&rb, BPF_RB_PROD_POS);
    
    /* If the buffer is more than 80% full, reduce the event send rate */
    if (avail > ring_size * 80 / 100)
        return 0;  /* skip this event */
    
    /* Send normally... */
    return 0;
}
```

---

<!-- chunk: 5. Perf Event Array -->## 5. Perf Event Array

## 5.1 Using the Perf Event Array

```c
/* BPF_MAP_TYPE_PERF_EVENT_ARRAY usage example */
/* Note: 5.8+ recommends using Ring Buffer instead, but this is still common in older code */

#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_tracing.h>

/* DNS query event */
struct dns_event {
    __u64 timestamp;
    __u32 pid;
    __u32 uid;
    char  comm[16];
    __u8  query[128];
    __u16 query_type;
    __u32 src_ip;
};

/* Perf Event Array */
struct {
    __uint(type, BPF_MAP_TYPE_PERF_EVENT_ARRAY);
    __uint(key_size, sizeof(__u32));
    __uint(value_size, sizeof(__u32));
} dns_events SEC(".maps");

SEC("tracepoint/net/net_dev_xmit")
int trace_dns_query(struct trace_event_raw_net_dev_xmit *ctx) {
    struct dns_event event = {};
    
    event.timestamp = bpf_ktime_get_ns();
    event.pid = bpf_get_current_pid_tgid() >> 32;
    event.uid = bpf_get_current_uid_gid() & 0xFFFFFFFF;
    bpf_get_current_comm(event.comm, sizeof(event.comm));
    
    /* Send to the current CPU's perf buffer */
    bpf_perf_event_output(ctx, &dns_events, 
                           BPF_F_CURRENT_CPU,  /* write to the current CPU's buffer */
                           &event, sizeof(event));
    return 0;
}

/* Sending variable-size data */
SEC("kprobe/sys_read")  
int trace_read(struct pt_regs *ctx) {
    /* Use BPF_F_CTXLEN_MASK to also send raw context data */
    struct {
        __u64 pid;
        char data[64];
    } sample = {};
    
    sample.pid = bpf_get_current_pid_tgid() >> 32;
    
    bpf_perf_event_output(ctx, &dns_events,
                           BPF_F_CURRENT_CPU,
                           &sample, sizeof(sample));
    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

```c
/* User-space side - reading the Perf Event Array */
#include <bpf/libbpf.h>
#include <sys/epoll.h>

struct perf_buffer *pb;

static void handle_dns_event(void *ctx, int cpu, void *data, __u32 size) {
    struct dns_event *event = data;
    printf("DNS query from PID %d: %s\n", event->pid, event->query);
}

static void handle_lost_events(void *ctx, int cpu, __u64 lost_cnt) {
    printf("Lost %llu events on CPU %d!\n", lost_cnt, cpu);
}

int main() {
    /* Create the Perf Buffer consumer */
    LIBBPF_OPTS(perf_buffer_opts, pb_opts,
        .sample_cb = handle_dns_event,
        .lost_cb = handle_lost_events,
    );
    
    pb = perf_buffer__new(
        bpf_map__fd(skel->maps.dns_events),
        64,        /* pages per CPU (64 × 4096 = 256 KB per CPU) */
        &pb_opts
    );
    
    /* Event loop */
    while (running) {
        perf_buffer__poll(pb, 100);  /* 100 ms timeout */
    }
    
    perf_buffer__free(pb);
    return 0;
}
```

---

<!-- chunk: 6. Stack and Queue Maps -->## 6. Stack and Queue Maps

## 6.1 BPF_MAP_TYPE_STACK (LIFO)

```c
/* Stack Map - last-in, first-out (LIFO) */
/* Uses: work queues, task stacks, event handling, etc. */

#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

/* An IP address stack - used to track network hops */
struct {
    __uint(type, BPF_MAP_TYPE_STACK);
    __uint(max_entries, 1024);
    __uint(value_size, sizeof(__u32));  /* Stack: no key */
    /* Note: Stack/Queue do not use a key, only a value */
} ip_stack SEC(".maps");

SEC("xdp")
int xdp_track_hops(struct xdp_md *ctx) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;
    
    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        return XDP_PASS;
    
    if (eth->h_proto != bpf_htons(ETH_P_IP))
        return XDP_PASS;
    
    struct iphdr *ip = (void *)(eth + 1);
    if ((void *)(ip + 1) > data_end)
        return XDP_PASS;
    
    __u32 src_ip = ip->saddr;
    
    /* Push the IP address onto the stack */
    bpf_map_push_elem(&ip_stack, &src_ip, BPF_EXIST);
    /* BPF_EXIST: if the stack is full, overwrite the oldest element */
    /* BPF_NOEXIST: if the stack is full, fail and return an error */
    
    return XDP_PASS;
}

/* Read from the stack (in a different program) */
SEC("kprobe/process_packets")
int process_ips(struct pt_regs *ctx) {
    __u32 ip;
    
    /* Pop: last-in, first-out */
    int ret = bpf_map_pop_elem(&ip_stack, &ip);
    if (ret == 0) {
        bpf_printk("Processing IP: %x\n", bpf_ntohl(ip));
    }
    
    /* Peek: look at the top without removing it */
    ret = bpf_map_peek_elem(&ip_stack, &ip);
    if (ret == 0) {
        bpf_printk("Top of stack IP: %x\n", bpf_ntohl(ip));
    }
    
    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

## 6.2 BPF_MAP_TYPE_QUEUE (FIFO)

```c
/* Queue Map - first-in, first-out (FIFO) */
/* Uses: task queues, message passing, traffic shaping, etc. */

#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

/* A queue of pending packet information */
struct pkt_info {
    __u32 src_ip;
    __u32 dst_ip;
    __u16 src_port;
    __u16 dst_port;
    __u32 pkt_len;
    __u64 timestamp;
};

struct {
    __uint(type, BPF_MAP_TYPE_QUEUE);
    __uint(max_entries, 4096);
    __uint(value_size, sizeof(struct pkt_info));
} pkt_queue SEC(".maps");

/* Producer: enqueue packet information */
SEC("xdp")
int xdp_enqueue(struct xdp_md *ctx) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;
    
    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        return XDP_PASS;
    
    if (eth->h_proto != bpf_htons(ETH_P_IP))
        return XDP_PASS;
    
    struct iphdr *ip = (void *)(eth + 1);
    if ((void *)(ip + 1) > data_end)
        return XDP_PASS;
    
    struct pkt_info info = {
        .src_ip = ip->saddr,
        .dst_ip = ip->daddr,
        .pkt_len = ctx->data_end - ctx->data,
        .timestamp = bpf_ktime_get_ns(),
    };
    
    /* Enqueue (fails if full) */
    bpf_map_push_elem(&pkt_queue, &info, 0);
    
    return XDP_PASS;
}

/* Consumer: dequeue packet information for processing */
SEC("kprobe/process_pkt_queue")
int process_queue(struct pt_regs *ctx) {
    struct pkt_info info;
    
    /* Dequeue: first-in, first-out */
    while (bpf_map_pop_elem(&pkt_queue, &info) == 0) {
        bpf_printk("Processing pkt: %x -> %x (%u bytes)\n",
                   bpf_ntohl(info.src_ip),
                   bpf_ntohl(info.dst_ip),
                   info.pkt_len);
        /* Process at most 10 items to avoid loop-detection issues */
        /* A real implementation should use bpf_loop() */
    }
    
    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

## 6.3 BPF_MAP_TYPE_STACK_TRACE: Call-Stack Tracing

```c
/* Stack Trace Map - stores kernel/user-space call stacks */

#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

#define MAX_STACK_DEPTH 20

/* Call-stack storage Map */
struct {
    __uint(type, BPF_MAP_TYPE_STACK_TRACE);
    __uint(max_entries, 10000);
    __uint(key_size, sizeof(__u32));        /* stack_id */
    __uint(value_size, MAX_STACK_DEPTH * sizeof(__u64));  /* array of stack-frame addresses */
} stack_traces SEC(".maps");

/* CPU profiling */
struct profile_key {
    __u32 pid;
    __s32 kernel_stack_id;  /* kernel stack ID */
    __s32 user_stack_id;    /* user stack ID */
};

struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __uint(max_entries, 100000);
    __type(key, struct profile_key);
    __type(value, __u64);  /* sample count */
} profile_counts SEC(".maps");

/* perf_event program - CPU sampling profiler */
SEC("perf_event")
int profile_cpu(struct bpf_perf_event_data *ctx) {
    __u64 pid_tgid = bpf_get_current_pid_tgid();
    __u32 pid = pid_tgid >> 32;
    
    /* Get the kernel-space call stack */
    __s32 kernel_stack_id = bpf_get_stackid(ctx, &stack_traces, 
                                              0 /* flags */);
    
    /* Get the user-space call stack */
    __s32 user_stack_id = bpf_get_stackid(ctx, &stack_traces,
                                           BPF_F_USER_STACK);
    
    struct profile_key key = {
        .pid = pid,
        .kernel_stack_id = kernel_stack_id,
        .user_stack_id = user_stack_id,
    };
    
    /* Increment the sample count */
    __u64 *count = bpf_map_lookup_elem(&profile_counts, &key);
    if (count) {
        (*count)++;
    } else {
        __u64 init = 1;
        bpf_map_update_elem(&profile_counts, &key, &init, BPF_NOEXIST);
    }
    
    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

```bash
# Resolving call stacks from user space (using bpftrace)
bpftrace -e '
profile:hz:99 {
    @[kstack, ustack, comm] = count();
}
interval:s:10 {
    print(@);
    clear(@);
}'

# Or use the bcc profile tool
/usr/share/bcc/tools/profile -F 99 30
```

---

<!-- chunk: 7. LPM Trie Map -->## 7. LPM Trie Map

## 7.1 LPM Trie Principles

```
LPM Trie (Longest Prefix Match Trie) Structure
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Uses: IP route lookup, ACL policy matching

Example IP prefix table:
  10.0.0.0/8     → "Internal Network"
  10.1.0.0/16    → "Dev VLAN"  
  10.1.1.0/24    → "Dev Team A"
  10.1.1.1/32    → "Dev Server 1"
  192.168.0.0/16 → "Lab Network"

Looking up 10.1.1.1:
  Matches 10.0.0.0/8     (8-bit match)
  Matches 10.1.0.0/16    (16-bit match)
  Matches 10.1.1.0/24    (24-bit match)  
  Matches 10.1.1.1/32    (32-bit match) ← the longest prefix, this rule wins

Trie tree structure:
              root
              /  \
           10.* 192.*
            |      \
         10.1.*   192.168.*
            |
         10.1.1.*
            |
         10.1.1.1

Characteristics:
• Time complexity: O(prefix_length) for lookups
• Supports IPv4 (32-bit) and IPv6 (128-bit)
• Maximum prefix depth = key_size * 8 bits
• Only supports BPF_F_NO_PREALLOC (allocated on demand)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

```c
/* A complete LPM Trie Map usage example - IP access control */
#include <linux/bpf.h>
#include <linux/if_ether.h>
#include <linux/ip.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_endian.h>

/* LPM Trie key structure: prefixlen + data */
struct ipv4_lpm_key {
    __u32 prefixlen;  /* prefix length (1-32) */
    __u32 ip;         /* IP address (network byte order) */
};

struct ipv6_lpm_key {
    __u32 prefixlen;   /* prefix length (1-128) */
    __u8  ip[16];      /* IPv6 address */
};

/* ACL rule */
struct acl_rule {
    __u32 action;       /* 0=DENY, 1=ALLOW */
    __u32 priority;     /* rule priority */
    char  comment[64];  /* rule description */
};

/* IPv4 LPM Trie */
struct {
    __uint(type, BPF_MAP_TYPE_LPM_TRIE);
    __uint(max_entries, 65536);
    __type(key, struct ipv4_lpm_key);    /* key_size = 8 bytes */
    __type(value, struct acl_rule);
    __uint(map_flags, BPF_F_NO_PREALLOC);  /* required for LPM Trie */
} acl_v4 SEC(".maps");

/* IPv6 LPM Trie */
struct {
    __uint(type, BPF_MAP_TYPE_LPM_TRIE);
    __uint(max_entries, 65536);
    __type(key, struct ipv6_lpm_key);    /* key_size = 20 bytes */
    __type(value, struct acl_rule);
    __uint(map_flags, BPF_F_NO_PREALLOC);
} acl_v6 SEC(".maps");

/* Count denied packets */
struct {
    __uint(type, BPF_MAP_TYPE_PERCPU_ARRAY);
    __uint(max_entries, 1);
    __type(key, __u32);
    __type(value, __u64);
} denied_count SEC(".maps");

SEC("xdp")
int xdp_acl(struct xdp_md *ctx) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;
    
    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        return XDP_PASS;
    
    __u16 proto = bpf_ntohs(eth->h_proto);
    
    if (proto == ETH_P_IP) {
        struct iphdr *ip = (void *)(eth + 1);
        if ((void *)(ip + 1) > data_end)
            return XDP_PASS;
        
        /* LPM lookup - automatically matches the longest prefix */
        struct ipv4_lpm_key key = {
            .prefixlen = 32,     /* an exact-match key; the Trie automatically finds the longest match */
            .ip = ip->saddr,
        };
        
        struct acl_rule *rule = bpf_map_lookup_elem(&acl_v4, &key);
        if (rule && rule->action == 0) {
            /* A rule matched and its action is DENY */
            __u32 cnt_key = 0;
            __u64 *count = bpf_map_lookup_elem(&denied_count, &cnt_key);
            if (count)
                (*count)++;
            return XDP_DROP;
        }
    }
    
    return XDP_PASS;
}

char LICENSE[] SEC("license") = "GPL";
```

```c
/* Managing the LPM Trie from user space */
#include <bpf/libbpf.h>
#include <bpf/bpf.h>
#include <arpa/inet.h>

struct ipv4_lpm_key {
    uint32_t prefixlen;
    uint32_t ip;
};

struct acl_rule {
    uint32_t action;
    uint32_t priority;
    char     comment[64];
};

/* Add a CIDR rule */
int add_acl_rule(int map_fd, const char *cidr, int action, const char *comment) {
    char ip_str[64];
    int prefix_len;
    
    /* Parse the CIDR (e.g. "10.0.0.0/8") */
    sscanf(cidr, "%[^/]/%d", ip_str, &prefix_len);
    
    struct ipv4_lpm_key key = {
        .prefixlen = prefix_len,
    };
    inet_pton(AF_INET, ip_str, &key.ip);
    
    struct acl_rule rule = {
        .action = action,
        .priority = 100,
    };
    strncpy(rule.comment, comment, sizeof(rule.comment) - 1);
    
    return bpf_map_update_elem(map_fd, &key, &rule, BPF_ANY);
}

/* Delete a rule */
int del_acl_rule(int map_fd, const char *cidr) {
    char ip_str[64];
    int prefix_len;
    sscanf(cidr, "%[^/]/%d", ip_str, &prefix_len);
    
    struct ipv4_lpm_key key = {.prefixlen = prefix_len};
    inet_pton(AF_INET, ip_str, &key.ip);
    
    return bpf_map_delete_elem(map_fd, &key);
}

int main() {
    /* Assume the program has already been loaded and map_fd obtained */
    int map_fd = /* ... */;
    
    /* Add rules */
    add_acl_rule(map_fd, "10.0.0.0/8", 1, "Allow internal");
    add_acl_rule(map_fd, "192.168.100.0/24", 0, "Block specific subnet");
    add_acl_rule(map_fd, "10.1.1.1/32", 0, "Block specific host");
    
    /* Query a rule */
    struct ipv4_lpm_key query = {
        .prefixlen = 32,
        .ip = inet_addr("10.1.1.1"),
    };
    struct acl_rule result;
    if (bpf_map_lookup_elem(map_fd, &query, &result) == 0) {
        printf("Rule for 10.1.1.1: action=%d, comment=%s\n",
               result.action, result.comment);
    }
    
    return 0;
}
```

---

<!-- chunk: 8. Map-in-Map Nested Structures -->## 8. Map-in-Map Nested Structures

## 8.1 Map-in-Map Principles and Types

```
Map-in-Map Nested Structure
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Types:
  BPF_MAP_TYPE_ARRAY_OF_MAPS  - the outer layer is an array, the inner layer any Map type
  BPF_MAP_TYPE_HASH_OF_MAPS   - the outer layer is a hash, the inner layer any Map type

Use cases:
┌─────────────────────────────────────────────────────────────────┐
│ Scenario 1: isolating data by namespace/tenant                  │
│                                                                 │
│  Outer Map (Hash):        Inner Map (Hash):                    │
│  namespace_id → map_fd    conn_tuple → stats                   │
│                                                                 │
│  namespace_1 → [map_fd1] → {conn1: stats1, conn2: stats2}     │
│  namespace_2 → [map_fd2] → {conn1: stats3, conn3: stats4}     │
│                                                                 │
│  Advantage: each namespace has its own independent Map,        │
│  operations are isolated, updating one does not affect others  │
│                                                                 │
│ Scenario 2: atomically swapping a policy table                 │
│                                                                 │
│  Outer Array (index 0):   Inner Map (the current policy):      │
│  [0] → policy_map_fd    rule1 → action, rule2 → action         │
│                                                                 │
│  Update flow:                                                    │
│  1. Create a new inner Map (new_policy_map)                    │
│  2. User space loads the new rules into new_policy_map         │
│  3. Atomically update the outer Array: array[0] = new_policy_map_fd │
│  4. The eBPF program automatically uses the new policy on its  │
│     next access                                                 │
│  → Achieves zero-downtime policy hot-reloading!                │
└─────────────────────────────────────────────────────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

```c
/* Map-in-Map example - multi-tenant connection tracking */
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

/* Inner Map prototype (defines the structural template) */
struct inner_map_type {
    __uint(type, BPF_MAP_TYPE_HASH);
    __uint(max_entries, 1024);
    __type(key, __u64);   /* connection hash */
    __type(value, __u64); /* byte count */
} inner_map_proto SEC(".maps");

/* Outer Map - indexed by tenant ID, value is the fd of the inner Map */
struct {
    __uint(type, BPF_MAP_TYPE_ARRAY_OF_MAPS);
    __uint(max_entries, 256);          /* up to 256 tenants */
    __type(key, __u32);               /* tenant ID */
    __type(value, __u32);             /* inner Map fd (managed by the kernel) */
    /* references the inner Map type */
    __array(values, struct inner_map_type);  /* BTF style */
} tenant_maps SEC(".maps");

SEC("xdp")
int multi_tenant_tracking(struct xdp_md *ctx) {
    __u32 tenant_id = 0;  /* a real implementation would extract this from the packet header (e.g. VXLAN VNI) */
    __u64 conn_hash = 0;  /* a real implementation should hash the 5-tuple */
    __u32 pkt_len = ctx->data_end - ctx->data;
    
    /* Look up the tenant's inner Map */
    void *inner_map = bpf_map_lookup_elem(&tenant_maps, &tenant_id);
    if (!inner_map)
        return XDP_PASS;  /* unknown tenant */
    
    /* Update connection statistics in the inner Map */
    __u64 *bytes = bpf_map_lookup_elem(inner_map, &conn_hash);
    if (bytes) {
        __sync_fetch_and_add(bytes, pkt_len);
    } else {
        __u64 init = pkt_len;
        bpf_map_update_elem(inner_map, &conn_hash, &init, BPF_NOEXIST);
    }
    
    return XDP_PASS;
}

char LICENSE[] SEC("license") = "GPL";
```

```c
/* Policy hot-reloading - achieving zero-downtime updates using Map-in-Map */
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>

/* Inner Map: the policy rule table */
struct policy_rule {
    __u32 action;        /* 0=deny, 1=allow */
    __u32 rate_limit;    /* packets allowed per second */
    __u64 hit_count;     /* number of hits */
};

struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __uint(max_entries, 10000);
    __type(key, __u32);                 /* source IP */
    __type(value, struct policy_rule);
} policy_inner_proto SEC(".maps");

/* Outer Map: the currently active policy table (a single-element array) */
struct {
    __uint(type, BPF_MAP_TYPE_ARRAY_OF_MAPS);
    __uint(max_entries, 1);
    __type(key, __u32);
    __uint(value_size, sizeof(__u32));
    __array(values, struct {
        __uint(type, BPF_MAP_TYPE_HASH);
        __uint(max_entries, 10000);
        __type(key, __u32);
        __type(value, struct policy_rule);
    });
} active_policy SEC(".maps");

SEC("xdp")
int policy_enforcer(struct xdp_md *ctx) {
    void *data = (void *)(long)ctx->data;
    void *data_end = (void *)(long)ctx->data_end;
    
    /* Get the currently active policy Map (an atomic read) */
    __u32 idx = 0;
    void *policy_map = bpf_map_lookup_elem(&active_policy, &idx);
    if (!policy_map)
        return XDP_PASS;  /* no policy, allow everything */
    
    /* Extract the source IP */
    if ((void *)(data + sizeof(struct ethhdr) + sizeof(struct iphdr)) > data_end)
        return XDP_PASS;
    
    struct iphdr *ip = data + sizeof(struct ethhdr);
    __u32 src_ip = ip->saddr;
    
    /* Look up the policy */
    struct policy_rule *rule = bpf_map_lookup_elem(policy_map, &src_ip);
    if (rule) {
        __sync_fetch_and_add(&rule->hit_count, 1);
        if (rule->action == 0)
            return XDP_DROP;
    }
    
    return XDP_PASS;
}

char LICENSE[] SEC("license") = "GPL";
```

```c
/* User-space hot-reload flow */
#include <bpf/libbpf.h>
#include <bpf/bpf.h>

int hot_update_policy(int outer_map_fd, struct policy_entry *new_rules, int count) {
    /* 1. Create a new inner Map */
    LIBBPF_OPTS(bpf_map_create_opts, opts);
    int new_inner_fd = bpf_map_create(
        BPF_MAP_TYPE_HASH,
        "policy_new",
        sizeof(__u32),                /* key_size */
        sizeof(struct policy_rule),   /* value_size */
        10000,                        /* max_entries */
        &opts
    );
    
    if (new_inner_fd < 0) {
        perror("bpf_map_create");
        return -1;
    }
    
    /* 2. Load the new rules into the new Map */
    for (int i = 0; i < count; i++) {
        struct policy_rule rule = {
            .action = new_rules[i].action,
            .rate_limit = new_rules[i].rate_limit,
        };
        bpf_map_update_elem(new_inner_fd, &new_rules[i].src_ip, &rule, BPF_ANY);
    }
    
    /* 3. Atomically update the outer Map - the eBPF program automatically uses the new Map on its next execution */
    __u32 idx = 0;
    int ret = bpf_map_update_elem(outer_map_fd, &idx, &new_inner_fd, BPF_ANY);
    
    if (ret < 0) {
        perror("bpf_map_update_elem (outer)");
        close(new_inner_fd);
        return -1;
    }
    
    printf("Policy updated atomically with %d rules\n", count);
    
    /* 4. Close the new Map's fd (the kernel still holds a reference) */
    close(new_inner_fd);
    
    return 0;
}
```

---

<!-- chunk: 9. User-Space and Kernel-Space Communication Patterns -->## 9. User-Space and Kernel-Space Communication Patterns

## 9.1 Overview of Communication Patterns

```
eBPF Kernel ↔ User-Space Communication Patterns
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Pattern                Data Direction  Characteristics          Suitable Scenario
────────────────────  ───────────── ──────────────────────  ─────────────────────
Array/Hash Map         bidirectional  poll-based reads, good for aggregated data  statistics, config push
Ring Buffer            kernel→user    zero-copy, ordered, efficient  real-time event streams
Perf Event Array       kernel→user    per-CPU, high-frequency events  high-frequency sampling (older approach)
Socket Map             redirection    transparent proxying, no copies  service mesh, proxies
BPF Task/Sk Storage    bidirectional  bound to kernel objects  per-socket state
BPF Iterator           kernel→user    iterates kernel objects  bulk data export

                       ┌─────────────────────────────────────┐
                       │           Selection Guide            │
                       │                                     │
                       │  High-frequency real-time events    │
                       │  (>100K/s)?                         │
                       │  ┌─ Yes ─▶ Ring Buffer (5.8+)       │
                       │  └─ No                              │
                       │      │                              │
                       │      ▼                              │
                       │  Need aggregated statistics?         │
                       │  ┌─ Yes ─▶ Per-CPU Array/Hash       │
                       │  └─ No                              │
                       │      │                              │
                       │      ▼                              │
                       │  Need to push configuration?         │
                       │  ┌─ Yes ─▶ Hash/Array Map           │
                       │  └─ No ─▶ Ring Buffer (general)     │
                       └─────────────────────────────────────┘
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 9.2 BPF Iterator - Efficient Bulk Data Export

```c
/* BPF Iterator - iterate over kernel objects and export data (5.8+) */
#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_tracing.h>

/* Export all Map data via the seq_file interface */
/* Once pinned to /sys/fs/bpf/, the data can be read with the cat command */

struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __uint(max_entries, 10240);
    __type(key, __u32);
    __type(value, __u64);
} my_data SEC(".maps");

/* BPF Iterator program - iterate over Map entries */
SEC("iter/bpf_map_elem")
int dump_map_elem(struct bpf_iter__bpf_map_elem *ctx) {
    struct seq_file *seq = ctx->meta->seq;
    __u32 *key = ctx->key;
    __u64 *value = ctx->value;
    
    if (!key || !value)
        return 0;
    
    /* Formatted output to the seq_file */
    BPF_SEQ_PRINTF(seq, "key=%-10u value=%-20llu\n", *key, *value);
    
    return 0;
}

/* Iterate over all sockets */
SEC("iter/tcp4")
int dump_tcp_sockets(struct bpf_iter__tcp *ctx) {
    struct seq_file *seq = ctx->meta->seq;
    struct sock_common *sk_common = ctx->sk_common;
    
    if (!sk_common)
        return 0;
    
    __u32 src_ip = BPF_CORE_READ(sk_common, skc_rcv_saddr);
    __u32 dst_ip = BPF_CORE_READ(sk_common, skc_daddr);
    __u16 src_port = BPF_CORE_READ(sk_common, skc_num);
    __u16 dst_port = BPF_CORE_READ(sk_common, skc_dport);
    
    BPF_SEQ_PRINTF(seq, "%x:%u -> %x:%u\n",
                   src_ip, src_port, dst_ip, bpf_ntohs(dst_port));
    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

## 9.3 BPF Local Storage - Storage Bound to an Object

```c
/* BPF Local Storage - object-bound storage requiring no hash lookup */
/* Binds data directly to a kernel object (socket/inode/task) */

#include <linux/bpf.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_tracing.h>
#include "vmlinux.h"

/* Per-socket local storage */
struct socket_stats {
    __u64 bytes_sent;
    __u64 bytes_recv;
    __u64 conn_start_ns;
    __u32 pid;
    char  comm[16];
};

/* SK Storage Map definition (note: max_entries is not needed) */
struct {
    __uint(type, BPF_MAP_TYPE_SK_STORAGE);
    __uint(map_flags, BPF_F_NO_PREALLOC);
    __type(key, int);                      /* sock fd (placeholder) */
    __type(value, struct socket_stats);
} sk_stats_map SEC(".maps");

/* Per-task local storage */
struct task_ctx {
    __u64 syscall_count;
    __u64 last_syscall_ns;
    __u32 suspicious_count;
};

struct {
    __uint(type, BPF_MAP_TYPE_TASK_STORAGE);
    __uint(map_flags, BPF_F_NO_PREALLOC);
    __type(key, int);
    __type(value, struct task_ctx);
} task_ctx_map SEC(".maps");

/* Initialize socket storage when a TCP connection is established */
SEC("fentry/tcp_v4_connect")
int BPF_PROG(track_new_conn, struct sock *sk) {
    struct socket_stats *stats;
    
    /* bpf_sk_storage_get: get or create the storage bound to a socket */
    stats = bpf_sk_storage_get(&sk_stats_map, sk, NULL, BPF_LOCAL_STORAGE_GET_F_CREATE);
    if (!stats)
        return 0;
    
    stats->conn_start_ns = bpf_ktime_get_ns();
    stats->pid = bpf_get_current_pid_tgid() >> 32;
    bpf_get_current_comm(stats->comm, sizeof(stats->comm));
    
    return 0;
}

/* Track data being sent */
SEC("fentry/tcp_sendmsg")
int BPF_PROG(track_sendmsg, struct sock *sk, struct msghdr *msg, size_t size) {
    /* Look up statistics for this socket */
    struct socket_stats *stats = bpf_sk_storage_get(&sk_stats_map, sk, NULL, 0);
    if (!stats)
        return 0;
    
    __sync_fetch_and_add(&stats->bytes_sent, size);
    return 0;
}

/* Clean up when the socket is closed (happens automatically, but can also be manual) */
SEC("fentry/inet_sock_destruct")
int BPF_PROG(cleanup_sk_storage, struct sock *sk) {
    /* Read the final statistics */
    struct socket_stats *stats = bpf_sk_storage_get(&sk_stats_map, sk, NULL, 0);
    if (stats) {
        bpf_printk("Connection closed: pid=%d sent=%llu recv=%llu\n",
                   stats->pid, stats->bytes_sent, stats->bytes_recv);
    }
    /* The storage is freed automatically along with the socket */
    return 0;
}

/* Task Storage - tracking suspicious process behavior */
SEC("tracepoint/raw_syscalls/sys_enter")
int track_syscalls(struct trace_event_raw_sys_enter *ctx) {
    struct task_struct *task = (void *)bpf_get_current_task();
    
    /* Get or create the context bound to this task */
    struct task_ctx *tctx = bpf_task_storage_get(&task_ctx_map, task, NULL,
                                                   BPF_LOCAL_STORAGE_GET_F_CREATE);
    if (!tctx)
        return 0;
    
    tctx->syscall_count++;
    tctx->last_syscall_ns = bpf_ktime_get_ns();
    
    /* Detect a high frequency of syscalls (a possible exploit signature) */
    if (tctx->syscall_count % 10000 == 0) {
        bpf_printk("High syscall frequency: pid=%d count=%llu\n",
                   bpf_get_current_pid_tgid() >> 32,
                   tctx->syscall_count);
    }
    
    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

---

<!-- chunk: 10. Map Performance Optimization and Tuning -->## 10. Map Performance Optimization and Tuning

## 10.1 Map Selection Decision Tree

```
Map Type Selection Decision Tree
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

What kind of data needs to be stored?
│
├─▶ Events/messages (kernel → user space)
│   ├─ High frequency (>50K events/sec), kernel 5.8+ → BPF_MAP_TYPE_RINGBUF
│   └─ Compatibility needs or an older kernel       → BPF_MAP_TYPE_PERF_EVENT_ARRAY
│
├─▶ Statistics counters (high-concurrency writes)
│   ├─ Integer counting, lock-free is optimal   → BPF_MAP_TYPE_PERCPU_ARRAY (fastest)
│   ├─ Dynamic keys (e.g. PID), lock-free       → BPF_MAP_TYPE_PERCPU_HASH
│   └─ Some contention is acceptable            → BPF_MAP_TYPE_ARRAY + __sync_fetch_and_add
│
├─▶ Key-value configuration (pushed from user space)
│   ├─ Fixed count, contiguous keys             → BPF_MAP_TYPE_ARRAY (fastest)
│   └─ Dynamic keys, arbitrary types             → BPF_MAP_TYPE_HASH
│
├─▶ Bounded cache (automatic eviction)
│   ├─ High concurrency, evenly distributed     → BPF_MAP_TYPE_LRU_PERCPU_HASH
│   └─ General-purpose scenario                  → BPF_MAP_TYPE_LRU_HASH
│
├─▶ IP routing/prefix matching                   → BPF_MAP_TYPE_LPM_TRIE
│
├─▶ Program chains/dynamic dispatch              → BPF_MAP_TYPE_PROG_ARRAY
│
├─▶ Socket redirection                           → BPF_MAP_TYPE_SOCKMAP / SOCKHASH
│
├─▶ Multi-tenancy/hot-reloading                  → BPF_MAP_TYPE_ARRAY_OF_MAPS
│                                                  BPF_MAP_TYPE_HASH_OF_MAPS
│
├─▶ Task queue (FIFO)                            → BPF_MAP_TYPE_QUEUE
├─▶ Work stack (LIFO)                            → BPF_MAP_TYPE_STACK
└─▶ Call-stack tracing                           → BPF_MAP_TYPE_STACK_TRACE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 10.2 Map Performance Benchmarks

```
Map Operation Performance Benchmarks (Intel Xeon, Linux 5.15, eBPF JIT)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Test scenario: single core, 32-byte key+value, 1M entries

Map type                  Lookup (ns) Update (ns) Notes
─────────────────────── ──────────  ──────────  ─────────────────────────
PERCPU_ARRAY (read)       ~10         ~8        fastest, lock-free, contiguous memory
ARRAY (read, no contention) ~12        ~10       atomic op but no hashing
PERCPU_HASH (lock-free)    ~25         ~30       lock-free hash, handles collisions
HASH (light load)          ~35         ~40       bucket lock, low contention
LRU_HASH                    ~45         ~50       extra LRU list maintenance
LPM_TRIE                    ~80        ~100       tree traversal, depends on prefix count
LRU_PERCPU_HASH             ~30         ~35       Per-CPU LRU, low contention

Note: actual performance is significantly affected by load, memory pressure, and CPU cache

High-concurrency scenario (32 cores, heavy contention):
  HASH (contended writes)  ~200-500 ns  (bucket-lock contention)
  PERCPU_HASH (lock-free)   ~25-40  ns  (no contention)
  → PERCPU_HASH is 5-20x faster under concurrent-write scenarios
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## 10.3 Memory Optimization Strategies

```c
/* Memory optimization tips */

/* Tip 1: set max_entries sensibly */
/* Do not over-reserve, but leave some headroom */
struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    /* Set based on the actual expected number of connections; don't blindly set it to 1M */
    __uint(max_entries, 65536);  /* 64K is usually plenty */
    __type(key, struct conn_key);
    __type(value, struct conn_val);
    __uint(map_flags, BPF_F_NO_PREALLOC);  /* allocate on demand */
} conn_map SEC(".maps");

/* Tip 2: trim the value struct to reduce padding waste */
/* Not recommended: a lot of padding bytes */
struct bad_stats {
    __u64 packets;    /* 8 bytes */
    __u8  proto;      /* 1 byte */
    /* 7 bytes of wasted padding! */
    __u64 bytes;      /* 8 bytes */
    /* total: 24 bytes (useful: 17 bytes) */
};

/* Recommended: order fields from largest to smallest */
struct good_stats {
    __u64 packets;    /* 8 bytes */
    __u64 bytes;      /* 8 bytes */
    __u8  proto;      /* 1 byte */
    __u8  _pad[7];    /* explicit padding (clearer intent) */
    /* total: 24 bytes (same, but the intent is clear) */
};

/* Even better: drop unnecessary padding entirely */
struct best_stats {
    __u64 packets;    /* 8 bytes */
    __u64 bytes;      /* 8 bytes */
    /* drop proto entirely if it isn't needed */
    /* total: 16 bytes */
} __attribute__((packed));  /* note: packed can hurt performance */

/* Tip 3: use BPF_F_NO_PREALLOC to save memory */
/* Preallocated vs on-demand allocation:
   Preallocated:  all memory is allocated at startup, but there's less fragmentation and access is faster
   On-demand:     memory usage is lower, but allocation may occasionally fail */

/* For sparse Maps (large max_entries but few actual entries), use NO_PREALLOC */
struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __uint(max_entries, 1000000);    /* an upper bound of 1 million entries */
    __uint(map_flags, BPF_F_NO_PREALLOC);  /* only allocate memory that is actually used */
    __type(key, __u64);
    __type(value, __u64);
} sparse_map SEC(".maps");

/* Tip 4: use a PERCPU Map to avoid false sharing */
/* When multiple CPU cores frequently read/write adjacent memory, cache-line contention is severe */
/* A Per-CPU Map gives each core its own independent cache line, avoiding contention */
```

## 10.4 Map Monitoring and Tuning

```bash
# Map monitoring tools

# 1. List all Maps and their memory usage
bpftool map list
# Output:
# 42: hash  name conn_track  flags 0x1
#         key 16B  value 32B  max_entries 65536  memlock 4194304B
#         btf_id 156

# 2. View detailed Map information (JSON)
bpftool map show id 42 -p

# 3. Monitor Map memory usage
watch -n 1 'bpftool map list | grep memlock'

# 4. View Map contents (with BTF-based formatting)
bpftool map dump id 42

# 5. Count the number of Map entries
bpftool map dump id 42 | grep "key" | wc -l

# 6. View kernel BPF memory statistics
cat /proc/net/xdp_diag 2>/dev/null || true
cat /proc/sys/kernel/bpf_stats_enabled

# 7. Use bpftrace to monitor the frequency of Map operations
bpftrace -e '
kprobe:htab_map_update_elem {
    @updates[comm] = count();
}
interval:s:5 {
    print(@updates);
    clear(@updates);
}'

# 8. Check the Map memory ceiling
cat /proc/sys/kernel/bpf_stats_enabled

# 9. Adjust the process's memlock limit (Maps need locked memory)
ulimit -l unlimited  # or set this in /etc/security/limits.conf
# or in a systemd service:
# LimitMEMLOCK=infinity

# Setting memlock in Kubernetes
# In a DaemonSet's securityContext:
# resources:
#   limits:
#     memory: 2Gi
```

---

<!-- chunk: 11. Practical bpftool Map Operations -->## 11. Practical bpftool Map Operations

## 11.1 Basic bpftool Operations

```bash
# ========================================================
# Complete guide to bpftool Map operations
# ========================================================

# 1. List all Maps
bpftool map list
bpftool map list --json | jq '.'  # JSON format

# Example output:
# 5: percpu_array  name xdp_stats  flags 0x0
#     key 4B  value 48B  max_entries 1  memlock 364544B
# 6: hash  name conn_track  flags 0x1
#     key 16B  value 40B  max_entries 65536  memlock 6291456B
#     btf_id 89

# 2. Show Map details
bpftool map show id 6
bpftool map show name conn_track  # look up by name

# 3. Dump the entire contents of a Map
bpftool map dump id 6
# Formatted output with BTF type information (requires the program to use BTF)

# 4. Query a specific key
# a 16-byte key (an IPv4 5-tuple), in hex format
bpftool map lookup id 6 key hex 0a 00 00 01 0a 00 00 02 1f 90 00 50 06 00 00 00

# 5. Update/add an entry
bpftool map update id 6 \
    key hex 0a 00 00 01 0a 00 00 02 1f 90 00 50 06 00 00 00 \
    value hex 00 00 00 00 00 00 00 64 00 00 00 00 00 00 00 01 ...

# 6. Delete an entry
bpftool map delete id 6 key hex 0a 00 00 01 ...

# 7. Pin a Map to the BPF filesystem
bpftool map pin id 6 /sys/fs/bpf/conn_track_map

# 8. Load a Map from its pin
bpftool map show pinned /sys/fs/bpf/conn_track_map

# 9. Batch operations (more efficient for iterating over large Maps)
bpftool map dump id 6 | head -100  # the first 100 entries

# 10. View a Map's BTF type information
bpftool btf show id <btf_id>
bpftool btf dump id <btf_id>
```

## 11.2 Practical Script Examples

```bash
#!/bin/bash
# ebpf-map-monitor.sh - eBPF Map monitoring script

set -euo pipefail

PROG_NAME=${1:-""}

echo "=== eBPF Map Monitoring Report ==="
echo "Time: $(date)"
echo ""

# Get all Maps
MAPS=$(bpftool map list --json 2>/dev/null || echo "[]")

if [ "$MAPS" = "[]" ]; then
    echo "No eBPF Maps found"
    exit 0
fi

echo "=== Map List ==="
bpftool map list

echo ""
echo "=== Memory Usage Statistics ==="
total_mem=0
while IFS= read -r line; do
    memlock=$(echo "$line" | grep -oP 'memlock \K\d+' || echo "0")
    total_mem=$((total_mem + memlock))
done < <(bpftool map list)

echo "Total Map memory locked: $((total_mem / 1024 / 1024)) MB"

echo ""
echo "=== XDP Statistics (if present) ==="
XDP_MAP_ID=$(bpftool map list 2>/dev/null | grep "xdp_stats" | awk '{print $1}' | tr -d ':')
if [ -n "$XDP_MAP_ID" ]; then
    echo "XDP Stats Map (ID: $XDP_MAP_ID):"
    bpftool map dump id "$XDP_MAP_ID" 2>/dev/null || echo "Unable to read"
fi

echo ""
echo "=== Connection Tracking Map (if present) ==="
CONN_MAP_ID=$(bpftool map list 2>/dev/null | grep "conn_track" | awk '{print $1}' | tr -d ':')
if [ -n "$CONN_MAP_ID" ]; then
    ENTRY_COUNT=$(bpftool map dump id "$CONN_MAP_ID" 2>/dev/null | grep -c "key" || echo "0")
    echo "Connection tracking entry count: $ENTRY_COUNT"
fi
```

```bash
#!/bin/bash
# lpm-trie-manager.sh - LPM Trie management script

# Add an IP/CIDR to the LPM Trie
add_prefix() {
    local map_id=$1
    local cidr=$2      # format: "10.0.0.0/8"
    local action=$3    # 0=deny, 1=allow

    local ip prefix_len
    IFS='/' read -r ip prefix_len <<< "$cidr"

    # Convert the IP to little-endian hex
    local ip_hex
    ip_hex=$(python3 -c "
import socket, struct
ip = socket.inet_aton('$ip')
print(' '.join(f'{b:02x}' for b in ip))
")

    # prefixlen occupies 4 bytes
    local plen_hex
    plen_hex=$(python3 -c "print(f'{$prefix_len:08x}' | sed 's/../& /g'")

    # key = prefixlen(4B) + ip(4B)
    local key_hex="$(printf '%02x %02x %02x %02x' \
        $(($prefix_len & 0xFF)) 0 0 0) $ip_hex"

    # value = action(4B) + padding
    local val_hex="$(printf '%02x 00 00 00' $action) 00 00 00 00 ..."

    echo "Adding $cidr (action=$action) to map $map_id"
    bpftool map update id "$map_id" key hex $key_hex value hex $val_hex
}

# Usage example
# MAP_ID=$(bpftool map list | grep "acl_v4" | awk '{print $1}' | tr -d ':')
# add_prefix "$MAP_ID" "192.168.100.0/24" 0  # deny this subnet
# add_prefix "$MAP_ID" "10.0.0.0/8" 1        # allow the internal network
```

## 11.3 A Complete Example Using a libbpf Skeleton

```c
/* A complete eBPF program skeleton - demonstrating combined Map usage */

/* ---- kernel/map_demo.bpf.c ---- */
#include <vmlinux.h>
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_tracing.h>
#include <bpf/bpf_core_read.h>

/* Config Map (written by user space, read by kernel space) */
struct config {
    __u32 sampling_rate;     /* sampling rate 1/N */
    __u32 min_latency_us;    /* minimum latency threshold (microseconds) */
    __u8  enabled;           /* on/off switch */
};

struct {
    __uint(type, BPF_MAP_TYPE_ARRAY);
    __uint(max_entries, 1);
    __type(key, __u32);
    __type(value, struct config);
} config_map SEC(".maps");

/* Stats Map (Per-CPU, written frequently by the kernel, read periodically by user space) */
struct stats {
    __u64 total_calls;
    __u64 slow_calls;
    __u64 total_latency_ns;
};

struct {
    __uint(type, BPF_MAP_TYPE_PERCPU_ARRAY);
    __uint(max_entries, 1);
    __type(key, __u32);
    __type(value, struct stats);
} stats_map SEC(".maps");

/* Event Map (written by the kernel, read by user space) */
struct slow_event {
    __u64 timestamp;
    __u64 latency_ns;
    __u32 pid;
    char  comm[16];
    char  func[32];
};

struct {
    __uint(type, BPF_MAP_TYPE_RINGBUF);
    __uint(max_entries, 1 << 23);  /* 8 MB */
} events SEC(".maps");

/* Tracks the start time */
struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __uint(max_entries, 10240);
    __type(key, __u64);   /* tid */
    __type(value, __u64); /* start_ns */
    __uint(map_flags, BPF_F_NO_PREALLOC);
} start_times SEC(".maps");

SEC("fentry/vfs_read")
int BPF_PROG(fentry_vfs_read, struct file *file, char __user *buf,
             size_t count, loff_t *pos) {
    /* Check whether the config is enabled */
    __u32 cfg_key = 0;
    struct config *cfg = bpf_map_lookup_elem(&config_map, &cfg_key);
    if (!cfg || !cfg->enabled)
        return 0;

    /* Sampling: record once every sampling_rate calls */
    __u64 tid = bpf_get_current_pid_tgid();
    if (cfg->sampling_rate > 1) {
        __u32 rand = bpf_get_prandom_u32();
        if (rand % cfg->sampling_rate != 0)
            return 0;
    }

    __u64 start = bpf_ktime_get_ns();
    bpf_map_update_elem(&start_times, &tid, &start, BPF_ANY);
    return 0;
}

SEC("fexit/vfs_read")
int BPF_PROG(fexit_vfs_read, struct file *file, char __user *buf,
             size_t count, loff_t *pos, ssize_t ret) {
    __u64 tid = bpf_get_current_pid_tgid();

    __u64 *start = bpf_map_lookup_elem(&start_times, &tid);
    if (!start)
        return 0;

    __u64 latency = bpf_ktime_get_ns() - *start;
    bpf_map_delete_elem(&start_times, &tid);

    /* Update statistics */
    __u32 stats_key = 0;
    struct stats *s = bpf_map_lookup_elem(&stats_map, &stats_key);
    if (s) {
        s->total_calls++;
        s->total_latency_ns += latency;
    }

    /* Read the configured threshold */
    __u32 cfg_key = 0;
    struct config *cfg = bpf_map_lookup_elem(&config_map, &cfg_key);
    if (!cfg)
        return 0;

    /* Only record slow calls that exceed the threshold */
    if (latency < (__u64)cfg->min_latency_us * 1000)
        return 0;

    if (s)
        s->slow_calls++;

    /* Send a slow-call event */
    struct slow_event *event = bpf_ringbuf_reserve(&events, sizeof(*event), 0);
    if (!event)
        return 0;

    event->timestamp = bpf_ktime_get_boot_ns();
    event->latency_ns = latency;
    event->pid = tid >> 32;
    bpf_get_current_comm(event->comm, sizeof(event->comm));
    __builtin_memcpy(event->func, "vfs_read", 8);

    bpf_ringbuf_submit(event, 0);
    return 0;
}

char LICENSE[] SEC("license") = "GPL";
```

```yaml
# Kubernetes ConfigMap - eBPF monitoring configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: ebpf-monitor-config
  namespace: monitoring
data:
  config.json: |
    {
      "sampling_rate": 10,
      "min_latency_us": 1000,
      "enabled": true,
      "map_sizes": {
        "conn_track": 65536,
        "events_ringbuf_mb": 64,
        "stats_array": 1
      }
    }
  
  # Deployment script
  deploy.sh: |
    #!/bin/bash
    # Load the eBPF program
    ./map_demo &
    
    # Configuration parameters
    MAP_ID=$(bpftool map list | grep "config_map" | awk '{print $1}' | tr -d ':')
    
    # Set the sampling rate to 10 (sample once every 10 calls)
    # key=0, value: sampling_rate=10, min_latency_us=1000, enabled=1
    bpftool map update id $MAP_ID key hex 00 00 00 00 \
        value hex 0a 00 00 00 e8 03 00 00 01 00 00 00
    
    echo "eBPF monitor configured"
```

---

<!-- chunk: 📊 Map Type Quick Reference -->## 📊 Map Type Quick Reference

| Map Type | Introduced | Key Type | Concurrency Safety | Auto-Eviction | Primary Use |
|----------|----------|----------|----------|----------|----------|
| HASH | 3.19 | any | bucket lock | no | general-purpose key-value storage |
| PERCPU_HASH | 4.6 | any | lock-free | no | high-frequency counting |
| LRU_HASH | 4.10 | any | bucket lock | yes | connection-tracking cache |
| LRU_PERCPU_HASH | 4.10 | any | lock-free | yes | high-concurrency cache |
| ARRAY | 3.19 | u32 | atomic | no | configuration, fixed statistics |
| PERCPU_ARRAY | 4.6 | u32 | lock-free | no | highest-performance counting |
| PROG_ARRAY | 4.2 | u32 | - | - | tail-call program chains |
| RINGBUF | 5.8 | - | lock-free | - | high-performance event streams |
| PERF_EVENT_ARRAY | 4.3 | u32(cpu) | per-CPU | - | event output (older approach) |
| STACK_TRACE | 4.6 | u32 | bucket lock | no | call-stack analysis |
| LPM_TRIE | 4.11 | prefix+ip | bucket lock | no | IP prefix matching |
| STACK | 4.20 | none | lock | no | LIFO queue |
| QUEUE | 4.20 | none | lock | no | FIFO queue |
| ARRAY_OF_MAPS | 4.12 | u32 | atomic | - | Map nesting/hot-reload |
| HASH_OF_MAPS | 4.12 | any | bucket lock | - | multi-tenant Maps |
| SK_STORAGE | 5.2 | sock | lock-free | with the sock | per-socket state |
| TASK_STORAGE | 5.11 | task | lock-free | with the task | per-task state |
| INODE_STORAGE | 5.10 | inode | lock-free | with the inode | per-file state |
| BLOOM_FILTER | 5.16 | - | lock-free | no | fast existence checks |
| SOCKMAP | 4.14 | u32 | lock | - | socket redirection |
| DEVMAP | 4.14 | u32 | - | - | XDP device redirection |
| CPUMAP | 4.15 | u32 | - | - | XDP CPU redirection |

---

<!-- chunk: 🔗 Related Resources -->## 🔗 Related Resources

- **Kernel documentation**: [kernel.org/doc/html/latest/bpf/maps.html](https://www.kernel.org/doc/html/latest/bpf/maps.html)
- **libbpf API**: [libbpf.readthedocs.io](https://libbpf.readthedocs.io/)
- **bpftool**: `man bpftool-map`
- **BCC Map documentation**: [github.com/iovisor/bcc/blob/master/docs/reference_guide.md](https://github.com/iovisor/bcc/blob/master/docs/reference_guide.md)
- **eBPF sample programs**: [github.com/torvalds/linux/tree/master/samples/bpf](https://github.com/torvalds/linux/tree/master/samples/bpf)
- **[[Cilium|Cilium]] eBPF Go library**: [github.com/cilium/ebpf](https://github.com/cilium/ebpf)

---

<!-- chunk: 📝 Related Documents -->## 📝 Related Documents

- **[01-eBPF Architecture Fundamentals](./01-ebpf-architecture-fundamentals.md)** - the eBPF virtual machine, program types, the verifier
- **[03-Cilium CNI Architecture](./03-cilium-cni-architecture.md)** - how Maps are used in practice within Cilium
- **[07-Hubble Network Observability](./07-hubble-network-observability.md)** - how Ring Buffer is used in observability
- **[08-bcc and bpftrace Toolchain](./08-bcc-bpftrace-tools.md)** - Map debugging and analysis tools

---
*This document is maintained by the cloud-native technology expert team, based on the latest 2026 eBPF ecosystem practices.*

---

<!-- chunk: Obsidian Related Documents -->## Obsidian Related Documents

- domain-03-networking-traffic MOC
- [[domain-03-networking-traffic/README.md|Domain 03: eBPF Technology Stack]]
- Domain 03 eBPF Technology — Open Source Project Index
- eBPF Architecture Fundamentals and Program Types
- Cilium CNI Architecture and Deployment
- Cilium Network Policy L3/L4/L7
- Cilium Service Mesh Sidecar-less Architecture
- Tetragon Runtime Security
- Hubble Network Observability
- bcc and bpftrace Tools
- eBPF Performance Optimization Practice
- eBPF Security Applications and Use Cases

## See Also

- 10-ebpf-security-applications
- 01-ebpf-architecture-fundamentals
- 03-cilium-cni-architecture
- 04-cilium-network-policy


<!-- risk-assessed -->
