---
title: Disaster Recovery & Business Continuity
description: '## Overview'
summary: 'Disaster recovery and business continuity are the lifeline of platform operations. Through establishing comprehensive backup and recovery strategies, active-active architectures, and emergency response mechanisms, they ensure continuous business availability in various problem scenarios.'
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- istio
- postgresql
- daemonset
- gateway
- operator
- webhook
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Platform Engineer
- Operations Engineer
estimated_read_time: 5min
intent_queries:
- Disaster Recovery & Business Continuity Overview
- How to implement Disaster Recovery & Business Continuity
- Kubernetes platform ops best practices
trigger_keywords:
- Disaster Recovery and Business Continuity
- Disaster
- Recovery
- Business
- Continuity
- platform
- ops
prerequisites:
- kubectl-basics
- platform-engineering-basics
- service-mesh-basics
- backup-basics
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
  path: ../domain-06-observability/
  label: 'Related Knowledge Domain: domain-06-observability'
- type: domain
  path: ../domain-15-specialized-tech/
  label: 'Related Knowledge Domain: domain-15-specialized-tech'
- type: domain
  path: ../domain-10-troubleshooting-diagnostics/
  label: 'Related Knowledge Domain: domain-10-troubleshooting-diagnostics'
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/operate/11-disaster-recovery-business-continuity.md
original_language: Chinese
---

> **Production Environment Security Reminder**
>
> This document contains directly executable operations commands. Before execution, ensure: the target cluster and namespace are correct; you have sufficient RBAC permissions; you have verified in non-production environments. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state but typically can be rolled back), 🟢 Low risk/Read-only (information collection, no side effects).




# Disaster Recovery & Business Continuity

<!-- chunk: Overview -->
## Overview

Disaster recovery and business continuity are the lifeline of platform operations. Through establishing comprehensive backup and recovery strategies, active-active architectures, and emergency response mechanisms, they ensure continuous business availability in various problem scenarios.

<!-- chunk: Disaster Recovery Strategy -->
## Disaster Recovery Strategy

### RTO/RPO Target Definition
```
RTO (Recovery Time Objective): 15 minutes
RPO (Recovery Point Objective): 5 minutes
MTTR (Mean Time To Recovery): 30 minutes
```

### Disaster Type Classification
- **Natural Disasters**: Earthquakes, floods, fires, etc.
- **Human-caused Disasters**: Misoperations, malicious attacks, code defects
- **Technical Issues**: Hardware failures, network interruptions, power failures
- **Vendor Issues**: Cloud service provider problems, third-party service outages

<!-- chunk: Backup Strategy System -->
## Backup Strategy System

### Data Backup Hierarchy
```
Application Data Backup → System Configuration Backup → Infrastructure Backup → Disaster Recovery Environment Backup
```

### Velero Backup Configuration
```yaml
# Velero Installation Configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: velero
  namespace: velero
spec:
  replicas: 2
  selector:
    matchLabels:
      name: velero
  template:
    metadata:
      labels:
        name: velero
    spec:
      restartPolicy: Always
      serviceAccountName: velero
      containers:
      - name: velero
        image: velero/velero:v1.11.0
        command:
        - /velero
        args:
        - server
        - --backup-sync-period=1m
        - --restic-timeout=1h
        env:
        - name: AWS_SHARED_CREDENTIALS_FILE
          value: /credentials/cloud
        - name: VELERO_SCRATCH_DIR
          value: /scratch
        volumeMounts:
        - name: cloud-credentials
          mountPath: /credentials
        - name: plugins
          mountPath: /plugins
        - name: scratch
          mountPath: /scratch

---
# Backup Storage Location Configuration
apiVersion: velero.io/v1
kind: BackupStorageLocation
metadata:
  name: default
  namespace: velero
spec:
  provider: aws
  objectStorage:
    bucket: velero-backup-bucket
    prefix: backups
  config:
    region: us-west-2
    s3ForcePathStyle: "true"
    s3Url: https://s3.us-west-2.amazonaws.com
```

### Backup Strategy Configuration
```yaml
# Application Data Backup Strategy
apiVersion: velero.io/v1
kind: Schedule
metadata:
  name: app-backup-hourly
  namespace: velero
spec:
  schedule: "0 * * * *"  # Execute hourly
  template:
    ttl: "168h"  # Retain for 7 days
    includedNamespaces:
    - production
    includedResources:
    - persistentvolumeclaims
    - persistentvolumes
    snapshotVolumes: true
    storageLocation: default

---
# System Configuration Backup Strategy
apiVersion: velero.io/v1
kind: Schedule
metadata:
  name: config-backup-daily
  namespace: velero
spec:
  schedule: "0 2 * * *"  # Daily at 2 AM
  template:
    ttl: "720h"  # Retain for 30 days
    includedNamespaces:
    - kube-system
    - monitoring
    - logging
    includedResources:
    - deployments
    - services
    - configmaps
    - secrets
    snapshotVolumes: false
```

### Cross-region Backup
```yaml
# Cross-region Backup Location
apiVersion: velero.io/v1
kind: BackupStorageLocation
metadata:
  name: cross-region-backup
  namespace: velero
spec:
  provider: aws
  objectStorage:
    bucket: velero-dr-bucket
    prefix: dr-backups
  config:
    region: us-east-1  # Disaster recovery region
    s3ForcePathStyle: "true"
    s3Url: https://s3.us-east-1.amazonaws.com

---
# Disaster Recovery Backup Strategy
apiVersion: velero.io/v1
kind: Schedule
metadata:
  name: dr-backup-weekly
  namespace: velero
spec:
  schedule: "0 3 * * 0"  # Weekly on Sunday at 3 AM
  template:
    ttl: "8760h"  # Retain for 1 year
    includedNamespaces:
    - production
    - staging
    storageLocation: cross-region-backup
    snapshotVolumes: true
```

<!-- chunk: Recovery Drill Process -->
## Recovery Drill Process

### Recovery Test Script

> ⚠️ **🔴 Catastrophic Operation** — Contains irreversible commands. Before execution, you must satisfy the change window + dual-person review + pre-operation backup + rollback plan
> - `kubectl delete namespace`: Permanently delete namespace and all resources, irreversible
> - `kubectl apply/create/replace`: Create/modify cluster resources

> **🔴 High Risk Operation Warning**
>
> The commands below are irreversible or high-impact operations. Before execution, ensure:
> - Critical data and configurations have been backed up
> - You are within an approved change window
> - You have obtained authorization from relevant stakeholders
> - You have prepared a rollback or recovery plan
> - The target cluster, namespace, node/resource names are correct

``` bash
# 🔴 High risk: May cause data loss or service interruption. Requires backup, change approval, and rollback plan before execution
#!/bin/bash
# disaster-recovery-test.sh

set -e

NAMESPACE="dr-test"
BACKUP_NAME="test-backup-$(date +%Y%m%d-%H%M%S)"

echo "🚀 Starting Disaster Recovery Test"

# 1. Create test environment
echo "1. Creating test environment..."
kubectl create namespace $NAMESPACE

# 2. Deploy test application
echo "2. Deploying test application..."
kubectl apply -f test-app.yaml -n $NAMESPACE

# 3. Wait for application readiness
echo "3. Waiting for application to be ready..."
kubectl wait --for=condition=ready pod -l app=test-app -n $NAMESPACE --timeout=300s

# 4. Create backup
echo "4. Creating backup..."
velero backup create $BACKUP_NAME \
  --include-namespaces $NAMESPACE \
  --snapshot-volumes \
  --wait

# 5. Verify backup success
echo "5. Verifying backup..."
if velero backup describe $BACKUP_NAME | grep -q "Completed"; then
    echo "✅ Backup completed successfully"
else
    echo "❌ Backup failed"
    exit 1
fi

# 6. Delete test environment
echo "6. Deleting test environment..."
kubectl delete namespace $NAMESPACE --wait=false  # ⚠️ Irreversible: Permanently delete namespace and all resources

# 7. Wait for deletion completion
sleep 30

# 8. Perform recovery
echo "7. Restoring from backup..."
velero restore create --from-backup $BACKUP_NAME \
  --namespace-mappings $NAMESPACE:$NAMESPACE-restored \
  --wait

# 9. Verify recovery
echo "8. Verifying restoration..."
kubectl wait --for=condition=ready pod -l app=test-app -n $NAMESPACE-restored --timeout=300s

# 10. Functionality verification
echo "9. Performing functionality test..."
if curl -f http://test-app.$NAMESPACE-restored.svc.cluster.local/health; then
    echo "✅ Application restored and functioning properly"
else
    echo "❌ Application restoration verification failed"
    exit 1
fi

# 11. Clean up test resources
echo "10. Cleaning up test resources..."
kubectl delete namespace $NAMESPACE-restored  # ⚠️ Irreversible: Permanently delete namespace and all resources
velero backup delete $BACKUP_NAME --confirm

echo "🎉 Disaster Recovery Test Completed Successfully!"
```
### Recovery Time Verification
```python
# Recovery time monitoring script
import time
import subprocess
import json

class RecoveryTimeMonitor:
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.metrics = {}
    
    def start_monitoring(self):
        self.start_time = time.time()
        print(f"⏱️  Recovery monitoring started at {time.ctime(self.start_time)}")
    
    def check_recovery_completion(self, namespace, deployment):
        """Check if recovery is complete"""
        cmd = f"kubectl get deployment {deployment} -n {namespace} -o json"
        try:
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            deployment_info = json.loads(result.stdout)
            
            replicas = deployment_info['status'].get('replicas', 0)
            ready_replicas = deployment_info['status'].get('readyReplicas', 0)
            
            return replicas > 0 and ready_replicas == replicas
        except Exception as e:
            print(f"Error checking deployment status: {e}")
            return False
    
    def stop_monitoring(self):
        self.end_time = time.time()
        recovery_time = self.end_time - self.start_time
        self.metrics['recovery_time'] = recovery_time
        print(f"⏱️  Recovery completed in {recovery_time:.2f} seconds")
        return recovery_time
    
    def generate_report(self):
        return {
            'recovery_time_seconds': self.metrics.get('recovery_time'),
            'rto_compliance': self.metrics.get('recovery_time', 0) <= 900,  # 15-minute RTO
            'test_timestamp': time.ctime(self.start_time)
        }
```

<!-- chunk: Active-Active Architecture Design -->
## Active-Active Architecture Design

### Primary-Standby Cluster Architecture
```
Primary Cluster (us-west) ←→ Standby Cluster (us-east)
        ↑                          ↑
    Load Balancer ← Health Check → Failover Mechanism
```

### Cluster Synchronization Configuration
```yaml
# Primary Cluster Configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sync-controller
  namespace: dr-system
spec:
  replicas: 2
  selector:
    matchLabels:
      app: sync-controller
  template:
    metadata:
      labels:
        app: sync-controller
    spec:
      containers:
      - name: sync-controller
        image: dr/sync-controller:v1.0
        env:
        - name: PRIMARY_CLUSTER
          value: "https://k8s-primary.example.com"
        - name: STANDBY_CLUSTER
          value: "https://k8s-standby.example.com"
        - name: SYNC_INTERVAL
          value: "30s"
        volumeMounts:
        - name: kubeconfig
          mountPath: /etc/kubernetes
          readOnly: true
      volumes:
      - name: kubeconfig
        secret:
          secretName: cluster-kubeconfigs

---
# Data Synchronization Policy
apiVersion: dr.system/v1
kind: DataSyncPolicy
metadata:
  name: production-sync
spec:
  source:
    cluster: primary
    namespaces:
    - production
    - staging
  target:
    cluster: standby
    namespaces:
    - production-dr
    - staging-dr
  syncMode: continuous
  conflictResolution: last-write-wins
  resources:
    include:
    - deployments
    - services
    - configmaps
    - secrets
    exclude:
    - events
    - pods
```

### Automatic Failover
```yaml
# Health Check and Failover
apiVersion: apps/v1
kind: Deployment
metadata:
  name: failover-controller
  namespace: dr-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: failover-controller
  template:
    metadata:
      labels:
        app: failover-controller
    spec:
      containers:
      - name: failover-controller
        image: dr/failover-controller:v1.0
        env:
        - name: HEALTH_CHECK_INTERVAL
          value: "10s"
        - name: FAILURE_THRESHOLD
          value: "3"
        - name: FAILOVER_TIMEOUT
          value: "300"  # 5-minute timeout
        - name: NOTIFICATION_WEBHOOK
          value: "https://alerts.example.com/webhook"
```

<!-- chunk: Business Continuity Assurance -->
## Business Continuity Assurance

### Multi-active Application Deployment
```yaml
# Multi-region Deployment Configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: multi-region-app
spec:
  replicas: 6
  selector:
    matchLabels:
      app: multi-region-app
  template:
    metadata:
      labels:
        app: multi-region-app
        version: v1.0
    spec:
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchExpressions:
                - key: app
                  operator: In
                  values:
                  - multi-region-app
              topologyKey: topology.kubernetes.io/zone
      containers:
      - name: app
        image: myapp:v1.0
        ports:
        - containerPort: 8080
        readinessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10

---
# Multi-region Service Configuration
apiVersion: v1
kind: Service
metadata:
  name: multi-region-service
spec:
  selector:
    app: multi-region-app
  ports:
  - port: 80
    targetPort: 8080
  type: LoadBalancer
  loadBalancerSourceRanges:
  - 0.0.0.0/0

---
# Traffic Splitting Configuration
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: multi-region-routing
spec:
  hosts:
  - multi-region.example.com
  gateways:
  - multi-region-gateway
  http:
  - route:
    - destination:
        host: multi-region-app.primary.svc.cluster.local
      weight: 80
    - destination:
        host: multi-region-app.standby.svc.cluster.local
      weight: 20
```

### Database High Availability
```yaml
# PostgreSQL Primary-Standby Configuration
apiVersion: postgresql.cnpg.io/v1
kind: Cluster
metadata:
  name: postgres-ha
spec:
  instances: 3
  primaryUpdateStrategy: unsupervised
  storage:
    size: 50Gi
  bootstrap:
    initdb:
      database: app
      owner: app
  backup:
    barmanObjectStore:
      destinationPath: s3://postgres-backup/
      endpointURL: https://s3.us-west-2.amazonaws.com
      s3Credentials:
        accessKeyId:
          name: postgres-s3-creds
          key: ACCESS_KEY_ID
        secretAccessKey:
          name: postgres-s3-creds
          key: SECRET_ACCESS_KEY
  affinity:
    podAntiAffinity:
      requiredDuringSchedulingIgnoredDuringExecution:
      - topologyKey: kubernetes.io/hostname
        labelSelector:
          matchLabels:
            postgresql: postgres-ha
```

<!-- chunk: Emergency Response Process -->
## Emergency Response Process

### Incident Level Definition
```yaml
# Incident Level Classification
incident_levels:
  P0:  # Critical Incident
    description: "Core business interrupted, impact >50%"
    response_time: "15 minutes"
    escalation: "CTO Notification"
    
  P1:  # High Priority Incident
    description: "Important business impacted, impact 10-50%"
    response_time: "1 hour"
    escalation: "Technical Director Notification"
    
  P2:  # Medium Priority Incident
    description: "General business impacted, impact <10%"
    response_time: "4 hours"
    escalation: "Team Lead Notification"
    
  P3:  # Low Priority Incident
    description: "Minor issue, no business impact"
    response_time: "24 hours"
    escalation: "Routine Handling"
```

### Emergency Response Manual
```markdown
# Emergency Response Manual

<!-- chunk: Contact List -->
## Contact List
- **On-call Manager**: ops-oncall@example.com
- **Infrastructure Team**: infra-team@example.com
- **Application Team**: app-team@example.com
- **Security Team**: security-team@example.com

<!-- chunk: Standard Operating Procedure (SOP) -->
## Standard Operating Procedure (SOP)

### 1. Incident Detection and Confirmation
- Monitoring alert reception
- Initial fault localization
- Impact scope assessment
- Incident level determination

### 2. Emergency Response Initiation
- Notify relevant personnel
- Initiate emergency meeting
- Assign handling tasks
- Establish communication channels

### 3. Fault Handling Execution
- Execute according to pre-plan
- Real-time progress updates
- Decision log preservation
- Stakeholder synchronization

### 4. Recovery Verification
- Functionality test verification
- Performance metric checking
- User experience confirmation
- Business regression testing

### 5. Post-incident Summary
- Root cause analysis of the problem
- Handling process review
- Improvement measures formulation
- Knowledge base update
```

### Automated Emergency Response
```python
# Automated Emergency Response System
class EmergencyResponseSystem:
    def __init__(self):
        self.handlers = {
            'node_failure': self.handle_node_failure,
            'network_outage': self.handle_network_outage,
            'data_corruption': self.handle_data_corruption,
            'security_breach': self.handle_security_breach
        }
    
    def trigger_response(self, incident_type, details):
        """Trigger emergency response"""
        handler = self.handlers.get(incident_type)
        if handler:
            return handler(details)
        else:
            return self.handle_unknown_incident(incident_type, details)
    
    def handle_node_failure(self, details):
        """Handle node failure"""
        affected_nodes = details.get('nodes', [])
        
        # 1. Isolate problem nodes
        for node in affected_nodes:
            self.isolate_node(node)
        
        # 2. Migrate workloads
        self.migrate_workloads(affected_nodes)
        
        # 3. Provision replacement nodes
        self.provision_replacement_nodes(len(affected_nodes))
        
        # 4. Verify service recovery
        return self.verify_service_recovery()
    
    def handle_network_outage(self, details):
        """Handle network outage"""
        # 1. Check network connectivity
        # 2. Switch to backup network paths
        # 3. Reconfigure network policies
        # 4. Verify network recovery
        pass
    
    def isolate_node(self, node_name):
        """Isolate problem node"""
        cmd = f"kubectl cordon {node_name}"
        subprocess.run(cmd.split())
        cmd = f"kubectl drain {node_name} --ignore-daemonsets --delete-emptydir-data"
        subprocess.run(cmd.split())
    
    def migrate_workloads(self, nodes):
        """Migrate workloads"""
        for node in nodes:
            cmd = f"kubectl get pods --field-selector spec.nodeName={node} -o json"
            result = subprocess.run(cmd.split(), capture_output=True, text=True)
            pods = json.loads(result.stdout)
            
            for pod in pods.get('items', []):
                # Reschedule Pod
                pass
```

<!-- chunk: Continuous Improvement Mechanism -->
## Continuous Improvement Mechanism

### Regular Drill Plan
```yaml
# Disaster Recovery Drill Plan
disaster_recovery_exercises:
  quarterly_exercises:
    - name: "Complete Data Center Failure Recovery"
      frequency: "Quarterly"
      participants: ["Operations Team", "Development Team", "Business Team"]
      duration: "4 hours"
      objectives:
        - Verify RTO/RPO metrics
        - Test cross-region recovery
        - Evaluate team collaboration efficiency
      
    - name: "Single Application Failure Recovery"
      frequency: "Monthly"
      participants: ["Application Team", "Operations Team"]
      duration: "2 hours"
      objectives:
        - Verify application-level recovery
        - Test backup integrity
        - Optimize recovery process

  annual_exercises:
    - name: "Large-scale Disaster Recovery Drill"
      frequency: "Annually"
      participants: ["Full participation"]
      duration: "1 day"
      objectives:
        - Comprehensively verify DR capability
        - Test business continuity
        - Perfect emergency plans
```

### Improvement Measure Tracking
```yaml
# Improvement Measure Tracking System
improvement_tracking:
  metrics_collection:
    - recovery_time_metrics
    - backup_success_rate
    - team_response_time
    - user_impact_assessment
  
  feedback_loop:
    - post_incident_reviews
    - exercise_debrief_sessions
    - stakeholder_feedback
    - industry_best_practices
  
  action_items:
    - automation_improvements
    - process_optimizations
    - tool_enhancements
    - training_program_updates
```

By establishing a comprehensive disaster recovery and business continuity system, it is possible to minimize the impact of issues on business and ensure that business operations can be maintained normally in various extreme situations.

---

<!-- chunk: Obsidian Related Documentation -->
## Obsidian Related Documentation

- domain-07-platform-engineering KUDIG Database — Global MOC
- [[domain-07-platform-engineering/README.md|[[Platform Ops Domain|Platform Ops Domain]]]]
- index.md|Domain-9 Platform Ops — Open Source Project Index]]
- Platform Ops Overview
- Cluster Lifecycle Management
- [[domain-07-platform-engineering/governance/03-capacity-planning-resource-assessment.md|03 capacity planning resource assessment]]
- Performance Benchmarking & Tuning
- Operations Metrics System
- Monitoring and Alerting System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization & FinOps

## See Also

- 09-cost-optimization-finops
- 10-security-compliance
- 12-backup-recovery-strategy
- 13-multi-cluster-management


<!-- risk-assessed -->