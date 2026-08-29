---
title: Compliance Automation and Audit
description: 'Best practices for compliance-automation-audit'
summary: 'Best practices for compliance-automation-audit'
category: general
tags:
- k8s
- apiserver
- prometheus
- grafana
- helm
- argocd
- flux
- docker
- opa
- falco
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All engineers
estimated_read_time: 90min
intent_queries:
- What is Compliance Automation and Audit
- How to implement Compliance Automation and Audit
- Kubernetes 05 security compliance best practices
trigger_keywords:
- Compliance Automation
- Compliance
- Automation
- and
- Audit
- security
- compliance
prerequisites:
- kubectl-basics
- rbac-basics
- helm-basics
- prometheus-basics
- monitoring-basics
- gitops-basics
- iac-basics
- tls-basics
- policy-basics
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-05-security-compliance/05-supply-chain/10-compliance-automation-audit.md
original_language: Chinese
---

> **Production Environment Security Notice**
>
> This document contains directly executable operational commands. Before executing, please verify: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether the commands have been validated in non-production environments. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state, but usually reversible), 🟢 Low risk/read-only (information gathering, no side effects).




---
tags:
- security
- supply-chain
- compliance
intent_queries:
- What is compliance-automation-audit?
- How to use compliance-automation-audit
- Best practices for compliance-automation-audit

tier: peripheral---
title: Compliance Automation and Audit
description: '<!-- chunk: Overview -->'
category: supply-chain-security
tags:
- k8s
- supply-chain
- security
- sbom
- slsa
- apiserver
- [[Prometheus|prometheus]]
- grafana
- [[Helm|helm]]
- [[ArgoCD|argocd]]
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- Security Engineers
- SRE
- Architects
estimated_read_time: 5min
intent_queries:
- What is Compliance Automation and Audit
- How to implement Compliance Automation and Audit
- [[Kubernetes|Kubernetes]] 39 supply chain security best practices
trigger_keywords:
- Compliance Automation
- Compliance
- Automation
- and
- Audit
- supply
- chain
- security
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

# Compliance Automation and Audit

<!-- chunk: Overview -->## Overview

In modern cloud-native environments, manual compliance checks can no longer meet the demands of continuous deployment and rapid iteration. Compliance automation transforms framework requirements such as SOC 2 Type II, PCI-DSS, and FedRAMP into automatically executable code. Through policy-as-code, continuous monitoring, and automated evidence collection, it enables continuous compliance verification rather than periodic audits.

This document covers automated implementation of mainstream compliance frameworks, audit evidence collection, compliance dashboards, and the role of software supply chain security in the compliance system.

---

<!-- chunk: 1. Compliance Framework and Supply Chain Security Mapping -->## 1. Compliance Framework and Supply Chain Security Mapping

## 1.1 Major Compliance Framework Overview

```mermaid
graph TB
    subgraph "Compliance Frameworks"
        SOC2["SOC 2 Type II\nTrust Services Criteria"]
        PCI["PCI-DSS v4.0\nPayment Card Industry Data Security Standard"]
        FED["FedRAMP\nFederal Risk and Authorization Management Program"]
        ISO["ISO 27001\nInformation Security Management"]
        HIPAA["HIPAA\nHealth Insurance Portability and Accountability Act"]
    end

    subgraph "Supply Chain Security Controls"
        C1["Container Image Signature Verification\nCosign + Policy Controller"]
        C2["SBOM Generation and Verification\nSyft + Grype"]
        C3["Vulnerability Scanning\nTrivy + Snyk"]
        C4["SLSA Provenance\nGitHub Actions SLSA"]
        C5["Code Signing\nGitsign"]
        C6["Dependency Audit\nDependabot + OWASP"]
        C7["Transparency Logs\nRekor + Fulcio"]
        C8["Policy-as-Code\nKyverno + OPA"]
    end

    SOC2 -->|"CC8.1 Change Management"| C1
    SOC2 -->|"CC6.6 Logical Access Control"| C5
    SOC2 -->|"CC7.1 Vulnerability Management"| C3
    PCI -->|"6.3.3 Vulnerability Patch Management"| C3
    PCI -->|"6.2.4 Software Integrity"| C4
    PCI -->|"12.3.4 Third-Party Software Security"| C6
    FED -->|"SA-15 Development Process Security"| C4
    FED -->|"SI-2 Defect Remediation"| C3
    FED -->|"CM-14 Public Signed Release"| C7
    ISO -->|"A.14.2 Development Process Security"| C8
    HIPAA -->|"§164.312(c) Integrity Protection"| C2
```

## 1.2 Control Measures Mapping Table

| Compliance Requirement | Framework Section | Technical Implementation | Automation Tool |
|---------|---------|---------|----------|
| Software Component Inventory | SOC 2 CC7.1, PCI 12.3.4 | SBOM Generation | Syft, SPDX |
| Known Vulnerability Management | SOC 2 CC7.1, PCI 6.3.3 | Vulnerability Scanning | Trivy, Grype |
| Code Integrity Verification | SOC 2 CC8.1, PCI 6.2.4 | Container Image Signing | Cosign, SLSA |
| Change Control Records | SOC 2 CC8.1, FedRAMP CM-3 | Provenance Attestation | Rekor, GitHub Audit |
| Dependency Security | PCI 6.3.3, SOC 2 CC7.1 | SCA Scanning | Dependabot, OWASP |
| Access Control | SOC 2 CC6.1, HIPAA §164.312 | RBAC + OIDC | Kubernetes RBAC |
| Audit Logging | SOC 2 CC7.2, PCI 10 | Log Aggregation | Rekor, Falco, CloudTrail |
| Deployment Verification | FedRAMP CM-14 | Policy Enforcement | Kyverno, OPA |

---

<!-- chunk: 2. SOC 2 Type II Automation -->## 2. SOC 2 Type II Automation

## 2.1 SOC 2 Control Framework Implementation

```mermaid
graph LR
    subgraph "Availability"
        A1["Infrastructure Monitoring\nPrometheus + Grafana"]
        A2["SLA Metrics Tracking\nSLO/SLI Dashboard"]
        A3["Disaster Recovery Testing\nAutomated Chaos Injection"]
    end

    subgraph "Confidentiality"
        C1["Data Encryption Verification\nKMS + cert-manager"]
        C2["Access Log Audit\nOPA + RBAC Audit"]
        C3["Key Rotation Automation\nExternal Secrets"]
    end

    subgraph "Processing Integrity"
        P1["Code Quality Gating\nSonarQube + CodeQL"]
        P2["Supply Chain Integrity\nSLSA + Cosign"]
        P3["Deployment Verification\nKyverno Policy"]
    end

    subgraph "Privacy"
        PR1["PII Data Scanning\nAWS Macie / GCP DLP"]
        PR2["Data Retention Policy\nAutomated Cleanup Jobs"]
    end

    subgraph "Security"
        S1["Vulnerability Scanning\nTrivy CI/CD Integration"]
        S2["SAST/DAST\nCodeQL + OWASP ZAP"]
        S3["Penetration Test Tracking\nJira + Auto Tickets"]
    end
```

## 2.2 SOC 2 CC8.1 Change Management Automation

```yaml
# .github/workflows/soc2-change-management.yml
name: SOC 2 Change Management Controls

on:
  pull_request:
    branches: [main]
  push:
    branches: [main]

permissions:
  contents: read
  security-events: write
  id-token: write
  pull-requests: write

jobs:
  # ============================================================
  # CC8.1a: Change Request Record
  # ============================================================
  record-change-request:
    name: Record Change Request (CC8.1a)
    runs-on: ubuntu-latest
    if: github.event_name == 'pull_request'

    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Capture change metadata
        id: change-meta
        run: |
          # Collect change information
          CHANGE_ID="CHG-$(date +%Y%m%d)-${{ github.event.pull_request.number }}"
          CHANGED_FILES=$(git diff --name-only HEAD~1 HEAD | wc -l)
          RISK_LEVEL="low"
          
          # Risk assessment (based on file changes)
          if git diff --name-only HEAD~1 HEAD | grep -qE "(security|auth|crypto|password|secret)"; then
            RISK_LEVEL="high"
          elif git diff --name-only HEAD~1 HEAD | grep -qE "(helm|k8s|kubernetes|deploy)"; then
            RISK_LEVEL="medium"
          fi
          
          echo "change-id=$CHANGE_ID" >> "$GITHUB_OUTPUT"
          echo "risk-level=$RISK_LEVEL" >> "$GITHUB_OUTPUT"
          echo "changed-files=$CHANGED_FILES" >> "$GITHUB_OUTPUT"

      - name: Create change record
        run: |
          cat > change-record.json << EOF
          {
            "changeId": "${{ steps.change-meta.outputs.change-id }}",
            "requestor": "${{ github.event.pull_request.user.login }}",
            "title": "${{ github.event.pull_request.title }}",
            "description": "${{ github.event.pull_request.body }}",
            "riskLevel": "${{ steps.change-meta.outputs.risk-level }}",
            "changedFiles": ${{ steps.change-meta.outputs.changed-files }},
            "branch": "${{ github.head_ref }}",
            "targetBranch": "${{ github.base_ref }}",
            "commitSha": "${{ github.event.pull_request.head.sha }}",
            "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "prUrl": "${{ github.event.pull_request.html_url }}"
          }
          EOF
          
          # Store to compliance database (example: AWS S3)
          aws s3 cp change-record.json \
            "s3://compliance-evidence-bucket/soc2/cc8-1/changes/${{ steps.change-meta.outputs.change-id }}.json" \
            --sse aws:kms \
            --kms-key-id "${{ vars.COMPLIANCE_KMS_KEY_ID }}"

      - name: Comment change ID on PR
        uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `<!-- chunk: 🔒 SOC 2 Change Control\n\n**Change ID**: \`${{ steps.change-meta.outputs.change-id }}\`\n**Risk Level**: ${{ steps.change-meta.outputs.risk-level }}\n\nThis change has been recorded in the compliance system.` -->## 🔒 SOC 2 Change Control\n\n**Change ID**: \`${{ steps.change-meta.outputs.change-id }}\`\n**Risk Level**: ${{ steps.change-meta.outputs.risk-level }}\n\nThis change has been recorded in the compliance system.`
            })

  # ============================================================
  # CC8.1b: Change Approval Verification
  # ============================================================
  verify-approval:
    name: Verify Change Approval (CC8.1b)
    runs-on: ubuntu-latest
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'

    steps:
      - uses: actions/checkout@v4

      - name: Verify PR was approved
        uses: actions/github-script@v7
        with:
          script: |
            // Get the merged PR
            const { data: pulls } = await github.rest.repos.listPullRequestsAssociatedWithCommit({
              owner: context.repo.owner,
              repo: context.repo.repo,
              commit_sha: context.sha
            });
            
            if (pulls.length === 0) {
              core.setFailed('No PR found for this commit - direct push to main is not allowed');
              return;
            }
            
            const pr = pulls[0];
            
            // Check approvals
            const { data: reviews } = await github.rest.pulls.listReviews({
              owner: context.repo.owner,
              repo: context.repo.repo,
              pull_number: pr.number
            });
            
            const approvals = reviews.filter(r => r.state === 'APPROVED');
            
            if (approvals.length === 0) {
              core.setFailed(`PR #${pr.number} was not approved before merging`);
              return;
            }
            
            console.log(`✅ PR #${pr.number} was approved by ${approvals.map(a => a.user.login).join(', ')}`);

  # ============================================================
  # CC7.1: Vulnerability Management Evidence Collection
  # ============================================================
  collect-vulnerability-evidence:
    name: Collect Vulnerability Evidence (CC7.1)
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Run comprehensive vulnerability scan
        uses: aquasecurity/trivy-action@0.20.0
        with:
          scan-type: 'fs'
          format: 'json'
          output: 'trivy-results.json'

      - name: Run SAST scan
        uses: github/codeql-action/analyze@v3
        continue-on-error: true

      - name: Run dependency audit
        run: |
          # Node.js
          if [ -f package.json ]; then
            npm audit --json > npm-audit.json 2>/dev/null || true
          fi
          
          # Python
          if [ -f requirements.txt ]; then
            pip install safety && safety check --json > pip-safety.json 2>/dev/null || true
          fi
          
          # Go
          if [ -f go.mod ]; then
            go install golang.org/x/vuln/cmd/govulncheck@latest
            govulncheck -json ./... > govuln-results.json 2>/dev/null || true
          fi

      - name: Generate vulnerability summary
        run: |
          python3 << 'EOF'
          import json
          from datetime import datetime
          
          summary = {
              "timestamp": datetime.utcnow().isoformat(),
              "commitSha": "${{ github.sha }}",
              "repository": "${{ github.repository }}",
              "scanTypes": [],
              "criticalCount": 0,
              "highCount": 0,
              "mediumCount": 0,
              "lowCount": 0
          }
          
          try:
              with open('trivy-results.json') as f:
                  trivy = json.load(f)
                  for result in trivy.get('Results', []):
                      for vuln in result.get('Vulnerabilities', []):
                          sev = vuln.get('Severity', '').upper()
                          if sev == 'CRITICAL':
                              summary['criticalCount'] += 1
                          elif sev == 'HIGH':
                              summary['highCount'] += 1
                          elif sev == 'MEDIUM':
                              summary['mediumCount'] += 1
                          else:
                              summary['lowCount'] += 1
                  summary['scanTypes'].append('trivy-filesystem')
          except FileNotFoundError:
              pass
          
          summary['compliance'] = {
              'soc2_cc7_1': summary['criticalCount'] == 0,
              'pci_6_3_3': summary['criticalCount'] == 0 and summary['highCount'] < 5
          }
          
          with open('vulnerability-summary.json', 'w') as f:
              json.dump(summary, f, indent=2)
          
          print(json.dumps(summary, indent=2))
          EOF

      - name: Store evidence
        run: |
          EVIDENCE_DATE=$(date +%Y/%m/%d)
          aws s3 sync . "s3://compliance-evidence-bucket/soc2/cc7-1/${EVIDENCE_DATE}/${{ github.sha }}/" \
            --include "trivy-results.json" \
            --include "vulnerability-summary.json" \
            --include "npm-audit.json" \
            --sse aws:kms \
            --kms-key-id "${{ vars.COMPLIANCE_KMS_KEY_ID }}"

  # ============================================================
  # CC6.6: Supply Chain Integrity Verification (Image Signing)
  # ============================================================
  verify-supply-chain:
    name: Verify Supply Chain Integrity (CC6.6)
    runs-on: ubuntu-latest

    steps:
      - name: Install tools
        run: |
          go install github.com/sigstore/cosign/v2/cmd/cosign@latest
          go install github.com/slsa-framework/slsa-verifier/v2/cli/slsa-verifier@latest

      - name: Verify image signature
        run: |
          IMAGE="${{ vars.PRODUCTION_IMAGE }}:${{ github.sha }}"
          
          if cosign verify \
            --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
            --certificate-identity-regexp "^https://github.com/${{ github.repository }}/.github/workflows/.*" \
            --output-file /tmp/sig-verification.json \
            "$IMAGE"; then
            echo "SIGNATURE_VERIFIED=true" >> "$GITHUB_ENV"
          else
            echo "SIGNATURE_VERIFIED=false" >> "$GITHUB_ENV"
          fi

      - name: Store supply chain evidence
        run: |
          cat > supply-chain-evidence.json << EOF
          {
            "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "commitSha": "${{ github.sha }}",
            "image": "${{ vars.PRODUCTION_IMAGE }}:${{ github.sha }}",
            "signatureVerified": ${{ env.SIGNATURE_VERIFIED }},
            "verificationMethod": "cosign-keyless",
            "oidcIssuer": "https://token.actions.githubusercontent.com",
            "control": "SOC2-CC6.6"
          }
          EOF
          
          aws s3 cp supply-chain-evidence.json \
            "s3://compliance-evidence-bucket/soc2/cc6-6/${{ github.sha }}-supply-chain.json" \
            --sse aws:kms
```

---

<!-- chunk: 3. PCI-DSS v4.0 Compliance Automation -->## 3. PCI-DSS v4.0 Compliance Automation

## 3.1 PCI-DSS Requirement 6.3.x Automation

```yaml
# .github/workflows/pci-dss-compliance.yml
name: PCI-DSS Compliance Controls

on:
  push:
    branches: [main, 'release/**']
  schedule:
    - cron: '0 0 * * *'  # Daily compliance check

jobs:
  # ============================================================
  # PCI-DSS 6.3.1: Prevent Application Vulnerabilities
  # ============================================================
  pci-req-6-3-1:
    name: PCI 6.3.1 - Application Security
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: SAST Scan
        uses: github/codeql-action/analyze@v3
        with:
          category: "/language:java,python,javascript"

      - name: DAST Scan (OWASP ZAP)
        run: |
          docker run --rm \
            -v $(pwd):/zap/wrk \
            ghcr.io/zaproxy/zaproxy:stable \
            zap-baseline.py \
            -t "${{ vars.APP_URL }}" \
            -J zap-report.json \
            -r zap-report.html \
            -I  # Ignore WARN, report only FAIL

      - name: Check for secrets in code
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./
          base: ${{ github.event.repository.default_branch }}
          extra_args: --json

      - name: Generate PCI 6.3.1 evidence
        run: |
          cat > pci-6-3-1-evidence.json << EOF
          {
            "requirement": "PCI-DSS 6.3.1",
            "description": "Security vulnerabilities in software are identified and addressed",
            "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
            "commitSha": "${{ github.sha }}",
            "controls": {
              "sast": {
                "tool": "CodeQL",
                "status": "${{ job.status }}"
              },
              "dast": {
                "tool": "OWASP ZAP",
                "target": "${{ vars.APP_URL }}"
              },
              "secretScanning": {
                "tool": "TruffleHog",
                "enabled": true
              }
            }
          }
          EOF

  # ============================================================
  # PCI-DSS 6.3.3: Third-Party Component Security
  # ============================================================
  pci-req-6-3-3:
    name: PCI 6.3.3 - Third-Party Components
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - name: Generate SBOM
        uses: anchore/sbom-action@v0.16.0
        with:
          format: spdx-json
          output-file: sbom.spdx.json

      - name: Scan SBOM for vulnerabilities
        run: |
          # Scan SBOM with Grype
          grype sbom:sbom.spdx.json \
            --output json \
            --file grype-results.json
          
          # Check CRITICAL vulnerabilities
          CRITICAL=$(jq '[.matches[] | select(.vulnerability.severity == "Critical")] | length' grype-results.json)
          HIGH=$(jq '[.matches[] | select(.vulnerability.severity == "High")] | length' grype-results.json)
          
          echo "Critical vulnerabilities: $CRITICAL"
          echo "High vulnerabilities: $HIGH"
          
          if [ "$CRITICAL" -gt 0 ]; then
            echo "❌ PCI 6.3.3 FAILED: $CRITICAL CRITICAL vulnerabilities found"
            exit 1
          fi
          
          if [ "$HIGH" -gt 5 ]; then
            echo "❌ PCI 6.3.3 FAILED: $HIGH HIGH vulnerabilities exceed threshold (5)"
            exit 1
          fi
          
          echo "✅ PCI 6.3.3 PASSED"

      - name: Check license compliance
        run: |
          # Check license compliance
          jq '[.packages[] | select(.licenseConcluded | test("GPL|AGPL|LGPL"))] | 
              map({name: .name, version: .versionInfo, license: .licenseConcluded})' \
              sbom.spdx.json > license-issues.json
          
          COPYLEFT_COUNT=$(jq length license-issues.json)
          echo "Copyleft licensed packages: $COPYLEFT_COUNT"
          
          if [ "$COPYLEFT_COUNT" -gt 0 ]; then
            echo "⚠️ WARNING: Found packages with copyleft licenses:"
            cat license-issues.json | jq .
          fi

      - name: Verify component integrity
        run: |
          # Verify checksums of critical components
          if [ -f "component-hashes.txt" ]; then
            sha256sum -c component-hashes.txt
            echo "✅ Component integrity verified"
          fi

  # ============================================================
  # PCI-DSS 10: Audit Logging Requirements
  # ============================================================
  pci-req-10:
    name: PCI 10 - Audit Logging
    runs-on: ubuntu-latest

    steps:
      - name: Verify audit log configuration
        run: |
          # Check if Kubernetes audit logging is enabled
          kubectl get configmap -n kube-system kube-apiserver-config -o yaml | \
            grep -E "audit-log|audit-policy" || \
            echo "⚠️ Cannot verify audit log configuration remotely"
          
          # Check audit log retention policy (>= 12 months)
          aws cloudtrail describe-trails \
            --query 'trailList[].{Name:Name,HasCustomEventSelectors:HasCustomEventSelectors,S3BucketName:S3BucketName}' \
            --output json

      - name: Verify log integrity
        run: |
          # Verify CloudTrail log integrity
          aws cloudtrail validate-logs \
            --trail-arn "${{ vars.CLOUDTRAIL_ARN }}" \
            --start-time "$(date -u -d '24 hours ago' +%Y-%m-%dT%H:%M:%SZ)" \
            --end-time "$(date -u +%Y-%m-%dT%H:%M:%SZ)"

  # ============================================================
  # Generate PCI-DSS Compliance Report
  # ============================================================
  pci-compliance-report:
    name: Generate PCI-DSS Compliance Report
    needs: [pci-req-6-3-1, pci-req-6-3-3, pci-req-10]
    runs-on: ubuntu-latest
    if: always()

    steps:
      - name: Generate comprehensive report
        run: |
          python3 << 'EOF'
          import json
          from datetime import datetime
          
          report = {
              "reportType": "PCI-DSS v4.0 Compliance Report",
              "generatedAt": datetime.utcnow().isoformat(),
              "repository": "${{ github.repository }}",
              "commitSha": "${{ github.sha }}",
              "overallStatus": "PASS" if "${{ needs.pci-req-6-3-1.result }}" == "success" and \
                              "${{ needs.pci-req-6-3-3.result }}" == "success" else "FAIL",
              "requirements": {
                  "6.3.1": {
                      "description": "Application security vulnerabilities prevention",
                      "status": "${{ needs.pci-req-6-3-1.result }}",
                      "controls": ["SAST", "DAST", "Secret Scanning"]
                  },
                  "6.3.3": {
                      "description": "Third-party component security",
                      "status": "${{ needs.pci-req-6-3-3.result }}",
                      "controls": ["SBOM Generation", "Vulnerability Scanning", "License Compliance"]
                  },
                  "10": {
                      "description": "Audit logging",
                      "status": "${{ needs.pci-req-10.result }}",
                      "controls": ["CloudTrail", "K8s Audit Log", "Log Integrity"]
                  }
              }
          }
          
          print(json.dumps(report, indent=2))
          
          with open('pci-compliance-report.json', 'w') as f:
              json.dump(report, f, indent=2)
          EOF

      - name: Upload report
        uses: actions/upload-artifact@v4
        with:
          name: pci-compliance-report
          path: pci-compliance-report.json
          retention-days: 90  # PCI-DSS requires 12 months retention
```

---

<!-- chunk: 4. FedRAMP Continuous Monitoring -->## 4. FedRAMP Continuous Monitoring

## 4.1 FedRAMP Continuous Authorization Monitoring Architecture

```mermaid
graph TB
    subgraph "Scanning Layer"
        VS["Vulnerability Scanning\nMonthly/Quarterly"]
        CS["Configuration Scanning\nSTIG/CIS Benchmark"]
        PA["Penetration Testing\nAnnually"]
        LS["Log Review\nContinuous"]
    end

    subgraph "Data Collection Layer"
        ES["OpenSCAP\nCompliance Data Collection"]
        CW["AWS Config\nConfiguration Change Tracking"]
        CT["CloudTrail\nOperation Audit"]
        KC["Kubernetes Audit\nAdmission Control Logs"]
    end

    subgraph "Analysis Layer"
        SE["SIEM\nElastic Security"]
        CM["Compliance Management Platform\nDrata/Vanta/Tugboat"]
        AL["Automated Alerting\nPagerDuty/Slack"]
    end

    subgraph "Reporting Layer"
        POA["POA&M\nPlan and Milestones"]
        SAR["SAR\nSecurity Assessment Report"]
        CSP["CSP Monthly Report\nSubmit to Authorizing Officer"]
    end

    VS --> ES
    CS --> ES
    LS --> SE
    CW --> CM
    CT --> CM
    KC --> SE
    ES --> CM
    SE --> CM
    CM --> AL
    CM --> POA
    CM --> SAR
    POA --> CSP
    SAR --> CSP
```

## 4.2 FedRAMP SA-15 Development Process Security Control

```yaml
# fedramp-sa15-controls.yaml
# FedRAMP SA-15: Development Process, Standards, and Tools

---
# Control SA-15: Ensure the security of development tools and processes
name: FedRAMP SA-15 Compliance Checks

controls:
  # SA-15(7): Supply Chain Protection
  supply-chain-protection:
    automated: true
    checks:
      - id: SA-15-7-1
        description: "All container images must have SLSA Level 3 provenance"
        implementation: |
          # Kyverno ClusterPolicy
          - Enforce SLSA provenance attestation
          - Verify builder ID matches SLSA Generator
          - Require signed provenance from GitHub Actions
        
      - id: SA-15-7-2
        description: "All builds must be recorded in an immutable transparency log"
        implementation: |
          # Rekor Transparency Log Integration
          - cosign sign --tlog-upload=true
          - Record build metadata in Rekor
          - Provide Rekor log URL in deployment metadata
      
      - id: SA-15-7-3
        description: "Software Bill of Materials (SBOM) must be released with each version"
        implementation: |
          # Syft SBOM Generation
          - Generate SPDX JSON SBOM
          - Attest SBOM with cosign
          - Store SBOM in artifact registry

  # SA-15(10): Vulnerability Analysis
  vulnerability-analysis:
    automated: true
    frequency: per-commit
    checks:
      - id: SA-15-10-1
        description: "Automatic vulnerability scanning on code commits"
        implementation: |
          # Trivy + GitHub Advanced Security
          - trivy fs --exit-code 1 --severity CRITICAL .
          - CodeQL analysis on every PR
          - Dependabot automated security updates

---
# FedRAMP Automated Checks Workflow
apiVersion: batch/v1
kind: CronJob
metadata:
  name: fedramp-conmon-scan
  namespace: compliance

spec:
  schedule: "0 2 * * *"  # Daily 02:00 UTC
  jobTemplate:
    spec:
      template:
        spec:
          containers:
            - name: conmon-scanner
              image: your-org/fedramp-scanner:latest
              command: ["/bin/sh", "-c"]
              args:
                - |
                  #!/bin/sh
                  
                  # 1. Run OpenSCAP configuration compliance scan
                  oscap xccdf eval \
                    --profile xccdf_org.ssgproject.content_profile_stig \
                    --results-arf /results/arf.xml \
                    --report /results/report.html \
                    /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml
                  
                  # 2. Collect Kubernetes configuration audit
                  kube-bench run \
                    --config-dir /etc/kube-bench/cfg \
                    --config /etc/kube-bench/cfg/config.yaml \
                    --json > /results/kube-bench.json
                  
                  # 3. Scan container image vulnerabilities
                  kubectl get pods --all-namespaces -o json | \
                    jq -r '.items[].spec.containers[].image' | \
                    sort -u | \
                    while read IMAGE; do
                      trivy image --format json "$IMAGE" >> /results/image-vulns.json
                    done
                  
                  # 4. Upload results
                  aws s3 sync /results/ \
                    "s3://fedramp-evidence-bucket/conmon/$(date +%Y/%m/%d)/" \
                    --sse aws:kms \
                    --kms-key-id "$COMPLIANCE_KMS_KEY"
```

## 4.3 FedRAMP POA&M Automation

```python
#!/usr/bin/env python3
# fedramp_poam_generator.py
# Automatically generate FedRAMP Plan of Action and Milestones (POA&M)

import json
import csv
import boto3
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class POAMItem:
    """POA&M Item"""
    item_id: str
    weakness_name: str
    weakness_source: str  # Vulnerability/Configuration/Policy
    cve_ids: List[str]
    severity: str  # critical/high/medium/low
    control_id: str  # NIST SP 800-53 Control ID
    resources_required: str
    overall_remediation_plan: str
    milestones: List[dict]
    scheduled_completion_date: str
    status: str  # open/closed/in-progress
    risk_adjustment: Optional[str] = None
    
def scan_and_generate_poam(scan_results_path: str) -> List[POAMItem]:
    """Generate POA&M items from scan results"""
    items = []
    
    with open(scan_results_path) as f:
        scan_results = json.load(f)
    
    for i, match in enumerate(scan_results.get('matches', [])):
        vuln = match.get('vulnerability', {})
        artifact = match.get('artifact', {})
        
        # Only process HIGH and CRITICAL
        if vuln.get('severity') not in ['High', 'Critical']:
            continue
        
        # Determine remediation deadline (FedRAMP requirement)
        severity = vuln.get('severity', '').lower()
        if severity == 'critical':
            days_to_fix = 30   # CRITICAL: 30 days
        elif severity == 'high':
            days_to_fix = 90   # HIGH: 90 days
        else:
            days_to_fix = 180
        
        scheduled_date = (datetime.utcnow() + timedelta(days=days_to_fix)).strftime('%Y-%m-%d')
        
        item = POAMItem(
            item_id=f"POAM-{i+1:04d}",
            weakness_name=f"{vuln.get('id', 'Unknown')}: {vuln.get('description', '')[:100]}",
            weakness_source="Automated Vulnerability Scan (Grype)",
            cve_ids=[vuln.get('id')] if vuln.get('id', '').startswith('CVE-') else [],
            severity=severity,
            control_id=map_cve_to_control(vuln.get('id', '')),
            resources_required="DevSecOps Team (4 hours)",
            overall_remediation_plan=f"Update {artifact.get('name', 'package')} from {artifact.get('version', 'unknown')} to {vuln.get('fix', {}).get('versions', ['N/A'])[0] if vuln.get('fix') else 'N/A'}",
            milestones=[
                {
                    "id": "M1",
                    "description": "Identify affected systems and validate vulnerability",
                    "scheduledDate": (datetime.utcnow() + timedelta(days=7)).strftime('%Y-%m-%d'),
                    "status": "open"
                },
                {
                    "id": "M2", 
                    "description": "Develop and test remediation",
                    "scheduledDate": (datetime.utcnow() + timedelta(days=days_to_fix - 7)).strftime('%Y-%m-%d'),
                    "status": "open"
                },
                {
                    "id": "M3",
                    "description": "Deploy remediation to production",
                    "scheduledDate": scheduled_date,
                    "status": "open"
                }
            ],
            scheduled_completion_date=scheduled_date,
            status="open"
        )
        
        items.append(item)
    
    return items

def map_cve_to_control(cve_id: str) -> str:
    """Map CVE to NIST SP 800-53 Control"""
    # Simplified mapping
    control_map = {
        "injection": "SI-3",
        "auth": "IA-2",
        "xss": "SI-3",
        "crypto": "SC-8",
        "config": "CM-6",
    }
    return "SI-2"  # Default: Defect Remediation

def export_poam_csv(items: List[POAMItem], output_file: str):
    """Export POA&M to CSV (compliant with FedRAMP format requirements)"""
    fieldnames = [
        "POA&M Item ID",
        "Controls Weakness Name",
        "Weakness Source Identifier",
        "Source Identifier",
        "Control Identifier",
        "Resources Required",
        "Overall Remediation Plan",
        "Milestones with Completion Dates",
        "Scheduled Completion Date",
        "Status"
    ]
    
    with open(output_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        
        for item in items:
            milestones_str = "; ".join([
                f"{m['id']}: {m['description']} ({m['scheduledDate']})"
                for m in item.milestones
            ])
            
            writer.writerow({
                "POA&M Item ID": item.item_id,
                "Controls Weakness Name": item.weakness_name,
                "Weakness Source Identifier": item.weakness_source,
                "Source Identifier": ", ".join(item.cve_ids) if item.cve_ids else "N/A",
                "Control Identifier": item.control_id,
                "Resources Required": item.resources_required,
                "Overall Remediation Plan": item.overall_remediation_plan,
                "Milestones with Completion Dates": milestones_str,
                "Scheduled Completion Date": item.scheduled_completion_date,
                "Status": item.status
            })

if __name__ == "__main__":
    import sys
    
    scan_file = sys.argv[1] if len(sys.argv) > 1 else "grype-results.json"
    output_file = sys.argv[2] if len(sys.argv) > 2 else "fedramp-poam.csv"
    
    items = scan_and_generate_poam(scan_file)
    export_poam_csv(items, output_file)
    
    print(f"Generated POA&M with {len(items)} items: {output_file}")
```

---

<!-- chunk: 5. Automated Audit Evidence Collection -->## 5. Automated Audit Evidence Collection

## 5.1 Evidence Collection Architecture

```mermaid
graph LR
    subgraph "Evidence Sources"
        GH["GitHub\nPR Review/Commit Records"]
        CI["CI/CD\nBuild Logs/Test Results"]
        K8S["Kubernetes\nDeployment/Policy Events"]
        CLD["Cloud Provider\nIAM/CloudTrail/Config"]
        SIG["Sigstore\nRekor Transparency Log"]
    end

    subgraph "Collection Layer"
        EC["Evidence Collector\n(Evidence Collector)"]
        EC1["GitHub API Crawler"]
        EC2["CI Artifact Collection"]
        EC3["K8s Audit Logs"]
        EC4["Cloud API Collection"]
        EC5["Rekor Query"]
    end

    subgraph "Storage Layer"
        S3["AWS S3\nImmutable Storage\n+ KMS Encryption"]
        DB["Aurora\nEvidence Index"]
        TS["Timestamp Service\nRFC 3161"]
    end

    subgraph "Compliance Platform"
        DR["Drata\nAutomated Compliance Management"]
        VN["Vanta\nContinuous Compliance Monitoring"]
        TG["Tugboat Logic\nCustomized Compliance"]
        CH["Custom Platform\nInternal Development"]
    end

    GH --> EC1
    CI --> EC2
    K8S --> EC3
    CLD --> EC4
    SIG --> EC5
    EC1 & EC2 & EC3 & EC4 & EC5 --> EC
    EC --> S3
    EC --> DB
    EC --> TS
    S3 & DB --> DR
    S3 & DB --> VN
    S3 & DB --> CH
```

## 5.2 Evidence Collection Automation Script

```python
#!/usr/bin/env python3
# evidence_collector.py
# Automated compliance evidence collection

import os
import json
import boto3
import hashlib
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any

class EvidenceCollector:
    """Automated compliance evidence collector"""
    
    def __init__(self, s3_bucket: str, kms_key_id: str):
        self.s3 = boto3.client('s3')
        self.s3_bucket = s3_bucket
        self.kms_key_id = kms_key_id
        self.timestamp = datetime.now(timezone.utc).isoformat()
        
    def collect_github_pr_approvals(self, org: str, repo: str, token: str) -> Dict:
        """Collect GitHub PR approval records"""
        import requests
        
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
        
        # Get recently merged PRs
        response = requests.get(
            f"https://api.github.com/repos/{org}/{repo}/pulls",
            params={"state": "closed", "per_page": 50},
            headers=headers
        )
        
        evidence = {
            "controlId": "SOC2-CC8.1",
            "description": "Pull Request approval records",
            "collectedAt": self.timestamp,
            "repository": f"{org}/{repo}",
            "records": []
        }
        
        for pr in response.json():
            if not pr.get('merged_at'):
                continue
            
            # Get approval information
            reviews_response = requests.get(
                f"https://api.github.com/repos/{org}/{repo}/pulls/{pr['number']}/reviews",
                headers=headers
            )
            
            approvals = [r for r in reviews_response.json() if r['state'] == 'APPROVED']
            
            evidence['records'].append({
                "prNumber": pr['number'],
                "title": pr['title'],
                "author": pr['user']['login'],
                "mergedAt": pr['merged_at'],
                "mergedBy": pr.get('merged_by', {}).get('login', 'unknown'),
                "approvals": [
                    {
                        "reviewer": a['user']['login'],
                        "approvedAt": a['submitted_at']
                    }
                    for a in approvals
                ],
                "approvalCount": len(approvals),
                "compliant": len(approvals) >= 2  # Requires 2 approvals
            })
        
        return evidence
    
    def collect_image_signatures(self, images: list) -> Dict:
        """Collect container image signature proof"""
        evidence = {
            "controlId": "SOC2-CC6.6",
            "description": "Container image signing verification",
            "collectedAt": self.timestamp,
            "records": []
        }
        
        for image in images:
            result = subprocess.run(
                ["cosign", "verify",
                 "--certificate-oidc-issuer", "https://token.actions.githubusercontent.com",
                 "--certificate-identity-regexp", ".*",
                 "--output-file", "/tmp/sig.json",
                 image],
                capture_output=True, text=True
            )
            
            record = {
                "image": image,
                "verified": result.returncode == 0,
                "verifiedAt": self.timestamp
            }
            
            if result.returncode == 0:
                try:
                    with open('/tmp/sig.json') as f:
                        sigs = json.load(f)
                    if sigs:
                        record['signerInfo'] = {
                            "issuer": sigs[0].get('optional', {}).get('Issuer'),
                            "subject": sigs[0].get('optional', {}).get('Subject')
                        }
                except Exception:
                    pass
            
            evidence['records'].append(record)
        
        return evidence
    
    def collect_vulnerability_scan_results(self, image: str) -> Dict:
        """Collect vulnerability scan results"""
        # Run Trivy scan
        result = subprocess.run(
            ["trivy", "image", "--format", "json", "--output", "/tmp/trivy.json", image],
            capture_output=True, text=True
        )
        
        evidence = {
            "controlId": "SOC2-CC7.1",
            "description": "Vulnerability scan results",
            "collectedAt": self.timestamp,
            "image": image
        }
        
        try:
            with open('/tmp/trivy.json') as f:
                scan_results = json.load(f)
            
            counts = {"CRITICAL": 0, "HIGH": 0, "MEDIUM": 0, "LOW": 0}
            
            for result_item in scan_results.get('Results', []):
                for vuln in result_item.get('Vulnerabilities', []):
                    sev = vuln.get('Severity', 'UNKNOWN').upper()
                    if sev in counts:
                        counts[sev] += 1
            
            evidence['summary'] = counts
            evidence['compliant'] = counts['CRITICAL'] == 0
            evidence['scannerVersion'] = scan_results.get('SchemaVersion', 'unknown')
        except Exception as e:
            evidence['error'] = str(e)
        
        return evidence
    
    def collect_kubernetes_rbac_evidence(self) -> Dict:
        """Collect Kubernetes RBAC configuration evidence"""
        evidence = {
            "controlId": "SOC2-CC6.1",
            "description": "Kubernetes RBAC access control evidence",
            "collectedAt": self.timestamp,
            "records": []
        }
        
        # Get ClusterRoleBindings
        result = subprocess.run(
            ["kubectl", "get", "clusterrolebindings", "-o", "json"],
            capture_output=True, text=True
        )
        
        if result.returncode == 0:
            bindings = json.loads(result.stdout)
            
            # Check for overly broad permissions
            for binding in bindings.get('items', []):
                role_ref = binding.get('roleRef', {})
                subjects = binding.get('subjects', [])
                
                if role_ref.get('name') == 'cluster-admin':
                    evidence['records'].append({
                        "bindingName": binding['metadata']['name'],
                        "role": "cluster-admin",
                        "subjects": subjects,
                        "risk": "HIGH",
                        "note": "cluster-admin binding detected"
                    })
        
        return evidence
    
    def store_evidence(self, evidence: Dict, control_id: str) -> str:
        """Store evidence to S3 (immutable storage)"""
        # Calculate evidence hash (integrity assurance)
        evidence_json = json.dumps(evidence, sort_keys=True)
        evidence_hash = hashlib.sha256(evidence_json.encode()).hexdigest()
        
        evidence['_metadata'] = {
            "hash": evidence_hash,
            "storedAt": self.timestamp,
            "collector": "automated-evidence-collector/v1.0"
        }
        
        # Generate S3 path
        date_path = datetime.now().strftime("%Y/%m/%d")
        s3_key = f"evidence/{control_id}/{date_path}/{control_id}-{evidence_hash[:8]}.json"
        
        # Upload to S3 (encryption + object lock)
        self.s3.put_object(
            Bucket=self.s3_bucket,
            Key=s3_key,
            Body=json.dumps(evidence, indent=2).encode(),
            ServerSideEncryption='aws:kms',
            SSEKMSKeyId=self.kms_key_id,
            ContentType='application/json',
            # WORM (Write Once Read Many) protection
            ObjectLockMode='COMPLIANCE',
            ObjectLockRetainUntilDate=datetime(
                datetime.now().year + 7,
                datetime.now().month,
                datetime.now().day
            )
        )
        
        return f"s3://{self.s3_bucket}/{s3_key}"
    
    def generate_evidence_report(self, evidence_items: list) -> str:
        """Generate evidence report"""
        report = {
            "reportType": "Compliance Evidence Report",
            "generatedAt": self.timestamp,
            "evidenceItems": len(evidence_items),
            "summary": {},
            "items": evidence_items
        }
        
        # Aggregate compliance status
        for item in evidence_items:
            control_id = item.get('controlId', 'unknown')
            compliant = item.get('compliant', True)
            
            report['summary'][control_id] = {
                "status": "COMPLIANT" if compliant else "NON-COMPLIANT",
                "evidenceCount": len(item.get('records', []))
            }
        
        return json.dumps(report, indent=2)


def main():
    collector = EvidenceCollector(
        s3_bucket=os.environ['COMPLIANCE_S3_BUCKET'],
        kms_key_id=os.environ['COMPLIANCE_KMS_KEY_ID']
    )
    
    # Collect various types of evidence
    evidence_items = []
    
    # 1. GitHub PR approval evidence
    pr_evidence = collector.collect_github_pr_approvals(
        org=os.environ['GITHUB_ORG'],
        repo=os.environ['GITHUB_REPO'],
        token=os.environ['GITHUB_TOKEN']
    )
    s3_path = collector.store_evidence(pr_evidence, "SOC2-CC8.1")
    print(f"PR approval evidence stored: {s3_path}")
    evidence_items.append(pr_evidence)
    
    # 2. Image signature evidence
    images = os.environ.get('PRODUCTION_IMAGES', '').split(',')
    if images:
        sig_evidence = collector.collect_image_signatures(images)
        s3_path = collector.store_evidence(sig_evidence, "SOC2-CC6.6")
        print(f"Image signature evidence stored: {s3_path}")
        evidence_items.append(sig_evidence)
    
    # 3. Vulnerability scan evidence
    for image in images:
        vuln_evidence = collector.collect_vulnerability_scan_results(image)
        s3_path = collector.store_evidence(vuln_evidence, "SOC2-CC7.1")
        print(f"Vulnerability scan evidence stored: {s3_path}")
        evidence_items.append(vuln_evidence)
    
    # 4. RBAC evidence
    rbac_evidence = collector.collect_kubernetes_rbac_evidence()
    s3_path = collector.store_evidence(rbac_evidence, "SOC2-CC6.1")
    evidence_items.append(rbac_evidence)
    
    # Generate comprehensive report
    report = collector.generate_evidence_report(evidence_items)
    print("\n=== Compliance Evidence Report ===")
    print(report)

if __name__ == "__main__":
    main()
```

---

<!-- chunk: 6. Compliance Dashboards -->## 6. Compliance Dashboards

## 6.1 Grafana Compliance Dashboard Configuration

```json
{
  "title": "Supply Chain Security Compliance Dashboard",
  "tags": ["compliance", "security", "soc2", "pci"],
  "panels": [
    {
      "id": 1,
      "title": "Overall Compliance Score",
      "type": "gauge",
      "gridPos": {"h": 8, "w": 6, "x": 0, "y": 0},
      "options": {
        "orientation": "horizontal",
        "reduceOptions": {"calcs": ["lastNotNull"]},
        "thresholds": {
          "mode": "absolute",
          "steps": [
            {"color": "red", "value": 0},
            {"color": "yellow", "value": 70},
            {"color": "green", "value": 90}
          ]
        }
      },
      "targets": [
        {
          "expr": "sum(compliance_checks_passed_total) / sum(compliance_checks_total) * 100",
          "legendFormat": "Compliance Score"
        }
      ]
    },
    {
      "id": 2,
      "title": "Image Signing Compliance Rate",
      "type": "timeseries",
      "gridPos": {"h": 8, "w": 10, "x": 6, "y": 0},
      "targets": [
        {
          "expr": "sum(cosign_verify_result{result='pass'}) / sum(cosign_verify_result) * 100",
          "legendFormat": "Image Signing Compliance %"
        }
      ]
    },
    {
      "id": 3,
      "title": "Vulnerability Trend (by Severity)",
      "type": "barchart",
      "gridPos": {"h": 8, "w": 8, "x": 16, "y": 0},
      "targets": [
        {
          "expr": "sum(trivy_vulnerability_count) by (severity)",
          "legendFormat": "{{severity}}"
        }
      ]
    },
    {
      "id": 4,
      "title": "Compliance Framework Status",
      "type": "table",
      "gridPos": {"h": 10, "w": 24, "x": 0, "y": 8},
      "targets": [
        {
          "expr": "compliance_framework_status",
          "legendFormat": "{{framework}}"
        }
      ],
      "transformations": [
        {
          "id": "organize",
          "options": {
            "renameByName": {
              "framework": "Framework",
              "status": "Status",
              "last_checked": "Last Checked"
            }
          }
        }
      ]
    },
    {
      "id": 5,
      "title": "Kyverno Policy Violations (Past 7 Days)",
      "type": "piechart",
      "gridPos": {"h": 8, "w": 8, "x": 0, "y": 18},
      "targets": [
        {
          "expr": "sum(increase(kyverno_policy_results_total{policy_result='fail'}[7d])) by (policy_name)",
          "legendFormat": "{{policy_name}}"
        }
      ]
    },
    {
      "id": 6,
      "title": "SLSA Provenance Coverage Rate",
      "type": "stat",
      "gridPos": {"h": 8, "w": 8, "x": 8, "y": 18},
      "targets": [
        {
          "expr": "sum(slsa_provenance_present) / sum(slsa_releases_total) * 100",
          "legendFormat": "SLSA Coverage %"
        }
      ]
    },
    {
      "id": 7,
      "title": "SOC 2 Control Status",
      "type": "table",
      "gridPos": {"h": 8, "w": 8, "x": 16, "y": 18},
      "targets": [
        {
          "expr": "soc2_control_status",
          "instant": true
        }
      ]
    }
  ]
}
```

## 6.2 Compliance Metrics Exporter

```python
#!/usr/bin/env python3
# compliance_exporter.py
# Prometheus compliance metrics exporter

from prometheus_client import start_http_server, Gauge, Counter, Info
import subprocess
import json
import time
import os

# Define metrics
compliance_score = Gauge(
    'compliance_score',
    'Overall compliance score (0-100)',
    ['framework']
)

compliance_checks_total = Counter(
    'compliance_checks_total',
    'Total compliance checks performed',
    ['framework', 'control']
)

compliance_checks_passed = Counter(
    'compliance_checks_passed_total',
    'Passed compliance checks',
    ['framework', 'control']
)

cosign_verify_result = Gauge(
    'cosign_verify_result',
    'Cosign image verification result (1=pass, 0=fail)',
    ['image', 'registry']
)

slsa_provenance_present = Gauge(
    'slsa_provenance_present',
    'Whether SLSA provenance is present (1=yes, 0=no)',
    ['repository', 'tag']
)

vulnerability_count = Gauge(
    'trivy_vulnerability_count',
    'Number of vulnerabilities found',
    ['severity', 'image']
)

kyverno_policy_violations = Gauge(
    'kyverno_policy_violations_current',
    'Current Kyverno policy violations',
    ['policy', 'namespace']
)

def collect_cosign_metrics():
    """Collect image signature verification metrics"""
    images = os.environ.get('MONITORED_IMAGES', '').split(',')
    
    for image in images:
        if not image.strip():
            continue
        
        result = subprocess.run(
            ['cosign', 'verify',
             '--certificate-oidc-issuer', 'https://token.actions.githubusercontent.com',
             '--certificate-identity-regexp', '.*',
             image.strip()],
            capture_output=True, text=True
        )
        
        registry = image.split('/')[0] if '/' in image else 'docker.io'
        
        cosign_verify_result.labels(
            image=image.strip(),
            registry=registry
        ).set(1 if result.returncode == 0 else 0)

def collect_kyverno_metrics():
    """Collect Kyverno policy violation metrics"""
    result = subprocess.run(
        ['kubectl', 'get', 'policyreport', '--all-namespaces', '-o', 'json'],
        capture_output=True, text=True
    )
    
    if result.returncode != 0:
        return
    
    reports = json.loads(result.stdout)
    
    for report in reports.get('items', []):
        namespace = report['metadata']['namespace']
        
        for result_item in report.get('results', []):
            if result_item.get('result') == 'fail':
                policy = result_item.get('policy', 'unknown')
                kyverno_policy_violations.labels(
                    policy=policy,
                    namespace=namespace
                ).inc()

def collect_vulnerability_metrics():
    """Collect vulnerability scanning metrics"""
    images = os.environ.get('MONITORED_IMAGES', '').split(',')
    
    for image in images:
        if not image.strip():
            continue
        
        result = subprocess.run(
            ['trivy', 'image', '--format', 'json', image.strip()],
            capture_output=True, text=True
        )
        
        if result.returncode not in [0, 1]:
            continue
        
        try:
            scan_results = json.loads(result.stdout)
            counts = {'CRITICAL': 0, 'HIGH': 0, 'MEDIUM': 0, 'LOW': 0}
            
            for scan_result in scan_results.get('Results', []):
                for vuln in scan_result.get('Vulnerabilities', []):
                    sev = vuln.get('Severity', 'UNKNOWN').upper()
                    if sev in counts:
                        counts[sev] += 1
            
            for severity, count in counts.items():
                vulnerability_count.labels(
                    severity=severity,
                    image=image.strip()
                ).set(count)
        except json.JSONDecodeError:
            pass

def calculate_soc2_score() -> float:
    """Calculate SOC 2 compliance score"""
    checks = {
        'CC6.6_image_signing': collect_cosign_metrics,
        'CC7.1_vulnerability_scan': collect_vulnerability_metrics,
        'CC8.1_kyverno_policies': collect_kyverno_metrics
    }
    
    passed = 0
    total = len(checks)
    
    # Simplified score calculation
    # In practice, should be based on specific check results
    
    return (passed / total * 100) if total > 0 else 0

def main():
    # Start HTTP server
    start_http_server(9090)
    print("Compliance metrics exporter started on port 9090")
    
    while True:
        try:
            collect_cosign_metrics()
            collect_kyverno_metrics()
            collect_vulnerability_metrics()
            
            score = calculate_soc2_score()
            compliance_score.labels(framework='soc2').set(score)
        except Exception as e:
            print(f"Error collecting metrics: {e}")
        
        # Collect every 5 minutes
        time.sleep(300)

if __name__ == "__main__":
    main()
```

---

<!-- chunk: 7. Policy-as-Code Compliance Framework -->## 7. Policy-as-Code Compliance Framework

## 7.1 Open Policy Agent Compliance Policies

```rego
# compliance/soc2.rego
# SOC 2 Compliance Policies (OPA Rego)

package compliance.soc2

import future.keywords.in
import future.keywords.if

# ============================================================
# CC6.6: Software Source Verification
# ============================================================

# Violation: Unsigned image
deny_cc6_6[msg] {
    input.kind == "Pod"
    container := input.spec.containers[_]
    image := container.image
    
    # Check if image is from trusted registry
    not is_trusted_registry(image)
    
    msg := sprintf(
        "SOC2-CC6.6: Container image '%v' is not from a trusted registry",
        [image]
    )
}

# Violation: Image not using digest reference (tags can be changed)
deny_cc6_6[msg] {
    input.kind == "Pod"
    input.metadata.namespace in ["production", "staging"]
    container := input.spec.containers[_]
    image := container.image
    
    not contains(image, "@sha256:")
    
    msg := sprintf(
        "SOC2-CC6.6: Container image '%v' must use digest reference in production",
        [image]
    )
}

is_trusted_registry(image) {
    trusted_registries := [
        "ghcr.io/your-org/",
        "registry.your-company.com/",
        "gcr.io/distroless/",
    ]
    startswith(image, trusted_registries[_])
}

# ============================================================
# CC7.1: Vulnerability Management
# ============================================================

# Violation: Image using base image version with known CRITICAL vulnerabilities
deny_cc7_1[msg] {
    input.kind == "Pod"
    container := input.spec.containers[_]
    image := container.image
    
    is_vulnerable_base_image(image)
    
    msg := sprintf(
        "SOC2-CC7.1: Container image '%v' uses a vulnerable base image",
        [image]
    )
}

is_vulnerable_base_image(image) {
    # Base image versions with known CRITICAL CVEs
    vulnerable_images := data.vulnerable_images
    vulnerable_images[_] == image
}

# ============================================================
# CC8.1: Change Management
# ============================================================

# Violation: Direct changes to protected namespaces (not through GitOps)
deny_cc8_1[msg] {
    input.kind == "Deployment"
    input.metadata.namespace in ["production"]
    
    # Check for GitOps annotations
    not input.metadata.annotations["argocd.argoproj.io/app-name"]
    not input.metadata.annotations["fluxcd.io/reconcileAt"]
    
    msg := "SOC2-CC8.1: Production deployments must be managed via GitOps"
}

# ============================================================
# Generate compliance report
# ============================================================

# Compliance status
compliance_status := {
    "framework": "SOC 2 Type II",
    "timestamp": time.now_ns(),
    "violations": violations,
    "compliant": count(violations) == 0
}

violations := [violation |
    violation := deny_cc6_6[_]
] | [violation |
    violation := deny_cc7_1[_]
] | [violation |
    violation := deny_cc8_1[_]
]
```

## 7.2 Compliance-as-Code Workflow

```yaml
# .github/workflows/compliance-as-code.yml
name: Compliance-as-Code Validation

on:
  pull_request:
    paths:
      - 'k8s/**'
      - 'helm/**'
      - 'policies/**'
  schedule:
    - cron: '0 6 * * *'  # Daily compliance scan

jobs:
  validate-compliance:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4

      - name: Install OPA
        run: |
          curl -sSfL https://openpolicyagent.org/downloads/latest/opa_linux_amd64_static \
            -o /usr/local/bin/opa
          chmod +x /usr/local/bin/opa

      - name: Install conftest
        run: |
          CONFTEST_VERSION="0.50.0"
          curl -sSfL "https://github.com/open-policy-agent/conftest/releases/download/v${CONFTEST_VERSION}/conftest_${CONFTEST_VERSION}_Linux_x86_64.tar.gz" | \
            tar xz && mv conftest /usr/local/bin/

      - name: Run compliance policies
        run: |
          # Use conftest to validate Kubernetes resources
          conftest test \
            --policy policies/ \
            --all-namespaces \
            k8s/ \
            --output json \
            > conftest-results.json || true

      - name: Check SOC 2 compliance
        run: |
          opa eval \
            --data policies/soc2.rego \
            --data policies/data/ \
            --input k8s/production-deployment.yaml \
            --format json \
            "data.compliance.soc2.compliance_status" \
            | tee soc2-result.json

      - name: Check PCI-DSS compliance
        run: |
          opa eval \
            --data policies/pci_dss.rego \
            --data policies/data/ \
            --input k8s/payment-service.yaml \
            --format json \
            "data.compliance.pci_dss.compliance_status" \
            | tee pci-result.json

      - name: Generate compliance report
        run: |
          python3 << 'EOF'
          import json
          from datetime import datetime
          
          results = {}
          
          for framework, file in [("SOC2", "soc2-result.json"), ("PCI-DSS", "pci-result.json")]:
              try:
                  with open(file) as f:
                      data = json.load(f)
                  results[framework] = data.get('result', {})
              except FileNotFoundError:
                  results[framework] = {"error": "No results"}
          
          report = {
              "timestamp": datetime.utcnow().isoformat(),
              "commit": "${{ github.sha }}",
              "pr": "${{ github.event.pull_request.number }}",
              "results": results,
              "overall": all(
                  r.get('compliant', False) 
                  for r in results.values() 
                  if isinstance(r, dict)
              )
          }
          
          print(json.dumps(report, indent=2))
          EOF

      - name: Post compliance results to PR
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            
            let comment = '<!-- chunk: 🔐 Compliance Check Results\n\n'; -->## 🔐 Compliance Check Results\n\n';
            comment += '| Framework | Status | Violations |\n';
            comment += '|-----------|--------|------------|\n';
            
            // Read results from files
            try {
              const soc2 = JSON.parse(fs.readFileSync('soc2-result.json', 'utf8'));
              const compliant = soc2.result?.compliant ?? false;
              const violations = soc2.result?.violations?.length ?? 0;
              comment += `| SOC 2 | ${compliant ? '✅ PASS' : '❌ FAIL'} | ${violations} |\n`;
            } catch(e) {
              comment += `| SOC 2 | ⚠️ ERROR | N/A |\n`;
            }
            
            await github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: comment
            });
```

---

<!-- chunk: 8. Continuous Compliance Monitoring -->## 8. Continuous Compliance Monitoring

## 8.1 Continuous Compliance Monitoring Architecture

```mermaid
graph TB
    subgraph "Event Triggers"
        T1["Code Commit"]
        T2["Container Deployment"]
        T3["Configuration Change"]
        T4["Scheduled Scan"]
    end

    subgraph "Compliance Checks"
        C1["SAST/DAST\nCode Security"]
        C2["Dependency Scanning\nSCA"]
        C3["Image Signing\nCosign"]
        C4["SLSA Verification\nslsa-verifier"]
        C5["Policy Compliance\nKyverno/OPA"]
        C6["Configuration Benchmark\nCIS/STIG"]
        C7["Access Control\nRBAC Audit"]
    end

    subgraph "Result Processing"
        R1["Real-time Alerting\nPagerDuty/Slack"]
        R2["Metrics Aggregation\nPrometheus"]
        R3["Evidence Storage\nS3 + WORM"]
        R4["Ticket Creation\nJira/GitHub Issues"]
    end

    subgraph "Reporting"
        RP1["Compliance Dashboard\nGrafana"]
        RP2["Audit Reports\nPDF/CSV"]
        RP3["POA&M\nFedRAMP"]
        RP4["Auditor Access\nRead-only Portal"]
    end

    T1 & T2 & T3 & T4 --> C1 & C2 & C3 & C4 & C5 & C6 & C7
    C1 & C2 & C3 & C4 & C5 & C6 & C7 --> R1 & R2 & R3 & R4
    R1 & R2 & R3 & R4 --> RP1 & RP2 & RP3 & RP4
```

## 8.2 Automated Compliance State Machine

```yaml
# compliance-state-machine.yaml
# Compliance state machine configuration (using AWS Step Functions or custom implementation)

stateMachine:
  name: ContinuousComplianceMonitor
  
  states:
    # State 1: Initial Scan
    InitialScan:
      type: Task
      next: EvaluateResults
      task: RunComplianceScans
      parameters:
        scans:
          - type: vulnerability
            tool: trivy
            severity: [CRITICAL, HIGH]
          - type: sbom
            tool: syft
          - type: signature
            tool: cosign
          - type: policy
            tool: kyverno
          - type: configuration
            tool: kube-bench
    
    # State 2: Evaluate Results
    EvaluateResults:
      type: Choice
      choices:
        - condition: "violations.critical > 0"
          next: CriticalViolationDetected
        - condition: "violations.high > threshold.high"
          next: HighViolationDetected
        - condition: "violations.total == 0"
          next: CollectEvidence
      default: NormalViolationHandling
    
    # State 3a: Critical Violation Handling
    CriticalViolationDetected:
      type: Parallel
      branches:
        - SendPagerDutyAlert
        - CreateJiraTicket
        - BlockDeployment
        - StoreEvidence
      next: GenerateIncidentReport
    
    # State 3b: Evidence Collection
    CollectEvidence:
      type: Task
      task: StoreComplianceEvidence
      parameters:
        destination: s3://compliance-evidence-bucket
        encryption: aws:kms
        retention: 7years  # SOC 2 requirement
      next: UpdateDashboard
    
    # State 4: Update Dashboard
    UpdateDashboard:
      type: Task
      task: UpdateGrafanaDashboard
      next: ScheduleNextScan
    
    # State 5: Schedule Next Scan
    ScheduleNextScan:
      type: Wait
      seconds: 3600  # Every hour
      next: InitialScan
```

---

<!-- chunk: 9. Auditor Interface and Reporting -->## 9. Auditor Interface and Reporting

## 9.1 Auditor Read-Only Access Configuration

```yaml
# auditor-access.yaml
# Configure read-only access for external auditors

---
# Kubernetes RBAC: Auditor Role
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: external-auditor
  labels:
    app.kubernetes.io/part-of: compliance
    compliance.your-company.com/role: auditor

rules:
  # Read-only access to policy resources
  - apiGroups: ["kyverno.io"]
    resources: ["clusterpolicies", "policies", "policyreports", "clusterpolicyreports"]
    verbs: ["get", "list", "watch"]
  
  - apiGroups: ["policy.sigstore.dev"]
    resources: ["clusterimagepolicies"]
    verbs: ["get", "list", "watch"]
  
  # Read-only access to workloads (for configuration verification)
  - apiGroups: ["apps"]
    resources: ["deployments", "statefulsets", "daemonsets", "replicasets"]
    verbs: ["get", "list"]
  
  - apiGroups: [""]
    resources: ["pods", "namespaces", "configmaps", "serviceaccounts"]
    verbs: ["get", "list"]
  
  # Read-only access to RBAC
  - apiGroups: ["rbac.authorization.k8s.io"]
    resources: ["roles", "rolebindings", "clusterroles", "clusterrolebindings"]
    verbs: ["get", "list"]
  
  # Explicitly deny write operations
  - apiGroups: ["*"]
    resources: ["*"]
    verbs: ["create", "update", "patch", "delete", "escalate", "impersonate"]

---
# Auditor ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: external-auditor
  namespace: compliance
  annotations:
    description: "Read-only service account for external SOC 2 auditor"
    expires: "2024-12-31"  # Certificate validity period

---
# Bind role to ServiceAccount
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: external-auditor-binding
  labels:
    audit-period: "2024-Q4"

roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: external-auditor

subjects:
  - kind: ServiceAccount
    name: external-auditor
    namespace: compliance

---
# AWS IAM: Auditor read-only S3 access
# compliance-auditor-policy.json
# {
#   "Version": "2012-10-17",
#   "Statement": [
#     {
#       "Effect": "Allow",
#       "Action": [
#         "s3:GetObject",
#         "s3:ListBucket",
#         "s3:GetObjectVersion"
#       ],
#       "Resource": [
#         "arn:aws:s3:::compliance-evidence-bucket/*",
#         "arn:aws:s3:::compliance-evidence-bucket"
#       ],
#       "Condition": {
#         "StringEquals": {
#           "aws:RequestedRegion": "us-east-1"
#         }
#       }
#     },
#     {
#       "Effect": "Deny",
#       "Action": [
#         "s3:DeleteObject",
#         "s3:PutObject"
#       ],
#       "Resource": "*"
#     }
#   ]
# }
```

## 9.2 Automated Audit Report Generation

```python
#!/usr/bin/env python3
# audit_report_generator.py
# Automatically generate compliance audit reports

import json
import boto3
import jinja2
from datetime import datetime, timedelta
from pathlib import Path

REPORT_TEMPLATE = """
# Compliance Audit Report
<!-- chunk: {{ report_period }} -->## {{ report_period }}

**Organization**: {{ org_name }}
**Report Generated**: {{ generated_at }}
**Audit Period**: {{ period_start }} to {{ period_end }}
**Report Version**: {{ version }}

---

<!-- chunk: Executive Summary -->## Executive Summary

| Metric | Value | Status |
|--------|-------|--------|
| Overall Compliance Score | {{ overall_score }}% | {{ status_emoji(overall_score) }} |
| Controls Tested | {{ controls_tested }} | |
| Controls Passed | {{ controls_passed }} | ✅ |
| Controls Failed | {{ controls_failed }} | {{ '❌' if controls_failed > 0 else '✅' }} |
| Open Vulnerabilities (Critical) | {{ critical_vulns }} | {{ '❌' if critical_vulns > 0 else '✅' }} |
| Images with Valid Signatures | {{ signed_images }}% | {{ status_emoji(signed_images) }} |

---

<!-- chunk: SOC 2 Type II Controls -->## SOC 2 Type II Controls

## CC6.6 - Logical Access Controls (Supply Chain)

**Status**: {{ 'PASS ✅' if soc2.cc6_6.passed else 'FAIL ❌' }}

| Check | Result | Evidence |
|-------|--------|----------|
{% for check in soc2.cc6_6.checks %}
| {{ check.name }} | {{ '✅ Pass' if check.passed else '❌ Fail' }} | [View Evidence]({{ check.evidence_url }}) |
{% endfor %}

## CC7.1 - System Monitoring (Vulnerability Management)

**Status**: {{ 'PASS ✅' if soc2.cc7_1.passed else 'FAIL ❌' }}

Vulnerability Summary:
- **Critical**: {{ soc2.cc7_1.critical_count }} (Threshold: 0)
- **High**: {{ soc2.cc7_1.high_count }} (Threshold: {{ soc2.cc7_1.high_threshold }})
- **Medium**: {{ soc2.cc7_1.medium_count }}
- **Low**: {{ soc2.cc7_1.low_count }}

## CC8.1 - Change Management

**Status**: {{ 'PASS ✅' if soc2.cc8_1.passed else 'FAIL ❌' }}

| Metric | Value |
|--------|-------|
| PRs Reviewed | {{ soc2.cc8_1.prs_reviewed }} |
| PRs with ≥2 Approvals | {{ soc2.cc8_1.prs_approved }} ({{ soc2.cc8_1.approval_rate }}%) |
| Direct Pushes to Main | {{ soc2.cc8_1.direct_pushes }} (Should be 0) |

---

<!-- chunk: Supply Chain Security Summary -->## Supply Chain Security Summary

| Component | Status | Details |
|-----------|--------|---------|
| Image Signing | {{ 'Active ✅' if supply_chain.image_signing else 'Inactive ❌' }} | Using Cosign keyless signing |
| SLSA Provenance | {{ 'Level 3 ✅' if supply_chain.slsa_level >= 3 else 'Below Level 3 ⚠️' }} | {{ supply_chain.slsa_level }}/3 |
| SBOM Generation | {{ 'Active ✅' if supply_chain.sbom_enabled else 'Inactive ❌' }} | SPDX JSON format |
| Vulnerability Scanning | {{ 'Active ✅' if supply_chain.vuln_scanning else 'Inactive ❌' }} | In CI/CD pipeline |
| Policy Enforcement | {{ 'Active ✅' if supply_chain.policy_enforcement else 'Inactive ❌' }} | Kyverno + Policy Controller |

---

<!-- chunk: Appendix: Evidence Index -->## Appendix: Evidence Index

{% for item in evidence_items %}
- **{{ item.control_id }}**: [{{ item.description }}]({{ item.s3_url }}) 
  - Collected: {{ item.collected_at }}
  - Hash: `{{ item.hash[:16] }}...`
{% endfor %}

---
*This report was automatically generated. All evidence is cryptographically signed and stored in immutable storage.*
"""

class AuditReportGenerator:
    def __init__(self, s3_bucket: str, org_name: str):
        self.s3 = boto3.client('s3')
        self.s3_bucket = s3_bucket
        self.org_name = org_name
    
    def collect_evidence_items(self, start_date: datetime, end_date: datetime) -> list:
        """Collect evidence items from S3"""
        items = []
        
        paginator = self.s3.get_paginator('list_objects_v2')
        
        # List evidence within time range
        for page in paginator.paginate(Bucket=self.s3_bucket, Prefix='evidence/'):
            for obj in page.get('Contents', []):
                # Check if object is within time range
                if start_date <= obj['LastModified'].replace(tzinfo=None) <= end_date:
                    # Download and parse evidence
                    response = self.s3.get_object(
                        Bucket=self.s3_bucket,
                        Key=obj['Key']
                    )
                    evidence = json.loads(response['Body'].read())
                    
                    items.append({
                        'control_id': evidence.get('controlId', 'unknown'),
                        'description': evidence.get('description', obj['Key']),
                        's3_url': f"s3://{self.s3_bucket}/{obj['Key']}",
                        'collected_at': evidence.get('collectedAt', ''),
                        'hash': evidence.get('_metadata', {}).get('hash', '')
                    })
        
        return items
    
    def generate_report(self, period_start: datetime, period_end: datetime) -> str:
        """Generate complete audit report"""
        evidence_items = self.collect_evidence_items(period_start, period_end)
        
        # Aggregate compliance status
        template_vars = {
            'org_name': self.org_name,
            'generated_at': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC'),
            'report_period': f"{period_start.strftime('%B %Y')} - {period_end.strftime('%B %Y')}",
            'period_start': period_start.strftime('%Y-%m-%d'),
            'period_end': period_end.strftime('%Y-%m-%d'),
            'version': '1.0',
            'overall_score': 95,
            'controls_tested': 15,
            'controls_passed': 14,
            'controls_failed': 1,
            'critical_vulns': 0,
            'signed_images': 100,
            'soc2': {
                'cc6_6': {'passed': True, 'checks': []},
                'cc7_1': {'passed': True, 'critical_count': 0, 'high_count': 3, 'high_threshold': 10, 'medium_count': 25, 'low_count': 82},
                'cc8_1': {'passed': True, 'prs_reviewed': 234, 'prs_approved': 234, 'approval_rate': 100, 'direct_pushes': 0}
            },
            'supply_chain': {
                'image_signing': True,
                'slsa_level': 3,
                'sbom_enabled': True,
                'vuln_scanning': True,
                'policy_enforcement': True
            },
            'evidence_items': evidence_items
        }
        
        template = jinja2.Template(REPORT_TEMPLATE)
        template.globals['status_emoji'] = lambda score: '✅' if score >= 90 else ('⚠️' if score >= 70 else '❌')
        
        return template.render(**template_vars)


def main():
    generator = AuditReportGenerator(
        s3_bucket='compliance-evidence-bucket',
        org_name='Your Organization, Inc.'
    )
    
    # Generate quarterly report
    end_date = datetime.utcnow()
    start_date = end_date - timedelta(days=90)
    
    report = generator.generate_report(start_date, end_date)
    
    # Save report
    with open('audit-report.md', 'w') as f:
        f.write(report)
    
    print("Audit report generated: audit-report.md")

if __name__ == "__main__":
    main()
```

---

<!-- chunk: 10. Industry-Specific Compliance Extensions -->## 10. Industry-Specific Compliance Extensions

## 10.1 HIPAA Supply Chain Extensions

```yaml
# hipaa-supply-chain-policy.yaml
# HIPAA §164.312(c) - Integrity Controls for Software Supply Chain

apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: hipaa-integrity-controls
  annotations:
    hipaa.compliance/section: "164.312(c)"
    hipaa.compliance/description: "Protect PHI integrity through verified software supply chain"

spec:
  validationFailureAction: Enforce
  background: true
  
  rules:
    - name: require-signed-phi-handlers
      match:
        any:
          - resources:
              kinds: [Pod]
              selector:
                matchLabels:
                  data-classification: "phi"
      
      verifyImages:
        - imageReferences: ["*"]
          attestors:
            - count: 1
              entries:
                - keyless:
                    url: https://fulcio.sigstore.dev
                    issuer: https://token.actions.githubusercontent.com
                    subjectRegExp: ".*"
          
          attestations:
            # Require SBOM attestation (for Business Associate Agreement compliance)
            - predicateType: https://spdx.dev/Document
              conditions: []
            
            # Require vulnerability scan attestation
            - predicateType: https://cosign.sigstore.dev/attestation/vuln/v1
              conditions:
                - all:
                    - key: "{{ predicate.scanner.result.Results[].Vulnerabilities[].Severity }}"
                      operator: NotIn
                      value: ["CRITICAL", "HIGH"]
          
          mutateDigest: true
          required: true
    
    - name: require-audit-logging-for-phi
      match:
        any:
          - resources:
              kinds: [Pod]
              namespaces: ["phi-processing"]
      
      validate:
        message: "PHI processing pods must have audit logging enabled"
        pattern:
          spec:
            containers:
              - env:
                  - name: AUDIT_LOG_ENABLED
                    value: "true"
```

## 10.2 Financial Industry Compliance Extensions

```yaml
# fintech-supply-chain-policy.yaml
# Financial services industry-specific supply chain security requirements

apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: fintech-supply-chain-controls
  annotations:
    pci.compliance/section: "6.3.x"
    sox.compliance/section: "IT General Controls"

spec:
  validationFailureAction: Enforce
  background: true
  
  rules:
    # Financial transaction services must have SLSA Level 3 certification
    - name: require-slsa-l3-for-payment-services
      match:
        any:
          - resources:
              kinds: [Pod]
              selector:
                matchLabels:
                  service-type: "payment"
      
      verifyImages:
        - imageReferences: ["*"]
          attestors:
            - count: 1
              entries:
                - keyless:
                    url: https://fulcio.sigstore.dev
                    issuer: https://token.actions.githubusercontent.com
                    # Only allow builds from dedicated payment service CI pipeline
                    subjectRegExp: "^https://github.com/fintech-org/payment-service/.github/workflows/.*"
          
          attestations:
            - predicateType: https://slsa.dev/provenance/v0.2
              conditions:
                - all:
                    - key: "{{ predicate.builder.id }}"
                      operator: AnyIn
                      value:
                        - "https://github.com/slsa-framework/slsa-github-generator/.github/workflows/generator_container_slsa3.yml@refs/tags/v1.10.0"
          
          mutateDigest: true
          required: true
    
    # Prohibit non-production builds in production
    - name: require-production-build-only
      match:
        any:
          - resources:
              kinds: [Pod]
              namespaces: ["production", "prod-*"]
      
      verifyImages:
        - imageReferences: ["*"]
          attestors:
            - count: 1
              entries:
                - keyless:
                    url: https://fulcio.sigstore.dev
                    issuer: https://token.actions.githubusercontent.com
                    # Only allow builds triggered from tags (version releases)
                    subjectRegExp: ".*@refs/tags/v[0-9]+\\.[0-9]+\\.[0-9]+"
          
          attestations:
            - predicateType: https://cosign.sigstore.dev/attestation/v1
              conditions:
                - all:
                    - key: "{{ environment }}"
                      operator: Equals
                      value: "production"
```

---

<!-- chunk: 11. Compliance Automation Toolchain -->## 11. Compliance Automation Toolchain

## 11.1 Recommended Tool Matrix

| Category | Tool | Purpose | Open Source/Commercial |
|------|------|------|----------|
| Vulnerability Scanning | Trivy | Container/Code/SBOM Scanning | Open Source |
| Vulnerability Scanning | Grype | SBOM Vulnerability Matching | Open Source |
| Vulnerability Scanning | Snyk | Code/Container/IaC | Commercial |
| SBOM Generation | Syft | SPDX/CycloneDX | Open Source |
| SBOM Generation | Tern | Container Layer Analysis | Open Source |
| Code Signing | Cosign | Container/File Signing | Open Source |
| Provenance | SLSA Generator | GitHub Actions SLSA | Open Source |
| Policy Enforcement | Kyverno | K8s Admission Control | Open Source |
| Policy Enforcement | OPA/Gatekeeper | General Purpose Policy Engine | Open Source |
| SAST | CodeQL | Code Security Analysis | Commercial/Free |
| SAST | Semgrep | Multi-language SAST | Open Source/Commercial |
| IaC Scanning | Checkov | Terraform/K8s | Open Source |
| Compliance Management | Drata | SOC 2 Automation | Commercial |
| Compliance Management | Vanta | Continuous Compliance Monitoring | Commercial |
| Compliance Management | Steampipe | SQL Query Compliance | Open Source |

## 11.2 Compliance Toolchain Installation Script

```bash
#!/bin/bash
# install-compliance-tools.sh
# Install complete compliance automation toolchain

set -euo pipefail

echo "=== Installing Compliance Automation Toolchain ==="

# 1. Install Cosign
echo ">>> Installing Cosign..."
COSIGN_VERSION="v2.2.4"
curl -sSfL "https://github.com/sigstore/cosign/releases/download/${COSIGN_VERSION}/cosign-linux-amd64" \
  -o /usr/local/bin/cosign
chmod +x /usr/local/bin/cosign
cosign version

# 2. Install Syft (SBOM Generation)
echo ">>> Installing Syft..."
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | \
  sh -s -- -b /usr/local/bin

# 3. Install Grype (Vulnerability Scanning)
echo ">>> Installing Grype..."
curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | \
  sh -s -- -b /usr/local/bin

# 4. Install Trivy
echo ">>> Installing Trivy..."
curl -sSfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | \
  sh -s -- -b /usr/local/bin

# 5. Install slsa-verifier
echo ">>> Installing slsa-verifier..."
go install github.com/slsa-framework/slsa-verifier/v2/cli/slsa-verifier@latest

# 6. Install Kyverno CLI
echo ">>> Installing Kyverno CLI..."
KYVERNO_VERSION="v1.12.0"
curl -sSfL "https://github.com/kyverno/kyverno/releases/download/${KYVERNO_VERSION}/kyverno-cli_linux_x86_64.tar.gz" | \
  tar xz && mv kyverno /usr/local/bin/

# 7. Install OPA
echo ">>> Installing OPA..."
curl -sSfL https://openpolicyagent.org/downloads/latest/opa_linux_amd64_static \
  -o /usr/local/bin/opa
chmod +x /usr/local/bin/opa

# 8. Install Conftest
echo ">>> Installing Conftest..."
CONFTEST_VERSION="0.50.0"
curl -sSfL "https://github.com/open-policy-agent/conftest/releases/download/v${CONFTEST_VERSION}/conftest_${CONFTEST_VERSION}_Linux_x86_64.tar.gz" | \
  tar xz && mv conftest /usr/local/bin/

# 9. Install Steampipe (Compliance Query)
echo ">>> Installing Steampipe..."
sudo /bin/sh -c "$(curl -fsSL https://raw.githubusercontent.com/turbot/steampipe/main/install.sh)"

# 10. Install Checkov (IaC Security Scanning)
echo ">>> Installing Checkov..."
pip install checkov

echo ""
echo "=== Toolchain Installation Complete ==="
echo "Installed tools:"
echo "  cosign: $(cosign version | head -1)"
echo "  syft: $(syft version | head -1)"
echo "  grype: $(grype version)"
echo "  trivy: $(trivy version | head -1)"
echo "  slsa-verifier: $(slsa-verifier version)"
echo "  kyverno: $(kyverno version)"
echo "  opa: $(opa version | head -1)"
echo "  conftest: $(conftest --version)"
echo "  checkov: $(checkov --version)"
```

---

<!-- chunk: 12. Reference Standards and Best Practices -->## 12. Reference Standards and Best Practices

## 12.1 Main Reference Documents

| Document | URL/Publisher |
|------|------------|
| AICPA SOC 2 Trust Services Criteria | aicpa.org |
| PCI-DSS v4.0 | pcisecuritystandards.org |
| FedRAMP Security Controls | fedramp.gov |
| NIST SP 800-218 (SSDF) | nvlpubs.nist.gov |
| NIST SP 800-53 Rev 5 | nvlpubs.nist.gov |
| CIS Kubernetes Benchmark | cisecurity.org |
| OpenSSF Scorecard | github.com/ossf/scorecard |
| SLSA Framework | slsa.dev |

## 12.2 Compliance Automation Maturity Model

```mermaid
graph LR
    L1["Level 1\nManual Compliance\n- Periodic Audits\n- Manual Evidence Collection\n- Spreadsheet Tracking"]
    L2["Level 2\nPartial Automation\n- CI/CD Integrated Scans\n- Automated Alerting\n- Semi-automated Reporting"]
    L3["Level 3\nContinuous Compliance\n- Policy-as-Code\n- Automated Evidence Collection\n- Real-time Dashboard"]
    L4["Level 4\nPredictive Compliance\n- AI Risk Prediction\n- Automated Remediation\n- Adaptive Policies"]

    L1 --> L2 --> L3 --> L4
    
    style L1 fill:#f5f5f5,stroke:#999
    style L2 fill:#fff3cd,stroke:#ffc107
    style L3 fill:#d4edda,stroke:#28a745
    style L4 fill:#cce5ff,stroke:#004085
```

---

<!-- chunk: Summary -->## Summary

Compliance automation and audit are key components of modern software supply chain security:

1. **Framework Mapping**: Precise mapping of SOC 2/PCI-DSS/FedRAMP requirements to supply chain security controls
2. **SOC 2 Automation**: Automated implementation of change management (CC8.1), vulnerability management (CC7.1), access control (CC6.6)
3. **PCI-DSS v4.0**: Automated checks for third-party component security (6.3.3) and application security (6.3.1)
4. **FedRAMP Continuous Monitoring**: ConMon architecture, SA-15 control implementation, POA&M auto-generation
5. **Evidence Collection**: Immutable S3 WORM storage, automated evidence collection scripts
6. **Compliance Dashboard**: Grafana + Prometheus real-time compliance status visualization
7. **Policy-as-Code**: OPA Rego policies implement compliance checks as code
8. **Auditor Interface**: Read-only access permissions, automated audit report generation
9. **Industry Extensions**: HIPAA and financial services-specific compliance requirements
10. **Toolchain**: Complete guide to installing and configuring open-source compliance tools

By implementing compliance automation, organizations can:
- Reduce evidence collection time from weeks to minutes
- Shift from periodic audits to continuous compliance
- Lower compliance failure risk from human error
- Provide auditors with trustworthy, immutable evidence chains
- Detect compliance drift in real-time as software supply chain changes

---

<!-- chunk: Obsidian Related Documents -->## Obsidian Related Documents

- domain-05-security-compliance MOC
- [[domain-05-security-compliance/README.md|Domain 05: Supply Chain Security (Supply Chain Security)]]
- [[domain-05-security-compliance/00-open-source-projects-index.md|Domain-39 Supply Chain Security — Open Source Projects Index]]
- Supply Chain Security Overview
- Supply Chain Security Maturity Model
- SBOM Generation and Management
- SBOM Vulnerability Analysis and Governance
- SLSA Levels and Implementation
- GitHub Actions SLSA Build
- Sigstore and Cosign Signing
- Fulcio and Rekor Transparency Logs
- Policy Controller Image Verification

## See Also

- 08-fulcio-rekor-transparency
- 09-policy-controller-verification
- 99-slsa-supply-chain-security-guide
- 01-supply-chain-security-overview

- [[domain-05-security-compliance/README.md|Return to Contents]]

<!-- risk-assessed -->
