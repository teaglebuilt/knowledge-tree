---title: Security & Compliance Open Source Projects Index
description: Security & Compliance Open Source Projects Index
summary: Security & Compliance Open Source Projects Index
category: reference
tags:
- security
- compliance
- open-source
- index
- opa
- falco
tier: core
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All engineers
estimated_read_time: 5min
intent_queries:
- What is Security & Compliance Open Source Projects Index
- How to use Security & Compliance Open Source Projects Index
- Kubernetes 05 security compliance best practices
trigger_keywords:
- Security
- Compliance
- Open
- Source
- Projects
- Index
- security
- compliance
prerequisites:
- kubectl-basics
- rbac-basics
- tls-basics
- policy-basics
original_language: Chinese
authors:
- name: Dillan Teagle
  role: contributor
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/00-open-source-projects-index.md
---

> **Production Environment Security Warning**
>
> This document contains directly executable operational commands. Before executing, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have verified in a non-production environment. Command risk levels are marked: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state, but can usually be rolled back), 🟢 Low risk/read-only (information collection, no side effects).




# Security & Compliance Open Source Projects Index

> This index consolidates open source project information from the original three domains: `domain-7-security`, `domain-25-cloud-native-security`, and `domain-39-supply-chain-security`.

## Identity & Access

| Project | Type | Description | Documentation Location |
|------|------|------|----------|
| Vault | Secret Management | HashiCorp enterprise-grade Secret management | `01-identity-access/05-vault-enterprise-secrets-management.md` |
| cert-manager | Certificate Management | Kubernetes automatic TLS certificates | `06-compliance/99-cert-manager-tls-guide.md` |

## Runtime Security

| Project | Type | Description | Documentation Location |
|------|------|------|----------|
| [[Falco|Falco]] | Threat Detection | Cloud-native runtime security | `03-runtime-security/01-falco-cloud-native-security.md` |
| Sysdig | Security Monitoring | Container and system monitoring | `03-runtime-security/02-sysdig-enterprise-container-security.md` |
| Aqua | Container Security | Enterprise container security platform | `03-runtime-security/03-aqua-enterprise-container-security.md` |
| gVisor | Container Sandbox | User-space kernel sandbox | `03-runtime-security/17-gvisor-container-sandbox.md` |

## Policy Governance

| Project | Type | Description | Documentation Location |
|------|------|------|----------|
| OPA / Gatekeeper | Policy Engine | Universal policy enforcement | `04-policy-governance/09-opa-gatekeeper-policy.md` |
| Kyverno | Kubernetes Policy | Native Kubernetes policy management | `04-policy-governance/04-kyverno-enterprise-policy-management.md` |

## Supply Chain Security

| Project | Type | Description | Documentation Location |
|------|------|------|----------|
| Sigstore | Signature Verification | Open source software signing ecosystem | `05-supply-chain/07-sigstore-cosign-signing.md` |
| Cosign | Container Signing | Container image signing tool | `05-supply-chain/07-sigstore-cosign-signing.md` |
| SLSA | Standard | Software supply chain security levels | `05-supply-chain/05-slsa-levels-implementation.md` |
| Syft / Grype | SBOM/Scanning | Generate SBOM and scan for vulnerabilities | `05-supply-chain/03-sbom-generation-management.md` |

## Original Index References

See detailed indexes:
- `98-merged-indexes/00-open-source-projects-index-from-domain-7.md`
- `98-merged-indexes/00-open-source-projects-index-from-domain-25.md`
- `98-merged-indexes/00-open-source-projects-index-from-domain-39.md`

## Related

- [[domain-05-security-compliance/README.md|Back to index]]
- [[domain-19-landscape-references/topic-index/pvc-index.md|PVC Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/etcd-index.md|etcd Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Graph Index]]
- [[domain-19-landscape-references/topic-index/gitops-cicd-index.md|GitOps / CI-CD Global Index]]


<!-- risk-assessed -->
