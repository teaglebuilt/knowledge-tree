---
title: WasmEdge Runtime
description: 'WasmEdge is a lightweight, high-performance, extensible WebAssembly runtime designed for cloud-native, edge computing, and distributed applications. As a CNCF Sandbox project, it provides comprehensive WASI support, AI inference capabilities, and seamless Kubernetes integration.'
summary: 'Covers WasmEdge architecture, WASI extensions, Kubernetes integration via containerd shim, edge deployment strategies, AI inference with ONNX/TensorFlow Lite/LLM support, network plugins, performance optimization through AOT compilation and SIMD, and production deployment patterns with monitoring and CI/CD.'
category: webassembly-cloud-native
tags:
- k8s
- wasm
- webassembly
- cloud-native
- prometheus
- containerd
- docker
- job
- operator
- gpu
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
- What is WasmEdge Runtime
- How to use WasmEdge Runtime
- Kubernetes 38 webassembly cloud native best practices
trigger_keywords:
- WasmEdge
- Runtime
- webassembly
- cloud
- native
prerequisites:
- kubectl-basics
- prometheus-basics
- gpu-scheduling-basics
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

# [[WasmEdge|WasmEdge]] WasmEdge Runtime

<!-- chunk: Table of Contents -->## Table of Contents

1. [WasmEdge Overview](#1-wasmedge-overview)
2. [Architecture and Core Components](#2-architecture-and-core-components)
3. [WASI Support and Extensions](#3-wasi-support-and-extensions)
4. [[entities/kubernetes.md|Kubernetes]] Integration](#4-kubernetes-integration)
5. [Edge Deployment](#5-edge-deployment)
6. [Network Plugins](#6-network-plugins)
7. [AI Inference Support](#7-ai-inference-support)
8. [ONNX Integration](#8-onnx-integration)
9. [TensorFlow Lite Integration](#9-tensorflow-lite-integration)
10. [LLM Inference](#10-llm-inference)
11. [Performance Optimization](#11-performance-optimization)
12. [Production Practices](#12-production-practices)

---

<!-- chunk: 1. WasmEdge Overview -->## 1. WasmEdge Overview

## 1.1 What is WasmEdge

WasmEdge is a lightweight, high-performance, extensible WebAssembly runtime designed for cloud-native, edge computing, and distributed applications. It is a CNCF Sandbox project (joined in 2021):

```
# 🟢 Low Risk: Read-only/information gathering, typically no side effects
WasmEdge Core Features

┌─────────────────────────────────────────────────────────────┐
│  High Performance                                            │
│  - AOT (Ahead-of-Time) Compilation                          │
│  - SIMD Support                                             │
│  - Near-Native Speed                                        │
├─────────────────────────────────────────────────────────────┤
│  Cloud-Native Integration                                    │
│  - containerd shim (WasmEdge-containerd)                    │
│  - Kubernetes RuntimeClass                                   │
│  - Docker Desktop Plugin                                     │
├─────────────────────────────────────────────────────────────┤
│  AI/ML Inference                                             │
│  - WASI-NN Standard Interface                               │
│  - ONNX Runtime Backend                                      │
│  - TensorFlow Lite Backend                                   │
│  - PyTorch Backend                                           │
│  - OpenVINO Backend                                          │
├─────────────────────────────────────────────────────────────┤
│  Networking Capabilities                                     │
│  - WASI-Socket Support                                       │
│  - HTTP/1.1 + HTTP/2                                        │
│  - Async Networking (Tokio-style)                           │
├─────────────────────────────────────────────────────────────┤
│  Extensibility                                               │
│  - Host Functions                                            │
│  - Plugin System                                             │
│  - Custom WASI Implementation                                │
└─────────────────────────────────────────────────────────────┘
```

## 1.2 WasmEdge vs Other Runtimes

```mermaid
graph TD
    subgraph "Wasm Runtime Comparison"
        A[Wasmtime] --> B[General Server Wasm\nSecurity-First\nBytecode Alliance]
        C[WasmEdge] --> D[Edge/AI/Cloud-Native\nHigh Performance\nCNCF Sandbox]
        E[Wasmer] --> F[General Purpose\nMulti-Backend\nCommercial-Friendly]
        G[wazero] --> H[Pure Go\nEmbed-Friendly\nZero Dependencies]
        I[V8] --> J[Browser-First\nJS Engine Integration\nMost Mature]
    end
    
    subgraph "WasmEdge Advantage Scenarios"
        K[Edge Computing] --> C
        L[AI Inference] --> C
        M[IoT Devices] --> C
        N[Function Computing FaaS] --> C
        O[Database UDF] --> C
    end
```

## 1.3 Version History and Roadmap

```
WasmEdge Version Timeline

0.8.x (2021)  - Basic WASI support, containerd integration
0.9.x (2022)  - WASI-NN initial support, networking enhancements
0.10.x (2022) - AOT optimization, SIMD support
0.11.x (2023) - WASI Preview 2 initial support, LLM inference
0.12.x (2023) - Component Model support, WasmEdge-LLMC
0.13.x (2024) - WASI 0.2 complete support, GGUF format support
0.14.x (2025) - Production-grade AI inference, multimodal support

Roadmap 2025-2026:
- Full RISC-V support
- Distributed AI inference
- WebGPU support
- Enhanced JIT optimization
```

---

<!-- chunk: 2. Architecture and Core Components -->## 2. Architecture and Core Components

## 2.1 Overall Architecture

```mermaid
graph TD
    subgraph "WasmEdge Architecture"
        subgraph "Application Layer"
            A[Rust App] 
            B[Go App]
            C[C/C++ App]
            D[Node.js App]
        end
        
        subgraph "WasmEdge C API"
            E[WasmEdge_VMCreate]
            F[WasmEdge_VMExecute]
            G[WasmEdge_VMDelete]
        end
        
        subgraph "Core Execution Engine"
            H[Interpreter]
            I[AOT Compiler]
            J[JIT Compiler]
        end
        
        subgraph "Module Layer"
            K[WASI Implementation]
            L[Host Functions API]
            M[Plugin System]
            N[WASI-NN]
        end
        
        subgraph "Backend Layer"
            O[ONNX Runtime]
            P[TensorFlow Lite]
            Q[PyTorch]
            R[OpenVINO]
            S[whisper.cpp]
            T[llama.cpp]
        end
    end
    
    A & B & C & D --> E & F & G
    E & F & G --> H & I & J
    H & I & J --> K & L & M & N
    N --> O & P & Q & R & S & T
```

## 2.2 Core C API

```c
// WasmEdge C API usage example
#include <wasmedge/wasmedge.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    // Initialize configuration
    WasmEdge_ConfigureContext *ConfCxt = WasmEdge_ConfigureCreate();
    
    // Enable WASI
    WasmEdge_ConfigureAddHostRegistration(
        ConfCxt,
        WasmEdge_HostRegistration_Wasi
    );
    
    // Enable AOT compilation (performance boost)
    WasmEdge_ConfigureSetAOTCompilerOptimizationLevel(
        ConfCxt,
        WasmEdge_CompilerOptimizationLevel_O3
    );
    
    // Create VM
    WasmEdge_VMContext *VMCxt = WasmEdge_VMCreate(ConfCxt, NULL);
    
    // Create WASI import object
    WasmEdge_ImportObjectContext *WasiObj = WasmEdge_ImportObjectCreateWASI(
        /* Command line arguments */ (const char *[]){argv[0], "--test"}, 2,
        /* Environment variables */ (const char *[]){"LOG_LEVEL=debug"}, 1,
        /* Preopened directories */ (const char *[]){"."}, 1
    );
    
    // Register WASI
    WasmEdge_VMRegisterModuleFromImport(VMCxt, WasiObj);
    
    // Load and execute Wasm module
    WasmEdge_String ModName = WasmEdge_StringCreateByCString("app");
    WasmEdge_Result Res = WasmEdge_VMRunWasmFromFile(
        VMCxt,
        "app.wasm",
        WasmEdge_StringCreateByCString("_start"),
        NULL, 0,  // Parameters
        NULL, 0   // Return values
    );
    
    if (!WasmEdge_ResultOK(Res)) {
        printf("Execution failed: %s\n", WasmEdge_ResultGetMessage(Res));
    }
    
    // Cleanup
    WasmEdge_ImportObjectDelete(WasiObj);
    WasmEdge_VMDelete(VMCxt);
    WasmEdge_ConfigureDelete(ConfCxt);
    
    return 0;
}
```

## 2.3 Rust Bindings

```rust
// Cargo.toml
[dependencies]
wasmedge-sdk = "0.14"

[features]
default = ["aot"]
aot = ["wasmedge-sdk/aot"]
```

```rust
// WasmEdge Rust SDK usage example
use wasmedge_sdk::{
    config::{CommonConfigOptions, ConfigBuilder, HostRegistrationConfigOptions},
    params, Vm, WasmVal,
};
use std::collections::HashMap;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    // Configure WasmEdge VM
    let config = ConfigBuilder::new(CommonConfigOptions::default())
        .with_host_registration_config(
            HostRegistrationConfigOptions::default().wasi(true)
        )
        .build()?;
    
    // Create VM
    let vm = Vm::new(Some(config))?;
    
    // Configure WASI
    let mut wasi_module = vm.wasi_module_mut()?;
    wasi_module.initialize(
        Some(vec!["app", "--verbose"]),   // Command line arguments
        Some(vec![("LOG_LEVEL", "info")]), // Environment variables
        Some(vec![(".", ".")]),            // Preopened directories: (host path, guest path)
    );
    
    // Load Wasm module from file
    let vm = vm.register_module_from_file("app", "app.wasm")?;
    
    // Call exported function
    let result = vm.run_func(
        Some("app"),  // Module name
        "add",        // Function name
        params!(42i32, 58i32),  // Parameters
    )?;
    
    println!("Result: {:?}", result);
    
    Ok(())
}
```

## 2.4 Go Bindings

```go
// go.mod
// require github.com/second-state/WasmEdge-go v0.14.0

package main

import (
    "fmt"
    "os"
    
    wasmedge "github.com/second-state/WasmEdge-go/wasmedge"
)

func main() {
    // Initialize configuration
    conf := wasmedge.NewConfigure(wasmedge.WASI)
    defer conf.Release()
    
    // Create VM
    vm := wasmedge.NewVMWithConfig(conf)
    defer vm.Release()
    
    // Configure WASI
    var wasi = vm.GetImportModule(wasmedge.WASI)
    wasi.InitWasi(
        os.Args[1:],                        // Command line arguments
        os.Environ(),                       // Environment variables
        []string{".:."})                    // Directory mapping
    
    // Load and validate Wasm module
    err := vm.LoadWasmFile("app.wasm")
    if err != nil {
        fmt.Printf("Load failed: %v\n", err)
        return
    }
    
    err = vm.Validate()
    if err != nil {
        fmt.Printf("Validation failed: %v\n", err)
        return
    }
    
    // Instantiate
    err = vm.Instantiate()
    if err != nil {
        fmt.Printf("Instantiation failed: %v\n", err)
        return
    }
    
    // Call function
    result, err := vm.Execute("fibonacci", int32(30))
    if err != nil {
        fmt.Printf("Execution failed: %v\n", err)
        return
    }
    
    fmt.Printf("fibonacci(30) = %v\n", result[0])
    
    // Register host function
    mod := wasmedge.NewModule("host")
    defer mod.Release()
    
    // Register logging function
    logFunc := wasmedge.NewFunction(
        wasmedge.NewFunctionType(
            []wasmedge.ValType{wasmedge.ValType_I32, wasmedge.ValType_I32}, // ptr, len
            []wasmedge.ValType{},
        ),
        func(callFrame *wasmedge.CallingFrame, params []interface{}) ([]interface{}, wasmedge.Result) {
            ptr := params[0].(int32)
            length := params[1].(int32)
            
            // Read string from Wasm memory
            mem := callFrame.GetMemoryByIndex(0)
            data, _ := mem.GetData(uint(ptr), uint(length))
            fmt.Printf("[Wasm Log] %s\n", string(data))
            
            return nil, wasmedge.Result_Success
        },
        nil,
    )
    mod.AddFunction("log", logFunc)
    
    vm.RegisterModule(mod)
}
```

---

<!-- chunk: 3. WASI Support and Extensions -->## 3. WASI Support and Extensions

## 3.1 WASI Implementation Overview

```mermaid
graph LR
    subgraph "WasmEdge WASI Support"
        A[wasi_snapshot_preview1] --> B[Filesystem]
        A --> C[Random]
        A --> D[Clock/Time]
        A --> E[Environment Variables]
        A --> F[Arguments]
        A --> G[Process Exit]
        A --> H[Socket]
        
        I[wasi:http@0.2.0] --> J[HTTP Client]
        I --> K[HTTP Server]
        
        L[wasi:nn@0.1.0] --> M[Neural Network Inference]
        
        N[wasi:crypto@0.2.1] --> O[Crypto Operations]
        N --> P[Hash]
        N --> Q[HMAC]
        N --> R[Signatures]
    end
```

## 3.2 WASI Socket Extension

```rust
// WasmEdge async networking - HTTP server
use wasmedge_http_req::request;
use std::io::Write;

fn main() {
    // Make HTTP request (WasmEdge network extension)
    let uri = "https://httpbin.org/json".parse().unwrap();
    
    let mut body = Vec::new();
    let res = request::get(uri, &mut body).unwrap();
    
    println!("Status: {}", res.status_code());
    println!("Response: {}", String::from_utf8_lossy(&body));
}
```

```rust
// WasmEdge async HTTP server (using tokio)
use hyper::service::{make_service_fn, service_fn};
use hyper::{Body, Request, Response, Server};
use std::convert::Infallible;
use std::net::SocketAddr;

async fn handle_request(req: Request<Body>) -> Result<Response<Body>, Infallible> {
    let path = req.uri().path().to_string();
    
    match path.as_str() {
        "/health" => Ok(Response::builder()
            .status(200)
            .body(Body::from(r#"{"status":"healthy"}"#))
            .unwrap()),
        "/echo" => {
            let body_bytes = hyper::body::to_bytes(req.into_body()).await.unwrap();
            Ok(Response::new(Body::from(body_bytes)))
        }
        _ => Ok(Response::builder()
            .status(404)
            .body(Body::from("Not Found"))
            .unwrap()),
    }
}

#[tokio::main(flavor = "current_thread")]
async fn main() {
    let addr = SocketAddr::from(([0, 0, 0, 0], 8080));
    
    let make_svc = make_service_fn(|_| async {
        Ok::<_, Infallible>(service_fn(handle_request))
    });
    
    let server = Server::bind(&addr).serve(make_svc);
    
    println!("WasmEdge HTTP server listening on: {}", addr);
    
    if let Err(e) = server.await {
        eprintln!("Server error: {}", e);
    }
}
```

## 3.3 WASI Crypto Extension

```rust
// WasmEdge WASI-Crypto usage example
use wasi_crypto::*;

fn sign_and_verify(message: &[u8]) -> Result<(), String> {
    // Generate Ed25519 keypair
    let key_pair = keypair_generate(
        AlgorithmType::Signatures,
        "Ed25519",
        None,
    ).map_err(|e| format!("Keypair generation failed: {:?}", e))?;
    
    // Sign
    let sig_state = signature_state_open(key_pair)
        .map_err(|e| format!("Open signature state failed: {:?}", e))?;
    
    signature_state_update(sig_state, message)
        .map_err(|e| format!("Update signature failed: {:?}", e))?;
    
    let signature = signature_state_sign(sig_state)
        .map_err(|e| format!("Sign failed: {:?}", e))?;
    
    // Get public key
    let public_key = keypair_publickey(key_pair)
        .map_err(|e| format!("Get public key failed: {:?}", e))?;
    
    // Verify
    let verification_state = signature_verification_state_open(public_key)
        .map_err(|e| format!("Open verification state failed: {:?}", e))?;
    
    signature_verification_state_update(verification_state, message)
        .map_err(|e| format!("Update verification state failed: {:?}", e))?;
    
    signature_verification_state_verify(verification_state, signature)
        .map_err(|e| format!("Verification failed: {:?}", e))?;
    
    println!("Signature verification successful!");
    
    // Cleanup
    signatures_close(signature).ok();
    publickey_close(public_key).ok();
    keypair_close(key_pair).ok();
    
    Ok(())
}

fn hash_data(data: &[u8]) -> Vec<u8> {
    // SHA-256 hash
    let state = hash_open("SHA-256")
        .expect("Open hash state failed");
    
    hash_update(state, data)
        .expect("Update hash failed");
    
    let digest = hash_digest(state)
        .expect("Get digest failed");
    
    let mut result = vec![0u8; 32];
    array_output_pull(digest, &mut result)
        .expect("Get output failed");
    
    result
}
```

---

<!-- chunk: 4. Kubernetes Integration -->## 4. Kubernetes Integration

## 4.1 WasmEdge containerd shim

```bash
# Install WasmEdge containerd shim
# Method 1: Using official installation script

WASMEDGE_VERSION="0.14.0"
CONTAINERD_WASM_VERSION="0.5.0"

# Install WasmEdge runtime
curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | \
  bash -s -- \
  --version="${WASMEDGE_VERSION}" \
  --tf-version="${WASMEDGE_VERSION}" \  # TensorFlow plugin
  --image-classification-extension      # Image classification extension

# Set environment variables
export LD_LIBRARY_PATH="/root/.wasmedge/lib:$LD_LIBRARY_PATH"

# Install containerd-shim-wasmedge
wget "https://github.com/containerd/runwasi/releases/download/v${CONTAINERD_WASM_VERSION}/containerd-shim-wasmedge-$(uname -m).tar.gz"
tar -xzf "containerd-shim-wasmedge-$(uname -m).tar.gz"
sudo install -m 755 containerd-shim-wasmedge-v1 /usr/local/bin/

# Verify installation
/usr/local/bin/containerd-shim-wasmedge-v1 --version
wasmedge --version
```

```toml
# /etc/containerd/config.toml - Add WasmEdge runtime
version = 2

[plugins."io.containerd.grpc.v1.cri".containerd.runtimes]
  # Standard runc
  [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.runc]
    runtime_type = "io.containerd.runc.v2"
  
  # WasmEdge runtime
  [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.wasmedge]
    runtime_type = "io.containerd.wasmedge.v1"
    runtime_path = "/usr/local/bin/containerd-shim-wasmedge-v1"
    
  # WasmEdge AI runtime (with AI plugins)
  [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.wasmedge-ai]
    runtime_type = "io.containerd.wasmedge.v1"
    runtime_path = "/usr/local/bin/containerd-shim-wasmedge-v1"
    [plugins."io.containerd.grpc.v1.cri".containerd.runtimes.wasmedge-ai.options]
      # Enable WASI-NN plugin
      WasmEdgePluginDir = "/root/.wasmedge/plugin"
```

## 4.2 RuntimeClass Configuration

```yaml
# WasmEdge RuntimeClass
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: wasmedge
handler: wasmedge
scheduling:
  nodeClassification:
    tolerations:
    - key: "wasmedge.io/enabled"
      operator: "Exists"
      effect: "NoSchedule"
    nodeSelector:
      matchLabels:
        wasmedge.io/enabled: "true"
overhead:
  podFixed:
    memory: "8Mi"
    cpu: "10m"

---
# WasmEdge AI RuntimeClass (with GPU acceleration)
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: wasmedge-ai
handler: wasmedge-ai
scheduling:
  nodeClassification:
    tolerations:
    - key: "wasmedge.io/ai"
      operator: "Exists"
      effect: "NoSchedule"
    nodeSelector:
      matchLabels:
        wasmedge.io/ai: "true"
        hardware.accelerator/type: gpu
overhead:
  podFixed:
    memory: "256Mi"
    cpu: "500m"
```

## 4.3 Kubernetes Deployment Example

```yaml
# WasmEdge HTTP Service Deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wasmedge-http-service
  namespace: production
  labels:
    app: wasmedge-http
    runtime: wasmedge
spec:
  replicas: 5
  selector:
    matchLabels:
      app: wasmedge-http
  template:
    metadata:
      labels:
        app: wasmedge-http
      annotations:
        module.wasm.image/variant: compat-smart
    spec:
      runtimeClassName: wasmedge
      
      containers:
      - name: http-service
        image: ghcr.io/myorg/wasmedge-http:latest
        ports:
        - containerPort: 8080
          name: http
        env:
        - name: WASMEDGE_PLUGIN_PATH
          value: "/root/.wasmedge/plugin"
        - name: LISTEN_ADDR
          value: "0.0.0.0:8080"
        resources:
          requests:
            memory: "16Mi"
            cpu: "50m"
          limits:
            memory: "64Mi"
            cpu: "200m"
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 2
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 1
          periodSeconds: 5
      
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: wasmedge.io/enabled
                operator: Exists

---
# WasmEdge AI Inference Service
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wasmedge-ai-inference
  namespace: production
spec:
  replicas: 2
  selector:
    matchLabels:
      app: wasmedge-ai
  template:
    metadata:
      labels:
        app: wasmedge-ai
    spec:
      runtimeClassName: wasmedge-ai
      
      containers:
      - name: ai-service
        image: ghcr.io/myorg/wasmedge-image-classifier:latest
        ports:
        - containerPort: 8090
        env:
        - name: MODEL_PATH
          value: "/models/mobilenet_v2.onnx"
        - name: WASI_NN_BACKEND
          value: "ONNX"
        resources:
          requests:
            memory: "512Mi"
            cpu: "500m"
          limits:
            memory: "2Gi"
            cpu: "2"
            # GPU resources (if available)
            # nvidia.com/gpu: "1"
        
        volumeMounts:
        - name: models
          mountPath: /models
          readOnly: true
      
      volumes:
      - name: models
        persistentVolumeClaim:
          claimName: ai-models-pvc
      
      nodeSelector:
        wasmedge.io/ai: "true"
```

---

<!-- chunk: 5. Edge Deployment -->## 5. Edge Deployment

## 5.1 Edge Architecture

```mermaid
graph TD
    subgraph "Cloud"
        A[Central K8s Cluster]
        B[Model Registry]
        C[Configuration Management]
    end
    
    subgraph "Edge Gateway"
        D[K3s / MicroK8s]
        E[WasmEdge Runtime]
        F[Edge AI Actor]
        G[Data Collector]
    end
    
    subgraph "Edge Devices"
        H[IoT Device 1]
        I[IoT Device 2]
        J[Camera]
    end
    
    A --> D
    B --> D
    C --> D
    D --> E
    E --> F
    E --> G
    H & I & J --> G
    F --> G
    G --> A
```

## 5.2 Edge Node Installation

```bash
# Install WasmEdge on ARM64 edge device

# Method 1: Using official installation script (ARM64)
curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | \
  bash -s -- \
  --platform=manylinux2014_aarch64 \
  --version=0.14.0

# Method 2: Manual download
ARCH="aarch64"
VERSION="0.14.0"

wget "https://github.com/WasmEdge/WasmEdge/releases/download/${VERSION}/WasmEdge-${VERSION}-manylinux2014_${ARCH}.tar.gz"
tar -xzf "WasmEdge-${VERSION}-manylinux2014_${ARCH}.tar.gz"
sudo cp -r WasmEdge-${VERSION}-Linux/* /usr/local/

# Install WASI-NN plugin (for edge AI)
wget "https://github.com/WasmEdge/WasmEdge/releases/download/${VERSION}/WasmEdge-plugin-wasi_nn-ggml-${VERSION}-manylinux2014_${ARCH}.tar.gz"
tar -xzf "WasmEdge-plugin-wasi_nn-ggml-${VERSION}-manylinux2014_${ARCH}.tar.gz"
sudo mkdir -p /usr/local/lib/wasmedge/
sudo cp libwasmedgePluginWasiNN.so /usr/local/lib/wasmedge/

# Verify
wasmedge --version
wasmedge --dir .:. hello.wasm

# Install K3s (lightweight Kubernetes)
curl -sfL https://get.k3s.io | \
  INSTALL_K3S_EXEC="--container-runtime-endpoint /run/containerd/containerd.sock" \
  sh -
```

## 5.3 Edge Wasm Application Example

```rust
// Edge sensor data processing Wasm application
use serde::{Deserialize, Serialize};
use std::collections::VecDeque;

#[derive(Debug, Deserialize, Serialize, Clone)]
struct SensorReading {
    sensor_id: String,
    timestamp: u64,
    temperature: f32,
    humidity: f32,
    pressure: f32,
    vibration: f32,
}

#[derive(Debug, Serialize)]
struct ProcessedData {
    sensor_id: String,
    window_avg_temp: f32,
    window_avg_humidity: f32,
    anomaly_detected: bool,
    anomaly_type: Option<String>,
    alert_level: AlertLevel,
}

#[derive(Debug, Serialize)]
enum AlertLevel {
    Normal,
    Warning,
    Critical,
}

struct SensorProcessor {
    window_size: usize,
    readings: VecDeque<SensorReading>,
    
    // Threshold configuration
    temp_max: f32,
    temp_min: f32,
    humidity_max: f32,
    vibration_max: f32,
}

impl SensorProcessor {
    fn new(window_size: usize) -> Self {
        Self {
            window_size,
            readings: VecDeque::new(),
            temp_max: 85.0,
            temp_min: -20.0,
            humidity_max: 95.0,
            vibration_max: 10.0,
        }
    }
    
    fn process(&mut self, reading: SensorReading) -> ProcessedData {
        // Update sliding window
        self.readings.push_back(reading.clone());
        if self.readings.len() > self.window_size {
            self.readings.pop_front();
        }
        
        // Calculate window statistics
        let avg_temp = self.readings.iter()
            .map(|r| r.temperature)
            .sum::<f32>() / self.readings.len() as f32;
        
        let avg_humidity = self.readings.iter()
            .map(|r| r.humidity)
            .sum::<f32>() / self.readings.len() as f32;
        
        // Anomaly detection
        let mut anomaly = false;
        let mut anomaly_type = None;
        let mut alert_level = AlertLevel::Normal;
        
        if reading.temperature > self.temp_max {
            anomaly = true;
            anomaly_type = Some(format!("High temperature: {}°C", reading.temperature));
            alert_level = AlertLevel::Critical;
        } else if reading.temperature < self.temp_min {
            anomaly = true;
            anomaly_type = Some(format!("Low temperature: {}°C", reading.temperature));
            alert_level = AlertLevel::Warning;
        }
        
        if reading.humidity > self.humidity_max {
            anomaly = true;
            anomaly_type = Some(format!("High humidity: {}%", reading.humidity));
            alert_level = AlertLevel::Warning;
        }
        
        if reading.vibration > self.vibration_max {
            anomaly = true;
            anomaly_type = Some(format!("Excessive vibration: {}g", reading.vibration));
            alert_level = AlertLevel::Critical;
        }
        
        // Z-score anomaly detection
        let temp_std = self.calc_std_dev(
            self.readings.iter().map(|r| r.temperature).collect()
        );
        let z_score = (reading.temperature - avg_temp).abs() / (temp_std + 0.001);
        if z_score > 3.0 {
            anomaly = true;
            anomaly_type = Some(format!("Statistical anomaly (Z={:.2}): {}°C", z_score, reading.temperature));
            if matches!(alert_level, AlertLevel::Normal) {
                alert_level = AlertLevel::Warning;
            }
        }
        
        ProcessedData {
            sensor_id: reading.sensor_id,
            window_avg_temp: avg_temp,
            window_avg_humidity: avg_humidity,
            anomaly_detected: anomaly,
            anomaly_type,
            alert_level,
        }
    }
    
    fn calc_std_dev(&self, values: Vec<f32>) -> f32 {
        if values.is_empty() {
            return 0.0;
        }
        let mean = values.iter().sum::<f32>() / values.len() as f32;
        let variance = values.iter()
            .map(|v| (v - mean).powi(2))
            .sum::<f32>() / values.len() as f32;
        variance.sqrt()
    }
}

fn main() {
    let mut processor = SensorProcessor::new(100);  // 100-reading sliding window
    
    // Simulate sensor data processing
    let readings = vec![
        SensorReading {
            sensor_id: "sensor-001".to_string(),
            timestamp: 1000,
            temperature: 72.5,
            humidity: 45.0,
            pressure: 1013.0,
            vibration: 0.5,
        },
        SensorReading {
            sensor_id: "sensor-001".to_string(),
            timestamp: 1001,
            temperature: 95.0,  // Temperature anomaly
            humidity: 45.0,
            pressure: 1013.0,
            vibration: 0.5,
        },
    ];
    
    for reading in readings {
        let result = processor.process(reading);
        let json = serde_json::to_string_pretty(&result).unwrap();
        println!("{}", json);
        
        // If critical anomaly detected, report to cloud (via WASI network)
        if matches!(result.alert_level, AlertLevel::Critical) {
            eprintln!("⚠️  Critical alert: {:?}", result.anomaly_type);
        }
    }
}
```

---

<!-- chunk: 6. Network Plugins -->## 6. Network Plugins

## 6.1 WasmEdge Networking Capabilities

```
WasmEdge Network Plugin Layers

┌──────────────────────────────────────────────────────┐
│  Application Layer                                    │
│  Rust hyper / reqwest                                 │
│  Go net/http                                          │
├──────────────────────────────────────────────────────┤
│  Async Runtime Layer                                  │
│  tokio-wasmedge / async-std-wasmedge                  │
├──────────────────────────────────────────────────────┤
│  WASI Socket Layer                                    │
│  WASI Preview 2: wasi:sockets                        │
│  WasmEdge Extension: wasmedge_wasi_socket             │
├──────────────────────────────────────────────────────┤
│  OS Layer                                             │
│  TCP/UDP Socket                                       │
│  TLS (via native-tls/rustls)                         │
└──────────────────────────────────────────────────────┘
```

## 6.2 Async HTTP Server

```rust
// Build high-performance HTTP server using WasmEdge async runtime
use hyper::{Body, Request, Response, Server};
use hyper::service::{make_service_fn, service_fn};
use std::convert::Infallible;
use std::net::SocketAddr;
use std::sync::Arc;
use tokio::sync::RwLock;
use serde::{Deserialize, Serialize};

#[derive(Clone)]
struct AppState {
    request_count: Arc<RwLock<u64>>,
    cache: Arc<RwLock<std::collections::HashMap<String, String>>>,
}

async fn handle(
    state: AppState,
    req: Request<Body>,
) -> Result<Response<Body>, Infallible> {
    // Update request count
    {
        let mut count = state.request_count.write().await;
        *count += 1;
    }
    
    let path = req.uri().path();
    let method = req.method();
    
    let response = match (method, path) {
        (&hyper::Method::GET, "/") => {
            let count = state.request_count.read().await;
            Response::new(Body::from(format!(
                "WasmEdge HTTP Server\nTotal Requests: {}",
                *count
            )))
        }
        
        (&hyper::Method::GET, "/cache") => {
            let key = req.uri().query()
                .and_then(|q| q.split('=').nth(1))
                .unwrap_or("");
            
            let cache = state.cache.read().await;
            match cache.get(key) {
                Some(val) => Response::new(Body::from(val.clone())),
                None => Response::builder()
                    .status(404)
                    .body(Body::from("Cache miss"))
                    .unwrap(),
            }
        }
        
        (&hyper::Method::POST, "/cache") => {
            let body = hyper::body::to_bytes(req.into_body()).await.unwrap();
            
            #[derive(Deserialize)]
            struct CacheEntry {
                key: String,
                value: String,
            }
            
            if let Ok(entry) = serde_json::from_slice::<CacheEntry>(&body) {
                let mut cache = state.cache.write().await;
                cache.insert(entry.key.clone(), entry.value);
                
                Response::builder()
                    .status(201)
                    .body(Body::from(format!("Cached: {}", entry.key)))
                    .unwrap()
            } else {
                Response::builder()
                    .status(400)
                    .body(Body::from("Invalid request body"))
                    .unwrap()
            }
        }
        
        (&hyper::Method::GET, "/metrics") => {
            let count = state.request_count.read().await;
            let cache = state.cache.read().await;
            
            let metrics = format!(
                "# HELP requests_total Total requests\n\
                 # TYPE requests_total counter\n\
                 requests_total {}\n\
                 # HELP cache_entries Cache entries\n\
                 # TYPE cache_entries gauge\n\
                 cache_entries {}\n",
                *count,
                cache.len()
            );
            
            Response::builder()
                .header("Content-Type", "text/plain; version=0.0.4")
                .body(Body::from(metrics))
                .unwrap()
        }
        
        _ => Response::builder()
            .status(404)
            .body(Body::from("Not Found"))
            .unwrap(),
    };
    
    Ok(response)
}

#[tokio::main(flavor = "current_thread")]
async fn main() {
    let addr: SocketAddr = ([0, 0, 0, 0], 8080).into();
    
    let state = AppState {
        request_count: Arc::new(RwLock::new(0)),
        cache: Arc::new(RwLock::new(std::collections::HashMap::new())),
    };
    
    let make_svc = make_service_fn(move |_conn| {
        let state = state.clone();
        async move {
            Ok::<_, Infallible>(service_fn(move |req| {
                handle(state.clone(), req)
            }))
        }
    });
    
    let server = Server::bind(&addr).serve(make_svc);
    
    println!("WasmEdge async HTTP server running on: http://{}", addr);
    
    server.await.expect("Server error");
}
```

---

<!-- chunk: 7. AI Inference Support -->## 7. AI Inference Support

## 7.1 WASI-NN Standard

```mermaid
graph TD
    subgraph "WASI-NN Architecture"
        A[Wasm Application] --> B[WASI-NN API]
        B --> C{Backend Selection}
        
        C --> D[ONNX Runtime]
        C --> E[TensorFlow Lite]
        C --> F[PyTorch]
        C --> G[OpenVINO]
        C --> H[ggml/llama.cpp]
        C --> I[Whisper.cpp]
        
        D --> J[CPU/GPU]
        E --> K[CPU/Edge NPU]
        F --> L[CUDA/CPU]
        G --> M[Intel OpenVINO]
        H --> N[LLM Inference]
        I --> O[Speech Recognition]
    end
```

```
WASI-NN Core API

// Load model
load: func(
    builder: list<graph-builder-array>,
    encoding: graph-encoding,
    target: execution-target
) -> result<graph, error>

// Initialize execution context
init-execution-context: func(graph: graph) -> result<graph-execution-context, error>

// Set input
set-input: func(
    ctx: graph-execution-context,
    index: u32,
    tensor: tensor
) -> result<_, error>

// Execute inference
compute: func(ctx: graph-execution-context) -> result<_, error>

// Get output
get-output: func(
    ctx: graph-execution-context,
    index: u32
) -> result<tensor, error>
```

## 7.2 Complete Image Classification Example

```rust
// Image classification using WasmEdge WASI-NN
use wasi_nn::{
    ExecutionTarget, Graph, GraphEncoding, GraphExecutionContext, 
    TensorType,
};
use std::fs;
use std::io::Read;
use serde_json;

struct ImageClassifier {
    graph: Graph,
    labels: Vec<String>,
}

impl ImageClassifier {
    fn new(model_path: &str, labels_path: &str) -> Result<Self, String> {
        // Load model weights
        let model_weights = fs::read(model_path)
            .map_err(|e| format!("Failed to read model: {}", e))?;
        
        // Load model into WASI-NN
        let graph = unsafe {
            wasi_nn::load(
                &[&model_weights],
                GraphEncoding::Onnx,
                ExecutionTarget::CPU,
            )
        }.map_err(|e| format!("Failed to load graph: {:?}", e))?;
        
        // Load class labels
        let labels_content = fs::read_to_string(labels_path)
            .map_err(|e| format!("Failed to read labels: {}", e))?;
        
        let labels: Vec<String> = labels_content
            .lines()
            .map(|s| s.to_string())
            .collect();
        
        Ok(Self { graph, labels })
    }
    
    fn preprocess_image(&self, image_data: &[u8], width: u32, height: u32) -> Vec<f32> {
        // Convert image data to model input format
        // Assumed input format: [batch, channels, height, width] = [1, 3, H, W]
        // Normalize pixel values to [0, 1], then standardize
        
        let mean = [0.485f32, 0.456, 0.406];  // ImageNet mean
        let std = [0.229f32, 0.224, 0.225];    // ImageNet std
        
        let size = (width * height) as usize;
        let mut tensor = vec![0f32; 3 * size];
        
        for i in 0..size {
            let r = image_data[i * 4] as f32 / 255.0;
            let g = image_data[i * 4 + 1] as f32 / 255.0;
            let b = image_data[i * 4 + 2] as f32 / 255.0;
            
            tensor[i] = (r - mean[0]) / std[0];
            tensor[size + i] = (g - mean[1]) / std[1];
            tensor[2 * size + i] = (b - mean[2]) / std[2];
        }
        
        tensor
    }
    
    fn classify(&self, image_data: &[u8], width: u32, height: u32) 
        -> Result<Vec<(String, f32)>, String> 
    {
        // Create execution context
        let ctx = unsafe {
            wasi_nn::init_execution_context(self.graph)
        }.map_err(|e| format!("Failed to initialize context: {:?}", e))?;
        
        // Preprocess image
        let input = self.preprocess_image(image_data, width, height);
        
        // Set input tensor
        unsafe {
            wasi_nn::set_input(
                ctx,
                0,
                wasi_nn::Tensor {
                    dimensions: &[1, 3, height, width],
                    r#type: TensorType::F32,
                    data: bytemuck::cast_slice(&input),
                },
            )
        }.map_err(|e| format!("Failed to set input: {:?}", e))?;
        
        // Execute inference
        unsafe {
            wasi_nn::compute(ctx)
        }.map_err(|e| format!("Inference failed: {:?}", e))?;
        
        // Get output
        let mut output = vec![0f32; 1000];  // ImageNet 1000 classes
        unsafe {
            wasi_nn::get_output(
                ctx,
                0,
                &mut output as *mut _ as *mut u8,
                (output.len() * 4) as u32,
            )
        }.map_err(|e| format!("Failed to get output: {:?}", e))?;
        
        // Softmax
        let max = output.iter().cloned().fold(f32::NEG_INFINITY, f32::max);
        let exp: Vec<f32> = output.iter().map(|&x| (x - max).exp()).collect();
        let sum: f32 = exp.iter().sum();
        let probs: Vec<f32> = exp.iter().map(|&x| x / sum).collect();
        
        // Get Top-5 results
        let mut indexed_probs: Vec<(usize, f32)> = probs.iter()
            .enumerate()
            .map(|(i, &p)| (i, p))
            .collect();
        
        indexed_probs.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
        
        let results: Vec<(String, f32)> = indexed_probs[..5]
            .iter()
            .map(|(idx, prob)| {
                let label = self.labels.get(*idx)
                    .cloned()
                    .unwrap_or_else(|| format!("class_{}", idx));
                (label, *prob)
            })
            .collect();
        
        Ok(results)
    }
}

fn main() {
    // Initialize classifier
    let classifier = ImageClassifier::new(
        "/models/mobilenet_v2.onnx",
        "/models/imagenet_labels.txt",
    ).expect("Failed to initialize classifier");
    
    // Process HTTP requests
    use hyper::{Body, Request, Response, Server};
    // ... HTTP server code
    println!("Image classification service started");
}
```

---

<!-- chunk: 8. ONNX Integration -->## 8. ONNX Integration

## 8.1 ONNX Model Preparation

```python
# Python: Export PyTorch model to ONNX
import torch
import torchvision.models as models
import torch.onnx

# Load pre-trained model
model = models.resnet50(pretrained=True)
model.eval()

# Example input
dummy_input = torch.randn(1, 3, 224, 224)

# Export to ONNX
torch.onnx.export(
    model,
    dummy_input,
    "resnet50.onnx",
    export_params=True,
    opset_version=17,
    input_names=['input'],
    output_names=['output'],
    dynamic_axes={
        'input': {0: 'batch_size'},
        'output': {0: 'batch_size'}
    }
)

print("Model exported to resnet50.onnx")

# Verify ONNX model
import onnx
model_onnx = onnx.load("resnet50.onnx")
onnx.checker.check_model(model_onnx)
print("ONNX model validation passed")
```

```bash
# Optimize ONNX model (reduce size, improve performance)
pip install onnxoptimizer onnxruntime

python3 << 'EOF'
import onnxoptimizer
import onnx

# Load
model = onnx.load("resnet50.onnx")

# Optimize
passes = [
    "eliminate_identity",
    "eliminate_nop_dropout",
    "fuse_add_bias_into_conv",
    "fuse_bn_into_conv",
    "fuse_consecutive_squeezes",
    "fuse_consecutive_transposes",
    "fuse_matmul_add_bias_into_gemm",
    "fuse_pad_into_conv",
    "fuse_transpose_into_gemm",
]

optimized_model = onnxoptimizer.optimize(model, passes)
onnx.save(optimized_model, "resnet50_optimized.onnx")
print("Optimized model size:", 
      sum(1 for _ in optimized_model.graph.node), "operator nodes")
EOF
```

## 8.2 Rust ONNX Inference

```rust
// Rust ONNX inference (using WasmEdge WASI-NN ONNX backend)
use wasi_nn::{ExecutionTarget, GraphEncoding, TensorType};
use std::fs;

const MODEL_PATH: &str = "/models/resnet50_optimized.onnx";
const INPUT_SIZE: usize = 1 * 3 * 224 * 224;  // batch * channels * H * W
const OUTPUT_SIZE: usize = 1000;  // ImageNet classes

fn run_onnx_inference(input_data: &[f32]) -> Result<Vec<f32>, String> {
    // Read model
    let model = fs::read(MODEL_PATH)
        .map_err(|e| format!("Failed to read model: {}", e))?;
    
    // Load graph
    let graph = unsafe {
        wasi_nn::load(
            &[model.as_slice()],
            GraphEncoding::Onnx,
            ExecutionTarget::CPU,
        )
    }.map_err(|e| format!("Failed to load graph: {:?}", e))?;
    
    // Initialize execution context
    let ctx = unsafe {
        wasi_nn::init_execution_context(graph)
    }.map_err(|e| format!("Initialization failed: {:?}", e))?;
    
    // Set input
    let input_bytes: &[u8] = bytemuck::cast_slice(input_data);
    unsafe {
        wasi_nn::set_input(
            ctx,
            0,
            wasi_nn::Tensor {
                dimensions: &[1u32, 3, 224, 224],
                r#type: TensorType::F32,
                data: input_bytes,
            },
        )
    }.map_err(|e| format!("Failed to set input: {:?}", e))?;
    
    // Inference
    unsafe {
        wasi_nn::compute(ctx)
    }.map_err(|e| format!("Inference failed: {:?}", e))?;
    
    // Get output
    let mut output = vec![0f32; OUTPUT_SIZE];
    unsafe {
        wasi_nn::get_output(
            ctx,
            0,
            output.as_mut_ptr() as *mut u8,
            (OUTPUT_SIZE * 4) as u32,
        )
    }.map_err(|e| format!("Failed to get output: {:?}", e))?;
    
    Ok(output)
}

// Batch inference
fn batch_inference(images: Vec<Vec<f32>>) -> Vec<Vec<f32>> {
    images.iter()
        .map(|img| {
            run_onnx_inference(img)
                .unwrap_or_else(|e| {
                    eprintln!("Inference failed: {}", e);
                    vec![0.0f32; OUTPUT_SIZE]
                })
        })
        .collect()
}
```

---

<!-- chunk: 9. TensorFlow Lite Integration -->## 9. TensorFlow Lite Integration

## 9.1 TFLite Model Inference

```rust
// TensorFlow Lite inference (WasmEdge TFLite backend)
use wasi_nn::{ExecutionTarget, GraphEncoding, TensorType};
use std::fs;

struct TFLiteClassifier {
    graph: wasi_nn::Graph,
    input_width: u32,
    input_height: u32,
    num_classes: usize,
}

impl TFLiteClassifier {
    fn new(model_path: &str, width: u32, height: u32, classes: usize) 
        -> Result<Self, String> 
    {
        let model_bytes = fs::read(model_path)
            .map_err(|e| format!("Failed to read TFLite model: {}", e))?;
        
        // Load TensorFlow Lite model
        let graph = unsafe {
            wasi_nn::load(
                &[model_bytes.as_slice()],
                GraphEncoding::TfLite,  // TFLite format
                ExecutionTarget::CPU,
            )
        }.map_err(|e| format!("Failed to load TFLite graph: {:?}", e))?;
        
        Ok(Self {
            graph,
            input_width: width,
            input_height: height,
            num_classes: classes,
        })
    }
    
    fn predict(&self, input: &[u8]) -> Result<Vec<(usize, f32)>, String> {
        let ctx = unsafe {
            wasi_nn::init_execution_context(self.graph)
        }.map_err(|e| format!("Failed to initialize context: {:?}", e))?;
        
        // TFLite MobileNet input format: [1, H, W, 3] (NHWC)
        // Pixel value range: [0, 255] or [-1, 1]
        
        // Normalize
        let normalized: Vec<f32> = input.iter()
            .map(|&p| (p as f32 - 127.5) / 127.5)  // Normalize to [-1, 1]
            .collect();
        
        let input_bytes: &[u8] = bytemuck::cast_slice(&normalized);
        
        unsafe {
            wasi_nn::set_input(
                ctx,
                0,
                wasi_nn::Tensor {
                    dimensions: &[1, self.input_height, self.input_width, 3],
                    r#type: TensorType::F32,
                    data: input_bytes,
                },
            )
        }.map_err(|e| format!("Failed to set input: {:?}", e))?;
        
        // Inference
        unsafe {
            wasi_nn::compute(ctx)
        }.map_err(|e| format!("Inference failed: {:?}", e))?;
        
        // Get output probabilities
        let mut output = vec![0f32; self.num_classes];
        unsafe {
            wasi_nn::get_output(
                ctx,
                0,
                output.as_mut_ptr() as *mut u8,
                (self.num_classes * 4) as u32,
            )
        }.map_err(|e| format!("Failed to get output: {:?}", e))?;
        
        // Sort and return Top-5
        let mut scored: Vec<(usize, f32)> = output.iter()
            .enumerate()
            .map(|(i, &s)| (i, s))
            .collect();
        
        scored.sort_by(|a, b| b.1.partial_cmp(&a.1).unwrap());
        scored.truncate(5);
        
        Ok(scored)
    }
}
```

## 9.2 Object Detection

```rust
// YOLO object detection (using TFLite)
struct YoloDetector {
    graph: wasi_nn::Graph,
    confidence_threshold: f32,
    nms_threshold: f32,
}

#[derive(Debug, Clone)]
struct Detection {
    class_id: usize,
    class_name: String,
    confidence: f32,
    bbox: [f32; 4],  // [x1, y1, x2, y2] normalized coordinates
}

impl YoloDetector {
    fn detect(&self, image: &[f32], width: u32, height: u32) 
        -> Result<Vec<Detection>, String> 
    {
        let ctx = unsafe {
            wasi_nn::init_execution_context(self.graph)
        }.map_err(|e| format!("Initialization failed: {:?}", e))?;
        
        let input_bytes: &[u8] = bytemuck::cast_slice(image);
        unsafe {
            wasi_nn::set_input(
                ctx,
                0,
                wasi_nn::Tensor {
                    dimensions: &[1, height, width, 3],
                    r#type: TensorType::F32,
                    data: input_bytes,
                },
            )
        }.map_err(|e| format!("Failed to set input: {:?}", e))?;
        
        unsafe {
            wasi_nn::compute(ctx)
        }.map_err(|e| format!("Inference failed: {:?}", e))?;
        
        // YOLO output format processing
        // Output: [batch, num_boxes, 5 + num_classes]
        // Each box: [x_center, y_center, width, height, confidence, class_probs...]
        
        let num_boxes = 2535usize;  // YOLOv5s output boxes
        let num_classes = 80usize;  // COCO dataset
        let output_size = num_boxes * (5 + num_classes);
        
        let mut raw_output = vec![0f32; output_size];
        unsafe {
            wasi_nn::get_output(
                ctx,
                0,
                raw_output.as_mut_ptr() as *mut u8,
                (output_size * 4) as u32,
            )
        }.map_err(|e| format!("Failed to get output: {:?}", e))?;
        
        // Parse detection results
        let mut detections = Vec::new();
        
        for i in 0..num_boxes {
            let offset = i * (5 + num_classes);
            let confidence = raw_output[offset + 4];
            
            if confidence < self.confidence_threshold {
                continue;
            }
            
            let x_center = raw_output[offset];
            let y_center = raw_output[offset + 1];
            let box_width = raw_output[offset + 2];
            let box_height = raw_output[offset + 3];
            
            // Find maximum class probability
            let (class_id, class_prob) = raw_output[offset + 5..offset + 5 + num_classes]
                .iter()
                .enumerate()
                .max_by(|a, b| a.1.partial_cmp(b.1).unwrap())
                .map(|(i, &p)| (i, p))
                .unwrap_or((0, 0.0));
            
            let final_confidence = confidence * class_prob;
            
            if final_confidence >= self.confidence_threshold {
                detections.push(Detection {
                    class_id,
                    class_name: format!("class_{}", class_id),
                    confidence: final_confidence,
                    bbox: [
                        x_center - box_width / 2.0,  // x1
                        y_center - box_height / 2.0, // y1
                        x_center + box_width / 2.0,  // x2
                        y_center + box_height / 2.0, // y2
                    ],
                });
            }
        }
        
        // NMS (Non-Maximum Suppression)
        let final_detections = self.apply_nms(detections);
        
        Ok(final_detections)
    }
    
    fn apply_nms(&self, mut detections: Vec<Detection>) -> Vec<Detection> {
        // Sort by confidence
        detections.sort_by(|a, b| b.confidence.partial_cmp(&a.confidence).unwrap());
        
        let mut result = Vec::new();
        let mut suppressed = vec![false; detections.len()];
        
        for i in 0..detections.len() {
            if suppressed[i] { continue; }
            result.push(detections[i].clone());
            
            for j in (i + 1)..detections.len() {
                if suppressed[j] { continue; }
                if detections[i].class_id != detections[j].class_id { continue; }
                
                let iou = self.calc_iou(&detections[i].bbox, &detections[j].bbox);
                if iou > self.nms_threshold {
                    suppressed[j] = true;
                }
            }
        }
        
        result
    }
    
    fn calc_iou(&self, bbox1: &[f32; 4], bbox2: &[f32; 4]) -> f32 {
        let x1 = bbox1[0].max(bbox2[0]);
        let y1 = bbox1[1].max(bbox2[1]);
        let x2 = bbox1[2].min(bbox2[2]);
        let y2 = bbox1[3].min(bbox2[3]);
        
        if x2 <= x1 || y2 <= y1 {
            return 0.0;
        }
        
        let intersection = (x2 - x1) * (y2 - y1);
        let area1 = (bbox1[2] - bbox1[0]) * (bbox1[3] - bbox1[1]);
        let area2 = (bbox2[2] - bbox2[0]) * (bbox2[3] - bbox2[1]);
        let union = area1 + area2 - intersection;
        
        intersection / union
    }
}
```

---

<!-- chunk: 10. LLM Inference -->## 10. LLM Inference

## 10.1 WasmEdge LLM Support

```
WasmEdge LLM Inference Solutions

Solution 1: llama.cpp plugin
  Supported formats: GGUF
  Supported models: Llama 2/3, Mistral, Qwen, Yi, etc.
  Backends: CPU, CUDA, Metal

Solution 2: WASI-NN + GGML backend
  Standard WASI-NN interface
  GGML model format
  
Solution 3: LlamaEdge
  Complete LLM inference framework
  Multi-turn dialogue support
  OpenAI-compatible API
```

## 10.2 LlamaEdge API Server

```bash
# Install WasmEdge with GGML plugin
curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | \
  bash -s -- \
  --plugins wasi_nn-ggml

# Download LLM model (Llama-3.1-8B-Instruct GGUF format)
wget "https://huggingface.co/bartowski/Meta-Llama-3.1-8B-Instruct-GGUF/resolve/main/Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf"

# Download LlamaEdge API server
wget "https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm"

# Start LLM API server (OpenAI API compatible)
wasmedge --dir .:. \
  --nn-preload default:GGML:AUTO:Meta-Llama-3.1-8B-Instruct-Q4_K_M.gguf \
  llama-api-server.wasm \
  --model-name "Llama-3.1-8B" \
  --ctx-size 4096 \
  --socket-addr "0.0.0.0:8080" \
  --log-prompts \
  --log-stat
```

```rust
// WasmEdge LLM inference - Rust client
use wasi_nn::{ExecutionTarget, GraphEncoding, TensorType};
use serde_json::{json, Value};

async fn chat_completion(
    prompt: &str,
    system_prompt: &str,
    max_tokens: u32,
) -> Result<String, String> {
    // Build prompt (Llama-3 format)
    let full_prompt = format!(
        "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\
         {system}\n\
         <|eot_id|><|start_header_id|>user<|end_header_id|>\n\
         {user}\n\
         <|eot_id|><|start_header_id|>assistant<|end_header_id|>\n",
        system = system_prompt,
        user = prompt,
    );
    
    // Convert prompt to token indices (simplified)
    let prompt_bytes = full_prompt.as_bytes();
    
    // Load LLM graph (using GGML backend)
    let graph = unsafe {
        wasi_nn::load_by_name("default")
    }.map_err(|e| format!("Failed to load LLM: {:?}", e))?;
    
    let ctx = unsafe {
        wasi_nn::init_execution_context(graph)
    }.map_err(|e| format!("Failed to initialize context: {:?}", e))?;
    
    // Set inference parameters
    let params = json!({
        "stream_stdout": false,
        "n-predict": max_tokens,
        "ctx-size": 4096,
        "temperature": 0.7,
        "top-p": 0.9,
        "repeat-penalty": 1.1,
    });
    
    let params_bytes = params.to_string();
    unsafe {
        wasi_nn::set_input(
            ctx,
            1,  // Parameter input index
            wasi_nn::Tensor {
                dimensions: &[1],
                r#type: TensorType::U8,
                data: params_bytes.as_bytes(),
            },
        )
    }.map_err(|e| format!("Failed to set parameters: {:?}", e))?;
    
    // Set prompt input
    unsafe {
        wasi_nn::set_input(
            ctx,
            0,  // Prompt input index
            wasi_nn::Tensor {
                dimensions: &[1],
                r#type: TensorType::U8,
                data: prompt_bytes,
            },
        )
    }.map_err(|e| format!("Failed to set prompt: {:?}", e))?;
    
    // Execute inference
    unsafe {
        wasi_nn::compute(ctx)
    }.map_err(|e| format!("Inference failed: {:?}", e))?;
    
    // Get generated text
    let mut output_buf = vec![0u8; 4096 * 4];  // Max 4096 tokens
    let output_size = unsafe {
        wasi_nn::get_output(
            ctx,
            0,
            output_buf.as_mut_ptr(),
            output_buf.len() as u32,
        )
    }.map_err(|e| format!("Failed to get output: {:?}", e))?;
    
    let response = String::from_utf8_lossy(&output_buf[..output_size as usize])
        .to_string();
    
    Ok(response)
}
```

## 10.3 Kubernetes LLM Inference Deployment

```yaml
# WasmEdge LLM Inference Service
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wasmedge-llm-service
  namespace: ai-inference
spec:
  replicas: 2
  selector:
    matchLabels:
      app: wasmedge-llm
  template:
    metadata:
      labels:
        app: wasmedge-llm
    spec:
      runtimeClassName: wasmedge-ai
      
      initContainers:
      # Download model (only when PVC is empty)
      - name: model-downloader
        image: curlimages/curl:latest
        command:
        - sh
        - -c
        - |
          if [ ! -f /models/llama-3.1-8b-q4.gguf ]; then
            echo "Downloading LLM model..."
            curl -L -o /models/llama-3.1-8b-q4.gguf \
              "https://huggingface.co/.../llama-3.1-8b-q4.gguf"
            echo "Download complete"
          else
            echo "Model already exists, skipping download"
          fi
        volumeMounts:
        - name: models
          mountPath: /models
      
      containers:
      - name: llm-server
        image: ghcr.io/myorg/wasmedge-llm-server:latest
        ports:
        - containerPort: 8080
          name: http
        env:
        - name: MODEL_PATH
          value: "/models/llama-3.1-8b-q4.gguf"
        - name: MODEL_NAME
          value: "Llama-3.1-8B"
        - name: CTX_SIZE
          value: "4096"
        - name: GPU_LAYERS
          value: "35"  # Number of GPU-accelerated layers
        resources:
          requests:
            memory: "8Gi"
            cpu: "2"
          limits:
            memory: "16Gi"
            cpu: "8"
            # nvidia.com/gpu: "1"  # Enable GPU
        volumeMounts:
        - name: models
          mountPath: /models
          readOnly: true
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 60  # LLM loading takes time
          periodSeconds: 30
      
      volumes:
      - name: models
        persistentVolumeClaim:
          claimName: llm-models-pvc

---
# PVC for model storage
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: llm-models-pvc
  namespace: ai-inference
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 50Gi
  storageClassName: fast-ssd
```

---

<!-- chunk: 11. Performance Optimization -->## 11. Performance Optimization

## 11.1 AOT Compilation Optimization

```bash
# WasmEdge AOT compilation
wasmedge compile \
  --optimize 3 \          # Optimization level 0-3
  --output app.so \       # Output AOT shared library
  app.wasm

# Run AOT compiled module
wasmedge app.so

# Optimize for specific CPU features
wasmedge compile \
  --cpu-features avx512f,avx2 \  # Enable AVX-512 and AVX2
  --optimize 3 \
  --output app.so \
  app.wasm

# ARM64 optimization
wasmedge compile \
  --cpu-features neon \           # Enable ARM NEON
  --optimize 3 \
  --output app-arm64.so \
  app.wasm
```

```rust
// Enable AOT in WasmEdge SDK
use wasmedge_sdk::{
    config::{
        CommonConfigOptions, ConfigBuilder, CompilerConfigOptions,
        CompilerOptimizationLevel,
    },
    Compiler, Vm,
};

fn compile_wasm_to_aot(wasm_path: &str, output_path: &str) -> Result<(), Box<dyn std::error::Error>> {
    let config = ConfigBuilder::new(CommonConfigOptions::default())
        .with_compiler_config(
            CompilerConfigOptions::default()
                .optimization_level(CompilerOptimizationLevel::O3)
                .output_format(wasmedge_sdk::config::CompilerOutputFormat::Native)
                .generic_binary(false)  // Optimize for current CPU
                .interruptible(true),   // Support interruption
        )
        .build()?;
    
    let compiler = Compiler::new(Some(&config))?;
    compiler.compile_from_file(wasm_path, output_path)?;
    
    println!("AOT compilation complete: {} -> {}", wasm_path, output_path);
    Ok(())
}
```

## 11.2 SIMD Acceleration

```rust
// Leverage WasmEdge SIMD128 for vector acceleration
// Requires compilation with: --target-feature +simd128

#[cfg(target_arch = "wasm32")]
use std::arch::wasm32::*;

#[cfg(target_arch = "wasm32")]
#[target_feature(enable = "simd128")]
pub unsafe fn dot_product_simd(a: &[f32], b: &[f32]) -> f32 {
    assert_eq!(a.len(), b.len());
    
    let n = a.len();
    let chunks = n / 4;
    let mut sum = f32x4_splat(0.0);
    
    for i in 0..chunks {
        let va = v128_load(a[i*4..].as_ptr() as *const v128);
        let vb = v128_load(b[i*4..].as_ptr() as *const v128);
        let product = f32x4_mul(va, vb);
        sum = f32x4_add(sum, product);
    }
    
    // Horizontal sum
    let sum_arr = [
        f32x4_extract_lane::<0>(sum),
        f32x4_extract_lane::<1>(sum),
        f32x4_extract_lane::<2>(sum),
        f32x4_extract_lane::<3>(sum),
    ];
    
    let mut result = sum_arr.iter().sum::<f32>();
    
    // Handle remaining elements
    for i in (chunks * 4)..n {
        result += a[i] * b[i];
    }
    
    result
}

// Non-SIMD fallback
#[cfg(not(target_arch = "wasm32"))]
pub fn dot_product_simd(a: &[f32], b: &[f32]) -> f32 {
    a.iter().zip(b.iter()).map(|(x, y)| x * y).sum()
}

// Matrix multiplication SIMD optimization
#[cfg(target_arch = "wasm32")]
#[target_feature(enable = "simd128")]
pub unsafe fn matrix_multiply_simd(
    a: &[f32], b: &[f32], c: &mut [f32],
    m: usize, n: usize, k: usize,
) {
    for i in 0..m {
        for j in 0..n {
            let mut sum = f32x4_splat(0.0);
            let chunks = k / 4;
            
            for l in 0..chunks {
                let va = v128_load(a[i * k + l * 4..].as_ptr() as *const v128);
                let vb = v128_load(b[l * 4 * n + j..].as_ptr() as *const v128);
                sum = f32x4_add(sum, f32x4_mul(va, vb));
            }
            
            let mut result = f32x4_extract_lane::<0>(sum) +
                             f32x4_extract_lane::<1>(sum) +
                             f32x4_extract_lane::<2>(sum) +
                             f32x4_extract_lane::<3>(sum);
            
            // Handle remaining
            for l in (chunks * 4)..k {
                result += a[i * k + l] * b[l * n + j];
            }
            
            c[i * n + j] = result;
        }
    }
}
```

## 11.3 Memory Optimization

```bash
# WasmEdge memory configuration optimization
wasmedge \
  --max-memory-page 1024 \  # Maximum memory: 1024 * 64KB = 64MB
  --memory-init-page 16 \   # Initial memory: 16 * 64KB = 1MB
  app.wasm

# Limit stack size
wasmedge \
  --force-interpreter \     # Use interpreter mode (low memory, slow speed)
  --max-memory-page 64 \    # Limit to 4MB
  app.wasm
```

---

<!-- chunk: 12. Production Practices -->## 12. Production Practices

## 12.1 Production Deployment Architecture

```yaml
# Complete production-grade WasmEdge deployment
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wasmedge-prod
  namespace: production
  annotations:
    kubernetes.io/change-cause: "Deploy WasmEdge AI inference service v1.5.0"
spec:
  replicas: 5
  selector:
    matchLabels:
      app: wasmedge-prod
  
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 2
      maxUnavailable: 0  # Zero downtime update
  
  template:
    metadata:
      labels:
        app: wasmedge-prod
        version: "v1.5.0"
      annotations:
        module.wasm.image/variant: compat-smart
        prometheus.io/scrape: "true"
        prometheus.io/port: "9090"
    
    spec:
      runtimeClassName: wasmedge-ai
      
      # Priority
      priorityClassName: production-critical
      
      # Security context
      securityContext:
        runAsNonRoot: true
        runAsUser: 65534
        seccompProfile:
          type: RuntimeDefault
      
      containers:
      - name: inference
        image: ghcr.io/myorg/wasmedge-inference:v1.5.0
        
        ports:
        - containerPort: 8080
          name: http
        - containerPort: 9090
          name: metrics
        
        env:
        - name: WASMEDGE_PLUGIN_PATH
          value: "/usr/lib/wasmedge"
        - name: MODEL_PATH
          value: "/models/mobilenet_v3.onnx"
        - name: BATCH_SIZE
          value: "8"
        - name: NUM_THREADS
          value: "4"
        
        resources:
          requests:
            memory: "256Mi"
            cpu: "500m"
          limits:
            memory: "1Gi"
            cpu: "2"
        
        livenessProbe:
          httpGet:
            path: /health
            port: 8080
          initialDelaySeconds: 10
          periodSeconds: 15
          failureThreshold: 3
        
        readinessProbe:
          httpGet:
            path: /ready
            port: 8080
          initialDelaySeconds: 5
          periodSeconds: 5
        
        startupProbe:
          httpGet:
            path: /health
            port: 8080
          failureThreshold: 30
          periodSeconds: 3
        
        securityContext:
          allowPrivilegeEscalation: false
          readOnlyRootFilesystem: true
          capabilities:
            drop: [ALL]
        
        volumeMounts:
        - name: models
          mountPath: /models
          readOnly: true
        - name: tmp
          mountPath: /tmp
        - name: cache
          mountPath: /cache
      
      volumes:
      - name: models
        persistentVolumeClaim:
          claimName: ai-models-pvc
      - name: tmp
        emptyDir: {}
      - name: cache
        emptyDir:
          sizeLimit: 256Mi
      
      # Topology spread
      topologySpreadConstraints:
      - maxSkew: 1
        topologyKey: kubernetes.io/hostname
        whenUnsatisfiable: DoNotSchedule
        labelSelector:
          matchLabels:
            app: wasmedge-prod
      - maxSkew: 2
        topologyKey: topology.kubernetes.io/zone
        whenUnsatisfiable: ScheduleAnyway
        labelSelector:
          matchLabels:
            app: wasmedge-prod
      
      # Node affinity
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: wasmedge.io/ai
                operator: Exists
      
      tolerations:
      - key: wasmedge.io/ai
        operator: Exists
        effect: NoSchedule
```

## 12.2 CI/CD Pipeline

```yaml
# .github/workflows/wasmedge-deploy.yml
name: WasmEdge Build and Deploy

on:
  push:
    branches: [main]
  pull_request:

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    
    - name: Install Rust toolchain
      uses: dtolnay/rust-toolchain@stable
      with:
        targets: wasm32-wasi
    
    - name: Install WasmEdge
      run: |
        curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | \
          bash -s -- --version 0.14.0
        echo "$HOME/.wasmedge/bin" >> $GITHUB_PATH
    
    - name: Compile Wasm module
      run: |
        cargo build --target wasm32-wasi --release
        ls -lh target/wasm32-wasi/release/*.wasm
    
    - name: AOT compilation optimization
      run: |
        wasmedge compile \
          --optimize 3 \
          target/wasm32-wasi/release/app.wasm \
          target/app.aot.wasm
        echo "AOT module size: $(du -sh target/app.aot.wasm)"
    
    - name: Run Wasm tests
      run: |
        wasmedge --dir .:. target/wasm32-wasi/release/tests.wasm
    
    - name: Build OCI image
      run: |
        docker build \
          --label "org.opencontainers.image.revision=${{ github.sha }}" \
          -t ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }} \
          -t ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest \
          .
    
    - name: Push image
      if: github.event_name == 'push'
      run: |
        echo ${{ secrets.GITHUB_TOKEN }} | docker login ${{ env.REGISTRY }} -u ${{ github.actor }} --password-stdin
        docker push ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
        docker push ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:latest
    
    - name: Deploy to Kubernetes
      if: github.ref == 'refs/heads/main'
      uses: azure/k8s-set-context@v3
      with:
        kubeconfig: ${{ secrets.KUBECONFIG }}
      
    - run: |
        kubectl set image deployment/wasmedge-prod \
          inference=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }} \
          -n production
        kubectl rollout status deployment/wasmedge-prod -n production
```

## 12.3 Monitoring and Alerting

```yaml
# WasmEdge production alert rules
apiVersion: monitoring.coreos.com/v1
kind: PrometheusRule
metadata:
  name: wasmedge-production-alerts
  namespace: monitoring
spec:
  groups:
  - name: wasmedge.critical
    rules:
    # High inference latency
    - alert: WasmEdgeInferenceLatencyHigh
      expr: |
        histogram_quantile(0.99,
          rate(wasmedge_inference_duration_seconds_bucket[5m])
        ) > 0.5
      for: 3m
      labels:
        severity: critical
        team: ai-platform
      annotations:
        summary: "WasmEdge inference P99 latency exceeds 500ms"
        description: "Current P99 latency: {{ $value }}s"
    
    # High memory usage
    - alert: WasmEdgeHighMemory
      expr: |
        container_memory_usage_bytes{container="inference"} /
        container_spec_memory_limit_bytes{container="inference"} > 0.9
      for: 5m
      labels:
        severity: warning
      annotations:
        summary: "WasmEdge container memory usage exceeds 90%"
    
    # High inference error rate
    - alert: WasmEdgeHighErrorRate
      expr: |
        rate(wasmedge_inference_errors_total[5m]) /
        rate(wasmedge_inference_total[5m]) > 0.01
      for: 2m
      labels:
        severity: critical
      annotations:
        summary: "WasmEdge inference error rate exceeds 1%"
    
    # Frequent pod restarts
    - alert: WasmEdgePodRestartHigh
      expr: |
        increase(kube_pod_container_status_restarts_total{
          container="inference"
        }[1h]) > 3
      labels:
        severity: warning
      annotations:
        summary: "WasmEdge Pod restarted more than 3 times in 1 hour"
```

---

<!-- chunk: References -->## References

## Official Resources
- [WasmEdge Official Documentation](https://wasmedge.org/docs/)
- [WasmEdge GitHub](https://github.com/WasmEdge/WasmEdge)
- [WasmEdge Plugins](https://wasmedge.org/docs/start/install#wasmedge-plug-ins)

## AI Inference
- [WASI-NN Specification](https://github.com/WebAssembly/wasi-nn)
- [LlamaEdge](https://github.com/LlamaEdge/LlamaEdge)
- [WasmEdge AI Examples](https://github.com/second-state/WasmEdge-WASINN-examples)

## CNCF Related
- [WasmEdge CNCF Sandbox](https://www.cncf.io/projects/wasmedge-runtime/)
- [containerd runwasi](https://github.com/containerd/runwasi)

## Learning Resources
- [WasmEdge Book](https://wasmedge.org/docs/)
- [WasmEdge Rust SDK](https://github.com/second-state/wasmedge-rust-sdk)
- [Second State Blog](https://www.secondstate.io/articles/)

---

*Last Updated: 2025-03-04*
*Version: 1.0.0*

---

<!-- chunk: Obsidian Related Documents -->## Obsidian Related Documents

- domain-38-webassembly-cloud-native MOC
- [[domain-15-specialized-tech/README.md|Domain 15: WebAssembly Cloud Native]]
- Domain-38 WebAssembly Cloud Native - Open Source Project Index
- WebAssembly Cloud Native Fundamentals
- containerd Wasm Runtime
- SpinKube Framework Practice
- wasmCloud Platform
- Wasm Component Model
- Wasm Plugin System
- Wasm AI Inference
- Wasm Serverless
- Wasm Security and Sandbox

## See Also

- 03-spinkube-framework
- 04-wasmcloud-platform
- 06-wasm-component-model
- 07-wasm-plugin-system

<!-- risk-assessed -->
