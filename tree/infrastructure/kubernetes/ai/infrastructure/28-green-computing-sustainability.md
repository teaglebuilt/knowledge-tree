---
title: 28 - AI Green Computing and Sustainability
description: '## one,AI Green Computing Panorama Architecture'
summary: 'Level 4: Intelligent Optimization'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- scheduler
- prometheus
- grafana
- istio
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
- AI Green Computing and Sustainability is what
- How AI Green Computing and Sustainability
- Kubernetes 11 ai infra best practices
trigger_keywords:
- AI Green Computing and Sustainability
- ai
- infra
prerequisites:
- kubectl-basics
- helm-basics
- service-mesh-basics
- prometheus-basics
- monitoring-basics
- ebpf-basics
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
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/28-green-computing-sustainability.md
---

> **Production Environment Security Tips**
>
> This document contains executable operational commands. Please confirm before execution: whether the target cluster and Namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# 28 - AI Green Computing and Sustainable Development

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **AI Stack Version**: PyTorch 2.1+ | **Last Updated**: 2026-02 | **Quality Level**: Expert


## 1. Overall Architecture of AI Green Computing

### 1.1 Green AI Ecosystem

```
┌─────────────────────────────────────────────────────────────────────────┐
│                       Green AI Ecosystem Architecture                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  🌱 Green Energy Layer (Green Energy Layer)                                    │
│  ├─ Renewable Energy: Wind, Solar, Hydroelectricity                                      │
│  ├─ Green Data Center: LEED Certification, PUE < 1.2                                   │
│  ├─ Carbon Footprint Tracking: Real-time Carbon Emission Monitoring                                          │
│  └─ Energy Procurement: Green Power Certificates (RECs)                                        │
│                                                                         │
│  ⚡ Energy Monitoring Layer (Energy Monitoring Layer)                               │
│  ├─ Hardware-Level Monitoring: RAPL, IPMI Sensors                                        │
│  ├─ Software-Level Monitoring: Kepler, eBPF                                            │
│  ├─ Application-Level Monitoring: Model Energy Consumption Analysis │
│  └─ Cost-Level Monitoring: Energy Cost Attribution                                            │
│                                                                         │
│  🧠 AI Optimization Layer (AI Optimization Layer)                                   │
│  ├─ Model Compression: Quantization, Distillation, Pruning                                          │
│  ├─ Algorithm Optimization: Efficient Training Algorithms                                              │
│  ├─ Resource Scheduling: Carbon-Aware Scheduler                                              │
│  └─ Architecture Optimization: Serverless, Edge Computing                                      │
│                                                                         │
│  📊 Governance & Management Layer (Governance & Management Layer)                         │
│  ├─ Green Policy: Corporate ESG Goals                                               │
│  ├─ Compliance Regulation: Carbon Emission Regulations Follow-up                                            │
│  ├─ Performance Evaluation: Green KPI Indicators                                               │
│  └─ Continuous Improvement: Loop Optimization Mechanism                                      │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Energy Consumption Characteristics Analysis of AI Workloads

| AI Task Type | Energy Characteristics | Main Influencing Factors | Optimization Potential | Green Strategy |
|-----------|---------|-------------|---------|---------|
| **Large Model Training** | High energy consumption, long duration | Model size, number of training epochs | 40-60% | Mixed precision, distributed training |
| **Model Inference** | Moderate energy consumption, high frequency | Number of requests, batch size | 30-50% | Model compression, cache optimization |
| **Data Processing** | Low to moderate energy consumption | Data volume, algorithm complexity | 20-40% | Vectorized computing, parallel processing |
| **Experiment Management** | Low energy consumption, intermittent | Frequency of experiments, resource allocation | 10-30% | Resource recycling, demand-based allocation |


## 2. Enterprise-Level Green Computing Implementation Framework

### 2.1 Green Computing Maturity Model

```
Level 1: Basic Monitoring (Basic Monitoring)
├─ Deploy basic energy consumption monitoring tools
├─ Establish baseline data for energy consumption
├─ Set up basic alert mechanisms
└─ Goal: Visibility established

Level 2: Resource Optimization (Resource Optimization)
├─ Implement auto-scaling
├─ Enable resource right-sizing
├─ Optimize scheduling strategies
└─ Goal: Resource utilization improved by 30%

Level 3: Green Scheduling (Green Scheduling)
├─ Deploy carbon-aware schedulers
├─ Implement spatial-temporal load shifting
├─ Optimize energy procurement strategies
└─ Goal: Carbon emissions reduced by 20%

Level 4: Intelligent Optimization (Intelligent Optimization)
├─ AI-driven energy optimization
├─ Predictive resource management
├─ Adaptive green strategies
└─ Goal: End-to-end efficiency improved by 50%

Level 5: Circular Economy
├─ Full lifecycle carbon management
├─ Sustainable supply chain integration
├─ Achieve carbon neutrality target
└─ Goal: Carbon-neutral operations
```

### 2.2 Green Computing Technology Stack

```yaml
# green-computing-tech-stack.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: green-computing-technology-stack
  namespace: sustainability
data:
  tech-stack.yaml: |
    monitoring_layer:
      hardware_monitoring:
        - name: "Intel RAPL"
          purpose: "Hardware energy measurement"
          integration: "Kernel module"
          metrics: ["power_pkg", "power_cores", "power_gpu"]
        
        - name: "NVIDIA NVML"
          purpose: "GPU energy monitoring"
          integration: "Driver API"
          metrics: ["power_usage", "temperature", "utilization"]
        
        - name: "IPMI Sensors"
          purpose: "Server-level monitoring"
          integration: "BMC interface"
          metrics: ["watts", "temperature", "fan_speed"]
      
      software_monitoring:
        - name: "Kepler"
          purpose: "Container-level energy allocation"
          integration: "eBPF + Prometheus"
          metrics: ["container_joules", "process_energy"]
        
        - name: "Green Metrics Collector"
          purpose: "Application-level energy analysis"
          integration: "Sidecar injection"
          metrics: ["model_energy", "request_energy"]
    
    optimization_layer:
      model_optimization:
        - name: "Model Compression Toolkit"
          techniques: ["quantization", "pruning", "distillation"]
          tools: ["Intel Neural Compressor", "NVIDIA TensorRT"]
          savings: "30-60% energy reduction"
        
        - name: "Efficient Training"
          techniques: ["mixed_precision", "gradient_accumulation", "checkpointing"]
          tools: ["PyTorch AMP", "DeepSpeed", "FairScale"]
          savings: "40-70% training energy"
      
      resource_optimization:
        - name: "Carbon-Aware Scheduler"
          features: ["time_shifting", "region_shifting", "load_balancing"]
          integration: "Kubernetes scheduler extender"
          savings: "20-40% carbon footprint"
        
        - name: "Green Load Balancer"
          features: ["energy_routing", "server_selection", "request_batching"]
          integration: "Envoy/Istio filter"
          savings: "15-30% network energy"
    
    governance_layer:
      policy_management:
        - name: "Green Policy Engine"
          rules: ["carbon_budget", "energy_quota", "efficiency_target"]
          enforcement: "OPA Gatekeeper"
          compliance: "Real-time validation"
        
        - name: "Sustainability Dashboard"
          features: ["carbon_footprint", "energy_efficiency", "roi_analysis"]
          visualization: "Grafana + custom panels"
          reporting: "Automated ESG reports"
```


## 3. Advanced Energy Consumption Monitoring and Analysis

### 3.1 Multi-Dimensional Energy Consumption Monitoring System

```python
# advanced-energy-monitoring.py
import asyncio
import time
from typing import Dict, List, Tuple, Optional
import numpy as np
from dataclasses import dataclass
import json
import logging

@dataclass
class EnergyMetrics:
    timestamp: float
    cpu_energy_joules: float
    gpu_energy_joules: float
    memory_energy_joules: float
    network_energy_joules: float
    storage_energy_joules: float
    total_energy_joules: float
    carbon_emissions_kg: float
    utilization_rates: Dict[str, float]

class AdvancedEnergyMonitor:
    def __init__(self, cluster_name: str = "ai-cluster"):
        self.cluster_name = cluster_name
        self.metrics_history: List[EnergyMetrics] = []
        self.carbon_intensity_map = {
            "cn-hangzhou": 0.581,  # kg CO2e/kWh
            "eu-west-1": 0.276,
            "us-west-2": 0.417,
            "green-region": 0.050  # 可再生能源区域
        }
        self.logger = logging.getLogger(__name__)
        
    async def collect_hardware_metrics(self) -> Dict[str, float]:
        """collect hardware-level energy metrics"""
        metrics = {}
        
        # simulate collecting CPU energy from RAPL interface
        try:
            # actual implementation would call /sys/class/powercap/intel-rapl/
            metrics['cpu_energy'] = await self._read_rapl_energy('cpu')
        except Exception as e:
            self.logger.warning(f"Failed to read CPU energy: {e}")
            metrics['cpu_energy'] = 0.0
            
        # collect GPU energy
        try:
            metrics['gpu_energy'] = await self._read_nvml_power()
        except Exception as e:
            self.logger.warning(f"Failed to read GPU energy: {e}")
            metrics['gpu_energy'] = 0.0
            
        # collect energy from other components
        metrics.update({
            'memory_energy': await self._estimate_memory_energy(),
            'network_energy': await self._calculate_network_energy(),
            'storage_energy': await self._calculate_storage_energy()
        })
        
        return metrics
    
    async def _read_rapl_energy(self, component: str) -> float:
        """read RAPL energy data"""
        # simplified simulation implementation
        base_values = {
            'cpu': 150.0,  # Joules
            'cores': 120.0,
            'uncore': 30.0,
            'dram': 25.0
        }
        # add random fluctuations to simulate real environment
        noise = np.random.normal(0, 5)
        return base_values.get(component, 0.0) + noise
    
    async def _read_nvml_power(self) -> float:
        """read NVIDIA GPU power"""
        # simulate NVIDIA-SMI data
        power_draw_watts = 250.0 + np.random.normal(0, 20)
        # convert to energy (assuming sample interval is 1 second)
        return power_draw_watts
    
    async def _estimate_memory_energy(self) -> float:
        """estimate memory energy consumption"""
        # estimate based on memory usage
        memory_gb = 64.0  # 假设64GB内存
        energy_per_gb_per_second = 0.05  # Joules/GB/second
        return memory_gb * energy_per_gb_per_second
    
    async def _calculate_network_energy(self) -> float:
        """calculate network energy consumption"""
        # estimate based on network traffic
        bytes_transferred = 1000000.0  # 1MB
        energy_per_gb = 0.002  # Joules/GB (典型网络设备)
        return (bytes_transferred / 1e9) * energy_per_gb
    
    async def _calculate_storage_energy(self) -> float:
        """calculate storage energy consumption"""
        # estimate based on I/O operations
        io_operations = 1000
        energy_per_operation = 0.001  # Joules/operation
        return io_operations * energy_per_operation
    
    def calculate_carbon_emissions(self, total_energy_joules: float, region: str = "cn-hangzhou") -> float:
        """calculate carbon emissions"""
        energy_kwh = total_energy_joules / 3600000  # 转换为kWh
        carbon_intensity = self.carbon_intensity_map.get(region, 0.581)
        return energy_kwh * carbon_intensity
    
    async def monitor_ai_workload_energy(self, model_name: str, batch_size: int) -> EnergyMetrics:
        """monitor AI workload energy consumption"""
        start_time = time.time()
        
        # collect energy at the start of monitoring
        start_metrics = await self.collect_hardware_metrics()
        
        # Simulate AI inference process
        await asyncio.sleep(2)  # 模拟推理时间
        
        # Collect end-of-process energy consumption
        end_metrics = await self.collect_hardware_metrics()
        
        # Calculate difference
        energy_diff = {
            'cpu': end_metrics['cpu_energy'] - start_metrics['cpu_energy'],
            'gpu': end_metrics['gpu_energy'] - start_metrics['gpu_energy'],
            'memory': end_metrics['memory_energy'] - start_metrics['memory_energy'],
            'network': end_metrics['network_energy'] - start_metrics['network_energy'],
            'storage': end_metrics['storage_energy'] - start_metrics['storage_energy']
        }
        
        total_energy = sum(energy_diff.values())
        carbon_emissions = self.calculate_carbon_emissions(total_energy)
        
        # Calculate utilization
        utilization_rates = {
            'cpu_utilization': 75.0 + np.random.normal(0, 5),
            'gpu_utilization': 85.0 + np.random.normal(0, 3),
            'memory_utilization': 60.0 + np.random.normal(0, 8)
        }
        
        metrics = EnergyMetrics(
            timestamp=start_time,
            cpu_energy_joules=energy_diff['cpu'],
            gpu_energy_joules=energy_diff['gpu'],
            memory_energy_joules=energy_diff['memory'],
            network_energy_joules=energy_diff['network'],
            storage_energy_joules=energy_diff['storage'],
            total_energy_joules=total_energy,
            carbon_emissions_kg=carbon_emissions,
            utilization_rates=utilization_rates
        )
        
        self.metrics_history.append(metrics)
        return metrics
    
    def generate_energy_report(self, time_window_hours: int = 24) -> Dict:
        """Generate energy report"""
        if not self.metrics_history:
            return {"error": "No metrics data available"}
        
        # Filter data within the time window
        cutoff_time = time.time() - (time_window_hours * 3600)
        recent_metrics = [m for m in self.metrics_history if m.timestamp >= cutoff_time]
        
        if not recent_metrics:
            return {"error": "No recent metrics data"}
        
        # Calculate statistical information
        total_energy = sum(m.total_energy_joules for m in recent_metrics)
        total_carbon = sum(m.carbon_emissions_kg for m in recent_metrics)
        avg_utilization = np.mean([m.utilization_rates['gpu_utilization'] for m in recent_metrics])
        
        # Analyze energy consumption by component
        component_energy = {
            'cpu': sum(m.cpu_energy_joules for m in recent_metrics),
            'gpu': sum(m.gpu_energy_joules for m in recent_metrics),
            'memory': sum(m.memory_energy_joules for m in recent_metrics),
            'network': sum(m.network_energy_joules for m in recent_metrics),
            'storage': sum(m.storage_energy_joules for m in recent_metrics)
        }
        
        return {
            "report_period_hours": time_window_hours,
            "total_energy_consumed_kwh": total_energy / 3600000,
            "total_carbon_emissions_kg": total_carbon,
            "average_gpu_utilization_percent": avg_utilization,
            "energy_by_component_kwh": {k: v/3600000 for k, v in component_energy.items()},
            "efficiency_score": self._calculate_efficiency_score(recent_metrics),
            "recommendations": self._generate_recommendations(recent_metrics)
        }
    
    def _calculate_efficiency_score(self, metrics: List[EnergyMetrics]) -> float:
        """Calculate efficiency score (0-100)"""
        if not metrics:
            return 0.0
            
        # Based on utilization and energy-to-utilization ratio calculate
        avg_utilization = np.mean([m.utilization_rates['gpu_utilization'] for m in metrics])
        avg_energy_per_request = np.mean([m.total_energy_joules for m in metrics])
        
        # Simplified scoring algorithm
        utilization_score = min(avg_utilization / 100.0, 1.0) * 50
        energy_efficiency_score = max(0, (1000 - avg_energy_per_request) / 1000) * 50
        
        return utilization_score + energy_efficiency_score
    
    def _generate_recommendations(self, metrics: List[EnergyMetrics]) -> List[str]:
        """Generate optimization suggestions"""
        recommendations = []
        
        if not metrics:
            return recommendations
            
        avg_gpu_util = np.mean([m.utilization_rates['gpu_utilization'] for m in metrics])
        avg_cpu_util = np.mean([m.utilization_rates['cpu_utilization'] for m in metrics])
        
        if avg_gpu_util < 60:
            recommendations.append("GPU utilization is low, consider increasing batch size or merging small tasks")
        
        if avg_cpu_util < 50:
            recommendations.append("CPU utilization is insufficient, check for I/O bottlenecks")
        
        # Check energy trend
        if len(metrics) > 10:
            recent_energy = np.mean([m.total_energy_joules for m in metrics[-5:]])
            older_energy = np.mean([m.total_energy_joules for m in metrics[:5]])
            if recent_energy > older_energy * 1.1:
                recommendations.append("Energy consumption is rising, suggest checking resource allocation strategies")
        
        return recommendations

# Usage Example
async def main():
    monitor = AdvancedEnergyMonitor(cluster_name="ai-production-cluster")
    
    # Monitor multiple AI workloads
    workloads = [
        ("llama2-7b-inference", 32),
        ("stable-diffusion-xl", 8),
        ("whisper-large", 16)
    ]
    
    for model_name, batch_size in workloads:
        metrics = await monitor.monitor_ai_workload_energy(model_name, batch_size)
        print(f"Model: {model_name}")
        print(f"Total Energy: {metrics.total_energy_joules:.2f} J")
        print(f"Carbon Emissions: {metrics.carbon_emissions_kg:.4f} kg")
        print("---")
    
    # Generate report
    report = monitor.generate_energy_report(time_window_hours=1)
    print("\nEnergy Report:")
    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
```

### 3.2 Carbon Sensing Scheduler Implementation

```yaml
# carbon-aware-scheduler.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: carbon-aware-scheduler-config
  namespace: kube-system
data:
  scheduler-policy.yaml: |
    {
      "kind": "Policy",
      "apiVersion": "v1",
      "predicates": [
        {
          "name": "CarbonAwarePredicate",
          "argument": {
            "carbonDataEndpoint": "http://carbon-intensity-service:8080/api/v1/intensity",
            "maxCarbonIntensity": 400,  # gCO2/kWh
            "fallbackRegion": "green-region"
          }
        },
        {
          "name": "MatchInterPodAffinity"
        },
        {
          "name": "CheckVolumeBinding"
        }
      ],
      "priorities": [
        {
          "name": "CarbonFootprintPriority",
          "weight": 5,
          "argument": {
            "carbonWeight": 0.7,
            "performanceWeight": 0.3
          }
        },
        {
          "name": "LeastRequestedPriority",
          "weight": 3
        },
        {
          "name": "BalancedResourceAllocation",
          "weight": 1
        }
      ]
    }

---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: carbon-intensity-service
  namespace: monitoring
spec:
  replicas: 2
  selector:
    matchLabels:
      app: carbon-intensity
  template:
    metadata:
      labels:
        app: carbon-intensity
    spec:
      containers:
      - name: carbon-intensity-api
        image: company/carbon-intensity-service:latest
        ports:
        - containerPort: 8080
        env:
        - name: CARBON_DATA_SOURCE
          value: "electricitymaps"
        - name: DEFAULT_REGION
          value: "cn-hangzhou"
        - name: UPDATE_INTERVAL_MINUTES
          value: "15"
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
          limits:
            cpu: "500m"
            memory: "256Mi"
```


## 4. Green AI Best Practices and Case Studies


## Green Computing Metrics

| Metric | Description | Unit | Monitoring Method |
|-----|------|------|---------|
| **Energy Consumption** | Total energy consumption | kWh | Kepler/Cloud Monitoring |
| **Carbon Emission** | CO2 emissions | kg CO2e | Calculation formula |
| **PUE** | Data center efficiency | Ratio | Data center metrics |
| **Resource Utilization** | CPU/memory usage rate | % | Prometheus |
| **Idle Resources** | Unused resources | Cores/GB | Resource audit |


## Kepler(Kubernetes Energy Efficiency)

```yaml
# Kepler deployment
# helm repo add kepler https://sustainable-computing-io.github.io/kepler-helm-chart
# helm install kepler kepler/kepler -n kepler --create-namespace

# Kepler metrics
# kepler_container_joules_total - container energy consumption (joules)
# kepler_node_core_joules_total - node CPU energy consumption
# kepler_node_dram_joules_total - node DRAM energy consumption
# kepler_node_platform_joules_total - node total energy consumption
```

```yaml
# Kepler DaemonSet configuration
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: kepler
  namespace: kepler
spec:
  selector:
    matchLabels:
      app: kepler
  template:
    metadata:
      labels:
        app: kepler
    spec:
      containers:
      - name: kepler
        image: quay.io/sustainable_computing_io/kepler:latest
        securityContext:
          privileged: true
        ports:
        - containerPort: 9102
          name: metrics
        volumeMounts:
        - name: lib-modules
          mountPath: /lib/modules
        - name: tracing
          mountPath: /sys/kernel/debug
        - name: proc
          mountPath: /proc
      volumes:
      - name: lib-modules
        hostPath:
          path: /lib/modules
      - name: tracing
        hostPath:
          path: /sys/kernel/debug
      - name: proc
        hostPath:
          path: /proc
```


## Energy Consumption Optimization Strategies

| Strategy | Description | Implementation Method | Savings Potential |
|-----|------|---------|---------|
| **Right-sizing Resources** | Reduce over-provisioning | VPA/Resource Audit | 20-40% |
| **Auto-scaling** | Use resources on-demand | HPA/CA | 20-50% |
| **Node Consolidation** | Merge underutilized nodes | Descheduler | 10-30% |
| **Spot Instances** | Use idle resources | Node pool configuration | - |
| **Scheduler Optimization** | Optimize Pod distribution | Scheduler policies | 5-15% |
| **Close idle nodes** | Reduce to zero | CA configuration | Large change |


## Descheduler Node Integration

```yaml
# Descheduler strategy
apiVersion: descheduler/v1alpha1
kind: DeschedulerPolicy
profiles:
- name: default
  pluginConfig:
  - name: LowNodeUtilization
    args:
      thresholds:
        cpu: 20
        memory: 20
        pods: 20
      targetThresholds:
        cpu: 50
        memory: 50
        pods: 50
      numberOfNodes: 3  # 至少3个低利用节点才触发
  - name: RemovePodsHavingTooManyRestarts
    args:
      podRestartThreshold: 100
      includingInitContainers: true
  - name: RemoveDuplicates
  plugins:
    balance:
      enabled:
      - LowNodeUtilization
      - RemoveDuplicates
    deschedule:
      enabled:
      - RemovePodsHavingTooManyRestarts
```


## Carbon Emission Calculation

```yaml
# Carbon emission formula
# Carbon = Energy (kWh) × Carbon Intensity (kg CO2e/kWh)

# Carbon emissions coefficients for each region (example)
# Average for China: 0.581 kg CO2e/kWh
# Average for United States: 0.417 kg CO2e/kWh
# Average for Europe: 0.276 kg CO2e/kWh
# For renewable energy: ~0 kg CO2e/kWh

# Prometheus query example
# Hourly container energy consumption (Wh)
sum(increase(kepler_container_joules_total[1h])) / 3600
# Estimate carbon emissions (kg CO2e)
sum(increase(kepler_container_joules_total[24h])) / 3600000 * 0.581
```


## Green Scheduling

```yaml
# Carbon-aware scheduler configuration (example concept)
apiVersion: v1
kind: ConfigMap
metadata:
  name: carbon-aware-scheduler-config
data:
  config.yaml: |
    regions:
      - name: cn-hangzhou
        carbonIntensity: 0.6
      - name: cn-shanghai
        carbonIntensity: 0.58
      - name: eu-west-1
        carbonIntensity: 0.25
    scheduling:
      preferLowCarbon: true
      carbonThreshold: 0.4
```


## Resource Utilization Optimization

```yaml
# Resource utilization alert rules
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: resource-efficiency
spec:
  groups:
  - name: efficiency
    rules:
    # Alert for underutilized nodes
    - alert: NodeLowUtilization
      expr: |
        (1 - avg by(node) (rate(node_cpu_seconds_total{mode="idle"}[5m]))) < 0.2
        and
        (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) < 0.3
      for: 1h
      labels:
        severity: info
      annotations:
        summary: "Node {{ $labels.node }} resource utilization is low"
    
    # Over-provisioned Pod alert
    - alert: PodOverProvisioned
      expr: |
        (sum by(namespace, pod) (container_cpu_usage_seconds_total) / 
         sum by(namespace, pod) (kube_pod_container_resource_requests{resource="cpu"})) < 0.2
      for: 24h
      labels:
        severity: info
      annotations:
        summary: "Pod {{ $labels.pod }} CPU usage is persistently below the requested 20%"
```


## Green Operations Checklist

| Item | Target | Current Status | Optimization Suggestions |
|-------|------|---------|---------|
| **Average CPU Utilization** | >50% | Check | Enable HPA/VPA |
| **Average Memory Utilization** | >60% | Check | Resource Audit |
| **Spot Instance Ratio** | >30% | Check | Increase Spot Nodes |
| **Idle Nodes** | 0 | Check | Configure to reduce to zero |
| **Over-provisioned Pods** | <10% | Check | VPA Adjustments |
| **Energy Consumption Monitoring** | Enabled | Check | Deploy Kepler |


## Green Operations Report Template

| Function | Description | Configuration Method |
|-----|------|---------|
| **Carbon Ledger** | Track carbon emissions | Cloud Billing |
| **Green Instances** | Renewable energy data center | Choose region |
| **Spot Instances** | Utilize idle resources | Node pool configuration |
| **Elastic Scaling** | On-demand use | ESS configuration |


## Alibaba Cloud Green Computing

```markdown
# Monthly green operations report


## Summary
- 总能耗: XXX kWh
- 碳排放: XXX kg CO2e
- 平均资源利用率: XX%


## Results
- 节点整合: 减少X个节点
- 能耗节省: XX%
- 成本节省: XX%


## Suggestions for Improvement
1. 增加Spot实例比例
2. 优化低利用率工作负载
3. 考虑迁移到绿色数据中心
```

---

**Green Principles**: Monitor energy consumption, optimize utilization, continuously improve

---

**Table bottom mark**: Kusheet Project, author Allen Galler (allengaller@gmail.com)

---


## Obsidian Related Documentation

- domain-11-ai-infra KUDIG Database — Global MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- index.md|Domain-11 AI Infrastructure — Open Source Project Index]]
- Domain-11 AI Infrastructure Architecture
- 132 - AI/ML Workload Operations (AI/ML Workloads Operations)
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management

## See Also

- 26-cost-optimization-overview
- 27-cost-management-kubecost
- 29-alibaba-cloud-integration
- 30-ai-security-compliance


<!-- risk-assessed -->
