---
title: 14 - Add-ons and Extensions Table
description: '| Component | Purpose | Deployment Method | Version Compatibility | Production Required | ACK Integration |'
summary: '| Component | Purpose | Deployment Method | Version Compatibility | Production Required | ACK Integration |'
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- prometheus
- grafana
- jaeger
- istio
- envoy
- cilium
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Platform Engineers
- Operations Engineers
estimated_read_time: 10min
intent_queries:
- What is Add-ons and Extensions Table
- How to use Add-ons and Extensions Table
- Kubernetes 9 platform ops best practices
trigger_keywords:
- Add-ons and Extensions Table
- platform
- ops
prerequisites:
- kubectl-basics
- platform-engineering-basics
- helm-basics
- service-mesh-basics
- prometheus-basics
- monitoring-basics
- gitops-basics
- ebpf-basics
- cilium-basics
- cni-basics
- kafka-basics
- redis-basics
- mysql-basics
- tls-basics
- policy-basics
- logging-basics
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
  path: ../domain-06-observability/
  label: 'Related Knowledge Domain: domain-06-observability'
- type: domain
  path: ../domain-15-specialized-tech/
  label: 'Related Knowledge Domain: domain-15-specialized-tech'
- type: domain
  path: ../domain-10-troubleshooting-diagnostics/
  label: 'Related Knowledge Domain: domain-10-troubleshooting-diagnostics'
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./build/24-addons-extensions.md
original_language: Chinese
---

> **Production Environment Security Notice**
>
> This document contains directly executable operations commands. Before execution, please confirm: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether it has been verified in a non-production environment. Command risk levels: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state, but usually reversible), 🟢 Low Risk/Read-Only (information gathering, no side effects).

# 14 - Add-ons and Extensions Table

> **Applicable Versions**: v1.25 - v1.32 | **Last Updated**: 2026-01 | **Reference**: [[entities/kubernetes.md|kubernetes]].io/docs/concepts/cluster-administration/addons](https://kubernetes.io/docs/concepts/cluster-administration/addons/)

<!-- chunk: Essential Add-ons -->
## Essential Add-ons

| Component | Purpose | Deployment Method | Version Compatibility | Production Required | ACK Integration |
|-----|------|---------|---------|---------|---------|
| **[[CoreDNS|CoreDNS]]** | Cluster DNS Service | Deployment | Synchronized with K8S | Yes | Auto-installed |
| **Metrics Server** | Resource Metrics API | Deployment | v0.7+ for v1.28+ | Yes (Required for HPA/VPA) | Optional Installation |
| **CNI Plugin** | Container Network | [[DaemonSet|DaemonSet]] | Depends on plugin | Yes | Terway/Flannel |
| **kube-proxy** | Service Network Proxy | DaemonSet | Synchronized with K8S | Yes | Auto-installed |
| **CSI Driver** | Storage Interface | DaemonSet+Deployment | Depends on driver | Yes (when using storage) | Cloud Disk/NAS CSI |

<!-- chunk: Observability Components -->
## Observability Components

| Component | Purpose | Deployment Method | Version Compatibility | Resource Requirements | ACK Alternative |
|-----|------|---------|---------|---------|---------|
| **Prometheus** | Metrics Collection and Storage | Operator/Helm | v2.45+ | Medium-High | ARMS Prometheus |
| **Grafana** | Metrics Visualization | Helm | v10+ | Low-Medium | Grafana Service |
| **Alertmanager** | Alert Management | Operator/Helm | Bundle with Prometheus | Low | ARMS Alerts |
| **Loki** | Log Aggregation | Helm | v2.9+ | Medium-High | SLS |
| **Jaeger** | Distributed Tracing | Operator/Helm | v1.50+ | Medium | Link Tracing Service |
| **kube-state-metrics** | K8S Object State Metrics | Deployment | v2.10+ | Low | ARMS Integration |
| **node-exporter** | Node Metrics | DaemonSet | v1.7+ | Very Low | Cloud Monitoring |

<!-- chunk: Ingress Controllers -->
## Ingress Controllers

| Component | Features | Deployment Method | Version Requirements | Production Recommended | ACK Integration |
|-----|------|---------|---------|---------|---------|
| **Nginx Ingress** | Full-featured, Active Community | Helm/YAML | v1.9+ | Yes | Supported |
| **Traefik** | Dynamic Configuration, Middleware | Helm | v2.10+ | Yes | - |
| **Kong Ingress** | API Gateway Features | Helm | v3.4+ | API Scenarios | - |
| **ALB Ingress** | Alibaba Cloud Native | Automatic | v1.25+ | ACK Recommended | Native |
| **Contour** | Envoy Proxy | YAML/Helm | v1.28+ | Yes | - |

<!-- chunk: Service Mesh -->
## Service Mesh

| Component | Features | Deployment Method | Version Requirements | Complexity | ACK Integration |
|-----|------|---------|---------|-------|---------|
| **Istio** | Most Comprehensive | istioctl/Helm | v1.20+ | High | ASM Managed |
| **Linkerd** | Lightweight, Low Resource | CLI/Helm | v2.14+ | Medium | - |
| **Cilium Service Mesh** | eBPF Native | Helm | v1.15+ | Medium | - |
| **Consul Connect** | Multi-environment Support | Helm | v1.17+ | Medium-High | - |

<!-- chunk: Security Components -->
## Security Components

| Component | Purpose | Deployment Method | Version Requirements | Features |
|-----|------|---------|---------|------|
| **cert-manager** | Automatic Certificate Management | Helm | v1.13+ | Auto Request/Renewal of Certificates |
| **External Secrets** | External Secret Synchronization | Helm | v0.9+ | Sync Vault/Cloud KMS |
| **Vault** | Secret Management | Helm | v1.15+ | Dynamic Secrets, Encryption as a Service |
| **Falco** | Runtime Security Monitoring | Helm | v0.37+ | Anomalous Behavior Detection |
| **OPA Gatekeeper** | Policy Enforcement | Helm | v3.14+ | Admission Policies |
| **Kyverno** | Policy Engine | Helm | v1.11+ | Resource Validation/Mutation |
| **Trivy Operator** | Vulnerability Scanning | Helm | v0.18+ | Image/Configuration Scanning |

<!-- chunk: GitOps/CD Components -->
## GitOps/CD Components

| Component | Purpose | Deployment Method | Version Requirements | Pattern | ACK Integration |
|-----|------|---------|---------|------|---------|
| **ArgoCD** | GitOps Continuous Delivery | Helm | v2.9+ | Pull | - |
| **Flux** | GitOps Toolkit | CLI | v2.2+ | Pull | - |
| **Tekton** | CI/CD Pipeline | YAML | v0.53+ | Pipeline | - |
| **Jenkins X** | K8S Native CI/CD | CLI | v3+ | Pipeline | - |

<!-- chunk: Auto Scaling Components -->
## Auto Scaling Components

| Component | Purpose | Deployment Method | Version Requirements | Features |
|-----|------|---------|---------|------|
| **Cluster Autoscaler** | Automatic Node Scaling | Deployment | v1.28+ | Scale Nodes Based on Pod Demands |
| **VPA** | Vertical Pod Auto Scaling | Deployment | v1.0+ | Automatically Adjust Resource Requests |
| **KEDA** | Event-driven Auto Scaling | Helm | v2.12+ | Scale Based on Events/Metrics |
| **Karpenter** | Fast Node Scaling | Helm | v0.33+ | Faster Node Provisioning |

<!-- chunk: Developer Tools -->
## Developer Tools

| Component | Purpose | Installation Method | Features |
|-----|------|---------|------|
| **Helm** | Package Manager | Binary | Chart Installation/Management |
| **Kustomize** | Configuration Customization | kubectl Built-in | Declarative Configuration Management |
| **Skaffold** | Development Workflow | Binary | Local Development Iteration |
| **Telepresence** | Local Development Debugging | Binary | Connect Local to Remote Cluster |
| **k9s** | Terminal UI | Binary | Interactive Cluster Management |
| **Lens** | Desktop IDE | Installation Package | Visual Management |
| **kubectx/kubens** | Context Switching | Binary | Quick Cluster/Namespace Switching |

<!-- chunk: Operator Frameworks -->
## Operator Frameworks

| Framework | Language | Features | Version Requirements |
|-----|------|------|---------|
| **Operator SDK** | Go/Ansible/Helm | Red Hat Official | v1.33+ |
| **Kubebuilder** | Go | K8S SIG Official | v3.14+ |
| **KUDO** | YAML | Declarative Operator | v0.19+ |
| **Metacontroller** | Any Language | Lambda-style Controller | v2.6+ |

<!-- chunk: Common Operators -->
## Common Operators

| Operator | Managed Object | Deployment Method | Production Maturity |
|---------|---------|---------|-----------|
| **Prometheus Operator** | Prometheus/Alertmanager | Helm | High |
| **Cert-Manager** | Certificate | Helm | High |
| **Strimzi** | Kafka | Helm/YAML | High |
| **MySQL Operator** | MySQL | Helm | Medium-High |
| **PostgreSQL Operator** | PostgreSQL | Helm | High |
| **Redis Operator** | Redis | Helm | Medium-High |
| **Elasticsearch Operator** | ES Cluster | Helm | High |
| **MongoDB Operator** | MongoDB | Helm | Medium-High |

<!-- chunk: Component Version Compatibility Matrix -->
## Component Version Compatibility Matrix

| Component | v1.28 | v1.29 | v1.30 | v1.31 | v1.32 |
|-----|-------|-------|-------|-------|-------|
| **Metrics Server** | v0.6+ | v0.7+ | v0.7+ | v0.7+ | v0.7+ |
| **Nginx Ingress** | v1.9+ | v1.9+ | v1.10+ | v1.10+ | v1.11+ |
| **cert-manager** | v1.13+ | v1.13+ | v1.14+ | v1.14+ | v1.15+ |
| **ArgoCD** | v2.8+ | v2.9+ | v2.10+ | v2.11+ | v2.12+ |
| **Prometheus** | v2.47+ | v2.48+ | v2.50+ | v2.52+ | v2.54+ |
| **Istio** | v1.19+ | v1.20+ | v1.21+ | v1.22+ | v1.23+ |

<!-- chunk: ACK Component Marketplace -->
## ACK Component Marketplace

| Component Category | Optional Components | Installation Method |
|---------|---------|---------|
| **Logging & Monitoring** | Logtail, ARMS, SLS | Console One-Click Installation |
| **Network** | Terway, Nginx Ingress, ALB | Select at Creation/Install Later |
| **Storage** | Cloud Disk CSI, NAS CSI, OSS CSI | Auto-installed |
| **Security** | Cloud Security Center, KMS | Console Configuration |
| **DevOps** | Cloud Efficiency, Jenkins | Console Installation |

<!-- chunk: Component Resource Consumption Assessment -->
## Component Resource Consumption Assessment

| Component | CPU Request | Memory Request | Storage Requirement | Node Count | Monthly Cost Estimate (ACK) |
|-----|--------|---------|---------|-------|---------------|
| **CoreDNS** | 100m | 70Mi | - | 2 Replicas | Included |
| **Metrics Server** | 100m | 300Mi | - | 1 Replica | Included |
| **Prometheus** | 1-4 Cores | 4-16Gi | 100-500Gi | 1 | 800-3000 CNY |
| **Grafana** | 100m | 128Mi | 10Gi | 1 | 50 CNY |
| **Loki** | 500m-2 Cores | 2-8Gi | 100-1000Gi | 1 | 500-2000 CNY |
| **Istio** | 1 Core | 2Gi | - | Control Plane 1 | 400 CNY |
| **ArgoCD** | 500m | 512Mi | 10Gi | 1 | 80 CNY |
| **cert-manager** | 100m | 128Mi | - | 1 | 20 CNY |
| **KEDA** | 100m | 128Mi | - | 1 | 20 CNY |
| **Nginx Ingress** | 200m/node | 256Mi/node | - | DaemonSet | Included in node cost |

<!-- chunk: Component Installation Priority Matrix -->
## Component Installation Priority Matrix

### P0 - Production Required (Install at cluster creation)

| Component | Purpose | Impact if Not Installed |
|-----|------|------------|
| **CoreDNS** | Service Discovery | Cluster cannot resolve services |
| **CNI Plugin** | Pod Network | Pods cannot communicate |
| **kube-proxy** | Service Proxy | Service unavailable |
| **CSI Driver** | Storage | Cannot use persistent storage |

### P1 - Operations Required (Install immediately after cluster creation)

| Component | Purpose | Installation Recommendation |
|-----|------|---------|
| **Metrics Server** | Resource Monitoring | Required for enabling HPA/VPA |
| **Ingress Controller** | Traffic Entry | Select based on north-south traffic needs |
| **Prometheus** | Metrics Monitoring | Or use ARMS as alternative |
| **Logging Component** | Log Collection | Loki or SLS |

### P2 - Enhanced Features (Install as needed)

| Component | Purpose | Installation Timing |
|-----|------|---------|
| **cert-manager** | Certificate Management | When using HTTPS |
| **ArgoCD/Flux** | GitOps | When adopting GitOps pattern |
| **Service Mesh** | Service Governance | When microservice complexity is high |
| **Cluster Autoscaler** | Automatic Node Scaling | When elasticity is needed |
| **VPA** | Pod Resource Optimization | When optimizing resource usage |
| **KEDA** | Event-driven Auto Scaling | With special scaling requirements |

### P3 - Advanced Features (Specific scenarios)

| Component | Purpose | Installation Timing |
|-----|------|---------|
| **Vault** | Secret Management | With strict security requirements |
| **Falco** | Runtime Security | With compliance requirements |
| **OPA Gatekeeper** | Policy Enforcement | Multi-tenant/Compliance |
| **Jaeger** | Distributed Tracing | Performance troubleshooting |

<!-- chunk: Component Deployment Best Practices -->
## Component Deployment Best Practices

### Prometheus Stack Production Configuration

```yaml
# Prometheus Operator Helm installation
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install prometheus prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  --set prometheus.prometheusSpec.retention=15d \
  --set prometheus.prometheusSpec.storageSpec.volumeClaimTemplate.spec.storageClassName=alicloud-disk-essd \
  --set prometheus.prometheusSpec.storageSpec.volumeClaimTemplate.spec.resources.requests.storage=200Gi \
  --set prometheus.prometheusSpec.resources.requests.cpu=2 \
  --set prometheus.prometheusSpec.resources.requests.memory=8Gi \
  --set grafana.persistence.enabled=true \
  --set grafana.persistence.storageClassName=alicloud-disk-essd \
  --set grafana.persistence.size=10Gi \
  --set alertmanager.alertmanagerSpec.storage.volumeClaimTemplate.spec.storageClassName=alicloud-disk-essd \
  --set alertmanager.alertmanagerSpec.storage.volumeClaimTemplate.spec.resources.requests.storage=10Gi

# Configure data retention policy
kubectl edit prometheuses.monitoring.coreos.com -n monitoring
# spec.retention: 15d
# spec.retentionSize: 180GB
```

### Nginx Ingress Controller Production Configuration

```yaml
# Helm installation
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx
helm install ingress-nginx ingress-nginx/ingress-nginx \
  --namespace ingress-nginx \
  --create-namespace \
  --set controller.replicaCount=3 \
  --set controller.resources.requests.cpu=500m \
  --set controller.resources.requests.memory=512Mi \
  --set controller.service.type=LoadBalancer \
  --set controller.service.annotations."service\.beta\.kubernetes\.io/alibaba-cloud-loadbalancer-spec"="slb.s3.medium" \
  --set controller.metrics.enabled=true \
  --set controller.metrics.serviceMonitor.enabled=true \
  --set controller.autoscaling.enabled=true \
  --set controller.autoscaling.minReplicas=3 \
  --set controller.autoscaling.maxReplicas=10 \
  --set controller.autoscaling.targetCPUUtilizationPercentage=80

# ConfigMap optimization
apiVersion: v1
kind: ConfigMap
metadata:
  name: ingress-nginx-controller
  namespace: ingress-nginx
data:
  allow-snippet-annotations: "false"  # Security: disable snippet
  enable-real-ip: "true"  # Get real IP
  proxy-body-size: "100m"  # Upload size limit
  proxy-connect-timeout: "15"
  proxy-read-timeout: "600"
  proxy-send-timeout: "600"
  use-gzip: "true"
  gzip-level: "5"
  client-header-buffer-size: "64k"
  large-client-header-buffers: "4 64k"
  ssl-protocols: "TLSv1.2 TLSv1.3"
  ssl-ciphers: "ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256"
```

### cert-manager Production Configuration

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend --dry-run or diff before confirming
> - `helm upgrade/install`: Deploy/upgrade release

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, please confirm target, scope of impact and authorization before execution
# Install cert-manager
helm repo add jetstack https://charts.jetstack.io
helm install cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.14.0 \
  --set installCRDs=true \
  --set global.leaderElection.namespace=cert-manager
```
```yaml
# Let's Encrypt ClusterIssuer (Production environment)
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: admin@example.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
    - http01:
        ingress:
          class: nginx
    # Or use DNS validation (support wildcard certificates)
    - dns01:
        aliDNS:
          accessKeyId: LTAI5t...
          accessKeySecretRef:
            name: alidns-secret
            key: accessKeySecret
          regionId: cn-hangzhou

---
# Ingress with automatic certificate issuance
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: app-ingress
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - app.example.com
    secretName: app-tls
  rules:
  - host: app.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: app-service
            port:
              number: 80
```

### ArgoCD GitOps Production Configuration

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend --dry-run or diff before confirming
> - `kubectl apply/create/replace`: Create/modify cluster resources

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, please confirm target, scope of impact and authorization before execution
# Install ArgoCD
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml

# Expose with Ingress
cat <<EOF | kubectl apply -f -
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: argocd-server
  namespace: argocd
  annotations:
    cert-manager.io/cluster-issuer: letsencrypt-prod
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/backend-protocol: "HTTPS"
spec:
  ingressClassName: nginx
  tls:
  - hosts:
    - argocd.example.com
    secretName: argocd-tls
  rules:
  - host: argocd.example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: argocd-server
            port:
              number: 443
EOF

# Get initial password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```
<!-- chunk: Component Upgrade Strategy -->
## Component Upgrade Strategy

| Component Type | Upgrade Frequency | Upgrade Method | Rollback Plan |
|---------|---------|---------|---------|
| **Core Components** | With K8S Upgrade | Automatic at cluster upgrade | Cluster rollback |
| **Monitoring Components** | Quarterly | Helm upgrade | Helm rollback |
| **Ingress** | Semi-annually | Canary upgrade | Rollback image version |
| **GitOps** | Semi-annually | Blue-green deployment | Switch traffic |
| **Service Mesh** | Annually | Canary upgrade | Uninstall Sidecar |

### Helm Component Upgrade Commands

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend --dry-run or diff before confirming
> - `helm upgrade/install`: Deploy/upgrade release

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, please confirm target, scope of impact and authorization before execution
# Check available upgrade versions
helm repo update
helm search repo <chart-name> --versions

# Backup before upgrade
helm get values <release-name> -n <namespace> > values-backup.yaml

# Execute upgrade
helm upgrade <release-name> <chart> -n <namespace> \
  -f values-backup.yaml \
  --version <new-version>

# Verify upgrade
helm list -n <namespace>
kubectl get pods -n <namespace> -w

# Rollback
helm rollback <release-name> <revision> -n <namespace>
```
<!-- chunk: Component Monitoring and Alerting -->
## Component Monitoring and Alerting

### Key Metrics

```yaml
# Prometheus alert rules
groups:
- name: addon_alerts
  rules:
  # CoreDNS monitoring
  - alert: CoreDNSDown
    expr: up{job="kube-dns"} == 0
    for: 3m
    labels:
      severity: critical
    annotations:
      summary: "CoreDNS is down"
      
  # Ingress Controller monitoring
  - alert: IngressControllerDown
    expr: up{job="ingress-nginx"} == 0
    for: 3m
    labels:
      severity: critical
      
  - alert: IngressHighErrorRate
    expr: rate(nginx_ingress_controller_requests{status=~"5.."}[5m]) > 0.05
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "Ingress 5xx error rate > 5%"
      
  # Metrics Server monitoring
  - alert: MetricsServerDown
    expr: up{job="metrics-server"} == 0
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "Metrics Server is down, HPA/VPA unavailable"
      
  # cert-manager monitoring
  - alert: CertificateExpiringSoon
    expr: certmanager_certificate_expiration_timestamp_seconds - time() < 7*24*3600
    for: 1h
    labels:
      severity: warning
    annotations:
      summary: "Certificate {{ $labels.name }} expires in < 7 days"
```

<!-- chunk: Component Troubleshooting -->
## Component Troubleshooting

### General Troubleshooting Steps

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, please confirm target, scope of impact and authorization before execution
# 1. Check Pod status
kubectl get pods -n <namespace> -o wide

# 2. View Pod events
kubectl describe pod <pod-name> -n <namespace>

# 3. View logs
kubectl logs <pod-name> -n <namespace> --tail=100 -f

# 4. Check resource quota
kubectl top pods -n <namespace>
kubectl describe resourcequota -n <namespace>

# 5. Check network connectivity
kubectl run -it --rm debug --image=busybox --restart=Never -- sh
wget -O- http://<service>.<namespace>.svc.cluster.local
```
### Ingress Troubleshooting

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend --dry-run or diff before confirming
> - `kubectl exec`: Enter container to execute commands, may change container state

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, please confirm target, scope of impact and authorization before execution
# Check Ingress configuration
kubectl get ingress -A
kubectl describe ingress <ingress-name> -n <namespace>

# Check Ingress Controller logs
kubectl logs -n ingress-nginx -l app.kubernetes.io/component=controller --tail=100 -f

# Check backend Service and Endpoints
kubectl get svc <service-name> -n <namespace>
kubectl get endpoints <service-name> -n <namespace>

# Test Ingress Controller configuration
kubectl exec -n ingress-nginx <controller-pod> -- nginx -T
```
<!-- chunk: ACK Component Marketplace Extension -->
## ACK Component Marketplace Extension

### ACK Native Component Advantages

| Component | ACK Native | Open Source Version | Advantages |
|-----|---------|---------|------|
| **Logging Service** | SLS Integration | ELK/Loki | Operation-free, Pay-as-you-go |
| **Monitoring Service** | ARMS | Prometheus | Managed, Automatic Alerting |
| **Ingress** | ALB Ingress | Nginx Ingress | Native Integration, High Performance |
| **Network Plugin** | Terway | Calico/Flannel | High Performance, ENI Direct Pass-through |
| **Storage** | CSI Auto-installed | Manual Installation | Auto-configured |

### ACK Component One-Click Installation

```bash
# Install components through ACK console "Application Marketplace"
# Or use aliyun CLI

# Install ARMS Prometheus
aliyun cs InstallClusterAddons \
  --ClusterId <cluster-id> \
  --Addons '[{"name":"arms-prometheus"}]'

# Install SLS logging component
aliyun cs InstallClusterAddons \
  --ClusterId <cluster-id> \
  --Addons '[{"name":"logtail-ds","config":{"sls_project":"k8s-log-<cluster-id>"}}]'

# Install Nginx Ingress
aliyun cs InstallClusterAddons \
  --ClusterId <cluster-id> \
  --Addons '[{"name":"nginx-ingress-controller"}]'
```

<!-- chunk: Component Security Hardening -->
## Component Security Hardening

### Image Security

```yaml
# Use ImagePolicyWebhook to restrict image sources
apiVersion: v1
kind: Pod
metadata:
  name: app
spec:
  containers:
  - name: app
    image: registry.cn-hangzhou.aliyuncs.com/namespace/image:tag  # Only allow enterprise image repository
```

### Network Isolation

```yaml
# NetworkPolicy to isolate component namespaces
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: deny-external-egress
  namespace: monitoring
spec:
  podSelector: {}
  policyTypes:
  - Egress
  egress:
  - to:
    - namespaceSelector: {}  # Only allow cluster-internal communication
  - to:  # Allow DNS
    - namespaceSelector:
        matchLabels:
          name: kube-system
    ports:
    - protocol: UDP
      port: 53
```

### RBAC Permission Control

```yaml
# Component-specific ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: prometheus
  namespace: monitoring

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: prometheus
rules:
- apiGroups: [""]
  resources: ["nodes", "nodes/metrics", "services", "endpoints", "pods"]
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["get"]

---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: prometheus
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: prometheus
subjects:
- kind: ServiceAccount
  name: prometheus
  namespace: monitoring
```

---

**Component Selection Principles**: Install as needed, avoid excess, focus on compatibility, monitoring first, security hardening

---

**Table Maintenance**: Kusheet Project | **Author**: Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian Related Documentation -->
## Obsidian Related Documentation

- domain-07-platform-engineering MOC
- [[domain-07-platform-engineering/README.md|Platform Ops Domain]]
- Domain-9 Platform Ops — Open Source Project Index
- Platform Ops Overview
- Cluster Lifecycle Management
- Capacity Planning & Resource Assessment
- Performance Benchmarking & Tuning
- Operations Metrics System
- Monitoring and Alerting System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization & FinOps

## See Also

- 22-client-libraries
- 23-cli-enhancement-tools
- 25-virtual-clusters
- 26-kubectl-plugin-ecosystem

<!-- risk-assessed -->