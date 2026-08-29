---
title: Inner Source Contribution Model
description: 'Platform SDK design, self-service PR workflow, modular platform components, contributor guide, and automated code review'
summary: 'Platform SDK design, self-service PR workflow, modular platform components, contributor guide, and automated code review'
category: platform-engineering
tags:
- inner-source
- platform-sdk
- contributing
- code-review
- developer-experience
tier: supporting
created: '2026-07-02'
last_updated: 2026-07
difficulty: advanced
reading_level: advanced
audience:
- All engineers
- Architects
- SRE
estimated_read_time: 15min
intent_queries:
- What is Inner Source Contribution Model
- How to implement Inner Source
trigger_keywords:
- Inner Source
- Inner Source
- Platform SDK
- Contributor Guide
- Code Review
prerequisites:
- kubectl-basics
- microservice-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: KUDIG Team
  role: contributor
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/developer-experience/01-inner-source-contribution-model.md
original_language: Chinese
---

> **Production Environment Security Note**
>
> This document contains operations commands that can be executed directly. Before execution, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have verified in a non-production environment. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (will modify cluster state, but usually reversible), 🟢 Low Risk/Read-only (information collection, no side effects).


# Inner Source Contribution Model

## 1. Overview

Inner Source brings the collaborative model of open source software into enterprises, allowing any team to contribute code to platform components. Through transparent contribution processes, modular architecture, and automated review, it accelerates platform capability evolution while fostering a sense of ownership among engineers.

## 2. Core Principles

```
Five Principles of Inner Source:

1. Transparency (Transparency)
   → All code, documentation, and decisions are publicly visible
   → Issue tracking and PR reviews are open to all engineers

2. Contributor First (Contributor First)
   → Lower contribution barriers, simplify PR processes
   → Provide clear contribution guidelines and templates

3. Modularity (Modularity)
   → Platform components are independently pluggable
   → Clear interface contracts and version management

4. Autonomy + Governance (Autonomy + Governance)
   → Component maintainers have technical decision authority
   → Architecture committee is responsible for cross-component coordination

5. Metrics Driven (Metrics Driven)
   → Track contribution activity and PR merge time
   → Publish community health reports regularly
```

## 3. Platform SDK Design

### 3.1 SDK Architecture Layering

```
Platform SDK Layered Architecture:

Layer 1: Core SDK (Core Layer)
  → Authentication, configuration, logging, metrics and other foundational capabilities
  → All platform components must depend on this

Layer 2: Domain SDK (Domain Layer)
  → Shared capabilities across business domains
  → Optional dependencies, introduce as needed

Layer 3: Component SDK (Component Layer)
  → Clients for specific platform components
  → Depend on Core + corresponding Domain

Layer 4: Application SDK (Application Layer)
  → Integration toolkit for business applications
  → Depend on Core + multiple Components
```

### 3.2 SDK Directory Structure

```go
// Platform SDK Directory Structure
platform-sdk/
├── core/                    // Layer 1: Core Capabilities
│   ├── auth/               // Authentication and Authorization
│   │   ├── token.go        // Token Management
│   │   ├── middleware.go   // Authentication Middleware
│   │   └── rbac.go         // RBAC Permissions
│   ├── config/             // Configuration Management
│   │   ├── loader.go       // Configuration Loader
│   │   ├── watcher.go      // Configuration Watcher
│   │   └── source/         // Configuration Sources (ConfigMap, Vault)
│   ├── logging/            // Structured Logging
│   ├── metrics/            // Metrics Collection
│   └── tracing/            // Distributed Tracing
│
├── domain/                  // Layer 2: Domain Capabilities
│   ├── messaging/          // Message Queue
│   │   ├── kafka/          // Kafka Client
│   │   ├── rabbitmq/       // RabbitMQ Client
│   │   └── nats/           // NATS Client
│   ├── database/           // Database
│   │   ├── postgres/       // PostgreSQL
│   │   ├── redis/          // Redis
│   │   └── mongodb/        // MongoDB
│   └── storage/            // Object Storage
│
├── component/               // Layer 3: Component Clients
│   ├── order-service/      // Order Service Client
│   ├── user-service/       // User Service Client
│   └── notification/       // Notification Service Client
│
└── app/                     // Layer 4: Application Integration
    ├── gin/                // Gin Framework Integration
    ├── grpc/               // gRPC Integration
    └── http/               // HTTP Client Integration
```

### 3.3 SDK Version Management

```yaml
# Go Module Version Management
# go.mod
module github.com/company/platform-sdk

go 1.22

require (
    github.com/company/platform-sdk/core v1.2.0
    github.com/company/platform-sdk/domain/messaging v1.1.0
    github.com/company/platform-sdk/component/order-service v1.0.0
)

# Version Policy:
# Core SDK: Semantic versioning, Breaking Changes require major version upgrade
# Domain SDK: Aligned with Core SDK version
# Component SDK: Follows component API changes
```

```yaml
# Version Compatibility Matrix
apiVersion: v1
kind: ConfigMap
metadata:
  name: sdk-compatibility-matrix
data:
  matrix.yaml: |
    core_versions:
      - version: "1.2.x"
        compatible_domain:
          - "messaging >=1.1.0,<1.3.0"
          - "database >=1.0.0,<1.2.0"
        compatible_component:
          - "order-service >=1.0.0,<2.0.0"
      - version: "1.1.x"
        compatible_domain:
          - "messaging >=1.0.0,<1.2.0"
          - "database >=1.0.0,<1.1.0"
```

## 4. Self-Service PR Workflow

### 4.1 PR Template

```yaml
# .github/PULL_REQUEST_TEMPLATE.md
## Description
<!-- Briefly describe the content and purpose of this change -->

## Change Type
- [ ] Bug fix
- [ ] New feature
- [ ] Refactoring
- [ ] Documentation update
- [ ] Dependency upgrade

## Impact Scope
- [ ] Core SDK
- [ ] Domain SDK (which domain: ___)
- [ ] Component SDK (which component: ___)
- [ ] Documentation
- [ ] CI/CD

## Testing
- [ ] Unit tests pass
- [ ] Integration tests pass
- [ ] E2E tests pass (if applicable)

## Checklist
- [ ] Code conforms to project style guide
- [ ] Added necessary tests
- [ ] Updated relevant documentation
- [ ] Checked backward compatibility
- [ ] Passed security scans

## Related Issue
<!-- Related Issue numbers -->
```

### 4.2 PR Automation Workflow

```yaml
# GitHub Actions PR Automation
name: PR Automation
on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  auto-label:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/labeler@v4
        with:
          repo-token: "${{ secrets.GITHUB_TOKEN }}"

  auto-assign:
    runs-on: ubuntu-latest
    steps:
      - uses: kentaro-m/auto-assign-action@v1.2.5
        with:
          configurationPath: ".github/auto-assign.yml"

  size-label:
    runs-on: ubuntu-latest
    steps:
      - uses: codelytv/pr-size-labeler@v1
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          xs_max_size: 10
          s_max_size: 100
          m_max_size: 500
          l_max_size: 1000
          fail_if_xl: false

  check-pr-template:
    runs-on: ubuntu-latest
    steps:
      - name: Check PR template filled
        uses: actions/github-script@v6
        with:
          script: |
            const body = context.payload.pull_request.body;
            if (!body.includes('## Description')) {
              core.setFailed('Please fill in the PR template');
            }
```

### 4.3 Contributor Permission Model

```yaml
# CODEOWNERS File
# Format: <pattern> <owner1> <owner2>

# Core SDK - Maintained by Platform Team
/core/ @platform-core-team

# Domain SDK - Maintained by respective domain teams
/domain/messaging/ @messaging-team @platform-core-team
/domain/database/ @database-team @platform-core-team

# Component SDK - Maintained by component owners
/component/order-service/ @order-team
/component/user-service/ @user-team

# Documentation - Maintained by docs team + domain experts
/docs/ @docs-team @platform-core-team

# CI/CD - Maintained by DevOps team
/.github/ @devops-team
/Makefile @devops-team
```

## 5. Modular Platform Components

### 5.1 Component Interface Contract

```protobuf
// Component API Contract (Protocol Buffers)
syntax = "proto3";
package platform.order.v1;

import "google/protobuf/timestamp.proto";

service OrderService {
  // Create order
  rpc CreateOrder(CreateOrderRequest) returns (CreateOrderResponse);
  // Query order
  rpc GetOrder(GetOrderRequest) returns (Order);
  // List query
  rpc ListOrders(ListOrdersRequest) returns (ListOrdersResponse);
  // Cancel order
  rpc CancelOrder(CancelOrderRequest) returns (CancelOrderResponse);
}

message Order {
  string id = 1;
  string customer_id = 2;
  OrderStatus status = 3;
  repeated OrderItem items = 4;
  int64 total_amount_cents = 5;
  string currency = 6;
  google.protobuf.Timestamp created_at = 7;
  google.protobuf.Timestamp updated_at = 8;
}
```

### 5.2 Component Registration and Discovery

```yaml
# Component Registry Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: component-registry
data:
  registry.yaml: |
    components:
      order-service:
        version: "1.2.0"
        team: order-team
        repository: github.com/company/platform-components/order-service
        api_version: "v1"
        health_endpoint: /health
        metrics_endpoint: /metrics
        dependencies:
          - user-service
          - inventory-service

      user-service:
        version: "2.0.0"
        team: user-team
        repository: github.com/company/platform-components/user-service
        api_version: "v2"
        health_endpoint: /health
        metrics_endpoint: /metrics
        dependencies: []
```

## 6. Contributor Guide

### 6.1 CONTRIBUTING.md Template

```markdown
# Contribution Guide

## Quick Start

1. Fork this repository
2. Clone to local: `git clone git@github.com:your-name/platform-sdk.git`
3. Install dependencies: `make setup`
4. Run tests: `make test`

## Development Workflow

1. Create a feature branch from `main`: `git checkout -b feature/your-feature`
2. Write code and tests
3. Ensure all tests pass: `make test`
4. Commit code: `git commit -m "feat: your feature description"`
5. Push branch: `git push origin feature/your-feature`
6. Create a Pull Request

## Code Standards

- Go code follows [Effective Go](https://go.dev/doc/effective_go)
- Use `golangci-lint` for code checking
- Unit test coverage > 80%
- All public functions must have documentation comments

## Commit Standards

Use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation update
- `refactor:` Code refactoring
- `test:` Test related
- `chore:` Build/tool changes

## Code Review

- All PRs require approval from at least 2 reviewers
- Component maintainers have final merge authority
- Review focus: security, performance, maintainability

## Issue Feedback

- Use Issue template to submit bug reports
- Use Discussion for questions and discussions
- Report security issues via security email
```

### 6.2 New Contributor Onboarding

```yaml
# New Contributor Auto-Onboarding
name: Welcome New Contributors
on:
  pull_request_target:
    types: [opened]

jobs:
  welcome:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/first-interaction@v1
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
          pr-message: |
            Thank you for your first contribution! 🎉

            Please make sure:
            1. You have read the [Contribution Guide](CONTRIBUTING.md)
            2. You filled in the PR template
            3. You passed all automated checks

            If you have any questions, please ask in the comments and maintainers will respond promptly.

      - name: Add first-time contributor label
        uses: actions/github-script@v6
        with:
          script: |
            github.rest.issues.addLabels({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              labels: ['first-time-contributor']
            })
```

## 7. Code Review Automation

### 7.1 Automated Verification Pipeline

```yaml
# Complete Code Review Pipeline
name: Code Review Pipeline
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: golangci/golangci-lint-action@v3
        with:
          version: latest
          args: --timeout=5m

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v5
        with:
          go-version: '1.22'
      - run: go test -race -coverprofile=coverage.out ./...
      - uses: codecov/codecov-action@v3
        with:
          file: coverage.out

  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          severity: 'CRITICAL,HIGH'

  dependency-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Check for outdated dependencies
        run: go list -u -m all | grep '\[' || echo "All dependencies up to date"

  api-compatibility:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Check API compatibility
        run: |
          git diff origin/main -- proto/ | \
          python3 scripts/check-api-compat.py
```

### 7.2 Intelligent Code Review Bot

```yaml
# AI-Assisted Code Review
name: AI Code Review
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  ai-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: AI Code Review
        uses: codacy/codacy-analysis-cli-action@master
        with:
          project-token: ${{ secrets.CODACY_PROJECT_TOKEN }}
          upload: true

      - name: Auto-comment on PR
        uses: actions/github-script@v6
        with:
          script: |
            const { data: files } = await github.rest.pulls.listFiles({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: context.issue.number
            });

            // Check for large files
            for (const file of files) {
              if (file.changes > 500) {
                await github.rest.issues.createComment({
                  owner: context.repo.owner,
                  repo: context.repo.repo,
                  issue_number: context.issue.number,
                  body: `⚠️ File ${file.filename} has over 500 lines changed, consider splitting the PR`
                });
              }
            }
```

## 8. Community Health Metrics

### 8.1 Key Metrics

```yaml
# Community Health Metrics Configuration
metrics:
  contribution_health:
    - name: PR_merge_time
      description: "Average PR merge time"
      target: "< 48h"
      alert: "> 72h"

    - name: first_response_time
      description: "First review response time"
      target: "< 24h"
      alert: "> 48h"

    - name: contributor_count
      description: "Monthly active contributor count"
      target: "> 20"
      alert: "< 10"

    - name: external_contributions
      description: "Non-maintainer contribution ratio"
      target: "> 30%"
      alert: "< 10%"

    - name: issue_resolution_time
      description: "Average issue resolution time"
      target: "< 7d"
      alert: "> 14d"

  code_quality:
    - name: test_coverage
      description: "Test coverage"
      target: "> 80%"
      alert: "< 70%"

    - name: bug_escape_rate
      description: "Production bug escape rate"
      target: "< 5%"
      alert: "> 10%"
```

### 8.2 Health Report Automation

```yaml
# Monthly Community Health Report
name: Monthly Health Report
on:
  schedule:
    - cron: '0 9 1 * *'  # 1st of every month at 9:00

jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Generate health report
        run: |
          python3 scripts/generate-health-report.py \
            --repo ${{ github.repository }} \
            --token ${{ secrets.GITHUB_TOKEN }} \
            --output report.md

      - name: Post to Slack
        uses: slackapi/slack-github-action@v1
        with:
          channel-id: 'C0123456789'
          slack-message: |
            📊 Monthly Community Health Report
            - Active contributors: 25 people
            - Average PR merge time: 36 hours
            - Test coverage: 85%
            Detailed report: ${{ github.server_url }}/${{ github.repository }}/actions/runs/${{ github.run_id }}
```

## 9. Governance Model

### 9.1 Roles and Responsibilities

```
Inner Source Governance Roles:

Maintainer (Maintainer):
  → Has merge authority for components
  → Responsible for API design and technical decisions
  → Guides contributors, reviews PRs
  → Participates in architecture committee discussions

Contributor (Contributor):
  → Submits PRs to fix bugs or add features
  → Participates in Issue discussions and code reviews
  → Follows contribution guidelines and code standards

Architect Committee (Architect Committee):
  → Sets overall platform architecture direction
  → Approves cross-component API changes
  → Resolves technical disputes between teams
  → Maintains architecture documentation and decision records

Platform Team (Platform Team):
  → Maintains Core SDK and infrastructure
  → Provides development tools and CI/CD support
  → Organizes community activities and training
```

### 9.2 Decision Process

```
Technical Decision Process (ADR):

1. Proposal Phase
   → Create RFC (Request for Comments)
   → Open discussion in Discussion
   → Collect feedback from all parties

2. Review Phase
   → Architecture committee reviews
   → Assesses impact scope and risks
   → Forms consensus or makes voting decision

3. Implementation Phase
   → Create implementation plan
   → Assign responsible teams
   → Set milestones and checkpoints

4. Retrospective Phase
   → Review effectiveness post-implementation
   → Document lessons learned
   → Update decision records
```

## Related

- [[domain-07-platform-engineering/developer-experience/02-developer-onboarding-automation|Developer Onboarding Automation]]
- domain-07-platform-engineering/
- [[CONTRIBUTING|Contribution Guide]]

## See Also

- Inner Source Official Guide
- GitHub Contributor Guide
- Code Review Best Practices


<!-- risk-assessed -->