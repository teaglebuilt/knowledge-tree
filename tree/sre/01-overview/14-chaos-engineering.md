---
title: 52 - Chaos Engineering Practices
description: 'title: 52 - Chaos Engineering Practices'
summary: 'title: 52 - Chaos Engineering Practices'
category: general
tags:
- k8s
- observability
- prometheus
- monitoring
- scheduler
- grafana
- coredns
- helm
- containerd
- docker
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 35min
intent_queries:
- What is chaos-engineering?
- How to use chaos-engineering
- Best practices for chaos-engineering
trigger_keywords:
- Chaos Engineering Practices
- observability
prerequisites:
- kubectl-basics
- observability-basics
- helm-basics
- prometheus-basics
- monitoring-basics
- ebpf-basics
- mysql-basics
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/01-overview/14-chaos-engineering.md
---

> **Production Environment Safety Notice**
>
> This document contains directly executable operations commands. Before execution, please confirm: that the target cluster and Namespace are correct; that you have sufficient RBAC permissions; that you have verified the commands in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state, but can usually be rolled back), 🟢 Low risk/read-only (information gathering, no side effects).




title: 52 - Chaos Engineering Practices
description: '# 52 - Chaos Engineering Practices'
category: observability
tags:
- k8s
- observability
- monitoring
- logging
- tracing
- scheduler
- prometheus
- grafana
- coredns
- helm
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Operations Engineers
- Monitoring Engineers
estimated_read_time: 5min
intent_queries:
- What is Chaos Engineering Practices
- How to implement Chaos Engineering Practices
- Kubernetes 8 observability best practices
trigger_keywords:
- Chaos Engineering Practices
- observability
cross_refs:
- type: domain
  path: ../domain-01-cluster-fundamentals/
  label: 'Related Knowledge Domain: domain-01-cluster-fundamentals'
- type: domain
  path: ../domain-02-workloads-applications/
  label: 'Related Knowledge Domain: domain-02-workloads-applications'
- type: domain
  path: ../domain-03-networking-traffic/
  label: 'Related Knowledge Domain: domain-03-networking-traffic'
- type: domain
  path: ../domain-07-platform-engineering/
  label: 'Related Knowledge Domain: domain-07-platform-engineering'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/promql.md
  label: 'Quick Reference: promql'
authors:
- name: KUDIG Team
  role: contributor
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
---

# 52 - Chaos Engineering Practices

> **Applicable Versions**: v1.25 - v1.32 | **Last Updated**: 2026-01 | **Reference**: [chaos-mesh.org](https://chaos-mesh.org/)

<!-- chunk: Chaos Engineering Architecture -->
## Chaos Engineering Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      Chaos Engineering Practice Architecture                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                     Chaos Engineering Lifecycle                      │  │
│   │                                                                      │  │
│   │   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐     │  │
│   │   │  Plan    │───▶│ Execute  │───▶│ Observe  │───▶│ Analyze  │     │  │
│   │   │ Planning │    │ Execute  │    │ Observe  │    │ Analyze  │     │  │
│   │   └──────────┘    └──────────┘    └──────────┘    └──────────┘     │  │
│   │        │                                               │            │  │
│   │        └───────────────────────────────────────────────┘            │  │
│   │                          Feedback Loop                              │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                     Chaos Mesh Architecture                          │  │
│   │                                                                      │  │
│   │   ┌────────────────────────────────────────────────────────────┐   │  │
│   │   │                   Chaos Dashboard                           │   │  │
│   │   │  • Web UI Management Interface    • Experiment Create/Manage│   │  │
│   │   │  • Real-time Status Monitoring                             │   │  │
│   │   └────────────────────────────────────────────────────────────┘   │  │
│   │                              │                                      │  │
│   │   ┌────────────────────────────────────────────────────────────┐   │  │
│   │   │              Chaos Controller Manager                       │   │  │
│   │   │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │   │  │
│   │   │  │ PodChaos     │  │ NetworkChaos │  │ IOChaos      │     │   │  │
│   │   │  │ Controller   │  │ Controller   │  │ Controller   │     │   │  │
│   │   │  └──────────────┘  └──────────────┘  └──────────────┘     │   │  │
│   │   │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │   │  │
│   │   │  │ StressChaos  │  │ TimeChaos    │  │ DNSChaos     │     │   │  │
│   │   │  │ Controller   │  │ Controller   │  │ Controller   │     │   │  │
│   │   │  └──────────────┘  └──────────────┘  └──────────────┘     │   │  │
│   │   └────────────────────────────────────────────────────────────┘   │  │
│   │                              │                                      │  │
│   │   ┌────────────────────────────────────────────────────────────┐   │  │
│   │   │                   Chaos Daemon (DaemonSet)                  │   │  │
│   │   │  • Runs on each node              • Inject issues into containers
│   │   │  • Uses eBPF/ptrace               • Network/IO/Process injection
│   │   └────────────────────────────────────────────────────────────┘   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                     Fault Injection Layers                          │  │
│   │                                                                      │  │
│   │   ┌─────────────────────────────────────────────────────────────┐  │  │
│   │   │ Layer 4: Application Layer │ HTTPChaos, JVMChaos, GRPCChaos│  │  │
│   │   ├─────────────────────────────────────────────────────────────┤  │  │
│   │   │ Layer 3: Service Layer     │ DNSChaos, PodChaos, NetworkChaos│  │  │
│   │   ├─────────────────────────────────────────────────────────────┤  │  │
│   │   │ Layer 2: System Layer      │ IOChaos, StressChaos, TimeChaos │  │  │
│   │   ├─────────────────────────────────────────────────────────────┤  │  │
│   │   │ Layer 1: Infrastructure    │ AWSChaos, GCPChaos, PhysicalMachine
│   │   └─────────────────────────────────────────────────────────────┘  │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- chunk: Chaos Engineering Principles -->
## Chaos Engineering Principles

| Principle | Description | Practice Method | Importance |
|-----|------|---------|-------|
| **Establish Steady State Hypothesis** | Define system normal behavior metrics | SLI/SLO definition, baseline measurement | P0 |
| **Real World Events** | Simulate real problem scenarios | Based on historical issues, probability modeling | P0 |
| **Production Environment Experiments** | Real environments reveal real issues | Canary testing, canary deployment | P1 |
| **Automated Continuous** | Run experiments continuously | CI/CD integration, scheduled execution | P1 |
| **Minimize Blast Radius** | Control experiment impact scope | Progressive scaling, emergency stop | P0 |
| **Document and Learn** | Record findings and improve system | Post-mortem review, knowledge base | P1 |

<!-- chunk: Chaos Engineering Tools Comparison -->
## Chaos Engineering Tools Comparison

| Tool | Architecture | Supported Scenarios | K8s Native | Learning Curve | Community Activity | Use Case |
|-----|------|---------|--------|---------|-----------|---------|
| **Chaos Mesh** | Operator | All scenarios | ✅ | Medium | ⭐⭐⭐⭐⭐ | K8s environment first choice |
| **LitmusChaos** | Operator | All scenarios | ✅ | Medium | ⭐⭐⭐⭐⭐ | GitOps integration |
| **Chaos Monkey** | Standalone | Instance termination | ❌ | Low | ⭐⭐⭐ | Netflix ecosystem |
| **Gremlin** | SaaS | All scenarios | ✅ | Low | ⭐⭐⭐⭐ | Enterprise-grade managed |
| **AWS FIS** | Managed | AWS resources | ❌ | Low | ⭐⭐⭐⭐ | AWS environment |
| **Chaosblade** | Agent | All scenarios | ✅ | Medium | ⭐⭐⭐⭐ | Alibaba ecosystem |
| **Toxiproxy** | Proxy | Network issues | ❌ | Low | ⭐⭐⭐ | Test environment |
| **Pumba** | CLI | Container issues | ✅ | Low | ⭐⭐⭐ | Docker environment |

<!-- chunk: Chaos Mesh Problem Type Details -->
## Chaos Mesh Problem Type Details

| Type | CRD | Description | Injection Method | Typical Scenario |
|-----|-----|------|---------|---------|
| **Pod Issues** | PodChaos | Kill Pod/container failure | API call | Test self-healing capability |
| **Network Issues** | NetworkChaos | Delay/packet loss/partition | tc/iptables | Test service degradation |
| **File System** | IOChaos | IO delay/error | fuse/eBPF | Test storage issues |
| **Kernel Issues** | KernelChaos | Kernel error injection | eBPF | Test system stability |
| **Time Skew** | TimeChaos | Clock skew | VDSO hook | Test time-sensitive logic |
| **Stress Testing** | StressChaos | CPU/memory pressure | stress-ng | Test resource contention |
| **JVM Issues** | JVMChaos | Java exception injection | Byteman | Test Java applications |
| **HTTP Issues** | HTTPChaos | HTTP request issues | eBPF/sidecar | Test API fault tolerance |
| **DNS Issues** | DNSChaos | DNS resolution issues | CoreDNS injection | Test DNS dependencies |
| **Cloud Platform Issues** | AWSChaos/GCPChaos | Cloud resource issues | Cloud API | Test cloud failover |

<!-- chunk: Chaos Mesh Installation and Deployment -->
## Chaos Mesh Installation and Deployment

### Helm Installation

> ⚠️ **🟡 Medium Risk Change** — modifies cluster resource state, recommend --dry-run or diff before confirming
> - `helm upgrade/install`: deploy/upgrade release
> - `kubectl apply/create/replace`: create/modify cluster resources

``` bash
# 🟡 Medium risk: will modify cluster/resource state, confirm target, impact scope, and authorization before executing
# Add Helm repository
helm repo add chaos-mesh https://charts.chaos-mesh.org
helm repo update

# Create namespace
kubectl create namespace chaos-mesh

# Install Chaos Mesh
helm install chaos-mesh chaos-mesh/chaos-mesh \
  -n chaos-mesh \
  --set chaosDaemon.runtime=containerd \
  --set chaosDaemon.socketPath=/run/containerd/containerd.sock \
  --set dashboard.securityMode=true \
  --set dashboard.service.type=ClusterIP

# Verify installation
kubectl get pods -n chaos-mesh
kubectl get crd | grep chaos-mesh

# Access Dashboard (via port-forward)
kubectl port-forward -n chaos-mesh svc/chaos-dashboard 2333:2333
```
### RBAC Configuration

```yaml
# chaos-mesh-rbac.yaml - fine-grained RBAC control
apiVersion: v1
kind: ServiceAccount
metadata:
  name: chaos-operator
  namespace: production
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: chaos-operator-role
  namespace: production
rules:
# Allow chaos experiments to run in production namespace
- apiGroups: ["chaos-mesh.org"]
  resources: ["*"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
- apiGroups: [""]
  resources: ["pods", "pods/log"]
  verbs: ["get", "list", "watch", "delete"]
- apiGroups: [""]
  resources: ["events"]
  verbs: ["get", "list", "watch", "create"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: chaos-operator-binding
  namespace: production
subjects:
- kind: ServiceAccount
  name: chaos-operator
  namespace: production
roleRef:
  kind: Role
  name: chaos-operator-role
  apiGroup: rbac.authorization.k8s.io
```

<!-- chunk: PodChaos Detailed Configuration -->
## PodChaos Detailed Configuration

### Pod Kill Experiment

```yaml
# pod-kill-experiment.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: PodChaos
metadata:
  name: pod-kill-experiment
  namespace: chaos-mesh
  labels:
    experiment-type: resilience
    target-service: api-server
spec:
  # Problem action: pod-kill/pod-failure/container-kill
  action: pod-kill
  
  # Selection mode
  # one: select one randomly
  # all: select all matches
  # fixed: fixed number
  # fixed-percent: fixed percentage
  # random-max-percent: random max percentage
  mode: fixed-percent
  value: "30"  # Kill 30% of Pods
  
  # Target selector
  selector:
    namespaces:
    - production
    labelSelectors:
      app: api-server
      tier: backend
    # Optional: node selection
    nodeSelectors:
      node-type: worker
    # Optional: Pod name regex
    pods:
      production:
      - api-server-*
    # Optional: exclude specific Pods
    expressionSelectors:
    - key: version
      operator: NotIn
      values:
      - canary
      
  # Duration
  duration: "60s"
  
  # Graceful termination period (only pod-kill)
  gracePeriod: 0
  
  # Scheduler configuration (optional)
  scheduler:
    cron: "@every 4h"  # Run every 4 hours
    
---
# container-kill experiment - only kill container without Pod
apiVersion: chaos-mesh.org/v1alpha1
kind: PodChaos
metadata:
  name: container-kill-experiment
  namespace: chaos-mesh
spec:
  action: container-kill
  mode: one
  selector:
    namespaces:
    - production
    labelSelectors:
      app: web-server
  containerNames:
  - nginx  # Only kill nginx container, preserve sidecar
  duration: "30s"
  
---
# pod-failure experiment - simulate Pod issues without deletion
apiVersion: chaos-mesh.org/v1alpha1
kind: PodChaos
metadata:
  name: pod-failure-experiment
  namespace: chaos-mesh
spec:
  action: pod-failure
  mode: fixed
  value: "2"  # Affect 2 Pods
  selector:
    namespaces:
    - production
    labelSelectors:
      app: worker
  duration: "120s"  # Problem persists for 2 minutes then auto-recovers
```

<!-- chunk: NetworkChaos Detailed Configuration -->
## NetworkChaos Detailed Configuration

### Network Delay Experiment

```yaml
# network-delay-experiment.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: network-delay-to-database
  namespace: chaos-mesh
spec:
  action: delay
  mode: all
  
  # Source selector (affected Pods)
  selector:
    namespaces:
    - production
    labelSelectors:
      app: api-server
      
  # Delay configuration
  delay:
    latency: "100ms"       # Base latency
    correlation: "25"       # Correlation (0-100), affects latency variance consistency
    jitter: "50ms"         # Jitter range
    
  # Direction: to/from/both
  direction: to
  
  # Target selector (delay target)
  target:
    selector:
      namespaces:
      - database
      labelSelectors:
        app: mysql
    mode: all
    
  # External target (optional, for external services)
  externalTargets:
  - "api.external-service.com"
  
  duration: "5m"

---
# Network packet loss experiment
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: network-loss-experiment
  namespace: chaos-mesh
spec:
  action: loss
  mode: all
  selector:
    namespaces:
    - production
    labelSelectors:
      app: frontend
  loss:
    loss: "25"              # Packet loss rate 25%
    correlation: "25"
  direction: both
  duration: "3m"

---
# Network partition experiment
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: network-partition-experiment
  namespace: chaos-mesh
spec:
  action: partition
  mode: all
  selector:
    namespaces:
    - production
    labelSelectors:
      app: service-a
  direction: both
  target:
    selector:
      namespaces:
      - production
      labelSelectors:
        app: service-b
    mode: all
  duration: "2m"

---
# Bandwidth limit experiment
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: bandwidth-limit-experiment
  namespace: chaos-mesh
spec:
  action: bandwidth
  mode: all
  selector:
    namespaces:
    - production
    labelSelectors:
      app: data-processor
  bandwidth:
    rate: "1mbps"           # Limit bandwidth to 1Mbps
    limit: 20971520         # Queue size (bytes)
    buffer: 10000           # Buffer size
  direction: to
  target:
    selector:
      namespaces:
      - storage
      labelSelectors:
        app: minio
    mode: all
  duration: "5m"

---
# Network duplicate packet experiment
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: network-duplicate-experiment
  namespace: chaos-mesh
spec:
  action: duplicate
  mode: all
  selector:
    namespaces:
    - production
    labelSelectors:
      app: message-queue
  duplicate:
    duplicate: "10"         # 10% of packets will be duplicated
    correlation: "25"
  direction: both
  duration: "3m"

---
# Network packet corruption experiment
apiVersion: chaos-mesh.org/v1alpha1
kind: NetworkChaos
metadata:
  name: network-corrupt-experiment
  namespace: chaos-mesh
spec:
  action: corrupt
  mode: all
  selector:
    namespaces:
    - production
    labelSelectors:
      app: tcp-service
  corrupt:
    corrupt: "5"            # 5% of packets will be corrupted
    correlation: "25"
  direction: both
  duration: "2m"
```

<!-- chunk: StressChaos Detailed Configuration -->
## StressChaos Detailed Configuration

```yaml
# stress-chaos-experiment.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: StressChaos
metadata:
  name: cpu-memory-stress
  namespace: chaos-mesh
spec:
  mode: one
  selector:
    namespaces:
    - production
    labelSelectors:
      app: compute-intensive
      
  # CPU pressure configuration
  stressors:
    cpu:
      workers: 2            # Number of CPU pressure workers
      load: 80              # CPU load percentage
      
    # Memory pressure configuration
    memory:
      workers: 2            # Number of memory pressure workers
      size: "512MB"         # Memory consumed per worker
      # Or use percentage
      # size: "80%"
      
  # Container-level pressure (optional)
  containerNames:
  - main-app
  
  duration: "5m"

---
# CPU pressure only
apiVersion: chaos-mesh.org/v1alpha1
kind: StressChaos
metadata:
  name: cpu-stress-only
  namespace: chaos-mesh
spec:
  mode: fixed
  value: "3"
  selector:
    namespaces:
    - production
    labelSelectors:
      app: api-server
  stressors:
    cpu:
      workers: 4
      load: 90
  duration: "3m"

---
# Memory pressure only (test OOM handling)
apiVersion: chaos-mesh.org/v1alpha1
kind: StressChaos
metadata:
  name: memory-stress-oom-test
  namespace: chaos-mesh
spec:
  mode: one
  selector:
    namespaces:
    - production
    labelSelectors:
      app: memory-sensitive
  stressors:
    memory:
      workers: 1
      size: "90%"           # Consume 90% of container memory limit
      oomScoreAdj: 1000     # Increase OOM priority
  duration: "2m"
```

<!-- chunk: IOChaos Detailed Configuration -->
## IOChaos Detailed Configuration

```yaml
# io-chaos-experiment.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: IOChaos
metadata:
  name: io-latency-experiment
  namespace: chaos-mesh
spec:
  action: latency
  mode: one
  selector:
    namespaces:
    - production
    labelSelectors:
      app: database
      
  # Mount volume path
  volumePath: /var/lib/mysql
  
  # File path pattern (supports wildcards)
  path: /var/lib/mysql/data/**
  
  # Delay configuration
  delay: "100ms"
  
  # Percentage of impact
  percent: 50               # 50% of IO operations affected
  
  # IO operation type filter
  methods:
  - read
  - write
  - fsync
  
  # Container name
  containerNames:
  - mysql
  
  duration: "5m"

---
# IO fault injection
apiVersion: chaos-mesh.org/v1alpha1
kind: IOChaos
metadata:
  name: io-fault-experiment
  namespace: chaos-mesh
spec:
  action: fault
  mode: one
  selector:
    namespaces:
    - production
    labelSelectors:
      app: storage-app
  volumePath: /data
  path: /data/critical/**
  errno: 5                  # EIO error code
  percent: 10               # 10% of IO returns error
  methods:
  - write
  duration: "3m"

---
# IO attribute override (return error file attributes)
apiVersion: chaos-mesh.org/v1alpha1
kind: IOChaos
metadata:
  name: io-attr-override
  namespace: chaos-mesh
spec:
  action: attrOverride
  mode: one
  selector:
    namespaces:
    - production
    labelSelectors:
      app: file-processor
  volumePath: /data
  path: /data/input/**
  attr:
    size: 0                 # File size display as 0
  percent: 100
  duration: "2m"
```

<!-- chunk: DNSChaos Detailed Configuration -->
## DNSChaos Detailed Configuration

```yaml
# dns-chaos-experiment.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: DNSChaos
metadata:
  name: dns-error-experiment
  namespace: chaos-mesh
spec:
  action: error
  mode: all
  selector:
    namespaces:
    - production
    labelSelectors:
      app: external-api-client
      
  # DNS domain pattern
  patterns:
  - "api.external-service.com"
  - "*.third-party.io"
  
  duration: "3m"

---
# DNS random response
apiVersion: chaos-mesh.org/v1alpha1
kind: DNSChaos
metadata:
  name: dns-random-experiment
  namespace: chaos-mesh
spec:
  action: random
  mode: all
  selector:
    namespaces:
    - production
    labelSelectors:
      app: dns-dependent
  patterns:
  - "internal-service.default.svc.cluster.local"
  duration: "2m"
```

<!-- chunk: TimeChaos Detailed Configuration -->
## TimeChaos Detailed Configuration

```yaml
# time-chaos-experiment.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: TimeChaos
metadata:
  name: time-skew-experiment
  namespace: chaos-mesh
spec:
  mode: all
  selector:
    namespaces:
    - production
    labelSelectors:
      app: scheduler-service
      
  # Time offset configuration
  timeOffset: "-2h"         # Time back 2 hours
  # Or forward: "+30m"
  
  # Clock ID (optional)
  # CLOCK_REALTIME: 0 (default)
  # CLOCK_MONOTONIC: 1
  clockIds:
  - 0
  
  # Container name
  containerNames:
  - main-app
  
  duration: "5m"

---
# Test leap second scenario
apiVersion: chaos-mesh.org/v1alpha1
kind: TimeChaos
metadata:
  name: leap-second-test
  namespace: chaos-mesh
spec:
  mode: one
  selector:
    namespaces:
    - production
    labelSelectors:
      app: time-sensitive
  timeOffset: "-1s"
  duration: "10s"
```

<!-- chunk: HTTPChaos Detailed Configuration -->
## HTTPChaos Detailed Configuration

```yaml
# http-chaos-experiment.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: HTTPChaos
metadata:
  name: http-delay-experiment
  namespace: chaos-mesh
spec:
  mode: all
  selector:
    namespaces:
    - production
    labelSelectors:
      app: api-gateway
      
  # Target configuration
  target: Request           # Request/Response
  port: 8080
  
  # Path matching
  path: "/api/v1/*"
  method: "GET"
  
  # Delay configuration
  delay: "2s"
  
  duration: "5m"

---
# HTTP fault injection
apiVersion: chaos-mesh.org/v1alpha1
kind: HTTPChaos
metadata:
  name: http-abort-experiment
  namespace: chaos-mesh
spec:
  mode: all
  selector:
    namespaces:
    - production
    labelSelectors:
      app: backend-service
  target: Response
  port: 8080
  path: "/api/orders/*"
  method: "POST"
  
  # Abort configuration
  abort: true
  
  # Or return specific status code
  # code: 503
  
  duration: "3m"

---
# HTTP response modification
apiVersion: chaos-mesh.org/v1alpha1
kind: HTTPChaos
metadata:
  name: http-replace-experiment
  namespace: chaos-mesh
spec:
  mode: all
  selector:
    namespaces:
    - production
    labelSelectors:
      app: api-server
  target: Response
  port: 8080
  path: "/api/health"
  
  # Replace response body
  replace:
    body: '{"status": "degraded"}'
    headers:
      X-Chaos-Injected: "true"
    code: 200
    
  duration: "5m"
```

<!-- chunk: JVMChaos Detailed Configuration -->
## JVMChaos Detailed Configuration

```yaml
# jvm-chaos-experiment.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: JVMChaos
metadata:
  name: jvm-exception-experiment
  namespace: chaos-mesh
spec:
  mode: one
  selector:
    namespaces:
    - production
    labelSelectors:
      app: java-service
      
  # Target class and method
  class: "com.example.service.OrderService"
  method: "processOrder"
  
  # Action type
  action: exception
  
  # Exception configuration
  exception: "java.lang.RuntimeException"
  message: "Chaos injected exception"
  
  # Container name
  containerNames:
  - java-app
  
  # JVM Agent port
  port: 9288
  
  duration: "3m"

---
# JVM GC pressure
apiVersion: chaos-mesh.org/v1alpha1
kind: JVMChaos
metadata:
  name: jvm-gc-stress
  namespace: chaos-mesh
spec:
  mode: one
  selector:
    namespaces:
    - production
    labelSelectors:
      app: java-service
  action: stress
  # GC pressure
  memType: heap
  duration: "5m"

---
# JVM method latency
apiVersion: chaos-mesh.org/v1alpha1
kind: JVMChaos
metadata:
  name: jvm-latency-experiment
  namespace: chaos-mesh
spec:
  mode: one
  selector:
    namespaces:
    - production
    labelSelectors:
      app: java-service
  class: "com.example.dao.UserDao"
  method: "findById"
  action: latency
  latency: 2000             # Method execution delay 2 seconds
  duration: "5m"

---
# JVM method return value modification
apiVersion: chaos-mesh.org/v1alpha1
kind: JVMChaos
metadata:
  name: jvm-return-experiment
  namespace: chaos-mesh
spec:
  mode: one
  selector:
    namespaces:
    - production
    labelSelectors:
      app: java-service
  class: "com.example.service.ConfigService"
  method: "isFeatureEnabled"
  action: return
  value: "false"            # Force return false
  duration: "3m"
```

<!-- chunk: Workflow Orchestration -->
## Workflow Orchestration

### Serial Execution

```yaml
# serial-workflow.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: Workflow
metadata:
  name: serial-chaos-workflow
  namespace: chaos-mesh
spec:
  entry: serial-entry
  templates:
  # Entry template - serial execution
  - name: serial-entry
    templateType: Serial
    deadline: "30m"
    children:
    - network-delay-step
    - verify-step-1
    - pod-kill-step
    - verify-step-2
    - stress-step
    
  # Step 1: network delay
  - name: network-delay-step
    templateType: NetworkChaos
    deadline: "5m"
    networkChaos:
      action: delay
      mode: all
      selector:
        namespaces: [production]
        labelSelectors:
          app: frontend
      delay:
        latency: "200ms"
      duration: "3m"
      
  # Verification step 1
  - name: verify-step-1
    templateType: Suspend
    deadline: "2m"
    suspend:
      duration: "1m"        # Pause 1 minute for verification
      
  # Step 2: Pod issues
  - name: pod-kill-step
    templateType: PodChaos
    deadline: "3m"
    podChaos:
      action: pod-kill
      mode: fixed-percent
      value: "20"
      selector:
        namespaces: [production]
        labelSelectors:
          app: api-server
          
  # Verification step 2
  - name: verify-step-2
    templateType: Suspend
    deadline: "2m"
    suspend:
      duration: "1m"
      
  # Step 3: resource pressure
  - name: stress-step
    templateType: StressChaos
    deadline: "6m"
    stressChaos:
      mode: one
      selector:
        namespaces: [production]
        labelSelectors:
          app: worker
      stressors:
        cpu:
          workers: 2
          load: 70
      duration: "5m"
```

### Parallel Execution

```yaml
# parallel-workflow.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: Workflow
metadata:
  name: parallel-chaos-workflow
  namespace: chaos-mesh
spec:
  entry: parallel-entry
  templates:
  # Entry template - parallel execution
  - name: parallel-entry
    templateType: Parallel
    deadline: "10m"
    children:
    - network-chaos-branch
    - pod-chaos-branch
    - stress-chaos-branch
    
  # Branch 1: network issues
  - name: network-chaos-branch
    templateType: NetworkChaos
    deadline: "5m"
    networkChaos:
      action: delay
      mode: all
      selector:
        namespaces: [production]
        labelSelectors:
          app: service-a
      delay:
        latency: "100ms"
      duration: "4m"
      
  # Branch 2: Pod issues
  - name: pod-chaos-branch
    templateType: PodChaos
    deadline: "5m"
    podChaos:
      action: pod-failure
      mode: one
      selector:
        namespaces: [production]
        labelSelectors:
          app: service-b
      duration: "4m"
      
  # Branch 3: resource pressure
  - name: stress-chaos-branch
    templateType: StressChaos
    deadline: "5m"
    stressChaos:
      mode: one
      selector:
        namespaces: [production]
        labelSelectors:
          app: service-c
      stressors:
        memory:
          workers: 1
          size: "256MB"
      duration: "4m"
```

### Complex Orchestration

```yaml
# complex-workflow.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: Workflow
metadata:
  name: complex-chaos-workflow
  namespace: chaos-mesh
spec:
  entry: main
  templates:
  # Main process
  - name: main
    templateType: Serial
    deadline: "1h"
    children:
    - prepare-phase
    - chaos-phase
    - cleanup-phase
    
  # Prepare phase
  - name: prepare-phase
    templateType: Suspend
    deadline: "5m"
    suspend:
      duration: "30s"       # Preparation time
      
  # Chaos phase - includes multiple parallel experiments
  - name: chaos-phase
    templateType: Parallel
    deadline: "30m"
    children:
    - frontend-chaos-serial
    - backend-chaos-serial
    
  # Frontend service chaos test process
  - name: frontend-chaos-serial
    templateType: Serial
    deadline: "15m"
    children:
    - frontend-network-delay
    - frontend-pod-kill
    
  - name: frontend-network-delay
    templateType: NetworkChaos
    deadline: "6m"
    networkChaos:
      action: delay
      mode: all
      selector:
        namespaces: [production]
        labelSelectors:
          tier: frontend
      delay:
        latency: "150ms"
      duration: "5m"
      
  - name: frontend-pod-kill
    templateType: PodChaos
    deadline: "4m"
    podChaos:
      action: pod-kill
      mode: one
      selector:
        namespaces: [production]
        labelSelectors:
          tier: frontend
          
  # Backend service chaos test process
  - name: backend-chaos-serial
    templateType: Serial
    deadline: "15m"
    children:
    - backend-io-chaos
    - backend-stress
    
  - name: backend-io-chaos
    templateType: IOChaos
    deadline: "6m"
    ioChaos:
      action: latency
      mode: one
      selector:
        namespaces: [production]
        labelSelectors:
          tier: backend
      volumePath: /data
      delay: "50ms"
      percent: 30
      duration: "5m"
      
  - name: backend-stress
    templateType: StressChaos
    deadline: "6m"
    stressChaos:
      mode: one
      selector:
        namespaces: [production]
        labelSelectors:
          tier: backend
      stressors:
        cpu:
          workers: 2
          load: 60
      duration: "5m"
      
  # Cleanup phase
  - name: cleanup-phase
    templateType: Suspend
    deadline: "5m"
    suspend:
      duration: "1m"        # Cleanup and observation time
```

<!-- chunk: LitmusChaos Configuration -->
## LitmusChaos Configuration

### ChaosEngine Configuration

```yaml
# litmus-chaos-engine.yaml
apiVersion: litmuschaos.io/v1alpha1
kind: ChaosEngine
metadata:
  name: nginx-chaos-engine
  namespace: production
spec:
  # Application info
  appinfo:
    appns: production
    applabel: "app=nginx"
    appkind: deployment
    
  # Service account
  chaosServiceAccount: litmus-admin
  
  # Task cleanup policy
  jobCleanUpPolicy: delete
  
  # Experiment list
  experiments:
  - name: pod-delete
    spec:
      components:
        env:
        - name: TOTAL_CHAOS_DURATION
          value: "60"
        - name: CHAOS_INTERVAL
          value: "10"
        - name: FORCE
          value: "false"
        - name: PODS_AFFECTED_PERC
          value: "50"
          
  - name: pod-network-latency
    spec:
      components:
        env:
        - name: TOTAL_CHAOS_DURATION
          value: "120"
        - name: NETWORK_LATENCY
          value: "100"
        - name: CONTAINER_RUNTIME
          value: "containerd"
          
  # Probe configuration
  probe:
  - name: http-probe
    type: httpProbe
    httpProbe/inputs:
      url: "http://nginx-service:80/health"
      insecureSkipVerify: false
      method:
        get:
          criteria: "=="
          responseCode: "200"
    mode: Continuous
    runProperties:
      probeTimeout: 5
      interval: 5
      retry: 3
      
---
# Litmus service account
apiVersion: v1
kind: ServiceAccount
metadata:
  name: litmus-admin
  namespace: production
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: litmus-admin
rules:
- apiGroups: [""]
  resources: ["pods", "pods/log", "events", "configmaps", "secrets", "services"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
- apiGroups: ["apps"]
  resources: ["deployments", "statefulsets", "replicasets", "daemonsets"]
  verbs: ["get", "list", "watch", "update", "patch"]
- apiGroups: ["batch"]
  resources: ["jobs"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
- apiGroups: ["litmuschaos.io"]
  resources: ["chaosengines", "chaosexperiments", "chaosresults"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
```

<!-- chunk: Steady State Metrics and Monitoring -->
## Steady State Metrics and Monitoring

### Steady State Metrics Definition

| Metric Category | Metric Name | Calculation | Threshold Recommendation | Monitoring Tool |
|---------|---------|---------|---------|---------|
| **Availability** | Successful Request Rate | successful requests / total requests | >99.9% | Prometheus |
| **Latency** | P99 Response Time | histogram_quantile | <500ms | Prometheus |
| **Latency** | P50 Response Time | histogram_quantile | <100ms | Prometheus |
| **Throughput** | QPS | rate(requests_total) | ±10% variation | Prometheus |
| **Error Rate** | 5xx Ratio | 5xx requests / total requests | <0.1% | Prometheus |
| **Resource** | CPU Usage | container_cpu_usage | <80% | cAdvisor |
| **Resource** | Memory Usage | container_memory_working_set | <85% | cAdvisor |
| **Queue** | Message Accumulation | queue depth | <1000 | Middleware monitoring |
| **Connection** | DB Connection Pool Usage | active connections / max connections | <80% | Application metrics |
| **Recovery** | MTTR | time from issue to recovery | <5min | Alerting system |

### Prometheus Alert Rules

```yaml
# chaos-alerting-rules.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: chaos-experiment-alerts
  namespace: monitoring
spec:
  groups:
  - name: chaos.steadystate
    interval: 30s
    rules:
    # Availability drop alert
    - alert: ChaosSteadyStateAvailabilityBreach
      expr: |
        sum(rate(http_requests_total{status=~"2.."}[1m])) / 
        sum(rate(http_requests_total[1m])) < 0.999
      for: 1m
      labels:
        severity: warning
        chaos_related: "true"
      annotations:
        summary: "Steady state assumption violated: availability below 99.9%"
        description: "Current availability: {{ $value | printf \"%.4f\" }}"
        
    # Latency increase alert
    - alert: ChaosSteadyStateLatencyBreach
      expr: |
        histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[1m])) by (le)) > 0.5
      for: 1m
      labels:
        severity: warning
        chaos_related: "true"
      annotations:
        summary: "Steady state assumption violated: P99 latency exceeds 500ms"
        description: "Current P99 latency: {{ $value | printf \"%.3f\" }}s"
        
    # Error rate increase alert
    - alert: ChaosSteadyStateErrorRateBreach
      expr: |
        sum(rate(http_requests_total{status=~"5.."}[1m])) / 
        sum(rate(http_requests_total[1m])) > 0.001
      for: 1m
      labels:
        severity: critical
        chaos_related: "true"
      annotations:
        summary: "Steady state assumption violated: 5xx error rate exceeds 0.1%"
        description: "Current error rate: {{ $value | printf \"%.4f\" }}"
        
    # Pod recovery time alert
    - alert: ChaosPodRecoveryTooSlow
      expr: |
        time() - kube_pod_start_time{namespace="production"} > 120
        and on(pod) kube_pod_status_phase{phase="Pending"} == 1
      for: 2m
      labels:
        severity: warning
        chaos_related: "true"
      annotations:
        summary: "Pod recovery time exceeds 2 minutes"
```

### Grafana Dashboard

```json
{
  "dashboard": {
    "title": "Chaos Engineering Dashboard",
    "panels": [
      {
        "title": "Service Availability",
        "type": "gauge",
        "targets": [
          {
            "expr": "sum(rate(http_requests_total{status=~\"2..\"}[5m])) / sum(rate(http_requests_total[5m])) * 100"
          }
        ],
        "thresholds": {
          "mode": "absolute",
          "steps": [
            {"color": "red", "value": null},
            {"color": "yellow", "value": 99},
            {"color": "green", "value": 99.9}
          ]
        }
      },
      {
        "title": "Request Latency Distribution",
        "type": "heatmap",
        "targets": [
          {
            "expr": "sum(rate(http_request_duration_seconds_bucket[5m])) by (le)"
          }
        ]
      },
      {
        "title": "Active Chaos Experiments",
        "type": "stat",
        "targets": [
          {
            "expr": "count(chaos_mesh_experiments{status=\"Running\"})"
          }
        ]
      },
      {
        "title": "Pod Restarts",
        "type": "graph",
        "targets": [
          {
            "expr": "sum(increase(kube_pod_container_status_restarts_total{namespace=\"production\"}[5m])) by (pod)"
          }
        ]
      }
    ]
  }
}
```

<!-- chunk: Experiment Scenario Design -->
## Experiment Scenario Design

### Scenario 1: Service Self-Healing Capability Validation

```yaml
# scenario-1-self-healing.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: Workflow
metadata:
  name: self-healing-test
  namespace: chaos-mesh
  annotations:
    scenario: "Validate service self-healing capability"
    hypothesis: "When 30% of Pods are killed, the system should recover to normal state within 60 seconds"
spec:
  entry: main
  templates:
  - name: main
    templateType: Serial
    children:
    - baseline-check
    - pod-kill-chaos
    - recovery-observation
    
  - name: baseline-check
    templateType: Suspend
    suspend:
      duration: "30s"
      
  - name: pod-kill-chaos
    templateType: PodChaos
    podChaos:
      action: pod-kill
      mode: fixed-percent
      value: "30"
      selector:
        namespaces: [production]
        labelSelectors:
          app: api-server
          
  - name: recovery-observation
    templateType: Suspend
    suspend:
      duration: "2m"
```

### Scenario 2: Service Degradation Validation

```yaml
# scenario-2-graceful-degradation.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: Workflow
metadata:
  name: graceful-degradation-test
  namespace: chaos-mesh
  annotations:
    scenario: "Validate service degradation mechanism"
    hypothesis: "When downstream service responds slowly, it should trigger timeouts and degradation without affecting core functionality"
spec:
  entry: main
  templates:
  - name: main
    templateType: Serial
    children:
    - inject-downstream-latency
    - observe-degradation
    
  - name: inject-downstream-latency
    templateType: NetworkChaos
    networkChaos:
      action: delay
      mode: all
      selector:
        namespaces: [production]
        labelSelectors:
          app: recommendation-service
      delay:
        latency: "5s"
      duration: "5m"
      
  - name: observe-degradation
    templateType: Suspend
    suspend:
      duration: "6m"
```

### Scenario 3: Database Failover

```yaml
# scenario-3-db-failover.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: Workflow
metadata:
  name: db-failover-test
  namespace: chaos-mesh
  annotations:
    scenario: "Validate database failover"
    hypothesis: "When primary database is unavailable, it should failover to replica within 30 seconds"
spec:
  entry: main
  templates:
  - name: main
    templateType: Serial
    children:
    - partition-primary-db
    - verify-failover
    - restore-network
    
  - name: partition-primary-db
    templateType: NetworkChaos
    networkChaos:
      action: partition
      mode: all
      selector:
        namespaces: [database]
        labelSelectors:
          app: mysql
          role: primary
      direction: both
      target:
        selector:
          namespaces: [production]
        mode: all
      duration: "3m"
      
  - name: verify-failover
    templateType: Suspend
    suspend:
      duration: "4m"
      
  - name: restore-network
    templateType: Suspend
    suspend:
      duration: "30s"
```

### Scenario 4: Resource Contention Testing

```yaml
# scenario-4-resource-contention.yaml
apiVersion: chaos-mesh.org/v1alpha1
kind: Workflow
metadata:
  name: resource-contention-test
  namespace: chaos-mesh
  annotations:
    scenario: "Validate resource contention handling"
    hypothesis: "When node resources are tight, the system should handle correctly and ensure critical service availability"
spec:
  entry: main
  templates:
  - name: main
    templateType: Parallel
    children:
    - cpu-stress
    - memory-stress
    
  - name: cpu-stress
    templateType: StressChaos
    stressChaos:
      mode: fixed
      value: "2"
      selector:
        namespaces: [production]
        labelSelectors:
          tier: worker
      stressors:
        cpu:
          workers: 4
          load: 85
      duration: "5m"
      
  - name: memory-stress
    templateType: StressChaos
    stressChaos:
      mode: fixed
      value: "2"
      selector:
        namespaces: [production]
        labelSelectors:
          tier: worker
      stressors:
        memory:
          workers: 2
          size: "70%"
      duration: "5m"
```

<!-- chunk: Experiment Report Template -->
## Experiment Report Template

```yaml
# experiment-report-template.yaml
experiment:
  name: "API Service Pod Failure Recovery Test"
  id: "chaos-exp-2026011701"
  date: "2026-01-17"
  owner: "SRE Team"
  reviewer: "Platform Team"
  
# Steady state hypothesis
hypothesis:
  description: "When 30% of API Pods are killed, the system should recover to normal state within 60 seconds"
  steady_state_metrics:
    - metric: "success_rate"
      operator: ">"
      expected: "99%"
      actual: "99.2%"
      pass: true
    - metric: "p99_latency"
      operator: "<"
      expected: "200ms"
      actual: "180ms"
      pass: true
    - metric: "error_rate"
      operator: "<"
      expected: "0.1%"
      actual: "0.05%"
      pass: true

# Experiment execution
execution:
  blast_radius: "production/api-server (3/10 pods)"
  duration: "60s"
  start_time: "2026-01-17T10:00:00Z"
  end_time: "2026-01-17T10:02:30Z"
  monitoring_dashboard: "https://grafana.example.com/d/chaos-123"
  chaos_resource: "podchaos/api-server-kill-test"
  
# Results
results:
  hypothesis_validated: true
  metrics:
    success_rate: "99.2%"
    p99_latency: "180ms"
    error_rate: "0.05%"
    recovery_time: "45s"
  observations:
    - "HPA responded promptly, new Pods started within 30 seconds"
    - "Load balancer correctly removed unhealthy Pods"
    - "No data loss, all requests correctly retried"
    - "Monitoring alerts triggered within 15 seconds"
    
# Findings discovered
findings:
  - severity: "medium"
    description: "Pod startup time is long (approximately 25 seconds), mainly due to image pull"
    recommendation: "Enable image prewarming or use smaller base images"
  - severity: "low"
    description: "Some Pods concentrated on same node"
    recommendation: "Increase Pod anti-affinity configuration"
    
# Improvement recommendations
recommendations:
  - priority: "P1"
    action: "Add Pod anti-affinity to avoid Pod concentration on same node"
    owner: "Platform Team"
    deadline: "2026-01-24"
  - priority: "P2"
    action: "Optimize startup probe configuration to reduce Pod ready time"
    owner: "Dev Team"
    deadline: "2026-01-31"
  - priority: "P2"
    action: "Configure image prewarming Job"
    owner: "Platform Team"
    deadline: "2026-02-07"
    
# Follow-up actions
follow_up:
  next_experiment: "Increase blast_radius to 50% for testing"
  scheduled_date: "2026-02-01"
```

<!-- chunk: ACK Chaos Engineering Integration -->
## ACK Chaos Engineering Integration

> ⚠️ **🟡 Medium Risk Change** — modifies cluster resource state, recommend --dry-run or diff before confirming
> - `helm upgrade/install`: deploy/upgrade release
> - `kubectl apply/create/replace`: create/modify cluster resources

``` bash
# 🟡 Medium risk: will modify cluster/resource state, confirm target, impact scope, and authorization before executing
# ACK install Chaos Mesh
helm repo add chaos-mesh https://charts.chaos-mesh.org
helm repo update

# Install to ACK cluster
helm install chaos-mesh chaos-mesh/chaos-mesh \
  -n chaos-mesh --create-namespace \
  --set chaosDaemon.runtime=containerd \
  --set chaosDaemon.socketPath=/run/containerd/containerd.sock \
  --set dashboard.securityMode=true \
  --set dashboard.service.type=LoadBalancer \
  --set controllerManager.replicaCount=3

# Configure ARMS integration (observability)
kubectl apply -f - <<EOF
apiVersion: v1
kind: ConfigMap
metadata:
  name: chaos-mesh-arms-config
  namespace: chaos-mesh
data:
  arms-endpoint: "https://arms.cn-hangzhou.aliyuncs.com"
  arms-license-key: "<your-license-key>"
EOF

# Configure SLS log collection
kubectl apply -f - <<EOF
apiVersion: log.alibabacloud.com/v1alpha1
kind: AliyunLogConfig
metadata:
  name: chaos-mesh-logs
  namespace: chaos-mesh
spec:
  logstore: chaos-mesh-logs
  shardCount: 2
  lifeCycle: 30
  logtailConfig:
    inputType: plugin
    configName: chaos-mesh-logs
    inputDetail:
      plugin:
        inputs:
        - type: service_docker_stdout
          detail:
            Stderr: true
            Stdout: true
            IncludeLabel:
              app: chaos-mesh
EOF
```
<!-- chunk: Best Practices -->
## Best Practices

### Chaos Engineering Implementation Checklist

| Phase | Activity | Description | Checklist |
|-----|------|------|-------|
| **Preparation** | Define Steady State Hypothesis | SLI/SLO baseline | □ Metrics defined |
| **Preparation** | Select Experiment Scope | Start small | □ Blast radius determined |
| **Preparation** | Configure Monitoring | Dashboard/alerts | □ Monitoring ready |
| **Preparation** | Prepare Rollback Plan | Emergency stop mechanism | □ Rollback process verified |
| **Execution** | Notify Related Teams | Experiment calendar | □ Teams notified |
| **Execution** | Run Experiment | Monitor steady state metrics | □ Experiment running |
| **Execution** | Real-time Observation | Watch for anomalies | □ Continuous monitoring |
| **Analysis** | Collect Data | Metrics/logs/events | □ Data collection complete |
| **Analysis** | Validate Hypothesis | Compare to steady state metrics | □ Hypothesis validation complete |
| **Analysis** | Document Findings | Issues and improvements | □ Report generated |
| **Improvement** | Create Improvement Plan | Priority sorting | □ Improvement plan created |
| **Improvement** | Implement Improvements | Track progress | □ Improvements implemented |
| **Improvement** | Re-test | Verify improvement effectiveness | □ Retest passed |

### Security Considerations

```yaml
# Production environment security configuration
# 1. Limit experiment scope
apiVersion: chaos-mesh.org/v1alpha1
kind: PodChaos
metadata:
  name: safe-pod-chaos
spec:
  # Limit to non-critical namespaces only
  selector:
    namespaces:
    - production-non-critical
    # Exclude critical services
    expressionSelectors:
    - key: critical
      operator: NotIn
      values:
      - "true"
  # Limit impact scope
  mode: fixed
  value: "1"              # At most affect 1 Pod
  duration: "30s"         # Limit duration

---
# 2. Configure admission control
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: chaos-mesh-validation
webhooks:
- name: validate.chaos-mesh.org
  rules:
  - apiGroups: ["chaos-mesh.org"]
    apiVersions: ["v1alpha1"]
    operations: ["CREATE", "UPDATE"]
    resources: ["*"]
  # Only allow specific users to create chaos experiments
  namespaceSelector:
    matchLabels:
      chaos-mesh-enabled: "true"
```

<!-- chunk: Version Changelog -->
## Version Changelog

| Tool | Version | Changes | Impact |
|-----|------|---------|------|
| Chaos Mesh | 2.5 | Multi-cluster support improvement | Cross-cluster experiments |
| Chaos Mesh | 2.6 | Physical machine fault injection | Extend to VM |
| Chaos Mesh | 2.7 | HTTPChaos enhancement | gRPC support |
| LitmusChaos | 3.0 | GitOps mode support | CI/CD integration |
| LitmusChaos | 3.1 | ChaosHub improvement | Experiment marketplace |

---

**Chaos Engineering Principles**: Start small → Define steady state hypothesis → Automated continuous execution → Timely rollback mechanism → Document and improve learning

---

**Table footer mark**: Kusheet Project, Author Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian Related Documentation -->
## Obsidian Related Documentation

- domain-06-observability MOC
- [[domain-06-observability/README.md|Observability Domain]]
- [[domain-06-observability/00-open-source-projects-index.md|Domain-8 Observability — Open Source Projects Index]]
- Kubernetes Observability Architecture System
- Metrics Monitoring System Details
- 03 - Logging Collection Architecture Details (Logging Architecture)
- Distributed Tracing System
- 05 - Alert Management Strategy (Alerting Management)
- 06 - Monitoring Alerting Practice and Best Practices (Monitoring Alerting Practice)
- 04 - Monitoring Dashboard Design and Best Practices (Monitoring Dashboards)
- 08 - Logging Audit and Compliance Management (Logging Auditing & Compliance)
- 05 - Events and Audit Log Management (Events & Audit Logs)

## Related

- [[domain-02-workloads-applications/07-java-observability-kubernetes.md|07-java-observability-kubernetes]]

- [[domain-06-observability/README.md|Back to index]]- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Graph Index]]

## See Also

- 12-logging-auditing
- 13-cluster-health-check
- 15-enterprise-scale-monitoring
- 16-multi-cluster-monitoring-governance

```

<!-- risk-assessed -->
