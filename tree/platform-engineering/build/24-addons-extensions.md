---
title: Security & Compliance Management
description: '# Security & Compliance Management'
summary: 'Security and compliance management is a foundational requirement for platform operations. By implementing zero-trust security architecture, continuous security monitoring, and compliance checks, we ensure the secure and stable operation of the Kubernetes platform. This document, from a Chief Security Officer (CSO) perspective, provides an in-depth analysis of enterprise-grade security compliance systems, implementation strategies, and combines financial-grade security standards with regulatory compliance requirements to provide professional guidance for building world-class secure platforms.'
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- etcd
- apiserver
- kubelet
- istio
- harbor
- falco
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Platform Engineers
- Operations Engineers
estimated_read_time: 5min
intent_queries:
- What is Security & Compliance Management
- How to implement Security & Compliance Management
- Kubernetes platform ops best practices
trigger_keywords:
- Security and Compliance Management
- Security
- Compliance
- Management
- platform
- ops
prerequisites:
- kubectl-basics
- platform-engineering-basics
- service-mesh-basics
- etcd-basics
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
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./governance/10-security-compliance.md
original_language: Chinese
---

> **Production Environment Security Notice**
>
> This document contains directly executable operational commands. Before executing, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether it has been verified in non-production environments. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state, but usually reversible), 🟢 Low Risk/Read-only (information gathering, no side effects).




# Security & Compliance Management ([[domain-07-platform-engineering/governance/10-security-compliance.md|Security & Compliance]] Management)

> **Applicable Versions**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **Document Version**: v2.0 | **Last Updated**: 2026-02
> **Professional Level**: Enterprise Production Environment | **Author**: Allen Galler

<!-- chunk: Overview -->
## Overview

Security and compliance management is a foundational requirement for platform operations. By implementing zero-trust security architecture, continuous security monitoring, and compliance checks, we ensure the secure and stable operation of the Kubernetes platform. This document, from a Chief Security Officer (CSO) perspective, provides an in-depth analysis of enterprise-grade security compliance systems, implementation strategies, and combines financial-grade security standards with regulatory compliance requirements to provide professional guidance for building world-class secure platforms.

---

<!-- chunk: Zero Trust Security Architecture -->
## Zero Trust Security Architecture

### Core Principles
```
Never Trust, Always Verify
```

### Security Layer Model
```
Identity Authentication → Access Authorization → Network Isolation → Data Protection → Continuous Monitoring
```

<!-- chunk: Identity Authentication and Authorization -->
## Identity Authentication and Authorization

### OIDC Integration Configuration
```yaml
# Dex OAuth2 Configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: dex
  namespace: auth
spec:
  replicas: 2
  selector:
    matchLabels:
      app: dex
  template:
    metadata:
      labels:
        app: dex
    spec:
      containers:
      - name: dex
        image: dexidp/dex:v2.37.0
        ports:
        - containerPort: 5556
        args:
        - dex
        - serve
        - /etc/dex/config.yaml
        volumeMounts:
        - name: config
          mountPath: /etc/dex
      volumes:
      - name: config
        configMap:
          name: dex-config

---
# Dex Configuration File
issuer: https://dex.example.com
storage:
  type: kubernetes
  config:
    inCluster: true
web:
  http: 0.0.0.0:5556
connectors:
- type: ldap
  name: LDAP
  id: ldap
  config:
    host: ldap.example.com:636
    insecureNoSSL: false
    bindDN: cn=admin,dc=example,dc=com
    bindPW: password
    usernamePrompt: Username
    userSearch:
      baseDN: ou=People,dc=example,dc=com
      filter: "(objectClass=person)"
      username: uid
      idAttr: uid
      emailAttr: mail
      nameAttr: cn
```

### Fine-Grained RBAC Permissions
```yaml
# Namespace Administrator Role
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: namespace-admin
  namespace: production
rules:
- apiGroups: [""]
  resources: ["pods", "services", "configmaps", "secrets"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
- apiGroups: ["apps"]
  resources: ["deployments", "statefulsets", "daemonsets"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
- apiGroups: ["networking.k8s.io"]
  resources: ["networkpolicies", "ingresses"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]

---
# Role Binding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: team-a-admin
  namespace: production
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: namespace-admin
subjects:
- kind: Group
  name: team-a-admins
  apiGroup: rbac.authorization.k8s.io
```

### Service Account Management
```yaml
# Restrictive Service Account
apiVersion: v1
kind: ServiceAccount
metadata:
  name: restricted-sa
  namespace: production
automountServiceAccountToken: false

---
# Pod Security Context
apiVersion: v1
kind: Pod
metadata:
  name: secure-pod
spec:
  serviceAccountName: restricted-sa
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    fsGroup: 2000
  containers:
  - name: app
    image: myapp:latest
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
```

<!-- chunk: Network Security Policy -->
## Network Security Policy

### NetworkPolicy Configuration
```yaml
# Default Deny-All Policy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress

---
# Allow Specific Traffic
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-backend-to-database
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: database
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: backend
    ports:
    - protocol: TCP
      port: 5432

---
# External Access Control
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-ingress-controller
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: frontend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: ingress-nginx
    ports:
    - protocol: TCP
      port: 80
    - protocol: TCP
      port: 443
```

### Istio Service Mesh Security
```yaml
# PeerAuthentication Mutual TLS
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: istio-system
spec:
  mtls:
    mode: STRICT

---
# AuthorizationPolicy Access Control
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: frontend-policy
  namespace: production
spec:
  selector:
    matchLabels:
      app: frontend
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/production/sa/backend-sa"]
    to:
    - operation:
        methods: ["GET", "POST"]
        paths: ["/api/*"]
  - when:
    - key: request.auth.claims[groups]
      values: ["admin"]
```

<!-- chunk: Image Security Management -->
## Image Security Management

### Harbor Private Image Registry
```yaml
# Harbor Deployment Configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: harbor-core
  namespace: harbor
spec:
  replicas: 2
  selector:
    matchLabels:
      app: harbor
      component: core
  template:
    metadata:
      labels:
        app: harbor
        component: core
    spec:
      containers:
      - name: core
        image: goharbor/harbor-core:v2.8.0
        env:
        - name: CORE_SECRET
          valueFrom:
            secretKeyRef:
              name: harbor-core-secret
              key: secret
        - name: JOBSERVICE_SECRET
          valueFrom:
            secretKeyRef:
              name: harbor-jobservice-secret
              key: secret
        ports:
        - containerPort: 8080
        livenessProbe:
          httpGet:
            path: /api/v2.0/ping
            port: 8080
          initialDelaySeconds: 300
          periodSeconds: 10
```

### Image Scanning Strategy
```yaml
# Trivy Scanning Configuration
apiVersion: batch/v1
kind: CronJob
metadata:
  name: image-scanner
  namespace: security
spec:
  schedule: "0 2 * * *"  # Execute daily at 2 AM
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: trivy
            image: aquasec/trivy:0.40.0
            command:
            - /bin/sh
            - -c
            - |
              trivy image --exit-code 1 --severity HIGH,CRITICAL \
                --ignore-unfixed $IMAGE_NAME
            env:
            - name: IMAGE_NAME
              valueFrom:
                configMapKeyRef:
                  name: scan-targets
                  key: image-list
          restartPolicy: OnFailure
```

### Image Signature Verification
```yaml
# Cosign Signature Policy
apiVersion: policy.sigstore.dev/v1alpha1
kind: ClusterImagePolicy
metadata:
  name: image-policy
spec:
  images:
  - glob: "registry.example.com/**"
  authorities:
  - key:
      kms: gcpkms://projects/my-project/locations/global/keyRings/my-ring/cryptoKeys/my-key
    attestations:
    - name: custom
      predicateType: custom
      policy:
        type: cue
        data: |
          predicateType: "cosign.sigstore.dev/attestation/v1"
          subject:
            name: string
```

<!-- chunk: Key Management -->
## Key Management

### HashiCorp Vault Integration
```yaml
# Vault Agent Injector Configuration
apiVersion: apps/v1
kind: Deployment
metadata:
  name: vault-agent-demo
spec:
  replicas: 2
  selector:
    matchLabels:
      app: vault-agent-demo
  template:
    metadata:
      annotations:
        vault.hashicorp.com/agent-inject: "true"
        vault.hashicorp.com/role: "app-role"
        vault.hashicorp.com/agent-inject-secret-database-config.txt: "secret/database/config"
        vault.hashicorp.com/agent-inject-template-database-config.txt: |
          {{- with secret "secret/database/config" -}}
          username: {{ .Data.username }}
          password: {{ .Data.password }}
          {{- end }}
      labels:
        app: vault-agent-demo
    spec:
      serviceAccountName: vault-agent
      containers:
      - name: app
        image: myapp:latest
        volumeMounts:
        - name: vault-secrets
          mountPath: /vault/secrets
          readOnly: true
```

### SealedSecrets Encryption
```yaml
# SealedSecret Creation
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  name: database-credentials
  namespace: production
spec:
  encryptedData:
    username: AgCQX1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/=
    password: AgCQX1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+/=
  template:
    metadata:
      name: database-credentials
      namespace: production
    data:
      username: ""
      password: ""
```

<!-- chunk: Compliance Checking -->
## Compliance Checking

### CIS Benchmark Scanning
```yaml
# kube-bench Configuration
apiVersion: batch/v1
kind: Job
metadata:
  name: cis-benchmark
  namespace: security
spec:
  template:
    spec:
      hostPID: true
      containers:
      - name: kube-bench
        image: aquasec/kube-bench:0.6.12
        command: ["kube-bench", "run", "--targets", "node,master,etcd,policies"]
        volumeMounts:
        - name: var-lib-etcd
          mountPath: /var/lib/etcd
          readOnly: true
        - name: var-lib-kubelet
          mountPath: /var/lib/kubelet
          readOnly: true
        - name: etc-systemd
          mountPath: /etc/systemd
          readOnly: true
        - name: etc-kubernetes
          mountPath: /etc/kubernetes
          readOnly: true
      volumes:
      - name: var-lib-etcd
        hostPath:
          path: "/var/lib/etcd"
      - name: var-lib-kubelet
        hostPath:
          path: "/var/lib/kubelet"
      - name: etc-systemd
        hostPath:
          path: "/etc/systemd"
      - name: etc-kubernetes
        hostPath:
          path: "/etc/kubernetes"
      restartPolicy: Never
```

### Security Baseline Check
``` bash
# 🟢 Low Risk: Read-only/information gathering, typically no side effects
# Security Configuration Check Script
#!/bin/bash

echo "=== Kubernetes Security Baseline Check ==="

# Check anonymous access
echo "1. Checking anonymous access..."
if kubectl get --raw='/healthz?verbose' | grep -q "anon"; then
    echo "❌ Anonymous access enabled"
else
    echo "✅ Anonymous access disabled"
fi

# Check RBAC status
echo "2. Checking RBAC status..."
if kubectl api-versions | grep -q "rbac.authorization.k8s.io"; then
    echo "✅ RBAC enabled"
else
    echo "❌ RBAC not enabled"
fi

# Check network policies
echo "3. Checking network policies..."
np_count=$(kubectl get networkpolicies --all-namespaces --no-headers | wc -l)
if $np_count -gt 0; then
    echo "✅ Network policies configured ($np_count policies)"
else
    echo "❌ No network policies found"
fi

# Check Pod security
echo "4. Checking Pod security..."
kubectl get pods --all-namespaces -o json | jq -r '
  .items[] | 
  select(.spec.containers[].securityContext.privileged == true) |
  "\(.metadata.namespace)/\(.metadata.name) - privileged container"
'
```
<!-- chunk: Security Monitoring and Alerting -->
## Security Monitoring and Alerting

### Falco Intrusion Detection
```yaml
# Falco Configuration
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: falco
  namespace: security
spec:
  selector:
    matchLabels:
      app: falco
  template:
    metadata:
      labels:
        app: falco
    spec:
      containers:
      - name: falco
        image: falcosecurity/falco:0.35.0
        securityContext:
          privileged: true
        volumeMounts:
        - name: dev-fs
          mountPath: /dev
        - name: proc-fs
          mountPath: /proc
        - name: boot-fs
          mountPath: /boot
        - name: lib-modules
          mountPath: /lib/modules
        - name: usr-fs
          mountPath: /usr
        - name: etc-fs
          mountPath: /etc
        env:
        - name: SYSDIG_BPF_PROBE
          value: ""
        - name: FALCO_FRONTEND
          value: "noninteractive"
      volumes:
      - name: dev-fs
        hostPath:
          path: /dev
      - name: proc-fs
        hostPath:
          path: /proc
      - name: boot-fs
        hostPath:
          path: /boot
      - name: lib-modules
        hostPath:
          path: /lib/modules
      - name: usr-fs
        hostPath:
          path: /usr
      - name: etc-fs
        hostPath:
          path: /etc
```

### Security Event Alerting
```yaml
# Security Alert Rules
groups:
- name: security.rules
  rules:
  - alert: HighPrivilegeContainer
    expr: kube_pod_container_info{container_security_context_privileged="true"} == 1
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "Privileged container detected"
      description: "Pod {{ $labels.pod }} in namespace {{ $labels.namespace }} contains a privileged container"

  - alert: UnauthorizedAccess
    expr: rate(apiserver_request_total{code=~"4.."}[5m]) > 10
    for: 10m
    labels:
      severity: warning
    annotations:
      summary: "API Server unauthorized access"
      description: "Large number of 4xx error requests detected"

  - alert: FailedLoginAttempts
    expr: rate(authentication_attempts{result="failure"}[5m]) > 5
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "Excessive authentication failures"
      description: "Frequent authentication failure attempts detected"
```

<!-- chunk: Audit Log Management -->
## Audit Log Management

### Audit Policy Configuration
```yaml
# Audit Policy
apiVersion: audit.k8s.io/v1
kind: Policy
rules:
- level: Metadata
  resources:
  - group: ""
    resources: ["secrets", "configmaps"]
  - group: authentication.k8s.io
    resources: ["tokenreviews"]
  verbs: ["create", "update", "delete"]

- level: RequestResponse
  resources:
  - group: ""
    resources: ["pods", "services", "deployments"]
  verbs: ["create", "update", "delete"]

- level: None
  users: ["system:kube-proxy"]
  verbs: ["watch"]

- level: None
  userGroups: ["system:authenticated"]
  nonResourceURLs:
  - "/api*"
  - "/version"
```

### Audit Log Analysis
```python
# Audit Log Analysis Script
import json
from datetime import datetime, timedelta

class AuditAnalyzer:
    def __init__(self, log_file):
        self.log_file = log_file
        self.suspicious_patterns = [
            self.detect_privilege_escalation,
            self.detect_unauthorized_access,
            self.detect_anomalous_behavior
        ]
    
    def analyze_logs(self):
        alerts = []
        with open(self.log_file, 'r') as f:
            for line in f:
                event = json.loads(line)
                for pattern in self.suspicious_patterns:
                    alert = pattern(event)
                    if alert:
                        alerts.append(alert)
        return alerts
    
    def detect_privilege_escalation(self, event):
        if (event.get('verb') == 'create' and 
            'rolebinding' in event.get('objectRef', {}).get('resource', '')):
            return {
                'type': 'privilege_escalation',
                'timestamp': event['requestReceivedTimestamp'],
                'user': event['user']['username'],
                'resource': event['objectRef']
            }
        return None
```

<!-- chunk: Best Practices -->
## Best Practices

### 1. Security Design Principles
- Principle of Least Privilege
- Defense in Depth Strategy
- Security Left-Shift Practice
- Zero Trust Architecture

### 2. Continuous Security Monitoring
- Real-time Threat Detection
- Anomalous Behavior Analysis
- Security Incident Response
- Vulnerability Management Process

### 3. Compliance Assurance
- Regular Security Audits
- Automated Compliance Checks
- Continuous Security Training
- Third-Party Security Assessments

### 4. Incident Response
- Security Incident Contingency Plans
- Rapid Response Mechanisms
- Damage Control Measures
- Post-Incident Review and Improvement

By establishing a comprehensive security and compliance management system, we can effectively prevent security threats, meet regulatory requirements, and provide a secure and reliable platform foundation for business development.

---

<!-- chunk: Obsidian Related Documents -->
## Obsidian Related Documents

- domain-07-platform-engineering KUDIG Database — Global MOC
- [[domain-07-platform-engineering/README.md|[[Platform Ops Domain (Platform Operations Domain)|Platform Ops Domain (Platform Operations Domain)]]]]
- index.md|Domain-9 Platform Operations — Open Source Project Index]]
- Platform Operations Overview
- Cluster Lifecycle Management
- Capacity Planning & Resource Assessment
- Performance Benchmarking & Tuning
- Operations Metrics System Construction
- Monitoring and Alerting System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization & FinOps Practice

## See Also

- 08-automation-toolchain
- 09-cost-optimization-finops
- 11-disaster-recovery-business-continuity
- 12-backup-recovery-strategy


<!-- risk-assessed -->