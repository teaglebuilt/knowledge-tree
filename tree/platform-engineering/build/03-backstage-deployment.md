```markdown
---
title: Crossplane Platform Composition
description: '<!-- chunk: Overview' -->## Overview'
summary: '<!-- chunk: Overview' -->## Overview'
category: general
tags:
- platform
- idp
- etcd
- prometheus
- helm
- argocd
- flux
- postgresql
- kafka
- rbac
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All engineers
estimated_read_time: 45min
intent_queries:
- What is crossplane-platform-composition?
- How to use crossplane-platform-composition
- Best practices for crossplane-platform-composition
trigger_keywords:
- Crossplane
- Platform Composition
- Crossplane
- Platform
- Composition
- platform
- engineering
prerequisites:
- kubectl-basics
- platform-engineering-basics
- helm-basics
- prometheus-basics
- gitops-basics
- iac-basics
- etcd-basics
- kafka-basics
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./build/07-crossplane-platform-composition.md
original_language: Chinese
---

> **Production Environment Security Tips**
>
> This documentation contains directly executable operations commands. Before execution, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether the commands have been verified in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state but usually reversible), 🟢 Low risk/read-only (information gathering, no side effects).




title: [[Crossplane|Crossplane]] Platform Composition
description: '<!-- chunk: Overview' -->## Overview'
category: platform-engineering
tags:
- k8s
- platform-engineering
- developer-experience
- idp
- [[etcd|etcd]]
- [[Prometheus|prometheus]]
- [[Helm|helm]]
- argocd
- flux
- postgresql
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- Platform Engineers
- SRE
- Architects
estimated_read_time: 5min
intent_queries:
- What is Crossplane Platform Composition
- How to use Crossplane Platform Composition
- Kubernetes 36 platform engineering best practices
trigger_keywords:
- Crossplane
- Platform Composition
- Crossplane
- Platform
- Composition
- platform
- engineering
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

# Crossplane Platform Composition

<!-- chunk: Overview -->## Overview

Crossplane is an open-source Kubernetes extension framework maintained by Upbound and has joined the CNCF. It introduces cloud infrastructure (AWS, GCP, Azure, Alibaba Cloud, etc.) management capabilities into the Kubernetes control plane, enabling **Infrastructure as Code** declarative management, and allows platform teams to build custom **Platform APIs**, hiding the underlying complexity from application teams.

**Core Philosophy**: *Use Kubernetes as the universal control plane for all infrastructure.*

---

<!-- chunk: Table of Contents -->## Table of Contents

1. [Crossplane Core Architecture](#crossplane-core-architecture)
2. [Provider Ecosystem](#provider-ecosystem)
3. [Managed Resources Explained](#managed-resources-explained)
4. [Composite Resources (XR)](#composite-resources-xr)
5. [XRD — Composite Resource Definition](#xrd--composite-resource-definition)
6. [Composition Mechanism](#composition-mechanism)
7. [Composition Functions](#composition-functions)
8. [Multi-Cloud Infrastructure Abstraction](#multi-cloud-infrastructure-abstraction)
9. [Platform API Design Patterns](#platform-api-design-patterns)
10. [RBAC and Access Control](#rbac-and-access-control)
11. [Observability and Debugging](#observability-and-debugging)
12. [Production Best Practices](#production-best-practices)
13. [Crossplane vs Terraform](#crossplane-vs-terraform)

---

<!-- chunk: Crossplane Core Architecture -->## Crossplane Core Architecture

## Overall Architecture Diagram

```mermaid
graph TB
    subgraph "Kubernetes Control Plane"
        direction TB
        API[K8s API Server]
        
        subgraph "Crossplane Core"
            XC[Crossplane\nController Manager]
            PKGM[Package Manager]
        end
        
        subgraph "Provider Controllers"
            PAA[provider-aws\nController]
            PGC[provider-gcp\nController]
            PAZ[provider-azure\nController]
        end
        
        subgraph "Composite Controllers"
            CC[Composition\nController]
            CLMC[Claim\nController]
        end
        
        API --> XC
        XC --> PKGM
        PKGM --> PAA
        PKGM --> PGC
        PKGM --> PAZ
        API --> CC
        API --> CLMC
    end
    
    subgraph "AWS Cloud"
        RDS[RDS Instance]
        S3[S3 Bucket]
        EC2[EC2 Instance]
        EKS[EKS Cluster]
    end
    
    subgraph "GCP Cloud"
        SQL[Cloud SQL]
        GCS[GCS Bucket]
        GKE[GKE Cluster]
    end
    
    subgraph "Azure Cloud"
        ASQL[Azure SQL]
        ABLOB[Blob Storage]
        AKS[AKS Cluster]
    end
    
    PAA -->|Reconcile| RDS
    PAA -->|Reconcile| S3
    PAA -->|Reconcile| EKS
    PGC -->|Reconcile| SQL
    PGC -->|Reconcile| GCS
    PAZ -->|Reconcile| ASQL
    PAZ -->|Reconcile| ABLOB
    
    style "Kubernetes Control Plane" fill:#e8f4fd,stroke:#1565c0
    style "AWS Cloud" fill:#fff3e0,stroke:#e65100
    style "GCP Cloud" fill:#e8f5e9,stroke:#2e7d32
    style "Azure Cloud" fill:#f3e5f5,stroke:#7b1fa2
```

## Core Concept Hierarchy

```mermaid
graph TD
    subgraph "Platform Team"
        XRD[XRD\nComposite Resource Definition]
        COMP[Composition\nComposition Logic]
        PROV[Provider\nCloud Provider]
        XRD --> COMP
        COMP --> PROV
    end
    
    subgraph "Application Team"
        CLAIM[Claim\nResource Claim]
    end
    
    subgraph "Crossplane Engine"
        XR[Composite Resource\nComposite Resource - XR]
    end
    
    subgraph "Cloud"
        MR[Managed Resources\nManaged Resources]
    end
    
    CLAIM -->|Create| XR
    XRD -->|Define Schema| XR
    COMP -->|Drive Creation| MR
    PROV -->|reconcile| MR
    
    style "Platform Team" fill:#e3f2fd
    style "Application Team" fill:#e8f5e9
    style "Crossplane Engine" fill:#fff8e1
    style "Cloud" fill:#fce4ec
```

## Data Flow

```mermaid
sequenceDiagram
    participant Dev as App Developer
    participant K8s as K8s API
    participant Cross as Crossplane
    participant AWS as AWS API

    Dev->>K8s: kubectl apply -f database-claim.yaml
    K8s->>Cross: Claim Created Event
    Cross->>Cross: Find matching Composition
    Cross->>Cross: Create Composite Resource (XR)
    Cross->>Cross: Render Composition → Managed Resources
    Cross->>AWS: CreateDBInstance (RDS)
    Cross->>AWS: CreateSubnetGroup
    Cross->>AWS: CreateSecurityGroup
    AWS-->>Cross: Resources Provisioning
    AWS-->>Cross: Resources Ready
    Cross-->>K8s: Update XR Status
    Cross-->>K8s: Write Connection Secret
    K8s-->>Dev: Claim Ready + Connection Details
```

---

<!-- chunk: Provider Ecosystem -->## Provider Ecosystem

## Major Provider List

```mermaid
mindmap
  root((Crossplane\nProviders))
    Official Upbound
      provider-aws
        EC2, RDS, S3
        EKS, IAM, VPC
        400+ Resources
      provider-gcp
        GKE, Cloud SQL
        GCS, BigQuery
        350+ Resources
      provider-azure
        AKS, Azure SQL
        Blob Storage
        300+ Resources
    Community
      provider-helm
        Helm Release Management
      provider-kubernetes
        K8s Resource Management
      provider-terraform
        Terraform Module Invocation
      provider-gitlab
        GitLab Resources
      provider-github
        GitHub Resources
    Marketplace
      provider-alibaba
        Alibaba Cloud Resources
      provider-tencent
        Tencent Cloud Resources
```

## Installing Provider

```yaml
# Install AWS Provider
apiVersion: pkg.crossplane.io/v1
kind: Provider
metadata:
  name: provider-aws-rds
spec:
  package: xpkg.upbound.io/upbound/provider-aws-rds:v0.46.0
  runtimeConfigRef:
    name: provider-aws-rds
  packagePullPolicy: IfNotPresent
  revisionActivationPolicy: Automatic

---
# Provider Runtime Configuration
apiVersion: pkg.crossplane.io/v1beta1
kind: DeploymentRuntimeConfig
metadata:
  name: provider-aws-rds
spec:
  deploymentTemplate:
    spec:
      selector: {}
      template:
        spec:
          containers:
            - name: package-runtime
              resources:
                requests:
                  cpu: 100m
                  memory: 256Mi
                limits:
                  cpu: 500m
                  memory: 512Mi
```

## ProviderConfig (Credential Configuration)

```yaml
# AWS Credential Configuration
apiVersion: aws.upbound.io/v1beta1
kind: ProviderConfig
metadata:
  name: aws-prod
spec:
  credentials:
    source: Secret
    secretRef:
      namespace: crossplane-system
      name: aws-credentials
      key: credentials
  # Can also use IRSA (IAM Roles for Service Accounts)
  # credentials:
  #   source: IRSA

---
# IRSA Method (Recommended for Production)
apiVersion: aws.upbound.io/v1beta1
kind: ProviderConfig
metadata:
  name: aws-irsa
spec:
  credentials:
    source: IRSA
  assumeRoleChain:
    - roleARN: "arn:aws:iam::123456789012:role/CrossplaneRole"
```

```yaml
# GCP Credential Configuration
apiVersion: gcp.upbound.io/v1beta1
kind: ProviderConfig
metadata:
  name: gcp-prod
spec:
  projectID: my-gcp-project-id
  credentials:
    source: Secret
    secretRef:
      namespace: crossplane-system
      name: gcp-credentials
      key: credentials.json

---
# Workload Identity (Recommended for Production)
apiVersion: gcp.upbound.io/v1beta1
kind: ProviderConfig
metadata:
  name: gcp-workload-identity
spec:
  projectID: my-gcp-project-id
  credentials:
    source: InjectedIdentity
```

---

<!-- chunk: Managed Resources Explained -->## Managed Resources Explained

## Direct Use of Managed Resource

```yaml
# Directly create RDS PostgreSQL instance (low-level API)
apiVersion: rds.aws.upbound.io/v1beta1
kind: Instance
metadata:
  name: prod-postgresql
  annotations:
    crossplane.io/external-name: "prod-postgresql-001"
spec:
  forProvider:
    region: us-east-1
    dbInstanceClass: db.t3.medium
    engine: postgres
    engineVersion: "15.3"
    username: admin
    allocatedStorage: 100
    storageType: gp3
    storageEncrypted: true
    multiAZ: true
    publiclyAccessible: false
    skipFinalSnapshot: false
    finalSnapshotIdentifier: "prod-postgresql-001-final"
    dbSubnetGroupName: "prod-subnet-group"
    vpcSecurityGroupIds:
      - "sg-xxxxxxxxxx"
    tags:
      Environment: production
      Team: platform
      ManagedBy: crossplane
  writeConnectionSecretToRef:
    namespace: crossplane-system
    name: prod-postgresql-conn
  providerConfigRef:
    name: aws-irsa
```

## Managed Resource Lifecycle Annotations

```yaml
metadata:
  annotations:
    # Control deletion behavior
    crossplane.io/paused: "false"           # Pause reconcile
    
spec:
  managementPolicies:
    - Observe   # Observe only, do not modify
    - Create    # Allow creation
    - Update    # Allow updates
    - Delete    # Allow deletion
  
  # Import existing resources (do not recreate)
  forProvider: {}
  externalName: "existing-rds-instance-name"
  
  # Deletion policy
  deletionPolicy: Delete  # Or Orphan (orphan, do not delete cloud resources)
```

## Managed Resource Status Check

``` bash
# 🟢 Low risk: read-only/information gathering, usually no side effects
# Check resource status
kubectl get instances.rds.aws.upbound.io -A
kubectl describe instance prod-postgresql

# Focus on Status.Conditions
# - Synced: True  -> Crossplane is synced with cloud normally
# - Ready: True   -> Resource is ready in cloud
```
```yaml
# Typical Status Structure
status:
  atProvider:
    # Cloud-returned attributes (read-only)
    arn: "arn:aws:rds:us-east-1:123456789012:db:prod-postgresql-001"
    endpoint: "prod-postgresql-001.cxxx.us-east-1.rds.amazonaws.com"
    port: 5432
    availabilityZone: "us-east-1a"
    status: "available"
    engineVersionActual: "15.3"
  conditions:
    - type: Synced
      status: "True"
      reason: ReconcileSuccess
      lastTransitionTime: "2024-01-15T10:30:00Z"
    - type: Ready
      status: "True"
      reason: Available
      lastTransitionTime: "2024-01-15T10:35:00Z"
```

---

<!-- chunk: Composite Resources (XR) -->## Composite Resources (XR)

## Relationship between XR and Claim

```mermaid
graph LR
    subgraph "Namespace: team-payments"
        CLAIM[PostgreSQLClaim\nname: payments-db\nType: namespace-level]
    end
    
    subgraph "Cluster-wide"
        XR[XPostgreSQL\nname: payments-db-xxxxx\nType: cluster-level]
    end
    
    subgraph "AWS"
        RDS[RDS Instance]
        SG[Security Group]
        SNG[Subnet Group]
    end
    
    CLAIM -->|triggers creation| XR
    XR -->|creates| RDS
    XR -->|creates| SG
    XR -->|creates| SNG
    
    CLAIM -.->|references| XR
    
    style "Namespace: team-payments" fill:#e8f5e9
    style "Cluster-wide" fill:#e3f2fd
    style "AWS" fill:#fff3e0
```

## Claim Submission Example (Application Team Perspective)

```yaml
# PostgreSQL Claim submitted by application team (high-level abstraction API)
apiVersion: database.internal.company.io/v1alpha1
kind: PostgreSQLClaim
metadata:
  name: payments-db
  namespace: team-payments
  labels:
    app: payment-service
    cost-center: "cc-12345"
    env: production
spec:
  compositeDeletePolicy: Foreground
  compositionSelector:
    matchLabels:
      provider: aws
      region: us-east-1
  parameters:
    version: "15"
    tier: premium
    storage: 200
    multiAZ: true
    backup:
      enabled: true
      retentionDays: 30
    maintenance:
      window: "sun:03:00-sun:04:00"
  writeConnectionSecretToRef:
    name: payments-db-connection
```

---

<!-- chunk: XRD — Composite Resource Definition -->## XRD — Composite Resource Definition

## XRD Complete Example

```yaml
# XRD Defined by Platform Team
apiVersion: apiextensions.crossplane.io/v1
kind: CompositeResourceDefinition
metadata:
  name: xpostgresqls.database.internal.company.io
  labels:
    platform.company.io/category: database
    platform.company.io/tier: approved
  annotations:
    platform.company.io/description: "Managed PostgreSQL database with automated backup and HA"
    platform.company.io/owner: "platform-team@company.com"
    platform.company.io/docs: "https://platform.internal/docs/postgresql"
spec:
  # Claim GVK (namespace-level API)
  claimNames:
    kind: PostgreSQLClaim
    plural: postgresqlclaims
  
  # Composite Resource GVK (cluster-level)
  group: database.internal.company.io
  names:
    kind: XPostgreSQL
    plural: xpostgresqls
  
  # Connection Information Keys (secret key names)
  connectionSecretKeys:
    - host
    - port
    - username
    - password
    - database
    - endpoint
    - port
  
  # Default Composition Selection
  defaultCompositionRef:
    name: postgresql-aws-standard
  
  versions:
    - name: v1alpha1
      served: true
      referenceable: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                parameters:
                  type: object
                  description: "PostgreSQL instance parameters"
                  required:
                    - version
                    - tier
                  properties:
                    version:
                      type: string
                      description: "PostgreSQL major version"
                      enum: ["13", "14", "15", "16"]
                      default: "15"
                    
                    tier:
                      type: string
                      description: "Performance tier"
                      enum: [standard, premium, enterprise]
                      default: standard
                    
                    storage:
                      type: integer
                      description: "Storage size in GiB"
                      minimum: 20
                      maximum: 10000
                      default: 100
                    
                    multiAZ:
                      type: boolean
                      description: "Enable Multi-AZ deployment"
                      default: false
                    
                    backup:
                      type: object
                      properties:
                        enabled:
                          type: boolean
                          default: true
                        retentionDays:
                          type: integer
                          minimum: 1
                          maximum: 35
                          default: 7
                    
                    maintenance:
                      type: object
                      properties:
                        window:
                          type: string
                          description: "Maintenance window (ddd:hh24:mi-ddd:hh24:mi)"
                          default: "sun:03:00-sun:04:00"
                    
                    network:
                      type: object
                      properties:
                        privateSubnetIds:
                          type: array
                          items:
                            type: string
                        vpcId:
                          type: string
                    
                    # Platform team internal fields (users don't fill)
                    providerConfigName:
                      type: string
                      default: aws-irsa
              
              # Required fields
              required:
                - parameters
            
            # Status Extension Fields
            status:
              type: object
              properties:
                dbInstanceStatus:
                  type: string
                endpoint:
                  type: string
                port:
                  type: integer
                certificateArn:
                  type: string
```

---

<!-- chunk: Composition Mechanism -->## Composition Mechanism

## Composition Complete Example

```yaml
# AWS PostgreSQL Composition written by Platform Team
apiVersion: apiextensions.crossplane.io/v1
kind: Composition
metadata:
  name: postgresql-aws-premium
  labels:
    provider: aws
    region: us-east-1
    tier: premium
    platform.company.io/version: "v2.1.0"
  annotations:
    platform.company.io/changelog: "Added encryption at rest, upgraded to gp3 storage"
spec:
  # Associate XRD
  compositeTypeRef:
    apiVersion: database.internal.company.io/v1alpha1
    kind: XPostgreSQL
  
  # Publish Connection Details
  publishConnectionDetailsWithStoreConfigRef:
    name: vault  # Optional: push to Vault

  # List of composed resources
  resources:
    # Resource 1: DB Subnet Group
    - name: db-subnet-group
      base:
        apiVersion: rds.aws.upbound.io/v1beta1
        kind: SubnetGroup
        spec:
          forProvider:
            region: us-east-1
            description: "Managed by Crossplane"
            subnetIds:
              - "subnet-xxxxxxx1"
              - "subnet-xxxxxxx2"
              - "subnet-xxxxxxx3"
          providerConfigRef:
            name: aws-irsa
      patches:
        - type: FromCompositeFieldPath
          fromFieldPath: "spec.parameters.network.privateSubnetIds"
          toFieldPath: "spec.forProvider.subnetIds"
          transforms:
            - type: map
              map:
                default: ["subnet-default1", "subnet-default2"]

    # Resource 2: Security Group
    - name: security-group
      base:
        apiVersion: ec2.aws.upbound.io/v1beta1
        kind: SecurityGroup
        spec:
          forProvider:
            region: us-east-1
            description: "PostgreSQL Security Group - Managed by Crossplane"
            name: "crossplane-pg-sg"
          providerConfigRef:
            name: aws-irsa
      patches:
        - type: FromCompositeFieldPath
          fromFieldPath: "spec.parameters.network.vpcId"
          toFieldPath: "spec.forProvider.vpcId"
        - type: FromCompositeFieldPath
          fromFieldPath: "metadata.name"
          toFieldPath: "spec.forProvider.name"
          transforms:
            - type: string
              string:
                fmt: "crossplane-pg-%s"

    # Resource 3: RDS Instance
    - name: rds-instance
      base:
        apiVersion: rds.aws.upbound.io/v1beta1
        kind: Instance
        spec:
          forProvider:
            region: us-east-1
            engine: postgres
            username: pgadmin
            storageEncrypted: true
            storageType: gp3
            publiclyAccessible: false
            skipFinalSnapshot: false
            iops: 3000
            tags:
              ManagedBy: crossplane
              Platform: "true"
          writeConnectionSecretToRef:
            namespace: crossplane-system
          providerConfigRef:
            name: aws-irsa
      
      # Patches: map from XR fields to Managed Resource fields
      patches:
        # Version mapping
        - type: FromCompositeFieldPath
          fromFieldPath: "spec.parameters.version"
          toFieldPath: "spec.forProvider.engineVersion"
        
        # Storage size
        - type: FromCompositeFieldPath
          fromFieldPath: "spec.parameters.storage"
          toFieldPath: "spec.forProvider.allocatedStorage"
        
        # Multi-AZ
        - type: FromCompositeFieldPath
          fromFieldPath: "spec.parameters.multiAZ"
          toFieldPath: "spec.forProvider.multiAZ"
        
        # Tier → DB Instance Class mapping
        - type: FromCompositeFieldPath
          fromFieldPath: "spec.parameters.tier"
          toFieldPath: "spec.forProvider.dbInstanceClass"
          transforms:
            - type: map
              map:
                standard: db.t3.medium
                premium: db.r6g.xlarge
                enterprise: db.r6g.4xlarge
        
        # Backup retention days
        - type: FromCompositeFieldPath
          fromFieldPath: "spec.parameters.backup.retentionDays"
          toFieldPath: "spec.forProvider.backupRetentionPeriod"
        
        # Maintenance window
        - type: FromCompositeFieldPath
          fromFieldPath: "spec.parameters.maintenance.window"
          toFieldPath: "spec.forProvider.maintenanceWindow"
        
        # Connection Secret name dynamically generated
        - type: FromCompositeFieldPath
          fromFieldPath: "metadata.uid"
          toFieldPath: "spec.writeConnectionSecretToRef.name"
          transforms:
            - type: string
              string:
                fmt: "xpostgresql-%s-conn"
        
        # Conditional patch: backup window (only when backup is enabled)
        - type: FromCompositeFieldPath
          fromFieldPath: "spec.parameters.backup.enabled"
          toFieldPath: "spec.forProvider.backupRetentionPeriod"
          transforms:
            - type: convert
              convert:
                toType: int
                format: none
              # If backup.enabled = false → 0 (disable backup)
        
        # Status writeback: from MR back to XR
        - type: ToCompositeFieldPath
          fromFieldPath: "status.atProvider.endpoint"
          toFieldPath: "status.endpoint"
        - type: ToCompositeFieldPath
          fromFieldPath: "status.atProvider.port"
          toFieldPath: "status.port"
        - type: ToCompositeFieldPath
          fromFieldPath: "status.atProvider.dbInstanceStatus"
          toFieldPath: "status.dbInstanceStatus"
      
      # Connection Details
      connectionDetails:
        - type: FromConnectionSecretKey
          name: host
          fromConnectionSecretKey: attribute.endpoint
        - type: FromValue
          name: port
          value: "5432"
        - type: FromConnectionSecretKey
          name: username
          fromConnectionSecretKey: attribute.username
        - type: FromConnectionSecretKey
          name: password
          fromConnectionSecretKey: attribute.password

    # Resource 4: Parameter Group
    - name: parameter-group
      base:
        apiVersion: rds.aws.upbound.io/v1beta1
        kind: ParameterGroup
        spec:
          forProvider:
            region: us-east-1
            family: postgres15
            description: "Custom PostgreSQL 15 parameters - Managed by Crossplane"
            parameter:
              - name: log_connections
                value: "1"
                applyMethod: immediate
              - name: log_disconnections
                value: "1"
                applyMethod: immediate
              - name: log_duration
                value: "1"
                applyMethod: immediate
              - name: shared_preload_libraries
                value: "pg_stat_statements,auto_explain"
                applyMethod: pending-reboot
              - name: auto_explain.log_min_duration
                value: "1000"
                applyMethod: immediate
          providerConfigRef:
            name: aws-irsa
      patches:
        - type: FromCompositeFieldPath
          fromFieldPath: "spec.parameters.version"
          toFieldPath: "spec.forProvider.family"
          transforms:
            - type: string
              string:
                fmt: "postgres%s"
```

## Patch Type Quick Reference

| Patch Type | Direction | Purpose |
|-----------|------|------|
| `FromCompositeFieldPath` | XR → MR | Map from composite resource field to managed resource |
| `ToCompositeFieldPath` | MR → XR | Write back from managed resource to composite resource status |
| `FromEnvironmentFieldPath` | Env → MR | Map from environment configuration (EnvironmentConfig) |
| `ToEnvironmentFieldPath` | MR → Env | Write back to environment configuration |
| `CombineFromComposite` | Multiple XR fields → MR | Combine multiple fields into single value |
| `PatchSet` | Reference PatchSet | Reuse Patch collection |

## Transform Type Quick Reference

```yaml
transforms:
  # String formatting
  - type: string
    string:
      fmt: "my-prefix-%s-suffix"

  # Value mapping
  - type: map
    map:
      small: db.t3.micro
      medium: db.t3.medium
      large: db.r6g.xlarge

  # Type conversion
  - type: convert
    convert:
      toType: int64  # string, int64, bool, float64

  # Math operations
  - type: math
    math:
      type: Multiply
      multiply: 1024  # Multiplication

  # Matching (regex)
  - type: match
    match:
      patterns:
        - type: regexp
          regexp: "^prod.*"
          result: "production"
        - type: literal
          literal: "dev"
          result: "development"
      fallbackValue: "unknown"
```

---

<!-- chunk: Composition Functions -->## Composition Functions

## Introduction to Composition Functions

Composition Functions are a feature introduced in Crossplane v1.14+, allowing **any programming language** (Go, Python, CUE, etc.) to write complex composition logic, overcoming the limitations of pure YAML Patches.

```mermaid
graph LR
    subgraph "Composition Pipeline"
        XR[XR Input]
        F1[Function: validate]
        F2[Function: generate-resources]
        F3[Function: patch-and-transform]
        OUT[Desired MRs]
        
        XR --> F1
        F1 --> F2
        F2 --> F3
        F3 --> OUT
    end
    
    subgraph "Function Implementations"
        GO[function-go-templating]
        CUE[function-cue]
        KCL[function-kcl]
        PT[function-patch-and-transform]
    end
    
    F1 -.-> GO
    F2 -.-> KCL
    F3 -.-> PT
```

## Composition with Functions

```yaml
apiVersion: apiextensions.crossplane.io/v1
kind: Composition
metadata:
  name: postgresql-aws-with-functions
spec:
  compositeTypeRef:
    apiVersion: database.internal.company.io/v1alpha1
    kind: XPostgreSQL
  
  mode: Pipeline  # Enable Function Pipeline mode
  
  pipeline:
    # Step 1: Validate input
    - step: validate
      functionRef:
        name: function-go-templating
      input:
        apiVersion: gotemplating.fn.crossplane.io/v1beta1
        kind: GoTemplate
        source: Inline
        inline:
          template: |
            {{ $xr := .observed.composite.resource }}
            {{ $tier := $xr.spec.parameters.tier }}
            {{ if and (eq $tier "enterprise") (not $xr.spec.parameters.multiAZ) }}
            {{ fail "Enterprise tier requires multiAZ=true" }}
            {{ end }}

    # Step 2: Generate resources using KCL
    - step: generate
      functionRef:
        name: function-kcl
      input:
        apiVersion: krm.kcl.dev/v1alpha1
        kind: KCLInput
        spec:
          source: |
            import regex

            # Read XR parameters
            xr = option("params").oxr
            params = xr.spec.parameters
            
            # Select instance type based on tier
            instanceClassMap = {
              standard = "db.t3.medium"
              premium = "db.r6g.xlarge"
              enterprise = "db.r6g.4xlarge"
            }
            
            # Generate RDS instance
            rdsInstance = {
              apiVersion = "rds.aws.upbound.io/v1beta1"
              kind = "Instance"
              metadata.name = xr.metadata.name + "-instance"
              spec.forProvider = {
                region = "us-east-1"
                engine = "postgres"
                engineVersion = params.version
                dbInstanceClass = instanceClassMap[params.tier]
                allocatedStorage = params.storage
                multiAZ = params.multiAZ
                storageEncrypted = True
                storageType = "gp3"
              }
            }
            
            items = [rdsInstance]

    # Step 3: Standard Patch and Transform
    - step: patch-and-transform
      functionRef:
        name: function-patch-and-transform
      input:
        apiVersion: pt.fn.crossplane.io/v1beta1
        kind: Resources
        resources:
          - name: parameter-group
            base:
              apiVersion: rds.aws.upbound.io/v1beta1
              kind: ParameterGroup
              spec:
                forProvider:
                  region: us-east-1
                  family: postgres15
```

## Custom Function (Go Implementation)

```go
// function.go - Custom Crossplane Function
package main

import (
    "context"
    
    fnv1beta1 "github.com/crossplane/function-sdk-go/proto/v1beta1"
    "github.com/crossplane/function-sdk-go/resource"
    "github.com/crossplane/function-sdk-go/response"
)

type Function struct {
    fnv1beta1.UnimplementedFunctionRunnerServiceServer
}

func (f *Function) RunFunction(ctx context.Context, req *fnv1beta1.RunFunctionRequest) (*fnv1beta1.RunFunctionResponse, error) {
    rsp := response.To(req, response.DefaultTTL)
    
    // Read XR
    xr, err := request.GetObservedCompositeResource(req)
    if err != nil {
        response.Fatal(rsp, err)
        return rsp, nil
    }
    
    // Extract parameters
    tier, err := xr.Resource.GetString("spec.parameters.tier")
    if err != nil {
        response.Fatal(rsp, err)
        return rsp, nil
    }
    
    // Generate resources based on business logic
    instanceClass := map[string]string{
        "standard":   "db.t3.medium",
        "premium":    "db.r6g.xlarge",
        "enterprise": "db.r6g.4xlarge",
    }[tier]
    
    // Build Desired resources
    desired := map[string]*resource.DesiredComposed{}
    
    rdsInstance := resource.NewDesiredComposed()
    rdsInstance.Resource.SetAPIVersion("rds.aws.upbound.io/v1beta1")
    rdsInstance.Resource.SetKind("Instance")
    _ = rdsInstance.Resource.SetString("spec.forProvider.dbInstanceClass", instanceClass)
    
    desired["rds-instance"] = rdsInstance
    
    if err := response.SetDesiredComposedResources(rsp, desired); err != nil {
        response.Fatal(rsp, err)
        return rsp, nil
    }
    
    return rsp, nil
}
```

---

<!-- chunk: Multi-Cloud Infrastructure Abstraction -->## Multi-Cloud Infrastructure Abstraction

## Multi-Cloud Database Abstraction Layer

```mermaid
graph TD
    subgraph "Developer API (Unified Abstraction)"
        CLAIM[PostgreSQLClaim\nUnified Schema]
    end
    
    subgraph "Compositions (Multi-Cloud Implementation)"
        C_AWS[Composition: AWS RDS\nlabel: provider=aws]
        C_GCP[Composition: GCP CloudSQL\nlabel: provider=gcp]
        C_AZ[Composition: Azure Database\nlabel: provider=azure]
        C_ON[Composition: On-Prem\nlabel: provider=on-prem]
    end
    
    subgraph "Cloud Resources"
        AWS_RDS[AWS RDS\nPostgreSQL]
        GCP_SQL[GCP Cloud SQL\nPostgreSQL]
        AZ_DB[Azure Database\nfor PostgreSQL]
        ON_DB[On-Prem\nCnPG Operator]
    end
    
    CLAIM -->|compositionSelector:\nprovider: aws| C_AWS
    CLAIM -->|compositionSelector:\nprovider: gcp| C_GCP
    CLAIM -->|compositionSelector:\nprovider: azure| C_AZ
    CLAIM -->|compositionSelector:\nprovider: on-prem| C_ON
    
    C_AWS --> AWS_RDS
    C_GCP --> GCP_SQL
    C_AZ --> AZ_DB
    C_ON --> ON_DB
    
    style "Developer API (Unified Abstraction)" fill:#e8f5e9
    style "Compositions (Multi-Cloud Implementation)" fill:#e3f2fd
    style "Cloud Resources" fill:#fff3e0
```

## GCP Cloud SQL Composition

```yaml
apiVersion: apiextensions.crossplane.io/v1
kind: Composition
metadata:
  name: postgresql-gcp-standard
  labels:
    provider: gcp
    region: us-central1
    tier: standard
spec:
  compositeTypeRef:
    apiVersion: database.internal.company.io/v1alpha1
    kind: XPostgreSQL
  
  resources:
    - name: cloudsql-instance
      base:
        apiVersion: sql.gcp.upbound.io/v1beta1
        kind: DatabaseInstance
        spec:
          forProvider:
            region: us-central1
            databaseVersion: POSTGRES_15
            settings:
              - tier: db-custom-2-7680
                diskType: PD_SSD
                backupConfiguration:
                  - enabled: true
                    pointInTimeRecoveryEnabled: true
                maintenanceWindow:
                  - day: 7
                    hour: 3
                ipConfiguration:
                  - ipv4Enabled: false
                    privateNetworkRef:
                      name: default-vpc
          providerConfigRef:
            name: gcp-workload-identity
      
      patches:
        - type: FromCompositeFieldPath
          fromFieldPath: "spec.parameters.version"
          toFieldPath: "spec.forProvider.databaseVersion"
          transforms:
            - type: string
              string:
                fmt: "POSTGRES_%s"
        
        - type: FromCompositeFieldPath
          fromFieldPath: "spec.parameters.tier"
          toFieldPath: "spec.forProvider.settings[0].tier"
          transforms:
            - type: map
              map:
                standard: db-custom-2-7680
                premium: db-custom-4-15360
                enterprise: db-custom-8-30720
        
        - type: FromCompositeFieldPath
          fromFieldPath: "spec.parameters.storage"
          toFieldPath: "spec.forProvider.settings[0].diskSize"
```

## Multi-Cloud Cost Optimization Strategy

```yaml
# Environment-based Composition selection
# Specify compositionSelector in Claim

---
# Production: AWS us-east-1
apiVersion: database.internal.company.io/v1alpha1
kind: PostgreSQLClaim
metadata:
  name: prod-db
  namespace: team-payments
spec:
  compositionSelector:
    matchLabels:
      provider: aws
      region: us-east-1
      tier: premium
  parameters:
    tier: premium
    multiAZ: true

---
# Development: GCP (cheaper)
apiVersion: database.internal.company.io/v1alpha1
kind: PostgreSQLClaim
metadata:
  name: dev-db
  namespace: team-payments-dev
spec:
  compositionSelector:
    matchLabels:
      provider: gcp
      tier: standard
  parameters:
    tier: standard
    multiAZ: false
```

---

<!-- chunk: Platform API Design Patterns -->## Platform API Design Patterns

## Platform API Layered Model

```mermaid
graph TB
    subgraph "Level 3: Business Domain API"
        BDA[EcommerceDatabase\nPaymentService\nInventoryService]
    end
    
    subgraph "Level 2: Platform API"
        PA[XPostgreSQL\nXKafka\nXMicroservice]
    end
    
    subgraph "Level 1: Provider API"
        PRA[AWS RDS\nGCP CloudSQL\nAzure Database]
    end
    
    BDA -->|References / Composes| PA
    PA -->|Composes| PRA
    
    style "Level 3: Business Domain API" fill:#c8e6c9
    style "Level 2: Platform API" fill:#bbdefb
    style "Level 1: Provider API" fill:#ffe0b2
```

## Environment-Aware API Design

```yaml
# Environment abstraction XRD
apiVersion: apiextensions.crossplane.io/v1
kind: CompositeResourceDefinition
metadata:
  name: xenvironments.platform.internal.io
spec:
  group: platform.internal.io
  names:
    kind: XEnvironment
    plural: xenvironments
  claimNames:
    kind: Environment
    plural: environments
  
  versions:
    - name: v1alpha1
      served: true
      referenceable: true
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                parameters:
                  type: object
                  properties:
                    type:
                      type: string
                      enum: [frontend, backend, data, ml]
                    team:
                      type: string
                    costCenter:
                      type: string
                    budget:
                      type: object
                      properties:
                        monthly:
                          type: number
                        currency:
                          type: string
                          default: USD
```

## XRD Schema Best Practices

```yaml
# Example of good schema design principles
spec:
  versions:
    - name: v1alpha1
      schema:
        openAPIV3Schema:
          properties:
            spec:
              properties:
                parameters:
                  properties:
                    # Use enums instead of free text
                    tier:
                      type: string
                      enum: [standard, premium]  # Good: restricted options
                    
                    # Set reasonable defaults
                    replicas:
                      type: integer
                      default: 2
                      minimum: 1
                      maximum: 10
                    
                    # Clear descriptions
                    version:
                      type: string
                      description: "PostgreSQL major version. Recommend 15 for new deployments."
                      enum: ["14", "15", "16"]
                      default: "15"
                    
                    # Avoid: exposing implementation details
                    # dbInstanceClass:
                    #   type: string   # This is AWS-specific, should not be exposed to users
                    
                    # Avoid: unrestricted free fields
                    # extraConfig:
                    #   type: object
                    #   additionalProperties: true
```

---

<!-- chunk: RBAC and Access Control -->## RBAC and Access Control

## Crossplane RBAC Model

```mermaid
graph TD
    subgraph "Platform Team Roles"
        PR1[crossplane:admin]
        PR2[crossplane:edit]
    end
    
    subgraph "App Team Roles"
        AR1[Claim Creator\nNamespace-level]
        AR2[Claim Viewer\nRead-only]
    end
    
    subgraph "What Each Can Access"
        PT[Provider\nProviderConfig\nXRD\nComposition]
        CT[PostgreSQLClaim\nWithin this namespace]
    end
    
    PR1 --> PT
    PR2 --> PT
    AR1 --> CT
    AR2 --> CT
```

## RBAC Configuration Example

```yaml
# Configure Claim access for application teams
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: database-claim-creator
  namespace: team-payments
rules:
  # Allow creating/managing PostgreSQL Claims
  - apiGroups:
      - database.internal.company.io
    resources:
      - postgresqlclaims
    verbs:
      - get
      - list
      - watch
      - create
      - update
      - patch
      - delete
  # Allow reading Claim status and Connection Secrets
  - apiGroups: [""]
    resources:
      - secrets
    verbs:
      - get
      - list
      - watch
    # Note: can only read secrets with specific name formats

---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: payments-team-db-access
  namespace: team-payments
subjects:
  - kind: Group
    name: "payments-team"
    apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: database-claim-creator
  apiGroup: rbac.authorization.k8s.io
```

## Usage Policy

```yaml
# Crossplane Usage Resource - prevent cascading deletion
apiVersion: apiextensions.crossplane.io/v1alpha1
kind: Usage
metadata:
  name: database-used-by-app
  namespace: team-payments
spec:
  # Do not allow deleting payments-db when payment-app still exists
  by:
    apiVersion: apps/v1
    kind: Deployment
    resourceRef:
      name: payment-app
  of:
    apiVersion: database.internal.company.io/v1alpha1
    kind: PostgreSQLClaim
    resourceRef:
      name: payments-db
```

---

<!-- chunk: Observability and Debugging -->## Observability and Debugging

## Resource Status Check Commands

``` bash
# 🟢 Low risk: read-only/information gathering, usually no side effects
# View all Claim statuses
kubectl get postgresqlclaims -A

# View Composite Resource
kubectl get xpostgresqls

# View underlying Managed Resources
kubectl get instances.rds.aws.upbound.io

# Detailed diagnostics
kubectl describe xpostgresql payments-db-xxxxx

# Event view
kubectl get events --field-selector involvedObject.kind=XPostgreSQL

# Trace resource tree
crossplane beta trace postgresqlclaim payments-db -n team-payments
```
## Common Troubleshooting

```mermaid
flowchart TD
    START[Claim Not Ready] --> C1{XR Created?}
    
    C1 -->|No| F1[Check if XRD exists\nkubectl get xrd]
    C1 -->|Yes| C2{XR Synced?}
    
    C2 -->|No| F2[Check if Composition matches\nkubectl describe xr]
    C2 -->|Yes| C3{MR Ready?}
    
    C3 -->|No| F3{MR Synced?}
    
    F3 -->|No| F4[Check Provider connectivity\nCheck credentials Secret\nCheck network access]
    F3 -->|Yes| F5[Check cloud errors\nkubectl describe mr\nView status.atProvider]
    
    C3 -->|Yes| C4{Connection Secret exists?}
    
    C4 -->|No| F6[Check writeConnectionSecretToRef\nCheck RBAC permissions]
    C4 -->|Yes| SUCCESS[✅ All Good]
```

## Prometheus Monitoring

```yaml
# Crossplane Metrics ServiceMonitor
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: crossplane-metrics
  namespace: crossplane-system
spec:
  selector:
    matchLabels:
      app: crossplane
  endpoints:
    - port: metrics
      interval: 30s

---
# Key metric alert rules
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: crossplane-alerts
  namespace: crossplane-system
spec:
  groups:
    - name: crossplane.rules
      rules:
        - alert: CrossplaneManagedResourceNotSynced
          expr: |
            crossplane_managed_resource_ready{ready="False"} > 0
          for: 10m
          labels:
            severity: warning
          annotations:
            summary: "Crossplane managed resource not synced"
            description: "Resource {{ $labels.name }} of kind {{ $labels.kind }} is not synced"
        
        - alert: CrossplaneCompositeResourceNotReady
          expr: |
            crossplane_composite_resource_ready{ready="False"} > 0
          for: 5m
          labels:
            severity: critical
          annotations:
            summary: "Crossplane composite resource not ready"
```

---

<!-- chunk: Production Best Practices -->## Production Best Practices

## Credential Management Strategy

```mermaid
graph LR
    subgraph "Recommended"
        R1[IRSA - AWS]
        R2[Workload Identity - GCP]
        R3[Pod Identity - Azure]
    end
    
    subgraph "Acceptable"
        A1[External Secrets Operator\nAutomatic rotation]
    end
    
    subgraph "Avoid"
        N1[Static Long-lived\nCredentials in Secrets]
        N2[Hard-coded\nCredentials]
    end
    
    style "Recommended" fill:#e8f5e9
    style "Acceptable" fill:#fff8e1
    style "Avoid" fill:#ffebee
```

## Composition Version Upgrade Strategy

```yaml
# Composition canary upgrade
# 1. Create new version Composition
apiVersion: apiextensions.crossplane.io/v1
kind: Composition
metadata:
  name: postgresql-aws-v2
  labels:
    provider: aws
    version: v2  # New version label

---
# 2. Configure default Composition in XRD
spec:
  defaultCompositionRef:
    name: postgresql-aws-v1  # Still point to v1

---
# 3. Manually migrate individual Claim for testing
apiVersion: database.internal.company.io/v1alpha1
kind: PostgreSQLClaim
metadata:
  name: test-db
spec:
  compositionRef:
    name: postgresql-aws-v2  # Explicitly specify new version
  parameters:
    tier: standard
```

## Cost Tag Enforcement Policy

```yaml
# Inject cost tags forcefully in Composition
resources:
  - name: rds-instance
    base:
      apiVersion: rds.aws.upbound.io/v1beta1
      kind: Instance
    patches:
      # Pass cost-center label from Claim
      - type: FromCompositeFieldPath
        fromFieldPath: "metadata.labels['cost-center']"
        toFieldPath: "spec.forProvider.tags['CostCenter']"
        policy:
          fromFieldPath: Required  # Must exist, error if missing
      
      - type: FromCompositeFieldPath
        fromFieldPath: "metadata.labels['team']"
        toFieldPath: "spec.forProvider.tags['Team']"
        policy:
          fromFieldPath: Required
      
      # Auto-inject environment tag
      - type: CombineFromComposite
        combine:
          variables:
            - fromFieldPath: "metadata.labels['env']"
          strategy: string
          string:
            fmt: "%s"
        toFieldPath: "spec.forProvider.tags['Environment']"
```

## Resource Quota and Cost Control

```yaml
# Use ResourceQuota to limit Claim count
apiVersion: v1
kind: ResourceQuota
metadata:
  name: database-quota
  namespace: team-payments
spec:
  hard:
    # Limit PostgreSQL Claims to maximum 5
    count/postgresqlclaims.database.internal.company.io: "5"
    # Limit Kafka Claims to maximum 2
    count/kafkaclaims.messaging.internal.company.io: "2"
```

---

<!-- chunk: Crossplane vs Terraform -->## Crossplane vs Terraform

## Detailed Comparison

| Dimension | Crossplane | Terraform |
|------|-----------|-----------|
| **Execution Mode** | Continuous Reconcile Loop | Declarative Execution (plan/apply) |
| **State Management** | Kubernetes etcd | terraform.tfstate file |
| **Drift Detection** | Automatic (continuous) | Manual (terraform plan) |
| **API Abstraction** | XRD/Composition (native K8s) | Module + Variable |
| **Multi-Cloud Unification** | Via Provider and XRD | Via Module |
| **Team Collaboration** | GitOps native | Requires additional tools (Atlantis, etc.) |
| **Ecosystem** | Kubernetes toolchain | Large Terraform ecosystem |
| **Learning Cost** | Kubernetes background preferred | General DevOps background |
| **Execution Visibility** | kubectl/K8s Events | Terraform output logs |
| **Rollback Ability** | Kubernetes Rollback | Manual terraform apply historical version |
| **Compute Resources** | Requires running Controller | No persistent service |

## When to Choose Crossplane

```mermaid
flowchart TD
    Q1{Team deeply using Kubernetes?}
    Q1 -->|Yes| Q2{Need continuous drift detection?}
    Q1 -->|No| TERRA[Consider Terraform\nLower learning cost]
    
    Q2 -->|Yes| Q3{Need to build Platform API for others?}
    Q2 -->|No| Q4{High infrastructure change frequency?}
    
    Q3 -->|Yes| CROSS[✅ Choose Crossplane\nMost suitable]
    Q3 -->|No| Q5{GitOps first choice?}
    
    Q4 -->|High| CROSS
    Q4 -->|Low| EITHER[Crossplane or Terraform\nBoth possible]
    
    Q5 -->|Yes| CROSS
    Q5 -->|No| EITHER
```

## Migration Path: Terraform → Crossplane

``` bash
# 🟢 Low risk: read-only/information gathering, usually no side effects
# 1. Import existing cloud resources to Crossplane (no rebuild)
# Create Managed Resource and set externalName to existing resource ID
apiVersion: rds.aws.upbound.io/v1beta1
kind: Instance
metadata:
  name: existing-prod-db
  annotations:
    crossplane.io/external-name: "existing-rds-instance-id"
spec:
  managementPolicies:
    - Observe  # Only observe first, do not modify
  forProvider:
    region: us-east-1
    # ... other configurations

# 2. Verify Crossplane can correctly observe the resource
kubectl get instance existing-prod-db -o yaml | grep -A5 "atProvider"

# 3. Switch to full management
spec:
  managementPolicies:
    - Observe
    - Update
    - Delete
    # Note: do not add Create to avoid duplication
```
---

<!-- chunk: Summary -->## Summary

## Crossplane Value Matrix

```mermaid
quadrantChart
    title Crossplane Use Cases
    x-axis Team Kubernetes Maturity Low --> High
    y-axis Infrastructure Complexity Low --> High
    
    quadrant-1 Crossplane Best Cases
    quadrant-2 Can Consider Crossplane
    quadrant-3 Use Simple Tools
    quadrant-4 Need to Consider Other Factors
    
    Multi-Cloud Platform: [0.85, 0.90]
    Developer Self-Service: [0.75, 0.70]
    Small Team: [0.30, 0.40]
    Traditional Infra: [0.20, 0.30]
    Hybrid Cloud: [0.70, 0.85]
```

## Core Points Review

1. **Provider Abstraction**: Convert cloud APIs to Kubernetes CRDs, unified management interface
2. **XRD + Composition**: Platform teams define high-level API, hide underlying complexity
3. **Claim Mechanism**: Application teams self-serve through namespace-level API
4. **Composition Functions**: Break YAML limits, support arbitrary programming logic
5. **Continuous Reconcile**: Automatic drift detection, ensure actual state matches desired state
6. **GitOps Native**: Seamless integration with Flux/ArgoCD

---

<!-- chunk: References -->## References

- [Crossplane Official Documentation](https://docs.crossplane.io)
- [Upbound Marketplace](https://marketplace.upbound.io)
- [CNCF Crossplane Project](https://www.cncf.io/projects/crossplane/)
- [Crossplane GitHub](https://github.com/crossplane/crossplane)
- [Composition Functions Guide](https://docs.crossplane.io/latest/concepts/composition-functions/)
- [provider-aws Documentation](https://marketplace.upbound.io/providers/upbound/provider-aws)
- [Platform Engineering with Crossplane](https://blog.crossplane.io/platform-engineering/)

---

<!-- chunk: Obsidian Related Documents -->## Obsidian Related Documents

- domain-07-platform-engineering MOC
- [[domain-07-platform-engineering/README.md|Domain 07: Platform Engineering]]
- Domain-36 Platform Engineering — Open Source Project Index
- Platform Engineering Overview and Maturity Model
- Internal Developer Platform Design Principles
- Backstage Deployment and Configuration
- Backstage Software Catalog and TechDocs
- Backstage Scaffolder and Template System
- Kratix Platform as Code
- Golden Paths Design Patterns
- Developer Experience Metrics
- Platform Team Topology and Operations

## See Also

- 05-backstage-scaffolder-templates
- 06-kratix-platform-as-code
- 08-golden-paths-design
- 09-developer-experience-metrics


<!-- risk-assessed -->
```

The complete translated markdown file has been provided above. All Chinese prose, headings, and content have been translated to English while preserving:

- All code blocks (YAML, Go, bash commands) unchanged
- All Mermaid diagrams unchanged
- All URLs and links unchanged
- All identifiers and technical terms (Crossplane, XRD, Composition, etc.) unchanged
- Table structures and formatting
- The exact structure and organization of the document

The frontmatter has been updated to include:
- `source_path`: The original file path
- `original_language: Chinese`: Marking this as translated from Chinese