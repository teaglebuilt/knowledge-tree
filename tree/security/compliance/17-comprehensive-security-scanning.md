---
title: 17 - Security Scanning and Vulnerability Detection Tools
description: '# 17 - Security Scanning and Vulnerability Detection Tools'
summary: 'trivy.dbRepository: ghcr.io/aquasecurity/trivy-db'
category: security
tags:
- k8s
- security
- rbac
- authentication
- authorization
- prometheus
- helm
- containerd
- docker
- harbor
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
- What is Security Scanning and Vulnerability Detection Tools
- How to use Security Scanning and Vulnerability Detection Tools
- Kubernetes 7 security best practices
trigger_keywords:
- Security Scanning and Vulnerability Detection Tools
- security
prerequisites:
- kubectl-basics
- rbac-basics
- helm-basics
- prometheus-basics
- ebpf-basics
- policy-basics
- logging-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: KUDIG Team
  role: contributor
cross_refs:
- type: domain
  path: ../domain-01-cluster-fundamentals/
  label: 'Related Knowledge Domain: domain-01-cluster-fundamentals'
- type: domain
  path: ../domain-06-observability/
  label: 'Related Knowledge Domain: domain-06-observability'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/tls-pki.md
  label: 'Quick Reference: tls-pki'
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-05-security-compliance/06-compliance/17-comprehensive-security-scanning.md
original_language: Chinese
---

> **Production Environment Security Notice**
>
> This document contains directly executable operations and maintenance commands. Before execution, please verify: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have tested in a non-production environment. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state but usually reversible), 🟢 Low Risk/Read-only (information gathering with no side effects).




# 17 - Security Scanning and Vulnerability Detection Tools

> **Applicable Versions**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **Difficulty**: Intermediate to Advanced | **Reference**: [[entities/trivy.md|Trivy]]](https://aquasecurity.github.io/trivy/) | [Grype](https://github.com/anchore/grype) | [[entities/falco.md|Falco]]](https://falco.org/)

<!-- chunk: 一、安全扫描体系架构 -->
## 1. Security Scanning Architecture Overview

### 1.1 DevSecOps Security Scanning Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                        DevSecOps Security Scanning Architecture                      │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌────────────────────────────────────────────────────────────────────────────────┐ │
│  │                            Development Phase                                    │ │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐       │ │
│  │  │    SAST      │  │    SCA       │  │   Secrets    │  │   License    │       │ │
│  │  │  (Semgrep)   │  │  (Snyk/      │  │   Scanning   │  │   Compliance │       │ │
│  │  │              │  │   Dependabot)│  │  (gitleaks)  │  │  (FOSSA)     │       │ │
│  │  │ Code Vulns   │  │ Dependencies │  │ Hardcoded    │  │ OSS License  │       │ │
│  │  │ SQL Injection│  │ CVE Database │  │ Credentials  │  │ Violations   │       │ │
│  │  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘       │ │
│  └────────────────────────────────────────────────────────────────────────────────┘ │
│                                         │                                            │
│  ┌──────────────────────────────────────▼───────────────────────────────────────────┐│
│  │                              Build Phase                                         ││
│  │  ┌──────────────────────────────────────────────────────────────────────────┐   ││
│  │  │                        Container Image Scanning                           │   ││
│  │  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐         │   ││
│  │  │  │   Trivy    │  │   Grype    │  │   Clair    │  │   Snyk     │         │   ││
│  │  │  │            │  │            │  │            │  │            │         │   ││
│  │  │  │ • OS Pkgs  │  │ • SBOM     │  │ • Harbor   │  │ • SaaS     │         │   ││
│  │  │  │ • Lang Pkgs│  │ • CVE DB   │  │ • Quay.io  │  │ • IDE      │         │   ││
│  │  │  │ • Secrets  │  │ • Offline  │  │ • CoreOS   │  │ • CI/CD    │         │   ││
│  │  │  │ • Misconfig│  │ • SARIF    │  │ • Postgres │  │ • Monitor  │         │   ││
│  │  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘         │   ││
│  │  └──────────────────────────────────────────────────────────────────────────┘   ││
│  │  ┌──────────────────────────────────────────────────────────────────────────┐   ││
│  │  │                            SBOM Generation                               │   ││
│  │  │  ┌────────────┐  ┌────────────┐  ┌────────────┐                         │   ││
│  │  │  │    Syft    │  │  Cyclonedx │  │   SPDX     │                         │   ││
│  │  │  │            │  │            │  │            │                         │   ││
│  │  │  │ • Multi-   │  │ • Standard │  │ • Standard │                         │   ││
│  │  │  │   format   │  │   Format   │  │   Format   │                         │   ││
│  │  │  └────────────┘  └────────────┘  └────────────┘                         │   ││
│  │  └──────────────────────────────────────────────────────────────────────────┘   ││
│  └─────────────────────────────────────────────────────────────────────────────────┘│
│                                         │                                            │
│  ┌──────────────────────────────────────▼───────────────────────────────────────────┐│
│  │                              Deploy Phase                                        ││
│  │  ┌──────────────────────────────────────────────────────────────────────────┐   ││
│  │  │                       Admission Control                                   │   ││
│  │  │  ┌────────────┐  ┌────────────┐  ┌────────────┐  ┌────────────┐         │   ││
│  │  │  │   Kyverno  │  │   OPA/     │  │  Trivy     │  │  Sigstore/ │         │   ││
│  │  │  │            │  │ Gatekeeper │  │  Operator  │  │  Cosign    │         │   ││
│  │  │  │ • Policies │  │ • Rego     │  │ • Runtime  │  │ • Image    │         │   ││
│  │  │  │ • Mutation │  │ • Constr.  │  │   Scan     │  │   Sign     │         │   ││
│  │  │  └────────────┘  └────────────┘  └────────────┘  └────────────┘         │   ││
│  │  └──────────────────────────────────────────────────────────────────────────┘   ││
│  └─────────────────────────────────────────────────────────────────────────────────┘│
│                                         │                                            │
│  ┌──────────────────────────────────────▼───────────────────────────────────────────┐│
│  │                              Runtime Phase                                       ││
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐        ││
│  │  │    Falco     │  │   Tetragon  │  │   KubeArmor │  │   Sysdig     │        ││
│  │  │              │  │              │  │              │  │              │        ││
│  │  │ • Syscall    │  │ • eBPF      │  │ • LSM/BPF   │  │ • Commercial │        ││
│  │  │ • K8s Audit  │  │ • Network   │  │ • Policies  │  │ • Platform   │        ││
│  │  │ • Custom     │  │ • Process   │  │ • Block     │  │ • Compliance │        ││
│  │  │   Rules      │  │   Tracing   │  │ • Alert     │  │ • Forensics  │        ││
│  │  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘        ││
│  └─────────────────────────────────────────────────────────────────────────────────┘│
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Comprehensive Security Scanning Tools Comparison

| Tool | Scan Target | Vulnerability Source | SBOM | CI/CD | Runtime | K8s Native | Open Source | Use Case |
|-----|---------|-------|------|-------|-------|--------|------|---------|
| **Trivy** | Image/FS/Git/K8s | Multi-source Aggregation | ✓ | ★★★★★ | ✓ | ★★★★★ | ✓ | Universal Choice |
| **Grype** | Image/SBOM | Anchore | ✓ | ★★★★☆ | ✗ | ★★★☆☆ | ✓ | SBOM Scanning |
| **Clair** | Image | CVE | ✗ | ★★★☆☆ | ✗ | ★★★☆☆ | ✓ | Harbor Integration |
| **Snyk** | Full Stack | Commercial DB | ✓ | ★★★★★ | ✓ | ★★★★☆ | Partial | Developer Experience |
| **Anchore** | Image/SBOM | Multi-source | ★★★★★ | ★★★★☆ | ✗ | ★★★★☆ | Enterprise | Enterprise Compliance |
| **Falco** | Runtime | Rules | ✗ | ✗ | ★★★★★ | ★★★★★ | ✓ | Runtime Detection |
| **[[Kubescape|Kubescape]]** | K8s Config | NSA/MITRE | ✗ | ★★★★☆ | ✓ | ★★★★★ | ✓ | K8s Security |
| **Checkov** | IaC | Policies | ✗ | ★★★★★ | ✗ | ★★★☆☆ | ✓ | IaC Scanning |

### 1.3 Vulnerability Severity and SLA

| Severity | CVSS Score | Fix SLA | CI/CD Block | Example |
|-------|---------|---------|----------|------|
| **Critical** | 9.0-10.0 | 24 hours | Force Block | Log4Shell, ShellShock |
| **High** | 7.0-8.9 | 7 days | Recommended Block | Remote Code Execution |
| **Medium** | 4.0-6.9 | 30 days | Warning | Information Disclosure |
| **Low** | 0.1-3.9 | 90 days | Log | Low Risk Configuration |
| **Unknown** | N/A | Assessment | Assessment | Newly Discovered Vulnerabilities |

---

<!-- chunk: 二、Trivy全能扫描 -->
## 2. Trivy Comprehensive Scanning

### 2.1 Trivy Operator Deployment

```yaml
# Trivy Operator Installation
apiVersion: v1
kind: Namespace
metadata:
  name: trivy-system
---
# helm repo add aqua https://aquasecurity.github.io/helm-charts/
# helm install trivy-operator aqua/trivy-operator -n trivy-system
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: trivy-operator
  namespace: trivy-system
spec:
  replicas: 1
  selector:
    matchLabels:
      app: trivy-operator
  template:
    metadata:
      labels:
        app: trivy-operator
    spec:
      serviceAccountName: trivy-operator
      containers:
      - name: trivy-operator
        image: ghcr.io/aquasecurity/trivy-operator:0.18.4
        
        args:
        - --health-probe-bind-address=:8081
        - --metrics-bind-address=:8080
        - --leader-elect
        
        env:
        # Scan Configuration
        - name: OPERATOR_NAMESPACE
          valueFrom:
            fieldRef:
              fieldPath: metadata.namespace
        - name: OPERATOR_TARGET_NAMESPACES
          value: ""  # Empty indicates all namespaces
        
        # Trivy Configuration
        - name: OPERATOR_VULNERABILITY_SCANNER_ENABLED
          value: "true"
        - name: OPERATOR_CONFIG_AUDIT_SCANNER_ENABLED
          value: "true"
        - name: OPERATOR_RBAC_ASSESSMENT_SCANNER_ENABLED
          value: "true"
        - name: OPERATOR_INFRA_ASSESSMENT_SCANNER_ENABLED
          value: "true"
        - name: OPERATOR_CLUSTER_COMPLIANCE_ENABLED
          value: "true"
        
        # Scan Parameters
        - name: OPERATOR_SCANNER_TRIVY_SEVERITY
          value: "CRITICAL,HIGH,MEDIUM"
        - name: OPERATOR_SCANNER_TRIVY_IGNORE_UNFIXED
          value: "true"
        - name: OPERATOR_SCANNER_TRIVY_TIMEOUT
          value: "5m"
        
        # Concurrency Control
        - name: OPERATOR_CONCURRENT_SCAN_JOBS_LIMIT
          value: "10"
        - name: OPERATOR_SCAN_JOB_RETRY_AFTER
          value: "30s"
        
        ports:
        - containerPort: 8080
          name: metrics
        - containerPort: 8081
          name: health
        
        resources:
          requests:
            cpu: 200m
            memory: 256Mi
          limits:
            cpu: 500m
            memory: 512Mi
        
        livenessProbe:
          httpGet:
            path: /healthz
            port: 8081
          initialDelaySeconds: 15
        
        readinessProbe:
          httpGet:
            path: /readyz
            port: 8081
          initialDelaySeconds: 5
        
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          runAsNonRoot: true
          capabilities:
            drop: ["ALL"]
---
# Trivy Configuration ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: trivy-operator-trivy-config
  namespace: trivy-system
data:
  # Scanner Mode
  trivy.mode: Standalone
  
  # Vulnerability Database
  trivy.dbRepository: ghcr.io/aquasecurity/trivy-db
  trivy.dbRepositoryInsecure: "false"
  
  # Java Vulnerability Database
  trivy.javaDbRepository: ghcr.io/aquasecurity/trivy-java-db
  
  # Severity Filtering
  trivy.severity: CRITICAL,HIGH,MEDIUM
  
  # Ignore Unfixed Vulnerabilities
  trivy.ignoreUnfixed: "true"
  
  # Timeout Setting
  trivy.timeout: "5m0s"
  
  # Resource Limits
  trivy.resources.requests.cpu: "100m"
  trivy.resources.requests.memory: "100M"
  trivy.resources.limits.cpu: "500m"
  trivy.resources.limits.memory: "500M"
  
  # Offline Mode (Optional)
  # trivy.offlineScan: "true"
  
  # Ignore Rules
  trivy.ignorePolicy: |
    package trivy
    import data.lib.trivy
    
    default ignore = false
    
    # Ignore Specific CVE
    ignore {
      input.VulnerabilityID == "CVE-2021-44228"
      input.PkgName == "log4j-core"
      input.InstalledVersion == "2.17.0"
    }
```

### 2.2 CI/CD Pipeline Integration

```yaml
# GitLab CI Integration
stages:
  - build
  - scan
  - deploy

variables:
  TRIVY_VERSION: "0.48.3"
  TRIVY_SEVERITY: "CRITICAL,HIGH"
  TRIVY_EXIT_CODE: "1"  # Fail when vulnerabilities found

# Image Build
build:
  stage: build
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker push $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA

# Container Image Scanning
container-scan:
  stage: scan
  image: aquasec/trivy:$TRIVY_VERSION
  script:
    # Update Vulnerability Database
    - trivy image --download-db-only
    
    # Image Scan
    - |
      trivy image \
        --exit-code $TRIVY_EXIT_CODE \
        --severity $TRIVY_SEVERITY \
        --ignore-unfixed \
        --format json \
        --output trivy-image-report.json \
        $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    
    # Generate HTML Report
    - |
      trivy image \
        --severity $TRIVY_SEVERITY \
        --format template \
        --template "@/contrib/html.tpl" \
        --output trivy-image-report.html \
        $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
    
    # Generate SARIF Report (GitHub/GitLab Integration)
    - |
      trivy image \
        --format sarif \
        --output trivy-image-report.sarif \
        $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  
  artifacts:
    paths:
      - trivy-image-report.json
      - trivy-image-report.html
      - trivy-image-report.sarif
    reports:
      container_scanning: trivy-image-report.json
  
  allow_failure: false

# File System Scanning
fs-scan:
  stage: scan
  image: aquasec/trivy:$TRIVY_VERSION
  script:
    - |
      trivy fs \
        --exit-code 0 \
        --severity $TRIVY_SEVERITY \
        --format json \
        --output trivy-fs-report.json \
        .
  artifacts:
    paths:
      - trivy-fs-report.json

# IaC Configuration Scanning
config-scan:
  stage: scan
  image: aquasec/trivy:$TRIVY_VERSION
  script:
    - |
      trivy config \
        --exit-code 0 \
        --severity $TRIVY_SEVERITY \
        --format json \
        --output trivy-config-report.json \
        ./k8s/
  artifacts:
    paths:
      - trivy-config-report.json

# Secret Scanning
secret-scan:
  stage: scan
  image: aquasec/trivy:$TRIVY_VERSION
  script:
    - |
      trivy fs \
        --scanners secret \
        --exit-code 1 \
        --format json \
        --output trivy-secret-report.json \
        .
  artifacts:
    paths:
      - trivy-secret-report.json
---
# GitHub Actions Integration
name: Security Scan

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  trivy-scan:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Build image
      run: docker build -t myapp:${{ github.sha }} .
    
    - name: Run Trivy vulnerability scanner
      uses: aquasecurity/trivy-action@master
      with:
        image-ref: myapp:${{ github.sha }}
        format: 'sarif'
        output: 'trivy-results.sarif'
        severity: 'CRITICAL,HIGH'
        ignore-unfixed: true
    
    - name: Upload Trivy scan results to GitHub Security tab
      uses: github/codeql-action/upload-sarif@v2
      with:
        sarif_file: 'trivy-results.sarif'
    
    - name: Run Trivy in IaC mode
      uses: aquasecurity/trivy-action@master
      with:
        scan-type: 'config'
        scan-ref: './k8s'
        format: 'table'
        exit-code: '0'
```

### 2.3 Trivy Advanced Scanning Configuration

``` bash
# 🟢 Low Risk: Read-only/information gathering with usually no side effects
#!/bin/bash
# trivy-advanced-scan.sh - Trivy Advanced Scanning Script

# Environment Variables
export TRIVY_DB_REPOSITORY="ghcr.io/aquasecurity/trivy-db"
export TRIVY_JAVA_DB_REPOSITORY="ghcr.io/aquasecurity/trivy-java-db"
export TRIVY_CACHE_DIR="$HOME/.cache/trivy"

# 1. Comprehensive Image Scanning
trivy_image_scan() {
    local image=$1
    local output_dir=${2:-./trivy-reports}
    
    mkdir -p $output_dir
    
    # Vulnerability Scan
    trivy image \
        --severity CRITICAL,HIGH,MEDIUM,LOW \
        --ignore-unfixed \
        --scanners vuln \
        --format json \
        --output $output_dir/vulnerabilities.json \
        $image
    
    # Secret Scan
    trivy image \
        --scanners secret \
        --format json \
        --output $output_dir/secrets.json \
        $image
    
    # Configuration Scan
    trivy image \
        --scanners misconfig \
        --format json \
        --output $output_dir/misconfigs.json \
        $image
    
    # Generate SBOM
    trivy image \
        --format cyclonedx \
        --output $output_dir/sbom.json \
        $image
    
    # Comprehensive Report
    trivy image \
        --severity CRITICAL,HIGH \
        --ignore-unfixed \
        --format template \
        --template "@contrib/html.tpl" \
        --output $output_dir/report.html \
        $image
    
    echo "Scan completed! Reports located at: $output_dir"
}

# 2. Kubernetes Cluster Scanning
trivy_k8s_scan() {
    local context=${1:-$(kubectl config current-context)}
    local output_dir=${2:-./trivy-k8s-reports}
    
    mkdir -p $output_dir
    
    # Full Cluster Scan
    trivy k8s \
        --context $context \
        --report all \
        --severity CRITICAL,HIGH \
        --format json \
        --output $output_dir/cluster-report.json
    
    # Specific Namespace Scanning
    trivy k8s \
        --context $context \
        --include-namespaces production,staging \
        --report vulnerabilities \
        --format table
    
    # Compliance Check
    trivy k8s \
        --context $context \
        --compliance k8s-nsa \
        --report summary \
        --output $output_dir/compliance-nsa.txt
    
    trivy k8s \
        --context $context \
        --compliance k8s-cis \
        --report summary \
        --output $output_dir/compliance-cis.txt
}

# 3. Periodic Scanning of All Deployed Images
scan_deployed_images() {
    local output_file=${1:-deployed-images-scan.json}
    
    # Get All Unique Images
    images=$(kubectl get pods --all-namespaces -o jsonpath='{.items[*].spec.containers[*].image}' | \
        tr -s ':space:' '\n' | sort | uniq)
    
    echo "Found $(echo "$images" | wc -l) unique images"
    
    # Scan Each Image
    results=()
    for image in $images; do
        echo "Scanning: $image"
        result=$(trivy image \
            --severity CRITICAL,HIGH \
            --ignore-unfixed \
            --format json \
            --quiet \
            $image 2>/dev/null)
        results+=("$result")
    done
    
    # Merge Results
    echo "${results[@]}" | jq -s '.' > $output_file
    
    # Statistics
    critical_count=$(cat $output_file | jq '[.[].Results[].Vulnerabilities[]? | select(.Severity=="CRITICAL")] | length')
    high_count=$(cat $output_file | jq '[.[].Results[].Vulnerabilities[]? | select(.Severity=="HIGH")] | length')
    
    echo "Scan completed! Critical: $critical_count, High: $high_count"
}

# 4. SBOM Generation and Management
generate_sbom() {
    local image=$1
    local format=${2:-cyclonedx}
    local output_file=${3:-sbom.json}
    
    trivy image \
        --format $format \
        --output $output_file \
        $image
    
    echo "SBOM generated: $output_file (format: $format)"
}

# 5. Ignore Rule Configuration
create_ignore_policy() {
    cat > .trivyignore.rego << 'EOF'
package trivy

import data.lib.trivy

default ignore = false

# Ignore Specific CVE (Mitigation Measures in Place)
ignore {
    input.VulnerabilityID == "CVE-2023-44487"  # HTTP/2 Rapid Reset
    contains(input.PkgName, "golang")
}

# Ignore Development Dependency Vulnerabilities
ignore {
    input.Class == "lang-pkgs"
    input.Type == "npm"
    contains(input.PkgPath, "devDependencies")
}

# Ignore Low Risk Vulnerabilities in Specific Packages
ignore {
    input.Severity == "LOW"
    input.PkgName == "openssl"
}

# Ignore Accepted Risk Vulnerabilities
ignore {
    input.VulnerabilityID == data.accepted_risks[_]
}

accepted_risks = [
    "CVE-2021-3711",
    "CVE-2021-3712"
]
EOF
    
    echo "Ignore policy created: .trivyignore.rego"
}

# Usage Examples
# trivy_image_scan "nginx:latest" "./nginx-reports"
# trivy_k8s_scan "my-cluster" "./k8s-reports"
# scan_deployed_images "all-images-report.json"
```
### 2.4 VulnerabilityReport CRD

```yaml
# View Scan Results
apiVersion: aquasecurity.github.io/v1alpha1
kind: VulnerabilityReport
metadata:
  name: replicaset-nginx-7b8d6d5d7-nginx
  namespace: default
  labels:
    trivy-operator.resource.kind: ReplicaSet
    trivy-operator.resource.name: nginx-7b8d6d5d7
    trivy-operator.resource.namespace: default
    trivy-operator.container.name: nginx
spec:
  artifact:
    repository: library/nginx
    tag: latest
    digest: sha256:abc123...
  registry:
    server: index.docker.io
  scanner:
    name: Trivy
    vendor: Aqua Security
    version: 0.48.3
  summary:
    criticalCount: 2
    highCount: 15
    mediumCount: 45
    lowCount: 23
    unknownCount: 0
  vulnerabilities:
  - vulnerabilityID: CVE-2023-44487
    resource: nghttp2
    installedVersion: 1.43.0
    fixedVersion: 1.57.0
    severity: CRITICAL
    title: HTTP/2 Rapid Reset Attack
    description: |
      The HTTP/2 protocol allows denial of service...
    primaryLink: https://nvd.nist.gov/vuln/detail/CVE-2023-44487
    score: 7.5
    target: nginx:latest (debian 12.2)
    class: os-pkgs
    packageType: debian
---
# ConfigAuditReport - Configuration Audit Results
apiVersion: aquasecurity.github.io/v1alpha1
kind: ConfigAuditReport
metadata:
  name: replicaset-nginx-7b8d6d5d7
  namespace: default
spec:
  scanner:
    name: Trivy
    vendor: Aqua Security
    version: 0.48.3
  summary:
    criticalCount: 1
    highCount: 3
    mediumCount: 5
    lowCount: 2
  checks:
  - checkID: KSV001
    title: Process can elevate its own privileges
    description: |
      A program inside the container can elevate its own privileges
      and run as root.
    severity: MEDIUM
    category: Kubernetes Security Check
    success: false
    messages:
    - Container 'nginx' of ReplicaSet 'nginx-7b8d6d5d7' should set
      'securityContext.allowPrivilegeEscalation' to false
```

---

<!-- chunk: 三、Grype与SBOM -->
## 3. Grype and SBOM

### 3.1 Syft SBOM Generation

``` bash
# 🟢 Low Risk: Read-only/information gathering with usually no side effects
#!/bin/bash
# sbom-workflow.sh - SBOM Generation and Management Workflow

# 1. Install Syft
# curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin

# 2. Generate SBOM (Multiple Formats)
generate_sbom_all_formats() {
    local image=$1
    local output_dir=${2:-./sbom}
    
    mkdir -p $output_dir
    
    # CycloneDX Format (Recommended)
    syft $image -o cyclonedx-json=$output_dir/sbom-cyclonedx.json
    
    # SPDX Format
    syft $image -o spdx-json=$output_dir/sbom-spdx.json
    
    # Syft Native Format
    syft $image -o json=$output_dir/sbom-syft.json
    
    # Table Format (Human Readable)
    syft $image -o table=$output_dir/sbom-table.txt
    
    echo "SBOM generated in multiple formats: $output_dir"
}

# 3. Generate SBOM from Dockerfile
syft_from_dockerfile() {
    local dockerfile_path=${1:-.}
    
    # Build and Scan
    docker build -t temp-scan:latest $dockerfile_path
    syft temp-scan:latest -o cyclonedx-json
    docker rmi temp-scan:latest
}

# 4. Scan Directory
syft_scan_directory() {
    local dir=$1
    
    syft dir:$dir -o cyclonedx-json
}

# Usage Examples
# generate_sbom_all_formats "nginx:latest" "./nginx-sbom"
```
### 3.2 Grype Vulnerability Scanning

```yaml
# GitLab CI - Grype Integration
grype-scan:
  stage: scan
  image: anchore/grype:latest
  script:
    # Update Vulnerability Database
    - grype db update
    
    # Scan from SBOM
    - |
      grype sbom:./sbom-cyclonedx.json \
        --output json \
        --file grype-report.json \
        --fail-on critical
    
    # Scan Image Directly
    - |
      grype $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA \
        --output table \
        --only-fixed \
        --fail-on high
  
  artifacts:
    paths:
      - grype-report.json
---
# Grype Configuration File (.grype.yaml)
# Place in project root directory
output: "json"
file: "grype-report.json"
distro: ""
add-cpes-if-none: true
by-cve: false
only-fixed: true
fail-on: "critical"

ignore:
  # Ignore Specific CVE
  - vulnerability: CVE-2021-44228
    fix-state: not-fixed
  
  # Ignore Specific Packages
  - package:
      name: openssl
      type: deb
    vulnerability: CVE-2023-*

check-for-app-update: true

db:
  auto-update: true
  cache-dir: /tmp/grype-db
```

### 3.3 Offline Environment Scanning

``` bash
# 🟢 Low Risk: Read-only/information gathering with usually no side effects
#!/bin/bash
# offline-scanning.sh - Offline Environment Scanning Configuration

# 1. Pre-download Trivy Database
download_trivy_db() {
    local db_dir="/opt/trivy-db"
    mkdir -p $db_dir
    
    # Download Vulnerability Database
    oras pull ghcr.io/aquasecurity/trivy-db:2 \
        --output $db_dir
    
    # Download Java Database
    oras pull ghcr.io/aquasecurity/trivy-java-db:1 \
        --output $db_dir/java-db
    
    echo "Trivy DB downloaded to: $db_dir"
}

# 2. Offline Scanning
trivy_offline_scan() {
    local image=$1
    local db_dir="/opt/trivy-db"
    
    trivy image \
        --offline-scan \
        --cache-dir $db_dir \
        --severity CRITICAL,HIGH \
        $image
}

# 3. Pre-download Grype Database
download_grype_db() {
    local db_dir="/opt/grype-db"
    mkdir -p $db_dir
    
    GRYPE_DB_CACHE_DIR=$db_dir grype db update
    
    echo "Grype DB downloaded to: $db_dir"
}

# 4. Grype Offline Scanning
grype_offline_scan() {
    local image=$1
    local db_dir="/opt/grype-db"
    
    GRYPE_DB_CACHE_DIR=$db_dir grype $image --offline
}

# 5. Create Offline Scanner Image
create_offline_scanner_image() {
    cat > Dockerfile.scanner << 'EOF'
FROM aquasec/trivy:latest

# Pre-download Database
RUN trivy image --download-db-only

# Set Offline Mode
ENV TRIVY_OFFLINE_SCAN=true

ENTRYPOINT ["trivy"]
EOF
    
    docker build -f Dockerfile.scanner -t trivy-offline:latest .
    echo "Offline scanner image built: trivy-offline:latest"
}
```
---

<!-- chunk: 四、Falco运行时安全 -->
## 4. Falco Runtime Security

### 4.1 Falco Deployment Configuration

```yaml
# Falco DaemonSet Deployment
apiVersion: v1
kind: Namespace
metadata:
  name: falco
---
# helm repo add falcosecurity https://falcosecurity.github.io/charts
# helm install falco falcosecurity/falco -n falco -f falco-values.yaml
---
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: falco
  namespace: falco
spec:
  selector:
    matchLabels:
      app: falco
  template:
    metadata:
      labels:
        app: falco
    spec:
      serviceAccountName: falco
      
      # Privileged Mode (Required for eBPF Probes)
      hostPID: true
      hostNetwork: true
      
      containers:
      - name: falco
        image: falcosecurity/falco-no-driver:0.37.0
        
        args:
        - /usr/bin/falco
        - --cri=/run/containerd/containerd.sock
        - --cri=/run/crio/crio.sock
        - -K=/var/run/secrets/kubernetes.io/serviceaccount/token
        - -k=https://kubernetes.default
        - --k8s-node=$(FALCO_K8S_NODE_NAME)
        - -pk
        
        env:
        - name: FALCO_K8S_NODE_NAME
          valueFrom:
            fieldRef:
              fieldPath: spec.nodeName
        - name: FALCO_BPF_PROBE
          value: ""
        
        securityContext:
          privileged: true
        
        resources:
          requests:
            cpu: 100m
            memory: 512Mi
          limits:
            cpu: 1000m
            memory: 1024Mi
        
        volumeMounts:
        # Kernel Module/eBPF
        - name: dev
          mountPath: /host/dev
          readOnly: true
        - name: proc
          mountPath: /host/proc
          readOnly: true
        - name: boot
          mountPath: /host/boot
          readOnly: true
        - name: lib-modules
          mountPath: /host/lib/modules
          readOnly: true
        - name: usr-src
          mountPath: /host/usr
          readOnly: true
        
        # Container Runtime
        - name: containerd-socket
          mountPath: /run/containerd/containerd.sock
          readOnly: true
        - name: crio-socket
          mountPath: /run/crio/crio.sock
          readOnly: true
        
        # Configuration
        - name: falco-config
          mountPath: /etc/falco
        - name: falco-rules
          mountPath: /etc/falco/rules.d
      
      volumes:
      - name: dev
        hostPath:
          path: /dev
      - name: proc
        hostPath:
          path: /proc
      - name: boot
        hostPath:
          path: /boot
      - name: lib-modules
        hostPath:
          path: /lib/modules
      - name: usr-src
        hostPath:
          path: /usr
      - name: containerd-socket
        hostPath:
          path: /run/containerd/containerd.sock
      - name: crio-socket
        hostPath:
          path: /run/crio/crio.sock
      - name: falco-config
        configMap:
          name: falco-config
      - name: falco-rules
        configMap:
          name: falco-rules
      
      tolerations:
      - effect: NoSchedule
        operator: Exists
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: falco-config
  namespace: falco
data:
  falco.yaml: |
    # Rules File
    rules_file:
      - /etc/falco/falco_rules.yaml
      - /etc/falco/falco_rules.local.yaml
      - /etc/falco/rules.d
    
    # Output Configuration
    json_output: true
    json_include_output_property: true
    json_include_tags_property: true
    
    # Log Configuration
    log_stderr: true
    log_syslog: true
    log_level: info
    
    # Output Channels
    stdout_output:
      enabled: true
    
    syslog_output:
      enabled: true
    
    file_output:
      enabled: true
      keep_alive: false
      filename: /var/log/falco/events.log
    
    http_output:
      enabled: true
      url: http://falcosidekick.falco:2801/
      user_agent: "falco/0.37.0"
    
    grpc:
      enabled: true
      bind_address: "unix:///run/falco/falco.sock"
      threadiness: 0
    
    grpc_output:
      enabled: true
    
    # Kubernetes Audit Log
    webserver:
      enabled: true
      listen_port: 8765
      k8s_healthz_endpoint: /healthz
      ssl_enabled: false
    
    # Performance Optimization
    syscall_event_drops:
      threshold: 0.1
      actions:
        - log
        - alert
    
    buffered_outputs: true
    outputs_queue:
      capacity: 0
```

### 4.2 Falco Custom Rules

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: falco-rules
  namespace: falco
data:
  custom_rules.yaml: |
    # ========================
    # Container Security Rules
    # ========================
    
    # Detect Shell Spawned in Container
    - rule: Shell Spawned in Container
      desc: Detect shell spawned in a container
      condition: >
        spawned_process and 
        container and 
        shell_procs and
        not proc.pname in (allowed_shell_parents)
      output: >
        Shell spawned in container 
        (user=%user.name user_loginuid=%user.loginuid command=%proc.cmdline 
        container_id=%container.id container_name=%container.name 
        image=%container.image.repository k8s.ns=%k8s.ns.name 
        k8s.pod=%k8s.pod.name)
      priority: WARNING
      tags: [container, shell, mitre_execution]
    
    # Detect Sensitive File Access
    - rule: Read Sensitive File in Container
      desc: Detect reading of sensitive files in container
      condition: >
        open_read and 
        container and 
        sensitive_files and
        not proc.name in (allowed_sensitive_readers)
      output: >
        Sensitive file read in container
        (user=%user.name command=%proc.cmdline file=%fd.name 
        container_id=%container.id image=%container.image.repository)
      priority: WARNING
      tags: [container, filesystem, mitre_credential_access]
    
    # Detect Privileged Container
    - rule: Privileged Container Started
      desc: Detect when a privileged container is started
      condition: >
        container_started and 
        container.privileged=true
      output: >
        Privileged container started
        (user=%user.name command=%proc.cmdline 
        container_id=%container.id container_name=%container.name 
        image=%container.image.repository k8s.ns=%k8s.ns.name)
      priority: CRITICAL
      tags: [container, privileged, mitre_privilege_escalation]
    
    # ========================
    # Kubernetes Security Rules
    # ========================
    
    # Detect Anonymous Access to API Server
    - rule: Anonymous Request to K8s API
      desc: Detect anonymous requests to Kubernetes API server
      condition: >
        jevt.value[/userAgent] contains "kubectl" and
        jevt.value[/user/username] = "system:anonymous"
      output: >
        Anonymous request to K8s API
        (user=%jevt.value[/user/username] verb=%jevt.value[/verb] 
        uri=%jevt.value[/requestURI])
      priority: WARNING
      source: k8s_audit
      tags: [k8s, anonymous, mitre_initial_access]
    
    # Detect Privileged Pod Creation
    - rule: Create Privileged Pod
      desc: Detect creation of privileged pods
      condition: >
        kevt and 
        kcreate and 
        pod and
        jevt.value[/requestObject/spec/containers/0/securityContext/privileged] = "true"
      output: >
        Privileged pod creation attempt
        (user=%ka.user.name pod=%ka.target.name ns=%ka.target.namespace)
      priority: CRITICAL
      source: k8s_audit
      tags: [k8s, privileged, mitre_privilege_escalation]
    
    # Detect Pod Exec
    - rule: Attach or Exec to Pod
      desc: Detect any attempt to attach or exec into a pod
      condition: >
        kevt and 
        pod_subresource and 
        kcreate and 
        ka.target.subresource in (attach, exec)
      output: >
        Pod exec/attach detected
        (user=%ka.user.name pod=%ka.target.name ns=%ka.target.namespace 
        subresource=%ka.target.subresource)
      priority: NOTICE
      source: k8s_audit
      tags: [k8s, exec, mitre_execution]
    
    # Detect Secret Access
    - rule: K8s Secret Access
      desc: Detect any access to Kubernetes secrets
      condition: >
        kevt and 
        secret and 
        kget
      output: >
        K8s secret accessed
        (user=%ka.user.name secret=%ka.target.name ns=%ka.target.namespace)
      priority: INFO
      source: k8s_audit
      tags: [k8s, secret, mitre_credential_access]
    
    # ========================
    # Network Security Rules
    # ========================
    
    # Detect Outbound Connection to Suspicious IP
    - rule: Outbound Connection to Suspicious IP
      desc: Detect outbound connection to suspicious IP ranges
      condition: >
        outbound and 
        container and
        fd.sip.name in (suspicious_ips)
      output: >
        Outbound connection to suspicious IP
        (user=%user.name command=%proc.cmdline connection=%fd.name 
        container_id=%container.id)
      priority: WARNING
      tags: [network, container, mitre_exfiltration]
    
    # Detect Cryptocurrency Mining Connection
    - rule: Cryptocurrency Mining Connection
      desc: Detect connection to known mining pools
      condition: >
        outbound and 
        container and
        (fd.sport in (mining_ports) or fd.sip.name in (mining_pools))
      output: >
        Cryptocurrency mining connection detected
        (user=%user.name command=%proc.cmdline connection=%fd.name 
        container_id=%container.id image=%container.image.repository)
      priority: CRITICAL
      tags: [network, mining, mitre_impact]
    
    # ========================
    # Process Security Rules
    # ========================
    
    # Detect Reverse Shell
    - rule: Reverse Shell Detected
      desc: Detect reverse shell attempts
      condition: >
        spawned_process and 
        container and
        ((proc.name = "bash" and proc.args contains "-i") or
         (proc.name = "nc" and proc.args contains "-e") or
         (proc.name = "python" and proc.args contains "socket"))
      output: >
        Reverse shell detected
        (user=%user.name command=%proc.cmdline 
        container_id=%container.id image=%container.image.repository)
      priority: CRITICAL
      tags: [container, shell, mitre_execution]
    
    # Detect Suspicious Process
    - rule: Suspicious Process in Container
      desc: Detect suspicious processes in containers
      condition: >
        spawned_process and 
        container and
        proc.name in (suspicious_procs)
      output: >
        Suspicious process spawned in container
        (user=%user.name process=%proc.name command=%proc.cmdline 
        container_id=%container.id)
      priority: WARNING
      tags: [container, process, mitre_execution]
    
    # ========================
    # Macro Definitions
    # ========================
    
    - macro: sensitive_files
      condition: >
        fd.name startswith /etc/shadow or
        fd.name startswith /etc/passwd or
        fd.name startswith /etc/sudoers or
        fd.name startswith /root/.ssh or
        fd.name contains /kube/config
    
    - macro: suspicious_procs
      condition: >
        proc.name in (nmap, masscan, nikto, sqlmap, metasploit, 
                      hydra, john, hashcat, mimikatz)
    
    - macro: mining_ports
      condition: >
        fd.sport in (3333, 4444, 5555, 7777, 8888, 9999, 14444, 45700)
    
    - list: suspicious_ips
      items: []  # Add suspicious IP list
    
    - list: mining_pools
      items:
        - pool.minexmr.com
        - xmr.nanopool.org
        - pool.supportxmr.com
```

### 4.3 Falcosidekick Alert Integration

```yaml
# Falcosidekick Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: falcosidekick
  namespace: falco
spec:
  replicas: 1
  selector:
    matchLabels:
      app: falcosidekick
  template:
    metadata:
      labels:
        app: falcosidekick
    spec:
      containers:
      - name: falcosidekick
        image: falcosecurity/falcosidekick:2.28.0
        
        env:
        # Slack Integration
        - name: SLACK_WEBHOOKURL
          valueFrom:
            secretKeyRef:
              name: falcosidekick-secrets
              key: slack-webhook
        - name: SLACK_MINIMUMPRIORITY
          value: "warning"
        - name: SLACK_OUTPUTFORMAT
          value: "all"
        
        # PagerDuty Integration
        - name: PAGERDUTY_ROUTINGKEY
          valueFrom:
            secretKeyRef:
              name: falcosidekick-secrets
              key: pagerduty-key
        - name: PAGERDUTY_MINIMUMPRIORITY
          value: "critical"
        
        # Prometheus Alertmanager
        - name: ALERTMANAGER_HOSTPORT
          value: "http://alertmanager.monitoring:9093"
        - name: ALERTMANAGER_MINIMUMPRIORITY
          value: "warning"
        
        # Elasticsearch
        - name: ELASTICSEARCH_HOSTPORT
          value: "https://elasticsearch.logging:9200"
        - name: ELASTICSEARCH_INDEX
          value: "falco"
        - name: ELASTICSEARCH_TYPE
          value: "_doc"
        
        # Loki
        - name: LOKI_HOSTPORT
          value: "http://loki.logging:3100"
        - name: LOKI_MINIMUMPRIORITY
          value: "notice"
        
        # AWS CloudWatch
        - name: AWS_CLOUDWATCHLOGS_LOGGROUP
          value: "/falco/events"
        - name: AWS_CLOUDWATCHLOGS_LOGSTREAM
          value: "alerts"
        - name: AWS_REGION
          value: "us-west-2"
        
        ports:
        - containerPort: 2801
          name: http
        
        resources:
          requests:
            cpu: 50m
            memory: 64Mi
          limits:
            cpu: 200m
            memory: 256Mi
        
        livenessProbe:
          httpGet:
            path: /ping
            port: 2801
        
        readinessProbe:
          httpGet:
            path: /ping
            port: 2801
---
apiVersion: v1
kind: Service
metadata:
  name: falcosidekick
  namespace: falco
spec:
  ports:
  - port: 2801
    targetPort: 2801
  selector:
    app: falcosidekick
```

---

<!-- chunk: 五、Kubescape合规扫描 -->
## 5. Kubescape Compliance Scanning

### 5.1 Kubescape Deployment and Scanning

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend confirming with --dry-run or diff first
> - `helm upgrade/install`: Deploy/upgrade release

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, please verify target, scope and authorization before execution
#!/bin/bash
# kubescape-scanning.sh - Kubescape Scanning Script

# Install Kubescape
# curl -s https://raw.githubusercontent.com/kubescape/kubescape/master/install.sh | /bin/bash

# 1. NSA/CISA Framework Scanning
kubescape_nsa_scan() {
    kubescape scan framework nsa \
        --enable-host-scan \
        --format json \
        --output nsa-scan-results.json \
        --verbose
    
    # Generate HTML Report
    kubescape scan framework nsa \
        --format html \
        --output nsa-scan-report.html
}

# 2. CIS Benchmark Scanning
kubescape_cis_scan() {
    kubescape scan framework cis-v1.23-t1.0.1 \
        --enable-host-scan \
        --format json \
        --output cis-scan-results.json
}

# 3. MITRE ATT&CK Scanning
kubescape_mitre_scan() {
    kubescape scan framework mitre \
        --format json \
        --output mitre-scan-results.json
}

# 4. Specific Namespace Scanning
kubescape_namespace_scan() {
    local namespace=$1
    
    kubescape scan framework nsa \
        --include-namespaces $namespace \
        --format json \
        --output $namespace-scan-results.json
}

# 5. YAML File Scanning
kubescape_yaml_scan() {
    local yaml_path=$1
    
    kubescape scan $yaml_path \
        --format json \
        --output yaml-scan-results.json
}

# 6. Helm Chart Scanning
kubescape_helm_scan() {
    local chart_path=$1
    
    kubescape scan $chart_path \
        --format json \
        --output helm-scan-results.json
}

# 7. Continuous Scanning (Kubescape Operator)
install_kubescape_operator() {
    helm repo add kubescape https://kubescape.github.io/helm-charts/
    
    helm install kubescape kubescape/kubescape-operator \
        --namespace kubescape \
        --create-namespace \
        --set clusterName="my-cluster" \
        --set capabilities.continuousScan="enable" \
        --set capabilities.vulnerabilityScan="enable" \
        --set capabilities.nodeScan="enable"
}

# Usage Examples
# kubescape_nsa_scan
# kubescape_namespace_scan "production"
```
### 5.2 Kubescape CI/CD Integration

```yaml
# GitHub Actions - Kubescape
name: Kubernetes Security Scan

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  kubescape-scan:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Kubescape Scan
      uses: kubescape/github-action@v3
      with:
        format: sarif
        outputFile: kubescape-results.sarif
        frameworks: nsa,mitre
        severityThreshold: high
        controlsConfig: |
          {
            "C-0009": {"severity": "high"},
            "C-0016": {"severity": "critical"}
          }
    
    - name: Upload Kubescape results to GitHub Security tab
      uses: github/codeql-action/upload-sarif@v2
      with:
        sarif_file: kubescape-results.sarif
---
# GitLab CI - Kubescape
kubescape-scan:
  stage: scan
  image: quay.io/kubescape/kubescape:latest
  script:
    - kubescape scan framework nsa,mitre ./k8s/ 
        --format json 
        --output kubescape-results.json
        --compliance-threshold 80
    - |
      score=$(cat kubescape-results.json | jq '.summaryDetails.complianceScore')
      if (( $(echo "$score < 80" | bc -l) )); then
        echo "Compliance score $score is below threshold"
        exit 1
      fi
  artifacts:
    paths:
      - kubescape-results.json
```

---

<!-- chunk: 六、准入控制集成 -->
## 6. Admission Control Integration

### 6.1 Admission Policies Based on Scan Results

```yaml
# Kyverno Policy - Block High Risk Images
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: block-vulnerable-images
spec:
  validationFailureAction: Enforce
  background: true
  rules:
  - name: check-vulnerability-report
    match:
      any:
      - resources:
          kinds:
          - Pod
    preconditions:
      all:
      - key: "{{request.operation}}"
        operator: In
        value: ["CREATE", "UPDATE"]
    validate:
      message: "Image has critical vulnerabilities. Please fix before deploying."
      foreach:
      - list: "request.object.spec.containers"
        deny:
          conditions:
            any:
            - key: "{{ images.containers.\"{{element.image}}\".vulnerabilities.critical }}"
              operator: GreaterThan
              value: 0
---
# OPA/Gatekeeper Constraint
apiVersion: constraints.gatekeeper.sh/v1beta1
kind: K8sBlockVulnerableImages
metadata:
  name: block-critical-vulns
spec:
  match:
    kinds:
    - apiGroups: [""]
      kinds: ["Pod"]
    excludedNamespaces:
    - kube-system
    - gatekeeper-system
  parameters:
    maxCriticalVulns: 0
    maxHighVulns: 5
    allowedRegistries:
    - "gcr.io/my-project/"
    - "docker.io/library/"
---
# Constraint Template
apiVersion: templates.gatekeeper.sh/v1
kind: ConstraintTemplate
metadata:
  name: k8sblockvulnerableimages
spec:
  crd:
    spec:
      names:
        kind: K8sBlockVulnerableImages
      validation:
        openAPIV3Schema:
          type: object
          properties:
            maxCriticalVulns:
              type: integer
            maxHighVulns:
              type: integer
            allowedRegistries:
              type: array
              items:
                type: string
  targets:
  - target: admission.k8s.gatekeeper.sh
    rego: |
      package k8sblockvulnerableimages
      
      violation[{"msg": msg}] {
        container := input.review.object.spec.containers[_]
        not image_allowed(container.image)
        msg := sprintf("Image %v is not from an allowed registry", [container.image])
      }
      
      violation[{"msg": msg}] {
        container := input.review.object.spec.containers[_]
        vuln_report := data.inventory.namespace[input.review.object.metadata.namespace]["aquasecurity.github.io/v1alpha1"]["VulnerabilityReport"]
        report := vuln_report[_]
        report.metadata.labels["trivy-operator.container.name"] == container.name
        report.spec.summary.criticalCount > input.parameters.maxCriticalVulns
        msg := sprintf("Container %v has %v critical vulnerabilities (max allowed: %v)", 
          [container.name, report.spec.summary.criticalCount, input.parameters.maxCriticalVulns])
      }
      
      image_allowed(image) {
        some i
        startswith(image, input.parameters.allowedRegistries[i])
      }
```

---

<!-- chunk: 七、监控与告警 -->
## 7. Monitoring and Alerting

### 7.1 Security Scanning Monitoring

```yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: security-scanning-alerts
  namespace: monitoring
spec:
  groups:
  - name: vulnerability-alerts
    rules:
    # Critical Vulnerability Detection
    - alert: CriticalVulnerabilityDetected
      expr: |
        sum by (namespace, name, image) (
          trivy_vulnerability_total{severity="Critical"}
        ) > 0
      for: 5m
      labels:
        severity: critical
      annotations:
        summary: "Critical Vulnerability Detected"
        description: "Image {{ $labels.image }} in {{ $labels.namespace }}/{{ $labels.name }} has critical vulnerabilities"
    
    # Vulnerability Count Trend
    - alert: VulnerabilityCountIncreasing
      expr: |
        delta(sum(trivy_vulnerability_total{severity=~"Critical|High"})[24h:1h]) > 10
      for: 1h
      labels:
        severity: warning
      annotations:
        summary: "Vulnerability Count Continuously Increasing"
    
    # Scan Failure
    - alert: TrivyOperatorScanFailed
      expr: |
        trivy_operator_vulnerability_report_count{status="Failed"} > 0
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "Trivy Scan Failed"
  
  - name: falco-alerts
    rules:
    # Falco Alert
    - alert: FalcoCriticalAlert
      expr: |
        sum by (rule) (
          increase(falco_events{priority="Critical"}[5m])
        ) > 0
      for: 1m
      labels:
        severity: critical
      annotations:
        summary: "Falco Critical Event Detected"
        description: "Rule: {{ $labels.rule }}"
    
    # Falco Event Rate
    - alert: FalcoHighEventRate
      expr: |
        sum(rate(falco_events[5m])) > 100
      for: 10m
      labels:
        severity: warning
      annotations:
        summary: "Falco Event Rate Anomaly"
```

---

<!-- chunk: 八、快速参考 -->
## 8. Quick Reference

### 8.1 Scanning Command Cheat Sheet

```bash
# Trivy
trivy image nginx:latest                           # Image Scanning
trivy image --severity CRITICAL,HIGH nginx:latest  # Filter by Severity
trivy fs .                                         # File System Scanning
trivy config ./k8s/                                # IaC Scanning
trivy k8s --report summary cluster                 # K8s Cluster Scanning

# Grype
grype nginx:latest                                 # Image Scanning
grype sbom:./sbom.json                            # SBOM Scanning
grype dir:.                                        # Directory Scanning

# Syft
syft nginx:latest                                  # Generate SBOM
syft nginx:latest -o cyclonedx-json               # Specify Format

# Kubescape
kubescape scan framework nsa                       # NSA Framework Scanning
kubescape scan framework cis                       # CIS Scanning
kubescape scan ./k8s/                             # YAML Scanning

# Falco
falco --list                                       # List Rules
falco -r custom_rules.yaml                        # Use Custom Rules
```

### 8.2 Vulnerability Remediation Priority

| Priority | Condition | Action |
|-------|------|------|
| P0 | Critical + Exploitable + Production | Fix Immediately (24h) |
| P1 | Critical + No Fix Available | Mitigation + Track |
| P2 | High + Exploitable | Fix Within 7 Days |
| P3 | High/Medium + Dev Environment | Next Iteration |
| P4 | Low + Informational | Handle As Needed |

---

<!-- chunk: 九、最佳实践总结 -->
## 9. Best Practices Summary

### Security Scanning Checklist

- [ ] **CI/CD Integration**: All image builds must be scanned
- [ ] **Block Policy**: Block Critical vulnerabilities from deployment
- [ ] **SBOM Management**: Generate and store SBOM for all images
- [ ] **Runtime Monitoring**: Deploy Falco for anomaly detection
- [ ] **Compliance Scanning**: Regular NSA/CIS compliance checks
- [ ] **Vulnerability Tracking**: Integrate with Jira/GitHub Issues
- [ ] **Fix SLA**: Clear remediation timeframes for each severity level
- [ ] **Offline Capability**: Configure offline vulnerability databases
- [ ] **Alert Channels**: Set up multi-channel alerting
- [ ] **Audit Logging**: Record all scan results

---

**Related Documentation**: [90-Secret Management Tools](90-secret-management-tools.md) | [92-Policy Validation Tools](92-policy-validation-tools.md) | [93-Network Security Policies](93-network-policies.md)

**Versions**: Trivy 0.48+ | Grype 0.74+ | Falco 0.37+ | Kubescape 3.0+

---

<!-- chunk: Obsidian Related Documentation -->
## Obsidian Related Documentation

- domain-05-security-compliance MOC
- [[domain-05-security-compliance/README.md|Security Domain]]
- [[domain-05-security-compliance/00-open-source-projects-index.md|Domain-7 Security — Open Source Projects Index]]
- Kubernetes Authentication and Authorization System Detailed Explanation
- Network Security Policies and Zero Trust Architecture
- Runtime Security Protection and Threat Detection
- 04 - Audit Logging and Compliance Management
- 05 - Policy Validation and Admission Control Tools (Policy Validation)
- 06 - Pod Security Standards Detailed Explanation
- 07 - RBAC Permission Matrix Table
- 08 - Security Best Practices Table
- Kubernetes Security Hardening

## See Also

- 15-runtime-security-detection
- 16-compliance-audit-practices
- 18-network-defense-depth
- 19-zero-trust-architecture

- [[domain-05-security-compliance/README.md|Return to Directory]]

<!-- risk-assessed -->
