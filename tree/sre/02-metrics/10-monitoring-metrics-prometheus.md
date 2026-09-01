---
title: "07 - Monitoring and Metrics Table"
description: "Comprehensive reference for Kubernetes monitoring metrics from system components, alerting rules, and integration patterns with Prometheus"
summary: "Key metrics from kube-apiserver, etcd, scheduler, kubelet, kube-proxy, and node resources with recommended alert thresholds"
category: observability
tags:
- k8s
- observability
- monitoring
- logging
- tracing
- etcd
- apiserver
- kubelet
- scheduler
- controller-manager
last_updated: 2026-05
difficulty: intermediate
reading_level: intermediate
audience:
- SRE
- Operations Engineer
- Monitoring Engineer
estimated_read_time: 10min
intent_queries:
- What is Monitoring and Metrics Table
- How to use Monitoring and Metrics Table
- Kubernetes observability best practices
trigger_keywords:
- Monitoring and Metrics Table
- observability
cross_refs:
- type: domain
  path: ../domain-01-cluster-fundamentals/
  label: "Related Knowledge Domain: domain-01-cluster-fundamentals"
- type: domain
  path: ../domain-02-workloads-applications/
  label: "Related Knowledge Domain: domain-02-workloads-applications"
- type: domain
  path: ../domain-03-networking-traffic/
  label: "Related Knowledge Domain: domain-03-networking-traffic"
- type: domain
  path: ../domain-07-platform-engineering/
  label: "Related Knowledge Domain: domain-07-platform-engineering"
- type: fta
  path: ../domain-10-troubleshooting-diagnostics/topic-fta/list/monitoring-fta.md
  label: "Failure Tree: monitoring"
- type: cheatsheet
  path: ../domain-17-system-foundation/topic-cheat-sheet/promql.md
  label: "Quick Reference: promql"
authors:
- name: Dillan Teagle
  role: contributor
k8s_versions:
- '1.28'
- '1.29'
- '1.30'
- '1.31'
- '1.32'
original_language: Chinese
source_path: /Users/teaglebuilt/workspace/kudig-database/domain-06-observability/02-metrics/10-monitoring-metrics-prometheus.md
---

# 07 - Monitoring and Metrics Table

> **Applicable Versions**: v1.25 - v1.32 | **Last Updated**: 2026-01 | **Reference**: [kubernetes.io/docs/concepts/cluster-administration/system-metrics](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/)

> **Production Environment Safety Notice**
>
> This document contains directly executable operations commands. Before executing, please confirm: whether the target cluster and namespace are correct; whether you have sufficient RBAC permissions; whether you have tested in a non-production environment. Command risk levels: 🔴 High Risk (may cause data loss or service interruption), 🟡 Medium Risk (modifies cluster state but usually reversible), 🟢 Low Risk / Read-only (information gathering, no side effects).

<!-- chunk: kube-apiserver key metrics -->
## kube-apiserver Key Metrics

| Metric Name | Type | Source | Description | Version Added | Alert Threshold | Operations Scenario |
|---------|------|------|------|---------|-------------|---------|
| `apiserver_request_total` | Counter | apiserver | Total API requests (grouped by verb/resource/code) | Stable | 5xx error rate > 1% | Monitor API health |
| `apiserver_request_duration_seconds` | Histogram | apiserver | API request latency | Stable | P99 > 1s | Performance troubleshooting |
| `apiserver_current_inflight_requests` | Gauge | apiserver | Current in-flight requests | Stable | > 80% limit | Overload detection |
| `apiserver_longrunning_requests` | Gauge | apiserver | Long-running requests (watch, etc.) | Stable | Abnormal increase | Watch leak detection |
| `apiserver_request_terminations_total` | Counter | apiserver | Request terminations | Stable | Rapid increase | Timeout issues |
| `apiserver_audit_event_total` | Counter | apiserver | Audit events | v1.29 Enhanced | - | Audit monitoring |
| `apiserver_storage_objects` | Gauge | apiserver | etcd objects (by resource) | Stable | Approaching quota | Storage capacity |
| `apiserver_admission_controller_admission_duration_seconds` | Histogram | apiserver | Admission control latency | Stable | P99 > 500ms | Admission performance |
| `apiserver_watch_events_total` | Counter | apiserver | Total watch events | Stable | - | Watch monitoring |
| `apiserver_watch_events_sizes` | Histogram | apiserver | Watch event size | Stable | Too many large events | Bandwidth issues |

<!-- chunk: etcd key metrics -->
## etcd Key Metrics

| Metric Name | Type | Source | Description | Version Added | Alert Threshold | Operations Scenario |
|---------|------|------|------|---------|-------------|---------|
| `etcd_server_has_leader` | Gauge | etcd | Has leader | Stable | = 0 | Cluster health |
| `etcd_server_leader_changes_seen_total` | Counter | etcd | Leader changes | Stable | > 3/h | Stability issues |
| `etcd_disk_wal_fsync_duration_seconds` | Histogram | etcd | WAL sync latency | Stable | P99 > 10ms | Disk performance |
| `etcd_disk_backend_commit_duration_seconds` | Histogram | etcd | Backend commit latency | Stable | P99 > 25ms | Disk performance |
| `etcd_mvcc_db_total_size_in_bytes` | Gauge | etcd | Database size | Stable | > 80% quota | Storage capacity |
| `etcd_mvcc_db_total_size_in_use_in_bytes` | Gauge | etcd | Actual usage size | Stable | - | Fragmentation calculation |
| `etcd_network_peer_round_trip_time_seconds` | Histogram | etcd | Peer node RTT | Stable | P99 > 100ms | Network issues |
| `etcd_server_proposals_failed_total` | Counter | etcd | Failed proposals | Stable | > 0 continuously | Raft issues |
| `etcd_server_proposals_pending` | Gauge | etcd | Pending proposals | Stable | > 5 | Performance issues |
| `etcd_debugging_mvcc_keys_total` | Gauge | etcd | Total keys | Stable | Rapid increase | Object leaks |

<!-- chunk: kube-scheduler key metrics -->
## kube-scheduler Key Metrics

| Metric Name | Type | Source | Description | Version Added | Alert Threshold | Operations Scenario |
|---------|------|------|------|---------|-------------|---------|
| `scheduler_pending_pods` | Gauge | scheduler | Pending pods (by queue) | Stable | > 100 continuously | Scheduling bottleneck |
| `scheduler_pod_scheduling_duration_seconds` | Histogram | scheduler | Scheduling latency | Stable | P99 > 5s | Scheduling performance |
| `scheduler_schedule_attempts_total` | Counter | scheduler | Scheduling attempts (by result) | Stable | unschedulable increase | Insufficient resources |
| `scheduler_scheduling_algorithm_duration_seconds` | Histogram | scheduler | Algorithm execution time | v1.25 framework | P99 > 100ms | Algorithm performance |
| `scheduler_preemption_attempts_total` | Counter | scheduler | Preemption attempts | Stable | Continuous increase | Resource contention |
| `scheduler_preemption_victims` | Gauge | scheduler | Preemption victims | Stable | > 0 | Resource pressure |
| `scheduler_framework_extension_point_duration_seconds` | Histogram | scheduler | Plugin execution time | v1.25 framework | P99 > 50ms | Plugin performance |
| `scheduler_queue_incoming_pods_total` | Counter | scheduler | Queue incoming pods | Stable | - | Traffic monitoring |

<!-- chunk: kube-controller-manager key metrics -->
## kube-controller-manager Key Metrics

| Metric Name | Type | Source | Description | Version Added | Alert Threshold | Operations Scenario |
|---------|------|------|------|---------|-------------|---------|
| `workqueue_depth` | Gauge | controller | Work queue depth (by name) | Stable | > 100 | Controller backlog |
| `workqueue_adds_total` | Counter | controller | Queue additions | Stable | - | Load monitoring |
| `workqueue_queue_duration_seconds` | Histogram | controller | Queue wait time | Stable | P99 > 30s | Processing latency |
| `workqueue_work_duration_seconds` | Histogram | controller | Processing time | Stable | P99 > 10s | Processing performance |
| `workqueue_retries_total` | Counter | controller | Retry count | Stable | Rapid increase | Error rate |
| `node_collector_evictions_total` | Counter | controller | Node evictions | Stable | > 0 | Node issues |
| `cronjob_controller_cronjob_job_creation_skew_duration_seconds` | Histogram | controller | CronJob skew | v1.21+ | P99 > 60s | Scheduling accuracy |

<!-- chunk: kubelet key metrics -->
## kubelet Key Metrics

| Metric Name | Type | Source | Description | Version Added | Alert Threshold | Operations Scenario |
|---------|------|------|------|---------|-------------|---------|
| `kubelet_running_pods` | Gauge | kubelet | Running pods | Stable | Approaching max-pods | Node capacity |
| `kubelet_running_containers` | Gauge | kubelet | Running containers | Stable | - | Container density |
| `kubelet_pod_start_duration_seconds` | Histogram | kubelet | Pod startup latency | Stable | P99 > 60s | Startup performance |
| `kubelet_pod_worker_duration_seconds` | Histogram | kubelet | Pod worker time | Stable | P99 > 10s | Worker latency |
| `kubelet_pleg_relist_duration_seconds` | Histogram | kubelet | PLEG refresh latency | Stable | P99 > 3s | PLEG health |
| `kubelet_pleg_relist_interval_seconds` | Histogram | kubelet | PLEG refresh interval | Stable | > 3s | PLEG frequency |
| `kubelet_node_status_update_duration_seconds` | Histogram | kubelet | Status update latency | Stable | P99 > 10s | Status sync |
| `kubelet_evictions` | Counter | kubelet | Eviction count (by signal) | Stable | > 0 | Resource pressure |
| `kubelet_volume_stats_used_bytes` | Gauge | kubelet | Volume usage | Stable | > 85% | Storage alert |
| `kubelet_volume_stats_capacity_bytes` | Gauge | kubelet | Volume capacity | Stable | - | Capacity planning |
| `kubelet_cgroup_manager_duration_seconds` | Histogram | kubelet | cgroup management latency | v1.24 cgroup v2 | P99 > 100ms | cgroup performance |
| `kubelet_container_log_filesystem_used_bytes` | Gauge | kubelet | Container log usage | Stable | Rapid increase | Log management |

<!-- chunk: kube-proxy key metrics -->
## kube-proxy Key Metrics

| Metric Name | Type | Source | Description | Version Added | Alert Threshold | Operations Scenario |
|---------|------|------|------|---------|-------------|---------|
| `kubeproxy_sync_proxy_rules_duration_seconds` | Histogram | kube-proxy | Rule sync latency | Stable | P99 > 5s | Sync performance |
| `kubeproxy_sync_proxy_rules_last_timestamp_seconds` | Gauge | kube-proxy | Last sync timestamp | Stable | > 60s ago | Sync health |
| `kubeproxy_network_programming_duration_seconds` | Histogram | kube-proxy | Network programming latency | Stable | P99 > 10s | Rule update |
| `kubeproxy_sync_proxy_rules_iptables_total` | Counter | kube-proxy | iptables rule count | Stable | > 10000 | Rule explosion |
| `kubeproxy_sync_proxy_rules_endpoint_changes_total` | Counter | kube-proxy | Endpoint changes | Stable | - | Change monitoring |
| `kubeproxy_sync_proxy_rules_service_changes_total` | Counter | kube-proxy | Service changes | Stable | - | Change monitoring |

<!-- chunk: Node Resource Metrics (Node Exporter / cAdvisor) -->
## Node Resource Metrics (Node Exporter / cAdvisor)

| Metric Name | Type | Source | Description | Alert Threshold | Operations Scenario |
|---------|------|------|------|-------------|---------|
| `node_cpu_seconds_total` | Counter | node-exporter | CPU usage time | Usage > 80% | CPU monitoring |
| `node_memory_MemTotal_bytes` | Gauge | node-exporter | Total memory | - | Capacity planning |
| `node_memory_MemAvailable_bytes` | Gauge | node-exporter | Available memory | < 10% | Memory alert |
| `node_filesystem_avail_bytes` | Gauge | node-exporter | Filesystem available | < 15% | Disk alert |
| `node_filesystem_size_bytes` | Gauge | node-exporter | Filesystem size | - | Capacity planning |
| `node_disk_io_time_seconds_total` | Counter | node-exporter | Disk IO time | Saturation > 80% | IO performance |
| `node_network_receive_bytes_total` | Counter | node-exporter | Network receive bytes | - | Bandwidth monitoring |
| `node_network_transmit_bytes_total` | Counter | node-exporter | Network transmit bytes | - | Bandwidth monitoring |
| `container_cpu_usage_seconds_total` | Counter | cAdvisor | Container CPU usage | - | Container monitoring |
| `container_memory_working_set_bytes` | Gauge | cAdvisor | Container memory usage | > limits | OOM risk |
| `container_network_receive_bytes_total` | Counter | cAdvisor | Container network receive | - | Container networking |
| `container_fs_usage_bytes` | Gauge | cAdvisor | Container filesystem | - | Storage monitoring |

<!-- chunk: kube-state-metrics key metrics -->
## kube-state-metrics Key Metrics

| Metric Name | Type | Description | Alert Threshold | Operations Scenario |
|---------|------|------|-------------|---------|
| `kube_pod_status_phase` | Gauge | Pod phase status | Pending/Failed continuously | Pod health |
| `kube_pod_container_status_restarts_total` | Counter | Container restart count | > 5/h | Stability issues |
| `kube_pod_container_status_waiting_reason` | Gauge | Container waiting reason | CrashLoopBackOff | Startup issues |
| `kube_pod_container_resource_requests` | Gauge | Resource requests | - | Resource planning |
| `kube_pod_container_resource_limits` | Gauge | Resource limits | - | Resource planning |
| `kube_deployment_status_replicas_available` | Gauge | Available replicas | < desired replicas | Deployment health |
| `kube_deployment_status_replicas_unavailable` | Gauge | Unavailable replicas | > 0 | Deployment issues |
| `kube_node_status_condition` | Gauge | Node status condition | Ready != True | Node health |
| `kube_node_status_allocatable` | Gauge | Node allocatable resources | - | Capacity planning |
| `kube_namespace_status_phase` | Gauge | Namespace status | Terminating stuck | Deletion issues |
| `kube_job_status_failed` | Gauge | Failed jobs | > 0 | Job monitoring |
| `kube_cronjob_next_schedule_time` | Gauge | Next schedule time | - | Scheduled tasks |
| `kube_persistentvolumeclaim_status_phase` | Gauge | PVC status | Pending continuously | Storage issues |
| `kube_horizontalpodautoscaler_status_current_replicas` | Gauge | HPA current replicas | Reached max | Scaling |
| `kube_resourcequota_usage` | Gauge | Quota usage | > 80% | Quota alert |

<!-- chunk: CoreDNS key metrics -->
## CoreDNS Key Metrics

| Metric Name | Type | Description | Alert Threshold | Operations Scenario |
|---------|------|------|-------------|---------|
| `coredns_dns_requests_total` | Counter | Total DNS requests | - | Traffic monitoring |
| `coredns_dns_responses_total` | Counter | Total DNS responses (by rcode) | SERVFAIL > 1% | DNS health |
| `coredns_dns_request_duration_seconds` | Histogram | DNS request latency | P99 > 100ms | DNS performance |
| `coredns_cache_hits_total` | Counter | Cache hits | - | Cache efficiency |
| `coredns_cache_misses_total` | Counter | Cache misses | - | Cache efficiency |
| `coredns_forward_requests_total` | Counter | Forwarded requests | - | Upstream load |
| `coredns_forward_responses_total` | Counter | Forwarded responses (by rcode) | Error increase | Upstream issues |
| `coredns_panics_total` | Counter | Panic count | > 0 | Stability |

<!-- chunk: Prometheus alert rules examples -->
## Prometheus Alert Rules Examples

```yaml
groups:
- name: kubernetes
  rules:
  # API Server
  - alert: KubeAPIServerDown
    expr: absent(up{job="kubernetes-apiservers"} == 1)
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "Kubernetes API Server is down"
  
  # API Server error rate
  - alert: KubeAPIServerErrors
    expr: sum(rate(apiserver_request_total{code=~"5.."}[5m])) / sum(rate(apiserver_request_total[5m])) > 0.01
    for: 5m
    labels:
      severity: warning
  
  # etcd Leader lost
  - alert: EtcdNoLeader
    expr: etcd_server_has_leader == 0
    for: 1m
    labels:
      severity: critical
  
  # etcd disk latency
  - alert: EtcdHighFsyncDuration
    expr: histogram_quantile(0.99, rate(etcd_disk_wal_fsync_duration_seconds_bucket[5m])) > 0.01
    for: 5m
    labels:
      severity: warning
  
  # Scheduler backlog
  - alert: KubeSchedulerPendingPods
    expr: scheduler_pending_pods > 100
    for: 10m
    labels:
      severity: warning
  
  # kubelet PLEG issues
  - alert: KubeletPLEGDurationHigh
    expr: histogram_quantile(0.99, rate(kubelet_pleg_relist_duration_seconds_bucket[5m])) > 3
    for: 5m
    labels:
      severity: warning
  
  # Pod restarts too frequently
  - alert: PodRestartingTooMuch
    expr: increase(kube_pod_container_status_restarts_total[1h]) > 5
    for: 5m
    labels:
      severity: warning
  
  # Node NotReady
  - alert: KubeNodeNotReady
    expr: kube_node_status_condition{condition="Ready",status="true"} == 0
    for: 5m
    labels:
      severity: critical
  
  # Node memory pressure
  - alert: NodeMemoryPressure
    expr: (1 - node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes) > 0.9
    for: 5m
    labels:
      severity: warning
  
  # PVC Pending
  - alert: PersistentVolumeClaimPending
    expr: kube_persistentvolumeclaim_status_phase{phase="Pending"} == 1
    for: 15m
    labels:
      severity: warning
```

<!-- chunk: ACK monitoring integration -->
## ACK Monitoring Integration

| Component | ACK Integration Method | Data Source | Alert Configuration |
|-----|------------|-------|---------|
| **ARMS Prometheus** | Auto-installed | Component metrics | ARMS alert rules |
| **Cloud Monitoring** | Auto-integrated | Node/Pod metrics | Cloud monitoring alerts |
| **SLS** | Optional install | Logs/Audit | SLS alerts |
| **AHAS** | Optional install | Rate limiting/Circuit breaking | Custom rules |

---

**Metric Retrieval Commands**:
``` bash
# 🟢 Low Risk: Read-only / Information gathering, usually no side effects
# Get component metrics
kubectl get --raw /metrics
kubectl get --raw /apis/metrics.k8s.io/v1beta1/nodes
kubectl get --raw /apis/metrics.k8s.io/v1beta1/pods

# View kubelet metrics
curl -k https://<node-ip>:10250/metrics

# etcd metrics
etcdctl endpoint status --cluster
```
---

**Table Footer Attribution**: Kusheet Project, author Allen Galler (allengaller@gmail.com)

---

<!-- chunk: Obsidian related documentation -->
## Obsidian Related Documentation

- domain-06-observability MOC
- [[domain-06-observability/README.md|Observability Domain]]
- [[domain-06-observability/00-open-source-projects-index.md|Domain-8 Observability — Open Source Projects Index]]
- Kubernetes observability architecture system
- Metrics monitoring system explained
- 03 - Logging Collection Architecture (Logging Architecture)
- Distributed tracing system
- 05 - Alert Management Strategy (Alerting Management)
- 06 - Monitoring Alert Practice and Best Practices (Monitoring Alerting Practice)
- 04 - Monitoring Dashboard Design and Best Practices (Monitoring Dashboards)
- 08 - Logging Audit and Compliance Management (Logging Auditing & Compliance)
- 05 - Events and Audit Log Management (Events & Audit Logs)

## Related

- [[domain-02-workloads-applications/07-java-observability-kubernetes.md|07-java-observability-kubernetes]]

- [[domain-06-observability/README.md|Back to index]] - [[domain-19-landscape-references/topic-index/observability-index.md|Observability Knowledge Map Index]]

## See Also

- 08-logging-audit-compliance
- 09-events-audit-logs
- 11-custom-metrics-adapter
- 12-logging-auditing

<!-- risk-assessed -->
