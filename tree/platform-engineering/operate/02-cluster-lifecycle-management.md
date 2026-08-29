---
title: 69 - Lease & Leader Election Mechanism (Lease & Leader Election)
description: '## Lease Mechanism Architecture Overview'
summary: 'node.kubernetes.io/instance-type: ecs.g6.xlarge'
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- etcd
- apiserver
- kubelet
- scheduler
- controller-manager
- prometheus
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- platform engineers
- operations engineers
estimated_read_time: 5min
intent_queries:
- What is Lease & Leader Election Mechanism (Lease & Leader Election)
- How to use Lease & Leader Election Mechanism (Lease & Leader Election)
- Kubernetes 9 platform ops best practices
trigger_keywords:
- Lease
- Leader
- Election mechanism
- Lease
- Leader
- Election
- platform
- ops
prerequisites:
- kubectl-basics
- platform-engineering-basics
- prometheus-basics
- etcd-basics
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
authors:
- name: KUDIG Team
  role: contributor
cross_refs:
- type: domain
  path: ../domain-06-observability/
  label: 'Related knowledge domain: domain-06-observability'
- type: domain
  path: ../domain-15-specialized-tech/
  label: 'Related knowledge domain: domain-15-specialized-tech'
- type: domain
  path: ../domain-10-troubleshooting-diagnostics/
  label: 'Related knowledge domain: domain-10-troubleshooting-diagnostics'
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/operate/19-lease-leader-election.md
original_language: Chinese
---

> **Production Environment Security Notice**
>
> This document contains operations commands that can be executed directly. Before execution, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have tested it in a non-production environment. Command risk levels are marked as: 🔴 High risk (may cause data loss or service disruption), 🟡 Medium risk (modifies cluster state, but usually reversible), 🟢 Low risk/read-only (information collection, no side effects).




# 69 - Lease & Leader Election Mechanism (Lease & Leader Election)

> **Applicable versions**: v1.25 - v1.32 | **Last updated**: 2026-01 | **Difficulty**: Advanced

<!-- chunk: Lease Mechanism Architecture Overview -->
## Lease Mechanism Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                         Kubernetes Lease Mechanism Overview                         │
├─────────────────────────────────────────────────────────────────────────────────────┤
│                                                                                      │
│  ┌──────────────────────────────────────────────────────────────────────────────┐   │
│  │                          Lease Core Use Cases                                │   │
│  │                                                                               │   │
│  │  ┌─────────────────────┐  ┌─────────────────────┐  ┌───────────────────────┐ │   │
│  │  │   Leader Election   │  │    Node Heartbeat   │  │   Custom Coordination │ │   │
│  │  │                     │  │                     │  │                       │ │   │
│  │  │ • kube-controller   │  │ • kubelet heartbeat │  │ • distributed locks   │ │   │
│  │  │ • kube-scheduler    │  │ • node health       │  │ • task coordination   │ │   │
│  │  │ • cloud-controller  │  │ • 40s lease         │  │ • custom operators    │ │   │
│  │  │ • custom operators  │  │                     │  │                       │ │   │
│  │  └─────────────────────┘  └─────────────────────┘  └───────────────────────┘ │   │
│  └──────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  ┌──────────────────────────────────────────────────────────────────────────────┐   │
│  │                          Lease Workflow                                      │   │
│  │                                                                               │   │
│  │  ┌────────────┐    ┌────────────┐    ┌────────────┐    ┌────────────────┐   │   │
│  │  │  Acquire   │───▶│   Hold     │───▶│   Renew    │───▶│    Release     │   │   │
│  │  │   lease    │    │   lease    │    │    lease   │    │    lease       │   │   │
│  │  └────────────┘    └────────────┘    └────────────┘    └────────────────┘   │   │
│  │        │                 │                 │                  │             │   │
│  │        ▼                 ▼                 ▼                  ▼             │   │
│  │  ┌────────────┐    ┌────────────┐    ┌────────────┐    ┌────────────────┐   │   │
│  │  │ Create or  │    │  Execute   │    │  Update    │    │ Delete or      │   │   │
│  │  │  Update    │    │   Leader   │    │ renewTime  │    │ Let Expire     │   │   │
│  │  │ Lease Obj  │    │   Logic    │    │   Field    │    │                │   │   │
│  │  └────────────┘    └────────────┘    └────────────┘    └────────────────┘   │   │
│  └──────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
│  ┌──────────────────────────────────────────────────────────────────────────────┐   │
│  │                          Timeline Parameter Relationships                    │   │
│  │                                                                               │   │
│  │  |◄─────────────── LeaseDuration (15s) ──────────────►|                     │   │
│  │  |◄──── RenewDeadline (10s) ────►|                                          │   │
│  │  |◄── RetryPeriod (2s) ──►|                                                 │   │
│  │                                                                               │   │
│  │  Constraint: LeaseDuration > RenewDeadline > RetryPeriod × 2                │   │
│  │                                                                               │   │
│  └──────────────────────────────────────────────────────────────────────────────┘   │
│                                                                                      │
└─────────────────────────────────────────────────────────────────────────────────────┘
```

<!-- chunk: Lease Object Details -->
## Lease Object Details

### Lease Field Descriptions

| Field | Type | Description | Typical Value |
|-----|-----|------|--------|
| `spec.holderIdentity` | string | Current holder identity (usually Pod name) | `controller-manager-xxx` |
| `spec.leaseDurationSeconds` | int | Lease duration (seconds) | 15-40 |
| `spec.acquireTime` | MicroTime | Time lease was acquired | RFC3339 microseconds |
| `spec.renewTime` | MicroTime | Last renewal time | RFC3339 microseconds |
| `spec.leaseTransitions` | int | Number of lease transfers (Leader change count) | incrementing integer |

### System Lease Purpose Matrix

| Lease Name | Namespace | Purpose | Holder | Lease Duration |
|-------|---------|------|--------|---------|
| `kube-controller-manager` | kube-system | Controller manager leader election | CM Pod | 15s |
| `kube-scheduler` | kube-system | Scheduler leader election | Scheduler Pod | 15s |
| `cloud-controller-manager` | kube-system | Cloud controller leader election | CCM Pod | 15s |
| `<node-name>` | kube-node-lease | Node heartbeat | kubelet | 40s |
| `kube-apiserver-<id>` | kube-system | API Server identity (v1.26+) | API Server | 3600s |

### Complete Lease Object Example

```yaml
# Node heartbeat Lease
apiVersion: coordination.k8s.io/v1
kind: Lease
metadata:
  name: node-worker-1
  namespace: kube-node-lease
  ownerReferences:
    - apiVersion: v1
      kind: Node
      name: node-worker-1
      uid: abc123-def456
  labels:
    node.kubernetes.io/instance-type: ecs.g6.xlarge
spec:
  holderIdentity: node-worker-1
  leaseDurationSeconds: 40
  acquireTime: "2024-01-15T10:00:00.000000Z"
  renewTime: "2024-01-15T10:30:25.123456Z"
  leaseTransitions: 0
---
# Controller leader election Lease
apiVersion: coordination.k8s.io/v1
kind: Lease
metadata:
  name: kube-controller-manager
  namespace: kube-system
spec:
  holderIdentity: kube-controller-manager-master-1_abc123
  leaseDurationSeconds: 15
  acquireTime: "2024-01-15T08:00:00.000000Z"
  renewTime: "2024-01-15T10:30:22.456789Z"
  leaseTransitions: 3
```

<!-- chunk: Leader Election Parameter Details -->
## Leader Election Parameter Details

### Core Parameters

| Parameter | Default | Description | Tuning Suggestion |
|-----|-------|------|---------|
| `--leader-elect` | true | Enable leader election | Must be enabled in production |
| `--leader-elect-lease-duration` | 15s | Lease duration | Can increase for unstable networks |
| `--leader-elect-renew-deadline` | 10s | Renewal deadline | < leaseDuration |
| `--leader-elect-retry-period` | 2s | Retry interval | < renewDeadline/2 |
| `--leader-elect-resource-lock` | leases | Lock resource type | Keep default |
| `--leader-elect-resource-name` | component name | Lock resource name | Specify for custom components |
| `--leader-elect-resource-namespace` | kube-system | Lock resource namespace | Adjust as needed |

### Parameter Relationships and Constraints

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    Leader Election Time Parameter Relationships          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  LeaseDuration = 15s (lease validity period)                            │
│  ├── RenewDeadline = 10s (renewal must complete by this time)           │
│  │   └── RetryPeriod = 2s (renewal retry interval)                      │
│  │                                                                       │
│  Timeline:                                                               │
│  |←─────────────── LeaseDuration (15s) ───────────────→|                │
│  |←───── RenewDeadline (10s) ─────→|                   |                │
│  |←─ Retry ─→|←─ Retry ─→|←─ Retry ─→|←─ Retry ─→|    |                │
│  |   (2s)    |   (2s)    |   (2s)    |   (2s)    |    |                │
│  T0          T2          T4          T6          T8   T10  ...  T15     │
│  ↑           ↑           ↑           ↑           ↑         ↑           │
│  Acquire     Retry 1     Retry 2     Retry 3     Retry 4  Renewal      │
│  Lease                                            (last chance) failure │
│                                                                          │
│  Constraint Rules:                                                       │
│  1. LeaseDuration > RenewDeadline                                       │
│  2. RenewDeadline > RetryPeriod × 2                                     │
│  3. RetryPeriod should allow multiple retry opportunities               │
│                                                                          │
│  Recommended Configurations:                                            │
│  - Stable network: 15s / 10s / 2s (default)                            │
│  - Unstable network: 30s / 20s / 4s                                    │
│  - High availability: 10s / 8s / 2s (faster failover)                  │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

<!-- chunk: client-go Leader Election Implementation -->
## client-go Leader Election Implementation

### Complete Example Code

```go
package main

import (
    "context"
    "flag"
    "fmt"
    "os"
    "os/signal"
    "syscall"
    "time"

    "k8s.io/client-go/kubernetes"
    "k8s.io/client-go/rest"
    "k8s.io/client-go/tools/clientcmd"
    "k8s.io/client-go/tools/leaderelection"
    "k8s.io/client-go/tools/leaderelection/resourcelock"
    "k8s.io/klog/v2"
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
)

var (
    leaseLockName      = flag.String("lease-lock-name", "my-controller-lock", "lease lock name")
    leaseLockNamespace = flag.String("lease-lock-namespace", "default", "lease lock namespace")
    leaseDuration      = flag.Duration("lease-duration", 15*time.Second, "lease duration")
    renewDeadline      = flag.Duration("renew-deadline", 10*time.Second, "renewal deadline")
    retryPeriod        = flag.Duration("retry-period", 2*time.Second, "retry interval")
)

func main() {
    klog.InitFlags(nil)
    flag.Parse()

    // Get Pod identity
    id := os.Getenv("POD_NAME")
    if id == "" {
        hostname, _ := os.Hostname()
        id = hostname
    }
    
    klog.Infof("Starting leader election with identity: %s", id)

    // Create Kubernetes client
    config, err := getConfig()
    if err != nil {
        klog.Fatalf("Failed to get config: %v", err)
    }

    clientset, err := kubernetes.NewForConfig(config)
    if err != nil {
        klog.Fatalf("Failed to create clientset: %v", err)
    }

    // Create context to support graceful shutdown
    ctx, cancel := context.WithCancel(context.Background())
    defer cancel()

    // Listen for termination signals
    sigCh := make(chan os.Signal, 1)
    signal.Notify(sigCh, syscall.SIGINT, syscall.SIGTERM)
    go func() {
        sig := <-sigCh
        klog.Infof("Received signal %v, shutting down", sig)
        cancel()
    }()

    // Create Lease lock
    lock := &resourcelock.LeaseLock{
        LeaseMeta: metav1.ObjectMeta{
            Name:      *leaseLockName,
            Namespace: *leaseLockNamespace,
        },
        Client: clientset.CoordinationV1(),
        LockConfig: resourcelock.ResourceLockConfig{
            Identity: id,
        },
    }

    // Configure leader election
    leaderElectionConfig := leaderelection.LeaderElectionConfig{
        Lock:            lock,
        ReleaseOnCancel: true,  // Release lease when cancelled
        LeaseDuration:   *leaseDuration,
        RenewDeadline:   *renewDeadline,
        RetryPeriod:     *retryPeriod,
        Callbacks: leaderelection.LeaderCallbacks{
            OnStartedLeading: func(ctx context.Context) {
                klog.Info("Started leading - running controller logic")
                runController(ctx)
            },
            OnStoppedLeading: func() {
                klog.Info("Stopped leading")
                // Optional: cleanup resources or exit
                os.Exit(0)
            },
            OnNewLeader: func(identity string) {
                if identity == id {
                    klog.Info("Still the leader")
                    return
                }
                klog.Infof("New leader elected: %s", identity)
            },
        },
    }

    // Start leader election
    leaderelection.RunOrDie(ctx, leaderElectionConfig)
}

func getConfig() (*rest.Config, error) {
    // Prefer in-cluster config
    config, err := rest.InClusterConfig()
    if err == nil {
        return config, nil
    }

    // Fallback to kubeconfig
    kubeconfig := os.Getenv("KUBECONFIG")
    if kubeconfig == "" {
        kubeconfig = os.Getenv("HOME") + "/.kube/config"
    }
    return clientcmd.BuildConfigFromFlags("", kubeconfig)
}

func runController(ctx context.Context) {
    klog.Info("Controller is running...")
    
    ticker := time.NewTicker(5 * time.Second)
    defer ticker.Stop()

    for {
        select {
        case <-ctx.Done():
            klog.Info("Controller context cancelled, stopping")
            return
        case <-ticker.C:
            // Execute controller logic
            klog.Info("Performing controller work...")
            doWork()
        }
    }
}

func doWork() {
    // Actual controller work logic
    klog.Info("Processing work items...")
}
```

### controller-runtime Leader Election

```go
package main

import (
    "flag"
    "os"
    "time"

    "k8s.io/apimachinery/pkg/runtime"
    utilruntime "k8s.io/apimachinery/pkg/util/runtime"
    clientgoscheme "k8s.io/client-go/kubernetes/scheme"
    ctrl "sigs.k8s.io/controller-runtime"
    "sigs.k8s.io/controller-runtime/pkg/healthz"
    "sigs.k8s.io/controller-runtime/pkg/log/zap"
    "sigs.k8s.io/controller-runtime/pkg/manager"
)

var (
    scheme   = runtime.NewScheme()
    setupLog = ctrl.Log.WithName("setup")
)

func init() {
    utilruntime.Must(clientgoscheme.AddToScheme(scheme))
}

func main() {
    var (
        metricsAddr          string
        healthProbeAddr      string
        enableLeaderElection bool
        leaderElectionID     string
        leaseDuration        time.Duration
        renewDeadline        time.Duration
        retryPeriod          time.Duration
    )

    flag.StringVar(&metricsAddr, "metrics-addr", ":8080", "Metrics address")
    flag.StringVar(&healthProbeAddr, "health-probe-addr", ":8081", "Health check address")
    flag.BoolVar(&enableLeaderElection, "leader-elect", true, "Enable leader election")
    flag.StringVar(&leaderElectionID, "leader-election-id", "my-controller", "Leader election ID")
    flag.DurationVar(&leaseDuration, "lease-duration", 15*time.Second, "Lease duration")
    flag.DurationVar(&renewDeadline, "renew-deadline", 10*time.Second, "Renewal deadline")
    flag.DurationVar(&retryPeriod, "retry-period", 2*time.Second, "Retry interval")

    opts := zap.Options{Development: true}
    opts.BindFlags(flag.CommandLine)
    flag.Parse()

    ctrl.SetLogger(zap.New(zap.UseFlagOptions(&opts)))

    // Create Manager
    mgr, err := ctrl.NewManager(ctrl.GetConfigOrDie(), ctrl.Options{
        Scheme:                  scheme,
        MetricsBindAddress:      metricsAddr,
        HealthProbeBindAddress:  healthProbeAddr,
        
        // Leader election configuration
        LeaderElection:          enableLeaderElection,
        LeaderElectionID:        leaderElectionID,
        LeaderElectionNamespace: getLeaderElectionNamespace(),
        LeaseDuration:           &leaseDuration,
        RenewDeadline:           &renewDeadline,
        RetryPeriod:             &retryPeriod,
        
        // Leader election release configuration
        LeaderElectionReleaseOnCancel: true,
    })
    if err != nil {
        setupLog.Error(err, "unable to create manager")
        os.Exit(1)
    }

    // Register health checks
    if err := mgr.AddHealthzCheck("healthz", healthz.Ping); err != nil {
        setupLog.Error(err, "unable to set up health check")
        os.Exit(1)
    }
    if err := mgr.AddReadyzCheck("readyz", healthz.Ping); err != nil {
        setupLog.Error(err, "unable to set up ready check")
        os.Exit(1)
    }

    // Add leader election readiness check
    if err := mgr.AddReadyzCheck("leader-election", mgr.GetLeaderElectionElector().Check); err != nil {
        setupLog.Error(err, "unable to set up leader election ready check")
        os.Exit(1)
    }

    // Setup controllers
    if err := setupControllers(mgr); err != nil {
        setupLog.Error(err, "unable to setup controllers")
        os.Exit(1)
    }

    setupLog.Info("starting manager")
    if err := mgr.Start(ctrl.SetupSignalHandler()); err != nil {
        setupLog.Error(err, "problem running manager")
        os.Exit(1)
    }
}

func getLeaderElectionNamespace() string {
    // Prefer environment variable
    if ns := os.Getenv("LEADER_ELECTION_NAMESPACE"); ns != "" {
        return ns
    }
    // Try to get from ServiceAccount
    if data, err := os.ReadFile("/var/run/secrets/kubernetes.io/serviceaccount/namespace"); err == nil {
        return string(data)
    }
    return "default"
}

func setupControllers(mgr manager.Manager) error {
    // Register controllers
    // if err := (&MyReconciler{
    //     Client: mgr.GetClient(),
    //     Scheme: mgr.GetScheme(),
    // }).SetupWithManager(mgr); err != nil {
    //     return err
    // }
    return nil
}
```

<!-- chunk: Kubernetes Deployment Configuration -->
## Kubernetes Deployment Configuration

```yaml
# leader-election-deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-controller
  namespace: my-system
spec:
  replicas: 3  # Multiple replicas for high availability
  selector:
    matchLabels:
      app: my-controller
  template:
    metadata:
      labels:
        app: my-controller
    spec:
      serviceAccountName: my-controller
      containers:
        - name: controller
          image: my-controller:v1.0.0
          args:
            - --leader-elect=true
            - --leader-election-id=my-controller
            - --lease-duration=15s
            - --renew-deadline=10s
            - --retry-period=2s
            - --metrics-addr=:8080
            - --health-probe-addr=:8081
          env:
            - name: POD_NAME
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
            - name: LEADER_ELECTION_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
          ports:
            - name: metrics
              containerPort: 8080
            - name: health
              containerPort: 8081
          livenessProbe:
            httpGet:
              path: /healthz
              port: health
            initialDelaySeconds: 15
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /readyz
              port: health
            initialDelaySeconds: 5
            periodSeconds: 5
          resources:
            requests:
              cpu: 100m
              memory: 128Mi
            limits:
              cpu: 500m
              memory: 512Mi
      # Pod anti-affinity - distribute to different nodes
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              podAffinityTerm:
                labelSelector:
                  matchLabels:
                    app: my-controller
                topologyKey: kubernetes.io/hostname
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-controller
  namespace: my-system
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: my-controller-leader-election
  namespace: my-system
rules:
  # Permissions required for leader election
  - apiGroups: ["coordination.k8s.io"]
    resources: ["leases"]
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
  - apiGroups: [""]
    resources: ["events"]
    verbs: ["create", "patch"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: my-controller-leader-election
  namespace: my-system
subjects:
  - kind: ServiceAccount
    name: my-controller
    namespace: my-system
roleRef:
  kind: Role
  name: my-controller-leader-election
  apiGroup: rbac.authorization.k8s.io
```

<!-- chunk: Node Heartbeat Lease Mechanism -->
## Node Heartbeat Lease Mechanism

### kubelet Heartbeat Configuration

| kubelet Parameter | Default | Description | Tuning Suggestion |
|------------|-------|------|---------|
| `--node-lease-duration-seconds` | 40 | Node lease duration | Can increase for large clusters |
| `--node-status-update-frequency` | 10s | NodeStatus update frequency | Keep default or reduce |
| `--node-status-report-frequency` | 5m | Full status report frequency | Keep default |

### Node Heartbeat Workflow

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                         Node Heartbeat and Health Detection                      │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  kubelet                          kube-node-lease                API Server     │
│     │                                  │                             │          │
│     │  ─── Create/Update Lease ──────▶ │                             │          │
│     │       (every 10s)                │                             │          │
│     │                                  │                             │          │
│     │  ─── Update NodeStatus ──────────────────────────────────────▶ │          │
│     │       (every 10s, only on change)                              │          │
│     │                                  │                             │          │
│     │                                  │    node-lifecycle-controller │          │
│     │                                  │           │                  │          │
│     │                                  │  ◄─────── Check Lease ────── │          │
│     │                                  │           │                  │          │
│     │                                  │           ▼                  │          │
│     │                                  │    Lease.renewTime          │          │
│     │                                  │    + leaseDuration          │          │
│     │                                  │    < now()?                 │          │
│     │                                  │           │                  │          │
│     │                                  │     Yes   │   No            │          │
│     │                                  │     ┌─────┴─────┐           │          │
│     │                                  │     ▼           ▼           │          │
│     │                                  │  Mark Node    Node Healthy  │          │
│     │                                  │  NotReady                   │          │
│     │                                  │     │                       │          │
│     │                                  │     ▼                       │          │
│     │                                  │  Wait Grace Period          │          │
│     │                                  │  (pod-eviction-timeout)     │          │
│     │                                  │     │                       │          │
│     │                                  │     ▼                       │          │
│     │                                  │  Evict Pods                │          │
│     │                                  │                             │          │
└─────────────────────────────────────────────────────────────────────────────────┘

Time Parameters:
- Lease Duration: 40s (node lease validity period)
- Node Monitor Grace Period: 40s (node monitoring grace period)
- Pod Eviction Timeout: 5m (pod eviction timeout)

Determination Flow:
1. kubelet updates Lease.renewTime every 10s
2. node-lifecycle-controller checks: now() - renewTime > leaseDuration?
3. If timeout, mark node as NotReady
4. Evict pods after NotReady exceeds pod-eviction-timeout
```

<!-- chunk: Lease Monitoring and Alerting -->
## Lease Monitoring and Alerting

### Monitoring Commands

``` bash
# 🟢 Low risk: read-only/information collection, typically no side effects
# ==================== View Leases ====================

# View all Leases
kubectl get leases -A

# View node heartbeat Leases
kubectl get leases -n kube-node-lease

# View control plane leader election
kubectl get leases -n kube-system

# View specific Lease in detail
kubectl get lease kube-controller-manager -n kube-system -o yaml

# View Lease change history
kubectl get lease kube-scheduler -n kube-system -o jsonpath='{.spec.leaseTransitions}'

# ==================== Monitor Leader Status ====================

# View current Leader
kubectl get lease kube-controller-manager -n kube-system \
  -o jsonpath='{.spec.holderIdentity}'

# View last renewal time
kubectl get lease kube-controller-manager -n kube-system \
  -o jsonpath='{.spec.renewTime}'

# Batch view all control plane Leaders
for lease in kube-controller-manager kube-scheduler cloud-controller-manager; do
  echo "=== $lease ==="
  kubectl get lease $lease -n kube-system -o jsonpath=\
'{.spec.holderIdentity} (transitions: {.spec.leaseTransitions}, renewed: {.spec.renewTime})'
  echo
done

# ==================== Node Health Check ====================

# View renewal time for all node Leases
kubectl get leases -n kube-node-lease \
  -o custom-columns=NODE:.metadata.name,RENEWED:.spec.renewTime

# Find potentially unhealthy nodes (Lease not updated)
kubectl get leases -n kube-node-lease -o json | \
  jq -r '.items[] | select(
    (now - (.spec.renewTime | fromdateiso8601)) > 60
  ) | .metadata.name'
```
### [[Prometheus|Prometheus]] Monitoring Rules

```yaml
# prometheus-lease-rules.yaml
groups:
  - name: lease-monitoring
    interval: 30s
    rules:
      # Leader election transition count
      - record: kubernetes:leader_election:transitions_total
        expr: |
          max by (lease_name) (
            kube_lease_spec_lease_transitions{namespace="kube-system"}
          )

      # Lease expiration time
      - record: kubernetes:lease:time_until_expiry_seconds
        expr: |
          (
            kube_lease_spec_renew_time + 
            kube_lease_spec_lease_duration_seconds
          ) - time()

      # Leader election health check
      - alert: LeaderElectionLost
        expr: |
          changes(kube_lease_spec_holder_identity{namespace="kube-system"}[5m]) > 2
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Leader election switching frequently"
          description: "{{ $labels.lease_name }} switched Leader more than 2 times in 5 minutes"

      # Control plane Leader missing
      - alert: ControlPlaneLeaderMissing
        expr: |
          absent(kube_lease_spec_holder_identity{
            namespace="kube-system",
            lease_name=~"kube-controller-manager|kube-scheduler"
          })
        for: 1m
        labels:
          severity: critical
        annotations:
          summary: "Control plane Leader missing"
          description: "{{ $labels.lease_name }} has no Leader"

      # Node heartbeat timeout
      - alert: NodeHeartbeatTimeout
        expr: |
          (time() - kube_lease_spec_renew_time{namespace="kube-node-lease"}) 
          > kube_lease_spec_lease_duration_seconds{namespace="kube-node-lease"} * 1.5
        for: 2m
        labels:
          severity: warning
        annotations:
          summary: "Node heartbeat timeout"
          description: "Node {{ $labels.lease_name }} Lease not updated beyond 1.5x lease duration"

      # Large number of Leader transitions
      - alert: HighLeaderTransitionRate
        expr: |
          increase(kube_lease_spec_lease_transitions{namespace="kube-system"}[1h]) > 5
        for: 5m
        labels:
          severity: warning
        annotations:
          summary: "Leader transition frequency too high"
          description: "{{ $labels.lease_name }} transitioned {{ $value }} times in 1 hour"
```

<!-- chunk: Leader Election Troubleshooting -->
## Leader Election Troubleshooting

### Common Issue Diagnosis

| Issue | Symptoms | Troubleshooting | Solution |
|-----|------|---------|---------|
| **Split-brain** | Two instances working simultaneously | Check NTP sync, network partitions | Fix time sync, check network |
| **No leader** | No instance performing work | Check API Server connection, RBAC | Fix network, check permissions |
| **Frequent switching** | Leader changing frequently | Check network stability, resources | Increase lease duration, optimize network |
| **Renewal failure** | Leader lost unexpectedly | Check API Server load | Scale API Server, optimize parameters |
| **Election timeout** | Slow new Leader election | Check etcd performance | Optimize etcd, adjust parameters |

### Troubleshooting Script

``` bash
# 🟢 Low risk: read-only/information collection, typically no side effects
#!/bin/bash
# lease-troubleshoot.sh

echo "=== Control Plane Leader Status ==="
for component in kube-controller-manager kube-scheduler cloud-controller-manager; do
  echo "--- $component ---"
  kubectl get lease $component -n kube-system -o jsonpath=\
'Holder: {.spec.holderIdentity}
Transitions: {.spec.leaseTransitions}
Renewed: {.spec.renewTime}
Duration: {.spec.leaseDurationSeconds}s
' 2>/dev/null || echo "Not found"
  echo
done

echo "=== Node Lease Status ==="
kubectl get leases -n kube-node-lease \
  -o custom-columns=\
'NODE:.metadata.name,RENEWED:.spec.renewTime,DURATION:.spec.leaseDurationSeconds'

echo ""
echo "=== Potentially Unhealthy Nodes (Lease not updated > 60s) ==="
kubectl get leases -n kube-node-lease -o json | \
  jq -r '.items[] | select(
    (now - (.spec.renewTime | fromdateiso8601)) > 60
  ) | "\(.metadata.name): \(now - (.spec.renewTime | fromdateiso8601) | floor)s ago"'

echo ""
echo "=== Recent Leader Change Events ==="
kubectl get events -n kube-system \
  --field-selector reason=LeaderElection \
  --sort-by='.lastTimestamp' \
  | tail -10

echo ""
echo "=== NTP Sync Status ==="
for node in $(kubectl get nodes -o jsonpath='{.items[*].metadata.name}'); do
  echo "--- $node ---"
  kubectl debug node/$node -it --image=busybox -- \
    /bin/sh -c "ntpq -p 2>/dev/null || echo 'NTP check not available'" &
done
wait
```
<!-- chunk: Lease Best Practices -->
## Lease Best Practices

### Parameter Tuning Recommendations

| Scenario | LeaseDuration | RenewDeadline | RetryPeriod | Description |
|-----|---------------|---------------|-------------|------|
| **Default** | 15s | 10s | 2s | Standard configuration |
| **High availability** | 10s | 8s | 2s | Faster failover |
| **Unstable network** | 30s | 20s | 4s | Tolerates network jitter |
| **Large-scale cluster** | 60s | 40s | 5s | Reduces API pressure |
| **Edge scenarios** | 120s | 90s | 10s | High latency networks |

### Best Practices Checklist

- [ ] **Enable Leader Election**: Must be enabled in production
- [ ] **Set Timeouts Reasonably**: LeaseDuration > RenewDeadline > RetryPeriod × 2
- [ ] **NTP Time Sync**: Ensure cluster node time is synchronized
- [ ] **Monitor Transitions**: Watch the leaseTransitions metric
- [ ] **Graceful Shutdown**: Configure ReleaseOnCancel=true
- [ ] **Unique Identity**: Use Pod name as identity
- [ ] **Pod Anti-affinity**: Distribute multiple replicas to different nodes
- [ ] **Health Checks**: Configure liveness/readiness probes
- [ ] **RBAC Permissions**: Principle of least privilege
- [ ] **Alert Configuration**: Monitor Leader switching and heartbeats

<!-- chunk: Version Change Log -->
## Version Change Log

| Version | Changes |
|------|---------|
| v1.14 | Node Lease GA |
| v1.17 | Lease becomes default leader election resource |
| v1.20 | Endpoints no longer used for election |
| v1.26 | API Server Identity Lease |
| v1.27 | Lease optimization, reduced API calls |
| v1.29 | Finer-grained Lease monitoring metrics |

---

**Table Footer Attribution**: Kusheet Project, author Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian Related Documentation -->
## Obsidian Related Documentation

- domain-07-platform-engineering MOC
- [[domain-07-platform-engineering/README.md|Platform Ops Domain (Platform Operations Domain)]]
- Domain-9 Platform Operations — Open Source Project Index
- Platform Operations Overview
- Cluster Lifecycle Management
- Capacity Planning & Resource Assessment
- Performance Benchmarking & Tuning
- Operations Metrics System
- Monitoring and Alerting System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization & FinOps Practice

## See Also

- 17-multi-tenant-management
- 18-platform-observability-practice
- 20-crd-operator-development
- 21-api-aggregation

## Related

- [[domain-19-landscape-references/topic-index/etcd-index.md|etcd Knowledge Graph Index]]


<!-- risk-assessed -->