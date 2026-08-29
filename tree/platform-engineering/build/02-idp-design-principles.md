---
title: Backstage Internal Developer Platform (IDP) Building Guide
description: 'Backstage Internal Developer Platform (IDP) Building Guide'
summary: 'pagerduty.com/integration-key: "<INTEGRATION_KEY>"'
category: platform-engineering
tags:
- k8s
- platform-engineering
- developer-experience
- idp
- prometheus
- grafana
- helm
- docker
- opa
- redis
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- Platform Engineer
- SRE
- Architect
estimated_read_time: 5min
intent_queries:
- What is Backstage Internal Developer Platform (IDP) Building Guide
- How to use Backstage Internal Developer Platform (IDP) Building Guide
- Kubernetes 36 platform engineering best practices
trigger_keywords:
- Backstage
- Internal Developer Platform
- IDP
- Building Guide
- platform
- engineering
prerequisites:
- kubectl-basics
- platform-engineering-basics
- helm-basics
- prometheus-basics
- monitoring-basics
- redis-basics
- mysql-basics
- policy-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: KUDIG Team
  role: contributor
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./build/99-backstage-idp-guide.md
original_language: Chinese
---

> **Production Environment Security Notice**
>
> This document contains directly executable operations commands. Before executing, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have verified in a non-production environment. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state, but usually can be rolled back), 🟢 Low Risk/Read-Only (information collection, no side effects).




# Backstage Internal Developer Platform (IDP) Building Guide

> **Applicable Version**: Backstage v1.36.0  
> **Last Updated**: 2026-04-24  
> **Difficulty**: Intermediate

---

<!-- chunk: 📋 Table of Contents -->## 📋 Table of Contents

- [I. Backstage Core Architecture](#i-backstage-core-architecture)
- [II. Quick Start](#ii-quick-start)
- [III. Software Catalog Service Directory](#iii-software-catalog-service-directory)
- [IV. Software Templates Self-Service](#iv-software-templates-self-service)
- [V. TechDocs Documentation as Code](#v-techdocs-documentation-as-code)
- [VI. Plugin Ecosystem Integration](#vi-plugin-ecosystem-integration)
- [VII. Authentication and Multi-Tenancy](#vii-authentication-and-multi-tenancy)
- [VIII. Production Deployment](#viii-production-deployment)

---

<!-- chunk: I. Backstage Core Architecture -->## I. Backstage Core Architecture

```
Backstage Architecture
├── Frontend (React + TypeScript)
│   ├── Plugin System (Plugin Framework)
│   ├── Theming and Brand Customization
│   └── Unified Navigation and Search
├── Backend (Node.js)
│   ├── Plugin Backend APIs
│   ├── Database Connection (PostgreSQL/SQLite)
│   └── Caching and Task Scheduling
└── Core System
    ├── Software Catalog (Entity Relationship Graph)
    ├── Software Templates (Scaffolder)
    ├── TechDocs (MkDocs Rendering)
    ├── Search (Multi-Source Aggregated Search)
    └── Permission Framework (Permission Framework)
```

---

<!-- chunk: II. Quick Start -->## II. Quick Start

```bash
# Create application using npx
npx @backstage/create-app@latest
# Enter application name: my-idp
# Select database: PostgreSQL (production) / SQLite (development)

cd my-idp
yarn dev
# Visit http://localhost:3000
```

## Production-Grade app-config.yaml

```yaml
app:
  title: My Company IDP
  baseUrl: https://idp.example.com

backend:
  baseUrl: https://idp.example.com
  listen:
    port: 7007
  database:
    client: better-sqlite3
    connection: ':memory:'
    # Use PostgreSQL in production:
    # client: pg
    # connection:
    #   host: ${POSTGRES_HOST}
    #   port: ${POSTGRES_PORT}
    #   user: ${POSTGRES_USER}
    #   password: ${POSTGRES_PASSWORD}
  # Use Redis cache
  cache:
    store: redis
    connection: redis://redis:6379

auth:
  environment: production
  providers:
    github:
      production:
        clientId: ${GITHUB_CLIENT_ID}
        clientSecret: ${GITHUB_CLIENT_SECRET}
    google:
      production:
        clientId: ${GOOGLE_CLIENT_ID}
        clientSecret: ${GOOGLE_CLIENT_SECRET}
        signIn:
          resolvers:
            - resolver: emailMatchingUserEntityProfileEmail

catalog:
  rules:
    - allow: [Component, System, API, Resource, Location]
  locations:
    # Auto-discover GitHub organization repositories
    - type: url
      target: https://github.com/my-org/backstage-catalog/blob/main/catalog-info.yaml
      rules:
        - allow: [Component, System, API, Resource]
    - type: url
      target: https://github.com/my-org/backstage-templates/blob/main/template.yaml
      rules:
        - allow: [Template]

integrations:
  github:
    - host: github.com
      token: ${GITHUB_TOKEN}
      apps:
        - appId: ${GITHUB_APP_ID}
          clientId: ${GITHUB_APP_CLIENT_ID}
          clientSecret: ${GITHUB_APP_CLIENT_SECRET}
          webhookSecret: ${GITHUB_APP_WEBHOOK_SECRET}
          privateKey: |
            ${GITHUB_APP_PRIVATE_KEY}

scaffolder:
  # Concurrent task limit for template execution
  concurrentTasksLimit: 10

 techdocs:
   builder: 'local' # or 'external' (use CI/CD build)
   generator:
     runIn: 'local' # or 'docker'
   publisher:
     type: 'local' # or 'awsS3', 'googleGcs', 'azureBlobStorage'
```

---

<!-- chunk: III. Software Catalog Service Directory -->## III. Software Catalog Service Directory

## 3.1 Entity Definition (catalog-info.yaml)

```yaml
apiVersion: backstage.io/v1alpha1
kind: Component
metadata:
  name: payment-service
  description: Payment core service
  tags:
    - java
    - spring-boot
    - microservice
  annotations:
    github.com/project-slug: my-org/payment-service
    backstage.io/techdocs-ref: dir:.
    grafana/dashboard-selector: "tags @> ['payment']"
    pagerduty.com/integration-key: "<INTEGRATION_KEY>"
    snyk.io/org-name: my-org
spec:
  type: service
  lifecycle: production
  owner: team-payments
  system: payment-platform
  dependsOn:
    - resource:postgres-payment-db
    - component:notification-service
  providesApis:
    - payment-api
---
apiVersion: backstage.io/v1alpha1
kind: Resource
metadata:
  name: postgres-payment-db
  description: Payment database
  tags:
    - postgres
    - database
spec:
  type: database
  owner: dba-team
  system: payment-platform
  dependencyOf:
    - component:payment-service
---
apiVersion: backstage.io/v1alpha1
kind: API
metadata:
  name: payment-api
  description: Payment REST API
  tags:
    - rest
    - openapi
spec:
  type: openapi
  lifecycle: production
  owner: team-payments
  system: payment-platform
  definition:
    $text: https://github.com/my-org/payment-service/blob/main/openapi.yaml
```

## 3.2 Auto-Discovery Configuration

```yaml
# app-config.production.yaml
catalog:
  providers:
    githubOrg:
      myOrg:
        organization: 'my-org'
        catalogPath: '/catalog-info.yaml'
        filters:
          branch: 'main'
          repository: '.*'
        schedule:
          frequency: { minutes: 30 }
          timeout: { minutes: 3 }
```

---

<!-- chunk: IV. Software Templates Self-Service -->## IV. Software Templates Self-Service

## 4.1 Template Definition

```yaml
apiVersion: scaffolder.backstage.io/v1beta3
kind: Template
metadata:
  name: microservice-template
  title: Spring Boot Microservice
  description: Create standardized Spring Boot microservices
  tags:
    - spring-boot
    - java
    - recommended
spec:
  owner: platform-team
  type: service
  parameters:
    - title: Service Information
      required:
        - name
        - owner
      properties:
        name:
          title: Service Name
          type: string
          description: Unique microservice name
          ui:autofocus: true
        owner:
          title: Team
          type: string
          ui:field: OwnerPicker
          ui:options:
            allowedKinds:
              - Group
        description:
          title: Description
          type: string
          description: Brief description of service purpose
    - title: Technology Stack
      properties:
        javaVersion:
          title: Java Version
          type: string
          enum: ['17', '21']
          default: '21'
        database:
          title: Database
          type: string
          enum: ['PostgreSQL', 'MySQL', 'MongoDB', 'None']
          default: 'PostgreSQL'
  steps:
    - id: fetch-base
      name: Fetch Template
      action: fetch:template
      input:
        url: ./skeleton
        values:
          name: ${{ parameters.name }}
          owner: ${{ parameters.owner }}
          description: ${{ parameters.description }}
          javaVersion: ${{ parameters.javaVersion }}
          database: ${{ parameters.database }}
    - id: publish
      name: Publish to GitHub
      action: publish:github
      input:
        allowedHosts: ['github.com']
        description: ${{ parameters.description }}
        repoUrl: github.com?owner=my-org&repo=${{ parameters.name }}
        defaultBranch: main
        repoVisibility: internal
    - id: register
      name: Register to Catalog
      action: catalog:register
      input:
        repoContentsUrl: ${{ steps.publish.output.repoContentsUrl }}
        catalogInfoPath: '/catalog-info.yaml'
  output:
    links:
      - title: Repository
        url: ${{ steps.publish.output.remoteUrl }}
      - title: Directory
        icon: catalog
        entityRef: ${{ steps.register.output.entityRef }}
```

---

<!-- chunk: V. TechDocs Documentation as Code -->## V. TechDocs Documentation as Code

```yaml
# mkdocs.yaml
site_name: 'Payment Service Docs'
nav:
  - Home: index.md
  - Architecture: architecture.md
  - API Reference: api.md
  - Runbooks: runbooks/
  - Onboarding: onboarding.md

plugins:
  - techdocs-core
```

**Directory Structure**
```
docs/
├── index.md
├── architecture.md
├── api.md
├── runbooks/
│   ├── incident-response.md
│   └── failover.md
└── onboarding.md
```

---

<!-- chunk: VI. Plugin Ecosystem Integration -->## VI. Plugin Ecosystem Integration

## 6.1 Core Production Plugins

| Plugin | Purpose | Installation |
|:---|:---|:---|
| `@backstage/plugin-kubernetes` | K8s resource visualization | `yarn add` + backend configuration |
| `@backstage/plugin-argo-cd` | Argo CD application status | `yarn add` |
| `@backstage/plugin-prometheus` | Prometheus metrics | `yarn add` |
| `@backstage/plugin-grafana` | Grafana dashboard | `yarn add` |
| `@backstage/plugin-sonarqube` | Code quality dashboard | `yarn add` |
| `@backstage/plugin-jira` | Jira integration | `yarn add` |
| `@backstage/plugin-pagerduty` | On-call and alerts | `yarn add` |
| `@backstage/plugin-cost-insights` | Cost insights | `yarn add` |
| `@roadiehq/backstage-plugin-github-pull-requests` | PR dashboard | `yarn add` |
| `@roadiehq/backstage-plugin-security-insights` | Security insights | `yarn add` |
| `@roadiehq/backstage-plugin-argo-cd` | Argo CD enhancement | `yarn add` |
| `@k-phoen/backstage-plugin-opsgenie` | OpsGenie integration | `yarn add` |
| `@backstage/plugin-sentry` | Error tracking | `yarn add` |
| `@backstage/plugin-lighthouse` | Web performance | `yarn add` |
| `@backstage/plugin-airbrake` | Error monitoring | `yarn add` |
| `@backstage/plugin-badges` | Status badges | `yarn add` |

## 6.2 K8s Plugin Configuration

```yaml
# app-config.yaml
kubernetes:
  serviceLocatorMethod:
    type: 'multiTenant'
  clusterLocatorMethods:
    - type: 'config'
      clusters:
        - url: https://k8s-api.example.com
          name: production
          authProvider: 'serviceAccount'
          skipTLSVerify: false
          skipMetricsLookup: false
          serviceAccountToken: ${K8S_SA_TOKEN}
          dashboardUrl: https://k8s-dashboard.example.com
          dashboardApp: standard
```

---

<!-- chunk: VII. Authentication and Multi-Tenancy -->## VII. Authentication and Multi-Tenancy

## 7.1 GitHub OAuth + Organization Members

```typescript
// packages/backend/src/plugins/auth.ts
import { createOAuthProviderIntegration } from '@backstage/plugin-auth-backend';

export default createOAuthProviderIntegration({
  provider: {
    github: {
      production: {
        signIn: {
          resolvers: [
            {
              resolver: 'emailMatchingUserEntityProfileEmail',
            },
          ],
        },
      },
    },
  },
});
```

## 7.2 Permission Framework

```yaml
# app-config.yaml
permission:
  enabled: true
```

```typescript
// Custom permission policy
// packages/backend/src/plugins/permission.ts
import { createBackendModule } from '@backstage/backend-defaults';
import { policyExtensionPoint } from '@backstage/plugin-permission-node/alpha';

export default createBackendModule({
  pluginId: 'permission',
  moduleId: 'custom-policy',
  register(reg) {
    reg.registerInit({
      deps: { policy: policyExtensionPoint },
      async init({ policy }) {
        policy.setPolicy(async (request) => {
          if (request.permission.name === 'catalog.entity.read') {
            return { result: AuthorizeResult.ALLOW };
          }
          return { result: AuthorizeResult.DENY };
        });
      },
    });
  },
});
```

---

<!-- chunk: VIII. Production Deployment -->## VIII. Production Deployment

## 8.1 Docker Build

```dockerfile
# packages/backend/Dockerfile
FROM node:20-bookworm-slim
WORKDIR /app
COPY yarn.lock package.json packages/backend/dist/skeleton.tar.gz ./
RUN tar xzf skeleton.tar.gz && rm skeleton.tar.gz
RUN yarn install --frozen-lockfile --production --network-timeout 300000
COPY packages/backend/dist/bundle.tar.gz ./
RUN tar xzf bundle.tar.gz && rm bundle.tar.gz
CMD ["node", "packages/backend", "--config", "app-config.yaml", "--config", "app-config.production.yaml"]
```

## 8.2 Helm Deployment

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend --dry-run or diff confirmation first
> - `helm upgrade/install`: deploy/upgrade release

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, confirm target, scope of impact and authorization before executing
# Community Helm Chart (unofficial)
helm repo add backstage https://backstage.github.io/charts
helm install backstage backstage/backstage \
  --namespace backstage \
  --create-namespace \
  --set backstage.image.tag=latest \
  --set postgresql.enabled=true
```

## 8.3 Production Checklist

| Checklist Item | Recommendation |
|:---|:---|
| Database | Use PostgreSQL, backup regularly |
| Cache | Configure Redis cache |
| Authentication | Enable SSO (GitHub/Google/Okta) |
| Catalog Discovery | Configure automatic synchronization, avoid manual maintenance |
| TechDocs | Use S3/GCS storage, pre-build with CI/CD |
| Plugin Version | Lock versions, upgrade regularly |
| Monitoring | Enable Prometheus metrics export |
| Logging | Structured JSON logging |
| Permissions | Enable Permission Framework |
| Search | Configure Elasticsearch/OpenSearch |

---

<!-- chunk: Reference Links -->## Reference Links

- [Backstage Official Documentation](https://backstage.io/docs/)
- [Backstage Plugins Marketplace](https://backstage.io/plugins/)
- [Backstage Create App Guide](https://backstage.io/docs/getting-started/)
- [Software Catalog Definition](https://backstage.io/docs/features/software-catalog/descriptor-format/)
- [Software Templates](https://backstage.io/docs/features/software-templates/writing-templates/)
- [TechDocs](https://backstage.io/docs/features/techdocs/getting-started/)
- [Permissions Framework](https://backstage.io/docs/permissions/overview/)

---

<!-- chunk: Obsidian Related Documentation -->## Obsidian Related Documentation

- domain-07-platform-engineering MOC
- Domain 07: Platform Engineering (Platform Engineering)
- Domain-36 Platform Engineering — Open Source Project Index
- Platform Engineering Overview and Maturity Model
- Internal Developer Platform Design Principles
- Backstage Deployment and Configuration
- Backstage Software Catalog and TechDocs
- Backstage Scaffolder and Template System
- Kratix Platform as Code (Kratix Platform as Code)
- Crossplane Platform Composition (Crossplane Platform Composition)
- Golden Paths Design Patterns (Golden Paths Design Patterns)
- Developer Experience Metrics (Developer Experience Metrics)

## See Also

- 10-platform-team-topology
- 11-vercel-frontend-deployment-platform
- 01-platform-engineering-overview
- 02-idp-design-principles


<!-- risk-assessed -->