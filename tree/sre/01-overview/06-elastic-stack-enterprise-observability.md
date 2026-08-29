---
title: Deep Practice of Elastic Stack Enterprise-Level Observability Platform
description: 'title: Deep Practice of Elastic Stack Enterprise-Level Observability Platform'
summary: 'title: Deep Practice of Elastic Stack Enterprise-Level Observability Platform'
category: general
tags:
- observability
- monitoring
- alerting
- prometheus
- grafana
- docker
- redis
- mysql
- kafka
- elasticsearch
tier: supporting
created: '2026-05-23'
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- All engineers
estimated_read_time: 45min
intent_queries:
- What is elastic-stack-enterprise-observability?
- How to use elastic-stack-enterprise-observability
- Best practices for elastic-stack-enterprise-observability
trigger_keywords:
- Elastic
- Stack enterprise-level observability platform deep practice
- observability
prerequisites:
- kubectl-basics
- observability-basics
- prometheus-basics
- monitoring-basics
- kafka-basics
- redis-basics
- mysql-basics
- logging-basics
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/01-overview/06-elastic-stack-enterprise-observability.md
---

> **Production Environment Security Notice**
>
> This document contains directly executable operations commands. Before execution, please confirm: whether the current target cluster and Namespace are correct; whether you have sufficient RBAC permissions; whether you have verified in non-production environments. Command risk levels are marked as: 🔴 High risk (may cause data loss or service interruption), 🟡 Medium risk (modifies cluster state, but usually reversible), 🟢 Low risk/read-only (information collection, no side effects).




title: Deep Practice of Elastic Stack Enterprise-Level Observability Platform
description: '# Deep Practice of Elastic Stack Enterprise-Level Observability Platform'
category: enterprise-monitoring-alerting
tags:
- k8s
- monitoring
- alerting
- [[Prometheus|prometheus]]
- docker
- redis
- mysql
- kafka
- elasticsearch
- [[StatefulSet|statefulset]]
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Monitoring engineers
- Operations engineers
estimated_read_time: 5min
intent_queries:
- What is Elastic Stack enterprise-level observability platform deep practice
- How to Elastic Stack enterprise-level observability platform deep practice
- Kubernetes 20 enterprise monitoring alerting best practices
trigger_keywords:
- Elastic
- Stack enterprise-level observability platform deep practice
- enterprise
- monitoring
- alerting
cross_refs:
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/promql.md
  label: 'Quick Reference: promql'
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

# Deep Practice of Elastic Stack Enterprise-Level Observability Platform

> **Document Positioning**: Complete Elasticsearch, Logstash, Kibana, Beats observability solution for enterprises | **Updated**: 2026-02-07
> 
> This document provides in-depth analysis of building a complete observability platform for Elastic Stack in enterprise environments, covering core functionalities including log analysis, metrics monitoring, APM tracing, and security analytics, providing professional guidance for building a unified enterprise-level data insight platform.

<!-- chunk: 📋 Document Table of Contents -->## 📋 Document Table of Contents

- [Architecture Overview](#architecture-overview)
- [In-Depth Core Components Analysis](#in-depth-core-components-analysis)
- [Enterprise-Level Deployment Architecture](#enterprise-level-deployment-architecture)
- [Log Analysis and Processing](#log-analysis-and-processing)
- [Metrics Monitoring System](#metrics-monitoring-system)
- [APM Application Performance Monitoring](#apm-application-performance-monitoring)
- [Security Information and Event Management](#security-information-and-event-management)
- [Visualization and Alerting](#visualization-and-alerting)
- [Performance Optimization Strategies](#performance-optimization-strategies)
- [Best Practices Summary](#best-practices-summary)

---

<!-- chunk: Architecture Overview -->## Architecture Overview

## Elastic Stack Platform Architecture

```yaml
# Elastic Stack enterprise-level observability platform overall architecture
elastic_stack_platform:
  data_collection_layer:
    filebeat: File log collector
    metricbeat: System metrics collector
    packetbeat: Network packet analyzer
    winlogbeat: Windows event log collector
    auditbeat: Audit data collector
    heartbeat: Availability monitor
    apm_server: APM data receiver
    
  data_processing_layer:
    logstash: Data processing and transformation pipeline
    elasticsearch_ingest_nodes: Ingest node processing
    apm_server_processing: APM data processing
    
  storage_analysis_layer:
    elasticsearch_cluster: Distributed search engine cluster
    ilm_policy: Index lifecycle management
    snapshot_repository: Snapshot backup storage
    
  display_management_layer:
    kibana: Data visualization and analysis platform
    apm_ui: APM dedicated interface
    siem_app: Security information event management
    monitoring_ui: Cluster monitoring interface
```

## Core Value Proposition

**Unified Data Platform**
- Single platform processing Logs, Metrics, APM three major data types
- Unified query language and API interfaces
- Cross-domain data correlation and analysis capabilities
- Reduced complexity of multi-tool chain integration

**Real-Time Analysis Capability**
- Sub-second data ingestion and query response
- Real-time streaming data processing
- Machine learning driven anomaly detection
- Interactive data analysis experience

**Enterprise-Level Features**
- Multi-tenant architecture and fine-grained permission control
- Data encryption and compliance assurance
- High availability deployment and disaster recovery capability
- Horizontal scaling and elastic expansion

---

<!-- chunk: In-Depth Core Components Analysis -->## In-Depth Core Components Analysis

## Elasticsearch Architecture Detailed Explanation

## Cluster Architecture Design

```yaml
# Elasticsearch enterprise-level cluster architecture
elasticsearch_cluster:
  master_nodes:
    - node_name: es-master-01
      roles: [master]
      heap_size: 4g
      storage: 50gb
      
    - node_name: es-master-02
      roles: [master]
      heap_size: 4g
      storage: 50gb
      
    - node_name: es-master-03
      roles: [master]
      heap_size: 4g
      storage: 50gb
      
  data_nodes:
    - node_name: es-data-hot-01
      roles: [data, ingest]
      heap_size: 31g
      storage: 2tb_ssd
      node_attributes:
        data: hot
        
    - node_name: es-data-warm-01
      roles: [data]
      heap_size: 31g
      storage: 4tb_hdd
      node_attributes:
        data: warm
        
  coordinating_nodes:
    - node_name: es-coord-01
      roles: [ingest]
      heap_size: 8g
      storage: 100gb
      
  machine_learning_nodes:
    - node_name: es-ml-01
      roles: [ml, transform]
      heap_size: 8g
      storage: 500gb
```

## Index Lifecycle Management (ILM)

```json
{
  "policy": {
    "phases": {
      "hot": {
        "min_age": "0ms",
        "actions": {
          "rollover": {
            "max_age": "7d",
            "max_size": "50gb",
            "max_docs": 10000000
          },
          "set_priority": {
            "priority": 100
          }
        }
      },
      "warm": {
        "min_age": "7d",
        "actions": {
          "allocate": {
            "number_of_replicas": 1,
            "include": {
              "data": "warm"
            }
          },
          "forcemerge": {
            "max_num_segments": 1
          },
          "set_priority": {
            "priority": 50
          }
        }
      },
      "cold": {
        "min_age": "30d",
        "actions": {
          "allocate": {
            "number_of_replicas": 1,
            "include": {
              "data": "cold"
            }
          },
          "freeze": {},
          "set_priority": {
            "priority": 0
          }
        }
      },
      "delete": {
        "min_age": "365d",
        "actions": {
          "delete": {}
        }
      }
    }
  }
}
```

## Beats Data Collector Detailed Explanation

## Filebeat Configuration Optimization

```yaml
# Filebeat enterprise-level configuration
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /var/log/application/*.log
      - /var/log/nginx/access.log
      - /var/log/system/*.log
    fields:
      service: web-application
      environment: production
      data_center: dc1
      
    multiline.pattern: '^\d{4}-\d{2}-\d{2}'
    multiline.negate: true
    multiline.match: after
    
    ignore_older: 72h
    close_inactive: 2h
    clean_inactive: 25h
    
    harvester_buffer_size: 16384
    max_bytes: 10485760

  - type: container
    enabled: true
    paths:
      - '/var/lib/docker/containers/*/*.log'
    stream: all
    cri.parse_flags: true
    ids:
      - "*"

processors:
  - add_host_metadata: ~
  - add_cloud_metadata: ~
  - add_docker_metadata: ~
  - add_kubernetes_metadata:
      in_cluster: true
      
  - decode_json_fields:
      fields: ["message"]
      process_array: false
      max_depth: 10
      target: "json"
      overwrite_keys: true
      
  - drop_fields:
      fields: ["agent", "ecs", "log", "input"]
      ignore_missing: true

output.elasticsearch:
  hosts: ["https://es-coord-01:9200", "https://es-coord-02:9200"]
  username: "${ELASTIC_USERNAME}"
  password: "${ELASTIC_PASSWORD}"
  ssl.certificate_authorities: ["/etc/filebeat/certs/ca.crt"]
  ssl.certificate: "/etc/filebeat/certs/filebeat.crt"
  ssl.key: "/etc/filebeat/certs/filebeat.key"
  
  bulk_max_size: 2048
  flush_interval: 1s
  compression_level: 3
  
  index: "filebeat-%{[agent.version]}-%{+yyyy.MM.dd}"

setup.template.enabled: true
setup.template.name: "filebeat"
setup.template.pattern: "filebeat-*"
setup.ilm.enabled: true
setup.ilm.rollover_alias: "filebeat"
setup.ilm.pattern: "{now/d}-000001"
```

## Metricbeat System Monitoring

```yaml
# Metricbeat system monitoring configuration
metricbeat.modules:
  - module: system
    metricsets:
      - cpu
      - load
      - memory
      - network
      - process
      - process_summary
      - uptime
      - socket
    enabled: true
    period: 10s
    processes: ['.*']
    
  - module: docker
    metricsets:
      - container
      - cpu
      - diskio
      - healthcheck
      - image
      - info
      - memory
      - network
    enabled: true
    period: 30s
    hosts: ["unix:///var/run/docker.sock"]
    
  - module: kubernetes
    metricsets:
      - container
      - node
      - pod
      - system
      - volume
    enabled: true
    period: 30s
    hosts: ["${NODE_NAME}:10255"]
    bearer_token_file: /var/run/secrets/kubernetes.io/serviceaccount/token
    ssl.verification_mode: none

processors:
  - add_cloud_metadata: ~
  - add_docker_metadata: ~
  - add_kubernetes_metadata:
      in_cluster: true
      
  - script:
      lang: javascript
      id: calculate_derived_metrics
      source: >
        function process(event) {
          // Calculate CPU usage percentage
          var cpu_total = event.Get("system.cpu.total.norm.pct");
          if (cpu_total !== null) {
            event.Put("system.cpu.usage_percent", Math.round(cpu_total * 100));
          }
          
          // Calculate memory usage percentage
          var memory_used = event.Get("system.memory.actual.used.bytes");
          var memory_total = event.Get("system.memory.total");
          if (memory_used !== null && memory_total !== null && memory_total > 0) {
            var memory_pct = (memory_used / memory_total) * 100;
            event.Put("system.memory.usage_percent", Math.round(memory_pct));
          }
        }

output.elasticsearch:
  hosts: ["https://es-coord-01:9200"]
  username: "${ELASTIC_USERNAME}"
  password: "${ELASTIC_PASSWORD}"
  indices:
    - index: "metricbeat-system-%{+yyyy.MM.dd}"
      when.contains:
        kubernetes.namespace: "system"
        
    - index: "metricbeat-apps-%{+yyyy.MM.dd}"
      when.not.contains:
        kubernetes.namespace: "system"
```

---

<!-- chunk: Enterprise-Level Deployment Architecture -->## Enterprise-Level Deployment Architecture

## High Availability Cluster Deployment

## Kubernetes Deployment Architecture

```yaml
# Elastic Stack Kubernetes deployment configuration
apiVersion: v1
kind: Namespace
metadata:
  name: elastic-stack

---
# Elasticsearch StatefulSet
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: elasticsearch
  namespace: elastic-stack
spec:
  serviceName: elasticsearch-headless
  replicas: 6
  selector:
    matchLabels:
      app: elasticsearch
  template:
    metadata:
      labels:
        app: elasticsearch
    spec:
      initContainers:
        - name: sysctl
          image: busybox:1.27.2
          command: ["sysctl", "-w", "vm.max_map_count=262144"]
          securityContext:
            privileged: true
        - name: chown
          image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
          command: ["chown", "-R", "1000:1000", "/usr/share/elasticsearch/data"]
          volumeMounts:
            - name: elasticsearch-data
              mountPath: /usr/share/elasticsearch/data
              
      containers:
        - name: elasticsearch
          image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
          env:
            - name: cluster.name
              value: "enterprise-elastic"
            - name: node.name
              valueFrom:
                fieldRef:
                  fieldPath: metadata.name
            - name: discovery.seed_hosts
              value: "elasticsearch-0.elasticsearch-headless,elasticsearch-1.elasticsearch-headless,elasticsearch-2.elasticsearch-headless"
            - name: cluster.initial_master_nodes
              value: "elasticsearch-0,elasticsearch-1,elasticsearch-2"
            - name: ES_JAVA_OPTS
              value: "-Xms31g -Xmx31g"
            - name: xpack.security.enabled
              value: "true"
            - name: xpack.security.transport.ssl.enabled
              value: "true"
              
          ports:
            - containerPort: 9200
              name: http
            - containerPort: 9300
              name: transport
              
          readinessProbe:
            exec:
              command:
                - bash
                - -c
                - |
                  curl -s --cacert /usr/share/elasticsearch/config/certs/ca.crt \
                  -u ${ELASTIC_USERNAME}:${ELASTIC_PASSWORD} \
                  https://127.0.0.1:9200/_cluster/health?local=true | grep -q '"status":"green"|"status":"yellow"'
            initialDelaySeconds: 60
            periodSeconds: 10
            
          livenessProbe:
            exec:
              command:
                - bash
                - -c
                - |
                  curl -s --cacert /usr/share/elasticsearch/config/certs/ca.crt \
                  -u ${ELASTIC_USERNAME}:${ELASTIC_PASSWORD} \
                  https://127.0.0.1:9200/_cluster/health?local=true | grep -q '"status":"red"' && exit 1 || exit 0
            initialDelaySeconds: 120
            periodSeconds: 30
            
          resources:
            requests:
              memory: "32Gi"
              cpu: "8"
            limits:
              memory: "64Gi"
              cpu: "16"
              
          volumeMounts:
            - name: elasticsearch-data
              mountPath: /usr/share/elasticsearch/data
            - name: elasticsearch-config
              mountPath: /usr/share/elasticsearch/config/elasticsearch.yml
              subPath: elasticsearch.yml
            - name: certs
              mountPath: /usr/share/elasticsearch/config/certs
              readOnly: true
              
      volumes:
        - name: elasticsearch-config
          configMap:
            name: elasticsearch-config
        - name: certs
          secret:
            secretName: elasticsearch-certs
            
  volumeClaimTemplates:
    - metadata:
        name: elasticsearch-data
      spec:
        accessModes: ["ReadWriteOnce"]
        storageClassName: fast-ssd
        resources:
          requests:
            storage: 2Ti
```

## Network Security Configuration

```yaml
# Network policy configuration
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: elastic-stack-policy
  namespace: elastic-stack
spec:
  podSelector:
    matchLabels:
      app: elasticsearch
  policyTypes:
    - Ingress
    - Egress
    
  ingress:
    # Allow Kibana access
    - from:
        - podSelector:
            matchLabels:
              app: kibana
      ports:
        - protocol: TCP
          port: 9200
          
    # Allow Beats access
    - from:
        - namespaceSelector:
            matchLabels:
              name: monitoring
      ports:
        - protocol: TCP
          port: 9200
          
    # Allow internal node communication
    - from:
        - podSelector:
            matchLabels:
              app: elasticsearch
      ports:
        - protocol: TCP
          port: 9300
          
  egress:
    # Allow DNS queries
    - to:
        - namespaceSelector:
            matchLabels:
              name: kube-system
      ports:
        - protocol: UDP
          port: 53
        - protocol: TCP
          port: 53
          
    # Allow external storage access (e.g., S3)
    - to:
        - ipBlock:
            cidr: 0.0.0.0/0
      ports:
        - protocol: TCP
          port: 443
```

## Security Hardening Configuration

## RBAC Permission Management

```yaml
# Elasticsearch role and user configuration
roles:
  admin_role:
    cluster: 
      - all
    indices:
      - names: ["*"]
        privileges: ["all"]
    applications:
      - application: "kibana-.kibana"
        privileges: ["all"]
        
  monitoring_role:
    cluster:
      - monitor
      - manage_index_templates
    indices:
      - names: [".monitoring*", "metricbeat-*", "filebeat-*"]
        privileges: ["read", "view_index_metadata"]
        
  log_reader_role:
    cluster: []
    indices:
      - names: ["filebeat-*", "logstash-*"]
        privileges: ["read", "view_index_metadata"]
        
  apm_writer_role:
    cluster: []
    indices:
      - names: ["apm-*"]
        privileges: ["write", "create_index", "manage"]
        
users:
  elastic_admin:
    password: "${ADMIN_PASSWORD}"
    roles: ["admin_role", "kibana_admin"]
    
  monitoring_user:
    password: "${MONITORING_PASSWORD}"
    roles: ["monitoring_role"]
    
  log_collector:
    password: "${LOG_COLLECTOR_PASSWORD}"
    roles: ["log_reader_role"]
    
  apm_server:
    password: "${APM_SERVER_PASSWORD}"
    roles: ["apm_writer_role"]
```

## TLS Certificate Management

> ⚠️ **🟡 Medium Risk Modification** — Modifies cluster resource state, recommend --dry-run or diff confirmation first
> - `kubectl apply/create/replace`: create/modify cluster resources

``` bash
# 🟡 Medium risk: modifies cluster/resource state, confirm target, scope and authorization before execution
#!/bin/bash
# Elasticsearch TLS certificate generation script

# Create CA
openssl genrsa -out ca.key 4096
openssl req -new -x509 -key ca.key -out ca.crt -days 3650 -subj "/CN=Elasticsearch CA"

# Generate certificates for each node
NODES=("es-master-01" "es-master-02" "es-master-03" "es-data-01" "es-data-02" "es-coord-01")

for node in "${NODES[@]}"; do
    # Generate node private key
    openssl genrsa -out ${node}.key 2048
    
    # Generate certificate signing request
    openssl req -new -key ${node}.key -out ${node}.csr -subj "/CN=${node}"
    
    # Sign certificate with CA
    openssl x509 -req -in ${node}.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out ${node}.crt -days 365
    
    # Create PKCS#12 format certificate (for Java clients)
    openssl pkcs12 -export -in ${node}.crt -inkey ${node}.key -out ${node}.p12 -name ${node} -CAfile ca.crt -caname root -password pass:${node}_password
done

# Generate HTTP layer certificate
openssl genrsa -out http.key 2048
openssl req -new -key http.key -out http.csr -subj "/CN=elasticsearch-http"
openssl x509 -req -in http.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out http.crt -days 365

# Create Kubernetes Secret
kubectl create secret generic elasticsearch-certs \
    --from-file=ca.crt \
    --from-file=es-master-01.crt \
    --from-file=es-master-01.key \
    --from-file=es-master-02.crt \
    --from-file=es-master-02.key \
    --from-file=es-master-03.crt \
    --from-file=es-master-03.key \
    --from-file=http.crt \
    --from-file=http.key \
    -n elastic-stack
```
---

<!-- chunk: Log Analysis and Processing -->## Log Analysis and Processing

## Logstash Pipeline Configuration

## Complex Log Processing Pipeline

```ruby
# Logstash enterprise-level configuration
input {
  beats {
    port => 5044
    ssl => true
    ssl_certificate => "/etc/logstash/certs/logstash.crt"
    ssl_key => "/etc/logstash/certs/logstash.key"
  }
  
  kafka {
    bootstrap_servers => "kafka-01:9092,kafka-02:9092,kafka-03:9092"
    topics => ["application-logs", "system-logs", "security-logs"]
    group_id => "logstash-consumer"
    codec => json
  }
}

filter {
  # Universal field standardization
  mutate {
    add_field => {
      "[@metadata][ingest_timestamp]" => "%{@timestamp}"
      "[fields][collector]" => "logstash"
    }
    
    rename => {
      "message" => "[log][original]"
      "host" => "[host][name]"
    }
  }
  
  # Timestamp processing
  date {
    match => [ "[log][timestamp]", "ISO8601", "yyyy-MM-dd HH:mm:ss", "UNIX_MS" ]
    target => "@timestamp"
    timezone => "Asia/Shanghai"
  }
  
  # JSON log parsing
  json {
    source => "[log][original]"
    skip_on_invalid_json => true
    target => "[json]"
  }
  
  # User agent parsing
  useragent {
    source => "[http][request][headers][user-agent]"
    target => "[user_agent]"
    regexes => "/etc/logstash/regexes.yaml"
  }
  
  # Geolocation parsing
  geoip {
    source => "[client][ip]"
    target => "[geoip]"
    database => "/etc/logstash/GeoLite2-City.mmdb"
  }
  
  # Application-specific processing
  if [fields][service] == "nginx" {
    grok {
      match => {
        "[log][original]" => "%{IPORHOST:[nginx][access][remote_ip]} - %{DATA:[nginx][access][user_name]} \[%{HTTPDATE:[nginx][access][time]}\] \"%{WORD:[nginx][access][method]} %{DATA:[nginx][access][url]} HTTP/%{NUMBER:[nginx][access][http_version]}\" %{NUMBER:[nginx][access][response_code]} %{NUMBER:[nginx][access][body_sent][bytes]} \"%{DATA:[nginx][access][referrer]}\" \"%{DATA:[nginx][access][agent]}\""
      }
    }
    
    mutate {
      convert => {
        "[nginx][access][response_code]" => "integer"
        "[nginx][access][body_sent][bytes]" => "integer"
      }
    }
  }
  
  # Anomaly detection and enrichment
  ruby {
    code => "
      # Calculate response size category
      if event.get('[nginx][access][body_sent][bytes]') && event.get('[nginx][access][body_sent][bytes]') > 1048576
        event.set('[nginx][access][size_category]', 'large')
      elsif event.get('[nginx][access][body_sent][bytes]') && event.get('[nginx][access][body_sent][bytes]') > 102400
        event.set('[nginx][access][size_category]', 'medium')
      else
        event.set('[nginx][access][size_category]', 'small')
      end
      
      # Mark anomalous access
      if event.get('[nginx][access][response_code]') && event.get('[nginx][access][response_code]').to_i >= 500
        event.set('[error][type]', 'server_error')
      elsif event.get('[nginx][access][response_code]') && event.get('[nginx][access][response_code]').to_i >= 400
        event.set('[error][type]', 'client_error')
      end
    "
  }
  
  # Data masking
  mutate {
    replace => {
      "[user][password]" => "[MASKED]"
      "[credit_card][number]" => "[MASKED]"
    }
  }
}

output {
  # Primary output to Elasticsearch
  elasticsearch {
    hosts => ["https://es-coord-01:9200", "https://es-coord-02:9200"]
    user => "${ELASTIC_USERNAME}"
    password => "${ELASTIC_PASSWORD}"
    ssl_certificate_verification => true
    cacert => "/etc/logstash/certs/ca.crt"
    
    index => "%{[@metadata][beat]}-%{[@metadata][version]}-%{+YYYY.MM.dd}"
    template_name => "logstash"
    template => "/etc/logstash/templates/logstash-template.json"
    template_overwrite => true
    
    # Bulk processing optimization
    document_id => "%{[@metadata][fingerprint]}"
    action => "index"
    retry_max_interval => 60
    retry_max_times => 3
  }
  
  # Backup output to object storage
  s3 {
    access_key_id => "${AWS_ACCESS_KEY_ID}"
    secret_access_key => "${AWS_SECRET_ACCESS_KEY}"
    region => "cn-north-1"
    bucket => "log-backup-enterprise"
    time_file => 10
    size_file => 10485760
    codec => "json_lines"
    prefix => "logs/%{+YYYY}/%{+MM}/%{+dd}/"
  }
  
  # Real-time alert output
  if [error][type] == "server_error" or [nginx][access][response_code] >= 500 {
    kafka {
      bootstrap_servers => "kafka-alerts:9092"
      topic_id => "critical-alerts"
      codec => json
    }
  }
}
```

## Index Template Configuration

```json
{
  "index_patterns": ["filebeat-*", "logstash-*"],
  "template": {
    "settings": {
      "number_of_shards": 3,
      "number_of_replicas": 1,
      "refresh_interval": "30s",
      "blocks": {
        "read_only_allow_delete": "false"
      },
      "analysis": {
        "analyzer": {
          "log_analyzer": {
            "type": "custom",
            "tokenizer": "whitespace",
            "filter": ["lowercase", "stop"]
          }
        }
      }
    },
    "mappings": {
      "dynamic_templates": [
        {
          "strings_as_keywords": {
            "match_mapping_type": "string",
            "mapping": {
              "type": "text",
              "analyzer": "log_analyzer",
              "fields": {
                "keyword": {
                  "type": "keyword",
                  "ignore_above": 256
                }
              }
            }
          }
        }
      ],
      "properties": {
        "@timestamp": {
          "type": "date"
        },
        "message": {
          "type": "text",
          "analyzer": "log_analyzer"
        },
        "host.name": {
          "type": "keyword"
        },
        "service.name": {
          "type": "keyword"
        },
        "log.level": {
          "type": "keyword"
        },
        "http.response.status_code": {
          "type": "short"
        },
        "geoip.location": {
          "type": "geo_point"
        }
      }
    }
  },
  "composed_of": ["logs-mappings", "logs-settings"],
  "priority": 500,
  "version": 3,
  "_meta": {
    "description": "Default template for log data"
  }
}
```

---

<!-- chunk: Metrics Monitoring System -->## Metrics Monitoring System

## Metricbeat Advanced Configuration

## Custom Metrics Collection

```yaml
# Metricbeat custom module configuration
metricbeat.modules:
  # Custom JVM monitoring
  - module: jolokia
    metricsets: ["jmx"]
    enabled: true
    period: 30s
    hosts: ["localhost:8778"]
    namespace: "jvm"
    jmx.mappings:
      - mbean: "java.lang:type=Memory"
        attributes:
          - attr: HeapMemoryUsage
            field: memory.heap
          - attr: NonHeapMemoryUsage
            field: memory.non_heap
            
      - mbean: "java.lang:type=Threading"
        attributes:
          - attr: ThreadCount
            field: threads.count
          - attr: PeakThreadCount
            field: threads.peak
            
      - mbean: "java.lang:type=OperatingSystem"
        attributes:
          - attr: SystemLoadAverage
            field: system.load.average
          - attr: ProcessCpuLoad
            field: process.cpu.load

  # Database monitoring
  - module: mysql
    metricsets: ["status", "performance"]
    enabled: true
    period: 30s
    hosts: ["tcp(127.0.0.1:3306)/"]
    username: "${MYSQL_MONITOR_USER}"
    password: "${MYSQL_MONITOR_PASSWORD}"
    
    # Custom SQL query monitoring
    sql_queries:
      - name: "slow_queries"
        query: "SHOW GLOBAL STATUS LIKE 'Slow_queries'"
        fields:
          - name: "slow_queries_count"
            column: "Value"
            type: "long"
            
      - name: "connection_stats"
        query: "SHOW STATUS LIKE 'Threads_connected'"
        fields:
          - name: "current_connections"
            column: "Value"
            type: "long"

  # Redis monitoring
  - module: redis
    metricsets: ["info", "keyspace"]
    enabled: true
    period: 30s
    hosts: ["localhost:6379"]
    password: "${REDIS_PASSWORD}"
    
    # Custom keyspace analysis
    keyspace_analysis:
      enabled: true
      sample_keys: 1000
      expiration_analysis: true
```

## Metrics Preprocessing and Enrichment

```javascript
// Metricbeat JavaScript processor example
processors:
  - script:
      lang: javascript
      id: calculate_derived_metrics
      source: >
        function process(event) {
          // Calculate CPU usage rate of change
          var prev_cpu = event.Get("prev.system.cpu.total.norm.pct");
          var current_cpu = event.Get("system.cpu.total.norm.pct");
          
          if (prev_cpu !== null && current_cpu !== null) {
            var cpu_delta = Math.abs(current_cpu - prev_cpu);
            event.Put("system.cpu.delta", cpu_delta);
            
            // Mark CPU spikes
            if (cpu_delta > 0.3) {
              event.Put("system.cpu.spike", true);
            }
          }
          
          // Calculate memory pressure index
          var memory_used_pct = event.Get("system.memory.actual.used.pct");
          var swap_used_pct = event.Get("system.memory.swap.used.pct");
          
          if (memory_used_pct !== null && swap_used_pct !== null) {
            var memory_pressure = (memory_used_pct * 0.7) + (swap_used_pct * 0.3);
            event.Put("system.memory.pressure_index", memory_pressure);
          }
          
          // Network anomaly detection
          var network_in_drops = event.Get("system.network.in.dropped");
          var network_out_drops = event.Get("system.network.out.dropped");
          
          if ((network_in_drops !== null && network_in_drops > 100) || 
              (network_out_drops !== null && network_out_drops > 100)) {
            event.Put("network.anomaly", true);
          }
        }
```

---

<!-- chunk: APM Application Performance Monitoring -->## APM Application Performance Monitoring

## APM Server Configuration

## Advanced APM Configuration

```yaml
# APM Server enterprise-level configuration
apm-server:
  host: "0.0.0.0:8200"
  max_connections: 1000
  idle_timeout: 45s
  read_timeout: 30s
  write_timeout: 30s
  shutdown_timeout: 5s
  
  ssl:
    enabled: true
    certificate: "/etc/apm-server/certs/apm-server.crt"
    key: "/etc/apm-server/certs/apm-server.key"
    certificate_authorities: ["/etc/apm-server/certs/ca.crt"]
    client_authentication: "optional"

  rum:
    enabled: true
    allow_origins: ["*"]
    allow_headers: ["Content-Type", "Authorization"]
    rate_limit:
      event_limit: 300
      ip_limit: 1000
      
  kibana:
    enabled: true
    host: "kibana:5601"
    username: "${KIBANA_USERNAME}"
    password: "${KIBANA_PASSWORD}"
    
  elasticsearch:
    hosts: ["https://es-coord-01:9200", "https://es-coord-02:9200"]
    username: "${ELASTIC_USERNAME}"
    password: "${ELASTIC_PASSWORD}"
    ssl.certificate_authorities: ["/etc/apm-server/certs/ca.crt"]
    
    bulk_max_size: 2048
    flush_interval: 1s
    compression_level: 3
    
  # Sampling configuration
  sampling:
    tail:
      enabled: true
      interval: 1m
      policies:
        - service:
            name: "critical-service"
          sample_rate: 1.0
          
        - service:
            name: "standard-service"
          sample_rate: 0.1
          
        - trace:
            outcome: "failure"
          sample_rate: 1.0

  # Data enrichment
  data_streams:
    enabled: true
    namespace: "default"
    
  # External monitoring integration
  monitoring:
    enabled: true
    elasticsearch:
      hosts: ["https://es-coord-01:9200"]
      username: "${MONITORING_USERNAME}"
      password: "${MONITORING_PASSWORD}"
```

## Application APM Integration

## Java Application APM Configuration

```java
// Spring Boot application APM configuration example
@Configuration
public class ApmConfiguration {
    
    @Bean
    public ElasticApmAgent elasticApmAgent() {
        // Configure APM agent
        System.setProperty("elastic.apm.service_name", "user-service");
        System.setProperty("elastic.apm.server_urls", "https://apm-server:8200");
        System.setProperty("elastic.apm.secret_token", "${APM_SECRET_TOKEN}");
        System.setProperty("elastic.apm.application_packages", "com.company.userservice");
        System.setProperty("elastic.apm.environment", "production");
        System.setProperty("elastic.apm.log_level", "INFO");
        
        // Advanced configuration
        System.setProperty("elastic.apm.span_frames_min_duration", "5ms");
        System.setProperty("elastic.apm.transaction_max_spans", "500");
        System.setProperty("elastic.apm.central_config", "true");
        System.setProperty("elastic.apm.metrics_interval", "30s");
        
        return new ElasticApmAgent();
    }
    
    @Bean
    public WebMvcConfigurer webMvcConfigurer() {
        return new WebMvcConfigurer() {
            @Override
            public void addInterceptors(InterceptorRegistry registry) {
                registry.addInterceptor(new ApmTransactionInterceptor());
            }
        };
    }
}

// Custom Span annotation
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface TracedOperation {
    String value() default "";
    String type() default "business";
}

// AOP aspect processing
@Aspect
@Component
public class ApmTracingAspect {
    
    @Around("@annotation(tracedOperation)")
    public Object traceMethod(ProceedingJoinPoint joinPoint, TracedOperation tracedOperation) throws Throwable {
        Span span = ElasticApm.currentSpan()
            .startSpan(tracedOperation.type(), "method", tracedOperation.value());
            
        try {
            span.setName(joinPoint.getSignature().getName());
            span.activate();
            
            // Add method parameters as tags
            Object[] args = joinPoint.getArgs();
            for (int i = 0; i < args.length; i++) {
                span.addLabel("param_" + i, String.valueOf(args[i]));
            }
            
            Object result = joinPoint.proceed();
            span.addLabel("result_type", result != null ? result.getClass().getSimpleName() : "null");
            
            return result;
        } catch (Exception e) {
            span.captureException(e);
            throw e;
        } finally {
            span.end();
        }
    }
}
```

## Database Query Monitoring

```java
// Database query performance monitoring
@Component
public class DatabasePerformanceMonitor {
    
    @EventListener
    public void handleSlowQuery(SlowQueryEvent event) {
        Transaction transaction = ElasticApm.currentTransaction();
        
        if (transaction != null) {
            Span span = transaction.startSpan("db", "mysql", "query");
            span.setName("Slow Query Detection");
            span.addLabel("sql", event.getSql());
            span.addLabel("execution_time_ms", event.getExecutionTime());
            span.addLabel("rows_affected", event.getRowsAffected());
            
            // Set performance threshold
            if (event.getExecutionTime() > 1000) {
                span.setOutcome(Outcome.FAILURE);
                transaction.setOutcome(Outcome.FAILURE);
                span.addLabel("performance_issue", "slow_query");
            }
            
            span.end();
        }
    }
    
    // JPA query interceptor
    @Component
    public static class JpaQueryInterceptor implements StatementInspector {
        
        @Override
        public String inspect(String sql) {
            // Record query performance
            long startTime = System.currentTimeMillis();
            
            return sql; // Return original SQL, does not affect execution
        }
    }
}
```

---

<!-- chunk: Security Information and Event Management -->## Security Information and Event Management

## SIEM Configuration

## Threat Detection Rules

```yaml
# Elastic SIEM threat detection rules
apiVersion: detection.k8s.elastic.co/v1alpha1
kind: DetectionRule
metadata:
  name: suspicious-login-patterns
  namespace: security
spec:
  name: "Suspicious login pattern detection"
  description: "Detect abnormal login behavior and potential security threats"
  enabled: true
  risk_score: 73
  severity: high
  type: detection
  language: kuery
  
  query: |
    event.action:"user_login" and 
    user.name:* and 
    (
      # Abnormal time login
      (event.created:[now-1h TO now] and 
       (event.created.hour:< 6 or event.created.hour:> 22)) or
       
      # Multiple geographic location login
      (geoip.country_iso_code:* and 
       geoip.country_iso_code != geoip.previous_country_iso_code) or
       
      # Excessive failed login attempts
      (event.outcome:"failure" and 
       event.action_count:> 5)
    )
    
  threat:
    - framework: MITRE ATT&CK
      tactic:
        id: TA0006
        name: Credential Access
        reference: https://attack.mitre.org/tactics/TA0006/
      technique:
        - id: T1110
          name: Brute Force
          reference: https://attack.mitre.org/techniques/T1110/
          
  schedule:
    interval: 5m
    lookback: 1h
    
  actions:
    - action_type: "index"
      destination_index: "security-alerts"
      
    - action_type: "webhook"
      url: "https://security-orchestrator/webhook/incident"
      payload:
        incident_type: "suspicious_login"
        priority: "high"
        assign_to: "security-team"
```

## Security Log Analysis

```python
# Security log analysis Python script
from elasticsearch import Elasticsearch
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

class SecurityAnalyzer:
    def __init__(self, es_client):
        self.es = es_client
        self.index_pattern = "logs-security-*"
        
    def detect_bruteforce_attacks(self, time_window_hours=24):
        """Detect brute force attacks"""
        query = {
            "bool": {
                "must": [
                    {"term": {"event.category": "authentication"}},
                    {"term": {"event.outcome": "failure"}},
                    {"range": {
                        "@timestamp": {
                            "gte": f"now-{time_window_hours}h/h",
                            "lt": "now/h"
                        }
                    }}
                ]
            }
        }
        
        # Aggregation analysis
        aggs = {
            "by_source_ip": {
                "terms": {
                    "field": "source.ip",
                    "size": 1000
                },
                "aggs": {
                    "failure_count": {
                        "cardinality": {
                            "field": "user.name.keyword"
                        }
                    },
                    "unique_users": {
                        "cardinality": {
                            "field": "user.name.keyword"
                        }
                    },
                    "timeline": {
                        "date_histogram": {
                            "field": "@timestamp",
                            "calendar_interval": "1h"
                        }
                    }
                }
            }
        }
        
        response = self.es.search(
            index=self.index_pattern,
            body={
                "query": query,
                "aggs": aggs,
                "size": 0
            }
        )
        
        # Analysis results
        threats = []
        for bucket in response['aggregations']['by_source_ip']['buckets']:
            failure_count = bucket['failure_count']['value']
            unique_users = bucket['unique_users']['value']
            
            # Determine if brute force attack
            if failure_count > 10 and unique_users > 5:
                threats.append({
                    'source_ip': bucket['key'],
                    'failure_attempts': failure_count,
                    'affected_users': unique_users,
                    'risk_score': min(100, failure_count * 2 + unique_users * 5),
                    'timestamp': datetime.now().isoformat()
                })
                
        return threats
        
    def analyze_lateral_movement(self):
        """Analyze lateral movement behavior"""
        query = {
            "bool": {
                "must": [
                    {"terms": {"event.action": ["user_login", "session_start"]}},
                    {"exists": {"field": "host.name"}},
                    {"range": {
                        "@timestamp": {
                            "gte": "now-7d/d",
                            "lt": "now/d"
                        }
                    }}
                ]
            }
        }
        
        aggs = {
            "user_sessions": {
                "terms": {
                    "field": "user.name.keyword",
                    "size": 1000
                },
                "aggs": {
                    "hosts": {
                        "cardinality": {
                            "field": "host.name.keyword"
                        }
                    },
                    "distinct_hosts": {
                        "terms": {
                            "field": "host.name.keyword",
                            "size": 100
                        }
                    }
                }
            }
        }
        
        response = self.es.search(
            index=self.index_pattern,
            body={
                "query": query,
                "aggs": aggs,
                "size": 0
            }
        )
        
        # Detect anomalous host access patterns
        suspicious_users = []
        for bucket in response['aggregations']['user_sessions']['buckets']:
            host_count = bucket['hosts']['value']
            
            if host_count > 10:  # Single user accessing more than 10 hosts
                suspicious_users.append({
                    'user': bucket['key'],
                    'hosts_accessed': host_count,
                    'host_list': [h['key'] for h in bucket['distinct_hosts']['buckets']],
                    'anomaly_score': host_count
                })
                
        return suspicious_users

# Usage example
if __name__ == "__main__":
    es = Elasticsearch(['https://es-coord-01:9200'], 
                      http_auth=('username', 'password'),
                      verify_certs=True)
    
    analyzer = SecurityAnalyzer(es)
    
    # Detect brute force
    bruteforce_threats = analyzer.detect_bruteforce_attacks()
    print(f"Found {len(bruteforce_threats)} brute force threats")
    
    # Analyze lateral movement
    lateral_movements = analyzer.analyze_lateral_movement()
    print(f"Found {len(lateral_movements)} suspicious lateral movement behaviors")
```

---

<!-- chunk: Visualization and Alerting -->## Visualization and Alerting

## Kibana Dashboard Configuration

## Advanced Visualization Configuration

```json
{
  "dashboard": {
    "id": "enterprise-observability-dashboard",
    "title": "Enterprise-Level Observability Overview",
    "description": "Comprehensive display of infrastructure, application performance and security status",
    "panels": [
      {
        "id": "system-health-panel",
        "type": "visualization",
        "gridData": {
          "x": 0,
          "y": 0,
          "w": 24,
          "h": 12
        },
        "embeddableConfig": {
          "visState": {
            "title": "System Health Status",
            "type": "timelion",
            "params": {
              "expression": ".es(index=metricbeat-*, timefield='@timestamp', metric='avg:system.cpu.user.pct').label('CPU usage'), .es(index=metricbeat-*, timefield='@timestamp', metric='avg:system.memory.actual.used.pct').label('Memory usage'), .es(index=metricbeat-*, timefield='@timestamp', metric='avg:system.disk.used.pct').label('Disk usage')"
            }
          }
        }
      },
      {
        "id": "application-performance-panel",
        "type": "visualization",
        "gridData": {
          "x": 0,
          "y": 12,
          "w": 24,
          "h": 12
        },
        "embeddableConfig": {
          "visState": {
            "title": "Application Performance Monitoring",
            "type": "lens",
            "references": [
              {
                "id": "apm-transaction-duration",
                "name": "indexpattern-datasource-layer-0",
                "type": "index-pattern"
              }
            ],
            "state": {
              "visualization": {
                "layers": [
                  {
                    "layerId": "layer_0",
                    "layerType": "data",
                    "state": {
                      "columns": [
                        {
                          "columnId": "x-axis-column",
                          "sourceField": "@timestamp"
                        },
                        {
                          "columnId": "y-axis-column",
                          "sourceField": "transaction.duration.us"
                        }
                      ]
                    }
                  }
                ]
              }
            }
          }
        }
      }
    ],
    "options": {
      "useMargins": true,
      "hidePanelTitles": false
    },
    "timeRestore": true,
    "timeTo": "now",
    "timeFrom": "now-24h",
    "refreshInterval": {
      "pause": false,
      "value": 30000
    }
  }
}
```

## Alerting Rule Configuration

```yaml
# Watcher alerting configuration
PUT _watcher/watch/system-resource-alert
{
  "trigger": {
    "schedule": {
      "interval": "5m"
    }
  },
  "input": {
    "search": {
      "request": {
        "search_type": "query_then_fetch",
        "indices": ["metricbeat-*"],
        "body": {
          "size": 0,
          "query": {
            "bool": {
              "filter": [
                {
                  "range": {
                    "@timestamp": {
                      "gte": "now-5m"
                    }
                  }
                }
              ]
            }
          },
          "aggs": {
            "hosts": {
              "terms": {
                "field": "host.name.keyword",
                "size": 100
              },
              "aggs": {
                "avg_cpu": {
                  "avg": {
                    "field": "system.cpu.user.pct"
                  }
                },
                "avg_memory": {
                  "avg": {
                    "field": "system.memory.actual.used.pct"
                  }
                }
              }
            }
          }
        }
      }
    }
  },
  "condition": {
    "script": {
      "source": """
        def alerts = [];
        for (bucket in ctx.payload.aggregations.hosts.buckets) {
          if (bucket.avg_cpu.value > 0.85 || bucket.avg_memory.value > 0.90) {
            alerts.add([
              'host': bucket.key,
              'cpu_usage': bucket.avg_cpu.value,
              'memory_usage': bucket.avg_memory.value
            ]);
          }
        }
        ctx.alerts = alerts;
        return alerts.size() > 0;
      """
    }
  },
  "actions": {
    "send_email": {
      "email": {
        "to": ["ops-team@company.com"],
        "subject": "System resource alert - {{ctx.alerts.size()}} hosts",
        "body": """
          Alert details:
          
          {% for alert in ctx.alerts %}
          Host: {{alert.host}}
          CPU usage: {{alert.cpu_usage}}%
          Memory usage: {{alert.memory_usage}}%
          
          {% endfor %}
          
          Please handle resource bottleneck issues promptly.
        """
      }
    },
    "create_incident": {
      "webhook": {
        "scheme": "https",
        "host": "incident-management.company.com",
        "port": 443,
        "method": "post",
        "path": "/api/incidents",
        "body": "{{#toJson}}ctx{{/toJson}}"
      }
    }
  }
}
```

---

<!-- chunk: Performance Optimization Strategies -->## Performance Optimization Strategies

## Elasticsearch Performance Tuning

## Index Optimization Configuration

```yaml
# Index performance optimization configuration
index_settings:
  # Sharding strategy
  number_of_shards: 6
  number_of_replicas: 1
  
  # Refresh interval optimization
  refresh_interval: 30s
  
  # Merge strategy
  merge.policy:
    max_merge_at_once: 10
    segments_per_tier: 10
    max_merged_segment: 5gb
    
  # Cache configuration
  requests.cache.enable: true
  fielddata.cache.size: 40%
  
  # Query cache
  queries.cache.enabled: true
  
  # Translog configuration
  translog:
    durability: async
    sync_interval: 30s
    retention:
      size: 512mb
      age: 12h

# Specific index template optimization
PUT _index_template/logs-optimized
{
  "index_patterns": ["logs-*"],
  "template": {
    "settings": {
      "number_of_shards": 3,
      "number_of_replicas": 1,
      "refresh_interval": "60s",
      "codec": "best_compression",
      "blocks": {
        "read_only_allow_delete": "false"
      }
    },
    "mappings": {
      "dynamic_templates": [
        {
          "strings_as_keywords": {
            "match_mapping_type": "string",
            "mapping": {
              "type": "keyword",
              "ignore_above": 1024
            }
          }
        }
      ],
      "properties": {
        "@timestamp": {
          "type": "date"
        },
        "message": {
          "type": "text",
          "index": false
        },
        "host.name": {
          "type": "keyword"
        }
      }
    }
  }
}
```

## Query Performance Optimization

```json
{
  "profile": true,
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "@timestamp": {
              "gte": "now-1h",
              "lte": "now"
            }
          }
        },
        {
          "term": {
            "service.name.keyword": "user-service"
          }
        }
      ],
      "filter": [
        {
          "exists": {
            "field": "error.message"
          }
        }
      ]
    }
  },
  "aggs": {
    "errors_by_type": {
      "terms": {
        "field": "error.type.keyword",
        "size": 10,
        "min_doc_count": 1
      },
      "aggs": {
        "top_errors": {
          "top_hits": {
            "size": 3,
            "_source": {
              "includes": ["@timestamp", "error.message", "trace.id"]
            },
            "sort": [
              {
                "@timestamp": {
                  "order": "desc"
                }
              }
            ]
          }
        }
      }
    }
  },
  "highlight": {
    "fields": {
      "error.message": {}
    }
  }
}
```

## Cluster Health Monitoring

```bash
#!/bin/bash
# Elasticsearch cluster health check script

CLUSTER_URL="https://es-coord-01:9200"
AUTH_HEADER="Authorization: Basic $(echo -n 'username:password' | base64)"

# Check cluster health status
cluster_health=$(curl -s -k -H "$AUTH_HEADER" "$CLUSTER_URL/_cluster/health")
status=$(echo $cluster_health | jq -r '.status')

echo "Cluster status: $status"

# Check node status
nodes_stats=$(curl -s -k -H "$AUTH_HEADER" "$CLUSTER_URL/_nodes/stats")
node_count=$(echo $nodes_stats | jq '.nodes | length')

echo "Node count: $node_count"

# Check index status
indices_stats=$(curl -s -k -H "$AUTH_HEADER" "$CLUSTER_URL/_cat/indices?v&health=red")
if [ -n "$indices_stats" ]; then
    echo "Red indices:"
    echo "$indices_stats"
fi

# Check disk usage
disk_usage=$(curl -s -k -H "$AUTH_HEADER" "$CLUSTER_URL/_cat/allocation?v")
echo "Disk allocation:"
echo "$disk_usage"

# Check JVM heap memory usage
heap_usage=$(curl -s -k -H "$AUTH_HEADER" "$CLUSTER_URL/_nodes/stats/jvm" | jq '.nodes[].jvm.mem')
echo "JVM memory usage:"
echo "$heap_usage"
```

---

<!-- chunk: Best Practices Summary -->## Best Practices Summary

## Deployment Architecture Best Practices

```yaml
# Production environment recommended configuration
production_recommendations:
  cluster_sizing:
    master_nodes: 3
    data_nodes: 6+
    coordinating_nodes: 2+
    ml_nodes: 2
    
  hardware_requirements:
    master_nodes:
      cpu: 4 cores
      memory: 16GB
      storage: 100GB SSD
      
    data_hot_nodes:
      cpu: 16 cores
      memory: 128GB
      storage: 2TB NVMe
      
    data_warm_nodes:
      cpu: 8 cores
      memory: 64GB
      storage: 4TB HDD
      
  network_configuration:
    bandwidth: 10Gbps minimum
    latency: < 2ms between nodes
    mtu: 9000 (jumbo frames)
    
  backup_strategy:
    snapshot_frequency: every_6_hours
    retention_policy: 30_days_local_90_days_remote
    verification_schedule: daily
```

## Monitoring and Maintenance

## Daily Operations Checklist

- [ ] Cluster health status check
- [ ] Node resource usage monitoring
- [ ] Index shard distribution balance
- [ ] Disk space usage
- [ ] JVM garbage collection performance
- [ ] Query performance baseline testing
- [ ] Backup integrity verification
- [ ] Security configuration review

## Performance Baseline Testing

```bash
#!/bin/bash
# Elasticsearch performance baseline testing script

ES_HOST="https://es-coord-01:9200"
INDEX_NAME="benchmark-test-$(date +%Y%m%d)"
ITERATIONS=10000

# Create test index
curl -X PUT "$ES_HOST/$INDEX_NAME" -H "Content-Type: application/json" -d '
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 1,
    "refresh_interval": "-1"
  },
  "mappings": {
    "properties": {
      "timestamp": {"type": "date"},
      "message": {"type": "text"},
      "value": {"type": "double"}
    }
  }
}'

# Bulk indexing test
echo "Starting bulk indexing test..."
start_time=$(date +%s)

for i in $(seq 1 $ITERATIONS); do
    bulk_data='{"index":{"_index":"'$INDEX_NAME'"}}\n{"timestamp":"'$(( $(date +%s) * 1000 ))'","message":"Test message '$i'","value":'$i'}\n'
    curl -s -X POST "$ES_HOST/_bulk" -H "Content-Type: application/x-ndjson" -d "$bulk_data" > /dev/null
done

# Refresh index
curl -X POST "$ES_HOST/$INDEX_NAME/_refresh"

end_time=$(date +%s)
duration=$((end_time - start_time))
rate=$((ITERATIONS / duration))

echo "Indexing completed: $ITERATIONS documents in $duration seconds, rate: $rate docs/sec"

# Query performance test
echo "Starting query performance test..."

query_times=()
for i in {1..100}; do
    start=$(date +%s%3N)
    curl -s -X GET "$ES_HOST/$INDEX_NAME/_search" -H "Content-Type: application/json" -d '
    {
      "query": {
        "range": {
          "value": {
            "gte": 1000,
            "lte": 5000
          }
        }
      },
      "size": 100
    }' > /dev/null
    
    end=$(date +%s%3N)
    query_times+=($((end - start)))
done

# Calculate average query time
sum=0
for time in "${query_times[@]}"; do
    sum=$((sum + time))
done
avg_time=$((sum / ${#query_times[@]}))

echo "Average query time: ${avg_time}ms"

# Clean up test data
curl -X DELETE "$ES_HOST/$INDEX_NAME"
```

Through the comprehensive deep practice of Elastic Stack enterprise-level observability platform, you can build a powerful one-stop solution for log analysis, metrics monitoring, APM tracing and security analytics.

---

<!-- chunk: Obsidian Related Documents -->## Obsidian Related Documents

- domain-20-enterprise-monitoring-alerting MOC
- [[domain-06-observability/README.md|Domain 06: Enterprise Monitoring and Alerting (Enterprise Monitoring & Alerting)]]
- [[domain-06-observability/00-open-source-projects-index.md|Domain-20 Enterprise Monitoring and Alerting — Open Source Projects Index]]
- Deep Practice in Prometheus Enterprise Monitoring System
- Grafana Enterprise Observability Platform Deep Practice
- OpenTelemetry Distributed Tracing and Observability Deep Practice
- Thanos Enterprise Metrics Federation and Long-term Storage
- Datadog Enterprise APM Deep Practice
- Datadog Enterprise Monitoring Platform Deep Practice
- Elastic Stack Enterprise Log Analysis Deep Practice
- Zabbix Enterprise Monitoring Platform Deep Practice
- New Relic Enterprise APM Platform Deep Practice

## See Also

- 05-datadog-enterprise-monitoring
- 06-elastic-stack-enterprise-logging
- 07-zabbix-enterprise-monitoring
- 08-new-relic-enterprise-apm

- [[domain-06-observability/README.md|Back to index]]

## Related

- [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Graph Index]]


<!-- risk-assessed -->
