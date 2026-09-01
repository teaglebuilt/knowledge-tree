---title: IoT Platform Kubernetes Production Architecture Design
description: 'title: IoT Platform Architecture Design'
summary: 'title: IoT Platform Architecture Design'
category: general
tags:
- architecture
- best-practice
- flux
- kafka
- statefulset
- gateway
- operator
- rag
tier: core
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 15min
intent_queries:
- What is IoT Platform Kubernetes Production Architecture Design
- How to implement IoT Platform Kubernetes Production Architecture Design
- Kubernetes 20 application patterns best practices
trigger_keywords:
- IoT Platform
- Internet of Things
- Platform
- Kubernetes
- Production Architecture Design
- application
- patterns
prerequisites:
- kubectl-basics
- prometheus-basics
- kafka-basics
authors:
- name: Dillan Teagle
  role: contributor
source_path: /Users/teaglebuilt/github/teaglebuilt/knowledge/tree/application/architecture/iot-platform-architecture.md
original_language: Chinese
---

> **Production Environment Safety Notice**
>
> This document contains operational commands that can be executed directly. Before executing, confirm: the target cluster and namespace are correct; you have sufficient RBAC permissions; the command has been tested in a non-production environment. Risk levels for commands: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state but usually reversible), 🟢 Low risk/read-only (information gathering, no side effects).

title: IoT Platform Architecture Design
description: '# IoT Platform [[Kubernetes|Kubernetes]] Production Architecture Design'
category: application-architecture
tags:
- k8s
- architecture
- industry
- [[Flux|flux]]
- kafka
- [[StatefulSet|statefulset]]
- gateway
- operator
- rag
last_updated: 2026-05-18
difficulty: advanced
reading_level: advanced
audience:
- IoT Architects
- Embedded Engineers
- Platform Engineers
estimated_read_time: 5min
intent_queries:
- IoT Platform Kubernetes Device Access Architecture
- MQTT Broker EMQX Cluster Deployment
- Edge Computing KubeEdge Device Management
- Time Series Database TDengine IoT Data
- Digital Twin IoT Platform
trigger_keywords:
- IoT Platform
- Internet of Things
- MQTT
- EMQX
- Device Access
- Edge Computing
- KubeEdge
- OpenYurt
- Time Series Database
- OTA Upgrade
- Device Shadow
related_domains:
- domain-03-networking-traffic
- domain-10-troubleshooting-diagnostics
related_topics:
- topic-iot-platform-architecture
- topic-edge-computing
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
---

# IoT Platform Kubernetes Production Architecture Design

> **Applicable Scenarios**: Smart Home / Industrial IoT / Connected Vehicles / Smart Cities / Agricultural Monitoring / Energy Management
> **Applicable Versions**: Kubernetes v1.29 - v1.33
> **Last Updated**: 2026-04-24
> **Target Readers**: IoT Architects, Embedded Engineers, Platform Engineers

---

## Table of Contents

- [1. Overall Architecture Overview](#1-overall-architecture-overview)
- [2. Device Access and Authentication Architecture](#2-device-access-and-authentication-architecture)
- [3. Message Bus and Data Flow Architecture](#3-message-bus-and-data-flow-architecture)
- [4. Rule Engine and Real-Time Processing Architecture](#4-rule-engine-and-real-time-processing-architecture)
- [5. Digital Twin and Visualization Architecture](#5-digital-twin-and-visualization-architecture)
- [6. OTA Upgrade Architecture](#6-ota-upgrade-architecture)
- [7. Edge Computing Architecture](#7-edge-computing-architecture)
- [8. K8s Deployment Architecture](#8-k8s-deployment-architecture)

---

## 1. Overall Architecture Overview

```mermaid
flowchart TB
    subgraph Devices["Device Layer"]
        SENSOR["Sensors<br/>Temperature/Humidity/Light/Pressure"]
        ACTUATOR["Actuators<br/>Motors/Valves/Switches"]
        CAMERA["Cameras<br/>Images/Video"]
        VEHICLE["Vehicle Devices<br/>T-Box / OBD"]
        GATEWAY["Edge Gateway<br/>Protocol Conversion"]
    end

    subgraph Edge["Edge Layer"]
        EDGE_COMPUTE["Edge Computing<br/>KubeEdge / OpenYurt"]
        EDGE_MQTT["Edge MQTT Broker"]
        EDGE_STORE["Local Storage<br/>Offline Sync"]
    end

    subgraph Cloud["Cloud Platform Layer"]
        IOT_HUB["IoT Hub<br/>Device Access/Management"]
        RULE_ENGINE["Rule Engine<br/>Data Routing"]
        STREAM["Stream Processing<br/>Flink / Kafka"]
        TWIN["Digital Twin<br/>Device Shadow"]
    end

    subgraph Application["Application Layer"]
        DASHBOARD["Monitoring Dashboard<br/>Real-time Data"]
        ALERT["Alert Center<br/>Thresholds/Anomalies"]
        ANALYSIS["Data Analysis<br/>BI / AI"]
        CONTROL["Remote Control<br/>Command Delivery"]
    end

    subgraph DataStore["Data Storage"]
        TSDB["Time Series Database<br/>TDengine / InfluxDB"]
        HBASE["HBase<br/>Massive Device Data"]
        OSS["Object Storage<br/>Files/Logs"]
    end

    Devices --> Edge --> Cloud --> Application
    Cloud --> DataStore
    Application --> DataStore

    style Edge fill:#e3f2fd
    style Cloud fill:#fff8e1
    style Application fill:#e8f5e9
```

---

## 2. Device Access and Authentication Architecture

```mermaid
flowchart TB
    subgraph DeviceAuth["Device Authentication"]
        CERT["X.509 Certificates<br/>Mutual TLS"]
        TOKEN["Device Token<br/>HMAC-SHA256"]
        TPM["TPM Chip<br/>Hardware Security"]
        PKI["PKI System<br/>Certificate Issuance/Revocation"]
    end

    subgraph Connection["Connection Management"]
        MQTT["MQTT 3.1/5.0<br/>Publish/Subscribe"]
        COAP["CoAP<br/>Constrained Devices"]
        LORA["LoRaWAN<br/>Long-Distance Low-Power"]
        NB_IOT["NB-IoT<br/>Cellular Network"]
    end

    subgraph Management["Device Management"]
        REGISTRY["Device Registry<br/>Metadata/Status"]
        LIFECYCLE["Lifecycle<br/>Register/Activate/Disable/Revoke"]
        GROUP["Device Groups<br/>Batch Management"]
        TAG["Tag System<br/>Search/Permissions"]
    end

    DeviceAuth --> Connection --> Management

    style DeviceAuth fill:#e3f2fd
    style Connection fill:#fff8e1
    style Management fill:#e8f5e9
```

## Device Authentication Flow

```mermaid
sequenceDiagram
    participant Device as IoT Device
    participant Hub as IoT Hub
    participant CA as CA Center
    participant Registry as Device Registry

    Device->>Device: Generate Device Key Pair
    Device->>Hub: Connection Request + Device Certificate
    Hub->>CA: Verify Certificate Chain
    CA-->>Hub: Certificate Valid
    Hub->>Registry: Query Device Status
    Registry-->>Hub: Device Registered/Active
    Hub->>Hub: Generate Session Token
    Hub-->>Device: Authentication Successful + Token
    Device->>Hub: Report Data (Token Auth)
```

---

## 3. Message Bus and Data Flow Architecture

```mermaid
flowchart TB
    subgraph Ingestion["Data Ingestion"]
        MQTT_BROKER["MQTT Broker Cluster<br/>EMQX / HiveMQ / VerneMQ"]
        KAFKA_INGEST["Kafka Ingest<br/>High Throughput Buffer"]
    end

    subgraph Processing["Data Processing"]
        VALIDATE["Data Validation<br/>Format/Range/Completeness"]
        ENRICH["Data Enrichment<br/>Device Info/Location"]
        TRANSFORM["Data Transformation<br/>Unit Conversion/Aggregation"]
    end

    subgraph Routing["Data Routing"]
        HOT["Hot Data<br/>Real-time Monitoring"]
        WARM["Warm Data<br/>Analysis/Query"]
        COLD["Cold Data<br/>Archive Storage"]
    end

    subgraph Consumers["Consumers"]
        RULE["Rule Engine"]
        AI["AI Inference"]
        DB["Data Storage"]
        APP["Business Application"]
    end

    Ingestion --> Processing --> Routing --> Consumers

    style Ingestion fill:#e3f2fd
    style Processing fill:#fff8e1
    style Routing fill:#e8f5e9
```

## EMQX MQTT Broker K8s Deployment

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: emqx
  namespace: iot-platform
spec:
  serviceName: emqx-headless
  replicas: 3
  selector:
    matchLabels:
      app: emqx
  template:
    metadata:
      labels:
        app: emqx
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions:
                  - key: app
                    operator: In
                    values:
                      - emqx
              topologyKey: kubernetes.io/hostname
      containers:
        - name: emqx
          image: emqx/emqx:5.5
          ports:
            - containerPort: 1883
              name: mqtt
            - containerPort: 8883
              name: mqtts
            - containerPort: 8083
              name: ws
            - containerPort: 8084
              name: wss
            - containerPort: 18083
              name: dashboard
          env:
            - name: EMQX_NODE_NAME
              value: "emqx@$(POD_NAME).emqx-headless.iot-platform.svc.cluster.local"
            - name: EMQX_CLUSTER__DISCOVERY_STRATEGY
              value: "dns"
            - name: EMQX_CLUSTER__DNS__NAME
              value: "emqx-headless.iot-platform.svc.cluster.local"
            - name: EMQX_LISTENERS__SSL__DEFAULT__ENABLE
              value: "true"
            - name: EMQX_LISTENERS__SSL__DEFAULT__SSL_OPTIONS__CERTFILE
              value: "/etc/emqx/certs/server.crt"
            - name: EMQX_LISTENERS__SSL__DEFAULT__SSL_OPTIONS__KEYFILE
              value: "/etc/emqx/certs/server.key"
          resources:
            requests:
              cpu: "1"
              memory: "2Gi"
            limits:
              cpu: "4"
              memory: "8Gi"
          volumeMounts:
            - name: emqx-data
              mountPath: /opt/emqx/data
            - name: emqx-certs
              mountPath: /etc/emqx/certs
              readOnly: true
  volumeClaimTemplates:
    - metadata:
        name: emqx-data
      spec:
        storageClassName: fast-ssd
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 50Gi
```

---

## 4. Rule Engine and Real-Time Processing Architecture

```mermaid
flowchart TB
    subgraph Rules["Rule Definition"]
        CONDITION["Trigger Conditions<br/>Temperature>80 / Offline>5min"]
        ACTION["Execute Actions<br/>Alert/Linkage/Storage"]
        SCHEDULE["Scheduled Rules<br/>Daily Report/Scheduled Tasks"]
    end

    subgraph Execution["Rule Execution"]
        FILTER["Data Filtering<br/>SQL-like"]
        WINDOW["Time Window<br/>Sliding/Tumbling/Session"]
        AGGREGATE["Aggregate Computation<br/>AVG/SUM/COUNT"]
        JOIN["Stream Join<br/>Device/User"]
    end

    subgraph Output["Rule Output"]
        ALERT["Alert Notification<br/>DingTalk/SMS/Email"]
        COMMAND["Device Commands<br/>Remote Control"]
        FORWARD["Data Forwarding<br/>Kafka/API"]
        STORE["Data Storage<br/>DB/TSDB"]
    end

    Rules --> Execution --> Output

    style Rules fill:#e3f2fd
    style Execution fill:#fff8e1
    style Output fill:#e8f5e9
```

---

## 5. Digital Twin and Visualization Architecture

```mermaid
flowchart TB
    subgraph Physical["Physical World"]
        DEV1["Device A<br/>Running"]
        DEV2["Device B<br/>Fault"]
        DEV3["Device C<br/>Standby"]
    end

    subgraph Shadow["Device Shadow / Digital Twin"]
        SHADOW1["Shadow A<br/>Real-time State Mirror"]
        SHADOW2["Shadow B<br/>Predictive Maintenance"]
        SHADOW3["Shadow C<br/>Energy Optimization"]
    end

    subgraph Visualization["Visualization"]
        DASHBOARD["Monitoring Dashboard<br/>3D/Map/Charts"]
        DIGITAL_TWIN["Digital Twin<br/>BIM/3D Models"]
        REPORT["Report Analysis<br/>Trends/Comparison"]
    end

    Physical -->|Data Sync| Shadow --> Visualization

    style Shadow fill:#e3f2fd
    style Visualization fill:#e8f5e9
```

---

## 6. OTA Upgrade Architecture

```mermaid
flowchart TB
    subgraph Prepare["Preparation Phase"]
        BUILD["Firmware Build<br/>Compile/Sign"]
        TEST["Canary Testing<br/>Internal/Public"]
        SIGN["Firmware Signing<br/>Private Key Sign"]
        CDN_PUSH["CDN Distribution<br/>Preload"]
    end

    subgraph Rollout["Distribution Phase"]
        BATCH["Batch Strategy<br/>5% → 20% → 100%"]
        SCHEDULE["Scheduled Upgrade<br/>Off-Peak Hours"]
        FORCE["Forced Upgrade<br/>Security Patches"]
    end

    subgraph Monitor["Monitoring Phase"]
        PROGRESS["Progress Monitoring<br/>Success Rate"]
        ROLLBACK["Auto Rollback<br/>Anomaly Detection"]
        REPORT["Upgrade Report<br/>Version Distribution"]
    end

    Prepare --> Rollout --> Monitor

    style Prepare fill:#e3f2fd
    style Rollout fill:#fff8e1
    style Monitor fill:#e8f5e9
```

---

## 7. Edge Computing Architecture

```mermaid
flowchart TB
    subgraph CloudCenter["Cloud Center"]
        CLOUD_APP["Cloud Application<br/>Global Management"]
        CLOUD_AI["Cloud AI<br/>Model Training"]
        CLOUD_DB["Cloud Database<br/>Archive/Analysis"]
    end

    subgraph EdgeNodes["Edge Nodes"]
        subgraph Edge1["Edge Node 1 (Factory A)"]
            E1_APP["Edge Application<br/>Real-time Control"]
            E1_AI["Edge AI<br/>Defect Detection"]
            E1_DB["Local Storage<br/>Offline Sync"]
            E1_MQTT["Local MQTT"]
        end

        subgraph Edge2["Edge Node 2 (Factory B)"]
            E2_APP["Edge Application"]
            E2_AI["Edge AI"]
            E2_DB["Local Storage"]
            E2_MQTT["Local MQTT"]
        end
    end

    subgraph Devices["Field Devices"]
        PLC["PLC Controller"]
        ROBOT["Industrial Robot"]
        CAMERA_M["Industrial Camera"]
        SENSOR_M["Sensor Array"]
    end

    CloudCenter <-->|Control/Model Distribution| EdgeNodes
    EdgeNodes -->|Data Report| CloudCenter
    Edge1 <-->|KubeEdge| Devices
    E1_MQTT --> PLC & ROBOT & CAMERA_M & SENSOR_M

    style EdgeNodes fill:#e3f2fd
    style CloudCenter fill:#fff8e1
```

## KubeEdge Edge Node Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: edge-app-controller
  namespace: iot-edge
spec:
  replicas: 1
  selector:
    matchLabels:
      app: edge-app-controller
  template:
    metadata:
      labels:
        app: edge-app-controller
    spec:
      nodeName: edge-node-factory-a
      containers:
        - name: controller
          image: iot/edge-controller:v1.0
          env:
            - name: EDGE_NODE_ID
              value: "factory-a-line-1"
            - name: CLOUD_SYNC_INTERVAL
              value: "30"
            - name: LOCAL_MQTT_BROKER
              value: "tcp://localhost:1883"
          resources:
            requests:
              cpu: "500m"
              memory: "512Mi"
            limits:
              cpu: "2"
              memory: "2Gi"
          volumeMounts:
            - name: local-buffer
              mountPath: /data/buffer
      volumes:
        - name: local-buffer
          hostPath:
            path: /opt/edge/buffer
            type: DirectoryOrCreate
```

---

## 8. K8s Deployment Architecture

## Time Series Database TDengine Deployment

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: tdengine-dnode
  namespace: iot-platform
spec:
  serviceName: tdengine-dnode
  replicas: 3
  selector:
    matchLabels:
      app: tdengine-dnode
  template:
    metadata:
      labels:
        app: tdengine-dnode
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions:
                  - key: app
                    operator: In
                    values:
                      - tdengine-dnode
              topologyKey: kubernetes.io/hostname
      containers:
        - name: tdengine
          image: tdengine/tdengine:3.2
          ports:
            - containerPort: 6030
              name: taosd
            - containerPort: 6041
              name: rest
          env:
            - name: TAOS_FQDN
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: TAOS_FIRST_EP
              value: "tdengine-dnode-0.tdengine-dnode.iot-platform.svc.cluster.local:6030"
          resources:
            requests:
              cpu: "2"
              memory: "8Gi"
            limits:
              cpu: "8"
              memory: "32Gi"
          volumeMounts:
            - name: taos-data
              mountPath: /var/lib/taos
  volumeClaimTemplates:
    - metadata:
        name: taos-data
      spec:
        storageClassName: fast-ssd
        accessModes: ["ReadWriteOnce"]
        resources:
          requests:
            storage: 1Ti
```

---

## Reference Links

- [EMQX Documentation](https://www.emqx.io/docs/)
- [KubeEdge Documentation](https://kubeedge.io/docs/)
- [TDengine Documentation](https://docs.tdengine.com/)
- [IoT MQTT Protocol](https://mqtt.org/)

---

## Obsidian Related Documents

- topic-application-architecture MOC
- [[domain-20-application-patterns/topic-application-architecture/README.md|Topic Application Architecture Design Best Practices]]
- [[domain-20-application-patterns/topic-application-architecture/01-ecommerce-architecture.md|E-Commerce System Kubernetes Production Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/02-mini-program-architecture.md|Mini Program Platform Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/03-cms-architecture.md|CMS Content Management System Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/04-im-rtc-architecture.md|Real-Time Communication IM/RTC Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/05-online-education-architecture.md|Online Education Platform Kubernetes Production Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/06-fintech-architecture.md|FinTech Financial Technology Kubernetes Production Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/08-ai-ml-inference-architecture.md|AI/ML Inference Service Kubernetes Production Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/09-gaming-backend-architecture.md|Gaming Backend Kubernetes Production Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/10-social-media-architecture.md|Social Media Platform Kubernetes Production Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/11-smart-retail-architecture.md|Smart Retail & New Retail Kubernetes Production Architecture Design]]

## See Also

- 05-online-education-architecture
- 06-fintech-architecture
- 08-ai-ml-inference-architecture
- 09-gaming-backend-architecture


<!-- risk-assessed -->
