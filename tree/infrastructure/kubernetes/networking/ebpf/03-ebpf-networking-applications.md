---
title: eBPF Network Application Practical
description: 'Cilium CNI Advanced Configuration, XDP Load Balancing, TC Traffic Control and High Performance Service Mesh'
summary: 'Cilium CNI Advanced Configuration, XDP Load Balancing, TC Traffic Control and High Performance Service Mesh'
category: specialized-tech
tags:
- ebpf
- cilium
- xdp
- katran
- service-mesh
- cni
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
- What is Cilium CNI
- How to configure advanced network policies in Cilium
- How does XDP load balancing work
trigger_keywords:
- cilium
- cni
- xdp
- katran
- service-mesh
- ebpf
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
source_path: tree/infrastructure/kubernetes/networking/ebpf/03-ebpf-networking-applications.md
---

> **Production Environment Security Reminders**
>
> This document contains executable operational commands. Please confirm before execution: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the command has been validated in a non-production environment. Command risk levels are annotated: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).


# eBPF Network Application Practical

## 1. Cilium CNI Architecture

Cilium based on eBPF's Kubernetes CNI implementation, replacing iptables/IPVS:

```
Pod → eBPF Datapath → Network Policy → Service Load Balancing → Target Pod
  │                      │              │
  │                      └── L3/L4/L7   └── Maglev/random/polling
  └── veth pair / ipvlan
```

Core features:

| Feature | Description |
|------|------|
| **eBPF Datapath** | Replaces iptables, O(1) performance |
| **Network Policy** | Layer 3/4/7 network policies |
| **Service Mesh** | Sidecar-free Service Mesh |
| **Hubble** | Network observability platform |
| **Cluster Mesh** | Multi-cluster networking |

## 2. Cilium Installation and Configuration

### 2.1 Basic Installation

``` bash
# 🔴 Medium Risk: modifies cluster/resource status, confirm target, impact scope, and authorization before proceeding
# Helm Installation
helm repo add cilium https://helm.cilium.io/
helm repo update

helm install cilium cilium/cilium \
  --namespace kube-system \
  --set kubeProxyReplacement=strict \
  --set k8sServiceHost=10.0.0.10 \
  --set k8sServicePort=6443 \
  --set hubble.enabled=true \
  --set hubble.relay.enabled=true \
  --set hubble.ui.enabled=true
```
### 2.2 Advanced Configuration

```yaml
# values-cilium.yaml
kubeProxyReplacement: strict
k8sServiceHost: "10.0.0.10"
k8sServicePort: "6443"

# eBPF Configuration
bpf:
  hostLegacyRouting: false
  masquerade: true
  tproxy: true
  preallocateMaps: true

# IPAM Configuration
ipam:
  mode: "kubernetes"
  operator:
    clusterPoolIPv4PodCIDR: "10.244.0.0/16"
    clusterPoolIPv4MaskSize: "24"

# Hubble Observability
hubble:
  enabled: true
  listenAddress: ":4244"
  metrics:
    enabled:
      - dns
      - drop
      - tcp
      - flow
      - icmp
      - http
  relay:
    enabled: true
  ui:
    enabled: true

# Network Policies
policyEnforcement: "default"
policyAuditMode: false

# Advanced Features
enableIPv4Masquerade: true
enableIPv6Masquerade: false
enableHostLegacyRouting: false
tunnel: "disabled"    # native routing 模式
autoDirectNodeRoutes: true
```

### 2.3 Bandwidth Management (BBR)

```yaml
# Enable BBR Congestion Control
bandwidthManager:
  enabled: true
  bbr: true
```

## 3. Cilium Network Policy

### 3.1 Layer 3/Layer 4 Policies

```yaml
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: backend-policy
  namespace: production
spec:
  endpointSelector:
    matchLabels:
      app: backend
  ingress:
    - fromEndpoints:
        - matchLabels:
            app: frontend
      toPorts:
        - ports:
            - port: "8080"
              protocol: TCP
    - fromEndpoints:
        - matchLabels:
            app: monitoring
      toPorts:
        - ports:
            - port: "9090"
              protocol: TCP
  egress:
    - toEndpoints:
        - matchLabels:
            app: database
      toPorts:
        - ports:
            - port: "5432"
              protocol: TCP
    - toFQDNs:
        - matchName: "api.external.com"
      toPorts:
        - ports:
            - port: "443"
              protocol: TCP
```

### 3.2 Layer 7 Policies (HTTP)

```yaml
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: api-l7-policy
spec:
  endpointSelector:
    matchLabels:
      app: api-gateway
  ingress:
    - fromEndpoints:
        - matchLabels:
            app: frontend
      toPorts:
        - ports:
            - port: "8080"
              protocol: TCP
        - rules:
            http:
              - method: GET
                path: "/api/v1/.*"
              - method: POST
                path: "/api/v1/orders"
              - method: GET
                path: "/healthz"
```

### 3.3 DNS Policies

```yaml
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: dns-policy
spec:
  endpointSelector:
    matchLabels:
      app: backend
  egress:
    - toEndpoints:
        - matchLabels:
            "k8s:io.kubernetes.pod.namespace": kube-system
            "k8s:k8s-app": kube-dns
      toPorts:
        - ports:
            - port: "53"
              protocol: UDP
          rules:
            dns:
              - matchPattern: "*.production.svc.cluster.local"
              - matchPattern: "*.external.com"
    - toFQDNs:
        - matchName: "db.external.com"
      toPorts:
        - ports:
            - port: "5432"
              protocol: TCP
```

## 4. XDP Load Balancing

### 4.1 XDP Program Example

```c
// xdp_lb.c - Simple XDP Load Balancer
#include "vmlinux.h"
#include <bpf/bpf_helpers.h>
#include <bpf/bpf_endian.h>

struct {
    __uint(type, BPF_MAP_TYPE_HASH);
    __uint(max_entries, 256);
    __type(key, __u32);     // 目标 IP
    __type(value, __u32);   // 后端 IP
} backends SEC(".maps");

SEC("xdp")
int xdp_load_balancer(struct xdp_md *ctx) {
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

    // Only handle TCP
    if (iph->protocol != IPPROTO_TCP)
        return XDP_PASS;

    // Lookup backend
    __u32 vip = iph->daddr;
    __u32 *backend = bpf_map_lookup_elem(&backends, &vip);
    if (!backend)
        return XDP_PASS;

    // Replace target IP
    iph->daddr = *backend;

    // Recalculate checksum
    iph->check = 0;
    iph->check = bpf_csum_diff(0, 0, (__be32 *)iph, sizeof(*iph), 0);

    // Simplify MAC address modification
    // ...

    return XDP_TX;
}
```

### 4.2 Katran (Facebook XDP Load Balancer)

```bash
# Katran Architecture
# User Space: Manage backend pool, health checks, configuration updates
# Kernel Space: XDP program processes each packet

# Katran Core Features:
# - Maglev Consistent Hashing
# - GUE/GIP Encapsulation
# Health Checks
# DDoS Protection
```

### 4.3 XDP Integration with Cilium

```yaml
# Cilium uses XDP to Accelerate Service Load Balancing
# values-cilium.yaml
loadBalancer:
  algorithm: maglev    # 一致性哈希
  acceleration: native # XDP 加速
```

## 5. TC Traffic Control

### 5.1 TC Integration with eBPF

```c
// tc_mark.c - Uses TC eBPF to Mark Traffic
#include "vmlinux.h"
#include <bpf/bpf_helpers.h>

SEC("tc")
int tc_mark_priority(struct __sk_buff *skb) {
    void *data = (void *)(long)skb->data;
    void *data_end = (void *)(long)skb->data_end;

    struct ethhdr *eth = data;
    if ((void *)(eth + 1) > data_end)
        return TC_ACT_OK;

    if (eth->h_proto != bpf_htons(ETH_P_IP))
        return TC_ACT_OK;

    struct iphdr *iph = (void *)(eth + 1);
    if ((void *)(iph + 1) > data_end)
        return TC_ACT_OK;

    // Mark High-Priority Traffic
    if (iph->protocol == IPPROTO_TCP) {
        struct tcphdr *tcp = (void *)(iph + 1);
        if ((void *)(tcp + 1) > data_end)
            return TC_ACT_OK;

        // Mark HTTPS Traffic as High-Priority
        if (tcp->dest == bpf_htons(443)) {
            skb->priority = 100;
        }
    }

    return TC_ACT_OK;
}
```

### 5.2 TC Command Configuration

```bash
# Load eBPF TC Program
tc qdisc add dev eth0 clsact
tc filter add dev eth0 ingress bpf da obj tc_mark.o sec tc
tc filter add dev eth0 egress bpf da obj tc_mark.o sec tc

# View Loaded TC Programs
tc filter show dev eth0 ingress
```

## 6. IPVS Alternatives

### 6.1 Cilium Alternative to kube-proxy

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state; confirm target, impact scope, and authorization before execution
# Disable kube-proxy, use Cilium eBPF
helm upgrade cilium cilium/cilium \
  --namespace kube-system \
  --set kubeProxyReplacement=strict \
  --set k8sServiceHost=10.0.0.10 \
  --set k8sServicePort=6443

# Verify
cilium status
cilium service list
```
### 6.2 Performance Comparison

| Solution | Connections per second | 99th percentile latency | CPU overhead |
|------|-----------|----------|----------|
| iptables | 50K | 5ms | High |
| IPVS | 200K | 2ms | Medium |
| Cilium eBPF | 500K | 0.5ms | Low |

### 6.3 DSR (Direct Server Return)

```yaml
# Enable DSR Mode
loadBalancer:
  mode: dsr    # 直接服务器返回
  dsrEncapsulation: geneve
```

## 7. High Performance Service Mesh

### 7.1 Cilium Service Mesh(Sidecar-free)

```yaml
# Enable Cilium Service Mesh
kubeProxyReplacement: strict
hubble:
  enabled: true
  relay:
    enabled: true
  ui:
    enabled: true
```

### 7.2 Layer 7 Load Balancing

```yaml
apiVersion: cilium.io/v2
kind: CiliumEnvoyConfig
metadata:
  name: envoy-config
  namespace: production
spec:
  services:
    - name: backend
      namespace: production
  backendServices:
    - name: backend
      namespace: production
  resources:
    - "@type": type.googleapis.com/envoy.config.listener.v3.Listener
      name: envoy-l7-listener
      filter_chains:
        - filters:
            - name: envoy.filters.network.http_connection_manager
              typed_config:
                "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
                stat_prefix: ingress_http
                route_config:
                  virtual_hosts:
                    - name: backend
                      domains: ["*"]
                      routes:
                        - match:
                            prefix: "/api/v1"
                          route:
                            cluster: backend
                http_filters:
                  - name: envoy.filters.http.router
```

### 7.3 mTLS Encryption

```yaml
# Enable WireGuard Encryption
encryption:
  enabled: true
  type: wireguard
  nodeEncryption: true
```

### 7.4 SPIFFE/SPIRE Integration

```yaml
# SPIRE Integration
authentication:
  enabled: true
  mutual:
    spire:
      enabled: true
      install:
        enabled: true
```

## 8. Multi-cluster Networking (Cluster Mesh)

### 8.1 Configuration

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state; confirm target, impact scope, and authorization before execution
# Cluster 1
helm install cilium cilium/cilium \
  --namespace kube-system \
  --set cluster.name=cluster1 \
  --set cluster.id=1 \
  --set etcd.enabled=true \
  --set etcd.managed=true

# Cluster 2
helm install cilium cilium/cilium \
  --namespace kube-system \
  --set cluster.name=cluster2 \
  --set cluster.id=2 \
  --set etcd.enabled=true \
  --set etcd.managed=true
```
### 8.2 Cross-cluster Service Discovery

```yaml
apiVersion: cilium.io/v2
kind: CiliumNetworkPolicy
metadata:
  name: cross-cluster-policy
spec:
  endpointSelector:
    matchLabels:
      app: backend
  ingress:
    - fromEndpoints:
        - matchLabels:
            "io.cilium.k8s.namespace.labels.cluster": "cluster2"
            app: frontend
```

## 9. Monitoring and Troubleshooting

```bash
# Cilium Status
cilium status

# View eBPF Programs
cilium bpf lb list
cilium bpf endpoint list

# Hubble Network Flow
hubble observe --namespace production --since 1h

# Policy Audit
cilium monitor --type drop
cilium monitor --type policy-verdict

# End-to-End Latency
cilium connectivity test
```

---

## Related

- [[domain-15-specialized-tech/05-ebpf-programming/01-ebpf-programming-fundamentals|eBPF Development Basics]]
- [[domain-15-specialized-tech/05-ebpf-programming/02-ebpf-observability-tools|eBPF Observability Tools]]
- [[domain-15-specialized-tech/05-ebpf-programming/04-ebpf-security-runtime|eBPF Security Runtime]]

## See Also

- [Cilium Official Documentation](https://docs.cilium.io/)
- [Cilium Network Policy](https://docs.cilium.io/en/stable/network/kubernetes/policy/)
- [Hubble](https://docs.cilium.io/en/stable/observability/)


<!-- risk-assessed -->
