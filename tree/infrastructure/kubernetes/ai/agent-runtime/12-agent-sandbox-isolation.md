---
title: Agent Sandbox and Isolation
description: 'Agent execution sandbox architecture: Docker container isolation, gVisor syscall interception, Firecracker microVM, cloud sandbox services, and K8s security policies'
summary: 'Agent execution sandbox architecture: Docker container isolation, gVisor syscall interception, Firecracker microVM, cloud sandbox services, and K8s security policies'
category: ai-ml-infra
tags:
- ai
- agent
- runtime
- sandbox
- security
- isolation
tier: supporting
created: '2026-07-02'
last_updated: 2026-07
difficulty: advanced
reading_level: advanced
audience:
- AI Engineers
- Platform Engineers
- Architects
estimated_read_time: 20min
intent_queries:
- What is Agent sandbox isolation
- How to build a secure sandbox for Agents
- gVisor Firecracker Agent isolation
trigger_keywords:
- agent-sandbox
- isolation
- gvisor
- firecracker
- security
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
source_path: tree/infrastructure/kubernetes/ai/agent-runtime/12-agent-sandbox-isolation.md
---
> **Production Environment Safety Notice**
>
> This document contains operational commands that can be executed directly. Before executing, confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether validation has been performed in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state, but generally reversible), 🟢 Low risk/Read-only (information gathering, no side effects).


# Agent Sandbox and Isolation

## Overview

Security isolation for AI Agents is a core challenge in production deployments. Unlike traditional applications, Agents typically need to execute LLM-generated code, call external APIs, and access the file system — all of which introduce significant security risks. An out-of-control Agent can lead to data leakage, resource abuse, or even system intrusion.

This document systematically introduces multiple Agent sandbox implementation approaches: from lightweight Docker container isolation to strongly isolated Firecracker microVMs, as well as cloud-based sandbox services such as E2B and Modal, along with security policy configurations in K8s environments.

```
Isolation Level Comparison:

Level         Technology              Isolation Strength    Startup Time    Resource Overhead
──────────────────────────────────────────────────────────────────────────────────────────
Process       Docker container        Medium                ~100ms          Low
Syscall       gVisor                  Medium-High           ~200ms          Medium
Hardware      Firecracker microVM     High                  ~125ms          Medium-High
Cloud         E2B/Modal               High                  ~500ms          On-demand
```

## Docker Container Sandbox

### Basic Container Configuration

```dockerfile
# Agent sandbox base image
FROM python:3.11-slim AS base

# Create non-root user
RUN groupadd -r agent && useradd -r -g agent -d /home/agent agent

# Install minimal dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /workspace

# Switch to non-root user
USER agent

# Entrypoint
ENTRYPOINT ["python", "-m", "agent_executor"]
```

### Resource Limits

```yaml
# K8s Pod resource configuration
apiVersion: v1
kind: Pod
metadata:
  name: agent-sandbox
  labels:
    app: agent-executor
spec:
  securityContext:
    runAsNonRoot: true
    runAsUser: 1000
    runAsGroup: 1000
    fsGroup: 1000
    seccompProfile:
      type: RuntimeDefault

  containers:
    - name: agent
      image: registry.example.com/agent-sandbox:latest
      resources:
        requests:
          cpu: "250m"
          memory: "256Mi"
          ephemeral-storage: "1Gi"
        limits:
          cpu: "1"
          memory: "512Mi"
          ephemeral-storage: "5Gi"

      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL

      volumeMounts:
        - name: workspace
          mountPath: /workspace
        - name: tmp
          mountPath: /tmp

  volumes:
    - name: workspace
      emptyDir:
        sizeLimit: 1Gi
    - name: tmp
      emptyDir:
        medium: Memory
        sizeLimit: 100Mi
```

### seccomp Configuration

```json
{
  "defaultAction": "SCMP_ACT_ERRNO",
  "architectures": ["SCMP_ARCH_X86_64"],
  "syscalls": [
    {
      "names": [
        "read", "write", "open", "close", "stat", "fstat",
        "lstat", "poll", "lseek", "mmap", "mprotect", "munmap",
        "brk", "ioctl", "access", "pipe", "select", "sched_yield",
        "mremap", "msync", "mincore", "madvise", "dup", "dup2",
        "nanosleep", "getpid", "clone", "fork", "vfork", "execve",
        "exit", "wait4", "kill", "uname", "fcntl", "flock",
        "fsync", "fdatasync", "truncate", "ftruncate", "getdents",
        "getcwd", "chdir", "rename", "mkdir", "rmdir", "link",
        "unlink", "symlink", "readlink", "chmod", "chown", "arch_prctl",
        "gettimeofday", "getuid", "getgid", "geteuid", "getegid",
        "getppid", "getpgrp", "setsid", "setuid", "setgid",
        "sigaltstack", "rt_sigaction", "rt_sigprocmask",
        "pread64", "pwrite64", "readv", "writev",
        "socket", "connect", "accept", "sendto", "recvfrom",
        "sendmsg", "recvmsg", "shutdown", "bind", "listen",
        "getsockname", "getpeername", "socketpair",
        "epoll_create", "epoll_ctl", "epoll_wait",
        "clock_gettime", "clock_getres", "exit_group",
        "futex", "set_robust_list", "get_robust_list",
        "epoll_create1", "pipe2", "dup3", "preadv", "pwritev",
        "recvmmsg", "sendmmsg", "getrandom", "memfd_create",
        "statx", "rseq", "clone3", "close_range",
        "epoll_pwait2", "faccessat2"
      ],
      "action": "SCMP_ACT_ALLOW"
    }
  ]
}
```

### AppArmor Configuration

```bash
# /etc/apparmor.d/agent-sandbox
#include <tunables/global>

profile agent-sandbox flags=(attach_disconnected,mediate_deleted) {
  #include <abstractions/base>
  #include <abstractions/python>
  #include <abstractions/openssl>

  # Allow reading system libraries
  /usr/lib/** r,
  /lib/** r,

  # Read/write working directory
  /workspace/** rw,
  /tmp/** rw,

  # Deny access to sensitive directories
  deny /etc/shadow r,
  deny /etc/passwd w,
  deny /root/** rwx,
  deny /home/**/.* rwx,

  # Network access (restrict outbound)
  network inet stream,
  network inet dgram,
  deny network inet6,

  # Deny mounting
  deny mount,
  deny umount,
  deny pivot_root,

  # Deny loading kernel modules
  deny /sbin/modprobe x,
  deny /sbin/insmod x,

  # Signal restrictions
  signal receive,
  signal send,
}
```

## gVisor Sandbox

### gVisor Principles

gVisor is a user-space kernel that provides strong isolation by intercepting system calls:

```
Traditional container:
  Application → syscall → host kernel → hardware
  
gVisor:
  Application → syscall → Sentry (user-space kernel) → Gofer (file proxy) → host kernel → hardware

gVisor core components:
  Sentry: User-space kernel, implements the Linux syscall interface
  Gofer: File system proxy, restricts host file access
  Runsc: OCI-compatible container runtime
```

### Integrating gVisor with K8s

```yaml
# Install gVisor RuntimeClass
apiVersion: node.k8s.io/v1
kind: RuntimeClass
metadata:
  name: gvisor
handler: runsc
scheduling:
  nodeSelector:
    node.kubernetes.io/gvisor: "true"
---
# Agent Pod using gVisor
apiVersion: v1
kind: Pod
metadata:
  name: agent-gvisor-sandbox
spec:
  runtimeClassName: gvisor
  containers:
    - name: agent
      image: registry.example.com/agent-sandbox:latest
      resources:
        requests:
          cpu: "500m"
          memory: "512Mi"
        limits:
          cpu: "2"
          memory: "1Gi"
      securityContext:
        runAsNonRoot: true
        readOnlyRootFilesystem: true
```

### gVisor Runtime Configuration

```json
// /etc/docker/daemon.json
{
  "runtimes": {
    "runsc": {
      "path": "/usr/local/bin/runsc",
      "runtimeArgs": [
        "--platform=systrap",
        "--network=sandbox",
        "--fsgofer-host-uds",
        "--overlay2=all:memory",
        "--file-access=exclusive",
        "--lisafs",
        "-fuse-overlayfs"
      ]
    }
  }
}
```

```yaml
# runsc configuration file
# /etc/runsc/config.toml
[runsc]
  # Network isolation
  network = "sandbox"
  
  # File system
  file-access = "exclusive"
  overlay2 = "all:memory"
  
  # Syscall filtering
  platform = "systrap"
  
  # Memory limit
  total-memory-limit = "1Gi"
  
  # CPU limit
  cpu-rate-limit = 100000
  
  # Logging
  debug = false
  log = "/var/log/runsc/"
  log-packets = false
```
## Firecracker microVM

### Firecracker Principles

Firecracker is a lightweight virtual machine monitor developed by AWS that provides hardware-level isolation:

```
Firecracker Architecture:

Traditional VM:
  Application → Guest OS → Hypervisor (KVM) → Host Kernel → Hardware
  
Firecracker microVM:
  Application → Slim Guest OS → Firecracker VMM → KVM → Host Kernel → Hardware

Features:
  - Boot time: ~125ms
  - Memory overhead: <5MB per microVM
  - Supports >4000 microVMs per host
  - Minimized attack surface (approximately 50K lines of Rust code)
```

### Firecracker Agent Sandbox

```python
import firectl
from firectl import FirecrackerClient

class FirecrackerAgentSandbox:
    """Agent sandbox based on Firecracker"""

    def __init__(self, socket_path: str):
        self.client = FirecrackerClient(socket_path)

    async def create_sandbox(
        self,
        agent_id: str,
        config: SandboxConfig,
    ) -> str:
        """Create a Firecracker microVM sandbox"""
        # Configure VM
        vm_config = {
            "boot-source": {
                "kernel_image_path": config.kernel_path,
                "boot_args": "console=ttyS0 reboot=k panic=1 pci=off",
            },
            "drives": [
                {
                    "drive_id": "rootfs",
                    "path_on_host": config.rootfs_path,
                    "is_root_device": True,
                    "is_read_only": True,
                },
            ],
            "machine-config": {
                "vcpu_count": config.vcpus,
                "mem_size_mib": config.memory_mb,
                "smt": False,
            },
            "network-interfaces": [
                {
                    "iface_id": "eth0",
                    "guest_mac": self._generate_mac(),
                    "host_dev_name": f"tap-{agent_id[:8]}",
                },
            ],
        }

        # Start microVM
        await self.client.create_vm(vm_config)

        # Configure cgroup limits
        await self._setup_cgroups(agent_id, config)

        return agent_id

    async def execute_in_sandbox(
        self,
        agent_id: str,
        command: str,
    ) -> ExecutionResult:
        """Execute a command inside the microVM"""
        # Execute command via API
        result = await self.client.api_put(
            f"/actions",
            {
                "action_type": "SendCtrlAltDel",
            },
        )
        return result

    async def _setup_cgroups(
        self,
        agent_id: str,
        config: SandboxConfig,
    ):
        """Configure cgroup resource limits"""
        cgroup_path = f"/sys/fs/cgroup/firecracker/{agent_id}"

        # CPU limit
        with open(f"{cgroup_path}/cpu.max", "w") as f:
            f.write(f"{config.cpu_quota} {config.cpu_period}")

        # Memory limit
        with open(f"{cgroup_path}/memory.max", "w") as f:
            f.write(str(config.memory_limit_bytes))

        # I/O limit
        with open(f"{cgroup_path}/io.max", "w") as f:
            f.write(f"8:0 rbps={config.read_bps} wbps={config.write_bps}")
```

### Kata Containers (Firecracker Integration)

```yaml
# K8s using Kata Containers (Firecracker backend)
apiVersion: v1
kind: Pod
metadata:
  name: agent-kata-sandbox
spec:
  runtimeClassName: kata-fc
  containers:
    - name: agent
      image: registry.example.com/agent-sandbox:latest
      resources:
        requests:
          cpu: "500m"
          memory: "512Mi"
        limits:
          cpu: "2"
          memory: "2Gi"
      securityContext:
        privileged: false
        runAsNonRoot: true
```

## E2B Cloud Sandbox

### E2B Overview

E2B (Environment to Build) provides managed cloud-based code execution sandboxes:

```python
from e2b_code_interpreter import Sandbox

class E2BAgentSandbox:
    """Agent code execution sandbox based on E2B"""

    def __init__(self, api_key: str):
        self.api_key = api_key

    async def execute_code(
        self,
        code: str,
        language: str = "python",
    ) -> ExecutionResult:
        """Execute code in an E2B sandbox"""
        sandbox = Sandbox(api_key=self.api_key)

        try:
            # Execute code
            execution = sandbox.run_code(code)

            return ExecutionResult(
                stdout=execution.logs.stdout,
                stderr=execution.logs.stderr,
                exit_code=execution.exit_code,
                artifacts=execution.results,
            )
        finally:
            sandbox.kill()

    async def execute_with_files(
        self,
        code: str,
        files: dict[str, bytes],
    ) -> ExecutionResult:
        """Upload files and execute in sandbox"""
        sandbox = Sandbox(api_key=self.api_key)

        try:
            # Upload files
            for filename, content in files.items():
                sandbox.files.write(filename, content)

            # Execute code
            execution = sandbox.run_code(code)

            # Download result files
            output_files = {}
            for path in sandbox.files.list("/workspace"):
                if path.endswith(".out") or path.endswith(".result"):
                    output_files[path] = sandbox.files.read(path)

            return ExecutionResult(
                stdout=execution.logs.stdout,
                stderr=execution.logs.stderr,
                exit_code=execution.exit_code,
                output_files=output_files,
            )
        finally:
            sandbox.kill()
```

### E2B Custom Templates

```dockerfile
# E2B custom sandbox template
# e2b.Dockerfile
FROM e2bdev/code-interpreter:latest

# Install additional dependencies
RUN pip install pandas numpy matplotlib scikit-learn

# Install Node.js
RUN apt-get update && apt-get install -y nodejs npm

# Copy custom tools
COPY tools/ /usr/local/bin/tools/

# Configure environment
ENV PYTHONUNBUFFERED=1
ENV E2B_TEMPLATE_ID="custom-agent-sandbox"
```
## Modal Serverless Sandbox

### Modal Overview

Modal provides a serverless code execution environment with GPU acceleration support:

```python
import modal

app = modal.App("agent-sandbox")

# Define sandbox image
sandbox_image = (
    modal.Image.debian_slim(python_version="3.11")
    .pip_install("pandas", "numpy", "scikit-learn")
    .apt_install("git")
)

@app.function(
    image=sandbox_image,
    timeout=300,
    cpu=2,
    memory=1024,
    # GPU support
    # gpu="A10G",
)
def execute_agent_code(code: str, context: dict) -> dict:
    """Execute Agent-generated code in a Modal sandbox"""
    import io
    import sys

    # Capture output
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = io.StringIO()
    sys.stderr = io.StringIO()

    try:
        # Inject context variables
        exec_globals = {"__builtins__": __builtins__}
        exec_globals.update(context)

        # Execute code
        exec(code, exec_globals)

        return {
            "stdout": sys.stdout.getvalue(),
            "stderr": sys.stderr.getvalue(),
            "exit_code": 0,
        }
    except Exception as e:
        return {
            "stdout": sys.stdout.getvalue(),
            "stderr": f"{type(e).__name__}: {str(e)}",
            "exit_code": 1,
        }
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr


# Modal Sandbox API (recommended)
@app.function()
async def run_in_sandbox(code: str) -> dict:
    """Use the Modal Sandbox API"""
    sb = modal.Sandbox.create(
        image=sandbox_image,
        timeout=300,
        cpu=2,
        memory=1024,
    )

    # Execute command
    process = sb.exec("python", "-c", code)

    return {
        "stdout": process.stdout.read(),
        "stderr": process.stderr.read(),
        "exit_code": process.wait(),
    }
```

## Code Execution Security Policies

### Static Code Analysis

```python
import ast
from typing import Optional

class CodeSafetyAnalyzer:
    """Static analyzer for code safety"""

    # Blocked modules
    BLOCKED_MODULES = {
        "os", "subprocess", "shutil", "sys",
        "socket", "http", "urllib", "requests",
        "ctypes", "importlib", "code",
        "compile", "exec", "eval",
    }

    # Blocked built-in functions
    BLOCKED_BUILTINS = {
        "exec", "eval", "compile",
        "__import__", "globals", "locals",
        "getattr", "setattr", "delattr",
    }

    # Dangerous AST node types
    DANGEROUS_NODE_TYPES = {
        ast.Import,
        ast.ImportFrom,
        ast.Exec,
        ast.Yield,  # May be used for generator-based attacks
    }

    def analyze(self, code: str) -> SafetyReport:
        """Analyze code safety"""
        try:
            tree = ast.parse(code)
        except SyntaxError as e:
            return SafetyReport(
                safe=False,
                violations=[f"Syntax error: {str(e)}"],
            )

        violations = []

        for node in ast.walk(tree):
            # Check imports
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name.split(".")[0] in self.BLOCKED_MODULES:
                        violations.append(
                            f"Blocked module import: {alias.name} (line {node.lineno})"
                        )

            if isinstance(node, ast.ImportFrom):
                if node.module and node.module.split(".")[0] in self.BLOCKED_MODULES:
                    violations.append(
                        f"Blocked from-module import: {node.module} (line {node.lineno})"
                    )

            # Check dangerous function calls
            if isinstance(node, ast.Call):
                if isinstance(node.func, ast.Name):
                    if node.func.id in self.BLOCKED_BUILTINS:
                        violations.append(
                            f"Blocked call: {node.func.id}() (line {node.lineno})"
                        )

            # Check attribute access
            if isinstance(node, ast.Attribute):
                if node.attr.startswith("__"):
                    violations.append(
                        f"Blocked magic attribute access: {node.attr} (line {node.lineno})"
                    )

        return SafetyReport(
            safe=len(violations) == 0,
            violations=violations,
        )
```

### Runtime Sandbox

```python
import resource
import signal

class RuntimeSandbox:
    """Runtime code execution sandbox"""

    def __init__(
        self,
        max_memory_mb: int = 256,
        max_cpu_seconds: int = 30,
        max_output_bytes: int = 1024 * 1024,
    ):
        self.max_memory_mb = max_memory_mb
        self.max_cpu_seconds = max_cpu_seconds
        self.max_output_bytes = max_output_bytes

    def execute(self, code: str, context: dict) -> ExecutionResult:
        """Execute code inside the sandbox"""
        import io
        import sys

        # Set resource limits
        self._set_resource_limits()

        # Set timeout signal
        signal.signal(signal.SIGALRM, self._timeout_handler)
        signal.alarm(self.max_cpu_seconds)

        # Capture output
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()

        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = stdout_capture
        sys.stderr = stderr_capture

        try:
            # Create a restricted namespace
            safe_builtins = self._create_safe_builtins()
            exec_globals = {"__builtins__": safe_builtins}
            exec_globals.update(context)

            # Execute code
            exec(code, exec_globals)

            return ExecutionResult(
                stdout=stdout_capture.getvalue()[:self.max_output_bytes],
                stderr=stderr_capture.getvalue()[:self.max_output_bytes],
                exit_code=0,
            )
        except TimeoutError:
            return ExecutionResult(
                stdout="",
                stderr="Execution timed out",
                exit_code=124,
            )
        except MemoryError:
            return ExecutionResult(
                stdout="",
                stderr="Memory limit exceeded",
                exit_code=137,
            )
        except Exception as e:
            return ExecutionResult(
                stdout=stdout_capture.getvalue(),
                stderr=f"{type(e).__name__}: {str(e)}",
                exit_code=1,
            )
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr
            signal.alarm(0)

    def _set_resource_limits(self):
        """Set system resource limits"""
        # Memory limit
        memory_bytes = self.max_memory_mb * 1024 * 1024
        resource.setrlimit(
            resource.RLIMIT_AS,
            (memory_bytes, memory_bytes),
        )

        # CPU time limit
        resource.setrlimit(
            resource.RLIMIT_CPU,
            (self.max_cpu_seconds, self.max_cpu_seconds),
        )

        # File size limit
        resource.setrlimit(
            resource.RLIMIT_FSIZE,
            (100 * 1024 * 1024, 100 * 1024 * 1024),  # 100MB
        )

    def _timeout_handler(self, signum, frame):
        raise TimeoutError("Execution timed out")

    def _create_safe_builtins(self) -> dict:
        """Create a safe set of built-in functions"""
        import builtins

        safe = {}
        allowed = [
            "abs", "all", "any", "bin", "bool", "chr", "dict",
            "divmod", "enumerate", "filter", "float", "format",
            "frozenset", "hash", "hex", "id", "int", "isinstance",
            "issubclass", "iter", "len", "list", "map", "max",
            "min", "next", "oct", "ord", "pow", "print", "range",
            "repr", "reversed", "round", "set", "slice", "sorted",
            "str", "sum", "tuple", "type", "zip",
        ]

        for name in allowed:
            if hasattr(builtins, name):
                safe[name] = getattr(builtins, name)

        return safe
```
## K8s Pod Security Standards

### PSS/PSA Configuration

```yaml
# Pod Security Standards - Restricted level
apiVersion: v1
kind: Namespace
metadata:
  name: agent-sandbox
  labels:
    pod-security.kubernetes.io/enforce: restricted
    pod-security.kubernetes.io/audit: restricted
    pod-security.kubernetes.io/warn: restricted
```

### NetworkPolicy

```yaml
# Agent network isolation policy
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: agent-network-policy
  namespace: agent-sandbox
spec:
  podSelector:
    matchLabels:
      app: agent-executor
  policyTypes:
    - Ingress
    - Egress
  ingress:
    # Allow inbound traffic only from API Gateway
    - from:
        - namespaceSelector:
            matchLabels:
              name: api-gateway
          podSelector:
            matchLabels:
              app: api-gateway
      ports:
        - port: 8080
          protocol: TCP
  egress:
    # Allow DNS queries
    - to:
        - namespaceSelector: {}
          podSelector:
            matchLabels:
              k8s-app: kube-dns
      ports:
        - port: 53
          protocol: UDP
        - port: 53
          protocol: TCP
    # Allow access to LLM API (restricted IP range)
    - to:
        - ipBlock:
            cidr: 0.0.0.0/0
            except:
              - 10.0.0.0/8      # Block access to internal network
              - 172.16.0.0/12
              - 192.168.0.0/16
      ports:
        - port: 443
          protocol: TCP
```

### SecurityContext Constraints

```yaml
# Fully hardened Pod template with security constraints
apiVersion: v1
kind: Pod
metadata:
  name: agent-hardened
  namespace: agent-sandbox
  annotations:
    container.apparmor.security.beta.kubernetes.io/agent: localhost/agent-sandbox
spec:
  automountServiceAccountToken: false
  hostNetwork: false
  hostPID: false
  hostIPC: false
  
  securityContext:
    runAsNonRoot: true
    runAsUser: 65534
    runAsGroup: 65534
    fsGroup: 65534
    seccompProfile:
      type: Localhost
      localhostProfile: profiles/agent-sandbox.json
  
  containers:
    - name: agent
      image: registry.example.com/agent-sandbox:latest@sha256:abc123...
      
      securityContext:
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop:
            - ALL
        seccompProfile:
          type: RuntimeDefault
      
      resources:
        requests:
          cpu: "250m"
          memory: "256Mi"
          ephemeral-storage: "1Gi"
        limits:
          cpu: "1"
          memory: "512Mi"
          ephemeral-storage: "5Gi"
      
      volumeMounts:
        - name: workspace
          mountPath: /workspace
        - name: tmp
          mountPath: /tmp
        - name: cache
          mountPath: /home/agent/.cache
      
      env:
        - name: PYTHONUNBUFFERED
          value: "1"
        - name: PYTHONPYCACHEPREFIX
          value: "/tmp/pycache"
      
      livenessProbe:
        httpGet:
          path: /health
          port: 8080
        initialDelaySeconds: 5
        periodSeconds: 10
      
      readinessProbe:
        httpGet:
          path: /ready
          port: 8080
        initialDelaySeconds: 5
        periodSeconds: 5
  
  volumes:
    - name: workspace
      emptyDir:
        sizeLimit: 1Gi
    - name: tmp
      emptyDir:
        medium: Memory
        sizeLimit: 100Mi
    - name: cache
      emptyDir:
        sizeLimit: 500Mi
```

---

*The agent sandbox is critical infrastructure for securely executing LLM-generated code; choosing the appropriate isolation level requires striking a balance between security, performance, and cost.*


<!-- risk-assessed -->
