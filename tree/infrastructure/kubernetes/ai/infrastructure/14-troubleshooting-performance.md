---
title: AI Platform Fault Diagnosis and Performance Optimization
description: '# AI Platform Fault Diagnosis and Performance Optimization'
summary: 'nvidia-smi --query-gpu=temperature.gpu,power.draw,enforced.power.limit --format=csv,noheader,nounits'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- kubelet
- prometheus
- jaeger
- docker
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- MLOps Engineers
- SRE
estimated_read_time: 5min
intent_queries:
- What is AI Platform Fault Diagnosis and Performance Optimization
- How to do AI Platform Fault Diagnosis and Performance Optimization
- Kubernetes 11 ai infra best practices
- Fault Diagnosis and Troubleshooting for AI Platform
- Steps for Troubleshooting AI Platform
trigger_keywords:
- AI Platform Fault Diagnosis and Performance Optimization
- ai
- infra
prerequisites:
- kubectl-basics
- prometheus-basics
- cni-basics
- gpu-scheduling-basics
- tracing-basics
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
  path: ../domain-02-workloads-applications/
  label: 'Related Knowledge Domain: domain-02-workloads-applications'
- type: domain
  path: ../domain-03-networking-traffic/
  label: 'Related Knowledge Domain: domain-03-networking-traffic'
- type: skill
  path: ../domain-10-troubleshooting-diagnostics/topic-skills/17-performance-bottleneck.md
  label: 'Operational Skills: 17-performance-bottleneck'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/14-troubleshooting-performance.md
---

> **Production Environment Security Tips**
>
> This document contains executable operational commands. Before executing, please confirm: whether the target cluster and Namespace are correct; whether sufficient RBAC permissions exist; and whether these commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# AI Platform Fault Diagnosis and Performance Optimization

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **Last Updated**: 2026-02 | **Reference**: [Kubernetes Troubleshooting](https://kubernetes.io/docs/tasks/debug/) | [NVIDIA DCGM](https://developer.nvidia.com/dcgm)


## 1. AI Platform Fault Diagnosis System

### 1.1 Problem Classification and Diagnosis Workflow

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                          AI Platform Troubleshooting Framework                      │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                            Problem Identification Stage                          │  │
│  │                                                                               │  │
│  │  Report User Issues ──▶ Symptoms Collection ──▶ Impact Scope Evaluation ──▶ Priority Determination                      │  │
│  │       │              │              │              │                            │  │
│  │       ▼              ▼              ▼              ▼                            │  │
│  │  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐                         │  │
│  │  │  SLA    │   │  Logs    │   │  Monitoring    │   │  Users    │                         │  │
│  │  │  Impact   │   │  Collection    │   │  Data    │   │  Feedback    │                         │  │
│  │  └─────────┘   └─────────┘   └─────────┘   └─────────┘                         │  │
│  │                                                                               │  │
│  └─────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                            Root Cause Analysis Stage                              │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │   Infrastructure   │  │    Model     │  │    Application     │  │    Network     │          │  │
│  │  │    Layer     │  │    Layer     │  │    Layer     │  │    Layer     │          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  │ • GPU issues   │  │ • Model Damage   │  │ • Code Defects   │  │ • Network Latency   │          │  │
│  │  │ • Storage Abnormalities   │  │ • Version Mismatch │  │ • Configuration Errors   │  │ • Bandwidth Insufficiency   │          │  │
│  │  │ • Node Issues   │  │ • Data Pollution   │  │ • Resource Competition   │  │ • DNS Resolution   │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └─────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                            Solution Implementation Stage                           │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │   Temporary   │  │   Permanent   │  │   Preventive   │  │   Validation   │          │  │
│  │  │   Repair   │  │   Repair   │  │   Measure   │  │   Test   │          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  │ • Quick Mitigation   │  │ • Root Cause Fix   │  │ • Improve Monitoring   │  │ • Regression Testing   │          │  │
│  │  │ • Service Degradation   │  │ • Code Fix   │  │ • Process Update   │  │ • Performance Validation   │          │  │
│  │  │ • Fault Tolerance Switch   │  │ • Architecture Optimization   │  │ • Training Documentation   │  │ • User Acceptance   │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └─────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                            Knowledge Management Stage                             │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │   Document   │  │   Training   │  │   Tool   │  │   Process   │          │  │
│  │  │   Update   │  │   Share   │  │   Improve   │  │   Optimize   │          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  │ • Issue Manual   │  │ • Experience Sharing   │  │ • Automation   │  │ • SOP Updates   │          │  │
│  │  │ • Best Practices   │  │ • Team Training   │  │ • Alert Mechanism   │  │ • Speed Up Response   │          │  │
│  │  │ • Case Library   │  │ • Knowledge Transfer   │  │ • Diagnostic Tools   │  │ • Collaboration Improvement   │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Common Fault Pattern Matrix

| Problem Type | Typical Symptoms | Impact Level | MTTR | Diagnostic Tools |
|----------|----------|----------|------|----------|
| **GPU Issues** | CUDA errors, driver crashes, high temperature | Infrastructure | 30min | nvidia-smi, dcgmi |
| **Model Loading Failure** | Unable to start, OOM, weight damage | Application Layer | 15min | model logs, kubectl describe |
| **High Latency Inference** | P99>500ms, throughput decline | Service Layer | 45min | [[Prometheus|Prometheus]], [[Jaeger|Jaeger]] |
| **Training Stuck** | Loss not converging, gradient vanishing | Compute Layer | 60min | TensorBoard, profiling |
| **Data Access Abnormalities** | Slow data read, file damage | Storage Layer | 20min | iostat, storage logs |
| **Network Communication Issues** | Connection timeouts, severe packet loss | Network Layer | 25min | ping, tcpdump, traceroute |

---


## 2. Infrastructure Layer Fault Diagnosis

### 2.1 GPU-related Issue Diagnosis

```bash
#!/bin/bash
# gpu_diagnostics.sh - GPU diagnostic script

echo "=== GPU diagnosis report ==="
echo "Generated time: $(date)"
echo "Node name: $(hostname)"
echo

# 1. Collect basic information
echo "1. GPU basic information:"
nvidia-smi --query-gpu=name,driver_version,memory.total,memory.used --format=csv,noheader,nounits
echo

# 2. Check temperature and power consumption
echo "2. Temperature and power state:"
nvidia-smi --query-gpu=temperature.gpu,power.draw,enforced.power.limit --format=csv,noheader,nounits
echo

# 3. Check process and memory usage
echo "3. GPU process occupancy:"
nvidia-smi pmon -i 0 -s um
echo

# 4. ECC error check
echo "4. ECC error statistics:"
nvidia-smi --query-gpu=ecc.errors.corrected.volatile.total,ecc.errors.uncorrected.volatile.total --format=csv,noheader,nounits
echo

# 5. PCIe connection status
echo "5. PCIe connection status:"
nvidia-smi --query-gpu=pcie.link.gen.current,pcie.link.width.current --format=csv,noheader,nounits
echo

# 6. DCGM health check
echo "6. DCGM health status:"
if command -v dcgmi &> /dev/null; then
    dcgmi health -g 0 -v
else
    echo "DCGM not installed, skipping health check"
fi
echo

# 7. GPU topology check
echo "7. GPU topology:"
nvidia-smi topo -m
echo

# 8. Performance test
echo "8. GPU performance benchmark:"
python3 -c "
import torch
if torch.cuda.is_available():
    device = torch.device('cuda')
    # Simple matrix multiplication test
    a = torch.randn(1000, 1000).to(device)
    b = torch.randn(1000, 1000).to(device)
    torch.cuda.synchronize()
    import time
    start = time.time()
    c = torch.mm(a, b)
    torch.cuda.synchronize()
    end = time.time()
    print(f'Matrix multiplication time: {(end-start)*1000:.2f} ms')
    print(f'GPU utilization: {torch.cuda.utilization()}%')
else:
    print('CUDA unavailable')
"
```

**Common GPU Fault Handling**:

> ⚠️ **🟠 High-Risk Operations** — Affect business traffic or node status, require change ticket + impact assessment + planned rollback
> - `systemctl stop/restart`: Stop/restart system services, affecting all containers on the node

``` bash
# 🟢 Low risk: read-only/information gathering, usually no side effects
# GPU driver issues
# Restart NVIDIA driver
sudo systemctl restart nvidia-persistenced
sudo modprobe -r nvidia_uvm && sudo modprobe nvidia_uvm

# Clean GPU memory
sudo nvidia-smi --gpu-reset

# Check if GPU is exclusive
lsof /dev/nvidia*

# Handle high temperatures
# Check fan speed
nvidia-settings -q [gpu:0]/GPUFanControlState
# Set fan policy
nvidia-settings -a [gpu:0]/GPUFanControlState=1 -a [fan:0]/GPUTargetFanSpeed=80
```
### 2.2 Storage Performance Issue Diagnosis

```bash
#!/bin/bash
# storage_diagnostics.sh - Storage performance diagnostic

echo "=== Storage diagnosis report ==="
echo "Node: $(hostname)"
echo "Time: $(date)"
echo

# 1. Check storage mountings
echo "1. Storage mount status:"
df -h | grep -E "(models|data|storage)"
mount | grep -E "(nfs|ceph|gluster)"
echo

# 2. I/O performance testing
echo "2. I/O performance benchmark:"
echo "Sequential read test:"
dd if=/dev/zero of=/tmp/testfile bs=1G count=1 oflag=direct 2>&1 | tail -1
echo "Sequential write test:"
dd if=/tmp/testfile of=/dev/null bs=1G count=1 iflag=direct 2>&1 | tail -1
rm -f /tmp/testfile
echo

# 3. Storage latency check
echo "3. Storage delay statistics:"
iostat -x 1 5 | grep -A 1 "^Device"
echo

# 4. File system check
echo "4. File system health status:"
for fs in $(df -T | awk '/ext4|xfs|zfs/{print $1}'); do
    echo "Checking $fs:"
    tune2fs -l $fs 2>/dev/null | grep -E "(State|Last checked)"
done
echo

# 5. NFS mount issue troubleshooting
echo "5. NFS connection status:"
showmount -e localhost 2>/dev/null || echo "NFS service is not running"
rpcinfo -p localhost 2>/dev/null | grep nfs
echo

# 6. Ceph storage check (if used)
if command -v ceph &> /dev/null; then
    echo "6. Ceph cluster status:"
    ceph health detail
    ceph df
    ceph osd pool stats
fi
```

---


## 3. Application-Level Fault Diagnosis

### 3.1 Model Service Fault Diagnosis

``` bash
# 🟢 Low risk: read-only/information gathering, typically no side effects
#!/bin/bash
# model_service_diagnostics.sh - model service diagnostic script

NAMESPACE=${1:-ai-models}
SERVICE_NAME=${2:-llama3-inference}

echo "=== Model service diagnostic report ==="
echo "Namespace: $NAMESPACE"
echo "Service name: $SERVICE_NAME"
echo "Time: $(date)"
echo

# 1. Check pod status
echo "1. Pod running status:"
kubectl get pods -n $NAMESPACE -l app=$SERVICE_NAME -o wide
echo

# 2. Endpoint check
echo "2. Service endpoint status:"
kubectl get endpoints -n $NAMESPACE $SERVICE_NAME
echo

# 3. Service log analysis
echo "3. Recent error logs:"
kubectl logs -n $NAMESPACE -l app=$SERVICE_NAME --tail=100 | grep -i "error|exception|failed" | tail -20
echo

# 4. Resource usage
echo "4. Resource usage statistics:"
kubectl top pods -n $NAMESPACE -l app=$SERVICE_NAME
echo

# 5. Service description information
echo "5. Service detailed information:"
kubectl describe service $SERVICE_NAME -n $NAMESPACE
echo

# 6. Deployment configuration check
echo "6. Deployment configuration status:"
kubectl describe deployment $SERVICE_NAME -n $NAMESPACE
echo

# 7. Network policy check
echo "7. Network policy impact:"
kubectl get networkpolicies -n $NAMESPACE
echo

# 8. Health check probes
echo "8. Health check status:"
kubectl get events -n $NAMESPACE --field-selector involvedObject.name=$SERVICE_NAME --sort-by='.lastTimestamp' | tail -10
```
**Common Causes of Model Loading Failure**:

```python
# model_loading_debugger.py
import traceback
import sys
import psutil
import GPUtil

class ModelLoadingDebugger:
    def __init__(self):
        self.checks = []
        
    def diagnose_loading_failure(self, model_path, error_message):
        """Diagnose the root cause of model loading failure"""
        
        diagnosis = {
            'error_analysis': self._analyze_error_message(error_message),
            'resource_check': self._check_system_resources(),
            'file_integrity': self._verify_file_integrity(model_path),
            'dependency_check': self._check_dependencies(),
            'recommendations': []
        }
        
        # Generate recommendations based on diagnosis results
        diagnosis['recommendations'] = self._generate_recommendations(diagnosis)
        
        return diagnosis
        
    def _analyze_error_message(self, error_msg):
        """Analyze error message types"""
        
        error_patterns = {
            'memory_error': ['out of memory', 'oom', 'cuda out of memory'],
            'file_error': ['file not found', 'corrupted', 'checksum'],
            'compatibility_error': ['version mismatch', 'incompatible'],
            'permission_error': ['permission denied', 'access denied'],
            'network_error': ['connection refused', 'timeout', 'unreachable']
        }
        
        error_type = 'unknown'
        for category, patterns in error_patterns.items():
            if any(pattern in error_msg.lower() for pattern in patterns):
                error_type = category
                break
                
        return {
            'type': error_type,
            'message': error_msg,
            'stack_trace': traceback.format_exc()
        }
        
    def _check_system_resources(self):
        """Check system resources"""
        
        # GPU resource check
        gpus = GPUtil.getGPUs()
        gpu_info = []
        for gpu in gpus:
            gpu_info.append({
                'id': gpu.id,
                'name': gpu.name,
                'memory_free': gpu.memoryFree,
                'memory_used': gpu.memoryUsed,
                'memory_total': gpu.memoryTotal,
                'utilization': gpu.load
            })
            
        # CPU and memory check
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        
        return {
            'cpu_usage': cpu_percent,
            'memory_available_gb': memory.available / (1024**3),
            'memory_total_gb': memory.total / (1024**3),
            'gpus': gpu_info
        }
        
    def _verify_file_integrity(self, model_path):
        """validate model file integrity"""
        
        import os
        import hashlib
        
        if not os.path.exists(model_path):
            return {'status': 'missing', 'details': 'file not found'}
            
        # Check file size
        file_size = os.path.getsize(model_path)
        
        # Calculate checksum (if known model)
        expected_checksums = {
            'llama3-70b.bin': 'expected_md5_hash_here'
        }
        
        filename = os.path.basename(model_path)
        if filename in expected_checksums:
            actual_hash = self._calculate_md5(model_path)
            expected_hash = expected_checksums[filename]
            
            return {
                'status': 'valid' if actual_hash == expected_hash else 'corrupted',
                'file_size_mb': file_size / (1024*1024),
                'checksum_match': actual_hash == expected_hash
            }
            
        return {
            'status': 'unknown',
            'file_size_mb': file_size / (1024*1024),
            'note': 'no checksum information'
        }
        
    def _calculate_md5(self, filepath):
        """calculate file MD5 checksum"""
        import hashlib
        hash_md5 = hashlib.md5()
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
        
    def _check_dependencies(self):
        """check compatibility of dependencies"""
        
        import torch
        import transformers
        
        return {
            'torch_version': torch.__version__,
            'transformers_version': transformers.__version__,
            'cuda_available': torch.cuda.is_available(),
            'cuda_version': torch.version.cuda if torch.cuda.is_available() else 'N/A',
            'cudnn_version': torch.backends.cudnn.version() if torch.backends.cudnn.is_available() else 'N/A'
        }
        
    def _generate_recommendations(self, diagnosis):
        """Generate solution suggestions"""
        
        recommendations = []
        error_type = diagnosis['error_analysis']['type']
        
        if error_type == 'memory_error':
            recommendations.extend([
                "increase GPU memory allocation",
                "enable model quantization to reduce memory demand",
                "use model parallelism or pipeline parallelism",
                "check if other processes are occupying GPU memory"
            ])
            
        elif error_type == 'file_error':
            recommendations.extend([
                "re-download the model file",
                "validate the integrity of the storage system",
                "check file permission settings",
                "confirm correct model path configuration"
            ])
            
        elif error_type == 'compatibility_error':
            recommendations.extend([
                "update PyTorch and Transformers versions",
                "check compatibility of CUDA and cuDNN versions",
                "confirm model format matches framework version",
                "review the version requirements in the official documentation"
            ])
            
        # Add general suggestions
        recommendations.extend([
            "view complete error stack trace information",
            "check system logs for more information",
            "try to reproduce the issue in different environments",
            "contact the model provider for support"
        ])
        
        return recommendations

# Usage Example
debugger = ModelLoadingDebugger()

try:
    # Try loading the model
    model = load_model("path/to/model")
except Exception as e:
    # Diagnose failure reasons
    diagnosis = debugger.diagnose_loading_failure("path/to/model", str(e))
    
    print("=== model loading fault diagnosis report ===")
    print(f"error type: {diagnosis['error_analysis']['type']}")
    print(f"Error details: {diagnosis['error_analysis']['message']}")
    print("\nSystem resources:\n")
    print(f"Available memory: {diagnosis['resource_check']['memory_available_gb']:.2f} GB")
    print(f"GPU status: {[gpu['name'] for gpu in diagnosis['resource_check']['gpus']]}")
    print("\nSuggestion:\n")
    for i, rec in enumerate(diagnosis['recommendations'], 1):
        print(f"{i}. {rec}")
```

### 3.2 Inference Performance Analysis

```python
# inference_performance_analyzer.py
import time
import threading
import statistics
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt
import numpy as np

class InferencePerformanceAnalyzer:
    def __init__(self, endpoint_url, model_name):
        self.endpoint_url = endpoint_url
        self.model_name = model_name
        self.metrics = {
            'latencies': [],
            'throughputs': [],
            'errors': [],
            'resource_usage': []
        }
        
    def stress_test(self, duration_seconds=300, concurrent_requests=10, payload=None):
        """Perform stress testing"""
        
        print(f"Starting pressure test: {duration_seconds} seconds, {concurrent_requests} concurrent")
        
        start_time = time.time()
        end_time = start_time + duration_seconds
        
        # Test load
        default_payload = {
            "prompt": "Hello, how are you?",
            "max_tokens": 100,
            "temperature": 0.7
        }
        test_payload = payload or default_payload
        
        # Concurrent execution test
        with ThreadPoolExecutor(max_workers=concurrent_requests) as executor:
            futures = []
            
            while time.time() < end_time:
                future = executor.submit(self._single_request, test_payload)
                futures.append(future)
                
                # Control request frequency
                time.sleep(0.1)
                
        # Collect results
        for future in futures:
            try:
                result = future.result(timeout=30)
                if result:
                    self.metrics['latencies'].append(result['latency'])
                    self.metrics['throughputs'].append(result['throughput'])
                    if result['error']:
                        self.metrics['errors'].append(result['error'])
            except Exception as e:
                self.metrics['errors'].append(str(e))
                
        self._analyze_results()
        
    def _single_request(self, payload):
        """Perform a single inference request"""
        
        import requests
        import json
        
        start_time = time.time()
        
        try:
            response = requests.post(
                self.endpoint_url,
                json=payload,
                timeout=30
            )
            
            end_time = time.time()
            latency = (end_time - start_time) * 1000  # 转换为毫秒
            
            if response.status_code == 200:
                # Calculate throughput (tokens/second)
                response_data = response.json()
                output_tokens = len(response_data.get('generated_text', '').split())
                throughput = output_tokens / (latency / 1000) if latency > 0 else 0
                
                return {
                    'latency': latency,
                    'throughput': throughput,
                    'error': None,
                    'response_size': len(json.dumps(response_data))
                }
            else:
                return {
                    'latency': latency,
                    'throughput': 0,
                    'error': f"HTTP {response.status_code}",
                    'response_size': 0
                }
                
        except Exception as e:
            end_time = time.time()
            latency = (end_time - start_time) * 1000
            return {
                'latency': latency,
                'throughput': 0,
                'error': str(e),
                'response_size': 0
            }
            
    def _analyze_results(self):
        """Analyze test results"""
        
        latencies = self.metrics['latencies']
        errors = self.metrics['errors']
        
        if not latencies:
            print("No successful requests found:\n")
            return
            
        # Basic statistics
        stats = {
            'total_requests': len(latencies) + len(errors),
            'successful_requests': len(latencies),
            'error_rate': len(errors) / (len(latencies) + len(errors)) * 100,
            'avg_latency': statistics.mean(latencies),
            'median_latency': statistics.median(latencies),
            'p95_latency': np.percentile(latencies, 95),
            'p99_latency': np.percentile(latencies, 99),
            'min_latency': min(latencies),
            'max_latency': max(latencies),
            'std_deviation': statistics.stdev(latencies)
        }
        
        # Throughput statistics
        throughputs = self.metrics['throughputs']
        if throughputs:
            stats.update({
                'avg_throughput': statistics.mean(throughputs),
                'max_throughput': max(throughputs),
                'min_throughput': min(throughputs)
            })
            
        self._print_analysis(stats)
        self._generate_charts(stats)
        
    def _print_analysis(self, stats):
        """Print analysis results"""
        
        print("\n=== Inference Performance Analysis Report ===\n")
        print(f"Model: {self.model_name}\n")
        print(f"Test time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        print("\n--- Performance metrics ---\n")
        print(f"Total requests: {stats['total_requests']}\n")
        print(f"Successful requests: {stats['successful_requests']}\n")
        print(f"Error rate: {stats['error_rate']:.2f}%\n")
        print(f"\nLatency statistics (ms):\n")
        print(f"  Average latency: {stats['avg_latency']:.2f}\n")
        print(f"  Median latency: {stats['median_latency']:.2f}\n")
        print(f"  P95 latency: {stats['p95_latency']:.2f}\n")
        print(f"  P99 latency: {stats['p99_latency']:.2f}\n")
        print(f"  Minimum latency: {stats['min_latency']:.2f}\n")
        print(f"  Maximum delay: {stats['max_latency']:.2f}")
        print(f"  Standard deviation: {stats['std_deviation']:.2f}")
        
        if 'avg_throughput' in stats:
            print(f"  Maximum throughput: {stats['max_throughput']:.2f}")
            print(f"  Minimum throughput: {stats['min_throughput']:.2f}")
            print(f"  maximum throughput: {stats['max_throughput']:.2f}")
            print(f"  minimum throughput: {stats['min_throughput']:.2f}")
            
        # Performance rating
        self._performance_rating(stats)
        
    def _performance_rating(self, stats):
        """Performance rating"""
        
        ratings = []
        
        # Latency rating
        avg_latency = stats['avg_latency']
        if avg_latency < 100:
            ratings.append(("delay", "excellent ⭐⭐⭐⭐⭐"))
        elif avg_latency < 300:
            ratings.append(("delay", "good ⭐⭐⭐⭐"))
        elif avg_latency < 500:
            ratings.append(("delay", "average ⭐⭐⭐"))
        else:
            ratings.append(("delay", "poor ⭐⭐"))
            
        # Error rate rating
        error_rate = stats['error_rate']
        if error_rate == 0:
            ratings.append(("Stability", "Excellent ⭐⭐⭐⭐⭐"))
        elif error_rate < 1:
            ratings.append(("Stability", "good ⭐⭐⭐⭐"))
        elif error_rate < 5:
            ratings.append(("Stability", "average ⭐⭐⭐"))
        else:
            ratings.append(("Stability", "poor ⭐⭐"))
            
        print("\n--- Performance Rating ---")
        for metric, rating in ratings:
            print(f"  {metric}: {rating}")
            
    def _generate_charts(self, stats):
        """Generate performance charts"""
        
        latencies = sorted(self.metrics['latencies'])
        percentiles = [i/len(latencies)*100 for i in range(len(latencies))]
        
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))
        
        # Delay histogram
        ax1.hist(latencies, bins=50, alpha=0.7, color='blue')
        ax1.set_xlabel('delay (ms)')
        ax1.set_ylabel('frequency')
        ax1.set_title('delay distribution')
        ax1.axvline(stats['avg_latency'], color='red', linestyle='--', 
                   ax1.set_ylabel('Frequency')
        ax1.axvline(stats['p95_latency'], color='orange', linestyle='--',
                   label=f'P95: {stats["p95_latency"]:.1f}ms')
        ax1.legend()
        
        # Cumulative distribution function
        ax2.plot(percentiles, latencies)
        ax2.set_xlabel('percentile (%)')
        ax2.set_ylabel('delay (ms)')
        ax2.set_title('cumulative distribution of delay')
        ax2.grid(True)
        
        # Throughput trend (if time series data available)
        if len(self.metrics['throughputs']) > 1:
            throughputs = self.metrics['throughputs']
            time_points = range(len(throughputs))
            ax3.plot(time_points, throughputs, marker='o', markersize=2)
            ax3.set_xlabel('request number')
            ax3.set_ylabel('throughput (tokens/sec)')
            ax3.set_title('Throughput trend')
            ax3.grid(True)
            
        # Delay distribution histogram
        error_categories = {}
        for error in self.metrics['errors']:
            category = error.split(':')[0] if ':' in error else 'Other'
            error_categories[category] = error_categories.get(category, 0) + 1
            
        if error_categories:
            ax4.pie(error_categories.values(), labels=error_categories.keys(), autopct='%1.1f%%')
            ax4.set_title('Error type distribution')
        else:
            ax4.text(0.5, 0.5, 'No error', ha='center', va='center', transform=ax4.transAxes)
            ax4.set_title('Error analysis')
            
        plt.tight_layout()
        plt.savefig(f'inference_performance_{int(time.time())}.png', dpi=300, bbox_inches='tight')
        plt.show()
        
        print(f"\nPerformance charts have been saved as: inference_performance_{int(time.time())}.png")

# Usage example
analyzer = InferencePerformanceAnalyzer(
    endpoint_url="http://model-service.ai-models.svc.cluster.local:8000/v1/completions",
    model_name="llama3-70b"
)

# Execute pressure testing
analyzer.stress_test(
    duration_seconds=300,  # 5分钟测试
    concurrent_requests=20,  # 20并发
    payload={
        "prompt": "Explain quantum computing in simple terms:",
        "max_tokens": 200,
        "temperature": 0.7
    }
)
```

---


## 4. Monitoring and Alerting System Construction

### 4.1 Key Metric Alert Configuration

```yaml
# ai_monitoring_alerts.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: ai-platform-alerts
  namespace: monitoring
spec:
  groups:
  # GPU-related alerts
  - name: ai.gpu.alerts
    rules:
    - alert: HighGPUUtilization
      expr: avg by(instance, gpu)(DCGM_FI_DEV_GPU_UTIL) > 95
      for: 5m
      labels:
        severity: warning
        team: ai-platform
      annotations:
        summary: "GPU utilization is too high ({{ $labels.instance }} GPU {{ $labels.gpu }})"
        description: "GPU utilization has been consistently over 95%, which may cause performance bottlenecks"
        
    - alert: HighGPUTemperature
      expr: DCGM_FI_DEV_GPU_TEMP > 80
      for: 2m
      labels:
        severity: critical
        team: ai-platform
      annotations:
        summary: "GPU temperature is too high ({{ $labels.instance }})"
        description: "GPU temperature reaches {{ $value }}°C, which may affect stability and lifespan"
        
    - alert: GPUMemoryPressure
      expr: (DCGM_FI_DEV_FB_USED / DCGM_FI_DEV_FB_TOTAL) * 100 > 90
      for: 3m
      labels:
        severity: warning
        team: ai-platform
      annotations:
        summary: "GPU memory pressure is too high"
        description: "GPU memory usage rate is {{ $value | printf \"%.2f\" }}%, approaching the upper limit"
        
  # Model service alerts
  - name: ai.model.alerts
    rules:
    - alert: HighInferenceLatency
      expr: histogram_quantile(0.99, sum(rate(http_request_duration_seconds_bucket[5m])) by (le, service)) > 0.5
      for: 3m
      labels:
        severity: warning
        service: inference
      annotations:
        summary: "Inference delay is too high ({{ $labels.service }})"
        description: "P99 delay exceeds 500ms, current value: {{ $value | printf \"%.3f\" }}s"
        
    - alert: ModelServiceDown
      expr: up{job=~"model-.*"} == 0
      for: 1m
      labels:
        severity: critical
        team: ai-platform
      annotations:
        summary: "Model service is unavailable"
        description: "Service {{ $labels.job }} cannot be accessed"
        
    - alert: HighModelErrorRate
      expr: sum(rate(model_errors_total[5m])) / sum(rate(model_requests_total[5m])) > 0.05
      for: 2m
      labels:
        severity: critical
        service: model-serving
      annotations:
        summary: "Model error rate is abnormal"
        description: "Error rate exceeds 5%, current value: {{ $value | printf \"%.2f\" }}%"
        
  # Training task alerts
  - name: ai.training.alerts
    rules:
    - alert: TrainingJobStuck
      expr: kube_job_status_active{job_name=~"training-.*"} > 0
      for: 30m
      labels:
        severity: warning
        team: ml-engineering
      annotations:
        summary: "Training task stuck"
        description: "Training task {{ $labels.job_name }} has run for more than 30 minutes without progress"
        
    - alert: TrainingLossNaN
      expr: training_loss{status="invalid"} > 0
      for: 1m
      labels:
        severity: critical
        team: ml-engineering
      annotations:
        summary: "Training loss shows NaN value"
        description: "Invalid loss value occurred during training, please check the data and model configuration"
        
  # Storage alerts
  - name: ai.storage.alerts
    rules:
    - alert: LowDiskSpace
      expr: (node_filesystem_avail_bytes / node_filesystem_size_bytes) * 100 < 10
      for: 5m
      labels:
        severity: critical
        team: ai-platform
      annotations:
        summary: "Insufficient disk space"
        description: "Node {{ $labels.instance }} available space below 10%"
        
    - alert: HighStorageLatency
      expr: rate(node_disk_read_time_seconds_total[1m]) / rate(node_disk_reads_completed_total[1m]) > 0.1
      for: 3m
      labels:
        severity: warning
        team: ai-platform
      annotations:
        summary: "Storage delay is too high"
        description: "Storage I/O delay exceeds 100ms"
```

### 4.2 Automated Diagnostic Tools

```python
# automated_diagnostic_tool.py
import subprocess
import json
import yaml
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class AutomatedDiagnosticTool:
    def __init__(self, config_file="diagnostic_config.yaml"):
        self.config = self._load_config(config_file)
        self.results = {}
        
    def _load_config(self, config_file):
        """Load diagnostic configuration"""
        with open(config_file, 'r') as f:
            return yaml.safe_load(f)
            
    def run_full_diagnosis(self):
        """Run full diagnosis"""
        
        print("Starting comprehensive diagnosis of AI platform...")
        start_time = datetime.now()
        
        # 1. Infrastructure check
        self.results['infrastructure'] = self._check_infrastructure()
        
        # 2. Kubernetes cluster status
        self.results['kubernetes'] = self._check_kubernetes()
        
        # 3. AI service status
        self.results['ai_services'] = self._check_ai_services()
        
        # 4. Performance metric analysis
        self.results['performance'] = self._analyze_performance()
        
        # 5. Security check
        self.results['security'] = self._check_security()
        
        # 6. Generate report
        self._generate_report()
        
        # 7. Send alert (if there's an issue)
        if self._has_critical_issues():
            self._send_alerts()
            
        end_time = datetime.now()
        print(f"Diagnosis completed, duration: {end_time - start_time}")
        
        return self.results
        
    def _check_infrastructure(self):
        """Check infrastructure status"""
        
        checks = {}
        
        # GPU status check
        try:
            gpu_output = subprocess.check_output(['nvidia-smi', '--query-gpu=name,temperature.gpu,utilization.gpu,memory.used,memory.total', '--format=csv,noheader,nounits'], text=True)
            checks['gpus'] = []
            for line in gpu_output.strip().split('\n'):
                parts = line.split(', ')
                checks['gpus'].append({
                    'name': parts[0],
                    'temperature': int(parts[1]),
                    'utilization': int(parts[2]),
                    'memory_used': int(parts[3]),
                    'memory_total': int(parts[4])
                })
        except subprocess.CalledProcessError:
            checks['gpus'] = 'Unable to obtain GPU information'
            
        # Storage status check
        try:
            df_output = subprocess.check_output(['df', '-h'], text=True)
            checks['storage'] = df_output
        except subprocess.CalledProcessError:
            checks['storage'] = 'Unable to obtain storage information'
            
        # Network connectivity check
        checks['network'] = self._check_network_connectivity()
        
        return checks
        
    def _check_kubernetes(self):
        """Check Kubernetes cluster status"""
        
        checks = {}
        
        # Node status
        try:
            nodes_output = subprocess.check_output(['kubectl', 'get', 'nodes', '-o', 'wide'], text=True)
            checks['nodes'] = nodes_output
        except subprocess.CalledProcessError:
            checks['nodes'] = 'Unable to obtain node information'
            
        # Pod status (related to AI)
        try:
            pods_output = subprocess.check_output(['kubectl', 'get', 'pods', '-n', 'ai-models', '-o', 'wide'], text=True)
            checks['ai_pods'] = pods_output
        except subprocess.CalledProcessError:
            checks['ai_pods'] = 'Unable to obtain AI Pods information'
            
        # Resource usage
        try:
            top_output = subprocess.check_output(['kubectl', 'top', 'nodes'], text=True)
            checks['resource_usage'] = top_output
        except subprocess.CalledProcessError:
            checks['resource_usage'] = 'Unable to obtain resource usage information'
            
        return checks
        
    def _check_ai_services(self):
        """Check AI service status"""
        
        services = ['model-registry', 'inference-service', 'training-operator']
        checks = {}
        
        for service in services:
            try:
                # Check service endpoints
                endpoints_output = subprocess.check_output(['kubectl', 'get', 'endpoints', '-n', 'ai-models', service], text=True)
                checks[f'{service}_endpoint'] = 'Normal' if 'ports' in endpoints_output else 'Abnormal'
                
                # Check errors in service logs
                logs_output = subprocess.check_output(['kubectl', 'logs', '-n', 'ai-models', f'deployment/{service}', '--tail=100'], text=True)
                error_count = logs_output.count('ERROR') + logs_output.count('Exception')
                checks[f'{service}_errors'] = error_count
                
            except subprocess.CalledProcessError as e:
                checks[f'{service}_endpoint'] = f'Diagnosis failed: {str(e)}'
                checks[f'{service}_errors'] = -1
                
        return checks
        
    def _analyze_performance(self):
        """Analyze performance metrics"""
        
        # Fetch metrics from Prometheus (requires Prometheus address configuration)
        performance_data = {}
        
        # Here you can integrate Prometheus API calls
        # Example metric check
        performance_data['recent_issues'] = self._get_recent_performance_issues()
        
        return performance_data
        
    def _check_security(self):
        """Security check"""
        
        security_checks = {}
        
        # Check Pod security policies
        try:
            psp_output = subprocess.check_output(['kubectl', 'get', 'podsecuritypolicies'], text=True)
            security_checks['pod_security_policies'] = 'Present' if 'NAME' in psp_output else 'Missing'
        except subprocess.CalledProcessError:
            security_checks['pod_security_policies'] = 'Diagnosis failed'
            
        # Check network policies
        try:
            netpol_output = subprocess.check_output(['kubectl', 'get', 'networkpolicies', '--all-namespaces'], text=True)
            security_checks['network_policies'] = 'exists' if 'NAME' in netpol_output else 'missing'
        except subprocess.CalledProcessError:
            security_checks['network_policies'] = 'check failed'
            
        return security_checks
        
    def _check_network_connectivity(self):
        """Check network connectivity"""
        
        targets = ['google.com', 'github.com', 'internal-registry.local']
        results = {}
        
        for target in targets:
            try:
                subprocess.check_output(['ping', '-c', '3', target], stderr=subprocess.STDOUT)
                results[target] = 'reachable'
            except subprocess.CalledProcessError:
                results[target] = 'unreachable'
                
        return results
        
    def _get_recent_performance_issues(self):
        """Find recent performance issues"""
        # Use simulated data instead of actual from monitoring system
        return [
            {'type': 'high_latency', 'timestamp': '2024-01-15T10:30:00Z', 'severity': 'warning'},
            {'type': 'low_throughput', 'timestamp': '2024-01-15T09:15:00Z', 'severity': 'info'}
        ]
        
    def _has_critical_issues(self):
        """Check for severe issues"""
        
        # Simplified logic for severe issue detection
        critical_indicators = [
            'gpus' in self.results.get('infrastructure', {}) and isinstance(self.results['infrastructure']['gpus'], str),
            'nodes' in self.results.get('kubernetes', {}) and 'NotReady' in self.results['kubernetes']['nodes'],
            any(service.endswith('_endpoint') and self.results['ai_services'][service] != 'normal' 
                for service in self.results.get('ai_services', {}))
        ]
        
        return any(critical_indicators)
        
    def _generate_report(self):
        """Generate diagnostic report"""
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'summary': self._generate_summary(),
            'detailed_results': self.results
        }
        
        # Save report
        with open(f'ai_diagnostic_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json', 'w') as f:
            json.dump(report, f, indent=2, default=str)
            
        # Generate HTML report
        self._generate_html_report(report)
        
    def _generate_summary(self):
        """Generate summary"""
        
        issues = []
        
        # Infrastructure issues
        infra = self.results.get('infrastructure', {})
        if isinstance(infra.get('gpus'), str):
            issues.append("GPU status abnormal")
            
        # Kubernetes issues
        k8s = self.results.get('kubernetes', {})
        if 'NotReady' in k8s.get('nodes', ''):
            issues.append("Kubernetes node abnormal")
            
        # AI service issues
        ai_services = self.results.get('ai_services', {})
        for service, status in ai_services.items():
            if service.endswith('_endpoint') and status != 'normal':
                issues.append(f"{service.replace('_endpoint', '')} service abnormal")
                
        return {
            'total_checks': len(self.results),
            'issues_found': len(issues),
            'critical_issues': issues,
            'overall_status': 'HEALTHY' if not issues else 'WARNING'
        }
        
    def _generate_html_report(self, report):
        """Generate HTML format report"""
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>AI平台诊断报告</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                .header {{ background-color: #f0f0f0; padding: 10px; border-radius: 5px; }}
                .section {{ margin: 20px 0; }}
                .issue {{ color: red; font-weight: bold; }}
                .ok {{ color: green; }}
                pre {{ background-color: #f5f5f5; padding: 10px; overflow-x: auto; }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>AI平台诊断报告</h1>
                <p>生成时间: {report['timestamp']}</p>
                <p>总体状态: <span class="{report['summary']['overall_status'].lower()}">{report['summary']['overall_status']}</span></p>
                <p>发现问题: {report['summary']['issues_found']} 个</p>
            </div>
            
            <div class="section">
                <h2>关键问题</h2>
                <ul>
        """
        
        for issue in report['summary']['critical_issues']:
            html_content += f"<li class='issue'>{issue}</li>"
            
        html_content += """
                </ul>
            </div>
            
            <div class="section">
                <h2>详细结果</h2>
                <pre>
        """
        
        html_content += json.dumps(report['detailed_results'], indent=2, default=str)
        html_content += """
                </pre>
            </div>
        </body>
        </html>
        """
        
        filename = f'ai_diagnostic_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html'
        with open(filename, 'w') as f:
            f.write(html_content)
            
        print(f"HTML report has been generated: {filename}")
        
    def _send_alerts(self):
        """Send alert email"""
        
        # Email configuration
        smtp_server = self.config.get('smtp_server', 'localhost')
        smtp_port = self.config.get('smtp_port', 587)
        sender_email = self.config.get('sender_email', 'alerts@company.com')
        recipient_emails = self.config.get('recipient_emails', [])
        
        if not recipient_emails:
            print("No configured recipient email")
            return
            
        # Create email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ', '.join(recipient_emails)
        msg['Subject'] = f"AI platform diagnostic alert - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        
        body = f"""
        AI平台诊断发现严重问题：
        
        {chr(10).join(self.results['summary']['critical_issues'])}
        
        请及时处理。
        
        详细报告请查看附件。
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            # If authentication is needed, uncomment and fill in credentials below
            # server.login(sender_email, "your_password")
            server.send_message(msg)
            server.quit()
            print("Alert email sent")
        except Exception as e:
            print(f"Send mail failed: {e}")

# Usage example
if __name__ == "__main__":
    diagnostic = AutomatedDiagnosticTool("diagnostic_config.yaml")
    results = diagnostic.run_full_diagnosis()
    print("Diagnosis completed, results saved")
```

---


## 5. Performance Optimization Best Practices

### 5.1 System-level Optimization

> ⚠️ **🟠 High-Risk Operations** — Affect business traffic or node status, require change ticket + impact assessment + planned rollback
> - `systemctl stop/restart`: Stop/restart system services, affecting all containers on the node

> **🔴 High-Risk Operation Warning**
>
> Below commands belong to irreversible or high-impact operations, execute only after confirming:
> - Key data and configurations have been backed up
> - Approved change window period is active
> - Has obtained authorization from relevant responsible parties
> - Has prepared rollback or recovery plans
> - Target cluster, Namespace, node/resource names are correct without error

``` bash
# 🔴 High-risk: May cause data loss or service disruption, execute after backing up, change approval, and rollback plan
#!/bin/bash
# system_optimization.sh - System performance optimization script

echo "Starting system performance optimization..."

# 1. Kernel parameter optimization
echo "Optimizing kernel parameters..."
cat >> /etc/sysctl.conf << EOF
# Network optimization
net.core.rmem_max = 134217728
net.core.wmem_max = 134217728
net.ipv4.tcp_rmem = 4096 87380 134217728
net.ipv4.tcp_wmem = 4096 65536 134217728
net.ipv4.tcp_congestion_control = bbr

# File system optimization
fs.file-max = 2097152
fs.nr_open = 2097152

# Memory optimization
vm.swappiness = 1
vm.dirty_ratio = 15
vm.dirty_background_ratio = 5
EOF

sysctl -p

# 2. GPU driver optimization
echo "Optimizing GPU driver settings..."
cat > /etc/modprobe.d/nvidia.conf << EOF
options nvidia NVreg_RegistryDwords="PerfLevelSrc=0x2222"
options nvidia NVreg_RestrictProfilingToAdminUsers=0
options nvidia NVreg_EnableGpuFirmware=1
EOF

# 3. systemd service optimization
echo "Optimizing systemd services..."
mkdir -p /etc/systemd/system/docker.service.d
cat > /etc/systemd/system/docker.service.d/override.conf << EOF
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd --data-root /fast-ssd/docker --log-driver=json-file --log-opt max-size=100m --log-opt max-file=3
EOF

systemctl daemon-reload
systemctl restart docker

# 4. Kubernetes component optimization
echo "Optimizing Kubernetes components..."
# kubelet configuration optimization
cat > /var/lib/kubelet/config.yaml << EOF
apiVersion: kubelet.config.k8s.io/v1beta1
kind: KubeletConfiguration
maxPods: 110
podPidsLimit: 4096
serializeImagePulls: false
evictionHard:
  memory.available: "500Mi"
  nodefs.available: "10%"
  nodefs.inodesFree: "5%"
featureGates:
  CPUManager: true
  MemoryManager: true
cpuManagerPolicy: static
memoryManagerPolicy: Static
reservedSystemCPUs: "0,1"
systemReserved:
  cpu: "1"
  memory: "4Gi"
kubeReserved:
  cpu: "1"
  memory: "4Gi"
EOF

echo "System optimization completed! Please restart the related services to make the configuration effective."
```
### 5.2 Application-level Optimization Checklist

✅ **Model Optimization**
- [ ] Enable model quantization (FP16/INT8)
- [ ] Use model parallelism to reduce single-GPU pressure
- [ ] Implement dynamic batching to improve throughput
- [ ] Enable KV caching reuse
- [ ] Optimize attention mechanisms (Flash Attention)

✅ **Container Optimization**
- [ ] Set reasonable resource limits and requests
- [ ] Enable node affinity and anti-affinity
- [ ] Configure appropriate probe timeout times
- [ ] Optimize image layer count and size
- [ ] Enable image pre-fetching

✅ **Network Optimization**
- [ ] Enable service mesh sidecar injection
- [ ] Configure reasonable connection pool parameters
- [ ] Enable HTTP/2 and gRPC
- [ ] Optimize DNS resolution configuration
- [ ] Enable connection reuse

---

---


## Obsidian Documentation

- domain-11-ai-infra MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — Open Source Project Index
- AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management
- [[domain-10-troubleshooting-diagnostics/topic-fta/list/apiserver-fta.md|API Server Fault Tree Analysis]]
- [[domain-10-troubleshooting-diagnostics/topic-fta/list/backup-restore-fta.md|Backup/Restore Fault Tree Analysis]]
- [[domain-10-troubleshooting-diagnostics/topic-fta/list/calico-fta.md|Calico FTA Tree: Calico CNI Fault Diagnosis]]

## See Also

- 12-ai-cost-analysis-finops
- 13-ai-platform-observability
- 15-llm-data-pipeline
- 16-llm-finetuning

```

<!-- risk-assessed -->
