---
title: Kubernetes AI/ML Production Operations Runbook
description: Covers GPU OOM, NCCL timeout, inference latency, model rollback, training checkpoints, MIG/DRA, multi-tenant quotas, and observability of AI workloads in production-grade operations manual
summary: Covers GPU OOM, NCCL timeout, inference latency, model rollback, training checkpoints, MIG/DRA, multi-tenant quotas, and observability of AI workloads in production-grade operations manual
category: ai-ml-infra
tags:
- production
- best-practices
- playbook
- ai
- ml
- gpu
- nvidia
- nccl
- inference
- checkpoint
- mig
- dra
- quota
- observability
tier: core
created: '2026-07-01'
last_updated: '2026-07'
difficulty: advanced
reading_level: advanced
audience:
- SRE
- Operations Engineer
- Platform Engineer
estimated_read_time: 25min
intent_queries:
- What is Kubernetes AI/ML Production Operations Runbook
- How to handle GPU OOM
- How to troubleshoot NCCL timeout
- How to optimize inference latency
- How to do model rollback
- How to use MIG/DRA
- How to use AI multi-tenant quotas
trigger_keywords:
- ai ml ops
- gpu oom
- nccl timeout
- inference latency
- model rollback
- checkpoint
- mig
- dra
- multi-tenant quota
- gpu observability
prerequisites:
- kubectl-basics
- gpu-scheduling-basics
- nvidia-gpu-basics
- prometheus-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
- '1.33'
authors:
- name: Dillan Teagle
  role: contributor
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/45-ai-ml-ops-runbook.md
---

> **Production Environment Security Tips**
>
> This document contains executable operational commands. Execute them only after confirming: the correct target cluster and namespace; sufficient RBAC permissions; and successful validation in a non-production environment. Risk levels are annotated: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).


# Kubernetes AI/ML Production Operations Runbook

> **Scope**: Kubernetes v1.28–v1.33 | **Last Updated**: 2026-07 | **Document Type**: Production Operations Guide

This Runbook targets SREs and MLOps engineers managing AI/ML production platforms, focusing on high-frequency faults and operations scenarios for GPU workloads: GPU OOM, NCCL distributed training timeout, inference latency spike, model version rollback, checkpoint protection, MIG/DRA resource partitioning, multi-tenant GPU quotas, and observability. AI workloads are resource-intensive, costly to fix, and complex to debug, necessitating dedicated monitoring, quota, and emergency response procedures.

---

## 1. Scope and Scope of Application

- **GPU OOM**: Training or inference Pods are killed due to insufficient GPU memory, or CUDA out-of-memory triggers.
- **NCCL Timeout**: NCCL collective communication times out during multi-node multi-card training, often due to network, topology, or IB/RoCE configuration issues.
- **Inference Latency**: Online inference services exceed SLAs with P99 latency, possibly caused by batch size, model version, or GPU contention.
- **Model Rollback**: New models degrade performance post-launch, requiring rapid rollback to previous versions.
- **Checkpoint Protection**: Long-running training tasks must periodically save checkpoints and recover from node failures.
- **MIG/DRA**: Production implementation of NVIDIA MIG physical partitioning and Kubernetes DRA dynamic resource allocation.
- **Multi-Tenant Quotas**: Allocate GPUs, VRAM, CPUs, and memory based on teams/projects to prevent noisy neighbors.

---

## 2. Pre-requisites and Tools

### 2.1 Infrastructure Pre-requisites

- NVIDIA Driver + NVIDIA Container Toolkit + device-plugin are installed on nodes.
- DCGM Exporter and Node Feature Discovery (NFD) are deployed.
- RuntimeClass (nvidia) and GPU Operator are configured.
- Training storage uses high-performance parallel file systems (Lustre/BeeGFS/FSx for Lustre) or object storage + PVC.

### 2.2 Essential Tools

| Tool | Purpose | Recommended Version |
|------|------|----------|
| `nvidia-smi` | GPU Status and Memory View | With Driver |
| `dcgmi` | GPU Health Diagnosis | 3.x+ |
| `nccl-tests` | NCCL Performance Benchmark | 2.20+ |
| `kubectl` | Pod/Node/Event View | v1.28+ |
| Prometheus + DCGM Exporter | GPU Metrics Collection | v3.x+ |
| Volcano/Yunikorn | Batch Scheduling and Queues | 1.9+ / 1.5+ |
| KServe/Triton | Inference Service Management | 0.13+ / 2.48+ |

---

## 3. Standard Operating Procedures

### 3.1 Diagnosing and Handling GPU OOM

#### On-Site Collection

``` bash
# 🟡 Medium Risk: modifies cluster/resource state; confirm target, impact scope, and authorization before execution
# View Pod status and events
kubectl describe pod <pod> -n <ns>
kubectl logs <pod> -n <ns> --previous

# View node GPU memory
kubectl exec -it <pod> -n <ns> -- nvidia-smi

# View DCGM metrics
kubectl port-forward -n monitoring svc/dcgm-exporter 9400:9400
curl -s localhost:9400/metrics | grep -i memory
```
#### Common Root Causes

- **Batch Size Too Large**: Reduce batch size or enable gradient accumulation.
- **Incorrect Model Parallel Strategy**: Use ZeRO/FSDP/Tensor Parallelism instead.
- **Memory Leaks**: PyTorch cache not released, add `torch.cuda.empty_cache()`.
- **Shared GPU for Multiple Tasks**: MIG partitioning insufficient, or Request/Limit not aligned with actual GPU memory.

#### Mitigation Commands

``` bash
# 🟡 Medium Risk: modifies cluster/resource state; confirm target, impact scope, and authorization
# Reduce batch size (via environment variable or ConfigMap)
kubectl set env deployment/<training> -n <ns> BATCH_SIZE=16

# Temporarily increase GPU resources
kubectl patch deployment <training> -n <ns> -p '{"spec":{"template":{"spec":{"containers":[{"name":"train","resources":{"limits":{"nvidia.com/gpu":"2"}}}]}}}}'
```
### 3.2 Diagnosing NCCL Timeout Issues

NCCL timeout typically manifests as `NCCL_TIMEOUT` or `NCCL_WATCHDOG` errors.

#### Checklist

1. **Network Connectivity**:
   ```bash
   kubectl exec -it <pod> -n <ns> -- bash
   ping <peer-pod-ip>
   ib_write_bw # 若使用 InfiniBand
   ```
2. **NCCL Debug Logs**:
   ```bash
   export NCCL_DEBUG=INFO
   export NCCL_DEBUG_SUBSYS=ALL
   ```
3. **Topology and NIC Binding**:
   ```bash
   nvidia-smi topo -m
   ```
4. **Firewall and Security Groups**: Ensure Pod-to-Pod connectivity on ports like 29500 for NCCL.
5. **IB/RoCE Configuration**: Check that `NCCL_IB_DISABLE`, `NCCL_SOCKET_IFNAME` are correctly set.

#### Common Fixes

``` bash
# 🟡 Medium Risk: modifies cluster/resource state; confirm target, impact scope, and authorization
# Force use of TCP Socket (temporarily bypass RoCE instability)
kubectl set env job/<distributed-training> NCCL_IB_DISABLE=1

# Specify communication NIC
kubectl set env job/<distributed-training> NCCL_SOCKET_IFNAME=eth0
```
### 3.3 Optimizing Inference Latency

#### Diagnostic Commands

``` bash
# 🟡 Medium Risk: modifies cluster/resource state; confirm target, impact scope, and authorization
# KServe inference Pod latency metric
curl http://<inference-service>/v2/models/<model>/metrics

# GPU utilization and memory
kubectl exec -it <inference-pod> -n <ns> -- nvidia-smi dmon -s u
```
#### Optimization Measures

| Issue | Optimization Measures |
|------|----------|
| Insufficient Batch Size | Enable dynamic batching / Triton ensemble |
| Model Too Large | Quantization (INT8/FP16), distillation, model pruning |
| GPU Contention | Set high PriorityClass and exclusive GPU for inference services. |
| Cold Start | Configure minimum replica count and pre-warm KServe predictor. |
| Network Latency | Deploy inference Pods near the entry point, use topology-aware routing. |

### 3.4 Model Rollback

KServe InferenceService Rollback:

``` bash
# 🟡 Medium Risk: modifies cluster/resource state; confirm target, impact scope, and authorization
# View historical revisions
kubectl get revision -n <ns> -l serving.kserve.io/inferenceservice=<model>

# Rollback to specified revision
kubectl patch inferenceservice <model> -n <ns> -p '{"spec":{"predictor":{"canaryTrafficPercent":0,"tensorflow":{"storageUri":"s3://models/v1.2.3"}}}}' --type=merge
```
Or use Argo Rollouts to manage model service instances:

```bash
argocd app rollback <model-service> <revision>
```

### 3.5 Protecting Training Checkpoints

#### Checkpoint Saving Strategies

```yaml
spec:
  containers:
  - name: train
    env:
    - name: CHECKPOINT_DIR
      value: /checkpoints
    - name: SAVE_INTERVAL
      value: "3600"
    volumeMounts:
    - name: checkpoints
      mountPath: /checkpoints
  volumes:
  - name: checkpoints
    persistentVolumeClaim:
      claimName: training-checkpoints
```

#### Fault Recovery Strategies

``` bash
# 🟡 Medium Risk: modifies cluster/resource state; confirm target, impact scope, and authorization
# View latest checkpoint
kubectl exec -it <pod> -n <ns> -- ls -lt /checkpoints

# Resubmit training task, load latest checkpoint
kubectl create job --from=cronjob/<training-cron> resume-training-$(date +%s) -n <ns>
```
### 3.6 MIG And DRA Configuration

#### MIG Strategy

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: nvidia-mig-config
  namespace: gpu-operator
data:
  config.yaml: |
    version: v1
    mig-configs:
      all-1g.5gb:
        - devices: all
          mig-enabled: true
          mig-devices:
            "1g.5gb": 7
```

Pod requests MIG:

```yaml
resources:
  limits:
    nvidia.com/mig-1g.5gb: 1
```

#### DRA (Dynamic Resource Allocation)

Applicable for K8s v1.32+, requires enabling the `DynamicResourceAllocation` feature gate and deploying the DRA driver.

### 3.7 Multi-Tenant GPU Quota

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: team-ai-quota
  namespace: team-ai
spec:
  hard:
    requests.nvidia.com/gpu: 8
    limits.nvidia.com/gpu: 8
    requests.memory: 512Gi
    requests.cpu: 64
```

Complement with LimitRange and Volcano Queue to implement priority and preemptive strategies.

---

## 4. Key Points and Verification Commands

| Check Item | Command | Pass Criteria |
|--------|------|----------|
| GPU Node Status | `kubectl get nodes -L nvidia.com/gpu.count` | Node Ready, correct GPU count |
| Pod GPU Allocation | `kubectl describe pod <pod> -n <ns>` | GPU allocated successfully |
| GPU Utilization | `curl localhost:9400/metrics \| grep DCGM_FI_DEV_GPU_UTIL` | Within expected range |
| NCCL Test | `all_reduce_perf -b 8M -e 1G -f 2 -g 8` | Bandwidth close to theoretical value |
| Inference Latency | KServe/Triton metrics | P99 ≤ Service Level Objective (SLO) |
| Checkpoint Integrity | `ls -lt /checkpoints` | Recent checkpoint exists within the last hour |
| Quota Usage | `kubectl describe quota -n <ns>` | Not over quota |

---

## 5. Rollback/Incident Response Plan

- **GPU Node Failure**: Mark the node as unschedulable and evict the workload.
  ```bash
  kubectl cordon <node>
  kubectl drain <node> --ignore-daemonsets --force --delete-emptydir-data
  ```
- **Training Task OOM Repeated Failures**: Reduce batch size, enable CPU offloading, or switch to a larger GPU model.
- **Inference Service Degradation**: Immediately revert to the previous model version and ensure minimum replicas via PDB + HPA.
- **NCCL Communication Completely Interrupted**: Temporarily switch to single-node multi-GPU or reduce distributed scale, investigate network issues before recovery.
- **Checkpoint Damage**: Rollback to the last valid checkpoint, losing some training progress.

---

## 6. Risks and Considerations

1. **GPU Driver and CUDA Version Consistency**: Inconsistent versions can lead to hidden performance degradation or crashes.
2. **MIG and DRA Coexistence Risks**: Do not mix traditional device-plugin with DRA on the same node to avoid resource conflicts.
3. **Long-Running Training Tasks**: Tasks exceeding 24 hours must configure checkpoints, and nodes should be maintained with prior notification and graceful termination.
4. **Inference Service Cold Start Costs** : Long model loading times require configuring minimum replicas and readiness probe timeouts.
5. **Tenant Isolation** : GPU memory isolation relies on MIG/DRA, while process-level isolation still requires seccomp/AppArmor.

---

## 7. Related Runbooks / Recommended Reading

- [[domain-14-ai-ml-infra/99-production-readiness-operations-guide.md|AI/ML Infrastructure Production Readiness Operations Guide]]
- [[domain-11-production-operations/99-production-readiness-operations-guide.md|Production Operations Production Readiness Operations Guide]]
- [[domain-14-ai-ml-infra/01-ai-infra/03-gpu-scheduling-management.md|GPU Scheduling and Management]]
- [[domain-14-ai-ml-infra/01-ai-infra/04-gpu-monitoring-dcgm.md|GPU Monitoring and DCGM]]
- [[domain-14-ai-ml-infra/01-ai-infra/05-distributed-training-frameworks.md|Distributed Training Frameworks]]
- [[domain-14-ai-ml-infra/01-ai-infra/10-model-deployment-management.md|Model Deployment Management]]
- [[domain-14-ai-ml-infra/01-ai-infra/14-troubleshooting-performance.md|Performance Troubleshooting]]
- [[domain-14-ai-ml-infra/01-ai-infra/17-llm-inference-serving.md|LLM Inference Serving]]


<!-- risk-assessed -->
