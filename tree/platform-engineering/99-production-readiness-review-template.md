---
title: 12-Automated Operations Toolchain
description: 'title: 12-Automated Operations Toolchain'
summary: 'title: 12-Automated Operations Toolchain'
category: general
tags:
- k8s
- production
- best-practice
- kubelet
- prometheus
- helm
- containerd
- docker
- ingress
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All engineers
estimated_read_time: 25min
intent_queries:
- What is automated-operations-toolchain?
- How to use automated-operations-toolchain
- Best practices for automated-operations-toolchain
trigger_keywords:
- Automated operations toolchain
- platform
- engineering
prerequisites:
- kubectl-basics
- platform-engineering-basics
- helm-basics
- prometheus-basics
- iac-basics
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./12-automated-operations-toolchain.md
original_language: Chinese
---

> **Production Environment Security Alert**
>
> This document contains directly executable operations commands. Before execution, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether the commands have been validated in non-production environments. Command risk levels are marked: 🔴 High risk (may cause data loss or service disruption), 🟡 Medium risk (modifies cluster state but is usually reversible), 🟢 Low risk/Read-only (information collection, no side effects).




title: 12-Automated Operations Toolchain
description: '# 12-Automated Operations Toolchain'
category: production-operations
tags:
- k8s
- production
- operations
- best-practices
- [[kubelet|kubelet]]
- [[Prometheus|prometheus]]
- [[Helm|helm]]
- [[containerd|containerd]]
- docker
- ingress
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- SRE
- Operations Engineer
- Platform Engineer
estimated_read_time: 5min
intent_queries:
- What is automated operations toolchain
- How to use automated operations toolchain
- Kubernetes 18 production operations best practices
trigger_keywords:
- Automated operations toolchain
- production
- operations
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

# 12-Automated Operations Toolchain

> **Applicable Scope**: Kubernetes v1.25-v1.32 | **Maintenance Status**: 🔧 Continuously Updated | **Expert Level**: ⭐⭐⭐⭐⭐

<!-- chunk: 📋 Overview -->## 📋 Overview

An automated operations toolchain is key to improving operational efficiency and system reliability. This document provides detailed guidance on automated operations tools and best practices in Kubernetes environments.

<!-- chunk: 🛠️ Core Tool Components -->## 🛠️ Core Tool Components

## Infrastructure Automation

## 1. Ansible Operations Playbook
```yaml
# Kubernetes node initialization playbook
---
- name: Initialize Kubernetes Nodes
  hosts: k8s_nodes
  become: yes
  vars:
    kubernetes_version: "1.28.2"
    container_runtime: "containerd"
    pod_network_cidr: "10.244.0.0/16"
  
  tasks:
  - name: Install container runtime
    apt:
      name: "{{ container_runtime }}"
      state: present
    when: ansible_os_family == "Debian"
  
  - name: Configure containerd
    copy:
      src: files/containerd-config.toml
      dest: /etc/containerd/config.toml
      owner: root
      group: root
      mode: '0644'
  
  - name: Install Kubernetes components
    apt:
      name:
        - kubelet={{ kubernetes_version }}-00
        - kubeadm={{ kubernetes_version }}-00
        - kubectl={{ kubernetes_version }}-00
      state: present
      update_cache: yes
  
  - name: Hold Kubernetes packages
    dpkg_selections:
      name: "{{ item }}"
      selection: hold
    loop:
      - kubelet
      - kubeadm
      - kubectl
  
  - name: Enable and start services
    systemd:
      name: "{{ item }}"
      enabled: yes
      state: started
    loop:
      - containerd
      - kubelet
```

## 2. Node Health Check Script
``` bash
# 🟢 Low risk: Read-only/information collection, typically no side effects
#!/bin/bash
# Node health check script

NODE_NAME=$(hostname)
CHECK_TIME=$(date -Iseconds)
HEALTH_STATUS="healthy"

# Check critical service status
check_services() {
    local services=("kubelet" "containerd" "docker")
    for service in "${services[@]}"; do
        if ! systemctl is-active --quiet "$service"; then
            echo "Service $service is not running"
            HEALTH_STATUS="unhealthy"
        fi
    done
}

# Check disk space
check_disk_space() {
    local threshold=85
    local usage=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
    
    if [ "$usage" -gt "$threshold" ]; then
        echo "Disk usage is ${usage}% (threshold: ${threshold}%)"
        HEALTH_STATUS="warning"
    fi
}

# Check memory usage
check_memory() {
    local threshold=90
    local usage=$(free | awk 'NR==2{printf "%.0f", $3*100/$2}')
    
    if [ "$usage" -gt "$threshold" ]; then
        echo "Memory usage is ${usage}% (threshold: ${threshold}%)"
        HEALTH_STATUS="warning"
    fi
}

# Check Kubernetes node status
check_k8s_node() {
    if ! kubectl get node "$NODE_NAME" -o jsonpath='{.status.conditions[?(@.type=="Ready")].status}' | grep -q "True"; then
        echo "Kubernetes node is not ready"
        HEALTH_STATUS="unhealthy"
    fi
}

# Execute checks
check_services
check_disk_space
check_memory
check_k8s_node

# Report health status
report_health() {
    local payload=$(jq -n \
        --arg node "$NODE_NAME" \
        --arg status "$HEALTH_STATUS" \
        --arg time "$CHECK_TIME" \
        '{
            node: $node,
            status: $status,
            timestamp: $time,
            checks: {
                services: "passed",
                disk_space: "passed",
                memory: "passed",
                k8s_node: "passed"
            }
        }')
    
    curl -X POST -H "Content-Type: application/json" \
        -d "$payload" \
        "http://monitoring-server/health"
}

report_health
```
## Application Deployment Automation

## 1. Helm Deployment Script

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend using --dry-run or diff to confirm first
> - `helm upgrade/install`: Deploy/upgrade release
> - `kubectl apply/create/replace`: Create/modify cluster resources

``` bash
# 🟡 Medium risk: Modifies cluster/resource state, please confirm target and impact scope before execution
#!/bin/bash
# Automated Helm deployment script

set -e

APP_NAME="$1"
NAMESPACE="$2"
VALUES_FILE="$3"
CHART_REPO="$4"
CHART_NAME="$5"
CHART_VERSION="$6"

# Validate parameters
validate_params() {
    if -z "$APP_NAME"; then
        echo "Usage: $0 <app-name> <namespace> <values-file> [chart-repo] [chart-name] [chart-version]"
        exit 1
    fi
    
    if ! -f "$VALUES_FILE"; then
        echo "Values file $VALUES_FILE not found"
        exit 1
    fi
}

# Initialize Helm
init_helm() {
    echo "Initializing Helm..."
    helm repo add stable https://charts.helm.sh/stable
    if -n "$CHART_REPO"; then
        helm repo add custom "$CHART_REPO"
    fi
    helm repo update
}

# Deploy application
deploy_application() {
    echo "Deploying $APP_NAME to namespace $NAMESPACE..."
    
    # Create namespace
    kubectl create namespace "$NAMESPACE" --dry-run=client -o yaml | kubectl apply -f -
    
    # Deploy application
    local helm_args=(
        "--namespace" "$NAMESPACE"
        "--values" "$VALUES_FILE"
        "--timeout" "10m"
        "--wait"
    )
    
    if -n "$CHART_VERSION"; then
        helm_args+=("--version" "$CHART_VERSION")
    fi
    
    if -n "$CHART_NAME" && -n "$CHART_REPO"; then
        helm upgrade --install "$APP_NAME" "$CHART_REPO/$CHART_NAME" "${helm_args[@]}"
    else
        helm upgrade --install "$APP_NAME" "./charts/$APP_NAME" "${helm_args[@]}"
    fi
}

# Verify deployment
verify_deployment() {
    echo "Verifying deployment..."
    
    # Wait for Pod readiness
    kubectl wait --for=condition=ready pod -l app.kubernetes.io/name="$APP_NAME" \
        --namespace "$NAMESPACE" --timeout=300s
    
    # Check service status
    if kubectl get svc -l app.kubernetes.io/name="$APP_NAME" --namespace "$NAMESPACE" >/dev/null 2>&1; then
        echo "Service is available"
    else
        echo "Warning: No service found for $APP_NAME"
    fi
    
    # Run health check
    if -f "scripts/health-check-$APP_NAME.sh"; then
        bash "scripts/health-check-$APP_NAME.sh" "$NAMESPACE"
    fi
}

# Rollback mechanism
rollback_on_failure() {
    echo "Deployment failed, rolling back..."
    helm rollback "$APP_NAME" --namespace "$NAMESPACE"
    exit 1
}

# Main execution flow
main() {
    trap rollback_on_failure ERR
    
    validate_params
    init_helm
    deploy_application
    verify_deployment
    
    echo "Deployment completed successfully!"
}

main "$@"
```
## 2. Blue-Green Deployment Script

> ⚠️ **🔴 Catastrophic Operation** — Contains irreversible commands, must satisfy change window + dual approval + pre-backup + rollback plan before execution
> - `helm uninstall`: Delete release and all associated resources
> - `helm upgrade/install`: Deploy/upgrade release
> - `kubectl edit/patch`: Modify running resources

> **🔴 High Risk Operation Warning**
>
> The following commands are irreversible or high-impact operations. Before execution, please confirm:
> - Critical data and configurations have been backed up
> - Operating within an approved change window
> - You have authorization from relevant stakeholders
> - Rollback or recovery plan is in place
> - Target cluster, Namespace, node/resource names are correct

``` bash
# 🔴 High risk: May cause data loss or service disruption, requires backup, change approval, and rollback plan
#!/bin/bash
# Blue-green deployment automation script

set -e

APP_NAME="$1"
NAMESPACE="$2"
NEW_VERSION="$3"

# Deploy new version (green environment)
deploy_green() {
    echo "Deploying new version to green environment..."
    
    helm upgrade --install "${APP_NAME}-green" "./charts/$APP_NAME" \
        --namespace "$NAMESPACE" \
        --set image.tag="$NEW_VERSION" \
        --set service.name="${APP_NAME}-green" \
        --set ingress.hosts[0].host="${APP_NAME}-green.example.com" \
        --timeout 10m \
        --wait
    
    # Verify green environment
    kubectl wait --for=condition=available deployment/"${APP_NAME}-green" \
        --namespace "$NAMESPACE" --timeout=300s
}

# Traffic switching
switch_traffic() {
    echo "Switching traffic to green environment..."
    
    # Update main service to point to green deployment
    kubectl patch service "$APP_NAME" \
        -p '{"spec":{"selector":{"app.kubernetes.io/name":"'"$APP_NAME"'","version":"green"}}}' \
        --namespace "$NAMESPACE"
    
    # Wait for traffic switch to complete
    sleep 30
    
    # Verify traffic switch
    if curl -f "http://${APP_NAME}.example.com/health" >/dev/null 2>&1; then
        echo "Traffic successfully switched to green environment"
    else
        echo "Health check failed after traffic switch"
        exit 1
    fi
}

# Clean up blue environment
cleanup_blue() {
    echo "Cleaning up blue environment..."
    
    helm uninstall "${APP_NAME}-blue" --namespace "$NAMESPACE" || true  # ⚠️ Delete release and associated resources
}

# Rollback function
rollback() {
    echo "Rolling back to blue environment..."
    
    # Restore service to point to blue environment
    kubectl patch service "$APP_NAME" \
        -p '{"spec":{"selector":{"app.kubernetes.io/name":"'"$APP_NAME"'","version":"blue"}}}' \
        --namespace "$NAMESPACE"
    
    # Redeploy blue environment
    helm upgrade --install "${APP_NAME}-blue" "./charts/$APP_NAME" \
        --namespace "$NAMESPACE" \
        --timeout 5m \
        --wait
    
    exit 1
}

# Main execution flow
main() {
    trap rollback ERR
    
    deploy_green
    switch_traffic
    cleanup_blue
    
    echo "Blue-green deployment completed successfully!"
}

main "$@"
```
<!-- chunk: 🤖 Intelligent Operations Tools -->## 🤖 Intelligent Operations Tools

## Self-Healing System

## 1. Automatic Fault Detection and Recovery
```python
#!/usr/bin/env python3
# Automatic fault detection and recovery system

import asyncio
import aiohttp
import json
import logging
from datetime import datetime, timedelta
from kubernetes import client, config
from kubernetes.client.rest import ApiException

class AutoHealingSystem:
    def __init__(self):
        config.load_kube_config()
        self.apps_v1 = client.AppsV1Api()
        self.core_v1 = client.CoreV1Api()
        self.monitoring_url = "http://prometheus:9090/api/v1/query"
        self.logger = self.setup_logger()
    
    def setup_logger(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger(__name__)
    
    async def check_pod_health(self, namespace, deployment_name):
        """Check pod health status"""
        try:
            deployment = self.apps_v1.read_namespaced_deployment(
                deployment_name, namespace
            )
            
            # Check replica status
            if (deployment.status.ready_replicas != deployment.status.replicas or
                deployment.status.unavailable_replicas > 0):
                return False, "Replica mismatch"
            
            # Check pod status
            pods = self.core_v1.list_namespaced_pod(
                namespace, 
                label_selector=f"app={deployment_name}"
            )
            
            for pod in pods.items:
                if pod.status.phase not in ['Running', 'Succeeded']:
                    return False, f"Pod {pod.metadata.name} in {pod.status.phase} state"
                
                # Check container restart count
                for container_status in pod.status.container_statuses or []:
                    if container_status.restart_count > 5:
                        return False, f"Container {container_status.name} restarted {container_status.restart_count} times"
            
            return True, "Healthy"
            
        except ApiException as e:
            return False, f"API Error: {e}"
    
    async def get_error_metrics(self, app_name):
        """Get application error metrics"""
        query = f'rate(http_requests_total{{app="{app_name}",status=~"5.."}}[5m])'
        
        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.monitoring_url, 
                params={'query': query}
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    if data['data']['result']:
                        return float(data['data']['result'][0]['value'][1])
                return 0.0
    
    async def restart_deployment(self, namespace, deployment_name):
        """Restart deployment"""
        try:
            # Trigger rolling update
            deployment = self.apps_v1.read_namespaced_deployment(
                deployment_name, namespace
            )
            
            # Add timestamp annotation to trigger update
            if deployment.spec.template.metadata.annotations is None:
                deployment.spec.template.metadata.annotations = {}
            
            deployment.spec.template.metadata.annotations['kubectl.kubernetes.io/restartedAt'] = \
                datetime.now().isoformat()
            
            self.apps_v1.patch_namespaced_deployment(
                deployment_name, namespace, deployment
            )
            
            self.logger.info(f"Restarted deployment {deployment_name} in {namespace}")
            return True
            
        except ApiException as e:
            self.logger.error(f"Failed to restart deployment: {e}")
            return False
    
    async def heal_application(self, namespace, app_name):
        """Heal application"""
        # Check health status
        is_healthy, reason = await self.check_pod_health(namespace, app_name)
        
        if is_healthy:
            # Check error rate
            error_rate = await self.get_error_metrics(app_name)
            
            if error_rate > 0.1:  # Error rate exceeds 10%
                self.logger.warning(f"High error rate ({error_rate:.2%}) for {app_name}")
                await self.restart_deployment(namespace, app_name)
        else:
            self.logger.warning(f"Unhealthy application {app_name}: {reason}")
            await self.restart_deployment(namespace, app_name)
    
    async def run_continuous_healing(self):
        """Run continuous healing system"""
        while True:
            try:
                # Get all application list
                namespaces = self.core_v1.list_namespace()
                
                for ns in namespaces.items:
                    if ns.metadata.name in ['kube-system', 'monitoring']:
                        continue
                    
                    deployments = self.apps_v1.list_namespaced_deployment(ns.metadata.name)
                    
                    for deployment in deployments.items:
                        app_name = deployment.metadata.name
                        await self.heal_application(ns.metadata.name, app_name)
                
                # Wait for next check
                await asyncio.sleep(300)  # 5 minutes
                
            except Exception as e:
                self.logger.error(f"Error in healing cycle: {e}")
                await asyncio.sleep(60)

# Usage example
async def main():
    healer = AutoHealingSystem()
    await healer.run_continuous_healing()

if __name__ == "__main__":
    asyncio.run(main())
```

## Capacity Planning Tool

## 1. Resource Prediction and Planning
```python
#!/usr/bin/env python3
# Container resource prediction tool

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

class ResourcePredictor:
    def __init__(self):
        self.cpu_model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.memory_model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.scaler = StandardScaler()
        
    def prepare_features(self, metrics_data):
        """Prepare feature data"""
        df = pd.DataFrame(metrics_data)
        
        # Time features
        df['hour'] = pd.to_datetime(df['timestamp']).dt.hour
        df['dayofweek'] = pd.to_datetime(df['timestamp']).dt.dayofweek
        df['month'] = pd.to_datetime(df['timestamp']).dt.month
        
        # Lag features
        for lag in [1, 2, 3, 6, 12, 24]:
            df[f'cpu_lag_{lag}h'] = df['cpu_usage'].shift(lag)
            df[f'memory_lag_{lag}h'] = df['memory_usage'].shift(lag)
        
        # Rolling window statistics
        windows = [3, 6, 12, 24]
        for window in windows:
            df[f'cpu_mean_{window}h'] = df['cpu_usage'].rolling(window=window).mean()
            df[f'cpu_std_{window}h'] = df['cpu_usage'].rolling(window=window).std()
            df[f'memory_mean_{window}h'] = df['memory_usage'].rolling(window=window).mean()
            df[f'memory_std_{window}h'] = df['memory_usage'].rolling(window=window).std()
        
        return df.dropna()
    
    def train_models(self, training_data):
        """Train prediction models"""
        df = self.prepare_features(training_data)
        
        feature_columns = [col for col in df.columns 
                          if col not in ['timestamp', 'cpu_usage', 'memory_usage']]
        
        X = df[feature_columns]
        y_cpu = df['cpu_usage']
        y_memory = df['memory_usage']
        
        # Normalize features
        X_scaled = self.scaler.fit_transform(X)
        
        # Train models
        self.cpu_model.fit(X_scaled, y_cpu)
        self.memory_model.fit(X_scaled, y_memory)
        
        print(f"Model trained on {len(df)} samples")
        print(f"Feature importance (CPU): {self.cpu_model.feature_importances_[:5]}")
    
    def predict_resources(self, future_timestamps):
        """Predict future resource requirements"""
        # Construct future time features
        future_dates = pd.to_datetime(future_timestamps)
        future_df = pd.DataFrame({
            'timestamp': future_timestamps,
            'hour': future_dates.hour,
            'dayofweek': future_dates.dayofweek,
            'month': future_dates.month
        })
        
        # Add lag feature placeholders
        for lag in [1, 2, 3, 6, 12, 24]:
            future_df[f'cpu_lag_{lag}h'] = 0.5  # Fill with average value
            future_df[f'memory_lag_{lag}h'] = 0.5
        
        # Add rolling statistics placeholders
        windows = [3, 6, 12, 24]
        for window in windows:
            future_df[f'cpu_mean_{window}h'] = 0.5
            future_df[f'cpu_std_{window}h'] = 0.1
            future_df[f'memory_mean_{window}h'] = 0.5
            future_df[f'memory_std_{window}h'] = 0.1
        
        feature_columns = [col for col in future_df.columns if col != 'timestamp']
        X_future = self.scaler.transform(future_df[feature_columns])
        
        cpu_predictions = self.cpu_model.predict(X_future)
        memory_predictions = self.memory_model.predict(X_future)
        
        return {
            'timestamps': future_timestamps,
            'cpu_predictions': cpu_predictions,
            'memory_predictions': memory_predictions
        }
    
    def generate_capacity_plan(self, predictions, current_capacity, growth_factor=1.2):
        """Generate capacity planning recommendations"""
        max_cpu = np.max(predictions['cpu_predictions'])
        max_memory = np.max(predictions['memory_predictions'])
        
        recommended_cpu = max_cpu * growth_factor
        recommended_memory = max_memory * growth_factor
        
        plan = {
            'current_capacity': current_capacity,
            'predicted_peak': {
                'cpu': max_cpu,
                'memory': max_memory
            },
            'recommended_capacity': {
                'cpu': recommended_cpu,
                'memory': recommended_memory
            },
            'scaling_required': {
                'cpu': recommended_cpu > current_capacity['cpu'],
                'memory': recommended_memory > current_capacity['memory']
            }
        }
        
        return plan

# Usage example
if __name__ == "__main__":
    # Simulate historical data
    dates = pd.date_range('2024-01-01', periods=168, freq='H')  # One week of data
    training_data = {
        'timestamp': dates,
        'cpu_usage': np.random.normal(0.6, 0.15, 168),  # 60% average CPU usage
        'memory_usage': np.random.normal(0.5, 0.12, 168)  # 50% average memory usage
    }
    
    # Train model
    predictor = ResourcePredictor()
    predictor.train_models(training_data)
    
    # Predict next week
    future_dates = pd.date_range('2024-01-08', periods=168, freq='H')
    predictions = predictor.predict_resources(future_dates)
    
    # Generate capacity plan
    current_capacity = {'cpu': 1.0, 'memory': 1.0}  # Current capacity 100%
    capacity_plan = predictor.generate_capacity_plan(predictions, current_capacity)
    
    print("Capacity Planning Results:")
    print(f"Current Capacity: {capacity_plan['current_capacity']}")
    print(f"Predicted Peak: {capacity_plan['predicted_peak']}")
    print(f"Recommended Capacity: {capacity_plan['recommended_capacity']}")
    print(f"Scaling Required: {capacity_plan['scaling_required']}")
```

<!-- chunk: 📊 Monitoring and Alerting System -->## 📊 Monitoring and Alerting System

## Intelligent Alert Aggregation

## 1. Alert Deduplication and Correlation
```python
#!/usr/bin/env python3
# Intelligent alert handling system

import asyncio
import json
from collections import defaultdict
from datetime import datetime, timedelta
import logging

class SmartAlertManager:
    def __init__(self):
        self.alert_history = defaultdict(list)
        self.correlation_rules = self.load_correlation_rules()
        self.logger = self.setup_logger()
    
    def setup_logger(self):
        logging.basicConfig(level=logging.INFO)
        return logging.getLogger(__name__)
    
    def load_correlation_rules(self):
        """Load alert correlation rules"""
        return {
            'node_failure_cascade': {
                'patterns': [
                    'NodeNotReady',
                    'PodEvicted',
                    'ServiceUnavailable'
                ],
                'time_window': 300  # 5 minute window
            },
            'resource_exhaustion': {
                'patterns': [
                    'HighMemoryUsage',
                    'HighCPULoad',
                    'PodPending'
                ],
                'time_window': 600  # 10 minute window
            }
        }
    
    def calculate_alert_severity(self, alert):
        """Calculate alert severity"""
        severity_weights = {
            'critical': 10,
            'warning': 5,
            'info': 1
        }
        
        base_severity = severity_weights.get(alert.get('severity', 'info'), 1)
        
        # Consider alert frequency
        recent_alerts = self.get_recent_alerts(
            alert['alertname'], 
            timedelta(minutes=30)
        )
        
        frequency_factor = min(len(recent_alerts) / 5.0, 2.0)  # Max 2x weight
        
        # Consider impact scope
        affected_pods = alert.get('affected_pods', 1)
        scope_factor = min(affected_pods / 10.0, 3.0)  # Max 3x weight
        
        return base_severity * frequency_factor * scope_factor
    
    def get_recent_alerts(self, alert_name, time_window):
        """Get recent same-type alerts"""
        cutoff_time = datetime.now() - time_window
        recent_alerts = []
        
        for alert in self.alert_history[alert_name]:
            if alert['timestamp'] > cutoff_time:
                recent_alerts.append(alert)
        
        return recent_alerts
    
    def detect_correlated_alerts(self, new_alert):
        """Detect correlated alerts"""
        correlations = []
        
        for rule_name, rule in self.correlation_rules.items():
            pattern_matches = 0
            
            for pattern in rule['patterns']:
                recent_alerts = self.get_recent_alerts(
                    pattern, 
                    timedelta(seconds=rule['time_window'])
                )
                
                if recent_alerts:
                    pattern_matches += 1
            
            # If enough patterns match, consider there is correlation
            if pattern_matches >= len(rule['patterns']) * 0.6:  # 60% match rate
                correlations.append({
                    'rule': rule_name,
                    'confidence': pattern_matches / len(rule['patterns']),
                    'related_alerts': self.get_related_alerts(rule['patterns'], rule['time_window'])
                })
        
        return correlations
    
    def get_related_alerts(self, patterns, time_window):
        """Get related alerts"""
        related = []
        cutoff_time = datetime.now() - timedelta(seconds=time_window)
        
        for pattern in patterns:
            for alert in self.alert_history[pattern]:
                if alert['timestamp'] > cutoff_time:
                    related.append(alert)
        
        return related
    
    def suppress_duplicate_alerts(self, new_alert):
        """Suppress duplicate alerts"""
        alert_name = new_alert['alertname']
        recent_alerts = self.get_recent_alerts(alert_name, timedelta(minutes=15))
        
        if not recent_alerts:
            return False
        
        # Check for duplicate alerts
        for recent_alert in recent_alerts:
            if (abs(new_alert.get('value', 0) - recent_alert.get('value', 0)) < 0.1 and
                new_alert.get('labels') == recent_alert.get('labels')):
                return True
        
        return False
    
    async def process_alert(self, alert_data):
        """Process new alert"""
        alert = json.loads(alert_data)
        alert['timestamp'] = datetime.now()
        
        # Record alert history
        self.alert_history[alert['alertname']].append(alert)
        
        # Check for duplicate alerts
        if self.suppress_duplicate_alerts(alert):
            self.logger.info(f"Suppressed duplicate alert: {alert['alertname']}")
            return
        
        # Calculate severity
        severity_score = self.calculate_alert_severity(alert)
        alert['severity_score'] = severity_score
        
        # Detect correlated alerts
        correlations = self.detect_correlated_alerts(alert)
        alert['correlations'] = correlations
        
        # Handle based on severity
        if severity_score > 50:
            await self.handle_critical_alert(alert)
        elif severity_score > 20:
            await self.handle_warning_alert(alert)
        else:
            await self.handle_info_alert(alert)
        
        self.logger.info(f"Processed alert: {alert['alertname']} (Severity: {severity_score})")
    
    async def handle_critical_alert(self, alert):
        """Handle critical alert"""
        self.logger.critical(f"CRITICAL ALERT: {alert}")
        
        # Send emergency notification
        await self.send_emergency_notification(alert)
        
        # Trigger auto repair
        if alert['alertname'] in ['NodeNotReady', 'PodCrashLooping']:
            await self.trigger_auto_repair(alert)
    
    async def handle_warning_alert(self, alert):
        """Handle warning alert"""
        self.logger.warning(f"WARNING ALERT: {alert}")
        
        # Send notification to relevant team
        await self.send_team_notification(alert)
        
        # Record for trend analysis
        await self.record_for_analysis(alert)
    
    async def handle_info_alert(self, alert):
        """Handle info alert"""
        self.logger.info(f"INFO ALERT: {alert}")
        
        # Record for statistical analysis
        await self.record_for_analysis(alert)
    
    async def send_emergency_notification(self, alert):
        """Send emergency notification"""
        notification = {
            'type': 'emergency',
            'alert': alert,
            'timestamp': datetime.now().isoformat(),
            'recipients': ['sre-team', 'oncall-engineer']
        }
        
        # Can integrate specific notification system here
        print(f"EMERGENCY NOTIFICATION: {json.dumps(notification, indent=2)}")
    
    async def send_team_notification(self, alert):
        """Send team notification"""
        notification = {
            'type': 'team',
            'alert': alert,
            'timestamp': datetime.now().isoformat(),
            'recipients': ['dev-team']
        }
        
        print(f"TEAM NOTIFICATION: {json.dumps(notification, indent=2)}")
    
    async def trigger_auto_repair(self, alert):
        """Trigger auto repair"""
        repair_actions = {
            'NodeNotReady': self.restart_node_components,
            'PodCrashLooping': self.restart_pod
        }
        
        action = repair_actions.get(alert['alertname'])
        if action:
            await action(alert)
    
    async def restart_node_components(self, alert):
        """Restart node components"""
        node_name = alert.get('labels', {}).get('node')
        if node_name:
            self.logger.info(f"Restarting components on node: {node_name}")
            # Execute restart command
            # await self.execute_command(f"kubectl drain {node_name}")
            # await self.execute_command(f"kubectl uncordon {node_name}")
    
    async def restart_pod(self, alert):
        """Restart pod"""
        namespace = alert.get('labels', {}).get('namespace')
        pod_name = alert.get('labels', {}).get('pod')
        
        if namespace and pod_name:
            self.logger.info(f"Restarting pod: {namespace}/{pod_name}")
            # await self.execute_command(f"kubectl delete pod {pod_name} -n {namespace}")

# Usage example
async def main():
    alert_manager = SmartAlertManager()
    
    # Simulate receiving alerts
    test_alerts = [
        '{"alertname": "HighMemoryUsage", "severity": "warning", "value": 85}',
        '{"alertname": "NodeNotReady", "severity": "critical", "labels": {"node": "node-1"}}',
        '{"alertname": "PodEvicted", "severity": "warning", "labels": {"namespace": "default", "pod": "app-1"}}'
    ]
    
    for alert_json in test_alerts:
        await alert_manager.process_alert(alert_json)
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(main())
```

<!-- chunk: 🔧 Implementation Checklist -->## 🔧 Implementation Checklist

## Automated Tool Deployment
- [ ] Deploy infrastructure automation tools (Ansible/Terraform)
- [ ] Configure application deployment automation scripts
- [ ] Implement intelligent fault detection and self-healing system
- [ ] Deploy capacity planning and forecasting tools
- [ ] Establish intelligent alert handling mechanism
- [ ] Configure monitoring and log collection automation

## Operations Process Optimization
- [ ] Implement standardized operations procedures
- [ ] Establish automated testing and validation mechanism
- [ ] Configure change management and approval workflow
- [ ] Implement rollback and disaster recovery mechanism
- [ ] Establish operations knowledge base and documentation
- [ ] Configure operations team training plan

## System Reliability Assurance
- [ ] Implement multi-level monitoring and alerting system
- [ ] Configure automated fault failover mechanism
- [ ] Establish performance benchmarks and capacity planning
- [ ] Implement security compliance automation checks
- [ ] Configure backup and recovery automation
- [ ] Establish continuous improvement feedback mechanism

---

*This document provides comprehensive technical solutions and best practice guidance for building enterprise-grade automated operations toolchains*

---

<!-- chunk: Obsidian Related Documents -->## Obsidian Related Documents

- domain-11-production-operations MOC
- [[domain-11-production-operations/README.md|Domain 11: Production Operations Best Practices]]
- Domain-18 Production Operations — Open Source Project Index
- [[domain-01-cluster-fundamentals/01-production-architecture-design-principles.md|01-Production Architecture Design Principles]]
- 02-Multi-cloud Hybrid Deployment Strategy
- 03-Edge Computing Production Deployment
- 04-Enterprise Monitoring System
- 05-Log Collection and Analysis Platform
- 06-APM Application Performance Monitoring
- 07-Zero Trust Security Architecture
- 08-CIS Benchmark Compliance Verification
- 09-Software Bill of Materials

## Related

- 22-production-checklist
- [[domain-02-workloads-applications/02-spring-boot-kubernetes-production.md|02-spring-boot-kubernetes-production]]

## See Also

- 10-gitops-pipeline-practices
- 11-infrastructure-as-code
- 13-kubernetes-cost-governance
- 14-resource-quota-management


<!-- risk-assessed -->