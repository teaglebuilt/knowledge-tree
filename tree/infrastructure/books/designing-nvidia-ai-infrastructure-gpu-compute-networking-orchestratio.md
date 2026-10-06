---
title: Designing NVIDIA AI Infrastructure GPU compute, networking, orchestration,
  and security in NVIDIAs stack, explained (Vivian Aranha)
source: books/pdf/Designing NVIDIA AI Infrastructure GPU compute, networking, orchestration,
  and security in NVIDIAs stack, explained (Vivian Aranha) (z-library.sk, 1lib.sk,
  z-lib.sk).pdf
source_type: book
source_hash: c05248e7987aa078df8eecf50ada4f5e801fbd022c7d10079235957e59a386a1
tags:
- infrastructure
- book
extracted: '2026-10-04'
---

FROM GPUs TO PRODUCTION
## DESIGNING NVIDIA AI INFRASTRUCTURE
###### GPU compute, networking, orchestration, and security in NVIDIA's stack, explained

##### **Vivian Aranha**

### **Designing NVIDIA AI** **Infrastructure**

GPU compute, networking, orchestration, and security in
NVIDIA's stack, explained

**Vivian Aranha**

**Designing NVIDIA AI Infrastructure**

Copyright © 2026 Packt Publishing

_All rights reserved_ . No part of this book may be reproduced, stored in a retrieval system, or transmitted in
any form or by any means, without the prior written permission of the publisher, except in the case of
brief quotations embedded in critical articles or reviews.
Every effort has been made in the preparation of this book to ensure the accuracy of the information
presented. However, the information contained in this book is sold without warranty, either express or
implied. Neither the author, nor Packt Publishing or its dealers and distributors, will be held liable for
any damages caused or alleged to have been caused directly or indirectly by this book.
Packt Publishing has endeavored to provide trademark information about all of the companies and
products mentioned in this book by the appropriate use of capitals. However, Packt Publishing cannot
guarantee the accuracy of this information.

**Portfolio Director:** Kartikey Pandey
**Relationship Lead:** Prachi Rana
**Project Manager:** Sonam Pandey
**Content Engineer:** Sayali Pingale
**Technical Editor:** Aysha Nadeem
**Indexer:** Manju Arasan
**Production Designer:** Shantanu Zagade
**Growth Lead:** Abin Baiju

First published: August 2026

Production reference: 1240826

Published by Packt Publishing Ltd.
Grosvenor House
11 St Paul's Square
Birmingham
B3 1RB, UK.

ISBN 978-1-80808-013-5
```
www.packtpub.com

```

### **Contributors**

**About the author**

**Vivian Aranha** is an AI leader and technical educator who leads School of AI, a global learning
platform offering more than 80 courses across generative AI, AI product management,
quantum computing, cloud technologies, and related fields. Since April 2025, the platform has
recorded over 1.5 million enrollments and reached more than 350,000 students. During more
than eight years at Delta Air Lines, he has contributed to enterprise AI strategy and digital
transformation initiatives. He also works with HeyGen as an AI Pioneer, focusing on AI-driven
video innovation. Through curriculum design, video production, and interactive labs, Vivian is
committed to making high-quality technical education accessible and helping the next
generation of technology professionals develop practical AI skills.

### **Table of Contents**

**<mark>Preface</mark>** **<mark>ix</mark>**

**Free benefits with your book...................................................................................................** **xv**

**<mark>Chapter 1: Foundations of AI Infrastructure</mark>** **<mark>1</mark>**

**Introduction to AI infrastructure design** **................................................................................... 2**

Designing for production • 3

**The role of GPUs in AI workloads** **.............................................................................................. 4**

Why GPUs often outperform CPUs for AI workloads • 4

Framework support and the NVIDIA GPU lineup • 5

**CPU vs GPU vs DPU architectures..............................................................................................** **5**

The three chip types • 5

The three-chip model in practice • 6

**GPU acceleration for AI/ML pipelines** **.......................................................................................** **7**

Accelerating the data stages • 8

Accelerating training, tuning, and inference • 8

**NVIDIA ecosystem overview** **..................................................................................................... 9**

The NVIDIA AI software stack • 9

Deployment and infrastructure components • 10

**Summary** **.................................................................................................................................** **11**

**Further reading** **........................................................................................................................ 12**

**<mark>Chapter 2: GPU Resource Management and Virtualization</mark>** **<mark>13</mark>**

**MIG configuration.................................................................................................................... 13**

How MIG works • 14

Configuring and monitoring MIG • 15

**GPU sharing and isolation techniques.....................................................................................** **16**

Managing memory and scheduling • 17

**Virtual GPUs (vGPU) setup and use cases** **................................................................................** **19**

How vGPU works • 19

Requirements, use cases, and management • 20

_Table of Contents_ vi

**GPU workload scheduling with Kubernetes............................................................................. 21**

Enabling and requesting GPUs • 22

Monitoring and best practices • 23

**Summary** **................................................................................................................................ 24**

**Further reading** **....................................................................................................................... 24**

**<mark>Chapter 3: Storage, Networking, and Data Pipelines for AI</mark>** **<mark>25</mark>**

**Storage architectures for AI workloads** **................................................................................... 26**

The three storage types • 26

**High-speed networking** **.......................................................................................................... 28**

**Data movement bottlenecks and optimization** **....................................................................... 30**

Optimizing storage, loading, and network • 31

**AI data pipeline design............................................................................................................** **32**

The ETL stage • 32

A production example • 34

**Summary** **................................................................................................................................** **35**

**Further reading** **.......................................................................................................................** **35**

**<mark>Chapter 4: AI Cluster Orchestration and Scalability</mark>** **<mark>37</mark>**

**Kubernetes for GPU-orchestrated AI workloads......................................................................** **37**

Enabling GPU support • 38

**Helm, operators, and cluster autoscaling** **................................................................................** **39**

Helm • 39

Operators • 40

Autoscaling • 40

**Integrating Slurm, Kubeflow, and MLflow..............................................................................** **42**

The three tools • 42

**Cluster topologies** **................................................................................................................... 44**

On-premises • 44

Cloud-native • 45

Hybrid • 45

**Summary** **................................................................................................................................** **47**

**Further reading** **.......................................................................................................................** **47**

vii _Table of Contents_

**<mark>Chapter 5: Performance Optimization and Monitoring</mark>** **<mark>49</mark>**

**Profiling GPU workloads** **......................................................................................................... 49**

**GPU metrics, telemetry, and alerting tools............................................................................... 51**

GPU metrics • 51

Telemetry • 52

Visualization and alerting • 52

**TensorRT and model optimization..........................................................................................** **52**

Deployment and impact • 53

**Bottleneck diagnosis and tuning.............................................................................................** **54**

Tuning strategies • 55

**Summary** **................................................................................................................................** **56**

**Further reading** **.......................................................................................................................** **56**

**<mark>Chapter 6: Security, Compliance, and Data Governance</mark>** **<mark>59</mark>**

**Securing GPU-powered workloads..........................................................................................** **59**

Cluster and data security • 61

**Encryption and access control** **................................................................................................** **62**

DPUs and the DOCA framework • 62

**Role-based access control (RBAC) for AI clusters** **.................................................................... 64**

RBAC components and GPU-specific controls • 65

Enterprise integration and practice • 66

**Regulatory compliance: GDPR, HIPAA, FedRAMP....................................................................** **67**

The three frameworks • 68

Compliance in AI infrastructure • 69

**Summary** **................................................................................................................................ 70**

**Further reading** **....................................................................................................................... 70**

**<mark>Chapter 7: Edge AI Infrastructure and Integration</mark>** **<mark>73</mark>**

**Edge vs cloud AI: Infrastructure implications** **.........................................................................** **73**

Latency, bandwidth, and security • 74

Scalability and hybrid strategies • 74

**NVIDIA Jetson and Orin for edge AI.........................................................................................** **76**

Software ecosystem and scaling • 76

**Federated learning and distributed inference** **......................................................................... 78**

_Table of Contents_ viii

**Use cases: Smart cities, retail, industrial IoT** **..........................................................................** **80**

The NVIDIA ecosystem and business impact • 80

**Summary** **................................................................................................................................** **81**

**Further reading** **.......................................................................................................................** **81**

**<mark>Chapter 8: NGC, Triton Inference Server, and Deployment</mark>** **<mark>83</mark>**

**Using NGC Catalog for pretrained models............................................................................... 83**

Accessing the catalog • 84

**Triton Inference Server** **........................................................................................................... 86**

Architecture • 87

**Model ensemble and multi-framework serving** **...................................................................... 89**

Ensemble architecture • 90

**Serving at scale** **.......................................................................................................................** **91**

Load balancing and high availability • 91

**Summary** **................................................................................................................................** **93**

**Further reading** **.......................................................................................................................** **93**

**<mark>Chapter 9: Real-World AI Infrastructure and Enterprise Workf</mark>** **l** **<mark>ows</mark>** **<mark>95</mark>**

**Case study: Building an AI supercomputer..............................................................................** **95**

Hardware and networking • 96

Storage, orchestration, and real systems • 97

**Case study: Multi-tenant AI infrastructure for healthcare** **...................................................... 98**

Isolation and security • 99

**End-to-end workflow: Data** **→** **train** **→** **deploy** **→** **monitor.................................................... 101**

Deployment and monitoring • 103

**Summary** **..............................................................................................................................** **104**

**Further reading** **.....................................................................................................................** **104**

**<mark>Chapter 10: Unlock Your Exclusive Benef</mark>** **i** **<mark>ts</mark>** **<mark>107</mark>**

**Unlock this Book's Free Benefits in 3 Easy Steps....................................................................** **108**

**<mark>Other Books You May Enjoy</mark>** **<mark>112</mark>**

**<mark>Index</mark>** **<mark>115</mark>**

### **Preface**

AI infrastructure is a system, not a single accelerator. GPUs can provide the compute required
for training and inference, but useful performance also depends on storage, networking,
scheduling, software compatibility, monitoring, security, and operational discipline. When one
layer is poorly matched to the workload, expensive capacity can sit idle or a deployment can
become difficult to operate reliably.

This book provides a practical foundation for understanding that complete system. It is
written for technically aware readers who want to make sense of NVIDIA-powered AI
platforms and the relationships between their major components. The emphasis is on the
infrastructure decisions that connect hardware capabilities with real deployment
requirements.

The book builds progressively. It begins with the compute and software foundations of AI
infrastructure, then examines GPU partitioning and virtualization, storage and high-speed
networking, Kubernetes and cluster orchestration, performance analysis, and security. It then
moves to edge AI, NGC assets, Triton Inference Server, scalable serving, and enterprise case
studies that bring the layers together.

The examples draw on NVIDIA technologies such as CUDA, MIG, vGPU, the GPU Operator,
DCGM, Nsight, TensorRT, Jetson, NGC, and Triton, alongside Kubernetes, Slurm, Kubeflow,
MLflow, Prometheus, and Grafana. These products provide concrete reference points, but the
wider lessons concern workload fit, resource isolation, data movement, measurable
performance, layered security, and reliable operations.

Throughout the book, version-specific capabilities are treated as claims to verify rather than
universal guarantees. The objective is to help infrastructure practitioners connect the layers of
an AI platform, identify the trade-offs that matter, and validate a design against the workload,
environment, and operational evidence available.

**Who this book is for**

This book is for systems and cloud administrators, DevOps and platform engineers, solutions
architects, MLOps practitioners, and developers who want a structured introduction to
NVIDIA AI infrastructure. It is also useful for technical leads who need to evaluate GPU
platforms, orchestration choices, model-serving patterns, or edge and data-center trade-offs.

_Preface_ x

Readers should be familiar with basic Linux administration, containers, networking, and cloud
or data center concepts. No previous experience designing GPU platforms is required. The book
is beginner-friendly within an infrastructure context, but it is not an introduction to operating
systems, networking, Kubernetes, or machine learning from first principles.

**What this book covers**

_Chapter 1_, _Foundations of AI Infrastructure_, introduces the compute, storage, networking,
software, and orchestration layers of an AI platform. It compares CPU, GPU, and DPU roles,
follows GPU acceleration across the AI/ML pipeline, and introduces CUDA, NGC, Triton, and
DOCA.

_Chapter 2_, _GPU Resource Management and Virtualization_, explains how MIG, software-based
sharing, containers, and vGPU technologies divide or share GPU capacity. It also covers
Kubernetes discovery, allocation, scheduling, monitoring, quotas, and placement controls for
physical GPUs and MIG instances.

_Chapter 3_, _Storage, Networking, and Data Pipelines for AI_, compares local, shared, and object
storage and explains PCIe, NVLink, InfiniBand, RDMA, and GPUDirect. It connects those
components to data ingestion, ETL, training, validation, inference, and systematic datamovement optimization.

_Chapter 4_, _AI Cluster Orchestration and Scalability_, examines GPU-aware Kubernetes scheduling,
Helm, operators, autoscaling, and DCGM-based telemetry. It then connects Kubernetes with
Slurm, Kubeflow, and MLflow and compares on-premises, cloud-native, and hybrid cluster
topologies.

_Chapter 5_, _Performance Optimization and Monitoring_, uses Nsight Systems, Nsight Compute,
framework profilers, and GPU telemetry to locate bottlenecks. It explains TensorRT
optimization and develops a measurement-led tuning loop across compute, memory, storage,
and networking.

_Chapter 6_, _Security, Compliance, and Data Governance_, presents layered controls for GPUpowered workloads, including platform trust, isolation, image verification, encryption,
Kubernetes RBAC, and policy enforcement. It also distinguishes the obligations and evidence
associated with GDPR, HIPAA, and FedRAMP.

_Chapter 7_, _Edge AI Infrastructure and Integration_, compares edge and cloud infrastructure,
examines Jetson and Orin platforms, and separates federated learning from distributed
inference. Smart city, retail, and industrial IoT examples show how local processing and
centralized services work together.

xi _Preface_

_Chapter 8_, _NGC, Triton Inference Server, and Deployment_, covers NGC containers, models, SDKs,
and deployment resources before examining Triton model repositories, schedulers, backends,
ensembles, and APIs. It then develops the surrounding patterns for load balancing,
autoscaling, redundancy, and failover.

_Chapter 9_, _Real-World AI Infrastructure and Enterprise Workflows_, brings the stack together
through an AI supercomputer case study, a multi-tenant healthcare platform, and an end-toend enterprise lifecycle from data preparation and training to deployment, monitoring, and
feedback.

**To get the most out of this book**

A working understanding of Linux, containers, IP networking, storage, and cloud or datacenter infrastructure will make the architecture discussions easier to apply. Familiarity with
Kubernetes objects and the broad stages of a machine learning lifecycle is helpful, but the
NVIDIA infrastructure concepts are introduced as they become relevant.

The chapters contain commands, configuration excerpts, deployment patterns, and case
studies rather than one cumulative lab. Readers can follow the book in sequence to understand
how the layers depend on one another, then return to individual chapters when planning or
evaluating a particular environment.

When reproducing an example, first confirm that the GPU model, driver, firmware, operating
system, container stack, and NVIDIA software versions are compatible. Product behavior and
supported configurations change over time, so the documentation and release notes for the
chosen versions remain part of the validation process.

Use non-production resources and synthetic or sanitized data while experimenting. Access
controls, network boundaries, encryption, monitoring, recovery procedures, and compliance
evidence must be designed for the actual environment before a workload moves into
production.

**Download the color images**

Your purchase includes a color, DRM-free PDF copy of this book, ideal for viewing color images,
screenshots, and diagrams. Refer to _Free benefits with your book section_ at the end of the _Preface_ to
unlock your PDF copy.

_Preface_ xii

**Conventions used**

There are a number of text conventions used throughout this book.

**CodeInText** : Indicates code words in text, environment variables, class and method names,
filenames, extensions, paths, commands, and user input. For example: " Run `nvidia‑smi ‑L` to
list the GPUs visible to the driver."

A block of code is set as follows:

```
  resources:

   limits:

    nvidia.com/gpu: 1

```

When we wish to draw attention to a particular part of a code block, the relevant line or item is
set in bold:

Any command-line input or output is written as follows:

```
  nvidia-smi -L

```

**Bold** : Indicates a new term, an important word, or words visible on the screen. For example:
"Open the **NGC Catalog** and select **Models** ."

xiii _Preface_

**Stay ahead in AI-Powered networking – join 16,000+ subscribers**

AI is changing how networks are designed, managed, automated, and secured. The AI
Networking newsletter delivers focused, practical insights to help networking professionals
keep pace with this shift.

Each issue explores topics such as:

AI-assisted network automation and troubleshooting

Agentic workflows for network operations

MCP, network copilots, and emerging AI tools

Guardrails for safe and reliable automation

Real-world approaches to building AI-ready networks

Whether you're a network engineer, infrastructure professional, automation specialist, or
technology leader, AI Networking helps you understand what is changing (and how to apply
it) without the noise.

Scan the QR code to join for free and get weekly insights straight to your inbox:

```
          https://theainetworkengineer.substack.com/

```

_Preface_ xiv

**Get in touch**

Feedback from our readers is always welcome.

**General feedback** : If you have questions about any aspect of this book or have any general
feedback, please email us at `customercare@packt.com` and mention the book's title in the
subject of your message.

**Errata** : Although we have taken every care to ensure the accuracy of our content, mistakes do
happen. If you have found a mistake in this book, we would be grateful if you reported this to
us. Please visit `[https://www.packt.com/submit-errata](https://www.packt.com/submit-errata)`, click **Submit Errata**, and fill in the
form.

**Piracy** : If you come across any illegal copies of our works in any form on the internet, we would
be grateful if you would provide us with the location address or website name. Please contact
us at `copyright@packt.com` with a link to the material.

**If you are interested in becoming an author** : If there is a topic that you have expertise in and
you are interested in either writing or contributing to a book, please visit `[https://](https://authors.packt.com/)`

`[authors.packt.com/](https://authors.packt.com/)` .

**Share your thoughts**

Once you've read _Designing NVIDIA AI Infrastructure_, we'd love to hear your thoughts! Scan the
QR code below to go straight to the Amazon review page for this book and share your feedback.

```
             https://packt.link/r/1808080130

```

Your review is important to us and the tech community and will help us make sure we're
delivering excellent quality content.

xv _Preface_

**Free benefits with your book**

This book comes with free benefits to support your learning. Activate them now for instant
access (see the " _How to Unlock_ " section for instructions).

Here's a quick overview of what you can instantly unlock with your purchase:

_Preface_ xvi

**How to Unlock**

Scan the QR code (or go to `[packtpub.com/unlock](https://packtpub.com/unlock)` ). Search for this book by name, confirm the
edition, and then follow the steps on the page.

_Note: Keep your invoice handy. Purchases made directly from Packt don't require one_

# 1
#### Foundations of AI Infrastructure

This chapter lays the foundation for everything that follows. AI infrastructure is more than
hardware. It is a carefully engineered stack of compute, storage, networking, software, and
orchestration layers designed to support demanding AI workloads from training through
inference. Whether an organization is supporting large-scale model training or deploying realtime inference services, understanding the components and trade-offs of infrastructure design
is essential.

This chapter establishes the core building blocks of AI infrastructure, the design principles that
support scalability and performance, and the constraints that shape production deployments.
It also examines the roles of **CPUs** ( **Central Processing Units** ), **GPUs** ( **Graphics Processing**
**Units** ), and **DPUs** ( **Data Processing Units** ), shows how GPU acceleration applies across an AI/
ML pipeline, and introduces the NVIDIA software ecosystem that connects model development
with production serving and infrastructure offload.

This chapter covers the following topics:

Introduction to AI infrastructure design

The role of GPUs in AI workloads

CPU vs GPU vs DPU architectures

GPU acceleration for AI/ML pipelines

NVIDIA ecosystem overview

Let's get started!

_Chapter 1_ 2

**Introduction to AI infrastructure design**

At its core, AI infrastructure refers to the systems and components that power machine
learning from data ingestion through inference. It is not simply a collection of powerful GPUs.
Compute, storage, networking, software, and orchestration must be integrated in a way that
can handle massive datasets and increasingly complex models.

A well-designed AI infrastructure emphasizes speed, scalability, and security. This allows data
scientists and engineers to focus on experimentation and deployment without repeatedly
encountering performance barriers. The infrastructure can be understood through five
essential layers:

**Compute** includes GPUs, CPUs, and DPUs. DPUs offload infrastructure tasks such as
security and networking.

**Storage** must be fast and flexible. NVMe drives provide local speed, while shared file
systems and object stores provide scalable access.

**Networking** moves large datasets and model weights quickly. Technologies such as
NVLink, InfiniBand, and Ethernet support this movement.

**The software stack** includes drivers, CUDA libraries, operating systems, and AI
frameworks such as TensorFlow and PyTorch.

**Orchestration tools** such as Kubernetes, Slurm, and Airflow manage resources, jobs,
and automation. Kubernetes is widely used for this role in AI infrastructure.

AI workloads differ from traditional web or batch computing. Training models such as GPT or
ResNet can involve millions to billions of parameters. At this scale, practical training
commonly depends on parallel accelerators such as GPUs or TPUs, together with enough
device memory and interconnect bandwidth. Inference has a different requirement: low
latency or high throughput, depending on whether the application serves real-time requests or
processes data in batches.

3 _Foundations of AI Infrastructure_

These workloads are also dynamic. One job may run for minutes, while another may run for
days, and their consumption of compute and data fluctuates. Data access often becomes the
bottleneck, which makes I/O optimization as important as compute performance.

**Designing for production**

The choice between on-premises, cloud, and hybrid infrastructure depends on organizational
requirements. On-premises infrastructure provides full control over performance, security, and
data locality, but requires high capital expenditure and ongoing maintenance. Cloud platforms
provide rapid scalability and cost flexibility, which suits experimentation, but can introduce
vendor lock-in and data privacy concerns. Hybrid infrastructure combines the two approaches,
allowing sensitive workloads to remain on-premises while peak compute demand bursts to the
cloud. Latency requirements, compliance mandates, and budget constraints often drive the
final decision.

Several principles guide the design of AI infrastructure:

**Scalability** : The infrastructure must support larger models and datasets in the future.

**Utilization** : Expensive GPUs should not remain idle because low utilization wastes
money.

**Flexibility** : The environment should support multiple frameworks and users,
including TensorFlow and PyTorch workloads.

**Security** : Security is non-negotiable. Data in healthcare, finance, and proprietary
environments must be protected in motion and at rest.

**Monitoring and observability** : Visibility at every layer helps detect performance
problems, cost spikes, and system failures early.

AI infrastructure design is a team effort. Infrastructure engineers focus on hardware, cluster
design, and performance tuning. MLOps professionals handle workflows, CI/CD for models,
and system automation. Cloud and systems architects ensure scalability and cost efficiency.
These roles work closely with data scientists, IT administrators, and security teams to align
goals with constraints. Regardless of job title, understanding how the components fit together
is essential when deploying real-world AI.

Real-world implementations reflect different performance, latency, and deployment
requirements. NVIDIA DGX platforms integrate accelerated compute, high-speed networking,
and NVIDIA software for enterprise AI infrastructure. Google has documented large-scale TPUbased training for PaLM and the first-generation Gemini family. In retail, Instacart uses Jetson
Orin NX modules for real-time sensor fusion in its smart carts. These examples show why
infrastructure design must follow the workload and deployment context.

_Chapter 1_ 4

**The role of GPUs in AI workloads**

While CPUs remain essential for general-purpose compute, many AI workloads require high
arithmetic throughput, memory bandwidth, and parallel execution. GPUs are designed for this
form of work. This section explains how GPU architecture differs from CPU architecture, why
GPUs often outperform CPUs for parallel AI tasks, and how common ML frameworks use GPU
acceleration. It also shows why benchmark results must be interpreted with their full
hardware and software configurations.

**Why GPUs often outperform CPUs for AI workloads**

CPUs are designed **f** or versatility and low-latency execution across operating systems,
applications, and control-heavy workloads. Modern CPUs are parallel processors and include
multiple cores and vector instructions, but they generally expose less aggregate parallel
throughput and memory bandwidth than GPUs designed for accelerated computing. CPUs
remain important for orchestration, data preparation, control flow, and workloads that are too
small, branch-heavy, or latency-sensitive to benefit from GPU execution.

GPUs are designed for highly parallel computing. NVIDIA GPUs contain many execution units,
including CUDA cores and specialized tensor-processing units, that execute large numbers of
threads concurrently. CUDA uses a **single instruction, multiple thread** ( **SIMT** ) execution
model rather than a purely SIMD model. High-bandwidth device memory and wide memory
interfaces help keep those execution units supplied with data. Together, parallel execution and
memory throughput make GPUs well suited to matrix, tensor, and vector operations used in AI.

AI training relies heavily on matrix multiplication, convolution, attention, and the gradient
calculations used during backpropagation. These operations contain substantial parallel work.
A GPU can distribute that work across many execution units and process multiple samples or
tensor elements concurrently. The resulting improvement depends on the model, batch size,
numerical precision, implementation, and the balance between computation, memory access,
and data movement.

GPUs are not limited to training. During inference, they can support high-throughput
recommendation, natural language processing, and computer vision workloads, including
object detection on edge devices. Inputs may be processed as batches or streams. TensorRT and
GPU-enabled ONNX Runtime execution providers can optimize supported model execution for
lower latency or higher throughput, but the result remains model- and configuration-specific.

Performance gains depend on the model, dataset, batch size, numerical precision, software
versions, and the exact CPU and GPU configurations. Comparisons should therefore use results
that disclose the complete system and test setup, such as MLPerf Training ( `[https://](https://mlcommons.org/benchmarks/training/)`

`[mlcommons.org/benchmarks/training/](https://mlcommons.org/benchmarks/training/)` ) and MLPerf Inference ( `[https://mlcommons.org/](https://mlcommons.org/benchmarks/inference-datacenter/)`

5 _Foundations of AI Infrastructure_

`[benchmarks/inference-datacenter/](https://mlcommons.org/benchmarks/inference-datacenter/)` ). GPU acceleration can reduce time to train or improve
inference throughput for suitable workloads, but lower cost per job is not guaranteed. Cost
must be evaluated against utilization, power, software, infrastructure, and operational
requirements.

**Framework support and the NVIDIA GPU lineup**

Modern deep learning frameworks provide accelerator-enabled builds. TensorFlow, PyTorch,
and JAX use CUDA, compiler runtimes, and GPU-accelerated libraries such as cuDNN, cuBLAS,
and NCCL for supported operations. CPU execution remains available for many workloads, but
performance depends on the model and implementation rather than the presence or absence
of one device type alone. Understanding the supported framework, CUDA, driver, and library
versions is essential when building reproducible AI pipelines.

NVIDIA offers different GPU families and form factors for data center and edge workloads. The
A100 and H100 represent the Ampere and Hopper data center generations. The H200 extends
Hopper with 141 GB of HBM3e memory at 4.8 TB/s, targeting workloads that exhaust memory
before they exhaust compute. The Blackwell generation follows, with the B200 and the rackscale GB200 NVL72, which connects 72 Blackwell GPUs and 36 Grace CPUs over fifthgeneration NVLink; the Blackwell Ultra tier adds the B300 and GB300. The L40S targets AI,
graphics, and media workloads in data centers, the T4 remains an established inference
accelerator for supported environments, and Jetson modules target edge AI and robotics.
Product selection should follow current **c** ompatibility, memory, performance, power, and
lifecycle requirements rather than a model name alone.

**CPU vs GPU vs DPU architectures**

As AI systems evolve, specialized hardware becomes **i** ncreasingly important. NVIDIA describes
a three-chip model in which CPUs handle general-purpose logic and orchestration, GPUs
accelerate AI and high-performance computing, and DPUs offload selected networking,
storage, security, and telemetry functions. This is a useful architectural model, but it is not a
universal requirement: the exact mix of processors depends on the platform and workload.

**The three chip types**

The CPU remains the general-purpose control processor in most computing systems. Within AI
infrastructure, it runs the operating system, manages memory, schedules work, and
coordinates accelerators. CPUs can execute parallel numerical work, but GPUs are designed to
provide greater throughput for many matrix- and tensor-heavy operations. The CPU therefore
remains critical for control flow, preprocessing, workload scheduling, and coordination across
the system.

_Chapter 1_ 6

The GPU supplies the parallel compute capacity behind AI workloads. As described earlier in
this chapter, it distributes work across many execution units under a SIMT model, which suits
deep neural network training and high-throughput inference. Wide memory interfaces and
high compute density keep those units supplied with data.

The DPU is purpose-built for infrastructure workloads such as networking, storage I/O,
security, and telemetry. Offloading these operations reduces CPU overhead and allows the CPU
to concentrate on control tasks. DPUs are widely used to support zero-trust security models,
multi-tenant environments, and software-defined data centers, though the controls they
enable still depend on how the wider system is designed and operated.

The three processors have distinct architectural roles. CPUs contain fewer, more powerful cores
suited to logic, control flow, scheduling, and system-level operations. GPUs contain thousands
of smaller cores optimized for tensor operations, matrix multiplication, AI/ML, and highperformance computing. DPUs operate like programmable smart network interface cards,
managing data flows and enforcing security policies without interrupting CPU or GPU work.
Modern data centers combine these roles to balance performance, isolation, and scale.

_Figure 1.1_ compares the architectural roles of CPUs, GPUs, and DPUs.

_Figure 1.1: Architectural comparison of CPU, GPU, and DPU roles_

**The three-chip model in practice**

DPUs can support secure sharing of GPU clusters by offloading data-path **f** unctions such as
network segmentation, encryption, and policy enforcement. This is useful in cloud and edge
environments where workloads require isolation. In regulated deployments, DPU capabilities
can strengthen technical controls, but they do not establish compliance by themselves.
Compliance also depends on architecture, configuration, identity and access management,
operational processes, and audit evidence.

7 _Foundations of AI Infrastructure_

Used together, the three processors are intended to provide speed, control, and isolation within
a single platform, with each one carrying the work it is best suited to.

NVIDIA BlueField-3 ( `[https://docs.nvidia.com/networking/display/bf3dpu](https://docs.nvidia.com/networking/display/bf3dpu)` ) illustrates
this role. Depending on the adapter configuration, the platform supports Ethernet or
InfiniBand connectivity at rates up to 400 Gb/s and provides hardware acceleration for
networking, storage, and cybersecurity. DOCA services and libraries expose functions for
infrastructure processing and telemetry. The available offloads depend on the BlueField model,
firmware, DOCA version, and deployed software configuration; they are not automatic simply
because a DPU is installed. Developers use the NVIDIA DOCA framework ( `[https://](https://docs.nvidia.com/doca/sdk/doca-framework/)`

`[docs.nvidia.com/doca/sdk/doca-framework/](https://docs.nvidia.com/doca/sdk/doca-framework/)` ) to build and manage BlueField-accelerated
applications and services.

**GPU acceleration for AI/ML pipelines**

GPUs can accelerate several stages of the AI lifecycle, not only model training. Their role can
extend to data preprocessing, feature engineering, hyperparameter tuning, deployment, and
inference when the workload and software support parallel execution. RAPIDS, DALI,
TensorRT, and Triton provide GPU-accelerated components across an end-to-end workflow.

A typical AI/ML pipeline contains five major stages:

**Data ingestion and preprocessing**, where raw data is cleaned, normalized, and
prepared.

**Feature engineering and selection**, where meaningful model inputs are created.

**Model training and evaluation**, which can be computationally intensive.

**Hyperparameter tuning**, where multiple training configurations are evaluated.

**Deployment and inference**, where the trained model produces real-world predictions.

_Figure 1.2_ places GPU acceleration within the five stages of an AI/ML pipeline.

_Figure 1.2: Five stages of an AI/ML pipeline_

_Chapter 1_ 8

**Accelerating the data stages**

Data preprocessing **c** an become a bottleneck when CPU-side loading and transformation
cannot supply data to the accelerator fast enough. RAPIDS provides GPU-accelerated libraries
for common data science workloads: cuDF for DataFrame processing, cuML for machine
learning algorithms, and cuGraph for graph analytics. These libraries can accelerate supported
operations such as joins, transformations, graph processing, and model training. The result
depends on dataset size, algorithm, data transfer, hardware, and software configuration, so
speedup claims must be tied to a named benchmark and reproducible setup. The RAPIDS cuML
benchmarking utilities provide one way to compare a specific algorithm and dataset against a
stated CPU baseline.

Image and video preprocessing can be expensive. NVIDIA DALI ( `[https://docs.nvidia.com/](https://docs.nvidia.com/deeplearning/dali/main-user-guide/docs/index.html)`

`[deeplearning/dali/main-user-guide/docs/index.html](https://docs.nvidia.com/deeplearning/dali/main-user-guide/docs/index.html)` ) accelerates data loading and can
offload supported operations such as decoding, resizing, cropping, and normalization to the
GPU. Current DALI documentation provides framework plugins or integrations for PyTorch,
TensorFlow, PaddlePaddle, and JAX. The MXNet plugin was supported only through DALI 1.39.
DALI also supports on-the-fly augmentation, prefetching, parallel execution, and batch
processing, which can reduce input-pipeline bottlenecks when the workload is configured
appropriately.

**Accelerating training, tuning, and inference**

Training models such as ResNet, BERT, or GPT may require more compute or memory than one
GPU can provide within the desired envelope. PyTorch **DistributedDataParallel** ( **DDP** ),
TensorFlow **MultiWorkerMirroredStrategy** ( **MWMS** ), and Horovod can distribute supported
training workloads across multiple GPUs and machines. Scaling is not automatic: network
bandwidth, collective communication, data loading, batch size, and framework configuration
determine efficiency. Distributed training can reduce time to train when the workload scales
effectively, but it does not guarantee linear speedup or unchanged convergence.

Hyperparameter tuning may require many training runs with different learning rates, batch
sizes, regularization values, and other parameters. GPUs can execute independent trials
concurrently when sufficient resources are available, particularly when paired with tools such
as Optuna, Ray Tune, or Weights & Biases Sweeps. Parallel execution can evaluate more
configurations within a fixed time budget, but the scheduling policy, search algorithm, and
available GPU memory determine the practical gain.

Inference is the point at which a model meets the real world, so latency and throughput
matter. A workload may involve batch scoring large datasets or making real-time decisions.
TensorRT ( `[https://docs.nvidia.com/deeplearning/tensorrt/latest/](https://docs.nvidia.com/deeplearning/tensorrt/latest/)` ) optimizes
supported models for NVIDIA GPU inference and can use reduced precision when the accuracy

9 _Foundations of AI Infrastructure_

trade-off is **a** cceptable. Triton Inference Server ( `[https://docs.nvidia.com/deeplearning/](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html)`

`[triton-inference-server/user-guide/docs/index.html](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html)` ), which NVIDIA now also refers to
as NVIDIA Dynamo-Triton following its move into the Dynamo platform, supports multiple
backends, dynamic batching, concurrent model execution, and standard inference protocols.
Achievable latency, throughput, concurrency, and reliability depend on the model, server
configuration, client behavior, network, and deployment architecture.

To summarize, GPUs can accelerate more than model training. Supported preprocessing,
training, tuning, and inference workloads can use RAPIDS, DALI, TensorRT, and Triton as parts
of a GPU-accelerated workflow. The benefit must be measured end to end because data
movement, unsupported operations, orchestration overhead, and low utilization can reduce or
eliminate the expected gain. Acceleration improves model execution performance; it does not
by itself improve model accuracy or guarantee lower cost.

**NVIDIA ecosystem overview**

NVIDIA is more than a hardware company. A software ecosystem sits above the GPUs and
determines what applications can actually do with them. This section covers the main
components: CUDA, the programming platform; cuDNN, the deep learning operation library;
NGC, the container and model catalog; and Triton, the multi-backend inference server. It then
looks at how these fit together across training pipelines and production systems, and what has
to be validated before they work as one stack.

**The NVIDIA AI software stack**

The NVIDIA AI software stack spans the layers required to develop and operate GPUaccelerated applications. Supported environments combine NVIDIA GPU drivers and the CUDA
platform with accelerated libraries, frameworks, containers, pretrained models, serving
software, and orchestration components. Portability and performance depend on supported
hardware, operating systems, drivers, CUDA versions, container images, and framework
compatibility, so the stack must be validated as a complete configuration.

_Figure 1.3_ shows how NVIDIA hardware, software, content, orchestration, and infrastructure
offload fit together.

_Chapter 1_ 10

_Figure 1.3: Layered view of NVIDIA AI software and infrastructure components_

CUDA ( `[https://docs.nvidia.com/cuda/cuda-programming-guide/index.html](https://docs.nvidia.com/cuda/cuda-programming-guide/index.html)` ) is the core

platform that allows applications to use NVIDIA GPUs for general-purpose accelerated
computing. It provides programming support and toolchains for C++, Fortran, and other
languages, with Python access through libraries, frameworks, and bindings. Specialized CUDA
libraries include cuBLAS for linear algebra, cuDNN for deep learning operations, and NCCL for
collective communication across GPUs.

cuDNN ( `[https://docs.nvidia.com/deeplearning/cudnn/latest/](https://docs.nvidia.com/deeplearning/cudnn/latest/)` ), the **CUDA Deep Neural**
**Network** library, provides highly tuned GPU implementations of operations used in deep
learning. Current documentation includes scaled dot-product attention, convolution, matrix
multiplication, normalization, softmax, pooling, pointwise operations, and supported fusion
patterns. Frameworks such as TensorFlow and PyTorch use cuDNN in compatible NVIDIA GPU
builds. The exact operations, hardware support, and performance characteristics depend on
the cuDNN, CUDA, driver, framework, and GPU versions.

**Deployment and infrastructure components**

The NVIDIA NGC Catalog ( `[https://catalog.ngc.nvidia.com/](https://catalog.ngc.nvidia.com/)` ) provides GPU-optimized
containers, pretrained models, SDKs, and Helm charts for supported cloud, data center, and
edge environments. Containers package compatible user-space libraries and frameworks,
while Helm charts can support deployment to Kubernetes. Availability, licensing,
compatibility, and deployment steps vary by artifact and version, so each catalog entry and its
release notes must be checked before use.

11 _Foundations of AI Infrastructure_

Once a model is trained, it needs a serving path. Triton supports multiple deep learning and
machine learning backends, including TensorFlow, PyTorch, ONNX Runtime, TensorRT, and
the FIL backend used for formats such as XGBoost. Features include dynamic batching,
concurrent model execution, model pipelines, version policies, HTTP/REST and gRPC
protocols, and server metrics. Triton can run in a container and can be deployed under
Kubernetes, but production readiness still depends on surrounding concerns such as health
checks, autoscaling, load balancing, observability, security, and high availability.

While CUDA powers GPU computation, the NVIDIA DOCA framework supports applications
and services that use BlueField DPUs and SuperNICs for networking, storage, security, and
telemetry. These capabilities can offload selected infrastructure work from the host and can
support isolation and observability controls. They do not automatically create a zero-trust or
compliant architecture; those outcomes depend on the complete system design, policy,
configuration, and operations.

Putting it all together: CUDA and accelerated libraries provide the programming and execution
foundation. NGC distributes versioned containers, models, SDKs, and deployment artifacts.
Triton provides a multi-backend inference-serving layer. DOCA and BlueField provide a
separate path for supported infrastructure offload. These components can be combined into an
end-to-end platform, but compatibility, performance, security, and reliability must be
validated for the chosen versions and deployment architecture.

**Summary**

In this chapter, we explored the foundations of AI infrastructure, including its core
components and deployment considerations. We examined how CPUs, GPUs, and DPUs can
work together to support AI workloads and how GPU acceleration can apply across an AI/ML
pipeline. We also saw why performance claims in this field have to be read alongside the
hardware, software, and configuration that produced them.

We also introduced NVIDIA's ecosystem, including CUDA, NGC, Triton, and DOCA, and
explained how these technologies contribute to scalable, secure, and production-oriented AI
systems when they are configured as part of a complete architecture.

_Chapter 1_ 12

**Further reading**

To learn more about the topics that were covered in this chapter, take a look at the following
resources:

NVIDIA DGX platforms: `[https://www.nvidia.com/en-us/data-center/dgx-](https://www.nvidia.com/en-us/data-center/dgx-platform/)`

```
platform/

```

NVIDIA H200 Tensor Core GPU: `[https://www.nvidia.com/en-us/data-center/h200/](https://www.nvidia.com/en-us/data-center/h200/)`

NVIDIA GB200 NVL72: `[https://www.nvidia.com/en-us/data-center/gb200-nvl72/](https://www.nvidia.com/en-us/data-center/gb200-nvl72/)`

PaLM: `[https://research.google/pubs/palm-scaling-language-modeling-with-](https://research.google/pubs/palm-scaling-language-modeling-with-pathways/)`

```
pathways/

```

First-generation Gemini family: `[https://arxiv.org/abs/2312.11805](https://arxiv.org/abs/2312.11805)`

Instacart case study: `[https://www.nvidia.com/en-us/case-studies/instacart/](https://www.nvidia.com/en-us/case-studies/instacart/)`

SIMT execution model: `[https://docs.nvidia.com/cuda/cuda-programming-guide/](https://docs.nvidia.com/cuda/cuda-programming-guide/03-advanced/advanced-kernel-programming.html)`

```
03-advanced/advanced-kernel-programming.html

```

RAPIDS cuML benchmarking utilities: `[https://docs.rapids.ai/api/cuml/stable/](https://docs.rapids.ai/api/cuml/stable/api/cuml.benchmark/)`

```
api/cuml.benchmark/

```

MXNet plugin support: `[https://docs.nvidia.com/deeplearning/dali/archives/](https://docs.nvidia.com/deeplearning/dali/archives/dali_1_39_0/user-guide/plugins/mxnet_tutorials.html)`

```
dali_1_39_0/user-guide/plugins/mxnet_tutorials.html

```

# 2
#### GPU Resource Management and Virtualization

Modern GPUs provide enough compute capacity to support several workloads, users, or
services at the same time. Using that capacity efficiently requires more than assigning an entire
GPU to every job. Infrastructure teams need mechanisms that divide, share, isolate, virtualize,
and schedule GPU resources while keeping performance predictable.

This chapter examines four approaches to GPU resource management. It begins with **Multi-**
**Instance GPU** ( **MIG** ) configuration and then considers software-based sharing and isolation.
It also explains **virtual GPUs** ( **vGPUs** ) for VM-based environments and concludes with
Kubernetes scheduling, monitoring, and allocation techniques for GPU workloads.

This chapter covers the following topics:

MIG configuration

GPU sharing and isolation techniques

Virtual GPUs (vGPU) setup and use cases

GPU workload scheduling with Kubernetes

Let's get started!

**MIG configuration**

As AI workloads scale, efficient GPU utilization becomes critical. Multi-Instance GPU, or MIG,
is an NVIDIA capability introduced with the A100 GPU. It partitions a supported physical GPU
into isolated GPU instances with dedicated compute and memory resources. This section
explains how MIG works, where its isolation boundary sits, and how to configure an A100
safely for multi-tenant AI workloads.

_Chapter 2_ 14

**How MIG works**

MIG can divide a 40 GB or 80 GB NVIDIA A100 into as many as seven GPU instances. Each GPU
instance receives **d** edicated **streaming multiprocessor** ( **SM** ) slices, memory capacity, memory
bandwidth, and L2 cache. Because these resources are partitioned in hardware, MIG provides
memory protection, fault isolation, and more predictable quality of service than software-only
sharing.

Modern GPUs such as the A100 can be larger than a small or medium AI workload requires.
Without partitioning, multiple workloads on the same GPU may contend for resources or wait
in a queue. MIG replaces that arrangement with fixed partitions, allowing smaller isolated jobs
to run concurrently and improving the use of each GPU hour.

MIG partitions are organized in two layers. **GPU instances** ( **GIs** ) combine GPU compute slices
with dedicated memory slices and GPU engines. A GI can then be subdivided **i** nto **compute**
**instances** ( **CIs** ). Each CI receives dedicated SM slices but shares the memory and engines of its
parent GI. This distinction matters because the GI is the memory-isolation boundary, while a
CI further partitions compute within that boundary.

_Figure 2.1_ shows the relationship between GPU instances and compute instances in the MIG
hierarchy.

_Figure 2.1: GPU instances and compute instances in the MIG hierarchy_

15 _GPU Resource Management and Virtualization_

The available profiles define the balance between compute slices and memory. The examples in
this chapter, including `1g.5gb`, `2g.10gb`, and `3g.20gb`, are specific to the 40 GB A100. In this
naming convention, `g` identifies the number of GPU compute slices and the memory suffix
identifies the profile's framebuffer class. For example, a `2g.10gb` profile uses two compute
slices and a 10 GB memory profile. A 40 GB A100 can expose as many as seven `1g.5gb`
instances. The 80 GB A100 uses different profile names, including `1g.10gb`, `2g.20gb`, and `3g.`

`40gb` . Always list the profiles exposed by the installed GPU and driver rather than assuming
that A100 profile names apply to another model. See the supported MIG profiles ( `[https://](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-mig-profiles.html)`

`[docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-mig-profiles.html](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-mig-profiles.html)` ) for
the current per-GPU tables.

**Configuring and monitoring MIG**

MIG is useful wherever GPU resources must be shared safely and efficiently. A JupyterHub
deployment can provide each user with a dedicated GPU slice. An inference platform can
isolate several models across separate instances. Universities and research laboratories can
segment a large GPU for parallel experiments, while cloud AI platforms can use MIG to provide
hardware-isolated GPU multi-tenancy.

We start with a basic MIG setup on GPU 0 of an A100 40 GB system.

1.

2.

First, confirm that no workload is using GPU 0, then enable MIG mode with
administrative privileges:

```
   sudo nvidia-smi -i 0 -mig 1

```

On an A100, enabling MIG mode causes the driver to attempt a GPU reset. If another
client is using the device, the command can remain pending until the client is stopped
or the system is rebooted. MIG mode persists across reboots on Ampere GPUs until it is
explicitly disabled.

Next, list the GPU instance profiles available on the installed A100 and driver:

```
   sudo nvidia-smi mig -lgip

```

_Chapter 2_ 16

3.

4.

Create one `1g.5gb` GPU instance and its corresponding compute instance. The `‑cgi`
option selects the GPU instance profile, and `‑C` creates the compute instance
automatically:

```
   sudo nvidia-smi mig -cgi 1g.5gb -C

```

Verify that the GPU instance and compute instance are visible:

```
   nvidia-smi -L

```

GPU and compute instance configurations are not persistent after a GPU reset or system
reboot. Production environments should recreate the required geometry during node
initialization, for example with NVIDIA MIG Partition Editor ( `mig‑parted` ) or the MIG
Manager included with NVIDIA GPU Operator.

The resulting MIG instances can be assigned to Docker containers, Kubernetes pods, or
individual users, giving the infrastructure team direct control over GPU allocation.

MIG-enabled GPUs can be enumerated with `nvidia‑smi ‑L`, and `nvidia‑smi` reports
configuration and memory information. On A100 and A30, however, NVIDIA documents GPU
utilization for MIG devices as unavailable in `nvidia‑smi` . For supported instance-level metrics,
NVIDIA **Data Center GPU Manager** ( **DCGM** ) and DCGM Exporter expose telemetry to
Prometheus **a** nd Grafana. Metric availability remains dependent on the GPU architecture,
driver, and DCGM version.

Partition sizes should reflect workload requirements. A training job that requires 20 GB of
memory will not fit in a `1g.5gb` instance. Excessive fragmentation can also leave slices
underutilized. MIG support is tied to exact GPU products, not to every GPU in a generation. The
current supported-GPU table lists GB200; B200; RTX PRO 6000 Blackwell Server, Workstation,
and Max-Q Workstation Editions; RTX PRO 5000 Blackwell; RTX PRO 4500 Blackwell; Thor
iGPU; H100-SXM5 and H100-PCIe in 80 GB and 94 GB variants; H100 on GH200; H20; H200SXM5; H200 NVL; A100-SXM4 and A100-PCIe in 40 GB and 80 GB variants; and A30. The
examples in this chapter remain scoped to the A100 40 GB.

**GPU sharing and isolation techniques**

MIG provides hardware partitioning, but many environments still depend on shared GPU
access, particularly when they use older GPUs or workloads with changing resource demands.
Safe sharing requires controls across processes, containers, frameworks, and schedulers,
together with an understanding of the trade-offs between utilization, fairness, performance,
and isolation.

17 _GPU Resource Management and Virtualization_

GPUs are expensive resources, yet many inference and lightweight training workloads do not
require an entire device. Some workloads use the GPU only during particular execution phases,
such as forward or backward passes. Sharing allows an organization to increase utilization,
lower costs, and serve multiple users or services on the same hardware. This is especially useful
in cloud-native and multi-tenant environments.

Common sharing techniques operate at different layers:

Time slicing alternates GPU execution among multiple processes.

Container isolation uses Linux namespaces and cgroups to establish logical
boundaries.

Framework-level controls in TensorFlow and PyTorch manage memory growth or perprocess allocation.

Schedulers such as Kubernetes and Slurm apply placement and fairness policies.

Time slicing allows the GPU driver to alternate execution among processes. This enables
multiple workloads to use one device, but it does not partition GPU memory or create the fault
and quality-of-service boundaries provided by MIG. Performance can vary when workloads
compete for compute or memory bandwidth, and one process can exhaust shared framebuffer
memory. Time slicing therefore suits development, interactive, or lightweight inference
workloads only when variable performance and shared-memory risk are acceptable.

Containers provide lightweight process and filesystem isolation in shared environments.
Docker's `‑‑gpus` flag and the NVIDIA Container Toolkit control which GPU devices a container
can access. Linux cgroups can limit host CPU, system memory, and I/O, but they do not
partition GPU compute capacity or framebuffer memory. Unless MIG, vGPU, MPS controls, or
an explicit time-slicing configuration is added, containers that share one GPU still share its
hardware resources.

**Managing memory and scheduling**

GPU memory contention is one of the largest risks in a shared environment. If several processes
request more memory than the device contains, workloads can slow down or fail with an outof-memory error. TensorFlow supports incremental allocation with

`TF_FORCE_GPU_ALLOW_GROWTH=true` and also provides programmatic logical-device memory
limits. PyTorch provides a per-process memory-fraction API. These controls manage allocation
behavior within a framework, but they do not create the hardware isolation provided by MIG.

`nvidia‑smi` provides device-level visibility, while DCGM supports continuous telemetry and
alerting.

In Kubernetes, the NVIDIA device plugin exposes GPUs as schedulable resources and supports
MIG configurations. Administrators can apply resource quotas, map pods to GPUs, and use

_Chapter 2_ 18

node affinity, taints, and tolerations to direct workloads to suitable GPU nodes. These controls
help distribute shared GPU capacity more fairly and reduce scheduling collisions.

Several practices improve predictability in a shared cluster:

Avoid colocating latency-sensitive inference with long-running training on the same
software-shared GPU unless performance tests show that the chosen isolation and
scheduling policy meets both workloads' service objectives.

Namespaces and user quotas can prevent greedy or runaway jobs.

Per-job and per-user monitoring can reveal anomalies.

Where supported, MIG or MIG-backed vGPU provides stronger hardware isolation and more
consistent resource access than software-only sharing. Time-sliced vGPU still shares compute
over time and should not be described as equivalent to a MIG partition.

Each technique involves a different compromise. Time slicing is straightforward but provides
no fixed memory or compute partition. Containers establish process boundaries and device
visibility without partitioning GPU hardware. MIG provides hardware-isolated GPU instances
but only on supported products and fixed profiles. vGPU integrates GPU access with VM
management, while its isolation and performance characteristics depend on whether the
selected profile is time-sliced or MIG-backed.

_Figure 2.2_ compares the isolation boundary, resource model, and constraints of the principal
GPU-sharing techniques.

_Figure 2.2: Comparison table of GPU sharing techniques_

The appropriate **c** hoice **d** epends on the required balance of isolation, cost, compatibility, and
performance.

19 _GPU Resource Management and Virtualization_

**Virtual GPUs (vGPU) setup and use cases**

Physical GPUs can be difficult to allocate efficiently in environments built around virtual
machines, **virtual desktop infrastructure** ( **VDI** ), or cloud virtualization. NVIDIA virtual GPU,
or vGPU, technology allows a supported physical GPU to provide GPU devices to multiple
virtual machines. Depending on the product, profile, and platform, those vGPUs can share
compute through time slicing or use MIG-backed hardware partitions.

A vGPU is a virtual GPU device assigned to a VM through a supported hypervisor and NVIDIA
vGPU Manager. It provides GPU acceleration while preserving VM lifecycle and management
boundaries. This makes vGPU suitable for VDI, enterprise applications, and AI development or
compute environments that require VM-based deployment.

**How vGPU works**

The host runs a supported hypervisor and contains the physical NVIDIA GPU. NVIDIA vGPU
Manager creates vGPU devices and assigns them to VMs. Each VM installs a compatible
NVIDIA guest driver. A time-sliced vGPU receives a defined framebuffer allocation while
sharing compute according to the scheduling policy. A MIG-backed vGPU maps the VM to a
hardware-isolated MIG partition. The VM sees the assigned vGPU as a device, while the
hypervisor and vGPU Manager coordinate access to the physical GPU.

_Figure 2.3_ shows how vGPU Manager exposes physical GPU resources to virtual machines.

_Figure 2.3: Physical GPU resources exposed to virtual machines through vGPU Manager_

NVIDIA uses different profile families for different products and workloads. Q-series profiles,
such as `A16‑1Q`, target virtual workstations and graphics use cases under NVIDIA vGPU

_Chapter 2_ 20

software. C-series compute profiles are now documented under NVIDIA AI Enterprise vGPU for
Compute. For example, `A100‑20C` is a time-sliced 20 GB compute vGPU profile for an A100 PCIe
40 GB GPU. MIG-backed A100 profiles use names such as `A100‑3‑20C` and map to the
corresponding MIG geometry. A profile name should therefore be interpreted only within the
documented GPU model, product family, and software release.

vGPU combines GPU acceleration with centralized VM management and supported lifecycle
capabilities. Exact features, including suspend and resume, migration, and update behavior,
vary by GPU, hypervisor, guest operating system, and software release. A deployment should
therefore be designed against the version-specific support matrix rather than assuming that
every virtualization feature applies to every vGPU profile.

The sharing methods differ primarily in their isolation boundary and deployment model.
Time-sliced vGPU integrates temporal sharing with VM management but does not provide a
fixed compute partition. MIG-backed vGPU combines VM assignment with MIG's hardware
isolation. Bare-metal or container-native MIG exposes the same hardware partitioning
without requiring a VM. Driver-level time slicing remains the lightest option and provides the
weakest isolation.

_Figure 2.4_ distinguishes vGPU, MIG-backed vGPU, bare-metal MIG, and driver-level time
slicing.

_Figure 2.4: Comparison of vGPU, MIG, and time slicing_

**Requirements, use cases, and management**

A vGPU deployment requires compatible hardware, a supported virtualization platform,
compatible host and guest drivers, and the correct license. Two NVIDIA product families must
be distinguished. NVIDIA vGPU software 19.x, the long-term support branch, ( `[https://](https://docs.nvidia.com/vgpu/19.0/index.html)`

21 _GPU Resource Management and Virtualization_

`[docs.nvidia.com/vgpu/19.0/index.html](https://docs.nvidia.com/vgpu/19.0/index.html)` ) covers the vWS, vPC, and vApps products used for
graphics, desktops, and applications. Its supported-GPU list includes A2, A10, A16, A40, RTX Aseries GPUs, L2, L4, L20, L40, L40S, RTX Ada GPUs, and supported RTX PRO Blackwell server
products, together with older products that remain in maintenance or extended support. A100
compute profiles are not part of that graphics-focused list. They are provided through NVIDIA
AI Enterprise vGPU for Compute and require an NVIDIA AI Enterprise license.

For vGPU software 19.x, NVIDIA publishes separate support tables for XenServer, Linux with
KVM, Microsoft Azure Local, Microsoft Windows Server, Nutanix AHV, Red Hat Enterprise
Linux with KVM, Ubuntu, and VMware vSphere ESXi. The exact GPU, hypervisor release, guest
operating system, and driver combination must be checked in the vGPU 19.x product support
matrix. The host vGPU Manager and guest driver do not always need identical build numbers,
but they must form a supported combination. When NVIDIA permits a guest driver from
another release in the same branch or a supported previous branch, only features common to
both releases are available. An incompatible combination prevents the vGPU from loading.

vGPU supports several enterprise and research use cases. A data science team can receive GPUaccelerated development VMs, while a university can assign a separate virtualized GPU
instance to each research group. VDI deployments can provide remote access to 3D design,
video rendering, and simulation workloads. The same model can deliver GPU-accelerated
cloud desktops to distributed teams.

NVIDIA's vGPU software suite includes host-side management, guest drivers, licensing, and
monitoring components. Administrators can inspect allocations and usage through the
hypervisor's management tools and NVIDIA command-line interfaces. vWS, vPC, and vApps
clients obtain licenses from NVIDIA License System; NVIDIA AI Enterprise enforces one license
per vGPU assigned to a compute VM. If a required license is not acquired, the VM continues
with reduced capability rather than providing normal licensed performance. DCGM and
Prometheus exporters can supply GPU telemetry where the selected hardware and software
combination supports the required metrics.

**GPU workload scheduling with Kubernetes**

As more AI workloads shift to cloud-native architectures, Kubernetes is widely used to
orchestrate containers that require GPU acceleration. GPUs are extended resources rather than
native CPU or memory resources, so nodes require vendor drivers, a device plugin, and explicit
scheduling configuration. This section explains how Kubernetes discovers GPUs, how pods
request them, and how placement, MIG strategy, quotas, and telemetry support predictable
allocation.

Kubernetes provides a control plane for deploying and managing containerized workloads
across on-premises and cloud infrastructure. The NVIDIA device plugin adds supported GPU

_Chapter 2_ 22

devices to the resources advertised by each node. Kubernetes then schedules pods against
those integer-valued extended resources; fractional sharing requires an additional NVIDIA
time-slicing, MPS, MIG, or vGPU configuration.

**Enabling and requesting GPUs**

GPU support begins with a compatible NVIDIA driver and container runtime configuration on
every GPU-enabled node. The NVIDIA device plugin ( `[https://github.com/NVIDIA/k8s-](https://github.com/NVIDIA/k8s-device-plugin)`

`[device-plugin](https://github.com/NVIDIA/k8s-device-plugin)` ) is then deployed as a DaemonSet. It discovers the available devices and
advertises them to the kubelet and scheduler as allocatable extended resources. The plugin
also supports MIG-aware scheduling when it is configured with the appropriate strategy.

The following complete Pod manifest runs NVIDIA's documented CUDA vector-add sample
and requests one GPU:

```
  apiVersion: v1

  kind: Pod

  metadata:

   name: gpu-vector-add

  spec:

   restartPolicy: Never

   containers:

    - name: cuda-sample

     image: nvcr.io/nvidia/k8s/cuda-sample:vectoradd-cuda12.5.0

     resources:

      requests:

       nvidia.com/gpu: 1

      limits:

       nvidia.com/gpu: 1

```

Kubernetes schedules the pod only on a node with available `nvidia.com/gpu` capacity. For GPU
extended resources, a pod can specify only `limits`, in which case Kubernetes uses the limit as
the request, or it can specify both `requests` and `limits` with equal values, as in this example. A
GPU request without a corresponding limit is not valid. If no suitable device is available, the
pod remains pending. See the Kubernetes guidance for scheduling GPUs for the current
extended-resource rules ( `[https://kubernetes.io/docs/tasks/manage-gpus/scheduling-](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)`

`[gpus/](https://kubernetes.io/docs/tasks/manage-gpus/scheduling-gpus/)` ).

Save the manifest as `gpu‑pod.yaml`, apply it with `kubectl apply ‑f gpu‑pod.yaml`, and
inspect the result with `kubectl logs gpu‑vector‑add` . The sample should report `Test`

`PASSED` when the driver, runtime, device plugin, and image are compatible.

23 _GPU Resource Management and Virtualization_

Node selectors or node affinity, taints, and tolerations provide finer placement control. GPU
nodes can be labeled, and a pod can use a node selector or affinity rule to require that label. A
NoSchedule taint can keep general workloads away from GPU nodes, while a matching
toleration admits the intended GPU workload. Labels and taints are scheduling controls only;
the device plugin resource request remains responsible for allocating a GPU.

MIG-enabled GPUs provide a more granular scheduling unit. The NVIDIA device plugin
supports `single` and `mixed` MIG strategies. Under `single`, nodes use a uniform MIG
configuration and MIG devices are advertised through the generic `nvidia.com/gpu` resource.
Under `mixed`, each profile is advertised by name. An A100 40 GB `1g.5gb` instance is therefore
requested as `nvidia.com/mig‑1g.5gb` . Use the mixed strategy whenever a pod must request a
specific profile rather than an interchangeable MIG device.

```
  resources:

  limits:

  nvidia.com/mig-1g.5gb: 1

```

NVIDIA documents the exact names and behavior in its MIG support for Kubernetes guide
( `[https://docs.nvidia.com/datacenter/cloud-native/kubernetes/latest/index.html](https://docs.nvidia.com/datacenter/cloud-native/kubernetes/latest/index.html)` )

**Monitoring and best practices**

Once GPU workloads are running, monitoring verifies that allocations behave as intended.

`kubectl describe pod` shows the requested extended resource and scheduling events. On the
node, `nvidia‑smi` enumerates the physical or MIG devices and the processes visible to the
driver. For cluster-wide telemetry, DCGM Exporter attaches Kubernetes labels to supported
GPU metrics, exposes them to Prometheus, and allows Grafana to visualize utilization,
framebuffer memory, temperature, power, and error counters. The metrics available for a
particular MIG instance depend on the GPU architecture and DCGM release.

Efficient scheduling also depends on policy. `ResourceQuota` can cap extended-resource
consumption in a namespace, while priority classes influence which workloads are scheduled
or preempted when capacity is constrained. Avoid colocating latency-sensitive inference with
training unless the sharing mechanism and performance tests demonstrate acceptable
interference. Long-running training jobs should use accurate CPU and memory requests,
checkpointing, and disruption policies appropriate to the platform; GPU allocation alone does
not protect a pod from node failure or every form of eviction.

Several open-source tools extend Kubernetes GPU scheduling and accounting. **NVIDIA GPU**
**Feature Discovery** ( **GFD** ) detects GPU **c** apabilities and publishes node labels used for
placement. OpenCost and Kubecost can allocate configured GPU costs to Kubernetes

_Chapter 2_ 24

workloads using metrics such as `container_gpu_allocation` . Volcano ( `[https://volcano.sh/](https://volcano.sh/docs/home/introduction/)`

`[docs/home/introduction/](https://volcano.sh/docs/home/introduction/)` ) adds batch-oriented features including queues, gang scheduling,
bin packing, and fair multi-resource scheduling. The KAI Scheduler ( `[https://github.com/](https://github.com/kai-scheduler/KAI-Scheduler)`

`[kai-scheduler/KAI-Scheduler](https://github.com/kai-scheduler/KAI-Scheduler)` ) is an open-source Kubernetes-native scheduler for AI
workloads that provides queues, quotas, preemption, and fair-share GPU allocation.

**Summary**

In this chapter, we explored how MIG, software-based sharing, containers, and vGPU
technology divide or share GPU resources across different workloads and deployment models.
We distinguished hardware partitioning from temporal sharing and clarified how vGPU
behavior changes between time-sliced and MIG-backed profiles.

Finally, we examined how Kubernetes discovers, schedules, and monitors physical GPUs and
MIG instances. Complete pod resource specifications, profile-aware MIG strategy, placement
controls, telemetry, quotas, and scheduler extensions provide the foundation for fair and
predictable GPU allocation.

**Further reading**

To learn more about the topics that were covered in this chapter, take a look at the following
resources:

MIG user guide: `[https://docs.nvidia.com/datacenter/tesla/mig-user-guide/](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/concepts.html)`

```
concepts.html

```

DCGM Exporter: `[https://docs.nvidia.com/datacenter/cloud-native/gpu-](https://docs.nvidia.com/datacenter/cloud-native/gpu-telemetry/latest/dcgm-exporter.html)`

```
telemetry/latest/dcgm-exporter.html

```

Current supported-GPU table: `[https://docs.nvidia.com/datacenter/tesla/mig-](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/supported-gpus.html)`

```
user-guide/supported-gpus.html

```

NVIDIA AI Enterprise vGPU for Compute: `[https://docs.nvidia.com/ai-enterprise/](https://docs.nvidia.com/ai-enterprise/release-7/latest/infra-software/vgpu.html)`

```
release-7/latest/infra-software/vgpu.html

```

vGPU 19.x product support matrix: `[https://docs.nvidia.com/vgpu/19.0/product-](https://docs.nvidia.com/vgpu/19.0/product-support-matrix/index.html)`

```
support-matrix/index.html

```

NVIDIA GPU Feature Discovery: `[https://github.com/NVIDIA/k8s-device-plugin/](https://github.com/NVIDIA/k8s-device-plugin/blob/main/docs/gpu-feature-discovery/README.md)`

```
blob/main/docs/gpu-feature-discovery/README.md

```

# 3
#### Storage, Networking, and Data Pipelines for AI

AI infrastructure depends on a continuous flow of data. Storage must deliver datasets and
checkpoints at the required speed, networking must move gradients, weights, activations, and
inputs without delaying compute, and the data pipeline must coordinate these resources from
ingestion through inference. A weakness in any one layer can leave expensive GPUs idle.

This chapter examines the storage, networking, and pipeline decisions that keep AI workloads
supplied with data. It compares local, shared, and object storage; explains NVLink, InfiniBand,
and **remote direct memory access** ( **RDMA** ); identifies common data movement bottlenecks;
and develops an end-to-end pipeline across **extract, transform, and load** ( **ETL** ), training,
validation, deployment, and inference.

This chapter covers the following topics:

Storage architectures for AI workloads

High-speed networking

Data movement bottlenecks and optimization

AI data pipeline design

Let's get started!

_Chapter 3_ 26

**Storage architectures for AI workloads**

Storage is more than a place to keep data in AI infrastructure. Large-scale model training, data
preprocessing, and real-time inference place different demands on a storage system, and an
unsuitable design can become a key performance bottleneck. The choice among local SSDs,
shared POSIX storage, and cloud-native object stores affects throughput, latency, cost, and
scalability.

AI models repeatedly read and write large volumes of data, particularly during training and
batch inference. When storage cannot keep pace, GPUs wait for data instead of performing
useful work. As datasets grow beyond memory capacity, models depend more heavily on disk
I/O and the surrounding data pipeline. The storage architecture therefore has a direct effect on
GPU utilization, training time, and inference responsiveness.

**The three storage types**

Three storage types are common in AI infrastructure. Local storage, particularly NVMe SSDs,
provides fast I/O close to the GPU. Shared file systems allow several nodes to access the same
namespace, which is often required for distributed training. Object storage provides scalable,
durable capacity in cloud and on-premises environments, but exposes object APIs rather than
native POSIX file-system semantics. Most production systems combine the three, using local
storage for hot data, shared storage for concurrent access, and object storage for durable
capacity and lifecycle-managed retention.

Local storage provides fast data access because it is attached to the compute node. High-speed
NVMe SSDs can offer low latency **a** nd high **input/output operations per second** ( **IOPS** ),
which makes them suitable for preprocessed dataset shards, temporary training files and
caches, and active checkpoints. Local storage is not natively shared across nodes. In a
distributed environment, data locality therefore requires staging, replication, or an explicit
sharing layer.

Shared storage presents a common file-system namespace to multiple compute nodes and
allows concurrent access to the same data. This capability is important when GPU workers
across a distributed training cluster require coordinated access to datasets, intermediate
results, or checkpoints. NFS provides a general-purpose option, while Lustre and BeeGFS are
parallel file systems designed for high-throughput environments. Under concurrency, the
shared layer can become a bottleneck, so aggregate throughput, metadata operations, request
size, caching, and I/O contention must be measured against the workload.

27 _Storage, Networking, and Data Pipelines for AI_

Object storage is common in cloud environments and is also available on-premises. Services
such as Amazon S3, Google Cloud Storage, and Azure Blob Storage provide scalable capacity
and durability features. Unlike a native POSIX file system, an object store is accessed through
object APIs; mount or gateway layers may add file-like access but do not make the underlying
semantics identical. Object storage is well suited to dataset staging, model artifacts, and
archival. Latency-sensitive training paths normally stage or cache active data closer to the
workers and validate the resulting throughput.

_Figure 3.1_ compares the roles of local, shared, and object storage in an AI platform.

_Figure 3.1: Local, shared, and object storage roles in an AI platform_

The appropriate combination depends on the stage of the AI workload. Model training can use
local NVMe for active shards and caches, with a shared file system for coordinated datasets and
checkpoints. Distributed training often benefits from a parallel shared file system such as
BeeGFS or Lustre when measured aggregate demand justifies it. Production inference can
retain model artifacts in object storage or a model registry while warming a local cache before
serving traffic. For long-term retention, object storage can provide a lower-cost tier when
lifecycle, retrieval, durability, and compliance requirements are accounted for.

_Figure 3.2_ maps storage placement to representative AI workload stages.

_Chapter 3_ 28

_Figure 3.2: Storage placement by AI workload stage_

Tiering brings these storage types together. Frequently accessed hot data can remain on local
NVMe, warm shared datasets can reside on a centralized or parallel file system, and cold data,
including older experiments, can move to lower-cost object storage. Monitor IOPS, latency,
bandwidth, queueing, and application-visible throughput rather than relying on device
specifications alone. Parallel reads, sharding, prefetching, and staging data close to GPU nodes
can help maintain the input rate required by the workload.

**High-speed networking**

In AI infrastructures, moving data quickly is as important as processing it. As model sizes and
dataset volumes grow, conventional network links can restrict distributed training and
inference. Modern AI systems therefore use high-bandwidth interconnects such as NVLink and
InfiniBand, together with RDMA-capable data paths, to improve throughput, scalability, and
GPU communication.

During training, GPUs exchange gradients, weights, and activations. During inference, systems
must retrieve input data at high speed. If communication is slow, GPUs wait and compute
capacity is wasted. Distributed performance therefore depends not only on the capability of
each node, but also on how quickly the nodes exchange data.

NVLink is NVIDIA's high-speed interconnect for GPU-to-GPU communication in supported
systems. The bandwidth is generation- and platform-specific. A100 systems use thirdgeneration NVLink with up to 600 GB/s of aggregate bidirectional bandwidth per GPU, while
H100 systems use fourth-generation NVLink with up to 900 GB/s per GPU ( `[https://](https://www.nvidia.com/en-us/data-center/h100/)`

`[www.nvidia.com/en-us/data-center/h100/](https://www.nvidia.com/en-us/data-center/h100/)` ). These are aggregate product specifications for
supported configurations, not application-level throughput guarantees. NVLink can reduce

29 _Storage, Networking, and Data Pipelines for AI_

transfers through host memory and improve collective communication within a multi-GPU
node.

NVIDIA InfiniBand, originating from Mellanox, is widely used for high-performance cluster
networking. HDR provides up to 200 Gb/s per port, while NDR provides up to 400 Gb/s per
port. InfiniBand supplies an RDMA-capable fabric; MPI and collective communication libraries
can run over that fabric, while GPUDirect RDMA requires supported GPUs, network adapters,
drivers, and topology. Advertised link rates should not be treated as application throughput
without a stated test configuration.

RDMA allows a network adapter to transfer data to or from registered memory with reduced
CPU involvement in the data path. This can reduce latency and CPU overhead for synchronized
workloads. RDMA is native to InfiniBand and is also available over Converged Ethernet
through RoCE. It is particularly important for collective operations such as all-reduce, where
gradients must be exchanged efficiently as distributed training scales.

The interfaces serve different communication scopes. PCIe is the general-purpose I/O
interconnect used to attach GPUs and other devices. NVLink provides higher-bandwidth GPUto-GPU communication within supported systems. InfiniBand provides an RDMA-capable
fabric between nodes in a distributed cluster. A large AI system may therefore combine PCIe
attachment, NVLink inside the node, and InfiniBand or another high-speed network between
nodes. The effective result depends on topology, software, message size, concurrency, and
workload behavior.

_Figure 3.3_ keeps PCIe, NVLink, and InfiniBand bandwidth figures tied to specific versions and
configurations.

_Figure 3.3: Version-specific PCIe, NVLink, and InfiniBand bandwidth_

_Chapter 3_ 30

The NVIDIA GPUDirect technology family can reduce intermediate copies in supported data
paths. GPUDirect RDMA ( `[https://docs.nvidia.com/cuda/gpudirect-rdma/index.html](https://docs.nvidia.com/cuda/gpudirect-rdma/index.html)` )
enables a peer device, such as a supported network adapter, to access GPU memory directly
over PCIe. GPUDirect Storage ( `[https://docs.nvidia.com/gpudirect-storage/overview-](https://docs.nvidia.com/gpudirect-storage/overview-guide/index.html)`

`[guide/index.html](https://docs.nvidia.com/gpudirect-storage/overview-guide/index.html)` ) enables direct DMA transfers between supported storage and GPU
memory, avoiding a bounce buffer in CPU system memory. The CPU still participates in the
control path, and the benefit depends on compatible hardware, drivers, topology, file systems
or object interfaces, and application integration.

High-speed interconnects support distributed training, collective communication, and data
movement for large AI workloads. Their value is workload-dependent: compute-heavy phases
may hide communication, while communication-heavy phases can become network-bound.
Scaling therefore requires profiling collective operations and end-to-end step time rather than
assuming that a higher link rate will translate directly into the same training-speed
improvement.

Network tuning completes the design. NVLink can connect GPUs within supported systems,
while InfiniBand with RDMA can connect nodes. GPUDirect features should be enabled only
where the complete hardware and software stack supports them. MTU, queues, buffers,
interrupt and CPU affinity, congestion control, and transport parameters must be tuned as an
end-to-end configuration; jumbo frames require a consistent MTU across the complete path.

`iperf3` measures TCP or UDP throughput, while RDMA perftest tools such as `ib_write_bw`
measure verbs paths. NVIDIA Fabric Manager manages NVSwitch and NVLink fabrics on
supported systems, and DCGM provides GPU and fabric telemetry. Record topology, versions,
message size, concurrency, and test direction so results can be reproduced.

**Data movement bottlenecks and optimization**

In AI infrastructure, moving data efficiently is as **i** mportant as compute and storage capacity.
Even a fast GPU is ineffective when it repeatedly waits for data. Bottlenecks in I/O, networking,
preprocessing, or memory transfers reduce accelerator utilization and extend end-to-end job
time.

A bottleneck is the stage that limits the throughput or latency of the complete AI pipeline. It
may occur in storage reads, metadata operations, network transfers, preprocessing, data
loading, or host-to-device copies. When the required data rate is not sustained, GPUs can sit
idle, increasing training time and infrastructure cost. Identifying the limiting stage requires
correlated measurements across the pipeline rather than a single utilization percentage.

Bottlenecks can occur in many parts of the pipeline:

   - Slow storage devices, saturated shared file systems, or metadata bottlenecks.

31 _Storage, Networking, and Data Pipelines for AI_

Oversubscribed or congested network paths and inconsistent end-to-end settings.

CPU-bound preprocessing or insufficient parallelism.

Single-process or underprovisioned data loaders.

Remote object storage accessed through small or highly serialized requests.

Every system is different, but most bottlenecks fall into one or more of these categories.

Diagnosis begins with measurement. `iostat` reports block-device and CPU statistics. `iotop`
attributes I/O activity to processes. `nvidia‑smi dmon` samples selected GPU metrics. `DCGM`
exposes device and profiling telemetry for supported data-center GPUs. PyTorch Profiler and
TensorFlow Profiler can separate input, preprocessing, transfer, and compute time. `iperf3`
measures TCP or UDP paths, while RDMA perftest tools measure verbs bandwidth or latency.
Prometheus exporters and Grafana can retain and visualize trends. Low GPU utilization is a
signal to investigate, but it does not identify the limiting stage by itself.

**Optimizing storage, loading, and network**

Storage access can be improved by placing hot data on NVMe SSDs or another tier that meets
the measured read pattern. Prefetching requests data before the training step requires it, while
local caching keeps frequently accessed shards close to the workers. Sharding can allow
parallel reads and can avoid a large number of tiny files, but shard size must be tuned to the
access pattern. Queue depth, request size, readahead, buffer sizes, and the file system or I/O
scheduler should be changed only after a baseline measurement identifies the limiting
behavior.

Data loading can become a bottleneck when work is serialized. In PyTorch, the default

`num_workers=0` loads data in the main process, while any positive `num_workers` value enables
worker processes. The appropriate value depends on CPU capacity, memory, storage, dataset
behavior, and distributed-process count, so it must be measured rather than set universally.
CPU-bound decoding and transformation can be parallelized where safe. NVIDIA DALI
provides optimized CPU, mixed, and GPU operators for supported image, video, and audio
pipelines; it does not move every preprocessing operation to the GPU automatically. Large
Python loops may also be constrained by interpreter overhead or the global interpreter lock
when implemented with threads.

Network bottlenecks are common in distributed AI systems. Moving from 1 or 10 GbE to 25,
100, or faster Ethernet, or to InfiniBand, increases the available link rate, but only when
endpoints, switches, cabling, topology, and software can sustain it. RDMA can reduce datapath CPU overhead for supported registered-memory transfers. Compression and batching
may reduce transfer overhead, but they add compute and buffering trade-offs. MTU, queues,

_Chapter 3_ 32

ring buffers, congestion control, CPU affinity, and transport settings must be validated end to
end under representative load.

Architectural changes can improve the pipeline beyond individual component tuning. Stagewise pipelines allow ingestion, preprocessing, and training to run in parallel threads, services,
or containers. Caching layers such as Redis or local SSDs can sit between object storage and
GPU nodes. Dedicated nodes can handle I/O-intensive work so that training GPUs remain
focused on compute, while distributed file systems such as BeeGFS or Lustre support parallel
access for multi-node workloads.

The objective is a smooth and continuous flow from storage to GPU. A practical bottleneck
review checks whether disk performance matches the dataset, data loaders are parallelized,
caching and prefetching are active, and the network is configured and monitored. The final
question is whether GPUs are processing data or spending time idle. That distinction often
reveals the next bottleneck to address.

**AI data pipeline design**

An AI model depends on the data pipeline that feeds and evaluates it. An AI data pipeline is a
connected sequence of stages that transforms raw data into training inputs, model artifacts,
and predictions. A typical flow moves through ingestion and transformation, training and
validation, deployment, and inference. Every stage operates across storage, compute, and
networking layers. Slow I/O, insufficient network capacity, or poorly utilized accelerators at
any point can limit the complete workflow.

Pipeline design is concerned with performance and resilience as well as function. Each stage
must supply the next with data at the required rate, and the full workflow must remain reliable
and scalable as datasets, models, and request volumes grow.

**The ETL stage**

ETL prepares raw data for downstream use. Extraction reads from object stores such as
Amazon S3 and Google Cloud Storage, SQL and NoSQL databases, or event streams such as
Kafka. Transformation cleans and enriches data, standardizes formats, resizes images,
tokenizes text, and filters records according to defined quality rules. Loading writes prepared
outputs to a tier such as local NVMe, NFS, or a parallel shared file system that the training
workers can access at the required aggregate rate.

Apache Airflow can orchestrate dependencies among batch-oriented stages, Spark can perform
distributed transformations, and Kafka can provide durable event streaming for ingestion.
RAPIDS cuDF accelerates supported tabular DataFrame operations on GPUs, while DALI
accelerates supported data loading and media preprocessing pipelines. The tools must be

33 _Storage, Networking, and Data Pipelines for AI_

selected according to data type, transformation semantics, failure model, deployment
environment, and the required handoff to training.

During training, the pipeline reads from storage and supplies batches to GPU workers. Parallel
data-loader workers, sharding, prefetching, and asynchronous host-to-device transfers can
overlap input work with computation when the framework and data path support it. Formats
such as TFRecord or Parquet may be useful for particular frameworks and data models, but
neither format is automatically GPU-optimized; record size, compression, sharding, and reader
implementation determine effective throughput. DALI can accelerate supported media
pipelines, while cuDF can accelerate supported tabular transformations. PyTorch or
TensorFlow executes the training loop, and checkpoints, logs, metrics, and validation outputs
must be written without blocking the critical path unnecessarily.

_Figure 3.4_ shows how data loading, preprocessing, transfer, and training can overlap in the
model-training path.

_Figure 3.4: Overlapped stages in a model-training data path_

Validation and hyperparameter tuning follow or overlap with training according to the
experiment design. Optuna, Ray Tune, and Weights & Biases Sweeps can automate trials
across batch size, learning rate, model layers, and other parameters. Trials may run
concurrently on separate GPUs or on isolated GPU partitions, so the scheduler must account
for compute, memory, storage, and network demand rather than GPU count alone. Validation
loads held-out data, performs inference, and computes the metrics defined for the model and
task.

A production inference pipeline contains preprocessing, model execution, and postprocessing.
It may operate in batch mode or serve online requests. Triton Inference Server ( `[https://](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html)`

`[docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html)` )
is a model server with configurable scheduling and batching, while TensorRT ( `[https://](https://docs.nvidia.com/deeplearning/tensorrt/latest/getting-started/quick-start-guide.html)`

```
docs.nvidia.com/deeplearning/tensorrt/latest/getting-started/quick-start```

`[guide.html](https://docs.nvidia.com/deeplearning/tensorrt/latest/getting-started/quick-start-guide.html)` ) is an SDK and runtime that builds and executes optimized inference engines for

_Chapter 3_ 34

supported models. TorchServe ( `[https://github.com/pytorch/serve](https://github.com/pytorch/serve)` ) can serve PyTorch
models, but its official repository states that the project is in limited maintenance with no
planned updates or security patches. Batching can improve throughput at the cost of queueing
delay, and a cache such as Redis can reduce repeated computation or data access when cache
semantics are safe for the application.

**A production example**

Consider an illustrative production architecture. Real-time events enter through Kafka, while
Airflow coordinates batch-oriented dependencies and recovery. Supported tabular
transformations use cuDF, and supported media loading or preprocessing uses DALI. Prepared
data is staged on local NVMe and shared through BeeGFS where concurrent workers require it.
GPU workers train the model, and validated artifacts are deployed to Triton Inference Server on
Kubernetes. Autoscaling and GPU allocation may respond to demand, but scaling behavior and
service latency must be verified with the selected model, batching policy, hardware, and
workload.

_Figure 3.5_ brings the ingestion, processing, training, serving, and control layers into one
illustrative architecture.

_Figure 3.5: Example end-to-end AI data architecture_

Optimization and resilience apply across the complete pipeline. Concurrent services can keep
independent stages active, while bounded queues prevent one stage from consuming
unlimited memory. Retries with exponential backoff can address transient failures, but
operations must be idempotent or otherwise protected against duplicate effects. Data and
schema validation, checkpointing, and artifact versioning support recovery and
reproducibility. Monitor stage latency, throughput, queue lag, error rate, and GPU idle time.
Kafka, Redis Streams, or another queue can decouple stages, but retention, delivery, ordering,
and replay semantics must match the workflow.

35 _Storage, Networking, and Data Pipelines for AI_

**Summary**

In this chapter, we explored how local, shared, and object storage support different AI
workload stages and how PCIe, generation-specific NVLink, InfiniBand, RDMA, and GPUDirect
move data within and across GPU nodes. It also showed why advertised link or device rates
must be separated from measured application throughput.

Finally, we followed an AI data pipeline from ingestion and ETL through training, validation,
and inference. Measurement, staging, parallel loading, compatible acceleration, orchestration,
serving, monitoring, and failure recovery work together to keep data flowing without turning
version-specific capabilities into universal guarantees.

**Further reading**

To learn more about the topics that were covered in this chapter, take a look at the following
resources:

NVIDIA HGX A100 datasheet: `[https://www.nvidia.com/content/dam/en-zz/](https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/HGX/pdf/nvidia-hgx-a100-datasheet.pdf)`

```
Solutions/Data-Center/HGX/pdf/nvidia-hgx-a100-datasheet.pdf

```

NVIDIA H100 Tensor Core GPU: `[https://www.nvidia.com/en-us/data-center/h100/](https://www.nvidia.com/en-us/data-center/h100/)`

InfiniBand HDR switch systems: `[https://docs.nvidia.com/qm87xx-1u-hdr-200gb-s-](https://docs.nvidia.com/qm87xx-1u-hdr-200gb-s-infiniband-switch-systems-user-manual.pdf)`

```
infiniband-switch-systems-user-manual.pdf

```

NDR cabling overview: `[https://docs.nvidia.com/dgx-superpod/design-guide-](https://docs.nvidia.com/dgx-superpod/design-guide-cabling-data-centers/latest/ndr-overview.html)`

```
cabling-data-centers/latest/ndr-overview.html

```

GPUDirect RDMA: `[https://docs.nvidia.com/cuda/gpudirect-rdma/index.html](https://docs.nvidia.com/cuda/gpudirect-rdma/index.html)`

GPUDirect Storage: `[https://docs.nvidia.com/gpudirect-storage/overview-](https://docs.nvidia.com/gpudirect-storage/overview-guide/index.html)`

```
guide/index.html

```

# 4
#### AI Cluster Orchestration and Scalability

Running AI workloads at scale is not only a question of adding more GPUs. The cluster also
needs a control plane that can place workloads, isolate resources, recover from failures, and
respond when demand changes. Kubernetes provides that foundation, while Helm, operators,
and autoscaling make the environment easier to deploy and manage.

This chapter follows that progression. We begin with GPU orchestration in Kubernetes, move
into repeatable deployment and elastic cluster management, and then connect Kubernetes
with Slurm, Kubeflow, and MLflow. The final section compares on-premises, cloud-native, and
hybrid cluster topologies and the trade-offs that shape the choice among them.

This chapter covers the following topics:

Kubernetes for GPU-orchestrated AI workloads

Helm, operators, and cluster autoscaling

Integrating Slurm, Kubeflow, and MLflow

Cluster topologies

Let's get started!

**Kubernetes for GPU-orchestrated AI workloads**

Kubernetes is a general-purpose container orchestration platform that can manage GPUaccelerated training, inference, and data-processing workloads when the cluster includes the
required GPU software stack. Kubernetes schedules containers, isolates resources, and
reconciles failed pods, while NVIDIA's device plugin and GPU Operator expose accelerator
resources and automate the supporting components.

_Chapter 4_ 38

For production AI infrastructure, Kubernetes provides a consistent control plane when
workloads already use containers and the operating model fits the platform. Jobs and services
can be defined as YAML manifests, which makes deployments reproducible across
development, staging, and production environments and allows configuration to be versioncontrolled. Kubernetes controllers recreate failed pods or retry Jobs according to configured
policies. Application-level recovery for stateful training still **d** epends on checkpointing and
restart logic.

**Enabling GPU support**

GPU scheduling begins with the NVIDIA device plugin, or with the NVIDIA GPU Operator that
installs and manages it. The plugin allows GPU-enabled nodes to advertise accelerator
resources to the Kubernetes scheduler. A pod then requests a GPU through the `nvidia.com/gpu`
extended resource. Under Kubernetes rules for extended resources, GPUs are specified in limits;
if requests is omitted, Kubernetes uses the limit as the request. Physical GPUs are allocated
exclusively by default. Administrators can expose supported MIG instances or configure timeslicing or MPS, but those sharing modes have different isolation and scheduling semantics.

The GPU request is placed under `resources` and `limits` in the container specification:

```
  resources:

  limits:

  nvidia.com/gpu: 1

```

A GPU workload uses a container image whose framework and CUDA libraries are compatible
with the driver installed on the node. The image does not have to use `nvidia/cuda` as its base
when it already contains a compatible GPU framework runtime. Training data can be mounted
through persistent volumes, and non-sensitive configuration can be supplied through
ConfigMaps. Use `kubectl logs` to inspect container output, and connect the workload to the
cluster's monitoring stack for retained metrics.

Before Kubernetes can schedule a GPU job, deploy the NVIDIA device plugin, or install the GPU
Operator to manage the complete NVIDIA software stack. The device plugin runs as a
DaemonSet on eligible nodes and registers allocatable GPU resources with each node's kubelet.
A default GPU Operator installation can also deploy the driver, NVIDIA Container Toolkit, GPU
Feature Discovery, DCGM Exporter, and MIG Manager. Verify that nvidia.com/gpu appears in
node allocatable resources before submitting workloads.

Kubernetes supports several patterns for training and inference. Replicas in a Deployment are
appropriate for stateless scale-out inference, while Kubernetes Jobs suit finite training tasks.
Current Kubeflow Trainer releases use `TrainJob` with `TrainingRuntime` or

39 _AI Cluster Orchestration and Scalability_

`ClusterTrainingRuntime` resources; older installations may expose framework-specific

`PyTorchJob`, `TFJob`, or `MPIJob` resources. Horovod can be used in an MPI-oriented training
design, but it is not implied by every `PyTorchJob` . For isolation and multi-tenancy, organize
workloads into namespaces and apply resource quotas, RBAC, and scheduling policy.

A stable GPU-aware cluster also needs deliberate placement rules. Label GPU nodes and use

`nodeSelector` to steer jobs to them. Add taints and tolerations so that CPU-only jobs do not
consume GPU nodes, and use node affinity to pin high-priority workloads where required.
These controls keep expensive accelerators available for the jobs that need them.

Finally, monitor GPU nodes with NVIDIA DCGM Exporter. It exposes DCGM metrics at an
HTTP endpoint that Prometheus can scrape, while Grafana can visualize the stored series.
These metrics provide health and workload visibility, but they do not change scheduling by
themselves. GPU-aware autoscaling requires an explicit metric-to-pod mapping and a custom
or external metrics **a** dapter. Kubernetes remains the control plane, while NVIDIA components
supply the device discovery, runtime integration, telemetry, and optional MIG management
required by GPU workloads.

**Helm, operators, and cluster autoscaling**

In this section, we examine three mechanisms with different responsibilities. Helm packages
and releases Kubernetes resources. Operators reconcile domain-specific custom resources.
Autoscaling changes workload replicas, CPU and memory requests, or node capacity according
to configured signals and policy. Used together, they support repeatable deployment and
elastic cluster operation without collapsing those responsibilities into one control loop.

**Helm**

Think of Helm as the `apt` or `pip` of Kubernetes. It packages Kubernetes manifests into reusable
units called **charts** . A chart can install a complete AI stack, including monitoring, inference,
and data tools, with a single command. Configuration can be overridden through

`values.yaml`, which is useful for MLOps workflows where reproducibility and version control
matter.

For example, add NVIDIA's chart repository and install a pinned GPU Operator release:

```
  helm repo add nvidia https://helm.ngc.nvidia.com/nvidia

  helm repo update

  helm install gpu-operator nvidia/gpu-operator \

  --namespace gpu-operator --create-namespace \

  --version v26.3.3 --wait

```

_Chapter 4_ 40

Helm can upgrade a release, roll back to an earlier revision, and work with private chart
repositories. Pin chart versions and store values files with the deployment source so that the
rendered manifests can be reviewed and reproduced. The result is a versioned and auditable
deployment process that scales with the infrastructure.

**Operators**

While Helm renders and installs manifests, an operator continuously reconciles a declared
custom resource with the state of the system. Operators use Kubernetes **Custom Resource**
**Definitions** ( **CRDs** ) and controllers to encode application-specific lifecycle logic. The NVIDIA
GPU Operator, for example, manages the software components that make GPUs available to
Kubernetes and keeps their deployment aligned with a `ClusterPolicy` resource.

Operators automate the lifecycle that their controllers explicitly implement. They can reconcile
configuration, replace failed managed resources, and coordinate controlled updates. Trafficbased scaling still belongs to an autoscaler such as HPA or KEDA, and an object-storage event
requires an eventing or workflow component. Treat the operator as a domain-specific
reconciliation loop, not as a general AI layer for the infrastructure.

**Autoscaling**

Kubernetes uses distinct mechanisms for workload and node scaling. The **Horizontal Pod**
**Autoscaler** ( **HPA** ) changes the replica count of a scalable workload. It reads CPU and memory
through the resource metrics API and can use custom or external metrics when a compatible
adapter exposes them. The **Vertical Pod Autoscaler** ( **VPA** ), which is **i** nstalled separately,
analyzes CPU and memory usage to recommend or update pod requests; it does not derive the
count of GPU extended resources from DCGM telemetry. A node autoscaler adds a compatible
GPU node when a pending pod cannot be scheduled and removes nodes when policy permits.
Together, these mechanisms can align workload replicas, CPU and memory requests, and
cluster capacity with demand.

|Autoscaler|Scaling<br>target|Scaling behavior|Typical trigger|
|---|---|---|---|
|**Horizontal**<br>**Pod**<br>**Autoscaler**<br>**(HPA)**|Pod<br>replicas|Scales horizontally by increasing or<br>decreasing the number of pod replicas<br>within the confgured minimum and<br>maximum limits.|Observed CPU or<br>memory utilization, or<br>custom metrics such as<br>GPU utilization when<br>exposed through a<br>compatible metrics<br>adapter.|

41 _AI Cluster Orchestration and Scalability_

|Autoscaler|Scaling<br>target|Scaling behavior|Typical trigger|
|---|---|---|---|
|**Vertical**<br>**Pod**<br>**Autoscaler**<br>**(VPA)**|Pod<br>resource<br>requests|Scales vertically by recommending or<br>applying updated resource requests<br>for containers. CPU and memory are<br>controlled by default. The number of<br>pod replicas remains unchanged. How<br>recommendations are applied<br>depends on the confgured update<br>mode and may involve creating or<br>replacing pods.|Historical and current<br>resource usage<br>compared with the<br>resources requested by<br>the workload.|
|**Cluster**<br>**Autoscaler**<br>**(CA)**|Cluster<br>nodes|Scales the infrastructure by adding<br>nodes when pods cannot be<br>scheduled because the cluster lacks<br>suffcient resources. It removes nodes<br>that remain underutilized when their<br>workloads can be safely moved<br>elsewhere.|Unschedulable pods<br>requiring additional<br>capacity, or nodes that<br>remain unneeded for a<br>confgured period.|

_Table 4.1: Cluster autoscaling strategies_

These strategies operate at different layers. HPA changes the number of workload replicas, VPA
changes the resources requested by each replica, and Cluster Autoscaler changes the compute
capacity available to the cluster.

GPU autoscaling introduces its own challenges. Long-running training should be checkpointed
and controlled by restartable job logic. A `PodDisruptionBudget` can limit voluntary evictions
for supported controllers, but it does not protect against node failure and is not a substitute for
checkpoints. For GPU-aware HPA behavior, DCGM Exporter exposes a selected metric,
Prometheus stores it, and Prometheus Adapter or another compatible adapter publishes it
through the Kubernetes custom metrics API. Use workload signals such as queue depth,
request rate, latency, or carefully validated GPU utilization; reserve temperature and hardwarehealth metrics primarily for alerting. Taints, tolerations, and workload placement policy can
separate training and inference, while MIG can expose smaller schedulable resources on
supported GPUs.

Together, Helm, operators, and autoscalers cover three different concerns. Helm provides
repeatable packaging and release management. Operators reconcile domain-specific lifecycle

_Chapter 4_ 42

state. Autoscalers change workload replicas, resource requests, or node capacity according to
explicit signals and policy. Keeping those responsibilities separate makes the cluster easier to
reason about and operate.

**Integrating Slurm, Kubeflow, and MLflow**

In modern AI infrastructure, Kubernetes can coexist with schedulers and MLOps services that
address different concerns. Slurm handles high-performance batch scheduling, Kubeflow
provides Kubernetes-native pipeline and training components, and MLflow records
experiment and model metadata. They do not become one platform automatically; a working
design must define how jobs are submitted, how status is returned, where artifacts are stored,
and how identities and permissions cross each boundary.

Each component serves a different operational role. Slurm allocates resources and schedules
jobs in its domain. Kubeflow defines and monitors containerized pipeline or training resources
on Kubernetes. MLflow records runs, artifacts, and registered model versions. A combined
environment can support data scientists, machine learning engineers, and HPC researchers,
but the value comes **f** rom explicit handoffs rather than the tools merely being installed

together.

**The three tools**

Slurm is a high-throughput batch scheduler designed for large clusters. It can coexist with
Kubernetes in separate resource pools, or it can interoperate through SchedMD's Slinky
projects. The Slinky Slurm Operator runs and manages Slurm clusters on Kubernetes, while
Slurm Bridge connects Slurm scheduling with the Kubernetes scheduling API. Volcano is a
Kubernetes-native batch scheduler, and `kube‑batch` was its predecessor; neither is a generic
Slurm integration layer. Slurm remains well suited to tightly coupled multi-node workloads,
including MPI-based training and simulation.

Kubeflow provides Kubernetes-native components for machine learning workflows and
distributed training. A Kubeflow Pipeline is authored with the KFP SDK and compiled to an
intermediate-representation YAML file before it is uploaded or submitted through the API or
UI. Pipeline components execute as containers. Distributed training is handled through
Kubeflow Trainer, with TrainJob in current releases and framework-specific CRDs in legacy v1
installations. GPU requests still flow through the NVIDIA device plugin and the Kubernetes
scheduler.

MLflow provides visibility into the model-development process. Tracking APIs record runs,
including parameters, metrics, datasets, and artifacts, and the UI supports comparison. The
Model Registry stores registered model versions, aliases, tags, and descriptions; a self-hosted
registry requires a database-backed backend store. Current MLflow webhooks can notify

43 _AI Cluster Orchestration and Scalability_

external CI/CD or governance services when registry events occur, but deployment behavior
remains an explicit integration rather than an automatic property of experiment tracking.

Here is how the pieces fit together. Kubeflow defines and monitors the pipeline. Training steps
can follow a Kubernetes-native path through Kubeflow Trainer or an explicit Slurm path
through Slinky or a submission gateway. Code running in either path sends tracking calls to
MLflow and writes artifacts to a shared or API-accessible artifact store. Shared storage alone
does not integrate the systems: identity, credentials, network policy, job status, retry behavior,
and artifact ownership must be defined at each boundary.

_Figure 4.1_ shows the explicit handoffs among Slurm, Kubeflow, and MLflow.

_Figure 4.1: Slurm, Kubeflow, and MLflow integration paths_

The pattern appears **a** cross industries:

A healthcare platform can use Kubeflow to coordinate retraining while MLflow records
model lineage and evaluation evidence.

A financial workflow can run parallel simulation or training jobs through Slurm while
MLflow records the associated experiments.

A university can retain Slurm for HPC research while using Kubernetes and Kubeflow
for containerized machine learning workflows.

A retail platform can use Kubeflow for pipeline execution and MLflow to compare
candidate models before an external deployment system promotes one.

_Chapter 4_ 44

Successful integration depends on explicit operational contracts:

Use shared file storage or an object store with defined paths, ownership, retention, and
consistency expectations for data and artifacts.

Secure service-to-service communication with TLS, scoped credentials, and network
policy.

Use Kubernetes namespaces, RBAC, labels, and quotas for Kubernetes workloads, and
map them deliberately to Slurm accounts, partitions, and quality-of-service policy
where required.

Centralize metrics, logs, and traces where the components expose them, and preserve
job identifiers across Kubeflow, Slurm, and MLflow so an execution can be followed
end to end.

These controls keep the **c** ombined platform observable and manageable as it supports
different workloads and teams.

**Cluster topologies**

Where AI infrastructure runs, whether on-premises, in the cloud, or in a hybrid configuration,
affects cost, performance, security, and scalability. Cluster topology describes the physical and
logical arrangement of compute, storage, and networking resources, together with how those
resources are accessed and managed. In AI infrastructure, that arrangement directly influences
how workloads are scheduled and executed.

For this comparison, we use three broad topology models: on-premises, cloud-native, and
hybrid. Each has strengths and compromises, and real deployments may combine elements of
more than one model. The right choice depends on workload behavior, data requirements, the
operating model, risk, and budget.

**On-premises**

On-premises clusters run in data centers that the organization owns or controls, using NVIDIA
DGX systems or custom GPU nodes. They can use local high-speed fabrics such as NVLink or
NVSwitch within supported systems and InfiniBand or Ethernet between nodes. This topology
provides direct control over hardware, networking, security, and data placement. It can suit
sensitive data, predictable utilization, or workloads that benefit from local data and tightly
engineered network paths, but latency still depends on the complete topology and application.

That control comes with substantial investment in hardware, cooling, power, facilities, and
operations. Capacity expansion follows procurement and deployment timelines. For sustained,
predictable utilization, the resulting unit economics can be competitive, but the outcome

45 _AI Cluster Orchestration and Scalability_

depends on utilization, depreciation, energy, staffing, support, and refresh cycles rather than
topology alone.

**Cloud-native**

Cloud-native GPU clusters provide on-demand access to accelerator-optimized instances and
managed infrastructure, subject to regional availability, service quota, and capacity.
Representative families include AWS P4 for A100 and P5 variants for H100 or H200, Azure NDm
A100 v4 and ND H100 v5, Google Cloud A2 and A3, and OCI GPU shapes, with Blackwell-based
families now offered alongside these by the major providers. Instance naming changes
frequently, so check the provider documentation listed at the end of this chapter rather than
relying on a family name alone.

Cloud platforms can provide elastic provisioning, regional services, and a usage-based
operating model that reduces upfront capital expenditure. They can also simplify collaboration
across locations. The trade-offs include quota and capacity constraints, network and datatransfer cost, provider-specific controls, and a shared-responsibility model for security and
compliance. Data residency and regulated workloads require architecture and policy decisions
rather than a universal cloud or on-premises answer.

**Hybrid**

Hybrid infrastructure combines on-premises and cloud resources. Sensitive or data-intensive
workloads can remain local, while selected jobs use cloud capacity when data movement,
identity, quota, and cost make that practical. Hybrid design can balance control and elasticity,
but it adds operational boundaries. Network capacity, dataset replication, artifact consistency,
identity federation, observability, and failure recovery must be designed across locations.

Multi-cluster management does not make several Kubernetes clusters one scheduler. Rancher
Manager can manage registered clusters, and Rancher Fleet can deliver GitOps bundles across
them. The former KubeFed project was archived and should not be presented as a current
default for new deployments. NVIDIA Fleet Intelligence provides GPU inventory and health
monitoring across enrolled hosts; it is an observability service rather than a Kubernetes
federation layer. Workload placement across sites still requires explicit policy, data access,
identity, and failure handling.

_Figure 4.2_ compares the workload-dependent trade-offs of on-premises, cloud-native, and
hybrid topologies.

_Chapter 4_ 46

_Figure 4.2: Workload-dependent cluster-topology trade-offs_

The comparison shows the operating tendencies of the three models without treating them as
guarantees. On-premises infrastructure offers direct control but expands through procurement
and deployment. Cloud-native infrastructure offers usage-based provisioning and elastic
capacity subject to quota and regional availability. Hybrid infrastructure combines the two and
therefore adds cross-environment identity, data movement, policy, and observability
requirements. Latency, compliance, and cost must be measured or assessed for the specific
design.

Representative NVIDIA components can appear in each topology. DGX SuperPOD reference
architectures describe integrated on-premises AI infrastructure, while containers and models
from the NGC catalog can be used across supported data-center and cloud environments. Edge
inference on Jetson with training performed in a data center or cloud is an illustrative hybrid
pattern, but the data path, model promotion, device management, and rollback process must
be designed explicitly.

Choosing a topology is both a technical and operating-model decision. If data control and local
infrastructure are the priority, on-premises or hybrid infrastructure may fit. If the priority is
rapid provisioning or variable demand, cloud capacity may fit. If the organization trains in one
environment and **d** eploys in another, a hybrid design can provide that flexibility while
increasing integration work. NVIDIA-Certified Systems and provider reference architectures
can inform component selection, but they do not replace workload-specific sizing, security
review, and total-cost analysis.

47 _AI Cluster Orchestration and Scalability_

**Summary**

In this chapter, we explored how Kubernetes schedules and isolates GPU-powered AI
workloads, how autoscalers change replicas or capacity, and how DCGM-based telemetry
supports monitoring. It also showed how Helm and operators provide repeatable deployment
and application-aware reconciliation without taking over the responsibilities of the scheduler
or autoscalers.

Finally, we connected Kubernetes with Slurm, Kubeflow, and MLflow across the AI lifecycle
and compared on-premises, cloud-native, and hybrid cluster topologies according to control,
cost, scalability, latency, and compliance.

**Further reading**

To learn more about the topics that were covered in this chapter, take a look at the following
resources:

NVIDIA GPU Operator: `[https://docs.nvidia.com/datacenter/cloud-native/gpu-](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html)`

```
operator/latest/getting-started.html

```

Kubernetes extended resources: `[https://kubernetes.io/docs/concepts/](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#extended-resources)`

```
configuration/manage-resources-containers/#extended-resources

```

Kubernetes node assignment: `[https://kubernetes.io/docs/concepts/scheduling-](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)`

```
eviction/assign-pod-node/

```

Kubernetes taints and tolerations: `[https://kubernetes.io/docs/concepts/](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/)`

```
scheduling-eviction/taint-and-toleration/

```

NVIDIA device plugin: `[https://github.com/NVIDIA/k8s-device-plugin](https://github.com/NVIDIA/k8s-device-plugin)`

NVIDIA DCGM Exporter: `[https://docs.nvidia.com/datacenter/cloud-native/gpu-](https://docs.nvidia.com/datacenter/cloud-native/gpu-telemetry/latest/dcgm-exporter.html)`

```
telemetry/latest/dcgm-exporter.html

```

Kubernetes HPA: `[https://kubernetes.io/docs/concepts/workloads/autoscaling/](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)`

```
horizontal-pod-autoscale/

```

Kubernetes VPA: `[https://kubernetes.io/docs/concepts/workloads/autoscaling/](https://kubernetes.io/docs/concepts/workloads/autoscaling/vertical-pod-autoscale/)`

```
vertical-pod-autoscale/

```

Kubernetes node autoscaling: `[https://kubernetes.io/docs/concepts/cluster-](https://kubernetes.io/docs/concepts/cluster-administration/node-autoscaling/)`

```
administration/node-autoscaling/

```

Pod disruptions: `[https://kubernetes.io/docs/concepts/workloads/pods/](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/)`

```
disruptions/

```

_Chapter 4_ 48

SchedMD Slinky: `[https://slurm.schedmd.com/slinky.html](https://slurm.schedmd.com/slinky.html)`

Kubeflow Pipelines compilation: `[https://www.kubeflow.org/docs/components/](https://www.kubeflow.org/docs/components/pipelines/user-guides/core-functions/compile-a-pipeline/)`

```
pipelines/user-guides/core-functions/compile-a-pipeline/

```

Kubeflow Trainer: `[https://trainer.kubeflow.org/en/latest/getting-started/](https://trainer.kubeflow.org/en/latest/getting-started/)`

MLflow Tracking: `[https://mlflow.org/docs/latest/ml/tracking/](https://mlflow.org/docs/latest/ml/tracking/)`

MLflow Model Registry: `[https://mlflow.org/docs/latest/ml/model-registry](https://mlflow.org/docs/latest/ml/model-registry)`

AWS accelerated instances: `[https://docs.aws.amazon.com/ec2/latest/](https://docs.aws.amazon.com/ec2/latest/instancetypes/ac.html)`

```
instancetypes/ac.html

```

Azure ND GPU family: `[https://learn.microsoft.com/en-us/azure/virtual-](https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nd-family)`

```
machines/sizes/gpu-accelerated/nd-family

```

Google accelerator-optimized machines: `[https://cloud.google.com/compute/docs/](https://cloud.google.com/compute/docs/accelerator-optimized-machines)`

```
accelerator-optimized-machines

```

OCI compute shapes: `[https://docs.oracle.com/en-us/iaas/Content/Compute/](https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm)`

```
References/computeshapes.htm

```

Archived KubeFed project `[: https://github.com/kubernetes-retired/kubefed](https://:%20https://github.com/kubernetes-retired/kubefed)`

Rancher Fleet: `[https://ranchermanager.docs.rancher.com/integrations-in-](https://ranchermanager.docs.rancher.com/integrations-in-rancher/fleet/)`

```
rancher/fleet/

```

NVIDIA Fleet Intelligence: `[https://docs.nvidia.com/fleet-intelligence/latest/](https://docs.nvidia.com/fleet-intelligence/latest/index.html)`

```
index.html

```

NVIDIA DGX SuperPOD: `[https://docs.nvidia.com/dgx-superpod/index.html](https://docs.nvidia.com/dgx-superpod/index.html)`

NVIDIA NGC catalog: `[https://catalog.ngc.nvidia.com/](https://catalog.ngc.nvidia.com/)`

NVIDIA-Certified Systems: `[https://www.nvidia.com/en-us/data-center/products/](https://www.nvidia.com/en-us/data-center/products/certified-systems/)`

```
certified-systems/

```

# 5
#### Performance Optimization and Monitoring

Performance optimization starts with visibility. Before we optimize a deep learning model or a
large-scale GPU workload, we first need to understand where the resources are being spent.
That means examining compute utilization, memory behavior, kernel execution, data
movement, storage, and networking rather than assuming that raw GPU power will produce
efficient execution.

This chapter begins with GPU profiling and the tools that reveal how workloads behave. It then
moves into continuous metrics, telemetry, and alerting for production environments. From
there, we examine how TensorRT optimizes inference and finish with a systematic approach to
diagnosing and tuning bottlenecks across the AI stack.

This chapter covers the following topics:

Profiling GPU workloads

GPU metrics, telemetry, and alerting tools

TensorRT and model optimization

Bottleneck diagnosis and tuning

Let's get started!

**Profiling GPU workloads**

Before we optimize deep learning models or large-scale GPU workloads, we first need to
understand where the resources are being spent. Profiling is the process of collecting detailed
performance data that helps us diagnose bottlenecks in compute utilization, memory usage,
kernel execution, or data movement.

_Chapter 5_ 50

Three types of tools are important here. NVIDIA Nsight Systems and Nsight Compute provide
system-level and kernel-level analysis. Framework-native profilers, such as PyTorch Profiler,
connect GPU activity to model operators. `nvtop` is a lightweight terminal monitor for rapid
device and process triage. Used together, these tools provide a progression from quick
observation to application traces and detailed kernel analysis.

Profiling matters because raw GPU power alone does not guarantee efficient execution. Many
workloads achieve only a fraction of peak GPU performance because of bottlenecks such as
input data stalls, memory bandwidth saturation, or kernel inefficiencies. Profiling pinpoints
where resources are being wasted. A model may appear slow because the GPU is constantly
waiting for data from the CPU, not because the GPU itself is underpowered. Profiling also
makes benchmarking reproducible, which is essential when comparing optimizations or
hardware platforms. Without it, we are essentially flying blind in performance tuning.

Nsight Systems is NVIDIA's system-wide profiler. It provides a timeline visualization that
shows how the CPU and GPU interact during execution, which makes it extremely valuable for
understanding where synchronization or idle time occurs. We can observe kernel launches,
CUDA stream concurrency, and overlapping data transfers, then determine whether a model is
GPU-bound, CPU-bound, or limited by PCIe or NVLink transfers.

Frequent gaps in GPU utilization, for example, may be caused by CPU preprocessing delays or
insufficient batching. Nsight Systems provides the high-level view needed to confirm the
cause.

Once we identify the performance issue at that level, we can move to Nsight Compute and
examine selected CUDA kernels in more detail. Nsight Compute reports launch configuration,
achieved occupancy, warp stall reasons, instruction and pipeline activity, and memory-system
metrics. Interpret these metrics together. Low occupancy can reduce latency hiding, but higher
occupancy does not automatically produce higher performance. Likewise, low memory
throughput is not proof of a poor access pattern when the kernel is limited by computation,
dependencies, or another resource. The profile should connect each proposed kernel, blocksize, or memory-layout change to a measured bottleneck. Together, Nsight Systems and Nsight
Compute form a measure-then-drill-down workflow.

DLProf appears in older NVIDIA deep learning workflows, but NVIDIA identifies version 1.8.0
as its final release. It produced model-oriented reports and, in earlier releases, supported a
TensorBoard plugin; later releases used the separate DLProf Viewer. For current environments,
use Nsight Systems and Nsight Compute alongside the profiler provided by the active
framework. Retain DLProf only when reproducing a version-matched legacy container or
workflow.

51 _Performance Optimization and Monitoring_

Heavy profiling tools are not always necessary for day-to-day observation. nvtop is a terminalbased GPU and accelerator process monitor. On supported devices it can display utilization,
memory use, temperature, power, and process information in real time. The exact fields
depend on the GPU vendor, driver interfaces, and permissions, so treat it as a fast operational
view rather than a source of kernel-level evidence.

Although nvtop does not provide deep kernel insight, it complements profilers by making idle
devices, memory pressure, and unexpected processes visible quickly. If a job is not using the
GPU as expected, nvtop can establish the symptom before a trace or kernel profile is collected.

**GPU metrics, telemetry, and alerting tools**

Monitoring GPU workloads in real time is essential for keeping AI infrastructure reliable and
efficient. Profiling helps identify bottlenecks during development, while telemetry and metrics
provide continuous visibility into GPU health, utilization, and workload performance in
production. NVIDIA provides tools for quick checks and detailed data center telemetry, while
Prometheus and Grafana provide collection, visualization, and alerting. Together, these tools
form the foundation of robust observability in GPU-powered environments.

**GPU metrics**

GPU metrics are central to performance observability in AI infrastructure. Utilization,
framebuffer memory, power, temperature, clocks, and error events provide different views of
workload and device behavior. Thermal limits are model-specific: `nvidia‑smi` distinguishes
slowdown and maximum operating or shutdown-related temperature fields where the device
exposes them. Do not use 95 degrees Celsius as a universal damage threshold. Alert against the
supported GPU's documented limits and account for sustained duration, ambient conditions,
fan behavior, and clock throttling. Low utilization also needs context because it can indicate
data starvation, synchronization, small batches, intentional burstiness, or a workload that is
not compute-bound.

Certain metrics are more informative only when they are interpreted together. A generic GPUutilization sample reports whether one or more kernels were active during a sampling interval;
it does not by itself quantify tensor-core efficiency or memory-bandwidth saturation. DCGM
profiling fields and Nsight provide more specific SM, tensor, memory, PCIe, or NVLink activity
where the GPU and collection mode support them. Framebuffer usage can expose capacity
pressure, while page-retirement, ECC, and Xid events can indicate device-health concerns.
Power, temperature, clocks, and throttling reasons explain whether the GPU is operating
within its intended envelope.

_Chapter 5_ 52

**Telemetry**

NVIDIA provides a suite of tools for this telemetry. `nvidia‑smi` provides a quick command-line
snapshot and supports repeated or query-based output. DCGM provides monitoring, health
and diagnostics, accounting, and policy notifications for supported data center GPUs. DCGM
Exporter selects DCGM fields and exposes them at a Prometheus metrics endpoint.
Prometheus then stores the scraped time series, while Grafana queries and visualizes them.
This separates point-in-time inspection from continuous collection and alerting.

**Visualization and alerting**

Once metrics are exposed, the next step is collection and visualization. Prometheus scrapes
configured endpoints at regular intervals and stores the resulting time series. With DCGM
Exporter, this supports cluster trends, capacity analysis, and comparison across labeled GPU
workloads. Sampling interval, metric compatibility, and workload labels must be configured
deliberately because not every DCGM profiling field is available or collectable at the same time
on every GPU architecture.

Grafana renders these metrics as dashboards with charts and graphs that are easier to
interpret. We can examine GPU utilization across an entire cluster, monitor job-level
performance, or identify workloads that are causing contention. This turns raw telemetry into
actionable insight.

Metrics are most valuable when they drive action. Alert rules in Prometheus or Grafana can
notify operators when a sustained temperature condition crosses a model-specific threshold,
utilization changes unexpectedly, or ECC and Xid events indicate a health concern.
Prometheus sends firing alerts to Alertmanager, which groups and routes notifications to
receivers such as Slack, email, PagerDuty, or a webhook.

Automation can be built on top of validated alerts, but remediation should be explicit and
guarded. A notification or webhook can invoke a runbook that marks a node unschedulable,
drains restartable workloads, or escalates a hardware fault. Neither DCGM Exporter nor the
Kubernetes device-plugin interface automatically migrates a running GPU workload. Recovery
still depends on orchestration policy, checkpointing, disruption handling, and application
restart behavior.

**TensorRT and model optimization**

When AI models move **i** nto production, performance optimization becomes critical. NVIDIA
TensorRT is an SDK for building optimized inference engines for NVIDIA GPUs. Its value must
be measured against the deployment's latency, throughput, memory, accuracy, and power
targets rather than assumed from the use of the toolkit alone.

53 _Performance Optimization and Monitoring_

At the core of AI infrastructure is the need to make models both capable and efficient.
Acceptable inference latency is application-specific, and throughput, tail latency, concurrency,
batch size, and accuracy can pull the design in different directions. Optimization can reduce
per-request work or increase the amount of useful work completed by the same hardware, but
the result must be demonstrated with a representative workload and a stated measurement
method.

TensorRT is NVIDIA's SDK for optimizing and running inference on supported NVIDIA GPUs. A
common workflow exports a trained model to ONNX and builds a serialized TensorRT engine
for the target environment. Framework integrations provide other routes, such as TorchTensorRT for PyTorch. TensorRT applies graph and kernel optimizations during the build and
produces an engine that is executed by the TensorRT runtime. Operator coverage, dynamic
shapes, precision support, and engine compatibility must be checked against the exact
TensorRT, CUDA, driver, and GPU combination.

The real power of TensorRT lies in its optimization techniques.

Layer and pointwise **f** usion can combine supported operations, reducing intermediate
memory traffic and kernel-launch overhead.

Reduced-precision inference can use formats such as FP16, BF16, FP8, or INT8 when the
model, GPU, and TensorRT release support them. FP16 or BF16 does not use INT8
calibration. Quantized workflows use explicit scales, post-training quantization, or
quantization-aware training, and every precision change requires accuracy validation.

TensorRT plans device-memory use for an engine and can reuse activation memory when
tensor lifetimes permit. During the build, it evaluates supported implementation tactics and
selects choices according to the builder configuration and target environment. Timing caches
can reduce repeated build work, but a cache is tied to relevant device, software, and
configuration details. These optimizations can compound, which is why the engine must be
benchmarked after it is built.

**Deployment and impact**

Optimized models are useful only when they can be served reliably. NVIDIA Triton Inference
Server can load models from a model repository, route requests through per-model schedulers,
batch supported workloads, and run multiple models or model instances on one server.
Triton's local schedulers distribute work among configured model instances; balancing across
multiple Triton pods or nodes belongs to the surrounding deployment platform, such as a
Kubernetes Service, ingress or gateway, and autoscaling policy. TensorRT engines can be
served through Triton's TensorRT backend, while other backends support additional model
formats.

_Chapter 5_ 54

The impact is measurable only for a defined configuration. Report the model and input shapes,
precision, GPU, TensorRT and CUDA versions, batch size, concurrency, warm-up, latency
percentile, throughput, and baseline. Replace universal multipliers with the measured result
from that comparison, and validate accuracy when reduced precision or quantization is used.

These benefits are particularly valuable in latency-sensitive or resource-constrained
deployments. Examples include medical-imaging pipelines, vehicle-perception workloads, and
inference on supported NVIDIA Jetson devices. Each domain has its own safety, accuracy, realtime, and power requirements, so TensorRT optimization is one part of a broader validation
and deployment process.

**Bottleneck diagnosis and tuning**

AI infrastructure, no matter how powerful, is only as strong as its weakest link. Performance
bottlenecks can emerge at any stage of the AI workflow, including CPU-GPU coordination,
memory bandwidth, networking, storage, or poorly tuned software libraries. The ability to
diagnose bottlenecks systematically and apply the right tuning technique is what separates a
stable system from one that crumbles under real workloads.

A performance bottleneck is like a traffic jam on an otherwise clear highway. Even if every
other component is optimized, the slowest component dictates the overall throughput. The
CPU may not deliver data to the GPU quickly enough, or the GPU may be starved for memory
bandwidth. The data pipeline, poorly optimized storage, or preprocessing may throttle the
system instead. The critical insight is that bottlenecks are not isolated. They can emerge
anywhere across the stack, so effective diagnosis requires us to examine the workflow
holistically rather than assume that one component is at fault.

There are a few usual suspects in AI workloads:

CPU-GPU coordination overhead can leave the GPU idle when the CPU takes too long
to queue work.

Insufficient GPU utilization can result from small batches, data-loading stalls, host
synchronization, launch overhead, or kernels that do not expose enough parallel work.

Memory bandwidth can limit kernels whose access patterns generate more traffic than
the memory system can sustain.

55 _Performance Optimization and Monitoring_

On the storage side, large datasets can encounter I/O bottlenecks when the access
pattern and aggregate loader demand exceed the throughput or metadata capacity of
the storage path.

In distributed training, collective communication can become a bottleneck as the GPU
count grows. The effect depends on the model, message sizes, topology, transport, and
the degree of compute-communication overlap.

Diagnosing these bottlenecks requires visibility at each stage. Nsight Systems exposes host,
CUDA, transfer, and GPU timelines; Nsight Compute examines selected kernels; framework
profilers connect operations to model code; and `nvidia‑smi` or DCGM provides sampled device
metrics. Storage tools should measure throughput, queueing, and latency, while network and
NCCL diagnostics should confirm topology, collective behavior, retransmissions, and link
utilization. No single utilization percentage identifies whether the workload is waiting on the
CPU, storage, memory, or network.

**Tuning strategies**

Once a bottleneck is measured, select a tuning change that addresses that cause. Batch size can
alter memory use, latency, and throughput. Mixed precision can improve performance on
supported operations, but it requires numerical validation. Pinned host memory enables
asynchronous host-to-device copies, and CUDA streams can overlap transfers with
computation when the hardware and dependency graph permit it. RDMA and GPUDirect
RDMA can reduce CPU involvement and copies on supported network paths, but page locking
alone is not RDMA. For distributed training, overlap collective communication with
computation only where the framework and dependency graph allow it. At the kernel level, use
profile evidence to tune launch configuration, occupancy, and memory access.

_Figure 5.1_ summarizes a disciplined bottleneck-tuning loop from baseline measurement
through remeasurement.

_Figure 5.1: A disciplined bottleneck-tuning loop_

Consider a distributed-training job whose scaling efficiency falls as more GPUs are added. First
separate computation from communication in the trace, then confirm the physical and logical
network topology, message sizes, and collective operations. If communication is the limiting
stage, NCCL can provide topology-aware collectives across supported PCIe, NVLink, InfiniBand
Verbs, or IP transports. On a correctly configured InfiniBand fabric, GPUDirect RDMA may
further improve the GPU-to-NIC data path.

_Chapter 5_ 56

After changing the collective, transport, topology, or overlap strategy, rerun the same
benchmark and report per-GPU throughput, end-to-end training time, and scaling efficiency. A
claimed speedup is valid only for that model, node and GPU count, fabric, message-size
distribution, software versions, and baseline. The lesson is not that one network change
guarantees a multiplier, but that measurement should identify the limiting path and verify the
result.

**Summary**

In this chapter, we explored how Nsight Systems and Nsight Compute reveal bottlenecks at
application and kernel levels, how framework profilers connect activity to model operators,
and how nvtop supports quick device and process triage. It also treated DLProf as a legacy tool
whose final release should be used only in version-matched environments.

Finally, we examined how TensorRT builds optimized inference engines through graph
transformation, precision choices, memory planning, and tactic selection. It also established a
systematic tuning loop across compute, memory, storage, and networking: measure a
representative baseline, locate the limiting stage, apply a controlled change, and remeasure
performance, accuracy, and reliability.

**Further reading**

To learn more about the topics that were covered in this chapter, take a look at the following
resources:

Nsight Systems user guide: `[https://docs.nvidia.com/nsight-systems/UserGuide/](https://docs.nvidia.com/nsight-systems/UserGuide/index.html)`

```
index.html

```

Nsight Compute Profiling guide: `[https://docs.nvidia.com/nsight-compute/](https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html)`

```
ProfilingGuide/index.html

```

PyTorch Profiler: `[https://docs.pytorch.org/tutorials/recipes/recipes/](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html)`

```
profiler_recipe.html

```

DLProf user guide: `[https://docs.nvidia.com/deeplearning/frameworks/dlprof-](https://docs.nvidia.com/deeplearning/frameworks/dlprof-user-guide/index.html)`

```
user-guide/index.html

```

nvidia-smi documentation: `[https://docs.nvidia.com/deploy/nvidia-smi/](https://docs.nvidia.com/deploy/nvidia-smi/index.html)`

```
index.html

```

DCGM overview: `[https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/](https://docs.nvidia.com/datacenter/dcgm/latest/user-guide/index.html)`

```
index.html

```

57 _Performance Optimization and Monitoring_

DCGM profiling: `[https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/](https://docs.nvidia.com/datacenter/dcgm/latest/dcgm-api/dcgm-api-profiling.html)`

```
dcgm-api-profiling.html

```

DCGM Exporter: `[https://docs.nvidia.com/datacenter/dcgm/latest/reference/](https://docs.nvidia.com/datacenter/dcgm/latest/reference/command-line-reference/dcgm-exporter.html)`

```
command-line-reference/dcgm-exporter.html

```

TensorRT documentation: `[https://docs.nvidia.com/deeplearning/tensorrt/](https://docs.nvidia.com/deeplearning/tensorrt/latest/)`

```
latest/

```

Torch-TensorRT: `[https://docs.pytorch.org/TensorRT/](https://docs.pytorch.org/TensorRT/)`

Triton architecture: `[https://docs.nvidia.com/deeplearning/triton-inference-](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/architecture.html)`

```
server/user-guide/docs/user_guide/architecture.html

```

Triton on Kubernetes: `[https://docs.nvidia.com/deeplearning/triton-inference-](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tutorials/Deployment/Kubernetes/README.html)`

```
server/user-guide/docs/tutorials/Deployment/Kubernetes/README.html

```

CUDA best practices: `[https://docs.nvidia.com/cuda/cuda-c-best-practices-](https://docs.nvidia.com/cuda/cuda-c-best-practices-guide/index.html)`

```
guide/index.html

```

NCCL overview: `[https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html)`

```
overview.html

```

# 6
#### Security, Compliance, and Data Governance

As AI systems scale into production, performance and reliability are only half of the equation.
The other half is security. GPU-powered workloads introduce challenges ranging from multitenant risks and memory exposure to malicious containers, poisoned datasets, and
unauthorized access across data pipelines.

This chapter examines how to secure AI infrastructure at the hardware, software, data, and
cluster levels. It begins with the layers that protect GPU-powered workloads, then moves into
encryption and access control with DPUs and DOCA. From there, it examines RBAC in multitenant AI clusters and finishes with the regulatory requirements that shape data governance
for AI infrastructure.

This chapter covers the following topics:

Securing GPU-powered workloads

Encryption and access control

Role-based access control (RBAC) for AI clusters

Regulatory compliance: GDPR, HIPAA, FedRAMP

Let's get started!

**Securing GPU-powered workloads**

GPU-powered workloads present unique challenges, from multi-tenant risks to data leakage
across pipelines. Securing this infrastructure requires protection at the hardware, software,
and cluster levels to defend against external and internal threats and keep workloads
trustworthy from end to end.

_Chapter 6_ 60

GPU workloads often process sensitive or proprietary data, including medical images, financial
records, and training datasets. Shared accelerators, containerized execution, and distributed
data paths add trust boundaries that must be examined explicitly. A threat model should cover
model artifacts, credentials, host and device memory, storage, network traffic, and controlplane APIs. The resulting controls must protect confidentiality, integrity, and availability
without assuming that one isolation feature secures the entire pipeline.

Multi-tenancy increases the importance of isolation. A vulnerability or misconfiguration in the
driver, runtime, hypervisor, container, or orchestration layer can expose data or enable lateral
movement. Untrusted images, excessive pod privileges, leaked credentials, poisoned datasets,
and adversarial inputs create additional risks. The practical response is defense in depth:
reduce privileges, verify software provenance, isolate workloads and networks, protect data at
each state, and retain evidence through logging and monitoring.

NVIDIA platforms provide several distinct safeguards, but their availability and guarantees
depend on the GPU generation and deployment mode. Secure Boot, signed firmware, and GPU
attestation can establish platform trust on supported systems. MIG partitions supported GPUs
into isolated instances with dedicated compute and memory resources, while vGPU isolation
depends on the supported hypervisor and NVIDIA vGPU stack. Hopper and later supported
confidential-computing configurations can extend protection for data in use to the GPU. ECC
and memory-error containment improve reliability by detecting, correcting, or containing
faults; they are not access-control mechanisms.

_Figure 6.1_ separates platform safeguards by the security or reliability boundary they address.

_Figure 6.1: GPU platform safeguards and their scope_

The software and driver stack is equally critical. Keep GPU drivers, firmware, the NVIDIA
Container Toolkit, Kubernetes components, and workload images within supported release
combinations and apply security updates promptly. The Container Toolkit enables containers
to use NVIDIA devices; it is not a security boundary by itself. NVIDIA signs NVIDIA-published
container images in NGC, and consumers can verify signatures with Cosign or enforce
verification through a compatible admission controller. Vulnerability scan results, SBOMs, and
VEX information can inform risk decisions where NGC publishes them. Runtime monitoring

61 _Security, Compliance, and Data Governance_

can surface suspicious processes or device behavior, but it must be correlated with identity,
container, node, and network telemetry.

**Cluster and data security**

Cluster-level security adds a further defense layer. Kubernetes RBAC authorizes API actions for
users, groups, and service accounts. Namespaces provide an administrative scope, while
NetworkPolicy can restrict pod traffic when the cluster uses a network plugin that enforces it.
PodSecurityPolicy was removed in Kubernetes 1.25; use the built-in Pod Security Admission
controller or a validating admission policy or webhook for more specific constraints. Several
GPU Operator operands require privileged access, host namespaces, host files, devices, and
kernel operations. Restrict access to the Operator namespace to cluster administrators, review
the generated service accounts and RBAC, and deploy only the operands required by the
chosen configuration.

Data security extends beyond isolation. Protect data in transit with an approved protocol and
configuration, such as TLS, IPsec, or MACsec at the appropriate layer. Protect data at rest with
encryption supplied by the storage platform, commonly using an approved AES mode, and
manage keys through a dedicated key-management service rather than application code or
images. For data in use, confidential computing is available only on supported CPU, GPU,
firmware, driver, and virtualization combinations and should be paired with attestation.
BlueField DPUs and DOCA can offload selected network and storage security functions, but the
deployed service and policy configuration determine the actual trust boundary.

The best practices for GPU security mirror general IT security principles, but they must be
adapted to AI infrastructure:

Apply the principle of least privilege so that no user, pod, or job has more access than
necessary.

Scan containers continuously for vulnerabilities.

Correlate GPU telemetry with process, container, identity, and network data.
Unexpected utilization can indicate an unauthorized workload, but utilization alone
does not identify malicious activity.

Map technical and organizational controls to the standards, contracts, and regulatory
programs that apply to the system. FedRAMP, for example, is relevant to in-scope cloud
services used by United States federal agencies rather than to every enterprise GPU
cluster.

Securing GPU-powered workloads therefore requires a multilayered defense strategy, from
hardware protections and container isolation to encryption, monitoring, and compliance
frameworks. As AI adoption grows, so does the attack surface. Applying these techniques
safeguards the infrastructure and supports AI systems that enterprises can trust.

_Chapter 6_ 62

**Encryption and access control**

Encryption and access **c** ontrol are foundations of data security in AI infrastructure. As GPUpowered clusters scale across data centers, clouds, and edge locations, protect sensitive data at
each relevant state and authorize every management and service interaction. BlueField DPUs
and DOCA can extend selected network and storage controls into the infrastructure data path.
They do not replace the identity, key-management, policy, or audit systems that define who is
trusted and how the control is operated.

AI workloads may process regulated or high-value data, from medical images and patient
records to financial transactions and government information. The applicable obligation
follows the organization, processing activity, data, and deployment, not the presence of a GPU.
Encryption can reduce exposure during storage or transfer, while authorization limits which
identities and services may perform defined actions. Together with retention, logging, incident
response, and governance, these controls support the trust boundaries required by the
applicable framework.

Encryption applies at several layers. At rest, the storage service can encrypt datasets and
artifacts with an approved algorithm and key-management design. In transit, TLS 1.3, IPsec, or
MACsec can protect different network layers when endpoints and infrastructure support the
chosen configuration. For data in use, supported NVIDIA confidential-computing deployments
combine CPU trusted execution, GPU confidential-computing mode, protected CPU-to-GPU
communication, and attestation. This is a platform capability, not a general claim that every
GPU buffer is encrypted in every deployment. Homomorphic encryption supports computation
over encrypted values for selected workloads, but its functionality and cost must be evaluated
for the specific operation.

Access control determines which identities can perform actions. Kubernetes RBAC authorizes
requests to the Kubernetes API for authenticated users, groups, and service accounts. It does
not evaluate arbitrary pod fields or provide general time-based or workload-based
authorization. Context-sensitive rules require a suitable identity, admission, or external policy
system. ResourceQuota can cap aggregate requests for extended resources such as

`nvidia.com/gpu` within a namespace, while admission policy can validate which workloads
may request them. OIDC, an authenticating proxy, or a webhook can connect Kubernetes
authentication to enterprise identity systems; LDAP or Active Directory is not integrated
directly by RBAC.

**DPUs and the DOCA framework**

A **data processing unit** ( **DPU** ) combines programmable processing with network interfaces
and hardware **a** ccelerators for infrastructure tasks. NVIDIA BlueField can run software on its

63 _Security, Compliance, and Data Governance_

Arm cores and offload supported networking, storage, and security operations to hardware.
Examples include packet steering, virtual switching, IPsec, and kernel TLS data-path
acceleration. These capabilities can separate infrastructure services from the host workload,
but they become security controls only when the platform mode, software, keys, rules, and
management interfaces are configured for the intended threat model.

NVIDIA DOCA is a software framework for BlueField networking platforms. It includes host
drivers and tools, SDK libraries and APIs, reference applications and services, and BlueField
platform software. Developers and operators can use these components to build or deploy
networking, security, storage, and telemetry functions. The DOCA IPsec and TLS guides
describe specific offload paths, prerequisites, and limitations. Throughput and latency depend
on the BlueField generation, link, protocol, packet sizes, software release, and configuration, so
terms such as line speed should be supported by measurements for the target system.

_Figure 6.2_ shows the roles of DOCA and BlueField across the control plane and accelerated data
path.

_Figure 6.2: DOCA and BlueField in the infrastructure data path_

BlueField and DOCA can accelerate supported cryptographic data paths and reduce host CPU
work. Key management is not automatic: for example, an IPsec deployment may use an IKE
implementation such as strongSwan, while TLS offload depends on the host's kernel TLS and
certificate and key configuration. The DPU processes the offloaded flow according to that
control plane. Some infrastructure offloads are transparent to the AI application, but
application-level TLS termination or custom DOCA services can require architectural or code
changes. Validate the complete key lifecycle, failure behavior, and observability rather than
treating the DPU as a general-purpose secret store.

_Chapter 6_ 64

Beyond encryption, BlueField can enforce configured network segmentation, virtual-switch,
and traffic-steering policies and can expose infrastructure telemetry. Enterprise IAM does not
automatically program these rules. An orchestrator or policy system must translate approved
identities and workload intent into the relevant network configuration. This distinction
matters for east-west traffic: the DPU can enforce the resulting data-path rules, while
authentication, authorization, rule lifecycle, and audit evidence remain control-plane
responsibilities.

Follow best practices for encryption and access control:

Use approved encryption for data in transit and at rest, with documented algorithms,
endpoints, keys, rotation, and recovery procedures.

Connect Kubernetes authentication to enterprise identity, bind groups to leastprivilege roles, and use workload identities for service-to-service access.

Where the threat model and platform support justify it, use BlueField and DOCA to
offload selected security functions and enforce configured network policies.

Regular compliance audits and vulnerability scans are also necessary to maintain trust
as the infrastructure scales.

Encryption and access control form part of a secure AI infrastructure, but no single product
creates a zero-trust environment. Traditional controls, Kubernetes authorization and
admission, enterprise identity, and configured BlueField or DOCA services can work together
across on-premises, cloud, and edge deployments. The trust boundaries and responsibilities
must be **d** ocumented for each environment.

**Role-based access control (RBAC) for AI clusters**

When multiple teams share the same AI infrastructure, security is not only about encrypting
data. It is also about controlling which identities can perform each action. Kubernetes **role-**
**based access control** ( **RBAC** ) authorizes API requests according to roles assigned to users,
groups, and service accounts. In multi-tenant GPU clusters, RBAC is one layer alongside
admission policy, quotas, scheduling controls, workload identity, and the authorization
systems used by storage, registries, and pipeline services.

65 _Security, Compliance, and Data Governance_

Data scientists, machine learning engineers, platform teams, and compliance personnel may
share the same cluster. Over-broad permissions can expose secrets, allow privileged
workloads, or grant control over another team's resources. RBAC supports least privilege and
produces authorization rules that can be reviewed and audited. It scales through reusable roles
and group bindings, but it must be designed carefully because permission to create pods can
indirectly expose service accounts, secrets, nodes, and host resources.

**RBAC components and GPU-specific controls**

Kubernetes RBAC has four core components:

Roles define allowed API verbs on `namespaced` resources within one namespace.

`RoleBindings` grant a Role or `ClusterRole` to users, groups, or service accounts within
the binding's namespace.

`ClusterRoles` define reusable permissions for `namespaced` resources, cluster-scoped
resources, or non-resource URLs.

`ClusterRoleBindings` grant a `ClusterRole` across the cluster to users, groups, or
service accounts.

This structure separates the permission set from the identities that receive it. Use a

`RoleBinding` when access should remain within one namespace, even when the binding
references a `ClusterRole` . Use a `ClusterRoleBinding` only when the same access is intended
across the cluster.

In a GPU-powered cluster, RBAC controls whether an identity may create or modify pods, Jobs,
quotas, secrets, and related Kubernetes objects. It does not authorize the `nvidia.com/gpu` field
independently from the rest of a pod specification. Use `ResourceQuota` to cap

`requests.nvidia.com/gpu` per namespace and use admission policy when only selected
identities or workload classes may request GPUs. The scheduler and NVIDIA device plugin then
allocate an available device. Access to object storage, a model registry, or an external pipeline
service is enforced by that system's credentials and roles, although a shared identity provider
or workload identity can align the policies.

_Figure 6.3_ traces authorization from enterprise identity through Kubernetes controls to GPU
allocation.

_Chapter 6_ 66

_Figure 6.3: Authorization path for a GPU workload_

Roles should reflect the functions of real users:

A data scientist may be permitted to create training Jobs and read approved Kubernetes
resources. Dataset access must also be granted by the storage system or its Kubernetes
integration.

A machine learning engineer may deploy models and manage pipeline resources
without permission to alter cluster-wide networking, admission, or operator
configuration.

A platform or DevOps engineer may monitor cluster health and manage approved
infrastructure components without automatically receiving access to application
datasets or model secrets.

A compliance officer may receive read-only access to approved audit evidence without
permission to modify workloads or retrieve unrelated secrets.

Clear functional roles reduce risk and align access with operational responsibilities.

**Enterprise integration and practice**

RBAC becomes more manageable when Kubernetes authentication is connected to an
enterprise identity provider. Kubernetes supports OIDC and JWT authentication directly;
LDAP, SAML, Kerberos, and similar protocols require an authenticating proxy, webhook, or
another integration. The authenticator supplies usernames and group strings, and

`RoleBindings` or `ClusterRoleBindings` grant permissions to those groups. Offboarding can
then remove access at the identity source, subject to token lifetime and cache behavior. Each

67 _Security, Compliance, and Data Governance_

cluster still retains its own bindings and must be governed consistently across hybrid or multicloud deployments.

To make RBAC effective, follow a few best practices:

Grant the smallest set of API verbs and resources required, and avoid wildcard
permissions where practical.

Use namespaces as an administrative boundary, then combine RBAC with
NetworkPolicy, quotas, Pod Security Admission, and workload identity. A namespace
alone does not isolate network traffic or GPU memory.

Apply ResourceQuota to aggregate GPU requests and use LimitRange for supported
per-container CPU and memory defaults or bounds. Protect those policy objects from
unauthorized modification.

Audit role and binding changes, test effective permissions, and remove unused serviceaccount tokens and grants.

Permissions should evolve with project needs, not accumulate unchecked. These measures
maintain security while keeping GPU resources well governed.

RBAC is not without challenges. At scale, dozens of roles and bindings increase complexity.
Consistent management becomes even harder across hybrid or multi-cloud deployments.
Over-permissioning creates security risk, while under-permissioning creates friction. RBAC
also requires cultural alignment. Teams must agree on responsibilities, boundaries, and
accountability, or the system becomes ineffective.

Within a zero-trust design, RBAC authorizes Kubernetes API requests, admission controls
validate workload specifications, and network or DPU controls enforce configured traffic
policy. These systems do not share policy automatically. Their identities, rules, and logs must
be connected deliberately to provide workload isolation and useful audit evidence.

RBAC is not merely a Kubernetes security checkbox. It is one part of governance for AI clusters.
Align roles with responsibilities, integrate authentication with enterprise identity, constrain
GPU consumption with quotas and admission policy, and keep external data and model
systems within the same access-review process.

**Regulatory compliance: GDPR, HIPAA, FedRAMP**

AI infrastructure operates within legal, contractual, and assurance frameworks that depend on
the organization, data, users, and deployment. GDPR, HIPAA, and FedRAMP address different
scopes: personal-data processing, electronic protected health information, and cloud services
used within United States federal agency systems. They should not be treated as
interchangeable certifications for a GPU cluster.

_Chapter 6_ 68

Compliance requires more than protecting sensitive data. It also includes governance,
documented responsibilities, risk decisions, individual rights, authorized uses, retention,
evidence, and incident response. The applicable obligations must be determined before
controls are mapped to the AI system. Penalties, authorization consequences, and contractual
exposure vary by framework and circumstance, so current official guidance and qualified legal
or compliance advice should be used for a production deployment.

**The three frameworks**

The **General Data Protection Regulation** ( **GDPR** ) governs processing of personal data within
its territorial scope. It is not based simply on European Union citizenship: it covers processing
in the context of an EU establishment and can apply to organizations outside the EU when
they offer goods or services to, or monitor the behavior of, people in the EU. Processing
requires a lawful basis; consent is one possible basis, not a universal requirement. GDPR also
establishes principles such as purpose limitation and data minimization and rights including
access, rectification, and erasure subject to the regulation's conditions. For certain
infringements, the higher maximum tier is up to EUR 20 million or 4 percent of total
worldwide annual turnover for the preceding financial year, whichever is higher.

The **Health Insurance Portability and Accountability Act** ( **HIPAA** ) rules apply to covered
entities and business associates as defined by United States law. The rule protects **electronic**
**protected health information** ( **ePHI** ) through administrative, physical, and technical
safeguards, including access control and audit controls. Encryption at rest and in transmission
is an addressable implementation specification, not an unconditional mandate. A regulated
entity must implement it when reasonable and appropriate after risk assessment, or document
the decision and use an appropriate alternative when the rule permits. AI models and pipelines
that create, receive, maintain, or transmit ePHI must remain within that risk-management and
documentation process.

The **Federal Risk and Authorization Management Program** ( **FedRAMP** ) provides a
standardized, reusable approach to security assessment and certification for cloud service
offerings used by federal agencies. Current FedRAMP guidance distinguishes the cloud service
offering's certification evidence from the agency's authorization of its own information
system. An agency authorizing official accepts the risk for the specific use, configuration,
integrations, information, and agency-operated controls. An in-scope cloud GPU service must
therefore use the certified service boundary and participate in the required ongoing
monitoring, vulnerability, change, and incident processes. A GPU cluster is not automatically
in scope merely because it runs in a public cloud.

69 _Security, Compliance, and Data Governance_

**Compliance in AI infrastructure**

AI workloads introduce distinct compliance challenges. Datasets are massive and often
sensitive, covering healthcare records, financial data, or government information. Moving data
across regions for cloud training or inference introduces jurisdictional risk. Multi-tenant GPU
clusters can create cross-tenant leakage if isolation is not enforced. Models may also memorize
personal information, which means compliance is not limited to the infrastructure. It extends
to model design and deployment.

Organizations use technical and organizational controls to meet the requirements that apply.
Encryption protects selected data states, while supported confidential-computing
configurations can reduce exposure for data in use. Kubernetes RBAC and workload identities
control API and service access; network and DPU policies can enforce configured traffic rules.
Masking, pseudonymization, tokenization, or de-identification can reduce exposure, but each
technique has limits and must be evaluated against the governing definition and reidentification risk. Logs, audit trails, tests, risk records, and incident reports provide evidence
that controls were designed and operated as intended.

Each framework has a different scope and vocabulary. A GDPR implementation may require
lawful-basis records, privacy notices, retention rules, and workflows for data-subject rights. A
HIPAA-regulated pipeline needs safeguards and evidence appropriate to ePHI, including access
and audit controls and a documented encryption decision. A FedRAMP-certified cloud service
offering and the agency system that uses it have defined shared responsibilities, continuousmonitoring activities, and incident and vulnerability reporting. These are representative
mappings rather than a universal control checklist.

_Figure 6.4_ maps regulatory scope to representative infrastructure controls and evidence.

_Figure 6.4: Mapping from regulatory scope to infrastructure evidence_

_Chapter 6_ 70

The best approach is to embed compliance from the start. Adding controls retroactively is
inefficient and error-prone. The infrastructure should undergo regular audits, and policies
must evolve as regulations change. Compliance is also a human challenge. Training teams on
security and data handling is as important as configuring the cluster.

NVIDIA NGC and NVIDIA AI Enterprise can contribute software supply-chain evidence and
lifecycle support. NVIDIA documents signed container images, vulnerability scan results,
SBOM and VEX artifacts for applicable content, and a Government Ready designation for
selected container versions intended for FedRAMP High or equivalent sovereign use cases.
These capabilities can support a regulated deployment, but they do not make the surrounding
AI system GDPR-compliant, HIPAA-compliant, or FedRAMP-certified. The organization
remains responsible for applicability, architecture, configuration, inherited and customeroperated controls, and continuing evidence.

Compliance is a continuing governance process. As AI systems handle more sensitive data,
teams must keep data inventories, access rules, risk assessments, technical configurations,
evidence, and incident procedures aligned with the current system and current official
requirements. Embedding those responsibilities into architecture and operations is more
reliable than adding them after deployment.

**Summary**

In this chapter, we examined the layered controls used to secure GPU-powered workloads,
including platform trust, supported GPU isolation and confidential-computing features,
signed-image verification, cluster policy, encryption, and configured BlueField and DOCA
services. It distinguished reliability features such as ECC from security controls and separated
Kubernetes authorization from admission, quotas, scheduling, and external-system access.

Finally, we explained how Kubernetes RBAC aligns API permissions with operational roles and
how GDPR, HIPAA, and FedRAMP create different obligations for data, systems, and evidence.
The central lesson is to define the applicable scope and threat model first, then connect
identities, technical controls, operational processes, and audit evidence across the full AI
infrastructure.

**Further reading**

To learn more about the topics that were covered in this chapter, take a look at the following
resources:

NVIDIA MIG User Guide: `[https://docs.nvidia.com/datacenter/tesla/mig-user-](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/latest/index.html)`

```
guide/latest/index.html

```

NVIDIA Trusted Computing: `[https://docs.nvidia.com/nvtrust/index.html](https://docs.nvidia.com/nvtrust/index.html)`

71 _Security, Compliance, and Data Governance_

NVIDIA vGPU documentation: `[https://docs.nvidia.com/vgpu/latest/index.html](https://docs.nvidia.com/vgpu/latest/index.html)`

NVIDIA GPU memory error management: `[https://docs.nvidia.com/deploy/a100-](https://docs.nvidia.com/deploy/a100-gpu-mem-error-mgmt/latest/index.html)`

```
gpu-mem-error-mgmt/latest/index.html

```

NGC signed container images: `[https://docs.nvidia.com/ngc/latest/ngc-catalog-](https://docs.nvidia.com/ngc/latest/ngc-catalog-user-guide.html#nvidia-signed-container-images-in-ngc-catalog)`

```
user-guide.html#nvidia-signed-container-images-in-ngc-catalog

```

NGC container security policy: `[https://docs.nvidia.com/ngc/latest/ngc-catalog-](https://docs.nvidia.com/ngc/latest/ngc-catalog-user-guide.html#ngc-container-security-policy)`

```
user-guide.html#ngc-container-security-policy

```

Kubernetes Pod Security Admission: `[https://kubernetes.io/docs/concepts/](https://kubernetes.io/docs/concepts/security/pod-security-admission/)`

```
security/pod-security-admission/

```

Kubernetes NetworkPolicy: `[https://kubernetes.io/docs/concepts/services-](https://kubernetes.io/docs/concepts/services-networking/network-policies/)`

```
networking/network-policies/

```

Kubernetes admission controllers: `[https://kubernetes.io/docs/reference/access-](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/)`

```
authn-authz/admission-controllers/

```

GPU Operator security: `[https://docs.nvidia.com/datacenter/cloud-native/gpu-](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/security.html)`

```
operator/latest/security.html

```

NIST AES standard: `[https://csrc.nist.gov/pubs/fips/197/final](https://csrc.nist.gov/pubs/fips/197/final)`

TLS 1.3: `[https://www.rfc-editor.org/rfc/rfc8446](https://www.rfc-editor.org/rfc/rfc8446)`

Kubernetes RBAC: `[https://kubernetes.io/docs/reference/access-authn-authz/](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)`

```
rbac/

```

Kubernetes authentication: `[https://kubernetes.io/docs/reference/access-authn-](https://kubernetes.io/docs/reference/access-authn-authz/authentication/)`

```
authz/authentication/

```

Kubernetes ResourceQuota: `[https://kubernetes.io/docs/concepts/policy/](https://kubernetes.io/docs/concepts/policy/resource-quotas/)`

```
resource-quotas/

```

Kubernetes ValidatingAdmissionPolicy: `[https://kubernetes.io/docs/reference/](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/)`

```
access-authn-authz/validating-admission-policy/

```

DOCA Framework: `[https://docs.nvidia.com/doca/sdk/doca-framework/](https://docs.nvidia.com/doca/sdk/doca-framework/)`

DOCA IPsec Security Gateway: `[https://docs.nvidia.com/doca/sdk/doca-ipsec-](https://docs.nvidia.com/doca/sdk/doca-ipsec-security-gateway-application-guide/)`

```
security-gateway-application-guide/

```

DOCA TLS offload: `[https://docs.nvidia.com/doca/sdk/doca-tls-offload-guide/](https://docs.nvidia.com/doca/sdk/doca-tls-offload-guide/)`

BlueField Secure Boot: `[https://docs.nvidia.com/networking/display/](https://docs.nvidia.com/networking/display/bluefieldbsp4140/secure-boot)`

```
bluefieldbsp4140/secure-boot

```

_Chapter 6_ 72

EU GDPR: `[https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng)`

EU GDPR business guidance: `[https://europa.eu/youreurope/business/](https://europa.eu/youreurope/business/governance-and-sustainability/digital-and-data-compliance/data-protection-gdpr/index_en.htm)`

```
governance-and-sustainability/digital-and-data-compliance/data
protection-gdpr/index_en.htm

```

HHS HIPAA Security Rule: `[https://www.hhs.gov/hipaa/for-professionals/](https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html)`

```
security/laws-regulations/index.html

```

HHS HIPAA encryption guidance: `[https://www.hhs.gov/hipaa/for-professionals/](https://www.hhs.gov/hipaa/for-professionals/faq/2001/is-the-use-of-encryption-mandatory-in-the-security-rule/index.html)`

```
faq/2001/is-the-use-of-encryption-mandatory-in-the-security-rule/

index.html

```

FedRAMP agency use: `[https://www.fedramp.gov/2026/agencies/use/](https://www.fedramp.gov/2026/agencies/use/)`

FedRAMP continuous monitoring: `[https://www.fedramp.gov/resources/documents/](https://www.fedramp.gov/resources/documents/Continuous_Monitoring_Playbook.pdf)`

```
Continuous_Monitoring_Playbook.pdf

```

NVIDIA AI Enterprise security: `[https://docs.nvidia.com/ai-enterprise/planning-](https://docs.nvidia.com/ai-enterprise/planning-resource/ai-enterprise-security-white-paper/latest/index.html)`

```
resource/ai-enterprise-security-white-paper/latest/index.html

```

NVIDIA Government Ready containers: `[https://docs.nvidia.com/ai-enterprise/](https://docs.nvidia.com/ai-enterprise/lifecycle/latest/government-ready.html)`

```
lifecycle/latest/government-ready.html

```

NGC signed container images: `[https://docs.nvidia.com/ngc/latest/ngc-catalog-](https://docs.nvidia.com/ngc/latest/ngc-catalog-user-guide.html#nvidia-signed-container-images-in-ngc-catalog)`

```
user-guide.html#nvidia-signed-container-images-in-ngc-catalog

```

# 7
#### Edge AI Infrastructure and Integration

Edge AI brings inference closer to the systems that generate and act on data. This changes the
infrastructure decisions around latency, bandwidth, security, scalability, and hardware. It also
creates a distributed operating model in which compact edge devices work together with
centralized cloud resources.

This chapter compares edge AI and cloud AI from an infrastructure perspective. It then
examines NVIDIA Jetson and Orin platforms, federated learning and distributed inference, and
the ways these technologies support smart cities, retail, and industrial IoT. Together, these
areas show how edge and cloud resources combine in modern hybrid AI systems.

This chapter covers the following topics:

Edge vs cloud AI: Infrastructure implications

NVIDIA Jetson and Orin for edge AI

Federated learning and distributed inference

Use cases: Smart cities, retail, industrial IoT

Let's get started!

**Edge vs cloud AI: Infrastructure implications**

The infrastructure choice between edge AI and cloud AI is shaped by practical trade-offs.
Latency, bandwidth, security, scalability, and hardware architecture all influence where an AI
workload should run. These considerations are especially important in healthcare, retail,
manufacturing, and smart cities, where systems must often respond quickly while handling
sensitive or high-volume data.

_Chapter 7_ 74

**Latency, bandwidth, and security**

One of the most important considerations is latency. When the complete inference path runs
locally, edge AI removes the wide-area network round trip from the immediate decision path.
This is important for time-sensitive tasks such as robotics and autonomous systems, where the
available response budget may be too small or too variable for a remote dependency. Cloud
inference sends requests across a network, so latency and availability also depend on
connectivity, routing, service capacity, and the application architecture.

Bandwidth matters for the same reason. Continuous streams from IoT sensors or cameras can
consume substantial network capacity if every frame or reading is sent upstream. Edge
processing can retain or discard raw data according to policy and send selected events,
aggregates, metadata, or approved samples to centralized services. The cloud can then perform
fleet-level analysis without requiring every raw stream to traverse the network continuously.

Security and governance can also influence placement. Local processing can keep selected
sensitive data, such as patient images or transaction records, within an on-site trust boundary.
That choice may reduce data movement, but it does not make the edge secure by itself. Devices
still require physical protection, identity, patching, encryption, access control, monitoring, and
a defined retention policy. Centralized cloud services create a different concentration of data
and control, with security properties determined by the service boundary and configuration.
The GDPR does not require edge processing, and the HIPAA Rules do not prescribe it. GDPR
data-minimization and security principles, and the HIPAA Security Rule's safeguards for
electronic protected health information, can nevertheless inform a design that limits
unnecessary collection, transfer, and exposure.

Many organizations use edge AI to support a data-minimization approach in which only
necessary results flow to centralized systems. Aggregated or de-identified information may
reduce exposure, but those terms must not be treated as automatic properties of edge
processing. De-identification requires an appropriate method and validation, and metadata
can still contain sensitive information. The edge is therefore not only a performance decision.
It can also be one component of a wider security and governance architecture.

**Scalability and hybrid strategies**

Cloud AI can provide elastic access to larger pools of compute, storage, and managed services.
The practical scale and provisioning time depend on the provider, region or zone, account
quota, instance availability, reservations, network topology, and workload architecture. Edge
environments operate under tighter local constraints, including CPU and GPU capacity,
memory, storage, thermal design, and power. NVIDIA Jetson modules address these
constraints with integrated accelerators and configurable power modes for edge inference, but
the achievable performance remains model- and configuration-specific.

75 _Edge AI Infrastructure and Integration_

At scale, an edge deployment is not simply one device. It may involve fleets distributed across
cities, factories, hospitals, or retail chains. Orchestrating these devices introduces a different
set of operational challenges because updates, monitoring, security policies, and lifecycle
management must remain consistent across many locations.

In practice, many deployments use a hybrid AI strategy. The edge handles latency-sensitive
inference and the local actions that must continue through a network interruption. Centralized
systems provide model development, fleet-level analytics, coordination, artifact management,
and controlled updates. Smart-city cameras, for example, can perform detection and filtering
locally, then send selected event metadata to a central service for wider analysis and planning.
Whether any raw footage is retained or transferred is a separate policy and architecture
decision.

Centralized training or evaluation can produce a new model candidate. That artifact should
pass validation, versioning, compatibility checks, staged rollout, monitoring, and rollback
gates before it reaches the device fleet. This closes the loop between local inference and
centralized learning without assuming that every update is deployed directly or
simultaneously.

_Figure 7.1_ shows the closed loop between local edge processing and centralized training and
fleet operations.

_Figure 7.1: Hybrid edge-to-cloud AI workflow_

To summarize, edge AI can improve responsiveness and reduce upstream data transfer, while
centralized infrastructure contributes elastic capacity, storage, fleet-wide analysis, and model
lifecycle services. Security and governance depend on the controls in each environment rather
than on placement alone. The infrastructure decision is therefore not binary. Both
environments can form a modern hybrid AI system.

_Chapter 7_ 76

**NVIDIA Jetson and Orin for edge AI**

NVIDIA Jetson is a **f** amily of embedded computing modules and developer kits, while Orin
identifies one Jetson system-on-chip generation. Jetson Orin modules bring GPU acceleration
and other dedicated engines into compact, power-configurable systems designed for edge AI
and robotics. This makes them suitable for workloads that must process sensor data and
produce decisions close to the source.

Jetson modules are compact computers that run AI inference and sensor-processing workloads
locally. JetPack provides Jetson Linux, drivers, accelerated libraries, tools, and samples. CUDA,
cuDNN, and TensorRT preserve important parts of the NVIDIA development stack across datacenter and edge platforms, but deployment is not a zero-change transfer. Teams must select a
JetPack release supported by the target module, rebuild or validate hardware-specific artifacts
such as TensorRT engines, and test performance, memory use, power, and device interfaces on
the final system. Jetson Nano and Jetson Xavier NX belong to earlier generations and use older
supported JetPack branches, while the current Jetson Orin family includes Orin Nano, Orin NX,
and AGX Orin modules.

Jetson Orin is based on the NVIDIA Ampere GPU architecture and spans multiple performance,
memory, and power tiers. It can run workloads such as real-time computer vision, robotics
pipelines, and appropriately sized transformer models, but model fit and latency depend on
precision, memory, power mode, software release, and optimization. Performance per watt is
especially important because an edge design must stay within the device's electrical and
thermal envelope while meeting its response targets.

These platforms are used wherever real-time decision-making is critical. In robotics, they
provide the compute foundation for autonomous navigation, perception, and decisionmaking. In smart cities, they power video analytics for traffic monitoring and public safety.
Retailers use them for shelf monitoring and automated checkout, while industrial IoT systems
use them for predictive maintenance and defect detection at the point of manufacture.

**Software ecosystem and scaling**

NVIDIA JetPack provides the operating-system image, board support, drivers, accelerated
libraries, tools, samples, and documentation used on Jetson. TensorRT builds and runs
optimized inference engines on supported NVIDIA GPUs, while DeepStream supplies
components for streaming video-analytics pipelines. At the time of publication, NVIDIA lists
JetPack 7.2 for the Jetson Orin family with Jetson Linux 39.2, CUDA 13.2.1, cuDNN 9.20.0,
TensorRT 10.16.2, and DeepStream 9.1. These versions form a tested release combination rather
than independent packages that can be mixed freely. Jetson also supports containerized
applications and cloud-native deployment patterns. Kubernetes or another orchestration layer

77 _Edge AI Infrastructure and Integration_

can participate in fleet operations where the target distribution, device integration, and
operational design support it; orchestration is not supplied by TensorRT or DeepStream
themselves.

_Figure 7.2_ places the Jetson hardware, JetPack software, application, and fleet-management
layers in context.

_Figure 7.2: Jetson software and fleet-management layers_

Performance and intended use vary across the product family. Within the Orin generation,
Orin Nano targets entry-class edge AI, Orin NX provides more compute in the small-module
form factor, and AGX Orin addresses the most demanding embedded workloads in the family.
Earlier Jetson Nano and Xavier modules remain relevant to installed systems but require their
supported software branches. Enterprise scalability comes from more than one device's peak
throughput. Fleet services must maintain inventory, device identity, health telemetry,
compatible artifacts, staged updates, and rollback across every managed location.

Jetson Orin can participate in hybrid edge-to-cloud infrastructure. Local inference reduces
dependence on a remote service for time-sensitive decisions, while centralized systems can
provide training, fleet-wide analytics, model registries, monitoring, and update coordination.
An approved model version reaches devices through a controlled rollout that verifies
compatibility, observes deployment health, and retains a rollback path. This keeps the edge
current without giving up the local autonomy required by the application.

_Chapter 7_ 78

Together, Jetson Orin hardware, JetPack, and accelerated libraries provide a foundation for
robotics, industrial systems, retail environments, and smart-city applications. Fleet identity,
orchestration, software **d** elivery, and operational governance remain separate layers that must
be integrated with the device platform.

**Federated learning and distributed inference**

Federated learning and distributed inference address different parts of distributed AI.
Federated learning coordinates training across sites while leaving the participating datasets
under local control. Distributed inference spreads serving capacity across replicas, or it
partitions model execution across multiple devices. They can appear in the same edge-tocloud architecture, but neither requires the other, and neither guarantees privacy, resilience, or
low latency without additional controls.

Federated learning begins with local training. Each participating site trains on its own data
and sends a permitted model update to a coordinator. The coordinator aggregates updates into
a global model rather than collecting the underlying datasets. Raw training records can remain
at the source, which changes the data-sharing boundary, but model updates and the resulting
model can still reveal information. Authentication, authorization, secure transport, update
validation, aggregation policy, and privacy mechanisms such as secure aggregation or
differential privacy must be selected for the threat model.

This approach is useful when several organizations or locations need to collaborate without
pooling their source datasets, including healthcare and financial settings. A global model can
learn from data held at multiple sites, although model quality depends on the training
algorithm, participant data, update policy, and evaluation design. A site can also use an
approved personalization strategy when the shared model must account for local conditions.

_Figure 7.3_ shows how federated sites exchange model updates without centralizing their raw
training data.

_Figure 7.3: Federated training workflow_

79 _Edge AI Infrastructure and Integration_

Distributed inference addresses a different constraint. Replica-based serving sends
independent requests to model instances on multiple GPUs or nodes to increase capacity and
availability. Model-parallel serving partitions one model or execution graph when it cannot
run efficiently on one device. Either pattern can improve throughput, and model partitioning
may make a larger model deployable, but communication, synchronization, batching, and
routing overhead can increase latency. The result must be measured with the target model,
request pattern, network, and hardware.

When these methods are used in the same system, the training lifecycle and the serving
lifecycle remain distinct. Participating sites produce model updates for controlled aggregation,
and an evaluated global model enters a separate registry and deployment process. During
serving, requests may be routed across independent replicas or processed by a backend that
partitions execution across devices. Connecting the lifecycles requires artifact versioning,
compatibility checks, deployment policy, monitoring, and rollback.

_Figure 7.4_ separates request routing across replicas from a model-partitioned execution path.

_Figure 7.4: Distributed inference workflow_

NVIDIA FLARE is the current open-source framework for federated-learning and other
federated-computing workflows. Clara Train documentation remains available as an archived,
healthcare-specific predecessor and should not be treated as the current general federatedlearning platform. For serving, Triton Inference Server manages models, requests, batching,
and model instances on a server. Multiple Triton replicas require an external routing and
orchestration layer. TensorRT can optimize and execute supported model engines, while NCCL
provides collective and point-to-point GPU communication primitives when a backend or
framework explicitly uses them. None of these components independently creates a multinode serving architecture.

These techniques can support collaboration across several industries. Healthcare institutions
can train across approved local datasets, and financial organizations can coordinate selected

_Chapter 7_ 80

fraud-detection workflows without pooling source transaction records. These architectures
still require legal agreements, governance, identity, privacy controls, update validation, and
evaluation for each participant. Smart-city or telecommunications systems can scale inference
across sites or serving nodes, but the useful topology depends on latency targets, data
placement, connectivity, and failure behavior.

Federated learning keeps participating source datasets local while sharing permitted training
artifacts; it does not make those artifacts risk-free. Distributed inference increases serving
capacity or spans a model across devices, but it requires an explicit routing or partitioning
design. Used together, the two patterns can connect **d** ecentralized training with a separately

governed deployment and serving lifecycle.

**Use cases: Smart cities, retail, industrial IoT**

Smart cities, retail, and **i** ndustrial IoT show how edge AI infrastructure operates in real
production environments. Each domain has different goals, but all three depend on low
latency, security, scale, and consistent performance. They also show why edge and distributed
AI are most effective when the infrastructure is designed around the operational setting.

Smart cities use edge AI for traffic management, public safety, and urban planning. Large
camera fleets can generate continuous video streams, and transferring every stream to a
central service can be costly or unnecessary. Running approved models near the cameras
allows the system to identify defined events in real time and send selected metadata or alerts.
Raw footage may still be retained or transferred for an authorized purpose, so privacy,
retention, accuracy, access, and human-oversight requirements must be designed separately.

In retail, edge AI can support customer-facing and operational workloads. Local inference can
reduce response time for smart-checkout, shelf-monitoring, and in-store analytics. The same
architecture can limit continuous upstream video transfer, although payment processing,
fraud detection, recommendations, and customer analytics often depend on additional
centralized services and governance controls.

Industrial IoT applies edge AI to productivity, quality, safety, and energy use. Sensors and local
models can identify conditions associated with equipment failure, detect defined anomalies, or
inspect products near the manufacturing line. Robots and collaborative robots use local
perception and control paths to meet response requirements. The claimed savings, defect
reduction, or energy improvement must be measured against the specific equipment, process,
model, and operating conditions.

**The NVIDIA ecosystem and business impact**

NVIDIA's ecosystem supports these deployments at several layers. Metropolis Microservices
and DeepStream provide components and reference workflows for vision AI in spaces such as

81 _Edge AI Infrastructure and Integration_

roadways, retail environments, logistics sites, hospitals, and factories. Clara Guardian is a
healthcare-specific smart-sensor framework and collection, not a retail platform. Jetson Orin
supplies embedded compute for local applications, while Triton can serve models on an edge
or centralized node when a managed serving layer is appropriate. Scaling across nodes or
locations still depends on external networking, routing, orchestration, and fleet-management
systems.

The business impact appears in different forms. Traffic operators and public-safety teams can
use approved event data to coordinate a response, subject to policy and oversight. Retailers can
use timely inventory and checkout signals to improve operations. Industrial organizations can
reduce avoidable downtime or defects when a validated model detects useful conditions early
enough for an operational response. More selective data movement and right-sized local
compute can also reduce network and centralized processing demand, although overall cost
and energy outcomes require end-to-end measurement.

These use cases show how edge AI infrastructure translates into real-world outcomes. Traffic
management, customer experience, predictive maintenance, and energy optimization all
depend on the same underlying capability: processing data close to where it is created, then
connecting local **i** ntelligence with centralized systems for coordination, learning, and scale.

**Summary**

In this chapter, we compared the infrastructure implications of edge and cloud AI, including
latency, bandwidth, security, scalability, operations, and hardware constraints. It also
examined the Jetson platform and the Orin generation, including the need to treat the module,
firmware, JetPack release, optimized artifacts, and fleet controls as one deployment
combination.

We then separated federated learning from distributed inference: one coordinates training
across local data owners, while the other scales or partitions model serving. Finally, it showed
how smart cities, retail, and industrial IoT combine local processing with centralized analytics,
model lifecycle services, and governance to support production AI systems.

**Further reading**

To learn more about the topics that were covered in this chapter, take a look at the following
resources:

   - Azure VM quotas and capacity: `[https://learn.microsoft.com/en-us/azure/](https://learn.microsoft.com/en-us/azure/virtual-machines/quotas)`

```
    virtual-machines/quotas

```

_Chapter 7_ 82

AWS capacity reservations: `[https://docs.aws.amazon.com/AWSEC2/latest/](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html)`

```
UserGuide/ec2-capacity-reservations.html

```

NVIDIA Jetson modules: `[https://developer.nvidia.com/embedded/jetson-modules](https://developer.nvidia.com/embedded/jetson-modules)`

NVIDIA DeepStream 9.1: `[https://docs.nvidia.com/metropolis/deepstream/dev-](https://docs.nvidia.com/metropolis/deepstream/dev-guide/text/DS_Overview.html)`

```
guide/text/DS_Overview.html

```

Cloud-Native on Jetson: `[https://developer.nvidia.com/embedded/jetson-cloud-](https://developer.nvidia.com/embedded/jetson-cloud-native)`

```
native

```

NVIDIA Jetson Orin: `[https://www.nvidia.com/en-us/autonomous-machines/](https://www.nvidia.com/en-us/autonomous-machines/embedded-systems/jetson-orin/)`

```
embedded-systems/jetson-orin/

```

Jetson Platform Services: `[https://developer.nvidia.com/embedded/jetpack/](https://developer.nvidia.com/embedded/jetpack/jetson-platform-services-get-started)`

```
jetson-platform-services-get-started

```

NIST federated-learning privacy attacks: `[https://www.nist.gov/blogs/](https://www.nist.gov/blogs/cybersecurity-insights/privacy-attacks-federated-learning)`

```
cybersecurity-insights/privacy-attacks-federated-learning

```

NVIDIA FLARE privacy controls: `[https://nvflare.readthedocs.io/en/main/](https://nvflare.readthedocs.io/en/main/user_guide/admin_guide/security/differential_privacy.html)`

```
user_guide/admin_guide/security/differential_privacy.html

```

Triton concurrent execution: `[https://docs.nvidia.com/deeplearning/triton-](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_execution.html)`

```
inference-server/user-guide/docs/user_guide/model_execution.html

```

NCCL overview: `[https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/overview.html)`

```
overview.html

```

NVIDIA FLARE overview: `[https://nvflare.readthedocs.io/en/main/](https://nvflare.readthedocs.io/en/main/flare_overview.html)`

```
flare_overview.html

```

Metropolis microservices: `[https://docs.nvidia.com/mms/text/](https://docs.nvidia.com/mms/text/MDX_Introduction.html)`

```
MDX_Introduction.html

```

Clara Guardian: `[https://developer.nvidia.com/clara-guardian](https://developer.nvidia.com/clara-guardian)`

# 8
#### NGC, Triton Inference Server, and Deployment

Moving an AI model from development into production requires more than a trained model.
The deployment stack also needs optimized assets, a consistent serving platform, and an
architecture that can remain reliable as traffic grows. NVIDIA NGC and Triton Inference Server
address these different parts of the deployment path.

This chapter begins with the containers, pretrained models, SDKs, and deployment resources
available through NGC. It then examines Triton's architecture and multi-framework serving
model, followed by ensembles that combine several model stages behind one endpoint. The
final section moves from a single server to load-balanced, highly available inference across
clusters, regions, and edge environments.

This chapter covers the following topics:

Using NGC Catalog for pretrained models

Triton Inference Server

Model ensemble and multi-framework serving

Serving at scale

Let's get started!

**Using NGC Catalog for pretrained models**

NVIDIA NGC Catalog ( `[https://docs.nvidia.com/ngc/latest/ngc-catalog-user-](https://docs.nvidia.com/ngc/latest/ngc-catalog-user-guide.html)`

`[guide.html](https://docs.nvidia.com/ngc/latest/ngc-catalog-user-guide.html)` ) is a curated catalog of GPU-optimized software for AI, high-performance
computing, and visualization. It includes containers, pretrained models, Helm charts, and

_Chapter 8_ 84

industry-specific SDKs published by NVIDIA and third parties. Each asset page supplies the
metadata and documentation needed to decide how that asset fits into an AI workflow.

Prebuilt NGC containers package frameworks and supporting libraries in a tested container
image, reducing environment assembly work. The container still has host-driver and platform
requirements that must be checked against its release notes. NGC also provides models,
resources, SDKs, and Helm charts, but the contents, support policy, and intended deployment
path vary by asset and publisher.

The catalog groups several types of resources:

Framework containers include NVIDIA-published TensorFlow and PyTorch images
with documented software versions and platform requirements.

Pretrained models cover domains such as computer vision, natural language
processing, speech, and recommendation. Some assets include scripts or notebooks for
evaluation, training, or fine-tuning, but these resources are asset-specific.

Helm charts and deployment resources package selected applications for Kubernetes.
Their values, prerequisites, and lifecycle must be checked on the individual asset page.

Together, these asset types provide a common catalog for selecting and integrating NVIDIAaccelerated software.

Starting from a suitable pretrained model can reduce the data, compute, and iteration required
to reach a useful baseline. Benchmark results, optimization claims, release cadence, security
information, and support status are not universal properties of every NGC asset. They must be
read from the selected asset's publisher, version history, release type, documentation, and
available scan or signature information.

Pretrained models are especially useful for transfer learning. An image model such as
ResNet-50 can be fine-tuned for another image-classification domain, including medical
images or retail products, when the **d** ata and validation plan support that use. Speech
transcription requires an appropriate speech model rather than ResNet-50. The pretrained
checkpoint provides a starting point, while domain data and evaluation determine whether
the adapted model is suitable.

**Accessing the catalog**

The public NGC Catalog can **b** e browsed without an account, and some public models and
resources support guest downloads. Authenticated content and command-line access require
an NVIDIA account connected to an NGC organization. A personal or service API key can then
be scoped to the required NGC services. Access requirements therefore depend on the asset and
operation rather than on catalog browsing alone.

85 _NGC, Triton Inference Server, and Deployment_

NGC assets can be discovered through the web catalog and accessed through the method
documented for that asset. Containers are commonly pulled from `nvcr.io` with Docker or a
compatible container client. Models and resources can be downloaded through the web
interface, NGC CLI, or documented `wget` or `curl` flow, with authentication when the asset
requires it. Pin a version or tag instead of relying on an unqualified latest asset.

For a container, copy the fully qualified image and tag from the asset page. An example
command shape is:

```
  docker pull nvcr.io/<namespace>/<repository>:<tag>

```

_Figure 8.1_ shows the controls that carry an NGC asset from selection through Triton
deployment.

_Figure 8.1: From NGC asset selection to Triton deployment_

Consider a conceptual image-classification workflow built around a suitable ResNet-50 asset:

1.

2.

3.

4.

Search NGC Catalog for a ResNet-50 asset whose framework, publisher, license,
version, and documentation fit the target workflow.

Download the selected model version and use the documented, version-matched
container or environment.

Run the publisher's baseline evaluation or inference flow to validate the asset and
environment before customization.

Fine-tune the model with domain data when the asset and workflow support it, then
evaluate the adapted model against the deployment requirements.

_Chapter 8_ 86

5.

6.

Export a format supported by the selected Triton backend, such as ONNX or a
TensorRT engine. Build and validate hardware- and software-sensitive artifacts against
the target environment.

Place the validated artifact and configuration in a Triton model repository and test the
production serving path.

This workflow connects catalog discovery to a controlled serving deployment. The useful
outcome is not merely downloading an asset. It is preserving the selected publisher, version,
dependencies, validation evidence, and serving configuration through the full path.

A few practices help keep this workflow stable. Pin model and container versions, record the
publisher and release information, and validate host-driver, CUDA, framework, TensorRT, and
hardware requirements as applicable. Use scripted access methods when a team must
reproduce the same artifact set. Review new versions and security information, but promote
them only after compatibility and regression testing.

NGC brings cataloged containers, models, SDKs, and deployment resources into one discovery
and distribution path. Once an asset has been selected and validated, Triton Inference Server
can provide the serving layer for supported model formats and backends.

**Triton Inference Server**

NVIDIA Triton Inference Server is open-source inference-serving software for deploying
models through installed backends such as TensorRT, PyTorch, ONNX Runtime, TensorFlow,
and Python. It exposes a consistent serving interface across these backends, subject to each
backend's supported model format, version, and execution target.

A Triton server can load models handled by different installed backends and can execute
supported models on CPU or GPU according to model configuration and backend capability.
This consolidates the serving interface without making framework artifacts or backend
requirements interchangeable.

One of Triton's most valuable features is concurrent model execution. Triton can create
multiple execution instances of a model and run different models or instances concurrently on
the same system when resources allow. Its dynamic batcher can combine compatible requests
for a stateless model to improve throughput, with queueing and latency trade-offs that must
be measured. These capabilities operate within a Triton server. Scaling across independent
servers or nodes requires external orchestration and request routing, unless a specific backend
implements distributed model execution.

87 _NGC, Triton Inference Server, and Deployment_

**Architecture**

At the heart is the model repository. It uses a defined directory layout containing model
directories, numbered version directories, backend-specific artifacts, and a `config.pbtxt` file
when configuration is required. Triton can read repositories from locally accessible storage and
supported cloud object stores, and more than one repository can be specified at server startup.

Inference backends execute the model artifacts they support. Incoming HTTP/REST, gRPC, or C
API requests are routed to the appropriate per-model scheduler. Depending on the model
configuration, Triton uses the default scheduler, dynamic batcher, sequence batcher, or
ensemble scheduler, then dispatches work to the configured model instances through the
backend. This per-model design is important because batching, instance count, device
placement, and sequence **b** ehavior can differ between models on the same server.

_Figure 8.2_ shows Triton's client, scheduler, backend, model-instance, and repository layers.

_Figure 8.2: Triton Inference Server architecture_

Deployment can begin with a standalone server on bare metal or a virtual machine, and
NVIDIA publishes Triton containers through NGC. Kubernetes can run replicated Triton
servers through manifests and deployment tooling, while NVIDIA's current documentation
provides workload-specific Kubernetes guides. NVIDIA also documents a separate Triton build
for Jetson and JetPack with platform-specific limitations. The exact container tag, backend set,
Kubernetes components, and Jetson release must therefore be selected for the target platform
rather than treated as one universal installation.

_Chapter 8_ 88

Consider an image-classification model exported from PyTorch to ONNX. The deployment
sequence is:

1.

2.

3.

4.

5.

Export the model to ONNX.

Place the ONNX model in the Triton model repository.

Create `config.pbtxt` when required, ensuring that model name, platform or backend,
input and output names, data types, dimensions, batching, and instance settings
match the exported model and selected backend.

Start Triton with the model repository mounted or otherwise accessible through a
supported repository location.

Verify server readiness and model metadata, then send inference requests whose tensor
names, data types, and shapes match the model configuration.

A minimal ONNX model repository uses the following layout. The model and tensor details
must come from the exported artifact:

```
  model_repository/

  resnet50/

  config.pbtxt

  1/

  model.onnx

```

Set the shell variable `TRITON_RELEASE` to the release number from the selected NGC Triton tag,
omitting the `‑py3` suffix. A Linux host with the NVIDIA Container Toolkit can then launch the
repository as follows:

```
  docker run --gpus=1 --rm \

  -p 8000:8000 -p 8001:8001 -p 8002:8002 \

  -v ${PWD}/model_repository:/models \

  nvcr.io/nvidia/tritonserver:${TRITON_RELEASE}-py3 \

  tritonserver --model-repository=/models

```

The readiness and model-metadata endpoints verify that the server is available and the named
model is known before an inference client is introduced:

```
  curl -f http://localhost:8000/v2/health/ready

  curl -f http://localhost:8000/v2/models/resnet50

```

89 _NGC, Triton Inference Server, and Deployment_

The actual inference request remains model-specific. Its input names, data types, dimensions,
and output contract must match `config.pbtxt` and the exported model rather than a generic
ResNet-50 example.

This standardized path gives development and operations teams a repeatable repository and
serving contract. It does not remove model-specific configuration. An executable inference
client cannot be made generic because the request schema must match the exported model.

The use cases span several industries. Triton can serve speech-recognition models,
recommendation models, perception models, and diagnostic-imaging models when their
backends, latency targets, throughput requirements, and validation obligations are supported
by the deployment. The serving architecture still has to be tested against the model and
request pattern rather than inferred from the industry label.

Triton provides a unified, multi-backend serving layer with dynamic batching, configurable
model instances, per-model scheduling, metrics, and standard inference protocols. A
production deployment **c** ombines these server capabilities with repository governance, traffic
management, observability, and infrastructure orchestration.

**Model ensemble and multi-framework serving**

Triton can serve not only individual models but also complete pipelines, even when their
stages come from different frameworks. A model ensemble is a workflow composed of multiple
models chained together so that the output of one stage becomes the input of the next. Triton
performs this chaining internally rather than requiring an external application to stitch the
stages together.

The ensemble is defined by a configuration file that specifies the sequence of models and the
flow of data between them. From the client perspective, the full pipeline appears as a single
model endpoint. This removes the need to call each model through a separate external API and
reduces the overhead of coordinating several serving systems.

Several advantages follow from this design:

Preprocessing, primary inference, and post-processing can be combined into one endto-end workflow.

Intermediate tensors remain within the ensemble execution path, avoiding separate
client-visible service calls between stages. This can reduce network calls and data

_Chapter 8_ 90

movement, although the actual latency depends on the models, backends, memory
transfers, batching, and hardware.

Client integration becomes simpler because the pipeline exposes one ensemble
endpoint. Operators must still version, configure, load, observe, and validate every
constituent model and the ensemble definition.

Versioning the constituent models and ensemble configuration together improves
reproducibility and makes the same pipeline easier to validate across environments.

Multi-framework support extends the same idea across heterogeneous model stacks. For
example, a supported preprocessing backend can feed a TensorRT inference model and a
supported post-processing backend within one ensemble. Tensor names, data types, shapes,
and memory behavior must remain compatible between steps. The client interacts with the
unified ensemble endpoint while each stage retains its own backend and model configuration.

**Ensemble architecture**

All constituent models and the ensemble definition are stored in the model repository. The
ensemble configuration maps named input and output tensors between steps. When a request
arrives, the ensemble scheduler follows those dependencies and invokes the configured
models through their own schedulers and backends. Independent branches can run when their
inputs are ready, so an ensemble is a dependency graph rather than necessarily one serial
chain. The full workflow is exposed as one model through Triton's standard APIs.

_Figure 8.3_ shows how one ensemble endpoint coordinates preprocessing, inference, and postprocessing models.

_Figure 8.3: Three-stage Triton ensemble_

91 _NGC, Triton Inference Server, and Deployment_

Consider **a** n image-classification service with three deterministic inference stages:

The first stage decodes, resizes, and normalizes the input according to the primary
model's contract. Training-time data augmentation is excluded unless a deliberate,
validated inference design requires it.

The second stage is the primary inference model, such as ResNet-50 optimized with
TensorRT.

The third stage converts raw model output into human-readable class labels or
confidence scores.

Triton defines the three models as one ensemble, so a client submits one image and receives
the final output through a single request.

The same pattern applies to more complex workloads. A speech pipeline may combine audio
preprocessing, automatic speech recognition, and intent detection. An imaging pipeline may
prepare an image before detection or classification. Recommendation systems may combine
embedding, ranking, and reranking stages. In each case, the ensemble is appropriate only
when the tensor contracts, backend support, performance, and failure behavior have been
validated end to end.

Model ensembles and multi-framework serving place a heterogeneous inference workflow
behind one client-facing model. This reduces external coordination while preserving modelspecific backends and configuration inside the repository.

**Serving at scale**

When production demand or failure tolerance exceeds one server's capacity, the serving layer
needs multiple independently recoverable replicas, a routing layer, and a defined modeldistribution process. A single server can otherwise become both a capacity limit and a point of
failure.

The required scale and redundancy come from measured request volume, latency objectives,
model resource use, recovery objectives, and the service-level target. High-availability patterns
reduce the impact of failures but do not guarantee zero downtime. A 99.9% annual availability
target still permits about 8 hours and 46 minutes of unavailability in a 365-day year, and the
achieved result depends on the complete dependency and failure model.

**Load balancing and high availability**

Load balancing distributes inference requests across ready Triton replicas. A proxy or client
may use policies such as round robin, least requests, or another implementation-specific
algorithm. Kubernetes Services route traffic to ready endpoints, but they do not route requests
according to current GPU utilization or memory use. Kubernetes GPU scheduling allocates

_Chapter 8_ 92

declared GPU resources to pods, while request routing is a separate layer. Envoy, NGINX, a
cloud load balancer, or gRPC client-side balancing can participate in that layer when
configured for the protocol and failure behavior of the service.

High availability addresses server, node, zone, and dependency failures. Active-active replicas
can share traffic, while an active-passive design directs traffic to a standby only after failover.
Kubernetes startup and readiness probes keep a replica out of service until it can accept traffic,
and liveness probes can restart a failed container. Replica spreading and disruption budgets
reduce selected risks, but disruption budgets govern voluntary evictions and do not guarantee
availability during node or zone failures.

_Figure 8.4_ shows how routing, health checks, replicas, metrics, and autoscaling support a
highly available Triton deployment.

_Figure 8.4: Highly available Triton deployment and autoscaling path_

Kubernetes can manage Triton replicas, recovery, placement, and service endpoints. HPA can
change replica count from CPU or memory resource metrics and from configured custom or
external metrics. Triton exposes Prometheus-format request and GPU metrics, but HPA cannot
consume them directly. A working path requires Prometheus scraping and aggregation, a

93 _NGC, Triton Inference Server, and Deployment_

metrics adapter that publishes the selected signal through the Kubernetes custom-metrics API,
and an HPA specification that targets that published metric. Request latency normally requires
a derived metric rather than a raw counter. GPU Operator manages the GPU software stack on
nodes, but it does not create this autoscaling path automatically.

Scaling can extend beyond one cluster. Hybrid and multi-region designs place independently
operable serving stacks across sites or regions. Cloudflare Load Balancing can steer traffic
across pools. AWS Application Load Balancer distributes traffic within a region, while Route 53
or AWS Global Accelerator can provide global entry and health-based routing. Such placement
can support data-residency, recovery, or latency objectives, but it does not provide regulatory
compliance by itself.

Successful scaling requires discipline. Redundancy and failover must be tied to explicit failure
scenarios. Observability should cover infrastructure, serving behavior, model behavior, and
dependencies. Autoscaling should use a tested signal, account for model-loading and warm-up
time, and avoid removing capacity faster than the workload can recover. Controlled resilience
testing, service-level objectives, and recovery objectives provide evidence that the design
behaves as intended.

Load balancing and high availability surround Triton rather than emerging from one server
setting. Triton can run on GPUs, clusters, regions, and edge platforms, but reliable service
depends on model **d** istribution, orchestration, health checks, telemetry, capacity policy, traffic
management, and tested failure handling.

**Summary**

In this chapter, we examined NGC catalog assets and Triton's model repositories, per-model
schedulers, backends, configurable instances, and standard APIs.

We also covered ensembles and the traffic, metrics, autoscaling, model-distribution,
redundancy, and failover patterns needed for reliable serving at scale.

**Further reading**

To learn more about the topics that were covered in this chapter, take a look at the following
resources:

NGC user and API-key guide: `[https://docs.nvidia.com/ngc/latest/ngc-user-](https://docs.nvidia.com/ngc/latest/ngc-user-guide.html)`

```
guide.html

```

Triton overview: `[https://docs.nvidia.com/deeplearning/triton-inference-](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/index.html)`

```
server/user-guide/docs/index.html

```

_Chapter 8_ 94

Triton batching: `[https://docs.nvidia.com/deeplearning/triton-inference-](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/batcher.html)`

```
server/user-guide/docs/user_guide/batcher.html

```

Triton concurrent execution: `[https://docs.nvidia.com/deeplearning/triton-](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_execution.html)`

```
inference-server/user-guide/docs/user_guide/model_execution.html

```

Triton model configuration: `[https://docs.nvidia.com/deeplearning/triton-](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_configuration.html)`

```
inference-server/user-guide/docs/user_guide/model_configuration.html

```

Triton model repository: `[https://docs.nvidia.com/deeplearning/triton-](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/model_repository.html)`

```
inference-server/user-guide/docs/user_guide/model_repository.html

```

Triton architecture: `[https://docs.nvidia.com/deeplearning/triton-inference-](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/architecture.html)`

```
server/user-guide/docs/user_guide/architecture.html

```

Triton schedulers: `[https://docs.nvidia.com/deeplearning/triton-inference-](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/scheduler.html)`

```
server/user-guide/docs/user_guide/scheduler.html

```

# 9
#### Real-World AI Infrastructure and Enterprise Workflows

Enterprise AI infrastructure comes together when individual choices in compute, networking,
storage, orchestration, security, and monitoring are designed as one system. At the largest
scale, that system may be an AI supercomputer. In a regulated environment, it may be a shared
platform that keeps every tenant isolated. In production, it must also support a complete
workflow from data preparation through monitoring and feedback.

This chapter examines those concerns through two case studies and one end-to-end workflow.
It begins with the architecture of an AI supercomputer, then turns to multi-tenant AI
infrastructure for healthcare. The final section connects data, training, deployment, and
monitoring into a unified enterprise AI lifecycle.

This chapter covers the following topics:

Case study: Building an AI supercomputer

Case study: Multi-tenant AI infrastructure for healthcare

End-to-end workflow: Data → train → deploy → monitor

Let's get started!

**Case study: Building an AI supercomputer**

When organizations push the boundaries of AI, they often require computing capabilities far
beyond a single server or a conventional cluster. AI supercomputers combine large numbers of
accelerators with high-bandwidth scale-up and scale-out networks, high-performance
storage, and the operational systems needed to run tightly coupled workloads reliably.

_Chapter 9_ 96

This case study examines documented systems and reference architectures from NVIDIA, Meta,
Oak Ridge National Laboratory, and Cerebras. It focuses on how compute, networking, storage,
cooling, and orchestration are co-designed. Every choice, from accelerator generation to failure
recovery, affects performance, scalability, availability, and cost.

An AI supercomputer is essentially the Formula One car of computing. It is not a typical
general-purpose cluster, but a specialized, tightly integrated system designed for large AI and
high-performance computing workloads. Instead of relying on CPUs alone, it combines GPUs
or other accelerators with high-bandwidth interconnects and parallel or distributed storage.
The same broad architecture can support foundation-model training, scientific simulation,
analytics, and other workloads, but the exact hardware and software stack is specific to the
system.

**Hardware and networking**

The hardware stack revolves around accelerators, but CPUs and infrastructure processors also
play critical roles. The A100, H100, H200, and Grace Hopper examples represent different
NVIDIA platform generations rather than one standard configuration. Selene, for example, is
an A100-based DGX SuperPOD, while the published DGX H100 and H200 systems use eight
Hopper-generation GPUs. Grace Hopper integrates an Arm CPU and Hopper GPU through a
coherent high-bandwidth interconnect. CPU hosts coordinate operating-system, scheduling, I/
O, and application work. DPUs or SmartNICs can offload selected networking, security,
storage, and telemetry functions when the architecture includes them.

Cooling is another critical design concern. Power and cooling requirements vary by system and
generation: NVIDIA's published H100 SuperPOD example exceeds 40 kW per rack, while
Frontier is a facility-scale system operating in the tens-of-megawatts range. Air, direct-liquid,
and hybrid cooling are therefore engineering choices, not one universal standard. The physical
architecture is modular, with compute nodes grouped into racks and larger scalable units
according to the vendor's reference design and the data center's power, cooling, cabling, and
maintenance constraints.

_Figure 9.1_ organizes an AI supercomputer into compute, fabric, storage, facilities, and
operations layers.

97 _Real-World AI Infrastructure and Enterprise Workflows_

_Figure 9.1: Layered AI supercomputer architecture_

Networking is the beating heart of a tightly coupled AI supercomputer. Within a server or rackscale system, accelerators may communicate over NVLink and NVSwitch. The available
bandwidth and topology depend on the GPU and system generation, so an aggregate
bandwidth figure must always be attached to a specific product and direction. Between nodes
and racks, the scale-out fabric may use InfiniBand with RDMA, Ethernet with an RDMA
transport, or another vendor-specific interconnect.

At data center scale, the topology is also system-specific. The NVIDIA DGX H100 SuperPOD
reference architecture uses NDR 400 Gbps InfiniBand and a fat-tree design, while Frontier uses
HPE Slingshot in a dragonfly topology. Newer products can use different link rates and layouts.
Collective operations such as all-reduce are sensitive to congestion, link imbalance, failures,
and topology, so performance claims must be based on the selected fabric and measured
workload rather than a generic 400 to 800 Gbps range.

**Storage, orchestration, and real systems**

Training a large AI model **i** s not only about compute. It is also about moving data and
checkpoints fast enough to keep the accelerators productive. Systems therefore use parallel or
distributed storage such as Lustre, IBM Storage Scale, or another qualified platform, depending
on the architecture. Local NVMe can provide cache or staging space. Published aggregate
throughput ranges from hundreds of gigabytes per second in a four-scalable-unit DGX H100

_Chapter 9_ 98

reference design to terabytes per second in particular leadership-class HPC systems, so
capacity and throughput must be quoted with the system size and workload.

Training data may be sharded, prefetched, cached, or staged to reduce stalls. The appropriate
method depends on dataset size, access pattern, storage design, and framework. ETL and
preprocessing can also use systems such as Spark or NVIDIA RAPIDS, but they remain separate
workloads whose CPU, GPU, memory, and I/O demands must be included in the end-to-end
design.

The orchestration layer sits on top of the hardware. Slurm and Kubernetes represent different
scheduling and workload-management approaches, while PyTorch DistributedDataParallel,
Horovod, and DeepSpeed provide distributed-training mechanisms used by applications.
Kubeflow can supply pipeline and training components, and MLflow can track runs and model
artifacts. These tools do not automatically form one continuous platform, so their
responsibilities, integrations, and sources of state must be defined explicitly.

Failures become more likely as component count and job duration increase, so telemetry and
checkpointing are essential. Checkpoint recovery belongs to the training framework and jobcontrol design. Prometheus can collect metrics and Grafana can visualize them, but neither
system resumes a failed training job by itself. The platform must coordinate detection, job
requeue or restart, checkpoint availability, and validation that recovery produced a correct
continuation.

Several real-world systems illustrate these design choices, but they are snapshots from
different generations. NVIDIA Selene is an A100-based DGX SuperPOD introduced in 2020.
Meta described its RSC with 16,000 A100 GPUs and later clusters with 24,576 H100 GPUs that
built on lessons from RSC. Oak Ridge's Summit combined IBM POWER9 CPUs and NVIDIA
V100 GPUs before it was decommissioned in November 2024; Frontier is an AMD CPU and GPU
exascale system using HPE Slingshot. Cerebras introduced Andromeda in 2022 as a 16-CS-2
wafer-scale cluster. These examples should be compared by architecture and workload, not
placed on one current performance ladder.

What unites these systems is the need to balance compute, networking, storage, cooling,
facilities, and operations. Building an AI supercomputer is not simply a matter of adding
accelerators. Every layer contributes to useful system throughput, while the workload
determines which bottleneck matters most.

**Case study: Multi-tenant AI infrastructure for**
**healthcare**

Healthcare organizations face a unique challenge when adopting AI. They must process vast
amounts of sensitive patient data while meeting strict regulatory requirements. Unlike a

99 _Real-World AI Infrastructure and Enterprise Workflows_

single-tenant research lab, many hospitals, clinics, research institutions, pharmaceutical
companies, and diagnostic providers need platforms where multiple organizations or
departments can securely share the same hardware without compromising data security,
performance, or compliance.

Building a separate GPU cluster for every stakeholder can be costly and inefficient, but sharing
infrastructure changes the threat model. A multi-tenant platform can improve utilization
when the required isolation is achievable and verified. Federated learning is a separate
collaboration pattern in which participating sites keep raw data local and exchange modelrelated information. It does not make the shared cluster or the model updates private
automatically.

**Isolation and security**

The foundation of multi-tenant healthcare AI is an explicit isolation design. Kubernetes
namespaces scope names and many policies, while RBAC controls requests to the Kubernetes
API. They do not form a complete security boundary by themselves. A shared cluster also needs
workload security controls, network isolation enforced by a compatible data plane, storage
authorization, identity and secret management, quotas, admission policy, and auditable
operations. BlueField DPUs and DOCA can participate in selected network and infrastructure
controls when those services are deployed and configured, but tenant isolation is not an
automatic property of the DPU.

Sensitive data should be protected at rest and in transit according to the applicable risk
assessment and regulatory obligations. NVIDIA Multi-Instance GPU, or MIG, partitions
supported GPUs into instances with isolated compute and memory resources, but the
scheduler, device plugin, node security, host software, storage, and network remain part of the
tenant boundary. Audit evidence must connect an authenticated identity to data access, policy
changes, workload execution, and administrative actions across the relevant systems.

Federated learning is one important capability in this architecture. The participating hospital,
clinic, or research center keeps its raw training data local. A federated workflow distributes
model state or tasks, performs local computation, and aggregates returned updates. Those
updates and the trained model can still leak information or be poisoned, so the design needs a
stated threat model and appropriate controls such as secure transport, authenticated
participants, protected aggregation, privacy mechanisms, validation, and audit logging.

_Figure 9.2_ separates tenant controls while retaining a protected federated-learning exchange.

_Chapter 9_ 100

_Figure 9.2: Multi-tenant healthcare AI and federated collaboration_

Representative healthcare applications include radiology image analysis, genomic analysis,
and drug-discovery research. NVIDIA FLARE is the current domain-agnostic, open-source SDK
for federated-learning and federated-computing workflows. Clara Train documentation is
archived; its later releases used MONAI and integrated federated learning through NVIDIA
FLARE. For a current design, use FLARE and the relevant maintained healthcare framework
rather than treating NVIDIA Clara as one current federated-learning product.

Healthcare AI systems can fall within several legal, regulatory, contractual, and assurance
frameworks, but those frameworks have different scopes. The HIPAA Rules apply to covered
entities, business associates, and protected health information within their legal definitions.
GDPR governs processing of personal data within its territorial scope. FDA oversight can apply
when an AI function is part of a regulated medical device or medical product. FedRAMP is
relevant to in-scope cloud service offerings used by United States federal agencies. None of
these frameworks applies merely because a workload runs on a healthcare GPU cluster, and no
single architecture automatically satisfies them.

Access controls should connect to the organization's identity and data-governance systems so
that approved clinicians, researchers, services, and administrators receive only the permissions
required for their roles. In Kubernetes, OPA Gatekeeper or Kyverno can evaluate admission

101 _Real-World AI Infrastructure and Enterprise Workflows_

policies for workload objects. They do not replace RBAC, storage authorization, application
authorization, or clinical identity systems. Compliance evidence must therefore connect policy
decisions and runtime activity across all of those boundaries.

Managing multi-tenant infrastructure is not only about isolation. It is also about allocation
and fairness. Kubernetes has no first-class tenant object or universal multi-tenant operator.
Namespaces, ResourceQuota, priorities, and admission controls provide building blocks. For
queued batch and AI workloads, Kueue can govern resource quotas and configured fair-sharing
policies across queues, including accelerator resources. The selected scheduler or queueing
system must be named because fairness behavior is implementation-specific.

Prometheus and Grafana can support per-tenant views when metrics carry reliable tenant
labels and access to dashboards is controlled. Resource usage, service performance, modelquality signals, and security events may come from different sources and require different
retention and authorization rules. Alerts can notify an incident-response system or invoke
approved automation, but remediation does not occur merely because Prometheus or Grafana
is present.

The value of multi-tenant healthcare AI is clearest in workloads that benefit from shared
capacity or multi-institution collaboration. Representative categories include radiology
analysis, genomics, operational forecasting, drug discovery, and remote diagnostic support.
Each use case still requires its own clinical validation, data-governance basis, performance
evaluation, human oversight, and regulatory determination. Shared infrastructure and
federated learning are enabling patterns, not evidence that a model is safe or effective.

This architecture combines workload isolation, federated collaboration, resource governance,
and operational **e** vidence. Its effectiveness depends on the strength of each configured
boundary and on the deployment's legal and clinical context. The design goal is to share
appropriate resources and learning while preserving required controls over data, identities,
workloads, and model behavior.

**End-to-end workflow: Data** **→** **train** **→** **deploy** **→**
**monitor**

AI projects often stumble not because of poor algorithms, but because the end-to-end
workflow is fragmented. In enterprise environments, success depends on a unified pipeline
that moves from data ingestion and preprocessing to model training, deployment, monitoring,
and feedback. The workflow must remain reliable, reproducible, and scalable across every
stage.

_Chapter 9_ 102

The enterprise AI lifecycle can be distilled into four connected stages:

**Data** : Collect, clean, label, and prepare data for model consumption.

**Train** : Develop models, tune hyperparameters, and optimize performance.

**Deploy** : Package models, serve them in production, and scale them across the required
infrastructure.

**Monitor** : Track drift, latency, throughput, resource cost, and model performance.

A feedback loop connects monitoring back to data, training, and deployment. Production
evidence can trigger data review, retraining, rollback, or another controlled change. The
trigger, approval path, and validation gate must be designed explicitly rather than assumed to
be automatic.

_Figure 9.3_ shows the controlled feedback loop across data, training, deployment, and
monitoring.

_Figure 9.3: Closed-loop enterprise AI lifecycle_

Data quality and data-pipeline behavior directly affect model outcomes. The data stage can
include ETL pipelines that transform clinical notes, sensor readings, logs, or other source data
into governed model inputs. Enterprises may combine object storage or data lakes for
unstructured data with warehouses for structured analytics. Feature engineering and labeling
then adapt the data to the contract of a specific model and use case.

At scale, preprocessing can use RAPIDS, Dask, Spark, or another selected execution engine.
Governance records metadata, lineage, quality checks, access decisions, and dataset versions
so that the inputs to a run can be identified and audited. Reproducibility still depends on
preserving code, configuration, environment, and external dependencies alongside the dataset
reference.

103 _Real-World AI Infrastructure and Enterprise Workflows_

Training is often where compute intensity peaks. Enterprises can run distributed training
across multiple accelerators and nodes under Kubernetes or Slurm. TensorFlow, PyTorch, and
JAX provide framework-specific distributed mechanisms, while tools such as Ray or Optuna
can coordinate hyperparameter searches. The framework, scheduler, topology, checkpoint
strategy, and tuning service must be integrated and measured as one workload path.

Training jobs can save checkpoints so that an interrupted run can resume when the framework
and storage design support compatible recovery. MLflow can record parameters, metrics, and
artifacts. Kubeflow Pipelines can define and execute workflow components. Neither tool makes
a run reproducible by itself; the pipeline must also pin code, data, environments,
dependencies, random-state handling, and model artifacts.

**Deployment and monitoring**

Once a model has been trained and validated, it can move through a controlled promotion
path. ONNX is an interoperable model representation, while TensorRT optimizes and executes
supported models for NVIDIA GPUs; neither is a general packaging system. Containers can
package the serving application and dependencies. Triton Inference Server can expose models
through installed backends, subject to each backend's supported formats, versions, and
execution targets. Deployment may occur at the edge, in a data center, in the cloud, or across a
hybrid design according to latency, data, availability, and operational requirements.

Kubernetes can manage serving replicas, placement, health checks, and rollout state.
Horizontal Pod Autoscaler changes replica count from configured resource, custom, or external
metrics; GPU or Triton metrics require a working collection and metrics-adapter path. Cluster
Autoscaler changes node capacity when pods cannot be scheduled and when nodes can be
safely removed. CI/CD can carry model and configuration changes through tests and
approvals, but an MLOps release also needs model validation, lineage, staged promotion,
observability, and rollback.

Monitoring is critical for operating the system and collecting evidence. Production systems
track infrastructure and service metrics such as availability, latency, throughput, errors,
saturation, and cost. They can also monitor input-distribution changes and modelperformance signals when suitable reference data, labels, or feedback exist. Prometheus and
Grafana cover metrics collection and visualization, while an ELK or equivalent stack can
centralize logs. These tools observe different layers and do not provide model-quality
monitoring automatically.

Alerts can feed incident-response systems such as PagerDuty or Opsgenie. A validated
automation may initiate rollback, quarantine, retraining, or pipeline review, while higher-risk
changes may require human approval. Monitoring therefore does more than report service
state: it supplies evidence for controlled decisions across the lifecycle.

_Chapter 9_ 104

When the stages are deliberately integrated, data pipelines feed training workflows, approved
model artifacts move into deployment, and monitoring closes the feedback loop. NVIDIA AI
Enterprise can supply supported application and infrastructure components across parts of
this lifecycle, but it is not the workflow definition itself. The organization must still select the
components, preserve versions and lineage, connect identities and data, define promotion
gates, and operate the resulting platform.

An end-to-end workflow is not only a technical architecture. It is an operating model for
sustainable AI. Connecting data, training, deployment, and monitoring through explicit
contracts and controlled feedback can improve scalability, reproducibility, resilience,
governance, and trust.

**Summary**

In this chapter, we examined how compute, scale-up and scale-out networking, storage,
cooling, facilities, and orchestration come together in an AI supercomputer. It also
distinguished historical systems from current reference architectures and showed why
performance figures must remain tied to a documented configuration.

We then explored how workload isolation, federated learning, access controls, fair resource
governance, monitoring, and context-specific compliance support shared healthcare AI
infrastructure. Finally, it connected data preparation, distributed training, deployment, and
monitoring into one enterprise AI lifecycle with a controlled feedback loop.

Taken together, these examples reinforce the central principle of this book: AI infrastructure
must be designed and operated as a complete system. Compute, storage, networking,
orchestration, security, serving, edge deployment, and governance create value only when they
are aligned with the workload and validated together. The enterprise lifecycle described here
provides a practical foundation for evaluating and building NVIDIA AI infrastructure as
requirements evolve.

**Further reading**

To learn more about the topics that were covered in this chapter, take a look at the following
resources:

DGX SuperPOD documentation: `[https://docs.nvidia.com/dgx-superpod/](https://docs.nvidia.com/dgx-superpod/index.html)`

```
index.html

```

ORNL Frontier: `[https://www.olcf.ornl.gov/olcf-resources/compute-systems/](https://www.olcf.ornl.gov/olcf-resources/compute-systems/frontier/)`

```
frontier/

```

Cerebras Andromeda: `[https://www.cerebras.ai/blog/sc22-is-a-wrap](https://www.cerebras.ai/blog/sc22-is-a-wrap)`

105 _Real-World AI Infrastructure and Enterprise Workflows_

DGX H100 and H200 systems: `[https://docs.nvidia.com/dgx/dgxh100-user-guide/](https://docs.nvidia.com/dgx/dgxh100-user-guide/introduction-to-dgxh100.html)`

```
introduction-to-dgxh100.html

```

NVIDIA Selene: `[https://blogs.nvidia.com/blog/nvidia-selene-supercomputer/](https://blogs.nvidia.com/blog/nvidia-selene-supercomputer/)`

Meta GenAI infrastructure: `[https://engineering.fb.com/2024/03/12/data-center-](https://engineering.fb.com/2024/03/12/data-center-engineering/building-metas-genai-infrastructure/)`

```
engineering/building-metas-genai-infrastructure/

```

NVIDIA FLARE: `[https://nvflare.readthedocs.io/en/main/flare_overview.html](https://nvflare.readthedocs.io/en/main/flare_overview.html)`

OPA for Kubernetes: `[https://www.openpolicyagent.org/docs/kubernetes](https://www.openpolicyagent.org/docs/kubernetes)`

Kyverno introduction: `[https://kyverno.io/docs/introduction/](https://kyverno.io/docs/introduction/)`

Kubernetes RBAC: `[https://kubernetes.io/docs/reference/access-authn-authz/](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)`

```
rbac/

```

Kubernetes multi-tenancy: `[https://kubernetes.io/docs/concepts/security/](https://kubernetes.io/docs/concepts/security/multi-tenancy/)`

```
multi-tenancy/

```

Kubernetes ResourceQuota: `[https://kubernetes.io/docs/concepts/policy/](https://kubernetes.io/docs/concepts/policy/resource-quotas/)`

```
resource-quotas/

```

Kueue fair sharing: `[https://kueue.sigs.k8s.io/docs/concepts/fair_sharing/](https://kueue.sigs.k8s.io/docs/concepts/fair_sharing/)`

RAPIDS documentation: `[https://docs.rapids.ai/](https://docs.rapids.ai/)`

Dask documentation: `[https://docs.dask.org/en/stable/](https://docs.dask.org/en/stable/)`

Apache Spark documentation: `[https://spark.apache.org/docs/latest/](https://spark.apache.org/docs/latest/)`

# 10
#### Unlock Your Exclusive Benefits

Your copy of this book includes the following exclusive benefits:

Follow the guide below to unlock them. The process takes only a few minutes and needs to be
completed once.

_Chapter 10_ 108

**Unlock this Book's Free Benefits in 3 Easy Steps**

**Step 1**

Keep your purchase invoice ready for _Step 3_ . If you have a physical copy, scan it using your
phone and save it as a PDF, JPG, or PNG.

For more help on finding your invoice, visit `[https://www.packtpub.com/en-us/unlock?](https://www.packtpub.com/en-us/unlock?step=1.)`

```
step=1.

```

**Step 2**

Scan the QR code or go to `[packtpub.com/unlock](https://packtpub.com/unlock)` .

On the page that opens (similar to _Figure 10.1_ on desktop), search for this book by name and
select the correct edition.

109 _Unlock Your Exclusive Benefits_

_Figure 10.1: Packt unlock landing page on desktop_

**Step 3**

After selecting your book, sign in to your Packt account or create one for free. Then upload your
invoice (PDF, PNG, or JPG, up to 10 MB). Follow the on-screen instructions to finish the
process.

**Need Help**

If you get stuck and need help, visit `[https://www.packtpub.com/unlock-benefits/help](https://www.packtpub.com/unlock-benefits/help)` for a
detailed FAQ on how to find your invoices and more. This QR code will take you to the help
page.

```
packtpub.com

```

Subscribe to our online digital library for full access to over 7,000 books and videos, as well as
industry leading tools to help you plan your personal development and advance your career.
For more information, please visit our website.

**Why subscribe?**

Spend less time learning and more time coding with practical eBooks and Videos from
over 4,000 industry professionals

Improve your learning with Skill Plans built especially for you

Get a free eBook or video every month

Fully searchable for easy access to vital information

Copy and paste, print, and bookmark content

At `[www.packtpub.com](https://www.packtpub.com)`, you can also read a collection of free technical articles, sign up for a
range of free newsletters, and receive exclusive discounts and offers on Packt books and
eBooks.

_Other Books You May Enjoy_ 112
### **Other Books You May Enjoy**

If you enjoyed this book, you may be interested in these other books by Packt:

**Kubernetes for Generative AI Solutions**

Ashok Srirama, Sukirti Gupta

ISBN: 9781836209935

Explore GenAI deployment stack, agents, RAG, and model fine-tuning

Implement HPA, VPA, and Karpenter for efficient autoscaling

Optimize GPU usage with fractional allocation, MIG, and MPS setups

Reduce cloud costs and monitor spending with Kubecost tools

Secure GenAI workloads with RBAC, encryption, and service meshes

Monitor system health and performance using Prometheus and Grafana

Ensure high availability and disaster recovery for GenAI systems

Automate GenAI pipelines for continuous integration and delivery

113 _Other Books You May Enjoy_

**Solutions Architect's Handbook**

Saurabh Shrivastava, Neelanjali Srivastav

ISBN: 9781835084236

Explore various roles of a solutions architect in the enterprise

Apply design principles for high-performance, cost-effective solutions

Choose the best strategies to secure your architectures and boost availability

Develop a DevOps and CloudOps mindset for collaboration, operational efficiency, and
streamlined production

Apply machine learning, data engineering, LLMs, and generative AI for improved
security and performance

Modernize legacy systems into cloud-native architectures with proven real-world
strategies

Master key solutions architect soft skills

_Other Books You May Enjoy_ 114

**Packt is searching for authors like you**

If you're interested in becoming an author for Packt, please visit `[authors.packt.com](https://authors.packt.com)` and apply
today. We have worked with thousands of developers and tech professionals, just like you, to
help them share their insight with the global tech community. You can make a general
application, apply for a specific hot topic that we are recruiting an author for, or submit your
own idea.

**Share your thoughts**

Now you've finished _Designing NVIDIA AI Infrastructure_, we'd love to hear your thoughts! Scan
the QR code below to go straight to the Amazon review page for this book and share your
feedback or leave a review on the site that you purchased it from.

```
             https://packt.link/r/1808080130

```

Your review is important to us and the tech community and will help us make sure we're
delivering excellent quality content.

### **Index**

**10**

**1**

**A**

**AI clusters**

role-based access control
(RBAC) for

64

**CUDA Deep Neural**
**Network library**

**Central Processing Units**
**(CPUs)**

versus DPU 5, 6
versus GPU 5, 6

**AI data pipeline design** **32**
ETL stage 32, 33
production example 34

**AI infrastructure**

data movement bottlenecks 30
design 2
designing, for production 3
high-speed networking 28 – 30
loading 31
network 31
optimization 30
regulatory compliance 67 – 70
storage, optimizing 31

**AI supercomputer**

building 95, 96
hardware and networking 96, 97
orchestration 97, 98
real systems 97, 98
storage 97, 98

**AI workloads**

GPUs, role in 4
storage architectures 26
storage types 26 – 28

**AI/ML pipelines**

GPU, accelerating for 7

**B**

**bottlenecks** **30**
diagnosis and tuning 54, 55
tuning, strategies 55, 56

**C**

**CUDA**

reference link 10

federated learning and
distributed inference

**Custom Resource**
**Definitions (CRDs)**

**40**

**charts** **39**

**cloud-native GPU**
**clusters**

**45**

**cluster autoscaling** **40 – 42**

**cluster, topologies** **44**
cloud-native GPU clusters 45
hybrid infrastructure 45, 46
on-premises clusters 44

**cluster-level security** **61**

**compute instances (CIs)** **14**

**cuDNN**

reference link 10

**D**

**DOCA framework** **62 – 64**

**Data Center GPU**
**Manager (DCGM)**

**Data Processing Units**
**(DPUs)**

**16**

**1, 62 – 64**

versus CPU 5, 6
versus GPU 5, 6

**DistributedDataParallel**
**(DDP)**

**data security, in AI infrastructure**

encryption and access
control

**8**

62 – 64

**distributed inference** **78 – 80**
**E**

**edge AI**

78 – 80

_Index_ 116

NVIDIA ecosystem and
business impact

80, 81

**Graphics Processing**
**Units (GPUs)**

accelerating, for AI/ML
pipelines

**1**

7

Orin modules for 76
use cases 80

**edge AI, versus cloud AI**

infrastructure implications 73 – 75

**electronic protected**
**health information**
**(ePHI)**

**68**

**end-to-end workflow** **101 – 103**
deployment and 103, 104
monitoring

**extract, transform, and**
**load (ETL)**

**25**

enabling 38, 39
enabling and requesting 22, 23
memory, managing 17, 18
monitoring and best 23, 24
practices

role, in AI workloads 4
scheduling 17, 18
sharing and isolation 16, 17
techniques

versus CPU 5, 6
versus DPU 5, 6
workload, scheduling with 21
Kubernetes

stage 32 – 34

**F**

**Federal Risk and**
**Authorization**
**Management Program**
**(FedRAMP)**

**68**

**H**

**Health Insurance**
**Portability and**
**Accountability Act**
**(HIPAA)**

**68**

**federated learning** **78 – 80**
**G**

**GPU instances (GIs)** **14**

**GPU workloads**

metrics 51
profiling 49 – 51
telemetry 52
visualization and alerting 52
tools

**GPU, for AI/ML pipelines**

data stages, accelerating 8
training, tuning, and 8, 9
inference, accelerating

**GPU-orchestrated AI workloads**

Kubernetes for 37, 38

**GPU-powered workloads**

cluster-level security 61
securing 59, 60

**GPU-specific controls** **65, 66**

**GPUs, in AI workloads**

acceleration 4, 5
framework support 5
NVIDIA 5

for GPU-orchestrated AI
workloads

used, for scheduling GPU
workload

**Kubernetes RBAC**

**Helm** **39, 40**

**Horizontal Pod**
**Autoscaler (HPA)**

**40**

**high availability** **92, 93**

**high-speed networking** **28 – 30**

**hybrid infrastructure** **45, 46**
**I**

**input/output operations**
**per second (IOPS)**

**K**

**KAI Scheduler**

**26**

reference link 24

**Kubeflow**

integrating 42 – 44

**Kubernetes**

37, 38

21

**General Data Protection**
**Regulation (GDPR)**

**68**

components 65, 66

117 _Index_

**L**

**load balancing** **91 – 93**
**M**

**MLflow**

integrating 42 – 44

**Multi-Instance GPU**
**(MIG)**

**13**

**O**

**Orin**

for edge AI 76

**on-premises clusters** **44**

**operators** **40**
**R**

**25**

66, 67

configuration 13
configuring and monitoring 15, 16
usage 14, 15

**MultiWorkerMirroredStra**
**tegy (MWMS)**

**8**

**remote direct memory**
**access (RDMA)**

**role-based access control (RBAC)**

enterprise integration and
practice

**model ensemble** **89**
architecture 90, 91

**multi-framework serving** **89**
architecture 90, 91

**multi-tenant AI infrastructure, for**
**healthcare**

case study 98
isolation and security 99 – 101

**N**

**NGC Catalog**

accessing 84 – 86
resources, types 84
using, for pretrained 83, 84
models

**NVIDIA** **5**
AI software stack 9, 10
deployment and 10, 11
infrastructure components

ecosystem overview 9

**NVIDIA BlueField-3**

reference link 7

**NVIDIA DOCA framework**

reference link 7

for AI clusters 64

**S**

**Slurm**

integrating 42 – 44

**single instruction,**
**multiple thread (SIMT)**

**streaming**
**multiprocessor (SM)**

**T**

**TensorRT**

**4**

**14**

deployment and impact 53, 54
model optimization 52, 53
optimization techniques 53
reference link 8

**Triton Inference Server** **86**
architecture 87 – 89
reference link 9

**V**

**Vertical Pod Autoscaler**
**(VPA)**

**Volcano**

**40**

**NVIDIA GPU Feature**
**Discovery (GFD)**

**NVIDIA JetPack**

software ecosystem and
scaling

**23**

76 – 78

reference link 24

**virtual GPUs (vGPUs)** **13**
management 20, 21
requirements 20, 21
setup and use cases 19
use cases 20, 21
working with 19, 20

**NVIDIA Jetson** **76**

**virtual desktop**
**infrastructure (VDI)**

**19**
