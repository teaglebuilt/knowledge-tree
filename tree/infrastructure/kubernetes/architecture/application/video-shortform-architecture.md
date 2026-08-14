---
Title: Kubernetes Production Architecture Design for Audio, Video and Short Video Platforms
Description: Title: Audio/Video and Short Video Platform Architecture Design
Summary: 'Title: Audio/Video and Short Video Platform Architecture Design'
category: general
tags:
- architecture
- best-practice
- docker
- redis
- hpa
- operator
- rag
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All Engineers
estimated_read_time: 15min
intent_queries:
What is the production architecture design for Kubernetes, an audio/video and short video platform?
- How to design a Kubernetes production architecture for audio/video and short video platforms
- Best Practices for Kubernetes 20 Application Patterns
trigger_keywords:
- Audio and video and short video platforms
- Kubernetes
- Production Architecture Design
- application
- patterns
prerequisites:
- kubectl-basics
- prometheus-basics
- redis-basics
---

# Production Architecture Design for Kubernetes Audio/Video and Short Video Platforms

**Applicable Scenarios:** Short video platforms / Long video on demand / Live streaming / Audio and video calls / Cloud editing / Digital humans  
**Cloud Provider:** Alibaba Cloud ACK + Video Cloud Product System  
**Applicable Versions:** Kubernetes v1.29 - v1.33  
Last updated: 2026-04-24  
**Target Audience:** Audio/video architects, CDN experts, Alibaba Cloud solution architects

---

<!-- chunk: I. Overall Architecture Overview-->## I. Overall Architecture Overview

```mermaid
flowchart TB
    subgraph Creators
        Upload video to mobile/PC using UPLOADER.
        LIVE_STREAMER["Broadcaster<br />OBS/Mobile"]
        EDITOR ["Cloud Editing, Online Editing"]
    end

    subgraph MediaCloud["Media Cloud Service (Alibaba Cloud)"]
        VOD_PROC["On-demand processing<br />Transcoding/Watermarking/Encryption"]
        LIVE_PROC["Live Streaming Processing<br />RTS/Transcoding/Recording"]
        AI_MED["Media AI Review/Tags/Summary"]
        CDN_MED["CDN Distribution<br />Global Acceleration"]
    end

    subgraph Platform["Platform Service (ACK)"]
        FEED_VIDEO["Feed Recommendations<br />Personalized"]
        COMMENT["Comment System<br />Bullet Screen/Interaction"]
        SOCIAL_VIDEO["Social Follow/Private Messages"]
        MONETIZE_VIDEO["Monetization<br />Advertising/E-commerce/Tipping"]
    end

    subgraph Consumers ["Consumers"]
        MOBILE_VIEWER["Mobile App/Mini Program"]
        WEB_VIEWER["Web Client<br />PC/Tablet"]
        TV_VIEWER["TV End<br />OTT/Casting"]
    end

    Creators --> MediaCloud --> Platform --> Consumers

    style MediaCloud fill:#e3f2fd
    style Platform fill:#fff8e1
```

## Alibaba Cloud Product Mapping

| Architecture Layer | Alibaba Cloud Solution | Description |
|:---|:---|:---|
| Container Platform | **ACK Pro** | Hosted Business Services |
Video on Demand (VOD) | Upload/Storage/Transcoding/Distribution |
| Live Streaming | **Video Live Streaming** | Push Streaming/Pull Streaming/RTS/Recording |
Real-time audio and video | **Audio and video communication RTC** | Multi-person video conferencing/interaction |
| CDN | **CDN** + **DCDN** | Static + Dynamic Acceleration |
| Media Processing | **Intelligent Media Service (IMS)** | AI Review/Tags/Summary |
Object Storage | **OSS** | Media Asset Storage |
| Message Queues | **RocketMQ** | Asynchronous Processing |
Big Data | MaxCompute + PAI | Recommendation/Analysis |

---

<!-- chunk: II. Short Video Production and Distribution Architecture-->## II. Short Video Production and Distribution Architecture

```mermaid
flowchart TB
    Subgraph Production [Content Production]
        CAPTURE ["Shooting Filters/Beauty"]
        EDIT["editing<br />beat matching/subtitles/effects"]
        MUSIC ["Soundtrack<br />Copyright Music Library"]
        UPLOAD_VIDEO["Upload with resume capability"]
    end

    Subgraph Processing [Cloud Processing]
        INSPECT["Content Moderation: Machine Review + Human Review"]
        TRANSCODE_VIDEO["Transcoding<br />Multi-resolution"]
        EXTRACT["Feature Extraction<br />Label/Cover/Fingerprint"]
        ENCRYPT_VIDEO["Encryption<br />DRM/Private"]
    end

    subgraph Distribution["distribution"]]
        REC_VIDEO["Recommendation Engine<br />Cold Start/Interest"]
        CDN_PUSH["CDN preheating<br />Hotspot push"]
        P2P ["P2P acceleration<br />Saves bandwidth"]
    end

    Production --> Processing --> Distribution

    style Production fill:#e3f2fd
    style Processing fill:#fff8e1
    style Distribution fill:#e8f5e9
```

---

<!-- chunk: III. Live Streaming Push-Pull Architecture-->## III. Live Streaming Push-Pull Architecture

```mermaid
flowchart TB
    subgraph Publisher["streaming end"]]
        OBS ["OBS / Professional Equipment"]
        MOBILE_LIVE["Mobile Live Streaming"]
        WEB_LIVE["Web 推流<br">WHIP"]
    end

    subgraph Ingestion["Access Layer"]]
        RTMP_INGEST["RTMP Access"]
        SRT_INGEST["SRT Access Low Latency"]
        WEBRTC_INGEST["WebRTC Access<br />Ultra-low latency"]
    end

    subgraph ProcessingLive["processing layer"]
        TRANSCODE_LIVE["Real-time transcoding<br />Multi-bitrate"]
        RECORD_LIVE["Recording<br />Time-shift/Playback"]
        AI_LIVE["AI processing<br />beauty/virtual background"]
    end

    subgraph DistributionLive["distribution layer"]
        HLS_LIVE["HLS<br>iOS/General"]
        FLV_LIVE["HTTP-FLV Low Latency"]
        RTS_LIVE["RTS<br />Alibaba Cloud Ultra-Low Latency"]
        WEBRTC_LIVE["WebRTC<br"><1s delay"]
    end

    Publisher --> Ingestion --> ProcessingLive --> DistributionLive

    style Ingestion fill:#e3f2fd
    style ProcessingLive fill:#fff8e1
    style DistributionLive fill:#e8f5e9
```

---

<!-- chunk: IV. Audio and Video Processing Pipeline Architecture --> ## IV. Audio and Video Processing Pipeline Architecture

```mermaid
flowchart TB
    subgraph Input["Input"]
        RAW_VIDEO["Original Video"]
        RAW_AUDIO["raw audio"]
        SUBTITLE["subtitle file"]
    end

    subgraph Pipeline ["Processing Pipeline (Tekton)"]
        DEMUX["Decompress MP4/MKV/FLV"]
        VIDEO_ENCODE["Video encoding: H.264/H.265/AV1"]
        AUDIO_ENCODE["Audio encoding<br>AAC/OPUS"]
        PACKAGE["packaged as DASH/HLS/MP4"]
        DRM["DRM encryption<br />Widevine/FairPlay"]
    end

    subgraph Output["output"]
        MP4_OUT["MP4 Download"]
        HLS_OUT["HLS<br">iOS"]
        DASH_OUT["DASH<br">Android/Web"]
        AUDIO_ONLY["Pure Audio Radio/Podcast"]
    end

    Input --> Pipeline --> Output

    style Pipeline fill:#e3f2fd
    style Output fill:#e8f5e9
```

## Video Processing K8s Pipeline

```yaml
apiVersion: tekton.dev/v1beta1
kind: Pipeline
metadata:
  name: video-processing-pipeline
  namespace: media-platform
spec:
  workspaces:
    - name: source
    - name: docker-config
  params:
    - name: input-url
      type: string
    - name: output-prefix
      type: string
  tasks:
    - name: download
      taskSpec:
        steps:
          - name: wget
            image: alpine
            script: |
              wget $(params.input-url) -O /workspace/source/input.mp4
      workspaces:
        - name: source
          workspace: source

    - name: transcode-multi-bitrate
      runAfter: [download]
      taskSpec:
        steps:
          - name: ffmpeg
            image: jrottenberg/ffmpeg:6.0-alpine
            script: |
              # 1080p
              ffmpeg -i /workspace/source/input.mp4 \
                -c:v libx264 -crf 23 -preset fast \
                -c:a aac -b:a 128k \
                -s 1920x1080 \
                /workspace/source/1080p.mp4
              # 720p
              ffmpeg -i /workspace/source/input.mp4 \
                -c:v libx264 -crf 26 -preset fast \
                -c:a aac -b:a 96k \
                -s 1280x720 \
                /workspace/source/720p.mp4
              # 480p
              ffmpeg -i /workspace/source/input.mp4 \
                -c:v libx264 -crf 28 -preset fast \
                -c:a aac -b:a 64k \
                -s 854x480 \
                /workspace/source/480p.mp4
      workspaces:
        - name: source
          workspace: source

    - name: package-hls
      runAfter: [transcode-multi-bitrate]
      taskSpec:
        steps:
          - name: hls-packager
            image: google/shaka-packager:latest
            script: |
              packager \
                'in=/workspace/source/1080p.mp4,stream=video,init_segment=1080p_init.mp4,segment_template=1080p_$Number$.m4s' \
                'in=/workspace/source/720p.mp4,stream=video,init_segment=720p_init.mp4,segment_template=720p_$Number$.m4s' \
                'in=/workspace/source/480p.mp4,stream=video,init_segment=480p_init.mp4,segment_template=480p_$Number$.m4s' \
                'in=/workspace/source/1080p.mp4,stream=audio,init_segment=audio_init.mp4,segment_template=audio_$Number$.m4s' \
                --mpd_output manifest.mpd \
                --hls_master_playlist_output master.m3u8
      workspaces:
        - name: source
          workspace: source

    - name: upload-to-oss
      runAfter: [package-hls]
      taskSpec:
        steps:
          - name: oss-upload
            image: registry.cn-hangzhou.aliyuncs.com/aliyun/ossutil:latest
            script: |
              ossutil cp -r /workspace/source/ \
                oss://media-bucket/processed/$(params.output-prefix)/
      workspaces:
        - name: source
          workspace: source
```

---

<!-- chunk: V. Recommendation and Personalized Distribution Architecture-->## V. Recommendation and Personalized Distribution Architecture

```mermaid
flowchart TB
    subgraph RecallLayer["Recall Layer"]
        CF["Collaborative Filtering<br />User Similarity"]
        CONTENT_BASED["Similar content<br>tags/Embedding"]
        HOT["Popular/Trending<br />Global/Regional"]
        FOLLOW_REC["Follow Stream<br />Time Sequence"]
    end

    subgraph RankLayer["Ranking Layer"]
        FEATURE["Feature concatenation<br />User/Content/Context"]
        DEEP_MODEL["Depth Model<br>DIN/DIEN"]
        MULTI_TASK["Multi-target<br />Play/Like/Follow"]
    end

    subgraph ReRank["reordering"]]
        DIVERSITY ["Diversity<br />Disrupt/Explore"]
        FRESHNESS ["Freshness and support for new content"]
        QUALITY ["Quality Filtering<br />Vulgar/Repetitive"]
        AD_INSERT["Ad Insertion Frequency Control"]
    end

    RecallLayer --> RankLayer --> ReRank

    style RecallLayer fill:#e3f2fd
    style RankLayer fill:#fff8e1
    style ReRank fill:#e8f5e9
```

---

<!-- chunk: VI. Real-time Interaction and Co-op Architecture --> ## VI. Real-time Interaction and Co-op Architecture

```mermaid
flowchart TB
    subgraph Interaction ["interactive format"]
        DANMU_VIDEO["Danmu ..."["Danmu_VIDEO"["Danmu_VIDEO"["Danmu_VIDEO
        GIFT["Gift Animation Effects"]
        LIKE_ANI["Like animation"]
        CO_HOST["A viewer joins the live stream"]
        PK ["PK battles across rooms"]
    end

    subgraph Signaling
        WS_SIGNAL["WebSocket state synchronization"]
        ROOM_MGMT["Room Management<br />Entry/Exit/Microphone Position"]
        PERMISSION["Permissions<br />Mute/Kick"]
    end

    subgraph MediaMedia["media"]
        MIXER ["mixing audio and video<br />merging"]
        EFFECT ["Special Effects<br />Beauty/Voice Changer"]
        RECORD_INT["Record<br />Highlights"]
    end

    Interaction --> Signaling --> MediaMedia

    style Signaling fill:#e3f2fd
    style MediaMedia fill:#e8f5e9
```

---

<!-- chunk: VII. Copyright Protection and Content Moderation Architecture --> ## VII. Copyright Protection and Content Moderation Architecture

```mermaid
flowchart TB
    subgraph UploadCheck["Upload Detection"]
        FINGERPRINT["Fingerprint Extraction<br />Video/Audio"]
        COMPARE_DB["Fingerprint Comparison Copyright Database"]
        DUPLICATE["Duplicate Detection<br />Internal Duplicate Check"]
    end

    subgraph ContentCheck["Content Moderation"]
        VIDEO_CHECK["Video Review<br />Frame Sampling + OCR"]
        AUDIO_CHECK["Audio Review<br />ASR+Semantic"]
        COMMENT_CHECK["Comment moderation NLP"]
    end

    subgraph ActionCheck["handle"]
        BLOCK_VIDEO["Block<br />Prevent posting"]
        LIMIT["Restrict visibility to only myself"]
        PASS_VIDEO["Normal release passed"]
        APPEAL ["Appeal<br />Manual Review"]
    end

    UploadCheck --> ContentCheck --> ActionCheck

    style UploadCheck fill:#e3f2fd
    style ContentCheck fill:#ffebee
    style ActionCheck fill:#e8f5e9
```

---

<!-- chunk: VIII. ACK Alibaba Cloud Deployment Architecture --> ## VIII. ACK Alibaba Cloud Deployment Architecture

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: video-recommendation-service
  namespace: media-platform
spec:
  replicas: 20
  selector:
    matchLabels:
      app: video-recommendation
  template:
    metadata:
      labels:
        app: video-recommendation
    spec:
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
                        - video-recommendation
                topologyKey: kubernetes.io/hostname
      containers:
        - name: recommend
          image: registry.cn-hangzhou.aliyuncs.com/media/recommendation:v3.0
          ports:
            - containerPort: 8080
          env:
            - name: REDIS_CLUSTER
              value: "r-bp1xxxxxxxxx.redis.rds.aliyuncs.com:6379"
            - name: FEATURE_SERVICE_URL
              value: "http://feature-service:8080"
            - name: MODEL_PATH
              value: "/models/din_v3"
          resources:
            requests:
              cpu: "4"
              memory: "8Gi"
            limits:
              cpu: "16"
              memory: "32Gi"
---
# HPA Based on QPS Scaling
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: video-recommend-hpa
  namespace: media-platform
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: video-recommendation-service
  minReplicas: 20
  maxReplicas: 200
  metrics:
    - type: Pods
      pods:
        metric:
          name: http_requests_per_second
        target:
          type: AverageValue
          averageValue: "5000"
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 60
```

## See Also

- smart-healthcare-architecture
- energy-power-architecture
- saas-multitenant-architecture
- data-midplatform-architecture
