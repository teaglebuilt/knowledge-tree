---
title: WebAssembly Production Deployment Guide
description: A guide for productionizing the deployment of WebAssembly (Wasm) workloads on Kubernetes, covering runtime selection (Spin/containerd-wasm-shim), scheduling, networking and storage, observability, security, and CI/CD.
summary: Guide for production deployment of Wasm on Kubernetes, covering runtime selection, scheduling, networking/storage, observability, security, and CI/CD.
category: specialized-tech
tags:
- production
- best-practices
- playbook
- specialized-tech
- webassembly
- wasm
- spin
- containerd-wasm-shim
tier: core
created: '2026-07-01'
last_updated: '2026-07'
difficulty: advanced
reading_level: advanced
audience:
- SRE
- Operations Engineer
- Platform Engineer
estimated_read_time: 25min
intent_queries:
- How to produceize Wasm deployment on Kubernetes
- How to choose between Spin and containerd-wasm-shim
- Wasm workload scheduling and observability
- Production security practices and CI/CD for Wasm
trigger_keywords:
- WebAssembly
- Wasm
- Spin
- containerd-wasm-shim
- WasmEdge
- Wasm runtime
prerequisites:
- kubectl-basics
- containerd-basics
- webassembly-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
- '1.33'
authors:
- name: Dillan Teagle
  role: contributor
original_language: Chinese
source_path: tree/infrastructure/kubernetes/webassembly/wasm-production-deployment.md
---

> **Production Environment Security Tips**
>
> Commands included in this document can be directly executed. Before execution, please confirm that the target cluster and namespace are correct; that you have sufficient RBAC permissions; and that the commands have been validated in a non-production environment. Risk level annotations for commands: 🔴 High risk (may cause data loss or service disruption), 🟡 Medium risk (will modify cluster state but usually rollbackable), 🟢 Low risk/readonly (information gathering with no side effects).


# WebAssembly Production Deployment Guide

This guide is aimed at Site Reliability Engineers (SRE) and Platform Engineers who wish to run WebAssembly (Wasm) workloads on Kubernetes in production standards, providing a complete operational path for runtime selection, node configuration, scheduling, networking/storage, observability, security, and CI/CD. WebAssembly's quick startup, small size, and strong isolation characteristics gradually become an effective supplement to running stateless functions and microservices in cloud-native scenarios. However, the Wasm ecosystem is rapidly evolving, with significant differences in runtimes, toolchains, and observability compared to traditional containers. The commands in this guide can be directly executed in environments where `kubectl`, `containerd`, and related CLI tools are installed. All changes should be validated in a test environment and followed the change management requirements outlined in the [[domain-11-production-operations/99-production-readiness-operations-guide.md|Production Readiness Operations Guide]].

## 1. Scope and Applicability

This guide is applicable to the following scenarios:

- Deploying microservices based on Spin, WasmEdge, or other Wasm runtimes on Kubernetes.
- Configuring containerd shim to support Wasm images.
- Designing scheduling, networking, storage, and observability solutions for Wasm workloads.
- Troubleshooting failed Wasm pod launches, runtime exceptions, network/storage mounting issues.
- Wanting to deploy Wasm alongside traditional container workloads in the same cluster.

## 2. Pre-requisites and Tools

``` bash
# 🟢 Low Risk: Read-only/information gathering, typically with no side effects
# Essential Tools
kubectl version
ctr version
spin --version

# Recommended Runtime
# containerd-wasm-shim: https://github.com/containerd/runwasi
# SpinKube / Spin Operator: https://www.spinkube.dev/
# WasmEdge: https://wasmedge.org/
```
Requirements:
- The cluster uses containerd as the CRI.
- Nodes have installed the corresponding Wasm runtime binary or shim.
- A RuntimeClass has been registered (e.g., `wasmtime-spin`, `wasmedge`).
- The image repository supports OCI artifacts or Wasm module format.

## 3. Core Concepts and Architecture

### 3.1 Choosing a Wasm Runtime

| Runtime | Features | Applicable Scenarios |
|---|---|---|
| **Spin (Fermyon)** | Event-driven, HTTP triggers, support for component model | Stateless microservices, APIs, function computing |
| **WasmEdge** | High performance, support for multiple languages, AI/media extensions | Edge inference, real-time processing |
| **containerd-wasm-shim (runwasi)** | Standard containerd shim, compatible with OCI | Requires mixed deployment with containers |

Production recommendation: Prioritize using Spin + SpinKube Operator for new services; use containerd-wasm-shim when integration with existing containers is required deeply.

### 3.2 Deployment Models

- **OCI Image Mode**: Package the Wasm module as an OCI image and start it via the shim by containerd. This mode is compatible with the existing container image supply chain and facilitates the use of existing CI/CD and image repositories.
- **Spin App Mode**: Use SpinKube CRDs (SpinApp) to directly describe the Wasm application, managed by the Spin Operator. This mode is closer to the native semantics of Wasm and supports automatic scaling and event triggering.

## 4. Standard Operational Procedures

### 4.1 Install containerd-wasm-shim

> **🔴 High Risk Operation Warning**
>
> The commands below are irreversible or highly impactful operations. Please confirm before executing:
> - Backup critical data and configurations
> - Be within an approved change window
> - Obtain authorization from relevant parties
> - Prepare rollback or recovery plans
> - Ensure correct cluster, Namespace, node/resource names

``` bash
# 🔴 High Risk: May cause data loss or service disruption. Execute only after backing up, approval, and rollback plan preparation
# Download shim on the node (using Spin as an example)
VERSION=v0.11.0
curl -LO https://github.com/containerd/runwasi/releases/download/${VERSION}/containerd-shim-spin-v2-linux-x86_64.tar.gz
sudo tar -xzf containerd-shim-spin-v2-linux-x86_64.tar.gz -C /usr/local/bin/

# Configure containerd /etc/containerd/config.toml
sudo tee -a /etc/containerd/config.toml <<EOF
[plugins."io.containerd.grpc.v1.cri".containerd.runtimes.spin]
  runtime_type = "io.containerd.spin.v2"
EOF

sudo systemctl restart containerd
```
### 4.2 Create RuntimeClass

``` bash
# 🟡 Medium Risk: Will modify cluster/resource states. Please confirm the target, impact scope, and authorization before execution
cat <<EOF | kubectl apply -f -
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: wasmtime-spin
handler: spin
scheduling:
  nodeSelector:
    runtime: wasm
EOF
```
### 4.3 Deploy Wasm Workloads (OCI mode)

``` bash
# 🟡 Medium Risk: Will modify cluster/resource states. Please confirm the target, impact scope, and authorization before execution
cat <<EOF | kubectl apply -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: wasm-hello
  namespace: prod
spec:
  replicas: 3
  selector:
    matchLabels:
      app: wasm-hello
  template:
    metadata:
      labels:
        app: wasm-hello
    spec:
      runtimeClassName: wasmtime-spin
      nodeSelector:
        runtime: wasm
      containers:
      - name: hello
        image: ghcr.io/deislabs/containerd-wasm-shims/examples/spin-rust-hello:latest
        resources:
          requests:
            cpu: "0.1"
            memory: 32Mi
          limits:
            cpu: "0.5"
            memory: 128Mi
---
apiVersion: v1
kind: Service
metadata:
  name: wasm-hello
  namespace: prod
spec:
  selector:
    app: wasm-hello
  ports:
  - port: 80
    targetPort: 8080
EOF
```
### 4.4 Deploy using SpinKube Operator

``` bash
# 🟡 Medium Risk: Will modify cluster/resource states. Please confirm the target, impact scope, and authorization before execution
# Install SpinKube
kubectl apply -f https://github.com/spinkube/spin-operator/releases/download/v0.2.0/spin-operator.runtime-class.yaml
kubectl apply -f https://github.com/spinkube/spin-operator/releases/download/v0.2.0/spin-operator.crds.yaml
kubectl apply -f https://github.com/spinkube/spin-operator/releases/download/v0.2.0/spin-operator.yaml

# Create SpinApp
cat <<EOF | kubectl apply -f -
apiVersion: core.spinoperator.dev/v1alpha1
kind: SpinApp
metadata:
  name: prod-spin-app
  namespace: prod
spec:
  image: ghcr.io/spinkube/spin-operator/samples/spin-rust-hello:latest
  replicas: 3
  executor: containerd-shim-spin
  resources:
    requests:
      cpu: "0.1"
      memory: 32Mi
EOF
```
### 4.5 Network and Storage

Wasm modules are typically stateless, and persistent needs are met through external services (object storage, database). For temporary storage:

```yaml
spec:
  containers:
  - name: app
    image: <wasm-image>
    volumeMounts:
    - name: tmp
      mountPath: /tmp
  volumes:
  - name: tmp
    emptyDir:
      sizeLimit: 100Mi
```

Network:
- Expose HTTP services using standard Kubernetes Service/Ingress.
- Limit outbound access to Wasm Pods using NetworkPolicy.
- For Wasm applications that need to access external services, use Kubernetes ExternalName Service or Sidecar proxies.

### 4.6 Observability

``` bash
# 🟡 Medium Risk: Modifies cluster/resource status; please confirm target, impact scope, and authorization before execution
# 🟡 Medium Risk: Modifies cluster/resource states; confirm target, impact scope, and authorization before execution
kubectl logs -l app=wasm-hello -n prod --tail=100

# Expose metrics (requires runtime support)
# Capture metrics at `/metrics` using Prometheus
cat <<EOF | kubectl apply -f -
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: wasm-hello
  namespace: monitoring
spec:
  selector:
    matchLabels:
      app: wasm-hello
  endpoints:
  - port: metrics
    path: /metrics
EOF
```
### 4.7 CI/CD

```yaml
# GitHub Actions Example Snippet
- name: Build Wasm module
  run: spin build

- name: Push OCI artifact
  run: spin registry push ghcr.io/<org>/wasm-hello:${{ github.sha }}

- name: Deploy to Kubernetes
  run: kubectl set image deployment/wasm-hello hello=ghcr.io/<org>/wasm-hello:${{ github.sha }} -n prod
```

Suggest enabling cosign signing for Wasm images and validating signatures before deployment using Kyverno or OPA.

## 5. Key Checkpoints and Verification Commands

| Checkpoint | Command | Passes Standard |
|---|---|---|
| RuntimeClass | `kubectl get runtimeclass` | `wasmtime-spin` exists |
| Node Labels | `kubectl get nodes -L runtime` | Wasm nodes have runtime=wasm |
| Pod Status | `kubectl get pods -n prod -l app=wasm-hello` | Running, no CrashLoop |
| Service Access | `kubectl port-forward svc/wasm-hello 8080:80 -n prod` | Curl returns 200 |
| Resource Usage | `kubectl top pods -n prod` | Resources usage is as expected |
| Logs | `kubectl logs -n prod -l app=wasm-hello` | No abnormal stack traces |

## 6. Common Faults and Remediation

| Phenomenon | Root Cause | Handling Command/Steps |
|---|---|---|
| Pod startup failure `runtime not found` | containerd not configured with shim or RuntimeClass mismatch | Check node shim installation and containerd configuration |
| Image pull failure | OCI artifact repository does not support Wasm type | Confirm registry support for OCI artifacts; check image tag |
| Service cannot be accessed | Incorrect port mapping, missing Ingress configuration | Check Container Port, Service targetPort, Ingress rules |
| Performance below expectations | Wasm module not optimized, CPU limits too low | Analyze module performance; adjust resources limits |
| Storage write fails | Wasm module lacks filesystem permissions | Use emptyDir or external storage; check WASI permissions |
| Missing monitoring metrics | Runtime not exposing /metrics | Check application code and ServiceMonitor configuration |

## 7. Risks and Considerations

1. **Wasm ecosystem is rapidly evolving**: Ensure runtime and Operator versions are stable and supported before production use.
2. **Not all workloads are suitable for Wasm**: I/O-intensive, native library-dependent scenarios should continue using containers.
3. **Sandbox security does not equal absolute security**: Still need to follow minimum privilege, NetworkPolicy, image signing, and vulnerability scanning.
4. **Resource limits must be cautious**: Wasm starts quickly but may be mistakenly perceived as resourceless, still set requests/limits to avoid node overload.
5. **Limited debugging tools**: Familiarize yourself with `spin logs`, `kubectl logs`, and `ctr`; use netshoot sidecar when necessary.
6. **Secure the image supply chain**: Sign Wasm OCI artifacts with cosign/notation to prevent unauthorized modules from running.
7. **Storage capabilities are limited**: WASI file system capabilities for Wasm are limited, complex persistent needs should be achieved through external services.

## 8. Related Runbooks / Recommended Reading

- [[domain-11-production-operations/99-production-readiness-operations-guide.md|Production Operations Domain Production Readiness Operations Guide]]
- [[01-wasm-fundamentals-cloud-native.md|Wasm Cloud Native Fundamentals]]
- [[02-containerd-wasm-shim.md|containerd-wasm-shim]]
- [[03-spinkube-framework.md|SpinKube Framework]]
- [[10-wasm-security-sandbox.md|WebAssembly Security Sandbox]]
- [[domain-13-container-runtime/README.md|Container Runtime Domain]]
- [[domain-05-security-compliance/README.md|Security Compliance Domain]]


<!-- risk-assessed -->
