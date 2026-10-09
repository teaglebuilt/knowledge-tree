---
title: 14 - Multi-Cluster Management & Federation
description: '# 14 - Multi-Cluster Management & Federation'
summary: 'cluster.x-k8s.io/cluster-name: production-cluster'
category: extensions
tags:
- k8s
- extensions
- crd
- operator
- webhook
- apiserver
- kubelet
- scheduler
- prometheus
- istio
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- SRE
- Developer
- Architect
estimated_read_time: 5min
intent_queries:
- What is Multi-Cluster Management & Federation
- How to do Multi-Cluster Management & Federation
- Kubernetes 10 best practices
trigger_keywords:
- Multi-Cluster Management & Federation
- Multi-Cluster
- Management
- Federation
- extensions
prerequisites:
- kubectl-basics
- helm-basics
- service-mesh-basics
- prometheus-basics
- gitops-basics
- cilium-basics
- cni-basics
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
  path: ../domain-07-platform-engineering/
  label: 'Related Knowledge Domain: domain-07-platform-engineering'
original_language: Chinese
source_path: tree/infrastructure/kubernetes/networking/14-multi-cluster-management.md
---

> **Production Environment Security Tips**
>
> Commands included in this document can be directly executed. Please confirm before execution: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; and whether the commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High risk (may cause data loss or service disruption), 🟡 Medium risk (will modify cluster state but usually rollbackable), 🟢 Low risk/readonly (information collection, no side effects).




# 14 - Multi-Cluster Management & Federation

> **Applicable Version**: v1.25 - v1.32 | **Last Updated**: 2026-02 | **Reference**: [[entities/kubernetes.md|kubernetes]].io/docs/concepts/architecture/multicluster](https://kubernetes.io/docs/concepts/architecture/multicluster/)


## Multi-Cluster Architecture Patterns

### Comparison of Cluster Management Models

| Model | Applicable Scenarios | Management Complexity | Data Synchronization | Network Requirements |
|------|----------|------------|----------|----------|
| **Independent Clusters** | Development/Test Environments | Low | None | Independent Network |
| **Cluster Federation** | Multi-regional Deployment | Moderate | Limited Synchronization | Cross-regional Network |
| **Cluster Registry** | Unified Management | High | Centralized View | Network Reachable |
| **Virtual Clusters** | Tenant Isolation | Moderate | Complete Isolation | Shared Underlay |

### Production Environment Multi-cluster Topology

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           Multi-cluster management architecture                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐     │
│  │  Management control plane    │    │  Registration center cluster    │    │  Monitoring alert center    │    │
│  │                 │    │                 │    │                 │    │
│  │ Cluster API     │◄──►│ Cluster Registry │◄──►│ Observability   │    │
│  │ ArgoCD          │    │ Fleet Manager   │    │ Central System  │    │
│  │ Rancher         │    │                 │    │                 │    │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘     │
│           │                       │                       │              │
│           ▼                       ▼                       ▼              │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐     │
│  │  Development cluster        │    │  Production cluster        │    │  Disaster recovery cluster        │    │
│  │  dev-cluster     │    │  prod-cluster    │    │  dr-cluster      │    │
│  │                 │    │                 │    │                 │    │
│  │ Applications    │    │ Critical Apps   │    │ Backup Systems  │    │
│  │ CI/CD Pipeline  │    │ HA Services     │    │ DR Procedures   │    │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘     │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```


## Cluster API Production Practices

### Infrastructure as Code Configuration

```yaml
# Cluster API Cluster Definition
apiVersion: cluster.x-k8s.io/v1beta1
kind: Cluster
metadata:
  name: production-cluster
  namespace: capi-system
spec:
  clusterNetwork:
    pods:
      cidrBlocks: ["192.168.0.0/16"]
    services:
      cidrBlocks: ["10.96.0.0/12"]
  infrastructureRef:
    apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
    kind: AWSCluster
    name: production-cluster
  controlPlaneRef:
    apiVersion: controlplane.cluster.x-k8s.io/v1beta1
    kind: KubeadmControlPlane
    name: production-control-plane

---
# AWS Infrastructure Configuration
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: AWSCluster
metadata:
  name: production-cluster
  namespace: capi-system
spec:
  region: us-west-2
  sshKeyName: production-key
  network:
    vpc:
      availabilityZoneUsageLimit: 3
      availabilityZoneSelection: Ordered
  bastion:
    enabled: true
    allowedCIDRBlocks:
    - 10.0.0.0/8

---
# Control Plane Configuration
apiVersion: controlplane.cluster.x-k8s.io/v1beta1
kind: KubeadmControlPlane
metadata:
  name: production-control-plane
  namespace: capi-system
spec:
  replicas: 3
  machineTemplate:
    infrastructureRef:
      apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
      kind: AWSMachineTemplate
      name: production-control-plane-machines
  kubeadmConfigSpec:
    clusterConfiguration:
      apiServer:
        extraArgs:
          audit-log-path: /var/log/apiserver/audit.log
          audit-policy-file: /etc/kubernetes/policies/audit-policy.yaml
        extraVolumes:
        - name: audit-policies
          hostPath: /etc/kubernetes/policies
          mountPath: /etc/kubernetes/policies
          readOnly: true
      controllerManager:
        extraArgs:
          horizontal-pod-autoscaler-sync-period: 10s
      scheduler:
        extraArgs:
          profiling: "false"
    initConfiguration:
      nodeRegistration:
        kubeletExtraArgs:
          cloud-provider: aws
    joinConfiguration:
      nodeRegistration:
        kubeletExtraArgs:
          cloud-provider: aws
```

### Node Group Management

```yaml
# Worker Node Pool Configuration
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineDeployment
metadata:
  name: production-workers
  namespace: capi-system
spec:
  clusterName: production-cluster
  replicas: 6
  selector:
    matchLabels:
      cluster.x-k8s.io/cluster-name: production-cluster
      pool: workers
  template:
    spec:
      clusterName: production-cluster
      version: v1.28.0
      bootstrap:
        configRef:
          apiVersion: bootstrap.cluster.x-k8s.io/v1beta1
          kind: KubeadmConfigTemplate
          name: production-worker-bootstrap
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: AWSMachineTemplate
        name: production-worker-machines

---
# Worker Node Machine Template
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: AWSMachineTemplate
metadata:
  name: production-worker-machines
  namespace: capi-system
spec:
  template:
    spec:
      instanceType: m5.xlarge
      ami:
        id: ami-0abcdef1234567890
      iamInstanceProfile: nodes.cluster-api-provider-aws.sigs.k8s.io
      rootVolume:
        size: 100
        type: gp3
      cloudInit:
        insecureSkipSecretsManager: true
      spotMarketOptions:
        maxPrice: "0.10"  # Spot实例价格上限

---
# Node Boot Configuration
apiVersion: bootstrap.cluster.x-k8s.io/v1beta1
kind: KubeadmConfigTemplate
metadata:
  name: production-worker-bootstrap
  namespace: capi-system
spec:
  template:
    spec:
      joinConfiguration:
        nodeRegistration:
          kubeletExtraArgs:
            cloud-provider: aws
            rotate-certificates: "true"
            streaming-connection-idle-timeout: "5m"
            max-pods: "110"
            register-with-taints: ""
      preKubeadmCommands:
      - hostname "{{ ds.meta_data.hostname }}"
      - echo "::1         ipv6-localhost ipv6-loopback" >/etc/hosts
      - echo "127.0.0.1   localhost" >>/etc/hosts
      postKubeadmCommands:
      - systemctl daemon-reload
      - systemctl enable kubelet
      - systemctl start kubelet
```


## Multi-cluster Registration and Management

### Rancher Multi-cluster Management

```yaml
# High Availability Deployment of Rancher Server
apiVersion: apps/v1
kind: Deployment
metadata:
  name: rancher
  namespace: cattle-system
spec:
  replicas: 3
  selector:
    matchLabels:
      app: rancher
  template:
    metadata:
      labels:
        app: rancher
    spec:
      serviceAccountName: rancher
      containers:
      - name: rancher
        image: rancher/rancher:v2.7.5
        args:
        - --http-port=80
        - --https-port=443
        - --audit-log-path=/var/log/auditlog/rancher-api-audit.log
        - --audit-level=2
        - --audit-log-maxage=30
        - --audit-log-maxbackup=10
        - --audit-log-maxsize=100
        - --features=multi-cluster-management=true
        - --features=fleet=false
        ports:
        - containerPort: 80
        - containerPort: 443
        volumeMounts:
        - name: audit-log
          mountPath: /var/log/auditlog
        readinessProbe:
          httpGet:
            path: /healthz
            port: 80
          initialDelaySeconds: 60
          periodSeconds: 30
      volumes:
      - name: audit-log
        emptyDir: {}

---
# Cluster Import Configuration
apiVersion: management.cattle.io/v3
kind: Cluster
metadata:
  name: imported-prod-cluster
spec:
  displayName: "Production Cluster"
  description: "Main production Kubernetes cluster"
  importedConfig:
    kubeConfigSecret: prod-cluster-kubeconfig
  clusterAgentDeploymentCustomization:
    overrideAffinity:
      nodeAffinity:
        requiredDuringSchedulingIgnoredDuringExecution:
          nodeSelectorTerms:
          - matchExpressions:
            - key: node-role.kubernetes.io/control-plane
              operator: In
              values:
              - "true"
  fleetWorkspaceName: prod-workspace
```

### Cluster Registry Configuration

```yaml
# Cluster Registry
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cluster-registry
  namespace: multicluster-system
spec:
  replicas: 2
  selector:
    matchLabels:
      app: cluster-registry
  template:
    metadata:
      labels:
        app: cluster-registry
    spec:
      containers:
      - name: registry-server
        image: k8s.gcr.io/cluster-registry:v0.1.0
        ports:
        - containerPort: 8080
        env:
        - name: CLUSTER_REGISTRY_CONFIG
          value: "/etc/cluster-registry/config.yaml"
        volumeMounts:
        - name: config-volume
          mountPath: /etc/cluster-registry
        livenessProbe:
          httpGet:
            path: /healthz
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
      volumes:
      - name: config-volume
        configMap:
          name: cluster-registry-config

---
# Cluster Metadata Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: cluster-registry-config
  namespace: multicluster-system
data:
  config.yaml: |
    clusters:
    - name: production-cluster
      endpoint: https://k8s-prod.example.com:6443
      auth:
        type: serviceaccount
        secretName: prod-cluster-sa-token
      labels:
        environment: production
        region: us-west-2
        purpose: customer-facing
      resources:
        cpu: 128
        memory: 512Gi
        nodes: 24
      
    - name: staging-cluster
      endpoint: https://k8s-staging.example.com:6443
      auth:
        type: certificate
        secretName: staging-cluster-cert
      labels:
        environment: staging
        region: us-east-1
        purpose: testing
      resources:
        cpu: 64
        memory: 256Gi
        nodes: 12
```


## Cross-cluster Application Deployment

### ArgoCD Multi-cluster Deployment

```yaml
# Multi-cluster Application Configuration
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: multi-cluster-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/example/microservices.git
    targetRevision: HEAD
    path: manifests/
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
  ignoreDifferences:
  - group: apps
    kind: Deployment
    jsonPointers:
    - /spec/replicas
  
  # Multi-cluster Target Configuration
  destinations:
  - name: production-cluster
    namespace: production
    server: https://k8s-prod.example.com:6443
  - name: staging-cluster
    namespace: staging
    server: https://k8s-staging.example.com:6443
  - name: dr-cluster
    namespace: disaster-recovery
    server: https://k8s-dr.example.com:6443

---
# Cluster Credential Management
apiVersion: v1
kind: Secret
metadata:
  name: cluster-credentials
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: cluster
type: Opaque
stringData:
  name: production-cluster
  server: https://k8s-prod.example.com:6443
  config: |
    {
      "bearerToken": "<token>",
      "tlsClientConfig": {
        "insecure": false,
        "caData": "<base64-encoded-ca-cert>"
      }
    }
```

### Fleet Multi-cluster Management

```yaml
# Fleet Bundle Configuration
apiVersion: fleet.cattle.io/v1alpha1
kind: Bundle
metadata:
  name: monitoring-stack
  namespace: fleet-default
spec:
  resources:
  - content: |
      apiVersion: apps/v1
      kind: Deployment
      metadata:
        name: prometheus
        namespace: monitoring
      spec:
        replicas: 2
        selector:
          matchLabels:
            app: prometheus
        template:
          metadata:
            labels:
              app: prometheus
          spec:
            containers:
            - name: prometheus
              image: prom/prometheus:v3.2.1
  targets:
  - clusterSelector:
      matchLabels:
        environment: production
    replicaCount: 3
    kustomize:
      patches:
      - patch: |-
          apiVersion: apps/v1
          kind: Deployment
          metadata:
            name: prometheus
          spec:
            template:
              spec:
                containers:
                - name: prometheus
                  resources:
                    requests:
                      memory: "2Gi"
                      cpu: "1"
                    limits:
                      memory: "4Gi"
                      cpu: "2"
  - clusterSelector:
      matchLabels:
        environment: staging
    replicaCount: 1
    kustomize:
      patches:
      - patch: |-
          apiVersion: apps/v1
          kind: Deployment
          metadata:
            name: prometheus
          spec:
            template:
              spec:
                containers:
                - name: prometheus
                  resources:
                    requests:
                      memory: "1Gi"
                      cpu: "500m"
                    limits:
                      memory: "2Gi"
                      cpu: "1"
```


## Inter-cluster Communication and Service Discovery

### Multi-cluster Service Mesh

```yaml
# Istio Multi-cluster Configuration
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
metadata:
  name: istio-multicluster
spec:
  profile: demo
  values:
    global:
      multiCluster:
        clusterName: production-cluster
      meshID: mesh1
      network: network1
    gateways:
      istio-ingressgateway:
        type: LoadBalancer
  components:
    ingressGateways:
    - name: istio-ingressgateway
      enabled: true
      k8s:
        service:
          ports:
          - port: 80
            targetPort: 8080
            name: http2
          - port: 443
            targetPort: 8443
            name: https

---
# Service Export Configuration
apiVersion: networking.istio.io/v1beta1
kind: ServiceEntry
metadata:
  name: remote-services
  namespace: istio-system
spec:
  hosts:
  - "*.remote-cluster.example.com"
  location: MESH_EXTERNAL
  ports:
  - number: 80
    name: http
    protocol: HTTP
  resolution: DNS
  endpoints:
  - address: remote-cluster-gateway.example.com
    ports:
      http: 80
```

### Cross-cluster DNS Configuration

```yaml
# CoreDNS Cross-cluster Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: coredns
  namespace: kube-system
data:
  Corefile: |
    .:53 {
        errors
        health {
           lameduck 5s
        }
        ready
        kubernetes cluster.local in-addr.arpa ip6.arpa {
           pods insecure
           fallthrough in-addr.arpa ip6.arpa
           ttl 30
        }
        prometheus :9153
        forward . /etc/resolv.conf {
           max_concurrent 1000
        }
        cache 30
        loop
        reload
        loadbalance
    }
    
    # Cross-cluster DNS Forwarding
    remote-cluster.example.com:53 {
        forward . 10.100.10.10 10.100.20.10 {
            health_check 5s
        }
        cache 30
    }
```


## Unified Monitoring and Alerts

### Multi-cluster Prometheus Configuration

```yaml
# Prometheus Federated Configuration
apiVersion: monitoring.coreos.com/v1
kind: Prometheus
metadata:
  name: federated-prometheus
  namespace: monitoring
spec:
  replicas: 2
  serviceAccountName: prometheus
  serviceMonitorSelector:
    matchLabels:
      team: frontend
  ruleSelector:
    matchLabels:
      team: frontend
  externalLabels:
    cluster: production-cluster
    region: us-west-2
  remoteWrite:
  - url: http://central-prometheus.monitoring.svc:9090/api/v1/write
    writeRelabelConfigs:
    - sourceLabels: [__name__]
      regex: (up|scrape_samples_scraped)
      action: keep
  additionalScrapeConfigs:
    name: additional-scrape-configs
    key: prometheus-additional.yaml

---
# Additional Fetch Configuration
apiVersion: v1
kind: Secret
metadata:
  name: additional-scrape-configs
  namespace: monitoring
stringData:
  prometheus-additional.yaml: |
    - job_name: 'federate'
      scrape_interval: 15s
      honor_labels: true
      metrics_path: '/federate'
      params:
        'match[]':
          - '{job=~"kubernetes-.*"}'
          - '{__name__=~"node_.*"}'
      static_configs:
      - targets:
        - 'prometheus-us-east.monitoring.svc:9090'
        - 'prometheus-eu-west.monitoring.svc:9090'
        labels:
          cluster: remote-clusters
```


## Security and Access Control

### Multi-cluster RBAC Management

```yaml
# Cluster-to-Cluster RBAC Synchronization
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: multicluster-admin
rules:
- apiGroups: [""]
  resources: ["pods", "services", "namespaces"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
- apiGroups: ["apps"]
  resources: ["deployments", "statefulsets"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
- apiGroups: ["networking.k8s.io"]
  resources: ["networkpolicies", "ingresses"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]

---
# Cross-cluster Role Binding
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: multicluster-admin-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: multicluster-admin
subjects:
- kind: User
  name: admin-user
  apiGroup: rbac.authorization.k8s.io
- kind: Group
  name: cluster-admins
  apiGroup: rbac.authorization.k8s.io
```


## Problem Diagnosis and Debugging

### Multi-cluster Diagnostic Tool

``` bash
# 🟡 Medium Risk: Modifies cluster/resource status; please confirm target, impact scope, and authorization before execution
#!/bin/bash
# multicluster-diagnostics.sh

CLUSTERS=("production-cluster" "staging-cluster" "dr-cluster")

diagnose_cluster_connectivity() {
    echo "=== Cluster Connectivity Diagnosis ==="
    for cluster in "${CLUSTERS[@]}"; do
        echo "Check cluster: $cluster"
        kubectl config use-context $cluster
        
        # Check API Server availability
        if kubectl cluster-info >/dev/null 2>&1; then
            echo "✅ $cluster API Server reachable"
        else
            echo "❌ $cluster API Server unreachable"
        fi
        
        # Check node status
        ready_nodes=$(kubectl get nodes --no-headers | grep -c " Ready ")
        total_nodes=$(kubectl get nodes --no-headers | wc -l)
        echo "📊 $cluster Node Status: $ready_nodes/$total_nodes ready"
    done
}

diagnose_cross_cluster_services() {
    echo "=== Cross-cluster Service Diagnosis ==="
    # Check service discovery
    for cluster in "${CLUSTERS[@]}"; do
        echo "Check services in $cluster..."
        kubectl config use-context $cluster
        kubectl get svc --all-namespaces | grep -E "(LoadBalancer|ClusterIP)" | head -5
    done
}

diagnose_network_connectivity() {
    echo "=== Network Connectivity Diagnosis ==="
    # Check inter-Pod communication
    for cluster in "${CLUSTERS[@]}"; do
        echo "Check network connectivity in $cluster..."
        kubectl config use-context $cluster
        kubectl run debug-pod --image=busybox --restart=Never --rm -it -- sh -c "
            ping -c 3 8.8.8.8
            nslookup kubernetes.default
        " 2>/dev/null || echo "网络测试失败"
    done
}

# Execute Diagnosis
diagnose_cluster_connectivity
diagnose_cross_cluster_services
diagnose_network_connectivity

echo "=== Diagnosis Complete ==="
```

## Best Practices for Production Environment

### Cluster Naming Conventions

```yaml
# Cluster Naming Conventions
clusters:
  # Environment-purpose-region-number
  production-customer-us-west-01:  # 生产客户集群-美国西部-01
    purpose: customer-facing
    sla: 99.99%
    
  staging-testing-us-east-01:      # 预发布测试集群-美国东部-01
    purpose: testing
    sla: 99.9%
    
  development-dev-us-west-01:      # 开发环境集群-美国西部-01
    purpose: development
    sla: 99%
```

### Version Management Strategy

```yaml
# Cluster Upgrade Plan
version_management:
  upgrade_schedule:
    - time: "2024-02-15T02:00:00Z"
      clusters: ["staging-cluster"]
      target_version: "v1.28.2"
      
    - time: "2024-02-22T02:00:00Z"
      clusters: ["production-cluster"]
      target_version: "v1.28.2"
      
  compatibility_matrix:
    kubernetes_versions: ["1.26", "1.27", "1.28"]
    supported_cnis: ["calico", "cilium", "flannel"]
    certified_platforms: ["aws", "gcp", "azure"]
```

---

**Table footer marker**: Kusheet Project, Author Allen Galler (allengaller@gmail.com)

---


## Obsidian Documentation

- domain-15-specialized-tech KUDIG Database — Global MOC
- [[domain-15-specialized-tech/README.md|Domain-10: Kubernetes Extended Ecosystem]]
- index.md|Domain-10 Extended and Customized — Index of Open Source Projects]
- CRD Custom Resource Definition Development Guide
- 02 - Operator Development Mode and Controller Implementation
- 03 - Admission Controller (Webhook) Configuration and Implementation
- Kubernetes API Aggregation Extension Mechanism Explained
- Package Management and Application Distribution Tools
- 47 - Helm Chart Development and Management
- 129 - Helm Advanced Operations: Complex Deployment, CI/CD Integration, and Security Best Practices
- CI/CD Pipeline
- 48 - GitOps Workflow

## See Also

- 12-service-mesh-advanced
- 13-kubernetes-operations-fundamentals
- 15-monitoring-alerting-system
- 16-security-compliance-management


<!-- risk-assessed -->
