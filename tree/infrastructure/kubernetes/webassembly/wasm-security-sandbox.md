---
title: Wasm Security and Sandbox
description: WebAssembly security sandbox model, capability-based security mechanisms, and supply chain security practices for building secure execution boundaries in cloud-native environments.
summary: WebAssembly security sandbox model, capability-based security mechanisms, and supply chain security practices for building secure execution boundaries in cloud-native environments.
category: webassembly-cloud-native
tags:
- k8s
- wasm
- webassembly
- cloud-native
- istio
- envoy
- containerd
- opa
- ingress
- networkpolicy
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
- What is Wasm Security and Sandbox
- How to implement Wasm Security and Sandbox
- Kubernetes 38 webassembly cloud native best practices
trigger_keywords:
- Wasm
- Security
- Sandbox
- webassembly
- cloud
prerequisites:
- kubectl-basics
- service-mesh-basics
- ebpf-basics
- policy-basics
authors:
- name: Dillan Teagle
  role: contributor
---

> **Production Safety Notice**
>
> This document contains directly executable operational commands. Before execution, confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether verification has been completed in a non-production environment. Command risk level marking: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (will modify cluster state but usually reversible), 🟢 Low risk/Read-only (information gathering, no side effects).


# Wasm Security and Sandbox

> WebAssembly's security sandbox model, capability-based security mechanisms, and supply chain security practices for building secure execution boundaries in cloud-native environments.

---

<!-- chunk: Table of Contents -->## Table of Contents

1. [Wasm Security Model Overview](#1-wasm-security-model-overview)
2. [Memory Safety Mechanisms](#2-memory-safety-mechanisms)
3. [WASI Capability Model](#3-wasi-capability-model)
4. [Capability-Based Access Control](#4-capability-based-access-control)
5. [Sandbox Isolation Implementation](#5-sandbox-isolation-implementation)
6. [Wasm Supply Chain Security](#6-wasm-supply-chain-security)
7. [Runtime Security Hardening](#7-runtime-security-hardening)
8. [Security Policy Engine](#8-security-policy-engine)
9. [Wasm Vulnerability Protection](#9-wasm-vulnerability-protection)
10. [Confidential Computing and TEE](#10-confidential-computing-and-tee)
11. [Compliance and Auditing](#11-compliance-and-auditing)
12. [Security Testing and Fuzzing](#12-security-testing-and-fuzzing)
13. [Production Security Best Practices](#13-production-security-best-practices)
14. [Security Incident Response](#14-security-incident-response)

---

<!-- chunk: 1. Wasm Security Model Overview -->## 1. Wasm Security Model Overview

## 1.1 Core Wasm Security Properties

WebAssembly has incorporated security as a first principle from its initial design, featuring four core security properties:

```mermaid
graph TB
    subgraph "Four Pillars of Wasm Security"
        MemSafe[Memory Safety<br/>Linear Memory Isolation]
        TypeSafe[Type Safety<br/>Strong Type System]
        SandBox[Sandbox Isolation<br/>Capability-Limited Execution]
        CodeInteg[Code Integrity<br/>Validation Mechanism]
    end

    subgraph "Security Property Details"
        MemSafe --> |"No Out-of-Bounds Access<br/>No Dangling Pointers"| MemDetail[All Memory Accesses Runtime Validated]
        TypeSafe --> |"Function Signature Verification<br/>Type Checking"| TypeDetail[Static Type Validation at Load Time]
        SandBox --> |"WASI Capabilities<br/>Host Function Restrictions"| SandDetail[Access Only Explicitly Granted Resources]
        CodeInteg --> |"Wasm Validation<br/>SHA256 Checksum"| IntegDetail[Module Integrity Verification Before Load]
    end
```

## 1.2 Security Boundary Model

```mermaid
graph LR
    subgraph "Host OS"
        subgraph "Wasm Runtime (wasmtime)"
            subgraph "Wasm Instance A"
                LinearMem_A[Linear Memory A<br/>0 ~ 4GB]
                Tables_A[Tables A]
                Globals_A[Globals A]
            end
            
            subgraph "Wasm Instance B"
                LinearMem_B[Linear Memory B<br/>Independent Address Space]
                Tables_B[Tables B]
                Globals_B[Globals B]
            end
            
            HostFunctions[Host Functions<br/>Explicitly Exposed]
            WASI[WASI Interface<br/>Capability Limited]
        end
        
        FileSystem[File System]
        Network[Network]
        Env[Environment Variables]
    end
    
    Wasm_A --> |Can Only Access| LinearMem_A
    Wasm_B --> |Can Only Access| LinearMem_B
    Wasm_A -.-> |Direct Access Prohibited| Wasm_B
    WASI --> |Capability Control| FileSystem
    WASI --> |Capability Control| Network
```

## 1.3 Comparison with Traditional Security Technologies

```
Security Technology Comparison:

┌─────────────────────────────────────────────────────────────┐
│ Technology      │ Memory Isolation │ Type Safety │ Startup Overhead │ Fine-Grained Control │
├─────────────────────────────────────────────────────────────┤
│ Process Isolation │ ★★★★★         │ ✗           │ High             │ Medium                │
│ Containers        │ ★★★★          │ ✗           │ Medium           │ Medium                │
│ VM/Hypervisor     │ ★★★★★         │ ✗           │ Very High        │ Low                   │
│ Wasm              │ ★★★★★         │ ★★★★★       │ Extremely Low    │ High                  │
│ eBPF              │ ★★★★          │ ★★★★        │ Extremely Low    │ High                  │
│ WASM+eBPF         │ ★★★★★         │ ★★★★★       │ Extremely Low    │ Extremely High        │
└─────────────────────────────────────────────────────────────┘
```

---

<!-- chunk: 2. Memory Safety Mechanisms -->## 2. Memory Safety Mechanisms

## 2.1 Linear Memory Model

```mermaid
graph TB
    subgraph "Wasm Linear Memory Layout"
        Stack[Stack Region<br/>Local Variables]
        Heap[Heap Region<br/>Dynamic Allocation]
        Data[Data Segment<br/>Global Variables]
        Code[Code Segment<br/>Read-Only]
        
        Boundary[Bounds Checking<br/>Validation Per Access]
    end
    
    subgraph "Memory Operation Validation"
        Load[i32.load / i64.load]
        Store[i32.store / i64.store]
        
        Load --> |"offset + size <= memory.size"| Boundary
        Store --> |"offset + size <= memory.size"| Boundary
    end
    
    subgraph "Memory Growth"
        GrowOp[memory.grow]
        SizeOp[memory.size]
        MaxMem[Maximum Memory Limit<br/>Configuration Constraint]
        
        GrowOp --> |Constrained By| MaxMem
    end
```

## 2.2 Memory Access Validation Implementation

```rust
// wasmtime memory bounds checking principle
// This is a conceptual internal runtime implementation

struct LinearMemory {
    data: *mut u8,
    current_size: usize,   // Current size (bytes)
    maximum_size: usize,   // Maximum size
    protection: MemoryProtection,
}

struct MemoryProtection {
    accessible: *mut u8,     // Start of accessible region
    accessible_size: usize,  // Accessible region size
    // Beyond accessible region is protected memory pages (SIGSEGV)
}

// Runtime check for memory access (pseudocode)
fn check_memory_access(
    mem: &LinearMemory,
    offset: u32,
    size: u32,
) -> Result<(), TrapCode> {
    let end = (offset as u64) + (size as u64);
    
    if end > mem.current_size as u64 {
        return Err(TrapCode::MemoryOutOfBounds);
    }
    
    Ok(())
}

// Actual bounds check code generated at compile time (Cranelift IR example)
// i32.load offset=0 align=4
// Equivalent to:
// bounds_check(ptr, 4)
// result = *(ptr as *const i32)
```

## 2.3 Memory Access Configuration

```rust
// wasmtime memory security configuration
use wasmtime::{Config, Engine, MemoryCreator};

fn create_secure_engine() -> anyhow::Result<Engine> {
    let mut config = Config::new();
    
    // === Memory Safety Configuration ===
    
    // Maximum memory size (prevent DoS)
    config.max_wasm_stack(512 * 1024);  // 512KB stack limit
    
    // Linear memory limits
    config.static_memory_maximum_size(100 * 1024 * 1024);  // 100MB maximum
    config.static_memory_guard_size(2 * 1024 * 1024);      // 2MB guard page
    config.dynamic_memory_guard_size(64 * 1024);            // 64KB dynamic guard
    
    // Use guard pages for out-of-bounds traps (faster than runtime checks)
    config.guard_before_linear_memory(true);
    
    // Memory initialization (CoW optimization)
    config.memory_init_cow(true);
    
    // Disable multi-memory proposal (if not needed)
    // config.wasm_multi_memory(false);
    
    // === Execution Safety Configuration ===
    
    // Enable epoch interruption (prevent infinite loops)
    config.epoch_interruption(true);
    
    // Configure fuel (limit instruction count)
    // config.consume_fuel(true);
    
    // Disable unsafe features
    config.wasm_simd(true);    // SIMD is safe
    config.wasm_threads(false); // Disable shared memory (prevent Spectre)
    
    Engine::new(&config)
}
```

## 2.4 Memory Isolation Validation Tests

```rust
// Tests to verify Wasm memory isolation
#[cfg(test)]
mod memory_safety_tests {
    use wasmtime::*;
    
    #[test]
    fn test_out_of_bounds_access_trapped() {
        let engine = Engine::default();
        let wat = r#"
            (module
                (memory 1)
                (func (export "oob-read") (result i32)
                    ;; Attempt to read at page 65536 (beyond memory bounds)
                    i32.const 65536
                    i32.load
                )
            )
        "#;
        
        let module = Module::new(&engine, wat).unwrap();
        let mut store = Store::new(&engine, ());
        let instance = Instance::new(&mut store, &module, &[]).unwrap();
        
        let oob_read = instance
            .get_typed_func::<(), i32>(&mut store, "oob-read")
            .unwrap();
        
        // Should trigger trap, not memory corruption
        let result = oob_read.call(&mut store, ());
        assert!(result.is_err(), "Out of bounds access should trap");
        
        let err = result.unwrap_err();
        assert!(
            err.to_string().contains("out of bounds"),
            "Error should indicate out of bounds: {}",
            err
        );
    }
    
    #[test]
    fn test_instance_memory_isolation() {
        let engine = Engine::default();
        let wat = r#"
            (module
                (memory 1)
                (global $magic_value (mut i32) (i32.const 0xDEADBEEF))
                (func (export "get-magic") (result i32)
                    global.get $magic_value
                )
                (func (export "set-magic") (param i32)
                    local.get 0
                    global.set $magic_value
                )
            )
        "#;
        
        let module = Module::new(&engine, wat).unwrap();
        let mut store = Store::new(&engine, ());
        
        // Create two independent instances
        let instance1 = Instance::new(&mut store, &module, &[]).unwrap();
        let instance2 = Instance::new(&mut store, &module, &[]).unwrap();
        
        let get1 = instance1.get_typed_func::<(), i32>(&mut store, "get-magic").unwrap();
        let set1 = instance1.get_typed_func::<i32, ()>(&mut store, "set-magic").unwrap();
        let get2 = instance2.get_typed_func::<(), i32>(&mut store, "get-magic").unwrap();
        
        // Modify instance1's value
        set1.call(&mut store, 0x12345678).unwrap();
        
        let val1 = get1.call(&mut store, ()).unwrap();
        let val2 = get2.call(&mut store, ()).unwrap();
        
        // Two instances have completely isolated memory
        assert_eq!(val1, 0x12345678);
        assert_eq!(val2, 0xDEADBEEFu32 as i32, "Instance 2 should not be affected");
    }
    
    #[test]
    fn test_memory_growth_limit() {
        let mut config = Config::new();
        config.static_memory_maximum_size(10 * 1024 * 1024);  // 10MB limit
        let engine = Engine::new(&config).unwrap();
        
        let wat = r#"
            (module
                (memory 1 160)  ;; Maximum 160 pages = 10MB
                (func (export "grow") (param i32) (result i32)
                    local.get 0
                    memory.grow
                )
            )
        "#;
        
        let module = Module::new(&engine, wat).unwrap();
        let mut store = Store::new(&engine, ());
        let instance = Instance::new(&mut store, &module, &[]).unwrap();
        
        let grow = instance.get_typed_func::<i32, i32>(&mut store, "grow").unwrap();
        
        // Valid growth
        let result = grow.call(&mut store, 10).unwrap();
        assert!(result >= 0, "Should succeed within limit");
        
        // Exceeds limit
        let result = grow.call(&mut store, 1000).unwrap();
        assert_eq!(result, -1, "Should fail when exceeding limit");
    }
}
```

---

<!-- chunk: 3. WASI Capability Model -->## 3. WASI Capability Model

## 3.1 WASI Zero-Permission Principle

```
WASI Permission Model: Deny by Default

Grant capabilities at startup > Execute code > Access authorized resources

Traditional process permission model:
  Process inherits parent process permissions
  Can request more permissions via syscall
  
WASI capability model:
  Runtime decides which capabilities to grant
  Wasm module cannot expand permissions on its own
  All resource access must go through capability handles
```

```mermaid
graph TD
    subgraph "WASI Capability Delegation"
        Runtime[Wasm Runtime<br/>Capability Grantor]
        
        subgraph "Pre-opened Resources"
            Dir1[/allowed/path Directory]
            Dir2[/tmp Directory]
            Stdin[Standard Input]
            Stdout[Standard Output]
        end
        
        subgraph "Wasm Module"
            Module[Module Code]
            FD1[File Descriptor 3<br/>→ /allowed/path]
            FD2[File Descriptor 4<br/>→ /tmp]
            FD0[FD 0 → stdin]
            FD1_out[FD 1 → stdout]
        end
        
        Runtime --> |"preopened_dirs"| FD1
        Runtime --> |"preopened_dirs"| FD2
        Runtime --> FD0
        Runtime --> FD1_out
        
        Module --> FD1
        Module --> FD2
        Module -.-> |Access Prohibited| HostFS[Host Other Files]
    end
```

## 3.2 WASI Capability Configuration

```rust
// Fine-grained WASI capability configuration
use wasmtime_wasi::{WasiCtxBuilder, ambient_authority};
use std::path::Path;

fn build_restricted_wasi_ctx(
    allowed_dirs: &[(&str, &str)],  // (host_path, guest_path)
    allowed_envs: &[(&str, &str)],  // (key, value)
    inherit_stdio: bool,
    allow_network: bool,
) -> anyhow::Result<wasmtime_wasi::WasiCtx> {
    let mut builder = WasiCtxBuilder::new();
    
    // === Filesystem Capabilities ===
    for (host_path, guest_path) in allowed_dirs {
        // Only allow access to specified directories (no directory traversal)
        let dir = wasmtime_wasi::Dir::open_ambient_dir(
            host_path,
            ambient_authority(),
        )?;
        builder.preopened_dir(dir, guest_path)?;
    }
    
    // === Environment Variable Capabilities ===
    // Don't inherit host environment variables, only expose explicitly allowed variables
    for (key, value) in allowed_envs {
        builder.env(key, value)?;
    }
    
    // === Standard IO Capabilities ===
    if inherit_stdio {
        builder.inherit_stdin()
                .inherit_stdout()
                .inherit_stderr();
    } else {
        // Redirect to /dev/null
        builder.stdin(wasmtime_wasi::pipe::ReadPipe::from(""))
               .stdout(wasmtime_wasi::pipe::WritePipe::new_in_memory())
               .stderr(wasmtime_wasi::pipe::WritePipe::new_in_memory());
    }
    
    // === Network Capabilities (WASI Preview 2) ===
    if allow_network {
        // Allow TCP connections
        // Note: Current WASI network capability control is limited in granularity
        builder.socket_addr_check(|addr, socket_type| {
            // Only allow connections to specific addresses
            let allowed_hosts = ["10.0.0.0/8", "192.168.0.0/16"];
            // Actual implementation needs IP address matching logic
            true
        });
    }
    
    // === Time Capabilities ===
    // Allow reading clock (allowed by default)
    
    // === Random Number Capabilities ===
    // Allow using random number generator (allowed by default)
    
    // === Process Exit Capabilities ===
    // Control whether to allow proc_exit
    builder.allow_blocking_current_thread(false);
    
    Ok(builder.build())
}

// Production environment recommended configuration
fn production_wasi_config(
    app_name: &str,
    data_dir: &str,
) -> anyhow::Result<wasmtime_wasi::WasiCtx> {
    build_restricted_wasi_ctx(
        &[
            (data_dir, "/data"),               // Data directory (read-write)
            ("/etc/ssl/certs", "/etc/ssl/certs"), // CA certificates (read-only)
        ],
        &[
            ("RUST_LOG", "info"),
            ("APP_NAME", app_name),
            ("TZ", "UTC"),
        ],
        false,  // Don't inherit stdio
        false,  // Don't allow network (proxy through host functions)
    )
}
```

## 3.3 Custom Capability Interfaces

```rust
// Implement custom capability interface (controlled host functions)
use wasmtime::{Engine, Linker, Store};

struct SecureCapabilities {
    allowed_http_hosts: Vec<String>,
    allowed_db_tables: Vec<String>,
    rate_limit: u32,
    request_count: u32,
}

impl SecureCapabilities {
    fn new(
        allowed_http_hosts: Vec<String>,
        allowed_db_tables: Vec<String>,
        rate_limit: u32,
    ) -> Self {
        Self {
            allowed_http_hosts,
            allowed_db_tables,
            rate_limit,
            request_count: 0,
        }
    }
    
    fn check_http_allowed(&self, url: &str) -> bool {
        self.allowed_http_hosts.iter().any(|host| {
            url.starts_with(&format!("https://{}", host))
                || url.starts_with(&format!("http://{}", host))
        })
    }
    
    fn check_rate_limit(&mut self) -> bool {
        if self.request_count >= self.rate_limit {
            return false;
        }
        self.request_count += 1;
        true
    }
}

fn register_secure_capabilities(
    linker: &mut Linker<SecureCapabilities>,
) -> anyhow::Result<()> {
    // HTTP request (controlled)
    linker.func_wrap(
        "secure-caps",
        "http-get",
        |mut caller: wasmtime::Caller<SecureCapabilities>,
         url_ptr: u32,
         url_len: u32,
         result_ptr: u32| -> i32 {
            // Read URL
            let url = {
                let mem = caller.get_export("memory")
                    .and_then(|e| e.into_memory())
                    .expect("memory export required");
                
                let data = mem.data(&caller);
                let bytes = &data[url_ptr as usize..(url_ptr + url_len) as usize];
                String::from_utf8_lossy(bytes).to_string()
            };
            
            // Check URL whitelist
            if !caller.data().check_http_allowed(&url) {
                eprintln!("SECURITY: HTTP request to blocked host: {}", url);
                return -1;  // Reject
            }
            
            // Check rate limit
            if !caller.data_mut().check_rate_limit() {
                eprintln!("SECURITY: Rate limit exceeded");
                return -2;  // Rate limited
            }
            
            // Execute actual HTTP request (using reqwest, etc.)
            // ... actual implementation
            0
        }
    )?;
    
    // Database access (controlled)
    linker.func_wrap(
        "secure-caps",
        "db-query",
        |mut caller: wasmtime::Caller<SecureCapabilities>,
         table_ptr: u32,
         table_len: u32,
         query_ptr: u32,
         query_len: u32| -> i32 {
            let table = {
                let mem = caller.get_export("memory")
                    .and_then(|e| e.into_memory())
                    .expect("memory export required");
                let data = mem.data(&caller);
                String::from_utf8_lossy(
                    &data[table_ptr as usize..(table_ptr + table_len) as usize]
                ).to_string()
            };
            
            // Check table whitelist
            if !caller.data().allowed_db_tables.contains(&table) {
                eprintln!("SECURITY: Access to unauthorized table: {}", table);
                return -1;
            }
            
            // Execute query
            0
        }
    )?;
    
    // Logging (always allowed, but forced prefix)
    linker.func_wrap(
        "secure-caps",
        "log",
        |caller: wasmtime::Caller<SecureCapabilities>,
         level: i32,
         msg_ptr: u32,
         msg_len: u32| {
            let mem = caller.get_export("memory")
                .and_then(|e| e.into_memory())
                .expect("memory export required");
            let data = mem.data(&caller);
            let msg = String::from_utf8_lossy(
                &data[msg_ptr as usize..(msg_ptr + msg_len) as usize]
            );
            
            let level_str = match level {
                0 => "ERROR",
                1 => "WARN",
                2 => "INFO",
                3 => "DEBUG",
                _ => "UNKNOWN",
            };
            
            // All logs prefixed with [wasm] for easy auditing
            println!("[wasm][{}] {}", level_str, msg);
        }
    )?;
    
    Ok(())
}
```

---

<!-- chunk: 4. Capability-Based Access Control -->## 4. Capability-Based Access Control

## 4.1 WASI Capability Tree

```
WASI Capability Hierarchy:

Root Capability (Runtime Holds)
├── Filesystem Capability
│   ├── preopened_dir("/data") → FD 3
│   │   ├── path_open("file.txt") → FD 5
│   │   ├── path_read_dir(".") → FD 6
│   │   └── fd_read(FD 5) 
│   └── preopened_dir("/tmp") → FD 4
│
├── Network Capability (WASI Preview 2)
│   ├── TCP listen
│   ├── TCP connect (restricted hosts)
│   └── UDP socket
│
├── Time Capability
│   ├── clock_time_get(REALTIME)
│   └── clock_time_get(MONOTONIC)
│
├── Random Number Capability
│   └── random_get()
│
└── Process Capability
    ├── proc_exit()
    └── args_get() / environ_get()
```

## 4.2 Fine-Grained Filesystem Capability Control

```rust
// Implement read-only filesystem access control
use wasmtime_wasi::{WasiCtx, WasiCtxBuilder};
use cap_std::fs::Dir;

fn create_readonly_fs_ctx(base_dir: &str) -> anyhow::Result<WasiCtx> {
    let dir = Dir::open_ambient_dir(base_dir, cap_std::ambient_authority())?;
    
    // Create read-only wrapper (controlled via permission bits)
    let readonly_dir = cap_std::fs::Dir::from_std_file(
        dir.open(".")?.into_std()
    );
    
    let ctx = WasiCtxBuilder::new()
        .preopened_dir(readonly_dir, "/")?
        .build();
    
    Ok(ctx)
}

// Path sandboxing (prevent directory traversal attacks)
fn sanitize_path(base: &str, user_path: &str) -> anyhow::Result<std::path::PathBuf> {
    use std::path::Path;
    
    let base = Path::new(base).canonicalize()?;
    let requested = base.join(user_path);
    
    // Prevent .. directory traversal
    let canonical = requested.canonicalize()
        .unwrap_or_else(|_| requested.clone());
    
    if !canonical.starts_with(&base) {
        anyhow::bail!(
            "Path traversal detected: {} is outside {}", 
            user_path, base.display()
        );
    }
    
    Ok(canonical)
}

// File access policy enforcer
struct FileAccessPolicy {
    allowed_extensions: Vec<String>,
    max_file_size_bytes: u64,
    allow_create: bool,
    allow_delete: bool,
    read_only_paths: Vec<String>,
}

impl FileAccessPolicy {
    fn check_access(
        &self,
        path: &str,
        operation: &str,
    ) -> Result<(), String> {
        // Check extension
        let ext = std::path::Path::new(path)
            .extension()
            .and_then(|e| e.to_str())
            .unwrap_or("");
        
        if !self.allowed_extensions.is_empty()
            && !self.allowed_extensions.contains(&ext.to_string())
        {
            return Err(format!(
                "File extension '{}' not allowed", ext
            ));
        }
        
        // Check read-only paths
        let is_readonly = self.read_only_paths.iter()
            .any(|p| path.starts_with(p));
        
        if is_readonly && (operation == "write" || operation == "delete") {
            return Err(format!("Write access denied to readonly path: {}", path));
        }
        
        // Check create/delete permissions
        if operation == "create" && !self.allow_create {
            return Err("File creation not allowed".to_string());
        }
        if operation == "delete" && !self.allow_delete {
            return Err("File deletion not allowed".to_string());
        }
        
        Ok(())
    }
}
```

## 4.3 OPA/Rego Policy Integration

```rego
# wasm-access-policy.rego
package wasm.access

import future.keywords.if
import future.keywords.in

# Default deny all access
default allow = false

# Allow rules
allow if {
    # Check principal
    valid_principal
    # Check resource
    allowed_resource
    # Check operation
    allowed_operation
}

# Verify Wasm module signature
valid_principal if {
    signature := input.module.signature
    signature.issuer in data.trusted_issuers
    not signature.revoked
    signature.expiry > time.now_ns()
}

# Resource access control
allowed_resource if {
    # Filesystem: only allow specific paths
    input.resource.type == "filesystem"
    path := input.resource.path
    some allowed_path in data.policies.filesystem.allowed_paths
    startswith(path, allowed_path)
}

allowed_resource if {
    # Network: only allow whitelisted hosts
    input.resource.type == "network"
    host := input.resource.host
    host in data.policies.network.allowed_hosts
}

allowed_resource if {
    # Environment variables: only allow whitelisted variables
    input.resource.type == "env"
    key := input.resource.key
    key in data.policies.env.allowed_keys
}

# Operation permissions
allowed_operation if {
    input.resource.type == "filesystem"
    input.operation in {"read", "readdir", "stat"}
}

allowed_operation if {
    input.resource.type == "filesystem"
    input.operation in {"write", "create", "delete"}
    # Write operations require additional authorization
    input.module.labels["write-access"] == "true"
}

# Rate limiting rules
rate_limit_ok if {
    current_rate := data.metrics.current_rps[input.module.id]
    max_rate := data.policies.rate_limits[input.module.labels["tier"]]
    current_rate <= max_rate
}
```

```rust
// Rust integration with OPA policy evaluation
use serde_json::{json, Value};

struct OpaEnforcer {
    opa_endpoint: String,
    policy_package: String,
}

impl OpaEnforcer {
    async fn evaluate(
        &self,
        module_id: &str,
        resource_type: &str,
        resource: &Value,
        operation: &str,
    ) -> anyhow::Result<bool> {
        let input = json!({
            "module": {
                "id": module_id,
                "labels": {},
                "signature": {
                    "issuer": "trusted-ca",
                    "revoked": false,
                    "expiry": u64::MAX,
                }
            },
            "resource": {
                "type": resource_type,
                ..resource.as_object().cloned().unwrap_or_default()
            },
            "operation": operation,
        });
        
        let url = format!(
            "{}/v1/data/{}/allow",
            self.opa_endpoint,
            self.policy_package.replace('.', "/")
        );
        
        let client = reqwest::Client::new();
        let resp: Value = client.post(&url)
            .json(&json!({"input": input}))
            .send().await?
            .json().await?;
        
        Ok(resp["result"].as_bool().unwrap_or(false))
    }
}
```

---

<!-- chunk: 5. Sandbox Isolation Implementation -->## 5. Sandbox Isolation Implementation

## 5.1 Multi-Layer Sandbox Architecture

```mermaid
graph TB
    subgraph "Multi-Layer Sandbox Defense"
        subgraph "Layer 1: Wasm Validation"
            TypeCheck[Type Checking]
            MemCheck[Memory Checking]
            StructCheck[Structure Validation]
        end
        
        subgraph "Layer 2: Runtime Isolation"
            LinearMem[Linear Memory Isolation]
            EpochInterrupt[Epoch Interruption]
            FuelLimit[Fuel Limiting]
        end
        
        subgraph "Layer 3: WASI Capabilities"
            FSCap[Filesystem Capability]
            NetCap[Network Capability]
            EnvCap[Environment Variable Capability]
        end
        
        subgraph "Layer 4: OS-Level Isolation"
            Seccomp[seccomp Filtering]
            Namespace[Linux Namespace]
            cgroup[cgroup Resource Limits]
        end
        
        subgraph "Layer 5: Hardware Isolation"
            SGX[Intel SGX / AMD SEV]
            TrustZone[ARM TrustZone]
        end
    end
```

## 5.2 Seccomp Hardening

```rust
// Use seccomp to further restrict Wasm runtime syscalls
use seccompiler::{
    BpfProgram, SeccompAction, SeccompCmpArgLen, SeccompCmpOp,
    SeccompCondition, SeccompFilter, SeccompRule,
};

fn create_wasm_runtime_seccomp() -> anyhow::Result<BpfProgram> {
    // Only allow syscalls needed by Wasm runtime
    let allowed_syscalls = vec![
        // Memory management
        "mmap", "mprotect", "munmap", "mremap",
        "madvise", "brk",
        
        // File IO (only allow operations on pre-opened FDs)
        "read", "write", "pread64", "pwrite64",
        "readv", "writev",
        "close", "fstat", "lseek",
        
        // Time
        "clock_gettime", "gettimeofday",
        
        // Random numbers
        "getrandom",
        
        // Threading (used by wasmtime)
        "futex", "clone3",
        
        // Process
        "exit", "exit_group",
        
        // Signals (used for timeouts)
        "rt_sigaction", "rt_sigreturn",
        "sigaltstack",
    ];
    
    let filter = SeccompFilter::new(
        // Default action: kill process
        SeccompAction::KillProcess,
        // Rule set
        allowed_syscalls.into_iter().map(|name| {
            (name.to_string(), vec![SeccompRule::new(vec![])])
        }).collect(),
        // Target architecture
        seccompiler::TargetArch::x86_64,
    )?;
    
    filter.try_into()
}

fn apply_wasm_sandbox_restrictions() -> anyhow::Result<()> {
    // Apply seccomp filter
    let bpf = create_wasm_runtime_seccomp()?;
    seccompiler::apply_filter(&bpf)?;
    
    println!("Seccomp filter applied");
    Ok(())
}
```

## 5.3 Resource Limit Configuration

```rust
// Complete resource limit configuration
use wasmtime::{Config, Engine, Store};

struct ResourceLimits {
    max_memory_bytes: usize,
    max_wasm_stack_bytes: usize,
    max_instances: usize,
    max_tables: usize,
    max_table_elements: u32,
    max_memories: u32,
    cpu_time_limit_ns: u64,
    max_fuel: u64,
}

impl Default for ResourceLimits {
    fn default() -> Self {
        Self {
            max_memory_bytes: 64 * 1024 * 1024,   // 64MB
            max_wasm_stack_bytes: 512 * 1024,      // 512KB
            max_instances: 100,
            max_tables: 10,
            max_table_elements: 100_000,
            max_memories: 1,
            cpu_time_limit_ns: 10_000_000_000,    // 10 seconds
            max_fuel: 1_000_000_000,              // 1 billion instructions
        }
    }
}

struct LimitedStore {
    limits: ResourceLimits,
    wasi: wasmtime_wasi::WasiCtx,
}

impl wasmtime::ResourceLimiter for LimitedStore {
    fn memory_growing(
        &mut self,
        current: usize,
        desired: usize,
        maximum: Option<usize>,
    ) -> anyhow::Result<bool> {
        if desired > self.limits.max_memory_bytes {
            eprintln!(
                "Memory growth blocked: {} > {} bytes",
                desired, self.limits.max_memory_bytes
            );
            return Ok(false);
        }
        Ok(true)
    }
    
    fn table_growing(
        &mut self,
        current: u32,
        desired: u32,
        maximum: Option<u32>,
    ) -> anyhow::Result<bool> {
        if desired > self.limits.max_table_elements {
            return Ok(false);
        }
        Ok(true)
    }
    
    fn instances(&self) -> usize { self.limits.max_instances }
    fn tables(&self) -> usize { self.limits.max_tables }
    fn memories(&self) -> usize { self.limits.max_memories as usize }
}

fn create_limited_store(
    engine: &Engine,
    limits: ResourceLimits,
    wasi: wasmtime_wasi::WasiCtx,
) -> Store<LimitedStore> {
    let mut store = Store::new(engine, LimitedStore { limits, wasi });
    
    // Set resource limiter
    store.limiter(|state| state);
    
    // Set fuel (instruction count limit)
    let max_fuel = store.data().limits.max_fuel;
    store.set_fuel(max_fuel).unwrap();
    
    // Set epoch interruption
    store.set_epoch_deadline(100);  // 100 epoch ticks
    
    store
}
```

---

<!-- chunk: 6. Wasm Supply Chain Security -->## 6. Wasm Supply Chain Security

## 6.1 Supply Chain Attack Threat Model

```mermaid
graph TD
    subgraph "Wasm Supply Chain Attack Surface"
        Source[Source Code Malicious Injection]
        Dep[Malicious Dependency Packages]
        Build[Build Environment Contamination]
        Registry[Registry Poisoning]
        Transport[Transport Tampering]
        Deploy[Deployment Misconfiguration]
    end
    
    subgraph "Protection Measures"
        SBOM[SBOM Software Bill of Materials]
        Signing[Digital Signature]
        Verification[Integrity Verification]
        PolicyEnforce[Policy Enforcement]
        AuditLog[Audit Logging]
    end
    
    Source --> SBOM
    Dep --> SBOM
    Build --> Signing
    Registry --> Verification
    Transport --> Signing
    Deploy --> PolicyEnforce
```

## 6.2 Wasm Module Signing

```rust
// Wasm module signing and verification
use ring::{
    signature::{Ed25519KeyPair, KeyPair, Signature, UnparsedPublicKey, ED25519},
    rand::SystemRandom,
};
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
struct WasmModuleMetadata {
    module_id: String,
    name: String,
    version: String,
    author: String,
    description: String,
    sha256: String,
    capabilities: Vec<String>,
    created_at: u64,
}

#[derive(Debug, Serialize, Deserialize)]
struct SignedWasmModule {
    metadata: WasmModuleMetadata,
    signature: String,    // Base64 encoded signature
    public_key: String,   // Base64 encoded public key
    wasm_base64: String,  // Base64 encoded wasm bytes
}

fn sign_wasm_module(
    wasm_bytes: &[u8],
    metadata: WasmModuleMetadata,
    private_key_pkcs8: &[u8],
) -> anyhow::Result<SignedWasmModule> {
    use base64::Engine;
    use sha2::Digest;
    
    // Calculate SHA256
    let sha256 = format!("{:x}", sha2::Sha256::digest(wasm_bytes));
    
    // Serialize metadata (including SHA256)
    let mut meta = metadata;
    meta.sha256 = sha256;
    let metadata_json = serde_json::to_string(&meta)?;
    
    // Create signature content (metadata + wasm hash)
    let sign_content = format!(
        "{}\n{}",
        metadata_json,
        meta.sha256
    );
    
    // Use Ed25519 signature
    let key_pair = Ed25519KeyPair::from_pkcs8(private_key_pkcs8)
        .map_err(|e| anyhow::anyhow!("Invalid private key: {:?}", e))?;
    
    let signature = key_pair.sign(sign_content.as_bytes());
    let public_key = key_pair.public_key().as_ref().to_vec();
    
    Ok(SignedWasmModule {
        metadata: meta,
        signature: base64::engine::general_purpose::STANDARD.encode(signature.as_ref()),
        public_key: base64::engine::general_purpose::STANDARD.encode(&public_key),
        wasm_base64: base64::engine::general_purpose::STANDARD.encode(wasm_bytes),
    })
}

fn verify_wasm_module(
    signed_module: &SignedWasmModule,
    trusted_public_keys: &[Vec<u8>],
) -> anyhly::Result<Vec<u8>> {
    use base64::Engine;
    use sha2::Digest;
    
    // 1. Decode data
    let wasm_bytes = base64::engine::general_purpose::STANDARD
        .decode(&signed_module.wasm_base64)?;
    let signature = base64::engine::general_purpose::STANDARD
        .decode(&signed_module.signature)?;
    let public_key = base64::engine::general_purpose::STANDARD
        .decode(&signed_module.public_key)?;
    
    // 2. Verify public key is trusted
    if !trusted_public_keys.contains(&public_key) {
        anyhow::bail!("Untrusted public key");
    }
    
    // 3. Verify content integrity
    let actual_sha256 = format!("{:x}", sha2::Sha256::digest(&wasm_bytes));
    if actual_sha256 != signed_module.metadata.sha256 {
        anyhow::bail!(
            "SHA256 mismatch: expected {}, got {}",
            signed_module.metadata.sha256,
            actual_sha256
        );
    }
    
    // 4. Verify signature
    let metadata_json = serde_json::to_string(&signed_module.metadata)?;
    let sign_content = format!(
        "{}\n{}",
        metadata_json,
        signed_module.metadata.sha256
    );
    
    let unparsed_key = UnparsedPublicKey::new(&ED25519, &public_key);
    unparsed_key.verify(sign_content.as_bytes(), &signature)
        .map_err(|_| anyhow::anyhow!("Signature verification failed"))?;
    
    println!("✅ Module {} v{} verified successfully",
        signed_module.metadata.name, signed_module.metadata.version);
    
    Ok(wasm_bytes)
}
```

## 6.3 SBOM Generation and Verification

```rust
// Generate Wasm Software Bill of Materials (SBOM)
use serde::{Deserialize, Serialize};

#[derive(Debug, Serialize, Deserialize)]
struct WasmSBOM {
    format: String,      // "CycloneDX" or "SPDX"
    version: String,
    metadata: SBOMMetadata,
    components: Vec<SBOMComponent>,
    dependencies: Vec<Dependency>,
    vulnerabilities: Vec<Vulnerability>,
}

#[derive(Debug, Serialize, Deserialize)]
struct SBOMMetadata {
    timestamp: String,
    tools: Vec<String>,
    component: SBOMComponent,
}

#[derive(Debug, Serialize, Deserialize)]
struct SBOMComponent {
    component_type: String,
    name: String,
    version: String,
    purl: String,         // Package URL
    hashes: Vec<Hash>,
    licenses: Vec<String>,
    supplier: Option<String>,
}

#[derive(Debug, Serialize, Deserialize)]
struct Hash {
    algorithm: String,   // "SHA-256", "SHA-512"
    value: String,
}

#[derive(Debug, Serialize, Deserialize)]
struct Dependency {
    r#ref: String,
    depends_on: Vec<String>,
}

#[derive(Debug, Serialize, Deserialize)]
struct Vulnerability {
    id: String,           // CVE-XXXX-XXXXX
    source: String,
    severity: String,
    affected: Vec<String>,
    recommendation: String,
}

fn generate_sbom(
    module_name: &str,
    module_version: &str,
    wasm_bytes: &[u8],
    cargo_lock: &str,  // Cargo.lock content
) -> WasmSBOM {
    use sha2::Digest;
    
    let sha256 = format!("{:x}", sha2::Sha256::digest(wasm_bytes));
    let sha512 = format!("{:x}", sha2::Sha512::digest(wasm_bytes));
    
    // Parse Cargo.lock to get dependencies
    let components = parse_cargo_lock_to_sbom_components(cargo_lock);
    
    WasmSBOM {
        format: "CycloneDX".to_string(),
        version: "1.5".to_string(),
        metadata: SBOMMetadata {
            timestamp: chrono::Utc::now().to_rfc3339(),
            tools: vec!["wasm-sbom-generator/1.0.0".to_string()],
            component: SBOMComponent {
                component_type: "application".to_string(),
                name: module_name.to_string(),
                version: module_version.to_string(),
                purl: format!(
                    "pkg:wasm/{}/{}@{}",
                    "my-org", module_name, module_version
                ),
                hashes: vec![
                    Hash { algorithm: "SHA-256".to_string(), value: sha256 },
                    Hash { algorithm: "SHA-512".to_string(), value: sha512 },
                ],
                licenses: vec!["Apache-2.0".to_string()],
                supplier: Some("My Organization".to_string()),
            },
        },
        components,
        dependencies: vec![],
        vulnerabilities: vec![],
    }
}

fn parse_cargo_lock_to_sbom_components(_cargo_lock: &str) -> Vec<SBOMComponent> {
    // Parse dependencies in Cargo.lock
    // Actual implementation uses cargo_lock crate
    vec![]
}
```

## 6.4 OCI Image Signing (Cosign)

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend --dry-run or diff to confirm first
> - `kubectl apply/create/replace`: Creates/modifies cluster resources

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, confirm target, impact scope, and authorization before execution
#!/bin/bash
# sign-and-verify-wasm.sh

WASM_FILE="my-plugin.wasm"
OCI_IMAGE="ghcr.io/my-org/my-plugin:1.0.0"
KEYLESS=true  # Use Sigstore keyless signing

# === Build and push OCI image ===
echo "Pushing Wasm OCI image..."
crane push "${WASM_FILE}" "${OCI_IMAGE}" \
  --media-type "application/vnd.module.wasm.content.layer.v1+wasm"

# === Generate SBOM ===
syft "${OCI_IMAGE}" -o cyclonedx-json > sbom.json
echo "SBOM generated"

# === Sign with Cosign (keyless mode) ===
if [ "$KEYLESS" = true ]; then
  echo "Signing with Sigstore (keyless)..."
  COSIGN_EXPERIMENTAL=1 cosign sign \
    --annotations "module.name=my-plugin" \
    --annotations "module.version=1.0.0" \
    "${OCI_IMAGE}"
  
  # Attach SBOM
  COSIGN_EXPERIMENTAL=1 cosign attach sbom \
    --sbom sbom.json \
    --type cyclonedx \
    "${OCI_IMAGE}"
else
  # Sign with key
  cosign sign \
    --key cosign.key \
    "${OCI_IMAGE}"
fi

echo "Image signed successfully"

# === Verify signature ===
echo "Verifying signature..."
if [ "$KEYLESS" = true ]; then
  COSIGN_EXPERIMENTAL=1 cosign verify \
    --certificate-identity "https://github.com/my-org/my-repo/.github/workflows/build.yml@refs/heads/main" \
    --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
    "${OCI_IMAGE}"
else
  cosign verify \
    --key cosign.pub \
    "${OCI_IMAGE}"
fi

echo "✅ Signature verified"

# === Use Kyverno policy in K8s ===
cat > kyverno-wasm-policy.yaml << 'EOF'
apiVersion: kyverno.io/v1
kind: ClusterPolicy
metadata:
  name: verify-wasm-images
spec:
  validationFailureAction: enforce
  rules:
    - name: verify-wasm-signature
      match:
        any:
          - resources:
              kinds: ["WasmPlugin"]
      verifyImages:
        - imageReferences:
            - "ghcr.io/my-org/*"
          attestors:
            - count: 1
              entries:
                - keyless:
                    subject: "https://github.com/my-org/my-repo/*"
                    issuer: "https://token.actions.githubusercontent.com"
                    rekor:
                      url: "https://rekor.sigstore.dev"
          attestations:
            - predicateType: "https://cyclonedx.org/bom"
              conditions:
                - all:
                    - key: "{{ components[] | length(@) }}"
                      operator: GreaterThanOrEquals
                      value: 1
EOF

kubectl apply -f kyverno-wasm-policy.yaml
```

---

<!-- chunk: 7. Runtime Security Hardening -->## 7. Runtime Security Hardening

## 7.1 Comprehensive Security Configuration

```rust
// Production-grade Wasm runtime security configuration
use wasmtime::{Config, Engine, OptLevel};

fn create_hardened_engine() -> anyhow::Result<Engine> {
    let mut config = Config::new();
    
    // === Memory Safety ===
    config.max_wasm_stack(512 * 1024);              // 512KB stack
    config.static_memory_maximum_size(256 * 1024 * 1024); // 256MB maximum memory
    config.static_memory_guard_size(4 * 1024 * 1024);     // 4MB guard page
    config.dynamic_memory_guard_size(64 * 1024);
    config.guard_before_linear_memory(true);
    config.memory_init_cow(true);
    
    // === Execution Safety ===
    config.epoch_interruption(true);   // Support timeout interruption
    config.consume_fuel(true);         // Support instruction counting
    config.debug_info(false);          // Disable debug info in production
    
    // === Wasm Feature Control ===
    config.wasm_threads(false);        // Disable multi-threading (prevent Spectre)
    config.wasm_simd(true);            // SIMD is safe
    config.wasm_bulk_memory(true);     // Safe feature
    config.wasm_reference_types(true); // Safe feature
    config.wasm_multi_memory(false);   // Disable multi-memory unless necessary
    
    // === Compilation Safety ===
    config.cranelift_opt_level(OptLevel::Speed);
    config.parallel_compilation(true);
    
    // === Caching (security considerations) ===
    // Don't use shared cache (avoid cache poisoning)
    // config.cache_config_load_default()?;  // Use cautiously in production
    
    Engine::new(&config)
}

// Execution timeout control
struct TimeoutController {
    engine: Engine,
    epoch_deadline_multiplier: u64,
}

impl TimeoutController {
    fn new(engine: Engine) -> Self {
        // Start epoch incrementing thread
        let engine_clone = engine.clone();
        std::thread::spawn(move || {
            loop {
                std::thread::sleep(std::time::Duration::from_millis(1));
                engine_clone.increment_epoch();
            }
        });
        
        Self {
            engine,
            epoch_deadline_multiplier: 1000,  // 1000ms per unit
        }
    }
    
    fn create_store_with_timeout<T>(
        &self,
        data: T,
        timeout_ms: u64,
    ) -> wasmtime::Store<T> {
        let mut store = wasmtime::Store::new(&self.engine, data);
        
        // Set epoch deadline (interrupt after timeout_ms milliseconds)
        let deadline = timeout_ms / self.epoch_deadline_multiplier;
        store.set_epoch_deadline(deadline.max(1));
        
        // Set timeout callback
        store.epoch_deadline_callback(|_| {
            anyhow::bail!("Execution timed out")
        });
        
        store
    }
}
```

## 7.2 Anomaly Detection and Protection

```rust
// Wasm runtime anomaly behavior detection
use std::sync::atomic::{AtomicU64, Ordering};
use std::sync::Arc;

struct AnomalyDetector {
    memory_growth_count: AtomicU64,
    fuel_consumed: AtomicU64,
    host_call_count: AtomicU64,
    error_count: AtomicU64,
    
    thresholds: AnomalyThresholds,
}

struct AnomalyThresholds {
    max_memory_growths_per_minute: u64,
    max_fuel_per_request: u64,
    max_host_calls_per_request: u64,
    max_errors_per_minute: u64,
}

impl AnomalyDetector {
    fn record_memory_growth(&self) {
        let count = self.memory_growth_count.fetch_add(1, Ordering::Relaxed) + 1;
        if count > self.thresholds.max_memory_growths_per_minute {
            eprintln!("ANOMALY: Excessive memory growth detected");
            // Trigger alert
        }
    }
    
    fn record_fuel_consumption(&self, fuel: u64) {
        let total = self.fuel_consumed.fetch_add(fuel, Ordering::Relaxed) + fuel;
        if total > self.thresholds.max_fuel_per_request {
            eprintln!("ANOMALY: Fuel consumption limit exceeded: {}", total);
        }
    }
    
    fn record_host_call(&self, function_name: &str) {
        let count = self.host_call_count.fetch_add(1, Ordering::Relaxed) + 1;
        if count > self.thresholds.max_host_calls_per_request {
            eprintln!(
                "ANOMALY: Too many host calls ({}): {}",
                count, function_name
            );
        }
    }
    
    fn generate_report(&self) -> AnomalyReport {
        AnomalyReport {
            memory_growths: self.memory_growth_count.load(Ordering::Relaxed),
            fuel_consumed: self.fuel_consumed.load(Ordering::Relaxed),
            host_calls: self.host_call_count.load(Ordering::Relaxed),
            errors: self.error_count.load(Ordering::Relaxed),
        }
    }
}

#[derive(Debug, serde::Serialize)]
struct AnomalyReport {
    memory_growths: u64,
    fuel_consumed: u64,
    host_calls: u64,
    errors: u64,
}
```

---

<!-- chunk: 8. Security Policy Engine -->## 8. Security Policy Engine

## 8.1 Built-in Policy Enforcement

```rust
// Wasm security policy engine
use std::collections::HashMap;

#[derive(Debug, Clone, serde::Deserialize)]
pub struct SecurityPolicy {
    pub name: String,
    pub rules: Vec<PolicyRule>,
    pub enforcement: EnforcementMode,
}

#[derive(Debug, Clone, serde::Deserialize)]
pub enum EnforcementMode {
    Enforce,  // Enforce, deny violations
    Audit,    // Audit mode, log but don't block
    Permissive, // Permissive mode, warn only
}

#[derive(Debug, Clone, serde::Deserialize)]
pub struct PolicyRule {
    pub name: String,
    pub resource_type: ResourceType,
    pub operations: Vec<Operation>,
    pub action: PolicyAction,
    pub conditions: Vec<Condition>,
}

#[derive(Debug, Clone, serde::Deserialize)]
pub enum ResourceType {
    Memory,
    File,
    Network,
    Env,
    Clock,
    Random,
    Process,
}

#[derive(Debug, Clone, serde::Deserialize)]
pub enum Operation {
    Read,
    Write,
    Execute,
    Delete,
    Create,
    Connect,
    Listen,
    Grow,
}

#[derive(Debug, Clone, serde::Deserialize)]
pub enum PolicyAction {
    Allow,
    Deny,
    Audit,
    Alert(AlertLevel),
}

#[derive(Debug, Clone, serde::Deserialize)]
pub enum AlertLevel {
    Info,
    Warning,
    Critical,
}

#[derive(Debug, Clone, serde::Deserialize)]
pub struct Condition {
    pub field: String,
    pub operator: ConditionOperator,
    pub value: serde_json::Value,
}

#[derive(Debug, Clone, serde::Deserialize)]
pub enum ConditionOperator {
    Equals,
    NotEquals,
    Contains,
    StartsWith,
    GreaterThan,
    LessThan,
    Matches,  // Regex
}

pub struct PolicyEngine {
    policies: Vec<SecurityPolicy>,
    audit_log: Vec<AuditEntry>,
}

#[derive(Debug)]
struct AuditEntry {
    timestamp: std::time::SystemTime,
    module_id: String,
    resource_type: String,
    operation: String,
    resource: String,
    decision: String,
    matched_rule: Option<String>,
}

impl PolicyEngine {
    pub fn new(policies: Vec<SecurityPolicy>) -> Self {
        Self {
            policies,
            audit_log: Vec::new(),
        }
    }
    
    pub fn evaluate(
        &mut self,
        module_id: &str,
        resource_type: &ResourceType,
        operation: &Operation,
        resource: &str,
        context: &HashMap<String, serde_json::Value>,
    ) -> PolicyDecision {
        for policy in &self.policies {
            for rule in &policy.rules {
                // Check resource type match
                if !self.resource_type_matches(&rule.resource_type, resource_type) {
                    continue;
                }
                
                // Check operation match
                if !rule.operations.iter().any(|op| self.operation_matches(op, operation)) {
                    continue;
                }
                
                // Check conditions
                if !self.evaluate_conditions(&rule.conditions, context) {
                    continue;
                }
                
                // Rule matched, apply action
                let decision = match &rule.action {
                    PolicyAction::Allow => PolicyDecision::Allow,
                    PolicyAction::Deny => PolicyDecision::Deny(rule.name.clone()),
                    PolicyAction::Audit => {
                        self.log_audit(module_id, resource_type, operation, resource, 
                            "ALLOW_WITH_AUDIT", Some(&rule.name));
                        PolicyDecision::Allow
                    }
                    PolicyAction::Alert(level) => {
                        self.trigger_alert(module_id, &rule.name, resource, level);
                        PolicyDecision::Allow
                    }
                };
                
                // Record audit log
                self.log_audit(
                    module_id,
                    resource_type,
                    operation,
                    resource,
                    &format!("{:?}", decision),
                    Some(&rule.name),
                );
                
                return decision;
            }
        }
        
        // No matching rule, default deny
        self.log_audit(module_id, resource_type, operation, resource, "DENY_DEFAULT", None);
        PolicyDecision::Deny("default-deny".to_string())
    }
    
    fn resource_type_matches(&self, rule_type: &ResourceType, actual: &ResourceType) -> bool {
        matches!(
            (rule_type, actual),
            (ResourceType::Memory, ResourceType::Memory)
            | (ResourceType::File, ResourceType::File)
            | (ResourceType::Network, ResourceType::Network)
            | (ResourceType::Env, ResourceType::Env)
        )
    }
    
    fn operation_matches(&self, rule_op: &Operation, actual: &Operation) -> bool {
        matches!(
            (rule_op, actual),
            (Operation::Read, Operation::Read)
            | (Operation::Write, Operation::Write)
            | (Operation::Execute, Operation::Execute)
        )
    }
    
    fn evaluate_conditions(
        &self,
        conditions: &[Condition],
        context: &HashMap<String, serde_json::Value>,
    ) -> bool {
        conditions.iter().all(|cond| {
            let value = context.get(&cond.field);
            match (&cond.operator, value) {
                (ConditionOperator::Equals, Some(v)) => v == &cond.value,
                (ConditionOperator::NotEquals, Some(v)) => v != &cond.value,
                (ConditionOperator::Contains, Some(serde_json::Value::String(s))) => {
                    cond.value.as_str().map(|p| s.contains(p)).unwrap_or(false)
                }
                (ConditionOperator::StartsWith, Some(serde_json::Value::String(s))) => {
                    cond.value.as_str().map(|p| s.starts_with(p)).unwrap_or(false)
                }
                _ => false,
            }
        })
    }
    
    fn log_audit(
        &mut self,
        module_id: &str,
        _resource_type: &ResourceType,
        _operation: &Operation,
        resource: &str,
        decision: &str,
        matched_rule: Option<&str>,
    ) {
        self.audit_log.push(AuditEntry {
            timestamp: std::time::SystemTime::now(),
            module_id: module_id.to_string(),
            resource_type: "unknown".to_string(),
            operation: "unknown".to_string(),
            resource: resource.to_string(),
            decision: decision.to_string(),
            matched_rule: matched_rule.map(|r| r.to_string()),
        });
    }
    
    fn trigger_alert(
        &self,
        module_id: &str,
        rule_name: &str,
        resource: &str,
        level: &AlertLevel,
    ) {
        eprintln!(
            "[{:?}] Security Alert: module={} rule={} resource={}",
            level, module_id, rule_name, resource
        );
        // TODO: Send to SIEM system
    }
    
    pub fn get_audit_log(&self) -> &[AuditEntry] {
        &self.audit_log
    }
}

#[derive(Debug, PartialEq)]
pub enum PolicyDecision {
    Allow,
    Deny(String),  // Denial reason
}
```

---

<!-- chunk: 9. Wasm Vulnerability Protection -->## 9. Wasm Vulnerability Protection

## 9.1 Known Wasm Vulnerability Protection

```
Wasm Known Security Issues and Protections:

1. Spectre/Meltdown (Speculative Execution Attacks)
   ✅ Protection:
   - Disable SharedArrayBuffer (wasm_threads = false)
   - Use time jitter
   - Periodically flush speculation buffers
   
2. Integer Overflow/Truncation
   ✅ Protection:
   - Use checked arithmetic
   - Rust default debug mode detects overflow
   - Explicitly handle overflow in production
   
3. Type Confusion
   ✅ Protection:
   - Wasm type system automatically protects
   - Runtime type checking
   
4. Denial of Service (DoS)
   ✅ Protection:
   - Fuel/Epoch limit execution time
   - Memory upper bounds
   - Rate limiting
   
5. Host Function Injection
   ✅ Protection:
   - Minimize exposed host functions
   - Input validation
   - Principle of least capability
   
6. Arbitrary Code Execution (Wasm → Host)
   ✅ Protection:
   - Strict host function review
   - Don't expose eval/exec-like functions
   - Prohibit Wasm from accessing runtime memory
```

## 9.2 Secure Coding Practices

```rust
// Wasm secure coding examples

// ❌ Unsafe: Unvalidated user input
fn process_user_data_unsafe(ptr: u32, len: u32) -> u32 {
    // Dangerous: No bounds checking
    let slice = unsafe {
        std::slice::from_raw_parts(ptr as *const u8, len as usize)
    };
    // Process data...
    0
}

// ✅ Safe: Validate input and use safe APIs
fn process_user_data_safe(data: &[u8]) -> Result<Vec<u8>, String> {
    // Input size limit
    const MAX_INPUT_SIZE: usize = 10 * 1024 * 1024;  // 10MB
    if data.len() > MAX_INPUT_SIZE {
        return Err(format!("Input too large: {} bytes", data.len()));
    }
    
    // UTF-8 validation
    let text = std::str::from_utf8(data)
        .map_err(|e| format!("Invalid UTF-8: {}", e))?;
    
    // Business validation
    if text.contains('\0') {
        return Err("Null bytes not allowed".to_string());
    }
    
    // Safe processing
    Ok(text.to_uppercase().into_bytes())
}

// ❌ Unsafe: Integer overflow
fn calculate_offset_unsafe(base: u32, offset: u32) -> u32 {
    base + offset  // Can overflow
}

// ✅ Safe: Checked arithmetic
fn calculate_offset_safe(base: u32, offset: u32) -> Result<u32, String> {
    base.checked_add(offset)
        .ok_or_else(|| format!("Integer overflow: {} + {}", base, offset))
}

// ❌ Unsafe: Ignore errors
fn write_to_file_unsafe(path: &str, data: &[u8]) {
    std::fs::write(path, data).ok();  // Ignore errors
}

// ✅ Safe: Properly handle errors and validate paths
fn write_to_file_safe(
    base_dir: &str,
    relative_path: &str,
    data: &[u8],
) -> Result<(), String> {
    // Prevent path traversal
    if relative_path.contains("..") || relative_path.starts_with('/') {
        return Err(format!("Invalid path: {}", relative_path));
    }
    
    let full_path = std::path::Path::new(base_dir).join(relative_path);
    
    // Verify path is within allowed directory
    let canonical = full_path.canonicalize()
        .or_else(|_| full_path.parent()
            .and_then(|p| p.canonicalize().ok())
            .map(|p| p.join(full_path.file_name().unwrap_or_default()))
            .ok_or_else(|| std::io::Error::new(std::io::ErrorKind::NotFound, "invalid path"))
        )
        .map_err(|e| e.to_string())?;
    
    if !canonical.starts_with(base_dir) {
        return Err("Path traversal detected".to_string());
    }
    
    // Size limit
    const MAX_FILE_SIZE: usize = 100 * 1024 * 1024;  // 100MB
    if data.len() > MAX_FILE_SIZE {
        return Err(format!("File too large: {} bytes", data.len()));
    }
    
    std::fs::write(&canonical, data)
        .map_err(|e| format!("Write failed: {}", e))
}
```

---

<!-- chunk: 10. Confidential Computing and TEE -->## 10. Confidential Computing and TEE

## 10.1 Wasm + Intel SGX

```mermaid
graph TB
    subgraph "Intel SGX + Wasm"
        subgraph "SGX Enclave"
            WasmRT[Wasm Runtime<br/>wasmtime/WAMR]
            WasmModule[Wasm Module]
            SecretData[Encryption Keys<br/>Confidential Data]
            
            WasmRT --> WasmModule
            WasmModule --> SecretData
        end
        
        subgraph "Untrusted Memory"
            OS[Operating System]
            OtherProc[Other Processes]
        end
        
        SGX_Boundary[SGX Hardware Boundary] 
        
        OS -.-> |Cannot Access| SGX_Boundary
        OtherProc -.-> |Cannot Access| SGX_Boundary
    end
    
    subgraph "Remote Attestation"
        Attestation[Remote Attestation]
        TrustVerify[Trust Verification]
    end
    
    SGX_Boundary --> |Attestation Report| Attestation
    Attestation --> TrustVerify
```

```rust
// Enarx framework: Run Wasm in TEE
// https://github.com/enarx/enarx

// Enarx supports multiple TEE backends:
// - Intel SGX
// - AMD SEV
// - ARM TrustZone

// Deploy using Enarx
// enarx deploy --wasmcfg keep.yaml my-module.wasm

// keep.yaml
// --------
// # keep.yaml - Enarx deployment configuration
// files:
//   - path: "wasmtime"
//     kind: "stdin"
//   - path: "wasmtime"
//     kind: "stdout"
// 
// args:
//   - name: "my-module"
//     value: "/dev/stdin"

// Access TEE features from Wasm module
#[cfg(target_arch = "wasm32")]
mod tee_features {
    // Get remote attestation report
    extern "C" {
        fn get_attestation_report(
            user_data: *const u8,
            user_data_len: u32,
            report: *mut u8,
            report_len: *mut u32,
        ) -> i32;
        
        fn seal_data(
            data: *const u8,
            data_len: u32,
            sealed: *mut u8,
            sealed_len: *mut u32,
        ) -> i32;
        
        fn unseal_data(
            sealed: *const u8,
            sealed_len: u32,
            data: *mut u8,
            data_len: *mut u32,
        ) -> i32;
    }
    
    pub fn attest(user_data: &[u8]) -> Result<Vec<u8>, i32> {
        let mut report = vec![0u8; 4096];
        let mut report_len = report.len() as u32;
        
        let result = unsafe {
            get_attestation_report(
                user_data.as_ptr(),
                user_data.len() as u32,
                report.as_mut_ptr(),
                &mut report_len,
            )
        };
        
        if result != 0 {
            return Err(result);
        }
        
        report.truncate(report_len as usize);
        Ok(report)
    }
}
```

## 10.2 Confidential Computing Workflow

```yaml
# confidential-computing-deployment.yaml
# Run Wasm using Confidential Containers (CoCo)

apiVersion: v1
kind: Pod
metadata:
  name: confidential-wasm-pod
  namespace: confidential
  annotations:
    io.containerd.cri.runtime-handler: "kata-containers"
spec:
  runtimeClassName: kata-cc  # Confidential Containers runtime
  
  containers:
    - name: wasm-service
      image: ghcr.io/my-org/confidential-service:1.0.0
      
      # Confidential config injected via sealed storage
      env:
        - name: SECRET_KEY
          valueFrom:
            secretKeyRef:
              name: encrypted-secrets
              key: service-key
      
      resources:
        limits:
          memory: "256Mi"
          cpu: "1"
          # Request SGX/SEV resources
          # sgx.intel.com/epc: "128Mi"

---
# Run confidential K8s cluster using Constellation
# constellation create --attestation azure-sev-snp
# constellation apply
```

---

<!-- chunk: 11. Compliance and Auditing -->## 11. Compliance and Auditing

## 11.1 Audit Logging System

```rust
// Comprehensive audit logging implementation
use serde::{Deserialize, Serialize};
use std::io::Write;

#[derive(Debug, Serialize, Deserialize)]
pub struct AuditEvent {
    pub event_id: String,
    pub timestamp: String,
    pub module_id: String,
    pub module_version: String,
    pub event_type: AuditEventType,
    pub resource: Option<AuditResource>,
    pub outcome: AuditOutcome,
    pub user_context: Option<UserContext>,
    pub metadata: serde_json::Value,
}

#[derive(Debug, Serialize, Deserialize)]
pub enum AuditEventType {
    ModuleLoaded,
    ModuleUnloaded,
    FunctionCalled,
    ResourceAccessed,
    PolicyViolation,
    SecurityAlert,
    Configuration,
}

#[derive(Debug, Serialize, Deserialize)]
pub struct AuditResource {
    pub resource_type: String,
    pub resource_id: String,
    pub operation: String,
}

#[derive(Debug, Serialize, Deserialize)]
pub enum AuditOutcome {
    Success,
    Failure(String),
    Blocked(String),
}

#[derive(Debug, Serialize, Deserialize)]
pub struct UserContext {
    pub user_id: Option<String>,
    pub session_id: Option<String>,
    pub request_id: String,
    pub source_ip: Option<String>,
}

pub struct AuditLogger {
    output: Box<dyn Write + Send>,
    filter: AuditFilter,
}

pub struct AuditFilter {
    include_types: Vec<AuditEventType>,
    min_severity: SeverityLevel,
}

#[derive(PartialOrd, Ord, PartialEq, Eq)]
pub enum SeverityLevel {
    Debug,
    Info,
    Warning,
    Error,
    Critical,
}

impl AuditLogger {
    pub fn new_syslog() -> Self {
        Self {
            output: Box::new(std::io::stderr()),
            filter: AuditFilter {
                include_types: vec![
                    AuditEventType::PolicyViolation,
                    AuditEventType::SecurityAlert,
                    AuditEventType::ResourceAccessed,
                ],
                min_severity: SeverityLevel::Info,
            },
        }
    }
    
    pub fn log(&mut self, event: AuditEvent) {
        // Serialize to JSON Lines format
        if let Ok(json) = serde_json::to_string(&event) {
            writeln!(self.output, "{}", json).ok();
        }
    }
    
    pub fn log_module_loaded(
        &mut self,
        module_id: &str,
        module_version: &str,
        sha256: &str,
    ) {
        self.log(AuditEvent {
            event_id: uuid_v4(),
            timestamp: now_rfc3339(),
            module_id: module_id.to_string(),
            module_version: module_version.to_string(),
            event_type: AuditEventType::ModuleLoaded,
            resource: None,
            outcome: AuditOutcome::Success,
            user_context: None,
            metadata: serde_json::json!({
                "sha256": sha256,
                "loaded_at": now_rfc3339(),
            }),
        });
    }
    
    pub fn log_policy_violation(
        &mut self,
        module_id: &str,
        resource: &str,
        operation: &str,
        rule: &str,
    ) {
        self.log(AuditEvent {
            event_id: uuid_v4(),
            timestamp: now_rfc3339(),
            module_id: module_id.to_string(),
            module_version: "unknown".to_string(),
            event_type: AuditEventType::PolicyViolation,
            resource: Some(AuditResource {
                resource_type: "file".to_string(),
                resource_id: resource.to_string(),
                operation: operation.to_string(),
            }),
            outcome: AuditOutcome::Blocked(rule.to_string()),
            user_context: None,
            metadata: serde_json::json!({
                "violated_rule": rule,
            }),
        });
    }
}

fn uuid_v4() -> String {
    format!("{:032x}", std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap_or_default()
        .as_nanos())
}

fn now_rfc3339() -> String {
    chrono::Utc::now().to_rfc3339()
}
```

## 11.2 Compliance Checklist

```yaml
# compliance-checklist.yaml
# Wasm deployment compliance checks

security_controls:
  
  # === Module Integrity ===
  module_integrity:
    - name: "SHA256 Verification"
      required: true
      check: "module_sha256_verified"
      
    - name: "Digital Signature Verification"
      required: true
      check: "module_signature_valid"
      
    - name: "SBOM Present"
      required: true
      check: "sbom_present"
  
  # === Runtime Security ===
  runtime_security:
    - name: "Memory Limit Configured"
      required: true
      check: "memory_limit_configured"
      
    - name: "CPU Time Limit"
      required: true
      check: "cpu_time_limit_configured"
      
    - name: "Fuel Limit"
      required: true
      check: "fuel_limit_configured"
      
    - name: "Network Access Whitelist"
      required: true
      check: "network_allowlist_configured"
      
    - name: "Filesystem Access Restricted"
      required: true
      check: "filesystem_access_restricted"
  
  # === Auditing ===
  audit:
    - name: "Audit Logging Enabled"
      required: true
      check: "audit_logging_enabled"
      
    - name: "Security Event Alerting"
      required: true
      check: "security_alerting_configured"
      
    - name: "Log Retention 90 Days"
      required: true
      check: "log_retention_90_days"
  
  # === Supply Chain ===
  supply_chain:
    - name: "Dependency Vulnerability Scan"
      required: true
      check: "dependency_scan_clean"
      
    - name: "Build Environment Isolation"
      required: true
      check: "build_env_isolated"
      
    - name: "Cosign Signature"
      required: true
      check: "cosign_signature_present"
```

---

<!-- chunk: 12. Security Testing and Fuzzing -->## 12. Security Testing and Fuzzing

## 12.1 Wasm Fuzzing

```rust
// Use cargo-fuzz for Wasm parser fuzzing
// fuzz/fuzz_targets/fuzz_wasm_parser.rs

#![no_main]
use libfuzzer_sys::fuzz_target;
use wasmtime::{Config, Engine, Module};

fuzz_target!(|data: &[u8]| {
    let mut config = Config::new();
    config.wasm_component_model(true);
    
    let engine = Engine::new(&config).unwrap();
    
    // Try parsing arbitrary bytes as Wasm module
    // Runtime should safely reject invalid input, not crash
    let _ = Module::new(&engine, data);
});

// Fuzz WASI interface
fuzz_target!(|data: &[u8]| {
    use wasmtime_wasi::WasiCtxBuilder;
    
    if data.len() < 4 { return; }
    
    let engine = Engine::default();
    
    // Use fuzzer input as file path
    let path_len = (data[0] as usize % 64).min(data.len() - 1);
    let path = String::from_utf8_lossy(&data[1..=path_len]).to_string();
    
    // Test if path handling is safe
    let _ = sanitize_path("/safe/base", &path);
});

fn sanitize_path(base: &str, user_path: &str) -> Result<std::path::PathBuf, String> {
    let base = std::path::Path::new(base);
    let requested = base.join(user_path);
    
    // Prevent path traversal
    if user_path.contains("..") {
        return Err("Path traversal".to_string());
    }
    
    Ok(requested)
}
```

## 12.2 Security Scanning Integration

```bash
#!/bin/bash
# security-scan.sh - Wasm security scanning workflow

set -euo pipefail

WASM_FILE="${1:-target/wasm32-wasi/release/my_module.wasm}"
REPORT_DIR="security-reports"

mkdir -p "${REPORT_DIR}"

echo "=== Wasm Security Scan ==="
echo "File: ${WASM_FILE}"

# 1. Basic validation
echo ""
echo "Step 1: Wasm Validation"
wasm-tools validate \
  --features component-model \
  "${WASM_FILE}" \
  && echo "✅ Wasm validation passed" \
  || echo "❌ Wasm validation failed"

# 2. Dependency vulnerability scan
echo ""
echo "Step 2: Dependency Vulnerability Scan"
if command -v cargo-audit &>/dev/null; then
  cargo audit \
    --json > "${REPORT_DIR}/cargo-audit.json" 2>&1 \
    && echo "✅ No known vulnerabilities" \
    || echo "⚠️  Vulnerabilities found, check ${REPORT_DIR}/cargo-audit.json"
fi

# 3. SBOM generation
echo ""
echo "Step 3: SBOM Generation"
if command -v syft &>/dev/null; then
  syft . -o cyclonedx-json > "${REPORT_DIR}/sbom.json" 2>&1
  echo "✅ SBOM generated: ${REPORT_DIR}/sbom.json"
fi

# 4. Static analysis (check unsafe code patterns)
echo ""
echo "Step 4: Static Analysis"
if command -v cargo-geiger &>/dev/null; then
  cargo geiger \
    --output-format json \
    2>/dev/null > "${REPORT_DIR}/unsafe-code.json" \
    && echo "✅ Unsafe code analysis complete" \
    || true
fi

# 5. Wasm structure analysis
echo ""
echo "Step 5: Wasm Structure Analysis"
wasm-tools print "${WASM_FILE}" | \
  grep -E "(import|export)" > "${REPORT_DIR}/imports-exports.txt"
echo "✅ Imports/exports analyzed: ${REPORT_DIR}/imports-exports.txt"

# Output imported host functions (security review point)
echo ""
echo "=== Imported Host Functions ==="
wasm-tools print "${WASM_FILE}" | \
  grep "import" | \
  grep -v "wasi:" || echo "(none)"

# 6. Memory limit verification
echo ""
echo "Step 6: Memory Configuration Check"
MAX_MEM=$(wasm-tools print "${WASM_FILE}" | \
  grep "memory" | \
  head -1)
echo "Memory config: ${MAX_MEM}"

# 7. Size analysis
echo ""
echo "Step 7: Size Analysis"
ORIGINAL_SIZE=$(wc -c < "${WASM_FILE}")
echo "Module size: ${ORIGINAL_SIZE} bytes ($(echo "scale=1; ${ORIGINAL_SIZE}/1024/1024" | bc)MB)"

# 8. Signature verification (if exists)
echo ""
echo "Step 8: Signature Verification"
if [ -f "${WASM_FILE}.sig" ]; then
  echo "Verifying signature..."
  openssl dgst -sha256 -verify "${WASM_FILE}.pub.pem" \
    -signature "${WASM_FILE}.sig" \
    "${WASM_FILE}" \
    && echo "✅ Signature valid" \
    || echo "❌ Signature invalid"
else
  echo "⚠️  No signature file found"
fi

# Generate summary report
echo ""
echo "=== Security Scan Summary ==="
echo "Reports saved to: ${REPORT_DIR}/"
echo "  - cargo-audit.json: Dependency vulnerabilities"
echo "  - sbom.json: Software Bill of Materials"
echo "  - unsafe-code.json: Unsafe Rust code usage"
echo "  - imports-exports.txt: Module interface analysis"
```

---

<!-- chunk: 13. Production Security Best Practices -->## 13. Production Security Best Practices

## 13.1 Security Hardening Checklist

```markdown
<!-- chunk: Wasm Production Security Hardening Checklist -->## Wasm Production Security Hardening Checklist

## Build Phase
- [x] Use Rust, minimize unsafe code
- [x] Enable all clippy warnings and fix
- [x] Run cargo-audit to check for known CVEs
- [x] Generate and attach SBOM
- [x] Sign OCI images with Cosign
- [x] Verify wasm-tools validate in CI

## Runtime Configuration
- [x] Set memory upper limit (recommend: 64-256MB)
- [x] Configure Fuel or Epoch interruption (prevent DoS)
- [x] Disable wasm_threads (prevent Spectre)
- [x] Enable guard pages
- [x] Minimize WASI capabilities (grant only necessary permissions)
- [x] Configure network access whitelist
- [x] Restrict filesystem access paths

## Supply Chain Security
- [x] Verify SHA256 of all dependencies
- [x] Verify Cosign signatures before deployment
- [x] Enforce signature policies via Kyverno/OPA
- [x] Regularly update dependencies and re-scan

## Runtime Monitoring
- [x] Enable audit logging
- [x] Configure security alerts (high error rate, abnormal memory growth)
- [x] Monitor cold start time (anomalies may indicate tampering)
- [x] Set resource usage alerts

## Compliance
- [x] Audit log retention ≥ 90 days
- [x] All policy violations have alerts
- [x] Conduct regular security reviews
- [x] Maintain module inventory (version, SHA256, deployment time)
```

## 13.2 Zero-Trust Wasm Deployment

```yaml
# zero-trust-wasm-deployment.yaml
# Each Wasm instance requires independent verification

apiVersion: apps/v1
kind: Deployment
metadata:
  name: zero-trust-wasm-service
  namespace: production
spec:
  template:
    metadata:
      annotations:
        # Re-verify with each deployment
        security.k8s.io/wasm-module-hash: "sha256:e3b0c44..."
        security.k8s.io/wasm-signed-by: "cosign"
        security.k8s.io/wasm-policy: "strict"
    spec:
      # Service account with minimal permissions
      serviceAccountName: wasm-minimal-sa
      automountServiceAccountToken: false
      
      # Security context
      securityContext:
        runAsNonRoot: true
        runAsUser: 65534  # nobody
        runAsGroup: 65534
        fsGroup: 65534
        seccompProfile:
          type: RuntimeDefault  # Or custom seccomp profile
      
      containers:
        - name: wasm-service
          image: ghcr.io/my-org/wasm-service:1.0.0
          
          securityContext:
            allowPrivilegeEscalation: false
            readOnlyRootFilesystem: true
            capabilities:
              drop: ["ALL"]
          
          resources:
            requests:
              cpu: "50m"
              memory: "64Mi"
            limits:
              cpu: "500m"
              memory: "256Mi"
          
          # Read-only filesystem + temporary write directory
          volumeMounts:
            - name: tmp
              mountPath: /tmp
            - name: data
              mountPath: /data
              readOnly: true  # Data read-only
      
      volumes:
        - name: tmp
          emptyDir:
            medium: Memory
            sizeLimit: 10Mi
        - name: data
          configMap:
            name: app-data
```

---

<!-- chunk: 14. Security Incident Response -->## 14. Security Incident Response

## 14.1 Incident Response Workflow

```mermaid
graph TD
    Detect[Security Event Detected] --> Triage[Triage/Initial Assessment]
    Triage --> |P0: Critical| Immediate[Immediate Response]
    Triage --> |P1: High| Urgent[Urgent Response 2h]
    Triage --> |P2: Medium| Standard[Standard Response 24h]
    
    Immediate --> Isolate[Isolate Affected Instances]
    Immediate --> Preserve[Preserve Evidence/Logs]
    Immediate --> Notify[Notify Security Team]
    
    Isolate --> Investigate[Investigate Root Cause]
    Investigate --> Remediate[Remediation]
    Remediate --> Verify[Verify Fix]
    Verify --> PostMortem[Post-Mortem Analysis]
    PostMortem --> Improve[Improvement Measures]
```

## 14.2 Incident Response Script

> ⚠️ **🟡 Medium Risk Change** — Modifies cluster resource state, recommend --dry-run or diff to confirm first
> - `kubectl apply/create/replace`: Creates/modifies cluster resources
> - `kubectl exec`: Enters container to execute commands, may change container state

``` bash
# 🟡 Medium Risk: Modifies cluster/resource state, confirm target, impact scope, and authorization before execution
#!/bin/bash
# incident-response.sh - Wasm security incident response

INCIDENT_ID="${1:-INC-$(date +%Y%m%d-%H%M%S)}"
AFFECTED_NAMESPACE="${2:-default}"
AFFECTED_SERVICE="${3:-}"

echo "=== Security Incident Response: ${INCIDENT_ID} ==="
echo "Timestamp: $(date -u +%Y-%m-%dT%H:%M:%SZ)"
echo "Namespace: ${AFFECTED_NAMESPACE}"
echo "Service: ${AFFECTED_SERVICE}"

# 1. Save current state
echo ""
echo "Step 1: Capturing current state..."
mkdir -p "incident-${INCIDENT_ID}"

# Save Pod state
kubectl get pods -n "${AFFECTED_NAMESPACE}" -o json \
  > "incident-${INCIDENT_ID}/pods.json"

# Save Wasm Plugin configuration
kubectl get wasmplugins -A -o json \
  > "incident-${INCIDENT_ID}/wasm-plugins.json"

# Save recent logs
if [ -n "${AFFECTED_SERVICE}" ]; then
  kubectl logs \
    -n "${AFFECTED_NAMESPACE}" \
    -l "app=${AFFECTED_SERVICE}" \
    --since=1h \
    --all-containers \
    > "incident-${INCIDENT_ID}/recent-logs.txt"
fi

echo "✅ State captured"

# 2. Isolate affected Pods (as needed)
echo ""
read -p "Step 2: Isolate affected pods? (y/n): " ISOLATE
if [ "${ISOLATE}" = "y" ]; then
  # Use NetworkPolicy to isolate
  kubectl apply -f - << EOF
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: incident-isolation-${INCIDENT_ID}
  namespace: ${AFFECTED_NAMESPACE}
spec:
  podSelector:
    matchLabels:
      app: ${AFFECTED_SERVICE}
  policyTypes:
    - Ingress
    - Egress
  # Deny all traffic
EOF
  echo "✅ Network isolation applied"
fi

# 3. Collect forensic data
echo ""
echo "Step 3: Collecting forensic data..."

# Collect Wasm audit logs
kubectl exec -n "${AFFECTED_NAMESPACE}" \
  -l "app=${AFFECTED_SERVICE}" \
  -- cat /var/log/wasm-audit.log 2>/dev/null \
  > "incident-${INCIDENT_ID}/audit-log.txt" || true

# Collect Envoy/Istio logs
kubectl logs \
  -n "${AFFECTED_NAMESPACE}" \
  -l "app=${AFFECTED_SERVICE}" \
  -c istio-proxy \
  --since=2h \
  > "incident-${INCIDENT_ID}/proxy-logs.txt" 2>/dev/null || true

echo "✅ Forensic data collected"

# 4. Verify Wasm module integrity
echo ""
echo "Step 4: Verifying Wasm module integrity..."

# Get currently used image
CURRENT_IMAGE=$(kubectl get pod -n "${AFFECTED_NAMESPACE}" \
  -l "app=${AFFECTED_SERVICE}" \
  -o jsonpath='{.items[0].spec.containers[0].image}' 2>/dev/null)

if [ -n "${CURRENT_IMAGE}" ]; then
  echo "Current image: ${CURRENT_IMAGE}"
  
  # Verify Cosign signature
  COSIGN_EXPERIMENTAL=1 cosign verify \
    --certificate-identity-regexp ".*" \
    --certificate-oidc-issuer "https://token.actions.githubusercontent.com" \
    "${CURRENT_IMAGE}" \
    && echo "✅ Image signature valid" \
    || echo "❌ Image signature INVALID - possible compromise!"
fi

# 5. Generate incident report
echo ""
echo "Step 5: Generating incident report..."
cat > "incident-${INCIDENT_ID}/report.md" << EOF
# Security Incident Report: ${INCIDENT_ID}

**Date:** $(date -u +%Y-%m-%dT%H:%M:%SZ)
**Severity:** [TBD]
**Status:** In Progress
**Affected Service:** ${AFFECTED_NAMESPACE}/${AFFECTED_SERVICE}

<!-- chunk: Summary -->## Summary
[Add incident summary here]

<!-- chunk: Timeline -->## Timeline
- $(date -u +%H:%M): Incident detected
- $(date -u +%H:%M): Response initiated

<!-- chunk: Impact -->## Impact
- [Describe user impact]
- [Describe data exposure risk]

<!-- chunk: Root Cause -->## Root Cause
[To be determined]

<!-- chunk: Remediation -->## Remediation
[Steps taken/planned]

<!-- chunk: Evidence Files -->## Evidence Files
- pods.json: Pod state at incident time
- wasm-plugins.json: WasmPlugin configurations
- recent-logs.txt: Service logs (1 hour)
- audit-log.txt: Wasm audit log
- proxy-logs.txt: Istio proxy logs

<!-- chunk: Lessons Learned -->## Lessons Learned
[Post-incident analysis]
EOF

echo "✅ Incident report template created"
echo ""
echo "=== Response Complete ==="
echo "Evidence saved to: incident-${INCIDENT_ID}/"
echo "Next: Fill in incident-${INCIDENT_ID}/report.md"
```

---

<!-- chunk: Summary -->## Summary

Wasm security sandbox builds industry-leading secure execution environments through multi-layer protection:

**Security Architecture Layers**:

```
Layer 1: Wasm Specification Validation  → Type Safety, Memory Bounds Checking
Layer 2: Runtime Resource Limiting      → Fuel/Epoch, Memory Upper Bound
Layer 3: WASI Capability Control        → Zero-Permission Default, Minimal Authorization
Layer 4: Policy Enforcement Engine      → OPA/Rego Fine-Grained Control
Layer 5: Supply Chain Security          → SBOM, Signing, Verification
Layer 6: OS-Level Hardening             → seccomp, namespace, cgroup
Layer 7: Confidential Computing (Optional) → SGX/SEV/TrustZone
```

**Core Security Principles**:
1. **Least Privilege**: Grant Wasm modules only the minimal capabilities needed to complete tasks
2. **Defense in Depth**: Multiple layers of security controls; single layer failure doesn't lead to total breach
3. **Supply Chain Trust**: Verify integrity from source code to runtime throughout
4. **Continuous Monitoring**: Audit logging, anomaly detection, security alerting
5. **Rapid Response**: Pre-defined incident response workflows and automation tools

**Key Differences from Traditional Security Methods**:
- Wasm security isolation is at the **language and runtime level**, not relying solely on OS permissions
- WASI capability model implements **fine-grained resource access control**, beyond traditional process permissions
- Wasm module **verifiability** makes supply chain security more achievable

---

*References:*
- [WebAssembly Security Overview](https://webassembly.org/docs/security/)
- [WASI Security Model](https://github.com/WebAssembly/WASI/blob/main/docs/security-model.md)
- [wasmtime Security](https://docs.wasmtime.dev/security.html)
- [Bytecode Alliance Security](https://bytecodealliance.org/security)
- [OWASP WebAssembly Security](https://cheatsheetseries.owasp.org/cheatsheets/WebAssembly_Security_Cheat_Sheet.html)
- [Sigstore/Cosign](https://docs.sigstore.dev/)
- [Confidential Containers](https://confidentialcontainers.org/)

---

<!-- chunk: Obsidian Related Documentation -->## Obsidian Related Documentation

- Domain 38: WebAssembly Cloud Native - Global MOC
- [[Domain 38: WebAssembly Cloud Native]]
- Domain-38 WebAssembly Cloud Native - Open Source Project Index
- WebAssembly Cloud Native Fundamentals
- containerd Wasm Runtime
- SpinKube Framework Practice
- wasmCloud Platform
- WasmEdge Runtime
- Wasm Component Model
- Wasm Plugin System
- Wasm AI Inference
- Wasm Serverless

## See Also

- 08-wasm-ai-inference
- 09-wasm-serverless
- 99-wasmedge-cloud-native-guide
- 01-wasm-fundamentals-cloud-native

<!-- risk-assessed -->
