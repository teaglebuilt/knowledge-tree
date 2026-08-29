---
title: Java Kubernetes Client and Operator SDK Development Guide
description: 'title: Java Kubernetes Client and Operator SDK Development Guide'
summary: 'title: Java Kubernetes Client and Operator SDK Development Guide'
category: general
tags:
- k8s
- devops
- daily-ops
- guide
- docker
- statefulset
- ingress
- rbac
- crd
- operator
tier: peripheral
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 25min
intent_queries:
- What is an Operator?
- How do I use Operator?
- What are the best practices for Operators?
trigger_keywords:
- Java
- Kubernetes
- Client
- Operator
- SDK
- Development Guide
- platform
- engineering
prerequisites:
- kubectl-basics
- platform-engineering-basics
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-07-platform-engineering/./build/99-java-k8s-client-operator-guide.md
original_language: Chinese
---

> **Production Environment Security Notice**
>
> This document contains directly executable operations commands. Before execution, please verify: whether the current target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have verified in a non-production environment. Command risk levels are marked as: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (will modify cluster state, but usually recoverable), 🟢 Low Risk / Read-Only (information gathering, no side effects).

---

title: Java [[Kubernetes|Kubernetes]] Client and Operator SDK Development Guide
description: '# Java Kubernetes Client and Operator SDK Development Guide'
category: platform-ops
tags:
- k8s
- platform
- operations
- devops
- docker
- [[StatefulSet|statefulset]]
- [[Ingress|ingress]]
- rbac
- crd
- operator
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Platform Engineer
- Operations Engineer
estimated_read_time: 5min
intent_queries:
- What is Java Kubernetes Client and Operator SDK Development Guide
- How to Java Kubernetes Client and Operator SDK Development Guide
- Kubernetes 9 platform ops best practices
trigger_keywords:
- Java
- Kubernetes
- Client
- Operator
- SDK
- Development Guide
- platform
- ops
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
authors:
- name: KUDIG Team
  role: contributor
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
---

# Java Kubernetes Client and Operator SDK Development Guide

> **Applicable Versions**: Kubernetes Java Client 20+ / Java Operator SDK 4.9+ / Quarkus Operator SDK 6.8+  
> **Last Updated**: 2026-04-30  
> **Difficulty**: Advanced

---

<!-- chunk: 📋 Table of Contents -->
## 📋 Table of Contents

- [I. Java K8s Client Ecosystem Overview](#ijava-k8s-client-ecosystem-overview)
- [II. fabric8 Kubernetes Client](#iifabric8-kubernetes-client)
- [III. Official Kubernetes Java Client](#iiiofficial-kubernetes-java-client)
- [IV. Java Operator SDK (JOSDK)](#ivjava-operator-sdk-josdk)
- [V. Quarkus Operator SDK](#vquarkus-operator-sdk)
- [VI. Informer and List-Watch Pattern](#viinformer-and-list-watch-pattern)
- [VII. Leader Election](#viileader-election)
- [VIII. CRD Definition and Status Management](#viiicrd-definition-and-status-management)
- [IX. Testing Strategy](#ixtesting-strategy)
- [X. Production Deployment Best Practices](#xproduction-deployment-best-practices)

---

<!-- chunk: I. Java K8s Client Ecosystem Overview -->
## I. Java K8s Client Ecosystem Overview

```mermaid
graph TD
    A[Java K8s Development] --> B{Scenario}
    B -->|Application Integration| C[Kubernetes Client]
    B -->|Operator Development| D[Operator SDK]

    C --> C1[fabric8/kubernetes-client<br/>DSL style, easy to use]
    C --> C2[kubernetes-client/java<br/>Official Maintenance, Complete API]

    D --> D1[Java Operator SDK (JOSDK)<br/>Lightweight, Spring Boot friendly]
    D --> D2[Quarkus Operator SDK<br/>Native compilation, Low memory]

    style A fill:#22c55e,stroke:#166534,color:#fff
    style D fill:#326ce5,stroke:#1a3a8f,color:#fff
```

### 1.1 Client Comparison

| Feature | fabric8 | kubernetes-client/java |
|---------|---------|----------------------|
| **Maintainer** | Fabric8 Community | Kubernetes Official |
| **API Style** | DSL (Fluent) | Builder Pattern |
| **Type Safety** | Strong | Strong |
| **Learning Curve** | Low | Medium |
| **Extensibility** | High | High |
| **Community Activity** | High | Very High |
| **Recommended Scenario** | Daily K8s Interaction | Complex API Operations |

---

<!-- chunk: II. fabric8 Kubernetes Client -->
## II. fabric8 Kubernetes Client

### 2.1 Dependency

```xml
<dependency>
    <groupId>io.fabric8</groupId>
    <artifactId>kubernetes-client</artifactId>
    <version>6.13.4</version>
</dependency>
```

### 2.2 Basic Usage

```java
@Configuration
public class KubernetesConfig {

    @Bean
    public KubernetesClient kubernetesClient() {
        Config config = ConfigBuilder.empty()
            .withMasterUrl("https://kubernetes.default.svc")
            .withNamespace("default")
            .build();
        return new KubernetesClientBuilder().withConfig(config).build();
    }
}

@Service
public class PodService {
    private final KubernetesClient client;

    public List<String> listPods(String namespace) {
        return client.pods()
            .inNamespace(namespace)
            .list()
            .getItems()
            .stream()
            .map(pod -> pod.getMetadata().getName())
            .toList();
    }

    public Pod getPod(String namespace, String name) {
        return client.pods()
            .inNamespace(namespace)
            .withName(name)
            .get();
    }

    public Pod createPod(String namespace, Pod pod) {
        return client.pods()
            .inNamespace(namespace)
            .resource(pod)
            .create();
    }

    public Pod patchPod(String namespace, String name, Pod pod) {
        return client.pods()
            .inNamespace(namespace)
            .withName(name)
            .patch(pod);
    }

    public Boolean deletePod(String namespace, String name) {
        return client.pods()
            .inNamespace(namespace)
            .withName(name)
            .delete();
    }
}
```

### 2.3 List-Watch Example

```java
@Service
public class PodWatcher {

    public void watchPods(String namespace) {
        client.pods()
            .inNamespace(namespace)
            .watch(new Watcher<Pod>() {
                @Override
                public void eventReceived(Action action, Pod pod) {
                    String name = pod.getMetadata().getName();
                    switch (action) {
                        case ADDED -> log.info("Pod added: {}", name);
                        case MODIFIED -> log.info("Pod modified: {}", name);
                        case DELETED -> log.info("Pod deleted: {}", name);
                        case ERROR -> log.error("Pod error: {}", name);
                    }
                }

                @Override
                public void onClose(WatcherException cause) {
                    log.warn("Watch closed", cause);
                }
            });
    }
}
```

### 2.4 Transactional Operations

```java
client.apps().deployments()
    .inNamespace("production")
    .withName("spring-app")
    .edit(deployment -> new DeploymentBuilder(deployment)
        .editSpec()
            .editTemplate()
                .editSpec()
                    .editContainer(0)
                        .withImage("registry.example.com/spring-app:v2.0.0")
                    .endContainer()
                .endSpec()
            .endTemplate()
        .endSpec()
        .build());
```

---

<!-- chunk: III. Official Kubernetes Java Client -->
## III. Official Kubernetes Java Client

### 3.1 Dependency

```xml
<dependency>
    <groupId>io.kubernetes</groupId>
    <artifactId>client-java</artifactId>
    <version>20.0.1</version>
</dependency>
```

### 3.2 Basic Usage

```java
@Configuration
public class K8sConfig {

    @Bean
    public ApiClient apiClient() throws IOException {
        ApiClient client = ClientBuilder.cluster().build();
        client.setHttpClient(
            client.getHttpClient().newBuilder()
                .readTimeout(Duration.ofSeconds(30))
                .writeTimeout(Duration.ofSeconds(30))
                .build()
        );
        Configuration.setDefaultApiClient(client);
        return client;
    }
}

@Service
public class DeploymentService {
    private final AppsV1Api api;

    public V1DeploymentList listDeployments(String namespace) throws ApiException {
        return api.listNamespacedDeployment(namespace)
            .execute();
    }

    public V1Deployment patchDeployment(String namespace, String name, V1Deployment body) throws ApiException {
        return api.patchNamespacedDeployment(name, namespace, body)
            .fieldManager("java-operator")
            .force(true)
            .execute();
    }
}
```

---

<!-- chunk: IV. Java Operator SDK (JOSDK) -->
## IV. Java Operator SDK (JOSDK)

### 4.1 Dependency

```xml
<dependency>
    <groupId>io.javaoperatorsdk</groupId>
    <artifactId>operator-framework</artifactId>
    <version>4.9.5</version>
</dependency>
```

### 4.2 CRD Definition

```java
@Group("apps.example.com")
@Version("v1alpha1")
public class WebApplication extends CustomResource<WebApplicationSpec, WebApplicationStatus>
    implements Namespaced {}

public class WebApplicationSpec {
    private String image;
    private int replicas;
    private String host;
    private Map<String, String> env;

    public String getImage() { return image; }
    public void setImage(String image) { this.image = image; }
    public int getReplicas() { return replicas; }
    public void setReplicas(int replicas) { this.replicas = replicas; }
    public String getHost() { return host; }
    public void setHost(String host) { this.host = host; }
    public Map<String, String> getEnv() { return env; }
    public void setEnv(Map<String, String> env) { this.env = env; }
}

public class WebApplicationStatus {
    private boolean ready;
    private String url;
    private List<String> conditions;

    public boolean isReady() { return ready; }
    public void setReady(boolean ready) { this.ready = ready; }
    public String getUrl() { return url; }
    public void setUrl(String url) { this.url = url; }
    public List<String> getConditions() { return conditions; }
    public void setConditions(List<String> conditions) { this.conditions = conditions; }
}
```

### 4.3 Reconciler Implementation

```java
@ControllerConfiguration
public class WebApplicationReconciler
        implements Reconciler<WebApplication>,
                   ContextInitializer<WebApplication> {

    private final KubernetesClient client;

    @Override
    public UpdateControl<WebApplication> reconcile(WebApplication resource, Context<WebApplication> context) {
        String name = resource.getMetadata().getName();
        String namespace = resource.getMetadata().getNamespace();
        WebApplicationSpec spec = resource.getSpec();

        try {
            ensureDeployment(resource, spec);
            ensureService(resource, spec);
            ensureIngress(resource, spec);

            WebApplicationStatus status = new WebApplicationStatus();
            status.setReady(true);
            status.setUrl("https://" + spec.getHost());
            resource.setStatus(status);

            return UpdateControl.updateStatus(resource);

        } catch (Exception e) {
            WebApplicationStatus status = new WebApplicationStatus();
            status.setReady(false);
            status.setConditions(List.of("Error: " + e.getMessage()));
            resource.setStatus(status);
            return UpdateControl.updateStatus(resource)
                .rescheduleAfter(Duration.ofSeconds(30));
        }
    }

    private void ensureDeployment(WebApplication resource, WebApplicationSpec spec) {
        Deployment deployment = new DeploymentBuilder()
            .withNewMetadata()
                .withName(resource.getMetadata().getName())
                .withNamespace(resource.getMetadata().getNamespace())
                .addToLabels("app", resource.getMetadata().getName())
                .addToLabels("managed-by", "webapp-operator")
                .addNewOwnerReference()
                    .withApiVersion(resource.getApiVersion())
                    .withKind(resource.getKind())
                    .withName(resource.getMetadata().getName())
                    .withUid(resource.getMetadata().getUid())
                .endOwnerReference()
            .endMetadata()
            .withNewSpec()
                .withReplicas(spec.getReplicas())
                .withNewSelector()
                    .addToMatchLabels("app", resource.getMetadata().getName())
                .endSelector()
                .withNewTemplate()
                    .withNewMetadata()
                        .addToLabels("app", resource.getMetadata().getName())
                    .endMetadata()
                    .withNewSpec()
                        .addNewContainer()
                            .withName("app")
                            .withImage(spec.getImage())
                            .addNewPort()
                                .withContainerPort(8080)
                            .endPort()
                            .withNewResources()
                                .addToRequests("memory", new Quantity("256Mi"))
                                .addToRequests("cpu", new Quantity("100m"))
                                .addToLimits("memory", new Quantity("512Mi"))
                                .addToLimits("cpu", new Quantity("500m"))
                            .endResources()
                        .endContainer()
                    .endSpec()
                .endTemplate()
            .endSpec()
            .build();

        client.apps().deployments()
            .inNamespace(resource.getMetadata().getNamespace())
            .resource(deployment)
            .serverSideApply();
    }

    @Override
    public void initContext(WebApplication resource, Context<WebApplication> context) {
    }
}
```

### 4.4 Operator Startup

```java
@SpringBootApplication
public class OperatorApplication {
    public static void main(String[] args) {
        SpringApplication.run(OperatorApplication.class, args);
    }

    @Bean
    public Operator operator(KubernetesClient client) {
        Operator operator = new Operator(client);
        operator.register(new WebApplicationReconciler(client));
        return operator;
    }
}
```

---

<!-- chunk: V. Quarkus Operator SDK -->
## V. Quarkus Operator SDK

### 5.1 Dependency

```xml
<dependency>
    <groupId>io.quarkiverse.operatorsdk</groupId>
    <artifactId>quarkus-operator-sdk</artifactId>
    <version>6.8.4</version>
</dependency>
```

### 5.2 Quarkus Reconciler

```java
@ControllerConfiguration(namespaces = Constants.WATCH_CURRENT_NAMESPACE)
@ApplicationScoped
public class DatabaseReconciler implements Reconciler<Database> {

    @Inject
    KubernetesClient client;

    @Override
    public UpdateControl<Database> reconcile(Database database, Context<Database> context) {
        ensureStatefulSet(database);
        ensureService(database);
        updateStatus(database);
        return UpdateControl.updateStatus(database);
    }

    @Override
    public DeleteControl cleanup(Database database, Context<Database> context) {
        return DeleteControl.defaultDelete();
    }
}
```

### 5.3 Native Compilation

```bash
# Build native Operator
./mvnw package -Dnative \
    -Dquarkus.native.container-build=true \
    -Dquarkus.container-image.build=true \
    -Dquarkus.container-image.push=true

# Memory usage: ~30MB (vs JVM mode ~200MB)
```

---

<!-- chunk: VI. Informer and List-Watch Pattern -->
## VI. Informer and List-Watch Pattern

### 6.1 SharedInformerFactory

```java
@Configuration
public class InformerConfig {

    @Bean
    public SharedInformerFactory sharedInformerFactory(KubernetesClient client) {
        SharedInformerFactory factory = client.informers();

        factory.sharedIndexInformerFor(
            Pod.class,
            PodList.class,
            Duration.ofMinutes(5).toMillis()
        );

        return factory;
    }
}

@Component
public class PodInformer {

    @PostConstruct
    public void startWatching() {
        Indexer<Pod> indexer = informerFactory.sharedIndexInformerFor(
            Pod.class, PodList.class, 300000L
        ).getIndexer();

        informerFactory.addSharedInformerEventListener(event -> {
            log.info("Informer event: {}", event);
        });
    }
}
```

---

<!-- chunk: VII. Leader Election -->
## VII. Leader Election

### 7.1 JOSDK Leader Election

```java
@ControllerConfiguration
@LeaderElectionConfiguration(
    leaseDuration = "PT30S",
    renewalDeadline = "PT15S",
    retryPeriod = "PT5S"
)
public class MyReconciler implements Reconciler<MyResource> {
    @Override
    public UpdateControl<MyResource> reconcile(MyResource resource, Context<MyResource> context) {
        if (!context.eventSourceRetriever().isLeader()) {
            return UpdateControl.noUpdate();
        }
        return doReconcile(resource);
    }
}
```

### 7.2 K8s Deployment Configuration

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-operator
spec:
  replicas: 3
  template:
    spec:
      serviceAccountName: my-operator-sa
      containers:
        - name: operator
          image: registry.example.com/my-operator:v1.0.0
          env:
            - name: JAVA_OPTS
              value: "-XX:+UseContainerSupport -XX:MaxRAMPercentage=75.0"
          resources:
            requests: { memory: "256Mi", cpu: "100m" }
            limits: { memory: "512Mi", cpu: "500m" }
---
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-operator-sa
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: my-operator-role
rules:
  - apiGroups: ["apps.example.com"]
    resources: ["webapplications", "webapplications/status", "webapplications/finalizers"]
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
  - apiGroups: [""]
    resources: ["services", "configmaps", "secrets"]
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
  - apiGroups: ["networking.k8s.io"]
    resources: ["ingresses"]
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
  - apiGroups: ["coordination.k8s.io"]
    resources: ["leases"]
    verbs: ["get", "list", "watch", "create", "update", "patch", "delete"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: my-operator-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: my-operator-role
subjects:
  - kind: ServiceAccount
    name: my-operator-sa
```

---

<!-- chunk: VIII. CRD Definition and Status Management -->
## VIII. CRD Definition and Status Management

### 8.1 CRD Auto-Generation

```bash
# JOSDK auto-generates CRD YAML
./mvnw k8s:generate-crd

# Quarkus auto-generates
./mvnw quarkus:generate-crd
```

### 8.2 CRD Installation

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: webapplications.apps.example.com
spec:
  group: apps.example.com
  names:
    kind: WebApplication
    listKind: WebApplicationList
    plural: webapplications
    singular: webapplication
    shortNames:
      - webapp
  scope: Namespaced
  versions:
    - name: v1alpha1
      served: true
      storage: true
      subresources:
        status: {}
      schema:
        openAPIV3Schema:
          type: object
          properties:
            spec:
              type: object
              properties:
                image:
                  type: string
                replicas:
                  type: integer
                  minimum: 1
                  maximum: 100
                host:
                  type: string
              required:
                - image
                - replicas
                - host
            status:
              type: object
              properties:
                ready:
                  type: boolean
                url:
                  type: string
                conditions:
                  type: array
                  items:
                    type: string
```

---

<!-- chunk: IX. Testing Strategy -->
## IX. Testing Strategy

### 9.1 Unit Testing

```java
@ExtendWith(MockitoExtension.class)
class WebApplicationReconcilerTest {

    @Mock
    KubernetesClient client;

    @Mock
    MixedOperation<Deployment, DeploymentList, Resource<Deployment>> deploymentOp;

    WebApplicationReconciler reconciler;

    @BeforeEach
    void setup() {
        reconciler = new WebApplicationReconciler(client);
        when(client.apps().deployments()).thenReturn(deploymentOp);
        when(deploymentOp.inNamespace(anyString())).thenReturn(deploymentOp);
        when(deploymentOp.resource(any())).thenReturn(deploymentOp);
        when(deploymentOp.serverSideApply()).thenReturn(null);
    }

    @Test
    void shouldCreateDeployment() {
        WebApplication resource = createTestResource();
        UpdateControl<WebApplication> result = reconciler.reconcile(resource, mock(Context.class));
        assertTrue(result.getResource().getStatus().isReady());
    }
}
```

### 9.2 Integration Testing (JOSDK)

```java
@Testcontainers
class OperatorIntegrationTest {

    @Container
    static K3sContainer k3s = new K3sContainer(
        DockerImageName.parse("rancher/k3s:v1.30.0-k3s1")
    );

    @Test
    void shouldReconcileWebApplication() {
        Config config = new ConfigBuilder()
            .withMasterUrl(k3s.getHttpsUrl())
            .withCaCertData(k3s.getCaCert())
            .build();

        try (KubernetesClient client = new KubernetesClientBuilder()
                .withConfig(config).build()) {
            Operator operator = new Operator(client);
            operator.register(new WebApplicationReconciler(client));
            operator.start();

            WebApplication webApp = createTestResource();
            client.resource(webApp).create();

            await().atMost(30, TimeUnit.SECONDS)
                .untilAsserted(() -> {
                    WebApplication updated = client.resource(webApp).get();
                    assertTrue(updated.getStatus().isReady());
                });
        }
    }
}
```

---

<!-- chunk: X. Production Deployment Best Practices -->
## X. Production Deployment Best Practices

| Checklist Item | Configuration | Description |
|--------|------|------|
| Leader Election | `@LeaderElectionConfiguration` | Only one active replica for multiple replicas |
| RBAC Least Privilege | Limit resources + verbs | Do not use `*:*` |
| Graceful Shutdown | `preStop: sleep 10` | Ensure current Reconcile completes |
| Resource Limits | memory 256-512Mi | Operator usually lightweight |
| Structured Logging | JSON format | Convenient for log platform retrieval |
| Health Checks | `/health/live`, `/health/ready` | Operator availability |
| CRD Validation | OpenAPI v3 Schema | Prevent illegal CRD input |
| Event Recording | `client.events().create()` | K8s Event audit |
| Finalizer | Implement `Cleaner` interface | Resource cleanup |

---

<!-- chunk: 🔗 Related Documentation -->
## 🔗 Related Documentation

- [CRD Development Guide](./01-crd-development-guide.md) — CRD Fundamentals
- [Operator Development Patterns](./20-crd-operator-development.md) — Operator Design Patterns
- [Java Containerization](../domain-13-container-runtime/12-java-containerization-guide.md) — Operator Containerization
- [Java Security](../domain-05-security-compliance/99-java-security-kubernetes-guide.md) — RBAC Security

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
- Cost Optimization & FinOps

## Related

- 12-demo-env-guide
- 21-platform-selection-guide

## See Also

- 25-virtual-clusters
- 26-kubectl-plugin-ecosystem
- 99-kubernetes-v1.33-platform-ops-guide
- 01-platform-ops-overview

<!-- risk-assessed -->