---
title: GitOps Configuration Management
description: GitOps Configuration Management
summary: GitOps is a Git-based operations philosophy and practice that achieves declarative configuration management and automated deployment workflows by storing infrastructure and application configurations in Git repositories.
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./operate/07-gitops-configuration-management.md
original_language: Chinese
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- helm
- argocd
- flux
- ingress
- rbac
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
- What is GitOps Configuration Management
- How to implement GitOps Configuration Management
- Kubernetes platform ops best practices
trigger_keywords:
- GitOps Configuration Management
- GitOps
- Configuration
- Management
- platform
- ops
prerequisites:
- kubectl-basics
- platform-engineering-basics
- helm-basics
- gitops-basics
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
---

> **Production Environment Security Notice**
>
> This document contains directly executable operations commands. Before execution, please confirm: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether it has been validated in a non-production environment. Command risk levels: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state, but usually recoverable), 🟢 Low risk/read-only (information collection, no side effects).




# GitOps Configuration Management

<!-- chunk: Overview -->
## Overview

GitOps is a Git-based operations philosophy and practice that achieves declarative configuration management and automated deployment workflows by storing infrastructure and application configurations in Git repositories.

<!-- chunk: Core Concepts -->
## Core Concepts

### Declarative Configuration
```
Desired State (Declarative) → Actual State → Automatic Sync
```

### Git as Single Source of Truth
- All configuration changes are submitted via Git
- Complete change history and audit trail
- Pull Request-based collaboration workflow

### Automated Synchronization
- Continuous monitoring of differences between actual and desired state
- Automatic application of configuration changes
- Automatic detection and remediation of state drift

<!-- chunk: ArgoCD Implementation -->
## ArgoCD Implementation

### Architecture Components
```
Git Repository → ArgoCD Server → Kubernetes Cluster
     ↑                ↓
Web UI/CLI ← Status Monitoring ← Health Checks
```

### Core Components
```yaml
# ArgoCD Deployment Configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: argocd-server
spec:
  replicas: 2
  selector:
    matchLabels:
      app: argocd-server
  template:
    metadata:
      labels:
        app: argocd-server
    spec:
      containers:
      - name: argocd-server
        image: quay.io/argoproj/argocd:v2.7.0
        ports:
        - containerPort: 8080
        - containerPort: 8083
        command:
        - argocd-server
        - --insecure
        - --staticassets
        - /shared/app
```

### Application Configuration
```yaml
# Application Definition Example
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: guestbook
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/argoproj/argocd-example-apps.git
    targetRevision: HEAD
    path: guestbook
  destination:
    server: https://kubernetes.default.svc
    namespace: guestbook
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
    - CreateNamespace=true
  ignoreDifferences:
  - group: apps
    kind: Deployment
    jsonPointers:
    - /spec/replicas
```

### Project Management
```yaml
# Project Configuration
apiVersion: argoproj.io/v1alpha1
kind: AppProject
metadata:
  name: production
  namespace: argocd
spec:
  description: Production project
  sourceRepos:
  - 'https://github.com/myorg/production-apps.git'
  destinations:
  - namespace: 'production-*'
    server: https://kubernetes.default.svc
  clusterResourceWhitelist:
  - group: '*'
    kind: '*'
  namespaceResourceBlacklist:
  - group: ''
    kind: ResourceQuota
  roles:
  - name: app-developer
    policies:
    - p, proj:production:app-developer, applications, get, production/*, allow
    - p, proj:production:app-developer, applications, sync, production/*, allow
    groups:
    - myorg:app-developers
```

<!-- chunk: FluxCD Implementation -->
## FluxCD Implementation

### Core Components
```yaml
# FluxCD Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flux
spec:
  replicas: 1
  selector:
    matchLabels:
      name: flux
  template:
    metadata:
      labels:
        name: flux
    spec:
      serviceAccountName: flux
      volumes:
      - name: git-key
        secret:
          secretName: flux-git-deploy
      containers:
      - name: flux
        image: fluxcd/flux:1.25.0
        ports:
        - containerPort: 3030
        volumeMounts:
        - name: git-key
          mountPath: /etc/fluxd/ssh
          readOnly: true
        args:
        - --git-url=git@github.com:myorg/myrepo
        - --git-path=clusters/production
        - --git-branch=main
        - --sync-garbage-collection
```

### HelmRelease Configuration
```yaml
# Helm Release Management
apiVersion: helm.fluxcd.io/v1
kind: HelmRelease
metadata:
  name: podinfo
  namespace: default
spec:
  releaseName: podinfo
  chart:
    repository: https://stefanprodan.github.io/podinfo
    name: podinfo
    version: 4.0.6
  values:
    replicaCount: 2
    image:
      repository: stefanprodan/podinfo
      tag: 5.0.3
    service:
      type: ClusterIP
      port: 9898
  rollback:
    enable: true
    retries: 5
  timeout: 300
```

### Kustomize Configuration
```yaml
# kustomization.yaml
apiVersion: kustomize.config.k8s.io/v1beta1
kind: Kustomization

resources:
- deployment.yaml
- service.yaml
- ingress.yaml

namespace: production

commonLabels:
  app: myapp
  version: v1.0.0

images:
- name: myapp
  newName: myregistry/myapp
  newTag: v1.0.0

patchesStrategicMerge:
- patch-deployment.yaml
```

<!-- chunk: Configuration Repository Structure -->
## Configuration Repository Structure

### Standard Directory Structure
```
infrastructure/
├── base/
│   ├── kustomization.yaml
│   ├── namespace.yaml
│   └── rbac/
├── overlays/
│   ├── dev/
│   ├── staging/
│   └── prod/
applications/
├── app1/
│   ├── base/
│   └── overlays/
└── app2/
    ├── base/
    └── overlays/
clusters/
├── dev/
│   ├── infrastructure.yaml
│   └── applications.yaml
├── staging/
└── prod/
```

### Environment-Specific Configuration
```yaml
# base/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 1
  template:
    spec:
      containers:
      - name: myapp
        image: myapp:latest
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"

---
# overlays/prod/deployment-patch.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  template:
    spec:
      containers:
      - name: myapp
        resources:
          requests:
            memory: "256Mi"
            cpu: "500m"
          limits:
            memory: "512Mi"
            cpu: "1000m"
```

<!-- chunk: Security Best Practices -->
## Security Best Practices

### Access Control
```yaml
# RBAC Configuration
apiVersion: v1
kind: ServiceAccount
metadata:
  name: argocd-manager
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: argocd-manager-role
rules:
- apiGroups:
  - '*'
  resources:
  - '*'
  verbs:
  - '*'
- nonResourceURLs:
  - '*'
  verbs:
  - '*'
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: argocd-manager-role-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: argocd-manager-role
subjects:
- kind: ServiceAccount
  name: argocd-manager
  namespace: kube-system
```

### Secret Management
```yaml
# SealedSecret Configuration
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: my-secret
  namespace: production
spec:
  encryptedData:
    username: AgBy3i4OJSWK+PiTySYZZA9rO43cGDEq.....
    password: AgBy3i4OJDTXkT2TTUTyyrws9B6CGi....
  template:
    metadata:
      name: my-secret
      namespace: production
    data:
      username: ""
      password: ""
```

### Signature Verification
```yaml
# Cosign Signature Verification
apiVersion: image.toolkit.fluxcd.io/v1beta2
kind: ImagePolicy
metadata:
  name: podinfo
spec:
  imageRepositoryRef:
    name: podinfo
  policy:
    semver:
      range: 5.0.x
  verification:
    provider: cosign
    secretRef:
      name: cosign-pub
```

<!-- chunk: Deployment Strategy -->
## Deployment Strategy

### Blue-Green Deployment
```yaml
# Blue-Green Deployment Configuration
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: blue-green-app
spec:
  source:
    repoURL: https://github.com/myorg/blue-green-demo.git
    targetRevision: HEAD
    path: blue-green
  destination:
    server: https://kubernetes.default.svc
    namespace: blue-green
  syncPolicy:
    syncOptions:
    - CreateNamespace=true
  strategy:
    blueGreen:
      activeService: active-service
      previewService: preview-service
      autoPromotionEnabled: false
```

### Canary Release
```yaml
# Flagger Canary Deployment
apiVersion: flagger.app/v1beta1
kind: Canary
metadata:
  name: podinfo
spec:
  targetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: podinfo
  service:
    port: 9898
    targetPort: 9898
  analysis:
    interval: 1m
    threshold: 10
    maxWeight: 50
    stepWeight: 5
    metrics:
    - name: request-success-rate
      thresholdRange:
        min: 99
      interval: 1m
    - name: request-duration
      thresholdRange:
        max: 500
      interval: 1m
```

<!-- chunk: Monitoring and Alerting -->
## Monitoring and Alerting

### ArgoCD Health Check
```yaml
# Health Check Configuration
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: health-check-app
spec:
  ignoreDifferences:
  - group: apps
    kind: Deployment
    jsonPointers:
    - /spec/replicas
  info:
  - name: url
    value: https://myapp.example.com
```

### Deployment Status Monitoring
```promql
# ArgoCD Metrics Queries
argocd_app_info{namespace="argocd", dest_namespace="production"}
argocd_app_sync_total{namespace="argocd"}
argocd_app_sync_status{namespace="argocd", status="Synced"}
```

<!-- chunk: Best Practices -->
## Best Practices

### 1. Configuration Management Principles
- Use declarative rather than imperative configuration
- Maintain idempotency and repeatability of configurations
- Implement configuration version control and change audits

### 2. Security Considerations
- Configure RBAC following the principle of least privilege
- Encrypt sensitive information in storage
- Regularly rotate keys and certificates

### 3. Deployment Strategy
- Progressive validation through canary releases
- Safeguard with automatic rollback mechanisms
- Ensure consistency across multiple environments

### 4. Monitoring and Alerting
- Real-time synchronization status monitoring
- Track deployment success rates
- Alert on configuration drift detection

Through GitOps practices, you can achieve standardized management of infrastructure and application configurations, improve deployment reliability and traceability, and reduce operational complexity.

---

<!-- chunk: Obsidian Related Documents -->
## Obsidian Related Documents

- domain-07-platform-engineering KUDIG Database — Global MOC
- [[domain-07-platform-engineering/README.md|[[Platform Ops Domain|Platform Ops Domain]]]]
- index.md|Domain-7 Platform Operations — Open Source Project Index]]
- Platform Operations Overview
- Cluster Lifecycle Management
- [[domain-07-platform-engineering/governance/03-capacity-planning-resource-assessment.md|03 capacity planning resource assessment]]
- Performance Benchmarking & Tuning
- Operations Metrics System
- Monitoring and Alerting System
- Operations Automation Toolchain
- Cost Optimization & FinOps
- Security & Compliance Management

## See Also

- 05-operations-metrics-system
- 06-monitoring-alerting-system
- 08-automation-toolchain
- 09-cost-optimization-finops

## Related

- [[domain-19-landscape-references/topic-index/gitops-cicd-index.md|GitOps / CI-CD Global Index]]


<!-- risk-assessed -->