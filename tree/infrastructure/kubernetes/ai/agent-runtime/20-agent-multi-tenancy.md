---
title: Agent Multi-Tenant Architecture
description: 'Agent system tenant isolation, Namespace model, API Key management, usage quotas, audit logs, and K8s NetworkPolicy'
summary: 'Agent system tenant isolation, Namespace model, API Key management, usage quotas, audit logs, and K8s NetworkPolicy'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- multi-tenancy
- isolation
- security
tier: supporting
created: '2026-07-02'
last_updated: 2026-07
difficulty: advanced
reading_level: advanced
audience:
- AI Engineer
- Platform Engineer
- Security Engineer
estimated_read_time: 20min
intent_queries:
- What is Agent multi-tenant architecture
- How to implement Agent tenant isolation
- K8s Agent multi-tenancy
- Agent API Key management
trigger_keywords:
- multi-tenancy
- tenant isolation
- namespace
- api key
- quota
- audit
- network policy
prerequisites:
- llm-basics
- kubernetes-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: Dillan Teagle
  role: contributor
original_language: Chinese
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/20-agent-multi-tenancy.md
---
# Agent Multi-Tenant Architecture

## Overview

When an Agent platform serves multiple teams or customers, multi-tenant architecture becomes a core requirement. The isolation dimensions of Agent multi-tenancy are more complex than traditional SaaS: in addition to data and network isolation, model access isolation, tool permission isolation, knowledge base isolation, and independent billing are also required.

This article covers four major isolation dimensions, the Namespace-per-Tenant model, API Key management, usage quotas, audit logs, and K8s NetworkPolicy configuration.

## 1. Tenant Isolation Dimensions

### 1.1 Isolation Matrix

```
┌──────────────┬──────────────────────────────────────────┐
│  Isolation   │              Isolation Strategy           │
│  Dimension   │                                           │
├──────────────┼──────────────────────────────────────────┤
│ Data         │ Tenant-dedicated database/schema/row-     │
│ Isolation    │ level filtering                           │
│              │ Vector database tenant partitioning       │
│              │ Object storage prefix isolation           │
├──────────────┼──────────────────────────────────────────┤
│ Model Access │ Tenant-dedicated model whitelist          │
│ Isolation    │ Independent token quotas                  │
│              │ Differentiated model routing policies     │
├──────────────┼──────────────────────────────────────────┤
│ Tool         │ Tenant tool whitelist                     │
│ Permission   │ API Key binding                           │
│ Isolation    │ Sandbox execution environment             │
├──────────────┼──────────────────────────────────────────┤
│ Billing      │ Independent budget accounts               │
│ Isolation    │ Usage metering and invoicing              │
│              │ Prepaid/postpaid modes                    │
└──────────────┴──────────────────────────────────────────┘
```

### 1.2 Isolation Levels

```python
from enum import Enum

class IsolationLevel(Enum):
    """Tenant isolation levels"""
    SHARED = "shared"           # Shared resources, logical isolation
    NAMESPACE = "namespace"     # Namespace isolation
    DEDICATED = "dedicated"     # Dedicated cluster/resource pool

ISOLATION_MATRIX = {
    IsolationLevel.SHARED: {
        "compute": "Shared Pod, request-level isolation",
        "data": "Shared database, row-level filtering",
        "model": "Shared API Key, quota isolation",
        "network": "Shared network, application-layer isolation",
        "cost": "Lowest",
        "isolation": "Weak",
    },
    IsolationLevel.NAMESPACE: {
        "compute": "Dedicated Namespace, dedicated Pod",
        "data": "Dedicated database instance or Schema",
        "model": "Dedicated API Key or Key Pool",
        "network": "NetworkPolicy isolation",
        "cost": "Medium",
        "isolation": "Medium",
    },
    IsolationLevel.DEDICATED: {
        "compute": "Dedicated node pool/cluster",
        "data": "Fully dedicated database cluster",
        "model": "Dedicated model deployment",
        "network": "VPC isolation",
        "cost": "High",
        "isolation": "Strong",
    },
}
```

## 2. Namespace-per-Tenant Model

### 2.1 Architecture Design

```
┌─────────────────────────────────────────────────────────┐
│                    K8s Cluster                           │
│                                                          │
│  ┌─────────────────────┐  ┌─────────────────────┐      │
│  │ ns: tenant-acme     │  │ ns: tenant-globex   │      │
│  │                     │  │                     │      │
│  │ ┌─────────────────┐ │  │ ┌─────────────────┐ │      │
│  │ │ agent-runtime   │ │  │ │ agent-runtime   │ │      │
│  │ │ (Deployment)    │ │  │ │ (Deployment)    │ │      │
│  │ └─────────────────┘ │  │ └─────────────────┘ │      │
│  │ ┌─────────────────┐ │  │ ┌─────────────────┐ │      │
│  │ │ knowledge-db    │ │  │ │ knowledge-db    │ │      │
│  │ │ (StatefulSet)   │ │  │ │ (StatefulSet)   │ │      │
│  │ └─────────────────┘ │  │ └─────────────────┘ │      │
│  │ ┌─────────────────┐ │  │ ┌─────────────────┐ │      │
│  │ │ cache           │ │  │ │ cache           │ │      │
│  │ │ (Redis)         │ │  │ │ (Redis)         │ │      │
│  │ └─────────────────┘ │  │ └─────────────────┘ │      │
│  │                     │  │                     │      │
│  │ NetworkPolicy:      │  │ NetworkPolicy:      │      │
│  │ deny-all + allow    │  │ deny-all + allow    │      │
│  └─────────────────────┘  └─────────────────────┘      │
│                                                          │
│  ┌──────────────────────────────────────────────────┐   │
│  │  ns: platform (Shared Services)                   │   │
│  │  - API Gateway    - LLM Proxy    - Auth Service  │   │
│  │  - Billing        - Monitoring   - Audit Log     │   │
│  └──────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

### 2.2 Tenant Namespace Template

```yaml
# tenant-namespace-template.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: tenant-${TENANT_ID}
  labels:
    tenant: ${TENANT_ID}
    isolation: namespace
    managed-by: agent-platform
  annotations:
    tenant.company.com/owner: "${TENANT_OWNER}"
    tenant.company.com/tier: "${TENANT_TIER}"
---
# ResourceQuota - Tenant resource quota
apiVersion: v1
kind: ResourceQuota
metadata:
  name: tenant-quota
  namespace: tenant-${TENANT_ID}
spec:
  hard:
    requests.cpu: "8"
    requests.memory: "16Gi"
    limits.cpu: "16"
    limits.memory: "32Gi"
    pods: "20"
    services: "10"
    persistentvolumeclaims: "10"
---
# LimitRange - Default resource limits
apiVersion: v1
kind: LimitRange
metadata:
  name: tenant-limits
  namespace: tenant-${TENANT_ID}
spec:
  limits:
  - type: Container
    default:
      cpu: "500m"
      memory: "512Mi"
    defaultRequest:
      cpu: "100m"
      memory: "128Mi"
    max:
      cpu: "4"
      memory: "8Gi"
---
# ServiceAccount - Tenant service account
apiVersion: v1
kind: ServiceAccount
metadata:
  name: tenant-agent-sa
  namespace: tenant-${TENANT_ID}
---
# Role - Tenant role
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: tenant-agent-role
  namespace: tenant-${TENANT_ID}
rules:
- apiGroups: [""]
  resources: ["pods", "services", "configmaps", "secrets"]
  verbs: ["get", "list", "watch", "create", "update", "delete"]
- apiGroups: ["apps"]
  resources: ["deployments", "statefulsets"]
  verbs: ["get", "list", "watch", "create", "update", "delete"]
---
# RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: tenant-agent-binding
  namespace: tenant-${TENANT_ID}
subjects:
- kind: ServiceAccount
  name: tenant-agent-sa
  namespace: tenant-${TENANT_ID}
roleRef:
  kind: Role
  name: tenant-agent-role
  apiGroup: rbac.authorization.k8s.io
```

### 2.3 Automated Tenant Provisioning

```python
from dataclasses import dataclass
import yaml

@dataclass
class TenantConfig:
    tenant_id: str
    owner: str
    tier: str  # free/pro/enterprise
    max_agents: int
    max_tokens_per_day: int
    allowed_models: list[str]
    allowed_tools: list[str]

class TenantProvisioner:
    """Automated tenant provisioning"""

    TIER_DEFAULTS = {
        "free": {
            "max_agents": 3,
            "max_tokens_per_day": 100_000,
            "allowed_models": ["gpt-4o-mini"],
            "allowed_tools": ["search", "calculator"],
            "cpu": "2",
            "memory": "4Gi",
        },
        "pro": {
            "max_agents": 20,
            "max_tokens_per_day": 1_000_000,
            "allowed_models": ["gpt-4o-mini", "gpt-4o", "claude-sonnet"],
            "allowed_tools": ["search", "calculator", "code_interpreter", "web_browse"],
            "cpu": "8",
            "memory": "16Gi",
        },
        "enterprise": {
            "max_agents": 100,
            "max_tokens_per_day": 10_000_000,
            "allowed_models": ["*"],  # All models
            "allowed_tools": ["*"],   # All tools
            "cpu": "32",
            "memory": "64Gi",
        },
    }

    def __init__(self, k8s_client, db_client):
        self.k8s = k8s_client
        self.db = db_client

    async def provision(self, tenant_id: str, owner: str, tier: str) -> dict:
        """Provision a tenant"""
        defaults = self.TIER_DEFAULTS[tier]

        # 1. Create Namespace
        ns_manifest = self._render_namespace(tenant_id, owner, tier, defaults)
        await self.k8s.apply(ns_manifest)

        # 2. Create resource quota
        quota_manifest = self._render_quota(tenant_id, defaults)
        await self.k8s.apply(quota_manifest)

        # 3. Create NetworkPolicy
        netpol_manifest = self._render_network_policy(tenant_id)
        await self.k8s.apply(netpol_manifest)

        # 4. Create API Key
        api_key = await self._generate_api_key(tenant_id)

        # 5. Initialize database
        await self.db.create_tenant_schema(tenant_id)

        # 6. Register in tenant management table
        await self.db.register_tenant(TenantConfig(
            tenant_id=tenant_id,
            owner=owner,
            tier=tier,
            **defaults,
        ))

        return {
            "tenant_id": tenant_id,
            "namespace": f"tenant-{tenant_id}",
            "api_key": api_key,
            "tier": tier,
            "limits": defaults,
        }

    def _render_namespace(self, tenant_id, owner, tier, defaults):
        return yaml.safe_load(f"""
apiVersion: v1
kind: Namespace
metadata:
  name: tenant-{tenant_id}
  labels:
    tenant: "{tenant_id}"
    tier: "{tier}"
  annotations:
    tenant.company.com/owner: "{owner}"
""")

    def _render_quota(self, tenant_id, defaults):
        return yaml.safe_load(f"""
apiVersion: v1
kind: ResourceQuota
metadata:
  name: tenant-quota
  namespace: tenant-{tenant_id}
spec:
  hard:
    requests.cpu: "{defaults['cpu']}"
    requests.memory: "{defaults['memory']}"
    pods: "20"
""")

    def _render_network_policy(self, tenant_id):
        return yaml.safe_load(f"""
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: tenant-isolation
  namespace: tenant-{tenant_id}
spec:
  podSelector: {{}}
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: platform
    - podSelector: {{}}
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          name: platform
    - podSelector: {{}}
  - to:
    - ipBlock:
        cidr: 0.0.0.0/0
    ports:
    - protocol: TCP
      port: 443
""")

    async def _generate_api_key(self, tenant_id):
        import secrets
        key = f"sk-agent-{tenant_id}-{secrets.token_hex(24)}"
        # Store to Secret
        await self.k8s.create_secret(
            namespace=f"tenant-{tenant_id}",
            name="api-keys",
            data={"api-key": key}
        )
        return key
```
## 3. API Key Management

### 3.1 Multi-tier API Key System

```python
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class KeyType(Enum):
    MASTER = "master"       # Master key, tenant administrator
    AGENT = "agent"         # Agent key, bound to a specific Agent
    SESSION = "session"     # Session key, temporary

@dataclass
class APIKey:
    key_id: str
    tenant_id: str
    key_type: KeyType
    key_hash: str           # Stored as hash, plaintext is never stored
    agent_id: str | None    # Bound Agent
    permissions: list[str]
    rate_limit: int         # RPM
    token_budget: int       # Daily token budget
    expires_at: datetime | None
    created_at: datetime
    last_used_at: datetime | None
    is_active: bool

class APIKeyManager:
    """API Key Manager"""

    def __init__(self, redis_client, db_client):
        self.redis = redis_client
        self.db = db_client

    def create_key(
        self,
        tenant_id: str,
        key_type: KeyType,
        agent_id: str | None = None,
        permissions: list[str] | None = None,
        rate_limit: int = 60,
        token_budget: int = 100_000,
        expires_in_days: int | None = None,
    ) -> tuple[str, APIKey]:
        """Create an API Key"""
        import secrets
        import hashlib

        # Generate Key
        raw_key = f"sk-{key_type.value}-{secrets.token_hex(32)}"
        key_hash = hashlib.sha256(raw_key.encode()).hexdigest()
        key_id = f"key-{secrets.token_hex(8)}"

        expires_at = None
        if expires_in_days:
            from datetime import timedelta
            expires_at = datetime.utcnow() + timedelta(days=expires_in_days)

        api_key = APIKey(
            key_id=key_id,
            tenant_id=tenant_id,
            key_type=key_type,
            key_hash=key_hash,
            agent_id=agent_id,
            permissions=permissions or ["chat", "tools"],
            rate_limit=rate_limit,
            token_budget=token_budget,
            expires_at=expires_at,
            created_at=datetime.utcnow(),
            last_used_at=None,
            is_active=True,
        )

        # Save to database
        self.db.save_api_key(api_key)

        # Cache to Redis (fast validation)
        self.redis.hset(f"apikey:{key_hash}", mapping={
            "tenant_id": tenant_id,
            "key_type": key_type.value,
            "agent_id": agent_id or "",
            "rate_limit": str(rate_limit),
            "token_budget": str(token_budget),
        })

        return raw_key, api_key

    def validate_key(self, raw_key: str) -> APIKey | None:
        """Validate an API Key"""
        import hashlib
        key_hash = hashlib.sha256(raw_key.encode()).hexdigest()

        # Check Redis cache first
        cached = self.redis.hgetall(f"apikey:{key_hash}")
        if not cached:
            # Fall back to database
            api_key = self.db.get_api_key_by_hash(key_hash)
            if not api_key or not api_key.is_active:
                return None
            return api_key

        # Check expiration
        # ... expiration check omitted

        return cached

    def revoke_key(self, key_id: str):
        """Revoke an API Key"""
        api_key = self.db.get_api_key(key_id)
        if api_key:
            api_key.is_active = False
            self.db.update_api_key(api_key)
            self.redis.delete(f"apikey:{api_key.key_hash}")
```

### 3.2 K8s Secret Storage

```yaml
# Tenant API Key Secret
apiVersion: v1
kind: Secret
metadata:
  name: tenant-api-keys
  namespace: tenant-${TENANT_ID}
type: Opaque
stringData:
  master-key: "sk-master-xxxxx"
  agent-key-default: "sk-agent-xxxxx"
  llm-proxy-key: "sk-proxy-xxxxx"
---
# External Secrets Operator - sync from Vault
apiVersion: external-secrets.io/v1beta1
kind: ExternalSecret
metadata:
  name: tenant-api-keys
  namespace: tenant-${TENANT_ID}
spec:
  refreshInterval: 1h
  secretStoreRef:
    name: vault-backend
    kind: ClusterSecretStore
  target:
    name: tenant-api-keys
  data:
  - secretKey: master-key
    remoteRef:
      key: secret/data/tenants/${TENANT_ID}
      property: master-key
  - secretKey: llm-proxy-key
    remoteRef:
      key: secret/data/tenants/${TENANT_ID}
      property: llm-proxy-key
```

## 4. Usage Quotas

### 4.1 Multi-dimensional Quota Management

```python
from dataclasses import dataclass
from datetime import date

@dataclass
class TenantQuota:
    tenant_id: str
    max_agents: int
    max_tokens_per_day: int
    max_tokens_per_month: int
    max_requests_per_minute: int
    max_tool_calls_per_day: int
    max_knowledge_base_size_gb: float

class QuotaManager:
    """Tenant Quota Manager"""

    def __init__(self, redis_client, db_client):
        self.redis = redis_client
        self.db = db_client

    def check_quota(
        self,
        tenant_id: str,
        resource: str,
        amount: int = 1
    ) -> tuple[bool, dict]:
        """Check quota"""
        quota = self.db.get_tenant_quota(tenant_id)
        if not quota:
            return False, {"error": "tenant_not_found"}

        today = date.today().isoformat()
        month = today[:7]

        checks = {
            "tokens_daily": {
                "used": self._get_usage(tenant_id, f"tokens:daily:{today}"),
                "limit": quota.max_tokens_per_day,
            },
            "tokens_monthly": {
                "used": self._get_usage(tenant_id, f"tokens:monthly:{month}"),
                "limit": quota.max_tokens_per_month,
            },
            "tool_calls_daily": {
                "used": self._get_usage(tenant_id, f"tool_calls:daily:{today}"),
                "limit": quota.max_tool_calls_per_day,
            },
        }

        if resource not in checks:
            return True, {}

        check = checks[resource]
        if check["used"] + amount > check["limit"]:
            return False, {
                "resource": resource,
                "used": check["used"],
                "limit": check["limit"],
                "requested": amount,
            }

        return True, checks

    def record_usage(self, tenant_id: str, resource: str, amount: int):
        """Record usage"""
        today = date.today().isoformat()
        month = today[:7]

        if resource == "tokens":
            self._incr_usage(tenant_id, f"tokens:daily:{today}", amount, 86400 * 2)
            self._incr_usage(tenant_id, f"tokens:monthly:{month}", amount, 86400 * 35)
        elif resource == "tool_calls":
            self._incr_usage(tenant_id, f"tool_calls:daily:{today}", amount, 86400 * 2)

    def _get_usage(self, tenant_id: str, key: str) -> int:
        value = self.redis.get(f"quota:{tenant_id}:{key}")
        return int(value) if value else 0

    def _incr_usage(self, tenant_id: str, key: str, amount: int, ttl: int):
        full_key = f"quota:{tenant_id}:{key}"
        self.redis.incrby(full_key, amount)
        self.redis.expire(full_key, ttl)
```
## 5. Audit Logs

### 5.1 Audit Event Structure

```python
from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

@dataclass
class AuditEvent:
    """Audit event"""
    event_id: str
    tenant_id: str
    user_id: str
    agent_id: str
    action: str                # chat/tool_call/admin/config_change
    resource: str              # Resource identifier
    details: dict              # Event details
    ip_address: str
    user_agent: str
    timestamp: datetime
    status: str                # success/failure/denied
    risk_level: str            # low/medium/high

class AuditLogger:
    """Audit log recorder"""

    def __init__(self, kafka_producer, db_client):
        self.kafka = kafka_producer
        self.db = db_client

    def log(self, event: AuditEvent):
        """Record an audit event"""
        # Send to Kafka (asynchronous persistence)
        self.kafka.send(
            topic="agent-audit-log",
            key=event.tenant_id.encode(),
            value=self._serialize(event),
        )

        # Synchronously write high-risk events to the database
        if event.risk_level == "high":
            self.db.insert_audit_event(event)

    def log_chat(self, tenant_id: str, user_id: str, agent_id: str, message: str, response: str):
        """Record a conversation event"""
        self.log(AuditEvent(
            event_id=self._generate_id(),
            tenant_id=tenant_id,
            user_id=user_id,
            agent_id=agent_id,
            action="chat",
            resource=f"agent:{agent_id}",
            details={
                "input_length": len(message),
                "output_length": len(response),
                "input_preview": message[:200],
            },
            ip_address="",
            user_agent="",
            timestamp=datetime.utcnow(),
            status="success",
            risk_level="low",
        ))

    def log_tool_call(self, tenant_id: str, user_id: str, agent_id: str, tool_name: str, params: dict, result: str):
        """Record a tool call event"""
        self.log(AuditEvent(
            event_id=self._generate_id(),
            tenant_id=tenant_id,
            user_id=user_id,
            agent_id=agent_id,
            action="tool_call",
            resource=f"tool:{tool_name}",
            details={
                "tool": tool_name,
                "params": params,
                "result_preview": result[:500],
            },
            ip_address="",
            user_agent="",
            timestamp=datetime.utcnow(),
            status="success",
            risk_level="medium",
        ))

    def _serialize(self, event: AuditEvent) -> bytes:
        import json
        return json.dumps({
            "event_id": event.event_id,
            "tenant_id": event.tenant_id,
            "user_id": event.user_id,
            "agent_id": event.agent_id,
            "action": event.action,
            "resource": event.resource,
            "details": event.details,
            "timestamp": event.timestamp.isoformat(),
            "status": event.status,
            "risk_level": event.risk_level,
        }).encode()

    def _generate_id(self):
        import secrets
        return f"audit-{secrets.token_hex(8)}"
```

### 5.2 Audit Log Querying

```yaml
# K8s deployment of the audit log service
apiVersion: apps/v1
kind: Deployment
metadata:
  name: audit-log-service
  namespace: platform
spec:
  replicas: 2
  selector:
    matchLabels:
      app: audit-log
  template:
    spec:
      containers:
      - name: audit
        image: audit-log-service:latest
        env:
        - name: KAFKA_BROKERS
          value: "kafka.platform.svc.cluster.local:9092"
        - name: CLICKHOUSE_URL
          value: "http://clickhouse.platform.svc.cluster.local:8123"
        resources:
          requests:
            cpu: "250m"
            memory: "256Mi"
---
# ClickHouse audit table
# CREATE TABLE agent_audit_log (
#     event_id String,
#     tenant_id String,
#     user_id String,
#     agent_id String,
#     action String,
#     resource String,
#     details String,
#     timestamp DateTime,
#     status String,
#     risk_level String
# ) ENGINE = MergeTree()
# PARTITION BY toYYYYMM(timestamp)
# ORDER BY (tenant_id, timestamp)
# TTL timestamp + INTERVAL 365 DAY
```

## 6. K8s NetworkPolicy

### 6.1 Tenant Network Isolation

```yaml
# Deny all traffic by default
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: tenant-${TENANT_ID}
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
---
# Allow intra-tenant communication
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-tenant-internal
  namespace: tenant-${TENANT_ID}
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector: {}  # Pods within the same Namespace
  egress:
  - to:
    - podSelector: {}  # Pods within the same Namespace
---
# Allow access to platform shared services
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-platform-services
  namespace: tenant-${TENANT_ID}
spec:
  podSelector:
    matchLabels:
      app: agent-runtime
  policyTypes:
  - Egress
  egress:
  # Allow access to LLM Proxy
  - to:
    - namespaceSelector:
        matchLabels:
          name: platform
      podSelector:
        matchLabels:
          app: llm-proxy
    ports:
    - protocol: TCP
      port: 8080
  # Allow access to Auth Service
  - to:
    - namespaceSelector:
        matchLabels:
          name: platform
      podSelector:
        matchLabels:
          app: auth-service
    ports:
    - protocol: TCP
      port: 8080
  # Allow access to external HTTPS (LLM API, etc.)
  - to:
    - ipBlock:
        cidr: 0.0.0.0/0
        except:
        - 10.0.0.0/8      # Exclude internal network
        - 172.16.0.0/12
        - 192.168.0.0/16
    ports:
    - protocol: TCP
      port: 443
---
# Allow platform to access tenants (monitoring/management)
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-platform-monitoring
  namespace: tenant-${TENANT_ID}
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          name: platform
      podSelector:
        matchLabels:
          app: prometheus
    ports:
    - protocol: TCP
      port: 9090  # metrics
```

### 6.2 Network Policy Validation

```python
class NetworkPolicyValidator:
    """Network policy validator"""

    def __init__(self, k8s_client):
        self.k8s = k8s_client

    async def validate_isolation(self, tenant_id: str) -> dict:
        """Validate tenant network isolation"""
        namespace = f"tenant-{tenant_id}"
        results = {
            "namespace": namespace,
            "checks": [],
        }

        # Check 1: Whether NetworkPolicy exists
        policies = await self.k8s.list_network_policies(namespace)
        results["checks"].append({
            "check": "network_policy_exists",
            "passed": len(policies) > 0,
            "details": f"Found {len(policies)} policies",
        })

        # Check 2: Default deny policy
        has_deny_all = any(
            p.spec.pod_selector == {} and "Ingress" in p.spec.policy_types and "Egress" in p.spec.policy_types
            for p in policies
        )
        results["checks"].append({
            "check": "default_deny_all",
            "passed": has_deny_all,
        })

        # Check 3: Cross-tenant access isolation
        cross_tenant_blocked = await self._test_cross_tenant_access(tenant_id)
        results["checks"].append({
            "check": "cross_tenant_isolation",
            "passed": cross_tenant_blocked,
        })

        results["all_passed"] = all(c["passed"] for c in results["checks"])
        return results

    async def _test_cross_tenant_access(self, tenant_id: str) -> bool:
        """Test whether cross-tenant access is blocked"""
        # Actually perform a network connectivity test
        # Attempt to access a pod in tenant-B from tenant-A
        return True  # Simplified implementation
```
## Related Topics

- [[domain-14-ai-ml-infra/03-agent-runtime/17-agent-rate-limiting-cost-control|Agent Rate Limiting and Cost Control]]
- [[domain-14-ai-ml-infra/03-agent-runtime/19-agent-ci-cd-pipeline|Agent CI/CD Pipeline]]
- [[domain-14-ai-ml-infra/03-agent-runtime/21-agent-runtime-architecture-overview|Agent Runtime Architecture Overview]]

## References

- Kubernetes Multi-Tenancy
- Network Policy Recipes
- External Secrets Operator
