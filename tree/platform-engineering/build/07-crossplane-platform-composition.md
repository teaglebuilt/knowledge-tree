Now I'll provide the complete translated markdown file:

```markdown
---
title: 46 - Kubernetes Client Libraries
description: '## Client Library Architecture'
summary: 'metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"'
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- crd
- operator
- webhook
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
- What is Kubernetes client libraries
- How to use Kubernetes client libraries
- Kubernetes platform ops best practices
trigger_keywords:
- Kubernetes client libraries
- platform
- ops
prerequisites:
- kubectl-basics
- platform-engineering-basics
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
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./build/22-client-libraries.md
original_language: Chinese
---

> **Production Environment Security Notice**
>
> This document contains directly executable operations commands. Before execution, please confirm: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether the command has been tested in a non-production environment. Command risk levels: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (will modify cluster state but usually can be rolled back), 🟢 Low Risk/Read-only (information collection with no side effects).




# 46 - Kubernetes Client Libraries

> **Applicable Versions**: v1.25 - v1.32 | **Last Updated**: 2026-01 | **Reference**: [[entities/kubernetes.md|kubernetes]].io/docs/reference/using-api/client-libraries](https://kubernetes.io/docs/reference/using-api/client-libraries/)

<!-- chunk: Client Library Architecture -->
## Client Library Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Kubernetes Client Library Architecture                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                     Application Layer                               │  │
│   │   ┌───────────────────────────────────────────────────────────┐    │  │
│   │   │              User Code / Controllers / Operators          │    │  │
│   │   └───────────────────────────────────────────────────────────┘    │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                        │                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                     Client Library Abstraction Layer                │  │
│   │   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                │  │
│   │   │ Clientset   │  │ Dynamic     │  │ Discovery   │                │  │
│   │   │ (Typed)     │  │ Client      │  │ Client      │                │  │
│   │   │             │  │ (Dynamic)   │  │ (API Discovery)             │  │
│   │   └─────────────┘  └─────────────┘  └─────────────┘                │  │
│   │                                                                      │  │
│   │   ┌────────────────────────────────────────────────────────────┐   │  │
│   │   │                    Informer / Lister                        │   │  │
│   │   │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │   │  │
│   │   │  │   Reflector  │  │    Store     │  │  Processor   │      │   │  │
│   │   │  │  List+Watch  │─▶│ Local Cache  │─▶│ Event Handler│      │   │  │
│   │   │  └──────────────┘  └──────────────┘  └──────────────┘      │   │  │
│   │   └────────────────────────────────────────────────────────────┘   │  │
│   │                                                                      │  │
│   │   ┌────────────────────────────────────────────────────────────┐   │  │
│   │   │                    WorkQueue                                │   │  │
│   │   │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │   │  │
│   │   │  │ AddRateLimited│  │DelayingQueue │  │   Worker    │      │   │  │
│   │   │  └──────────────┘  └──────────────┘  └──────────────┘      │   │  │
│   │   └────────────────────────────────────────────────────────────┘   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                        │                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                     REST Client Layer                              │  │
│   │   ┌────────────────────────────────────────────────────────────┐   │  │
│   │   │                  rest.RESTClient                            │   │  │
│   │   │  • HTTP request building    • Authentication              │   │  │
│   │   │  • Serialization/Deserialization • Retry logic            │   │  │
│   │   │  • Rate limiting            • Timeout handling            │   │  │
│   │   └────────────────────────────────────────────────────────────┘   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                        │                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                     Transport Layer                               │  │
│   │   ┌────────────────────────────────────────────────────────────┐   │  │
│   │   │           HTTP/2 + TLS + Authentication Credentials        │   │  │
│   │   └────────────────────────────────────────────────────────────┘   │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
│                                        │                                    │
│                                        ▼                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐  │
│   │                     Kubernetes API Server                           │  │
│   └─────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- chunk: Official Client Library Comparison -->
## Official Client Library Comparison

| Language | Repository | Maintenance Status | Version Mapping | Characteristics | Recommended Scenarios |
|----------|------------|-------------------|-----------------|-----------------|----------------------|
| **Go** | kubernetes/client-go | Official | Synchronized with K8s | Most complete functionality, best performance | Controller/Operator development |
| **Python** | kubernetes-client/python | Official | Synchronized with K8s | Simple and easy to use | Scripts/Automation |
| **Java** | kubernetes-client/java | Official | Synchronized with K8s | Enterprise-grade support | Java application integration |
| **JavaScript/TypeScript** | kubernetes-client/javascript | Official | Synchronized with K8s | Frontend friendly | Node.js applications |
| **C#** | kubernetes-client/csharp | Official | Synchronized with K8s | .NET ecosystem | .NET applications |
| **Haskell** | kubernetes-client/haskell | Community | Delayed sync | Functional programming | Haskell projects |

<!-- chunk: Go client-go Detailed Explanation -->
## Go client-go Detailed Explanation

### client-go Components

| Component | Function | Use Cases | Package Path |
|-----------|----------|-----------|--------------|
| **Clientset** | Typed client | Accessing built-in resources | k8s.io/client-go/kubernetes |
| **DynamicClient** | Dynamic client | Accessing arbitrary resources | k8s.io/client-go/dynamic |
| **RESTClient** | REST client | Low-level HTTP calls | k8s.io/client-go/rest |
| **DiscoveryClient** | Discovery client | API discovery | k8s.io/client-go/discovery |
| **Informer** | Event listener | Controller development | k8s.io/client-go/informers |
| **Lister** | Local cache query | Controller development | k8s.io/client-go/listers |
| **WorkQueue** | Work queue | Controller development | k8s.io/client-go/util/workqueue |

### Basic Usage Example

```go
package main

import (
    "context"
    "fmt"
    "os"
    "path/filepath"

    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "k8s.io/client-go/kubernetes"
    "k8s.io/client-go/tools/clientcmd"
    "k8s.io/client-go/rest"
)

func main() {
    // Method 1: Load config from kubeconfig (outside cluster)
    config, err := getKubeConfig()
    if err != nil {
        panic(err)
    }

    // Configure QPS and Burst
    config.QPS = 100
    config.Burst = 200
    config.Timeout = 30 * time.Second

    // Create clientset
    clientset, err := kubernetes.NewForConfig(config)
    if err != nil {
        panic(err)
    }

    // List Pods in default namespace
    pods, err := clientset.CoreV1().Pods("default").
        List(context.TODO(), metav1.ListOptions{})
    if err != nil {
        panic(err)
    }

    fmt.Printf("Found %d pods in default namespace\n", len(pods.Items))
    for _, pod := range pods.Items {
        fmt.Printf("  Pod: %s, Phase: %s\n", pod.Name, pod.Status.Phase)
    }

    // Get single Pod
    pod, err := clientset.CoreV1().Pods("default").
        Get(context.TODO(), "my-pod", metav1.GetOptions{})
    if err != nil {
        fmt.Printf("Pod not found: %v\n", err)
    } else {
        fmt.Printf("Pod %s is in phase %s\n", pod.Name, pod.Status.Phase)
    }

    // Create Pod
    newPod := &corev1.Pod{
        ObjectMeta: metav1.ObjectMeta{
            Name:      "test-pod",
            Namespace: "default",
        },
        Spec: corev1.PodSpec{
            Containers: []corev1.Container{
                {
                    Name:  "nginx",
                    Image: "nginx:1.21",
                },
            },
        },
    }
    
    createdPod, err := clientset.CoreV1().Pods("default").
        Create(context.TODO(), newPod, metav1.CreateOptions{})
    if err != nil {
        panic(err)
    }
    fmt.Printf("Created pod: %s\n", createdPod.Name)

    // Delete Pod
    err = clientset.CoreV1().Pods("default").
        Delete(context.TODO(), "test-pod", metav1.DeleteOptions{})
    if err != nil {
        fmt.Printf("Delete failed: %v\n", err)
    }
}

// getKubeConfig retrieves Kubernetes configuration
func getKubeConfig() (*rest.Config, error) {
    // Running in cluster
    if os.Getenv("KUBERNETES_SERVICE_HOST") != "" {
        return rest.InClusterConfig()
    }
    
    // Running outside cluster
    kubeconfig := filepath.Join(os.Getenv("HOME"), ".kube", "config")
    if envConfig := os.Getenv("KUBECONFIG"); envConfig != "" {
        kubeconfig = envConfig
    }
    
    return clientcmd.BuildConfigFromFlags("", kubeconfig)
}
```

### Informer Usage

```go
package main

import (
    "fmt"
    "time"

    corev1 "k8s.io/api/core/v1"
    "k8s.io/client-go/informers"
    "k8s.io/client-go/kubernetes"
    "k8s.io/client-go/tools/cache"
)

func main() {
    // Create clientset
    config, _ := getKubeConfig()
    clientset, _ := kubernetes.NewForConfig(config)

    // Create SharedInformerFactory
    // resyncPeriod: Periodic full synchronization interval, 0 means no re-sync
    factory := informers.NewSharedInformerFactory(clientset, time.Hour)

    // Get Informer for specific namespace
    // factory := informers.NewSharedInformerFactoryWithOptions(
    //     clientset,
    //     time.Hour,
    //     informers.WithNamespace("production"),
    // )

    // Get Pod Informer
    podInformer := factory.Core().V1().Pods()

    // Add event handlers
    podInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs{
        AddFunc: func(obj interface{}) {
            pod := obj.(*corev1.Pod)
            fmt.Printf("Pod ADDED: %s/%s\n", pod.Namespace, pod.Name)
        },
        UpdateFunc: func(oldObj, newObj interface{}) {
            oldPod := oldObj.(*corev1.Pod)
            newPod := newObj.(*corev1.Pod)
            if oldPod.ResourceVersion != newPod.ResourceVersion {
                fmt.Printf("Pod UPDATED: %s/%s\n", newPod.Namespace, newPod.Name)
            }
        },
        DeleteFunc: func(obj interface{}) {
            pod := obj.(*corev1.Pod)
            fmt.Printf("Pod DELETED: %s/%s\n", pod.Namespace, pod.Name)
        },
    })

    // Start Informer
    stopCh := make(chan struct{})
    factory.Start(stopCh)

    // Wait for cache sync
    if !cache.WaitForCacheSync(stopCh, podInformer.Informer().HasSynced) {
        panic("Failed to sync cache")
    }

    fmt.Println("Cache synced, informer is running...")

    // Use Lister to query from local cache (will not access API Server)
    lister := podInformer.Lister()
    
    // List all Pods
    pods, _ := lister.List(labels.Everything())
    fmt.Printf("Found %d pods in cache\n", len(pods))

    // List Pods in specific namespace
    defaultPods, _ := lister.Pods("default").List(labels.Everything())
    fmt.Printf("Found %d pods in default namespace\n", len(defaultPods))

    // Get specific Pod
    pod, err := lister.Pods("default").Get("my-pod")
    if err != nil {
        fmt.Printf("Pod not found in cache: %v\n", err)
    }

    // Block and wait
    <-stopCh
}
```

### Controller Development Pattern

```go
package main

import (
    "context"
    "fmt"
    "time"

    corev1 "k8s.io/api/core/v1"
    "k8s.io/apimachinery/pkg/util/runtime"
    "k8s.io/apimachinery/pkg/util/wait"
    "k8s.io/client-go/informers"
    "k8s.io/client-go/kubernetes"
    corev1listers "k8s.io/client-go/listers/core/v1"
    "k8s.io/client-go/tools/cache"
    "k8s.io/client-go/util/workqueue"
    "k8s.io/klog/v2"
)

// Controller controller structure
type Controller struct {
    clientset     kubernetes.Interface
    podLister     corev1listers.PodLister
    podSynced     cache.InformerSynced
    workqueue     workqueue.RateLimitingInterface
}

// NewController creates a controller
func NewController(
    clientset kubernetes.Interface,
    factory informers.SharedInformerFactory,
) *Controller {
    podInformer := factory.Core().V1().Pods()

    controller := &Controller{
        clientset: clientset,
        podLister: podInformer.Lister(),
        podSynced: podInformer.Informer().HasSynced,
        workqueue: workqueue.NewNamedRateLimitingQueue(
            workqueue.DefaultControllerRateLimiter(),
            "Pods",
        ),
    }

    // Add event handlers
    podInformer.Informer().AddEventHandler(cache.ResourceEventHandlerFuncs{
        AddFunc: controller.enqueuePod,
        UpdateFunc: func(old, new interface{}) {
            controller.enqueuePod(new)
        },
        DeleteFunc: controller.enqueuePod,
    })

    return controller
}

// enqueuePod adds Pod key to queue
func (c *Controller) enqueuePod(obj interface{}) {
    var key string
    var err error
    if key, err = cache.MetaNamespaceKeyFunc(obj); err != nil {
        runtime.HandleError(err)
        return
    }
    c.workqueue.Add(key)
}

// Run runs the controller
func (c *Controller) Run(workers int, stopCh <-chan struct{}) error {
    defer runtime.HandleCrash()
    defer c.workqueue.ShutDown()

    klog.Info("Starting controller")

    // Wait for cache sync
    klog.Info("Waiting for informer caches to sync")
    if ok := cache.WaitForCacheSync(stopCh, c.podSynced); !ok {
        return fmt.Errorf("failed to wait for caches to sync")
    }

    klog.Info("Starting workers")
    // Start workers
    for i := 0; i < workers; i++ {
        go wait.Until(c.runWorker, time.Second, stopCh)
    }

    klog.Info("Controller started")
    <-stopCh
    klog.Info("Shutting down controller")
    return nil
}

// runWorker worker loop
func (c *Controller) runWorker() {
    for c.processNextWorkItem() {
    }
}

// processNextWorkItem processes the next item in the queue
func (c *Controller) processNextWorkItem() bool {
    obj, shutdown := c.workqueue.Get()
    if shutdown {
        return false
    }

    err := func(obj interface{}) error {
        defer c.workqueue.Done(obj)
        
        key, ok := obj.(string)
        if !ok {
            c.workqueue.Forget(obj)
            return fmt.Errorf("expected string in workqueue but got %#v", obj)
        }

        // Execute reconcile logic
        if err := c.syncHandler(key); err != nil {
            // Re-queue
            c.workqueue.AddRateLimited(key)
            return fmt.Errorf("error syncing '%s': %s, requeuing", key, err.Error())
        }

        // Successful processing, clear retry count
        c.workqueue.Forget(obj)
        klog.Infof("Successfully synced '%s'", key)
        return nil
    }(obj)

    if err != nil {
        runtime.HandleError(err)
        return true
    }

    return true
}

// syncHandler actual reconcile logic
func (c *Controller) syncHandler(key string) error {
    namespace, name, err := cache.SplitMetaNamespaceKey(key)
    if err != nil {
        return fmt.Errorf("invalid resource key: %s", key)
    }

    // Get Pod from cache
    pod, err := c.podLister.Pods(namespace).Get(name)
    if err != nil {
        // Pod has been deleted
        if errors.IsNotFound(err) {
            klog.Infof("Pod %s/%s has been deleted", namespace, name)
            return nil
        }
        return err
    }

    // Execute business logic
    klog.Infof("Processing Pod %s/%s, Phase: %s", 
        pod.Namespace, pod.Name, pod.Status.Phase)

    // ... actual business logic

    return nil
}

func main() {
    config, _ := getKubeConfig()
    clientset, _ := kubernetes.NewForConfig(config)

    factory := informers.NewSharedInformerFactory(clientset, time.Hour)
    controller := NewController(clientset, factory)

    stopCh := make(chan struct{})
    factory.Start(stopCh)

    if err := controller.Run(2, stopCh); err != nil {
        klog.Fatalf("Error running controller: %s", err.Error())
    }
}
```

### Dynamic Client Usage

```go
package main

import (
    "context"
    "fmt"

    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "k8s.io/apimachinery/pkg/apis/meta/v1/unstructured"
    "k8s.io/apimachinery/pkg/runtime/schema"
    "k8s.io/client-go/dynamic"
)

func main() {
    config, _ := getKubeConfig()
    
    // Create dynamic client
    dynamicClient, err := dynamic.NewForConfig(config)
    if err != nil {
        panic(err)
    }

    // Define GVR (Group, Version, Resource)
    gvr := schema.GroupVersionResource{
        Group:    "",          // core API group is empty
        Version:  "v1",
        Resource: "pods",
    }

    // List Pods
    unstructuredList, err := dynamicClient.Resource(gvr).
        Namespace("default").
        List(context.TODO(), metav1.ListOptions{})
    if err != nil {
        panic(err)
    }

    for _, item := range unstructuredList.Items {
        name, _, _ := unstructured.NestedString(item.Object, "metadata", "name")
        phase, _, _ := unstructured.NestedString(item.Object, "status", "phase")
        fmt.Printf("Pod: %s, Phase: %s\n", name, phase)
    }

    // Create custom resource
    crdGVR := schema.GroupVersionResource{
        Group:    "myapp.example.com",
        Version:  "v1",
        Resource: "myapps",
    }

    myApp := &unstructured.Unstructured{
        Object: map[string]interface{}{
            "apiVersion": "myapp.example.com/v1",
            "kind":       "MyApp",
            "metadata": map[string]interface{}{
                "name":      "my-app-instance",
                "namespace": "default",
            },
            "spec": map[string]interface{}{
                "replicas": 3,
                "image":    "nginx:1.21",
            },
        },
    }

    created, err := dynamicClient.Resource(crdGVR).
        Namespace("default").
        Create(context.TODO(), myApp, metav1.CreateOptions{})
    if err != nil {
        fmt.Printf("Create failed: %v\n", err)
    } else {
        fmt.Printf("Created: %s\n", created.GetName())
    }
}
```

<!-- chunk: Python Client Usage -->
## Python Client Usage

### Basic Usage

```python
from kubernetes import client, config, watch
from kubernetes.client.rest import ApiException
import os

def main():
    # Load configuration
    # Outside cluster
    config.load_kube_config()
    # Inside cluster
    # config.load_incluster_config()

    # Create API client
    v1 = client.CoreV1Api()
    apps_v1 = client.AppsV1Api()

    # List Pods in all namespaces
    print("=== List all Pods ===")
    pods = v1.list_pod_for_all_namespaces(watch=False)
    for pod in pods.items:
        print(f"{pod.metadata.namespace}/{pod.metadata.name}: {pod.status.phase}")

    # List Pods in specific namespace
    print("\n=== Pods in default namespace ===")
    pods = v1.list_namespaced_pod(namespace="default")
    for pod in pods.items:
        print(f"  {pod.metadata.name}: {pod.status.phase}")

    # Create Pod
    print("\n=== Create Pod ===")
    pod_manifest = client.V1Pod(
        api_version="v1",
        kind="Pod",
        metadata=client.V1ObjectMeta(
            name="test-pod",
            labels={"app": "test"}
        ),
        spec=client.V1PodSpec(
            containers=[
                client.V1Container(
                    name="nginx",
                    image="nginx:1.21",
                    ports=[client.V1ContainerPort(container_port=80)]
                )
            ]
        )
    )
    
    try:
        created_pod = v1.create_namespaced_pod(
            namespace="default",
            body=pod_manifest
        )
        print(f"Created pod: {created_pod.metadata.name}")
    except ApiException as e:
        print(f"Exception when creating pod: {e}")

    # Delete Pod
    print("\n=== Delete Pod ===")
    try:
        v1.delete_namespaced_pod(
            name="test-pod",
            namespace="default"
        )
        print("Pod deleted")
    except ApiException as e:
        print(f"Exception when deleting pod: {e}")

    # Create Deployment
    print("\n=== Create Deployment ===")
    deployment = client.V1Deployment(
        api_version="apps/v1",
        kind="Deployment",
        metadata=client.V1ObjectMeta(name="nginx-deployment"),
        spec=client.V1DeploymentSpec(
            replicas=3,
            selector=client.V1LabelSelector(
                match_labels={"app": "nginx"}
            ),
            template=client.V1PodTemplateSpec(
                metadata=client.V1ObjectMeta(labels={"app": "nginx"}),
                spec=client.V1PodSpec(
                    containers=[
                        client.V1Container(
                            name="nginx",
                            image="nginx:1.21",
                            ports=[client.V1ContainerPort(container_port=80)]
                        )
                    ]
                )
            )
        )
    )
    
    try:
        apps_v1.create_namespaced_deployment(
            namespace="default",
            body=deployment
        )
        print("Deployment created")
    except ApiException as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    main()
```

### Watch Events

```python
from kubernetes import client, config, watch
import threading

def watch_pods():
    config.load_kube_config()
    v1 = client.CoreV1Api()
    
    w = watch.Watch()
    
    print("Starting to watch pods...")
    for event in w.stream(
        v1.list_namespaced_pod,
        namespace="default",
        timeout_seconds=300  # 5 minute timeout
    ):
        event_type = event['type']
        pod = event['object']
        print(f"Event: {event_type} Pod: {pod.metadata.name} Phase: {pod.status.phase}")
        
        # You can add exit conditions here
        # if some_condition:
        #     w.stop()
        #     break

def watch_with_resource_version():
    """Incremental Watch with resource version"""
    config.load_kube_config()
    v1 = client.CoreV1Api()
    
    # List first to get current resource version
    pod_list = v1.list_namespaced_pod(namespace="default")
    resource_version = pod_list.metadata.resource_version
    
    print(f"Starting watch from resource_version: {resource_version}")
    
    w = watch.Watch()
    for event in w.stream(
        v1.list_namespaced_pod,
        namespace="default",
        resource_version=resource_version,  # Start from specified version
        timeout_seconds=0  # 0 means server default timeout
    ):
        print(f"Event: {event['type']} Pod: {event['object'].metadata.name}")

if __name__ == "__main__":
    watch_pods()
```

### Asynchronous Client

```python
import asyncio
from kubernetes_asyncio import client, config, watch

async def main():
    # Load configuration
    await config.load_kube_config()
    
    # Create asynchronous API client
    async with client.ApiClient() as api:
        v1 = client.CoreV1Api(api)
        
        # List Pods
        pods = await v1.list_namespaced_pod(namespace="default")
        for pod in pods.items:
            print(f"Pod: {pod.metadata.name}")
        
        # Asynchronous Watch
        w = watch.Watch()
        async for event in w.stream(
            v1.list_namespaced_pod,
            namespace="default",
            timeout_seconds=60
        ):
            print(f"Event: {event['type']} Pod: {event['object'].metadata.name}")

if __name__ == "__main__":
    asyncio.run(main())
```

<!-- chunk: Java Client Usage -->
## Java Client Usage

### Basic Usage

```java
package com.example.k8s;

import io.kubernetes.client.openapi.ApiClient;
import io.kubernetes.client.openapi.ApiException;
import io.kubernetes.client.openapi.Configuration;
import io.kubernetes.client.openapi.apis.CoreV1Api;
import io.kubernetes.client.openapi.apis.AppsV1Api;
import io.kubernetes.client.openapi.models.*;
import io.kubernetes.client.util.Config;

import java.util.Arrays;
import java.util.Map;

public class KubernetesExample {
    public static void main(String[] args) throws Exception {
        // Load configuration
        // Load kubeconfig from default location
        ApiClient client = Config.defaultClient();
        // Or from within cluster
        // ApiClient client = Config.fromCluster();
        
        // Configure timeout
        client.setConnectTimeout(30000);
        client.setReadTimeout(30000);
        client.setWriteTimeout(30000);
        
        Configuration.setDefaultApiClient(client);
        
        // Create API instances
        CoreV1Api coreApi = new CoreV1Api();
        AppsV1Api appsApi = new AppsV1Api();
        
        // List Pods
        System.out.println("=== List Pods ===");
        V1PodList podList = coreApi.listNamespacedPod(
            "default",     // namespace
            null,          // pretty
            null,          // allowWatchBookmarks
            null,          // _continue
            null,          // fieldSelector
            null,          // labelSelector
            null,          // limit
            null,          // resourceVersion
            null,          // resourceVersionMatch
            null,          // sendInitialEvents
            null,          // timeoutSeconds
            null           // watch
        );
        
        for (V1Pod pod : podList.getItems()) {
            System.out.println("Pod: " + pod.getMetadata().getName() + 
                             " Phase: " + pod.getStatus().getPhase());
        }
        
        // Create Pod
        System.out.println("\n=== Create Pod ===");
        V1Pod newPod = new V1Pod()
            .apiVersion("v1")
            .kind("Pod")
            .metadata(new V1ObjectMeta()
                .name("test-pod")
                .labels(Map.of("app", "test")))
            .spec(new V1PodSpec()
                .containers(Arrays.asList(
                    new V1Container()
                        .name("nginx")
                        .image("nginx:1.21")
                        .ports(Arrays.asList(
                            new V1ContainerPort().containerPort(80)
                        ))
                )));
        
        try {
            V1Pod createdPod = coreApi.createNamespacedPod(
                "default", newPod, null, null, null, null
            );
            System.out.println("Created pod: " + createdPod.getMetadata().getName());
        } catch (ApiException e) {
            System.out.println("Exception: " + e.getResponseBody());
        }
        
        // Delete Pod
        System.out.println("\n=== Delete Pod ===");
        try {
            coreApi.deleteNamespacedPod(
                "test-pod", "default", null, null, null, null, null, null
            );
            System.out.println("Pod deleted");
        } catch (ApiException e) {
            System.out.println("Exception: " + e.getResponseBody());
        }
    }
}
```

### Watch Events

```java
package com.example.k8s;

import io.kubernetes.client.openapi.ApiClient;
import io.kubernetes.client.openapi.apis.CoreV1Api;
import io.kubernetes.client.openapi.models.V1Pod;
import io.kubernetes.client.util.Config;
import io.kubernetes.client.util.Watch;

import java.util.concurrent.TimeUnit;

public class WatchExample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Config.defaultClient();
        // Set timeout
        client.setHttpClient(client.getHttpClient().newBuilder()
            .readTimeout(0, TimeUnit.SECONDS)  // Infinite wait for Watch
            .build());
        
        CoreV1Api api = new CoreV1Api(client);
        
        // Create Watch
        try (Watch<V1Pod> watch = Watch.createWatch(
            client,
            api.listNamespacedPodCall(
                "default",
                null, null, null, null, null, null, null, null, null,
                true,  // watch=true
                null
            ),
            new TypeToken<Watch.Response<V1Pod>>() {}.getType()
        )) {
            System.out.println("Starting watch...");
            for (Watch.Response<V1Pod> event : watch) {
                System.out.println(String.format(
                    "Event: %s Pod: %s Phase: %s",
                    event.type,
                    event.object.getMetadata().getName(),
                    event.object.getStatus().getPhase()
                ));
            }
        }
    }
}
```

<!-- chunk: Authentication Methods -->
## Authentication Methods

### Authentication Methods Comparison

| Method | Scenario | Configuration | Security |
|--------|----------|---------------|----------|
| **kubeconfig** | Development outside cluster | Configuration file | Medium |
| **InCluster** | Running in Pod | Auto-mounted | High |
| **ServiceAccount** | Running in Pod | Token | High |
| **Bearer Token** | API access | Token string | Medium |
| **Client Certificate** | mTLS | Certificate + Key | High |
| **OIDC** | Enterprise SSO | OAuth2 | High |
| **Webhook Token** | Custom authentication | External service | High |

### Authentication Configuration Example (Go)

```go
package main

import (
    "k8s.io/client-go/rest"
    "k8s.io/client-go/tools/clientcmd"
)

// Method 1: kubeconfig file
func fromKubeconfig() (*rest.Config, error) {
    return clientcmd.BuildConfigFromFlags("", "/path/to/kubeconfig")
}

// Method 2: In-cluster (automatically uses ServiceAccount)
func inCluster() (*rest.Config, error) {
    return rest.InClusterConfig()
}

// Method 3: Bearer Token
func withBearerToken() *rest.Config {
    return &rest.Config{
        Host:        "https://kubernetes.default.svc",
        BearerToken: "your-token-here",
        TLSClientConfig: rest.TLSClientConfig{
            CAFile: "/var/run/secrets/kubernetes.io/serviceaccount/ca.crt",
        },
    }
}

// Method 4: Client Certificate
func withClientCert() *rest.Config {
    return &rest.Config{
        Host: "https://kubernetes.default.svc",
        TLSClientConfig: rest.TLSClientConfig{
            CAFile:   "/path/to/ca.crt",
            CertFile: "/path/to/client.crt",
            KeyFile:  "/path/to/client.key",
        },
    }
}

// Method 5: Combine multiple authentication methods
func combined() (*rest.Config, error) {
    config, err := rest.InClusterConfig()
    if err != nil {
        // Fall back to kubeconfig
        return clientcmd.BuildConfigFromFlags("", clientcmd.RecommendedHomeFile)
    }
    return config, nil
}
```

<!-- chunk: Client Version Compatibility -->
## Client Version Compatibility

### Version Mapping Table

| client-go Version | K8s Version | Go Version Required | Release Date |
|------------------|------------|-------------------|--------------|
| v0.25.x | v1.25 | go1.19+ | 2022-08 |
| v0.26.x | v1.26 | go1.19+ | 2022-12 |
| v0.27.x | v1.27 | go1.20+ | 2023-04 |
| v0.28.x | v1.28 | go1.20+ | 2023-08 |
| v0.29.x | v1.29 | go1.21+ | 2023-12 |
| v0.30.x | v1.30 | go1.22+ | 2024-04 |
| v0.31.x | v1.31 | go1.22+ | 2024-08 |
| v0.32.x | v1.32 | go1.23+ | 2024-12 |

### Compatibility Rules

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     Client Version Compatibility Rules                       │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   Official Support Matrix:                                                  │
│   • client-go X.Y supports K8s X.Y-1, X.Y, X.Y+1 (±1 version)              │
│                                                                             │
│   Recommended Practices:                                                    │
│   • Production environment: Client version <= Server version                │
│   • Development environment: Can use newer client with older server         │
│                                                                             │
│   Version Selection:                                                        │
│   ┌─────────────────────────────────────────────────────────────────┐      │
│   │ Server Version   Recommended Client Version   Compatible Versions│      │
│   ├─────────────────────────────────────────────────────────────────┤      │
│   │ v1.30            v0.30.x                      v0.29.x - v0.31.x│      │
│   │ v1.29            v0.29.x                      v0.28.x - v0.30.x│      │
│   │ v1.28            v0.28.x                      v0.27.x - v0.29.x│      │
│   └─────────────────────────────────────────────────────────────────┘      │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- chunk: Performance Optimization -->
## Performance Optimization

### Optimization Strategies

| Optimization Item | Description | Implementation | Effect |
|------------------|------------|-----------------|--------|
| **Use Informer** | Avoid frequent List calls | Local cache + Watch | Reduce API Server load |
| **Set ResourceVersion** | Incremental Watch | Use RV after List | Avoid full data transmission |
| **Limit Returned Fields** | Reduce transmitted data | fieldSelector | Reduce network bandwidth |
| **Pagination Query** | Handle large resources | limit/continue | Avoid timeout and memory issues |
| **Reuse Client** | Avoid duplicate connection creation | Singleton pattern | Reduce connection overhead |
| **Configure QPS Limit** | Prevent API Server overload | QPS/Burst configuration | Protect API Server |
| **Use ServerSideApply** | Reduce conflicts | Apply operation | Better concurrent control |

### QPS Configuration

```go
// QPS configuration example
config, _ := clientcmd.BuildConfigFromFlags("", kubeconfig)

// Basic configuration
config.QPS = 100              // Requests per second
config.Burst = 200            // Burst requests
config.Timeout = 30 * time.Second

// Adjust based on scenario
// Controller scenario (high concurrency)
config.QPS = 200
config.Burst = 400

// Batch processing scenario (low priority)
config.QPS = 20
config.Burst = 40

// Monitoring/Observation scenario
config.QPS = 50
config.Burst = 100
```

### Pagination Query

```go
// Pagination query for large number of resources
func listAllPods(clientset *kubernetes.Clientset) ([]corev1.Pod, error) {
    var allPods []corev1.Pod
    
    opts := metav1.ListOptions{
        Limit: 100,  // 100 per page
    }
    
    for {
        podList, err := clientset.CoreV1().Pods("").
            List(context.TODO(), opts)
        if err != nil {
            return nil, err
        }
        
        allPods = append(allPods, podList.Items...)
        
        // Check if there are more pages
        if podList.Continue == "" {
            break
        }
        opts.Continue = podList.Continue
    }
    
    return allPods, nil
}
```

### ServerSideApply

```go
// Server-Side Apply example
func applyPod(clientset *kubernetes.Clientset) error {
    pod := &corev1.Pod{
        TypeMeta: metav1.TypeMeta{
            APIVersion: "v1",
            Kind:       "Pod",
        },
        ObjectMeta: metav1.ObjectMeta{
            Name:      "my-pod",
            Namespace: "default",
        },
        Spec: corev1.PodSpec{
            Containers: []corev1.Container{
                {
                    Name:  "nginx",
                    Image: "nginx:1.21",
                },
            },
        },
    }
    
    // Use Apply (requires setting fieldManager)
    _, err := clientset.CoreV1().Pods("default").Apply(
        context.TODO(),
        &applycorev1.PodApplyConfiguration{
            TypeMetaApplyConfiguration: applymetav1.TypeMetaApplyConfiguration{
                APIVersion: ptr.To("v1"),
                Kind:       ptr.To("Pod"),
            },
            ObjectMetaApplyConfiguration: &applymetav1.ObjectMetaApplyConfiguration{
                Name:      ptr.To("my-pod"),
                Namespace: ptr.To("default"),
            },
            Spec: &applycorev1.PodSpecApplyConfiguration{
                Containers: []applycorev1.ContainerApplyConfiguration{
                    {
                        Name:  ptr.To("nginx"),
                        Image: ptr.To("nginx:1.21"),
                    },
                },
            },
        },
        metav1.ApplyOptions{
            FieldManager: "my-controller",
            Force:        true,
        },
    )
    return err
}
```

<!-- chunk: FAQ and Solutions -->
## FAQ and Solutions

| Problem | Root Cause | Solution |
|---------|-----------|----------|
| **Connection Timeout** | Network issues/High API Server load | Increase timeout, check network |
| **Authentication Failed** | Token expired/Certificate issue | Refresh token, check certificate validity |
| **Watch Disconnected** | Timeout/Stale resource version | Re-list to get RV, rebuild Watch |
| **Stale Resource Version** | Long time without sync | Re-list to get latest RV |
| **Memory Overflow** | Large resource cache | Use pagination, limit Informer scope |
| **Request Rate Limited** | QPS exceeded | Lower QPS, increase retry interval |
| **Concurrent Conflict** | Multiple clients modifying | Use ServerSideApply |

<!-- chunk: Version Change Log -->
## Version Change Log

| Version | Changes | Impact |
|---------|---------|--------|
| v0.25 | Watch Bookmarks GA | More reliable Watch |
| v0.26 | Improved retry logic | Better error handling |
| v0.27 | Apply configuration generator | Easier to use SSA |
| v0.28 | Improved Informer | Performance improvement |
| v0.29 | New authentication methods | More authentication options |
| v0.30 | HTTP/2 optimization | Connection performance improvement |

---

**Client Usage Principles**: Prioritize using Informer → Configure QPS properly → Use pagination query → Choose appropriate authentication method → Keep version compatible

---

**Table Bottom Note**: Kusheet Project, Author Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian Related Documentation -->
## Obsidian Related Documentation

- domain-07-platform-engineering KUDIG Database — Global MOC
- [[domain-07-platform-engineering/README.md|[[Platform Ops Domain|Platform Ops Domain]]]]
- Domain-9 Platform Operations — Open Source Project Index
- Platform Operations Overview
- Cluster Lifecycle Management
- Capacity Planning & Resource Assessment
- Performance Benchmarking & Tuning
- Operations Metrics System
- Monitoring and Alerting System
- GitOps Configuration Management
- Operations Automation Toolchain
- Cost Optimization & FinOps Practices

## See Also

- 20-crd-operator-development
- 21-api-aggregation
- 23-cli-enhancement-tools
- 24-addons-extensions


<!-- risk-assessed -->
```

Here is the complete translated markdown file with all Chinese prose, headings, and frontmatter translated to English, while preserving code identifiers, URLs, and structure. The source path and original language metadata have been added to the frontmatter.