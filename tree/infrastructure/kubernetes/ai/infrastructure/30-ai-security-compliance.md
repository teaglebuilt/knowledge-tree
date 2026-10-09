---
title: AI Platform Security Hardening and Compliance
description: '# AI Platform Security Hardening and Compliance'
summary: 'requiredDuringSchedulingIgnoredDuringExecution:'
category: ai-infra
tags:
- k8s
- ai
- gpu
- ml
- training
- inference
- kubelet
- istio
- docker
- opa
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- MLOps Engineers
- SRE
estimated_read_time: 5min
intent_queries:
- What is AI Platform Security Hardening and Compliance
- How to do AI Platform Security Hardening and Compliance
- Kubernetes 11 ai infra best practices
trigger_keywords:
- AI Platform Security Hardening and Compliance
- ai
- infra
prerequisites:
- kubectl-basics
- service-mesh-basics
- gpu-scheduling-basics
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
  path: ../domain-02-workloads-applications/
  label: 'Related Knowledge Domain: domain-02-workloads-applications'
- type: domain
  path: ../domain-03-networking-traffic/
  label: 'Related Knowledge Domain: domain-03-networking-traffic'
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/go.md
  label: 'Quick Reference Card: go'
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/infrastructure/30-ai-security-compliance.md
---

> **Production Environment Security Reminders**
>
> Commands included in this document are executable directly. Before executing, please confirm: the target cluster and namespace are correct; you have sufficient RBAC permissions; and the commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High Risk (may result in data loss or service disruption), 🟡 Medium Risk (will modify cluster state but usually rollbackable), 🟢 Low Risk/Read-Only (information gathering with no side effects).




# AI Platform Security Hardening and Compliance

> **Applicable Version**: [[Kubernetes|Kubernetes]] v1.25 - v1.32 | **Last Updated**: 2026-02 | **Reference**: [NIST AI RMF](https://csrc.nist.gov/publications/detail/white-paper/2023/03/01/artificial-intelligence-risk-management-framework-ai-rmf-10/final) | [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)


## 1. AI Platform Security Architecture

### 1.1 Layered Security Protection System

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                          AI Platform Security Architecture                          │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                            Access Control Layer (Access Control)                            │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │   IAM       │  │   RBAC      │  │   ABAC      │  │   mTLS      │          │  │
│  │  │  (Identity) │  │ (Kubernetes)│  │ (Attribute) │  │ (Transport) │          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  │ • User Authentication   │  │ • Permission Control   │  │ • Attribute Policy   │  │ • Service-to-Service Encryption │          │  │
│  │  │ • Multi-Factor   │  │ • Role Separation   │  │ • Dynamic Authorization   │  │ • Certificate Rotation   │          │  │
│  │  │ • SSO Integration    │  │ • Least Privilege   │  │ • Context-Aware   │  │ • Bidirectional Authentication   │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └─────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                            Data Protection Layer (Data Protection)                            │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │   Encryption│  │   Masking   │  │   Auditing  │  │   Retention │          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  │ • Static Encryption   │  │ • Data Masking   │  │ • Auditing Operations   │  │ • Lifecycle   │          │  │
│  │  │ • Transport Encryption   │  │ • PII Protection    │  │ • Change Tracking   │  │ • Automatic Cleanup   │          │  │
│  │  │ • Key Management   │  │ • Tokenization    │  │ • Compliance Reporting   │  │ • Archiving Strategy   │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └─────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                            Model Security Layer (Model Security)                            │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │   Integrity │  │   Privacy   │  │   Fairness  │  │   Robustness│          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  │ • Model Signing   │  │ • Differential Privacy   │  │ • Bias Detection   │  │ • Adversarial Attacks   │          │  │
│  │  │ • Version Control   │  │ • Federated Learning   │  │ • Fairness Testing │  │ • Input Validation   │          │  │
│  │  │ • Lineage Tracing   │  │ • Homomorphic Encryption   │  │ • Inclusivity Review │  │ • Anomaly Detection   │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └─────────────────────────────────────┬─────────────────────────────────────────┘  │
│                                       │                                             │
│                                       ▼                                             │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                            Threat Protection Layer (Threat Protection)                        │  │
│  │                                                                               │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐          │  │
│  │  │   Runtime   │  │   Network   │  │   Container │  │   Supply    │          │  │
│  │  │   Security  │  │   Security  │  │   Security  │  │   Chain     │          │  │
│  │  │             │  │             │  │             │  │             │          │  │
│  │  │ • Runtime Protection │  │ • Network Policies   │  │ • Image Scanning   │  │ • Dependency Checks   │          │  │
│  │  │ • Malicious Behavior Detection│  │ • Zero Trust Network │  │ • Vulnerability Scanning   │  │ • SBOM Generation   │          │  │
│  │  │ • Process Monitoring   │  │ • Traffic Encryption   │  │ • Baseline Checks   │  │ • License Compliance   │          │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘          │  │
│  │                                                                               │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

### 1.2 Security Control Matrix

| Security Domain | Control Measures | Implementation Component | Compliance Requirement | Importance |
|----------|----------|----------|----------|----------|
| **Authentication** | Multi-factor authentication, SSO integration | [[Keycloak|Keycloak]], LDAP | GDPR, SOC2 | ⭐⭐⭐⭐⭐ |
| **Access Control** | RBAC, ABAC, network policies | Kubernetes RBAC, OPA | HIPAA, ISO27001 | ⭐⭐⭐⭐⭐ |
| **Data Encryption** | Static encryption, transport encryption | Vault, cert-manager | PCI-DSS, GDPR | ⭐⭐⭐⭐⭐ |
| **Model Safety** | Model signing, differential privacy | Sigstore, OpenDP | AI Act, NIST AI RMF | ⭐⭐⭐⭐ |
| **Threat Detection** | Runtime protection, anomaly detection | [[Falco|Falco]], Sysdig | NIST CSF | ⭐⭐⭐⭐ |
| **Compliance Auditing** | Operational auditing, compliance reporting | Auditbeat, ELK | SOX, FINRA | ⭐⭐⭐ |

---


## 2. Authentication and Access Control

### 2.1 Enterprise IAM Integration

```yaml
# keycloak-ai-platform.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: ai-security
---
# Keycloak Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: keycloak
  namespace: ai-security
spec:
  replicas: 3
  selector:
    matchLabels:
      app: keycloak
  template:
    metadata:
      labels:
        app: keycloak
    spec:
      containers:
      - name: keycloak
        image: quay.io/keycloak/keycloak:22.0.1
        args: ["start", "--optimized"]
        env:
        - name: KEYCLOAK_ADMIN
          value: "admin"
        - name: KEYCLOAK_ADMIN_PASSWORD
          valueFrom:
            secretKeyRef:
              name: keycloak-admin-credentials
              key: password
        - name: KC_DB
          value: "postgres"
        - name: KC_DB_URL
          value: "jdbc:postgresql://postgres-keycloak:5432/keycloak"
        - name: KC_DB_USERNAME
          valueFrom:
            secretKeyRef:
              name: postgres-keycloak-credentials
              key: username
        - name: KC_DB_PASSWORD
          valueFrom:
            secretKeyRef:
              name: postgres-keycloak-credentials
              key: password
        - name: KC_HOSTNAME
          value: "keycloak.ai-platform.local"
        - name: KC_HTTP_ENABLED
          value: "true"
        - name: KC_PROXY
          value: "edge"
        ports:
        - name: http
          containerPort: 8080
        - name: https
          containerPort: 8443
        readinessProbe:
          httpGet:
            path: /realms/master
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
        resources:
          requests:
            cpu: "500m"
            memory: "1Gi"
          limits:
            cpu: "1"
            memory: "2Gi"
---
# AI Platform Realm Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: keycloak-ai-realm
  namespace: ai-security
data:
  ai-platform-realm.json: |
    {
      "id": "ai-platform",
      "realm": "ai-platform",
      "displayName": "AI Platform Realm",
      "enabled": true,
      "sslRequired": "external",
      "registrationAllowed": false,
      "loginWithEmailAllowed": true,
      "duplicateEmailsAllowed": false,
      "resetPasswordAllowed": true,
      "editUsernameAllowed": false,
      "roles": {
        "realm": [
          {
            "name": "ai-admin",
            "description": "AI platform administrator"
          },
          {
            "name": "ai-developer",
            "description": "AI developer"
          },
          {
            "name": "ai-ml-engineer",
            "description": "machine learning engineer"
          },
          {
            "name": "ai-data-scientist",
            "description": "data scientist"
          },
          {
            "name": "ai-auditor",
            "description": "AI auditor"
          }
        ]
      },
      "groups": [
        {
          "name": "ai-platform-admins",
          "path": "/ai-platform-admins",
          "attributes": {},
          "realmRoles": ["ai-admin"],
          "clientRoles": {}
        },
        {
          "name": "ml-teams",
          "path": "/ml-teams",
          "subGroups": [
            {
              "name": "research-team",
              "realmRoles": ["ai-ml-engineer", "ai-data-scientist"]
            },
            {
              "name": "production-team",
              "realmRoles": ["ai-developer"]
            }
          ]
        }
      ],
      "clients": [
        {
          "clientId": "kubernetes",
          "name": "Kubernetes API Server",
          "description": "K8s API Server OIDC Client",
          "enabled": true,
          "clientAuthenticatorType": "client-secret",
          "redirectUris": ["https://kubernetes.default.svc.cluster.local/*"],
          "webOrigins": [],
          "protocol": "openid-connect",
          "attributes": {
            "saml.assertion.signature": "false",
            "saml.force.post.binding": "false",
            "saml.multivalued.roles": "false",
            "saml.encrypt": "false",
            "oauth2.device.authorization.grant.enabled": "false",
            "backchannel.logout.revoke.offline.tokens": "false",
            "use.refresh.tokens": "true",
            "oidc.ciba.grant.enabled": "false",
            "backchannel.logout.session.required": "true",
            "client_credentials.use_refresh_token": "false",
            "acr.loa.map": "{}",
            "require.pushed.authorization.requests": "false",
            "tls.client.certificate.bound.access.tokens": "false",
            "display.on.consent.screen": "false",
            "token.response.type.bearer.lower-case": "false"
          }
        }
      ]
    }
```

### 2.2 Fine-grained Configuration of Kubernetes RBAC

```yaml
# ai-platform-rbac.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: ai-platform
  labels:
    name: ai-platform
---
# Core Role Definition
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: ai-model-operator
  namespace: ai-platform
rules:
# Model Deployment Permissions
- apiGroups: ["serving.kserve.io"]
  resources: ["inferenceservices", "trainedmodels"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
  
# Configuration Management Permissions
- apiGroups: [""]
  resources: ["configmaps", "secrets"]
  verbs: ["get", "list", "watch", "create", "update", "patch"]
  
# Monitoring View Permissions
- apiGroups: [""]
  resources: ["pods", "services", "endpoints"]
  verbs: ["get", "list", "watch"]
  
# Log Viewing Permissions
- apiGroups: [""]
  resources: ["pods/log"]
  verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: ai-security-auditor
  namespace: ai-platform
rules:
# Read Only Permissions
- apiGroups: ["*"]
  resources: ["*"]
  verbs: ["get", "list", "watch"]
  
# Audit Log Access
- apiGroups: [""]
  resources: ["events"]
  verbs: ["get", "list", "watch"]
  
# Security Log View
- apiGroups: ["security.istio.io"]
  resources: ["authorizationpolicies"]
  verbs: ["get", "list", "watch"]
---
# Role Binding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: ml-engineers-binding
  namespace: ai-platform
subjects:
- kind: Group
  name: oidc:ai-platform:ml-teams
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: ai-model-operator
  apiGroup: rbac.authorization.k8s.io
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: security-auditors-binding
  namespace: ai-platform
subjects:
- kind: Group
  name: oidc:ai-platform:ai-auditor
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: ai-security-auditor
  apiGroup: rbac.authorization.k8s.io
```

---


## 3. Data Protection and Privacy

### 3.1 Data Encryption Configuration

```yaml
# vault-ai-encryption.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: ai-security
---
# HashiCorp Vault Deployment
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: vault
  namespace: ai-security
spec:
  serviceName: vault
  replicas: 3
  selector:
    matchLabels:
      app: vault
  template:
    metadata:
      labels:
        app: vault
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
          - labelSelector:
              matchExpressions:
              - key: app
                operator: In
                values:
                - vault
            topologyKey: kubernetes.io/hostname
      containers:
      - name: vault
        image: hashicorp/vault:1.14.0
        securityContext:
          runAsNonRoot: true
          runAsUser: 1000
          capabilities:
            add: ["IPC_LOCK"]
        ports:
        - containerPort: 8200
          name: api
        - containerPort: 8201
          name: cluster
        env:
        - name: VAULT_ADDR
          value: "https://127.0.0.1:8200"
        - name: VAULT_API_ADDR
          value: "https://vault.ai-security.svc.cluster.local:8200"
        - name: VAULT_CLUSTER_ADDR
          value: "https://$(POD_IP):8201"
        - name: POD_IP
          valueFrom:
            fieldRef:
              fieldPath: status.podIP
        command:
        - vault
        - server
        - -config=/vault/config/vault-config.hcl
        volumeMounts:
        - name: vault-config
          mountPath: /vault/config
        - name: vault-storage
          mountPath: /vault/data
        livenessProbe:
          exec:
            command:
            - /bin/sh
            - -c
            - vault status
          initialDelaySeconds: 60
          periodSeconds: 5
        readinessProbe:
          exec:
            command:
            - /bin/sh
            - -c
            - vault status
          initialDelaySeconds: 30
          periodSeconds: 5
        resources:
          requests:
            cpu: "500m"
            memory: "1Gi"
          limits:
            cpu: "1"
            memory: "2Gi"
  volumeClaimTemplates:
  - metadata:
      name: vault-storage
    spec:
      accessModes: ["ReadWriteOnce"]
      storageClassName: fast-ssd
      resources:
        requests:
          storage: 10Gi
---
# Vault Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: vault-config
  namespace: ai-security
data:
  vault-config.hcl: |
    ui = true
    
    listener "tcp" {
      address = "[::]:8200"
      tls_cert_file = "/vault/certs/tls.crt"
      tls_key_file = "/vault/certs/tls.key"
      tls_disable = false
    }
    
    storage "raft" {
      path = "/vault/data"
      node_id = "node-${POD_INDEX}"
    }
    
    seal "awskms" {
      region     = "us-west-2"
      kms_key_id = "alias/vault-unseal-key"
    }
    
    api_addr = "https://vault.ai-security.svc.cluster.local:8200"
    cluster_addr = "https://$(POD_IP):8201"
    disable_mlock = true
```

### 3.2 Differential Privacy Implementation

```python
# differential_privacy.py
import numpy as np
from opendp.accuracy import laplacian_scale_to_accuracy
from opendp.mod import enable_features
from opendp.typing import L1Distance, VectorDomain, AllDomain

enable_features("floating-point", "contrib")

class DifferentialPrivacyEngine:
    def __init__(self, epsilon: float = 1.0, delta: float = 1e-5):
        """
        差分隐私引擎
        
        Args:
            epsilon: 隐私预算
            delta: δ值（通常很小）
        """
        self.epsilon = epsilon
        self.delta = delta
        
    def add_laplace_noise(self, data: np.ndarray, sensitivity: float) -> np.ndarray:
        """add Laplacian noise"""
        scale = sensitivity / self.epsilon
        noise = np.random.laplace(0, scale, data.shape)
        return data + noise
        
    def add_gaussian_noise(self, data: np.ndarray, sensitivity: float) -> np.ndarray:
        """Add Gaussian noise (for ε,δ-DP)"""
        # Calculate the standard deviation of Gaussian noise
        sigma = sensitivity * np.sqrt(2 * np.log(1.25 / self.delta)) / self.epsilon
        noise = np.random.normal(0, sigma, data.shape)
        return data + noise
        
    def private_mean(self, data: np.ndarray, bounds: tuple) -> float:
        """Calculate the mean while satisfying differential privacy"""
        # Clip data to specified range
        clipped_data = np.clip(data, bounds[0], bounds[1])
        
        # Compute sensitivity (for mean query)
        sensitivity = (bounds[1] - bounds[0]) / len(data)
        
        # Add Noise
        true_mean = np.mean(clipped_data)
        private_mean = self.add_laplace_noise(np.array([true_mean]), sensitivity)[0]
        
        return float(private_mean)
        
    def private_histogram(self, data: np.ndarray, bins: int, range_vals: tuple) -> np.ndarray:
        """Calculate histogram satisfying differential privacy"""
        # Calculate true histogram
        hist, bin_edges = np.histogram(data, bins=bins, range=range_vals)
        
        # Sensitivity is 1 (each individual affects at most one bin)
        sensitivity = 1.0
        
        # Add noise to each bin
        private_hist = self.add_laplace_noise(hist.astype(float), sensitivity)
        
        # Ensure non-negative
        private_hist = np.maximum(private_hist, 0)
        
        return private_hist

# Differential Privacy Application in AI Model Training
class PrivateAITraining:
    def __init__(self, privacy_engine: DifferentialPrivacyEngine):
        self.privacy_engine = privacy_engine
        
    def train_with_dp_sgd(self, model, dataloader, optimizer, epochs: int):
        """Train model using differential privacy SGD"""
        for epoch in range(epochs):
            epoch_loss = 0.0
            for batch_idx, (data, target) in enumerate(dataloader):
                # Forward propagation
                output = model(data)
                loss = self.compute_loss(output, target)
                
                # Compute gradient
                optimizer.zero_grad()
                loss.backward()
                
                # Add gradient noise (implement DP-SGD)
                self._add_gradient_noise(optimizer)
                
                # Gradient clipping
                self._clip_gradients(optimizer)
                
                # Update parameters
                optimizer.step()
                
                epoch_loss += loss.item()
                
            print(f"Epoch {epoch+1}, Average Loss: {epoch_loss/len(dataloader)}")
            
    def _add_gradient_noise(self, optimizer):
        """Add noise to the gradient"""
        for param_group in optimizer.param_groups:
            for param in param_group['params']:
                if param.grad is not None:
                    # Compute L2 sensitivity
                    sensitivity = 1.0  # 假设已进行梯度裁剪
                    noise = self.privacy_engine.add_gaussian_noise(
                        param.grad.data.cpu().numpy(), 
                        sensitivity
                    )
                    param.grad.data += torch.from_numpy(noise).to(param.device)
                    
    def _clip_gradients(self, optimizer, max_norm: float = 1.0):
        """Gradient clipping"""
        torch.nn.utils.clip_grad_norm_(optimizer.param_groups[0]['params'], max_norm)

# Usage Example
dp_engine = DifferentialPrivacyEngine(epsilon=0.1, delta=1e-5)
private_trainer = PrivateAITraining(dp_engine)

# Train model (satisfying differential privacy)
private_trainer.train_with_dp_sgd(model, train_loader, optimizer, epochs=10)

# Protect privacy when publishing statistics
sensitive_data = np.array([85, 92, 78, 96, 88, 73, 91, 87])
dp_mean = dp_engine.private_mean(sensitive_data, bounds=(0, 100))
print(f"Differential privacy protection score: {dp_mean}")
```

---


## 4. Model Security Protection

### 4.1 Model Integrity Protection

```yaml
# model-integrity-protection.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: model-security
---
# Sigstore Cosign Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: cosign-server
  namespace: model-security
spec:
  replicas: 2
  selector:
    matchLabels:
      app: cosign
  template:
    metadata:
      labels:
        app: cosign
    spec:
      containers:
      - name: cosign
        image: gcr.io/projectsigstore/cosign:v2.0.0
        ports:
        - containerPort: 8080
        env:
        - name: COSIGN_PASSWORD
          valueFrom:
            secretKeyRef:
              name: cosign-password
              key: password
        - name: COSIGN_PRIVATE_KEY
          valueFrom:
            secretKeyRef:
              name: cosign-private-key
              key: private-key
        volumeMounts:
        - name: keys-volume
          mountPath: /keys
        resources:
          requests:
            cpu: "100m"
            memory: "128Mi"
          limits:
            cpu: "200m"
            memory: "256Mi"
      volumes:
      - name: keys-volume
        secret:
          secretName: cosign-keys
---
# Model Signature Strategy
apiVersion: policy.sigstore.dev/v1beta1
kind: ClusterImagePolicy
metadata:
  name: ai-model-policy
spec:
  images:
  - glob: "registry.ai-platform.local/models/**"
  authorities:
  - key:
      kms: "gcpkms://projects/my-project/locations/global/keyRings/my-keyring/cryptoKeys/my-key"
    attestations:
    - name: model-integrity
      predicateType: "https://cosign.sigstore.dev/attestation/v1"
      policy:
        type: cue
        data: |
          predicateType: "https://cosign.sigstore.dev/attestation/v1"
          predicate: {
            model_hash: string
            training_data_hash: string
            timestamp: string
            signature: string
          }
```

### 4.2 Adversarial Sample Detection

```python
# adversarial_detection.py
import torch
import torch.nn as nn
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

class AdversarialDetector:
    def __init__(self, model, detector_type: str = "statistical"):
        self.model = model
        self.detector_type = detector_type
        self.scaler = StandardScaler()
        self.detector = None
        
    def fit_statistical_detector(self, clean_inputs, labels):
        """Training anomaly detector"""
        # Extract features (activations, gradients etc.)
        features = self._extract_features(clean_inputs, labels)
        
        # Standardize features
        normalized_features = self.scaler.fit_transform(features)
        
        # Train Isolation Forest detector
        self.detector = IsolationForest(
            contamination=0.1,  # 预期异常比例
            random_state=42
        )
        self.detector.fit(normalized_features)
        
    def _extract_features(self, inputs, labels):
        """Extract features from input samples"""
        features = []
        
        with torch.no_grad():
            for input_batch, label_batch in zip(inputs, labels):
                input_tensor = torch.tensor(input_batch, dtype=torch.float32)
                label_tensor = torch.tensor(label_batch)
                
                # Forward propagation to get intermediate activations
                activations = []
                hooks = []
                
                def hook_fn(module, input, output):
                    activations.append(output.flatten())
                
                # Register hooks to key layers
                for name, module in self.model.named_modules():
                    if isinstance(module, (nn.Linear, nn.Conv2d)):
                        hook = module.register_forward_hook(hook_fn)
                        hooks.append(hook)
                
                # Execute forward propagation
                output = self.model(input_tensor.unsqueeze(0))
                
                # Remove hooks
                for hook in hooks:
                    hook.remove()
                
                # Combine features
                sample_features = torch.cat(activations).numpy()
                features.append(sample_features)
                
        return np.array(features)
        
    def detect_adversarial(self, inputs):
        """Detect adversarial samples"""
        if self.detector is None:
            raise ValueError("Detector not trained yet")
            
        # Extract features
        features = self._extract_features(inputs, None)
        normalized_features = self.scaler.transform(features)
        
        # Detect anomalies
        anomaly_scores = self.detector.decision_function(normalized_features)
        predictions = self.detector.predict(normalized_features)
        
        # Return result (-1 for anomaly, 1 for normal)
        return {
            'is_adversarial': predictions == -1,
            'anomaly_scores': anomaly_scores,
            'confidence': np.abs(anomaly_scores)
        }

class InputValidation:
    def __init__(self, input_shape, validation_rules=None):
        self.input_shape = input_shape
        self.validation_rules = validation_rules or self._default_rules()
        
    def _default_rules(self):
        """Default validation rule"""
        return {
            'min_value': -10.0,
            'max_value': 10.0,
            'max_l2_norm': 5.0,
            'allowed_perturbation': 0.1
        }
        
    def validate_input(self, input_tensor, reference_tensor=None):
        """Validate input validity"""
        results = {}
        
        # Basic range check
        min_val = torch.min(input_tensor).item()
        max_val = torch.max(input_tensor).item()
        results['range_check'] = (
            min_val >= self.validation_rules['min_value'] and
            max_val <= self.validation_rules['max_value']
        )
        
        # L2 norm check
        l2_norm = torch.norm(input_tensor).item()
        results['norm_check'] = l2_norm <= self.validation_rules['max_l2_norm']
        
        # Check perturbation size if reference input is provided
        if reference_tensor is not None:
            perturbation = torch.norm(input_tensor - reference_tensor).item()
            results['perturbation_check'] = (
                perturbation <= self.validation_rules['allowed_perturbation']
            )
        else:
            results['perturbation_check'] = True
            
        # Synthesize validation results
        results['is_valid'] = all(results.values())
        
        return results

# Adversarial Training Defense
class AdversarialTraining:
    def __init__(self, model, epsilon: float = 0.03):
        self.model = model
        self.epsilon = epsilon
        
    def pgd_attack(self, images, labels, num_steps=10):
        """Projection Gradient Descent Attack"""
        images = images.clone().detach()
        images.requires_grad = True
        
        # PGD iteration
        for _ in range(num_steps):
            outputs = self.model(images)
            loss = nn.CrossEntropyLoss()(outputs, labels)
            
            # Compute gradient
            grad = torch.autograd.grad(loss, images, retain_graph=False, create_graph=False)[0]
            
            # Update image
            images = images.detach() + self.epsilon * grad.sign()
            
            # Project into epsilon ball
            delta = torch.clamp(images - images, min=-self.epsilon, max=self.epsilon)
            images = torch.clamp(images + delta, min=0, max=1).detach()
            images.requires_grad = True
            
        return images.detach()
        
    def train_with_adversarial_examples(self, train_loader, optimizer, epochs: int):
        """Use adversarial samples for training"""
        self.model.train()
        
        for epoch in range(epochs):
            total_loss = 0
            correct = 0
            total = 0
            
            for batch_idx, (data, target) in enumerate(train_loader):
                data, target = data.cuda(), target.cuda()
                
                # Generate adversarial sample
                adv_data = self.pgd_attack(data, target)
                
                # Mix normal and adversarial samples for training
                combined_data = torch.cat([data, adv_data], dim=0)
                combined_target = torch.cat([target, target], dim=0)
                
                # Forward propagation
                outputs = self.model(combined_data)
                loss = nn.CrossEntropyLoss()(outputs, combined_target)
                
                # Backward propagation
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                
                total_loss += loss.item()
                _, predicted = outputs.max(1)
                total += combined_target.size(0)
                correct += predicted.eq(combined_target).sum().item()
                
            accuracy = 100. * correct / total
            print(f'Epoch {epoch+1}: Loss={total_loss/len(train_loader):.4f}, Accuracy={accuracy:.2f}%')

# Usage Example
# 1. Train an adversarial detector
detector = AdversarialDetector(model)
detector.fit_statistical_detector(clean_training_data, labels)

# 2. Validate input
validator = InputValidation(input_shape=(3, 224, 224))
validation_result = validator.validate_input(test_input, clean_input)

# 3. Adversarial training
adv_trainer = AdversarialTraining(model, epsilon=0.03)
adv_trainer.train_with_adversarial_examples(train_loader, optimizer, epochs=20)

# 4. Online detection
detection_result = detector.detect_adversarial(suspicious_input)
if detection_result['is_adversarial']:
    print("Detected adversarial samples!")
    # Deny service or take other measures
```

---


## 5. Compliance Audits and Monitoring

### 5.1 Audit Log Configuration

```yaml
# audit-logging.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: ai-audit
---
# Auditbeat Deployment
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: auditbeat
  namespace: ai-audit
spec:
  selector:
    matchLabels:
      app: auditbeat
  template:
    metadata:
      labels:
        app: auditbeat
    spec:
      hostPID: true
      hostNetwork: true
      dnsPolicy: ClusterFirstWithHostNet
      containers:
      - name: auditbeat
        image: docker.elastic.co/beats/auditbeat:8.11.0
        securityContext:
          runAsUser: 0
          capabilities:
            add:
            - AUDIT_CONTROL
            - AUDIT_READ
        volumeMounts:
        - name: config
          mountPath: /usr/share/auditbeat/auditbeat.yml
          readOnly: true
          subPath: auditbeat.yml
        - name: data
          mountPath: /usr/share/auditbeat/data
        - name: auditd-socket
          mountPath: /var/run/audit
        env:
        - name: ELASTICSEARCH_HOST
          value: "https://elasticsearch.ai-audit.svc.cluster.local:9200"
        - name: ELASTICSEARCH_USERNAME
          valueFrom:
            secretKeyRef:
              name: elasticsearch-credentials
              key: username
        - name: ELASTICSEARCH_PASSWORD
          valueFrom:
            secretKeyRef:
              name: elasticsearch-credentials
              key: password
        resources:
          requests:
            cpu: "100m"
            memory: "200Mi"
          limits:
            cpu: "200m"
            memory: "400Mi"
      volumes:
      - name: config
        configMap:
          name: auditbeat-config
      - name: data
        hostPath:
          path: /var/lib/auditbeat
          type: DirectoryOrCreate
      - name: auditd-socket
        hostPath:
          path: /var/run/audit
          type: Directory
---
# Auditbeat Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: auditbeat-config
  namespace: ai-audit
data:
  auditbeat.yml: |
    auditbeat.modules:
    - module: auditd
      audit_rules: |
        # Monitor access to AI model files
        -w /models -p rwxa -k model_access
        -w /training-data -p rwxa -k data_access
        -w /model-registry -p rwxa -k registry_access
        
        # Monitoring of sensitive configuration files
        -w /etc/kubernetes -p rwxa -k k8s_config
        -w /var/lib/kubelet -p rwxa -k kubelet_data
        
        # Monitoring of user permission changes
        -a always,exit -F arch=b64 -S chmod -F auid>=1000 -F auid!=4294967295 -k perm_mod
        -a always,exit -F arch=b64 -S chown -F auid>=1000 -F auid!=4294967295 -k perm_mod
        
        # Network connection monitoring
        -a always,exit -F arch=b64 -S connect -F auid>=1000 -F auid!=4294967295 -k network
        
    - module: file_integrity
      paths:
      - /models
      - /training-data
      - /model-registry
      scan_at_start: true
      scan_rate_per_sec: 50 MiB
      max_file_size: 100 MiB
      hash_types: [sha256]
      recursive: true
      
    processors:
    - add_cloud_metadata: ~
    - add_docker_metadata: ~
    - add_kubernetes_metadata:
        host: ${NODE_NAME}
        matchers:
        - logs_path:
            logs_path: "/var/log/containers/"
            
    output.elasticsearch:
      hosts: ["${ELASTICSEARCH_HOST}"]
      username: "${ELASTICSEARCH_USERNAME}"
      password: "${ELASTICSEARCH_PASSWORD}"
      ssl.verification_mode: none
      
    setup.kibana:
      host: "https://kibana.ai-audit.svc.cluster.local:5601"
      
    setup.template.settings:
      index.number_of_shards: 1
```

### 5.2 Compliance Report Generation

```python
# compliance_reporter.py
import pandas as pd
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any
import logging

logger = logging.getLogger(__name__)

class ComplianceReporter:
    def __init__(self, es_client, report_period_days: int = 30):
        self.es_client = es_client
        self.report_period = timedelta(days=report_period_days)
        self.report_date = datetime.now()
        
    def generate_ai_compliance_report(self) -> Dict[str, Any]:
        """Generate compliance report for the AI platform"""
        
        report = {
            'report_date': self.report_date.isoformat(),
            'report_period': f"Last {self.report_period.days} days",
            'compliance_status': {},
            'findings': {},
            'recommendations': []
        }
        
        # GDPR compliance check
        report['compliance_status']['gdpr'] = self._check_gdpr_compliance()
        
        # SOC2 compliance check
        report['compliance_status']['soc2'] = self._check_soc2_compliance()
        
        # Compliance check for specific AI regulations
        report['compliance_status']['ai_act'] = self._check_ai_act_compliance()
        
        # Security event statistics
        report['findings']['security_incidents'] = self._analyze_security_incidents()
        
        # Access control audit
        report['findings']['access_control'] = self._analyze_access_patterns()
        
        # Data protection check
        report['findings']['data_protection'] = self._analyze_data_protection()
        
        # Generate recommendations
        report['recommendations'] = self._generate_recommendations(report)
        
        return report
        
    def _check_gdpr_compliance(self) -> Dict[str, Any]:
        """Check GDPR compliance"""
        
        # Check data processing records
        data_processing_logs = self._query_audit_logs(
            query="kubernetes.labels.app:model-registry AND event.action:data_access",
            time_range=self.report_period
        )
        
        # Check consent records
        consent_records = self._query_elasticsearch(
            index="consent-records-*",
            query={"exists": {"field": "user_consent"}},
            time_range=self.report_period
        )
        
        # Check data subject rights requests
        subject_requests = self._query_elasticsearch(
            index="subject-requests-*",
            query={"term": {"request_type": "data_deletion"}},
            time_range=self.report_period
        )
        
        return {
            'compliant': len(subject_requests) > 0,  # 至少处理过删除请求
            'data_processing_records': len(data_processing_logs),
            'consent_records': len(consent_records),
            'subject_requests_handled': len(subject_requests),
            'issues': self._identify_gdpr_issues(data_processing_logs)
        }
        
    def _check_soc2_compliance(self) -> Dict[str, Any]:
        """Check SOC2 compliance"""
        
        # Check security
        security_findings = self._query_elasticsearch(
            index="security-findings-*",
            query={"range": {"severity": {"gte": "medium"}}},
            time_range=self.report_period
        )
        
        # Availability monitoring
        uptime_data = self._query_monitoring_metrics(
            metric="up",
            labels={"job": "ai-services"},
            time_range=self.report_period
        )
        
        # Configuration change audit
        config_changes = self._query_audit_logs(
            query="event.category:configuration AND event.type:change",
            time_range=self.report_period
        )
        
        return {
            'security_rating': "pass" if len(security_findings) < 5 else "fail",
            'availability_percentage': self._calculate_uptime_percentage(uptime_data),
            'configuration_changes': len(config_changes),
            'remediation_items': len([f for f in security_findings if f['status'] == 'open'])
        }
        
    def _check_ai_act_compliance(self) -> Dict[str, Any]:
        """Check AI act compliance"""
        
        # High-Risk AI System Registration
        high_risk_models = self._query_model_registry(
            filters={"risk_level": "high"}
        )
        
        # Transparency Check Requirement
        transparency_docs = self._query_documentation(
            category="model-transparency"
        )
        
        # Record of Human Oversight
        human_oversight_logs = self._query_audit_logs(
            query="event.category:human_oversight",
            time_range=self.report_period
        )
        
        return {
            'high_risk_models_registered': len(high_risk_models),
            'transparency_documents': len(transparency_docs),
            'human_oversight_activities': len(human_oversight_logs),
            'compliance_score': self._calculate_ai_act_score(
                len(high_risk_models), 
                len(transparency_docs), 
                len(human_oversight_logs)
            )
        }
        
    def _analyze_security_incidents(self) -> Dict[str, Any]:
        """Analyze security incidents"""
        
        # Query Various Security Events
        incident_types = {
            'unauthorized_access': 'event.category:authentication AND event.outcome:failure',
            'data_breach': 'event.category:data_security AND event.type:breach',
            'malware_detection': 'event.module:antivirus AND threat.indicator.type:malware',
            'privilege_escalation': 'event.action:user_privilege_change AND event.outcome:success'
        }
        
        incidents_summary = {}
        for incident_type, query in incident_types.items():
            incidents = self._query_elasticsearch(
                index="security-logs-*",
                query={"query_string": {"query": query}},
                time_range=self.report_period
            )
            incidents_summary[incident_type] = {
                'count': len(incidents),
                'trend': self._calculate_trend(incidents),
                'severity_distribution': self._analyze_severity(incidents)
            }
            
        return incidents_summary
        
    def _analyze_access_patterns(self) -> Dict[str, Any]:
        """Analyze access control models"""
        
        # Abnormal Access Detection
        access_logs = self._query_audit_logs(
            query="event.category:access",
            time_range=timedelta(days=7)  # 近期活动分析
        )
        
        # User Behavior Analysis
        user_behaviors = self._analyze_user_behavior(access_logs)
        
        # Detection of Permission Drift
        permission_changes = self._detect_permission_drift()
        
        return {
            'anomalous_users': user_behaviors['anomalous_users'],
            'permission_drifts': permission_changes,
            'access_review_needed': user_behaviors['users_needing_review']
        }
        
    def _generate_recommendations(self, report: Dict) -> List[str]:
        """Generate improvement suggestions based on reports"""
        
        recommendations = []
        
        # GDPR Recommendations
        gdpr_status = report['compliance_status']['gdpr']
        if not gdpr_status['compliant']:
            recommendations.append("Establish a complete data processing record system")
            recommendations.append("Implement a process for handling data subject rights requests")
            
        # Security Recommendations
        security_findings = report['findings']['security_incidents']
        high_severity_count = sum(
            findings['count'] 
            for findings in security_findings.values() 
            if findings.get('severity_distribution', {}).get('high', 0) > 0
        )
        
        if high_severity_count > 0:
            recommendations.append(f"Immediately handle {high_severity_count} high-severity security incidents")
            recommendations.append("Enhance intrusion detection and response capabilities")
            
        # AI Governance Recommendations
        ai_act_status = report['compliance_status']['ai_act']
        if ai_act_status['compliance_score'] < 80:
            recommendations.append("Perfect the registration system for high-risk AI systems")
            recommendations.append("Enhance model transparency document management")
            
        return recommendations
        
    def export_report(self, report: Dict, format: str = "pdf") -> str:
        """Export compliance report"""
        
        if format == "json":
            filename = f"ai_compliance_report_{self.report_date.strftime('%Y%m%d')}.json"
            with open(filename, 'w') as f:
                json.dump(report, f, indent=2, default=str)
            return filename
            
        elif format == "csv":
            # Convert to CSV Format
            df = pd.json_normalize(report)
            filename = f"ai_compliance_report_{self.report_date.strftime('%Y%m%d')}.csv"
            df.to_csv(filename, index=False)
            return filename
            
        # Can Extend Support for Formats Such as PDF, HTML, etc.
        return ""

# Usage Example
reporter = ComplianceReporter(elasticsearch_client, report_period_days=30)
compliance_report = reporter.generate_ai_compliance_report()

# Export Report
json_file = reporter.export_report(compliance_report, format="json")
print(f"Compliance report has been generated: {json_file}")

# Scheduled Report Task
def scheduled_compliance_report():
    """Generate compliance report periodically"""
    reporter = ComplianceReporter(es_client)
    report = reporter.generate_ai_compliance_report()
    
    # Send report to relevant personnel
    send_email_report(report, recipients=["security-team@company.com"])
    
    # Store to compliance system
    store_compliance_record(report)

# Configure scheduled task (for example, execute on January 1st)
# Can use Kubernetes CronJob or Celery Beat etc. scheduler
```

---


## 6. Best Practices for Security Operations

### 6.1 Security Checklist

✅ **Pre-deployment Security Checks**
- [ ] Code security scanning completed (SAST/DAST)
- [ ] Third-party dependency vulnerability scans passed
- [ ] Container image security baseline checks
- [ ] Kubernetes security configuration review
- [ ] Model safety and bias assessment
- [ ] Data privacy impact assessment completed

✅ **Runtime Security Monitoring**
- [ ] Real-time threat detection system operates normally
- [ ] Anomaly behavior analysis rules are effective
- [ ] Security Incident Response Process Tested Successfully
- [ ] Access Log Audits Configured Correctly
- [ ] Vulnerability Scans Performed Regularly
- [ ] Security Patches Updated Timely

✅ **Compliance Continuous Monitoring**
- [ ] Regular Compliance Assessments Executed
- [ ] Audit Logs Integrity Verified
- [ ] Privacy Protection Measures Operate Effectively
- [ ] Security Training Conducted Regularly
- [ ] Third-Party Audits Coordinated
- [ ] Improvement Measures Followed Up

### 6.2 Emergency Response Process

**Security Event Categorization**
- 🔴 **Urgent**: Data Leakage, System Compromised, Model Poisoning
- 🟡 **High Risk**: Unauthorized Access, Malware Infection, Denial of Service
- 🟢 **Low/Moderate**: Configuration Errors, Minor Violations, Suspicious Activity

**Response Steps**
1. **Detection and Confirmation** - Validate Event Authenticity
2. **Containment and Isolation** - Limit Impact Scope
3. **Investigation and Analysis** - Determine Root Cause
4. **Removal and Recovery** - Remove Threat and Restore Normalcy
5. **Summarize and Improve** - Document lessons learned and improve defenses

---

---


## Obsidian Related Documentation

- domain-11-ai-infra MOC
- [[domain-14-ai-ml-infra/README.md|Domain-11: AI Infrastructure]]
- Domain-11 AI Infrastructure — List of Open Source Projects
- AI Infrastructure Architecture
- 132 - AI/ML Workloads Operations (AI/ML Workloads Operations)
- GPU Scheduling and Management
- GPU Monitoring and Observability
- Distributed Training Frameworks
- AI Data Processing Pipeline and Feature Engineering
- AI Experiment Management and MLOps Platform
- AutoML and Hyperparameter Tuning
- AI Model Registry and Version Management

## See Also

- 28-green-computing-sustainability
- 29-alibaba-cloud-integration
- 31-ai-platform-governance
- 32-mlops-pipeline


<!-- risk-assessed -->
