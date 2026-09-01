---
Title: SpinKube Framework Practice
Description: '# SpinKube Framework Practice'
Summary: SpinKube is a native WebAssembly runtime project for Kubernetes based on Fermyon Spin and is a CNCF Sandbox project. It brings the developer-friendly experience of Spin to Kubernetes, enabling cloud-native deployment of Wasm Serverless workloads.
category: webassembly-cloud-native
tags:
- k8s
- wasm
- webassembly
- cloud-native
- apiserver
- controller-manager
- prometheus
- grafana
- helm
- containerd
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: advanced
reading_level: advanced
audience:
- Architect
- Development Engineer
- SRE
estimated_read_time: 5min
intent_queries:
What are the practices of the SpinKube framework?
- How to implement the SpinKube framework
- Kubernetes 38 WebAssembly Cloud Native Best Practices
trigger_keywords:
- SpinKube
- Framework Practice
- webassembly
- cloud
- native
prerequisites:
- kubectl-basics
- helm-basics
- prometheus-basics
- monitoring-basics
- redis-basics
- mysql-basics
- tls-basics
- policy-basics
- logging-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: Dillan Teagle
  role: contributor
---

# [[SpinKube|SpinKube]] Framework Practice
# SpinKube Framework Practice

<!-- chunk: Table of Contents -->## Table of Contents

1. [SpinKube Overview](#1-spinkube-overview)
2. [[entities/spin.md|Spin]] Application Model](#2-spin-Application Model)
3. [SpinKube Architecture](#3-spinkube-architecture)
4. [SpinApp CRD](#4-spinapp-crd)
5. [Installation and Configuration](#5-Installation and Configuration)
6. [HTTP Triggers](#6-http-triggers)
7. [[entities/keda.md|KEDA]] Integration with Scale-to-Zero](#7-keda-integration-scale-to-zero)
8. [Storage System Integration](#8-Storage System Integration)
9. [Redis and Key-Value Store](#9-redis-and-kv-store)
10. [SQLite Integration](#10-sqlite-integration)
11. [Advanced Configuration and Security](#11-Advanced Configuration and Security)
12. [Monitoring and Observability](#12-Monitoring and Observability)

---

<!-- chunk: 1. SpinKube Overview-->## 1. SpinKube Overview

## 1.1 What is SpinKube

SpinKube is a native WebAssembly runtime project for Kubernetes based on Fermyon Spin, and is a CNCF Sandbox project. It brings the developer-friendly experience of Spin to Kubernetes, enabling cloud-native deployment of Wasm serverless workloads.

```
# 🟢 Low risk: Read-only/information collection, usually no side effects
SpinKube Project Components
github.com/spinkube
│
├── spin-operator # Kubernetes Operator (core)
│ ├── SpinApp CRD # Application Custom Resources
│ ├── SpinAppExec CRD # Execution Configuration
│ └── Reconciler # Coordination Controller
│
├── containerd-shim-spin # containerd Spin shim
│ └── spin.v2 # Spin v2 runtime
│
├── spin-runtime-class   # RuntimeClass 管理
│   └── Helm Chart
│
└── docs # Documents
```
## 1.2 SpinKube vs Other Solutions / SpinKube vs Alternatives

```mermaid
graph TD
    Subgraph "Comparison of Wasm solutions in Kubernetes"
        A [original runwasi + RuntimeClass] --> B {simple but lacking management}
        C[SpinKube] --> D{Full Operator Mode}
        E[wasmCloud on K8s] --> F{Actor Distributed Model}
        G[Knative + Wasm] --> H{Event-driven, complex}
    end
    
    subgraph "SpinKube Advantages"
        D --> I[SpinApp CRD - Declarative Management]
        D --> J [KEDA Integration - Scale-to-Zero]
        D --> K [Automated Health Checkup]
        D --> L [Multi-runtime support]
        D --> M [Full support for the Spin ecosystem]
    end
```

## 1.3 Core Features

| Features | Description |
|------|------|
| **SpinApp CRD** | Kubernetes Native Spin Application Management |
| **Scale-to-Zero** | Achieve true zero-replica scaling with KEDA |
| **OCI Image** | Standard OCI Image Distribution for Wasm Modules |
| **Multiple Triggers** | Triggering methods include HTTP, message queues, and timers |
| **KV/SQLite** | Built-in distributed storage support |
| **TLS Termination** | Built-in HTTPS Support |
| **Health Check** | Automated Liveness/Readiness Probe |
| **Canary Deployment** | Supports Canary/Blue-Green Deployment |

---

<!-- chunk: 2. Spin Application Model -->## 2. Spin Application Model

## 2.1 Spin Framework Overview

Spin is a WebAssembly Serverless framework developed by Fermyon, focusing on rapidly building HTTP microservices.

```mermaid
graph LR
    subgraph "Spin runtime"
        A [HTTP Request] --> B [Spin ​​Trigger]
        B --> C [Route matching]
        C --> D [Load Wasm component]
        D --> E [Execute the processing function]
        E --> F [HTTP Response]
        
        G [External Service] --> H [Outbound HTTP]
        G --> I[KV Store]
        G --> J[SQLite]
        G --> K[Redis]
        G --> L[MySQL/Postgres]
    end
```

## 2.2 spin.toml Application Manifest

```toml
# spin.toml - Spin application configuration list
spin_manifest_version = 2

[application]
name = "my-wasm-api"
version = "1.2.0"
description = "Cloud-native WebAssembly API Service"
authors = ["developer@example.com"]

# Global trigger configuration
[application.trigger.http]
base = "/"

# Variable definitions (from environment or Kubernetes Secret)
[variables]
db_url = { required = true }
api_key = { required = true }
log_level = { default = "info" }
cache_ttl = { default = "300" }

# Component 1: User API
trigger.http
route = "/api/v1/users/..."
component = "users-handler"

[component.users-handler]
source = "target/wasm32-wasi/release/users_handler.wasm"
description = "User Management API"

[component.users-handler.build]
command = "cargo build --target wasm32-wasi --release"
workdir = "users"
watch = ["src/**/*.rs", "Cargo.toml"]

# Allowed outbound HTTP domains
[component.users-handler.trigger]
executor = { type = "wagi" } # Spin is also supported (default)

[component.users-handler.allowed_outbound_hosts]
hosts = [
  "https://auth-service.internal",
  "https://email.sendgrid.com"
]

# KV Store Visit
[component.users-handler.key_value_stores]
stores = ["default", "sessions"]

# SQLite database access
[component.users-handler.sqlite_databases]
databases = ["users_db"]

# Variable Access
[component.users-handler.variables]
db_url = "{{ db_url }}"
api_key = "{{ api_key }}"

# Component 2: Health Check
trigger.http
route = "/health"
component = "health"

[component.health]
source = "target/wasm32-wasi/release/health.wasm"
description = "Health Check Endpoint"

# Component 3: Background Task (Redis Trigger)
trigger.redis
channel = "task-queue"
component = "task-processor"

[component.task-processor]
source = "target/wasm32-wasi/release/task_processor.wasm"
description = "Asynchronous task processing"

[component.task-processor.allowed_outbound_hosts]
hosts = ["https://api.external-service.com"]
```

## 2.3 Rust Spin Application Development

```rust
// Cargo.toml
[package]
name = "users-handler"
version = "1.0.0"
edition = "2021"

[lib]
crate-type = ["cdylib"]

[dependencies]
spin-sdk = "3.0"
serde = { version = "1", features = ["derive"] }
serde_json = "1"
anyhow = "1"
```

```rust
// src/lib.rs - Complete Spin HTTP Processor
use anyhow::Result;
use spin_sdk::{
    http::{
        IntoResponse, Method, Params, Request, Response, Router
    },
    http_component,
    key_value::Store,
    sqlite::{Connection, QueryResult, Value},
    variables,
};
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize, Clone)]
struct User {
    id: u64,
    username: String,
    email: String,
    created_at: String,
}

#[derive(Debug, Deserialize)]
struct CreateUserRequest {
    username: String,
    email: String,
}

#[derive(Debug, Serialize)]
struct ApiResponse<T> {
    success: bool,
    data: Option<T>,
    error: Option<String>,
    total: Option<usize>,
}

// Spin HTTP component entry point
#[http_component]
fn handle_request(req: Request) -> Result<impl IntoResponse> {
    let mut router = Router::new();
    
    // Register route
    router.get("/api/v1/users", list_users);
    router.get("/api/v1/users/:id", get_user);
    router.post("/api/v1/users", create_user);
    router.put("/api/v1/users/:id", update_user);
    router.delete("/api/v1/users/:id", delete_user);
    
    // Middleware: Logging
    println!("[{}] {} {}", 
        chrono_like_timestamp(),
        req.method(), 
        req.uri().path()
    );
    
    Ok(router.handle(req))
}

// Get user list
fn list_users(_req: Request, _params: Params) -> Result<impl IntoResponse> {
    let conn = Connection::open_default()?;
    
    let result = conn.execute(
        "SELECT id, username, email, created_at FROM users ORDER BY id DESC LIMIT 100",
        &[],
    )?;
    
    let users = rows_to_users(result);
    
    // Cache to KV Store
    let store = Store::open_default()?;
    let cache_key = "users:list";
    let cached = serde_json::to_vec(&users)?;
    store.set(cache_key, &cached)?;
    
    Ok(json_response(200, ApiResponse {
        success: true,
        data: Some(users.clone()),
        error: None,
        total: Some(users.len()),
    }))
}

// Get a single user
fn get_user(_req: Request, params: Params) -> Result<impl IntoResponse> {
    let id: u64 = params.get("id")
        .and_then(|s| s.parse().ok())
        .ok_or_else(|| anyhow::anyhow!("Invalid user ID"))?;
    
    // First check the key-value cache
    let store = Store::open_default()?;
    let cache_key = format!("user:{}", id);
    
    if let Some(cached) = store.get(&cache_key)? {
        if let Ok(user) = serde_json::from_slice::<User>(&cached) {
            return Ok(json_response(200, ApiResponse {
                success: true,
                data: Some(user),
                error: None,
                total: None,
            }));
        }
    }
    
    // Query from database
    let conn = Connection::open_default()?;
    let result = conn.execute(
        "SELECT id, username, email, created_at FROM users WHERE id = ?",
        &[Value::Integer(id as i64)],
    )?;
    
    let users = rows_to_users(result);
    
    match users.into_iter().next() {
        Some(user) => {
            // Cache results
            let cached = serde_json::to_vec(&user)?;
            store.set(&cache_key, &cached)?;
            
            Ok(json_response(200, ApiResponse {
                success: true,
                data: Some(user),
                error: None,
                total: None,
            }))
        }
        None => Ok(json_response(404, ApiResponse::<User> {
            success: false,
            data: None,
            Error: Some(format!("User {} does not exist", id)),
            total: None,
        })),
    }
}

// Create user
fn create_user(req: Request, _params: Params) -> Result<impl IntoResponse> {
    // Parse the request body
    let body = req.body();
    let create_req: CreateUserRequest = serde_json::from_slice(body)
        .map_err(|e| anyhow::anyhow!("Invalid request body: {}", e))?;
    
    // verify
    if create_req.username.is_empty() {
        return Ok(json_response(400, ApiResponse::<User> {
            success: false,
            data: None,
            Error: Some("Username cannot be empty".to_string()),
            total: None,
        }));
    }
    
    // Get the API key (from the Spin variable)
    let _api_key = variables::get("api_key")?;
    
    // Insert into database
    let conn = Connection::open_default()?;
    conn.execute(
        "INSERT INTO users (username, email, created_at) VALUES (?, ?, datetime('now'))",
        &[
            Value::Text(create_req.username.clone()),
            Value::Text(create_req.email.clone()),
        ],
    )?;
    
    // Get new user ID
    let id_result = conn.execute("SELECT last_insert_rowid()", &[])?;
    let id = id_result.rows.first()
        .and_then(|r| r.first())
        .and_then(|v| if let Value::Integer(n) = v { Some(*n as u64) } else { None })
        .unwrap_or(0);
    
    let user = User {
        id,
        username: create_req.username,
        email: create_req.email,
        created_at: "now".to_string(),
    };
    
    // Cache new users
    let store = Store::open_default()?;
    store.set(
        &format!("user:{}", id),
        &serde_json::to_vec(&user)?,
    )?;
    
    Ok(json_response(201, ApiResponse {
        success: true,
        data: Some(user),
        error: None,
        total: None,
    }))
}

// Update user
fn update_user(req: Request, params: Params) -> Result<impl IntoResponse> {
    let id: u64 = params.get("id")
        .and_then(|s| s.parse().ok())
        .ok_or_else(|| anyhow::anyhow!("Invalid user ID"))?;
    
    let body = req.body();
    let update_req: CreateUserRequest = serde_json::from_slice(body)?;
    
    let conn = Connection::open_default()?;
    conn.execute(
        "UPDATE users SET username = ?, email = ? WHERE id = ?",
        &[
            Value::Text(update_req.username.clone()),
            Value::Text(update_req.email.clone()),
            Value::Integer(id as i64),
        ],
    )?;
    
    // Clear cache
    let store = Store::open_default()?;
    store.delete(&format!("user:{}", id))?;
    store.delete("users:list")?;
    
    let user = User {
        id,
        username: update_req.username,
        email: update_req.email,
        created_at: "updated".to_string(),
    };
    
    Ok(json_response(200, ApiResponse {
        success: true,
        data: Some(user),
        error: None,
        total: None,
    }))
}

// Delete user
fn delete_user(_req: Request, params: Params) -> Result<impl IntoResponse> {
    let id: u64 = params.get("id")
        .and_then(|s| s.parse().ok())
        .ok_or_else(|| anyhow::anyhow!("Invalid user ID"))?;
    
    let conn = Connection::open_default()?;
    conn.execute(
        "DELETE FROM users WHERE id = ?",
        &[Value::Integer(id as i64)],
    )?;
    
    // Clear cache
    let store = Store::open_default()?;
    store.delete(&format!("user:{}", id))?;
    store.delete("users:list")?;
    
    Ok(Response::builder()
        .status(204)
        .body(())
        .build())
}

// Helper function: Line to User
fn rows_to_users(result: QueryResult) -> Vec<User> {
    result.rows.into_iter().filter_map(|row| {
        if row.len() >= 4 {
            Some(User {
                id: if let Value::Integer(n) = &row[0] { *n as u64 } else { 0 },
                username: if let Value::Text(s) = &row[1] { s.clone() } else { String::new() },
                email: if let Value::Text(s) = &row[2] { s.clone() } else { String::new() },
                created_at: if let Value::Text(s) = &row[3] { s.clone() } else { String::new() },
            })
        } else {
            None
        }
    }).collect()
}

// JSON response construction
fn json_response<T: Serialize>(status: u16, body: T) -> Response {
    let json = serde_json::to_vec(&body).unwrap_or_default();
    Response::builder()
        .status(status)
        .header("Content-Type", "application/json")
        .header("X-Powered-By", "SpinKube")
        .body(json)
        .build()
}

fn chrono_like_timestamp() -> String {
    "2025-03-04T00:00:00Z".to_string() // The actual clock should be WASI.
}
```

---

<!-- chunk: 3. SpinKube Architecture -->## 3. SpinKube Architecture

## 3.1 Overall Architecture

```mermaid
graph TD
    subgraph "user layer"
        A[kubectl apply SpinApp] --> B[Kubernetes API]
        C[spin kube scaffold] --> B
    end
    
    subgraph "control layer"
        B --> D[spin-operator Deployment]
        D --> E[SpinApp Reconciler]
        E --> F [Create/Update Deployment]
        E --> G [Manage Service]
        E --> H [Configure HPA/KEDA]
    end
    
    subgraph "Runtime Layer"
        F --> I[Pod with runtimeClassName: spin]
        I --> J[containerd-shim-spin-v2]
        J --> K [Wasmtime Engine]
        K --> L [Spin ​​component running]
    end
    
    subgraph "Storage layer"
        L --> M[KV Store Backend]
        L --> N[SQLite]
        L --> O[Redis]
        L --> P[MySQL/Postgres]
        
        M --> Q[Redis Cluster]
        M --> R[Memcached]
        M --> S [Memory Storage]
    end
    
    subgraph "scaling layer"
        T[KEDA] --> E
        T --> U{Trigger Detection}
        U --> V [HTTP Request Count]
        U --> W [Message Queue]
        U --> X [Timer]
    end
```

## 3.2 Spin-operator Controller

```
spin-operator workflow

1. Watch SpinApp CRD changes
   ↓
2. Verify the SpinApp specification.
   ↓
3. Pull the OCI Wasm image (obtain the spin.toml and .wasm files)
   ↓
4. Generate Kubernetes resources:
   ├── Deployment (Specify runtimeClassName: spin)
   ├── Service
   ├── ConfigMap（spin.toml）
   ├── Secret (Sensitive Variable)
   └── ScaledObject/HPA (if auto-scaling is configured)
   ↓
5. Reconcile:
   ├── Check the actual state vs. the expected state
   ├── Update SpinApp Status
   └── Handling errors and retrying
```

```go
// Core logic of spin-operator Reconciler (simplified)
package controller

import (
    "context"
    "fmt"
    
    spinv1alpha1 "github.com/spinkube/spin-operator/api/v1alpha1"
    appsv1 "k8s.io/api/apps/v1"
    corev1 "k8s.io/api/core/v1"
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "sigs.k8s.io/controller-runtime/pkg/client"
    "sigs.k8s.io/controller-runtime/pkg/reconcile"
)

type SpinAppReconciler struct {
    client.Client
    SpinImageCache *ImageCache
}

func (r *SpinAppReconciler) Reconcile(
    ctx context.Context,
    req reconcile.Request,
) (reconcile.Result, error) {
    
    // Get SpinApp resources
    spinApp := &spinv1alpha1.SpinApp{}
    if err := r.Get(ctx, req.NamespacedName, spinApp); err != nil {
        return reconcile.Result{}, client.IgnoreNotFound(err)
    }
    
    // Ensure the Deployment exists
    if err := r.reconcileDeployment(ctx, spinApp); err != nil {
        return reconcile.Result{}, fmt.Errorf("Reconciliation Deployment failed: %w", err)
    }
    
    // Ensure the Service exists
    if err := r.reconcileService(ctx, spinApp); err != nil {
        return reconcile.Result{}, fmt.Errorf("Service reconciliation failed: %w", err)
    }
    
    // Configure automatic scaling
    if spinApp.Spec.EnableAutoscaling {
        if err := r.reconcileKEDA(ctx, spinApp); err != nil {
            return reconcile.Result{}, fmt.Errorf("Reconciliation with KEDA failed: %w", err)
        }
    }
    
    // Update status
    spinApp.Status.ReadyReplicas = r.getReadyReplicas(ctx, spinApp)
    spinApp.Status.Phase = "Ready"
    r.Status().Update(ctx, spinApp)
    
    return reconcile.Result{}, nil
}

func (r *SpinAppReconciler) reconcileDeployment(
    ctx context.Context,
    spinApp *spinv1alpha1.SpinApp,
) error {
    
    deployment := &appsv1.Deployment{
        ObjectMeta: metav1.ObjectMeta{
            Name:      spinApp.Name,
            Namespace: spinApp.Namespace,
        },
        Spec: appsv1.DeploymentSpec{
            Replicas: &spinApp.Spec.Replicas,
            Selector: &metav1.LabelSelector{
                MatchLabels: map[string]string{
                    "app": spinApp.Name,
                },
            },
            Template: corev1.PodTemplateSpec{
                ObjectMeta: metav1.ObjectMeta{
                    Labels: spinApp.Spec.PodLabels,
                    Annotations: map[string]string{
                        "module.wasm.image/variant": "spin",
                    },
                },
                Spec: corev1.PodSpec{
                    RuntimeClassName: &spinApp.Spec.RuntimeClassName,
                    Containers: []corev1.Container{
                        {
                            Name:  spinApp.Name,
                            Image: spinApp.Spec.Image,
                            Env:   spinApp.Spec.Env,
                            Resources: spinApp.Spec.Resources,
                            Ports: []corev1.ContainerPort{
                                {ContainerPort: 80},
                            },
                        },
                    },
                },
            },
        },
    }
    
    // CreateOrUpdate mode
    return r.CreateOrUpdate(ctx, deployment)
}
```

---

<!-- chunk: 4. SpinApp CRD -->## 4. SpinApp CRD

## 4.1 SpinApp Resource Definition

```yaml
# SpinApp CRD Complete Example
apiVersion: core.spinoperator.dev/v1alpha1
kind: SpinApp
metadata:
  name: users-api
  namespace: production
  labels:
    app: users-api
    team: backend
    version: v2.1.0
  annotations:
    Description: "User Management API Service"
spec:
  # OCI Mirror (includes Wasm module and spin.toml)
  image: "ghcr.io/myorg/users-api:v2.1.0"
  
  # Runtime class used
  executor: containerd-shim-spin
  
  # Number of replicas (this is the initial value if auto-scaling is enabled)
  replicas: 3
  
  # Enable automatic scaling
  enableAutoscaling: true
  
  # Environment Variables
  env:
  - name: SPIN_LOG_LEVEL
    value: "info"
  - name: DB_URL
    valueFrom:
      secretKeyRef:
        name: db-secrets
        key: url
  - name: REDIS_URL
    valueFrom:
      configMapKeyRef:
        name: infra-config
        key: redis_url
  
  # Resource Allocation
  resources:
    requests:
      memory: "16Mi"
      cpu: "50m"
    limits:
      memory: "128Mi"
      cpu: "500m"
  
  # Health Check
  livenessProbe:
    httpGet:
      path: /health
      port: 80
    initialDelaySeconds: 3
    periodSeconds: 10
  
  readinessProbe:
    httpGet:
      path: /ready
      port: 80
    initialDelaySeconds: 1
    periodSeconds: 5
  
  # Storage Volume
  volumes:
  - name: config-data
    configMap:
      name: app-config
  
  volumeMounts:
  - name: config-data
    mountPath: /config
  
  # Pod annotation
  podAnnotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "9090"
  
  # Node Selection
  nodeSelector:
    runtime.wasm/enabled: "true"
  
  # Tolerance
  tolerations:
  - key: "runtime.wasm/enabled"
    operator: "Exists"
    effect: "NoSchedule"

# Status (automatically maintained by the operator)
status:
  conditions:
  - type: Ready
    status: "True"
    lastTransitionTime: "2025-03-04T00:00:00Z"
    reason: "SpinAppReady"
    message: "All 3 replicas are ready"
  activeReplicas: 3
  readyReplicas: 3
  phase: "Ready"
```

## 4.2 SpinApp Autoscaling Configuration

```yaml
# SpinApp with KEDA
apiVersion: core.spinoperator.dev/v1alpha1
kind: SpinApp
metadata:
  name: api-autoscale
  namespace: production
spec:
  image: "ghcr.io/myorg/api:latest"
  executor: containerd-shim-spin
  replicas: 1 # Initial replica (KEDA can be reduced to 0)
  enableAutoscaling: true
  
  # Automatic scaling configuration
  autoscalingConfig:
    minReplicas: 0 # Allows scaling down to 0!
    maxReplicas: 50
    
    # Stretch Trigger
    triggers:
    # HTTP Request Triggers (Based on Prometheus Metrics)
    - type: prometheus
      metadata:
        serverAddress: http://prometheus.monitoring.svc:9090
        metricName: spin_requests_per_second
        query: |
          sum(rate(spin_http_requests_total{app="api-autoscale"}[1m]))
        threshold: "50"
    
    # Cooldown time configuration
    cooldownPeriod: 300 # Shrink to 0 after 5 minutes of no requests.
    pollingInterval: 10 # Check every 10 seconds
```

## 4.3 SpinAppExec CRD / Execution Configuration

```yaml
# SpinAppExec - Defines the execution environment for SpinApp
apiVersion: core.spinoperator.dev/v1alpha1
kind: SpinAppExec
metadata:
  name: production-exec
  namespace: production
spec:
  # Associated SpinApp
  spinAppRef:
    name: users-api
  
  # Executor Configuration
  executor:
    name: containerd-shim-spin
    runtimeClassName: wasmtime-spin
    
    # Spin specific configuration
    spinConfig:
      # Allowed external services
      allowedOutboundHosts:
      - "https://auth.internal.example.com"
      - "https://api.sendgrid.com"
      
      # KV Store Backend Configuration
      keyValueStores:
      - label: "default"
        provider:
          type: redis
          redisUrl: "redis://redis.default.svc:6379"
      
      # SQLite database configuration
      sqliteDatabases:
      - label: "users_db"
        provider:
          type: libsql
          url: "libsql://users.turso.io"
          token:
            secretKeyRef:
              name: turso-secret
              key: token
```

---

<!-- chunk: 5. Installation and Configuration-->## 5. Installation and Configuration

## 5.1 Installing SpinKube using Helm

> ⚠️ **🟡 Medium-Risk Change** — This involves changing the status of cluster resources. It is recommended to first confirm using `--dry-run` or `diff`.
> - `helm upgrade/install`: Deploy/upgrade release
> - `kubectl apply/create/replace`: Creates/modifies cluster resources

``` bash
# 🟡 Medium Risk: Will modify cluster/resource status. Please confirm the target, scope of impact, and authorization before execution.
# Add SpinKube Helm repository
helm repo add spinkube https://spinkube.dev/helm-charts
helm repo update

# Install spin-operator
helm upgrade --install spin-operator \
  spinkube/spin-operator \
  --namespace spin-operator \
  --create-namespace \
  --version 0.3.0 \
  --wait

# Verify Installation
kubectl -n spin-operator get pods
# NAME                                    READY   STATUS    RESTARTS
# spin-operator-controller-manager-xxx   1/1     Running   0

# Install CRD
kubectl apply -f https://github.com/spinkube/spin-operator/releases/download/v0.3.0/spin-operator.crds.yaml

# Verify CRD
kubectl get crd | grep spin
# spinapps.core.spinoperator.dev
# spinappexecs.core.spinoperator.dev
```
> ⚠️ **🟡 Medium-Risk Change** — This involves changing the status of cluster resources. It is recommended to first confirm using `--dry-run` or `diff`.
> - `kubectl apply/create/replace`: Creates/modifies cluster resources

``` bash
# 🟡 Medium Risk: Will modify cluster/resource status. Please confirm the target, scope of impact, and authorization before execution.
# Install containerd-shim-spin (requires execution on each worker node)
SHIM_VERSION="v0.15.1"

# Use DaemonSet for automatic installation (recommended)
kubectl apply -f - <<EOF
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: spin-shim-installer
  namespace: kube-system
spec:
  selector:
    matchLabels:
      app: spin-shim-installer
  template:
    metadata:
      labels:
        app: spin-shim-installer
    spec:
      hostPID: true
      initContainers:
      - name: installer
        image: ghcr.io/spinkube/containerd-shim-spin:${SHIM_VERSION}
        command: ["/bin/sh", "-c"]
        args:
        - |
          cp /spin-shim/containerd-shim-spin-v2 /host/usr/local/bin/
          chmod +x /host/usr/local/bin/containerd-shim-spin-v2
          echo "Spin shim installation complete"
        volumeMounts:
        - name: host-bin
          mountPath: /host/usr/local/bin
        securityContext:
          privileged: true
      containers:
      - name: pause
        image: gcr.io/google_containers/pause:3.6
      volumes:
      - name: host-bin
        hostPath:
          path: /usr/local/bin
      tolerations:
      - operator: Exists
EOF
```
## 5.2 配置 RuntimeClass / Configure RuntimeClass

> ⚠️ **🟡 Medium-Risk Change** — This involves changing the status of cluster resources. It is recommended to first confirm using `--dry-run` or `diff`.
> - `kubectl apply/create/replace`: Creates/modifies cluster resources
> - `kubectl delete`: Deletes a resource (which can be reconstructed from a declarative manifest).
> - `kubectl label/annotate`: This metadata may affect selectors/controllers.

``` bash
# 🟡 Medium Risk: Will modify cluster/resource status. Please confirm the target, scope of impact, and authorization before execution.
# Using the official RuntimeClass configuration
kubectl apply -f - <<EOF
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: wasmtime-spin
handler: spin
scheduling:
  nodeClassification:
    tolerations:
    - effect: NoSchedule
      key: spin.fermyon.com/enabled
      operator: Exists
    nodeSelector:
      matchLabels:
        spin.fermyon.com/enabled: "true"
EOF

# Mark Node
kubectl label node worker-1 spin.fermyon.com/enabled=true

# verify
kubectl run test-spin \
  --image=ghcr.io/fermyon/spin-wasm-hello:latest \
  --overrides='{"spec":{"runtimeClassName":"wasmtime-spin"}}' \
  --restart=Never

kubectl get pod test-spin
kubectl delete pod test-spin
```
## 5.3 Install KEDA

> ⚠️ **🟡 Medium-Risk Change** — This involves changing the status of cluster resources. It is recommended to first confirm using `--dry-run` or `diff`.
> - `helm upgrade/install`: Deploy/upgrade release

``` bash
# 🟡 Medium Risk: Will modify cluster/resource status. Please confirm the target, scope of impact, and authorization before execution.
# Install KEDA using Helm
helm repo add kedacore https://kedacore.github.io/charts
helm repo update

helm install keda kedacore/keda \
  --namespace keda \
  --create-namespace \
  --version 2.13.0

# Verify KEDA installation
kubectl -nkeda get pods
# NAME                                      READY   STATUS
# keda-operator-xxx                         2/2     Running
# keda-operator-metrics-apiserver-xxx       1/1     Running

# Install the KEDA HTTP Add-on (optional, for HTTP scale-to-zero)
helm install keda-add-ons-http \
  kedacore/keda-add-ons-http \
  --namespace keda

# verify
kubectl -n keda get pods | grep http
```
---

<!-- chunk: 6. HTTP Triggers --> ## 6. HTTP Triggers

## 6.1 HTTP Routing Configuration

```toml
# spin.toml - Complex HTTP Routing Example
spin_manifest_version = 2

[application]
name = "advanced-api"
version = "2.0.0"

[application.trigger.http]
base = "/api/v2"

# Precise path matching
trigger.http
route = "/ping"
component = "ping"

# Wildcard Routing
trigger.http
route = "/users/..."
component = "users"

# Path parameters
trigger.http
route = "/products/:id"
component = "product-detail"

# Management Interface
trigger.http
route = "/admin/..."
component = "admin"

[component.admin]
source = "admin.wasm"
[component.admin.trigger]
# Only POST and DELETE are allowed
executor = { type = "http" }
```

## 6.2 HTTP Middleware Pattern

```rust
// src/lib.rs - HTTP Middleware Implementation
use spin_sdk::http::{
    IntoResponse, Request, Response,
};
use spin_sdk::http_component;
use anyhow::Result;

// Middleware chain
struct MiddlewareChain {
    middlewares: Vec<Box<dyn Middleware>>,
}

trait Middleware {
    fn handle(&self, req: &Request, next: &dyn Fn(&Request) -> Response) -> Response;
}

// Authentication Middleware
struct AuthMiddleware {
    api_key: String,
}

impl Middleware for AuthMiddleware {
    fn handle(&self, req: &Request, next: &dyn Fn(&Request) -> Response) -> Response {
        // Check authentication header
        let auth = req.header("X-API-Key")
            .and_then(|v| v.as_str());
        
        if auth != Some(self.api_key.as_str()) {
            return Response::builder()
                .status(401)
                .header("Content-Type", "application/json")
                .body(r#"{"error":"Unauthorized"}"#)
                .build();
        }
        
        next(req)
    }
}

// Rate limiting middleware (using KV Store counting)
struct RateLimitMiddleware {
    max_requests: u32,
    window_seconds: u64,
}

impl Middleware for RateLimitMiddleware {
    fn handle(&self, req: &Request, next: &dyn Fn(&Request) -> Response) -> Response {
        use spin_sdk::key_value::Store;
        
        // Get client IP
        let ip = req.header("X-Forwarded-For")
            .and_then(|v| v.as_str())
            .unwrap_or("unknown");
        
        let store = Store::open_default().unwrap();
        let key = format!("ratelimit:{}:{}", ip, 
            current_window(self.window_seconds));
        
        // Get the current count
        let count: u32 = store.get(&key)
            .ok()
            .flatten()
            .and_then(|v| String::from_utf8(v).ok())
            .and_then(|s| s.parse().ok())
            .unwrap_or(0);
        
        if count >= self.max_requests {
            return Response::builder()
                .status(429)
                .header("X-RateLimit-Limit", self.max_requests.to_string())
                .header("X-RateLimit-Remaining", "0")
                .body(r#"{"error":"Requests too frequent"}"#)
                .build();
        }
        
        // Increment the count
        store.set(&key, (count + 1).to_string().as_bytes()).ok();
        
        let mut response = next(req);
        // Add a rate limiting header to the response
        response
    }
}

// CORS Middleware
struct CorsMiddleware {
    allowed_origins: Vec<String>,
}

impl Middleware for CorsMiddleware {
    fn handle(&self, req: &Request, next: &dyn Fn(&Request) -> Response) -> Response {
        // Handling OPTIONS preflight requests
        if req.method() == spin_sdk::http::Method::Options {
            return Response::builder()
                .status(204)
                .header("Access-Control-Allow-Origin", "*")
                .header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
                .header("Access-Control-Allow-Headers", "Content-Type, Authorization, X-API-Key")
                .header("Access-Control-Max-Age", "86400")
                .body(())
                .build();
        }
        
        let mut response = next(req);
        // Add CORS Header
        response
    }
}

fn current_window(window_seconds: u64) -> u64 {
    // Simplified implementation (WASI clock should actually be used)
    0 / window_seconds
}

#[http_component]
fn handle_request(req: Request) -> Result<impl IntoResponse> {
    // Get authentication key
    let api_key = spin_sdk::variables::get("api_key")
        .unwrap_or_default();
    
    // Authentication check
    let auth = req.header("X-API-Key")
        .and_then(|v| v.as_str().map(|s| s.to_string()));
    
    if auth.as_deref() != Some(&api_key) && !req.uri().path().contains("/public") {
        return Ok(Response::builder()
            .status(401)
            .body(r#"{"error":"Unauthorized","code":401}"#)
            .build());
    }
    
    // Routing to the handler function
    let path = req.uri().path();
    let response = match (req.method(), path) {
        (spin_sdk::http::Method::Get, "/api/v2/ping") => {
            Response::builder()
                .status(200)
                .body(r#"{"status":"ok","runtime":"SpinKube"}"#)
                .build()
        }
        _ => {
            Response::builder()
                .status(404)
                .body(r#"{"error":"Route not found"}"#)
                .build()
        }
    };
    
    Ok(response)
}
```

## 6.3 Outbound HTTP Requests

```rust
// Spin outbound HTTP client
use spin_sdk::http::{IntoResponse, Request, Response};
use spin_sdk::http_component;
use spin_sdk::http_client;
use anyhow::Result;

#[http_component]
fn handle_request(req: Request) -> Result<impl IntoResponse> {
    // Outbound HTTP GET request
    let response = http_client::send(
        Request::builder()
            .method("GET")
            .uri("https://api.github.com/repos/spinkube/spin-operator")
            .header("User-Agent", "SpinKube-App/1.0")
            .header("Accept", "application/vnd.github.v3+json")
            .body(())?
    )?;
    
    let status = response.status();
    let body = response.into_body();
    
    Ok(Response::builder()
        .status(200)
        .header("Content-Type", "application/json")
        .body(format!(
            r#"{{"upstream_status": {}, "data": {}}}"#,
            status,
            String::from_utf8_lossy(&body)
        ))
        .build())
}
```

---

<!-- chunk: 7. KEDA Integration and Scale-to-Zero -->## 7. KEDA Integration and Scale-to-Zero

## 7.1 Scale-to-Zero 原理 / Scale-to-Zero Principle

```mermaid
sequenceDiagram
    Participant Client as Client
    participant KEDA_HTTP as KEDA HTTP 代理
    participant KEDA as KEDA Operator
    participant K8s as Kubernetes
    participant Spin as Spin Pod

    Note over Spin: Initial state: 0 copies
    
    Client->>KEDA_HTTP: HTTP Request
    KEDA_HTTP->>KEDA: Request detected, needs to be scaled up.
    KEDA->>K8s: Scale Deployment to 1
    Kubernetes Spin: Create a Pod (starts in < 1ms)
    
    Note over Spin: Wasm has extremely fast cold starts!
    
    KEDA_HTTP->>Spin: Forwarding requests
    Spin->>KEDA_HTTP: Response
    KEDA_HTTP->>Client: Returns response
    
    Note over KEDA: No requests for 300 seconds...
    
    KEDA->>K8s: Scale Deployment to 0
    K8s->>Spin: Destroy Pods
    Note over Spin: Status: 0 copies (saving resources)
```

## 7.2 KEDA ScaledObject 配置 / ScaledObject Configuration

```yaml
# HTTP-triggered scale-to-zero
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: users-api-scaler
  namespace: production
  annotations:
    # KEDA Annotations
    scaledobject.keda.sh/transfer-hpa-ownership: "true"
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: users-api
  
  # Allow shrinking to 0
  minReplicaCount: 0
  maxReplicaCount: 100
  
  # Scaling Strategy
  pollingInterval: 10 # Evaluate every 10 seconds
  cooldownPeriod: 300 # Reduces to 0 in 5 minutes
  
  # Pre-expansion time window (to reduce the impact of cold start)
  initialCooldownPeriod: 0
  
  # Advanced scaling configuration
  advanced:
    # Fast expansion, slow reduction
    scalingModifiers:
      formula: "max(target * 1.5, 1)"
    
    horizontalPodAutoscalerConfig:
      behavior:
        scaleUp:
          stabilizationWindowSeconds: 0 # Expand window size immediately
          policies:
          - type: Pods
            value: 10
            periodSeconds: 10
        scaleDown:
          StabilizationWindowSeconds: 300 # Stabilize the window again after 5 minutes.
          policies:
          - type: Percent
            value: 10
            periodSeconds: 60
  
  triggers:
  # Prometheus Metric Trigger
  - type: prometheus
    metadata:
      serverAddress: http://prometheus.monitoring.svc:9090
      metricName: spin_active_requests
      query: |
        sum(spin_http_active_requests{app="users-api"}) or vector(0)
      threshold: "5" # Maximum of 5 concurrent requests per instance
      activationThreshold: "1" # Activate with 1 request
  
  # CPU Trigger (Backup)
  - type: cpu
    metricType: Utilization
    metadata:
      value: "70" # Expand capacity when CPU utilization is 70%

---
# HTTPScaledObject (KEDA HTTP Add-on) - A simpler HTTP scale-to-zero solution
apiVersion: http.keda.sh/v1alpha1
kind: HTTPScaledObject
metadata:
  name: users-api-http-scaler
  namespace: production
spec:
  hosts:
  - users-api.production.svc.cluster.local
  - users.example.com # External domain
  
  # Maximum number of pending requests that can be handled per instance
  targetPendingRequests: 100
  
  scaleTargetRef:
    deployment: users-api
    service: users-api
    port: 80
  
  replicas:
    min: 0
    max: 50
```

## 7.3 Pre-scaling and Warmup

```yaml
# CronJob warms up Wasm instances before peak hours
apiVersion: batch/v1
kind: CronJob
metadata:
  name: spin-warmup
  namespace: production
spec:
  # Warm-up begins at 8:50 AM every morning (10 minutes before the 9:00 AM peak).
  schedule: "50 8 * * 1-5"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: warmup
            image: curlimages/curl:latest
            command:
            - sh
            - -c
            - |
              # Send a request in advance to wake up the Wasm instance
              for i in $(seq 1 5); do
                curl -s http://users-api.production.svc/health
                sleep 1
              done
              echo "Preheating complete"
          restartPolicy: OnFailure

---
# Implementing timed pre-expansion using KEDA Cron triggers
apiVersion: keda.sh/v1alpha1
kind: ScaledObject
metadata:
  name: users-api-cron-scaler
spec:
  scaleTargetRef:
    name: users-api
  minReplicaCount: 0
  maxReplicaCount: 20
  triggers:
  - type: cron
    metadata:
      timezone: "Asia/Shanghai"
      start: "50 8 * * 1-5" # Expand capacity on weekdays at 8:50
      end: "0 22 * ​​* 1-5" # Reduce capacity at 22:00 on weekdays
      desiredReplicas: "5" # Maintain 5 instances
  
  # Retain Prometheus triggers as well
  - type: prometheus
    metadata:
      serverAddress: http://prometheus.monitoring.svc:9090
      metricName: spin_requests
      query: rate(spin_http_requests_total[1m])
      threshold: "50"
```

---

<!-- chunk: 8. Storage System Integration-->## 8. Storage System Integration

## 8.1 Spin Storage Architecture

```mermaid
graph TD
    subgraph "Spin Application Storage Interface"
        A[KV Store API] --> B{Storage backend selection}
        C[SQLite API] --> D{Database Backend}
        E [Outbound HTTP] --> F [External Storage Service]
        
        B --> G[Redis]
        B --> H[Memcached]
        B --> I [Memory Storage]
        B --> J [Custom Backend]
        
        D --> K [Embedded SQLite]
        D --> L[libSQL/Turso]
        D --> M[MySQL via HTTP]
        D --> N[Postgres via HTTP]
    end
```

## 8.2 KV Store Configuration

```yaml
# Kubernetes ConfigMap - Spin KV Store Configuration
apiVersion: v1
kind: ConfigMap
metadata:
  name: spin-kv-config
  namespace: production
data:
  # Runtime config format
  runtime-config.toml: |
    # Default KV Store uses Redis
    [key_value_store.default]
    type = "redis"
    url = "redis://redis-master.default.svc:6379"
    
    # Session KV Store using a standalone Redis
    [key_value_store.sessions]
    type = "redis"
    url = "redis://sessions-redis.default.svc:6379"
    
    # Caching KV Store using Memcached
    # [key_value_store.cache]
    # type = "memcached"
    # url = "memcached://memcached.default.svc:11211"

---
# SpinApp using RuntimeConfig
apiVersion: core.spinoperator.dev/v1alpha1
kind: SpinApp
metadata:
  name: kv-demo
spec:
  image: ghcr.io/myorg/kv-demo:latest
  executor: containerd-shim-spin
  replicas: 2
  
  # Mount runtime configuration
  runtimeConfig:
    loadFromSecret: spin-runtime-secret
    # Or from ConfigMap
    # loadFromConfigMap: spin-kv-config
  
  env:
  - name: REDIS_URL
    valueFrom:
      secretKeyRef:
        name: redis-secret
        key: url
```

---

<!-- chunk: 9. Redis and KV Store -->## 9. Redis and KV Store

## 9.1 KV Store Operations

```rust
// KV Store Complete Operation Example
use spin_sdk::http::{IntoResponse, Request, Response};
use spin_sdk::http_component;
use spin_sdk::key_value::{Error, Store};
use serde::{Deserialize, Serialize};
use anyhow::Result;

#[derive(Debug, Serialize, Deserialize)]
struct Session {
    user_id: u64,
    username: String,
    expires_at: u64,
    metadata: std::collections::HashMap<String, String>,
}

// Session Manager (using KV Store)
struct SessionManager {
    big: Big,
    ttl_seconds: u64,
}

impl SessionManager {
    fn new() -> Result<Self> {
        Ok(Self {
            store: Store::open("sessions")
                .map_err(|e| anyhow::anyhow!("Unable to open KV Store: {:?}", e))?,
            ttl_seconds: 3600, // 1 hour
        })
    }
    
    fn create_session(&self, user_id: u64, username: &str) -> Result<String> {
        // Generate Session ID
        let session_id = generate_session_id();
        
        let session = Session {
            user_id,
            username: username.to_string(),
            expires_at: current_time() + self.ttl_seconds,
            metadata: std::collections::HashMap::new(),
        };
        
        let data = serde_json::to_vec(&session)?;
        self.store.set(&format!("session:{}", session_id), &data)
            .map_err(|e| anyhow::anyhow!("Failed to save session: {:?}", e))?;
        
        Ok(session_id)
    }
    
    fn get_session(&self, session_id: &str) -> Result<Option<Session>> {
        match self.store.get(&format!("session:{}", session_id)) {
            Ok(Some(data)) => {
                let session: Session = serde_json::from_slice(&data)?;
                
                // Check if it has expired
                if session.expires_at < current_time() {
                    self.delete_session(session_id)?;
                    return Ok(None);
                }
                
                Ok(Some(session))
            }
            Ok(None) => Ok(None),
            Err(e) => Err(anyhow::anyhow!("Failed to read session: {:?}", e)),
        }
    }
    
    fn delete_session(&self, session_id: &str) -> Result<()> {
        self.store.delete(&format!("session:{}", session_id))
            .map_err(|e| anyhow::anyhow!("Failed to delete session: {:?}", e))
    }
    
    fn list_sessions(&self) -> Result<Vec<String>> {
        // Note: Listing all keys can be slow and should be avoided in production.
        self.store.get_keys()
            .map_err(|e| anyhow::anyhow!("Failed to list keys: {:?}", e))
            .map(|keys| {
                keys.into_iter()
                    .filter(|k| k.starts_with("session:"))
                    .collect()
            })
    }
    
    fn refresh_session(&self, session_id: &str) -> Result<()> {
        if let Some(mut session) = self.get_session(session_id)? {
            session.expires_at = current_time() + self.ttl_seconds;
            let data = serde_json::to_vec(&session)?;
            self.store.set(&format!("session:{}", session_id), &data)
                .map_err(|e| anyhow::anyhow!("Failed to refresh session: {:?}", e))?;
        }
        Ok(())
    }
}

#[http_component]
fn handle_request(req: Request) -> Result<impl IntoResponse> {
    let manager = SessionManager::new()?;
    
    let path = req.uri().path().to_string();
    
    match path.as_str() {
        "/session/create" => {
            let session_id = manager.create_session(12345, "alice")?;
            Ok(Response::builder()
                .status(201)
                .header("Set-Cookie", format!("session={}; HttpOnly; Secure; SameSite=Strict", session_id))
                .body(format!(r#"{{"session_id":"{}"}}"#, session_id))
                .build())
        }
        _ if path.starts_with("/session/") => {
            let session_id = &path["/session/".len()..];
            match manager.get_session(session_id)? {
                Some(session) => Ok(Response::builder()
                    .status(200)
                    .header("Content-Type", "application/json")
                    .body(serde_json::to_vec(&session)?)
                    .build()),
                None => Ok(Response::builder()
                    .status(404)
                    .body(r#"{"error":"Session does not exist or has expired"}"#)
                    .build()),
            }
        }
        _ => Ok(Response::builder()
            .status(404)
            .body(r#"{"error":"Not found"}"#)
            .build()),
    }
}

fn generate_session_id() -> String {
    // Simplified implementation
    use std::collections::hash_map::DefaultHasher;
    use std::hash::{Hash, Hasher};
    let mut hasher = DefaultHasher::new();
    "session".hash(&mut hasher);
    format!("{:x}", hasher.finish())
}

fn current_time() -> u64 {
    0 // The WASI clock API should actually be used.
}
```

## 9.2 Redis Backend Deployment

```yaml
# Deploy Redis for SpinKube
apiVersion: apps/v1
kind: Deployment
metadata:
  name: redis
  namespace: production
spec:
  replicas: 1
  selector:
    matchLabels:
      app: redis
  template:
    metadata:
      labels:
        app: redis
    spec:
      containers:
      - name: redis
        image: redis:7-alpine
        command:
        - redis-server
        - --requirepass
        - $(REDIS_PASSWORD)
        - --maxmemory
        - 256mb
        - --maxmemory-policy
        - allkeys-lru
        - --save
        - "" # Disable RDB persistence (pure caching mode)
        env:
        - name: REDIS_PASSWORD
          valueFrom:
            secretKeyRef:
              name: redis-secret
              key: password
        ports:
        - containerPort: 6379
        resources:
          requests:
            memory: "64Mi"
            cpu: "100m"
          limits:
            memory: "256Mi"
            cpu: "500m"
        livenessProbe:
          exec:
            command:
            - redis-cli
            - ping
          initialDelaySeconds: 5
          periodSeconds: 10
        volumeMounts:
        - name: redis-data
          mountPath: /data
      volumes:
      - name: redis-data
        emptyDir: {}

---
apiVersion: v1
kind: Service
metadata:
  name: redis
  namespace: production
spec:
  selector:
    app: redis
  ports:
  - port: 6379
    targetPort: 6379
```

---

<!-- chunk: 10. SQLite Integration-->## 10. SQLite Integration

## 10.1 SQLite Database Operations

```rust
// Complete example of Spin SQLite operation
use spin_sdk::sqlite::{Connection, QueryResult, Value};
use anyhow::Result;

struct UserRepository {
    conn: Connection,
}

impl UserRepository {
    fn new() -> Result<Self> {
        let conn = Connection::open_default()?;
        
        // Initialize table structure
        conn.execute(
            "CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'user',
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
            )",
            &[],
        )?;
        
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_users_email ON users(email)",
            &[],
        )?;
        
        Ok(Self { conn })
    }
    
    fn create(&self, username: &str, email: &str, password_hash: &str) -> Result<u64> {
        self.conn.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (?, ?, ?)",
            &[
                Value::Text(username.to_string()),
                Value::Text(email.to_string()),
                Value::Text(password_hash.to_string()),
            ],
        )?;
        
        let result = self.conn.execute(
            "SELECT last_insert_rowid()",
            &[],
        )?;
        
        Ok(result.rows.first()
            .and_then(|r| r.first())
            .and_then(|v| if let Value::Integer(n) = v { Some(*n as u64) } else { None })
            .unwrap_or(0))
    }
    
    fn find_by_id(&self, id: u64) -> Result<Option<UserRow>> {
        let result = self.conn.execute(
            "SELECT id, username, email, role, created_at FROM users WHERE id = ?",
            &[Value::Integer(id as i64)],
        )?;
        
        Ok(result.rows.into_iter().next().map(UserRow::from_row))
    }
    
    fn find_by_email(&self, email: &str) -> Result<Option<UserRow>> {
        let result = self.conn.execute(
            "SELECT id, username, email, role, created_at FROM users WHERE email = ?",
            &[Value::Text(email.to_string())],
        )?;
        
        Ok(result.rows.into_iter().next().map(UserRow::from_row))
    }
    
    fn update_role(&self, id: u64, role: &str) -> Result<bool> {
        let result = self.conn.execute(
            "UPDATE users SET role = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
            &[
                Value::Text(role.to_string()),
                Value::Integer(id as i64),
            ],
        )?;
        
        Ok(result.rows_affected > 0)
    }
    
    fn delete(&self, id: u64) -> Result<bool> {
        let result = self.conn.execute(
            "DELETE FROM users WHERE id = ?",
            &[Value::Integer(id as i64)],
        )?;
        
        Ok(result.rows_affected > 0)
    }
    
    fn search(&self, query: &str, limit: usize, offset: usize) -> Result<Vec<UserRow>> {
        let pattern = format!("%{}%", query);
        let result = self.conn.execute(
            "SELECT id, username, email, role, created_at 
             FROM users 
             WHERE username LIKE ? OR email LIKE ?
             ORDER BY created_at DESC
             LIMIT ? OFFSET ?",
            &[
                Value::Text(pattern.clone()),
                Value::Text(pattern),
                Value::Integer(limit as i64),
                Value::Integer(offset as i64),
            ],
        )?;
        
        Ok(result.rows.into_iter().map(UserRow::from_row).collect())
    }
    
    fn count(&self) -> Result<u64> {
        let result = self.conn.execute(
            "SELECT COUNT(*) FROM users",
            &[],
        )?;
        
        Ok(result.rows.first()
            .and_then(|r| r.first())
            .and_then(|v| if let Value::Integer(n) = v { Some(*n as u64) } else { None })
            .unwrap_or(0))
    }
}

#[derive(Debug, serde::Serialize)]
struct UserRow {
    id: u64,
    username: String,
    email: String,
    role: String,
    created_at: String,
}

impl UserRow {
    fn from_row(row: Vec<Value>) -> Self {
        Self {
            id: if let Some(Value::Integer(n)) = row.get(0) { *n as u64 } else { 0 },
            username: if let Some(Value::Text(s)) = row.get(1) { s.clone() } else { String::new() },
            email: if let Some(Value::Text(s)) = row.get(2) { s.clone() } else { String::new() },
            role: if let Some(Value::Text(s)) = row.get(3) { s.clone() } else { "user".to_string() },
            created_at: if let Some(Value::Text(s)) = row.get(4) { s.clone() } else { String::new() },
        }
    }
}
```

## 10.2 libSQL/Turso Cloud Database

```toml
# spin.toml - Configure libSQL/Turso database
spin_manifest_version = 2

[application]
name = "turso-example"

[variables]
turso_url = { required = true }
turso_token = { required = true }

trigger.http
route = "/..."
component = "api"

[component.api]
source = "target/wasm32-wasi/release/api.wasm"

[component.api.sqlite_databases]
databases = ["main"]

# Runtime configuration (runtime-config.toml)
# [sqlite_database.main]
# type = "libsql"
# url = "libsql://mydb.turso.io"
# token = "eyJ..."
```

```yaml
# SpinKube using libSQL Secret
apiVersion: v1
kind: Secret
metadata:
  name: spin-runtime-secret
  namespace: production
type: Opaque
stringData:
  runtime-config.toml: |
    [sqlite_database.main]
    type = "libsql"
    url = "libsql://users-db.turso.io"
    token = "your-turso-token-here"
    
    [key_value_store.default]
    type = "redis"
    url = "redis://:password@redis.production.svc:6379"
```

---

<!-- chunk: 11. Advanced Configuration and Security-->## 11. Advanced Configuration and Security

## 11.1 TLS Configuration

```yaml
# SpinApp TLS Configuration
apiVersion: core.spinoperator.dev/v1alpha1
kind: SpinApp
metadata:
  name: secure-api
spec:
  image: ghcr.io/myorg/secure-api:latest
  executor: containerd-shim-spin
  replicas: 3
  
  # TLS Configuration
  tls:
    enabled: true
    secretName: api-tls-cert # Contains tls.crt and tls.key
    port: 443
  
  # Force HTTPS
  httpToHttpsRedirect: true
```

> ⚠️ **🟡 Medium-Risk Change** — This involves changing the status of cluster resources. It is recommended to first confirm using `--dry-run` or `diff`.
> - `kubectl apply/create/replace`: Creates/modifies cluster resources

``` bash
# 🟡 Medium Risk: Will modify cluster/resource status. Please confirm the target, scope of impact, and authorization before execution.
# Generate a self-signed certificate (for development use)
openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout tls.key \
  -out tls.crt \
  -subj "/CN=myapp.example.com"

# Create a TLS Secret
kubectl create secret tls api-tls-cert \
  --key=tls.key \
  --cert=tls.crt \
  --namespace=production

# Use cert-manager for automatic certificate management
```
## 11.2 RBAC and Security Policies

```yaml
# spin-operator ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: spin-operator
  namespace: spin-operator

---
# RBAC ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: spin-operator-role
rules:
- apiGroups: ["core.spinoperator.dev"]
  resources: ["spinapps", "spinappexecs"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
- apiGroups: ["core.spinoperator.dev"]
  resources: ["spinapps/status"]
  verbs: ["update", "patch"]
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
- apiGroups: [""]
  resources: ["services", "configmaps", "secrets"]
  verbs: ["get", "list", "watch", "create", "update", "patch"]
- apiGroups: ["keda.sh"]
  resources: ["scaledobjects"]
  verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]

---
# Pod Security Policy
apiVersion: v1
kind: Pod
metadata:
  name: spin-workload
spec:
  runtimeClassName: wasmtime-spin
  securityContext:
    runAsNonRoot: true
    runAsUser: 65534  # nobody
    runAsGroup: 65534
    fsGroup: 65534
    seccompProfile:
      type: RuntimeDefault
  
  containers:
  - name: app
    image: ghcr.io/myorg/app:latest
    securityContext:
      allowPrivilegeEscalation: false
      readOnlyRootFilesystem: true
      capabilities:
        drop:
        - ALL
    resources:
      requests:
        memory: "16Mi"
        cpu: "50m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```

## 11.3 Network Policies

```yaml
# SpinKube Network Policy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: spin-app-netpol
  namespace: production
spec:
  podSelector:
    matchLabels:
      app.kubernetes.io/managed-by: spin-operator
  
  policyTypes:
  - Ingress
  - Egress
  
  # Inbound: Only accept traffic from Ingress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          kubernetes.io/metadata.name: ingress-nginx
    - podSelector:
        matchLabels:
          app.kubernetes.io/name: ingress-nginx
    ports:
    - port: 80
      protocol: TCP
    - port: 443
      protocol: TCP
  
  # Outbound: Controls accessible external services
  egress:
  # DNS resolution
  - to:
    - namespaceSelector: {}
    ports:
    - port: 53
      protocol: UDP
  
  # Redis
  - to:
    - podSelector:
        matchLabels:
          app: redis
    ports:
    - port: 6379
  
  # Allow HTTPS outbound (Spin outbound HTTP)
  - to:
    - ipBlock:
        cidr: 0.0.0.0/0
        except:
        - 10.0.0.0/8
        - 172.16.0.0/12
        - 192.168.0.0/16
    ports:
    - port: 443
      protocol: TCP
```

---

<!-- chunk: 12. Monitoring and Observability-->## 12. Monitoring and Observability

## 12.1 Prometheus Metrics

```yaml
# Prometheus ServiceMonitor for SpinKube
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: spinkube-monitor
  namespace: monitoring
  labels:
    app: spinkube
    prometheus: kube-prometheus
spec:
  selector:
    matchLabels:
      app.kubernetes.io/managed-by: spin-operator
  namespaceSelector:
    matchNames:
    - production
  endpoints:
  - port: metrics
    interval: 15s
    path: /metrics

---
# Custom Alarm Rules
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: spinkube-alerts
  namespace: monitoring
spec:
  groups:
  - name: spinkube.rules
    interval: 30s
    rules:
    # Spin application unavailable
    - alert: SpinAppDown
      expr: |
        kube_deployment_status_replicas_available{
          deployment=~".*spin.*"
        } == 0
      for: 2m
      labels:
        severity: critical
        team: platform
      annotations:
        Summary: "No copies of the SpinKube application are available"
        Description: "Deploying {{ $labels.deployment }} in {{ $labels.namespace }} has no available replicas."
    
    # Scale-to-zero has not been activated for a long time
    - alert: SpinAppScaledToZeroTooLong
      expr: |
        kube_deployment_spec_replicas{
          deployment=~".*spin.*"
        } == 0
      for: 24h
      labels:
        severity: info
      annotations:
        Summary: "The SpinKube app has been scaled down to 0 for over 24 hours."
        Description: "Consider whether you need to delete or archive this application."
    
    # High latency
    - alert: SpinAppHighLatency
      expr: |
        histogram_quantile(0.99,
          rate(spin_http_request_duration_seconds_bucket[5m])
        ) > 1.0
      for: 5m
      labels:
        severity: warning
      annotations:
        Summary: "SpinKube application P99 has excessively high latency"
        Description: "P99 Delay {{ $value }}s exceeds the 1-second threshold"
```

## 12.2 Grafana Dashboard 配置 / Grafana Dashboard

```json
{
  "title": "SpinKube Application Monitoring",
  "panels": [
    {
      "title": "Number of Active Spin Instances",
      "type": "stat",
      "targets": [{
        "expr": "sum(kube_deployment_spec_replicas{deployment=~\".*spin.*\"})"
      }]
    },
    {
      "title": "Request Rate (RPS)"
      "type": "graph",
      "targets": [{
        "expr": "sum(rate(spin_http_requests_total[1m])) by (app)",
        "legendFormat": "{{app}}"
      }]
    },
    {
      "title": "P95 Response Time",
      "type": "graph",
      "targets": [{
        "expr": "histogram_quantile(0.95, rate(spin_http_request_duration_seconds_bucket[5m]))",
        "legendFormat": "P95 Delay"
      }]
    },
    {
      "title": "Scale-to-Zero Cold Start Count",
      "type": "counter",
      "targets": [{
        "expr": "increase(spin_cold_starts_total[1h])"
      }]
    },
    {
      "title": "KV Store Operation Speed",
      "type": "graph",
      "targets": [{
        "expr": "rate(spin_kv_ops_total[1m])"
      }]
    }
  ]
}
```

## 12.3 Log Collection

```yaml
# Fluentd Log Collection Configuration (for SpinKube)
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluentd-config
  namespace: kube-system
data:
  fluent.conf: |
    # Collect Spin application logs
    <source>
      @type tail
      path /var/log/containers/*spin*.log
      pos_file /var/log/fluentd-spin.log.pos
      tag spin.*
      <parse>
        @type json
        time_format %Y-%m-%dT%H:%M:%S.%NZ
      </parse>
    </source>
    
    # Add SpinKube related tags
    <filter spin.**>
      @type record_transformer
      <record>
        runtime wasm
        framework spin
        cluster ${ENV["CLUSTER_NAME"]}
      </record>
    </filter>
    
    # Output to Elasticsearch
    <match spin.**>
      @type elasticsearch
      host elasticsearch.logging.svc
      port 9200
      index_name spin-logs
      <buffer>
        @type file
        path /var/log/fluentd-spin-buffer
        flush_mode interval
        flush_interval 5s
      </buffer>
    </match>
```

---

<!-- chunk: References -->## References

## Official Documentation
- [SpinKube Official Documentation](https://www.spinkube.dev/docs/)
- [spin-operator GitHub](https://github.com/spinkube/spin-operator)
- [Fermyon Spin Documentation](https://developer.fermyon.com/spin/)

## CNCF Related
- [SpinKube CNCF Sandbox](https://www.cncf.io/projects/spinkube/)
- [KEDA Official Documentation](https://keda.sh/docs/)

## Example Code
- [Spin ​​Sample Repository](https://github.com/fermyon/spin-samples)
- [SpinKube Examples](https://github.com/spinkube/spin-operator/tree/main/config/samples)

---

Last Updated: 2025-03-04
Version: 1.0.0

---

<!-- chunk: Obsidian related documentation-->## Obsidian related documentation

- domain-38-webassembly-cloud-native MOC
- [[domain-15-specialized-tech/README.md|Domain 15: WebAssembly 云原生 (WebAssembly Cloud Native)]]
- Domain-38 WebAssembly Cloud Native — Open Source Project Index
WebAssembly Cloud Native Foundation
- containerd Wasm runtime
- wasmCloud platform
WasmEdge runtime
- Wasm Component Model
- Wasm Plugin System
- Wasm AI Inference
- Wasm Serverless (Wasm Serverless)
Wasm Security and Sandbox

## See Also

- 01-wasm-fundamentals-cloud-native
- 02-containerd-wasm-shim
- 04-wasmcloud-platform
- 05-wasmedge-runtime
