---
title: Performance Benchmarking & Tuning
description: '**Target Audience**: Performance Engineers, SRE Team, Platform Architects'
summary: '**Target Audience**: Performance Engineers, SRE Team, Platform Architects'
category: general
tags:
- k8s
- devops
- daily-ops
- performance
- etcd
- apiserver
- kubelet
- scheduler
- prometheus
- cilium
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 25min
intent_queries:
- How to optimize 04-performance-benchmarking-tuning performance?
- 04-performance-benchmarking-tuning performance tuning guide
- Where are the bottlenecks in 04-performance-benchmarking-tuning?
trigger_keywords:
- Performance Benchmarking & Tuning
- Performance
- Benchmarking
- Tuning
- platform
- engineering
prerequisites:
- kubectl-basics
- platform-engineering-basics
- prometheus-basics
- cilium-basics
- cni-basics
- etcd-basics
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./governance/04-performance-benchmarking-tuning.md
original_language: Chinese
---

> **Production Environment Security Reminder**
>
> This document contains directly executable operations commands. Before execution, please confirm: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether it has been verified in a non-production environment. Command risk levels: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state but usually can be rolled back), 🟢 Low Risk/Read-only (information gathering, no side effects).




title: Performance Benchmarking & Tuning
description: '**Target Audience**: Performance Engineers, SRE Team, Platform Architects'
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- [[etcd|etcd]]
- apiserver
- [[kubelet|kubelet]]
- scheduler
- [[Prometheus|prometheus]]
- [[Cilium|cilium]]
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Platform Engineers
- Operations Engineers
estimated_read_time: 5min
intent_queries:
- What is Performance Benchmarking & Tuning
- How to implement Performance Benchmarking & Tuning
- Kubernetes 9 platform ops best practices
trigger_keywords:
- Performance Benchmarking & Tuning
- Performance
- Benchmarking
- Tuning
- platform
- ops
cross_refs:
- type: domain
  path: ../domain-06-observability/
  label: 'Related Knowledge Domain: domain-06-observability'
- type: domain
  path: ../domain-15-specialized-tech/
  label: 'Related Knowledge Domain: domain-15-specialized-tech'
- type: domain
  path: ../domain-10-troubleshooting-diagnostics/
  label: 'Related Knowledge Domain: domain-10-troubleshooting-diagnostics'
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

# Performance Benchmarking & Tuning

> **Applicable Versions**: Kubernetes v1.25 - v1.32 | **Document Version**: v1.0 | **Last Updated**: 2026-02
> **Target Audience**: Performance Engineers, SRE Team, Platform Architects

<!-- chunk: Overview -->
## Overview

Performance tuning is a critical aspect of ensuring efficient and stable operation of Kubernetes clusters. This document provides comprehensive performance benchmarking methods, tuning strategies, and production environment best practices to help operations teams identify performance bottlenecks and implement effective optimizations.

<!-- chunk: Performance Tuning Landscape -->
## Performance Tuning Landscape

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    Kubernetes Performance Tuning System                      │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│  │  Benchmarking   │  │ Performance     │  │  Bottleneck     │            │
│  │                 │  │ Monitoring      │  │  Analysis       │            │
│  │ • Cluster perf  │  │                 │  │                 │            │
│  │ • Component     │  │ • Real-time     │  │ • Root Cause    │            │
│  │   benchmarks    │  │   Metrics       │  │   Location      │            │
│  │ • Workload      │  │ • Trend         │  │ • Impact        │            │
│  │                 │  │   Analysis      │  │   Assessment    │            │
│  │                 │  │ • Anomaly       │  │ • Optimization  │            │
│  │                 │  │   Detection     │  │   Recommendations
│  └─────────────────┘  └─────────────────┘  └─────────────────┘            │
│          │                     │                     │                     │
│          ▼                     ▼                     ▼                     │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐            │
│  │ Tuning          │  │ Performance     │  │ Continuous      │            │
│  │ Implementation  │  │ Verification    │  │ Optimization    │            │
│  │                 │  │                 │  │                 │            │
│  │ • Parameter     │  │ • Comparative   │  │ • Automation    │            │
│  │   Adjustment    │  │   Analysis      │  │ • Intelligent   │            │
│  │ • Architecture  │  │ • Regression    │  │   Tuning        │            │
│  │   Optimization  │  │   Testing       │  │ • Predictive    │            │
│  │ • Resource      │  │ • Performance   │  │   Analysis      │            │
│  │   Reallocation  │  │   Reports       │  │                 │            │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘            │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- chunk: Benchmarking Framework -->
## Benchmarking Framework

### Test Dimension Matrix
| Test Category | Key Metrics | Testing Tools | Frequency | Importance |
|---------|---------|---------|------|--------|
| **Cluster Level** | API response time, scheduling latency, etcd performance | kubemark, etcdctl | Quarterly | High |
| **Node Level** | CPU utilization, memory efficiency, network latency | sysbench, iperf3 | Monthly | High |
| **Network Level** | Pod-to-pod communication latency, bandwidth throughput, DNS resolution | iperf3, dnsperf | Monthly | Medium |
| **Storage Level** | IOPS, latency, throughput | fio, dd | Monthly | Medium |
| **Application Level** | QPS, response time, error rate | wrk, jmeter | Continuous | High |

### Benchmarking Environment Preparation
```yaml
benchmark_environment:
  isolation_requirements:
    dedicated_cluster: true        # Use dedicated test cluster
    separate_network: true         # Isolated network environment
    isolated_storage: true         # Isolated storage backend
    
  baseline_specifications:
    control_plane:
      - instances: 3
      - instance_type: "m5.xlarge"  # 4 cores, 16GB RAM
      - disk_type: "gp3"           # General Purpose SSD
      - disk_size: 100Gi
      
    worker_nodes:
      - instances: 5
      - instance_type: "m5.2xlarge" # 8 cores, 32GB RAM
      - disk_type: "gp3"
      - disk_size: 200Gi
      
  test_data_preparation:
    - clean_state_reset: "Reset cluster before each test"
    - consistent_workload: "Use standardized test workload"
    - baseline_recording: "Record initial performance baseline"
```

<!-- chunk: Core Component Performance Testing -->
## Core Component Performance Testing

### 1. API Server Performance Testing

#### Test Script
```bash
#!/bin/bash
# API Server Performance Benchmarking

test_api_server_performance() {
    local api_server_endpoint=$1
    local test_duration=${2:-300}  # Default 5 minute test
    local concurrent_users=${3:-100} # Default concurrent users
    
    echo "=== API Server Performance Test ==="
    echo "Test endpoint: $api_server_endpoint"
    echo "Test duration: ${test_duration} seconds"
    echo "Concurrent users: $concurrent_users"
    echo ""
    
    # Use hey tool for load testing
    hey -z "${test_duration}s" \
        -c $concurrent_users \
        -H "Authorization: Bearer $(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
        "$api_server_endpoint/api/v1/namespaces/default/pods" \
        > /tmp/api_benchmark_results.txt
    
    # Analyze results
    echo "=== Test Results Analysis ==="
    grep "Requests/sec" /tmp/api_benchmark_results.txt
    grep "Latencies" /tmp/api_benchmark_results.txt
    grep "Status code distribution" /tmp/api_benchmark_results.txt
}

# Usage example
test_api_server_performance "https://kubernetes.default.svc" 300 50
```

#### Performance Metrics Interpretation
```yaml
api_server_metrics:
  response_time_targets:
    p50: "< 50ms"      # 50th percentile response time
    p95: "< 200ms"     # 95th percentile response time
    p99: "< 500ms"     # 99th percentile response time
    
  throughput_targets:
    requests_per_second: "> 1000"  # Requests per second
    concurrent_connections: "> 500" # Concurrent connections
    
  resource_utilization:
    cpu_usage: "< 70%"   # CPU utilization
    memory_usage: "< 80%" # Memory utilization
```

### 2. etcd Performance Testing

#### etcd Benchmarking Tool
``` bash
# 🟢 Low Risk: Read-only/information gathering, typically no side effects
#!/bin/bash
# etcd Performance Test Script

test_etcd_performance() {
    local etcd_endpoints=$1
    local test_duration=${2:-60}
    
    echo "=== etcd Performance Test ==="
    
    # Write performance test
    echo "Executing write performance test..."
    etcdctl --endpoints=$etcd_endpoints bench put \
        --total 10000 \
        --key-size 256 \
        --val-size 1024 \
        --sequential-keys
    
    # Read performance test
    echo "Executing read performance test..."
    etcdctl --endpoints=$etcd_endpoints bench get \
        --total 10000 \
        --sequential-keys
    
    # Mixed read-write test
    echo "Executing mixed read-write test..."
    etcdctl --endpoints=$etcd_endpoints bench txn \
        --total 5000 \
        --ratio 0.7:0.3  # 70% read, 30% write
}

# Usage example
test_etcd_performance "https://etcd-0:2379,https://etcd-1:2379,https://etcd-2:2379"
```
#### etcd Performance Optimization Parameters
```yaml
etcd_optimization_params:
  resource_limits:
    cpu: "4"           # CPU cores
    memory: "8Gi"      # Memory size
    disk: "500Gi SSD"  # Disk type and size
    
  tuning_parameters:
    quota_backend_bytes: "8589934592"  # 8GB storage quota
    max_request_bytes: "1572864"       # 1.5MB max request size
    snapshot_count: "10000"            # Snapshot interval
    
  disk_optimization:
    iops_requirement: "> 3000"         # IOPS requirement
    latency_requirement: "< 10ms"      # Latency requirement
    disk_type: "SSD/NVMe"              # Recommended disk type
```

### 3. Scheduler Performance Testing

#### Scheduling Latency Test
```python
#!/usr/bin/env python3
"""
Pod Scheduling Performance Benchmark Tool
"""

import subprocess
import json
import time
from datetime import datetime

class SchedulerBenchmark:
    def __init__(self, kubeconfig=None):
        self.kubeconfig = kubeconfig or "~/.kube/config"
        
    def create_test_pods(self, count=100):
        """Create test Pods"""
        test_pod_template = {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "name": "benchmark-pod-{index}",
                "labels": {"app": "scheduler-benchmark"}
            },
            "spec": {
                "containers": [{
                    "name": "test-container",
                    "image": "nginx:alpine",
                    "resources": {
                        "requests": {"cpu": "100m", "memory": "128Mi"}
                    }
                }]
            }
        }
        
        created_pods = []
        for i in range(count):
            pod_manifest = test_pod_template.copy()
            pod_manifest["metadata"]["name"] = f"benchmark-pod-{i}"
            
            # Create Pod
            cmd = f"kubectl create -f - --kubeconfig {self.kubeconfig}"
            process = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, 
                                     stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            process.communicate(input=json.dumps(pod_manifest).encode())
            
            created_pods.append(f"benchmark-pod-{i}")
            
        return created_pods
    
    def measure_scheduling_latency(self, pod_names):
        """Measure scheduling latency"""
        latencies = []
        
        for pod_name in pod_names:
            # Get Pod creation time and scheduling time
            cmd = f"kubectl get pod {pod_name} -o jsonpath='{{.metadata.creationTimestamp}}' --kubeconfig {self.kubeconfig}"
            creation_time_str = subprocess.check_output(cmd, shell=True).decode().strip()
            creation_time = datetime.fromisoformat(creation_time_str.replace('Z', '+00:00'))
            
            # Wait for Pod to be scheduled
            while True:
                cmd = f"kubectl get pod {pod_name} -o jsonpath='{{.spec.nodeName}}' --kubeconfig {self.kubeconfig}"
                node_name = subprocess.check_output(cmd, shell=True).decode().strip()
                
                if node_name:
                    # Get node assignment time
                    cmd = f"kubectl get event --field-selector involvedObject.name={pod_name} --kubeconfig {self.kubeconfig}"
                    events_output = subprocess.check_output(cmd, shell=True).decode()
                    
                    # Parse scheduling event time
                    for line in events_output.split('\n'):
                        if 'Scheduled' in line:
                            # Extract event timestamp
                            # Simplified here, actual implementation requires parsing specific time
                            scheduled_time = datetime.now()
                            latency = (scheduled_time - creation_time).total_seconds()
                            latencies.append(latency)
                            break
                    break
                
                time.sleep(0.1)
        
        return latencies
    
    def run_benchmark(self, pod_count=100):
        """Run complete benchmark"""
        print("=== Scheduler Performance Benchmark ===")
        
        # Create test Pods
        print(f"Creating {pod_count} test Pods...")
        pod_names = self.create_test_pods(pod_count)
        
        # Measure scheduling latency
        print("Measuring scheduling latency...")
        latencies = self.measure_scheduling_latency(pod_names)
        
        # Output results
        if latencies:
            avg_latency = sum(latencies) / len(latencies)
            max_latency = max(latencies)
            min_latency = min(latencies)
            
            print(f"Average scheduling latency: {avg_latency:.3f} seconds")
            print(f"Maximum scheduling latency: {max_latency:.3f} seconds")
            print(f"Minimum scheduling latency: {min_latency:.3f} seconds")
            print(f"95th percentile latency: {sorted(latencies)[int(len(latencies)*0.95)]:.3f} seconds")
        else:
            print("No valid latency data collected")

# Usage example
if __name__ == "__main__":
    benchmark = SchedulerBenchmark()
    benchmark.run_benchmark(50)
```

<!-- chunk: Network Performance Tuning -->
## Network Performance Tuning

### Network Plugin Performance Comparison
```yaml
network_plugin_benchmark:
  performance_metrics:
    pod_to_pod_latency:
      calico: "150-300μs"
      cilium: "100-250μs" 
      flannel: "200-400μs"
      weave: "250-500μs"
      
    bandwidth_throughput:
      calico: "8-12Gbps"
      cilium: "10-15Gbps"
      flannel: "6-10Gbps"
      weave: "5-8Gbps"
      
    cpu_overhead:
      calico: "2-5% per node"
      cilium: "3-6% per node"
      flannel: "1-3% per node"
      weave: "4-8% per node"
```

### Network Performance Test Script

> ⚠️ **🔴 Catastrophic Operation** — Contains irreversible commands, must meet change window + dual review + pre-backup + rollback plan before execution
> - `kubectl delete namespace`: Permanently delete namespace and all resources, non-recoverable
> - `kubectl apply/create/replace`: Create/modify cluster resources

> **🔴 High Risk Operation Warning**
>
> The following commands are irreversible or high-impact operations. Before execution, please confirm:
> - Critical data and configurations have been backed up
> - Within approved change window
> - Authorized by relevant stakeholders
> - Rollback or recovery plan is prepared
> - Target cluster, Namespace, node/resource names are correct

``` bash
# 🔴 High Risk: May cause data loss or service interruption, requires backup, change approval, and rollback plan before execution
#!/bin/bash
# Network Performance Benchmark

test_network_performance() {
    local test_namespace=${1:-network-bench}
    
    echo "=== Network Performance Test ==="
    
    # Deploy iperf3 test environment
    kubectl create namespace $test_namespace
    
    # Deploy iperf3 server
    cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: iperf3-server
  namespace: $test_namespace
spec:
  replicas: 1
  selector:
    matchLabels:
      app: iperf3-server
  template:
    metadata:
      labels:
        app: iperf3-server
    spec:
      containers:
      - name: iperf3
        image: networkstatic/iperf3
        args: ["-s"]
        ports:
        - containerPort: 5201
---
apiVersion: v1
kind: Service
metadata:
  name: iperf3-server
  namespace: $test_namespace
spec:
  selector:
    app: iperf3-server
  ports:
  - port: 5201
    targetPort: 5201
EOF
    
    # Wait for service to start
    sleep 30
    
    # Execute network test
    echo "Executing Pod-to-Pod network performance test..."
    kubectl run iperf3-client \
        --image=networkstatic/iperf3 \
        --namespace=$test_namespace \
        --restart=Never \
        --attach \
        --rm \
        --overrides='{
            "spec": {
                "containers": [{
                    "name": "iperf3-client",
                    "image": "networkstatic/iperf3",
                    "args": ["-c", "iperf3-server.'$test_namespace'.svc.cluster.local", "-t", "30", "-P", "4"]
                }]
            }
        }'
    
    # Clean up test environment
    kubectl delete namespace $test_namespace  # ⚠️ Irreversible: Permanently delete namespace and all resources
}

test_network_performance
```
<!-- chunk: Storage Performance Tuning -->
## Storage Performance Tuning

### CSI Driver Performance Testing

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend --dry-run or diff first to confirm
> - `kubectl apply/create/replace`: Create/modify cluster resources
> - `kubectl delete`: Delete resources (can be reconstructed by declarative manifest)

> **🔴 High Risk Operation Warning**
>
> The following commands are irreversible or high-impact operations. Before execution, please confirm:
> - Critical data and configurations have been backed up
> - Within approved change window
> - Authorized by relevant stakeholders
> - Rollback or recovery plan is prepared
> - Target cluster, Namespace, node/resource names are correct

``` bash
# 🔴 High Risk: May cause data loss or service interruption, requires backup, change approval, and rollback plan before execution
#!/bin/bash
# Storage Performance Benchmark

test_storage_performance() {
    local storage_class=$1
    local test_size=${2:-1G}
    
    echo "=== Storage Performance Test ($storage_class) ==="
    
    # Create test PVC
    cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: storage-bench-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 10Gi
  storageClassName: $storage_class
EOF
    
    # Wait for PVC to bind
    kubectl wait --for=condition=bound pvc/storage-bench-pvc --timeout=300s
    
    # Deploy fio test Pod
    cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Pod
metadata:
  name: fio-benchmark
spec:
  containers:
  - name: fio
    image: ljishen/fio
    command: ["fio"]
    args:
    - "--name=k8s-test"
    - "--directory=/data"
    - "--rw=randrw"
    - "--bs=4k"
    - "--size=$test_size"
    - "--numjobs=4"
    - "--runtime=60"
    - "--time_based"
    - "--group_reporting"
    volumeMounts:
    - name: test-volume
      mountPath: /data
  volumes:
  - name: test-volume
    persistentVolumeClaim:
      claimName: storage-bench-pvc
  restartPolicy: Never
EOF
    
    # Wait for test to complete
    kubectl wait --for=condition=Ready pod/fio-benchmark --timeout=600s
    
    # Get test results
    kubectl logs fio-benchmark
    
    # Clean up resources
    kubectl delete pod fio-benchmark
    kubectl delete pvc storage-bench-pvc
}

# Test different storage classes
test_storage_performance "alicloud-disk-essd" "2G"
test_storage_performance "alicloud-disk-efficiency" "2G"
```
### Storage Performance Optimization Recommendations
```yaml
storage_optimization_guide:
  ssd_optimization:
    mount_options:
      - "noatime"        # Disable access time updates
      - "discard"        # Enable TRIM support
      - "barrier=0"      # Disable barrier writes
      
    scheduler_settings:
      elevator: "noop"   # Use NOOP scheduler
      nr_requests: "1024" # Increase request queue length
      
  filesystem_tuning:
    xfs_parameters:
      - "logbufs=8"      # Number of log buffers
      - "logbsize=256k"  # Log block size
      - "swidth=128"     # Stripe width
      
    ext4_parameters:
      - "data=ordered"   # Data write mode
      - "noauto_da_alloc" # Disable automatic delayed allocation
```

<!-- chunk: Performance Monitoring and Alerting -->
## Performance Monitoring and Alerting

### Key Performance Indicators (Metrics)
```yaml
performance_monitoring:
  cluster_level_metrics:
    - apiserver_request_duration_seconds
    - etcd_request_duration_seconds
    - scheduler_e2e_scheduling_duration_seconds
    - controller_manager_queue_depth
    
  node_level_metrics:
    - node_cpu_usage_seconds_total
    - node_memory_working_set_bytes
    - node_network_transmit_bytes_total
    - node_disk_io_time_seconds_total
    
  application_level_metrics:
    - container_cpu_usage_seconds_total
    - container_memory_working_set_bytes
    - container_network_receive_bytes_total
    - container_fs_writes_bytes_total
```

### Performance Alert Rules
```yaml
# Prometheus Alert Rules
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: performance-alerts
  namespace: monitoring
spec:
  groups:
  - name: performance.rules
    rules:
    # API Server performance alert
    - alert: APIServerHighLatency
      expr: histogram_quantile(0.95, rate(apiserver_request_duration_seconds_bucket[5m])) > 0.5
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "API Server response latency is too high"
        description: "95% of API requests have response time exceeding 500ms"
        
    # etcd performance alert
    - alert: EtcdHighDiskWalFsyncDuration
      expr: histogram_quantile(0.99, rate(etcd_disk_wal_fsync_duration_seconds_bucket[5m])) > 0.01
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "etcd disk write latency is too high"
        description: "etcd WAL fsync 99th percentile latency exceeds 10ms"
        
    # Scheduler performance alert
    - alert: SchedulerHighSchedulingLatency
      expr: histogram_quantile(0.95, rate(scheduler_e2e_scheduling_duration_seconds_bucket[5m])) > 5
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Pod scheduling latency is too high"
        description: "95% of Pod scheduling latency exceeds 5 seconds"
```

<!-- chunk: Tuning Best Practices -->
## Tuning Best Practices

### 1. System-level Tuning

> ⚠️ **🟠 High Risk Operation** — Affects business traffic or node state, requires change ticket + impact assessment + planned rollback
> - `systemctl stop/restart`: Stop/restart system services, affecting all containers on the node

> **🔴 High Risk Operation Warning**
>
> The following commands are irreversible or high-impact operations. Before execution, please confirm:
> - Critical data and configurations have been backed up
> - Within approved change window
> - Authorized by relevant stakeholders
> - Rollback or recovery plan is prepared
> - Target cluster, Namespace, node/resource names are correct

``` bash
# 🔴 High Risk: May cause data loss or service interruption, requires backup, change approval, and rollback plan before execution
#!/bin/bash
# Linux System Performance Tuning Script

optimize_system_performance() {
    echo "=== System Performance Tuning ==="
    
    # Kernel parameter tuning
    cat >> /etc/sysctl.conf <<EOF
# Network tuning
net.core.somaxconn = 65535
net.ipv4.tcp_max_syn_backlog = 65535
net.ipv4.ip_local_port_range = 1024 65535
net.ipv4.tcp_tw_reuse = 1

# Memory tuning
vm.swappiness = 1
vm.dirty_ratio = 15
vm.dirty_background_ratio = 5

# Filesystem tuning
fs.file-max = 2097152
fs.inotify.max_user_watches = 524288
EOF
    
    # Apply kernel parameters
    sysctl -p
    
    # systemd service tuning
    mkdir -p /etc/systemd/system/kubelet.service.d/
    cat > /etc/systemd/system/kubelet.service.d/10-kubeadm.conf <<EOF
[Service]
CPUAccounting=true
MemoryAccounting=true
ExecStart=
ExecStart=/usr/bin/kubelet \\
  --container-runtime=remote \\
  --container-runtime-endpoint=/run/containerd/containerd.sock \\
  --pod-infra-container-image=k8s.gcr.io/pause:3.6 \\
  --eviction-hard=memory.available<500Mi,nodefs.available<10% \\
  --eviction-minimum-reclaim=memory.available=0Mi,nodefs.available=5% \\
  --max-pods=110 \\
  --node-status-update-frequency=10s \\
  --image-gc-high-threshold=85 \\
  --image-gc-low-threshold=80
EOF
    
    systemctl daemon-reload
    systemctl restart kubelet
}

optimize_system_performance
```
### 2. Kubernetes Component Tuning
```yaml
# Component performance tuning configuration
component_tuning:
  api_server:
    runtime_config:
      - "api/all=true"
    feature_gates:
      - "AdvancedAuditing=true"
    audit_policy_file: "/etc/kubernetes/audit-policy.yaml"
    
  controller_manager:
    horizontal_pod_autoscaler_sync_period: "15s"
    node_monitor_grace_period: "40s"
    pod_eviction_timeout: "5m0s"
    
  scheduler:
    algorithm_provider: "DefaultProvider"
    percentage_of_nodes_to_score: 100
    bind_timeout_duration: "600s"
```

### 3. Container Runtime Tuning
```toml
# containerd configuration tuning
version = 2

[plugins."io.containerd.grpc.v1.cri"]
  stream_server_address = "127.0.0.1"
  stream_server_port = "0"
  enable_selinux = false
  
  [plugins."io.containerd.grpc.v1.cri".containerd]
    snapshotter = "overlayfs"
    default_runtime_name = "runc"
    
    [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
      runtime_type = "io.containerd.runc.v2"
      [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc.options]
        SystemdCgroup = true
        
  [plugins."io.containerd.grpc.v1.cri".cni]
    bin_dir = "/opt/cni/bin"
    conf_dir = "/etc/cni/net.d"
    
[plugins."io.containerd.internal.v1.opt"]
  path = "/opt/containerd"

[plugins."io.containerd.grpc.v1.containers"]
  no_pivot = false

[plugins."io.containerd.grpc.v1.diff"]
  default = "walking"
```

<!-- chunk: Performance Tuning Checklist -->
## Performance Tuning Checklist

```bash
#!/bin/bash
# Performance Tuning Checklist

performance_tuning_checklist() {
    echo "=== Performance Tuning Checklist ==="
    
    # Hardware resource checks
    echo "□ CPU cores >= 4 cores/node"
    echo "□ Memory >= 16Gi/node"
    echo "□ Disk uses SSD/NVMe"
    echo "□ Network bandwidth >= 10Gbps"
    
    # System configuration checks
    echo "□ Kernel parameters optimized"
    echo "□ File descriptor limit adjusted"
    echo "□ System services optimized"
    echo "□ Clock synchronization configured"
    
    # Kubernetes configuration checks
    echo "□ API Server parameters optimized"
    echo "□ etcd configuration tuned"
    echo "□ Scheduler parameters adjusted"
    echo "□ kubelet configuration optimized"
    
    # Monitoring and alerting checks
    echo "□ Performance monitoring deployed"
    echo "□ Key metrics configured"
    echo "□ Performance alerts set up"
    echo "□ Capacity planning completed"
    
    # Testing and validation checks
    echo "□ Baseline benchmarking completed"
    echo "□ Performance regression tests passed"
    echo "□ Stress testing executed"
    echo "□ Tuning effectiveness verified"
}

performance_tuning_checklist
```

Through systematic performance benchmarking and tuning practices, significant improvements can be achieved in the overall performance of Kubernetes clusters, providing applications with a more stable and efficient runtime environment.

---

<!-- chunk: Obsidian Related Documentation -->
## Obsidian Related Documentation

- domain-07-platform-engineering MOC
- [[domain-07-platform-engineering/README.md|Platform Ops Domain (Platform Operations Domain)]]
- Domain-9 Platform Operations - Open Source Project Index
- Platform Operations Overview
- Cluster Lifecycle Management
- Capacity Planning & Resource Assessment
- Operations Metrics System
- Monitoring and Alerting System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization & FinOps
- Security & Compliance Management

## Related

- [[domain-02-workloads-applications/03-jvm-gc-container-tuning.md|03-jvm-gc-container-tuning]]

## See Also

- 02-cluster-lifecycle-management
- 03-capacity-planning-resource-assessment
- 05-operations-metrics-system
- 06-monitoring-alerting-system


<!-- risk-assessed -->