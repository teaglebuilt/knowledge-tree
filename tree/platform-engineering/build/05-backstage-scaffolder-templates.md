---
title: 31 - CRD and Operator Development
description: 'storage: false  # Not the storage version'
summary: 'storage: false  # Not the storage version'
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- prometheus
- helm
- docker
- rbac
- crd
- operator
tier: peripheral
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
- What is CRD and Operator development
- How to develop CRD and Operator
- Kubernetes 9 platform ops best practices
trigger_keywords:
- CRD and Operator development
- platform
- ops
prerequisites:
- kubectl-basics
- platform-engineering-basics
- helm-basics
- prometheus-basics
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
  label: 'Related Knowledge Domain: domain-06-observability'
- type: domain
  path: ../domain-15-specialized-tech/
  label: 'Related Knowledge Domain: domain-15-specialized-tech'
- type: domain
  path: ../domain-10-troubleshooting-diagnostics/
  label: 'Related Knowledge Domain: domain-10-troubleshooting-diagnostics'
- type: fta
  path: ../domain-10-troubleshooting-diagnostics/topic-fta/list/crd-operator-fta.md
  label: 'Fault Tree: crd-operator'
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./build/20-crd-operator-development.md
original_language: Chinese
---

> **Production Environment Security Reminder**
>
> This document contains directly executable operations commands. Before execution, please confirm: is the current target cluster and Namespace correct; do you have sufficient RBAC permissions; has it been verified in a non-production environment. Command risk levels are marked: 🔴 High Risk (may cause data loss or service disruption), 🟡 Medium Risk (will modify cluster state, but usually reversible), 🟢 Low Risk/Read-only (information gathering, no side effects).




# 31 - CRD and Operator Development

> **Applicable Versions**: v1.25 - v1.32 | **Last Updated**: 2026-01 | **Reference**: [[entities/kubernetes.md|kubernetes]].io/docs/concepts/extend-kubernetes/api-extension/custom-resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)

<!-- chunk: CRD Version Specifications -->
## CRD Version Specifications

| API Version | Status | Features | K8s Version |
|--------|-----|------|--------|
| apiextensions.k8s.io/v1beta1 | Removed | Basic CRD | Before v1.22 |
| apiextensions.k8s.io/v1 | Stable | Full Features | v1.16+ |

<!-- chunk: CRD Structure Definition -->
## CRD Structure Definition

| Field | Type | Required | Description |
|-----|-----|-----|------|
| `spec.group` | string | ✅ | API Group Name |
| `spec.names.kind` | string | ✅ | Resource Type |
| `spec.names.plural` | string | ✅ | Plural Name |
| `spec.names.singular` | string | ❌ | Singular Name |
| `spec.names.shortNames` | []string | ❌ | Short Names |
| `spec.scope` | Namespaced/Cluster | ✅ | Scope |
| `spec.versions` | []Version | ✅ | Version List |
| `spec.conversion` | Conversion | ❌ | Version Conversion |

<!-- chunk: CRD Validation Rules -->
## CRD Validation Rules

| Validation Type | Field | Example |
|---------|-----|------|
| Required Fields | `required` | `required: [name, replicas]` |
| Type Validation | `type` | `type: string` |
| Enum Values | `enum` | `enum: [Running, Stopped]` |
| Numeric Range | `minimum/maximum` | `minimum: 1, maximum: 100` |
| String Length | `minLength/maxLength` | `minLength: 1` |
| Regex Matching | `pattern` | `pattern: "^[a-z]+$"` |
| Array Length | `minItems/maxItems` | `minItems: 1` |
| Default Value | `default` | `default: 3` |
| CEL Validation | `x-kubernetes-validations` | Custom Validation (v1.25+) |

<!-- chunk: CRD Example -->
## CRD Example

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: applications.app.example.com
  annotations:
    controller-gen.kubebuilder.io/version: v0.14.0
spec:
  group: app.example.com
  names:
    kind: Application
    plural: applications
    singular: application
    shortNames: [app]
    categories: [all]  # kubectl get all can see this
  scope: Namespaced
  versions:
  - name: v1
    served: true
    storage: true
    schema:
      openAPIV3Schema:
        type: object
        required: [spec]
        properties:
          spec:
            type: object
            required: [image, replicas]
            properties:
              image:
                type: string
                pattern: "^[a-z0-9.-]+/[a-z0-9.-]+:[a-z0-9.-]+$"
              replicas:
                type: integer
                minimum: 1
                maximum: 100
                default: 1
              ports:
                type: array
                maxItems: 10
                items:
                  type: object
                  required: [port]
                  properties:
                    port:
                      type: integer
                      minimum: 1
                      maximum: 65535
                    protocol:
                      type: string
                      enum: [TCP, UDP]
                      default: TCP
              resources:
                type: object
                properties:
                  cpu:
                    type: string
                    pattern: "^[0-9]+m?$"
                  memory:
                    type: string
                    pattern: "^[0-9]+(Mi|Gi)$"
            # CEL Validation Rules (v1.25+)
            x-kubernetes-validations:
            - rule: "self.replicas <= 10 || has(self.highAvailability)"
              message: "replicas > 10 requires highAvailability config"
            - rule: "!has(self.resources) || (has(self.resources.cpu) && has(self.resources.memory))"
              message: "if resources specified, both cpu and memory required"
          status:
            type: object
            properties:
              phase:
                type: string
                enum: [Pending, Running, Failed, Succeeded]
              availableReplicas:
                type: integer
              conditions:
                type: array
                items:
                  type: object
                  required: [type, status]
                  properties:
                    type:
                      type: string
                    status:
                      type: string
                      enum: ["True", "False", "Unknown"]
                    reason:
                      type: string
                    message:
                      type: string
                    lastTransitionTime:
                      type: string
                      format: date-time
    subresources:
      status: {}
      scale:
        specReplicasPath: .spec.replicas
        statusReplicasPath: .status.availableReplicas
    additionalPrinterColumns:
    - name: Replicas
      type: integer
      jsonPath: .spec.replicas
    - name: Available
      type: integer
      jsonPath: .status.availableReplicas
    - name: Phase
      type: string
      jsonPath: .status.phase
    - name: Age
      type: date
      jsonPath: .metadata.creationTimestamp
  # Version Conversion
  conversion:
    strategy: Webhook
    webhook:
      clientConfig:
        service:
          namespace: system
          name: webhook-service
          path: /convert
      conversionReviewVersions: ["v1"]
```

<!-- chunk: CRD Version Conversion -->
## CRD Version Conversion

```yaml
# Multi-version CRD Example
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: databases.db.example.com
spec:
  group: db.example.com
  names:
    kind: Database
    plural: databases
  scope: Namespaced
  versions:
  - name: v1
    served: true
    storage: false  # Not the storage version
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              size:
                type: string  # v1 uses string
  - name: v2
    served: true
    storage: true   # v2 is the storage version
    schema:
      openAPIV3Schema:
        type: object
        properties:
          spec:
            type: object
            properties:
              storageSize:
                type: integer  # v2 changed to integer (Gi)
              storageClass:
                type: string
  conversion:
    strategy: Webhook
    webhook:
      clientConfig:
        service:
          namespace: system
          name: conversion-webhook
          path: /convert
      conversionReviewVersions: ["v1"]
```

<!-- chunk: Operator Development Framework Comparison -->
## Operator Development Framework Comparison

| Framework | Language | Learning Curve | Features | Community Activity | Use Cases |
|-----|-----|---------|-----|-----------|---------|
| **Kubebuilder** | Go | Medium | Complete | ⭐⭐⭐⭐⭐ | Production-grade Operator |
| **Operator SDK** | Go/Ansible/Helm | Medium | Complete | ⭐⭐⭐⭐⭐ | Multi-language support |
| **controller-runtime** | Go | High | Low-level | ⭐⭐⭐⭐⭐ | Highly customizable |
| **KUDO** | YAML | Low | Basic | ⭐⭐⭐ | Simple stateful applications |
| **Metacontroller** | JS/Python | Low | Basic | ⭐⭐⭐ | Rapid prototyping |
| **kopf** | Python | Low | Medium | ⭐⭐⭐⭐ | Python ecosystem |
| **Java Operator SDK** | Java | Medium | Complete | ⭐⭐⭐⭐ | Java ecosystem |

<!-- chunk: Kubebuilder Development Workflow -->
## Kubebuilder Development Workflow

``` bash
# 🟢 Low Risk: Read-only/Information gathering, typically no side effects
# 1. Initialize project
kubebuilder init --domain example.com --repo github.com/example/app-operator

# 2. Create API
kubebuilder create api --group app --version v1 --kind Application
# Choose to create Resource and Controller

# 3. Create Webhook (optional)
kubebuilder create webhook --group app --version v1 --kind Application \
  --defaulting --programmatic-validation

# 4. Edit type definitions
# api/v1/application_types.go

# 5. Generate code and manifests
make generate    # Generate DeepCopy, etc.
make manifests   # Generate CRD/RBAC/Webhook

# 6. Install CRD
make install

# 7. Run locally for testing
make run

# 8. Build and deploy
make docker-build docker-push IMG=<registry>/app-operator:v1
make deploy IMG=<registry>/app-operator:v1

# 9. Uninstall
make undeploy
make uninstall
```
<!-- chunk: Controller Core Code Structure -->
## Controller Core Code Structure

```go
// internal/controller/application_controller.go
package controller

import (
    "context"
    "fmt"
    "time"

    appsv1 "k8s.io/api/apps/v1"
    corev1 "k8s.io/api/core/v1"
    "k8s.io/apimachinery/pkg/api/errors"
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "k8s.io/apimachinery/pkg/runtime"
    ctrl "sigs.k8s.io/controller-runtime"
    "sigs.k8s.io/controller-runtime/pkg/client"
    "sigs.k8s.io/controller-runtime/pkg/controller/controllerutil"
    "sigs.k8s.io/controller-runtime/pkg/log"

    appv1 "github.com/example/app-operator/api/v1"
)

const applicationFinalizer = "app.example.com/finalizer"

type ApplicationReconciler struct {
    client.Client
    Scheme *runtime.Scheme
}

// +kubebuilder:rbac:groups=app.example.com,resources=applications,verbs=get;list;watch;create;update;patch;delete
// +kubebuilder:rbac:groups=app.example.com,resources=applications/status,verbs=get;update;patch
// +kubebuilder:rbac:groups=app.example.com,resources=applications/finalizers,verbs=update
// +kubebuilder:rbac:groups=apps,resources=deployments,verbs=get;list;watch;create;update;patch;delete

func (r *ApplicationReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    logger := log.FromContext(ctx)

    // 1. Get CR
    app := &appv1.Application{}
    if err := r.Get(ctx, req.NamespacedName, app); err != nil {
        if errors.IsNotFound(err) {
            return ctrl.Result{}, nil
        }
        return ctrl.Result{}, err
    }

    // 2. Handle deletion
    if !app.DeletionTimestamp.IsZero() {
        if controllerutil.ContainsFinalizer(app, applicationFinalizer) {
            // Execute cleanup logic
            if err := r.cleanup(ctx, app); err != nil {
                return ctrl.Result{}, err
            }
            // Remove finalizer
            controllerutil.RemoveFinalizer(app, applicationFinalizer)
            if err := r.Update(ctx, app); err != nil {
                return ctrl.Result{}, err
            }
        }
        return ctrl.Result{}, nil
    }

    // 3. Add finalizer
    if !controllerutil.ContainsFinalizer(app, applicationFinalizer) {
        controllerutil.AddFinalizer(app, applicationFinalizer)
        if err := r.Update(ctx, app); err != nil {
            return ctrl.Result{}, err
        }
    }

    // 4. Sync Deployment
    deployment := r.constructDeployment(app)
    if err := controllerutil.SetControllerReference(app, deployment, r.Scheme); err != nil {
        return ctrl.Result{}, err
    }

    found := &appsv1.Deployment{}
    err := r.Get(ctx, client.ObjectKeyFromObject(deployment), found)
    if err != nil && errors.IsNotFound(err) {
        logger.Info("Creating Deployment", "name", deployment.Name)
        if err := r.Create(ctx, deployment); err != nil {
            return ctrl.Result{}, err
        }
    } else if err == nil {
        // Update Deployment
        if err := r.Update(ctx, deployment); err != nil {
            return ctrl.Result{}, err
        }
    } else {
        return ctrl.Result{}, err
    }

    // 5. Update status
    app.Status.Phase = "Running"
    app.Status.AvailableReplicas = found.Status.AvailableReplicas
    if err := r.Status().Update(ctx, app); err != nil {
        return ctrl.Result{}, err
    }

    // 6. Return result
    return ctrl.Result{RequeueAfter: 30 * time.Second}, nil
}

func (r *ApplicationReconciler) SetupWithManager(mgr ctrl.Manager) error {
    return ctrl.NewControllerManagedBy(mgr).
        For(&appv1.Application{}).
        Owns(&appsv1.Deployment{}).
        Complete(r)
}
```

<!-- chunk: Reconcile Pattern Deep Analysis -->
## Reconcile Pattern Deep Analysis

### Reconcile Triggering Mode Comparison

| Mode | Description | Trigger Condition | Use Cases | Pros/Cons |
|-----|------|---------|---------|--------|
| **Level-triggered** | Based on difference between desired and actual state | Watch events/Requeue | Most scenarios (recommended default) | ✅ Naturally idempotent ❌ Potentially redundant computation |
| **Edge-triggered** | Triggered only on state change edge | Event filtering Predicate | High-frequency events but few need handling | ✅ Reduce invalid reconciliation ❌ May miss state |
| **Periodic Sync** | Periodically enforce reconciliation | RequeueAfter timer | External resource sync/drift detection | ✅ Prevent drift ❌ Increase API pressure |
| **Hybrid Mode** | Event-driven + Periodic fallback | Watch + timer | Production-grade high-reliability scenarios | ✅ Highest reliability ❌ High complexity |

### Level-triggered vs Edge-triggered

```
┌─────────────── Level-triggered (Recommended) ───────────────┐
│                                                       │
│  Desired State (Spec) ─────┐                                │
│                       ├─→ Diff → Apply → Actual State     │
│  Actual State (Status) ───┘                                │
│                                                       │
│  Characteristics: Completely compare desired and actual state on each Reconcile      │
│  Advantage: Naturally supports idempotency, can self-heal even if events are missed                  │
│  Disadvantage: Each time requires complete state reading and comparison                  │
└───────────────────────────────────────────────────────┘

┌─────────────── Edge-triggered ───────────────────────┐
│                                                       │
│  Event(Create/Update/Delete) → Filter → Reconcile     │
│                                                       │
│  Characteristics: Trigger Reconcile only on specific events                │
│  Advantage: Reduce unnecessary processing, suitable for high-frequency event scenarios              │
│  Disadvantage: May cause state inconsistency due to event loss                    │
│  Remediation: Must be combined with periodic Requeue for fallback                         │
└───────────────────────────────────────────────────────┘
```

### Predicate Event Filtering (Edge-triggered Implementation)

```go
// Custom Predicate filter
func (r *ApplicationReconciler) SetupWithManager(mgr ctrl.Manager) error {
    return ctrl.NewControllerManagedBy(mgr).
        For(&appv1.Application{}, builder.WithPredicates(
            predicate.Or(
                predicate.GenerationChangedPredicate{}, // Only trigger on Spec changes
                predicate.AnnotationChangedPredicate{}, // Trigger on annotation changes
            ),
        )).
        Owns(&appsv1.Deployment{}, builder.WithPredicates(
            predicate.Funcs{
                CreateFunc: func(e event.CreateEvent) bool { return true },
                UpdateFunc: func(e event.UpdateEvent) bool {
                    // Trigger only when Ready replicas count changes
                    oldDep := e.ObjectOld.(*appsv1.Deployment)
                    newDep := e.ObjectNew.(*appsv1.Deployment)
                    return oldDep.Status.ReadyReplicas != newDep.Status.ReadyReplicas
                },
                DeleteFunc:  func(e event.DeleteEvent) bool { return true },
                GenericFunc: func(e event.GenericEvent) bool { return false },
            },
        )).
        // Monitor external resource changes (e.g., ConfigMap changes trigger related CR re-reconciliation)
        Watches(
            &corev1.ConfigMap{},
            handler.EnqueueRequestsFromMapFunc(r.findApplicationsForConfigMap),
            builder.WithPredicates(predicate.ResourceVersionChangedPredicate{}),
        ).
        WithOptions(controller.Options{
            MaxConcurrentReconciles: 5,
            RateLimiter: workqueue.NewMaxOfRateLimiter(
                workqueue.NewItemExponentialFailureRateLimiter(200*time.Millisecond, 1000*time.Second),
                &workqueue.BucketRateLimiter{Limiter: rate.NewLimiter(rate.Limit(10), 100)},
            ),
        }).
        Complete(r)
}

// Cross-resource association lookup
func (r *ApplicationReconciler) findApplicationsForConfigMap(
    ctx context.Context, obj client.Object,
) []reconcile.Request {
    configMap := obj.(*corev1.ConfigMap)
    var apps appv1.ApplicationList
    if err := r.List(ctx, &apps, client.InNamespace(configMap.Namespace),
        client.MatchingLabels{"config-ref": configMap.Name}); err != nil {
        return nil
    }
    requests := make([]reconcile.Request, len(apps.Items))
    for i, app := range apps.Items {
        requests[i] = reconcile.Request{
            NamespacedName: types.NamespacedName{Name: app.Name, Namespace: app.Namespace},
        }
    }
    return requests
}
```

### Periodic Sync and Hybrid Mode

```go
func (r *ApplicationReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    // ... Core reconciliation logic ...

    // Hybrid mode: Event-driven + Periodic fallback
    // Normally re-enqueue after 30 seconds for drift detection
    // If there's an error, use exponential backoff retry
    if reconcileErr != nil {
        // Error retry: Don't set RequeueAfter, let RateLimiter control backoff interval
        return ctrl.Result{}, reconcileErr
    }
    // After success, periodically reconcile to detect external system drift
    return ctrl.Result{RequeueAfter: 30 * time.Second}, nil
}
```

<!-- chunk: Operator Production-grade Best Practices -->
## Operator Production-grade Best Practices

### Core Practice Quick Reference Table

| Practice | Level | Description | Key Implementation |
|-----|------|------|----------|
| **Idempotency** | 🔴Required | Reconcile must be idempotent, consistent results across multiple executions | CreateOrUpdate / SSA |
| **State Management** | 🔴Required | Use Status subresource, separate spec/status updates | `r.Status().Update()` |
| **Ownership Management** | 🔴Required | Set OwnerReferences to implement cascading deletion | `SetControllerReference()` |
| **[[Finalizers\|Finalizers]]** | 🔴Required | Clean up external resources before deletion | Add/Remove Finalizer |
| **Condition Status** | 🔴Required | Use Conditions to standardize status reporting | `meta.SetStatusCondition()` |
| **Event Recording** | 🟡Recommended | Send K8s Events to record key operations | `recorder.Eventf()` |
| **Retry Strategy** | 🟡Recommended | Exponential backoff retry for failed operations | RateLimiter configuration |
| **Concurrency Control** | 🟡Recommended | Limit concurrent Reconcile count | `MaxConcurrentReconciles` |
| **Monitoring Metrics** | 🟡Recommended | Expose Prometheus custom metrics | controller-runtime metrics |
| **Graceful Shutdown** | 🟡Recommended | Leader election + graceful exit | `LeaderElection: true` |
| **SSA Patch** | 🟢Suggested | Server-Side Apply reduces conflicts | `Patch(SSA)` |
| **Cache Optimization** | 🟢Suggested | Optional caching reduces memory | `cache.ByObject` |

### 1. Idempotency Guarantee

```go
// ✅ Correct: Use CreateOrUpdate to ensure idempotency
func (r *ApplicationReconciler) reconcileDeployment(
    ctx context.Context, app *appv1.Application,
) error {
    deployment := &appsv1.Deployment{
        ObjectMeta: metav1.ObjectMeta{
            Name:      app.Name,
            Namespace: app.Namespace,
        },
    }
    
    op, err := controllerutil.CreateOrUpdate(ctx, r.Client, deployment, func() error {
        // mutate function: Only set desired state, regardless of current state
        deployment.Spec.Replicas = &app.Spec.Replicas
        deployment.Spec.Selector = &metav1.LabelSelector{
            MatchLabels: map[string]string{"app": app.Name},
        }
        deployment.Spec.Template = corev1.PodTemplateSpec{
            ObjectMeta: metav1.ObjectMeta{
                Labels: map[string]string{"app": app.Name},
            },
            Spec: corev1.PodSpec{
                Containers: []corev1.Container{{
                    Name:  "main",
                    Image: app.Spec.Image,
                }},
            },
        }
        return controllerutil.SetControllerReference(app, deployment, r.Scheme)
    })
    if err != nil {
        return fmt.Errorf("CreateOrUpdate Deployment failed: %w", err)
    }
    
    log.FromContext(ctx).Info("Deployment reconciled", "operation", op)
    return nil
}

// ✅ Recommended: Use Server-Side Apply (SSA) to achieve conflict-free idempotency
func (r *ApplicationReconciler) reconcileDeploymentSSA(
    ctx context.Context, app *appv1.Application,
) error {
    deployment := &appsv1.Deployment{
        TypeMeta: metav1.TypeMeta{APIVersion: "apps/v1", Kind: "Deployment"},
        ObjectMeta: metav1.ObjectMeta{
            Name:      app.Name,
            Namespace: app.Namespace,
        },
        Spec: appsv1.DeploymentSpec{
            Replicas: &app.Spec.Replicas,
            // ... Complete desired state
        },
    }
    // SSA: Fields identified by fieldManager are managed by this controller
    return r.Patch(ctx, deployment, client.Apply,
        client.FieldOwner("application-controller"),
        client.ForceOwnership,
    )
}

// ❌ Wrong: Non-idempotent implementation
// func reconcile() {
//     deployment.Spec.Replicas++ // Increments on each call, not idempotent!
// }
```

### 2. State Management and Conditions

```go
import "k8s.io/apimachinery/pkg/api/meta"

// Standardized Condition update
func (r *ApplicationReconciler) updateCondition(
    ctx context.Context, app *appv1.Application,
    condType string, status metav1.ConditionStatus,
    reason, message string,
) error {
    meta.SetStatusCondition(&app.Status.Conditions, metav1.Condition{
        Type:               condType,
        Status:             status,
        ObservedGeneration: app.Generation,  // Key: Record observed Generation
        Reason:             reason,
        Message:            message,
        LastTransitionTime: metav1.Now(),
    })
    return r.Status().Update(ctx, app)
}

// Complete Reconcile state management flow
func (r *ApplicationReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    app := &appv1.Application{}
    if err := r.Get(ctx, req.NamespacedName, app); err != nil {
        return ctrl.Result{}, client.IgnoreNotFound(err)
    }
    
    // Use defer to ensure status is always updated (even if error occurs)
    var reconcileErr error
    defer func() {
        if reconcileErr != nil {
            r.updateCondition(ctx, app, "Ready",
                metav1.ConditionFalse, "ReconcileFailed", reconcileErr.Error())
            r.updateCondition(ctx, app, "Progressing",
                metav1.ConditionFalse, "Error", reconcileErr.Error())
        } else {
            r.updateCondition(ctx, app, "Ready",
                metav1.ConditionTrue, "ReconcileSuccess", "All resources synced")
            r.updateCondition(ctx, app, "Progressing",
                metav1.ConditionFalse, "Synced", "Desired state achieved")
        }
    }()
    
    // Core reconciliation logic...
    reconcileErr = r.reconcileResources(ctx, app)
    if reconcileErr != nil {
        return ctrl.Result{}, reconcileErr
    }
    return ctrl.Result{RequeueAfter: 30 * time.Second}, nil
}
```

### 3. Finalizer Production-grade Implementation

```go
const applicationFinalizer = "app.example.com/cleanup"

func (r *ApplicationReconciler) handleFinalizerAndDeletion(
    ctx context.Context, app *appv1.Application,
) (ctrl.Result, bool, error) {
    logger := log.FromContext(ctx)
    
    // Resource is being deleted
    if !app.DeletionTimestamp.IsZero() {
        if controllerutil.ContainsFinalizer(app, applicationFinalizer) {
            logger.Info("Executing finalizer cleanup")
            
            // Set status to Terminating
            r.updateCondition(ctx, app, "Ready",
                metav1.ConditionFalse, "Terminating", "Cleaning up external resources")
            
            // Clean up external resources (with timeout protection)
            cleanupCtx, cancel := context.WithTimeout(ctx, 2*time.Minute)
            defer cancel()
            
            if err := r.cleanupExternalResources(cleanupCtx, app); err != nil {
                logger.Error(err, "Cleanup failed, will retry")
                r.Recorder.Eventf(app, corev1.EventTypeWarning,
                    "CleanupFailed", "External resource cleanup failed: %v", err)
                // Return error to trigger retry, but don't retry indefinitely
                return ctrl.Result{RequeueAfter: 10 * time.Second}, true, err
            }
            
            r.Recorder.Event(app, corev1.EventTypeNormal,
                "CleanupComplete", "External resources cleaned up")
            
            // Remove Finalizer
            controllerutil.RemoveFinalizer(app, applicationFinalizer)
            if err := r.Update(ctx, app); err != nil {
                return ctrl.Result{}, true, err
            }
        }
        return ctrl.Result{}, true, nil // isDeleting=true
    }
    
    // Ensure Finalizer exists
    if !controllerutil.ContainsFinalizer(app, applicationFinalizer) {
        controllerutil.AddFinalizer(app, applicationFinalizer)
        if err := r.Update(ctx, app); err != nil {
            return ctrl.Result{}, false, err
        }
    }
    
    return ctrl.Result{}, false, nil // isDeleting=false
}

// External resource cleanup (Example: delete cloud resources, DNS records, etc.)
func (r *ApplicationReconciler) cleanupExternalResources(
    ctx context.Context, app *appv1.Application,
) error {
    // 1. Delete external load balancer
    if err := r.ExternalLBClient.Delete(ctx, app.Status.ExternalLBID); err != nil {
        return fmt.Errorf("delete external LB: %w", err)
    }
    // 2. Clean up DNS records
    if err := r.DNSClient.DeleteRecord(ctx, app.Spec.Domain); err != nil {
        return fmt.Errorf("delete DNS record: %w", err)
    }
    // 3. Release IP addresses
    if err := r.IPAMClient.Release(ctx, app.Status.AllocatedIP); err != nil {
        return fmt.Errorf("release IP: %w", err)
    }
    return nil
}
```

### 4. Event Recording Specifications

```go
type ApplicationReconciler struct {
    client.Client
    Scheme   *runtime.Scheme
    Recorder record.EventRecorder  // Event recorder
}

// Event recording best practices
func (r *ApplicationReconciler) reconcileWithEvents(
    ctx context.Context, app *appv1.Application,
) error {
    // ✅ Record normal operations
    r.Recorder.Event(app, corev1.EventTypeNormal,
        "Reconciling", "Starting reconciliation")
    
    // ✅ Record important state changes
    if oldReplicas != app.Spec.Replicas {
        r.Recorder.Eventf(app, corev1.EventTypeNormal,
            "ScalingDeployment", "Scaling from %d to %d replicas",
            oldReplicas, app.Spec.Replicas)
    }
    
    // ✅ Record warning events
    if app.Spec.Replicas > 50 {
        r.Recorder.Eventf(app, corev1.EventTypeWarning,
            "HighReplicaCount", "Replica count %d exceeds recommended maximum 50",
            app.Spec.Replicas)
    }
    
    // ✅ Record error events
    if err := r.reconcileDeployment(ctx, app); err != nil {
        r.Recorder.Eventf(app, corev1.EventTypeWarning,
            "ReconcileFailed", "Failed to reconcile Deployment: %v", err)
        return err
    }
    
    return nil
}

// Register EventRecorder in SetupWithManager
func (r *ApplicationReconciler) SetupWithManager(mgr ctrl.Manager) error {
    r.Recorder = mgr.GetEventRecorderFor("application-controller")
    return ctrl.NewControllerManagedBy(mgr).
        For(&appv1.Application{}).
        Owns(&appsv1.Deployment{}).
        Complete(r)
}
```

### 5. Retry Strategy and Rate Limiting

| Strategy | Configuration | Description |
|-----|------|------|
| Exponential Backoff | `base=200ms, max=1000s` | Failure retry interval grows exponentially |
| Token Bucket | `rate=10/s, burst=100` | Global limit on Reconcile rate |
| Per-Object Backoff | `per-item failure tracker` | Single object failure doesn't affect others |
| Requeue Delay | `RequeueAfter=30s` | Periodically reconcile after success |

```go
// Production-grade RateLimiter configuration
import (
    "golang.org/x/time/rate"
    "k8s.io/client-go/util/workqueue"
)

func rateLimiter() workqueue.RateLimiter {
    return workqueue.NewMaxOfRateLimiter(
        // Per-object exponential backoff: 200ms → 400ms → 800ms → ... → max 1000s
        workqueue.NewItemExponentialFailureRateLimiter(200*time.Millisecond, 1000*time.Second),
        // Global rate limit: 10 QPS, burst 100
        &workqueue.BucketRateLimiter{Limiter: rate.NewLimiter(rate.Limit(10), 100)},
    )
}

// Retry return strategy in Reconcile
func (r *ApplicationReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    // Transient error → Return error and let RateLimiter handle backoff
    if isTransientError(err) {
        return ctrl.Result{}, err  // Automatic exponential backoff
    }
    // Waiting scenario → Fixed delay retry
    if isWaitingForDependency(app) {
        return ctrl.Result{RequeueAfter: 15 * time.Second}, nil
    }
    // Permanent error → Don't retry, only update status
    if isPermanentError(err) {
        r.updateCondition(ctx, app, "Ready", metav1.ConditionFalse, "PermanentError", err.Error())
        return ctrl.Result{}, nil  // Don't return error, don't retry
    }
    // Success → Periodically reconcile
    return ctrl.Result{RequeueAfter: 5 * time.Minute}, nil
}
```

### 6. Monitoring Metrics Exposure

```go
import (
    "github.com/prometheus/client_golang/prometheus"
    "sigs.k8s.io/controller-runtime/pkg/metrics"
)

var (
    reconcileTotal = prometheus.NewCounterVec(
        prometheus.CounterOpts{
            Name: "application_reconcile_total",
            Help: "Total number of reconciliations per controller",
        },
        []string{"controller", "result"},  // result: success/error/requeue
    )
    reconcileDuration = prometheus.NewHistogramVec(
        prometheus.HistogramOpts{
            Name:    "application_reconcile_duration_seconds",
            Help:    "Duration of reconciliation per controller",
            Buckets: []float64{0.01, 0.05, 0.1, 0.5, 1, 5, 10, 30},
        },
        []string{"controller"},
    )
    resourceCount = prometheus.NewGaugeVec(
        prometheus.GaugeOpts{
            Name: "application_managed_resources",
            Help: "Number of managed Application resources",
        },
        []string{"namespace", "phase"},
    )
)

func init() {
    metrics.Registry.MustRegister(reconcileTotal, reconcileDuration, resourceCount)
}

// Record metrics in Reconcile
func (r *ApplicationReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
    startTime := time.Now()
    defer func() {
        reconcileDuration.WithLabelValues("application").Observe(time.Since(startTime).Seconds())
    }()
    
    result, err := r.doReconcile(ctx, req)
    if err != nil {
        reconcileTotal.WithLabelValues("application", "error").Inc()
    } else if result.Requeue || result.RequeueAfter > 0 {
        reconcileTotal.WithLabelValues("application", "requeue").Inc()
    } else {
        reconcileTotal.WithLabelValues("application", "success").Inc()
    }
    return result, err
}
```

<!-- chunk: Operator Best Practices Quick Reference -->
## Operator Best Practices Quick Reference

| Practice | Description | Example |
|-----|------|------|
| **Idempotency** | Reconcile must be idempotent | Use CreateOrUpdate/SSA |
| **State Management** | Use Status subresource | Separate spec and status updates |
| **Ownership** | Set OwnerReferences | Cascading deletion of sub-resources |
| **Event Recording** | Send K8s Events | Record key operations |
| **Retry Strategy** | Exponential backoff retry | RateLimiter configuration |
| **Resource Limits** | Set concurrency and rate limits | MaxConcurrentReconciles |
| **Monitoring Metrics** | Expose Prometheus metrics | controller-runtime metrics |
| **Graceful Shutdown** | Handle termination signals | LeaderElection graceful |
| **Finalizers** | Clean up external resources | Execute cleanup before deletion |
| **Condition Status** | Use Conditions | Standardize status reporting |

<!-- chunk: Controller Configuration -->
## Controller Configuration

```go
// main.go
func main() {
    mgr, err := ctrl.NewManager(ctrl.GetConfigOrDie(), ctrl.Options{
        Scheme:                 scheme,
        MetricsBindAddress:     ":8080",
        HealthProbeBindAddress: ":8081",
        LeaderElection:         true,
        LeaderElectionID:       "app-operator.example.com",
        // Concurrency control
        Controller: config.Controller{
            GroupKindConcurrency: map[string]int{
                "Application.app.example.com": 10,  // Max 10 concurrent
            },
        },
    })

    if err := (&controller.ApplicationReconciler{
        Client: mgr.GetClient(),
        Scheme: mgr.GetScheme(),
    }).SetupWithManager(mgr); err != nil {
        setupLog.Error(err, "unable to create controller")
        os.Exit(1)
    }
}
```

<!-- chunk: Webhook Development -->
## Webhook Development

```go
// api/v1/application_webhook.go

// +kubebuilder:webhook:path=/mutate-app-example-com-v1-application,mutating=true,failurePolicy=fail,sideEffects=None,groups=app.example.com,resources=applications,verbs=create;update,versions=v1,name=mapplication.kb.io,admissionReviewVersions=v1

var _ webhook.Defaulter = &Application{}

func (r *Application) Default() {
    if r.Spec.Replicas == 0 {
        r.Spec.Replicas = 1
    }
}

// +kubebuilder:webhook:path=/validate-app-example-com-v1-application,mutating=false,failurePolicy=fail,sideEffects=None,groups=app.example.com,resources=applications,verbs=create;update,versions=v1,name=vapplication.kb.io,admissionReviewVersions=v1

var _ webhook.Validator = &Application{}

func (r *Application) ValidateCreate() (admission.Warnings, error) {
    if r.Spec.Replicas > 100 {
        return nil, fmt.Errorf("replicas cannot exceed 100")
    }
    return nil, nil
}

func (r *Application) ValidateUpdate(old runtime.Object) (admission.Warnings, error) {
    oldApp := old.(*Application)
    if r.Spec.Image != oldApp.Spec.Image {
        // Record image change
    }
    return r.ValidateCreate()
}

func (r *Application) ValidateDelete() (admission.Warnings, error) {
    return nil, nil
}
```

<!-- chunk: Operator Testing -->
## Operator Testing

```go
// internal/controller/application_controller_test.go
var _ = Describe("Application Controller", func() {
    Context("When reconciling a resource", func() {
        const resourceName = "test-application"

        ctx := context.Background()

        typeNamespacedName := types.NamespacedName{
            Name:      resourceName,
            Namespace: "default",
        }
        application := &appv1.Application{}

        BeforeEach(func() {
            By("creating the custom resource")
            err := k8sClient.Get(ctx, typeNamespacedName, application)
            if err != nil && errors.IsNotFound(err) {
                resource := &appv1.Application{
                    ObjectMeta: metav1.ObjectMeta{
                        Name:      resourceName,
                        Namespace: "default",
                    },
                    Spec: appv1.ApplicationSpec{
                        Image:    "nginx:1.25",
                        Replicas: 3,
                    },
                }
                Expect(k8sClient.Create(ctx, resource)).To(Succeed())
            }
        })

        It("should create Deployment", func() {
            By("Reconciling the created resource")
            controllerReconciler := &ApplicationReconciler{
                Client: k8sClient,
                Scheme: k8sClient.Scheme(),
            }

            _, err := controllerReconciler.Reconcile(ctx, reconcile.Request{
                NamespacedName: typeNamespacedName,
            })
            Expect(err).NotTo(HaveOccurred())

            deployment := &appsv1.Deployment{}
            Eventually(func() error {
                return k8sClient.Get(ctx, typeNamespacedName, deployment)
            }).Should(Succeed())
            Expect(*deployment.Spec.Replicas).To(Equal(int32(3)))
        })
    })
})
```

<!-- chunk: Version Change Log -->
## Version Change Log

| Version | Changes | Impact |
|------|---------|------|
| v1.25 | CRD Validation Rules CEL Support GA | Built-in complex validation |
| v1.26 | SelectableFields Alpha | Custom field selectors |
| v1.27 | CRD Validation Ratcheting Beta | Progressive validation |
| v1.28 | ValidatingAdmissionPolicy CRD Integration | Simplified webhooks |
| v1.29 | CRD SelectableFields Beta | More stable field selection |
| v1.30 | CEL Cost Estimation Improvement | Performance optimization |
| v1.31 | CRD Metadata Validation Enhancement | Stricter validation |
| v1.32 | SelectableFields GA | Production-ready |

---

**Operator Development Principles**: Idempotent Reconcile + OwnerReference cascading deletion + Finalizer cleanup of external resources + Status subresource state updates + Comprehensive test coverage

---

**Table Footer Attribution**: Kusheet Project, Author Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian Related Documentation -->
## Obsidian Related Documentation

- domain-07-platform-engineering MOC
- [[domain-07-platform-engineering/README.md|Platform Ops Domain]]
- Domain-9 Platform Ops - Open Source Project Index
- Platform Ops Overview
- Cluster Lifecycle Management
- Capacity Planning and Resource Assessment
- Performance Benchmarking and Tuning
- Operations Metrics System
- Monitoring and Alerting System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization and FinOps Practices

## See Also

- 18-platform-observability-practice
- 19-lease-leader-election
- 21-api-aggregation
- 22-client-libraries


<!-- risk-assessed -->