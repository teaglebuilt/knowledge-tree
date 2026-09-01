---
title: Wasm Plugin System
description: 'WebAssembly-based plugin systems enable programmable extensibility for network proxies, API gateways, and service meshes through sandbox security isolation and high-performance execution. Covers proxy-wasm specification, Envoy/Istio Wasm filters, APISIX/Kong plugins, authentication, rate limiting, observability, and production deployment best practices.'
summary: 'Comprehensive guide to Wasm plugin systems covering proxy-wasm specification, Envoy Wasm filter development, Istio plugin configuration, HTTP header manipulation, rate limiting, observability plugins, authentication and authorization, data transformation, debugging, APISIX and Kong plugins, performance optimization, and production deployment patterns.'
category: webassembly-cloud-native
tags:
- k8s
- wasm
- webassembly
- cloud-native
- prometheus
- istio
- envoy
- docker
- opa
- redis
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
- What is Wasm Plugin System
- How to implement Wasm plugins
- Kubernetes webassembly cloud native best practices
trigger_keywords:
- Wasm
- Plugin System
- proxy-wasm
- Envoy
- Istio
- webassembly
- cloud native
prerequisites:
- kubectl-basics
- service-mesh-basics
- prometheus-basics
- redis-basics
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
---

> **Production Safety Notice**
>
> This document contains directly executable operational commands. Before execution, confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether verification has been completed in a non-production environment. Command risk level marking: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state but usually reversible), 🟢 Low risk/Read-only (information gathering, no side effects).

# Wasm Plugin System

> WebAssembly-based plugin systems enable programmable extensibility for network proxies, API gateways, and service meshes through sandbox security isolation and high-performance execution.

---

<!-- chunk: Table of Contents -->## Table of Contents

1. [Plugin System Architecture Overview](#1-plugin-system-architecture-overview)
2. [proxy-wasm Specification Deep Dive](#2-proxy-wasm-specification-deep-dive)
3. [[entities/envoy.md|Envoy]] Wasm Filter Development](#3-envoy-wasm-filter-development)
4. [[entities/istio.md|Istio]] Wasm Plugin Configuration](#4-istio-wasm-plugin-configuration)
5. [HTTP Header Manipulation Plugins](#5-http-header-manipulation-plugins)
6. [Rate Limiting Plugin Implementation](#6-rate-limiting-plugin-implementation)
7. [Observability Plugins](#7-observability-plugins)
8. [Authentication and Authorization Plugins](#8-authentication-and-authorization-plugins)
9. [Data Transformation Plugins](#9-data-transformation-plugins)
10. [Plugin Debugging and Testing](#10-plugin-debugging-and-testing)
11. [APISIX Wasm Plugins](#11-apisix-wasm-plugins)
12. [Kong Wasm Plugins](#12-kong-wasm-plugins)
13. [Performance Optimization and Benchmarks](#13-performance-optimization-and-benchmarks)
14. [Production Deployment Best Practices](#14-production-deployment-best-practices)

---

<!-- chunk: 1. Plugin System Architecture Overview -->## 1. Plugin System Architecture Overview

## 1.1 Why Choose Wasm Plugins

Comparison of traditional network proxy extension methods:

```mermaid
graph TB
    subgraph "Traditional Extension Methods"
        Lua[Lua Scripts<br/>Limited Performance]
        Go[Go Plugins<br/>Requires Recompilation]
        C[C++ Filters<br/>Unsafe/Hard to Debug]
        gRPC[External gRPC<br/>High Latency]
    end

    subgraph "Wasm Plugin Advantages"
        Safe[Memory Safety Isolation]
        Perf[Near-Native Performance]
        Portable[Cross-Platform Portability]
        Dynamic[Dynamic Hot Loading]
        Multi[Multi-Language Support]
    end

    Wasm[Wasm Plugin System] --> Safe
    Wasm --> Perf
    Wasm --> Portable
    Wasm --> Dynamic
    Wasm --> Multi
```

## 1.2 proxy-wasm Ecosystem Landscape

```mermaid
graph LR
    subgraph "Language SDKs"
        RustSDK[proxy-wasm-rust-sdk]
        GoSDK[proxy-wasm-go-sdk]
        CPPSDK[proxy-wasm-cpp-sdk]
        AssemblySDK[AssemblyScript SDK]
    end

    subgraph "proxy-wasm ABI"
        Spec[proxy-wasm specification]
    end

    subgraph "Host Environments"
        Envoy[Envoy Proxy]
        Istio[Istio Sidecar]
        MOSN[MOSN]
        APISIX[Apache APISIX]
        Kong[Kong Gateway]
        Higress[Higress]
    end

    RustSDK --> Spec
    GoSDK --> Spec
    CPPSDK --> Spec
    AssemblySDK --> Spec

    Spec --> Envoy
    Spec --> Istio
    Spec --> MOSN
    Spec --> APISIX
    Spec --> Kong
    Spec --> Higress
```

## 1.3 proxy-wasm Execution Model

```mermaid
sequenceDiagram
    participant Client
    participant Envoy
    participant WasmPlugin as Wasm Plugin
    participant Upstream

    Client->>Envoy: HTTP Request
    Envoy->>WasmPlugin: on_http_request_headers()
    WasmPlugin-->>Envoy: Action::Continue
    Envoy->>WasmPlugin: on_http_request_body()
    WasmPlugin-->>Envoy: Action::Continue
    Envoy->>Upstream: Forward Request
    Upstream->>Envoy: HTTP Response
    Envoy->>WasmPlugin: on_http_response_headers()
    WasmPlugin-->>Envoy: Action::Continue
    Envoy->>WasmPlugin: on_http_response_body()
    WasmPlugin-->>Envoy: Action::Continue
    Envoy->>Client: HTTP Response
```

## 1.4 Plugin Lifecycle

```
Plugin Lifecycle (per Worker Thread):

1. VM Creation Phase
   └── _start() / proxy_on_vm_start()
       └── Initialize global state, read VM config

2. Plugin Configuration Phase
   └── proxy_on_configure()
       └── Parse plugin configuration (JSON/YAML)

3. Request Processing Phase (per request)
   ├── proxy_on_context_create()     # Create request context
   ├── proxy_on_request_headers()    # Process request headers
   ├── proxy_on_request_body()       # Process request body
   ├── proxy_on_request_trailers()   # Process request trailers
   ├── proxy_on_response_headers()   # Process response headers
   ├── proxy_on_response_body()      # Process response body
   ├── proxy_on_response_trailers()  # Process response trailers
   └── proxy_on_done()               # Request completed

4. Async Operations
   ├── proxy_on_http_call_response()  # HTTP callback
   ├── proxy_on_grpc_call_response()  # gRPC callback
   └── proxy_on_queue_ready()         # Queue message

5. Timer
   └── proxy_on_tick()               # Periodic trigger
```

---

<!-- chunk: 2. proxy-wasm Specification Deep Dive -->## 2. proxy-wasm Specification Deep Dive

## 2.1 Host Function ABI

proxy-wasm defines host function interfaces callable by Wasm plugins:

```
# Core Host Function Categories

<!-- chunk: Property Operations -->## Property Operations
proxy_get_property(path_data, path_size, return_value_data, return_value_size) -> Status
proxy_set_property(path_data, path_size, value_data, value_size) -> Status

<!-- chunk: HTTP Header Operations -->## HTTP Header Operations
proxy_get_header_map_value(map_type, key_data, key_size, return_value_data, return_value_size) -> Status
proxy_add_header_map_value(map_type, key_data, key_size, value_data, value_size) -> Status
proxy_replace_header_map_value(map_type, key_data, key_size, value_data, value_size) -> Status
proxy_remove_header_map_value(map_type, key_data, key_size) -> Status
proxy_get_header_map_pairs(map_type, return_map_data, return_map_size) -> Status
proxy_set_header_map_pairs(map_type, map_data, map_size) -> Status

<!-- chunk: HTTP Body Operations -->## HTTP Body Operations
proxy_get_buffer_bytes(buffer_type, start, max_size, return_buffer_data, return_buffer_size) -> Status
proxy_set_buffer_bytes(buffer_type, start, size, buffer_data, buffer_size) -> Status

<!-- chunk: Send Local Response -->## Send Local Response
proxy_send_local_response(status_code, status_code_details_data, status_code_details_size,
    body_data, body_size, headers_data, headers_size, grpc_status) -> Status

<!-- chunk: HTTP Call -->## HTTP Call
proxy_http_call(upstream_data, upstream_size, headers_data, headers_size,
    body_data, body_size, trailers_data, trailers_size, timeout, return_token) -> Status

<!-- chunk: Shared Data -->## Shared Data
proxy_get_shared_data(key_data, key_size, return_value_data, return_value_size, return_cas) -> Status
proxy_set_shared_data(key_data, key_size, value_data, value_size, cas) -> Status

<!-- chunk: Message Queue -->## Message Queue
proxy_register_shared_queue(name_data, name_size, return_id) -> Status
proxy_resolve_shared_queue(vm_id_data, vm_id_size, name_data, name_size, return_id) -> Status
proxy_dequeue_shared_queue(token, return_data, return_size) -> Status
proxy_enqueue_shared_queue(token, data, size) -> Status

<!-- chunk: Timer -->## Timer
proxy_set_tick_period_milliseconds(period) -> Status

<!-- chunk: Logging -->## Logging
proxy_log(level, logMessage_data, logMessage_size) -> Status

<!-- chunk: Metrics -->## Metrics
proxy_define_metric(metric_type, name_data, name_size, return_id) -> Status
proxy_increment_metric(metric_id, offset) -> Status
proxy_record_metric(metric_id, value) -> Status
proxy_get_metric(metric_id, return_value) -> Status
```

## 2.2 Map Type Constants

```rust
// proxy-wasm map types
pub enum MapType {
    HttpRequestHeaders = 0,
    HttpRequestTrailers = 1,
    HttpResponseHeaders = 2,
    HttpResponseTrailers = 3,
    GrpcReceiveInitialMetadata = 4,
    GrpcReceiveTrailingMetadata = 5,
    HttpCallResponseHeaders = 6,
    HttpCallResponseTrailers = 7,
}

// Buffer types
pub enum BufferType {
    HttpRequestBody = 0,
    HttpResponseBody = 1,
    NetworkDownstreamData = 2,
    NetworkUpstreamData = 3,
    HttpCallResponseBody = 4,
    GrpcReceiveBuffer = 5,
    VmConfiguration = 6,
    PluginConfiguration = 7,
}

// Return actions
pub enum Action {
    Continue = 0,  // Continue processing
    Pause = 1,     // Pause, waiting for async operation
}

// Status codes
pub enum Status {
    Ok = 0,
    NotFound = 1,
    BadArgument = 2,
    SerializationFailure = 3,
    ParseFailure = 4,
    BadExpression = 5,
    InvalidMemoryAccess = 6,
    Empty = 7,
    CasMismatch = 8,
    ResultMismatch = 9,
    InternalFailure = 10,
    BrokenConnection = 11,
    Unimplemented = 12,
}
```

---

<!-- chunk: 3. Envoy Wasm Filter Development -->## 3. Envoy Wasm Filter Development

## 3.1 Rust SDK Development Environment

```bash
# Install Rust Wasm toolchain
rustup target add wasm32-wasi
rustup target add wasm32-unknown-unknown

# Create plugin project
cargo new --lib envoy-wasm-plugin
cd envoy-wasm-plugin

# Cargo.toml configuration
cat > Cargo.toml << 'EOF'
[package]
name = "envoy-wasm-plugin"
version = "0.1.0"
edition = "2021"

[lib]
crate-type = ["cdylib"]

[dependencies]
proxy-wasm = "0.2"
serde = { version = "1", features = ["derive"] }
serde_json = "1"
log = "0.4"

[profile.release]
opt-level = "z"     # Minimize size
lto = true          # Link-time optimization
codegen-units = 1   # Reduce code size
panic = "abort"     # Remove panic handling code
strip = true        # Strip symbols
EOF
```

## 3.2 Complete HTTP Filter Implementation

```rust
// src/lib.rs - Complete HTTP filter
use proxy_wasm::traits::*;
use proxy_wasm::types::*;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

// Plugin global configuration
#[derive(Debug, Clone, Deserialize, Serialize)]
struct PluginConfig {
    #[serde(default)]
    add_headers: HashMap<String, String>,
    #[serde(default)]
    remove_headers: Vec<String>,
    #[serde(default)]
    allowed_paths: Vec<String>,
    #[serde(default = "default_upstream")]
    auth_service: String,
    #[serde(default = "default_timeout")]
    timeout_ms: u32,
}

fn default_upstream() -> String {
    "auth-service".to_string()
}

fn default_timeout() -> u32 {
    1000
}

// VM root context (one per Worker)
struct RootContext {
    config: Option<PluginConfig>,
    metric_request_count: u32,
    metric_error_count: u32,
}

// HTTP context (one per request)
struct HttpContext {
    config: PluginConfig,
    request_start: u64,
    metric_request_count: u32,
    metric_latency: u32,
    auth_token: Option<String>,
    call_token: Option<u32>,
}

// Register plugin factory
#[no_mangle]
pub fn _start() {
    proxy_wasm::set_log_level(LogLevel::Trace);
    proxy_wasm::set_root_context(|_| -> Box<dyn RootContext> {
        Box::new(RootContext {
            config: None,
            metric_request_count: 0,
            metric_error_count: 0,
        })
    });
}

impl proxy_wasm::traits::Context for RootContext {}

impl proxy_wasm::traits::RootContext for RootContext {
    fn on_vm_start(&mut self, _vm_configuration_size: usize) -> bool {
        log::info!("Plugin VM started");
        true
    }

    fn on_configure(&mut self, _plugin_configuration_size: usize) -> bool {
        // Read plugin configuration
        if let Some(config_bytes) = self.get_plugin_configuration() {
            match serde_json::from_slice::<PluginConfig>(&config_bytes) {
                Ok(config) => {
                    log::info!("Plugin configured: {:?}", config);
                    self.config = Some(config);
                }
                Err(e) => {
                    log::error!("Failed to parse plugin config: {}", e);
                    return false;
                }
            }
        } else {
            // Use default configuration
            self.config = Some(PluginConfig {
                add_headers: HashMap::new(),
                remove_headers: vec![],
                allowed_paths: vec![],
                auth_service: default_upstream(),
                timeout_ms: default_timeout(),
            });
        }

        // Register metrics
        self.metric_request_count = self.define_metric(
            MetricType::Counter,
            "plugin_requests_total",
        ).unwrap_or(0);

        self.metric_error_count = self.define_metric(
            MetricType::Counter,
            "plugin_errors_total",
        ).unwrap_or(0);

        true
    }

    fn create_http_context(&self, context_id: u32) -> Option<Box<dyn HttpContext>> {
        let config = self.config.clone()?;

        // Register request latency metric
        let metric_latency = self.define_metric(
            MetricType::Histogram,
            "plugin_request_duration_ms",
        ).unwrap_or(0);

        Some(Box::new(HttpContext {
            config,
            request_start: 0,
            metric_request_count: self.metric_request_count,
            metric_latency,
            auth_token: None,
            call_token: None,
        }))
    }

    fn get_type(&self) -> Option<ContextType> {
        Some(ContextType::HttpContext)
    }
}

impl proxy_wasm::traits::Context for HttpContext {
    fn on_http_call_response(
        &mut self,
        _token_id: u32,
        _num_headers: usize,
        body_size: usize,
        _num_trailers: usize,
    ) {
        // Handle external Auth service response
        let status = self.get_http_call_response_header(":status")
            .unwrap_or_default();

        if status == "200" {
            // Authentication passed, continue request
            if let Some(body) = self.get_http_call_response_body(0, body_size) {
                // Extract user info from auth response
                if let Ok(auth_resp) = serde_json::from_slice::<serde_json::Value>(&body) {
                    if let Some(user_id) = auth_resp["user_id"].as_str() {
                        self.add_http_request_header("x-authenticated-user", user_id);
                    }
                    if let Some(roles) = auth_resp["roles"].as_str() {
                        self.add_http_request_header("x-user-roles", roles);
                    }
                }
            }
            self.resume_http_request();
        } else {
            // Authentication failed, return 401
            self.send_http_response(
                401,
                vec![
                    ("content-type", "application/json"),
                    ("x-error-source", "wasm-auth-plugin"),
                ],
                Some(b"{\"error\":\"Unauthorized\",\"code\":401}"),
            );
        }
    }
}

impl proxy_wasm::traits::HttpContext for HttpContext {
    fn on_http_request_headers(&mut self, _num_headers: usize, _end_of_stream: bool) -> Action {
        // Record request start time
        self.request_start = self.get_current_time_nanoseconds();

        // Increment request count
        self.increment_metric(self.metric_request_count, 1);

        // Path check
        let path = self.get_http_request_header(":path")
            .unwrap_or_default();

        // Check if health check path (skip auth)
        if path == "/health" || path == "/ready" {
            return Action::Continue;
        }

        // Path whitelist check
        if !self.config.allowed_paths.is_empty() {
            let path_allowed = self.config.allowed_paths.iter()
                .any(|allowed| path.starts_with(allowed));
            if !path_allowed {
                self.send_http_response(
                    403,
                    vec![("content-type", "application/json")],
                    Some(b"{\"error\":\"Forbidden\",\"message\":\"Path not allowed\"}"),
                );
                return Action::Pause;
            }
        }

        // Extract Authorization header
        let auth_header = self.get_http_request_header("authorization")
            .unwrap_or_default();

        if auth_header.is_empty() {
            self.send_http_response(
                401,
                vec![
                    ("content-type", "application/json"),
                    ("www-authenticate", "Bearer realm=\"api\""),
                ],
                Some(b"{\"error\":\"Unauthorized\",\"message\":\"Missing Authorization header\"}"),
            );
            return Action::Pause;
        }

        // Call external Auth service to validate token
        let token = auth_header.trim_start_matches("Bearer ").to_string();
        self.auth_token = Some(token.clone());

        match self.dispatch_http_call(
            &self.config.auth_service,
            vec![
                (":method", "GET"),
                (":path", "/validate"),
                (":authority", &self.config.auth_service),
                ("authorization", &format!("Bearer {}", token)),
                ("content-type", "application/json"),
            ],
            None,
            vec![],
            std::time::Duration::from_millis(self.config.timeout_ms as u64),
        ) {
            Ok(token_id) => {
                self.call_token = Some(token_id);
                Action::Pause  // Pause waiting for Auth service response
            }
            Err(e) => {
                log::error!("Failed to dispatch auth call: {:?}", e);
                // Auth service unavailable, decide whether to allow based on config
                Action::Continue
            }
        }
    }

    fn on_http_request_body(&mut self, body_size: usize, end_of_stream: bool) -> Action {
        if !end_of_stream {
            return Action::Pause;
        }

        // Read and log request body size
        if let Some(body) = self.get_http_request_body(0, body_size) {
            log::debug!("Request body size: {} bytes", body.len());
        }

        Action::Continue
    }

    fn on_http_response_headers(&mut self, _num_headers: usize, _end_of_stream: bool) -> Action {
        // Add custom response headers
        for (name, value) in &self.config.add_headers {
            self.add_http_response_header(name, value);
        }

        // Remove sensitive response headers
        for header in &self.config.remove_headers {
            self.remove_http_response_header(header);
        }

        // Add processing identifier
        self.add_http_response_header("x-processed-by", "envoy-wasm-plugin/1.0");

        // Add request ID (if not exists)
        if self.get_http_response_header("x-request-id").is_none() {
            let req_id = format!("req-{}", self.request_start);
            self.add_http_response_header("x-request-id", &req_id);
        }

        Action::Continue
    }

    fn on_http_response_body(&mut self, _body_size: usize, _end_of_stream: bool) -> Action {
        Action::Continue
    }

    fn on_log(&mut self) {
        // Calculate request latency and record metrics
        let end_time = self.get_current_time_nanoseconds();
        let duration_ms = (end_time - self.request_start) / 1_000_000;

        self.record_metric(self.metric_latency, duration_ms);

        // Structured logging
        let method = self.get_http_request_header(":method").unwrap_or_default();
        let path = self.get_http_request_header(":path").unwrap_or_default();
        let status = self.get_http_response_header(":status").unwrap_or_default();

        log::info!(
            "request completed: method={} path={} status={} duration_ms={}",
            method, path, status, duration_ms
        );
    }
}
```

## 3.3 Build and Deployment

> ⚠️ **🟡 Medium Risk** — Changes cluster resource state, recommend --dry-run or diff confirmation first
> - `kubectl apply/create/replace`: Creates/modifies cluster resources

``` bash
# 🟡 Medium Risk: Will modify cluster/resource state, confirm target, impact scope, and authorization before execution
# Build Wasm plugin
cargo build --target wasm32-unknown-unknown --release

# Output path
ls target/wasm32-unknown-unknown/release/*.wasm

# Optimize size
wasm-opt -Oz \
  -o plugin-optimized.wasm \
  target/wasm32-unknown-unknown/release/envoy_wasm_plugin.wasm

# Check size
ls -lh plugin-optimized.wasm

# Deploy to ConfigMap
kubectl create configmap envoy-wasm-plugin \
  --from-file=plugin.wasm=plugin-optimized.wasm \
  -n default
```
---

<!-- chunk: 4. Istio Wasm Plugin Configuration -->## 4. Istio Wasm Plugin Configuration

## 4.1 WasmPlugin CRD

```yaml
# istio-wasm-plugin.yaml
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: auth-plugin
  namespace: default
spec:
  selector:
    matchLabels:
      app: my-service
  
  # Plugin source (supports OCI images or HTTP URLs)
  url: oci://ghcr.io/my-org/auth-wasm-plugin:1.0.0
  
  # Or use local ConfigMap
  # url: file:///var/local/lib/wasm-filters/plugin.wasm
  
  # SHA256 verification
  sha256: "e0e2b7b1..."
  
  # Execution phase
  phase: AUTHN
  # Options: UNSPECIFIED_PHASE, AUTHN, AUTHZ, STATS
  
  # Priority (order within same phase)
  priority: 10
  
  # Plugin configuration (JSON format)
  pluginConfig:
    auth_service: "auth-service.default.svc.cluster.local:8080"
    timeout_ms: 500
    allowed_paths:
      - "/public"
      - "/health"
    add_headers:
      x-gateway-version: "v2"
    remove_headers:
      - "x-internal-token"
      - "x-debug-info"
  
  # Image pull secret
  imagePullSecret: registry-credentials
  
  # VM configuration
  vmConfig:
    # Environment variables
    env:
      - name: LOG_LEVEL
        value: info
      - name: ENVIRONMENT
        valueFrom:
          fieldRef:
            fieldPath: metadata.namespace
```

## 4.2 Multi-Phase Plugin Configuration

```yaml
# Authentication plugin (AUTHN phase)
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: jwt-auth
  namespace: istio-system
spec:
  selector:
    matchLabels:
      istio: ingressgateway
  url: oci://registry.example.com/plugins/jwt-auth:2.1.0
  phase: AUTHN
  priority: 100
  pluginConfig:
    jwks_uri: "https://auth.example.com/.well-known/jwks.json"
    issuer: "https://auth.example.com"
    audiences:
      - "api.example.com"
    cache_duration_seconds: 300

---
# Authorization plugin (AUTHZ phase)
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: rbac-authz
  namespace: istio-system
spec:
  selector:
    matchLabels:
      istio: ingressgateway
  url: oci://registry.example.com/plugins/rbac:1.0.0
  phase: AUTHZ
  priority: 100
  pluginConfig:
    policy_endpoint: "http://opa-service:8181/v1/data/authz/allow"
    cache_size: 10000

---
# Statistics plugin (STATS phase)
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: custom-metrics
  namespace: istio-system
spec:
  selector:
    matchLabels:
      istio: ingressgateway
  url: oci://registry.example.com/plugins/metrics:1.2.0
  phase: STATS
  pluginConfig:
    metric_prefix: "envoy_wasm"
    histogram_buckets:
      - 1
      - 5
      - 10
      - 25
      - 50
      - 100
      - 250
      - 500
      - 1000
```

## 4.3 OCI Image Packaging

```dockerfile
# Dockerfile.wasm - Package Wasm plugin as OCI image
FROM scratch

# Copy Wasm file
COPY plugin-optimized.wasm /plugin.wasm

# OCI annotations
LABEL org.opencontainers.image.title="Auth Wasm Plugin"
LABEL org.opencontainers.image.version="1.0.0"
LABEL org.opencontainers.image.description="JWT authentication plugin for Envoy/Istio"
```

``` bash
# 🟢 Low Risk: Read-only/information gathering, typically no side effects
# Build and push OCI image
docker buildx build \
  --platform linux/amd64 \
  -t ghcr.io/my-org/auth-wasm-plugin:1.0.0 \
  -f Dockerfile.wasm \
  --push \
  .

# Or use crane to push Wasm OCI format
crane push plugin-optimized.wasm \
  ghcr.io/my-org/auth-wasm-plugin:1.0.0 \
  --media-type application/vnd.module.wasm.content.layer.v1+wasm

# Verify
crane manifest ghcr.io/my-org/auth-wasm-plugin:1.0.0
```
---

<!-- chunk: 5. HTTP Header Manipulation Plugins -->## 5. HTTP Header Manipulation Plugins

## 5.1 Request Header Enrichment Plugin

```rust
// Request header enrichment: add trace ID, request metadata
use proxy_wasm::traits::*;
use proxy_wasm::types::*;
use std::collections::HashMap;

struct HeaderEnrichPlugin {
    config: HeaderEnrichConfig,
    request_counter: u32,
}

#[derive(serde::Deserialize, Default)]
struct HeaderEnrichConfig {
    service_name: String,
    service_version: String,
    add_request_id: bool,
    add_timestamp: bool,
    forward_client_ip: bool,
    custom_headers: HashMap<String, String>,
    redact_headers: Vec<String>,
}

impl Context for HeaderEnrichPlugin {}

impl HttpContext for HeaderEnrichPlugin {
    fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
        // 1. Generate and inject request ID
        if self.config.add_request_id {
            if self.get_http_request_header("x-request-id").is_none() {
                let req_id = self.generate_request_id();
                self.set_http_request_header("x-request-id", Some(&req_id));
            }
        }

        // 2. Inject timestamp
        if self.config.add_timestamp {
            let ts = self.get_current_time_nanoseconds();
            self.set_http_request_header(
                "x-request-timestamp",
                Some(&ts.to_string()),
            );
        }

        // 3. Inject service identification
        self.set_http_request_header(
            "x-source-service",
            Some(&self.config.service_name),
        );
        self.set_http_request_header(
            "x-source-version",
            Some(&self.config.service_version),
        );

        // 4. Handle client IP
        if self.config.forward_client_ip {
            if let Some(remote_addr) = self.get_property(vec!["source", "address"]) {
                if let Ok(addr) = String::from_utf8(remote_addr) {
                    // Extract IP part
                    let ip = addr.split(':').next().unwrap_or(&addr);
                    
                    // Append to X-Forwarded-For
                    let existing = self.get_http_request_header("x-forwarded-for")
                        .unwrap_or_default();
                    let new_xff = if existing.is_empty() {
                        ip.to_string()
                    } else {
                        format!("{}, {}", existing, ip)
                    };
                    self.set_http_request_header("x-forwarded-for", Some(&new_xff));
                    self.set_http_request_header("x-real-ip", Some(ip));
                }
            }
        }

        // 5. Add custom headers
        for (name, value) in &self.config.custom_headers {
            self.set_http_request_header(name, Some(value));
        }

        // 6. Redact sensitive headers (log but don't delete, for auditing)
        for header in &self.config.redact_headers {
            if self.get_http_request_header(header).is_some() {
                self.set_http_request_header(header, Some("***REDACTED***"));
            }
        }

        Action::Continue
    }

    fn on_http_response_headers(&mut self, _: usize, _: bool) -> Action {
        // Pass request ID to response headers
        if let Some(req_id) = self.get_http_request_header("x-request-id") {
            self.set_http_response_header("x-request-id", Some(&req_id));
        }

        // Security response headers
        self.set_http_response_header("x-content-type-options", Some("nosniff"));
        self.set_http_response_header("x-frame-options", Some("DENY"));
        self.set_http_response_header("x-xss-protection", Some("1; mode=block"));
        self.set_http_response_header(
            "strict-transport-security",
            Some("max-age=31536000; includeSubDomains"),
        );

        // Remove sensitive service information
        self.remove_http_response_header("server");
        self.remove_http_response_header("x-powered-by");
        self.remove_http_response_header("x-aspnet-version");

        Action::Continue
    }
}

impl HeaderEnrichPlugin {
    fn generate_request_id(&self) -> String {
        // Use proxy-wasm to get random numbers
        let mut buf = [0u8; 16];
        // In proxy-wasm use random_bytes
        format!(
            "{:08x}-{:04x}-4{:03x}-{:04x}-{:012x}",
            self.get_current_time_nanoseconds() & 0xFFFFFFFF,
            (self.get_current_time_nanoseconds() >> 32) & 0xFFFF,
            (self.get_current_time_nanoseconds() >> 48) & 0xFFF,
            0x8000 | ((self.get_current_time_nanoseconds() >> 60) & 0x3FFF),
            self.get_current_time_nanoseconds() & 0xFFFFFFFFFFFF,
        )
    }
}
```

## 5.2 CORS Handling Plugin

```rust
// CORS handling plugin
use proxy_wasm::traits::*;
use proxy_wasm::types::*;

struct CorsPlugin {
    allowed_origins: Vec<String>,
    allowed_methods: String,
    allowed_headers: String,
    exposed_headers: String,
    max_age: String,
    allow_credentials: bool,
}

impl HttpContext for CorsPlugin {
    fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
        let method = self.get_http_request_header(":method")
            .unwrap_or_default();
        let origin = self.get_http_request_header("origin")
            .unwrap_or_default();

        if origin.is_empty() {
            return Action::Continue;
        }

        // Check if Origin is allowed
        let origin_allowed = self.allowed_origins.iter()
            .any(|allowed| {
                allowed == "*"
                    || allowed == &origin
                    || (allowed.starts_with("*.") && origin.ends_with(&allowed[1..]))
            });

        if !origin_allowed {
            self.send_http_response(
                403,
                vec![("content-type", "application/json")],
                Some(b"{\"error\":\"CORS origin not allowed\"}"),
            );
            return Action::Pause;
        }

        // Handle OPTIONS preflight request
        if method == "OPTIONS" {
            self.send_http_response(
                204,
                vec![
                    ("access-control-allow-origin", &origin),
                    ("access-control-allow-methods", &self.allowed_methods),
                    ("access-control-allow-headers", &self.allowed_headers),
                    ("access-control-max-age", &self.max_age),
                    ("access-control-allow-credentials",
                     if self.allow_credentials { "true" } else { "false" }),
                    ("vary", "Origin"),
                    ("content-length", "0"),
                ],
                None,
            );
            return Action::Pause;
        }

        Action::Continue
    }

    fn on_http_response_headers(&mut self, _: usize, _: bool) -> Action {
        let origin = self.get_http_request_header("origin")
            .unwrap_or_default();

        if !origin.is_empty() {
            let origin_allowed = self.allowed_origins.iter()
                .any(|a| a == "*" || a == &origin);

            if origin_allowed {
                self.set_http_response_header(
                    "access-control-allow-origin",
                    Some(&origin),
                );
                self.set_http_response_header(
                    "access-control-expose-headers",
                    Some(&self.exposed_headers),
                );
                if self.allow_credentials {
                    self.set_http_response_header(
                        "access-control-allow-credentials",
                        Some("true"),
                    );
                }
                self.set_http_response_header("vary", Some("Origin"));
            }
        }

        Action::Continue
    }
}
```

---

<!-- chunk: 6. Rate Limiting Plugin Implementation -->## 6. Rate Limiting Plugin Implementation

## 6.1 Token Bucket Rate Limiting

```rust
// Token bucket rate limiting plugin (using proxy-wasm shared memory)
use proxy_wasm::traits::*;
use proxy_wasm::types::*;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Deserialize)]
struct RateLimitConfig {
    rules: Vec<RateLimitRule>,
    default_limit: Option<u32>,
    key_type: KeyType,
    response_headers: bool,
}

#[derive(Deserialize)]
struct RateLimitRule {
    #[serde(default)]
    path_prefix: String,
    requests_per_second: u32,
    burst: u32,
}

#[derive(Deserialize)]
enum KeyType {
    #[serde(rename = "ip")]
    ClientIp,
    #[serde(rename = "header")]
    Header(String),
    #[serde(rename = "user")]
    AuthenticatedUser,
}

#[derive(Serialize, Deserialize)]
struct TokenBucket {
    tokens: f64,
    last_refill: u64,
    rate: f64,
    burst: f64,
}

impl TokenBucket {
    fn new(rate: u32, burst: u32) -> Self {
        Self {
            tokens: burst as f64,
            last_refill: 0,
            rate: rate as f64,
            burst: burst as f64,
        }
    }

    fn try_consume(&mut self, current_time_ns: u64) -> bool {
        // Refill tokens
        if self.last_refill > 0 {
            let elapsed_secs = (current_time_ns - self.last_refill) as f64 / 1e9;
            self.tokens = (self.tokens + elapsed_secs * self.rate).min(self.burst);
        }
        self.last_refill = current_time_ns;

        if self.tokens >= 1.0 {
            self.tokens -= 1.0;
            true
        } else {
            false
        }
    }

    fn tokens_remaining(&self) -> u32 {
        self.tokens as u32
    }

    fn reset_time(&self, current_time_ns: u64) -> u64 {
        if self.tokens < 1.0 {
            let needed = 1.0 - self.tokens;
            let wait_secs = needed / self.rate;
            current_time_ns + (wait_secs * 1e9) as u64
        } else {
            current_time_ns
        }
    }
}

struct RateLimitPlugin {
    config: RateLimitConfig,
}

impl Context for RateLimitPlugin {}

impl HttpContext for RateLimitPlugin {
    fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
        // Extract rate limit key
        let limit_key = self.extract_limit_key();
        let path = self.get_http_request_header(":path")
            .unwrap_or_default();

        // Match rate limit rule
        let rule = self.match_rule(&path);
        let (rate, burst) = match rule {
            Some(r) => (r.requests_per_second, r.burst),
            None => match self.config.default_limit {
                Some(limit) => (limit, limit * 2),
                None => return Action::Continue,
            },
        };

        let current_time = self.get_current_time_nanoseconds();
        let shared_key = format!("rl:{}:{}", limit_key, path);

        // Use CAS operation for atomic token bucket update
        let (allowed, remaining, reset_time) = self.check_and_update_bucket(
            &shared_key,
            rate,
            burst,
            current_time,
        );

        if self.config.response_headers {
            // Store rate limit info for response phase
            self.set_shared_data(
                &format!("rl_headers:{}", limit_key),
                Some(format!("{},{},{}", rate, remaining, reset_time).as_bytes()),
                None,
            ).ok();
        }

        if !allowed {
            let retry_after = ((reset_time - current_time) / 1_000_000_000 + 1).to_string();
            self.send_http_response(
                429,
                vec![
                    ("content-type", "application/json"),
                    ("retry-after", &retry_after),
                    ("x-ratelimit-limit", &rate.to_string()),
                    ("x-ratelimit-remaining", "0"),
                    ("x-ratelimit-reset", &reset_time.to_string()),
                ],
                Some(b"{\"error\":\"Too Many Requests\",\"code\":429,\"message\":\"Rate limit exceeded\"}"),
            );
            return Action::Pause;
        }

        Action::Continue
    }

    fn on_http_response_headers(&mut self, _: usize, _: bool) -> Action {
        if self.config.response_headers {
            let limit_key = self.extract_limit_key();
            if let Ok(Some((data, _))) = self.get_shared_data(
                &format!("rl_headers:{}", limit_key)
            ) {
                if let Ok(s) = String::from_utf8(data) {
                    let parts: Vec<&str> = s.split(',').collect();
                    if parts.len() == 3 {
                        self.set_http_response_header(
                            "x-ratelimit-limit",
                            Some(parts[0]),
                        );
                        self.set_http_response_header(
                            "x-ratelimit-remaining",
                            Some(parts[1]),
                        );
                        self.set_http_response_header(
                            "x-ratelimit-reset",
                            Some(parts[2]),
                        );
                    }
                }
            }
        }
        Action::Continue
    }
}

impl RateLimitPlugin {
    fn extract_limit_key(&self) -> String {
        match &self.config.key_type {
            KeyType::ClientIp => {
                self.get_property(vec!["source", "address"])
                    .and_then(|b| String::from_utf8(b).ok())
                    .map(|addr| addr.split(':').next().unwrap_or("unknown").to_string())
                    .unwrap_or_else(|| "unknown".to_string())
            }
            KeyType::Header(header) => {
                self.get_http_request_header(header)
                    .unwrap_or_else(|| "unknown".to_string())
            }
            KeyType::AuthenticatedUser => {
                self.get_http_request_header("x-authenticated-user")
                    .or_else(|| self.get_http_request_header("x-user-id"))
                    .unwrap_or_else(|| "anonymous".to_string())
            }
        }
    }

    fn match_rule<'a>(&'a self, path: &str) -> Option<&'a RateLimitRule> {
        self.config.rules.iter()
            .filter(|r| path.starts_with(&r.path_prefix))
            .max_by_key(|r| r.path_prefix.len())
    }

    fn check_and_update_bucket(
        &self,
        key: &str,
        rate: u32,
        burst: u32,
        current_time: u64,
    ) -> (bool, u32, u64) {
        loop {
            // Get current bucket state (with CAS version)
            let (bucket, cas) = match self.get_shared_data(key) {
                Ok((Some(data), cas)) => {
                    match serde_json::from_slice::<TokenBucket>(&data) {
                        Ok(b) => (b, cas),
                        Err(_) => (TokenBucket::new(rate, burst), None),
                    }
                }
                _ => (TokenBucket::new(rate, burst), None),
            };

            let mut bucket = bucket;
            let allowed = bucket.try_consume(current_time);
            let remaining = bucket.tokens_remaining();
            let reset_time = bucket.reset_time(current_time);

            // Serialize and CAS write
            let data = serde_json::to_vec(&bucket).unwrap_or_default();
            match self.set_shared_data(key, Some(&data), cas) {
                Ok(_) => return (allowed, remaining, reset_time),
                Err(Status::CasMismatch) => continue,  // Retry
                Err(_) => return (true, burst, current_time),  // On error, allow through
            }
        }
    }
}
```

## 6.2 Distributed Rate Limiting (External Service)

```rust
// Redis/external service-based distributed rate limiting
struct DistributedRateLimitPlugin {
    config: DistributedRLConfig,
    call_token: Option<u32>,
    limit_key: String,
}

#[derive(serde::Deserialize)]
struct DistributedRLConfig {
    rate_limit_service: String,
    timeout_ms: u32,
    fail_open: bool,  // Allow through when rate limit service fails
}

impl Context for DistributedRateLimitPlugin {
    fn on_http_call_response(&mut self, _: u32, _: usize, body_size: usize, _: usize) {
        let status = self.get_http_call_response_header(":status")
            .unwrap_or_default();

        match status.as_str() {
            "200" => {
                // Allow through
                self.add_http_request_header("x-ratelimit-allowed", "true");
                self.resume_http_request();
            }
            "429" => {
                // Rate limited
                let body = self.get_http_call_response_body(0, body_size)
                    .unwrap_or_default();
                self.send_http_response(429, vec![], Some(&body));
            }
            _ => {
                if self.config.fail_open {
                    self.resume_http_request();
                } else {
                    self.send_http_response(
                        503,
                        vec![],
                        Some(b"{\"error\":\"Rate limit service unavailable\"}"),
                    );
                }
            }
        }
    }
}

impl HttpContext for DistributedRateLimitPlugin {
    fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
        let client_ip = self.get_property(vec!["source", "address"])
            .and_then(|b| String::from_utf8(b).ok())
            .unwrap_or_else(|| "unknown".to_string());

        let path = self.get_http_request_header(":path")
            .unwrap_or_default();

        self.limit_key = format!("{}:{}", client_ip, path);

        let check_request = serde_json::json!({
            "key": self.limit_key,
            "descriptors": [{"key": "path", "value": path}]
        });

        match self.dispatch_http_call(
            &self.config.rate_limit_service,
            vec![
                (":method", "POST"),
                (":path", "/ratelimit"),
                (":authority", &self.config.rate_limit_service),
                ("content-type", "application/json"),
            ],
            Some(check_request.to_string().as_bytes()),
            vec![],
            std::time::Duration::from_millis(self.config.timeout_ms as u64),
        ) {
            Ok(token) => {
                self.call_token = Some(token);
                Action::Pause
            }
            Err(_) => {
                if self.config.fail_open {
                    Action::Continue
                } else {
                    self.send_http_response(503, vec![], None);
                    Action::Pause
                }
            }
        }
    }
}
```

---

<!-- chunk: 7. Observability Plugins -->## 7. Observability Plugins

## 7.1 Custom Metrics Plugin

```rust
// Comprehensive observability plugin
use proxy_wasm::traits::*;
use proxy_wasm::types::*;
use std::collections::HashMap;

struct ObservabilityPlugin {
    // Metric ID mapping
    metrics: ObservabilityMetrics,
    config: ObsConfig,
}

struct ObservabilityMetrics {
    request_total: u32,
    request_duration_ms: u32,
    request_body_bytes: u32,
    response_body_bytes: u32,
    error_total: u32,
    upstream_duration_ms: u32,
}

#[derive(serde::Deserialize)]
struct ObsConfig {
    metric_prefix: String,
    trace_sampling_rate: f64,
    log_slow_requests_ms: u64,
    #[serde(default)]
    custom_labels: HashMap<String, String>,
}

impl RootContext for ObsPlugin {
    fn on_configure(&mut self, _: usize) -> bool {
        // Register all metrics
        let prefix = self.config.metric_prefix.as_str();

        self.metrics = ObservabilityMetrics {
            request_total: self.define_metric(
                MetricType::Counter,
                &format!("{}_requests_total", prefix),
            ).unwrap_or(0),
            request_duration_ms: self.define_metric(
                MetricType::Histogram,
                &format!("{}_request_duration_milliseconds", prefix),
            ).unwrap_or(0),
            request_body_bytes: self.define_metric(
                MetricType::Counter,
                &format!("{}_request_body_bytes_total", prefix),
            ).unwrap_or(0),
            response_body_bytes: self.define_metric(
                MetricType::Counter,
                &format!("{}_response_body_bytes_total", prefix),
            ).unwrap_or(0),
            error_total: self.define_metric(
                MetricType::Counter,
                &format!("{}_errors_total", prefix),
            ).unwrap_or(0),
            upstream_duration_ms: self.define_metric(
                MetricType::Histogram,
                &format!("{}_upstream_duration_milliseconds", prefix),
            ).unwrap_or(0),
        };

        true
    }
}

struct ObsHttpContext {
    metrics: ObservabilityMetrics,
    config: ObsConfig,
    start_time: u64,
    request_size: usize,
    response_size: usize,
    should_trace: bool,
}

impl HttpContext for ObsHttpContext {
    fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
        self.start_time = self.get_current_time_nanoseconds();

        // Sampling decision
        let rand_val = (self.start_time % 10000) as f64 / 10000.0;
        self.should_trace = rand_val < self.config.trace_sampling_rate;

        // Inject trace ID
        if self.should_trace {
            let trace_id = format!("{:032x}", self.start_time);
            let span_id = format!("{:016x}", self.start_time >> 16);
            self.set_http_request_header(
                "x-b3-traceid",
                Some(&trace_id),
            );
            self.set_http_request_header(
                "x-b3-spanid",
                Some(&span_id),
            );
            self.set_http_request_header(
                "x-b3-sampled",
                Some("1"),
            );
        }

        Action::Continue
    }

    fn on_http_request_body(&mut self, body_size: usize, end_of_stream: bool) -> Action {
        self.request_size += body_size;
        Action::Continue
    }

    fn on_http_response_body(&mut self, body_size: usize, end_of_stream: bool) -> Action {
        self.response_size += body_size;
        Action::Continue
    }

    fn on_log(&mut self) {
        let end_time = self.get_current_time_nanoseconds();
        let duration_ms = (end_time - self.start_time) / 1_000_000;

        // Extract request/response information
        let method = self.get_http_request_header(":method")
            .unwrap_or_else(|| "unknown".to_string());
        let path = self.get_http_request_header(":path")
            .unwrap_or_default();
        let status_str = self.get_http_response_header(":status")
            .unwrap_or_else(|| "0".to_string());
        let status: u32 = status_str.parse().unwrap_or(0);

        // Record metrics
        self.increment_metric(self.metrics.request_total, 1);
        self.record_metric(self.metrics.request_duration_ms, duration_ms);
        self.increment_metric(self.metrics.request_body_bytes, self.request_size as u64);
        self.increment_metric(self.metrics.response_body_bytes, self.response_size as u64);

        if status >= 400 {
            self.increment_metric(self.metrics.error_total, 1);
        }

        // Slow request logging
        if duration_ms > self.config.log_slow_requests_ms {
            log::warn!(
                "slow_request: method={} path={} status={} duration_ms={} request_bytes={} response_bytes={}",
                method, path, status, duration_ms, self.request_size, self.response_size
            );
        }

        // Trace logging
        if self.should_trace {
            let trace_id = self.get_http_request_header("x-b3-traceid")
                .unwrap_or_default();
            log::info!(
                "trace: trace_id={} method={} path={} status={} duration_ms={}",
                trace_id, method, path, status, duration_ms
            );
        }
    }
}
```

## 7.2 Request/Response Body Sampling Plugin

```rust
// Request body audit sampling plugin
use proxy_wasm::traits::*;
use proxy_wasm::types::*;

struct AuditPlugin {
    sample_rate: f64,
    max_body_size: usize,
    audit_queue_id: Option<u32>,
    should_audit: bool,
    request_data: Vec<u8>,
}

impl Context for AuditPlugin {}

impl HttpContext for AuditPlugin {
    fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
        // Sampling decision
        let ts = self.get_current_time_nanoseconds();
        self.should_audit = (ts % 10000) as f64 / 10000.0 < self.sample_rate;
        Action::Continue
    }

    fn on_http_request_body(&mut self, body_size: usize, end_of_stream: bool) -> Action {
        if !self.should_audit {
            return Action::Continue;
        }

        // Read request body (with size limit)
        let read_size = body_size.min(self.max_body_size);
        if let Some(body) = self.get_http_request_body(0, read_size) {
            self.request_data = body;
        }

        if end_of_stream {
            self.flush_audit_record();
        }

        Action::Continue
    }

    fn on_log(&mut self) {
        if !self.should_audit {
            return;
        }

        let method = self.get_http_request_header(":method")
            .unwrap_or_default();
        let path = self.get_http_request_header(":path")
            .unwrap_or_default();
        let status = self.get_http_response_header(":status")
            .unwrap_or_default();
        let user = self.get_http_request_header("x-authenticated-user")
            .unwrap_or_else(|| "anonymous".to_string());

        let audit_record = serde_json::json!({
            "timestamp": self.get_current_time_nanoseconds(),
            "method": method,
            "path": path,
            "status": status,
            "user": user,
            "request_body_preview": String::from_utf8_lossy(&self.request_data[..self.request_data.len().min(200)]),
        });

        // Push to shared queue
        if let Some(queue_id) = self.audit_queue_id {
            let data = audit_record.to_string();
            self.enqueue_shared_queue(queue_id, Some(data.as_bytes())).ok();
        }
    }
}
```

---

<!-- chunk: 8. Authentication and Authorization Plugins -->## 8. Authentication and Authorization Plugins

## 8.1 JWT Validation Plugin

```rust
// JWT validation plugin (no external service dependency, local validation)
use proxy_wasm::traits::*;
use proxy_wasm::types::*;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Deserialize)]
struct JwtConfig {
    issuer: String,
    audiences: Vec<String>,
    jwks_keys: Vec<JwkKey>,    // Pre-configured public keys (avoid JWKS endpoint calls)
    clock_skew_seconds: i64,
    header_name: String,
    cookie_name: Option<String>,
    extract_claims: Vec<String>, // Claims to extract and inject as headers
}

#[derive(Deserialize, Clone)]
struct JwkKey {
    kid: String,
    kty: String,  // "RSA" or "EC"
    alg: String,  // "RS256", "ES256"
    n: Option<String>,   // RSA modulus
    e: Option<String>,   // RSA exponent
    x: Option<String>,   // EC x coordinate
    y: Option<String>,   // EC y coordinate
    crv: Option<String>, // EC curve
}

#[derive(Deserialize, Serialize)]
struct JwtClaims {
    iss: String,
    sub: String,
    #[serde(default)]
    aud: OneOrMany,
    exp: i64,
    iat: i64,
    #[serde(default)]
    nbf: Option<i64>,
    #[serde(flatten)]
    extra: HashMap<String, serde_json::Value>,
}

#[derive(Deserialize, Serialize)]
#[serde(untagged)]
enum OneOrMany {
    One(String),
    Many(Vec<String>),
}

impl Default for OneOrMany {
    fn default() -> Self { OneOrMany::Many(vec![]) }
}

struct JwtPlugin {
    config: JwtConfig,
}

impl HttpContext for JwtPlugin {
    fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
        // Extract JWT
        let token = self.extract_token();

        let token = match token {
            Some(t) => t,
            None => {
                self.send_http_response(
                    401,
                    vec![
                        ("content-type", "application/json"),
                        ("www-authenticate", &format!(
                            "Bearer realm=\"api\", error=\"invalid_request\", error_description=\"Missing token\""
                        )),
                    ],
                    Some(b"{\"error\":\"invalid_request\",\"error_description\":\"Missing authorization token\"}"),
                );
                return Action::Pause;
            }
        };

        // Parse and validate JWT (simplified implementation, actual needs cryptographic verification)
        match self.validate_jwt(&token) {
            Ok(claims) => {
                // Inject claims into request headers
                self.set_http_request_header("x-jwt-sub", Some(&claims.sub));
                self.set_http_request_header("x-jwt-iss", Some(&claims.iss));

                // Extract custom claims
                for claim_name in &self.config.extract_claims {
                    if let Some(value) = claims.extra.get(claim_name) {
                        let header_name = format!("x-jwt-{}", claim_name.replace('_', "-"));
                        let header_value = match value {
                            serde_json::Value::String(s) => s.clone(),
                            other => other.to_string(),
                        };
                        self.set_http_request_header(&header_name, Some(&header_value));
                    }
                }

                // Remove original token header (security)
                self.remove_http_request_header(&self.config.header_name);

                Action::Continue
            }
            Err(e) => {
                log::warn!("JWT validation failed: {}", e);
                self.send_http_response(
                    401,
                    vec![
                        ("content-type", "application/json"),
                        ("www-authenticate", &format!(
                            "Bearer realm=\"api\", error=\"invalid_token\", error_description=\"{}\"",
                            e
                        )),
                    ],
                    Some(format!("{{\"error\":\"invalid_token\",\"error_description\":\"{}\"}}", e).as_bytes()),
                );
                Action::Pause
            }
        }
    }
}

impl JwtPlugin {
    fn extract_token(&self) -> Option<String> {
        // 1. Extract from Authorization header
        if let Some(auth) = self.get_http_request_header(&self.config.header_name) {
            if auth.starts_with("Bearer ") {
                return Some(auth[7..].to_string());
            }
        }

        // 2. Extract from Cookie
        if let Some(cookie_name) = &self.config.cookie_name {
            if let Some(cookie_header) = self.get_http_request_header("cookie") {
                for cookie in cookie_header.split(';') {
                    let parts: Vec<&str> = cookie.trim().splitn(2, '=').collect();
                    if parts.len() == 2 && parts[0] == cookie_name {
                        return Some(parts[1].to_string());
                    }
                }
            }
        }

        // 3. Extract from Query parameter
        if let Some(path_query) = self.get_http_request_header(":path") {
            if let Some(query_start) = path_query.find('?') {
                let query = &path_query[query_start + 1..];
                for param in query.split('&') {
                    let parts: Vec<&str> = param.splitn(2, '=').collect();
                    if parts.len() == 2 && parts[0] == "access_token" {
                        return Some(parts[1].to_string());
                    }
                }
            }
        }

        None
    }

    fn validate_jwt(&self, token: &str) -> Result<JwtClaims, String> {
        // JWT consists of three parts: header.payload.signature
        let parts: Vec<&str> = token.split('.').collect();
        if parts.len() != 3 {
            return Err("Invalid JWT format".to_string());
        }

        // Decode payload (Base64URL decode)
        let payload = base64url_decode(parts[1])
            .map_err(|e| format!("Failed to decode payload: {}", e))?;

        let claims: JwtClaims = serde_json::from_slice(&payload)
            .map_err(|e| format!("Failed to parse claims: {}", e))?;

        // Validate issuer
        if claims.iss != self.config.issuer {
            return Err(format!("Invalid issuer: expected {}, got {}", self.config.issuer, claims.iss));
        }

        // Validate audience
        let aud_list = match &claims.aud {
            OneOrMany::One(s) => vec![s.as_str()],
            OneOrMany::Many(v) => v.iter().map(|s| s.as_str()).collect(),
        };
        let aud_valid = self.config.audiences.iter()
            .any(|a| aud_list.contains(&a.as_str()));
        if !aud_valid && !self.config.audiences.is_empty() {
            return Err("Invalid audience".to_string());
        }

        // Validate time
        let now = (self.get_current_time_nanoseconds() / 1_000_000_000) as i64;
        if claims.exp < now - self.config.clock_skew_seconds {
            return Err(format!("Token expired at {}", claims.exp));
        }
        if claims.iat > now + self.config.clock_skew_seconds {
            return Err("Token issued in the future".to_string());
        }
        if let Some(nbf) = claims.nbf {
            if nbf > now + self.config.clock_skew_seconds {
                return Err("Token not yet valid".to_string());
            }
        }

        // TODO: Verify signature (needs RSA/ECDSA verification implementation)
        // Signature verification is mandatory in production
        // This is simplified processing, actual needs crypto library

        Ok(claims)
    }
}

fn base64url_decode(input: &str) -> Result<Vec<u8>, String> {
    // Add padding
    let padded = match input.len() % 4 {
        0 => input.to_string(),
        2 => format!("{}==", input),
        3 => format!("{}=", input),
        _ => return Err("Invalid base64url".to_string()),
    };

    // Replace URL-safe characters
    let standard = padded.replace('-', "+").replace('_', "/");

    // Decode (simplified implementation, actual use base64 crate)
    Ok(standard.into_bytes()) // Simplified
}
```

---

<!-- chunk: 9. Data Transformation Plugins -->## 9. Data Transformation Plugins

## 9.1 Request/Response Body Transformation Plugin

```rust
// JSON <-> XML transformation plugin
use proxy_wasm::traits::*;
use proxy_wasm::types::*;
use serde_json::Value;

struct BodyTransformPlugin {
    config: TransformConfig,
    request_body: Vec<u8>,
    transform_request: bool,
    transform_response: bool,
}

#[derive(serde::Deserialize)]
struct TransformConfig {
    request_transform: Option<TransformRule>,
    response_transform: Option<TransformRule>,
    #[serde(default = "default_max_size")]
    max_body_size: usize,
}

fn default_max_size() -> usize { 1024 * 1024 } // 1MB

#[derive(serde::Deserialize)]
struct TransformRule {
    from_format: Format,
    to_format: Format,
    field_mappings: Vec<FieldMapping>,
    add_fields: std::collections::HashMap<String, Value>,
    remove_fields: Vec<String>,
}

#[derive(serde::Deserialize)]
enum Format {
    #[serde(rename = "json")]
    Json,
    #[serde(rename = "xml")]
    Xml,
    #[serde(rename = "form")]
    FormEncoded,
}

#[derive(serde::Deserialize)]
struct FieldMapping {
    from: String,
    to: String,
    transform: Option<String>,  // "uppercase", "lowercase", "string", "number"
}

impl Context for BodyTransformPlugin {}

impl HttpContext for BodyTransformPlugin {
    fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
        self.transform_request = self.config.request_transform.is_some();
        Action::Continue
    }

    fn on_http_request_body(&mut self, body_size: usize, end_of_stream: bool) -> Action {
        if !self.transform_request || !end_of_stream {
            if !end_of_stream {
                return Action::Pause;  // Wait for complete body
            }
            return Action::Continue;
        }

        let read_size = body_size.min(self.config.max_body_size);
        if let Some(body) = self.get_http_request_body(0, read_size) {
            if let Some(rule) = &self.config.request_transform {
                match self.apply_transform(&body, rule) {
                    Ok(transformed) => {
                        // Update request body
                        self.set_http_request_body(0, body_size, &transformed);
                        // Update Content-Length
                        self.set_http_request_header(
                            "content-length",
                            Some(&transformed.len().to_string()),
                        );
                        // Update Content-Type
                        let content_type = match &rule.to_format {
                            Format::Json => "application/json",
                            Format::Xml => "application/xml",
                            Format::FormEncoded => "application/x-www-form-urlencoded",
                        };
                        self.set_http_request_header("content-type", Some(content_type));
                    }
                    Err(e) => {
                        log::error!("Body transform failed: {}", e);
                        self.send_http_response(
                            400,
                            vec![("content-type", "application/json")],
                            Some(format!("{{\"error\":\"Body transformation failed: {}\"}}", e).as_bytes()),
                        );
                        return Action::Pause;
                    }
                }
            }
        }

        Action::Continue
    }

    fn on_http_response_headers(&mut self, _: usize, _: bool) -> Action {
        self.transform_response = self.config.response_transform.is_some();
        Action::Continue
    }

    fn on_http_response_body(&mut self, body_size: usize, end_of_stream: bool) -> Action {
        if !self.transform_response || !end_of_stream {
            if !end_of_stream {
                return Action::Pause;
            }
            return Action::Continue;
        }

        let read_size = body_size.min(self.config.max_body_size);
        if let Some(body) = self.get_http_response_body(0, read_size) {
            if let Some(rule) = &self.config.response_transform {
                if let Ok(transformed) = self.apply_transform(&body, rule) {
                    self.set_http_response_body(0, body_size, &transformed);
                    self.set_http_response_header(
                        "content-length",
                        Some(&transformed.len().to_string()),
                    );
                }
            }
        }

        Action::Continue
    }
}

impl BodyTransformPlugin {
    fn apply_transform(&self, body: &[u8], rule: &TransformRule) -> Result<Vec<u8>, String> {
        // Parse input
        let mut json_value = match &rule.from_format {
            Format::Json => {
                serde_json::from_slice(body)
                    .map_err(|e| format!("JSON parse error: {}", e))?
            }
            Format::FormEncoded => {
                let s = String::from_utf8_lossy(body);
                let mut map = serde_json::Map::new();
                for pair in s.split('&') {
                    let parts: Vec<&str> = pair.splitn(2, '=').collect();
                    if parts.len() == 2 {
                        map.insert(
                            parts[0].to_string(),
                            Value::String(parts[1].to_string()),
                        );
                    }
                }
                Value::Object(map)
            }
            Format::Xml => {
                // Simplified XML parsing
                Value::Object(serde_json::Map::new())
            }
        };

        // Field mapping
        if let Value::Object(ref mut map) = json_value {
            for mapping in &rule.field_mappings {
                if let Some(value) = map.remove(&mapping.from) {
                    let transformed_value = match mapping.transform.as_deref() {
                        Some("uppercase") => {
                            if let Value::String(s) = value {
                                Value::String(s.to_uppercase())
                            } else { value }
                        }
                        Some("lowercase") => {
                            if let Value::String(s) = value {
                                Value::String(s.to_lowercase())
                            } else { value }
                        }
                        Some("string") => {
                            Value::String(value.to_string())
                        }
                        Some("number") => {
                            if let Value::String(s) = &value {
                                s.parse::<f64>()
                                    .map(Value::from)
                                    .unwrap_or(value)
                            } else { value }
                        }
                        _ => value,
                    };
                    map.insert(mapping.to.clone(), transformed_value);
                }
            }

            // Add fields
            for (key, value) in &rule.add_fields {
                map.insert(key.clone(), value.clone());
            }

            // Remove fields
            for field in &rule.remove_fields {
                map.remove(field);
            }
        }

        // Serialize output
        match &rule.to_format {
            Format::Json => {
                serde_json::to_vec(&json_value)
                    .map_err(|e| format!("JSON serialize error: {}", e))
            }
            Format::FormEncoded => {
                if let Value::Object(map) = json_value {
                    let encoded: Vec<String> = map.iter()
                        .map(|(k, v)| format!("{}={}", k, v.as_str().unwrap_or("")))
                        .collect();
                    Ok(encoded.join("&").into_bytes())
                } else {
                    Err("Cannot convert non-object to form-encoded".to_string())
                }
            }
            Format::Xml => {
                // Simplified XML serialization
                Ok(format!("<root>{:?}</root>", json_value).into_bytes())
            }
        }
    }
}
```

---

<!-- chunk: 10. Plugin Debugging and Testing -->## 10. Plugin Debugging and Testing

## 10.1 Unit Testing

```rust
// tests/plugin_test.rs
#[cfg(test)]
mod tests {
    use proxy_wasm_test::*;

    #[test]
    fn test_rate_limit_allows_first_request() {
        let mut mock = MockHostFunctions::new();
        mock.set_current_time(1000000000000);
        mock.set_plugin_config(serde_json::json!({
            "requests_per_second": 10,
            "burst": 20
        }));

        let action = simulate_http_request_headers(
            &mut mock,
            vec![
                (":method", "GET"),
                (":path", "/api/test"),
                (":authority", "example.com"),
                ("x-real-ip", "192.168.1.1"),
            ],
        );

        assert_eq!(action, Action::Continue);
        assert!(!mock.sent_local_response());
    }

    #[test]
    fn test_rate_limit_blocks_exceeded_requests() {
        let mut mock = MockHostFunctions::new();
        mock.set_current_time(1000000000000);
        mock.set_plugin_config(serde_json::json!({
            "requests_per_second": 1,
            "burst": 1
        }));

        // First request passes
        simulate_http_request_headers(&mut mock, vec![
            (":method", "GET"),
            (":path", "/api/test"),
            ("x-real-ip", "192.168.1.1"),
        ]);

        // Second request is rate limited (same moment)
        let action = simulate_http_request_headers(&mut mock, vec![
            (":method", "GET"),
            (":path", "/api/test"),
            ("x-real-ip", "192.168.1.1"),
        ]);

        assert_eq!(action, Action::Pause);
        assert!(mock.sent_local_response());
        assert_eq!(mock.local_response_status(), 429);
    }

    #[test]
    fn test_jwt_plugin_valid_token() {
        let mut mock = MockHostFunctions::new();
        mock.set_plugin_config(serde_json::json!({
            "issuer": "https://auth.example.com",
            "audiences": ["api.example.com"],
            "header_name": "authorization",
            "clock_skew_seconds": 60
        }));

        // Valid JWT (Base64 encoded payload, no signature verification)
        let token = create_test_jwt("https://auth.example.com", "user123");

        let action = simulate_http_request_headers(&mut mock, vec![
            (":method", "GET"),
            (":path", "/api/data"),
            ("authorization", &format!("Bearer {}", token)),
        ]);

        assert_eq!(action, Action::Continue);
        assert_eq!(
            mock.get_added_request_header("x-jwt-sub"),
            Some("user123".to_string())
        );
    }
}

fn create_test_jwt(issuer: &str, sub: &str) -> String {
    let now = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap()
        .as_secs() as i64;

    let header = base64url_encode(b"{\"alg\":\"RS256\",\"typ\":\"JWT\"}");
    let payload = base64url_encode(
        serde_json::json!({
            "iss": issuer,
            "sub": sub,
            "aud": ["api.example.com"],
            "exp": now + 3600,
            "iat": now,
        }).to_string().as_bytes()
    );
    let signature = base64url_encode(b"fake_signature_for_testing");

    format!("{}.{}.{}", header, payload, signature)
}

fn base64url_encode(data: &[u8]) -> String {
    use std::io::Write;
    // Simplified implementation
    String::from_utf8_lossy(data).to_string()
}
```

## 10.2 Integration Testing (Using Envoy Sandbox)

```yaml
# docker-compose.test.yml
version: '3.8'

services:
  envoy:
    image: envoyproxy/envoy:v1.29.0
    ports:
      - "8080:8080"
      - "9901:9901"
    volumes:
      - ./envoy.yaml:/etc/envoy/envoy.yaml
      - ./plugin.wasm:/etc/envoy/plugin.wasm
    command: envoy -c /etc/envoy/envoy.yaml --log-level info

  upstream:
    image: kennethreitz/httpbin
    ports:
      - "8081:80"

  test-runner:
    image: curlimages/curl
    depends_on:
      - envoy
      - upstream
    entrypoint: /bin/sh
    command: |
      -c "
        sleep 2
        echo 'Test 1: Basic request'
        curl -s http://envoy:8080/get -H 'Authorization: Bearer test-token' | jq .

        echo 'Test 2: Rate limit test'
        for i in $(seq 1 20); do
          status=$(curl -s -o /dev/null -w '%{http_code}' http://envoy:8080/get)
          echo Request $i: $status
        done
      "
```

```yaml
# envoy.yaml - Test configuration
static_resources:
  listeners:
    - name: main
      address:
        socket_address:
          address: 0.0.0.0
          port_value: 8080
      filter_chains:
        - filters:
            - name: envoy.filters.network.http_connection_manager
              typed_config:
                "@type": type.googleapis.com/envoy.extensions.filters.network.http_connection_manager.v3.HttpConnectionManager
                stat_prefix: ingress_http
                http_filters:
                  # Wasm plugin
                  - name: envoy.filters.http.wasm
                    typed_config:
                      "@type": type.googleapis.com/envoy.extensions.filters.http.wasm.v3.Wasm
                      config:
                        name: "rate-limit-plugin"
                        root_id: "rate-limit"
                        vm_config:
                          runtime: "envoy.wasm.runtime.v8"
                          code:
                            local:
                              filename: /etc/envoy/plugin.wasm
                          allow_precompiled: false
                        configuration:
                          "@type": type.googleapis.com/google.protobuf.StringValue
                          value: |
                            {
                              "requests_per_second": 5,
                              "burst": 10,
                              "key_type": "ip"
                            }
                  - name: envoy.filters.http.router
                    typed_config:
                      "@type": type.googleapis.com/envoy.extensions.filters.http.router.v3.Router
                route_config:
                  name: local_route
                  virtual_hosts:
                    - name: backend
                      domains: ["*"]
                      routes:
                        - match:
                            prefix: "/"
                          route:
                            cluster: upstream_service
  clusters:
    - name: upstream_service
      connect_timeout: 5s
      type: STRICT_DNS
      lb_policy: ROUND_ROBIN
      load_assignment:
        cluster_name: upstream_service
        endpoints:
          - lb_endpoints:
              - endpoint:
                  address:
                    socket_address:
                      address: upstream
                      port_value: 80
```

---

<!-- chunk: 11. APISIX Wasm Plugins -->## 11. APISIX Wasm Plugins

## 11.1 APISIX Wasm Plugin Architecture

```mermaid
graph TB
    subgraph "Apache APISIX"
        Nginx[Nginx/OpenResty]
        LuaRuntime[Lua Runtime]
        WasmRuntime[Wasm Runtime<br/>Wasmtime/Wasmer]
        
        Nginx --> LuaRuntime
        LuaRuntime --> WasmRuntime
        WasmRuntime --> WasmPlugin[Wasm Plugin]
    end
    
    Client[HTTP Client] --> Nginx
    WasmPlugin --> |proxy-wasm ABI| WasmRuntime
```

## 11.2 APISIX Wasm Plugin Configuration

```yaml
# apisix-wasm-plugin.yaml
apiVersion: apisix.apache.org/v2
kind: ApisixRoute
metadata:
  name: api-with-wasm
  namespace: default
spec:
  http:
    - name: api-route
      match:
        paths:
          - /api/*
        methods:
          - GET
          - POST
      backends:
        - serviceName: backend-service
          servicePort: 8080
      plugins:
        # APISIX native plugin
        - name: limit-req
          enable: true
          config:
            rate: 100
            burst: 50
            key: remote_addr
        
        # Wasm plugin
        - name: wasm-plugin
          enable: true
          config:
            wasm_path: /opt/apisix/plugins/my-plugin.wasm
            config: |
              {
                "api_key_header": "x-api-key",
                "validate_upstream": true,
                "add_headers": {
                  "x-proxy-version": "apisix-2.15"
                }
              }
```

```bash
# Configure Wasm plugin via Admin API
curl -X PUT http://127.0.0.1:9180/apisix/admin/plugins/wasm \
  -H 'X-API-KEY: edd1c9f034335f136f87ad84b625c8f1' \
  -d '{
    "wasm_path": "/opt/apisix/plugins/my-plugin.wasm",
    "name": "custom-auth",
    "priority": 100
  }'

# Enable on route
curl -X PUT http://127.0.0.1:9180/apisix/admin/routes/1 \
  -H 'X-API-KEY: edd1c9f034335f136f87ad84b625c8f1' \
  -d '{
    "uri": "/api/*",
    "plugins": {
      "custom-auth": {
        "conf": "{\"secret_key\": \"my-secret\"}"
      }
    },
    "upstream": {
      "nodes": {
        "backend:8080": 1
      },
      "type": "roundrobin"
    }
  }'
```

## 11.3 Writing APISIX Plugin with AssemblyScript

```typescript
// apisix-plugin.ts (AssemblyScript)
import {
  Context,
  RootContext,
  FilterHeadersStatusValues,
  LogLevelValues,
  stream_context,
} from "@solo-io/proxy-runtime";

class PluginRootContext extends RootContext {
  onConfigure(config_size: u32): bool {
    const conf = this.getConfiguration();
    // Parse configuration
    log(LogLevelValues.info, "APISIX Wasm Plugin initialized");
    return true;
  }

  createContext(context_id: u32): Context {
    return new PluginContext(context_id, this);
  }
}

class PluginContext extends Context {
  onRequestHeaders(num_headers: u32, end_of_stream: bool): FilterHeadersStatusValues {
    // Get request method and path
    const method = this.getRequestHeader(":method");
    const path = this.getRequestHeader(":path");

    log(LogLevelValues.debug, `Processing request: ${method} ${path}`);

    // Add custom header
    this.addRequestHeader("x-wasm-processed", "true");
    this.addRequestHeader("x-processing-time", Date.now().toString());

    // Validate API Key
    const apiKey = this.getRequestHeader("x-api-key");
    if (!apiKey || apiKey.length === 0) {
      this.sendLocalResponse(
        401,
        "Unauthorized",
        `{"error":"Missing API key"}`,
        "content-type", "application/json"
      );
      return FilterHeadersStatusValues.StopIteration;
    }

    return FilterHeadersStatusValues.Continue;
  }

  onResponseHeaders(
    num_headers: u32,
    end_of_stream: bool
  ): FilterHeadersStatusValues {
    this.addResponseHeader("x-wasm-plugin", "active");
    return FilterHeadersStatusValues.Continue;
  }
}

registerRootContext(
  (context_id: u32) => new PluginRootContext(context_id),
  "apisix-wasm-plugin"
);
```

---

<!-- chunk: 12. Kong Wasm Plugins -->## 12. Kong Wasm Plugins

## 12.1 Kong PDK for Wasm

```rust
// Kong Wasm plugin (using proxy-wasm SDK)
use proxy_wasm::traits::*;
use proxy_wasm::types::*;

// Kong-specific property access
struct KongPlugin {
    config: KongPluginConfig,
}

#[derive(serde::Deserialize)]
struct KongPluginConfig {
    service_name: Option<String>,
    route_id: Option<String>,
    consumer_id: Option<String>,
    custom_logic: String,
}

impl HttpContext for KongPlugin {
    fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
        // Get route info via Kong properties
        let service_name = self.get_property(vec!["kong", "service", "name"])
            .and_then(|b| String::from_utf8(b).ok())
            .unwrap_or_else(|| "unknown".to_string());

        let route_id = self.get_property(vec!["kong", "route", "id"])
            .and_then(|b| String::from_utf8(b).ok())
            .unwrap_or_else(|| "unknown".to_string());

        let consumer = self.get_property(vec!["kong", "client", "consumer", "username"])
            .and_then(|b| String::from_utf8(b).ok());

        log::info!(
            "Kong request: service={} route={} consumer={:?}",
            service_name, route_id, consumer
        );

        // Inject Kong context into request headers
        self.set_http_request_header("x-kong-service", Some(&service_name));
        self.set_http_request_header("x-kong-route-id", Some(&route_id));
        if let Some(c) = consumer {
            self.set_http_request_header("x-consumer-username", Some(&c));
        }

        Action::Continue
    }
}
```

## 12.2 Kong Wasm Plugin Deployment

```yaml
# kong-wasm-plugin.yaml
apiVersion: configuration.konghq.com/v1
kind: KongPlugin
metadata:
  name: custom-wasm-plugin
  namespace: default
  annotations:
    kubernetes.io/ingress.class: "kong"
plugin: wasm
config:
  instance_name: custom-auth
  filters:
    - name: custom-auth
      config: |
        {
          "token_header": "x-auth-token",
          "validate_endpoint": "http://auth-service:8080/validate",
          "cache_ttl_seconds": 300
        }
---
# Bind plugin to Ingress
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-api
  annotations:
    konghq.com/plugins: custom-wasm-plugin
spec:
  rules:
    - host: api.example.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: my-service
                port:
                  number: 80
```

---

<!-- chunk: 13. Performance Optimization and Benchmarks -->## 13. Performance Optimization and Benchmarks

## 13.1 Plugin Performance Benchmarks

```
proxy-wasm Plugin Performance Benchmarks (Envoy + V8 Runtime):

Environment:
  - CPU: Intel Xeon 2.5GHz x 8 cores
  - Memory: 32GB
  - Connections: 1000 concurrent
  - Request size: 1KB header + 10KB body

Test Scenario                  P50 Latency  P99    Throughput    Memory Usage
──────────────────────────────────────────────────────────────────────────────
Baseline (no plugin)           0.8ms       2.1ms  85,000/s     45MB
Lua script plugin              1.2ms       3.5ms  72,000/s     52MB
Wasm plugin (simple headers)   0.9ms       2.4ms  81,000/s     48MB
Wasm plugin (JWT validation)   1.1ms       3.0ms  76,000/s     49MB
Wasm plugin (rate limiting)    1.0ms       2.8ms  79,000/s     50MB
Wasm plugin (external call)    2.5ms       8.0ms  35,000/s     51MB
gRPC external plugin           5.0ms      15.0ms  18,000/s     53MB
──────────────────────────────────────────────────────────────────────────────
```

## 13.2 Plugin Optimization Techniques

```rust
// Optimization technique 1: Use caching to avoid repeated parsing
static COMPILED_REGEX: std::sync::OnceLock<regex::Regex> = std::sync::OnceLock::new();

// Optimization technique 2: Pre-allocate buffers
struct OptimizedPlugin {
    header_buffer: Vec<u8>,  // Pre-allocated to avoid frequent allocations
    config: PluginConfig,
    
    // Shared data cache
    cached_jwks: Option<(u64, Vec<JwkKey>)>, // (expiry_time, keys)
}

impl HttpContext for OptimizedPlugin {
    fn on_http_request_headers(&mut self, _: usize, _: bool) -> Action {
        // Optimization technique 3: Fast path check
        let path = match self.get_http_request_header(":path") {
            Some(p) => p,
            None => return Action::Continue,  // Fast fail
        };

        // Optimization technique 4: Use shared data to cache expensive results
        let cache_key = "plugin:processed_routes";
        if let Ok((Some(data), _)) = self.get_shared_data(cache_key) {
            // Use cached result
        }

        // Optimization technique 5: Batch header operations
        let mut headers_to_add = vec![
            ("x-request-id", "generated-id"),
            ("x-timestamp", "12345"),
            ("x-service", "my-service"),
        ];
        // Use set_http_request_headers for batch setting (reduce host calls)

        Action::Continue
    }
}
```

## 13.3 Wasm Runtime Selection

```
Envoy-supported Wasm Runtime Comparison:

Runtime    Performance    Compatibility    Memory Isolation    Feature Support
─────────────────────────────────────────────────────────────────────────────
V8         ★★★★          ★★★★★           ★★★★               JS/Wasm complete
Wasmtime   ★★★★★         ★★★★            ★★★★★              WASI, Component Model
WAMR       ★★★★★         ★★★             ★★★★               Embedded optimized, low memory
Wasmer     ★★★★          ★★★★            ★★★★               Multi-backend compilation

Recommendations:
- Production: V8 (Envoy default, most mature) or Wasmtime (best performance)
- Edge/IoT: WAMR (lowest memory footprint)
- Development/Testing: Any runtime works
```

---

<!-- chunk: 14. Production Deployment Best Practices -->## 14. Production Deployment Best Practices

## 14.1 Plugin Version Management Strategy

```yaml
# Use Argo Rollout for progressive plugin rollout
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: wasm-plugin-rollout
spec:
  strategy:
    canary:
      steps:
        - setWeight: 5
        - pause: { duration: 5m }
        - setWeight: 20
        - pause: { duration: 10m }
        - setWeight: 50
        - pause: { duration: 15m }
        - setWeight: 100
      
      # Canary version uses new plugin
      canaryMetadata:
        annotations:
          wasm-plugin-version: "2.0.0"
      
      # Stable version uses old plugin
      stableMetadata:
        annotations:
          wasm-plugin-version: "1.9.0"
```

## 14.2 Multi-Cluster Plugin Distribution

``` bash
# 🟢 Low Risk: Read-only/information gathering, typically no side effects
#!/bin/bash
# deploy-wasm-plugin.sh - Multi-cluster plugin distribution script

PLUGIN_VERSION="1.2.0"
PLUGIN_FILE="auth-plugin-${PLUGIN_VERSION}.wasm"
OCI_IMAGE="ghcr.io/my-org/auth-plugin:${PLUGIN_VERSION}"
CLUSTERS=("cluster-us-east" "cluster-eu-west" "cluster-ap-south")

# 1. Build and optimize
echo "Building plugin..."
cargo build --target wasm32-unknown-unknown --release
wasm-opt -Oz \
  -o "${PLUGIN_FILE}" \
  target/wasm32-unknown-unknown/release/auth_plugin.wasm

# 2. Push to OCI registry
echo "Pushing to OCI registry..."
crane push "${PLUGIN_FILE}" "${OCI_IMAGE}"

DIGEST=$(crane digest "${OCI_IMAGE}")
echo "Plugin digest: ${DIGEST}"

# 3. Deploy to each cluster
for CLUSTER in "${CLUSTERS[@]}"; do
  echo "Deploying to ${CLUSTER}..."
  
  kubectl --context="${CLUSTER}" apply -f - << EOF
apiVersion: extensions.istio.io/v1alpha1
kind: WasmPlugin
metadata:
  name: auth-plugin
  namespace: default
spec:
  selector:
    matchLabels:
      app: api-gateway
  url: oci://${OCI_IMAGE}
  sha256: "${DIGEST#sha256:}"
  phase: AUTHN
  pluginConfig:
    version: "${PLUGIN_VERSION}"
    timeout_ms: 500
EOF

  echo "Waiting for rollout in ${CLUSTER}..."
  kubectl --context="${CLUSTER}" rollout status deployment -n istio-system
done

echo "Deployment complete!"
```

## 14.3 Plugin Monitoring and Alerting

```yaml
# prometheus-rules.yaml
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: wasm-plugin-alerts
  namespace: monitoring
spec:
  groups:
    - name: wasm-plugin-health
      interval: 30s
      rules:
        # Plugin error rate too high
        - alert: WasmPluginHighErrorRate
          expr: |
            rate(plugin_errors_total[5m]) / rate(plugin_requests_total[5m]) > 0.05
          for: 2m
          labels:
            severity: warning
          annotations:
            summary: "Wasm plugin error rate > 5%"
            description: "Plugin {{ $labels.plugin_name }} error rate is {{ $value | humanizePercentage }}"
        
        # Plugin latency too high
        - alert: WasmPluginHighLatency
          expr: |
            histogram_quantile(0.99, rate(plugin_request_duration_milliseconds_bucket[5m])) > 100
          for: 5m
          labels:
            severity: warning
          annotations:
            summary: "Wasm plugin P99 latency > 100ms"
        
        # Rate limit trigger rate too high
        - alert: WasmRateLimitExcessive
          expr: |
            rate(plugin_rate_limited_total[5m]) / rate(plugin_requests_total[5m]) > 0.1
          for: 5m
          labels:
            severity: info
          annotations:
            summary: "More than 10% of requests are being rate limited"
```

## 14.4 Troubleshooting Guide

> ⚠️ **🟡 Medium Risk** — Changes cluster resource state, recommend --dry-run or diff confirmation first
> - `kubectl exec`: Enters container to execute commands, may change container state

``` bash
# 🟡 Medium Risk: Will modify cluster/resource state, confirm target, impact scope, and authorization before execution
# Check Wasm plugin status
kubectl get wasmplugin -A

# View plugin logs in Istio proxy
kubectl logs -n default -l app=my-service \
  -c istio-proxy \
  --since=1h \
  | grep -i wasm

# Verify plugin loading
kubectl exec -n default deployment/my-service \
  -c istio-proxy \
  -- curl -s http://localhost:15000/config_dump \
  | jq '.configs[] | select(.["@type"] | contains("WasmPlugin"))'

# Check Envoy plugin statistics
kubectl exec -n default deployment/my-service \
  -c istio-proxy \
  -- curl -s http://localhost:15000/stats \
  | grep wasm

# Dynamically change log level
kubectl exec -n default deployment/my-service \
  -c istio-proxy \
  -- curl -X POST http://localhost:15000/logging?wasm=debug

# View plugin metrics
kubectl exec -n default deployment/my-service \
  -c istio-proxy \
  -- curl -s http://localhost:15020/metrics \
  | grep plugin_
```
---

<!-- chunk: Summary -->## Summary

Wasm plugin systems provide a standardized proxy extension mechanism through the **proxy-wasm specification**, achieving:

**Core Advantages**:
- 🔒 **Sandbox Security**: Plugins run in isolated Wasm VMs, issues don't affect host process
- ⚡ **High Performance**: Near-native code execution efficiency, P99 latency increase < 1ms
- 🌐 **Multi-Language**: Rust, Go, AssemblyScript, C++ can all write plugins
- 🔄 **Dynamic Loading**: Update plugins without restarting proxy
- 📦 **Portable**: One plugin runs on multiple platforms (Envoy/Istio/APISIX/Kong)

**Best Practices**:
1. Use Rust to write high-performance plugins, enable `opt-level = "z"` to minimize size
2. Leverage shared memory for cross-request state (rate limit counters, caches, etc.)
3. Async HTTP calls avoid blocking request flow
4. Distribute plugins via OCI images, verify integrity with SHA256
5. Monitor plugin runtime with [[Prometheus|Prometheus]] metrics
6. Progressive rollout of new plugin versions to reduce risk

---

*References:*
- [proxy-wasm Specification](https://github.com/proxy-wasm/spec)
- [proxy-wasm Rust SDK](https://github.com/proxy-wasm/proxy-wasm-rust-sdk)
- [Envoy Wasm Filter Documentation](https://www.envoyproxy.io/docs/envoy/latest/configuration/http/http_filters/wasm_filter)
- [Istio WasmPlugin API](https://istio.io/latest/docs/reference/config/proxy_extensions/wasm-plugin/)
- [APISIX Wasm Plugin](https://apisix.apache.org/docs/apisix/wasm/)

---

<!-- chunk: Obsidian Related Documentation -->## Obsidian Related Documentation

- Domain 38: WebAssembly Cloud Native - Global MOC
- [[domain-15-specialized-tech/README.md|Domain 38: WebAssembly Cloud Native]]
- Domain-38 WebAssembly Cloud Native - Open Source Project Index
- WebAssembly Cloud Native Fundamentals
- containerd Wasm Runtime
- SpinKube Framework Practice
- wasmCloud Platform
- WasmEdge Runtime
- Wasm Component Model
- Wasm AI Inference
- Wasm Serverless
- Wasm Security and Sandbox

## See Also

- 05-wasmedge-runtime
- 06-wasm-component-model
- 08-wasm-ai-inference
- 09-wasm-serverless

<!-- risk-assessed -->
