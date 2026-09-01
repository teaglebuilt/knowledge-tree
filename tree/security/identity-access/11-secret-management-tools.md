---
title: 11 - Secret and Sensitive Information Management Tools
description: '# 11 - Secret and Sensitive Information Management Tools'
summary: 'preferredDuringSchedulingIgnoredDuringExecution:'
category: security
tags:
- k8s
- security
- rbac
- authentication
- authorization
- etcd
- apiserver
- prometheus
- grafana
- helm
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- Security Engineer
- SRE
- Architect
estimated_read_time: 5min
intent_queries:
- What are Secret and Sensitive Information Management Tools
- How to use Secret and Sensitive Information Management Tools
- Kubernetes 7 security best practices
trigger_keywords:
- Secret and Sensitive Information Management Tools
- security
prerequisites:
- kubectl-basics
- rbac-basics
- helm-basics
- prometheus-basics
- monitoring-basics
- gitops-basics
- etcd-basics
- tls-basics
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
  path: ../domain-06-observability/
  label: 'Related Knowledge Domain: domain-06-observability'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/tls-pki.md
  label: 'Cheat sheet: tls-pki'
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-05-security-compliance/01-identity-access/11-secret-management-tools.md
---

> **Production Environment Security Warning**
>
> This document contains directly executable operations commands. Before executing, please confirm: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether verification has been completed in a non-production environment. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state but usually recoverable), 🟢 Low Risk/Read-only (information gathering, no side effects).




# 11 - Secret and Sensitive Information Management Tools

> **Applicable Versions**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **Difficulty**: Advanced | **Reference**: External Secretsts|Secrets]]](https://external-secrets.io/) | HashiCorp Vault](https://developer.hashicorp.com/vault) | [Sealed Secrets](https://sealed-secrets.netlify.app/)

<!-- chunk: 一、密钥管理架构全景 -->
## 1. Secret Management Architecture Overview

### 1.1 Enterprise-Grade Secret Management Architecture

```
# 🟢 Low Risk: Read-only/information gathering, typically no side effects
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                      Enterprise Secret Management Architecture                       │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌────────────────────────────────────────────────────────────────────────────────┐ │
│  │                           External Secret Stores                                │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │ │
│  │  │  HashiCorp   │  │   AWS        │  │   Azure      │  │   GCP        │       │ │
│  │  │    Vault     │  │   Secrets    │  │   Key Vault  │  │   Secret     │       │ │
│  │  │              │  │   Manager    │  │              │  │   Manager    │       │ │
│  │  │  ┌────────┐  │  │  ┌────────┐  │  │  ┌────────┐  │  │  ┌────────┐  │       │ │
│  │  │  │ KV V2  │  │  │  │Secrets │  │  │  │ Keys   │  │  │  │Versions│  │       │ │
│  │  │  │ PKI    │  │  │  │Rotation│  │  │  │Secrets │  │  │  │ IAM    │  │       │ │
│  │  │  │ Transit│  │  │  │  IAM   │  │  │  │Certs   │  │  │  │Rotation│  │       │ │
│  │  │  │ SSH    │  │  │  │  KMS   │  │  │  │  RBAC  │  │  │  │ Labels │  │       │ │
│  │  │  └────────┘  │  │  └────────┘  │  │  └────────┘  │  │  └────────┘  │       │ │
│  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘       │ │
│  └─────────┼─────────────────┼─────────────────┼─────────────────┼────────────────┘ │
│            │                 │                 │                 │                  │
│            └─────────────────┴─────────────────┴─────────────────┘                  │
│                                       │                                             │
│  ┌────────────────────────────────────▼───────────────────────────────────────────┐ │
│  │                        Secret Sync Controllers                                  │ │
│  │  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐              │ │
│  │  │ External Secrets │  │  Sealed Secrets  │  │   Vault Agent    │              │ │
│  │  │    Operator      │  │   Controller     │  │    Injector      │              │ │
│  │  │                  │  │                  │  │                  │              │ │
│  │  │ - Multi-provider │  │ - GitOps native  │  │ - Sidecar mode   │              │ │
│  │  │ - Auto-refresh   │  │ - Asymmetric enc │  │ - Template       │              │ │
│  │  │ - Templating     │  │ - Cluster-wide   │  │ - Dynamic creds  │              │ │
│  │  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘              │ │
│  └───────────┼─────────────────────┼─────────────────────┼────────────────────────┘ │
│              │                     │                     │                          │
│              └─────────────────────┴─────────────────────┘                          │
│                                    │                                                │
│  ┌─────────────────────────────────▼──────────────────────────────────────────────┐ │
│  │                          Kubernetes Secrets                                     │ │
│  │  ┌─────────────────────────────────────────────────────────────────────────┐   │ │
│  │  │                    Native K8s Secret (etcd encrypted)                   │   │ │
│  │  │  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐            │   │ │
│  │  │  │  Opaque   │  │   TLS     │  │ dockercfg │  │  SA Token │            │   │ │
│  │  │  │  Secrets  │  │  Secrets  │  │  Secrets  │  │  Secrets  │            │   │ │
│  │  │  └───────────┘  └───────────┘  └───────────┘  └───────────┘            │   │ │
│  │  └─────────────────────────────────────────────────────────────────────────┘   │ │
│  └────────────────────────────────────────────────────────────────────────────────┘ │
│                                    │                                                │
│  ┌─────────────────────────────────▼──────────────────────────────────────────────┐ │
│  │                         Application Consumption                                 │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │ │
│  │  │   Volume     │  │    Env       │  │   CSI        │  │   Sidecar    │       │ │
│  │  │   Mount      │  │   Variable   │  │   Driver     │  │   Injection  │       │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘       │ │
│  └────────────────────────────────────────────────────────────────────────────────┘ │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```
### 1.2 Comprehensive Comparison of Secret Management Solutions

| Solution | Architecture Mode | Multi-Cloud Support | Dynamic Secrets | GitOps | Audit | Complexity | Use Cases |
|-----|---------|---------|---------|-------|------|-------|---------|
| **External Secrets Operator** | Sync Controller | ★★★★★ | ✓ | ★★★★☆ | ★★★☆☆ | Medium | Multi-cloud/Hybrid Cloud |
| **HashiCorp Vault** | External Secret Repository | ★★★★☆ | ★★★★★ | ★★★☆☆ | ★★★★★ | High | Enterprise Security |
| **Sealed Secrets** | Encryption Controller | ★☆☆☆☆ | ✗ | ★★★★★ | ★★☆☆☆ | Low | GitOps Workflow |
| **[[SOPS|SOPS]]** | File Encryption | ★★★★☆ | ✗ | ★★★★★ | ★★☆☆☆ | Low | Small Teams |
| **AWS Secrets Manager** | Managed Service | AWS only | ★★★★★ | ★★★☆☆ | ★★★★★ | Low | AWS Native |
| **Azure Key Vault** | Managed Service | Azure only | ★★★★☆ | ★★★☆☆ | ★★★★★ | Low | Azure Native |
| **GCP Secret Manager** | Managed Service | GCP only | ★★★★☆ | ★★★☆☆ | ★★★★★ | Low | GCP Native |
| **CyberArk Conjur** | Enterprise Solution | ★★★★★ | ★★★★★ | ★★★☆☆ | ★★★★★ | High | Large Enterprises |

### 1.3 Secret Types and Security Levels

| Secret Type | Security Level | Rotation Period | Storage Recommendation | Access Control |
|---------|---------|---------|---------|---------|
| **Database Credentials** | High | 30 days | Vault/Cloud KMS | Application-specific |
| **API Keys** | High | 90 days | ESO Sync | Service Account |
| **TLS Certificates** | High | 365 days | cert-manager | Namespace Isolation |
| **SSH Keys** | High | Issuance-based | Vault SSH | Dynamic Issuance |
| **Configuration Keys** | Medium | As needed | Sealed Secrets | RBAC Control |
| **Encryption Keys** | Extremely High | As needed | HSM/CloudHSM | Least Privilege |

---

<!-- chunk: 二、External Secrets Operator -->
## 2. External Secrets Operator

### 2.1 ESO Architecture and Deployment

```yaml
# External Secrets Operator Installation
apiVersion: v1
kind: Namespace
metadata:
  name: external-secrets
---
# Install with Helm
# helm repo add external-secrets https://charts.external-secrets.io
# helm install external-secrets external-secrets/external-secrets -n external-secrets
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: external-secrets
  namespace: external-secrets
spec:
  replicas: 2
  selector:
    matchLabels:
      app: external-secrets
  template:
    metadata:
      labels:
        app: external-secrets
    spec:
      serviceAccountName: external-secrets
      containers:
      - name: external-secrets
        image: ghcr.io/external-secrets/external-secrets:v0.9.11
        args:
        - --concurrent=5
        - --metrics-addr=:8080
        - --health-probe-bind-address=:8081
        - --enable-leader-election
        - --loglevel=info
        
        ports:
        - containerPort: 8080
          name: metrics
        - containerPort: 8081
          name: health
        
        resources:
          requests:
            cpu: 100m
            memory: 256Mi
          limits:
            cpu: 500m
            memory: 512Mi
        
        livenessProbe:
          httpGet:
            path: /healthz
            port: 8081
          initialDelaySeconds: 15
          periodSeconds: 20
        
        readinessProbe:
          httpGet:
            path: /readyz
            port: 8081
          initialDelaySeconds: 5
          periodSeconds: 10
        
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          runAsNonRoot: true
          capabilities:
            drop: ["ALL"]
      
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
          - weight: 100
            podAffinityTerm:
              labelSelector:
                matchLabels:
                  app: external-secrets
              topologyKey: kubernetes.io/hostname
```

### 2.2 Multi-Cloud SecretStore Configuration

```yaml
# ========================
# AWS Secrets Manager
# ========================
apiVersion: external-secrets.io/v1beta1
kind: ClusterSecretStore
metadata:
  name: aws-secrets-manager
spec:
  provider:
    aws:
      service: SecretsManager
      region: us-west-2
      auth:
        jwt:
          serviceAccountRef:
            name: external-secrets-sa
            namespace: external-secrets
---
# ========================
# Azure Key Vault
# ========================
apiVersion: external-secrets.io/v1beta1
kind: ClusterSecretStore
metadata:
  name: azure-keyvault
spec:
  provider:
    azurekv:
      tenantId: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
      vaultUrl: "https://my-vault.vault.azure.net"
      authType: ManagedIdentity
      identityId: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
---
# ========================
# GCP Secret Manager
# ========================
apiVersion: external-secrets.io/v1beta1
kind: ClusterSecretStore
metadata:
  name: gcp-secret-manager
spec:
  provider:
    gcpsm:
      projectID: my-gcp-project
      auth:
        workloadIdentity:
          clusterLocation: us-central1
          clusterName: my-cluster
          clusterProjectID: my-gcp-project
          serviceAccountRef:
            name: external-secrets-gcp-sa
            namespace: external-secrets
---
# ========================
# HashiCorp Vault
# ========================
apiVersion: external-secrets.io/v1beta1
kind: ClusterSecretStore
metadata:
  name: vault-backend
spec:
  provider:
    vault:
      server: "https://vault.example.com:8200"
      path: "secret"
      version: "v2"
      namespace: "admin"
      caProvider:
        type: ConfigMap
        name: vault-ca
        namespace: external-secrets
        key: ca.crt
      auth:
        kubernetes:
          mountPath: "kubernetes"
          role: "external-secrets"
          serviceAccountRef:
            name: external-secrets-vault-sa
            namespace: external-secrets
---
# ========================
# Alibaba Cloud KMS
# ========================
apiVersion: external-secrets.io/v1beta1
kind: SecretStore
metadata:
  name: alicloud-kms
  namespace: production
spec:
  provider:
    alibaba:
      regionID: cn-hangzhou
      auth:
        secretRef:
          accessKeyIDSecretRef:
            name: alicloud-credentials
            key: access-key-id
          accessKeySecretSecretRef:
            name: alicloud-credentials
            key: access-key-secret
```

### 2.3 ExternalSecret Advanced Configuration

```yaml
# Basic ExternalSecret
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: database-credentials
  namespace: production
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: aws-secrets-manager
    kind: ClusterSecretStore
  
  target:
    name: db-secret
    creationPolicy: Owner
    deletionPolicy: Retain
    template:
      type: Opaque
      metadata:
        labels:
          app: myapp
          managed-by: external-secrets
      data:
        # Using template syntax
        connection-string: |
          postgresql://{{ .username }}:{{ .password }}@{{ .host }}:5432/{{ .database }}?sslmode=require
  
  data:
  - secretKey: username
    remoteRef:
      key: prod/database
      property: username
  - secretKey: password
    remoteRef:
      key: prod/database
      property: password
  - secretKey: host
    remoteRef:
      key: prod/database
      property: host
  - secretKey: database
    remoteRef:
      key: prod/database
      property: database
---
# Using dataFrom to fetch all key-value pairs
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: app-config
  namespace: production
spec:
  refreshInterval: 30m
  secretStoreRef:
    name: aws-secrets-manager
    kind: ClusterSecretStore
  
  target:
    name: app-config-secret
    creationPolicy: Owner
  
  dataFrom:
  - extract:
      key: prod/app-config
  - find:
      name:
        regexp: "^prod/features/.*"
      tags:
        environment: production
---
# Multi-source aggregation
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: multi-source-secret
  namespace: production
spec:
  refreshInterval: 1h
  
  target:
    name: aggregated-secrets
    creationPolicy: Owner
  
  data:
  # Fetch from AWS
  - secretKey: aws-api-key
    sourceRef:
      storeRef:
        name: aws-secrets-manager
        kind: ClusterSecretStore
    remoteRef:
      key: prod/api-keys
      property: aws
  
  # Fetch from Vault
  - secretKey: db-password
    sourceRef:
      storeRef:
        name: vault-backend
        kind: ClusterSecretStore
    remoteRef:
      key: database/creds/myapp
      property: password
  
  # Fetch from GCP
  - secretKey: gcp-service-account
    sourceRef:
      storeRef:
        name: gcp-secret-manager
        kind: ClusterSecretStore
    remoteRef:
      key: service-account-key
---
# PushSecret - Reverse sync to external storage
apiVersion: external-secrets.io/v1alpha1
kind: PushSecret
metadata:
  name: push-to-vault
  namespace: production
spec:
  refreshInterval: 10m
  secretStoreRefs:
  - name: vault-backend
    kind: ClusterSecretStore
  
  selector:
    secret:
      name: local-generated-secret
  
  data:
  - matchers:
    - secretKey="api-key"
    - remoteRef=""
    - remoteKey="prod/generated/api-key"
```

### 2.4 ESO Monitoring and Alerting

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: external-secrets-alerts
  namespace: external-secrets
spec:
  groups:
  - name: external-secrets
    rules:
    # Secret sync failed
    - alert: ExternalSecretSyncFailed
      expr: |
        externalsecret_status_condition{condition="Ready", status="False"} == 1
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "ExternalSecret sync failed"
        description: "Secret {{ $labels.namespace }}/{{ $labels.name }} sync failed"
    
    # SecretStore unhealthy
    - alert: SecretStoreUnhealthy
      expr: |
        secretstore_status_condition{condition="Ready", status="False"} == 1
      for: 2m
      labels:
        severity: critical
      annotations:
        summary: "SecretStore unhealthy"
        description: "SecretStore {{ $labels.namespace }}/{{ $labels.name }} status abnormal"
    
    # Sync delay
    - alert: ExternalSecretSyncDelay
      expr: |
        time() - externalsecret_status_sync_time > 7200
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "ExternalSecret sync delay"
        description: "Secret {{ $labels.namespace }}/{{ $labels.name }} not synced for more than 2 hours"
    
    # Controller restart
    - alert: ExternalSecretsControllerRestart
      expr: |
        increase(kube_pod_container_status_restarts_total{
          namespace="external-secrets",
          container="external-secrets"
        }[1h]) > 3
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "ESO controller frequent restart"
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: eso-grafana-dashboard
  namespace: monitoring
  labels:
    grafana_dashboard: "1"
data:
  external-secrets.json: |
    {
      "dashboard": {
        "title": "External Secrets Operator",
        "panels": [
          {
            "title": "Secret Sync Status",
            "type": "stat",
            "targets": [{
              "expr": "count(externalsecret_status_condition{condition=\"Ready\", status=\"True\"})"
            }]
          },
          {
            "title": "Failed Syncs",
            "type": "graph",
            "targets": [{
              "expr": "count(externalsecret_status_condition{condition=\"Ready\", status=\"False\"})"
            }]
          },
          {
            "title": "Sync Duration",
            "type": "graph",
            "targets": [{
              "expr": "histogram_quantile(0.99, rate(externalsecret_sync_duration_seconds_bucket[5m]))"
            }]
          }
        ]
      }
    }
```

---

<!-- chunk: 三、HashiCorp Vault -->
## 3. HashiCorp Vault

### 3.1 Vault High-Availability Deployment

```yaml
# Vault HA Deployment Configuration
apiVersion: v1
kind: Namespace
metadata:
  name: vault
---
# Install with Helm
# helm repo add hashicorp https://helm.releases.hashicorp.com
# helm install vault hashicorp/vault -n vault -f vault-values.yaml
---
# vault-values.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: vault-helm-values
  namespace: vault
data:
  values.yaml: |
    global:
      enabled: true
      tlsDisable: false
    
    injector:
      enabled: true
      replicas: 2
      resources:
        requests:
          memory: 256Mi
          cpu: 250m
        limits:
          memory: 512Mi
          cpu: 500m
      
      # Webhook configuration
      webhook:
        failurePolicy: Ignore
        matchPolicy: Exact
        timeoutSeconds: 30
      
      # Injection configuration
      agentDefaults:
        cpuLimit: "500m"
        cpuRequest: "250m"
        memLimit: "128Mi"
        memRequest: "64Mi"
    
    server:
      enabled: true
      image:
        repository: hashicorp/vault
        tag: "1.15.4"
      
      # HA configuration
      ha:
        enabled: true
        replicas: 3
        raft:
          enabled: true
          setNodeId: true
          config: |
            ui = true
            
            listener "tcp" {
              address = "[::]:8200"
              cluster_address = "[::]:8201"
              tls_cert_file = "/vault/userconfig/vault-tls/tls.crt"
              tls_key_file = "/vault/userconfig/vault-tls/tls.key"
              tls_client_ca_file = "/vault/userconfig/vault-tls/ca.crt"
            }
            
            storage "raft" {
              path = "/vault/data"
              retry_join {
                leader_api_addr = "https://vault-0.vault-internal:8200"
                leader_ca_cert_file = "/vault/userconfig/vault-tls/ca.crt"
              }
              retry_join {
                leader_api_addr = "https://vault-1.vault-internal:8200"
                leader_ca_cert_file = "/vault/userconfig/vault-tls/ca.crt"
              }
              retry_join {
                leader_api_addr = "https://vault-2.vault-internal:8200"
                leader_ca_cert_file = "/vault/userconfig/vault-tls/ca.crt"
              }
            }
            
            seal "awskms" {
              region     = "us-west-2"
              kms_key_id = "alias/vault-unseal-key"
            }
            
            service_registration "kubernetes" {}
            
            telemetry {
              prometheus_retention_time = "30s"
              disable_hostname = true
            }
      
      # Resource configuration
      resources:
        requests:
          memory: 1Gi
          cpu: 500m
        limits:
          memory: 2Gi
          cpu: 1000m
      
      # Data persistence
      dataStorage:
        enabled: true
        size: 50Gi
        storageClass: fast-ssd
      
      # Audit logging
      auditStorage:
        enabled: true
        size: 50Gi
        storageClass: standard
      
      # Service account
      serviceAccount:
        create: true
        annotations:
          eks.amazonaws.com/role-arn: arn:aws:iam::123456789012:role/vault-kms-unseal
      
      # Affinity
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchLabels:
                app.kubernetes.io/name: vault
            topologyKey: kubernetes.io/hostname
    
    ui:
      enabled: true
      serviceType: LoadBalancer
      annotations:
        service.beta.kubernetes.io/aws-load-balancer-internal: "true"
        service.beta.kubernetes.io/aws-load-balancer-type: nlb
```

### 3.2 Vault Policies and Authentication Configuration

```hcl
# vault-policies.hcl - Vault Policy Configuration

# Admin Policy
path "sys/*" {
  capabilities = ["create", "read", "update", "delete", "list", "sudo"]
}

path "auth/*" {
  capabilities = ["create", "read", "update", "delete", "list", "sudo"]
}

path "secret/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

# Application Read Policy
path "secret/data/{{identity.entity.aliases.auth_kubernetes_xxx.metadata.service_account_namespace}}/*" {
  capabilities = ["read", "list"]
}

# Database Dynamic Credentials Policy
path "database/creds/{{identity.entity.aliases.auth_kubernetes_xxx.metadata.service_account_namespace}}-*" {
  capabilities = ["read"]
}

# PKI Certificate Issuance Policy
path "pki/issue/{{identity.entity.aliases.auth_kubernetes_xxx.metadata.service_account_namespace}}" {
  capabilities = ["create", "update"]
}

# Transit Encryption Policy
path "transit/encrypt/{{identity.entity.aliases.auth_kubernetes_xxx.metadata.service_account_namespace}}-*" {
  capabilities = ["update"]
}

path "transit/decrypt/{{identity.entity.aliases.auth_kubernetes_xxx.metadata.service_account_namespace}}-*" {
  capabilities = ["update"]
}
```

```bash
#!/bin/bash
# vault-setup.sh - Vault Initialization Script

# Enable Kubernetes authentication
vault auth enable kubernetes

vault write auth/kubernetes/config \
    kubernetes_host="https://$KUBERNETES_PORT_443_TCP_ADDR:443" \
    token_reviewer_jwt="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
    kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt \
    issuer="https://kubernetes.default.svc.cluster.local"

# Create role
vault write auth/kubernetes/role/myapp \
    bound_service_account_names=myapp-sa \
    bound_service_account_namespaces=production \
    policies=myapp-policy \
    ttl=1h

# Enable KV secrets engine
vault secrets enable -path=secret kv-v2

# Enable database secrets engine
vault secrets enable database

vault write database/config/postgres \
    plugin_name=postgresql-database-plugin \
    allowed_roles="production-*" \
    connection_url="postgresql://{{username}}:{{password}}@postgres.database:5432/mydb?sslmode=require" \
    username="vault" \
    password="vault-password"

vault write database/roles/production-readonly \
    db_name=postgres \
    creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; GRANT SELECT ON ALL TABLES IN SCHEMA public TO \"{{name}}\";" \
    default_ttl="1h" \
    max_ttl="24h"

# Enable PKI engine
vault secrets enable pki
vault secrets tune -max-lease-ttl=87600h pki

vault write pki/root/generate/internal \
    common_name="example.com" \
    ttl=87600h

vault write pki/roles/example-dot-com \
    allowed_domains="example.com" \
    allow_subdomains=true \
    max_ttl=72h

# Enable Transit engine
vault secrets enable transit

vault write -f transit/keys/myapp-encryption \
    type=aes256-gcm96

# Enable audit logging
vault audit enable file file_path=/vault/audit/audit.log
```

### 3.3 Vault Agent Sidecar Injection

```yaml
# Application Pod with Vault Agent Injection
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
  namespace: production
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
      annotations:
        # Vault Agent Injector Annotations
        vault.hashicorp.com/agent-inject: "true"
        vault.hashicorp.com/role: "myapp"
        vault.hashicorp.com/agent-pre-populate-only: "false"
        vault.hashicorp.com/agent-revoke-on-shutdown: "true"
        vault.hashicorp.com/agent-revoke-grace: "180"
        
        # Inject database credentials
        vault.hashicorp.com/agent-inject-secret-db-creds: "database/creds/production-readonly"
        vault.hashicorp.com/agent-inject-template-db-creds: |
          {{- with secret "database/creds/production-readonly" -}}
          export DB_USER="{{ .Data.username }}"
          export DB_PASS="{{ .Data.password }}"
          {{- end }}
        
        # Inject application configuration
        vault.hashicorp.com/agent-inject-secret-app-config: "secret/data/production/myapp"
        vault.hashicorp.com/agent-inject-template-app-config: |
          {{- with secret "secret/data/production/myapp" -}}
          {
            "api_key": "{{ .Data.data.api_key }}",
            "encryption_key": "{{ .Data.data.encryption_key }}",
            "webhook_secret": "{{ .Data.data.webhook_secret }}"
          }
          {{- end }}
        
        # Inject TLS certificate
        vault.hashicorp.com/agent-inject-secret-tls-cert: "pki/issue/example-dot-com"
        vault.hashicorp.com/agent-inject-template-tls-cert: |
          {{- with secret "pki/issue/example-dot-com" "common_name=myapp.example.com" -}}
          {{ .Data.certificate }}
          {{ .Data.ca_chain }}
          {{- end }}
        
        vault.hashicorp.com/agent-inject-secret-tls-key: "pki/issue/example-dot-com"
        vault.hashicorp.com/agent-inject-template-tls-key: |
          {{- with secret "pki/issue/example-dot-com" "common_name=myapp.example.com" -}}
          {{ .Data.private_key }}
          {{- end }}
    
    spec:
      serviceAccountName: myapp-sa
      containers:
      - name: myapp
        image: myapp:latest
        command:
        - /bin/sh
        - -c
        - |
          source /vault/secrets/db-creds
          ./myapp --config /vault/secrets/app-config
        
        ports:
        - containerPort: 8080
        
        volumeMounts:
        - name: vault-secrets
          mountPath: /vault/secrets
          readOnly: true
        
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
      
      volumes:
      - name: vault-secrets
        emptyDir:
          medium: Memory
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: myapp-sa
  namespace: production
```

### 3.4 Vault CSI Provider

```yaml
# Vault CSI Provider Configuration
apiVersion: secrets-store.csi.x-k8s.io/v1
kind: SecretProviderClass
metadata:
  name: vault-db-creds
  namespace: production
spec:
  provider: vault
  parameters:
    vaultAddress: "https://vault.vault:8200"
    roleName: "myapp"
    
    objects: |
      - objectName: "db-username"
        secretPath: "database/creds/production-readonly"
        secretKey: "username"
      - objectName: "db-password"
        secretPath: "database/creds/production-readonly"
        secretKey: "password"
      - objectName: "api-key"
        secretPath: "secret/data/production/myapp"
        secretKey: "api_key"
  
  # Sync as Kubernetes Secret
  secretObjects:
  - secretName: myapp-db-creds
    type: Opaque
    data:
    - objectName: db-username
      key: username
    - objectName: db-password
      key: password
---
# Pod using CSI-mounted secrets
apiVersion: v1
kind: Pod
metadata:
  name: myapp-csi
  namespace: production
spec:
  serviceAccountName: myapp-sa
  containers:
  - name: myapp
    image: myapp:latest
    volumeMounts:
    - name: secrets-store
      mountPath: "/mnt/secrets"
      readOnly: true
    
    env:
    - name: DB_USER
      valueFrom:
        secretKeyRef:
          name: myapp-db-creds
          key: username
    - name: DB_PASS
      valueFrom:
        secretKeyRef:
          name: myapp-db-creds
          key: password
  
  volumes:
  - name: secrets-store
    csi:
      driver: secrets-store.csi.k8s.io
      readOnly: true
      volumeAttributes:
        secretProviderClass: "vault-db-creds"
```

---

<!-- chunk: 四、Sealed Secrets -->
## 4. Sealed Secrets

### 4.1 Sealed Secrets Deployment and Usage

```yaml
# Sealed Secrets Controller Deployment
apiVersion: v1
kind: Namespace
metadata:
  name: sealed-secrets
---
# Install with Helm
# helm repo add sealed-secrets https://bitnami-labs.github.io/sealed-secrets
# helm install sealed-secrets sealed-secrets/sealed-secrets -n sealed-secrets
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sealed-secrets-controller
  namespace: sealed-secrets
spec:
  replicas: 1
  selector:
    matchLabels:
      app: sealed-secrets-controller
  template:
    metadata:
      labels:
        app: sealed-secrets-controller
    spec:
      serviceAccountName: sealed-secrets-controller
      containers:
      - name: controller
        image: bitnami/sealed-secrets-controller:v0.25.0
        args:
        - --update-status
        - --key-renew-period=720h
        - --key-prefix=sealed-secrets-key
        - --rate-limit=10
        - --rate-limit-burst=50
        
        ports:
        - containerPort: 8080
          name: http
        - containerPort: 8081
          name: metrics
        
        resources:
          requests:
            cpu: 50m
            memory: 64Mi
          limits:
            cpu: 200m
            memory: 256Mi
        
        livenessProbe:
          httpGet:
            path: /healthz
            port: 8080
        
        readinessProbe:
          httpGet:
            path: /healthz
            port: 8080
        
        volumeMounts:
        - name: sealed-secrets-keys
          mountPath: /var/run/secrets/sealed-secrets
          readOnly: true
      
      volumes:
      - name: sealed-secrets-keys
        secret:
          secretName: sealed-secrets-key
```

### 4.2 Sealed Secrets Workflow

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend using --dry-run or diff to confirm first
> - `kubectl apply/create/replace`: Create/modify cluster resources

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, confirm target, scope and authorization before executing
#!/bin/bash
# sealed-secrets-workflow.sh - Sealed Secrets Workflow

# 1. Install kubeseal CLI
# brew install kubeseal  # macOS
# wget https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.25.0/kubeseal-0.25.0-linux-amd64.tar.gz

# 2. Fetch cluster public key
kubeseal --fetch-cert \
  --controller-name=sealed-secrets-controller \
  --controller-namespace=sealed-secrets \
  > pub-sealed-secrets.pem

# 3. Create and encrypt Secret
# Method A: Create from literal values
kubectl create secret generic my-secret \
  --namespace=production \
  --dry-run=client \
  --from-literal=username=admin \
  --from-literal=password=secretpassword \
  -o yaml | \
kubeseal \
  --cert pub-sealed-secrets.pem \
  --format yaml > sealed-my-secret.yaml

# Method B: Create from file
kubectl create secret generic tls-secret \
  --namespace=production \
  --dry-run=client \
  --from-file=tls.crt=./server.crt \
  --from-file=tls.key=./server.key \
  -o yaml | \
kubeseal \
  --cert pub-sealed-secrets.pem \
  --format yaml > sealed-tls-secret.yaml

# Method C: Encrypt only specific values (raw mode)
echo -n "mysupersecretpassword" | \
kubeseal --raw \
  --cert pub-sealed-secrets.pem \
  --namespace production \
  --name my-secret \
  --from-file=/dev/stdin

# 4. Commit to Git
git add sealed-*.yaml
git commit -m "Add sealed secrets"
git push

# 5. Apply SealedSecret
kubectl apply -f sealed-my-secret.yaml

# 6. Verify Secret created
kubectl get secret my-secret -n production -o yaml
```
### 4.3 SealedSecret Configuration Options

```yaml
# Cluster-wide SealedSecret
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: cluster-wide-secret
  namespace: production
  annotations:
    sealedsecrets.bitnami.com/cluster-wide: "true"
spec:
  encryptedData:
    password: AgBy8hCi...encrypted...
  template:
    metadata:
      labels:
        app: myapp
      annotations:
        description: "Cluster-wide secret"
    type: Opaque
---
# Namespace-scoped SealedSecret
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: namespace-scoped-secret
  namespace: production
  annotations:
    sealedsecrets.bitnami.com/namespace-wide: "true"
spec:
  encryptedData:
    api-key: AgBy8hCi...encrypted...
  template:
    type: Opaque
---
# Strict scope (default, bound to name and namespace)
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: strict-secret
  namespace: production
spec:
  encryptedData:
    username: AgBy8hCi...encrypted...
    password: AgCQx7ki...encrypted...
  template:
    metadata:
      labels:
        managed-by: sealed-secrets
    type: kubernetes.io/basic-auth
```

### 4.4 Key Rotation

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend using --dry-run or diff to confirm first
> - `kubectl apply/create/replace`: Create/modify cluster resources

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, confirm target, scope and authorization before executing
#!/bin/bash
# sealed-secrets-key-rotation.sh - Key Rotation

# 1. Backup current keys
kubectl get secret -n sealed-secrets -l sealedsecrets.bitnami.com/sealed-secrets-key -o yaml > sealed-secrets-keys-backup.yaml

# 2. Fetch new key
kubeseal --fetch-cert \
  --controller-name=sealed-secrets-controller \
  --controller-namespace=sealed-secrets \
  > new-pub-cert.pem

# 3. Re-encrypt all SealedSecrets
for ns in $(kubectl get namespaces -o jsonpath='{.items[*].metadata.name}'); do
  for ss in $(kubectl get sealedsecrets -n $ns -o jsonpath='{.items[*].metadata.name}'); do
    echo "Re-encrypting $ns/$ss"
    
    # Get original Secret
    kubectl get secret $ss -n $ns -o yaml > /tmp/secret.yaml
    
    # Re-encrypt
    kubeseal --cert new-pub-cert.pem < /tmp/secret.yaml > /tmp/sealed-secret.yaml
    
    # Apply new SealedSecret
    kubectl apply -f /tmp/sealed-secret.yaml
  done
done

# 4. Clean up temporary files
rm /tmp/secret.yaml /tmp/sealed-secret.yaml
```
---

<!-- chunk: 五、SOPS加密 -->
## 5. SOPS Encryption

### 5.1 SOPS Configuration and Usage

```yaml
# .sops.yaml - SOPS Configuration File
creation_rules:
  # Use AWS KMS for production
  - path_regex: .*production.*\.yaml$
    kms: arn:aws:kms:us-west-2:123456789012:key/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    encrypted_regex: ^(data|stringData)$
  
  # Use AGE for development
  - path_regex: .*development.*\.yaml$
    age: age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p
    encrypted_regex: ^(data|stringData)$
  
  # Default to PGP
  - path_regex: .*\.yaml$
    pgp: FBC7B9E2A4F9289AC0C1D4843D16CEE4A27381B4
    encrypted_regex: ^(data|stringData)$
```

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend using --dry-run or diff to confirm first
> - `kubectl apply/create/replace`: Create/modify cluster resources

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, confirm target, scope and authorization before executing
#!/bin/bash
# sops-workflow.sh - SOPS Workflow

# 1. Install SOPS
# brew install sops  # macOS
# apt install sops  # Ubuntu

# 2. Create unencrypted Secret YAML
cat > secret.yaml << EOF
apiVersion: v1
kind: Secret
metadata:
  name: my-secret
  namespace: production
type: Opaque
stringData:
  username: admin
  password: supersecretpassword
  api-key: abcd1234
EOF

# 3. Encrypt file
sops --encrypt secret.yaml > secret.enc.yaml

# 4. Edit encrypted file (automatically decrypts for editing, then re-encrypts)
sops secret.enc.yaml

# 5. Decrypt and apply
sops --decrypt secret.enc.yaml | kubectl apply -f -

# 6. Encrypt only specific keys
sops --encrypt --encrypted-regex '^(data|stringData)$' secret.yaml > secret.enc.yaml

# 7. Use key from environment variable
export SOPS_AGE_KEY_FILE=~/.config/sops/age/keys.txt
sops --decrypt secret.enc.yaml

# 8. Key rotation
sops --rotate --in-place secret.enc.yaml
```
### 5.2 SOPS and GitOps Integration

```yaml
# ArgoCD SOPS Plugin Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: argocd-cm
  namespace: argocd
data:
  configManagementPlugins: |
    - name: sops
      init:
        command: ["/bin/sh", "-c"]
        args: ["echo 'Initializing SOPS...'"]
      generate:
        command: ["/bin/sh", "-c"]
        args:
          - |
            find . -name '*.enc.yaml' -o -name '*.enc.yml' | while read file; do
              sops --decrypt "$file"
            done
---
# Flux SOPS Decryption Configuration
apiVersion: kustomize.toolkit.fluxcd.io/v1beta2
kind: Kustomization
metadata:
  name: production-secrets
  namespace: flux-system
spec:
  interval: 10m
  path: ./production
  prune: true
  sourceRef:
    kind: GitRepository
    name: infrastructure
  decryption:
    provider: sops
    secretRef:
      name: sops-age
---
apiVersion: v1
kind: Secret
metadata:
  name: sops-age
  namespace: flux-system
stringData:
  age.agekey: |
    # created: 2024-01-01T00:00:00Z
    # public key: age1ql3z7hjy54pw3hyww5ayyfg7zqgvc7w3j2elw8zmrj2kg5sfn9aqmcac8p
    AGE-SECRET-KEY-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

---

<!-- chunk: 六、etcd加密配置 -->
## 6. etcd Encryption Configuration

### 6.1 EncryptionConfiguration

```yaml
# /etc/kubernetes/encryption-config.yaml
apiVersion: apiserver.config.k8s.io/v1
kind: EncryptionConfiguration
resources:
  - resources:
    - secrets
    - configmaps
    providers:
    # Recommended: Use external KMS
    - kms:
        apiVersion: v2
        name: aws-encryption-provider
        endpoint: unix:///var/run/kmsplugin/socket.sock
        cachesize: 1000
        timeout: 3s
    # Alternative: AES-GCM
    - aescbc:
        keys:
        - name: key1
          secret: <base64-encoded-32-byte-key>
    # Backward compatibility with old data
    - identity: {}
---
# API Server Configuration
# kube-apiserver --encryption-provider-config=/etc/kubernetes/encryption-config.yaml
```

### 6.2 AWS KMS Provider

```yaml
# AWS KMS Encryption Provider
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: aws-encryption-provider
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: aws-encryption-provider
  template:
    metadata:
      labels:
        app: aws-encryption-provider
    spec:
      hostNetwork: true
      containers:
      - name: aws-encryption-provider
        image: amazon/aws-encryption-provider:v1.0.0
        args:
        - --key=arn:aws:kms:us-west-2:123456789012:key/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        - --region=us-west-2
        - --listen=/var/run/kmsplugin/socket.sock
        
        volumeMounts:
        - name: socket
          mountPath: /var/run/kmsplugin
      
      volumes:
      - name: socket
        hostPath:
          path: /var/run/kmsplugin
          type: DirectoryOrCreate
      
      nodeSelector:
        node-role.kubernetes.io/control-plane: ""
      
      tolerations:
      - key: node-role.kubernetes.io/control-plane
        operator: Exists
        effect: NoSchedule
```

---

<!-- chunk: 七、安全最佳实践 -->
## 7. Security Best Practices

### 7.1 Secret Management Security Checklist

| Checklist Item | Risk Level | Inspection Method | Fix Recommendation |
|-------|---------|---------|---------|
| **Hardcoded Secrets** | Extremely High | grep -r "password=" | Move to Secret/Vault |
| **Plaintext Secrets** | High | kubectl get secret -o yaml | Enable etcd encryption |
| **Overly Broad RBAC** | High | kubectl auth can-i | Least Privilege Principle |
| **No Rotation Policy** | Medium | Check secret creation time | Set up automatic rotation |
| **No Audit Logging** | Medium | Check audit configuration | Enable audit logging |
| **Secrets in Images** | High | trivy image scan | Remove and rebuild image |
| **Secrets in Git** | Extremely High | git-secrets scan | Use Sealed Secrets |

### 7.2 RBAC Least Privilege Configuration

```yaml
# Application-specific Secret read access
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: secret-reader
  namespace: production
rules:
- apiGroups: [""]
  resources: ["secrets"]
  resourceNames: ["myapp-db-creds", "myapp-api-keys"]
  verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: myapp-secret-reader
  namespace: production
subjects:
- kind: ServiceAccount
  name: myapp-sa
  namespace: production
roleRef:
  kind: Role
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
---
# Deny listing Secrets
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: deny-secret-list
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["list", "watch"]
```

### 7.3 Secret Audit Configuration

```yaml
# Audit Policy - Record all Secret access
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
# Record all Secret operations
- level: RequestResponse
  resources:
  - group: ""
    resources: ["secrets"]
  verbs: ["get", "list", "create", "update", "patch", "delete"]
  
# Record ServiceAccount Token creation
- level: Metadata
  resources:
  - group: ""
    resources: ["serviceaccounts/token"]
  verbs: ["create"]

# Record RBAC changes
- level: RequestResponse
  resources:
  - group: "rbac.authorization.k8s.io"
    resources: ["roles", "rolebindings", "clusterroles", "clusterrolebindings"]
```

---

<!-- chunk: 八、监控与告警 -->
## 8. Monitoring and Alerting

### 8.1 Secret Management Monitoring

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: secret-management-alerts
  namespace: monitoring
spec:
  groups:
  - name: secret-security
    rules:
    # Secret not encrypted storage
    - alert: SecretNotEncrypted
      expr: |
        kube_secret_info unless on(namespace, secret) 
        externalsecret_status_condition{condition="Ready", status="True"}
      for: 1h
      labels:
        severity: warning
      annotations:
        summary: "Discovered Secret not managed by ESO"
        description: "Secret {{ $labels.namespace }}/{{ $labels.secret }} not encrypted and managed"
    
    # Unusual Secret access
    - alert: UnusualSecretAccess
      expr: |
        increase(apiserver_request_total{
          resource="secrets",
          verb=~"get|list"
        }[5m]) > 100
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "Abnormal Secret access frequency"
    
    # Vault unhealthy
    - alert: VaultUnhealthy
      expr: vault_core_unsealed == 0
      for: 2m
      labels:
        severity: critical
      annotations:
        summary: "Vault is in sealed state"
    
    # Secret expiring soon
    - alert: SecretExpiringSoon
      expr: |
        (vault_secret_lease_expiration_time_seconds - time()) < 86400
      for: 1h
      labels:
        severity: warning
      annotations:
        summary: "Vault lease expiring soon"
```

---

<!-- chunk: 九、快速参考 -->
## 9. Quick Reference

### 9.1 Solution Selection Decision Tree

```
# 🟢 Low Risk: Read-only/information gathering, typically no side effects
Need secret management solution?
    │
    ├─ Multi-cloud/hybrid cloud environment?
    │   └─ YES → External Secrets Operator
    │
    ├─ Need dynamic secrets/certificate issuance?
    │   └─ YES → HashiCorp Vault
    │
    ├─ Pure GitOps workflow?
    │   └─ YES → Sealed Secrets
    │
    ├─ Small team quick start?
    │   └─ YES → SOPS
    │
    └─ Single cloud environment?
        └─ YES → Cloud-native solution (AWS SM/Azure KV/GCP SM)
```
### 9.2 Common Commands Quick Reference

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend using --dry-run or diff to confirm first
> - `kubectl apply/create/replace`: Create/modify cluster resources

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, confirm target, scope and authorization before executing
# External Secrets
kubectl get externalsecrets -A
kubectl describe externalsecret <name> -n <namespace>

# Vault
vault status
vault kv get secret/myapp
vault login -method=kubernetes role=myapp

# Sealed Secrets
kubeseal --fetch-cert > pub-cert.pem
kubectl create secret generic mysecret --dry-run=client -o yaml | kubeseal -o yaml

# SOPS
sops --encrypt secret.yaml > secret.enc.yaml
sops --decrypt secret.enc.yaml | kubectl apply -f -

# Check Secrets
kubectl get secrets -A -o json | jq '.items[] | select(.type=="Opaque") | .metadata.name'
```
---

<!-- chunk: 十、最佳实践总结 -->
## 10. Best Practices Summary

### Secret Management Checklist

- [ ] **No Hardcoding**: No plaintext secrets in code/configuration
- [ ] **etcd Encryption**: Enable EncryptionConfiguration
- [ ] **External Storage**: Use ESO/Vault/Cloud KMS
- [ ] **Least Privilege**: RBAC restricts Secret access
- [ ] **Automatic Rotation**: Set up secret rotation policy
- [ ] **Audit Logging**: Record all secret access
- [ ] **GitOps Security**: Use Sealed Secrets/SOPS
- [ ] **Monitoring/Alerting**: Anomalous access detection
- [ ] **Disaster Recovery**: Secret backup strategy
- [ ] **Compliance Checks**: Regular security scanning

---

**Related Documents**: [91-Security Scanning Tools](91-security-scanning-tools.md) | [92-Policy Validation Tools](92-policy-validation-tools.md) | [89-RBAC Permissions Management](89-rbac-permissions.md)

**Version**: External Secrets 0.9+ | Vault 1.15+ | Sealed Secrets 0.25+ | SOPS 3.8+

---

<!-- chunk: Obsidian Related Documents -->
## Obsidian Related Documents

- domain-05-security-compliance MOC
- [[domain-05-security-compliance/README.md|Security Domain]]
- [[domain-05-security-compliance/00-open-source-projects-index.md|Domain-7 Security — Open Source Projects Index]]
- Kubernetes Authentication and Authorization System Explained in Detail
- Network Security Policies and Zero Trust Architecture
- Runtime Security Protection and Threat Detection
- 04 - Audit Logging and Compliance Management
- 05 - Policy Validation and Admission Control Tools (Policy Validation)
- 06 - Pod Security Standards Explained in Detail
- 07 - RBAC Permission Matrix
- 08 - Security Best Practices
- Kubernetes Security Hardening

## See Also

- 09-security-hardening-production
- 10-certificate-management
- 12-compliance-certification
- 13-image-security-scanning

- [[domain-05-security-compliance/README.md|Return to Directory]]

## Related

- [[domain-19-landscape-references/topic-index/security-index.md|Security Knowledge Graph Index]]


<!-- risk-assessed -->
