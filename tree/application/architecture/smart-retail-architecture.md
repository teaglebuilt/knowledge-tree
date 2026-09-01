---
title: Smart Retail and New Retail Kubernetes Production Architecture
description: Smart Retail and New Retail Kubernetes Production Architecture Design
summary: Smart Retail and New Retail Kubernetes Production Architecture
category: application-architecture
tags:
- k8s
- architecture
- industry
- prometheus
- minio
- redis
- mysql
- kafka
- ingress
- gateway
- operator
tier: core
created: '2026-05-23'
last_updated: '2026-05-18'
difficulty: advanced
reading_level: advanced
audience:
- Retail Industry Architects
- Alibaba Cloud Solutions Architects
- Omnichannel Technology Lead
- E-commerce Developers
estimated_read_time: 5min
intent_queries:
- Smart retail system Kubernetes architecture
- Omnichannel transaction cell architecture
- Store digitalization edge ACK@Edge
- Member center marketing engine
- Same-day delivery rider scheduling
trigger_keywords:
- smart retail
- new retail
- omnichannel
- cell architecture
- ACK@Edge
- member center
- same-day delivery
- livestream commerce
- unified inventory
- O2O
related_domains:
- domain-01-cluster-fundamentals
- domain-03-networking-traffic
- domain-7-observability
- domain-5-iot-edge-computing
related_topics:
- domain-20-application-patterns/topic-application-architecture/26-aviation-travel
- domain-20-application-patterns/topic-application-architecture/12-smart-logistics-architecture
- domain-20-application-patterns/topic-application-architecture/17-saas-multitenant-architecture
- domain-02-workloads-applications/topic-functions/04-high-concurrency-system
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
source_path: /Users/teaglebuilt/github/teaglebuilt/knowledge/tree/application/architecture/smart-retail-architecture.md
original_language: Chinese
---

# Smart Retail and New Retail Kubernetes Production Architecture

> **Applicable Scenarios**: Chain store digitalization / Omnichannel retail / Member center / Intelligent shopping assistant / O2O same-day delivery / Livestream commerce  
> **Cloud Provider**: Alibaba Cloud ACK + Product Ecosystem  
> **Applicable Version**: Kubernetes v1.29 - v1.33  
> **Last Updated**: 2026-04-24  
> **Target Audience**: Retail industry architects, Alibaba Cloud solutions architects, technology leads

---

<!-- chunk: Table of Contents -->## 📋 Table of Contents

- [1. Overall Architecture Overview](#1-overall-architecture-overview)
- [2. Omnichannel Transaction Architecture](#2-omnichannel-transaction-architecture)
- [3. Store Digitalization Edge Architecture](#3-store-digitalization-edge-architecture)
- [4. Member Center and Marketing Architecture](#4-member-center-and-marketing-architecture)
- [5. Same-day Delivery and Fulfillment Architecture](#5-same-day-delivery-and-fulfillment-architecture)
- [6. Livestream Commerce and Content E-commerce Architecture](#6-livestream-commerce-and-content-e-commerce-architecture)
- [7. Unified Inventory Architecture](#7-unified-inventory-architecture)
- [8. ACK Alibaba Cloud Deployment Architecture](#8-ack-alibaba-cloud-deployment-architecture)

---

<!-- chunk: 1. Overall Architecture Overview -->## 1. Overall Architecture Overview

```mermaid
flowchart TB
    subgraph Channels["Consumer Touchpoints"]
        APP["Brand App<br/>Member/Mall"]
        MINI["Alipay/WeChat Mini-app<br/>Light Transactions"]
        LIVE["Livestream Commerce<br/>Douyin/Taobao Live"]
        POS["Store POS<br/>Checkout/Redemption"]
        KIOSK["Self-service Terminals<br/>Smart Cabinet/Pickup Cabinet"]
    end

    subgraph Gateway["Alibaba Cloud Ingress Layer"]
        DNS["Cloud DNS<br/>Intelligent Routing"]
        WAF["WAF / DDoS Protection<br/>Security"]
        CDN["DCDN<br/>Dynamic Acceleration"]
        ALB["ALB<br/>Layer 7 Load Balancing"]
    end

    subgraph Platform["Business Platform (ACK)"]
        MEMBER["Member Center<br/>Unified Identity/Points/Levels"]
        GOODS["Product Center<br/>SKU/SPU/Price/Inventory"]
        ORDER["Order Center<br/>Omnichannel Orders"]
        PROMO["Marketing Center<br/>Coupons/Discounts/Group Buy"]
        PAYMENT["Payment Center<br/>Aggregated Payments"]
        DELIVERY["Fulfillment Center<br/>O2O/Express"]
    end

    subgraph Data["Data Platform"]
        REALTIME["Real-time Compute<br/>Flink / Blink"]
        OFFLINE["Offline Compute<br/>MaxCompute"]
        LABEL["Label System<br/>Damoplateform"]
        REC["Recommendation Engine<br/>PAI"]
    end

    subgraph StoreEdge["Store Edge (ACK@Edge)"]
        EDGE_GATE["Store Gateway<br/>Local Cache"]
        LOCAL_POS["Local POS<br/>Offline Checkout"]
        CAMERA["AI Camera<br/>Customer Flow/Heatmap"]
        RFID["RFID Stocktake<br/>Inventory Sensing"]
    end

    Channels --> Gateway --> Platform --> Data
    Platform --> StoreEdge
    StoreEdge -.->|Data Reporting| Platform

    style Platform fill:#e3f2fd
    style Data fill:#e8f5e9
    style StoreEdge fill:#fff8e1
```

## Alibaba Cloud Product Mapping

| Architecture Layer | Open Source/K8s Solution | Alibaba Cloud Enterprise Solution | Selection Advice |
|:---|:---|:---|:---|
| Container Platform | Self-hosted K8s | **ACK Pro** / ACK Managed | Production must choose ACK Pro, no master maintenance |
| Load Balancing | Nginx Ingress | **ALB** (Application) / MSE Gateway | Large-scale use ALB, microservices use MSE |
| Database | MySQL | **PolarDB** (one-write-multi-read) / **RDS MySQL** | High concurrent read-write use PolarDB |
| Cache | Redis Cluster | **Cloud Database Redis Enterprise** (Tair) | Persistent in-memory type suits financial-grade cache |
| Message Queue | Kafka | **Message Queue RocketMQ 5.0** / **Kafka** | Trading scenarios prioritize RocketMQ |
| Object Storage | MinIO | **OSS** + CDN | Images/videos must use OSS |
| Big Data | Spark/Flink | **MaxCompute** + **Real-time Compute Flink** | Offline+real-time integrated |
| Monitoring | Prometheus | **ARMS** + **SLS** | Full-link tracing+logs |
| Edge | KubeEdge | **ACK@Edge** | Store/warehouse edge node management |

---

<!-- chunk: 2. Omnichannel Transaction Architecture -->## 2. Omnichannel Transaction Architecture

```mermaid
flowchart TB
    subgraph Channel["Channel Orders"]
        O_APP["App Order"]
        O_MINI["Mini-app Order"]
        O_POS["Store POS Order"]
        O_LIVE["Livestream Order"]
    end

    subgraph Router["Order Routing (MSE Cloud Native Gateway)"]
        ROUTE_APP["App Routing<br/>High Concurrency Distribution"]
        ROUTE_MINI["Mini-app Routing<br/>Rate Limiting Protection"]
        ROUTE_POS["POS Routing<br/>Store Priority"]
        ROUTE_LIVE["Livestream Routing<br/>Burst Scaling"]
    end

    subgraph Core["Trading Core (Cell Architecture)"]
        UNIT_A["Cell A<br/>East China Users"]
        UNIT_B["Cell B<br/>North China Users"]
        UNIT_C["Cell C<br/>South China Users"]
    end

    subgraph Storage["Data Layer"]
        POLARDB["PolarDB<br/>One Primary Multi-Replica"]
        REDIS["Tair<br/>Inventory/Session"]
        MQ["RocketMQ<br/>Order Events"]
    end

    O_APP --> ROUTE_APP --> UNIT_A
    O_MINI --> ROUTE_MINI --> UNIT_B
    O_POS --> ROUTE_POS --> UNIT_C
    O_LIVE --> ROUTE_LIVE --> UNIT_A
    UNIT_A & UNIT_B & UNIT_C --> POLARDB & REDIS & MQ

    style Core fill:#e3f2fd
    style Storage fill:#e8f5e9
```

## Cell Architecture Order Service ACK Deployment

```yaml
# Cell Architecture: Route to different cells by user ID sharding
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service-unit-a
  namespace: retail-unit-a
  labels:
    unit: a
    region: east-china
spec:
  replicas: 10
  selector:
    matchLabels:
      app: order-service
      unit: a
  template:
    metadata:
      labels:
        app: order-service
        unit: a
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
              - matchExpressions:
                  - key: topology.kubernetes.io/zone
                    operator: In
                    values:
                      - cn-hangzhou-a
                      - cn-hangzhou-b
                      - cn-hangzhou-c
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              podAffinityTerm:
                labelSelector:
                  matchExpressions:
                    - key: app
                      operator: In
                      values:
                        - order-service
                topologyKey: kubernetes.io/hostname
      containers:
        - name: order
          image: registry.cn-hangzhou.aliyuncs.com/retail/order-service:v2.1.0
          ports:
            - containerPort: 8080
          env:
            - name: UNIT_ID
              value: "A"
            - name: DB_HOST
              value: "pc-bp1xxxxxxxxxxxxx.mysql.polardb.rds.aliyuncs.com"
            - name: DB_NAME
              value: "retail_order_a"
            - name: REDIS_HOST
              value: "r-bp1xxxxxxxxxxxxx.redis.rds.aliyuncs.com"
            - name: ROCKETMQ_ENDPOINT
              value: "http://MQ_INST_xxxxxxx.cn-hangzhou.mq-internal.aliyuncs.com:8080"
            - name: ALICLOUD_ACCESS_KEY
              valueFrom:
                secretKeyRef:
                  name: alicloud-credentials
                  key: access-key-id
          resources:
            requests:
              cpu: "1"
              memory: "2Gi"
            limits:
              cpu: "4"
              memory: "8Gi"
          livenessProbe:
            httpGet:
              path: /health/live
              port: 8080
            initialDelaySeconds: 30
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /health/ready
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 5
---
# MSE Cloud Native Gateway Routing Rules
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: retail-order-ingress
  namespace: retail
  annotations:
    alb.ingress.kubernetes.io/scheme: internet
    alb.ingress.kubernetes.io/listen-ports: '[{"HTTPS":443}]'
    alb.ingress.kubernetes.io/certificate-ids: "cert-xxxxxx"
    alb.ingress.io/routing-policy: "weighted"
spec:
  ingressClassName: alb
  rules:
    - host: api.retail.example.com
      http:
        paths:
          - path: /order
            pathType: Prefix
            backend:
              service:
                name: order-service-unit-a
                port:
                  number: 8080
```

---

<!-- chunk: 3. Store Digitalization Edge Architecture -->## 3. Store Digitalization Edge Architecture

```mermaid
flowchart TB
    subgraph Cloud["Alibaba Cloud Center"]
        ACK_PRO["ACK Pro<br/>Hangzhou/Shanghai"]
        POLARDB_CORE["PolarDB<br/>Core DB"]
        SLS_CENTER["SLS<br/>Log Center"]
    end

    subgraph Edge["Store Edge (ACK@Edge)"]
        subgraph Store1["Store 1 (Shanghai Jing'an)"]
            E1_GATE["Edge Gateway<br/>Local Routing"]
            E1_POS["POS Terminal<br/>Offline Checkout"]
            E1_CAM["AI Camera<br/>Customer Flow Analysis"]
            E1_DB["SQLite<br/>Local Cache"]
        end

        subgraph StoreN["Store N (Beijing Chaoyang)"]
            EN_GATE["Edge Gateway"]
            EN_POS["POS Terminal"]
            EN_CAM["AI Camera"]
            EN_DB["SQLite"]
        end
    end

    Cloud <-->|Control/Config Deployment| Edge
    Edge -->|Data Reporting| Cloud
    E1_POS --> E1_DB --> E1_GATE
    E1_CAM --> E1_GATE
    EN_POS --> EN_DB --> EN_GATE
    EN_CAM --> EN_GATE

    style Cloud fill:#e3f2fd
    style Edge fill:#e8f5e9
```

## ACK@Edge Store Gateway Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: store-edge-gateway
  namespace: retail-edge
spec:
  replicas: 1
  selector:
    matchLabels:
      app: store-edge-gateway
  template:
    metadata:
      labels:
        app: store-edge-gateway
    spec:
      nodeName: edge-node-store-001  # ACK@Edge edge node
      hostNetwork: true
      containers:
        - name: gateway
          image: registry.cn-hangzhou.aliyuncs.com/retail/edge-gateway:v1.0
          ports:
            - containerPort: 8080
              hostPort: 8080
            - containerPort: 8443
              hostPort: 8443
          env:
            - name: STORE_ID
              value: "SH-JINGAN-001"
            - name: CLOUD_SYNC_INTERVAL
              value: "30"
            - name: OFFLINE_MODE
              value: "auto"  # Auto switch to offline mode on network loss
            - name: LOCAL_DB_PATH
              value: "/data/store.db"
            - name: CLOUD_API_ENDPOINT
              value: "https://api.retail.example.com"
          resources:
            requests:
              cpu: "500m"
              memory: "1Gi"
            limits:
              cpu: "2"
              memory: "4Gi"
          volumeMounts:
            - name: local-data
              mountPath: /data
            - name: edge-certs
              mountPath: /certs
              readOnly: true
      volumes:
        - name: local-data
          hostPath:
            path: /opt/retail/data
            type: DirectoryOrCreate
        - name: edge-certs
          secret:
            secretName: store-edge-certs
```

---

<!-- chunk: 4. Member Center and Marketing Architecture -->## 4. Member Center and Marketing Architecture

```mermaid
flowchart TB
    subgraph MemberData["Member Data"]
        PROFILE["Member Profile<br/>Basic Info"]
        BEHAVIOR["Behavior Data<br/>Browse/Purchase/Interact"]
        ASSET["Member Assets<br/>Points/Coupons/Balance"]
        TAGS["Label System<br/>RFM / Preferences"]
    end

    subgraph Engine["Marketing Engine"]
        SEGMENT["Audience Segmentation<br/>Rules/Models"]
        RULE["Rule Engine<br/>if-this-then-that"]
        AB_TEST["A/B Testing<br/>Strategy Comparison"]
        OPTIMIZE["Intelligent Optimization<br/>Send Time/Channel"]
    end

    subgraph Channels["Reach Channels"]
        PUSH["App Push<br/>Jiguang/Youmeng"]
        SMS["SMS<br/>Alibaba Cloud SMS"]
        MINI_MSG["Mini-app Subscribe Messages"]
        DM["In-app Messages<br/>App/Web"]
    end

    MemberData --> Engine --> Channels

    style MemberData fill:#e3f2fd
    style Engine fill:#fff8e1
    style Channels fill:#e8f5e9
```

---

<!-- chunk: 5. Same-day Delivery and Fulfillment Architecture -->## 5. Same-day Delivery and Fulfillment Architecture

```mermaid
flowchart TB
    subgraph Order["Order Trigger"]
        USER_ORDER["User Order<br/>Takeout/Fresh"]
        ALLOCATE["Order Allocation<br/>Store/Warehouse"]
    end

    subgraph Dispatch["Dispatch System"]
        RIDER_POOL["Rider Pool<br/>Real-time Location"]
        MATCH_ALG["Matching Algorithm<br/>Distance/Load/Rating"]
        ROUTE_OPT["Route Optimization<br/>Multi-order Merging"]
    end

    subgraph Fulfill["Fulfillment Execution"]
        PICKING["Picking/Packing<br/>Store/Forward Warehouse"]
        DELIVERY["In-transit<br/>Real-time Trajectory"]
        COMPLETE["Delivery Confirmation<br/>Photo/Signature"]
    end

    subgraph Monitor["Monitoring"]
        ETA["ETA Prediction<br/>Estimated Delivery Time"]
        ALERT["Anomaly Alert<br/>Timeout/Cancellation"]
    end

    Order --> Dispatch --> Fulfill --> Monitor

    style Dispatch fill:#e3f2fd
    style Fulfill fill:#e8f5e9
```

---

<!-- chunk: 6. Livestream Commerce and Content E-commerce Architecture -->## 6. Livestream Commerce and Content E-commerce Architecture

```mermaid
flowchart TB
    subgraph LiveRoom["Livestream Room"]
        ANCHOR["Streamer<br/>Streaming/Beauty/Product Explanation"]
        GOODS_SHOW["Product Showcase<br/>Real-time Shelving/Inventory"]
        COUPON["Livestream Coupon<br/>Limited Time Release"]
    end

    subgraph Media["Media Layer (Alibaba Cloud Video)"]
        RTS["RTS<br/>Ultra-low Latency Live"]
        TRANSCODE["Real-time Transcoding<br/>Multi-quality"]
        RECORD["Record Replay<br/>Highlight Clips"]
    end

    subgraph Interaction["Interaction Layer"]
        DANMU["Barrage<br/>Real-time Filtering"]
        LIKE["Likes/Gifts<br/>Animation Effects"]
        SECKILL["Livestream Flash Sale<br/>Inventory Deduction"]
    end

    subgraph Commerce["Transaction Layer"]
        SNAP_UP["Rush Purchase<br/>High Concurrency"]
        PAY["Payment<br/>Aggregated"]
        ORDER_LIVE["Order<br/>Livestream-specific Mark"]
    end

    LiveRoom --> Media --> Interaction --> Commerce

    style Media fill:#e3f2fd
    style Interaction fill:#fff8e1
    style Commerce fill:#e8f5e9
```

---

<!-- chunk: 7. Unified Inventory Architecture -->## 7. Unified Inventory Architecture

```mermaid
flowchart TB
    subgraph InventorySources["Inventory Sources"]
        STORE_STOCK["Store Inventory<br/>Real-time per Store"]
        WAREHOUSE["Regional Warehouse<br/>RDC/CDC"]
        VENDOR["Supplier<br/>VMI"]
        IN_TRANSIT["In-transit Inventory<br/>Transfer in Progress"]
    end

    subgraph Unified["Unified Inventory"]
        POOL["Inventory Pool<br/>Logical Aggregation"]
        RULE["Inventory Rules<br/>Allocation/Reserve/Safety Stock"]
        SYNC["Real-time Sync<br/>Change Events"]
    end

    subgraph Allocation["Inventory Allocation"]
        ONLINE["Online Order<br/>Nearest Store Ship"]
        OFFLINE["Store Retail<br/>Real-time Deduction"]
        TRANSFER["Transfer<br/>Between Stores/Warehouses"]
    end

    InventorySources --> Unified --> Allocation

    style Unified fill:#e3f2fd
    style Allocation fill:#e8f5e9
```

---

<!-- chunk: 8. ACK Alibaba Cloud Deployment Architecture -->## 8. ACK Alibaba Cloud Deployment Architecture

## Multi-AZ High Availability Architecture

```mermaid
flowchart TB
    subgraph ACKCluster["ACK Pro Cluster (Hangzhou)"]
        subgraph AZ_A["Availability Zone A"]
            NODE_A1["Worker Node"]
            NODE_A2["Worker Node"]
            NODE_A3["Worker Node"]
        end

        subgraph AZ_B["Availability Zone B"]
            NODE_B1["Worker Node"]
            NODE_B2["Worker Node"]
            NODE_B3["Worker Node"]
        end

        subgraph AZ_C["Availability Zone C"]
            NODE_C1["Worker Node"]
            NODE_C2["Worker Node"]
            NODE_C3["Worker Node"]
        end

        MASTER["Managed Master<br/>3-node HA"]
    end

    subgraph Database["Database Layer"]
        POLARDB_MASTER["PolarDB Primary<br/>AZ-A"]
        POLARDB_REPLICA_A["Replica A<br/>AZ-B"]
        POLARDB_REPLICA_B["Replica B<br/>AZ-C"]
    end

    subgraph Storage["Storage Layer"]
        OSS_HZ["OSS Hangzhou"]
        OSS_SH["OSS Shanghai<br/>Cross-region Replication"]
    end

    MASTER --> AZ_A & AZ_B & AZ_C
    AZ_A & AZ_B & AZ_C --> POLARDB_MASTER
    POLARDB_MASTER --> POLARDB_REPLICA_A & POLARDB_REPLICA_B
    AZ_A & AZ_B & AZ_C --> OSS_HZ --> OSS_SH

    style ACKCluster fill:#e3f2fd
    style Database fill:#e8f5e9
```

## ACK Cluster Node Pool Configuration

```yaml
# ACK Cluster Node Pool Configuration (Alibaba Cloud)
apiVersion: apps/v1
kind: Deployment
metadata:
  name: retail-core-service
  namespace: retail
spec:
  replicas: 12
  selector:
    matchLabels:
      app: retail-core
  template:
    metadata:
      labels:
        app: retail-core
    spec:
      topologySpreadConstraints:
        - maxSkew: 1
          topologyKey: topology.kubernetes.io/zone
          whenUnsatisfiable: DoNotSchedule
          labelSelector:
            matchLabels:
              app: retail-core
      affinity:
        podAntiAffinity:
          preferredDuringSchedulingIgnoredDuringExecution:
            - weight: 100
              podAffinityTerm:
                labelSelector:
                  matchExpressions:
                    - key: app
                      operator: In
                      values:
                        - retail-core
                topologyKey: kubernetes.io/hostname
      containers:
        - name: core
          image: registry.cn-hangzhou.aliyuncs.com/retail/core-service:v2.0
          ports:
            - containerPort: 8080
          env:
            - name: SPRING_PROFILES_ACTIVE
              value: "production,aliyun"
            - name: DB_URL
              valueFrom:
                secretKeyRef:
                  name: retail-db-secret
                  key: url
          resources:
            requests:
              cpu: "2"
              memory: "4Gi"
            limits:
              cpu: "8"
              memory: "16Gi"
---
# Alibaba Cloud ARMS Application Monitoring
apiVersion: arms.aliyun.com/v1beta1
kind: ArmsApplicationMonitor
metadata:
  name: retail-core-monitor
  namespace: retail
spec:
  appName: retail-core-service
  language: java
  agentVersion: "3.0"
  enable: true
  configs:
    - name: sampling_rate
      value: "10"
```

---

<!-- chunk: Reference Links -->## Reference Links

- [Alibaba Cloud ACK Documentation](https://www.aliyun.com/product/kubernetes)
- [Alibaba Cloud PolarDB](https://www.aliyun.com/product/polardb)
- [Alibaba Cloud MSE Microservice Engine](https://www.aliyun.com/product/aliware/mse)
- [New Retail Solution](https://www.aliyun.com/solution/newretail)

---

<!-- chunk: Obsidian Related Documents -->## Obsidian Related Documents

- topic-application-architecture MOC
- [[domain-20-application-patterns/topic-application-architecture/README.md|Topic Application Architecture Design Best Practices]]
- [[domain-20-application-patterns/topic-application-architecture/01-ecommerce-architecture.md|E-commerce System Kubernetes Production Architecture]]
- [[domain-20-application-patterns/topic-application-architecture/02-mini-program-architecture.md|Mini-program Platform Architecture]]
- [[domain-20-application-patterns/topic-application-architecture/03-cms-architecture.md|CMS Architecture]]
- [[domain-20-application-patterns/topic-application-architecture/04-im-rtc-architecture.md|Real-time Communication IM/RTC Architecture]]
- [[domain-20-application-patterns/topic-application-architecture/05-online-education-architecture.md|Online Education Platform Kubernetes Architecture]]
- [[domain-20-application-patterns/topic-application-architecture/06-fintech-architecture.md|FinTech Kubernetes Architecture]]
- [[domain-20-application-patterns/topic-application-architecture/07-iot-platform-architecture.md|IoT Platform Architecture]]
- [[domain-20-application-patterns/topic-application-architecture/08-ai-ml-inference-architecture.md|AI/ML Inference Service Kubernetes Architecture]]
- [[domain-20-application-patterns/topic-application-architecture/09-gaming-backend-architecture.md|Gaming Backend Kubernetes Architecture]]
- [[domain-20-application-patterns/topic-application-architecture/10-social-media-architecture.md|Social Media Platform Kubernetes Architecture]]

## See Also

- 09-gaming-backend-architecture
- 10-social-media-architecture
- 12-smart-logistics-architecture
- 13-digital-government-architecture

<!-- risk-assessed -->
