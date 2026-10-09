---
title: LLM Cost Monitoring and FinOps
description: '# LLM Cost Monitoring and FinOps'
summary: 'The cost structure of LLM workloads is significantly different from traditional applications, with GPU computing costs being predominant. This document details the LLM cost monitoring system, optimization strategies, and FinOps practices.'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- prometheus
- grafana
- helm
- hpa
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
- What is LLM Cost Monitoring and FinOps
- How is LLM Cost Monitoring and FinOps
- Kubernetes 11 AI Infrastructure Best Practices
trigger_keywords:
- LLM
- Cost Monitoring and
- FinOps
- ai
- infra
prerequisites:
- kubectl-basics
- helm-basics
- prometheus-basics
- monitoring-basics
- gpu-scheduling-basics
- policy-basics
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
- type: fta
  path: ../domain-10-troubleshooting-diagnostics/topic-fta/list/monitoring-fta.md
  label: 'Fault Tree: monitoring'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/23-llm-cost-monitoring.md
---

> **Production Environment Security Tips**
>
> This document contains executable operational commands. Execute them only after confirming: the correct target cluster and namespace; sufficient RBAC permissions; and successful validation in a non-production environment. Risk levels for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# LLM Cost Monitoring and FinOps


## Overview

LLM workloads have a significantly different cost structure compared to traditional applications, with GPU computing being dominant. This document details the LLM cost monitoring system, optimization strategies, and FinOps practices.


## Cost Architecture

### LLM Cost Composition Model

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              LLM Cost Composition Model                               │
│                                                                                      │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │                           Total Cost (Total Cost)                                │   │
│   │                                                                              │   │
│   │   ┌─────────────────────────────────────────────────────────────────────┐   │   │
│   │   │                      GPU Compute Cost (65-80%)                           │   │   │
│   │   │                                                                      │   │   │
│   │   │   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐               │   │   │
│   │   │   │   Training Cost   │   │   Inference Cost   │   │   Fine-tuning Cost   │               │   │   │
│   │   │   │             │   │             │   │             │               │   │   │
│   │   │   │ • Batch Size Large    │   │ • Continuous Run  │   │ • Medium Batch  │               │   │   │
│   │   │   │ • High Memory    │   │ • Low Latency    │   │ • Periodic  │               │   │   │
│   │   │   │ • Non-Interruptible    │   │ • Elastic Scaling  │   │ • Non-Interruptible  │               │   │   │
│   │   │   └─────────────┘   └─────────────┘   └─────────────┘               │   │   │
│   │   │                                                                      │   │   │
│   │   └──────────────────────────────────────────────────────────────────────┘   │   │
│   │                                                                              │   │
│   │   ┌────────────────────────┐   ┌────────────────────────┐                   │   │
│   │   │     Storage Cost (15-20%)   │   │     Network Cost (5-10%)    │                   │   │
│   │   │                        │   │                        │                   │   │
│   │   │  • Model Storage (Large)       │   │  • Cross-AZ Transfer          │                   │   │
│   │   │  • Checkpoint Storage          │   │  • Inference Request Traffic          │                   │   │
│   │   │  • Dataset Storage          │   │  • Model Distribution          │                   │   │
│   │   │  • Cache Storage            │   │  • API Gateway Traffic          │                   │   │
│   │   └────────────────────────┘   └────────────────────────┘                   │   │
│   │                                                                              │   │
│   │   ┌────────────────────────┐   ┌────────────────────────┐                   │   │
│   │   │     Management Cost (3-5%)     │   │     Other Costs (2-5%)     │                   │   │
│   │   │                        │   │                        │                   │   │
│   │   │  • Monitoring/Observability       │   │  • Log Storage            │                   │   │
│   │   │  • Orchestration Scheduling            │   │  • Security Audits            │                   │   │
│   │   │  • MLOps Tools            │   │  • Backups/DR            │                   │   │
│   │   └────────────────────────┘   └────────────────────────┘                   │   │
│   │                                                                              │   │
│   └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

### Cost Monitoring Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              LLM Cost Monitoring Architecture                               │
│                                                                                      │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │                           Data Collection Layer (Collection)                            │   │
│   │                                                                              │   │
│   │   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐ │   │
│   │   │   Kubecost   │   │   DCGM       │   │   Cloud Vendor     │   │   Custom     │ │   │
│   │   │   Exporter   │   │   Exporter   │   │   Billing    │   │   Metrics    │ │   │
│   │   │              │   │              │   │   API        │   │              │ │   │
│   │   │ • Pod Cost   │   │ • GPU Utilization │   │ • On-Demand Pricing  │   │ • Token Count  │ │   │
│   │   │ • node cost   │   │ • GPU usage   │   │ • Spot price   │   │ • request count   │ │   │
│   │   │ • storage cost   │   │ • power consumption   │   │ • RI/SP information   │   │ • model invocation   │ │   │
│   │   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘ │   │
│   │                                                                              │   │
│   └──────────────────────────────────┬──────────────────────────────────────────┘   │
│                                      │                                              │
│                                      ▼                                              │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │                           Storage Layer (Storage)                                   │   │
│   │                                                                              │   │
│   │   ┌──────────────────────────────────────────────────────────────────────┐  │   │
│   │   │                         Prometheus                                    │  │   │
│   │   │   • kubecost_*          • DCGM_FI_*        • llm_*                   │  │   │
│   │   │   • node_*              • container_*      • custom_*                │  │   │
│   │   └──────────────────────────────────────────────────────────────────────┘  │   │
│   │                                                                              │   │
│   └──────────────────────────────────┬──────────────────────────────────────────┘   │
│                                      │                                              │
│                                      ▼                                              │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │                          Analysis Layer (Analysis)                                   │   │
│   │                                                                              │   │
│   │   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐ │   │
│   │   │   Cost Allocation   │   │   Trend Forecasting   │   │   Anomaly Detection   │   │   Optimization Recommendations   │ │   │
│   │   │              │   │              │   │              │   │              │ │   │
│   │   │ • by team     │   │ • by day/week/month   │   │ • cost escalation   │   │ • resource adjustment   │ │   │
│   │   │ • project     │   │ • budget forecast   │   │ • idle GPU   │   │ • instance selection   │ │   │
│   │   │ • according to the model     │   │ • capacity planning   │   │ • waste of resources   │   │ • schedule optimization   │ │   │
│   │   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘ │   │
│   │                                                                              │   │
│   └──────────────────────────────────┬──────────────────────────────────────────┘   │
│                                      │                                              │
│                                      ▼                                              │
│   ┌─────────────────────────────────────────────────────────────────────────────┐   │
│   │                          Visualization Layer (Visualization)                              │   │
│   │                                                                              │   │
│   │   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐   ┌──────────────┐ │   │
│   │   │   Grafana    │   │   Kubecost   │   │   Custom     │   │   Alert Notification   │ │   │
│   │   │   Dashboard  │   │   UI         │   │   Report     │   │   Slack/Mail │ │   │
│   │   └──────────────┘   └──────────────┘   └──────────────┘   └──────────────┘ │   │
│   │                                                                              │   │
│   └─────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
└──────────────────────────────────────────────────────────────────────────────────────┘
```


## Cost Composition Details

### Proportion of Various Costs

| Cost Type | Ratio Range | Main Factors | Optimization Direction |
|---------|---------|---------|---------|
| **GPU Computing** | 65-80% | Instance type, utilization, runtime | Spot instances, batch processing, quantization |
| **Storage** | 15-20% | Model size, checkpoints, dataset | Layered storage, compression, cleanup strategy |
| **Network** | 5-10% | Cross-region transfers, API traffic | CDN, regional optimization, compression |
| **Management** | 3-5% | Monitoring, orchestration, MLOps | Tool integration, automation |
| **Other** | 2-5% | Logs, audits, backups | Retention policies, sampling |

### GPU Instance Price Comparison

| GPU Type | Memory | On-demand price/hour | Spot price/hour | Savings ratio | Applicable scenarios |
|---------|------|-------------|--------------|---------|---------|
| **NVIDIA A100 80GB** | 80GB | $32.77 | ~$10.00 | 70% | Large model training, multi-GPU training |
| **NVIDIA A100 40GB** | 40GB | $22.00 | ~$6.50 | 70% | Medium-sized model training |
| **NVIDIA A10G** | 24GB | $1.006 | ~$0.30 | 70% | Inference, fine-tuning |
| **NVIDIA L4** | 24GB | $0.81 | ~$0.25 | 69% | Inference optimization |
| **NVIDIA T4** | 16GB | $0.526 | ~$0.16 | 70% | Lightweight inference, development |
| **NVIDIA V100** | 16/32GB | $3.06 | ~$0.92 | 70% | General training |
| **NVIDIA H100** | 80GB | $50.00+ | ~$15.00 | 70% | Super large models, high performance |

### Storage Cost Segmentation

| Storage Type | Price Reference | Typical Usage | Monthly Cost Estimate | Optimization Strategies |
|---------|---------|---------|-----------|---------|
| **Model Storage** | $0.023/GB | 500GB-5TB | $12-$115 | Compression, deduplication |
| **Checkpoint Storage** | $0.023/GB | 1TB-10TB | $23-$230 | Regular cleanup, retention policies |
| **Data Set Storage** | $0.023/GB | 1TB-50TB | $23-$1150 | Tiered storage, archiving |
| **Cache Storage** | $0.10/GB | 100GB-1TB | $10-$100 | TTL policy, LRU |
| **Log Storage** | $0.50/GB | 50GB-500GB | $25-$250 | Sampling, compression |


## Kubecost Deployment and Configuration

### Complete Deployment Configuration

```yaml
# kubecost-values.yaml
# Kubecost Helm values configuration

global:
  # Enable GPU cost monitoring
  prometheus:
    enabled: true
    nodeExporter:
      enabled: true

# Core configuration for Kubecost
kubecostModel:
  # Custom GPU pricing
  gpuCost:
    enabled: true
    # Set prices by GPU type
    gpuTypeCosts:
      nvidia-tesla-a100: "32.77"
      nvidia-tesla-a10g: "1.006"
      nvidia-tesla-t4: "0.526"
      nvidia-tesla-v100: "3.06"
      nvidia-tesla-h100: "50.00"
      
  # Custom pricing
  customPricing:
    enabled: true
    configPath: "/var/configs/pricing.json"
    
  # Cost allocation configuration
  allocation:
    # Allocate costs by label
    labelConfig:
      enabled: true
      labels:
        - team
        - project
        - model
        - environment
        - cost-center
        
# Integration with Prometheus
prometheus:
  server:
    retention: "30d"
    resources:
      requests:
        cpu: "500m"
        memory: "2Gi"
      limits:
        cpu: "2"
        memory: "8Gi"
        
# DCGM Exporter integration (GPU monitoring)
dcgmExporter:
  enabled: true
  
# Network cost
networkCosts:
  enabled: true
  # Cross-region traffic cost
  zoneCost: "0.01"
  regionCost: "0.02"
  internetCost: "0.12"

# Storage configuration
persistentVolume:
  enabled: true
  size: "32Gi"
  storageClass: "gp3"

# Alert configuration
alerts:
  enabled: true
  # Budget alert
  budget:
    enabled: true
    
# RBAC
rbac:
  create: true
  
# ServiceAccount
serviceAccount:
  create: true
  annotations:
    # AWS IRSA
    # eks.amazonaws.com/role-arn: arn:aws:iam::ACCOUNT:role/kubecost-role
```

### Deployment Command

> ⚠️ **🟡 Medium Risk Change** — Change cluster resource state, suggest to first use --dry-run or diff to confirm
> - `helm upgrade/install`: Deploy/upgrade release
> - `kubectl apply/create/replace`: Create/modify cluster resources

``` bash
# 🟡 Medium risk: Will modify cluster/resource state, please confirm target, impact scope, and authorization before execution
#!/bin/bash
# deploy-kubecost.sh
# Kubecost deployment script

set -e

NAMESPACE="kubecost"
RELEASE_NAME="kubecost"

message: "Kubecost deployment ==="

# Add Helm repository
helm repo add kubecost https://kubecost.github.io/cost-analyzer/
helm repo update

# Create namespace
kubectl create namespace $NAMESPACE --dry-run=client -o yaml | kubectl apply -f -

# Deploy Kubecost
helm upgrade --install $RELEASE_NAME kubecost/cost-analyzer \
  --namespace $NAMESPACE \
  --values kubecost-values.yaml \
  --set kubecostToken="${KUBECOST_TOKEN}" \
  --wait

# Wait for Pod to be ready
kubectl wait --for=condition=Ready pod \
  -l app=cost-analyzer \
  -n $NAMESPACE \
  --timeout=300s

message: "Kubecost deployment complete ==="
message: "Access: kubectl port-forward -n $NAMESPACE svc/kubecost-cost-analyzer 9090:9090"
```

## Cost Tagging System

### Recommended Tagging Norms

```yaml
# cost-labels-convention.yaml
# LLM Workload Cost Label Specification

---
# Training Task Pod
apiVersion: v1
kind: Pod
metadata:
  name: llama2-70b-training
  namespace: ml-training
  labels:
    # Organizational Tag
    team: ml-research
    department: ai-platform
    cost-center: "CC-12345"
    
    # Project Tag
    project: llama2-finetuning
    model: llama2-70b
    task-type: training
    
    # Project Environment Tag
    environment: production
    
    # Resource Tag
    gpu-type: a100-80g
    gpu-count: "8"
    
  annotations:
    # Kubecost Cost Allocation Annotation
    cost.kubernetes.io/team: "ml-research"
    cost.kubernetes.io/project: "llama2-finetuning"
    cost.kubernetes.io/environment: "production"
    
    # Task Metadata
    ml.kubernetes.io/experiment-id: "exp-20240115-001"
    ml.kubernetes.io/run-id: "run-abc123"
    
spec:
  containers:
  - name: trainer
    image: pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime
    resources:
      limits:
        nvidia.com/gpu: 8
        memory: "640Gi"
        cpu: "64"
      requests:
        nvidia.com/gpu: 8
        memory: "512Gi"
        cpu: "32"
    env:
    - name: TRAINING_JOB_ID
      value: "job-20240115-001"

---
# Inference Service Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: llama2-inference
  namespace: ml-inference
  labels:
    team: ml-platform
    project: llm-inference
    model: llama2-7b
    task-type: inference
    environment: production
    cost-center: "CC-67890"
spec:
  replicas: 3
  selector:
    matchLabels:
      app: llama2-inference
  template:
    metadata:
      labels:
        app: llama2-inference
        team: ml-platform
        project: llm-inference
        model: llama2-7b
        task-type: inference
        gpu-type: a10g
      annotations:
        cost.kubernetes.io/team: "ml-platform"
        cost.kubernetes.io/project: "llm-inference"
    spec:
      containers:
      - name: inference
        image: vllm/vllm-openai:latest
        resources:
          limits:
            nvidia.com/gpu: 1
          requests:
            nvidia.com/gpu: 1
```

### Cost Tagging Verification Strategy

```yaml
# cost-label-policy.yaml
# Use Kyverno to enforce cost labels

apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: require-cost-labels
spec:
  validationFailureAction: Enforce
  background: true
  rules:
    - name: require-team-label
      match:
        any:
          - resources:
              kinds:
                - Pod
              namespaces:
                - ml-*
                - ai-*
      validate:
        message: "ML workload must contain team tag"
        pattern:
          metadata:
            labels:
              team: "?*"
              
    - name: require-project-label
      match:
        any:
          - resources:
              kinds:
                - Pod
              namespaces:
                - ml-*
                - ai-*
      validate:
        message: "ML workload must contain project tag"
        pattern:
          metadata:
            labels:
              project: "?*"
              
    - name: require-cost-center
      match:
        any:
          - resources:
              kinds:
                - Pod
              selector:
                matchLabels:
                  task-type: training
      validate:
        message: "Training task must contain cost-center tag"
        pattern:
          metadata:
            labels:
              cost-center: "?*"
```


## Cost Monitoring API

### Python Cost Monitoring Client

```python
# llm_cost_monitor.py
# LLM Cost Monitoring Client

import requests
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import json

class KubecostClient:
    """Kubecost API client"""
    
    def __init__(self, base_url: str = "http://kubecost-cost-analyzer.kubecost:9090"):
        self.base_url = base_url
        self.session = requests.Session()
        
    def get_allocation(
        self,
        window: str = "7d",
        aggregate: str = "namespace",
        filter_labels: Optional[Dict] = None
    ) -> Dict:
        """get cost allocation data"""
        url = f"{self.base_url}/model/allocation"
        params = {
            "window": window,
            "aggregate": aggregate,
            "accumulate": "true"
        }
        
        if filter_labels:
            filter_str = ",".join([f'{k}:"{v}"' for k, v in filter_labels.items()])
            params["filterLabels"] = filter_str
            
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_cost_by_label(
        self,
        label: str,
        window: str = "7d"
    ) -> Dict:
        """get cost by tag"""
        url = f"{self.base_url}/model/allocation"
        params = {
            "window": window,
            "aggregate": f"label:{label}",
            "accumulate": "true"
        }
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_gpu_cost(
        self,
        namespace: Optional[str] = None,
        window: str = "7d"
    ) -> Dict:
        """get GPU cost"""
        url = f"{self.base_url}/model/allocation"
        params = {
            "window": window,
            "aggregate": "namespace,label:gpu-type",
            "accumulate": "true"
        }
        
        if namespace:
            params["filterNamespaces"] = namespace
            
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()


class LLMCostMonitor:
    """LLM Cost Monitor"""
    
    def __init__(self, kubecost_url: str = "http://kubecost:9090"):
        self.kubecost = KubecostClient(kubecost_url)
        
    def get_training_cost(
        self,
        project: str,
        window: str = "30d"
    ) -> Dict:
        """get training task cost"""
        data = self.kubecost.get_allocation(
            window=window,
            aggregate="label:project",
            filter_labels={"task-type": "training", "project": project}
        )
        
        return self._parse_allocation(data, project)
    
    def get_inference_cost(
        self,
        model: str,
        window: str = "30d"
    ) -> Dict:
        """Get inference service cost"""
        data = self.kubecost.get_allocation(
            window=window,
            aggregate="label:model",
            filter_labels={"task-type": "inference", "model": model}
        )
        
        return self._parse_allocation(data, model)
    
    def get_team_cost_summary(
        self,
        window: str = "30d"
    ) -> pd.DataFrame:
        """Get team cost summary"""
        data = self.kubecost.get_cost_by_label("team", window)
        
        results = []
        for team, allocation in data.get("data", [{}])[0].items():
            if team == "__unmounted__":
                continue
            results.append({
                "Team": team,
                "CPU Cost": allocation.get("cpuCost", 0),
                "Memory Cost": allocation.get("ramCost", 0),
                "GPU Cost": allocation.get("gpuCost", 0),
                "Storage Cost": allocation.get("pvCost", 0),
                "Network Cost": allocation.get("networkCost", 0),
                "Total Cost": allocation.get("totalCost", 0)
            })
            
        df = pd.DataFrame(results)
        df = df.sort_values("Total Cost", ascending=False)
        return df
    
    def get_gpu_utilization_cost(
        self,
        namespace: str,
        window: str = "7d"
    ) -> Dict:
        """Get GPU utilization and cost"""
        # Get cost data
        cost_data = self.kubecost.get_gpu_cost(namespace, window)
        
        # Calculate GPU efficiency
        gpu_cost = sum([
            alloc.get("gpuCost", 0) 
            for alloc in cost_data.get("data", [{}])[0].values()
            if isinstance(alloc, dict)
        ])
        
        return {
            "namespace": namespace,
            "window": window,
            "gpu_cost": gpu_cost,
            "estimated_waste": gpu_cost * 0.3  # 假设 30% 闲置
        }
    
    def _parse_allocation(self, data: Dict, key: str) -> Dict:
        """Parse allocation data"""
        allocations = data.get("data", [{}])[0]
        allocation = allocations.get(key, {})
        
        return {
            "cpu_cost": allocation.get("cpuCost", 0),
            "memory_cost": allocation.get("ramCost", 0),
            "gpu_cost": allocation.get("gpuCost", 0),
            "storage_cost": allocation.get("pvCost", 0),
            "network_cost": allocation.get("networkCost", 0),
            "total_cost": allocation.get("totalCost", 0),
            "gpu_hours": allocation.get("gpuHours", 0),
            "cpu_hours": allocation.get("cpuCoreHours", 0)
        }


class BudgetManager:
    """Budget Manager"""
    
    def __init__(
        self,
        monthly_budget: float,
        alert_thresholds: List[float] = [0.5, 0.75, 0.9, 1.0]
    ):
        self.monthly_budget = monthly_budget
        self.daily_budget = monthly_budget / 30
        self.alert_thresholds = alert_thresholds
        
    def check_budget_status(
        self,
        current_spend: float,
        days_elapsed: int
    ) -> Dict:
        """Check budget status"""
        # Calculate expected monthly spend
        daily_avg = current_spend / max(days_elapsed, 1)
        projected_monthly = daily_avg * 30
        
        # Calculate budget usage rate
        budget_used = current_spend / self.monthly_budget
        projected_usage = projected_monthly / self.monthly_budget
        
        # Determine status
        if projected_usage > 1.1:
            status = "CRITICAL"
            message: "ML workload exceeds budget by {(projected_usage - 1) * 100:.1f}%"
        elif projected_usage > 1.0:
            status = "WARNING"
            message: "Budget overrun"
        elif projected_usage > 0.9:
            status = "CAUTION"
            message: "Approaching budget limit"
        else:
            status = "OK"
            message: "Budget usage normal"
            
        return {
            "status": status,
            "message": message,
            "current_spend": current_spend,
            "monthly_budget": self.monthly_budget,
            "budget_used_percent": budget_used * 100,
            "projected_monthly": projected_monthly,
            "projected_usage_percent": projected_usage * 100,
            "remaining_budget": self.monthly_budget - current_spend,
            "daily_budget_remaining": (self.monthly_budget - current_spend) / max(30 - days_elapsed, 1)
        }
    
    def get_alerts(
        self,
        current_spend: float
    ) -> List[Dict]:
        """Get budget alert"""
        alerts = []
        budget_used = current_spend / self.monthly_budget
        
        for threshold in self.alert_thresholds:
            if budget_used >= threshold:
                alerts.append({
                    "threshold": threshold * 100,
                    "current": budget_used * 100,
                    "severity": "critical" if threshold >= 1.0 else "warning" if threshold >= 0.9 else "info"
                })
                
        return alerts


# Usage Example
if __name__ == "__main__":
    # Initialize monitor
    monitor = LLMCostMonitor("http://kubecost:9090")
    
    # Get team cost summary
    team_costs = monitor.get_team_cost_summary(window="30d")
    print("=== Team cost summary ===")
    print(team_costs.to_markdown())
    
    # Get training cost
    training_cost = monitor.get_training_cost("llama2-finetuning", "30d")
    print(f"\n=== Training cost ===")
    print(f"GPU cost: ${training_cost['gpu_cost']:.2f}")
    print(f"Total cost: ${training_cost['total_cost']:.2f}")
    
    # Budget check
    budget = BudgetManager(monthly_budget=50000)
    status = budget.check_budget_status(current_spend=25000, days_elapsed=15)
    print(f"\n=== Budget status ===")
    print(f"Status: {status['status']}")
    print(f"Used: {status['budget_used_percent']:.1f}%")
    print(f"Monthly expenditure: ${status['projected_monthly']:.2f}")
```


## Cost Alert Rules

### Prometheus Alert Rules

```yaml
# llm-cost-alerting-rules.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: llm-cost-alerts
  namespace: monitoring
  labels:
    prometheus: k8s
    role: alert-rules
spec:
  groups:
    # =================================================================
    # Cost threshold alert
    # =================================================================
    - name: llm.cost.thresholds
      interval: 5m
      rules:
        - alert: LLMDailyCostHigh
          expr: |
            sum(increase(kubecost_cluster_cost_total[24h])) > 1000
          for: 30m
          labels:
            severity: warning
            team: finops
          annotations:
            summary: "LLM daily cost exceeds $1000"
            description: |
              过去 24 小时 LLM 工作负载成本: ${{ $value | printf "%.2f" }}
              阈值: $1000
            runbook_url: "https://wiki/runbooks/llm-cost-high"
            
        - alert: LLMDailyCostCritical
          expr: |
            sum(increase(kubecost_cluster_cost_total[24h])) > 5000
          for: 15m
          labels:
            severity: critical
            team: finops
          annotations:
            summary: "LLM daily cost severely overruns (> $5000)"
            description: |
              过去 24 小时 LLM 工作负载成本: ${{ $value | printf "%.2f" }}
              需要立即检查和优化
              
        - alert: LLMCostSpike
          expr: |
            (
              sum(increase(kubecost_namespace_cost_total{namespace=~"ml-.*|ai-.*"}[1h]))
              /
              avg_over_time(sum(increase(kubecost_namespace_cost_total{namespace=~"ml-.*|ai-.*"}[1h]))[24h:1h])
            ) > 2
          for: 15m
          labels:
            severity: warning
          annotations:
            summary: "LLM cost suddenly surged 200%"
            description: |
              当前小时成本相比 24 小时平均值增长 {{ $value | printf "%.1f" }}x
              请检查是否有异常任务运行
              
    # =================================================================
    # GPU utilization cost alert
    # =================================================================
    - name: llm.gpu.efficiency
      interval: 1m
      rules:
        - alert: GPUIdleHighCost
          expr: |
            (
              avg(DCGM_FI_DEV_GPU_UTIL{namespace=~"ml-.*|ai-.*"}) < 30
            ) and (
              sum(kubecost_pod_gpu_cost{namespace=~"ml-.*|ai-.*"}) > 0
            )
          for: 1h
          labels:
            severity: warning
          annotations:
            summary: "Low GPU utilization but high cost"
            description: |
              GPU 利用率: {{ $value | printf "%.1f" }}%
              GPU 处于低利用率状态超过 1 小时,造成成本浪费
              建议:
              - 检查任务是否卡住
              - 考虑使用更小的 GPU 实例
              - 启用自动缩容
              
        - alert: GPUMemoryUnderutilized
          expr: |
            (
              avg(DCGM_FI_DEV_FB_USED{namespace=~"ml-.*"}) 
              / 
              avg(DCGM_FI_DEV_FB_TOTAL{namespace=~"ml-.*"})
            ) < 0.5
          for: 2h
          labels:
            severity: info
          annotations:
            summary: "Low GPU memory utilization"
            description: |
              GPU 显存利用率: {{ $value | printf "%.1f" }}%
              建议考虑使用更小显存的 GPU 实例以节省成本
              
    # =================================================================
    # Budget alert
    # =================================================================
    - name: llm.budget
      interval: 15m
      rules:
        - alert: MonthlyBudget75Percent
          expr: |
            (
              sum(kubecost_cluster_cost_total)
              /
              kubecost_budget_monthly_total
            ) > 0.75
          labels:
            severity: warning
          annotations:
            summary: "Monthly budget has been used at 75%"
            description: "Current monthly expenses have reached {{ $value | printf \"%.1f\" }}% of the budget"
            
        - alert: MonthlyBudget90Percent
          expr: |
            (
              sum(kubecost_cluster_cost_total)
              /
              kubecost_budget_monthly_total
            ) > 0.90
          labels:
            severity: critical
          annotations:
            summary: "Monthly budget has been used at 90%"
            description: "Current monthly expenses have reached {{ $value | printf \"%.1f\" }}%, immediate expense control is needed"
            
        - alert: ProjectedOverBudget
          expr: |
            (
              predict_linear(kubecost_cluster_cost_total[7d], 30*24*3600)
              >
              kubecost_budget_monthly_total * 1.1
            )
          for: 1h
          labels:
            severity: warning
          annotations:
            summary: "Expected monthly cost will exceed budget by 10%"
            description: |
              基于过去 7 天趋势,预计月度支出将达 ${{ $value | printf "%.2f" }}
              
    # =================================================================
    # Resource waste alert
    # =================================================================
    - name: llm.waste
      interval: 30m
      rules:
        - alert: UnusedGPUNode
          expr: |
            (
              count(kube_node_status_condition{condition="Ready",status="true"} 
                * on(node) kube_node_labels{label_node_kubernetes_io_instance_type=~".*gpu.*"})
              -
              count(kube_pod_info{pod=~".*gpu.*"} * on(node) kube_node_labels{label_node_kubernetes_io_instance_type=~".*gpu.*"})
            ) > 0
          for: 30m
          labels:
            severity: warning
          annotations:
            summary: "Idle GPU nodes exist"
            description: "There are {{ $value }} GPU nodes running no GPU Pods, suggest resizing"
            
        - alert: OverprovisionedInference
          expr: |
            (
              sum(kube_deployment_spec_replicas{deployment=~".*inference.*"})
              /
              sum(kube_deployment_status_replicas_available{deployment=~".*inference.*"})
            ) > 1.5
          for: 1h
          labels:
            severity: info
          annotations:
            summary: "Inference service may be over-provisioned"
            description: "The number of inference service replicas may be too high, check the HPA configuration"
```


## Cost Optimization Strategies

### Training Cost Optimization Matrix

| Optimization Strategy | Implementation Method | Expected Savings | Complexity | Applicable Scenarios |
|---------|---------|---------|-------|---------|
| **Spot/Affordable Instances** | Karpenter configure priority spot | 60-70% | Low | Interruptible training |
| **Mixed Precision Training** | FP16/BF16 + Dynamic Loss Scaling | 30-40% | Low | Most models |
| **Gradient Accumulation** | Small Batch + Accumulated Update | 20-30% | Low | Memory-limited scenarios |
| **Gradient Checkpointing** | Time for Memory | 20-30% | Medium | Large model training |
| **Early Stopping** | Validation Set Monitoring | 15-25% | Low | Overfitting detection |
| **Model Parallelism** | Tensor/Pipeline Parallelism | - | High | Ultra-large models |
| **Data Parallel Optimization** | FSDP/DeepSpeed | 20-30% | Medium | Multi-GPU training |

### Inference Cost Optimization Matrix

| Optimization Strategy | Implementation Method | Expected Savings | Complexity | Applicable Scenarios |
|---------|---------|---------|-------|---------|
| **Dynamic Batch Processing** | vLLM continuous batching | 60-80% | Medium | High-concurrency inference |
| **Model Quantization** | INT8/INT4 Quantization | 50-75% | Medium | Inference deployment |
| **KV Cache Optimization** | PagedAttention | 30-50% | Low | Long sequence generation |
| **Speculative Decoding** | Speculative Decoding | 20-40% | High | Delay-sensitive scenarios |
| **Auto Scaling** | HPA/KEDA | 30-50% | Low | Large load fluctuations |
| **Semantic Cache** | Semantic Cache | 20-40% | Medium | Frequent Requests |
| **Model Distillation** | Model Distillation | 60-80% | High | Specific Tasks |

### Cost Optimization Configuration Example

```yaml
# cost-optimized-training.yaml
# Optimized training task configuration

apiVersion: batch/v1
kind: Job
metadata:
  name: llama2-finetune-optimized
  namespace: ml-training
  labels:
    team: ml-research
    project: llama2-finetuning
    cost-optimization: enabled
spec:
  backoffLimit: 3
  template:
    metadata:
      labels:
        team: ml-research
        project: llama2-finetuning
        spot-tolerant: "true"
    spec:
      # Prioritize Spot Instances
      nodeSelector:
        node.kubernetes.io/instance-type: p4d.24xlarge
      tolerations:
        - key: "spot"
          operator: "Equal"
          value: "true"
          effect: "NoSchedule"
        - key: "nvidia.com/gpu"
          operator: "Exists"
          effect: "NoSchedule"
          
      # Checkpoint storage (supports interruption recovery)
      volumes:
        - name: checkpoint
          persistentVolumeClaim:
            claimName: training-checkpoint-pvc
        - name: dataset
          persistentVolumeClaim:
            claimName: training-dataset-pvc
            
      containers:
        - name: trainer
          image: pytorch/pytorch:2.1.0-cuda12.1-cudnn8-runtime
          command:
            - python
            - -m
            - torch.distributed.run
            - --nproc_per_node=8
            - train.py
            - --mixed_precision=bf16        # 混合精度
            - --gradient_accumulation=4     # 梯度累积
            - --gradient_checkpointing=true # 梯度检查点
            - --checkpoint_dir=/checkpoints
            - --resume_from_checkpoint=auto # 自动恢复
          env:
            - name: PYTORCH_CUDA_ALLOC_CONF
              value: "max_split_size_mb:512"
          resources:
            limits:
              nvidia.com/gpu: 8
              memory: "640Gi"
              cpu: "96"
            requests:
              nvidia.com/gpu: 8
              memory: "512Gi"
              cpu: "64"
          volumeMounts:
            - name: checkpoint
              mountPath: /checkpoints
            - name: dataset
              mountPath: /data
              
      restartPolicy: OnFailure
      terminationGracePeriodSeconds: 300

---
# cost-optimized-inference.yaml
# Cost-optimized inference service configuration

apiVersion: apps/v1
kind: Deployment
metadata:
  name: llama2-inference-optimized
  namespace: ml-inference
spec:
  replicas: 2
  selector:
    matchLabels:
      app: llama2-inference
  template:
    metadata:
      labels:
        app: llama2-inference
        team: ml-platform
        cost-optimization: enabled
    spec:
      nodeSelector:
        node.kubernetes.io/instance-type: g5.2xlarge  # 使用更小的 GPU
      containers:
        - name: vllm
          image: vllm/vllm-openai:latest
          args:
            - --model=/models/llama2-7b-chat
            - --tensor-parallel-size=1
            - --dtype=float16
            - --quantization=awq              # 启用量化
            - --max-model-len=4096
            - --gpu-memory-utilization=0.9
            - --enable-prefix-caching         # 启用前缀缓存
          resources:
            limits:
              nvidia.com/gpu: 1
              memory: "32Gi"
            requests:
              nvidia.com/gpu: 1
              memory: "24Gi"
          ports:
            - containerPort: 8000

---
# HPA configuration
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: llama2-inference-hpa
  namespace: ml-inference
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: llama2-inference-optimized
  minReplicas: 1
  maxReplicas: 10
  metrics:
    - type: Pods
      pods:
        metric:
          name: vllm_requests_running
        target:
          type: AverageValue
          averageValue: "50"
  behavior:
    scaleDown:
      stabilizationWindowSeconds: 300
      policies:
        - type: Percent
          value: 10
          periodSeconds: 60
    scaleUp:
      stabilizationWindowSeconds: 0
      policies:
        - type: Percent
          value: 100
          periodSeconds: 15
```


## Cost Report Generation

### Automated Report Script

```python
# generate_cost_report.py
# Cost report generation script

import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List
import matplotlib.pyplot as plt
import io
import base64

class CostReportGenerator:
    """Cost Report Generator"""
    
    def __init__(self, kubecost_client, output_dir: str = "/reports"):
        self.kubecost = kubecost_client
        self.output_dir = output_dir
        
    def generate_monthly_report(self, year: int, month: int) -> str:
        """Generate Monthly Cost Report"""
        
        # Get data
        team_costs = self._get_team_costs(f"{year}-{month:02d}")
        project_costs = self._get_project_costs(f"{year}-{month:02d}")
        gpu_costs = self._get_gpu_costs(f"{year}-{month:02d}")
        trends = self._get_cost_trends(f"{year}-{month:02d}")
        
        # Generate report
        report = f"""
# Monthly LLM Cost Report


## Report Information
- **报告期间**: {year}年{month}月
- **生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}


## Executive Summary

| 指标 | 本月值 | 环比变化 | 状态 |
|-----|-------|---------|-----|
| 总成本 | ${team_costs['total']:.2f} | {trends['total_change']:.1f}% | {'⚠️' if trends['total_change'] > 20 else '✅'} |
| GPU 成本 | ${gpu_costs['total']:.2f} | {trends['gpu_change']:.1f}% | {'⚠️' if trends['gpu_change'] > 25 else '✅'} |
| 平均 GPU 利用率 | {gpu_costs['avg_utilization']:.1f}% | - | {'⚠️' if gpu_costs['avg_utilization'] < 50 else '✅'} |


## Team Cost Distribution

{self._format_team_table(team_costs['by_team'])}


## Top 10 Project Costs

{self._format_project_table(project_costs['top_10'])}


## GPU Usage Analysis

### By GPU Type
{self._format_gpu_table(gpu_costs['by_type'])}

### Distribution of GPU Utilization
- 高利用率 (>70%): {gpu_costs['high_util_percent']:.1f}%
- 中等利用率 (30-70%): {gpu_costs['medium_util_percent']:.1f}%
- 低利用率 (<30%): {gpu_costs['low_util_percent']:.1f}%


## Optimization Recommendations

{self._generate_recommendations(team_costs, gpu_costs)}


## Next Month's Forecast

基于当前趋势,预计下月成本: **${trends['next_month_forecast']:.2f}**

---
*Report generated by the LLM Cost Monitoring System*
"""
        
        return report
    
    def _format_team_table(self, data: List[Dict]) -> str:
        """Format the team cost table"""
        header = "| Team | Total Cost | GPU Cost | Ratio |\n|-----|-----------|----------|-----|"
        rows = []
        total = sum(d['total'] for d in data)
        for d in data:
            pct = d['total'] / total * 100 if total > 0 else 0
            rows.append(f"| {d['team']} | ${d['total']:.2f} | ${d['gpu']:.2f} | {pct:.1f}% |")
        return header + "\n" + "\n".join(rows)
    
    def _format_project_table(self, data: List[Dict]) -> str:
        """Format the project cost table"""
        header = "| Project | Cost | GPU Hours | Efficiency |\n|-----|------|--------|-----|"
        rows = []
        for d in data:
            rows.append(f"| {d['project']} | ${d['cost']:.2f} | {d['gpu_hours']:.1f} | {d['efficiency']:.1f}% |")
        return header + "\n" + "\n".join(rows)
    
    def _format_gpu_table(self, data: List[Dict]) -> str:
        """Format the GPU cost table"""
        header = "| GPU Type | Cost | Usage Time | Average Utilization |\n|--------|------|---------|----------|"
        rows = []
        for d in data:
            rows.append(f"| {d['type']} | ${d['cost']:.2f} | {d['hours']:.1f}h | {d['util']:.1f}% |")
        return header + "\n" + "\n".join(rows)
    
    def _generate_recommendations(self, team_costs: Dict, gpu_costs: Dict) -> str:
        """Generate optimization suggestions"""
        recommendations = []
        
        if gpu_costs['avg_utilization'] < 50:
            recommendations.append(
                "1. **Improve GPU Utilization**: Current average utilization is only {:.1f}%, suggest:\n"
                "   - Enable dynamic batch processing\n"
                "   - Use smaller GPU instances\n"
                "   - Configure automatic scaling"
            )
            
        if gpu_costs['low_util_percent'] > 30:
            recommendations.append(
                "2. **Reduce inefficient GPU usage**: {:.1f}% of GPU time is in low utilization state, suggest:\n"
                "   - review long-running tasks\n"
                "   - set GPU idle timeout".format(gpu_costs['low_util_percent'])
            )
            
        return "\n\n".join(recommendations) if recommendations else "Current cost efficiency is good, no special optimization suggestions."
    
    def _get_team_costs(self, period: str) -> Dict:
        # Simulate data retrieval
        return {
            'total': 45000,
            'by_team': [
                {'team': 'ml-research', 'total': 25000, 'gpu': 20000},
                {'team': 'ml-platform', 'total': 15000, 'gpu': 10000},
                {'team': 'data-science', 'total': 5000, 'gpu': 3000},
            ]
        }
    
    def _get_project_costs(self, period: str) -> Dict:
        return {
            'top_10': [
                {'project': 'llama2-finetuning', 'cost': 15000, 'gpu_hours': 500, 'efficiency': 75},
                {'project': 'gpt-inference', 'cost': 10000, 'gpu_hours': 1000, 'efficiency': 85},
            ]
        }
    
    def _get_gpu_costs(self, period: str) -> Dict:
        return {
            'total': 35000,
            'avg_utilization': 62,
            'high_util_percent': 45,
            'medium_util_percent': 35,
            'low_util_percent': 20,
            'by_type': [
                {'type': 'A100-80G', 'cost': 25000, 'hours': 800, 'util': 70},
                {'type': 'A10G', 'cost': 8000, 'hours': 2000, 'util': 55},
                {'type': 'T4', 'cost': 2000, 'hours': 1500, 'util': 45},
            ]
        }
    
    def _get_cost_trends(self, period: str) -> Dict:
        return {
            'total_change': 15.5,
            'gpu_change': 18.2,
            'next_month_forecast': 52000
        }
```


## Version Change Log

| Version | Change Content | Impact |
|-----|---------|------|
| **Kubecost 2.0** | Add GPU Cost Tracking | More Precise LLM Cost Analysis |
| **[[OpenCost|OpenCost]] 1.0** | Graduated from CNCF | Open Source Alternative |
| **v1.28** | Enhance Native GPU Monitoring | Better Device Plugin Support |


## Summary of Best Practices

### Cost Monitoring Checklist

- [ ] Deploy Kubecost or OpenCost
- [ ] Configure DCGM Exporter to Monitor GPUs
- [ ] Establish a cost tagging standard and enforce it
- [ ] Configure cost alert rules
- [ ] Set up team/project budgets
- [ ] Generate cost reports regularly
- [ ] Continuously optimize high-cost workloads

### Key Monitoring Metrics

- `kubecost_cluster_cost_total` - Total Cluster Cost
- `kubecost_pod_gpu_cost` - Pod GPU Cost
- `DCGM_FI_DEV_GPU_UTIL` - GPU Utilization
- `DCGM_FI_DEV_FB_USED` - GPU Memory Usage

---

**References**:
- [Kubecost Documentation](https://docs.kubecost.com/)
- [OpenCost Project](https://www.opencost.io/)
- [FinOps Foundation](https://www.finops.org/)

---


## Obsidian Documentation

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- index.md|Domain-11 AI Infrastructure — Open Source Project Index]]
- AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management

## See Also

- 21-multimodal-models
- 22-llm-privacy-security
- 24-llm-model-versioning
- 25-llm-observability

## Related

- [[domain-19-landscape-references/topic-index/ai-gpu-index.md|AI / GPU Infrastructure Knowledge Graph Index]]


<!-- risk-assessed -->
