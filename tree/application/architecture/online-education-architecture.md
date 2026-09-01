---
title: Online Education Platform Kubernetes Production Architecture Design (domain-20-application-patterns)
description: 'Online Education Platform Kubernetes Production Architecture Design'
summary: 'Online Education Platform Kubernetes Production Architecture Design'
category: general
tags:
- architecture
- best-practice
- redis
- kafka
- hpa
- crd
- operator
- rag
tier: core
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All engineers
estimated_read_time: 15min
intent_queries:
- What is Online Education Platform Kubernetes Production Architecture Design
- How to implement Online Education Platform Kubernetes Production Architecture Design
- Kubernetes 20 application patterns best practices
trigger_keywords:
- Online Education Platform
- Kubernetes
- Production Architecture Design
- application
- patterns
prerequisites:
- kubectl-basics
- prometheus-basics
- kafka-basics
- redis-basics
source_path: /Users/teaglebuilt/github/teaglebuilt/knowledge/tree/application/architecture/online-education-architecture.md
original_language: Chinese
---

> **Production Environment Security Notice**
>
> This document contains directly executable operations commands. Before execution, please verify: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether the commands have been tested in non-production environments. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state, but usually rollbackable), 🟢 Low risk/read-only (information gathering, no side effects).

title: Online Education Platform [[Kubernetes|Kubernetes]] Production Architecture Design
description: '# Online Education Platform Kubernetes Production Architecture Design'
category: application-architecture
tags:
- k8s
- architecture
- industry
- redis
- kafka
- hpa
- crd
- operator
- rag
last_updated: 2026-05-18
difficulty: advanced
reading_level: advanced
audience:
- Education Platform Architects
- Product Technology Leads
- SRE
estimated_read_time: 5min
intent_queries:
- Online Education Kubernetes Live Classroom
- Education Platform RTC Kubernetes Deployment
- Online Exam Anti-Cheating Kubernetes
- Interactive Whiteboard Kubernetes Real-time Synchronization
- Learning Data Recommendation System K8s
trigger_keywords:
- Online Education
- Kubernetes
- Live Classroom
- RTC
- Anti-Cheating
- Interactive Whiteboard
- Learning Recommendation
- Tekton
- HPA
related_domains:
- domain-01-cluster-fundamentals
- domain-11-production-operations
- domain-11-ai-infra
related_topics:
- 02-mini-program-architecture
- 04-im-rtc-architecture
- 48-vocational-edtech
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

# Online Education Platform Kubernetes Production Architecture Design

> **Applicable Scenarios**: K12 Education / Vocational Education / Enterprise Training / Live Classroom / Online Exam  
> **Applicable Versions**: Kubernetes v1.29 - v1.33  
> **Last Updated**: 2026-04-24  
> **Target Readers**: Education Platform Architects, Product Technology Leads

---

<!-- chunk: 📋 Table of Contents -->## 📋 Table of Contents

- [I. Overall Architecture Overview](#i-overall-architecture-overview)
- [II. Live Classroom Architecture](#ii-live-classroom-architecture)
- [III. Recorded Course Architecture](#iii-recorded-course-architecture)
- [IV. Online Exam and Anti-Cheating Architecture](#iv-online-exam-and-anti-cheating-architecture)
- [V. Interactive Whiteboard Architecture](#v-interactive-whiteboard-architecture)
- [VI. Learning Data and Recommendation Architecture](#vi-learning-data-and-recommendation-architecture)
- [VII. Content Safety and Compliance Architecture](#vii-content-safety-and-compliance-architecture)
- [VIII. K8s Deployment Architecture](#viii-k8s-deployment-architecture)

---

<!-- chunk: I. Overall Architecture Overview -->## I. Overall Architecture Overview

```mermaid
flowchart TB
    subgraph Users["User Roles"]
        STUDENT["Students<br/>Listen/Practice/Interact"]
        TEACHER["Teachers<br/>Teach/Q&A/Grade"]
        PARENT["Parents<br/>Supervise/Reports"]
        ADMIN["Administrators<br/>Courses/Users/Data"]
    end

    subgraph Frontend["Frontend Layer"]
        APP["Mobile App<br/>iOS/Android"]
        WEB["Web<br/>PC/Tablet"]
        MINI["Mini Program<br/>Lightweight Access"]
        PAD["Pad<br/>Large Screen Experience"]
    end

    subgraph Platform["Platform Services Layer"]
        LIVE["Live Service<br/>RTC / CDN"]
        VOD["Video on Demand<br/>Transcoding/Encryption/Playback"]
        CLASS["Classroom Service<br/>Attendance/Hand-raising/Q&A"]
        EXAM["Exam Service<br/>Question Generation/Anti-Cheating/Grading"]
        WHITEBOARD["Whiteboard Service<br/>Interaction/Recording"]
        MSG["Messaging Service<br/>IM / Notifications"]
    end

    subgraph Business["Business Middleware"]
        COURSE["Course Center<br/>Create/Manage/Sell"]
        USER["User Center<br/>Register/Permissions/Profiles"]
        ORDER["Order Center<br/>Payment/Refund/Reconciliation"]
        DATA["Data Center<br/>Learning Reports/Analytics"]
    end

    subgraph Infra["Infrastructure Layer"]
        DB[(Database)]
        CACHE[(Cache)]
        OSS[(Object Storage)]
        CDN[(CDN)]
    end

    Users --> Frontend --> Platform --> Business --> Infra

    style Platform fill:#e3f2fd
    style Business fill:#fff8e1
    style Infra fill:#e8f5e9
```

---

<!-- chunk: II. Live Classroom Architecture -->## II. Live Classroom Architecture

```mermaid
flowchart TB
    subgraph Teacher["Teacher Side"]
        T_CAMERA["Camera<br/>1080P"]
        T_SCREEN["Screen Share<br/>Course Materials/Code"]
        T_WHITEBOARD["Whiteboard<br/>Handwriting/Annotations"]
        T_CONTROL["Classroom Control<br/>Mute/Kick/Switch"]
    end

    subgraph MediaServer["Media Server"]
        INGEST["Stream Ingestion<br/>RTMP / WebRTC"]
        TRANSCODE["Real-time Transcoding<br/>Multi-bitrate"]
        RECORD["Recording Storage<br/>MP4 / HLS"]
        MIX["Stream Mixing<br/>Teacher+Student+Course Materials"]
    end

    subgraph Students["Student Side"]
        S1["Student 1<br/>Watch+Chat"]
        S2["Student 2<br/>On mic"]
        S3["Student 3<br/>Watch"]
        S4["Student N<br/>Watch"]
    end

    subgraph Interactive["Interaction Layer"]
        CHAT["Bullet Chat/Chat<br/>Text/Emoji"]
        QUESTION["Q&A Tool<br/>Multiple Choice/True-False"]
        RAISE_HAND["Hand Raising<br/>Mic Request"]
        REWARD["Rewards<br/>Virtual Gifts/Points"]
    end

    Teacher --> INGEST --> TRANSCODE --> Students
    INGEST --> RECORD --> OSS[(Object Storage)]
    MIX --> TRANSCODE
    Students --> Interactive
    Interactive --> MediaServer

    style MediaServer fill:#e3f2fd
    style Interactive fill:#fff8e1
```

## Live Classroom Sequence

```mermaid
sequenceDiagram
    participant Teacher as Teacher
    participant ClassSVC as Classroom Service
    participant Media as Media Service
    participant Student as Student
    participant Storage as Storage

    Teacher->>ClassSVC: Create Classroom (Create Room)
    ClassSVC->>ClassSVC: Generate Room ID + Token
    ClassSVC-->>Teacher: Return Classroom Info

    Teacher->>Media: Start Streaming (Audio/Video + Screen)
    Media-->>Teacher: Streaming Success

    Student->>ClassSVC: Join Classroom (Room ID)
    ClassSVC->>ClassSVC: Verify Course Permission
    ClassSVC-->>Student: Return Stream Pull URL

    Student->>Media: Pull Stream to Watch
    Media-->>Student: Video Stream

    Student->>ClassSVC: Send Bullet Chat
    ClassSVC->>ClassSVC: Sensitive Word Filter
    ClassSVC->>Student: Broadcast Bullet Chat

    Teacher->>ClassSVC: Start Q&A
    ClassSVC->>Student: Push Q&A Card
    Student-->>ClassSVC: Submit Answer
    ClassSVC->>Teacher: Statistics Q&A Results

    Teacher->>Media: End Streaming
    Media->>Storage: Save Recording File
    ClassSVC->>ClassSVC: Generate Classroom Report
```

---

<!-- chunk: III. Recorded Course Architecture -->## III. Recorded Course Architecture

```mermaid
flowchart TB
    subgraph Upload["Upload Processing"]
        RAW["Original Video<br/>Upload"]
        INSPECT["Quality Check<br/>Clarity/Audio/Black Screen"]
        TRANSCODE["Transcoding<br/>Multi-bitrate/Multi-format"]
        ENCRYPT["Encryption<br/>DRM / Private Protocol"]
    end

    subgraph Storage["Storage Distribution"]
        ORIGIN["Origin Storage<br/>Object Storage"]
        CDN_VIDEO["Video CDN<br/>Edge Cache"]
        P2P["P2P Acceleration<br/>Save Bandwidth"]
    end

    subgraph Player["Player"]
        ADAPTIVE["Adaptive Bitrate<br/>ABR"]
        PRELOAD["Preloading<br/>Intelligent Cache"]
        SEEK["Quick Play/Seek<br/>Keyframe Alignment"]
        WATERMARK["Watermark<br/>User ID / Dynamic"]
    end

    RAW --> INSPECT --> TRANSCODE --> ENCRYPT --> ORIGIN --> CDN_VIDEO --> P2P --> Player

    style Upload fill:#e3f2fd
    style Storage fill:#fff8e1
    style Player fill:#e8f5e9
```

## Video Encryption K8s Pipeline

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: video-processing-pipeline
  namespace: edu-media
spec:
  workspaces:
    - name: source
  params:
    - name: video-url
      type: string
    - name: course-id
      type: string
  tasks:
    - name: download
      taskSpec:
        steps:
          - name: wget
            image: alpine
            script: |
              wget $(params.video-url) -O /workspace/source/video.mp4
      workspaces:
        - name: source
          workspace: source

    - name: inspect
      runAfter: [download]
      taskSpec:
        steps:
          - name: ffprobe
            image: jrottenberg/ffmpeg:latest
            script: |
              ffprobe -v error \
                -select_streams v:0 \
                -show_entries stream=width,height,bit_rate \
                -of csv /workspace/source/video.mp4
      workspaces:
        - name: source
          workspace: source

    - name: transcode
      runAfter: [inspect]
      taskSpec:
        steps:
          - name: ffmpeg
            image: jrottenberg/ffmpeg:latest
            script: |
              # 1080p
              ffmpeg -i /workspace/source/video.mp4 \
                -c:v libx264 -crf 23 -preset fast \
                -c:a aac -b:a 128k \
                -s 1920x1080 \
                /workspace/source/1080p.mp4
              # 720p
              ffmpeg -i /workspace/source/video.mp4 \
                -c:v libx264 -crf 26 -preset fast \
                -c:a aac -b:a 96k \
                -s 1280x720 \
                /workspace/source/720p.mp4
      workspaces:
        - name: source
          workspace: source

    - name: encrypt-and-upload
      runAfter: [transcode]
      taskSpec:
        steps:
          - name: encrypt
            image: edu/video-encryptor:v1.0
            script: |
              encrypt-video \
                --input /workspace/source/ \
                --output-prefix $(params.course-id) \
                --drm fairplay-widevine
          - name: upload
            image: ossutil:latest
            script: |
              ossutil cp -r /workspace/source/ \
                oss://edu-videos/courses/$(params.course-id)/
      workspaces:
        - name: source
          workspace: source
```

---

<!-- chunk: IV. Online Exam and Anti-Cheating Architecture -->## IV. Online Exam and Anti-Cheating Architecture

```mermaid
flowchart TB
    subgraph ExamClient["Exam Client"]
        BROWSER["Browser<br/>Fullscreen Lock"]
        DESKTOP["Desktop<br/>Screen Monitoring"]
        MOBILE["Mobile<br/>App Proctoring"]
    end

    subgraph AntiCheat["Anti-Cheating System"]
        FACE["Face Recognition<br/>Liveness Detection"]
        GAZE["Gaze Tracking<br/>Abnormal Behavior"]
        AUDIO["Audio Monitoring<br/>Environment Sound Detection"]
        SCREEN["Screen Monitoring<br/>Screen Switching Detection"]
        PHONE["Phone Detection<br/>Second Device"]
        IP["IP Detection<br/>Unusual Location/Proxy"]
    end

    subgraph ExamServer["Exam Server"]
        PAPER["Smart Question Generation<br/>Random Question Sampling"]
        TIMER["Countdown<br/>Time Control"]
        ANSWER["Answer Management<br/>Auto-grading for Objective Questions"]
        SCORE["Score Statistics<br/>Analysis/Ranking"]
    end

    ExamClient --> AntiCheat --> ExamServer

    style AntiCheat fill:#ffebee
    style ExamServer fill:#e3f2fd
```

## Anti-Cheating Detection State Machine

```mermaid
stateDiagram-v2
    [*] --> Normal: Start Exam
    Normal --> Suspect: Detect Anomaly

    Suspect --> Normal: False Alarm/Recovery
    Suspect --> Warning: Anomaly Persists
    Suspect --> Flagged: Serious Violation

    Warning --> Normal: Manual Review Passes
    Warning --> Flagged: Review Fails
    Warning --> Disqualified: Multiple Warnings

    Flagged --> UnderReview: Submit for Manual Review
    Flagged --> Disqualified: Immediately Disqualify

    UnderReview --> Cleared: Review Passes
    UnderReview --> Disqualified: Review Fails

    Normal --> Completed: Exam Ends
    Cleared --> Completed
    Disqualified --> [*]: Score Voided
    Completed --> [*]: Score Valid

    style Normal fill:#c8e6c9
    style Disqualified fill:#ffebee
    style Flagged fill:#ffe0b2
```

---

<!-- chunk: V. Interactive Whiteboard Architecture -->## V. Interactive Whiteboard Architecture

```mermaid
flowchart TB
    subgraph WhiteboardCore["Whiteboard Core"]
        CANVAS["Canvas Rendering<br/>2D / WebGL"]
        SYNC["Real-time Sync<br/>OT / CRDT"]
        HISTORY["History<br/>Undo/Redo"]
        EXPORT["Export<br/>Image/PDF/SVG"]
    end

    subgraph Tools["Tool Layer"]
        PEN["Pen<br/>Multiple Strokes"]
        SHAPE["Geometric Shapes<br/>Rectangle/Circle/Line"]
        TEXT["Text<br/>Rich Text/Formula"]
        MEDIA["Media<br/>Image/Video Embedding"]
        LASER["Laser Pointer<br/>Presentation"]
    end

    subgraph Collaboration["Collaboration Layer"]
        CURSOR["Cursor Sync<br/>Multi-user Position"]
        SELECT["Selection<br/>Box Select/Move"]
        LOCK["Object Locking<br/>Permission Control"]
        RECORD["Recording Playback<br/>Classroom Playback"]
    end

    Tools --> WhiteboardCore --> Collaboration

    style WhiteboardCore fill:#e3f2fd
    style Collaboration fill:#e8f5e9
```

---

<!-- chunk: VI. Learning Data and Recommendation Architecture -->## VI. Learning Data and Recommendation Architecture

```mermaid
flowchart TB
    subgraph DataCollection["Data Collection"]
        WATCH["Watch Behavior<br/>Progress/Pause/Speed"]
        INTERACT["Interaction Behavior<br/>Q&A/Discussion/Notes"]
        TEST["Quiz Results<br/>Accuracy Rate/Time Spent"]
        ENGAGE["Engagement<br/>Login Frequency/Duration"]
    end

    subgraph Processing["Data Processing"]
        STREAM["Stream Processing<br/>Flink / Kafka Streams"]
        BATCH["Batch Processing<br/>Spark / Hive"]
        FEATURE["Feature Engineering<br/>User Profiles/Knowledge Graph"]
    end

    subgraph Intelligence["Intelligence Layer"]
        KNOWLEDGE["Knowledge Graph<br/>Concepts/Relations/Difficulty"]
        RECOMMEND["Recommendation Engine<br/>Content/Path/Teacher"]
        ADAPTIVE["Adaptive Learning<br/>Dynamic Difficulty Adjustment"]
        PREDICT["Learning Prediction<br/>Grade/Dropout Risk"]
    end

    subgraph Output["Output Application"]
        REPORT["Learning Report<br/>Parents/Teachers"]
        PATH["Learning Path<br/>Personalized Planning"]
        PUSH["Content Push<br/>Weak Point Reinforcement"]
    end

    DataCollection --> Processing --> Intelligence --> Output

    style Processing fill:#e3f2fd
    style Intelligence fill:#fff8e1
    style Output fill:#e8f5e9
```

---

<!-- chunk: VII. Content Safety and Compliance Architecture -->## VII. Content Safety and Compliance Architecture

```mermaid
flowchart TB
    subgraph ContentTypes["Content Types"]
        VIDEO["Video Content<br/>Live/Recorded"]
        AUDIO["Audio Content<br/>Voice/Music"]
        TEXT["Text Content<br/>Bullet Chat/Comments/Notes"]
        IMAGE["Image Content<br/>Avatar/Course Materials/Screenshots"]
    end

    subgraph Detection["Detection Engine"]
        ASR["Speech Recognition<br/>Sensitive Words/Violations"]
        OCR["Text Recognition<br/>Image Text"]
        NLP["Natural Language Processing<br/>Semantic Analysis"]
        CV["Computer Vision<br/>Adult/Violent/Political Content"]
    end

    subgraph Action["Action Measures"]
        BLOCK["Real-time Blocking<br/>Interrupt/Offline"]
        REVIEW["Manual Review<br/>Annotation/Confirmation"]
        WARN["Warning Alerts<br/>Rate Limit/Downgrade Rights"]
        RECORD["Record Archival<br/>Tracking/Reporting"]
    end

    ContentTypes --> Detection --> Action

    style Detection fill:#ffebee
    style Action fill:#fff8e1
```

---

<!-- chunk: VIII. K8s Deployment Architecture -->## VIII. K8s Deployment Architecture

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: edu-live-classroom
  namespace: edu-platform
spec:
  replicas: 5
  selector:
    matchLabels:
      app: edu-live-classroom
  template:
    metadata:
      labels:
        app: edu-live-classroom
    spec:
      affinity:
        podAntiAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            - labelSelector:
                matchExpressions:
                  - key: app
                    operator: In
                    values:
                      - edu-live-classroom
              topologyKey: kubernetes.io/hostname
      containers:
        - name: classroom
          image: edu/live-classroom:v2.0
          ports:
            - containerPort: 8080
            - containerPort: 9090
              name: grpc
          env:
            - name: RTC_SERVER_URL
              value: "wss://rtc.edu.com"
            - name: MAX_STUDENTS_PER_CLASS
              value: "500"
            - name: REDIS_URL
              value: "redis://redis-cluster:6379"
          resources:
            requests:
              cpu: "1"
              memory: "2Gi"
            limits:
              cpu: "4"
              memory: "8Gi"
---
# HPA Configuration (scale based on active classrooms)
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: edu-live-hpa
  namespace: edu-platform
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: edu-live-classroom
  minReplicas: 3
  maxReplicas: 50
  metrics:
    - type: Pods
      pods:
        metric:
          name: active_classrooms
        target:
          type: AverageValue
          averageValue: "10"
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

---

<!-- chunk: Reference Links -->## Reference Links

- [Agora Education Solution](https://www.agora.io/solutions/education)
- [Tencent Cloud TRTC Education](https://cloud.tencent.com/document/product/647/45458)
- [Kubernetes HPA Custom Metrics](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/)

---

<!-- chunk: Obsidian Related Documents -->## Obsidian Related Documents

- topic-application-architecture KUDIG Database — Global MOC
- [[domain-20-application-patterns/topic-application-architecture/README.md|[[Topic Application Layer Architecture Design Best Practices|Topic Application Layer Architecture Design Best Practices]]]]
- [[domain-20-application-patterns/topic-application-architecture/01-ecommerce-architecture.md|E-Commerce System Kubernetes Production Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/02-mini-program-architecture.md|Mini Program Platform Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/03-cms-architecture.md|Content Management System CMS Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/04-im-rtc-architecture.md|Real-time Communication IM/RTC Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/06-fintech-architecture.md|FinTech Kubernetes Production Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/07-iot-platform-architecture.md|IoT Platform Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/08-ai-ml-inference-architecture.md|AI/ML Inference Service Kubernetes Production Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/09-gaming-backend-architecture.md|Game Backend Kubernetes Production Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/10-social-media-architecture.md|Social Media Platform Kubernetes Production Architecture Design]]
- [[domain-20-application-patterns/topic-application-architecture/11-smart-retail-architecture.md|Smart Retail and New Retail Kubernetes Production Architecture Design]]

## See Also

- 03-cms-architecture
- 04-im-rtc-architecture
- 06-fintech-architecture
- 07-iot-platform-architecture


<!-- risk-assessed -->
